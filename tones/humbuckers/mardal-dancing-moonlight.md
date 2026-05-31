---
id: "mardal-dancing-moonlight"
created: "2026-05-02"
updated: "2026-05-16"
guitar: Epiphone Sheraton (humbuckers)
target: "\"Rebecca Mardal \\"Dancing in the Moonlight\\" \u2014 warm jazz clean with lush-not-ambient\"
tags: "jazz, clean, warm, lush, semi-hollow, neo-soul, neural-dsp"
tone-king-channel: rhythm
amp: "Amp Snob, Tone King Imperial Preamp"
status: tested
pickup_type: humbucker
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    compressorBlend: 0.55
    compressorCompression: 0.40
    compressorVolume: 2.50
    selectedAmp: 2
    selectedCab: 2
    ampCabLinkedState: false
    snobMid: 0.70
    snobTreble: 0.40
    snobPresence: 0.30
    snobVolume: 2.50
    snobBright: false
    leftCabPosition: 0.50
    leftCabDistance: 0.22
    leftCabActive: true
    leftCab0MicType: 4
    rightCabActive: false
    snobEQHpf: 20.0
    snobEQLpf: 20000.0
    tuberActive: false
    bigRigActive: false
    postalActive: false
    delayActive: false
    washActive: false
    chorusActive: false
  logic_compressor:
    ratio: 2026
    attack: 55
    makeup_gain: 2026
---

# Mardal "Dancing in the Moonlight"

## Target Sound
The goal is a warm, round, and clean tone where the Sheraton's natural semi-hollow bloom does most of the heavy lifting. The reverb should be musical and audible when you lift your fingers, but sit firmly behind the note rather than washing it out.

The Cory Wong X amp adds back the mids that the Tone King's Fender-style tonestack naturally scoops, creating a rich, vocal midrange.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Clean blackface platform |
| Volume | 2.5 | Minimal coloring; acts as a warm buffer |
| Attenuation | 5 | Nominal output |
| IR | Bypassed | Neural DSP provides the cab |

---

### 2. Archetype Cory Wong X: Pre FX — 4th Position Compressor

| Control | Setting | Purpose |
|---------|---------|---------|
| Active | On | |
| Blend | 55% | Preserves some direct attack |
| Compression | 40% | Evens out pick attack, adds sustain |

---

### 3. Archetype Cory Wong X: Amp — The Clean Machine

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Type | Clean | |
| Volume | 30% | High headroom |
| Bright | Off | Warm jazz focus |
| Middle | 70% | **Key call:** Fills in the midrange for a vocal jazz character |
| Treble | 40% | Smooth rolloff |
| Presence | 30% | Keeps the power amp warm |

---

### 4. Archetype Cory Wong X: Cab — Ribbon 121

| Control | Setting | Purpose |
|---------|---------|---------|
| Mic Type | Ribbon 121 | Warm, dark character |
| Position | 0.50 | Balanced response |
| Distance | 0.22 | Slight air around the speaker |
| Output Trim | −7.5 dB | Plugin output trim — calibrated 2026-05-16 to hit −12 dBFS |
| Room Send | −12.0 dB | Reduced from −3.0 dB; previous value was too hot/washed |

---

### 5. Archetype Cory Wong X: Post FX — The Wash (Reverb)

| Control | Setting | Purpose |
|---------|---------|---------|
| Active | On | |
| Mix | 10% | Subtle; sits well behind the dry signal |
| Shimmer | Off | Keeps it grounded in jazz |
| Decay | 55% | Medium tail |
| Low Cut | 27% | Prevents mud in the low-end |
| High Cut | 60% | Warm tails |

---

## Starting Point Guide

- **Reverb Weight**: If 10% Mix feels too dry, try 15%. Do not go above 20% or the notes will start to blur.
- **Midrange Balance**: The **Middle 70%** setting is crucial. If the tone feels too "thin," increase this. If it feels too "boxy," pull it back toward 50%.

---

## Feedback History

### 2026-05-16 — gain staging calibration (direct to iD14)
Signal path changed: guitar now routes direct into iD14 instrument input (Tone King Imperial Preamp bypassed pending its own calibration pass). iD14 gain set to **0**. Guitar bus changed to **Mono** (was Stereo). Archetype Cory Wong X **Output Trim set to −7.5 dB** to hit −12 dBFS target. **Room Send reduced from −3.0 dB to −12.0 dB** — the previous −3 dB was producing too much room wash with the direct signal path.

### 2026-05-02 — tested
Confirmed tested in previous version of this skill. Status updated to tested.

### 2026-05-02 — recreated
Recreated from legacy "Mardal Dancing in the Moonlight" print. Sheraton II focused. Uses Archetype Cory Wong X for the "Clean Machine" amp and its integrated spatial effects.
