---
amp: "Dream '65 + Enigmatic '82 (UADx)"
created: 2026-08-18
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (Humbuckers)"
id: paradise-dream-enigmatic-dual-rig
pickup_type: humbucker
preset_name: "Dream Enigmatic Dual Rig HB"
status: tested
tags: "dual-amp, humbucker, les-paul, dumble, dream, deluxe-reverb, enigmatic, ods, blackface, spring-reverb, warm-clean, parallel"
target: 'Vintage boutique dual rig pairing spongy 6V6 Deluxe Reverb clean bloom and spring reverb (Dream 65) with thick Dumble ODS vocal sustain (Enigmatic 82) for humbuckers.'
tone-king-channel: bypassed
updated: 2026-08-18
dual_rig: true
amp_a:
  name: "Amp A — Dream '65 (Vintage Deluxe Reverb Bloom)"
  model: "Dream '65 (UADx)"
  platform: uad_paradise
  pan: -12
  amp_settings:
    Volume: 4.0
    Treble: 4.8
    Bass: 4.5
    Bright: false
    Reverb: 2.2
    Boost: false
    Cab: "1x12 EV12"
    Output Gain: 8.0
amp_b:
  name: "Amp B — Enigmatic '82 (Dumble ODS Vocal Mids)"
  model: "Enigmatic '82 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 4.5
    Treble: 5.0
    Middle: 5.8
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
    mix: 0.10
    pre_delay: 10.0

    wet_solo: false
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

# Dream '65 + Enigmatic '82 — Vintage Deluxe & ODS Dual Rig (Humbuckers)

## Target Sound

This dual-rig toneprint pairs two legendary American tube voices for humbucker guitars (**Gibson Les Paul Studio** and **Epiphone Sheraton II**), blending vintage small-club warmth with boutique high-gain refinement:

* **Amp A (Left, Pan -12 — Dream '65 Deluxe Reverb Foundation)**: Delivers warm 6V6 power amp sag, a pillowy bottom end, gentle blooming compression, and lush tube-driven spring reverb (pulled back to **2.2** for optimal mix definition). Paired with the **1x12 EV12** cabinet to keep humbucker low-end tight, fast, and articulate.
* **Amp B (Right, Pan +12 — Enigmatic '82 Dumble ODS Singing Mids)**: Provides rich 800 Hz–2 kHz vocal midrange sustain, smooth overdrive compression, and touch-sensitive harmonic bite.

The Dream '65 gives chords an organic, three-dimensional acoustic bloom and sweet top end, while the Enigmatic ensures single-note leads sing with thick, creamy Dumble sustain.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Pre-Split Overdrive Staging (Guitar Input Track)

Tested and dialed specifically for humbuckers pushing the parallel amp pair:

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **Nembrini Clon Minotaur** | Gain / Treble / Output | **2.2 / 4.6 / 6.1** | Transparent low-gain push; lifts amp front-end without mid-hump congestion |
| **Nembrini NA 808** | Drive / Tone / Level | **2.0 / 3.9 / 4.1** | Low-drive vocal boost; smooth rounded top end |
| **Kuassa Blues Barker** | Gain / Tone / Level | **2.9 / 5.5 / 3.3** | Transparent Bluesbreaker dynamic crunch with open upper-mid bite |

---

### 3. Parallel Amp Configuration (UADx Paradise / Plugin Suite)

#### Channel Strip A: Dream '65 — Vintage Deluxe Reverb Bloom (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **4.0** | Clean edge-of-bloom sweet spot for humbuckers |
| Treble | **4.8** | Smooth high-frequency sheen without bright cap harshness |
| Bass | **4.5** | Controlled low end to prevent 6V6 mud on neck humbucker |
| Bright | **Off** | Warmer, rounder tone stack response |
| Reverb | **2.2** | Tuned spring reverb level — provides transient "gloss" without muddying bus reverb |
| Boost | **Off (Stock)** | Preserves clean headroom |
| Cab | **1x12 EV12** | High-headroom EVM-12L speaker keeps humbucker bass tight and punchy |
| Output Gain | **8.0 dB** | Trimmed to match Enigmatic channel level |

#### Channel Strip B: Enigmatic '82 — Dumble ODS Vocal Mids (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **4.5** | Touch-sensitive warm overdrive |
| Treble | **5.0** | Articulate high-end extension |
| Middle | **5.8** | Thick vocal core filling the Deluxe Reverb's natural mid-scoop |
| Bass | **4.8** | Tight low-end response |
| Presence | **4.5** | Upper-harmonic clarity |
| Master | **6.0** | Power section saturation and sustain |
| Model / Voice | **Suede / Skyline** | Classic Dumble ODS voicing |
| Tone Stack | **Jazz** | Deep, uncompressed headroom |
| Cab | **2x12 Boutique D65** | Two-Rock Celestion G12-65 response |
| Output Gain | **8.0 dB** | Level matched for stereo parity |

---

### 4. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Metering**: Solo Amp A and Amp B independently using Logic's Loudness Meter. Confirm both read **-20.0 Short-Term LUFS**.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **40.0**, Gain **30.0**) pulling **-1.5 to -2.5 dB GR** to glue the parallel soundstage.
* **Spatial Reverb**: UAD Hitsville / Capitol Chambers (Mix **10%**, Decay **2.0s**, Pre-Delay **10ms**) on parallel aux send (kept at 10% to complement the Dream's onboard spring reverb).

---

## Starting Point Guide

- **Spring vs. Room Reverb Balance**: With the Dream '65 spring reverb tuned to **2.2**, it provides mechanical string rattle and transient smoothing on the left channel, while the Hitsville bus reverb (10% mix) creates the 3D room glue across the stereo field.
- **Overdrive Staging**: Place a Klon (Nembrini Clon Minotaur), 808 (Nembrini NA 808), or Bluesbreaker (Kuassa Efektor Blues Barker) on the **Guitar Input Track** (pre-split). Pushing low-drive boosts with higher output levels preserves the Deluxe Reverb's clean bloom while driving the Enigmatic into thick, singing Dumble saturation.
- **Neck Humbucker Clarity**: If the neck pickup feels too dark, flip the Dream '65 Bright switch to **On** or switch the Cab to the **2x12 JBF120 (Twin JBLs)**.

---

## Feedback History

### 2026-08-18 — tested
* **Reverb Calibration**: Adjusted Dream '65 onboard spring reverb from 2.8 down to **2.2** based on session listening. Eliminates low-mid wash while preserving authentic mechanical spring transient gloss.
* **Pre-Split Drive Calibration**: Encoded fine-tuned pedal settings ("Showtime Enigmatic Tuning"):
  - **Nembrini Clon Minotaur**: Gain 2.2, Treble 4.6, Output 6.1 (transparent clean boost driving front-end headroom).
  - **Nembrini NA 808**: Drive 2.0, Tone 3.9, Level 4.1 (smooth low-gain vocal push).
  - **Kuassa Blues Barker**: Gain 2.9, Tone 5.5, Level 3.3 (open Bluesbreaker texture).
* Recompiled presets for Amp A, Amp B, Submix Bus, and all three overdrive pedals.
