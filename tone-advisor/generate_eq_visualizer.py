#!/usr/bin/env python3
"""
generate_eq_visualizer.py
Reads all tones/eqprints/*.md files and produces a self-contained eq-visualizer.html.

Usage:
    python3 generate_eq_visualizer.py
"""

import re
import sys
import json
from pathlib import Path

def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}, text
    data = {}
    current_key = None
    in_bands = False
    in_bands_7 = False
    bands = {}
    bands_7 = {}
    
    for line in m.group(1).splitlines():
        if line.startswith(' ') or line.startswith('\t'):
            # It's an indented line (part of bands/bands_7 dictionaries)
            if ':' in line:
                k, _, v = line.partition(':')
                try:
                    freq_val = float(k.strip())
                    if freq_val.is_integer():
                        freq_key = str(int(freq_val))
                    else:
                        freq_key = str(freq_val)
                except ValueError:
                    freq_key = k.strip()
                
                db_val = float(v.strip())
                if in_bands:
                    bands[freq_key] = db_val
                elif in_bands_7:
                    bands_7[freq_key] = db_val
            continue
            
        in_bands = False
        in_bands_7 = False
        if ':' in line:
            k, _, v = line.partition(':')
            key = k.strip()
            val = v.strip()
            
            # Detect bands dictionaries
            if key == 'bands':
                in_bands = True
                continue
            elif key == 'bands_7':
                in_bands_7 = True
                continue
                
            # Strip quotes if present
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            
            if val.lower() == 'true':
                val = True
            elif val.lower() == 'false':
                val = False
            else:
                try:
                    if '.' in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
            
            data[key] = val
            
    if bands:
        data['bands'] = bands
    if bands_7:
        data['bands_7'] = bands_7
    return data, text[m.end():]

def markdown_to_html(md_text):
    # Handle bold and italics first
    md_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md_text)
    md_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', md_text)
    
    html_lines = []
    in_list = False
    
    lines = md_text.split('\n')
    for line in lines:
        line_str = line.strip()
        if not line_str:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            continue
            
        if line_str.startswith('### '):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h4>{line_str[4:]}</h4>")
        elif line_str.startswith('## '):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h3>{line_str[3:]}</h3>")
        elif line_str.startswith('# '):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h2>{line_str[2:]}</h2>")
        elif line_str.startswith('- '):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{line_str[2:]}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            # Check for empty header or divider
            if line_str == '---':
                html_lines.append("<hr>")
            else:
                html_lines.append(f"<p>{line_str}</p>")
            
    if in_list:
        html_lines.append("</ul>")
        
    return "\n".join(html_lines)

def parse_eqprint_file(filepath):
    text = Path(filepath).read_text()
    fm, body = parse_frontmatter(text)
    
    # Generate HTML documentation
    explanation_html = markdown_to_html(body)
    
    # Standardize bands dictionary keys
    bands_str_keys = {}
    if 'bands' in fm:
        for k, v in fm['bands'].items():
            bands_str_keys[str(k)] = v
            
    # Standardize bands_7 dictionary keys
    bands_7_str_keys = {}
    if 'bands_7' in fm:
        for k, v in fm['bands_7'].items():
            bands_7_str_keys[str(k)] = v
            
    tags = [t.strip() for t in fm.get('tags', '').split(',') if t.strip()]
    
    return {
        'id': fm.get('id', filepath.stem),
        'title': fm.get('title', filepath.stem.replace('-', ' ').title()),
        'pedal': fm.get('pedal', 'Toneshaper 3000'),
        'pickup_type': fm.get('pickup_type', 'universal'),
        'guitar': fm.get('guitar', 'Universal'),
        'target': fm.get('target', ''),
        'tags': tags,
        'pedal_placement': fm.get('pedal_placement', 'pre-amp'),
        'bands': bands_str_keys,
        'bands_7': bands_7_str_keys,
        'level': fm.get('level', 0.0),
        'explanation_html': explanation_html
    }

