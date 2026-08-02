---
amp: "Woodrow '55 + Dream '65 (UADx)"
created: 2026-08-02
guitar: "Fender Player II Telecaster (Single-Coils)"
id: tele-woodrow-dream-dual-rig
pickup_type: single-coil
preset_name: "Tele Woodrow Dream Dual Rig SC"
status: initial
tags: "dual-amp, telecaster, single-coil, tweed, blackface, woodrow, dream-65, chris-buck, parallel"
target: 'Chris Buck-inspired Telecaster dual rig balancing woody Tweed edge-of-breakup mids (Woodrow 55) with pristine Fender Blackface glass (Dream 65).'
tone-king-channel: bypassed
updated: 2026-08-02
dual_rig: true
amp_a:
  name: "Amp A — Woodrow '55 (Tweed Breakup)"
  model: "Woodrow '55 (UADx)"
  platform: uad_paradise
  pan: -12
  amp_settings:
    Volume: 5.2
    Volume (Mic): 0.0
    Treble: 5.8
    Boost: false
    Cab: "1x12 Tweed Deluxe"
amp_b:
  name: "Amp B — Dream '65 (Blackface Clean)"
  model: "Dream '65 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 2.5
    Treble: 5.5
    Bass: 5.0
    Bright: false
    Reverb: 0.0
    Cab: "2x12 JBF120"
shared_fx:
  la2a:
    gain: 28.0
    peak_reduction: 25.0
  hitsville:
    decay: 1.8
    mix: 0.10
    pre_delay: 8.0
---

# Woodrow '55 + Dream '65 — Telecaster Dual Rig (Single-Coils)

## Target Sound

This toneprint implements **Approach 1 (Tweed Mid-Punch + Blackface Glass)** from our [Parallel Dual-Amp Guide](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/PARALLEL_AMP_GUIDE.md), optimized for the **Fender Player II Telecaster**.

Inspired by **Chris Buck (Cardinal Black)**, this setup pairs a warm, woody Tweed Deluxe right at the edge of breakup with a pristine, uncompressed Blackface Deluxe Reverb clean foundation.

* **Amp A (Left, Pan -12)**: **UAD Woodrow '55** delivers organic Tweed compression, raw midrange punch, and dynamic sag when picking aggressively.
* **Amp B (Right, Pan +12)**: **UAD Dream '65** stays wide open and clean, ensuring pick attacks, string separation, and high-frequency sparkle are preserved.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Parallel Amp Configuration (UADx Paradise / Plugin Suite)

#### Channel Strip A: Woodrow '55 — Tweed Edge-of-Breakup (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Instrument Volume | **5.2** | Edge of breakup; cleans up when picking lightly |
| Mic Volume | **0.0** | Independent channel isolation |
| Tone | **5.8** | Warm, woody midrange with smooth high roll-off |
| Boost | **Off** | Preserves touch-sensitive dynamics |
| Cab | **1x12 5E3** | Stock 12" Jensen P12R speaker |

#### Channel Strip B: Dream '65 — Blackface Glass (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **2.5** | 100% clean headroom; zero distortion |
| Treble | **5.5** | Crystalline top-end sparkle for Tele bridge/neck |
| Bass | **5.0** | Tight, controlled bottom end |
| Bright Switch | **Normal** | Prevents harsh Telecaster ice-pick treble |
| Cab | **2x12 JBF120** | JBL D120F cab for wide 3D air |

---

### 3. Parallel Submix Bus & Level Parity

* **Loudness Meter Parity**: Level Amp A and Amp B to match at **-20.0 Short-Term LUFS**. Trim Woodrow output fader slightly (-1.5 dB) if Tweed compression causes level runaway.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **25.0**, Gain **28.0**) for gentle submix glue.
* **Spatial Ambience**: UAD Hitsville Chambers (Mix **10%**, Pre-Delay **8ms**).

---

## Starting Point Guide

- **Pickup Selector**: Start on **Position 2 (Neck + Bridge parallel)** or **Neck pickup** for soulful blues and fingerstyle rhythm.
- **Dynamic Control**: Use pick attack to drive the Woodrow into crunch while the Dream stays crystal clear.
- **Drive Pedal Pairing**: Run a TS-808 (Nembrini 808) into **Amp A only** for searing lead tone while keeping **Amp B** clean.
