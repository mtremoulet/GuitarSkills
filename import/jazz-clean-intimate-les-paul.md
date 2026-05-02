---
id: jazz-clean-intimate-les-paul
created: 2026-04-16
updated: 2026-04-18
guitar: Gibson Les Paul Studio (490R neck pickup)
target: Pristine, warm jazz clean — jazz box intimacy through a transparent high-headroom platform; close and present, no reverb wash
tags: jazz, clean, warm, intimate, les-paul, humbucker
tone-king-channel: rhythm
status: tested
---

# Jazz Clean — Intimate Les Paul

## Target Sound
The goal is a Henriksen Blu / archtop-through-clean-amp sound: full, warm, and close-mic'd rather than roomy or ambient. The 490R neck pickup already brings body and warmth; the chain's job is to stay out of the way of that natural character while adding just enough optical compression for sustain and a small-room ambience that feels like the amp is in the corner of the studio. No delay, no chamber wash — just the guitar, articulate and present.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | 60s American blackface warmth; pairs naturally with the 490R's warm humbucker character |
| Volume | 3 | LP 490R has more output than a Tele — lower setting achieves equivalent clean headroom |
| Attenuation | 6 | Post-phase-inverter trim to compensate for the Showtime '64's low output at these clean settings |
| Bass | 5 | Neutral — the 490R has substantial natural low end; don't push it further here |
| Treble | 5 | Neutral — no extra sparkle needed from a warm humbucker |
| Reverb | Off | Bypassed — space handled by Space Designer |
| Tremolo | Off | Off |
| IR | **Bypassed** | Showtime '64 handles cab simulation — do not double-cab |

### 2. UADx Showtime '64 Tube Amp — clean platform

High-headroom, neutral-character amp. Unlike the Dream '65, it doesn't impose a mid-scoop or pronounced Blackface color on top of the Tone King Rhythm signal — it just passes the LP's voice cleanly.

| Control | Setting | Purpose |
|---------|---------|---------|
| In | HI-Z (center default) | Instrument level input |
| Bright / Normal | **Normal** | Removes bright cap; smooth, warm top end — right for a humbucker |
| Volume | 3 | Deep clean territory |
| Treble | 4 | Slight pullback — the 490R already has warmth; avoid the Fender-stack scoop pushing the low mids up |
| Middle | 5 | Neutral — let the guitar's midrange speak |
| Bass | 5 | Slightly less than the Tele jazz tone; the LP doesn't need as much added weight |
| Vibrato | Off | Off |
| Room | 30% | Slightly higher than the Tele ambient tone — gives an intimate "amp in the room" feel without an external reverb plugin doing heavy lifting |
| Mic | **Condenser 414** | Detailed and airy — adds note definition and articulation that the 490R's inherent warmth would otherwise round off. The ribbon would push this too dark. |

### 3. UADx LA-2A Silver Compressor — optical sustain

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 30 | Very light optical compression — less than the Tele tone because the 490R neck is already smooth and even; this is sustain-oriented, not corrective |
| Gain | 50 | Makeup |
| Mode | **Compress** (3:1) | Light touch; preserves jazz picking dynamics |

*The 490R is a balanced, medium-output pickup — it doesn't need much taming. Keep compression gentle enough that the natural dynamics of the neck pickup come through.*

### 4. Logic Channel EQ — humbucker cleanup

| Band | Frequency | Gain | Slope / Q | Purpose |
|------|-----------|------|-----------|---------|
| High-pass | 100 Hz | 12 dB/oct | — | Remove low-end rumble; higher than Tele (90Hz) because the LP has more natural bass bloom |
| Peak | 280 Hz | −2 dB | Q: 0.8 | Reduce the "wooly" low-mid buildup typical of neck humbuckers in a jazz context |

*No presence boost — the Condenser 414 handles that. No high-cut — the Normal mode Showtime '64 already rolls off the top naturally.*

### 5. Logic Space Designer — small room ambience

| Control | Setting | Purpose |
|---------|---------|---------|
| IR | Room category — small studio or small hall | Close, present acoustic space — not a plate or concert hall |
| Predelay | 5 ms | Keeps the dry note attack first; room ambience follows immediately behind |
| Size | 70% | Short, tight space — 70% of original IR size |
| Lo Spread | 60% | Modest stereo width on low frequencies |
| Hi Spread | 60% | Modest stereo width on high frequencies — consistent width across the spectrum |
| Dry | 0.0 dB | Dry signal at unity |
| Wet | −22 dB | ~8% wet — just enough physical space, not a reverb effect |

*No Q setting needed on the Space Designer's own controls. If −22 dB feels too dry, lower Wet in 2 dB increments (−20 dB ≈ 10%, −16.5 dB ≈ 15%). This tone lives in the −26 to −20 dB Wet range. Wetter than −16.5 dB crosses from "intimate studio" into "reverb effect" and defeats the brief.*

---

## Starting Point Guide

- **First adjustment**: Space Designer Wet fader — −22 dB is the floor (~8%). If the dry guitar sounds too "DAW flat," go to −20 dB (~10%). If it starts sounding roomy, come back down toward −24 dB.
- **Key interaction**: Condenser 414 + Channel EQ 280Hz cut. These two together define the tone's balance — the 414 adds air and definition, the 280Hz cut removes the LP's natural wooliness. If notes feel too thick and undefined, deepen the 280Hz cut to −3dB. If the tone feels too thin or bright, swap to Ribbon 160 and remove the 280Hz cut.
- **Tone King Volume**: Primary warmth lever. Vol 3 is clean and pristine; push to 4–5 for more body and harmonic color from the Rhythm channel.
- **Variations**:
  - Slightly warmer and rounder: swap Condenser 414 → Ribbon 160, reduce 280Hz cut to −1dB
  - More archtop-forward presence: add +1.5dB at 1.2kHz, Q: 1.5 in Channel EQ to emphasize the LP's hollow midrange characteristic

---

## Feedback History

### 2026-04-18 — tested
Confirmed. Tone holds up in play — no changes needed. Note: Showtime '64 may have been loaded inside Paradise Guitar Studio rather than as a standalone plugin; all settings identical, different cab sim used. Signal chain documentation unchanged.

### 2026-04-16 — initial
Built targeting jazz box intimacy — Henriksen Blu / archtop reference. Les Paul Studio with 490R neck pickup. Showtime '64 chosen for its neutral transparent character (avoids stacking Blackface color on top of Tone King Rhythm). Condenser 414 chosen over Ribbon 160 to add note definition that the 490R's warmth would otherwise round off. Space Designer at 8% for minimal, present-feeling ambience only.
