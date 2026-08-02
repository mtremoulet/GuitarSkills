#!/usr/bin/env python3
"""
generate_dual_tone_viewer.py

Dedicated HTML Vault Viewer Builder for Dual-Amp Parallel Rigs.
Reads dual-amp toneprints from tones/*.md (files with dual_rig: true or amp_a/amp_b)
and outputs a self-contained dual-tone-viewer.html.

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

TONES_DIR = Path("/Users/miketremoulet/claude-projects/GuitarSkills/tones")
OUTPUT_HTML = Path("/Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/dual-tone-viewer.html")


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


def load_dual_toneprints():
    dual_rigs = []
    for root, _, files in os.walk(TONES_DIR):
        for file in files:
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

                    dual_rigs.append({
                        "file": str(filepath.relative_to(TONES_DIR)),
                        "title": fm.get("preset_name", filepath.stem),
                        "guitar": fm.get("guitar", "Universal"),
                        "pickup_type": fm.get("pickup_type", "universal"),
                        "target": fm.get("target", ""),
                        "status": fm.get("status", "initial"),
                        "tags": fm.get("tags", ""),
                        "amp_a": amp_a,
                        "amp_b": amp_b,
                        "shared_fx": fm.get("shared_fx", {}),
                        "amp_a_preset": amp_a_preset,
                        "amp_b_preset": amp_b_preset,
                        "bus_la2a_preset": bus_la2a_preset,
                        "bus_hits_preset": bus_hits_preset,
                        "target_sound_md": sections.get("target sound", ""),
                        "starting_point_md": sections.get("starting point guide", "")
                    })
    return dual_rigs


def generate_html(dual_rigs):
    rigs_json = json.dumps(dual_rigs, indent=2)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parallel Dual-Amp Rig Vault</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0b0d12;
            --surface: #131722;
            --surface-card: #1a202c;
            --surface-border: #2a3245;
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.25);
            --accent-a: #ec4899;
            --accent-b: #06b6d4;
            --text: #f3f4f6;
            --text-muted: #9ca3af;
            --badge-bg: #222938;
            --code-bg: #0f131d;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: 'Outfit', sans-serif;
            padding: 2rem;
            line-height: 1.5;
        }}

        .header {{
            max-width: 1300px;
            margin: 0 auto 2rem auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--surface-border);
            padding-bottom: 1.5rem;
        }}

        .header h1 {{
            font-size: 2.2rem;
            font-weight: 700;
            background: linear-gradient(135deg, #a5b4fc, #6366f1, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .header p {{ color: var(--text-muted); font-size: 0.95rem; margin-top: 0.25rem; }}

        .search-bar {{
            max-width: 1300px;
            margin: 0 auto 2rem auto;
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}

        .search-input {{
            flex: 1;
            min-width: 300px;
            background: var(--surface);
            border: 1px solid var(--surface-border);
            color: var(--text);
            padding: 0.75rem 1.25rem;
            border-radius: 10px;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.2s;
        }}

        .search-input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px var(--primary-glow);
        }}

        .filter-btn {{
            background: var(--surface);
            border: 1px solid var(--surface-border);
            color: var(--text-muted);
            padding: 0.6rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.2s;
        }}

        .filter-btn:hover, .filter-btn.active {{
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }}

        .grid {{
            max-width: 1300px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 2.5rem;
        }}

        .rig-card {{
            background: var(--surface);
            border: 1px solid var(--surface-border);
            border-radius: 16px;
            padding: 1.75rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}

        .rig-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
        }}

        .rig-title {{ font-size: 1.5rem; font-weight: 600; color: #ffffff; }}
        .rig-guitar {{ color: var(--text-muted); font-size: 0.9rem; margin-top: 0.2rem; }}

        .badge-list {{ display: flex; gap: 0.5rem; flex-wrap: wrap; }}
        .badge {{
            background: var(--badge-bg);
            border: 1px solid var(--surface-border);
            padding: 0.25rem 0.65rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 500;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .target-box {{
            background: var(--code-bg);
            border-left: 4px solid var(--primary);
            padding: 0.85rem 1.1rem;
            border-radius: 6px;
            font-size: 0.95rem;
            color: #d1d5db;
            margin-bottom: 1.5rem;
        }}

        .amp-matrix {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }}

        @media (max-width: 900px) {{
            .amp-matrix {{ grid-template-columns: 1fr; }}
        }}

        .amp-card {{
            background: var(--surface-card);
            border: 1px solid var(--surface-border);
            border-radius: 12px;
            padding: 1.25rem;
        }}

        .amp-card.amp-a {{ border-top: 4px solid var(--accent-a); }}
        .amp-card.amp-b {{ border-top: 4px solid var(--accent-b); }}

        .amp-card-head {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }}

        .amp-name {{ font-size: 1.15rem; font-weight: 600; color: #fff; }}
        .pan-tag {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
        }}
        .amp-a .pan-tag {{ background: rgba(236, 72, 153, 0.15); color: #f472b6; }}
        .amp-b .pan-tag {{ background: rgba(6, 182, 212, 0.15); color: #38bdf8; }}

        .param-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
            margin-bottom: 1rem;
        }}

        .param-table th {{
            text-align: left;
            padding: 0.4rem 0.6rem;
            background: rgba(0,0,0,0.2);
            color: var(--text-muted);
            border-bottom: 1px solid var(--surface-border);
        }}

        .param-table td {{
            padding: 0.4rem 0.6rem;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}

        .param-name {{ font-weight: 500; color: #e5e7eb; }}
        .param-val {{ font-family: 'JetBrains Mono', monospace; color: #38bdf8; text-align: right; }}

        .copy-btn {{
            width: 100%;
            background: rgba(99, 102, 241, 0.1);
            border: 1px solid var(--primary);
            color: #a5b4fc;
            padding: 0.5rem;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.8rem;
            font-weight: 600;
            font-family: 'JetBrains Mono', monospace;
            transition: all 0.2s;
        }}

        .copy-btn:hover {{
            background: var(--primary);
            color: #ffffff;
        }}

        .bus-section {{
            background: rgba(15, 19, 29, 0.6);
            border: 1px dashed var(--surface-border);
            border-radius: 10px;
            padding: 1rem 1.25rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }}

        .bus-title {{ font-size: 0.95rem; font-weight: 600; color: #e5e7eb; }}
        .bus-details {{ font-size: 0.85rem; color: var(--text-muted); }}

        .preset-pills {{ display: flex; gap: 0.5rem; flex-wrap: wrap; }}
    </style>
</head>
<body>

    <div class="header">
        <div>
            <h1>Parallel Dual-Amp Rig Vault</h1>
            <p>Dedicated Dual-Amp Platform & Side-by-Side Parameter Matrix</p>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 1.5rem; font-weight: 700; color: var(--primary);">{len(dual_rigs)}</div>
            <div style="font-size: 0.8rem; color: var(--text-muted);">Dual Rigs Active</div>
        </div>
    </div>

    <div class="search-bar">
        <input type="text" id="searchInput" class="search-input" placeholder="Search dual rigs by guitar, amp models, or sound target...">
        <button class="filter-btn active" onclick="filterPickup('all')">All Pickups</button>
        <button class="filter-btn" onclick="filterPickup('humbucker')">Humbuckers</button>
        <button class="filter-btn" onclick="filterPickup('single-coil')">Single Coils</button>
        <button class="filter-btn" onclick="filterPickup('p-90')">P-90s</button>
    </div>

    <div class="grid" id="rigGrid">
        <!-- JS Rendered -->
    </div>

    <script>
        const rigs = {rigs_json};
        let currentPickup = 'all';

        function renderRigs() {{
            const query = document.getElementById('searchInput').value.toLowerCase();
            const grid = document.getElementById('rigGrid');
            grid.innerHTML = '';

            const filtered = rigs.filter(r => {{
                const matchesPickup = (currentPickup === 'all' || r.pickup_type === currentPickup);
                const matchesSearch = r.title.toLowerCase().includes(query) ||
                                      r.guitar.toLowerCase().includes(query) ||
                                      r.target.toLowerCase().includes(query) ||
                                      r.tags.toLowerCase().includes(query);
                return matchesPickup && matchesSearch;
            }});

            if (filtered.length === 0) {{
                grid.innerHTML = '<p style="text-align:center; color: var(--text-muted); padding: 3rem;">No matching dual-amp rigs found.</p>';
                return;
            }}

            filtered.forEach(r => {{
                const ampA = r.amp_a || {{}};
                const ampB = r.amp_b || {{}};
                const shared = r.shared_fx || {{}};

                const card = document.createElement('div');
                card.className = 'rig-card';
                card.innerHTML = `
                    <div class="rig-header">
                        <div>
                            <div class="rig-title">${{r.title}}</div>
                            <div class="rig-guitar">${{r.guitar}}</div>
                        </div>
                        <div class="badge-list">
                            <span class="badge" style="color: #60a5fa;">${{r.pickup_type}}</span>
                            <span class="badge" style="color: #34d399;">${{r.status}}</span>
                        </div>
                    </div>

                    <div class="target-box">
                        ${{r.target}}
                    </div>

                    <div class="amp-matrix">
                        <div class="amp-card amp-a">
                            <div class="amp-card-head">
                                <div class="amp-name">${{ampA.name || 'Amp A'}}</div>
                                <div class="pan-tag">PAN: ${{ampA.pan || -12}} (L)</div>
                            </div>
                            ${{renderParams(ampA.amp_settings)}}
                            <button class="copy-btn" onclick="copyPreset('${{r.amp_a_preset}}')">📋 Copy Amp A Preset Name</button>
                        </div>

                        <div class="amp-card amp-b">
                            <div class="amp-card-head">
                                <div class="amp-name">${{ampB.name || 'Amp B'}}</div>
                                <div class="pan-tag">PAN: +${{ampB.pan || 12}} (R)</div>
                            </div>
                            ${{renderParams(ampB.amp_settings)}}
                            <button class="copy-btn" onclick="copyPreset('${{r.amp_b_preset}}')">📋 Copy Amp B Preset Name</button>
                        </div>
                    </div>

                    <div class="bus-section">
                        <div>
                            <div class="bus-title">Parallel Submix Bus & Shared FX</div>
                            <div class="bus-details">
                                LA-2A: GR Peak Red ${{shared.la2a?.peak_reduction || 28}}, Gain ${{shared.la2a?.gain || 30}} |
                                Reverb: Hitsville Decay ${{shared.hitsville?.decay || 2.0}}s, Mix ${{shared.hitsville?.mix || 0.1}}
                            </div>
                        </div>
                        <div class="preset-pills">
                            <button class="copy-btn" style="width: auto;" onclick="copyPreset('${{r.bus_la2a_preset}}')">Copy Bus LA-2A</button>
                            <button class="copy-btn" style="width: auto;" onclick="copyPreset('${{r.bus_hits_preset}}')">Copy Bus Reverb</button>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            }});
        }}

        function renderParams(settings) {{
            if (!settings) return '<p style="color:var(--text-muted); font-size:0.8rem;">No settings</p>';
            let rows = '';
            for (let [k, v] of Object.entries(settings)) {{
                let displayVal = (v === true) ? 'ON' : ((v === false) ? 'OFF' : v);
                rows += `<tr><td class="param-name">${{k}}</td><td class="param-val">${{displayVal}}</td></tr>`;
            }}
            return `<table class="param-table"><thead><tr><th>Parameter</th><th>Value</th></tr></thead><tbody>${{rows}}</tbody></table>`;
        }}

        function copyPreset(text) {{
            navigator.clipboard.writeText(text);
            alert('Copied to clipboard: ' + text);
        }}

        function filterPickup(pickup) {{
            currentPickup = pickup;
            document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            renderRigs();
        }}

        document.getElementById('searchInput').addEventListener('input', renderRigs);
        renderRigs();
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

    # Sync to iCloud Drive location
    sync_script = Path(__file__).parent.parent / "scripts" / "sync_toneprints.sh"
    if sync_script.exists():
        print(f"Running sync script: {sync_script}")
        subprocess.run(["bash", str(sync_script)], check=False)
    else:
        print("Warning: sync_toneprints.sh not found, skipping sync.")

    if not build_only:
        try:
            subprocess.run(["open", str(OUTPUT_HTML)])
        except Exception:
            pass

if __name__ == "__main__":
    main()
