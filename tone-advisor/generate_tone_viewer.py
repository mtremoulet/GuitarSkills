#!/usr/bin/env python3
"""
generate_tone_viewer.py
Reads all tones/*.md files and produces a self-contained tone-viewer.html.

Usage:
    python3 generate_tone_viewer.py           # generate + open in browser
    python3 generate_tone_viewer.py --build-only  # generate only (for agent use)
"""

import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime


# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}, text
    data = {}
    for line in m.group(1).splitlines():
        # Ignore indented lines (extra metadata like overrides)
        if line.startswith(' ') or line.startswith('\t'):
            continue
        if ':' in line:
            k, _, v = line.partition(':')
            val = v.strip()
            # Strip quotes if present
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            data[k.strip()] = val
    return data, text[m.end():]


def parse_md_table(table_lines):
    """Parse a list of markdown table row strings into (headers, rows)."""
    headers = []
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        # Separator row detection
        if all(re.match(r'^[\s\-:]+$', c) for c in cells if c):
            continue
        if not headers:
            headers = cells
        else:
            rows.append(cells)
    return headers, rows


def parse_plugin_block(content):
    """
    Parse a plugin block's content. Handles multiple tables separated by headings.
    Returns dict with:
      pre_text: text before first table
      blocks:   list of {heading, headers, rows} — one per table found
      note:     trailing text after all tables (newline-joined)
      headers:  first table headers (backward compat)
      rows:     first table rows (backward compat)
    """
    lines = content.strip().split('\n')
    pre_lines = []
    blocks = []
    pending_heading_lines = []
    current_table_lines = []
    state = 'pre'  # pre | table | inter

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|'):
            state = 'table'
            current_table_lines.append(stripped)
        elif state == 'table' and not stripped.startswith('|'):
            headers, rows = parse_md_table(current_table_lines)
            blocks.append({
                'heading': ' '.join(pending_heading_lines).strip(),
                'headers': headers,
                'rows': rows,
            })
            current_table_lines = []
            pending_heading_lines = []
            state = 'inter'
            if stripped and stripped != '---':
                pending_heading_lines.append(stripped)
        elif state == 'pre':
            if stripped and stripped != '---':
                pre_lines.append(stripped)
        elif state == 'inter':
            if stripped and stripped != '---':
                pending_heading_lines.append(stripped)

    if current_table_lines:
        headers, rows = parse_md_table(current_table_lines)
        blocks.append({
            'heading': ' '.join(pending_heading_lines).strip(),
            'headers': headers,
            'rows': rows,
        })
        pending_heading_lines = []

    return {
        'pre_text': '\n'.join(pre_lines),
        'blocks': blocks,
        'note': '\n'.join(pending_heading_lines),
        'headers': blocks[0]['headers'] if blocks else [],
        'rows': blocks[0]['rows'] if blocks else [],
    }


def parse_signal_chain(chain_text):
    """
    Parse the Signal Chain section into a list of items.
    Each item is one of:
      {'kind': 'plugin',  'num', 'name', 'role', 'pre_text', 'blocks', 'note', 'headers', 'rows'}
      {'kind': 'track',   'num', 'name', 'role', 'track_note', 'plugins': [...]}
      {'kind': 'routing', 'num', 'name', 'role', 'note'}
    """
    items = []
    parts = re.split(r'^### (.+)$', chain_text, flags=re.MULTILINE)

    for i in range(1, len(parts), 2):
        header = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ''
        num = str(len(items) + 1)

        hm = re.match(r'^(?:\d+\.\s+)?(.+?)(?:\s+—\s+(.+))?$', header)
        name = hm.group(1).strip() if hm else header
        role = hm.group(2).strip() if hm and hm.group(2) else ''

        has_sub = bool(re.search(r'^#### ', body, re.MULTILINE))
        has_table = bool(re.search(r'^\|', body, re.MULTILINE))

        if has_sub:
            sub_parts = re.split(r'^#### (.+)$', body, flags=re.MULTILINE)
            track_note = sub_parts[0].strip().strip('---').strip() if sub_parts else ''
            child_plugins = []
            for j in range(1, len(sub_parts), 2):
                sp_hdr = sub_parts[j].strip()
                sp_body = sub_parts[j + 1].strip() if j + 1 < len(sub_parts) else ''
                sp_hm = re.match(r'^(?:(\d+)\.\s+)?(.+?)(?:\s+—\s+(.+))?$', sp_hdr)
                if sp_hm:
                    sp_num = sp_hm.group(1) or str(len(child_plugins) + 1)
                    sp_name = sp_hm.group(2).strip()
                    sp_role = sp_hm.group(3).strip() if sp_hm.group(3) else ''
                else:
                    sp_num = str(len(child_plugins) + 1)
                    sp_name = sp_hdr
                    sp_role = ''
                sp_block = parse_plugin_block(sp_body)
                child_plugins.append({'num': sp_num, 'name': sp_name, 'role': sp_role, **sp_block})
            items.append({'kind': 'track', 'num': num, 'name': name, 'role': role,
                          'track_note': track_note, 'plugins': child_plugins})

        elif has_table:
            block = parse_plugin_block(body)
            items.append({'kind': 'plugin', 'num': num, 'name': name, 'role': role, **block})

        else:
            note = body.replace('---', '').strip()
            items.append({'kind': 'routing', 'num': num, 'name': name, 'role': role, 'note': note})

    return items


def infer_genre(tags):
    tag_set = set(tags)
    if 'ambient' in tag_set or 'sound-bath' in tag_set:
        return 'ambient'
    if any(t in tag_set for t in ('classic-rock', 'crunch', 'jcm800', 'plexi', 'lead', 'zeppelin')):
        return 'rock'
    if any(t in tag_set for t in ('country', 'folk-rock', 'jangle', 'british-invasion', 'surf', 'chime')):
        return 'country'
    if 'neo-soul' in tag_set or 'jazz-blues' in tag_set:
        return 'jazz'
    if 'jazz' in tag_set and 'blues' not in tag_set:
        return 'jazz'
    if 'blues' in tag_set and 'jazz' not in tag_set:
        return 'blues'
    if 'jazz' in tag_set and 'blues' in tag_set:
        return 'jazz' if 'boutique' in tag_set else 'blues'
    if 'clean' in tag_set or 'pedal-platform' in tag_set:
        return 'clean'
    return 'jazz'


def infer_guitar_type(guitar_str):
    g = guitar_str.lower()
    if 'telecaster' in g or ' tele' in g:
        return 'telecaster'
    if 'stratocaster' in g or 'strat' in g:
        return 'strat'
    if 'sheraton' in g or 'semi-hollow' in g or '335' in g:
        return 'semi-hollow'
    if 'les paul' in g:
        return 'les-paul'
    if 'framus' in g:
        return 'framus'
    return 'other'


