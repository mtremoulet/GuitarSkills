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
        if ':' in line:
            k, _, v = line.partition(':')
            data[k.strip()] = v.strip()
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
    Parse a plugin subsection's content.
    Returns dict with: pre_text, headers, rows, note
    """
    lines = content.strip().split('\n')
    pre_lines = []
    table_lines = []
    post_lines = []
    state = 'pre'

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|'):
            state = 'table'
            table_lines.append(stripped)
        elif state == 'table' and not stripped.startswith('|'):
            state = 'post'
            if stripped:
                post_lines.append(stripped)
        elif state == 'pre' and stripped:
            pre_lines.append(stripped)
        elif state == 'post' and stripped:
            post_lines.append(stripped)

    headers, rows = parse_md_table(table_lines)
    return {
        'pre_text': ' '.join(pre_lines),
        'headers': headers,
        'rows': rows,
        'note': ' '.join(post_lines),
    }


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

    # Signal Chain → plugins
    plugins = []
    if 'Signal Chain' in sections:
        chain = sections['Signal Chain']
        plugin_parts = re.split(r'^### (.+)$', chain, flags=re.MULTILINE)
        for i in range(1, len(plugin_parts), 2):
            plugin_header = plugin_parts[i].strip()
            plugin_body = plugin_parts[i + 1].strip() if i + 1 < len(plugin_parts) else ''

            # Parse "N. Name — role" or "Name — role"
            hm = re.match(r'^(?:(\d+)\.\s+)?(.+?)(?:\s+—\s+(.+))?$', plugin_header)
            if hm:
                num = hm.group(1) or str(len(plugins) + 1)
                name = hm.group(2).strip()
                role = hm.group(3).strip() if hm.group(3) else ''
            else:
                num = str(len(plugins) + 1)
                name = plugin_header
                role = ''

            block = parse_plugin_block(plugin_body)
            plugins.append({'num': num, 'name': name, 'role': role, **block})

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

    # Determine platform
    parent_dir = Path(filepath).parent.name
    fm_platform = fm.get('platform', '').strip().lower()
    if parent_dir == 'thr10ii':
        platform_key = 'yamaha'
        platform_display = 'Yamaha'
    elif 'spark' in fm_platform:
        platform_key = 'spark-neo'
        platform_display = 'Spark NEO'
    else:
        platform_key = 'logic'
        platform_display = 'Logic'

    # Prefix thr10ii slugs to avoid collision with same-named Logic tones
    if parent_dir == 'thr10ii':
        slug = fm.get('id', 'thr10ii-' + Path(filepath).stem)
    else:
        slug = fm.get('id', Path(filepath).stem)

    checklist = []
    cl_path = Path(filepath).parent / 'presets' / slug / 'CHECKLIST.md'
    if cl_path.exists():
        cl_text = cl_path.read_text()
        cl_parts = re.split(r'^## (.+)$', cl_text, flags=re.MULTILINE)
        for i in range(1, len(cl_parts), 2):
            if i + 1 >= len(cl_parts):
                break
            hdr = cl_parts[i].strip()
            hm = re.match(r'^(.+?)(?:\s+—\s+(.+))?$', hdr)
            cl_name = hm.group(1).strip() if hm else hdr
            cl_role = hm.group(2).strip() if hm and hm.group(2) else ''
            cl_block = parse_plugin_block(cl_parts[i + 1].strip())
            checklist.append({'name': cl_name, 'role': cl_role, **cl_block})

    return {
        'id': slug,
        'created': fm.get('created', ''),
        'updated': fm.get('updated', ''),
        'guitar': fm.get('guitar', ''),
        'target': fm.get('target', ''),
        'tags': tags,
        'tone_king_channel': fm.get('tone-king-channel', ''),
        'status': fm.get('status', 'initial'),
        'platform_key': platform_key,
        'platform_display': platform_display,
        'title': title,
        'target_sound': sections.get('Target Sound', ''),
        'plugins': plugins,
        'guide_items': guide_items,
        'feedback': feedback,
        'checklist': checklist,
    }


# ── HTML helpers ──────────────────────────────────────────────────────────────

def h(s):
    """HTML-escape a string."""
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def inline_md(text):
    """Convert **bold** and *italic* markers to HTML. Input should be already HTML-escaped."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


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
}


