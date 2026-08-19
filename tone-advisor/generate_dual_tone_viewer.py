#!/usr/bin/env python3
"""
generate_dual_tone_viewer.py

Dedicated HTML Vault Viewer Builder for Dual-Amp Parallel Rigs.
Reads dual-amp toneprints from tones/*.md (files with dual_rig: true or amp_a/amp_b)
and outputs a self-contained dual-tone-viewer.html with tone vault sidebar filters,
dark/light themes, amp matrix rendering, and keyboard navigation.

Usage:
    python3 tone-advisor/generate_dual_tone_viewer.py           # generate + open in browser
    python3 tone-advisor/generate_dual_tone_viewer.py --build-only  # generate only (for agent use)
"""

import os
import sys
import re
import json
import subprocess
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
TONES_DIR = SCRIPT_DIR.parent / "tones"
OUTPUT_HTML = SCRIPT_DIR / "dual-tone-viewer.html"


def parse_yaml_frontmatter(content):
    match = re.match(r"^---\s*\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    body = content[match.end():]
    
    lines = yaml_text.splitlines()
    parsed_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith('"') and val.endswith('"'): val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"): val = val[1:-1]
            
            if val == "": val = None
            elif isinstance(val, str) and val.lower() == "true": val = True
            elif isinstance(val, str) and val.lower() == "false": val = False
            else:
                try:
                    if "." in str(val): val = float(val)
                    else: val = int(val)
                except ValueError:
                    pass
            parsed_lines.append((indent, key, val))

    def build_tree(start_idx, parent_indent):
        result = {}
        idx = start_idx
        while idx < len(parsed_lines):
            indent, key, val = parsed_lines[idx]
            if indent <= parent_indent:
                break
            
            next_idx = idx + 1
            has_children = False
            if next_idx < len(parsed_lines):
                next_indent, _, _ = parsed_lines[next_idx]
                if next_indent > indent:
                    has_children = True
            
            if has_children:
                child_dict, next_idx = build_tree(next_idx, indent)
                result[key] = child_dict
                idx = next_idx
            else:
                result[key] = val
                idx += 1
        return result, idx

    tree, _ = build_tree(0, -1)
    return tree, body


def parse_md_sections(body):
    sections = {}
    current_sec = "body"
    lines = body.splitlines()
    sec_content = []

    for line in lines:
        if line.startswith("## "):
            if sec_content:
                sections[current_sec] = "\n".join(sec_content)
                sec_content = []
            current_sec = line[3:].strip().lower()
        else:
            sec_content.append(line)
    if sec_content:
        sections[current_sec] = "\n".join(sec_content)
    return sections


def parse_md_table(table_lines):
    headers = []
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if all(re.match(r'^[\s\-:]+$', c) for c in cells if c):
            continue
        if not headers:
            headers = cells
        else:
            rows.append(cells)
    return headers, rows


def h(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def inline_md(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def render_table(headers, rows):
    if not headers:
        return ''
    setting_col = next((i for i, hd in enumerate(headers) if hd.lower() in ('setting', 'value')), None)
    purpose_col = next((i for i, hd in enumerate(headers) if hd.lower() == 'purpose'), None)

    out = ['<div class="table-wrap"><table class="settings-table"><thead><tr>']
    for i, hdr in enumerate(headers):
        cls = ''
        if i == setting_col: cls = ' class="col-setting"'
        elif i == purpose_col: cls = ' class="col-purpose"'
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


def render_markdown_content(text):
    if not text:
        return ''
    lines = text.split('\n')
    html_parts = []
    current_block = []
    block_type = None

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
        elif block_type == 'h3':
            h_text = ' '.join(current_block)
            html_parts.append(f'<h3 class="markdown-h3">{inline_md(h(h_text))}</h3>')
        elif block_type == 'h4':
            h_text = ' '.join(current_block)
            html_parts.append(f'<h4 class="markdown-h4">{inline_md(h(h_text))}</h4>')
        current_block = []
        block_type = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            close_block()
            continue
        if stripped.startswith('#### '):
            close_block()
            block_type = 'h4'
            current_block.append(stripped[5:].strip())
        elif stripped.startswith('### '):
            close_block()
            block_type = 'h3'
            current_block.append(stripped[4:].strip())
        elif stripped.startswith('|'):
            if block_type != 'table':
                close_block()
                block_type = 'table'
            current_block.append(stripped)
        elif re.match(r'^[\*\-\+]\s+', stripped):
            if block_type != 'ul':
                close_block()
                block_type = 'ul'
            current_block.append(re.sub(r'^[\*\-\+]\s+', '', stripped))
        elif re.match(r'^\d+\.\s+', stripped):
            if block_type != 'ol':
                close_block()
                block_type = 'ol'
            current_block.append(re.sub(r'^\d+\.\s+', '', stripped))
        else:
            if block_type in ('table', 'ul', 'ol', 'h3', 'h4'):
                close_block()
            if block_type is None:
                block_type = 'p'
            current_block.append(stripped)
    close_block()
    return '\n'.join(html_parts)


def infer_genre(tags_str):
    if not isinstance(tags_str, str):
        return 'jazz'
    tags = [t.strip().lower() for t in tags_str.split(',') if t.strip()]
    tag_set = set(tags)
    if 'ambient' in tag_set or 'sound-bath' in tag_set:
        return 'ambient'
    if any(t in tag_set for t in ('classic-rock', 'crunch', 'jcm800', 'plexi', 'lead', 'rock')):
        return 'rock'
    if any(t in tag_set for t in ('country', 'folk-rock', 'jangle', 'chime')):
        return 'country'
    if 'neo-soul' in tag_set or 'jazz-blues' in tag_set or ('jazz' in tag_set and 'blues' not in tag_set):
        return 'jazz'
    if 'blues' in tag_set:
        return 'blues'
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


def render_guide_item(text):
    m = re.match(r'\*\*(.+?)\*\*[:\s]+(.*)', text, re.DOTALL)
    if m:
        label = h(m.group(1))
        content = inline_md(h(m.group(2)))
        return f'<div class="guide-card"><span class="guide-label">{label}</span><span class="guide-content">{content}</span></div>'
    return f'<div class="guide-card"><span class="guide-content">{inline_md(h(text))}</span></div>'


def load_dual_toneprints():
    dual_rigs = []
    for root, _, files in os.walk(TONES_DIR):
        for file in sorted(files):
            if file.endswith(".md") and file != "INDEX.md":
                filepath = Path(root) / file
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                fm, body = parse_yaml_frontmatter(content)
                if fm.get("dual_rig") or "amp_a" in fm:
                    sections = parse_md_sections(body)
                    preset_name = fm.get("preset_name", filepath.stem)
                    amp_a = fm.get("amp_a", {})
                    amp_b = fm.get("amp_b", {})
                    
                    amp_a_model = amp_a.get("model", "Amp A")
                    amp_b_model = amp_b.get("model", "Amp B")
                    
                    amp_a_preset = f"Toneprint - {preset_name} - Amp A ({amp_a_model.split(' ')[0]})"
                    amp_b_preset = f"Toneprint - {preset_name} - Amp B ({amp_b_model.split(' ')[0]})"
                    bus_la2a_preset = f"Toneprint - {preset_name} - Bus LA-2A"
                    bus_hits_preset = f"Toneprint - {preset_name} - Bus Hitsville"

                    tags_raw = fm.get("tags", "")
                    tags_list = [t.strip() for t in tags_raw.split(",") if t.strip()] if isinstance(tags_raw, str) else []
                    guitar_str = fm.get("guitar", "Universal")
                    slug = fm.get("id", filepath.stem)

                    guide_items = []
                    sp_section = sections.get("starting point guide", "")
                    if sp_section:
                        for line in sp_section.split("\n"):
                            line = line.strip()
                            if line.startswith("- "):
                                guide_items.append(line[2:])

                    feedback = []
                    fb_section = sections.get("feedback history", "")
                    if fb_section:
                        fh_parts = re.split(r"^### (.+)$", fb_section, flags=re.MULTILINE)
                        for i in range(1, len(fh_parts), 2):
                            fh_hdr = fh_parts[i].strip()
                            fh_body = fh_parts[i + 1].strip() if i + 1 < len(fh_parts) else ""
                            dm = re.match(r"^(\d{4}-\d{2}-\d{2})\s+—\s+(.+)$", fh_hdr)
                            feedback.append({
                                "date": dm.group(1) if dm else fh_hdr,
                                "status": dm.group(2).strip() if dm else "",
                                "content": fh_body,
                            })

                    h1 = re.search(r"^# (.+)$", body, re.MULTILINE)
                    title = h1.group(1).strip() if h1 else fm.get("preset_name", filepath.stem)
                    rel_source = str(filepath.relative_to(TONES_DIR.parent))

                    dual_rigs.append({
                        "id": slug,
                        "file": rel_source,
                        "title": title,
                        "preset_name": preset_name,
                        "guitar": guitar_str,
                        "guitar_type": infer_guitar_type(guitar_str),
                        "pickup_type": fm.get("pickup_type", "universal"),
                        "target": fm.get("target", ""),
                        "status": fm.get("status", "initial"),
                        "tags": tags_list,
                        "tags_raw": tags_raw if isinstance(tags_raw, str) else "",
                        "genre": infer_genre(tags_raw),
                        "tone_king_channel": fm.get("tone-king-channel", "bypassed"),
                        "amp": fm.get("amp", f"{amp_a_model} + {amp_b_model}"),
                        "amp_a": amp_a,
                        "amp_b": amp_b,
                        "shared_fx": fm.get("shared_fx", {}),
                        "amp_a_preset": amp_a_preset,
                        "amp_b_preset": amp_b_preset,
                        "bus_la2a_preset": bus_la2a_preset,
                        "bus_hits_preset": bus_hits_preset,
                        "target_sound_md": sections.get("target sound", ""),
                        "signal_chain_md": sections.get("signal chain", ""),
                        "guide_items": guide_items,
                        "feedback": feedback
                    })
    return dual_rigs


STATUS_CLS = {
    'initial': 'status-initial',
    'tested': 'status-tested',
    'refined': 'status-refined',
    'verified': 'status-tested',
    'archived': 'status-archived',
}


def render_params_table(settings):
    if not settings or not isinstance(settings, dict):
        return '<p style="color:var(--muted); font-size:0.8rem;">No settings specified.</p>'
    
    rows = []
    for k, v in settings.items():
        if isinstance(v, bool):
            disp = 'ON' if v else 'OFF'
        else:
            disp = str(v)
        rows.append((k, disp))
    
    table_rows = "".join(f'<tr class="{"row-alt" if i%2 else "row-norm"}"><td class="param-name">{h(k)}</td><td class="param-val">{h(v)}</td></tr>' for i, (k, v) in enumerate(rows))
    
    return f'''<div class="table-wrap">
<table class="param-table">
  <thead><tr><th>Parameter</th><th style="text-align:right;">Setting</th></tr></thead>
  <tbody>{table_rows}</tbody>
</table>
</div>'''


def render_dual_rig_detail(r):
    rig_id = r["id"]
    status = r["status"]
    scls = STATUS_CLS.get(status, "status-initial")
    source_url = f"../{r['file']}"
    
    tags_html = "".join(f'<span class="tag">{h(t)}</span>' for t in r["tags"])
    
    amp_a = r.get("amp_a", {})
    amp_b = r.get("amp_b", {})
    shared = r.get("shared_fx", {})

    target_sound_html = ""
    if r["target_sound_md"]:
        target_sound_html = f'''
<section class="tone-section">
  <h2 class="section-header">Target Sound</h2>
  <div class="target-sound">{render_markdown_content(r["target_sound_md"])}</div>
</section>'''

    signal_chain_html = ""
    if r["signal_chain_md"]:
        signal_chain_html = f'''
<section class="tone-section">
  <h2 class="section-header">Signal Chain Breakdown</h2>
  <div class="target-sound">{render_markdown_content(r["signal_chain_md"])}</div>
</section>'''

    guide_html = ""
    if r["guide_items"]:
        items = "".join(render_guide_item(item) for item in r["guide_items"])
        guide_html = f'''
<section class="tone-section">
  <h2 class="section-header">Starting Point Guide</h2>
  <div class="guide-grid">{items}</div>
</section>'''

    feedback_html = ""
    if r["feedback"]:
        entries = []
        for fb in r["feedback"]:
            fb_scls = STATUS_CLS.get(fb["status"], "status-initial")
            content_p = f'<div class="feedback-content">{render_markdown_content(fb["content"])}</div>' if fb["content"] else ""
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

    return f'''
<div class="tone-detail" id="rig-{h(rig_id)}" style="display:none">
  <div class="tone-header">
    <div class="tone-header-top">
      <h1 class="tone-title">{h(r["title"])}</h1>
      <a href="{h(source_url)}" class="view-source-btn" target="_blank">View Source</a>
    </div>
    <div class="tone-meta">
      <span class="meta-guitar">{h(r["guitar"])}</span>
      <span class="badge {scls}">{h(status)}</span>
      <span class="badge" style="background:rgba(96,165,250,0.15); color:#60a5fa; border:1px solid #3b82f6;">{h(r["pickup_type"])}</span>
      <span class="meta-channel">TK: {h(r["tone_king_channel"])}</span>
    </div>
    <div class="tone-tags">{tags_html}</div>
    <p class="tone-target-desc">{h(r["target"])}</p>
  </div>

  {target_sound_html}

  <section class="tone-section">
    <h2 class="section-header">Parallel Amp Matrix</h2>
    <div class="amp-matrix">
      <div class="amp-card amp-a">
        <div class="amp-card-head">
          <div class="amp-name">{h(amp_a.get("name", "Amp A"))}</div>
          <div class="pan-tag">PAN: {h(amp_a.get("pan", -12))} (L)</div>
        </div>
        {render_params_table(amp_a.get("amp_settings"))}
        <button class="copy-btn" onclick="copyPreset('{h(r["amp_a_preset"])}')">📋 Copy Amp A Preset Name</button>
      </div>

      <div class="amp-card amp-b">
        <div class="amp-card-head">
          <div class="amp-name">{h(amp_b.get("name", "Amp B"))}</div>
          <div class="pan-tag">PAN: +{h(amp_b.get("pan", 12))} (R)</div>
        </div>
        {render_params_table(amp_b.get("amp_settings"))}
        <button class="copy-btn" onclick="copyPreset('{h(r["amp_b_preset"])}')">📋 Copy Amp B Preset Name</button>
      </div>
    </div>

    <div class="bus-section">
      <div>
        <div class="bus-title">Parallel Submix Bus & Shared FX</div>
        <div class="bus-details">
          LA-2A: Peak Red <strong>{shared.get("la2a", {}).get("peak_reduction", 30)}</strong>, Gain <strong>{shared.get("la2a", {}).get("gain", 30)}</strong> |
          Reverb: Hitsville Decay <strong>{shared.get("hitsville", {}).get("decay", 2.0)}s</strong>, Mix <strong>{shared.get("hitsville", {}).get("mix", 0.12)}</strong>
        </div>
      </div>
      <div class="preset-pills">
        <button class="copy-btn" style="width: auto;" onclick="copyPreset('{h(r["bus_la2a_preset"])}')">Copy Bus LA-2A</button>
        <button class="copy-btn" style="width: auto;" onclick="copyPreset('{h(r["bus_hits_preset"])}')">Copy Bus Reverb</button>
      </div>
    </div>
  </section>

  {signal_chain_html}
  {guide_html}
  {feedback_html}
</div>'''


def render_sidebar_item(r, is_first):
    rig_id = r["id"]
    status = r["status"]
    scls = STATUS_CLS.get(status, "status-initial")
    active = " active" if is_first else ""
    guitar_short = r["guitar"].split("/")[0].split("(")[0].strip()
    tags_preview = ", ".join(r["tags"][:3])
    
    amps_attr = f"{r.get('amp_a', {}).get('model', '')},{r.get('amp_b', {}).get('model', '')}"

    return f'''<div class="sidebar-item{active}" onclick="showTone('{h(rig_id)}')" data-id="{h(rig_id)}" data-status="{h(status)}" data-genre="{h(r['genre'])}" data-guitar="{h(r['guitar_type'])}" data-pickup="{h(r['pickup_type'])}" data-amp="{h(amps_attr)}" tabindex="0">
  <div class="sidebar-title">{h(r["title"])}</div>
  <div class="sidebar-sub">{h(guitar_short)}</div>
  <div class="sidebar-tags">{h(tags_preview)}</div>
  <span class="badge {scls} sidebar-badge">{h(status)}</span>
</div>'''


CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:              #191c22;
  --surface:         #22262f;
  --surface-alt:     #2c313d;
  --surface-card:    #1a202c;
  --border:          #363b48;
  --accent:          #5ba4c8;
  --accent-dim:      #2e5f7a;
  --accent-glow:     rgba(91,164,200,0.11);
  --accent-a:        #ec4899;
  --accent-b:        #06b6d4;
  --text:            #e8edf4;
  --secondary:       #8c96a4;
  --muted:           #545c68;
  --accent-fg:       #0e1014;
  --badge-tested-bg: rgba(91,164,200,0.14);
  --sidebar-w:       290px;
  --code-bg:         #0f131d;
}

[data-theme="light"] {
  --bg:              #f4f7f5;
  --surface:         #ffffff;
  --surface-alt:     #eef2ef;
  --surface-card:    #f8fafc;
  --border:          #c8d5cb;
  --accent:          #059669;
  --accent-dim:      #047857;
  --accent-glow:     rgba(5,150,105,0.10);
  --accent-a:        #db2777;
  --accent-b:        #0891b2;
  --text:            #111827;
  --secondary:       #374151;
  --muted:           #9ca3af;
  --accent-fg:       #ffffff;
  --badge-tested-bg: rgba(5,150,105,0.12);
  --code-bg:         #f1f5f9;
}

html, body { height: 100%; overflow: hidden; }

body {
  font-family: -apple-system, 'SF Pro Text', 'Helvetica Neue', sans-serif;
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
  max-width: 1050px;
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

.filters-toggle-bar:hover { background: var(--surface-alt); }
.filters-toggle-bar:hover .filter-title-label { color: var(--accent); }
.filters-toggle-bar:hover .filters-toggle-icon { color: var(--text); }

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

.filters-toggle-icon.collapsed { transform: rotate(-90deg); }

.filters-container {
  display: flex;
  flex-direction: column;
  gap: 7px;
  padding: 8px 12px 10px;
  border-bottom: 1px solid var(--border);
  overflow: hidden;
  transition: max-height 0.25s ease-out, padding 0.25s ease-out, border-bottom-width 0.25s ease-out;
  max-height: 600px;
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

.search-input-sidebar {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: 6px;
  padding: 5px 8px;
  font-size: 11px;
  font-family: inherit;
  outline: none;
  width: 100%;
  transition: border-color 0.12s;
}

.search-input-sidebar:focus {
  border-color: var(--accent);
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

/* ── Detail view ── */
.tone-header {
  margin-bottom: 28px;
  padding-bottom: 20px;
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
  font-size: 26px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 10px;
  line-height: 1.25;
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
  font-family: 'JetBrains Mono', 'SF Mono', monospace;
  letter-spacing: 0.03em;
}

.tone-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 12px;
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
  font-size: 13.5px;
  color: var(--secondary);
  font-style: italic;
  line-height: 1.55;
}

/* ── Section structure ── */
.tone-section { margin-bottom: 32px; }

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

.target-sound p, .target-sound li { margin-bottom: 8px; }
.target-sound ul { margin-left: 20px; }

/* ── Amp Matrix ── */
.amp-matrix {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

@media (max-width: 850px) {
  .amp-matrix { grid-template-columns: 1fr; }
}

.amp-card {
  background: var(--surface-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.amp-card.amp-a { border-top: 4px solid var(--accent-a); }
.amp-card.amp-b { border-top: 4px solid var(--accent-b); }

.amp-card-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.amp-name { font-size: 1.1rem; font-weight: 600; color: var(--text); }
.pan-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
}
.amp-a .pan-tag { background: rgba(236, 72, 153, 0.15); color: var(--accent-a); }
.amp-b .pan-tag { background: rgba(6, 182, 212, 0.15); color: var(--accent-b); }

.table-wrap { overflow-x: auto; }

.param-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
  margin-bottom: 1rem;
}

.param-table th {
  text-align: left;
  padding: 0.4rem 0.6rem;
  background: rgba(0,0,0,0.15);
  color: var(--muted);
  border-bottom: 1px solid var(--border);
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.param-table td {
  padding: 0.45rem 0.6rem;
  border-bottom: 1px solid var(--border);
}

.param-name { font-weight: 500; color: var(--text); }
.param-val { font-family: 'JetBrains Mono', monospace; color: var(--accent); text-align: right; font-weight: 600; }

.copy-btn {
  width: 100%;
  background: var(--accent-glow);
  border: 1px solid var(--accent-dim);
  color: var(--accent);
  padding: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
  transition: all 0.15s;
}

.copy-btn:hover {
  background: var(--accent);
  color: var(--accent-fg);
  border-color: var(--accent);
}

/* ── Bus Section ── */
.bus-section {
  background: var(--code-bg);
  border: 1px dashed var(--border);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.bus-title { font-size: 0.95rem; font-weight: 600; color: var(--text); }
.bus-details { font-size: 0.85rem; color: var(--secondary); margin-top: 2px; }
.preset-pills { display: flex; gap: 0.5rem; flex-wrap: wrap; }

/* ── Starting Point Guide & Feedback ── */
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
.guide-label { color: var(--accent); font-weight: 600; }
.guide-label::after { content: ': '; }
.guide-content { color: var(--text); }

.feedback-entry {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 13px 18px;
  margin-bottom: 8px;
  font-size: 13px;
  line-height: 1.6;
}
.feedback-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.feedback-date {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--accent);
  font-weight: 600;
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

/* ── Scrollbars & Responsive ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--surface-alt); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }

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

strong { color: var(--text); font-weight: 600; }
em { color: var(--secondary); }
code {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(255,255,255,0.08);
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 0.9em;
}
[data-theme="light"] code { background: rgba(0,0,0,0.05); }
"""


JS = """
var currentRigId = null;

function safeGet(key) {
  try { return localStorage.getItem(key); } catch (e) { return null; }
}
function safeSet(key, val) {
  try { localStorage.setItem(key, val); } catch (e) {}
}

function showTone(id) {
  document.querySelectorAll('.tone-detail').forEach(function(el) {
    el.style.display = 'none';
  });
  var target = document.getElementById('rig-' + id);
  if (target) { target.style.display = 'block'; }
  
  var empty = document.getElementById('empty-state');
  if (empty) { empty.style.display = target ? 'none' : 'flex'; }

  document.querySelectorAll('.sidebar-item').forEach(function(el) {
    el.classList.toggle('active', el.dataset.id === id);
  });
  var panel = document.getElementById('main-panel');
  if (panel) { panel.scrollTop = 0; }
  currentRigId = id;
}

var activeFilters = { status: 'all', genre: 'all', pickup: 'all', guitar: 'all', amp: 'all' };

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

function applyFilters() {
  var queryInput = document.getElementById('searchInputSidebar');
  var query = (queryInput ? queryInput.value : '').toLowerCase();
  var items = document.querySelectorAll('.sidebar-item');
  var visibleCount = 0;
  var firstVisible = null;
  var activeVisible = false;

  items.forEach(function(el) {
    var elAmps = el.dataset.amp ? el.dataset.amp.split(',').map(function(s) { return s.trim(); }) : [];
    var titleEl = el.querySelector('.sidebar-title');
    var subEl = el.querySelector('.sidebar-sub');
    var tagsEl = el.querySelector('.sidebar-tags');

    var title = titleEl ? titleEl.textContent.toLowerCase() : '';
    var sub = subEl ? subEl.textContent.toLowerCase() : '';
    var tags = tagsEl ? tagsEl.textContent.toLowerCase() : '';

    var matchesSearch = !query || title.includes(query) || sub.includes(query) || tags.includes(query);
    var matchesFilters = (activeFilters.status === 'all' || el.dataset.status === activeFilters.status)
            && (activeFilters.genre  === 'all' || el.dataset.genre  === activeFilters.genre)
            && (activeFilters.pickup === 'all' || el.dataset.pickup === activeFilters.pickup)
            && (activeFilters.guitar === 'all' || el.dataset.guitar === activeFilters.guitar)
            && (activeFilters.amp    === 'all' || elAmps.includes(activeFilters.amp));
    
    var show = matchesSearch && matchesFilters;
    el.style.display = show ? '' : 'none';
    if (show) {
      visibleCount++;
      if (!firstVisible) { firstVisible = el; }
      if (el.classList.contains('active')) { activeVisible = true; }
    }
  });

  var countEl = document.querySelector('.vault-count');
  if (countEl) {
    countEl.textContent = visibleCount + ' dual rig' + (visibleCount !== 1 ? 's' : '');
  }
  if (!activeVisible && firstVisible) {
    showTone(firstVisible.dataset.id);
  } else if (!firstVisible) {
    document.querySelectorAll('.tone-detail').forEach(function(el) { el.style.display = 'none'; });
    var empty = document.getElementById('empty-state');
    if (empty) { empty.style.display = 'flex'; }
  }
}

function copyPreset(text) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text);
  }
  alert('Copied to clipboard:\\n' + text);
}

document.addEventListener('keydown', function(e) {
  if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') { return; }
  var items = Array.from(document.querySelectorAll('.sidebar-item')).filter(function(el) {
    return el.style.display !== 'none';
  });
  if (!items.length) return;
  var idx = items.findIndex(function(el) { return el.classList.contains('active'); });
  var newIdx = idx + (e.key === 'ArrowDown' ? 1 : -1);
  newIdx = Math.max(0, Math.min(newIdx, items.length - 1));
  if (newIdx !== idx) {
    showTone(items[newIdx].dataset.id);
    items[newIdx].scrollIntoView({ block: 'nearest' });
  }
  e.preventDefault();
});

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
  safeSet('dtv-theme', next);
  var btn = document.getElementById('theme-toggle');
  if (btn) { btn.innerHTML = next === 'dark' ? '&#9788; Light' : '&#9790; Dark'; }
}

function toggleFilters() {
  var container = document.getElementById('filters-container');
  var icon = document.getElementById('filters-toggle-icon');
  if (container) {
    var isCollapsed = container.classList.toggle('collapsed');
    if (icon) icon.classList.toggle('collapsed', isCollapsed);
    safeSet('dtv-filters-collapsed', isCollapsed ? 'true' : 'false');
  }
}

(function() {
  var savedTheme = safeGet('dtv-theme');
  var btn = document.getElementById('theme-toggle');
  if (savedTheme) {
    document.documentElement.dataset.theme = savedTheme;
    if (btn) btn.innerHTML = savedTheme === 'dark' ? '&#9788; Light' : '&#9790; Dark';
  }
  
  var collapsed = safeGet('dtv-filters-collapsed');
  if (collapsed === 'true') {
    var container = document.getElementById('filters-container');
    var icon = document.getElementById('filters-toggle-icon');
    if (container) container.classList.add('collapsed');
    if (icon) icon.classList.add('collapsed');
  }
}());
"""


def generate_html(dual_rigs):
    if not dual_rigs:
        print("No dual rigs found.")
        return

    first_id = dual_rigs[0]["id"]

    amp_set = set()
    for r in dual_rigs:
        if r.get("amp_a", {}).get("model"):
            amp_set.add(r["amp_a"]["model"])
        if r.get("amp_b", {}).get("model"):
            amp_set.add(r["amp_b"]["model"])
    amp_values = sorted(list(amp_set))
    amp_options = "".join(f'<option value="{h(a)}">{h(a)}</option>' for a in amp_values)

    sidebar_items_html = "\n".join(render_sidebar_item(r, i == 0) for i, r in enumerate(dual_rigs))
    detail_items_html = "\n".join(render_dual_rig_detail(r) for r in dual_rigs)
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Parallel Dual-Amp Rig Vault</title>
<script>(function(){{try{{var t=localStorage.getItem('dtv-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}}}());</script>
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
          <span class="vault-name">Dual-Amp Vault</span>
        </div>
        <button class="theme-toggle" id="theme-toggle" onclick="toggleTheme()">&#9788; Light</button>
      </div>
      <div class="vault-count">{len(dual_rigs)} dual rig{'s' if len(dual_rigs) != 1 else ''}</div>
    </div>

    <div class="filters-toggle-bar" onclick="toggleFilters()">
      <span class="filter-title-label">Filters</span>
      <span class="filters-toggle-icon" id="filters-toggle-icon">&#x25BC;</span>
    </div>

    <div class="filters-container" id="filters-container">
      <div class="filter-section">
        <div class="filter-label">Search</div>
        <input type="text" id="searchInputSidebar" class="search-input-sidebar" placeholder="Search dual rigs..." oninput="applyFilters()">
      </div>

      <div class="filter-section">
        <div class="filter-label">Status</div>
        <div class="filter-row">
          <button class="filter-btn active" data-dim="status" data-filter="all" onclick="setFilter('status','all')">All</button>
          <button class="filter-btn" data-dim="status" data-filter="initial" onclick="setFilter('status','initial')">Initial</button>
          <button class="filter-btn" data-dim="status" data-filter="tested" onclick="setFilter('status','tested')">Tested</button>
          <button class="filter-btn" data-dim="status" data-filter="refined" onclick="setFilter('status','refined')">Refined</button>
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
        <div class="filter-label">Amp Model</div>
        <select class="amp-select" id="amp-filter-select" onchange="setFilter('amp', this.value)">
          <option value="all">All amps</option>
          {amp_options}
        </select>
      </div>
    </div>

    <div class="sidebar-list">
{sidebar_items_html}
    </div>

    <div class="sidebar-footer">Generated {generated_at}</div>
  </aside>

  <main class="main-panel" id="main-panel">
{detail_items_html}
    <div class="empty-state" id="empty-state" style="display:none">
      <div class="empty-icon">&#x2B21;</div>
      <p>No matching dual-amp rigs found</p>
    </div>
  </main>

</div>
<script>
{JS}
showTone('{first_id}');
</script>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated Dual Rig Viewer: '{OUTPUT_HTML}' ({len(dual_rigs)} dual rigs)")


def main():
    build_only = "--build-only" in sys.argv
    dual_rigs = load_dual_toneprints()
    generate_html(dual_rigs)

    sync_script = SCRIPT_DIR.parent / "scripts" / "sync_toneprints.sh"
    if sync_script.exists():
        print(f"Running sync script: {sync_script}")
        subprocess.run(["bash", str(sync_script)], check=False)
    else:
        print("Warning: sync_toneprints.sh not found, skipping sync.")

    if not build_only:
        try:
            subprocess.run(["open", str(OUTPUT_HTML)], check=False)
        except Exception:
            pass


if __name__ == "__main__":
    main()