def parse_tone_file(filepath):
    text = Path(filepath).read_text()
    fm, body = parse_frontmatter(text)

    # H1 title
    h1 = re.search(r'^# (.+)$', body, re.MULTILINE)
    title = h1.group(1).strip() if h1 else fm.get('id', '')

    # Split on ## section headers
    parts = re.split(r'^## (.+)$', body, flags=re.MULTILINE)
    sections = {}
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ''
        sections[name] = content.strip()

    # Signal Chain → items (track groups, simple plugins, routing notes)
    items = []
    if 'Signal Chain' in sections:
        items = parse_signal_chain(sections['Signal Chain'])
    plugins = [item for item in items if item['kind'] == 'plugin']

    # Starting Point Guide — bullet items
    guide_items = []
    if 'Starting Point Guide' in sections:
        for line in sections['Starting Point Guide'].split('\n'):
            line = line.strip()
            if line.startswith('- '):
                guide_items.append(line[2:])

    # Feedback History
    feedback = []
    if 'Feedback History' in sections:
        fh = sections['Feedback History']
        fh_parts = re.split(r'^### (.+)$', fh, flags=re.MULTILINE)
        for i in range(1, len(fh_parts), 2):
            fh_hdr = fh_parts[i].strip()
            fh_body = fh_parts[i + 1].strip() if i + 1 < len(fh_parts) else ''
            dm = re.match(r'^(\d{4}-\d{2}-\d{2})\s+—\s+(.+)$', fh_hdr)
            feedback.append({
                'date': dm.group(1) if dm else fh_hdr,
                'status': dm.group(2).strip() if dm else '',
                'content': fh_body,
            })

    tags = [t.strip() for t in fm.get('tags', '').split(',') if t.strip()]
    guitar = fm.get('guitar', '')
    slug = fm.get('id', Path(filepath).stem)

    return {
        'id': slug,
        'source_path': str(Path(filepath).relative_to(Path(__file__).parent.parent)),
        'created': fm.get('created', ''),
        'updated': fm.get('updated', ''),
        'guitar': guitar,
        'target': fm.get('target', ''),
        'tags': tags,
        'tone_king_channel': fm.get('tone-king-channel', ''),
        'status': fm.get('status', 'initial'),
        'amp': fm.get('amp', '').strip(),
        'genre': fm.get('genre', infer_genre(tags)).strip(),
        'guitar_type': infer_guitar_type(guitar),
        'pickup_type': fm.get('pickup_type', ''),
        'title': title,
        'target_sound': sections.get('Target Sound', ''),
        'items': items,
        'plugins': plugins,
        'guide_items': guide_items,
        'feedback': feedback,
    }


# ── HTML helpers ──────────────────────────────────────────────────────────────