def render_tone(tone):
    tid = tone['id']
    status = tone['status']
    scls = STATUS_CLS.get(status, 'status-initial')

    tags_html = ''.join(f'<span class="tag">{h(t)}</span>' for t in tone['tags'])

    # Signal chain flow chips
    chain_html = ''
    if tone['plugins']:
        chips = []
        for p in tone['plugins']:
            cname = chip_name(p['name'])
            chips.append(
                f'<button class="chain-chip" onclick="scrollToPlugin(\'{h(tid)}\',\'{h(p["num"])}\')">{h(cname)}</button>'
            )
        chain_html = (
            '<div class="chain-flow">'
            + '<span class="chain-arrow">&#8594;</span>'.join(chips)
            + '</div>'
        )

    # Plugin sections
    plugins_html_parts = []
    for p in tone['plugins']:
        pid = f'plugin-{tid}-{p["num"]}'
        role_html = f'<span class="plugin-role">{h(p["role"])}</span>' if p['role'] else ''

        pre_html = ''
        if p['pre_text']:
            pre_html = f'<p class="plugin-note">{inline_md(h(p["pre_text"]))}</p>'

        table_html = render_table(p['headers'], p['rows'])

        note_text = p.get('note', '')
        # Strip surrounding * if entire string is wrapped
        if note_text.startswith('*') and note_text.endswith('*') and len(note_text) > 1:
            note_text = note_text[1:-1]
        note_html = ''
        if note_text:
            note_html = f'<p class="interaction-note">{inline_md(h(note_text))}</p>'

        plugins_html_parts.append(f'''
<div class="plugin-section" id="{h(pid)}">
  <div class="plugin-header">
    <span class="plugin-num">{h(p["num"])}</span>
    <div class="plugin-title-block">
      <span class="plugin-name">{h(p["name"])}</span>
      {role_html}
    </div>
  </div>
  {pre_html}
  {table_html}
  {note_html}
</div>''')

    plugins_html = ''.join(plugins_html_parts)

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
            content_p = f'<p>{inline_md(h(fb["content"]))}</p>' if fb['content'] else ''
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
  <p class="target-sound">{inline_md(h(tone["target_sound"]))}</p>
</section>'''

    # Checklist view (JUCE plugins requiring manual setup)
    checklist_html = ''
    if tone.get('checklist'):
        cl_parts = []
        for p in tone['checklist']:
            cl_role = f'<span class="plugin-role">{h(p["role"])}</span>' if p['role'] else ''
            cl_table = render_table(p['headers'], p['rows'])
            cl_parts.append(f'''
<div class="plugin-section">
  <div class="plugin-header">
    <div class="plugin-title-block">
      <span class="plugin-name">{h(p["name"])}</span>
      {cl_role}
    </div>
  </div>
  {cl_table}
</div>''')
        checklist_html = f'''
<p class="checklist-intro">These plugins use proprietary formats — set manually in Logic using the values below.</p>
{''.join(cl_parts)}'''

    has_checklist = bool(tone.get('checklist'))
    tabs_html = ''
    if has_checklist:
        tabs_html = f'''
<div class="view-tabs">
  <button class="view-tab active" data-tone="{h(tid)}" data-view="chain"
          onclick="showView('{h(tid)}','chain')">Signal Chain</button>
  <button class="view-tab" data-tone="{h(tid)}" data-view="checklist"
          onclick="showView('{h(tid)}','checklist')">Setup Checklist</button>
</div>'''

    chain_section = f'''
  <section class="tone-section">
    <h2 class="section-header">Signal Chain</h2>
    {chain_html}
    {plugins_html}
  </section>
  {guide_html}
  {feedback_html}'''

    if has_checklist:
        body_html = f'''
  {tabs_html}
  <div id="chain-view-{h(tid)}">{chain_section}</div>
  <div id="checklist-view-{h(tid)}" style="display:none">
    <section class="tone-section">
      <h2 class="section-header">Setup Checklist</h2>
      {checklist_html}
    </section>
  </div>'''
    else:
        body_html = chain_section

    return f'''
