---
name: guitar-etude
description: Generate one original daily guitar practice idea with a musical theme and verified playable voicings.
---

# Guitar Practice Idea — Daily Generator

Generate one original guitar practice idea. Use the **Guitar Guru** persona (see CLAUDE.md) and the **Mandatory Tab Gate**.

## Rules

1. One focused idea — chord progression, fingerstyle pattern, scale exercise, or melodic loop.
2. Tonal palette: Jazz, Folk, Blues, Latin, Rock, J-pop/City Pop, Ambient, Neo-soul.
3. **Tab Gate Mandatory**: Run `build_tab.py` and `verify_tab.py` (in `scripts/`) before outputting any tab.
4. Keep prose under 120 words.

## Tab Gate

```bash
python3 scripts/build_tab.py --inline '<json_spec>' > /tmp/etude.tab
python3 scripts/verify_tab.py /tmp/etude.tab
```

Only include tab that passes with exit code 0. Fix and re-run if it fails.

## Chord JSON Format

```json
{
  "chords": [
    {
      "name": "Dm7",
      "roman": "ii7",
      "voices": {
        "e": [5, "1"],
        "B": [6, "2"],
        "G": [5, "1"],
        "D": [7, "4"],
        "A": [5, "1"],
        "E": null
      }
    }
  ],
  "rhythm": ["h", "h", "w"],
  "fingering": true
}
```

Voice values: `[fret, finger]`, `[fret]`, `"x"` (mute), `null` (not played).
Fingers: `"1"`=index, `"2"`=middle, `"3"`=ring, `"4"`=pinky, `"T"`=thumb.

## Output Format

```
🎵 TODAY'S PRACTICE IDEA
"[Name / Theme]"
[BPM] — [Genre/Mood]

[Prose description — under 120 words]

[Verified tab output]

[Extension suggestion]
```
