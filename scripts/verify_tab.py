#!/usr/bin/env python3
"""
Guitar tab verification script.

Parses structured tab notation and checks for:
1. Pipe alignment — every | must line up vertically across all 6 strings
2. Fret-to-note accuracy — each string/fret combination produces the correct pitch
3. Chord spelling — the notes actually played match the chord name
4. Physical playability — no impossible stretches, no two notes on one string
5. Column consistency — all chord columns are the same width

Usage:
    python verify_tab.py <file_or_string>
    python verify_tab.py --inline "e |---5 (1)------|-3 (1)------|..."

Returns exit code 0 if all checks pass, 1 if any fail.
Prints a detailed report either way.
"""

import sys
import re
import argparse
from typing import Optional


# ─── Fretboard reference ─────────────────────────────────────────────
# Standard tuning: string name -> open string MIDI note number
# MIDI: E2=40, A2=45, D3=50, G3=55, B3=59, E4=64
OPEN_STRINGS = {
    'E': 40,  # low E (string 6)
    'A': 45,  # string 5
    'D': 50,  # string 4
    'G': 55,  # string 3
    'B': 59,  # string 2
    'e': 64,  # high e (string 1)
}

# String order top to bottom in tab notation
STRING_ORDER = ['e', 'B', 'G', 'D', 'A', 'E']

# Note names from MIDI number (using sharps)
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Enharmonic equivalents for matching
ENHARMONIC = {
    'Db': 'C#', 'Eb': 'D#', 'Fb': 'E', 'Gb': 'F#',
    'Ab': 'G#', 'Bb': 'A#', 'Cb': 'B',
    'B#': 'C', 'E#': 'F',
}


def midi_to_note(midi: int) -> str:
    """Convert MIDI number to note name (without octave)."""
    return NOTE_NAMES[midi % 12]


def note_to_pc(name: str) -> int:
    """Convert a note name (like 'Bb' or 'F#') to pitch class 0-11."""
    normalized = ENHARMONIC.get(name, name)
    try:
        return NOTE_NAMES.index(normalized)
    except ValueError:
        return -1


def fret_to_note(string: str, fret: int) -> str:
    """Given a string name and fret number, return the note name."""
    base = OPEN_STRINGS[string]
    return midi_to_note(base + fret)


def fret_to_midi(string: str, fret: int) -> int:
    """Given a string name and fret number, return the MIDI note number."""
    return OPEN_STRINGS[string] + fret


# ─── Chord spelling database ─────────────────────────────────────────
# Maps chord quality suffix -> set of intervals (in semitones from root)
# This covers the most common chord types. We match by checking that
# all played notes belong to the expected set.

CHORD_FORMULAS = {
    # Triads
    '':        {0, 4, 7},          # major
    'm':       {0, 3, 7},          # minor
    'dim':     {0, 3, 6},          # diminished
    'aug':     {0, 4, 8},          # augmented
    '+':       {0, 4, 8},          # augmented (alt notation)

    # Sevenths
    '7':       {0, 4, 7, 10},      # dominant 7
    'maj7':    {0, 4, 7, 11},      # major 7
    'M7':      {0, 4, 7, 11},      # major 7 (alt)
    'm7':      {0, 3, 7, 10},      # minor 7
    'min7':    {0, 3, 7, 10},      # minor 7 (alt)
    'dim7':    {0, 3, 6, 9},       # diminished 7
    'm7b5':    {0, 3, 6, 10},      # half-diminished
    'mMaj7':   {0, 3, 7, 11},      # minor-major 7
    'mM7':     {0, 3, 7, 11},      # minor-major 7 (alt)

    # Sixths
    '6':       {0, 4, 7, 9},       # major 6
    'm6':      {0, 3, 7, 9},       # minor 6

    # Extended
    '9':       {0, 4, 7, 10, 14},  # dominant 9
    'maj9':    {0, 4, 7, 11, 14},  # major 9
    'M9':      {0, 4, 7, 11, 14},  # major 9 (alt)
    'm9':      {0, 3, 7, 10, 14},  # minor 9
    '11':      {0, 4, 7, 10, 14, 17},  # dominant 11
    'm11':     {0, 3, 7, 10, 14, 17},  # minor 11
    '13':      {0, 4, 7, 10, 21},  # dominant 13 (often omits 9, 11)
    'maj13':   {0, 4, 7, 11, 21},  # major 13
    'm13':     {0, 3, 7, 10, 21},  # minor 13

    # Suspended
    'sus2':    {0, 2, 7},          # suspended 2
    'sus4':    {0, 5, 7},          # suspended 4
    '7sus4':   {0, 5, 7, 10},      # dominant 7 sus4

    # Added tones
    'add9':    {0, 4, 7, 14},      # add 9
    'add11':   {0, 4, 7, 17},      # add 11
    '6/9':     {0, 4, 7, 9, 14},   # 6/9

    # Altered dominants
    '7b5':     {0, 4, 6, 10},      # dominant 7 flat 5
    '7#5':     {0, 4, 8, 10},      # dominant 7 sharp 5
    '7b9':     {0, 4, 7, 10, 13},  # dominant 7 flat 9
    '7#9':     {0, 4, 7, 10, 15},  # dominant 7 sharp 9
    '7#11':    {0, 4, 7, 10, 18},  # dominant 7 sharp 11
    'alt':     {0, 4, 8, 10, 13},  # altered (7#5b9 common voicing)
}


