---
name: song-walkthrough
description: Research a song by name and artist, then produce a complete guitarist's guide: a formatted lead sheet (chord symbols over lyrics), verified tab voicings for all chord shapes, a section-by-section song map, and targeted practice insights for each section. Use whenever Mike names a specific song to learn, asks for a song breakdown, wants to work through a particular track, or requests a lead sheet.
---

# Song Walkthrough

Given a song title and artist, this skill produces a complete learning guide in four phases. All tab content must pass through the guitar verification pipeline before appearing in any output.

The goal is a document Mike can sit with at the guitar — not a theory essay. Keep prose tight, insights specific, and tab accurate.

See `CLAUDE.md` for Mike's full profile and persona guidelines.

---

## Phase 1 — Research

Use web search to gather:

1. **Chord chart** — search for `"[song title]" "[artist]" guitar chords`. Look for multiple sources and note if they agree. Sites like Ultimate Guitar, Chordie, or transcription databases are good starting points. Cross-reference at least two sources if possible.

2. **Key, capo, and tuning** — establish the actual sounding key and any capo position. If capo is used, note both the capo key (where fingers play) and the concert key (how it sounds). If non-standard tuning is used, note it prominently.

3. **Song structure** — identify the distinct sections: intro, verse, pre-chorus, chorus, bridge, outro, and any instrumental breaks. Note which sections repeat and whether chord progressions change on repeats.

4. **Tempo and feel** — approximate BPM and rhythmic character (e.g., "driving 8th-note strum", "fingerpicked arpeggios", "half-time feel").

5. **Source transparency** — note where chord information came from and flag any uncertainty. Chord charts on the internet are often wrong or simplified. When sources disagree, pick the more harmonically coherent version and say so.

After gathering research, decide on the definitive chord set before proceeding.

---

## Phase 2 — Lead Sheet

The lead sheet has two layers.

### Layer 1: Chord-over-lyrics

Standard lead sheet notation: chord symbols placed above the lyric syllable where the change occurs, aligned with correct spacing. Each section is clearly labeled.

Format:
```
[VERSE 1]
Am              G
Yesterday, all my troubles seemed so far away
F                       C
Now it looks as though they're here to stay
```

Rules:
- Label every section: `[INTRO]`, `[VERSE 1]`, `[CHORUS]`, `[BRIDGE]`, `[OUTRO]`
- If a section repeats with identical chords, write `[VERSE 2 — same chords]` rather than duplicating
- Use concert key chord names (not capo-relative names) unless fingering in capo position is the lesson

**Copyright note:** Do not reproduce full song lyrics. Use short representative phrases (a few words per line) with ellipsis for the rest.

### Layer 2: Song map

A compact structural overview:

```
SONG MAP
─────────────────────────────────────────
Intro    (4 bars):   Am - G - F - C
Verse    (8 bars):   Am - G - F - C  × 2
Chorus   (4 bars):   F - C - G - Am
Verse 2  (8 bars):   same as Verse 1
Chorus   (4 bars):   same
Bridge   (4 bars):   Dm - Am - F - G
Outro    (4 bars):   Am - G - F - C  (fade)
─────────────────────────────────────────
Total: ~28 bars
```

---

## Phase 3 — Chord Voicings

Identify all **distinct** chords that appear in the song. For each chord, choose one idiomatic voicing that fits the style, sits comfortably in the hand, and transitions naturally from its neighbors.

Then specify voicings as JSON and run the verification pipeline:

```bash
python3 scripts/build_tab.py --inline '<json>' > /tmp/walkthrough_chords.tab
python3 scripts/verify_tab.py /tmp/walkthrough_chords.tab
```

Only include tab that passes with exit code 0. Fix errors before proceeding.

Present the verified tab under a **CHORD VOCABULARY** heading:

```
CHORD VOCABULARY
─────────────────────────────────────────
[verified tab output, with Roman numeral and chord name labels]
─────────────────────────────────────────
```

If the song has more than 6–7 unique chords, split into two tab blocks organized by section or hand position.

**Capo note:** If the song uses a capo, show voicings in capo-relative position (where fingers go) but label with concert key chord names. Add: `[Capo N — all shapes relative to capo]`.

---

## Phase 4 — Section Breakdown

For each distinct section, write a focused block covering:

1. **The progression** — name the harmonic movement (e.g., "i-VII-VI-VII in A minor")
2. **The feel** — rhythmic character, strumming pattern, or picking approach
3. **What makes it interesting** — voice leading, an unexpected chord, a rhythmic hook
4. **Specific challenge for Mike** — given his background and level, what's the likely sticking point?
5. **Practice approach** — a concrete suggestion ("Loop just bars 1–2 until the Am→G transition is automatic before adding the F")

Draw on Mike's multi-instrument background where it helps. If a chord move mirrors a saxophone or violin technique, say so.

Format:
```
─────────────────────────────────────────
VERSE — Am / G / F / C
─────────────────────────────────────────
This is a i-VII-VI-VII loop in A minor...

Rhythmic feel: ...
The interesting moment: ...
Challenge for you: ...
Practice approach: ...
```

---

## Output Assembly

Combine all phases into a single document saved to:

```
walkthroughs/[artist-slug]-[song-slug].md
```

Structure:
```
# "[Song Title]" — Artist
Key: X  |  Capo: N (or none)  |  Tuning: Standard  |  Tempo: ~N BPM

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEAD SHEET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[chord-over-lyrics for all sections]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SONG MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[structural overview with bar counts]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHORD VOCABULARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[verified tab — all unique chord shapes]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION BREAKDOWN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[one block per distinct section]
```

After saving, present the file path to Mike and give a one-sentence summary of the song's key learning opportunity.

---

## Important caveats

- Chord charts from the internet range from excellent to deeply wrong. Always flag uncertainty when sources disagree.
- Do not reproduce full song lyrics (copyright). Use short representative phrases with ellipsis.
- If the song is in an unusual key, offer a note about whether a capo or different position might be easier.
- If research turns up nothing reliable (rare for obscure tracks), say so rather than guessing.