<div class="tone-detail" id="tone-{h(tid)}" style="display:none">
  <div class="tone-header">
    <h1 class="tone-title">{h(tone["title"])}</h1>
    <div class="tone-meta">
      <span class="meta-guitar">{h(tone["guitar"])}</span>
      <span class="badge {scls}">{h(status)}</span>
      <span class="meta-channel">TK: {h(tone["tone_king_channel"])}</span>
    </div>
    <div class="tone-tags">{tags_html}</div>
    <p class="tone-target-desc">{h(tone["target"])}</p>
  </div>
  {target_sound_html}
  {body_html}
</div>'''


def render_sidebar_item(tone, is_first):
    tid = tone['id']
    status = tone['status']
    scls = STATUS_CLS.get(status, 'status-initial')
    active = ' active' if is_first else ''
    guitar_short = tone['guitar'].split('(')[0].strip()
    tags_preview = ', '.join(tone['tags'][:3])
    pk = tone['platform_key']
    pd = tone['platform_display']
    return f'''<div class="sidebar-item{active}" onclick="showTone('{h(tid)}')" data-id="{h(tid)}" data-platform="{h(pk)}" tabindex="0">
  <div class="sidebar-title">{h(tone["title"])}</div>
  <div class="sidebar-sub">{h(guitar_short)} <span class="platform-pill platform-{h(pk)}">{h(pd)}</span></div>
  <div class="sidebar-tags">{h(tags_preview)}</div>
  <span class="badge {scls} sidebar-badge">{h(status)}</span>