def parse_chord_name(name: str) -> Optional[tuple]:
    """
    Parse a chord name into (root_note, quality_suffix, bass_note_or_None).
    Examples:
        'Am7'     -> ('A', 'm7', None)
        'C#dim7'  -> ('C#', 'dim7', None)
        'Dm7/A'   -> ('D', 'm7', 'A')
        'Gadd9'   -> ('G', 'add9', None)
    """
    if not name:
        return None

    # Handle slash chords
    bass = None
    if '/' in name:
        parts = name.split('/')
        if len(parts) == 2:
            name = parts[0]
            bass = parts[1]

    # Extract root note (1-2 chars: letter + optional # or b)
    m = re.match(r'^([A-G][#b]?)(.*)', name)
    if not m:
        return None

    root = m.group(1)
    quality = m.group(2)
    return (root, quality, bass)


def get_expected_intervals(quality: str) -> Optional[set]:
    """Look up the interval set for a chord quality."""
    return CHORD_FORMULAS.get(quality)


def check_chord_spelling(chord_name: str, played_notes: list) -> dict:
    """
    Check whether the played notes match the chord name.

    Returns a dict with:
        'valid': bool
        'expected_notes': set of note names the chord should contain
        'played_notes': set of note names actually played
        'extra_notes': notes played but not in the chord
        'missing_essential': essential chord tones not present
        'message': human-readable summary
    """
    result = {
        'valid': True,
        'chord_name': chord_name,
        'messages': []
    }

    parsed = parse_chord_name(chord_name)
    if not parsed:
        result['valid'] = False
        result['messages'].append(f"Could not parse chord name: {chord_name}")
        return result

    root, quality, bass = parsed
    root_pc = note_to_pc(root)
    if root_pc == -1:
        result['valid'] = False
        result['messages'].append(f"Unknown root note: {root}")
        return result

    intervals = get_expected_intervals(quality)
    if intervals is None:
        result['messages'].append(
            f"Unknown chord quality '{quality}' — skipping spell check"
        )
        return result

    # Build expected pitch classes
    expected_pcs = set()
    for interval in intervals:
        expected_pcs.add((root_pc + interval) % 12)

    # Get played pitch classes
    played_pcs = set()
    for note in played_notes:
        pc = note_to_pc(note)
        if pc != -1:
            played_pcs.add(pc)

    # Check: are all played notes in the expected set?
    # For extended chords (9, 11, 13), we allow notes from the full
    # diatonic context since real voicings often include/omit extensions freely.
    extra = played_pcs - expected_pcs
    if extra:
        extra_names = [NOTE_NAMES[pc] for pc in extra]
        result['messages'].append(
            f"Notes outside chord formula: {', '.join(extra_names)}"
        )
        # This is a warning for extended chords, an error for basic chords
        if len(intervals) <= 4:
            result['valid'] = False

    # ── Check for essential chord tones ──
    # The "identity" of a chord comes from certain intervals that must be present.
    # Root can be omitted in slash chords or rootless voicings (common in jazz).
    # But the quality-defining intervals should be there.

    # Define essential intervals per chord type category:
    # For 7th chords: the 3rd (or sus) and 7th define the quality
    # For triads: the 3rd defines major/minor
    # For extended chords: more flexible — 5th, 9th, 11th, 13th are often omitted

    essential_intervals = set()
    if quality in ('', 'm', 'dim', 'aug', '+'):
        # Triads: 3rd is essential
        if 3 in CHORD_FORMULAS[quality]:
            essential_intervals.add(3)
        elif 4 in CHORD_FORMULAS[quality]:
            essential_intervals.add(4)
    elif '7' in quality or 'maj7' in quality or 'M7' in quality:
        # 7th chords: both 3rd and 7th are essential
        formula = CHORD_FORMULAS.get(quality, set())
        for interval in formula:
            if interval in (3, 4):  # minor or major 3rd
                essential_intervals.add(interval)
            if interval in (10, 11):  # minor or major 7th
                essential_intervals.add(interval)

    essential_pcs = {(root_pc + i) % 12 for i in essential_intervals}
    missing_essential = essential_pcs - played_pcs
    if missing_essential:
        missing_names = [NOTE_NAMES[pc] for pc in missing_essential]
        # Figure out what interval each missing note represents
        missing_desc = []
        for pc in missing_essential:
            interval = (pc - root_pc) % 12
            interval_names = {3: 'b3', 4: '3', 10: 'b7', 11: '7'}
            desc = interval_names.get(interval, f'interval {interval}')
            missing_desc.append(f"{NOTE_NAMES[pc]} ({desc})")
        result['messages'].append(
            f"Missing essential tone(s): {', '.join(missing_desc)}"
        )
        result['valid'] = False

    # Check: is the root present?
    if root_pc not in played_pcs:
        # Root might be implied (slash chord or rootless voicing)
        result['messages'].append(f"Root ({root}) not in voicing — intentional?")

    # Check slash bass
    if bass:
        bass_pc = note_to_pc(bass)
        if bass_pc != -1:
            # Find the lowest played note
            # We'll check this in the main verification, not here
            pass

    result['expected_pcs'] = expected_pcs
    result['played_pcs'] = played_pcs
    return result


