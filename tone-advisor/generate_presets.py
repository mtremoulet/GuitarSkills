#!/usr/bin/env python3
"""
generate_presets.py
Reads tone markdown files and generates:
  - Logic .pst preset files (Channel EQ confirmed; others as implemented)
    → saved to ~/Music/Audio Music Apps/Plug-In Settings/[Plugin]/Toneprints/[slug].pst
    → also saved to tones/presets/[slug]/ for project tracking
  - CHECKLIST.md for JUCE plugins (UADx, Neural DSP) requiring manual load

Usage:
    python3 generate_presets.py [tone-slug]    # one tone
    python3 generate_presets.py --all          # all tones
    python3 generate_presets.py --list         # list supported plugins

The Channel EQ .pst binary format (confirmed via factory preset analysis):
  Header: 32 bytes (GAMETSPP magic + size fields)
  Bands: 8 × 16 bytes starting at offset 0x20
  Each band: [freq_float, gain_or_slope_float, Q_float, enabled_float]
  Band order: HP, Low Shelf, Peak1, Peak2, Peak3, Peak4, High Shelf, LP
  Footer: remaining bytes (analyzer state, copied verbatim from template)
"""

import re
import sys
import struct
from pathlib import Path

# ── Constants ─────────────────────────────────────────────────────────────────

TONES_DIR = Path(__file__).parent.parent / 'tones'
PRESETS_DIR = TONES_DIR / 'presets'
LOGIC_SETTINGS = Path.home() / 'Music' / 'Audio Music Apps' / 'Plug-In Settings'
LOGIC_FACTORY  = Path('/Library/Application Support/Logic/Plug-In Settings')

JUCE_PREFIXES = ('UADx', 'UA ', 'Neural DSP', 'IK Multimedia', 'TONEX',
                 'Archetype', 'AmpliTube')

# Band index → type name (for diagnostics)
CHANNEL_EQ_BAND_NAMES = [
    'HP (Low Cut)', 'Low Shelf', 'Peak 1', 'Peak 2',
    'Peak 3', 'Peak 4', 'High Shelf', 'LP (High Cut)'
]

# Slope code → dB/oct mapping (stored in the "gain" field for HP/LP bands)
SLOPE_CODES = {
    '6': 1.0, '12': 2.0, '18': 3.0, '24': 4.0,
}


# ── Value parsers ──────────────────────────────────────────────────────────────

def parse_frequency(s: str) -> float:
    """Parse '100 Hz', '1.5 kHz', '280Hz', '1k' → float Hz."""
    s = s.strip().lower()
    s = re.sub(r'[^\d.k]', '', s)  # strip non-numeric except k
    if s.endswith('k'):
        return float(s[:-1]) * 1000
    return float(s) if s else 0.0


def parse_gain(s: str) -> float:
    """Parse '+1.5 dB', '−2 dB', '-2dB', '—' → float dB. '—' = 0."""
    s = s.strip()
    if s in ('—', '-', '', '0'):
        return 0.0
    # Unicode minus
    s = s.replace('−', '-').replace('–', '-')
    s = re.sub(r'[^0-9.\-+]', '', s)
    return float(s) if s else 0.0


def parse_q_slope(s: str) -> tuple[float, float]:
    """
    Parse Q/slope column.
    Returns (q_value, slope_code) where slope_code is only used for HP/LP bands.

    Accepts: 'Q: 0.8', '12 dB/oct', '12 dB/oct; Q: 0.71', '0.71'
    """
    s = s.strip()
    q = 0.71       # Logic Channel EQ default Q
    slope_code = 2.0  # 12 dB/oct default

    # Extract slope
    slope_m = re.search(r'(\d+)\s*db/oct', s, re.IGNORECASE)
    if slope_m:
        slope_code = SLOPE_CODES.get(slope_m.group(1), 2.0)

    # Extract Q
    q_m = re.search(r'q[:\s]+([0-9.]+)', s, re.IGNORECASE)
    if q_m:
        q = float(q_m.group(1))
    elif not slope_m:
        # Plain number with no labels → treat as Q
        plain = re.search(r'^([0-9.]+)$', s)
        if plain:
            q = float(plain.group(1))

    return q, slope_code


# ── Markdown parser (subset of generate_tone_viewer.py) ───────────────────────

def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}, text
    data = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            data[k.strip()] = v.strip()
    return data, text[m.end():]


def parse_md_table(table_lines: list[str]) -> tuple[list, list]:
    headers, rows = [], []
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


def parse_plugin_block(content: str) -> dict:
    lines = content.strip().split('\n')
    table_lines, state = [], 'pre'
    for line in lines:
        if line.strip().startswith('|'):
            state = 'table'
            table_lines.append(line.strip())
        elif state == 'table':
            state = 'post'
    headers, rows = parse_md_table(table_lines)
    return {'headers': headers, 'rows': rows}


