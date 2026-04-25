# Chord Voicing Preferences

Feedback and preferences that shape how voicings are curated and presented.
The skill reads this file to tailor results. Add entries as you use the tool.

## Ranking Preferences

- Avoid voicings that combine open strings with fretted notes above the 12th fret. These are physically playable but musically absurd (e.g., `20-18-20-0-X-X`).
- Penalize octave-duplicate shapes — if a shape exists at fret 3, the same shape at fret 15 is redundant unless specifically requested at that position.
- Voicings stacked entirely on the E-A-D strings tend to sound muddy. Power chords and bass-register walking lines are the exception, but for general chord voicings, prefer shapes that include the G string or higher.

## Voicing Type Preferences

- For jazz shell voicings, prefer the R-X-b7-b3 pattern on strings 6-skip-4-3 (e.g., `8-X-8-8-X-X` for Cm7). This is the classic Freddie Green skeleton — root on a bass string, guide tones on D and G, A string muted.
- Shell voicings should prioritize 3rd and 7th (the guide tones) over the 5th.

## Presentation Preferences

- When returning large result sets, curate aggressively. 3-5 genuinely useful voicings is better than 10+ with noise.
- Group voicings by position on the neck when showing multiple results.
- Call out what makes a voicing interesting or useful — don't just dump diagrams.
- The user is an experienced guitarist who understands theory. No need to explain what a shell voicing or drop-2 is — just show the shapes and note what's notable.