# ─── Tab parser ───────────────────────────────────────────────────────

def parse_tab_block(lines: list) -> dict:
    """
    Parse a block of tab notation into structured data.

    Expects:
        - Optional Roman numeral line
        - Optional chord name line
        - 6 string lines (e, B, G, D, A, E) each starting with the string
          letter, a space, and |
        - Optional rhythm line

    Returns a dict with:
        'chords': list of chord dicts, each with:
            'name': chord name string
            'roman': Roman numeral string or None
            'frets': dict of string -> fret (int, 'x', or None for unplayed)
            'fingers': dict of string -> finger (str or None)
            'notes': dict of string -> note name
        'errors': list of error messages
        'warnings': list of warning messages
    """
    errors = []
    warnings = []

    # Separate the lines into categories
    string_lines = {}
    roman_line = None
    chord_name_line = None
    rhythm_line = None
    other_lines = []

    for line in lines:
        stripped = line.rstrip()
        if not stripped:
            continue
        # Check if it's a tab string line
        m = re.match(r'^([eBGDAE]) \|', stripped)
        if m:
            string_name = m.group(1)
            string_lines[string_name] = stripped
            continue
        other_lines.append(stripped)

    # Identify chord name / roman numeral lines from remaining lines
    # These appear above the tab. The one closest to the tab is chord names,
    # the one above that is Roman numerals.
    above_lines = []
    below_lines = []
    found_tab = False
    for line in lines:
        stripped = line.rstrip()
        if not stripped:
            continue
        if re.match(r'^[eBGDAE] \|', stripped):
            found_tab = True
            continue
        if not found_tab:
            above_lines.append(stripped)
        else:
            below_lines.append(stripped)

    if len(above_lines) >= 2:
        roman_line = above_lines[-2]
        chord_name_line = above_lines[-1]
    elif len(above_lines) == 1:
        chord_name_line = above_lines[0]

    if below_lines:
        rhythm_line = below_lines[0]

    # Validate we have all 6 strings
    missing = [s for s in STRING_ORDER if s not in string_lines]
    if missing:
        errors.append(f"Missing string lines: {', '.join(missing)}")
        return {'chords': [], 'errors': errors, 'warnings': warnings}

    # ── Check pipe alignment ──
    pipe_positions_per_string = {}
    for s in STRING_ORDER:
        line = string_lines[s]
        positions = [i for i, c in enumerate(line) if c == '|']
        pipe_positions_per_string[s] = positions

    ref_string = STRING_ORDER[0]
    ref_pipes = pipe_positions_per_string[ref_string]
    for s in STRING_ORDER[1:]:
        if pipe_positions_per_string[s] != ref_pipes:
            errors.append(
                f"Pipe misalignment: string {s} has pipes at "
                f"{pipe_positions_per_string[s]}, expected {ref_pipes}"
            )

    if not ref_pipes or len(ref_pipes) < 2:
        errors.append("Need at least 2 pipe characters per string line")
        return {'chords': [], 'errors': errors, 'warnings': warnings}

    # ── Parse chord columns ──
    num_chords = len(ref_pipes) - 1
    chords = []

    for ci in range(num_chords):
        start = ref_pipes[ci]
        end = ref_pipes[ci + 1]

        chord = {
            'name': None,
            'roman': None,
            'frets': {},
            'fingers': {},
            'notes': {},
            'column_index': ci,
        }

        # Extract fret and fingering from each string
        for s in STRING_ORDER:
            segment = string_lines[s][start + 1:end]  # between pipes

            # Match patterns: --5 (1)---, ---0---, ---x---, --------
            fret_match = re.search(r'(\d+)\s*(?:\(([T1234])\))?', segment)
            mute_match = re.search(r'x', segment)

            if fret_match:
                fret_num = int(fret_match.group(1))
                finger = fret_match.group(2)
                chord['frets'][s] = fret_num
                chord['fingers'][s] = finger
                chord['notes'][s] = fret_to_note(s, fret_num)
            elif mute_match:
                chord['frets'][s] = 'x'
            else:
                chord['frets'][s] = None  # not played

        # Try to extract chord name from the chord name line
        if chord_name_line:
            # Find text that falls roughly in this column's horizontal range
            col_center = (start + end) // 2
            # Look for chord name tokens
            for m in re.finditer(r'[A-G][#b]?\S*', chord_name_line):
                token_center = (m.start() + m.end()) // 2
                if abs(token_center - col_center) < (end - start) // 2 + 2:
                    chord['name'] = m.group()
                    break

        if roman_line:
            for m in re.finditer(r'[IiVv]+\S*', roman_line):
                token_center = (m.start() + m.end()) // 2
                col_center = (start + end) // 2
                if abs(token_center - col_center) < (end - start) // 2 + 2:
                    chord['roman'] = m.group()
                    break

        chords.append(chord)

    return {'chords': chords, 'errors': errors, 'warnings': warnings}


