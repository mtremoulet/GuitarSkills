---
name: chord-voicing
description: "Query guitar chord voicings, shapes, and fingerings. Trigger on: chord names (C7, Am9, Gm7b5), 'how to play', 'show me voicings for', 'chord shape', 'fingering for', drop voicings, inversions, shell voicings, or any guitar chord question."
argument-hint: "[chord query, e.g. 'Cmaj7 drop 2 above 5th fret']"
allowed-tools: ["Bash", "Read"]
---

# Guitar Chord Voicing Skill

You have access to a comprehensive guitar chord voicing library. It algorithmically generates every physically playable voicing for any chord on a standard-tuned 6-string guitar.

## Library Path

The chord library is always at `chord-library/` relative to the GuitarSkills project root. Use:

```bash
CHORD_LIB="$(pwd)/chord-library"
```

If you are not already in the GuitarSkills project directory, adjust accordingly.

## IMPORTANT: Read Preferences First

Before presenting results, ALWAYS read the user's preferences file:

```bash
cat chord-library/preferences/voicing_feedback.md
```

Apply these preferences when curating and presenting voicings. If the user gives new feedback about voicing preferences (likes, dislikes, "never show me X", "I prefer Y"), append it to that file under the appropriate section.

## How to Use

Invoke the CLI to answer chord voicing questions:

```bash
cd chord-library && python3 chord_cli.py query \
  --root <NOTE> --quality <QUALITY> [filters...] \
  --format json --limit 10
```

### Required Arguments

| Flag | Description | Examples |
|------|-------------|---------|
| `--root` | Root note | C, C#, Db, F#, Bb |
| `--quality` | Chord quality symbol | (see quality table below) |

### Filter Arguments

| Flag | Description | Examples |
|------|-------------|---------|
| `--min-fret N` | Minimum fret position | `--min-fret 5` |
| `--max-fret N` | Maximum fret position | `--max-fret 4` |
| `--bass-string N` | Root must be on this string (1=high e, 6=low E) | `--bass-string 5` |
| `--voicing-type TYPE` | Filter by voicing type | open, barre, shell, drop2, drop3, close, spread |
| `--max-difficulty F` | Max difficulty score 0.0–1.0 | `--max-difficulty 0.5` |
| `--sort-by METHOD` | Sort order | default, compact, position_asc, open_strings |
| `--limit N` | Max results to return | `--limit 5` |

### Chord Quality Symbols

| Quality | Symbol | Example |
|---------|--------|---------|
| Major | maj | `--quality maj` |
| Minor | m | `--quality m` |
| Dominant 7th | 7 | `--quality 7` |
| Major 7th | maj7 | `--quality maj7` |
| Minor 7th | m7 | `--quality m7` |
| Half-diminished | m7b5 | `--quality m7b5` |
| Diminished 7th | dim7 | `--quality dim7` |
| Sus2 | sus2 | `--quality sus2` |
| Sus4 | sus4 | `--quality sus4` |
| Add9 | add9 | `--quality add9` |
| Major 9th | maj9 | `--quality maj9` |
| Minor 9th | m9 | `--quality m9` |
| Dominant 9th | 9 | `--quality 9` |
| Dominant 13th | 13 | `--quality 13` |
| (and 30+ more — run `python3 chord_cli.py list-qualities` to see all) | | |

## Presenting Results

1. **Curate**: Don't dump all results — pick the 2-3 most useful voicings for the musical context.
2. **Show the tab**: Include the ASCII diagram from the CLI output.
3. **Explain the choice**: Say why each voicing is useful (register, voice leading, style, difficulty).
4. **Reference Mike's context**: If a voicing is physically demanding, flag it. Connect to his musical background where relevant.

## Example Queries

```bash
# All C7 voicings with root on 5th string
cd chord-library && python3 chord_cli.py query --root C --quality 7 --bass-string 5

# Easy open-position Em7
cd chord-library && python3 chord_cli.py query --root E --quality m7 --max-fret 4 --max-difficulty 0.4

# Am9 drop-2 above 8th fret
cd chord-library && python3 chord_cli.py query --root A --quality m9 --min-fret 8 --voicing-type drop2

# Gm7b5 shell voicings (for jazz comping)
cd chord-library && python3 chord_cli.py query --root G --quality m7b5 --voicing-type shell --limit 5
```
