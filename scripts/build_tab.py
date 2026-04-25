#!/usr/bin/env python3
"""
Guitar tab builder — constructs properly aligned tab notation from a JSON
chord specification.

Usage:
    python build_tab.py <json_file>
    python build_tab.py --inline '<json_string>'

Input JSON format:
{
    "chords": [
        {
            "name": "Dm7",
            "roman": "ii7",          // optional
            "voices": {
                "e": [5, "1"],       // [fret, finger] — finger is optional
                "B": [6, "2"],
                "G": [5, "1"],
                "D": [7, "4"],
                "A": [5, "1"],
                "E": null            // null = not played
            }
        },
        ...
    ],
    "rhythm": ["h", "h", "w"],       // optional
    "fingering": true                  // whether to include fingering (default: true if fingers provided)
}

Voices can also be specified as:
    - [fret]           just fret number, no fingering
    - [fret, finger]   fret with fingering
    - "x"              muted string
    - null             not played

Output: properly formatted tab notation printed to stdout.
"""

import json
import sys
import argparse

STRING_ORDER = ['e', 'B', 'G', 'D', 'A', 'E']


def build_tab(spec: dict) -> str:
    """Build formatted tab notation from a chord specification dict."""
    chords = spec['chords']
    rhythm = spec.get('rhythm', [])
    include_fingering = spec.get('fingering', None)

    # Auto-detect fingering if not specified
    if include_fingering is None:
        include_fingering = any(
            isinstance(v, list) and len(v) > 1
            for chord in chords
            for v in chord.get('voices', {}).values()
            if v is not None
        )

    # Build column content for each string of each chord
    col_contents = []  # list of dicts: string -> content_str
    for chord in chords:
        col = {}
        voices = chord.get('voices', {})
        for s in STRING_ORDER:
            v = voices.get(s)
            if v is None:
                col[s] = ''  # not played
            elif v == 'x':
                col[s] = 'x'
            elif isinstance(v, list):
                fret = v[0]
                if include_fingering and len(v) > 1 and v[1] is not None:
                    col[s] = f'{fret} ({v[1]})'
                else:
                    col[s] = str(fret)
            elif isinstance(v, (int, float)):
                col[s] = str(int(v))
            else:
                col[s] = str(v)
        col_contents.append(col)

    # Determine uniform column width
    col_widths = []
    for col in col_contents:
        max_w = max((len(v) for v in col.values()), default=0)
        col_widths.append(max_w + 6)  # 3 leading dashes + 3 trailing minimum
    uniform_width = max(col_widths)

    # Build string lines
    tab_lines = {}
    for s in STRING_ORDER:
        parts = []
        for col in col_contents:
            content = col[s]
            if content:
                inner = f'---{content}'
                inner = inner + '-' * (uniform_width - len(inner))
            else:
                inner = '-' * uniform_width
            parts.append(inner)
        tab_lines[s] = f'{s} |' + '|'.join(parts) + '|'

    # Find pipe positions for centering labels
    ref_line = tab_lines[STRING_ORDER[0]]
    pipes = [i for i, c in enumerate(ref_line) if c == '|']

    def center_labels(labels, total_len):
        """Place labels centered over their respective columns."""
        chars = [' '] * total_len
        for ci, label in enumerate(labels):
            if label:
                start = pipes[ci]
                end = pipes[ci + 1]
                center = (start + end) // 2
                pos = center - len(label) // 2
                for j, ch in enumerate(label):
                    if 0 <= pos + j < total_len:
                        chars[pos + j] = ch
        return ''.join(chars).rstrip()

    # Assemble output
    output_lines = []

    # Roman numerals (if any chord has them)
    romans = [chord.get('roman', '') for chord in chords]
    if any(romans):
        output_lines.append(center_labels(romans, len(ref_line)))

    # Chord names
    names = [chord.get('name', '') for chord in chords]
    output_lines.append(center_labels(names, len(ref_line)))

    # Blank line before tab
    output_lines.append('')

    # Tab lines
    for s in STRING_ORDER:
        output_lines.append(tab_lines[s])

    # Rhythm
    if rhythm:
        output_lines.append('')
        output_lines.append(center_labels(rhythm, len(ref_line)))

    return '\n'.join(output_lines)


def main():
    parser = argparse.ArgumentParser(description='Build guitar tab from JSON')
    parser.add_argument('input', nargs='?', help='JSON file path')
    parser.add_argument('--inline', type=str, help='JSON string')
    args = parser.parse_args()

    if args.inline:
        spec = json.loads(args.inline)
    elif args.input:
        with open(args.input, 'r') as f:
            spec = json.load(f)
    else:
        spec = json.load(sys.stdin)

    print(build_tab(spec))


if __name__ == '__main__':
    main()
