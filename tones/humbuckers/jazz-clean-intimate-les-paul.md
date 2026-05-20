---
id: jazz-clean-intimate-les-paul
created: 2026-04-16
updated: 2026-05-16
guitar: Gibson Les Paul Studio (490R neck pickup)
target: "Pristine, warm jazz clean \u2014 jazz box intimacy through a transparent\
  \ high-headroom platform; close and present, no reverb wash"
tags: jazz, clean, warm, intimate, les-paul, humbucker
tone-king-channel: rhythm
amp: Showtime '64
status: tested
pickup_type: humbucker
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
| Room | 0 | Off — erroneously left at 30%; Space Designer handles the room |
| Cabinet | **2x12 (fixed)** | Showtime '64 includes only the original paired 2x12 cab — no alternative selections available |
| Mic | **Condenser 414** | Detailed and transparent; extended low and high frequency response. Adds note definition and articulation that the 490R's inherent warmth would otherwise round off. |

### 3. UADx LA-2A Silver Compressor — optical sustain

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 30 | Very light optical compression — less than the Tele tone because the 490R neck is already smooth and even; this is sustain-oriented, not corrective |
| Gain | 20 | Makeup gain — calibrated 2026-05-16; previous value of 50 confirmed clipping |
| Mode | **Compress** (3:1) | Light touch; preserves jazz picking dynamics |

### 4. Logic Space Designer — small room ambience

| Control | Setting | Purpose |
|---------|---------|---------|
| IR | Room category — small studio or small hall | Close, present acoustic space — not a plate or concert hall |
| Predelay | 5 ms | Keeps the dry note attack first; room ambience follows immediately behind |
| Size | 70% | Short, tight space — 70% of original IR size |
| Length | 103 ms | Default (367 ms) is too echo-y; 103 ms adds color and space without sounding like reverb |
| Dry | 0.0 dB | Dry signal at unity |
| Wet | −30 dB | Dialled back further during 2026-05-16 calibration — previous −22 dB was too prominent without TKIP in chain |

---

## Starting Point Guide

- **First adjustment**: Space Designer Wet fader — −22 dB is the floor (~8%). If the dry guitar sounds too "DAW flat," go to −20 dB (~10%).
- **Key interaction**: Condenser 414 + 490R neck. The 414 adds air and definition to the LP's natural warmth. If notes feel too thick, consider a small 2-3dB cut at 280Hz in Logic's Channel EQ.
- **Tone King Volume**: Primary warmth lever. Vol 3 is clean and pristine; push to 4–5 for more body and harmonic color from the Rhythm channel.

---

## Feedback History

### 2026-05-16 — gain staging calibration (direct to iD14)
Signal path changed: guitar now routes direct into iD14 instrument input (Tone King Imperial Preamp bypassed pending its own calibration pass). iD14 gain set to **0**. Guitar bus changed to **Mono** (was Stereo). Showtime '64 **Room set to 0** — was erroneously left at 30%; Space Designer handles the room, not the plugin's internal reverb. LA-2A **Gain pulled from 50 to 20** — confirmed clipping at 50 with the direct signal path; 30/20 now reads clean. Space Designer **Wet reduced to −30 dB** (from −22 dB) — the previous value felt too prominent without the TKIP's level shaping in the chain.

### 2026-05-03 — Space Designer Length corrected, status: tested
Space Designer Length was unspecified (defaulted to 367 ms) — too echo-y at that length. Setting to 103 ms brings it into "adds color and space" territory without sounding like a distinct reverb effect. Length added to the signal chain table. Status confirmed tested.

### 2026-05-02 — retitled/corrected
Corrected title and guitar specification (Les Paul Studio instead of Sheraton). Confirmed as tested.

### 2026-04-18 — tested
Confirmed. Tone holds up in play — no changes needed.

### 2026-04-16 — initial
Built targeting jazz box intimacy — Henriksen Blu / archtop reference. Les Paul Studio with 490R neck pickup. Showtime '64 chosen for its neutral transparent character (avoids stacking Blackface color on top of Tone King Rhythm). Condenser 414 chosen over Ribbon 160 to add note definition that the 490R's warmth would otherwise round off. Space Designer at 8% for minimal, present-feeling ambience only.