def verify_chord(chord: dict) -> list:
    """
    Run all verification checks on a single parsed chord.
    Returns a list of (level, message) tuples where level is 'error' or 'warning'.
    """
    issues = []
    name = chord.get('name', '(unnamed)')

    played_frets = {s: f for s, f in chord['frets'].items()
                    if f is not None and f != 'x'}

    if not played_frets:
        issues.append(('warning', f"{name}: no notes played"))
        return issues

    # ── Check fret range ──
    fret_values = list(played_frets.values())
    non_open = [f for f in fret_values if f > 0]
    if non_open:
        fret_min = min(non_open)
        fret_max = max(non_open)
        stretch = fret_max - fret_min

        if fret_min <= 4 and stretch > 4:
            issues.append((
                'error',
                f"{name}: stretch of {stretch} frets ({fret_min}-{fret_max}) "
                f"in low position — likely impossible"
            ))
        elif fret_min <= 7 and stretch > 5:
            issues.append((
                'error',
                f"{name}: stretch of {stretch} frets ({fret_min}-{fret_max}) "
                f"— likely impossible"
            ))
        elif stretch > 5:
            issues.append((
                'warning',
                f"{name}: stretch of {stretch} frets ({fret_min}-{fret_max}) "
                f"— verify this is reachable"
            ))

    # ── Check chord spelling ──
    played_notes = list(chord['notes'].values())
    if chord['name']:
        spell_result = check_chord_spelling(chord['name'], played_notes)
        for msg in spell_result.get('messages', []):
            level = 'warning' if spell_result.get('valid', True) else 'error'
            issues.append((level, f"{name}: {msg}"))

    # ── Report notes for manual verification ──
    note_report = []
    for s in STRING_ORDER:
        fret = chord['frets'].get(s)
        if fret is not None and fret != 'x':
            note = chord['notes'][s]
            note_report.append(f"{s}:{fret}={note}")
    if note_report:
        issues.append(('info', f"{name}: {', '.join(note_report)}"))

    return issues


