---
name: guitar-lesson-daily
description: >
  Generates a complete daily jazz standard guitar lesson and saves it to the
  guitar-coach library. Use this skill whenever asked to generate a daily
  guitar lesson, create today's practice session, pick a jazz standard to
  study, or run the daily guitar coach task. Also triggers automatically for
  any scheduled guitar lesson job. The skill selects a song not covered in the
  past two weeks, builds all tab through the mandatory verification pipeline,
  writes a full deep-dive session in the guitar-coach format, and updates the
  lesson index.
---

# Guitar Lesson Daily

You are generating an autonomous daily jazz guitar lesson for Mike. This often runs as a scheduled task with no user present, so make all decisions independently and document your reasoning clearly in the output.

See `CLAUDE.md` for Mike's full profile and persona guidelines.

## Paths

All paths below are relative to the `GuitarSkills/` project root.

| What | Path |
|------|------|
| Session output | `guitar-coach-library/sessions/YYYY-MM-DD-[slug]/session.md` |
| Library index | `guitar-coach-library/index.md` |
| Tab build script | `scripts/build_tab.py` |
| Tab verify script | `scripts/verify_tab.py` |
| Session template | `templates/session-plan-template.md` |
| Etude template | `templates/etude-template.md` |
| Chord voicings ref | `references/chord-voicings.md` |
| Common progressions ref | `references/common-progressions.md` |

---

## Step 1 — Select Today's Song

Scan `guitar-coach-library/sessions/` and note all directory names. Each directory name starts with `YYYY-MM-DD-`. **Compute the cutoff date first:** subtract 14 days from today's date (e.g., if today is 2026-04-25, the cutoff is 2026-04-11). Any session directory whose date is **on or after that cutoff** is off-limits. Anything dated before the cutoff is eligible.