def h(s):
    """HTML-escape a string."""
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def inline_md(text):
    """Convert **bold**, *italic*, and `code` markers to HTML. Input should be already HTML-escaped."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def render_markdown_content(text):
    if not text:
        return ''
    
    # Split text into lines
    lines = text.split('\n')
    
    html_parts = []
    current_block = []
    block_type = None  # None, 'table', 'ul', 'ol', 'p'
    
    def close_block():
        nonlocal block_type, current_block
        if not current_block:
            return
        
        if block_type == 'table':
            headers, rows = parse_md_table(current_block)
            html_parts.append(render_table(headers, rows))
        elif block_type == 'ul':
            html_parts.append('<ul class="markdown-ul">')
            for item in current_block:
                html_parts.append(f'<li>{inline_md(h(item))}</li>')
            html_parts.append('</ul>')
        elif block_type == 'ol':
            html_parts.append('<ol class="markdown-ol">')
            for item in current_block:
                html_parts.append(f'<li>{inline_md(h(item))}</li>')
            html_parts.append('</ol>')
        elif block_type == 'p':
            p_text = ' '.join(current_block)
            html_parts.append(f'<p class="markdown-p">{inline_md(h(p_text))}</p>')
        
        current_block = []
        block_type = None

    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            close_block()
            continue
            
        # Detect table
        if stripped.startswith('|'):
            if block_type != 'table':
                close_block()
                block_type = 'table'
            current_block.append(stripped)
            
        # Detect bullet list
        elif re.match(r'^[\*\-\+]\s+', stripped):
            if block_type != 'ul':
                close_block()
                block_type = 'ul'
            item_text = re.sub(r'^[\*\-\+]\s+', '', stripped)
            current_block.append(item_text)
            
        # Detect numbered list
        elif re.match(r'^\d+\.\s+', stripped):
            if block_type != 'ol':
                close_block()
                block_type = 'ol'
            item_text = re.sub(r'^\d+\.\s+', '', stripped)
            current_block.append(item_text)
            
        # Paragraph
        else:
            if block_type in ('table', 'ul', 'ol'):
                close_block()
            if block_type is None:
                block_type = 'p'
            current_block.append(stripped)
            
    close_block()
    return '\n'.join(html_parts)


def chip_name(plugin_name):
    """Shorten a plugin name for signal chain chips."""
    name = plugin_name
    for prefix in ('UADx ', 'UA ', 'Logic '):
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    if len(name) > 28:
        name = name[:26] + '\u2026'
    return name


# ── HTML rendering ────────────────────────────────────────────────────────────

def render_block_tables(blocks):
    """Render all table blocks within a plugin card (handles multi-table plugins)."""
    html = ''
    for block in blocks:
        if block.get('heading'):
            html += f'<div class="block-heading">{inline_md(h(block["heading"]))}</div>'
        html += render_table(block['headers'], block['rows'])
    return html


def render_plugin_card(p, tone_id, is_nested=False):
    """Render a plugin settings card. Used for both top-level and nested plugins."""
    pid = f'plugin-{tone_id}-{p["num"]}'
    role_html = f'<span class="plugin-role">{h(p["role"])}</span>' if p.get('role') else ''

    pre_html = ''
    if p.get('pre_text'):
        pre_html = f'<div class="plugin-note">{render_markdown_content(p["pre_text"])}</div>'

    tables_html = render_block_tables(p.get('blocks', []))
    if not tables_html:
        tables_html = render_table(p.get('headers', []), p.get('rows', []))

    note_text = p.get('note', '')
    if note_text.startswith('*') and note_text.endswith('*') and len(note_text) > 1:
        note_text = note_text[1:-1]
    note_html = ''
    if note_text:
        note_html = f'<div class="interaction-note">{render_markdown_content(note_text)}</div>'

    extra_cls = ' nested-plugin' if is_nested else ''
    return f'''
<div class="plugin-section{extra_cls}" id="{h(pid)}">
  <div class="plugin-header">
    <span class="plugin-num">{h(p["num"])}</span>
    <div class="plugin-title-block">
      <span class="plugin-name">{h(p["name"])}</span>
      {role_html}
    </div>
  </div>
  {pre_html}
  {tables_html}
  {note_html}
</div>'''


def render_track_group(track, tone_id):
    """Render a Logic track group (Aux/Guitar strip) with nested plugin cards."""
    tgid = f'track-{tone_id}-{track["num"]}'
    role_html = f'<span class="plugin-role">{h(track["role"])}</span>' if track.get('role') else ''

    track_note_html = ''
    if track.get('track_note'):
        track_note_html = f'<div class="track-note">{render_markdown_content(track["track_note"])}</div>'

    nested_html = ''.join(render_plugin_card(cp, tone_id, is_nested=True) for cp in track['plugins'])

    return f'''
<div class="track-group" id="{h(tgid)}">
  <div class="track-header">
    <span class="track-label">TRACK</span>
    <div class="plugin-title-block">
      <span class="track-name">{h(track["name"])}</span>
      {role_html}
    </div>
  </div>
  {track_note_html}
  <div class="track-body">
{nested_html}
  </div>
</div>'''


def render_routing_strip(item):
    """Render a routing-only section (send, bus assignment) as a strip."""
    note = item.get('note', '').replace('\n', ' ').strip()
    note_span = f' <span class="routing-detail">{h(note)}</span>' if note else ''
    return f'<div class="routing-note"><span class="routing-label">Route</span>{h(item["name"])}{note_span}</div>'


def render_table(headers, rows):
    if not headers:
        return ''

    # Find column roles
    setting_col = next((i for i, hd in enumerate(headers) if hd.lower() == 'setting'), None)
    purpose_col = next((i for i, hd in enumerate(headers) if hd.lower() == 'purpose'), None)

    out = ['<div class="table-wrap"><table class="settings-table"><thead><tr>']
    for i, hdr in enumerate(headers):
        cls = ''
        if i == setting_col:
            cls = ' class="col-setting"'
        elif i == purpose_col:
            cls = ' class="col-purpose"'
        out.append(f'<th{cls}>{h(hdr)}</th>')
    out.append('</tr></thead><tbody>')

    for ri, row in enumerate(rows):
        row_cls = 'row-alt' if ri % 2 else 'row-norm'
        out.append(f'<tr class="{row_cls}">')
        for ci in range(len(headers)):
            cell_raw = row[ci] if ci < len(row) else ''
            cell_html = inline_md(h(cell_raw))
            if ci == setting_col:
                out.append(f'<td class="col-setting">{cell_html}</td>')
            elif ci == purpose_col:
                out.append(f'<td class="col-purpose">{cell_html}</td>')
            else:
                out.append(f'<td>{cell_html}</td>')
        out.append('</tr>')

    out.append('</tbody></table></div>')
    return ''.join(out)


def render_guide_item(text):
    m = re.match(r'\*\*(.+?)\*\*[:\s]+(.*)', text, re.DOTALL)
    if m:
        label = h(m.group(1))
        content = inline_md(h(m.group(2)))
        return f'<div class="guide-card"><span class="guide-label">{label}</span><span class="guide-content">{content}</span></div>'
    return f'<div class="guide-card"><span class="guide-content">{inline_md(h(text))}</span></div>'


STATUS_CLS = {
    'initial': 'status-initial',
    'tested': 'status-tested',
    'refined': 'status-refined',
    'verified': 'status-tested',
    'archived': 'status-archived',
}


def render_tone(tone):
    tid = tone['id']
    status = tone['status']
    scls = STATUS_CLS.get(status, 'status-initial')
    source_url = f'../{tone["source_path"]}'

    tags_html = ''.join(f'<span class="tag">{h(t)}</span>' for t in tone['tags'])

    # Signal chain flow chips — one per ### section
    chain_html = ''
    if tone.get('items'):
        chips = []
        for item in tone['items']:
            cname = chip_name(item['name'])
            if item['kind'] == 'routing':
                chips.append(f'<span class="chain-routing-label">{h(cname)}</span>')
            elif item['kind'] == 'track':
                eid = f'track-{h(tid)}-{h(item["num"])}'
                chips.append(
                    f'<button class="chain-chip chain-chip-track" onclick="scrollToItem(\'{eid}\')">{h(cname)}</button>'
                )
            else:
                eid = f'plugin-{h(tid)}-{h(item["num"])}'
                chips.append(
                    f'<button class="chain-chip" onclick="scrollToItem(\'{eid}\')">{h(cname)}</button>'
                )
        chain_html = (
            '<div class="chain-flow">'
            + '<span class="chain-arrow">&#8594;</span>'.join(chips)
            + '</div>'
        )

    # Items rendering — track groups, plugin cards, routing strips
    items_html_parts = []
    for item in tone.get('items', []):
        if item['kind'] == 'track':
            items_html_parts.append(render_track_group(item, tid))
        elif item['kind'] == 'routing':
            items_html_parts.append(render_routing_strip(item))
        else:
            items_html_parts.append(render_plugin_card(item, tid))

    plugins_html = ''.join(items_html_parts)

    # Starting Point Guide
    guide_html = ''
    if tone['guide_items']:
        items = ''.join(render_guide_item(item) for item in tone['guide_items'])
        guide_html = f'''
<section class="tone-section">
  <h2 class="section-header">Starting Point Guide</h2>
  <div class="guide-grid">{items}</div>
</section>'''

    # Feedback History
    feedback_html = ''
    if tone['feedback']:
        entries = []
        for fb in tone['feedback']:
            fb_scls = STATUS_CLS.get(fb['status'], 'status-initial')
            content_p = f'<div class="feedback-content">{render_markdown_content(fb["content"])}</div>' if fb['content'] else ''
            entries.append(f'''
<div class="feedback-entry">
  <div class="feedback-header">
    <span class="feedback-date">{h(fb["date"])}</span>
    <span class="badge {fb_scls}">{h(fb["status"])}</span>
  </div>
  {content_p}
</div>''')
        feedback_html = f'''
<section class="tone-section">
  <h2 class="section-header">Feedback History</h2>
  {"".join(entries)}
</section>'''

    target_sound_html = ''
    if tone['target_sound']:
        target_sound_html = f'''
<section class="tone-section">
  <h2 class="section-header">Target Sound</h2>
  <div class="target-sound">{render_markdown_content(tone["target_sound"])}</div>
</section>'''

    return f'''
<div class="tone-detail" id="tone-{h(tid)}" style="display:none">
  <div class="tone-header">
    <div class="tone-header-top">
      <h1 class="tone-title">{h(tone["title"])}</h1>
      <a href="{h(source_url)}" class="view-source-btn" target="_blank">View Source</a>
    </div>
    <div class="tone-meta">
      <span class="meta-guitar">{h(tone["guitar"])}</span>
      <span class="badge {scls}">{h(status)}</span>
      <span class="meta-channel">TK: {h(tone["tone_king_channel"])}</span>
    </div>
    <div class="tone-tags">{tags_html}</div>
    <p class="tone-target-desc">{h(tone["target"])}</p>
  </div>
  {target_sound_html}
  <section class="tone-section">
    <h2 class="section-header">Signal Chain</h2>
    {chain_html}
    {plugins_html}
  </section>
  {guide_html}
  {feedback_html}
</div>'''


def render_sidebar_item(tone, is_first):
    tid = tone['id']
    status = tone['status']
    scls = STATUS_CLS.get(status, 'status-initial')
    active = ' active' if is_first else ''
    guitar_short = tone['guitar'].split('(')[0].strip()
    tags_preview = ', '.join(tone['tags'][:3])
    return f'''<div class="sidebar-item{active}" onclick="showTone('{h(tid)}')" data-id="{h(tid)}" data-status="{h(status)}" data-genre="{h(tone['genre'])}" data-guitar="{h(tone['guitar_type'])}" data-pickup="{h(tone['pickup_type'])}" data-amp="{h(tone['amp'])}" tabindex="0">
  <div class="sidebar-title">{h(tone["title"])}</div>
  <div class="sidebar-sub">{h(guitar_short)}</div>
  <div class="sidebar-tags">{h(tags_preview)}</div>
  <span class="badge {scls} sidebar-badge">{h(status)}</span>
</div>'''


# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:              #191c22;
  --surface:         #22262f;
  --surface-alt:     #2c313d;
  --border:          #363b48;
  --accent:          #5ba4c8;
  --accent-dim:      #2e5f7a;
  --accent-glow:     rgba(91,164,200,0.11);
  --text:            #e8edf4;
  --secondary:       #8c96a4;
  --muted:           #545c68;
  --accent-fg:       #0e1014;
  --badge-tested-bg: rgba(91,164,200,0.14);
  --sidebar-w:       290px;
}

[data-theme="light"] {
  --bg:              #f4f7f5;
  --surface:         #ffffff;
  --surface-alt:     #eef2ef;
  --border:          #c8d5cb;
  --accent:          #059669;
  --accent-dim:      #047857;
  --accent-glow:     rgba(5,150,105,0.10);
  --text:            #111827;
  --secondary:       #374151;
  --muted:           #9ca3af;
  --accent-fg:       #ffffff;
  --badge-tested-bg: rgba(5,150,105,0.12);
}

html, body { height: 100%; overflow: hidden; }

body {
  font-family: -apple-system, 'Helvetica Neue', sans-serif;
  background: var(--bg);
  color: var(--text);
  font-size: 14px;
  line-height: 1.6;
}

/* ── Layout ── */
.app { display: flex; height: 100vh; overflow: hidden; }

.sidebar {
  width: var(--sidebar-w);
  min-width: var(--sidebar-w);
  background: var(--surface);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.main-panel {
  flex: 1;
  overflow-y: auto;
  padding: 36px 48px 64px;
  max-width: 960px;
}

/* ── Sidebar header ── */
.sidebar-header {
  padding: 22px 20px 16px;
  border-bottom: 1px solid var(--border);
  text-align: center;
  flex-shrink: 0;
}

.vault-wordmark {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 4px;
}
.vault-wordmark-logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.vault-hex {
  color: var(--accent);
  font-size: 20px;
  line-height: 1;
}

.vault-name {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--text);
  text-transform: uppercase;
}

.vault-count {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: 0.05em;
}

/* ── Sidebar list ── */
.sidebar-list {
  flex: 1;
  overflow-y: auto;
  padding: 10px 8px;
}

.sidebar-item {
  padding: 11px 14px;
  border-radius: 8px;
  cursor: pointer;
  margin-bottom: 3px;
  position: relative;
  transition: background 0.12s, border-color 0.12s;
  border: 1px solid transparent;
  outline: none;
}

.sidebar-item:hover { background: var(--surface-alt); }

.sidebar-item:focus-visible {
  border-color: var(--accent-dim);
  background: var(--surface-alt);
}

.sidebar-item.active {
  background: var(--accent-glow);
  border-color: var(--accent-dim);
}

.sidebar-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 2px;
  line-height: 1.3;
  padding-right: 50px;
}

.sidebar-item.active .sidebar-title { color: var(--accent); }

.sidebar-sub {
  font-size: 11px;
  color: var(--secondary);
  margin-bottom: 2px;
}

.sidebar-tags {
  font-size: 10px;
  color: var(--muted);
}

.sidebar-badge {
  position: absolute;
  top: 11px;
  right: 10px;
}

/* ── Filters ── */
.filters-toggle-bar {
  padding: 10px 16px;
  background: rgba(0,0,0,0.06);
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  user-select: none;
  transition: background 0.12s;
}

.filters-toggle-bar:hover {
  background: var(--surface-alt);
}

.filters-toggle-bar:hover .filter-title-label {
  color: var(--accent);
}

.filters-toggle-bar:hover .filters-toggle-icon {
  color: var(--text);
}

.filter-title-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--secondary);
}

.filters-toggle-icon {
  font-size: 9px;
  color: var(--muted);
  transition: transform 0.2s ease;
}

.filters-toggle-icon.collapsed {
  transform: rotate(-90deg);
}

.filters-container {
  display: flex;
  flex-direction: column;
  gap: 7px;
  padding: 8px 12px 10px;
  border-bottom: 1px solid var(--border);
  overflow: hidden;
  transition: max-height 0.25s ease-out, padding 0.25s ease-out, border-bottom-width 0.25s ease-out;
  max-height: 500px;
}

.filters-container.collapsed {
  max-height: 0;
  padding-top: 0;
  padding-bottom: 0;
  border-bottom-width: 0;
}

.filter-section {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.filter-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 3px;
}

.filter-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--muted);
  border-radius: 20px;
  padding: 2px 8px;
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: background 0.12s, color 0.12s, border-color 0.12s;
  font-family: inherit;
}

.filter-btn:hover {
  background: var(--surface-alt);
  color: var(--text);
  border-color: var(--accent-dim);
}

.filter-btn.active {
  background: var(--accent-glow);
  color: var(--accent);
  border-color: var(--accent-dim);
}

.amp-select {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--secondary);
  border-radius: 4px;
  padding: 3px 8px;
  font-size: 10px;
  font-family: inherit;
  cursor: pointer;
  width: 100%;
  outline: none;
}

.amp-select:hover { border-color: var(--accent-dim); }

/* ── Sidebar footer ── */
.sidebar-footer {
  padding: 10px 16px;
  border-top: 1px solid var(--border);
  font-size: 10px;
  color: var(--muted);
  text-align: center;
  flex-shrink: 0;
  letter-spacing: 0.03em;
}

/* ── Badges ── */
.badge {
  display: inline-block;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 4px;
  white-space: nowrap;
}

.status-initial  { background: rgba(104,104,110,0.2); color: #8e8e98; border: 1px solid #4a4a52; }
.status-tested   { background: var(--badge-tested-bg); color: var(--accent); border: 1px solid var(--accent-dim); }
.status-refined  { background: rgba(52,199,89,0.15);  color: #34c759; border: 1px solid #1e5e30; }
.status-archived { background: rgba(142,142,147,0.18); color: #98989f; border: 1px solid #48484a; }
[data-theme="light"] .status-archived { background: rgba(142,142,147,0.14); color: #636366; border: 1px solid #c7c7cc; }

.filter-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.archived-toggle-label {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 9px;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
  transition: color 0.12s;
}

.archived-toggle-label:hover {
  color: var(--secondary);
}

.archived-toggle-label input[type="checkbox"] {
  accent-color: var(--accent);
  cursor: pointer;
  width: 11px;
  height: 11px;
  margin: 0;
}

/* ── Tone header ── */
.tone-header {
  margin-bottom: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--border);
}

.tone-header-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 4px;
}

.view-source-btn {
  font-size: 10px;
  font-weight: 600;
  color: var(--muted);
  text-decoration: none;
  border: 1px solid var(--border);
  padding: 4px 10px;
  border-radius: 4px;
  transition: all 0.12s;
  white-space: nowrap;
  margin-top: 6px;
}

.view-source-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--accent-glow);
}

.tone-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 12px;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.tone-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
  flex-wrap: wrap;
}

.meta-guitar {
  font-size: 13px;
  color: var(--secondary);
}

.meta-channel {
  font-size: 10px;
  color: var(--muted);
  font-family: 'SF Mono', 'Menlo', monospace;
  letter-spacing: 0.03em;
}

.tone-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 10px;
}

.tag {
  background: var(--surface-alt);
  color: var(--secondary);
  border: 1px solid var(--border);
  font-size: 10px;
  padding: 2px 9px;
  border-radius: 100px;
}

.tone-target-desc {
  font-size: 13px;
  color: var(--secondary);
  font-style: italic;
  line-height: 1.55;
}

/* ── Section structure ── */
.tone-section { margin-bottom: 36px; }

.section-header {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 14px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
}

.target-sound {
  font-size: 14px;
  line-height: 1.7;
  color: var(--text);
}

/* ── Signal chain flow ── */
.chain-flow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0;
  margin-bottom: 20px;
  padding: 14px 16px;
  background: var(--surface);
  border-radius: 10px;
  border: 1px solid var(--border);
  row-gap: 8px;
}

.chain-chip {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--secondary);
  font-family: inherit;
  font-size: 11px;
  font-weight: 500;
  padding: 5px 11px;
  border-radius: 5px;
  cursor: pointer;
  transition: color 0.12s, border-color 0.12s, background 0.12s;
  white-space: nowrap;
}

.chain-chip:first-child {
  border-color: var(--accent-dim);
  color: var(--accent);
  background: var(--accent-glow);
}

.chain-chip:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--accent-glow);
}

.chain-arrow {
  color: var(--muted);
  font-size: 11px;
  padding: 0 4px;
  user-select: none;
  flex-shrink: 0;
}

/* ── Plugin sections ── */
.plugin-section {
  margin-bottom: 16px;
  background: var(--surface);
  border-radius: 10px;
  border: 1px solid var(--border);
  overflow: hidden;
}

.plugin-header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 18px;
  background: rgba(0,0,0,0.18);
  border-bottom: 1px solid var(--border);
}

.plugin-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  background: var(--accent);
  color: var(--accent-fg);
  font-size: 10px;
  font-weight: 800;
  border-radius: 50%;
  flex-shrink: 0;
  margin-top: 2px;
  letter-spacing: 0;
}

.plugin-title-block {
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.plugin-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  line-height: 1.3;
}

.plugin-role {
  font-size: 11px;
  color: var(--muted);
}

.plugin-note {
  padding: 10px 18px;
  font-size: 13px;
  color: var(--secondary);
  line-height: 1.55;
  border-bottom: 1px solid var(--border);
  background: var(--accent-glow);
}

.interaction-note {
  padding: 10px 18px 12px;
  font-size: 12px;
  color: var(--secondary);
  line-height: 1.55;
  border-top: 1px solid var(--border);
  background: var(--accent-glow);
  font-style: italic;
}

/* ── Settings tables ── */
.table-wrap { overflow-x: auto; }

.settings-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}

.settings-table thead tr {
  background: rgba(0,0,0,0.12);
}

.settings-table th {
  padding: 7px 18px;
  text-align: left;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  border-bottom: 1px solid var(--border);
}

.settings-table td {
  padding: 9px 18px;
  vertical-align: top;
  border-bottom: 1px solid var(--border);
  line-height: 1.45;
}

.settings-table tr:last-child td { border-bottom: none; }

.row-alt { background: rgba(0,0,0,0.07); }

.col-setting {
  color: var(--accent) !important;
  font-weight: 600;
  white-space: nowrap;
}

.col-setting strong {
  color: var(--accent);
  font-weight: 700;
  background: var(--accent-glow);
  padding: 1px 4px;
  border-radius: 3px;
}

.col-purpose {
  color: var(--secondary) !important;
  font-size: 12px !important;
  line-height: 1.45 !important;
}

/* ── Starting Point Guide ── */
.guide-grid { display: grid; gap: 8px; }

.guide-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: 0 8px 8px 0;
  padding: 11px 16px;
  font-size: 13px;
  line-height: 1.55;
}

.guide-label {
  color: var(--accent);
  font-weight: 600;
}

.guide-label::after { content: ': '; }

.guide-content { color: var(--text); }

/* ── Feedback History ── */
.feedback-entry {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 13px 18px;
  margin-bottom: 8px;
  font-size: 13px;
  line-height: 1.6;
}

.feedback-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.feedback-date {
  font-family: 'SF Mono', 'Menlo', monospace;
  font-size: 11px;
  color: var(--accent);
  font-weight: 600;
  letter-spacing: 0.02em;
}

.feedback-entry p { color: var(--secondary); }

/* ── View tabs (Signal Chain / Setup Checklist) ── */
.view-tabs {
  display: flex;
  gap: 0;
  border-bottom: 1px solid var(--border);
  margin-bottom: 28px;
}

.view-tab {
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  padding: 9px 20px;
  margin-bottom: -1px;
  color: var(--muted);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: color 0.15s, border-color 0.15s;
  letter-spacing: 0.01em;
}

.view-tab:hover { color: var(--text); }

.view-tab.active {
  color: var(--accent);
  border-bottom-color: var(--accent);
}

.checklist-intro {
  font-size: 12px;
  color: var(--muted);
  font-style: italic;
  margin-bottom: 16px;
}

/* ── Theme toggle button ── */
.theme-toggle {
  background: none;
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 3px 10px;
  font-size: 10px;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  font-family: inherit;
  letter-spacing: 0.04em;
  transition: color 0.15s, border-color 0.15s;
  flex-shrink: 0;
}
.theme-toggle:hover { color: var(--text); border-color: var(--accent-dim); }

/* ── Scrollbars ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--surface-alt); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }
[data-theme="light"] ::-webkit-scrollbar-thumb { background: #c8d5cb; }
[data-theme="light"] ::-webkit-scrollbar-thumb:hover { background: #9ca3af; }

/* ── Empty state ── */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 60vh;
  color: var(--muted);
  text-align: center;
}

.empty-icon { font-size: 40px; margin-bottom: 14px; opacity: 0.3; }

/* ── Inline text ── */
strong { color: var(--text); font-weight: 600; }
em { color: var(--secondary); }

/* ── Responsive ── */
@media (max-width: 700px) {
  .sidebar { width: 220px; min-width: 220px; }
  .main-panel { padding: 24px 20px 48px; }
  .tone-title { font-size: 22px; }
  .col-purpose { display: none; }
}

/* ── Track groups ── */
.track-group {
  margin-bottom: 16px;
  background: var(--surface);
  border-radius: 10px;
  border: 1px solid var(--accent-dim);
  overflow: hidden;
}

.track-header {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 10px 18px;
  background: rgba(200,146,42,0.06);
  border-bottom: 1px solid var(--border);
}

.track-label {
  display: inline-flex;
  align-items: center;
  background: var(--accent);
  color: var(--accent-fg);
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 0.12em;
  padding: 2px 6px;
  border-radius: 3px;
  flex-shrink: 0;
  margin-top: 3px;
  text-transform: uppercase;
  font-family: 'SF Mono', 'Menlo', monospace;
}

.track-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--accent);
  line-height: 1.3;
}

.track-note {
  padding: 8px 18px;
  font-size: 12px;
  color: var(--secondary);
  border-bottom: 1px solid var(--border);
  font-style: italic;
}

.track-body {
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nested-plugin {
  margin-bottom: 0 !important;
}

/* ── Routing notes ── */
.routing-note {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 16px;
  margin-bottom: 8px;
  font-size: 12px;
  color: var(--secondary);
  font-family: 'SF Mono', 'Menlo', monospace;
  background: var(--surface);
  border-radius: 8px;
  border: 1px dashed var(--border);
}

.routing-label {
  display: inline-block;
  font-size: 8px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: rgba(58,58,60,0.6);
  color: var(--muted);
  padding: 1px 5px;
  border-radius: 3px;
  flex-shrink: 0;
  font-family: inherit;
}

.routing-detail {
  color: var(--muted);
  font-size: 11px;
}

/* ── Chain routing label (routing items in chain-flow bar) ── */
.chain-routing-label {
  font-size: 10px;
  color: var(--muted);
  padding: 4px 6px;
  font-style: italic;
  white-space: nowrap;
}

/* ── Track chips in chain-flow bar ── */
.chain-chip-track {
  border-color: var(--accent-dim) !important;
  color: var(--accent) !important;
  background: var(--accent-glow) !important;
}

.chain-chip-track:hover {
  border-color: var(--accent) !important;
}

/* ── Block headings within plugin cards (multi-table plugins) ── */
.block-heading {
  padding: 7px 18px 3px;
  font-size: 11px;
  font-weight: 600;
  color: var(--secondary);
  background: rgba(0,0,0,0.12);
  border-top: 1px solid var(--border);
}

/* ── Code blocks ── */
code {
  font-family: 'SF Mono', 'Menlo', monospace;
  background: rgba(255,255,255,0.08);
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 0.9em;
}
[data-theme="light"] code {
  background: rgba(0,0,0,0.05);
}

/* ── Markdown styling within parsed notes/text ── */
.plugin-note p, .interaction-note p, .track-note p, .target-sound p, .feedback-content p {
  margin-bottom: 8px;
}
.plugin-note p:last-child, .interaction-note p:last-child, .track-note p:last-child, .target-sound p:last-child, .feedback-content p:last-child {
  margin-bottom: 0;
}
.plugin-note ul, .plugin-note ol, .interaction-note ul, .interaction-note ol, .track-note ul, .track-note ol, .target-sound ul, .target-sound ol, .feedback-content ul, .feedback-content ol {
  margin-left: 20px;
  margin-top: 4px;
  margin-bottom: 4px;
}
.plugin-note li, .interaction-note li, .track-note li, .target-sound li, .feedback-content li {
  margin-bottom: 2px;
}
.track-note table {
  font-style: normal;
  margin-top: 8px;
  margin-bottom: 8px;
}
"""