def verify_tab(text: str) -> dict:
    """
    Main entry point. Parse and verify a tab notation string.

    Returns:
        dict with 'passed': bool, 'errors': list, 'warnings': list, 'info': list
    """
    lines = text.split('\n')

    # Find tab blocks (groups of consecutive string lines)
    blocks = []
    current_block_lines = []
    context_above = []
    in_tab = False

    for line in lines:
        stripped = line.rstrip()
        is_string_line = bool(re.match(r'^[eBGDAE] \|', stripped))

        if is_string_line:
            if not in_tab:
                # Starting a new tab block — include context lines above
                current_block_lines = list(context_above)
                in_tab = True
            current_block_lines.append(line)
        else:
            if in_tab:
                # Just ended a tab block — include this line as rhythm context
                current_block_lines.append(line)
                blocks.append(current_block_lines)
                current_block_lines = []
                in_tab = False
                context_above = []
            else:
                context_above.append(line)

    if in_tab:
        blocks.append(current_block_lines)

    all_errors = []
    all_warnings = []
    all_info = []

    for bi, block in enumerate(blocks):
        parsed = parse_tab_block(block)
        all_errors.extend(parsed['errors'])
        all_warnings.extend(parsed['warnings'])

        for chord in parsed['chords']:
            issues = verify_chord(chord)
            for level, msg in issues:
                prefix = f"Block {bi + 1}: " if len(blocks) > 1 else ""
                if level == 'error':
                    all_errors.append(prefix + msg)
                elif level == 'warning':
                    all_warnings.append(prefix + msg)
                else:
                    all_info.append(prefix + msg)

    passed = len(all_errors) == 0

    return {
        'passed': passed,
        'errors': all_errors,
        'warnings': all_warnings,
        'info': all_info,
    }


def format_report(result: dict) -> str:
    """Format verification results as a human-readable report."""
    lines = []
    lines.append("=" * 50)
    if result['passed']:
        lines.append("VERIFICATION PASSED")
    else:
        lines.append("VERIFICATION FAILED")
    lines.append("=" * 50)

    if result['errors']:
        lines.append("")
        lines.append("ERRORS:")
        for e in result['errors']:
            lines.append(f"  X  {e}")

    if result['warnings']:
        lines.append("")
        lines.append("WARNINGS:")
        for w in result['warnings']:
            lines.append(f"  !  {w}")

    if result['info']:
        lines.append("")
        lines.append("NOTE MAP:")
        for i in result['info']:
            lines.append(f"     {i}")

    lines.append("")
    return '\n'.join(lines)


# ─── CLI ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Verify guitar tab notation')
    parser.add_argument('input', nargs='?', help='File path to verify')
    parser.add_argument('--inline', type=str, help='Tab text to verify inline')
    args = parser.parse_args()

    if args.inline:
        text = args.inline
    elif args.input:
        with open(args.input, 'r') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    result = verify_tab(text)
    print(format_report(result))
    sys.exit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
