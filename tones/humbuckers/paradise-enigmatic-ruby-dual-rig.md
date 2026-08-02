---
amp: "Enigmatic '82 + Ruby '63 (UADx)"
created: 2026-08-02
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (Humbuckers)"
id: paradise-enigmatic-ruby-dual-rig
pickup_type: humbucker
preset_name: "Enigmatic Ruby Dual Rig HB"
status: tested
tags: "dual-amp, humbucker, dumble, vox, enigmatic, ruby, sustain, chime, parallel"
target: 'Boutique dual rig pairing Dumble liquid sustain (Enigmatic 82) with Vox Top Boost harmonic chime (Ruby 63) for humbucker guitars.'
tone-king-channel: bypassed
updated: 2026-08-02
dual_rig: true
amp_a:
  name: "Amp A — Enigmatic '82 (Liquid Sustain)"
  model: "Enigmatic '82 (UADx)"
  platform: uad_paradise
  pan: -12
  amp_settings:
    Volume: 4.5
    Treble: 5.0
    Middle: 5.5
    Bass: 5.0
    Presence: 4.5
    Master: 6.0
    Bright: true
    Voice: Suede
    Cab: "2x12 Boutique D65"
amp_b:
  name: "Amp B — Ruby '63 (Vox Chime)"
  model: "Ruby '63 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 3.5
    Treble: 5.5
    Bass: 4.5
    Tone Cut: 4.0
    Cut: false
    Boost: false
    Cab: "2x12 Silver 15"
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
    gain: 3.5
    tone: 5.0
    level: 2.75
  kuassa_blues_river:
    gain: 3.0
    tone: 5.0
    level: 2.2
  clon_minotaur:
    gain: 6.0
    treble: 4.5
    output: 4.5
  nembrini_808:
    drive: 5.4
    tone: 5.0
    level: 3.5
---

# Enigmatic '82 + Ruby '63 — Boutique Dual Rig (Humbuckers)

## Target Sound

This toneprint implements **Approach 2 (Dumble Liquid Sustain + Vox Harmonic Chime)** from our [Parallel Dual-Amp Guide](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/PARALLEL_AMP_GUIDE.md), tailored specifically for humbucker guitars (**Gibson Les Paul Studio** and **Epiphone Sheraton II**).

* **Amp A (Left, Pan -12)**: The **UAD Enigmatic '82** (ODS Dumble style) provides smooth, compressed lower-midrange sustain, vocal warmth, and touch-sensitive dynamics.
* **Amp B (Right, Pan +12)**: The **UAD Ruby '63** (Vox AC30 Top Boost) supplies bell-like high-end chime, upper-mid bite, and fast transient pick attack.

Together, they eliminate humbucker dark mud while giving single notes a soaring, singing lead quality inspired by John Mayer and Robben Ford.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Parallel Amp Configuration (UADx Paradise / Plugin Suite)

#### Channel Strip A: Enigmatic '82 — Liquid Sustain (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **4.5** | Touch-sensitive warm clean with subtle edge-of-breakup |
| Treble | **5.0** | Smooth high-frequency response |
| Middle | **5.5** | Thick, vocal midrange body |
| Bass | **5.0** | Tight, uncompressed fundamental |
| Presence | **4.5** | Gentle upper-mid control |
| Master | **6.0** | Clean power amp drive |
| Model / Voice | **Suede / Skyline** | Classic Dumble ODS voicing |
| Tone Stack | **Jazz** | Deep, flat headroom |

#### Channel Strip B: Ruby '63 — Vox Top Boost Chime (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Top Boost** | Brilliant harmonic chime |
| Volume | **3.5** | Cleaned-up Top Boost sweet spot; eliminates unwanted fuzz on thumb picking |
| Treble | **5.5** | High-frequency jangle and string definition |
| Bass | **4.5** | Tightened low end to prevent boominess |
| Tone Cut | **4.0** | Smooths out harsh top-end glass |
| Boost | **Off** | Linear headroom |
| Cab | **2x12 Silver 15** | Vintage Vox Silver Bulldog cab |
| Output Gain | **8.0 dB** | Trimmed -4.0 dB inside Paradise plugin to match Enigmatic and allow Logic fader at -3.8 dB |

---

### 3. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Metering**: Solo Amp A and Amp B independently using Logic's Loudness Meter. Adjust Amp B output so both read **-20.0 Short-Term LUFS**.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **40.0**, Gain **30.0**) on the parallel submix bus pulling **-1.5 to -3.0 dB GR** on strum peaks.
* **Spatial Reverb**: UAD Hitsville / Capitol Chambers (Mix **12%**, Decay **2.0s**) on parallel aux send.

---

## Starting Point Guide

- **Guitar Volume Knob**: Set Les Paul neck pickup volume to **8.0** for clean rhythm, and roll up to **10** for singing lead sustain.
- **Spectrum Balance**: If the Ruby dominates the right ear, roll the Ruby's `Tone Cut` up to **5.0**.
- **Drive Staging**: For leads, feed a Klon/Centaur (Clon Minotaur) into **both** amps to push Enigmatic into overdrive while keeping Ruby punchy.

---

## Feedback History

### 2026-08-02 — tested
* **User Testing**: Pairing works extremely well. Reduced Ruby Volume from 4.0 down to 3.5 to clean up unwanted fuzz/saturation when thumb picking with humbuckers while preserving Vox chime and clarity. 
* **Gain Staging Refinement**: Trimmed Ruby outer plugin output gain from +12.0 dB down to +8.0 dB inside Paradise. This allows Track 3 Logic channel strip fader to sit cleanly at -3.8 dB for fine resolution while keeping LUFS parity at -20.3 LUFS.
* **Bus Compression & Reverb Fix**: Increased LA-2A Peak Reduction to 40.0 for firmer submix glue. Fixed Hitsville preset compiler logic so Hitsville always loads in Power ON active state. Recompiled Bus LA-2A & Hitsville presets.