# ── JavaScript ────────────────────────────────────────────────────────────────

JS = """
var currentToneId = null;

function showTone(id) {
  document.querySelectorAll('.tone-detail').forEach(function(el) {
    el.style.display = 'none';
  });
  var target = document.getElementById('tone-' + id);
  if (target) { target.style.display = 'block'; }
  document.querySelectorAll('.sidebar-item').forEach(function(el) {
    el.classList.toggle('active', el.dataset.id === id);
  });
  var panel = document.getElementById('main-panel');
  if (panel) { panel.scrollTop = 0; }
  showView(id, 'chain');
  currentToneId = id;
}

function showView(toneId, view) {
  var chainEl = document.getElementById('chain-view-' + toneId);
  var checkEl = document.getElementById('checklist-view-' + toneId);
  if (chainEl) chainEl.style.display = view === 'chain' ? '' : 'none';
  if (checkEl) checkEl.style.display = view === 'checklist' ? '' : 'none';
  document.querySelectorAll('.view-tab[data-tone="' + toneId + '"]').forEach(function(t) {
    t.classList.toggle('active', t.dataset.view === view);
  });
}

function scrollToPlugin(toneId, num) {
  var el = document.getElementById('plugin-' + toneId + '-' + num);
  if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
}

function scrollToItem(id) {
  var el = document.getElementById(id);
  if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
}

var activeFilters = { status: 'all', genre: 'all', pickup: 'all', guitar: 'all', amp: 'all' };
var showArchived = false;

function setFilter(dim, val) {
  activeFilters[dim] = val;
  document.querySelectorAll('.filter-btn[data-dim="' + dim + '"]').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.filter === val);
  });
  if (dim === 'amp') {
    var sel = document.getElementById('amp-filter-select');
    if (sel) { sel.value = val; }
  }
  applyFilters();
}

function toggleShowArchived(checked) {
  showArchived = !!checked;
  localStorage.setItem('tv-show-archived', showArchived ? 'true' : 'false');
  applyFilters();
}

function applyFilters() {
  var items = document.querySelectorAll('.sidebar-item');
  var visibleCount = 0;
  var firstVisible = null;
  var activeVisible = false;
  items.forEach(function(el) {
    var elAmps = el.dataset.amp ? el.dataset.amp.split(',').map(function(s) { return s.trim(); }) : [];
    var isArchived = (el.dataset.status === 'archived');

    var statusMatch = false;
    if (activeFilters.status === 'archived') {
      statusMatch = isArchived;
    } else if (activeFilters.status === 'all') {
      statusMatch = !isArchived || showArchived;
    } else {
      statusMatch = (el.dataset.status === activeFilters.status);
    }

    var show = statusMatch
            && (activeFilters.genre  === 'all' || el.dataset.genre  === activeFilters.genre)
            && (activeFilters.pickup === 'all' || el.dataset.pickup === activeFilters.pickup)
            && (activeFilters.guitar === 'all' || el.dataset.guitar === activeFilters.guitar)
            && (activeFilters.amp    === 'all' || elAmps.includes(activeFilters.amp));

    el.style.display = show ? '' : 'none';
    if (show) {
      visibleCount++;
      if (!firstVisible) { firstVisible = el; }
      if (el.classList.contains('active')) { activeVisible = true; }
    }
  });

  var countEl = document.querySelector('.vault-count');
  if (countEl) {
    countEl.textContent = visibleCount + ' tone' + (visibleCount !== 1 ? 's' : '');
  }

  if (!activeVisible && firstVisible) {
    showTone(firstVisible.dataset.id);
  } else if (!firstVisible) {
    document.querySelectorAll('.tone-detail').forEach(function(el) {
      el.style.display = 'none';
    });
    var emptyEl = document.getElementById('empty-state');
    if (emptyEl) { emptyEl.style.display = 'flex'; }
  } else {
    var emptyEl = document.getElementById('empty-state');
    if (emptyEl) { emptyEl.style.display = 'none'; }
  }
}

// Keyboard navigation between tones
document.addEventListener('keydown', function(e) {
  if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') { return; }
  var items = Array.from(document.querySelectorAll('.sidebar-item')).filter(function(el) {
    return el.style.display !== 'none';
  });
  var idx = items.findIndex(function(el) { return el.classList.contains('active'); });
  var newIdx = idx + (e.key === 'ArrowDown' ? 1 : -1);
  newIdx = Math.max(0, Math.min(newIdx, items.length - 1));
  if (newIdx !== idx) {
    showTone(items[newIdx].dataset.id);
    items[newIdx].scrollIntoView({ block: 'nearest' });
  }
  e.preventDefault();
});

// Allow Enter/Space on sidebar items when focused
document.querySelectorAll('.sidebar-item').forEach(function(el) {
  el.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      showTone(el.dataset.id);
      e.preventDefault();
    }
  });
});

function toggleTheme() {
  var html = document.documentElement;
  var current = html.dataset.theme || 'dark';
  var next = current === 'dark' ? 'light' : 'dark';
  html.dataset.theme = next;
  localStorage.setItem('tv-theme', next);
  var btn = document.getElementById('theme-toggle');
  if (btn) { btn.innerHTML = next === 'dark' ? '&#9788; Light' : '&#9790; Dark'; }
}

function toggleFilters() {
  var container = document.getElementById('filters-container');
  var icon = document.getElementById('filters-toggle-icon');
  var isCollapsed = container.classList.toggle('collapsed');
  icon.classList.toggle('collapsed', isCollapsed);
  localStorage.setItem('tv-filters-collapsed', isCollapsed ? 'true' : 'false');
}

// Sync toggle states on load
(function() {
  var savedTheme = localStorage.getItem('tv-theme');
  var btn = document.getElementById('theme-toggle');
  if (savedTheme && btn) { btn.innerHTML = savedTheme === 'dark' ? '&#9788; Light' : '&#9790; Dark'; }
  
  var savedArchived = localStorage.getItem('tv-show-archived');
  if (savedArchived === 'true') {
    showArchived = true;
    var chk = document.getElementById('show-archived-checkbox');
    if (chk) chk.checked = true;
  }

  var collapsed = localStorage.getItem('tv-filters-collapsed');
  if (collapsed === 'true') {
    var container = document.getElementById('filters-container');
    var icon = document.getElementById('filters-toggle-icon');
    if (container) container.classList.add('collapsed');
    if (icon) icon.classList.add('collapsed');
  }

  applyFilters();
}());
"""

