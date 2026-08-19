---
amp: "Showtime '64 + Enigmatic '82 (UADx)"
created: 2026-08-18
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (Humbuckers)"
id: paradise-showtime-enigmatic-dual-rig
pickup_type: humbucker
preset_name: "Showtime Enigmatic Dual Rig HB"
status: tested
tags: "dual-amp, humbucker, les-paul, dumble, showtime, showman, enigmatic, ods, sss, high-headroom, vocal-mids, parallel"
target: 'High-headroom American dual rig pairing piano-like clean punch and tight low-end (Showtime 64) with Dumble ODS thick vocal sustain (Enigmatic 82) for humbuckers.'
tone-king-channel: bypassed
updated: 2026-08-18
dual_rig: true
amp_a:
  name: "Amp A — Showtime '64 (High-Headroom Clean Anchor)"
  model: "Showtime '64 (UADx)"
  platform: uad_paradise
  pan: -12
  amp_settings:
    Volume: 3.8
    Treble: 5.0
    Middle: 5.5
    Bass: 4.8
    Bright: false
    Room: 2.5
    Mic: "Ribbon 160"
    Cab: "2x12 Showman (UADx)"
    Output Gain: 8.0
amp_b:
  name: "Amp B — Enigmatic '82 (Dumble ODS Vocal Mids)"
  model: "Enigmatic '82 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 4.5
    Treble: 5.0
    Middle: 6.0
    Bass: 4.8
    Presence: 4.5
    Master: 6.0
    Bright: true
    Voice: Suede
    Cab: "2x12 Boutique D65"
    Output Gain: 8.0
shared_fx:
  la2a:
    gain: 30.0
    peak_reduction: 40.0
  hitsville:
    decay: 2.0
    mix: 0.12
    pre_delay: 10.0
  kuassa_blues_barker:
    gain: 2.86
    tone: 5.54
    level: 3.33
  nembrini_808:
    drive: 2.0
    tone: 3.9
    level: 4.1
  clon_minotaur:
    gain: 2.2
    treble: 4.6
    output: 6.1
---

# Showtime '64 + Enigmatic '82 — SSS & ODS Boutique Dual Rig (Humbuckers)

## Target Sound

This dual-rig toneprint implements the iconic **Steel String Singer (SSS) + Overdrive Special (ODS)** boutique architecture inspired by John Mayer, Stevie Ray Vaughan, and Robben Ford, tailored specifically for humbucker guitars (**Gibson Les Paul Studio** and **Epiphone Sheraton II**).

