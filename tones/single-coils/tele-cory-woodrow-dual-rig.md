---
amp: "Archetype Cory Wong X + Woodrow '55 (UADx)"
created: 2026-08-08
guitar: "Fender Player II Telecaster / Squier Stratocaster (Single-Coils)"
id: tele-cory-woodrow-dual-rig
pickup_type: single-coil
preset_name: "Cory Woodrow Dual Rig SC"
status: initial
tags: "dual-amp, single-coil, telecaster, stratocaster, neural-dsp, cory-wong, woodrow, tweed, clean-machine, parallel"
target: 'High-contrast dual rig pairing pristine solid-state precision (Cory Wong Clean Machine) with organic 1950s tube sag and saturation (Woodrow 55 Tweed).'
tone-king-channel: bypassed
updated: 2026-08-08
dual_rig: true
amp_a:
  name: "Amp A — Archetype Cory Wong X (Clean Machine)"
  model: "The Clean Machine (Archetype Cory Wong X)"
  platform: neural_dsp
  pan: -12
  amp_settings:
    selectedAmp: 0
    cleanBass: 5.0
    cleanMid: 5.5
    cleanTreble: 6.0
    cleanVolume: 5.0
    cleanMaster: 6.5
    cleanCut: 0.0
    compressorActive: true
    compressorVolume: 50.0
    compressorCompression: 30.0
amp_b:
  name: "Amp B — Woodrow '55 (Tweed Saturation)"
  model: "Woodrow '55 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 5.4
    Tone: 5.8
    Boost: false
    Cab: "1x12 Tweed Deluxe"
    Output Gain: 10.0
shared_fx:
  la2a:
    gain: 30.0
    peak_reduction: 38.0
  hitsville:
    decay: 2.0
    mix: 0.12
    pre_delay: 10.0
---

# Archetype Cory Wong X + Woodrow '55 — Hi-Fi & Tweed Dual Rig (Single-Coils)

## Target Sound

This dual-rig toneprint pairs two completely contrasting amplifier architectures to create a dynamic, 3D soundstage for single-coil guitars (**Fender Telecaster** and **Squier Stratocaster**):

* **Amp A (Left, Pan -12 — Hi-Fi Solid-State Precision)**: **Archetype Cory Wong X — "The Clean Machine"** provides hyper-articulate, ultra-fast transient pick response, pristine top-end air, and 100% linear clean headroom with zero tube distortion.
* **Amp B (Right, Pan +12 — Vintage Tweed Tube Sag)**: The **UAD Woodrow '55** (5E3 Tweed Deluxe) supplies organic tube compression, woody lower-mid body, and soft edge-of-breakup saturation.

Together, soft fingerpicking receives crystalline string clarity on the left, while aggressive pick attack makes the right channel bloom into raw Tweed tube crunch without muddying the low end.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Parallel Amp Configuration

#### Channel Strip A: Archetype Cory Wong X — Clean Machine (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Amplifier | **The Clean Machine** | Ultra-transparent clean platform |
| Volume | **5.0** | Pristine headroom |
| Master | **6.5** | Dynamic power section response |
| Treble | **6.0** | Crystalline top-end jangle |
| Mid | **5.5** | Balanced R&B/funk midrange |
| Bass | **5.0** | Tight, uncompressed low-end |
| 4th Pos Compressor | **On (Vol 50, Comp 30)** | Smooths out single-coil pick spikes |

#### Channel Strip B: Woodrow '55 — Tweed Tube Saturation (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **5.4** | Edge-of-breakup Tweed tube saturation |
| Tone | **5.8** | Bright top-end air to complement Amp A |
| Boost | **Off** | Linear dynamic response |
| Cab | **1x12 5E3** | Stock 12" Jensen P12R speaker |
| Output Gain | **10.0 dB** | Levels plugin output to match Amp A |

---

### 3. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Metering**: Solo Amp A and Amp B independently using Logic's Loudness Meter. Adjust Amp B output so both read **-20.0 Short-Term LUFS**.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **38.0**, Gain **30.0**) on the submix bus pulling **-1.5 dB GR** on strum peaks.
* **Spatial Reverb**: UAD Hitsville Chambers (Mix **12%**, Pre-Delay **10ms**) on parallel aux send.

---

## Starting Point Guide

- **Telecaster Pickup Selector**: Position 2 (Middle - Neck + Bridge) gives ultra-funky R&B rhythm snap on Amp A with warm Tweed body on Amp B.
- **Stratocaster Position 4**: Position 4 (Neck + Middle) yields classic Mayer/Wong neo-soul chime across both channels.