</div>'''


# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:          #1c1c1e;
  --surface:     #2c2c2e;
  --surface-alt: #3a3a3c;
  --border:      #3a3a3c;
  --amber:       #c8922a;
  --amber-dim:   #7a5518;
  --amber-glow:  rgba(200,146,42,0.12);
  --cream:       #f5e6c8;
  --secondary:   #a09070;
  --muted:       #68686e;
  --sidebar-w:   290px;
}

html, body { height: 100%; overflow: hidden; }

body {
  font-family: -apple-system, 'Helvetica Neue', sans-serif;
  background: var(--bg);
  color: var(--cream);
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
  justify-content: center;
  gap: 8px;
  margin-bottom: 4px;
}

.vault-hex {
  color: var(--amber);
  font-size: 20px;
  line-height: 1;
}

.vault-name {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--cream);
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
  border-color: var(--amber-dim);
  background: var(--surface-alt);
}

.sidebar-item.active {
  background: var(--amber-glow);
  border-color: var(--amber-dim);
}

.sidebar-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--cream);
  margin-bottom: 2px;
  line-height: 1.3;
  padding-right: 50px;
}

.sidebar-item.active .sidebar-title { color: var(--amber); }

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

/* ── Platform filter ── */
.platform-filter {
  display: flex;
  gap: 4px;
  justify-content: center;
  margin-top: 10px;
}

.filter-btn {
  background: none;
  border: 1px solid var(--border);
  color: var(--muted);
  border-radius: 20px;
  padding: 3px 10px;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: background 0.12s, color 0.12s, border-color 0.12s;
  font-family: inherit;
}

.filter-btn:hover {
  background: var(--surface-alt);
  color: var(--cream);
  border-color: var(--amber-dim);
}

.filter-btn.active {
  background: var(--amber-glow);
  color: var(--amber);
  border-color: var(--amber-dim);
}

/* ── Platform pills in sidebar ── */
.platform-pill {
  display: inline-block;
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 0.06em;
  border-radius: 3px;
  padding: 1px 5px;
  vertical-align: middle;
  margin-left: 4px;
  text-transform: uppercase;
}

.platform-logic   { background: rgba(100,160,255,0.12); color: #6aa0ff; }
.platform-yamaha  { background: rgba(90,190,120,0.12);  color: #5abc78; }
.platform-spark-neo { background: rgba(220,100,60,0.14); color: #e07044; }

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

.status-initial { background: rgba(104,104,110,0.2); color: #8e8e98; border: 1px solid #4a4a52; }
.status-tested  { background: rgba(200,146,42,0.18); color: var(--amber); border: 1px solid var(--amber-dim); }
.status-refined { background: rgba(52,199,89,0.15);  color: #34c759; border: 1px solid #1e5e30; }

/* ── Tone header ── */
.tone-header {
  margin-bottom: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--border);
}

.tone-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--cream);
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
  color: var(--amber);
  margin-bottom: 14px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
}

.target-sound {
  font-size: 14px;
  line-height: 1.7;
  color: var(--cream);
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
  border-color: var(--amber-dim);
  color: var(--amber);
  background: var(--amber-glow);
}

.chain-chip:hover {
  border-color: var(--amber);
  color: var(--amber);
  background: var(--amber-glow);
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
  background: var(--amber);
  color: #1c1c1e;
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
  color: var(--cream);
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
  background: rgba(200,146,42,0.04);
}

.interaction-note {
  padding: 10px 18px 12px;
  font-size: 12px;
  color: var(--secondary);
  line-height: 1.55;
  border-top: 1px solid var(--border);
  background: rgba(200,146,42,0.04);
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
  border-bottom: 1px solid rgba(58,58,60,0.5);
  line-height: 1.45;
}

.settings-table tr:last-child td { border-bottom: none; }

.row-alt { background: rgba(0,0,0,0.07); }

.col-setting {
  color: var(--amber) !important;
  font-weight: 600;
  white-space: nowrap;
}

.col-setting strong {
  color: var(--amber);
  font-weight: 700;
  background: rgba(200,146,42,0.15);
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
  border-left: 3px solid var(--amber);
  border-radius: 0 8px 8px 0;
  padding: 11px 16px;
  font-size: 13px;
  line-height: 1.55;
}

.guide-label {
  color: var(--amber);
  font-weight: 600;
}

.guide-label::after { content: ': '; }

.guide-content { color: var(--cream); }

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
  color: var(--amber);
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

.view-tab:hover { color: var(--cream); }

.view-tab.active {
  color: var(--amber);
  border-bottom-color: var(--amber);
}

.checklist-intro {
  font-size: 12px;
  color: var(--muted);
  font-style: italic;
  margin-bottom: 16px;
}

/* ── Scrollbars ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--surface-alt); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }

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
strong { color: var(--cream); font-weight: 600; }
em { color: var(--secondary); }

/* ── Responsive ── */
@media (max-width: 700px) {
  .sidebar { width: 220px; min-width: 220px; }
  .main-panel { padding: 24px 20px 48px; }
  .tone-title { font-size: 22px; }
  .col-purpose { display: none; }
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

var currentFilter = 'all';

function setFilter(filter) {
  currentFilter = filter;
  document.querySelectorAll('.filter-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.filter === filter);
  });
  var items = document.querySelectorAll('.sidebar-item');
  var visibleCount = 0;
  var firstVisible = null;
  var activeVisible = false;
  items.forEach(function(el) {
    var show = filter === 'all' || el.dataset.platform === filter;
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
"""

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    build_only = '--build-only' in sys.argv

    script_dir = Path(__file__).parent
    tones_dir = script_dir.parent / 'tones'
    output_path = script_dir / 'tone-viewer.html'

    tone_files = sorted(tones_dir.glob('*.md'))
    thr_files = sorted((tones_dir / 'thr10ii').glob('*.md')) if (tones_dir / 'thr10ii').is_dir() else []
    all_tone_files = tone_files + thr_files
    if not all_tone_files:
        print('No tone files found in tones/')
        sys.exit(0)

    tones = [parse_tone_file(f) for f in all_tone_files]
    first_id = tones[0]['id']

    sidebar_html = '\n'.join(render_sidebar_item(t, i == 0) for i, t in enumerate(tones))
    detail_html = '\n'.join(render_tone(t) for t in tones)
    generated_at = datetime.now().strftime('%Y-%m-%d %H:%M')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tone Vault</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="app">

  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="vault-wordmark">
        <span class="vault-hex">&#x2B21;</span>
        <span class="vault-name">Tone Vault</span>
      </div>
      <div class="platform-filter">
        <button class="filter-btn active" data-filter="all" onclick="setFilter('all')">All</button>
        <button class="filter-btn" data-filter="logic" onclick="setFilter('logic')">Logic</button>
        <button class="filter-btn" data-filter="yamaha" onclick="setFilter('yamaha')">Yamaha</button>
        <button class="filter-btn" data-filter="spark-neo" onclick="setFilter('spark-neo')">Spark</button>
      </div>
      <div class="vault-count">{len(tones)} tone{'s' if len(tones) != 1 else ''}</div>
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

    if not build_only:
        subprocess.run(['open', str(output_path)], check=False)


if __name__ == '__main__':
    main()