* **Amp A (Left, Pan -12 — Showtime '64 High-Headroom Foundation)**: Emulates the muscular, high-power 6L6 Showman circuit (the direct historical ancestor of the Dumble SSS). It provides an unyielding, piano-like low end and glassy upper-register clarity that never sags, mushes, or flubs out under hot neck-humbucker pick attack.
* **Amp B (Right, Pan +12 — Enigmatic '82 Dumble ODS Singing Mids)**: Provides the creamy, compressed 800 Hz–2 kHz vocal midrange core, liquid sustain, and touch-sensitive harmonic bloom.

Together, the Showtime keeps chord fundamentals articulate and punchy, while the Enigmatic delivers soaring, violin-like sustain.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Pre-Split Overdrive Staging (Guitar Input Track)

Tested and dialed specifically for the Showtime + Enigmatic dual-rig pairing to push both amps into articulate, non-muddy crunch:

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **Nembrini Clon Minotaur** | Gain / Treble / Output | **2.2 / 4.6 / 6.1** | Transparent low-gain push; lifts amp front-end without mid-hump congestion |
| **Nembrini NA 808** | Drive / Tone / Level | **2.0 / 3.9 / 4.1** | Low-drive vocal boost; smooth rounded top end |
| **Kuassa Blues Barker** | Gain / Tone / Level | **2.9 / 5.5 / 3.3** | Transparent Bluesbreaker dynamic crunch with open upper-mid bite |

---

### 3. Parallel Amp Configuration (UADx Paradise / Plugin Suite)

#### Channel Strip A: Showtime '64 — High-Headroom Clean Anchor (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **3.8** | Massive clean headroom with instant dynamic response |
| Treble | **5.0** | Clear, smooth top end without harshness |
| Middle | **5.5** | Fills the traditional blackface scoop to keep humbucker body solid |
| Bass | **4.8** | Tightened low end to prevent boominess on neck pickup |
| Bright | **Off (Normal)** | Keeps high-end warm and rounded for humbuckers |
| Room | **2.5** | Subtle studio ambient depth |
| Mic / Cab | **Ribbon 160 / 2x12 Showman** | Smooth ribbon mic warmth taming transient spikes |
| Output Gain | **8.0 dB** | Aligned with Amp B for LUFS balance |

#### Channel Strip B: Enigmatic '82 — Dumble ODS Vocal Mids (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **4.5** | Touch-sensitive edge-of-breakup drive |
| Treble | **5.0** | Smooth, sweet high frequencies |
| Middle | **6.0** | Pronounced vocal midrange push (fills the Showtime's spectral pocket) |
| Bass | **4.8** | Tight low-end contour |
| Presence | **4.5** | Gentle upper-harmonic lift |
| Master | **6.0** | Power section harmonic saturation |
| Model / Voice | **Suede / Skyline** | Classic Dumble ODS voicing |
| Tone Stack | **Jazz** | Flat, articulate frequency response |
| Cab | **2x12 Boutique D65** | Two-Rock style Celestion G12-65 response |
| Output Gain | **8.0 dB** | Level matched for stereo balance |

---

### 4. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Metering**: Solo Amp A and Amp B independently using Logic's Loudness Meter. Confirm both read **-20.0 Short-Term LUFS**.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **40.0**, Gain **30.0**) pulling **-1.5 to -2.5 dB GR** on strum peaks to glue the stereo image.
* **Spatial Reverb**: UAD Hitsville / Capitol Chambers (Mix **12%**, Decay **2.0s**, Pre-Delay **10ms**) on parallel aux send.

---

## Starting Point Guide

- **Guitar Volume Control**: Set Les Paul neck pickup to **7.5–8.0** for articulate rhythm playing; push to **10** to make the Enigmatic side jump into liquid lead sustain.
- **Drive Staging (Input Track Insertion)**: Place the Bluesbreaker (Kuassa Efektor Blues Barker), Clon (Nembrini Clon Minotaur), or NA 808 directly on the **Guitar Input Track** (pre-split). Pushing low-drive boosts with higher output levels (Output ~6.1 on Clon, Level ~4.1 on 808) preserves the unyielding clean punch of the Showtime while driving the Enigmatic into thick, singing sustain.
- **Midrange Fine-Tuning**: If the rig feels too mid-heavy with humbuckers, pull the Showtime's `Middle` down to **4.5** to create a deeper valley for the Enigmatic's vocal core.

---

## Feedback History

### 2026-08-18 — tested
* **Tuning Confirmation**: Tested with Les Paul humbuckers. Showtime '64 and Enigmatic '82 settings confirmed spot-on.
* **Pre-Split Drive Calibration**: Encoded fine-tuned pedal settings ("Showtime Enigmatic Tuning"):
  - **Nembrini Clon Minotaur**: Gain 2.2, Treble 4.6, Output 6.1 (transparent clean boost driving front-end headroom).
  - **Nembrini NA 808**: Drive 2.0, Tone 3.9, Level 4.1 (smooth low-gain vocal push).
  - **Kuassa Blues Barker**: Gain 2.9, Tone 5.5, Level 3.3 (open Bluesbreaker texture).
* Recompiled presets for Amp A, Amp B, Submix Bus, and all three overdrive pedals.
