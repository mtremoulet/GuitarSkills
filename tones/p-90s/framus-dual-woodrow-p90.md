---
amp: "Dual Woodrow '55 Differential (UADx)"
created: 2026-08-02
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s)"
id: framus-dual-woodrow-p90
pickup_type: p-90
preset_name: "Framus Dual Woodrow Sweet Spot P90"
status: tested
tags: "dual-amp, p-90, framus, tweed, woodrow, dual-same-amp, wet-dry, slapback, parallel"
target: 'Dual same-amp differential split pairing a dry fat Tweed (Woodrow 55) with a pushed bright slapback Tweed for Framus P-90s.'
tone-king-channel: bypassed
updated: 2026-08-08
dual_rig: true
amp_a:
  name: "Amp A — Woodrow '55 (Dry Fat Tweed)"
  model: "Woodrow '55 (UADx)"
  platform: uad_paradise
  pan: -12
  amp_settings:
    Volume: 4.6
    Tone: 4.5
    Boost: false
    Cab: "1x12 Tweed Deluxe"
amp_b:
  name: "Amp B — Woodrow '55 (Wet Saturated Tweed)"
  model: "Woodrow '55 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 6.2
    Tone: 6.5
    Boost: true
    Cab: "1x12 Tweed Deluxe"
shared_fx:
  galaxy_echo:
    feedback: 20.0
    mix: 0.25
    time: 110.0
  la2a:
    gain: 28.0
    peak_reduction: 26.0
  hitsville:
    decay: 1.6
    mix: 0.08
    pre_delay: 6.0

    wet_solo: false
---

# Dual Woodrow '55 — Framus P-90 Differential Rig

## Target Sound

This toneprint implements **Approach 4 (Dual Same-Amp Differential Split)** from our [Parallel Dual-Amp Guide](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/PARALLEL_AMP_GUIDE.md), tailored specifically for the **Framus Earl Slick Artist Series (DiMarzio P-90s)**.

By running **two instances of the UAD Woodrow '55** with differential settings and wet/dry FX separation, this rig amplifies the raw, growling character of P-90 pickups without phase mismatches or muddy frequency overlap.

* **Amp A (Left, Pan -12 - Dry Fat Tweed)**: Woodrow '55 tuned for dark, woody low-mids and clean punch. 100% bone-dry.
* **Amp B (Right, Pan +12 - Wet Bright Tweed & Slapback)**: Woodrow '55 pushed into edge-of-breakup saturation, brighter Tone contour, and fed by a vintage **UAD Galaxy Tape Echo** slapback delay (`110ms`).

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Parallel Amp Configuration (UADx Paradise / Plugin Suite)

#### Channel Strip A: Woodrow '55 — Dry Fat Tweed (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Instrument Volume | **4.6** | Clean, uncompressed punch for P-90 transients |
| Tone | **4.5** | Dark, warm midrange fundamental |
| Boost | **Off** | Linear dynamic response |
| Cab | **1x12 5E3** | Stock 12" Jensen P12R speaker |
| FX | **None (100% Dry)** | Holds down the dry center of the mix |

#### Channel Strip B: Woodrow '55 — Wet Saturated Tweed (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Instrument Volume | **6.2** | Pushed Tweed tube saturation and harmonic bloom |
| Tone | **6.5** | Bright top-end air to complement Amp A's dark tone |
| Boost | **Stock (+2 dB)** | Adds subtle gain push |
| Cab | **1x12 5E3** | Stock 12" Jensen speaker |
| Pre-FX Delay | **UAD Galaxy Tape Echo** | Slapback delay (`110ms`, Mix `25%`, Feedback `20%`) |

---

### 3. Parallel Submix Bus & Level Parity

* **Loudness Meter Parity**: Solo Amp A and Amp B; adjust faders until both read **-20.0 Short-Term LUFS**.
* **Submix Bus Glue**: UAD LA-2A Silver (Peak Reduction **26.0**, Gain **28.0**) pulling **-1.5 dB GR**.
* **Spatial Depth**: UAD Hitsville Chambers (Mix **8%**, Pre-Delay **6ms**).

---

## Starting Point Guide

- **Guitar Tone Knob**: Roll the Framus tone knob to **7.5** to round off high-end bite when playing on the bridge P-90 pickup.
- **Slapback Width**: Adjust the Galaxy Tape Echo mix on Amp B to control how far the spatial delay spreads out behind Amp A's dry fundamental.
- **Dynamic Drive**: Dig in hard with your pick to make Amp B jump into Tweed crunch while Amp A keeps your low end tight and clear.

---

## Feedback History

### 2026-08-08 — tested
* **User Testing**: Confirmed the setup sounds good with Framus P-90s. Noted that dual same-amp setups (two Woodrow '55s) are subtle and lean toward wet/dry slapback differentiation rather than distinct tonal contrast. Moving toward pairing contrasting amp families (e.g. Tweed + Dumble/Vox/Two-Rock) for stronger 3D character.