def generate_markdown_index(tones, output_path):
    """Generate a Markdown table index of all tones."""
    lines = [
        "# Tone Index",
        "",
        "| Title | Pickup Type | Intended/Tested Guitar | File Path | Status |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    for tone in tones:
        pickup = tone.get('pickup_type', '')
        # File path relative to 'tones' dir
        rel_path = tone['source_path'].replace('tones/', '')
        
        lines.append(f"| {tone['title']} | {pickup} | {tone['guitar']} | [{rel_path}]({rel_path}) | {tone['status']} |")
    
    output_path.write_text("\n".join(lines) + "\n", encoding='utf-8')


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    build_only = '--build-only' in sys.argv

    script_dir = Path(__file__).parent
    tones_dir = script_dir.parent / 'tones'
    output_path = script_dir / 'tone-viewer.html'
    index_path = tones_dir / 'INDEX.md'

    # Find all .md files in tones/ and its subdirectories, excluding INDEX.md and eqprints
    all_tone_files = sorted([
        f for f in tones_dir.rglob('*.md') 
        if f.name != 'INDEX.md' and 'eqprints' not in f.parts
    ])

    if not all_tone_files:
        print('No tone files found in tones/')
        sys.exit(0)

    tones = [parse_tone_file(f) for f in all_tone_files]

    # Add pickup_type to the tone data for index generation
    for i, f in enumerate(all_tone_files):
        fm, _ = parse_frontmatter(f.read_text())
        tones[i]['pickup_type'] = fm.get('pickup_type', '')

    # Generate MD Index
    generate_markdown_index(tones, index_path)
    print(f'Generated: {index_path}')

    first_id = tones[0]['id']

    amp_set = set()
    for t in tones:
        if t.get('amp'):
            for a in t['amp'].split(','):
                amp_set.add(a.strip())
    amp_values = sorted(list(amp_set))
    amp_options = ''.join(
        f'<option value="{h(a)}">{h(a)}</option>' for a in amp_values
    )

    sidebar_html = '\n'.join(render_sidebar_item(t, i == 0) for i, t in enumerate(tones))
    detail_html = '\n'.join(render_tone(t) for t in tones)
    generated_at = datetime.now().strftime('%Y-%m-%d %H:%M')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tone Vault</title>
<script>(function(){{var t=localStorage.getItem('tv-theme');if(t)document.documentElement.dataset.theme=t;}}());</script>
<style>
{CSS}
</style>
</head>
<body>
<div class="app">

  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="vault-wordmark">
        <div class="vault-wordmark-logo">
          <span class="vault-hex">&#x2B21;</span>
          <span class="vault-name">Tone Vault</span>
        </div>
        <button class="theme-toggle" id="theme-toggle" onclick="toggleTheme()">&#9788; Light</button>
      </div>
      <div class="vault-count">{len(tones)} tone{'s' if len(tones) != 1 else ''}</div>
    </div>
    <div class="filters-toggle-bar" onclick="toggleFilters()">
      <span class="filter-title-label">Filters</span>
      <span class="filters-toggle-icon" id="filters-toggle-icon">&#x25BC;</span>
    </div>
    <div class="filters-container" id="filters-container">
      <div class="filter-section">
        <div class="filter-header-row">
          <div class="filter-label">Status</div>
          <label class="archived-toggle-label" title="Show archived toneprints">
            <input type="checkbox" id="show-archived-checkbox" onchange="toggleShowArchived(this.checked)">
            <span>Show Archived</span>
          </label>
        </div>
        <div class="filter-row">
          <button class="filter-btn active" data-dim="status" data-filter="all" onclick="setFilter('status','all')">All</button>
          <button class="filter-btn" data-dim="status" data-filter="initial" onclick="setFilter('status','initial')">Initial</button>
          <button class="filter-btn" data-dim="status" data-filter="tested" onclick="setFilter('status','tested')">Tested</button>
          <button class="filter-btn" data-dim="status" data-filter="refined" onclick="setFilter('status','refined')">Refined</button>
          <button class="filter-btn" data-dim="status" data-filter="archived" onclick="setFilter('status','archived')">Archived</button>
        </div>
      </div>
      <div class="filter-section">
        <div class="filter-label">Style</div>
        <div class="filter-row">
          <button class="filter-btn active" data-dim="genre" data-filter="all" onclick="setFilter('genre','all')">All</button>
          <button class="filter-btn" data-dim="genre" data-filter="jazz" onclick="setFilter('genre','jazz')">Jazz</button>
          <button class="filter-btn" data-dim="genre" data-filter="blues" onclick="setFilter('genre','blues')">Blues</button>
          <button class="filter-btn" data-dim="genre" data-filter="rock" onclick="setFilter('genre','rock')">Rock</button>
          <button class="filter-btn" data-dim="genre" data-filter="country" onclick="setFilter('genre','country')">Country</button>
          <button class="filter-btn" data-dim="genre" data-filter="ambient" onclick="setFilter('genre','ambient')">Ambient</button>
          <button class="filter-btn" data-dim="genre" data-filter="clean" onclick="setFilter('genre','clean')">Clean</button>
        </div>
      </div>
      <div class="filter-section">
        <div class="filter-label">Pickup</div>
        <div class="filter-row">
          <button class="filter-btn active" data-dim="pickup" data-filter="all" onclick="setFilter('pickup','all')">All</button>
          <button class="filter-btn" data-dim="pickup" data-filter="humbucker" onclick="setFilter('pickup','humbucker')">HB</button>
          <button class="filter-btn" data-dim="pickup" data-filter="single-coil" onclick="setFilter('pickup','single-coil')">SC</button>
          <button class="filter-btn" data-dim="pickup" data-filter="p-90" onclick="setFilter('pickup','p-90')">P-90</button>
        </div>
      </div>
      <div class="filter-section">
        <div class="filter-label">Guitar</div>
        <div class="filter-row">
          <button class="filter-btn active" data-dim="guitar" data-filter="all" onclick="setFilter('guitar','all')">All</button>
          <button class="filter-btn" data-dim="guitar" data-filter="telecaster" onclick="setFilter('guitar','telecaster')">Tele</button>
          <button class="filter-btn" data-dim="guitar" data-filter="strat" onclick="setFilter('guitar','strat')">Strat</button>
          <button class="filter-btn" data-dim="guitar" data-filter="les-paul" onclick="setFilter('guitar','les-paul')">LP</button>
          <button class="filter-btn" data-dim="guitar" data-filter="semi-hollow" onclick="setFilter('guitar','semi-hollow')">Hollow</button>
          <button class="filter-btn" data-dim="guitar" data-filter="framus" onclick="setFilter('guitar','framus')">Framus</button>
        </div>
      </div>
      <div class="filter-section">
        <div class="filter-label">Amp</div>
        <select class="amp-select" id="amp-filter-select" onchange="setFilter('amp', this.value)">
          <option value="all">All amps</option>
          {amp_options}
        </select>
      </div>
    </div>
    <div class="sidebar-list">
{sidebar_html}
    </div>
    <div class="sidebar-footer">Generated {generated_at}</div>
  </aside>

  <main class="main-panel" id="main-panel">
{detail_html}
    <div class="empty-state" id="empty-state" style="display:none">
      <div class="empty-icon">&#x2B21;</div>
      <p>Select a tone from the sidebar</p>
    </div>
  </main>

</div>
<script>
{JS}
showTone('{first_id}');
</script>
</body>
</html>"""

    output_path.write_text(html, encoding='utf-8')
    print(f'Generated: {output_path}')

    # Automatically sync to cloud location
    sync_script = script_dir.parent / 'scripts' / 'sync_toneprints.sh'
    if sync_script.exists():
        print(f"Running sync script: {sync_script}")
        subprocess.run(['bash', str(sync_script)], check=False)
    else:
        print("Warning: sync_toneprints.sh not found, skipping sync.")

    if not build_only:
        subprocess.run(['open', str(output_path)], check=False)


if __name__ == '__main__':
    main()