def parse_tone_file(path: Path) -> dict:
    text = path.read_text()
    fm, body = parse_frontmatter(text)
    parts = re.split(r'^## (.+)$', body, flags=re.MULTILINE)
    sections = {parts[i].strip(): parts[i+1] for i in range(1, len(parts)-1, 2)}

    plugins = []
    if 'Signal Chain' in sections:
        chain = sections['Signal Chain']
        pp = re.split(r'^### (.+)$', chain, flags=re.MULTILINE)
        for i in range(1, len(pp)-1, 2):
            hdr = pp[i].strip()
            hm = re.match(r'^(?:\d+\.\s+)?(.+?)(?:\s+—\s+(.+))?$', hdr)
            name = hm.group(1).strip() if hm else hdr
            role = hm.group(2).strip() if hm and hm.group(2) else ''
            block = parse_plugin_block(pp[i+1])
            plugins.append({'name': name, 'role': role, **block})

    return {'id': fm.get('id', path.stem), 'plugins': plugins}


# ── Channel EQ .pst generator ─────────────────────────────────────────────────

BAND_OFFSET = 0x20
BAND_STRIDE = 16

BAND_TYPE_MAP = {
    # HP band (index 0)
    'high-pass': 0, 'high pass': 0, 'highpass': 0, 'hp': 0,
    'low cut': 0, 'low-cut': 0, 'lowcut': 0,
    # Low Shelf (index 1)
    'low shelf': 1, 'low-shelf': 1, 'lowshelf': 1, 'low shel': 1,
    # High Shelf (index 6)
    'high shelf': 6, 'high-shelf': 6, 'highshelf': 6, 'hi shelf': 6,
    # LP band (index 7)
    'low-pass': 7, 'low pass': 7, 'lowpass': 7, 'lp': 7,
    'high cut': 7, 'high-cut': 7, 'highcut': 7,
    # Peak — caller handles "peak" specially
}


def generate_channel_eq_pst(plugin_data: dict, output_path: Path) -> list[str]:
    """
    Generate a Channel EQ .pst from tone markdown data.
    Returns list of warning strings (empty = success).
    """
    template_path = LOGIC_FACTORY / 'Channel EQ' / '#default.pst'
    if not template_path.exists():
        return [f'Template not found: {template_path}']

    buf = bytearray(template_path.read_bytes())
    warnings = []

    headers = [h.lower() for h in plugin_data['headers']]
    rows = plugin_data['rows']

    col = {}
    for i, h in enumerate(headers):
        for key in ['band', 'frequency', 'gain', 'slope / q', 'slope/q', 'q', 'purpose']:
            if key in h and key not in col:
                col[key] = i

    peak_used = 0  # how many Peak bands consumed so far

    for row in rows:
        if not row or len(row) < 2:
            continue

        band_str = row[col.get('band', 0)].lower().strip() if 'band' in col else ''

        # Map to band index
        band_idx = None
        for key, idx in BAND_TYPE_MAP.items():
            if key in band_str:
                band_idx = idx
                break
        if band_idx is None and ('peak' in band_str or 'bell' in band_str):
            if peak_used < 4:
                band_idx = 2 + peak_used
                peak_used += 1

        if band_idx is None:
            warnings.append(f'Unrecognized band type: {row[col.get("band", 0)]!r}')
            continue

        base = BAND_OFFSET + band_idx * BAND_STRIDE

        # Parse values
        freq_raw = row[col['frequency']].strip() if 'frequency' in col else ''
        gain_raw = row[col['gain']].strip() if 'gain' in col else '0'
        q_raw_key = next((k for k in ['slope / q', 'slope/q', 'q'] if k in col), None)
        q_raw = row[col[q_raw_key]].strip() if q_raw_key else ''

        freq = parse_frequency(freq_raw)
        gain = parse_gain(gain_raw)
        q, slope_code = parse_q_slope(q_raw)

        if freq == 0.0:
            warnings.append(f'Could not parse frequency for band {band_idx}: {freq_raw!r}')
            continue

        # Write: [freq, gain_or_slope, Q, enabled=1]
        struct.pack_into('<f', buf, base,      freq)
        struct.pack_into('<f', buf, base + 4,  slope_code if band_idx in (0, 7) else gain)
        struct.pack_into('<f', buf, base + 8,  q)
        struct.pack_into('<f', buf, base + 12, 1.0)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(bytes(buf))
    return warnings


# ── Plugin dispatch ────────────────────────────────────────────────────────────

def is_juce_plugin(name: str) -> bool:
    return any(name.startswith(p) for p in JUCE_PREFIXES)