def main():
    script_dir = Path(__file__).parent
    tones_dir = script_dir.parent / 'tones'
    eqprints_dir = tones_dir / 'eqprints'
    output_path = script_dir / 'eq-visualizer.html'
    
    if not eqprints_dir.exists():
        print(f"Error: eqprints directory not found at {eqprints_dir}")
        sys.exit(1)
        
    preset_files = sorted(list(eqprints_dir.glob('*.md')))
    preset_files = [f for f in preset_files if f.name != 'INDEX.md']
    
    if not preset_files:
        print(f"No preset files found in {eqprints_dir}")
        sys.exit(0)
        
    presets = [parse_eqprint_file(f) for f in preset_files]
    presets_json = json.dumps(presets, indent=2)
    
    # HTML Template
    html_content = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Toneshaper 3000 — Interactive Graphic EQ Visualizer</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    
    :root {
      --bg:              #0f1115;
      --surface:         #161920;
      --surface-alt:     #1d212b;
      --border:          #2b3140;
      --border-glow:     #3c4559;
      --accent-blue:     #00d2ff;
      --accent-blue-glow:rgba(0, 210, 255, 0.4);
      --accent-red:      #ff3366;
      --accent-red-glow: rgba(255, 51, 102, 0.4);
      --text:            #e3e9f3;
      --secondary:       #94a3b8;
      --muted:           #475569;
      --pedal-chassis-bg:linear-gradient(135deg, #1e2330 0%, #12151d 100%);
      --pedal-border:    #333947;
      --grid-line-color: rgba(255, 255, 255, 0.04);
      --grid-line-zero:  rgba(255, 255, 255, 0.15);
      --fader-track-bg:  #090a0d;
      --knob-bg:         linear-gradient(to bottom, #474f5f 0%, #292e38 100%);
      --knob-border:     #1a1e24;
      --text-white:      #ffffff;
    }

    [data-theme="light"] {
      --bg:              #f1f5f9;
      --surface:         #ffffff;
      --surface-alt:     #f8fafc;
      --border:          #cbd5e1;
      --border-glow:     #94a3b8;
      --accent-blue:     #0284c7;
      --accent-blue-glow:rgba(2, 132, 199, 0.3);
      --accent-red:      #dc2626;
      --accent-red-glow: rgba(220, 38, 38, 0.3);
      --text:            #1e293b;
      --secondary:       #64748b;
      --muted:           #94a3b8;
      --pedal-chassis-bg:linear-gradient(135deg, #272d3d 0%, #1a1e29 100%);
      --pedal-border:    #475569;
    }

    body {
      font-family: 'Inter', -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      font-size: 14px;
      line-height: 1.6;
      height: 100vh;
      overflow: hidden;
      transition: background 0.3s, color 0.3s;
    }

    .app {
      display: flex;
      height: 100vh;
      overflow: hidden;
    }

    /* === SIDEBAR === */
    .sidebar {
      width: 320px;
      min-width: 320px;
      background: var(--surface);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transition: background 0.3s, border-color 0.3s;
    }

    .sidebar-header {
      padding: 24px 20px 16px;
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }

    .wordmark {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }

    .wordmark-left {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .wordmark-logo {
      width: 26px;
      height: 26px;
      background: linear-gradient(135deg, var(--accent-blue), var(--accent-red));
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Outfit', sans-serif;
      font-weight: 900;
      color: #000;
      font-size: 13px;
    }

    .wordmark-title {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 16px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text);
    }

    /* Theme Toggle Button */
    .theme-toggle-btn {
      background: transparent;
      border: 1px solid var(--border);
      color: var(--secondary);
      border-radius: 6px;
      width: 30px;
      height: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
      outline: none;
    }

    .theme-toggle-btn:hover {
      border-color: var(--border-glow);
      color: var(--text);
      background: var(--surface-alt);
    }

    .theme-icon {
      width: 16px;
      height: 16px;
    }

    [data-theme="light"] .theme-icon .sun-path {
      display: none;
    }
    
    [data-theme="dark"] .theme-icon .moon-path {
      display: none;
    }

    .search-box {
      width: 100%;
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px 12px;
      color: var(--text);
      font-size: 13px;
      outline: none;
      transition: border-color 0.2s, background-color 0.3s;
    }

    .search-box:focus {
      border-color: var(--accent-blue);
      background: var(--surface);
    }

    .filter-tabs {
      display: flex;
      gap: 5px;
      padding: 10px 20px;
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }

    .filter-tab {
      flex: 1;
      background: transparent;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 6px 0;
      font-size: 11px;
      font-weight: 600;
      color: var(--secondary);
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: all 0.2s;
    }

    .filter-tab.active {
      background: var(--surface-alt);
      border-color: var(--accent-blue);
      color: var(--accent-blue);
    }

    .preset-list {
      flex: 1;
      overflow-y: auto;
      padding: 12px 10px;
    }}

    .preset-item {
      padding: 12px 14px;
      border-radius: 8px;
      cursor: pointer;
      margin-bottom: 6px;
      border: 1px solid transparent;
      background: transparent;
      transition: all 0.2s;
    }

    .preset-item:hover {
      background: var(--surface-alt);
    }

    .preset-item.active {
      background: rgba(0, 210, 255, 0.06);
      border-color: rgba(0, 210, 255, 0.3);
    }

    [data-theme="light"] .preset-item.active {
      background: rgba(2, 132, 199, 0.08);
      border-color: rgba(2, 132, 199, 0.3);
    }

    .preset-item-title {
      font-size: 14px;
      font-weight: 600;
      color: var(--text);
      margin-bottom: 4px;
    }

    .preset-item.active .preset-item-title {
      color: var(--accent-blue);
    }

    .preset-item-meta {
      font-size: 11px;
      color: var(--secondary);
      display: flex;
      justify-content: space-between;
    }

    .badge {
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .badge-sc { background: rgba(0, 210, 255, 0.15); color: var(--accent-blue); }
    .badge-hb { background: rgba(255, 51, 102, 0.15); color: var(--accent-red); }
    .badge-univ { background: rgba(255, 255, 255, 0.1); color: var(--text); }
    [data-theme="light"] .badge-univ { background: rgba(0, 0, 0, 0.06); }

    /* === MAIN PLATFORM === */
    .main-content {
      flex: 1;
      display: flex;
      overflow: hidden;
    }

    .pedal-area {
      flex: 1.1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 30px;
      background: radial-gradient(circle at center, var(--surface-alt) 0%, var(--bg) 100%);
      border-right: 1px solid var(--border);
      overflow-y: auto;
      transition: background 0.3s, border-color 0.3s;
    }

    .pedal-title-banner {
      margin-bottom: 24px;
      text-align: center;
    }

    .pedal-title-banner h1 {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 24px;
      letter-spacing: 0.05em;
      color: var(--text);
    }

    .pedal-title-banner p {
      font-size: 12px;
      color: var(--secondary);
      letter-spacing: 0.2em;
      text-transform: uppercase;
      margin-top: 4px;
    }

    /* === THE PEDAL MOCKUP === */
    .pedal-chassis {
      width: 680px;
      background: var(--pedal-chassis-bg);
      border: 4px solid var(--pedal-border);
      border-radius: 20px;
      padding: 25px 20px 20px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 40px rgba(0, 210, 255, 0.05);
      position: relative;
      transition: background-image 0.3s, border-color 0.3s;
    }

    .pedal-chassis::after {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      border-radius: 16px;
      border: 1px solid rgba(255, 255, 255, 0.05);
      pointer-events: none;
    }

    .pedal-brand {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      border-bottom: 2px dashed var(--border);
      padding-bottom: 15px;
      transition: border-color 0.3s;
    }

    .pedal-brand-name {
      font-family: 'Outfit', sans-serif;
      font-size: 26px;
      font-weight: 900;
      letter-spacing: 0.12em;
      color: var(--text-white);
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
      text-transform: uppercase;
    }

    .pedal-subbrand {
      font-size: 10px;
      letter-spacing: 0.2em;
      color: var(--secondary);
      text-transform: uppercase;
      margin-top: 2px;
      font-weight: 500;
    }

    /* Mode button group on pedal */
    .mode-switch-group {
      display: flex;
      background: #090a0d;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 6px;
      padding: 2px;
    }

    .mode-switch-btn {
      background: transparent;
      border: 0;
      color: #94a3b8;
      font-size: 10px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: all 0.2s;
    }

    .mode-switch-btn.active {
      background: #272d3d;
      color: var(--accent-blue);
      box-shadow: 0 1px 3px rgba(0,0,0,0.5);
    }

    .sliders-container {
      display: flex;
      justify-content: space-between;
      height: 280px;
      padding: 0 10px;
      position: relative;
    }

    /* Grid lines behind faders */
    .fader-grid {
      position: absolute;
      top: 36px;
      left: 20px;
      right: 20px;
      height: 200px;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .grid-line {
      height: 1px;
      background: var(--grid-line-color);
      position: relative;
    }

    .grid-line.zero-line {
      background: var(--grid-line-zero);
      border-top: 1px dashed rgba(255, 255, 255, 0.15);
    }

    .grid-label {
      position: absolute;
      left: -18px;
      top: -6px;
      font-size: 9px;
      color: var(--muted);
      font-weight: 700;
    }

    .grid-label-right {
      position: absolute;
      right: -18px;
      top: -6px;
      font-size: 9px;
      color: var(--muted);
      font-weight: 700;
    }

    .slider-column {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      height: 100%;
      position: relative;
      z-index: 2;
    }

    .slider-freq {
      font-family: 'Outfit', sans-serif;
      font-size: 10px;
      font-weight: 700;
      color: var(--secondary);
      margin-top: auto;
      text-align: center;
      height: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .slider-value {
      font-size: 11px;
      font-weight: 700;
      color: var(--muted);
      margin-bottom: 6px;
      height: 14px;
      text-align: center;
    }

    .slider-value.active-val {
      font-size: 13px;
      font-weight: 800;
      color: var(--accent-blue);
      text-shadow: 0 0 5px var(--accent-blue-glow);
    }

    .slider-column-level .slider-value.active-val {
      font-size: 13px;
      font-weight: 800;
      color: var(--accent-red);
      text-shadow: 0 0 5px var(--accent-red-glow);
    }

    /* Slider track & fader body */
    .fader-track-wrapper {
      height: 234px;
      width: 100%;
      display: flex;
      justify-content: center;
      position: relative;
      cursor: ns-resize;
    }

    .fader-track {
      width: 6px;
      height: 200px;
      background: var(--fader-track-bg);
      border-radius: 3px;
      position: absolute;
      top: 10px;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.8);
      border: 1px solid rgba(255,255,255,0.05);
    }

    .fader-knob {
      width: 24px;
      height: 34px;
      background: var(--knob-bg);
      border: 2px solid var(--knob-border);
      border-radius: 4px;
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: 107px;
      box-shadow: 0 5px 10px rgba(0,0,0,0.6), inset 0 1px 1px rgba(255,255,255,0.2);
      cursor: grab;
      user-select: none;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: bottom 0.05s ease-out;
    }

    .fader-knob:active {
      cursor: grabbing;
    }

    /* LED indicator on knob */
    .fader-led {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #333;
      box-shadow: 0 0 2px rgba(0,0,0,0.5);
      transition: all 0.2s;
    }

    /* Glowing LED states */
    .slider-column-level .fader-led.lit {
      background: var(--accent-red);
      box-shadow: 0 0 8px var(--accent-red), 0 0 15px var(--accent-red);
    }

    .fader-led.lit {
      background: var(--accent-blue);
      box-shadow: 0 0 8px var(--accent-blue), 0 0 15px var(--accent-blue);
    }

    /* Split level column */
    .slider-column-level {
      border-right: 1px dashed var(--border);
      padding-right: 8px;
      flex: 0 0 54px;
      transition: border-color 0.3s;
    }

    .slider-column-level .slider-freq {
      color: var(--accent-red);
    }

    /* Controls beneath pedal */
    .pedal-controls {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 24px;
      padding: 0 10px;
    }

    .placement-info-tag {
      font-size: 11px;
      font-weight: 700;
      color: var(--secondary);
      background: var(--surface-alt);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background 0.3s, border-color 0.3s;
    }

    .placement-indicator {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--muted);
    }

    .placement-pre { background: var(--accent-blue); box-shadow: 0 0 8px var(--accent-blue); }
    .placement-post { background: var(--accent-red); box-shadow: 0 0 8px var(--accent-red); }

    .btn-group {
      display: flex;
      gap: 10px;
    }

    .pedal-btn {
      background: var(--surface-alt);
      border: 1px solid var(--border);
      color: var(--text);
      font-weight: 600;
      font-size: 12px;
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s, background-color 0.3s, border-color 0.3s;
    }

    .pedal-btn:hover {
      border-color: var(--border-glow);
      background: var(--surface);
    }

    .pedal-btn-reset {
      color: var(--accent-red);
    }

    .pedal-btn-reset:hover {
      border-color: rgba(255, 51, 102, 0.4);
      background: rgba(255, 51, 102, 0.05);
    }

    /* === INFO & CURVE PANEL === */
    .info-panel {
      flex: 0.9;
      background: var(--surface);
      border-left: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transition: background 0.3s, border-color 0.3s;
    }

    .panel-section {
      padding: 24px;
      border-bottom: 1px solid var(--border);
      transition: border-color 0.3s;
    }

    .panel-section-title {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--secondary);
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* === THE GRAPH === */
    .graph-container {
      width: 100%;
      height: 160px;
      background: #090a0d;
      border: 1px solid var(--border);
      border-radius: 10px;
      position: relative;
      overflow: hidden;
      transition: border-color 0.3s;
    }

    .graph-svg {
      width: 100%;
      height: 100%;
    }

    .graph-grid-line {
      stroke: rgba(255, 255, 255, 0.05);
      stroke-width: 1;
    }

    .graph-grid-line-zero {
      stroke: rgba(255, 255, 255, 0.2);
      stroke-width: 1;
      stroke-dasharray: 4 4;
    }

    .graph-curve {
      stroke: url(#curve-gradient);
      stroke-width: 3;
      fill: none;
      filter: drop-shadow(0 0 4px var(--accent-blue-glow));
    }

    .graph-point {
      fill: var(--accent-blue);
      stroke: #090a0d;
      stroke-width: 2;
      r: 4;
      transition: cy 0.05s ease-out;
    }

    /* === LIVE ANALYZER === */
    .analyzer-text-box {
      background: var(--surface-alt);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      font-size: 13px;
      min-height: 80px;
      border-left: 3px solid var(--accent-blue);
      transition: background 0.3s, border-color 0.3s;
    }

    /* === PRESET EXPLANATION === */
    .explanation-area {
      flex: 1;
      overflow-y: auto;
      padding: 24px;
    }

    .explanation-body h2, .explanation-body h3 {
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      color: var(--text);
      margin-top: 20px;
      margin-bottom: 8px;
    }

    .explanation-body h2:first-child {
      margin-top: 0;
    }

    .explanation-body p {
      margin-bottom: 12px;
      font-size: 13px;
      color: var(--secondary);
    }

    [data-theme="dark"] .explanation-body p {
      color: #cbd5e1;
    }

    .explanation-body ul {
      margin-left: 20px;
      margin-bottom: 14px;
    }

    .explanation-body li {
      margin-bottom: 6px;
      font-size: 13px;
      color: var(--secondary);
    }

    [data-theme="dark"] .explanation-body li {
      color: #cbd5e1;
    }

    .explanation-body strong {
      color: var(--text);
    }

    .explanation-body hr {
      border: 0;
      border-top: 1px solid var(--border);
      margin: 18px 0;
    }

    /* Modal dialog */
    .export-modal {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.8);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 100;
      padding: 20px;
    }

    .modal-content {
      background: var(--surface);
      border: 1px solid var(--border-glow);
      border-radius: 12px;
      width: 500px;
      max-width: 100%;
      padding: 24px;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5);
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }

    .modal-header h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 16px;
      font-weight: 700;
    }

    .close-modal-btn {
      background: transparent;
      border: 0;
      color: var(--secondary);
      cursor: pointer;
      font-size: 18px;
    }

    .code-textarea {
      width: 100%;
      height: 220px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      font-family: 'Courier New', Courier, monospace;
      font-size: 12px;
      color: #818cf8;
      padding: 12px;
      resize: none;
      outline: none;
      margin-bottom: 16px;
    }

    .copy-btn {
      background: var(--accent-blue);
      color: #000;
      border: 0;
      font-weight: 700;
      font-size: 13px;
      padding: 10px 20px;
      border-radius: 6px;
      cursor: pointer;
      width: 100%;
      transition: background 0.2s;
    }

    .copy-btn:hover {
      background: #00b8e6;
    }

    .no-preset-message {
      color: var(--muted);
      font-style: italic;
      text-align: center;
      padding-top: 40px;
    }
  </style>
</head>
<body>
  <div class="app">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="sidebar-header">
        <div class="wordmark">
          <div class="wordmark-left">
            <div class="wordmark-logo">TS</div>
            <div class="wordmark-title">Toneshaper Vault</div>
          </div>
          <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" title="Toggle Light/Dark Theme">
            <svg class="theme-icon" viewBox="0 0 24 24" fill="currentColor">
              <path class="sun-path" d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41l-1.06-1.06zm1.06-12.37c-.39-.39-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06c.39-.39.39-1.03 0-1.41zm-12.37 12.37c-.39-.39-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06c.39-.39.39-1.03 0-1.41z"/>
              <path class="moon-path" d="M12.3 22h-.1c-5.5 0-10-4.5-10-10 0-4.8 3.5-8.9 8.2-9.8.5-.1 1 .2 1.2.7.2.5 0 1.1-.4 1.4-2.8 1.9-4.3 5.3-3.7 8.7.6 3.5 3.4 6.3 6.9 6.9 3.4.6 6.8-.9 8.7-3.7.3-.4.9-.6 1.4-.4.5.2.8.7.7 1.2-.9 4.7-5 8.2-9.8 8.2z"/>
            </svg>
          </button>
        </div>
        <input type="text" class="search-box" id="searchBox" placeholder="Describe tone or search (e.g. 'warm jazz')...">
      </div>
      <div class="filter-tabs">
        <button class="filter-tab active" data-filter="all">All</button>
        <button class="filter-tab" data-filter="single-coil">Single-Coil</button>
        <button class="filter-tab" data-filter="humbucker">Humbucker</button>
      </div>
      <div class="preset-list" id="presetList">
        <!-- Presets populated by JS -->
      </div>
    </div>

    <!-- Main Content Area -->
    <div class="main-content">
      <!-- Pedal chassis area -->
      <div class="pedal-area">
        <div class="pedal-title-banner">
          <h1 id="activePresetTitle">Manual Mode</h1>
          <p id="activePresetGuitar">Toneshaper 3000 Graphic Equalizer</p>
        </div>

        <div class="pedal-chassis">
          <div class="pedal-brand">
            <div>
              <div class="pedal-brand-name">Toneshaper 3000</div>
              <div class="pedal-subbrand" id="pedalSubbrandName">10 Band Spectral Equalizer</div>
            </div>
            
            <div class="mode-switch-group">
              <button class="mode-switch-btn active" id="modeBtn-10" onclick="setPedalMode('10-band')">10-Band</button>
              <button class="mode-switch-btn" id="modeBtn-7" onclick="setPedalMode('7-band')">7-Band</button>
            </div>
          </div>

          <!-- Slider chassis will be populated dynamically -->
          <div class="sliders-container" id="slidersContainer">
            <!-- Populated dynamically by JS -->
          </div>

          <!-- Footer of pedal -->
          <div class="pedal-controls">
            <div class="placement-info-tag">
              <span class="placement-indicator" id="placementIndicator"></span>
              <span id="placementText">Placement: Pre-Amp</span>
            </div>
            <div class="btn-group">
              <button class="pedal-btn pedal-btn-reset" onclick="flattenEQ()">Flatten EQ</button>
              <button class="pedal-btn" onclick="openExportModal('yaml')">Export YAML</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Info and Visualizer Panel -->
      <div class="info-panel">
        <div class="panel-section">
          <div class="panel-section-title">Frequency Curve</div>
          <div class="graph-container">
            <svg class="graph-svg" id="graphSvg" viewBox="0 0 400 160">
              <defs>
                <linearGradient id="curve-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#3b82f6" />
                  <stop offset="50%" stop-color="#10b981" />
                  <stop offset="100%" stop-color="#ef4444" />
                </linearGradient>
              </defs>
              <!-- Horizontal grid lines -->
              <line class="graph-grid-line" x1="0" y1="20" x2="400" y2="20" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
              <line class="graph-grid-line" x1="0" y1="50" x2="400" y2="50" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
              <line class="graph-grid-line-zero" x1="0" y1="80" x2="400" y2="80" stroke="rgba(255,255,255,0.2)" stroke-width="1" stroke-dasharray="4 4" />
              <line class="graph-grid-line" x1="0" y1="110" x2="400" y2="110" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
              <line class="graph-grid-line" x1="0" y1="140" x2="400" y2="140" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
              
              <!-- Smooth spline curve -->
              <path class="graph-curve" id="responseCurve" d="M 0 80 L 400 80" />
              
              <!-- Frequency points (added dynamically by JS) -->
            </svg>
          </div>
        </div>

        <div class="panel-section" style="border-bottom: none; padding-bottom: 12px;">
          <div class="panel-section-title">Live Tone Analyzer</div>
          <div class="analyzer-text-box" id="analyzerTextBox">
            Flat EQ setting. Natural guitar signal with no coloration.
          </div>
        </div>

        <div class="explanation-area" id="explanationArea">
          <div class="explanation-body" id="explanationBody">
            <!-- Custom explanation body -->
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- EXPORT MODAL -->
  <div class="export-modal" id="exportModal">
    <div class="modal-content">
      <div class="modal-header">
        <h3 id="modalTitle">Export Configuration</h3>
        <button class="close-modal-btn" onclick="closeModal()">&times;</button>
      </div>
      <textarea class="code-textarea" id="exportCodeText" readonly></textarea>
      <button class="copy-btn" onclick="copyModalCode()">Copy to Clipboard</button>
    </div>
  </div>

  <script>
    // Embedded Presets Data
    const PRESETS = __PRESETS_JSON__;

    // Mode mappings
    const MODES = {
      '10-band': {
        name: 'Toneshaper 10-Band (Spectral Shaper)',
        subbrand: '10 Band Spectral Equalizer',
        bands: ["31.25", "62.5", "125", "250", "500", "1000", "2000", "4000", "8000", "16000"],
        labels: ["31.25", "62.5", "125", "250", "500", "1K", "2K", "4K", "8K", "16K"]
      },
      '7-band': {
        name: 'Toneshaper 7-Band (Classic GE-7 / EQ700)',
        subbrand: '7 Band Classic Equalizer',
        bands: ["100", "200", "400", "800", "1600", "3200", "6400"],
        labels: ["100", "200", "400", "800", "1.6K", "3.2K", "6.4K"]
      }
    };
    
    // UI state
    let activePresetId = null;
    let currentFilter = 'all';
    let currentMode = '10-band';
    
    // EQ database storing the levels for ALL bands of both modes
    const eq = {
      level: 0.0,
      // 10-band bands
      "31.25": 0.0,
      "62.5": 0.0,
      "125": 0.0,
      "250": 0.0,
      "500": 0.0,
      "1000": 0.0,
      "2000": 0.0,
      "4000": 0.0,
      "8000": 0.0,
      "16000": 0.0,
      // 7-band bands
      "100": 0.0,
      "200": 0.0,
      "400": 0.0,
      "800": 0.0,
      "1600": 0.0,
      "3200": 0.0,
      "6400": 0.0
    };
    
    // Dragging state
    let isDragging = false;
    let activeBand = null;
    let dragStartMouseY = 0;
    let dragStartBottomPx = 0;
    
    // Constants
    const MAX_DB = 12.0;
    const MIN_DB = -12.0;
    
    // Initialize
    window.addEventListener('DOMContentLoaded', () => {
      // Load saved theme
      const savedTheme = localStorage.getItem('theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      
      setupPresetsList();
      setPedalMode('10-band'); // Builds faders and initializes graph
      loadManualExplanation();
    });

    function toggleTheme() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }

    function setPedalMode(mode) {
      currentMode = mode;
      
      // Update toggle buttons active state
      document.getElementById('modeBtn-10').classList.toggle('active', mode === '10-band');
      document.getElementById('modeBtn-7').classList.toggle('active', mode === '7-band');
      
      // Update subbrand title on chassis
      document.getElementById('pedalSubbrandName').textContent = MODES[mode].subbrand;
      
      // Render components
      renderFaders();
      renderGraphPoints();
      
      // If we have a preset active, make sure its guitar text displays the active mode's pedal name
      if (activePresetId !== null) {
        const p = PRESETS.find(x => x.id === activePresetId);
        if (p) {
          document.getElementById('activePresetGuitar').textContent = p.guitar + " — " + MODES[mode].name;
        }
      } else {
        document.getElementById('activePresetGuitar').textContent = MODES[mode].name;
      }
      
      updateUI();
    }

    function renderFaders() {
      const container = document.getElementById('slidersContainer');
      const modeInfo = MODES[currentMode];
      
      let html = `
        <!-- Grid lines in background -->
        <div class="fader-grid">
          <div class="grid-line"><span class="grid-label">+12 dB</span><span class="grid-label-right">+12 dB</span></div>
          <div class="grid-line"><span class="grid-label">+6 dB</span><span class="grid-label-right">+6 dB</span></div>
          <div class="grid-line zero-line"><span class="grid-label">0 dB</span><span class="grid-label-right">0 dB</span></div>
          <div class="grid-line"><span class="grid-label">-6 dB</span><span class="grid-label-right">-6 dB</span></div>
          <div class="grid-line"><span class="grid-label">-12 dB</span><span class="grid-label-right">-12 dB</span></div>
        </div>
      `;
      
      // Render LEVEL slider
      html += `
        <div class="slider-column slider-column-level" id="slider-col-level">
          <div class="slider-value" id="val-level">0.0</div>
          <div class="fader-track-wrapper" data-band="level">
            <div class="fader-track"></div>
            <div class="fader-knob" id="knob-level">
              <div class="fader-led lit" id="led-level"></div>
            </div>
          </div>
          <div class="slider-freq">LEVEL</div>
        </div>
      `;
      
      // Render Mode-specific frequency sliders
      modeInfo.bands.forEach((b, idx) => {
        const label = modeInfo.labels[idx];
        const cleanId = getBandSelectorId(b);
        html += `
          <div class="slider-column" id="slider-col-${cleanId}">
            <div class="slider-value" id="val-${cleanId}">0.0</div>
            <div class="fader-track-wrapper" data-band="${b}">
              <div class="fader-track"></div>
              <div class="fader-knob" id="knob-${cleanId}">
                <div class="fader-led" id="led-${cleanId}"></div>
              </div>
            </div>
            <div class="slider-freq">${label}</div>
          </div>
        `;
      });
      
      container.innerHTML = html;
      setupSliderDragHandlers();
    }

    function renderGraphPoints() {
      const svg = document.getElementById('graphSvg');
      // Clear old points
      document.querySelectorAll('.graph-point').forEach(el => el.remove());
      
      const modeInfo = MODES[currentMode];
      const count = modeInfo.bands.length;
      
      // Evenly distribute from X=40px to X=360px
      const startX = 40;
      const endX = 360;
      const rangeX = endX - startX;
      const stepX = count > 1 ? rangeX / (count - 1) : 0;
      
      modeInfo.bands.forEach((b, idx) => {
        const x = startX + idx * stepX;
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('class', 'graph-point');
        circle.setAttribute('id', `gp-${getBandSelectorId(b)}`);
        circle.setAttribute('cx', x);
        circle.setAttribute('cy', 80);
        svg.appendChild(circle);
      });
    }

    function setupPresetsList() {
      const listEl = document.getElementById('presetList');
      listEl.innerHTML = '';
      
      const filtered = PRESETS.filter(p => {
        if (currentFilter === 'all') return true;
        return p.pickup_type === currentFilter;
      });
      
      if (filtered.length === 0) {
        listEl.innerHTML = '<div class="no-preset-message">No matching presets.</div>';
        return;
      }
      
      filtered.forEach(p => {
        const item = document.createElement('div');
        item.className = `preset-item ${activePresetId === p.id ? 'active' : ''}`;
        item.onclick = () => loadPreset(p.id);
        
        let badgeClass = 'badge-univ';
        let badgeText = 'Universal';
        if (p.pickup_type === 'single-coil') {
          badgeClass = 'badge-sc';
          badgeText = 'Single-Coil';
        } else if (p.pickup_type === 'humbucker') {
          badgeClass = 'badge-hb';
          badgeText = 'Humbucker';
        }
        
        item.innerHTML = `
          <div class="preset-item-title">${p.title}</div>
          <div class="preset-item-meta">
            <span>${p.guitar.split(' (')[0]}</span>
            <span class="badge ${badgeClass}">${badgeText}</span>
          </div>
        `;
        listEl.appendChild(item);
      });
    }

    function loadPreset(id) {
      activePresetId = id;
      const p = PRESETS.find(x => x.id === id);
      if (!p) return;
      
      // Load level fader
      eq.level = p.level;
      
      // Load 10-band levels
      MODES['10-band'].bands.forEach(b => {
        eq[b] = p.bands[b] !== undefined ? p.bands[b] : 0.0;
      });
      
      // Load 7-band levels
      MODES['7-band'].bands.forEach(b => {
        eq[b] = p.bands_7[b] !== undefined ? p.bands_7[b] : 0.0;
      });
      
      // Update UI title, tags, description
      document.getElementById('activePresetTitle').textContent = p.title;
      document.getElementById('activePresetGuitar').textContent = p.guitar + " — " + MODES[currentMode].name;
      
      // Update placement tag
      const placementInd = document.getElementById('placementIndicator');
      const placementText = document.getElementById('placementText');
      placementInd.className = "placement-indicator";
      if (p.pedal_placement === 'pre-amp') {
        placementInd.classList.add('placement-pre');
        placementText.textContent = "Placement: Pre-Amp (Shape Pickups)";
      } else {
        placementInd.classList.add('placement-post');
        placementText.textContent = "Placement: Post-Amp / Loop (Master EQ)";
      }
      
      // Load explanation text
      document.getElementById('explanationBody').innerHTML = p.explanation_html;
      
      // Highlight sidebar item
      document.querySelectorAll('.preset-item').forEach(el => el.classList.remove('active'));
      setupPresetsList();
      
      updateUI();
    }

    function loadManualExplanation() {
      document.getElementById('explanationBody').innerHTML = `
        <h2 style="font-size: 16px; margin-bottom: 12px;">Manual Toneshapping Vault</h2>
        <p>You are in Manual mode. Move any slider on the physical pedal to sculpt your guitar's frequency response.</p>
        <p><strong>Frequency Guide for Guitarists:</strong></p>
        <ul style="margin-top: 8px;">
          <li><strong>Bass frequencies (31.25Hz - 100Hz):</strong> Low-end rumble. Cut to prevent speaker mud and clarify chord shapes.</li>
          <li><strong>Lower Midrange (125Hz - 400Hz):</strong> Woody body warmth. Cut slightly to remove electric humbucker boxiness.</li>
          <li><strong>Midrange (500Hz - 800Hz):</strong> Mid body. Dip for modern scooped clean tone; boost for drive body.</li>
          <li><strong>High Midrange (1kHz - 1.6kHz):</strong> Projecting vocal range. Boost here to make solos cut through.</li>
          <li><strong>Treble Presence (2kHz - 3.2kHz):</strong> Attack bite. Boost for single-coil glassiness, cut to soften pick attack.</li>
          <li><strong>Brilliance & Air (4kHz - 16KHz):</strong> Chime or fizz. Cut to act as a speaker veil for smooth, dark jazz tones.</li>
        </ul>
      `;
    }

    function flattenEQ() {
      activePresetId = null;
      document.getElementById('activePresetTitle').textContent = "Manual Mode";
      document.getElementById('activePresetGuitar').textContent = MODES[currentMode].name;
      loadManualExplanation();
      
      eq.level = 0.0;
      MODES['10-band'].bands.forEach(b => eq[b] = 0.0);
      MODES['7-band'].bands.forEach(b => eq[b] = 0.0);
      
      // Reset placement tag
      const placementInd = document.getElementById('placementIndicator');
      placementInd.className = "placement-indicator";
      document.getElementById('placementText').textContent = "Placement: Pre-Amp";
      
      document.querySelectorAll('.preset-item').forEach(el => el.classList.remove('active'));
      updateUI();
    }

    function setupSliderDragHandlers() {
      document.querySelectorAll('.fader-track-wrapper').forEach(wrapper => {
        const band = wrapper.getAttribute('data-band');
        const cleanId = getBandSelectorId(band);
        const knob = wrapper.querySelector('.fader-knob');
        const led = wrapper.querySelector('.fader-led');
        
        wrapper.addEventListener('mousedown', (e) => {
          isDragging = true;
          activeBand = band;
          dragStartMouseY = e.clientY;
          
          const styleBottom = knob.style.bottom || '107px';
          dragStartBottomPx = parseFloat(styleBottom);
          
          led.classList.add('lit');
          e.preventDefault();
        });
        
        wrapper.addEventListener('dblclick', () => {
          eq[band] = 0.0;
          activePresetId = null;
          document.getElementById('activePresetTitle').textContent = "Manual Mode";
          updateUI();
        });
      });
    }
    
    window.addEventListener('mousemove', (e) => {
      if (!isDragging || !activeBand) return;
      
      const wrapper = document.querySelector(`.fader-track-wrapper[data-band="${activeBand}"]`);
      if (!wrapper) return;
      
      const deltaY = dragStartMouseY - e.clientY;
      let newBottomPx = dragStartBottomPx + deltaY;
      
      newBottomPx = Math.max(7, Math.min(207, newBottomPx));
      
      const percent = (newBottomPx - 7) / 200;
      let db = MIN_DB + percent * (MAX_DB - MIN_DB);
      
      db = Math.round(db * 2) / 2; // snap to 0.5dB
      
      eq[activeBand] = db;
      
      if (activePresetId !== null) {
        activePresetId = null;
        document.getElementById('activePresetTitle').textContent = "Manual Mode";
      }
      
      updateUI();
    });
    
    window.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        activeBand = null;
      }
    });

    function updateUI() {
      // Update sliders
      updateSliderUI('level', eq.level);
      
      const modeInfo = MODES[currentMode];
      modeInfo.bands.forEach(b => {
        updateSliderUI(b, eq[b] || 0.0);
      });
      
      // Replot SVG Curve
      drawCurve();
      
      // Run sound analysis
      analyzeTone();
    }

    function updateSliderUI(band, val) {
      const isLevel = band === 'level';
      const cleanId = getBandSelectorId(band);
      const valEl = document.getElementById(isLevel ? 'val-level' : `val-${cleanId}`);
      const knobEl = document.getElementById(isLevel ? 'knob-level' : `knob-${cleanId}`);
      const ledEl = document.getElementById(isLevel ? 'led-level' : `led-${cleanId}`);
      
      if (!valEl || !knobEl) return;
      
      valEl.textContent = (val > 0 ? "+" : "") + val.toFixed(1);
      if (val === 0.0) {
        valEl.className = "slider-value";
        if (!isLevel) ledEl.classList.remove('lit');
      } else {
        valEl.className = "slider-value active-val";
        ledEl.classList.add('lit');
      }
      
      const percent = (val - MIN_DB) / (MAX_DB - MIN_DB);
      const bottomPx = 7 + percent * 200;
      knobEl.style.bottom = `${bottomPx}px`;
    }
    
    function getBandSelectorId(band) {
      if (band === "31.25") return "31";
      if (band === "62.5") return "62";
      if (band === "1000") return "1k";
      if (band === "2000") return "2k";
      if (band === "4000") return "4k";
      if (band === "8000") return "8k";
      if (band === "16000") return "16k";
      // 7-band specific keys
      if (band === "100") return "100";
      if (band === "200") return "200";
      if (band === "400") return "400";
      if (band === "800") return "800";
      if (band === "1600") return "1600";
      if (band === "3200") return "3200";
      if (band === "6400") return "6400";
      return band;
    }

    function drawCurve() {
      const svgW = 400;
      const zeroY = 80;
      const pixelsPerDb = 60 / 12.0;
      
      const modeInfo = MODES[currentMode];
      const count = modeInfo.bands.length;
      const startX = 40;
      const endX = 360;
      const rangeX = endX - startX;
      const stepX = count > 1 ? rangeX / (count - 1) : 0;
      
      const points = modeInfo.bands.map((b, idx) => {
        const x = startX + idx * stepX;
        const db = eq[b] || 0.0;
        const y = zeroY - db * pixelsPerDb;
        
        const circle = document.getElementById(`gp-${getBandSelectorId(b)}`);
        if (circle) circle.setAttribute('cy', y);
        
        return { x, y };
      });
      
      const anchoredPoints = [
        { x: 0, y: points[0].y },
        ...points,
        { x: svgW, y: points[points.length-1].y }
      ];
      
      const curveEl = document.getElementById('responseCurve');
      if (curveEl) {
        curveEl.setAttribute('d', getSplinePath(anchoredPoints));
      }
    }

    function getSplinePath(points) {
      if (points.length < 2) return '';
      let d = `M ${points[0].x} ${points[0].y}`;
      
      for (let i = 0; i < points.length - 1; i++) {
        const p0 = points[i];
        const p1 = points[i+1];
        
        let cp1x = p0.x + (p1.x - p0.x) / 3;
        let cp1y = p0.y;
        let cp2x = p0.x + 2 * (p1.x - p0.x) / 3;
        let cp2y = p1.y;
        
        if (i > 0) {
          const pK = points[i-1];
          cp1y = p0.y + (p1.y - pK.y) / 6;
        }
        if (i < points.length - 2) {
          const pN = points[i+2];
          cp2y = p1.y - (pN.y - p0.y) / 6;
        }
        
        d += ` C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${p1.x} ${p1.y}`;
      }
      return d;
    }

    function analyzeTone() {
      const textEl = document.getElementById('analyzerTextBox');
      let lowVal, lowMidVal, midVal, presVal, highVal;
      
      if (currentMode === '10-band') {
        lowVal = (eq["31.25"] + eq["62.5"]) / 2;
        lowMidVal = (eq["125"] + eq["250"]) / 2;
        midVal = (eq["500"] + eq["1000"]) / 2;
        presVal = (eq["2000"] + eq["4000"]) / 2;
        highVal = (eq["8000"] + eq["16000"]) / 2;
      } else {
        lowVal = eq["100"] || 0.0;
        lowMidVal = (eq["200"] + eq["400"]) / 2;
        midVal = eq["800"] || 0.0;
        presVal = (eq["1600"] + eq["3200"]) / 2;
        highVal = eq["6400"] || 0.0;
      }
      
      let segments = [];
      
      // 1. Low end
      if (lowVal <= -6) {
        segments.push("Low-end is heavily filtered and tight, stripping sub-bass rumble.");
      } else if (lowVal < -2) {
        segments.push("Sub-bass is attenuated to reduce cabinet boom.");
      } else if (lowVal >= 3) {
        segments.push("Low-end is boosted, adding heavy, resonant cabinet rumble.");
      } else {
        segments.push("Low-end remains relatively transparent.");
      }
      
      // 2. Warmth / Humbucker Boxiness
      if (lowMidVal <= -3) {
        segments.push("Low-mid frequency dip clears humbucker boxiness/mud and increases note clarity.");
      } else if (lowMidVal >= 2) {
        segments.push("Boosted low-mids add vintage warmth, woodiness, and body to the notes.");
      }
      
      // 3. Midrange scoop
      if (midVal <= -4) {
        segments.push("Midrange is deeply scooped, producing a glassy, acoustic-like, or high-headroom clean voice.");
      } else if (midVal <= -1.5) {
        segments.push("Gentle mid scoop leaves room in the pocket for vocals or spatial reverb decay.");
      } else if (midVal >= 3) {
        segments.push("Midrange hump gives vocal, punchy projection, driving the front-end of the amp for solos.");
      }
      
      // 4. Presence / Articulation
      if (presVal >= 2.5) {
        segments.push("Presence is pushed to highlight pick attack and add glassy definition.");
      } else if (presVal <= -3) {
        segments.push("Presence is recessed, smoothing string attack and softening transients.");
      }
      
      // 5. Air / Treble fizz
      if (highVal <= -6) {
        segments.push("High treble is rolled off sharply, acting as a low-pass filter to deliver a warm, dark jazz-box feel.");
      } else if (highVal >= 3) {
        segments.push("High treble is boosted, adding sparkling clarity and shimmer.");
      }
      
      const activeBandsList = MODES[currentMode].bands;
      const isFlat = activeBandsList.every(b => eq[b] === 0.0) && eq.level === 0.0;
      
      if (isFlat) {
        textEl.textContent = `Flat EQ setting. Guitar signal passes through the ${currentMode === '10-band' ? '10-band' : '7-band'} matrix cleanly with no equalization active.`;
        textEl.style.borderLeftColor = "var(--muted)";
      } else {
        textEl.textContent = segments.join(" ") + (eq.level !== 0 ? ` Master Level trim: ${eq.level > 0 ? "+" : ""}${eq.level}dB.` : "");
        textEl.style.borderLeftColor = "var(--accent-blue)";
      }
    }

    function setupSearchAndFilters() {
      const searchBox = document.getElementById('searchBox');
      const tabs = document.querySelectorAll('.filter-tab');
      
      searchBox.addEventListener('input', () => filterPresets());
      
      tabs.forEach(tab => {
        tab.addEventListener('click', () => {
          tabs.forEach(t => t.classList.remove('active'));
          tab.classList.add('active');
          currentFilter = tab.getAttribute('data-filter');
          filterPresets();
        });
      });
    }

    function filterPresets() {
      const query = document.getElementById('searchBox').value.toLowerCase().trim();
      const listEl = document.getElementById('presetList');
      listEl.innerHTML = '';
      
      let matchedIds = new Set();
      if (query.length > 0) {
        if (query.includes("jazz") || query.includes("warm") || query.includes("dark") || query.includes("bickert")) {
          matchedIds.add("tele-jazz-bickert");
          matchedIds.add("sheraton-velvet-jazz");
        }
        if (query.includes("humbucker") || query.includes("boom") || query.includes("mud") || query.includes("sheraton")) {
          matchedIds.add("sheraton-velvet-jazz");
          matchedIds.add("mid-hump-lead-boost");
        }
        if (query.includes("quack") || query.includes("strat") || query.includes("glass") || query.includes("funk")) {
          matchedIds.add("strat-quack-enhancer");
          matchedIds.add("acoustic-piezo-sim");
        }
        if (query.includes("acoustic") || query.includes("piezo") || query.includes("sparkle")) {
          matchedIds.add("acoustic-piezo-sim");
          matchedIds.add("ambient-bath-scoop");
        }
        if (query.includes("boost") || query.includes("drive") || query.includes("screamer") || query.includes("lead") || query.includes("solo")) {
          matchedIds.add("mid-hump-lead-boost");
        }
        if (query.includes("ambient") || query.includes("bath") || query.includes("shimmer") || query.includes("reverb") || query.includes("decay")) {
          matchedIds.add("ambient-bath-scoop");
        }
      }
      
      const filtered = PRESETS.filter(p => {
        if (currentFilter !== 'all' && p.pickup_type !== currentFilter) return false;
        if (query.length === 0) return true;
        
        const textMatch = p.title.toLowerCase().includes(query) || 
                          p.guitar.toLowerCase().includes(query) || 
                          p.target.toLowerCase().includes(query) ||
                          p.tags.some(t => t.toLowerCase().includes(query));
                          
        return textMatch || matchedIds.has(p.id);
      });
      
      if (filtered.length === 0) {
        listEl.innerHTML = '<div class="no-preset-message">No matching presets.</div>';
        return;
      }
      
      filtered.forEach(p => {
        const item = document.createElement('div');
        item.className = `preset-item ${activePresetId === p.id ? 'active' : ''}`;
        item.onclick = () => loadPreset(p.id);
        
        let badgeClass = 'badge-univ';
        let badgeText = 'Universal';
        if (p.pickup_type === 'single-coil') {
          badgeClass = 'badge-sc';
          badgeText = 'Single-Coil';
        } else if (p.pickup_type === 'humbucker') {
          badgeClass = 'badge-hb';
          badgeText = 'Humbucker';
        }
        
        item.innerHTML = `
          <div class="preset-item-title">${p.title}</div>
          <div class="preset-item-meta">
            <span>${p.guitar.split(' (')[0]}</span>
            <span class="badge ${badgeClass}">${badgeText}</span>
          </div>
        `;
        listEl.appendChild(item);
      });
    }

    function openExportModal(format) {
      const modal = document.getElementById('exportModal');
      const textarea = document.getElementById('exportCodeText');
      const title = document.getElementById('modalTitle');
      
      title.textContent = "Export EQprint YAML Frontmatter";
      
      let presetData = "";
      if (currentMode === '10-band') {
        let bandsYaml = "  bands:\\n";
        MODES['10-band'].bands.forEach(b => {
          bandsYaml += `    ${b}: ${(eq[b] || 0.0).toFixed(1)}\\n`;
        });
        presetData = `# Copy this block into your Toneprint markdown frontmatter (10-Band):
preset_data:
  toneshaper_eq:
    mode: 10-band
    level: ${eq.level.toFixed(1)}
${bandsYaml}`;
      } else {
        let bandsYaml = "  bands_7:\\n";
        MODES['7-band'].bands.forEach(b => {
          bandsYaml += `    ${b}: ${(eq[b] || 0.0).toFixed(1)}\\n`;
        });
        presetData = `# Copy this block into your Toneprint markdown frontmatter (Classic 7-Band):
preset_data:
  toneshaper_eq:
    mode: 7-band
    level: ${eq.level.toFixed(1)}
${bandsYaml}`;
      }

      textarea.value = presetData;
      modal.style.display = "flex";
    }

    function closeModal() {
      document.getElementById('exportModal').style.display = "none";
    }

    function copyModalCode() {
      const textarea = document.getElementById('exportCodeText');
      textarea.select();
      document.execCommand('copy');
      alert("EQprint YAML copied to clipboard!");
      closeModal();
    }
  </script>
</body>
</html>
"""
    
    # Inject JSON and write output
    output_content = html_content.replace('__PRESETS_JSON__', presets_json)
    output_path.write_text(output_content)
    print(f"Generated visualizer page at: {output_path}")

if __name__ == '__main__':
    main()