**How to pick:** Choose something at a beginner-to-intermediate level with clear harmonic content worth studying. Avoid songs with extremely complex changes or unusual time signatures (Giant Steps, Moment's Notice, etc.) — those are out of scope here. Popular choices include Autumn Leaves, All Of Me, Fly Me To The Moon, Girl From Ipanema, Blue Bossa, Summertime, How High The Moon, Misty, My Funny Valentine, All The Things You Are, Satin Doll, Body And Soul, On Green Dolphin Street, Just Friends, Georgia On My Mind, La Vie En Rose, Besame Mucho, Round Midnight, and many others.

**Prefer variety across harmonic concepts.** If recent sessions covered a lot of minor ii-V-i, lean toward a major-key standard or a modal tune today. Look at the names of the last 3–4 sessions and pick something that offers a genuinely different harmonic focus.

---

## Step 2 — Read Reference Files

Read both template files and skim the reference files before generating the lesson:
- `templates/session-plan-template.md`
- `templates/etude-template.md`
- `references/chord-voicings.md`
- `references/common-progressions.md`

---

## Step 3 — The Mandatory Tab Gate (Non-Negotiable)

**Never output unverified tab.** Every chord voicing in every etude must pass through this pipeline before being included in the lesson:

```bash
# Build
python3 scripts/build_tab.py --inline '<json_spec>' > /tmp/etude_N.tab

# Verify — must exit 0
python3 scripts/verify_tab.py /tmp/etude_N.tab
```

If verification fails or warns, fix the chord JSON and re-run until you get a clean pass.

### Chord JSON format

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

Voice values: `[fret, "finger"]`, `[fret]` (no fingering), `"x"` (mute), `null` (string not played).
Fingers: `"1"`=index, `"2"`=middle, `"3"`=ring, `"4"`=pinky, `"T"`=thumb.

### Verifying note accuracy

Before building, check your intended notes manually:

| String | Open | Fret formula |
|--------|------|-------------|
| E (6)  | E2   | +1 per semitone |
| A (5)  | A2   | same |
| D (4)  | D3   | same |
| G (3)  | G3   | same |
| B (2)  | B3   | same |
| e (1)  | E4   | same |

Spell out the chord tones before placing fingers.

---

## Chord Diagram Formatting

### Primary format: compact notation (mandatory)

Every chord voicing must have compact notation:

```
Dm7: x-5-7-5-6-x
Am7: x-0-2-0-1-0
E7:  0-2-0-1-0-0
```

### Secondary: ASCII chord boxes (optional, use with care)

Only include when they genuinely help. Follow the template from `templates/etude-template.md`. If an ASCII box looks off when you read it back, drop it and keep only compact notation.

---

## Step 4 — Write the Full Lesson

Follow `templates/session-plan-template.md` structure exactly. A complete session includes all sections below.

### Required sections

1. **Song Background** (2–4 paragraphs)
   - Composer, year, original context
   - Why it matters; landmark recordings
   - Why it's particularly valuable on guitar
   - Bridge to Mike's background (violin, sax, other instruments) where natural

2. **Theory & Context** (2–4 paragraphs + tables/analysis)
   - Roman numeral analysis of the key sections
   - Explain *why* chords work the way they do
   - Call out borrowed chords, modal mixture, secondary dominants, etc.
   - Identify voice leading patterns worth noting

3. **Four Progressive Etudes** (see below)

4. **Suggested Practice Schedule** (table: Day / Focus / Time / Tempo)

5. **Songs to Play Along With** (5–8 recordings, table format)

6. **Jam Playlist** (Spotify search commands)

7. **Practice Tip** specific to this song

8. **What's Next** (related concepts, next-step songs)

### Etude design

Build four etudes of increasing difficulty:

| Etude | Focus | Difficulty |
|-------|-------|------------|
| 1 | Core shapes — isolated, slow, whole notes | ★★☆☆☆ |
| 2 | Full progression — add rhythm/movement | ★★☆☆☆–★★★☆☆ |
| 3 | Jazz voicings — shells, drop-2, extensions | ★★★☆☆ |
| 4 | Challenge — bridge section, alternate position, or melodic fragment | ★★★☆☆–★★★★☆ |

Each etude must include:
- Verified tab (from the Tab Gate)
- Compact notation for every chord (e.g. `Dm7: x-5-7-5-6-x`) — mandatory
- ASCII chord box diagrams — optional, only if they render cleanly
- Strum/picking pattern notation
- Three-phase practice instructions with target tempos
- "What to listen for" section

Keep etudes short (4–16 bars). Quality over quantity.

---

## Step 5 — Save and Index

### Session file

Save to:
```
guitar-coach-library/sessions/YYYY-MM-DD-[song-slug]/session.md
```

**Slug conventions:**
- Lowercase, hyphen-separated
- Drop articles (a, the, an) unless essential
- Examples: `summertime`, `fly-me-to-the-moon`, `girl-from-ipanema`, `all-the-things-you-are`

### Index update

Append a row to `guitar-coach-library/index.md`:

```
| YYYY-MM-DD | [Song Title] — [Subtitle] | [Genre] | [Level range] | sessions/YYYY-MM-DD-[slug]/session.md |
```

---

## Step 6 — Summary Output

After saving, output a brief confirmation message that includes:
- Which song was chosen and why (what made it the right pick today)
- The file path to the new session
- One sentence on what harmonic concept the lesson focuses on

---

## Quick checklist

Before finalizing:
- [ ] All tab passed the Tab Gate (build_tab.py + verify_tab.py both ran, exit code 0)
- [ ] Session has all 8 required sections
- [ ] Etude 1 is genuinely accessible for an advanced beginner
- [ ] Theory section explains *why*, not just *what*
- [ ] Mike's multi-instrument background gets at least one meaningful callback
- [ ] Every chord has compact notation (x-0-2-0-1-0 style)
- [ ] File saved to the correct path with correct slug
- [ ] `index.md` updated