def is_hardware(name: str) -> bool:
    return 'Tone King' in name


PLUGIN_GENERATORS = {
    'channel eq': ('Channel EQ', generate_channel_eq_pst),
}


def normalize_plugin_name(name: str) -> str:
    """Strip manufacturer prefix and numbering for lookup."""
    name = re.sub(r'^(Logic|Apple)\s+', '', name, flags=re.IGNORECASE)
    return name.lower().strip()


# ── Checklist generator ───────────────────────────────────────────────────────

def format_checklist_table(headers: list, rows: list) -> str:
    if not headers or not rows:
        return ''
    lines = ['| ' + ' | '.join(headers) + ' |',
             '| ' + ' | '.join('---' for _ in headers) + ' |']
    for row in rows:
        # pad row to header length
        padded = list(row) + [''] * (len(headers) - len(row))
        lines.append('| ' + ' | '.join(padded[:len(headers)]) + ' |')
    return '\n'.join(lines)


def generate_checklist(tone: dict, juce_plugins: list, output_path: Path):
    slug = tone['id']
    lines = [
        f'# Preset Loading Checklist — {slug}',
        '',
        'These plugins use proprietary preset formats and require manual settings.',
        'Open each plugin in Logic and dial in the values from the table below.',
        '',
    ]

    for p in juce_plugins:
        lines.append(f'## {p["name"]} — {p["role"]}')
        lines.append('')
        table = format_checklist_table(p['headers'], p['rows'])
        if table:
            lines.append(table)
        else:
            lines.append('*(No parameter table — see tone markdown for settings.)*')
        lines.append('')

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(lines))


# ── Main processing ────────────────────────────────────────────────────────────

def process_tone(slug: str) -> bool:
    tone_path = TONES_DIR / f'{slug}.md'
    if not tone_path.exists():
        print(f'ERROR: {tone_path} not found')
        return False

    tone = parse_tone_file(tone_path)
    preset_dir = PRESETS_DIR / slug
    preset_dir.mkdir(parents=True, exist_ok=True)

    print(f'\n── {slug} ──')

    generated = []
    juce_plugins = []

    for plugin in tone['plugins']:
        name = plugin['name']

        if is_hardware(name):
            print(f'  [skip]    {name} (physical hardware)')
            continue

        if is_juce_plugin(name):
            print(f'  [checklist] {name}')
            juce_plugins.append(plugin)
            continue

        norm = normalize_plugin_name(name)
        if norm in PLUGIN_GENERATORS:
            pst_subdir, gen_fn = PLUGIN_GENERATORS[norm]

            # Save to project presets dir
            project_path = preset_dir / f'{norm.replace(" ", "-")}.pst'
            # Also install to Logic presets (appears in plugin preset menu)
            logic_path = (LOGIC_SETTINGS / pst_subdir / 'Toneprints' / f'{slug}.pst')

            warnings = gen_fn(plugin, project_path)

            if warnings:
                print(f'  [warn]    {name}:')
                for w in warnings:
                    print(f'              {w}')
            else:
                print(f'  [pst]     {name} → {project_path.name}')

            # Install to Logic preset menu location
            try:
                logic_path.parent.mkdir(parents=True, exist_ok=True)
                logic_path.write_bytes(project_path.read_bytes())
                print(f'  [install] → {logic_path}')
            except Exception as e:
                print(f'  [warn]    Could not install to Logic presets: {e}')

            generated.append(name)
        else:
            print(f'  [skip]    {name} (no generator — add to PLUGIN_GENERATORS)')

    if juce_plugins:
        checklist_path = preset_dir / 'CHECKLIST.md'
        generate_checklist(tone, juce_plugins, checklist_path)
        print(f'  [checklist] → {checklist_path}')

    return True


def list_supported():
    print('Supported Logic native plugins (generate .pst):')
    for norm, (subdir, _) in PLUGIN_GENERATORS.items():
        print(f'  {norm} → saves to {subdir}/Toneprints/')
    print()
    print('JUCE plugins (checklist only):')
    for p in JUCE_PREFIXES:
        print(f'  plugins starting with "{p}"')
    print()
    print('Skipped:')
    print('  Tone King Imperial Preamp (physical hardware)')


def main():
    args = sys.argv[1:]

    if '--list' in args:
        list_supported()
        return

    if '--all' in args or not args:
        slugs = [p.stem for p in sorted(TONES_DIR.glob('*.md'))]
        if not slugs:
            print('No tone files found in tones/')
            return
        for slug in slugs:
            process_tone(slug)
    else:
        slug = args[0].removesuffix('.md')
        process_tone(slug)


if __name__ == '__main__':
    main()
