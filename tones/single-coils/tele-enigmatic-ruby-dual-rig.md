---
amp: "Enigmatic '82 + Ruby '63 (UADx)"
created: 2026-08-17
guitar: "Fender Player II Telecaster (Single-Coils)"
id: tele-enigmatic-ruby-dual-rig
pickup_type: single-coil
preset_name: "Tele Enigmatic Ruby Dual Rig SC"
status: tested
tags: "dual-amp, telecaster, single-coil, dumble, vox, enigmatic, ruby, sustain, chime, parallel"
target: 'Boutique dual rig pairing Dumble liquid sustain (Enigmatic 82) with Vox Top Boost harmonic chime (Ruby 63) for Telecaster single-coils.'
tone-king-channel: bypassed
updated: 2026-08-17
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

# Enigmatic '82 + Ruby '63 — Telecaster Dual Rig (Single-Coils)

## Target Sound

This toneprint adapts **Approach 2 (Dumble Liquid Sustain + Vox Harmonic Chime)** from our [Parallel Dual-Amp Guide](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/PARALLEL_AMP_GUIDE.md) specifically for the **Fender Player II Telecaster** (and single-coil guitars).

* **Amp A (Left, Pan -12)**: The **UAD Enigmatic '82** (ODS Dumble style) provides smooth, compressed lower-midrange sustain, vocal warmth, and touch-sensitive dynamics, fattening up the Telecaster's single coils without masking note definition.
* **Amp B (Right, Pan +12)**: The **UAD Ruby '63** (Vox AC30 Top Boost) supplies bell-like high-end chime, upper-mid bite, and fast transient pick attack.

Single-coil pickups deliver extraordinary clarity and cut through this setup, maintaining a wide, 3D stereo image with zero harshness.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Primary Guitar Input Track (Pre-Split Drive & Calibration)

* **Interface Calibration Offset**: Logic Utility Gain trim set to **-3.2 dB** (compensating for iD14's +9.0 dBu clipping point vs UAD's +12.2 dBu standard).
* **Pre-Split Drive Insertion**: Place **Nembrini Clon Minotaur** (Klon) or **Kuassa Efektor Blues Barker** (Bluesbreaker) directly on the **Guitar Input Track** (pre-split).
  * *Why*: Feeding overdrive into both Amp A and Amp B simultaneously preserves stereo balance and causes both amps to saturate harmonically together, completely avoiding the lopsided level and tonal drift of single-amp drive.

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **Nembrini Clon Minotaur** | Gain / Treble / Output | **6.0 / 4.5 / 4.5** | Transparent midrange boost and singing lead sustain across both amps |
| **Kuassa Efektor Blues Barker** | Gain / Tone / Level | **3.5 / 5.0 / 2.75** | Smooth, dynamic low-gain blues breakup across both amps |

---

### 3. Parallel Amp Configuration (UADx Paradise / Plugin Suite)

#### Channel Strip A: Enigmatic '82 — Liquid Sustain (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **4.5** | Touch-sensitive warm clean with subtle edge-of-breakup |
| Treble | **5.0** | Smooth high-frequency response tailored for single coils |
| Middle | **5.5** | Thick, vocal midrange body |
| Bass | **5.0** | Tight, uncompressed fundamental |
| Presence | **4.5** | Gentle upper-mid control |
| Master | **6.0** | Clean power amp drive |
| Model / Voice | **Suede / Skyline** | Classic Dumble ODS voicing |
| Tone Stack | **Jazz** | Deep, flat headroom |
| Cab | **2x12 Boutique D65** | Warm boutique cab voicing |

#### Channel Strip B: Ruby '63 — Vox Top Boost Chime (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Top Boost** | Brilliant harmonic chime |
| Volume | **3.5** | Cleaned-up Top Boost sweet spot; smooth response on single coils |
| Treble | **5.5** | High-frequency jangle and string definition |
| Bass | **4.5** | Tightened low end to prevent boominess |
| Tone Cut | **4.0** | Smooths out harsh top-end glass |
| Boost | **Off** | Linear headroom |
| Cab | **2x12 Silver 15** | Vintage Vox Silver Bulldog cab |
| Output Gain | **8.0 dB** | Trimmed -4.0 dB inside Paradise plugin to match Enigmatic and allow Logic fader at -3.8 dB |

---

### 4. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Metering**: Solo Amp A and Amp B independently using Logic's Loudness Meter. Adjust Amp B output so both read **-20.0 Short-Term LUFS**.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **40.0**, Gain **30.0**) on the parallel submix bus pulling **-1.5 to -3.0 dB GR** on strum peaks.
* **Spatial Reverb**: UAD Hitsville / Capitol Chambers (Mix **12%**, Decay **2.0s**) on parallel aux send.

---

## Starting Point Guide

- **Tele Pickup Positions**:
  - **Position 2 (Middle — Neck + Bridge)**: Rich, balanced acoustic-like chime with rich low-mid support.
  - **Position 3 (Neck)**: Deep, woody jazz/blues lead tone with blooming Dumble sustain.
- **Drive Staging**: Engage the Clon or Blues Barker on the **Guitar Input Track** to push both amps into singing overdrive simultaneously.
- **Spectrum Balance**: If the Telecaster bridge pickup has excessive bite on the Ruby side, increase Ruby `Tone Cut` to **5.0** or **5.5**.

---

## Feedback History

### 2026-08-17 — tested
* **Telecaster Testing**: Verified with Fender Player II Telecaster. The Enigmatic '82 + Ruby '63 dual-amp pairing proved outstanding for single coils, giving the Telecaster huge vocal sustain on the Enigmatic side while retaining Vox Top Boost harmonic sparkle on the Ruby side.
* **Pre-Split Input Track Drive Staging**: Confirmed high utility of inserting overdrive pedals (Nembrini Clon Minotaur, Kuassa Blues Barker) directly on the primary Guitar Input channel strip (following the -3.2 dB calibration trim). Feeding the driven signal pre-split into both amps keeps the stereo image perfectly centered and balanced, avoiding the lopsided dynamic imbalance of driving only one amp channel.
