---
amp: "Yamaha THR10II"
created: 2026-08-28
guitar: "Fender Player II Telecaster / Squier Stratocaster (single-coils)"
id: thr-hazy-thames-gold
pickup_type: single-coil
preset_name: "THR Hazy Thames Gold"
status: initial
tags: "clean, ambient, dream-65, single-coil, telecaster, stratocaster, tape-echo, dimension-d, sparkle, thr10ii"
target: "Shimmering, airy Blackface clean with warm tape bloom and subtle dimensional widening — inspired by London's warm August sun breaking through Thames morning haze."
tone-king-channel: bypassed
updated: 2026-08-28
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Clean
    cab: British Blues 2x12
    eq:
      gain: 34
      bass: 48
      mid: 54
      treble: 56
      master: 72
    tempo: 115
    compressor:
      enabled: true
      sustain: 45
      level: 55
    modulation:
      enabled: true
      type: Chorus
      mix: 20
      depth: 30
      freq: 20
      pre: 50
    echo:
      enabled: true
      type: Tape
      mix: 25
      feedback: 24
      time: 38
      bass: 40
      treble: 32
    reverb:
      enabled: true
      type: Spring
      mix: 24
      time: 45
      tone: 52
    gate:
      enabled: true
      thresh: 10
      decay: 50
---

# THR Hazy Thames Gold — Single-Coils

## Target Sound

This toneprint translates the London late-summer aesthetic from the UADx Dream '65 / Studio D / Galaxy Tape Echo "Hazy Thames Gold SC" toneprint directly into the **Yamaha THR10ii**.

The sound balances shimmering, high-headroom American Blackface chime with warm vintage tape flutter and subtle stereo dimensional spread. Celestion-style cabinet simulation rounds off the harsh top end while letting airy, golden presence bloom on single-coil decays.

---

## THR10ii Control Board

### 1. Physical Top Panel Knobs (Quick Reference)

| Knob | Physical Position (0–10) | Clock Setting |
|---|---|---|
| **Amp Select** | **CLASSIC / CLEAN** | — |
| **Gain** | **3.4** | ~9:30 |
| **Master** | **7.2** | ~2:30 |
| **Bass** | **4.8** | ~11:45 |
| **Middle** | **5.4** | ~12:30 |
| **Treble** | **5.6** | ~1:00 |
| **Effect** | **~2.0 (Chorus)** | ~8:30 (Chorus zone) |
| **Echo/Rev** | **~2.5 (Echo/Spring)** | ~9:00 (Echo/Rev zone) |

---

### 2. THR Remote App Deep Parameters

#### Amplifier Section
* **Amp Model**: `Classic Clean` (`THR10C_Deluxe` — Fender Deluxe Reverb '65 clean)
* **Cabinet**: `British Blues 2x12` (Marshall Bluesbreaker 2x12 with Celestion speakers — emulates the Greenback GB25 warmth over stock Jensen)
* **Gain (Drive)**: `34%` (`0.34`) — High-headroom clean with subtle touch-sensitive bloom
* **Master**: `72%` (`0.72`) — Pushes virtual power stage for harmonic overtones
* **Bass**: `48%` (`0.48`) — Firm, clear low end that prevents chord muddiness
* **Middle**: `54%` (`0.54`) — Warm midrange body (simulating the D-Tex circuit mod)
* **Treble**: `56%` (`0.56`) — Sparkling golden sunlight air and top-end shimmer

#### Dynamics & FX Pedals
* **Compressor (FX1)**: **ON** (`RedComp`)
  * **Sustain**: `45%` (`0.45`) — Gentle optical leveling that stabilizes decays without clamping
  * **Level**: `55%` (`0.55`) — Unity gain matching
* **Modulation (FX2)**: **ON** (`Chorus` / `StereoSquareChorus`)
  * **Mix**: `20%` (`0.20`) — Dimension Mode 1 subtle stereo spread
  * **Depth**: `30%` (`0.30`)
  * **Speed (Freq)**: `20%` (`0.20`) — Slow, watery shimmer
  * **Pre-Delay**: `50%` (`0.50`)
* **Echo / Delay (FX3)**: **ON** (`Tape Echo` / `TapeEcho`)
  * **Mix**: `25%` (`0.25`) — Ambient tape haze cushion
  * **Time**: `38%` (`0.38`) — ~240 ms ambient tempo sync
  * **Feedback**: `24%` (`0.24`) — 2–3 gentle trailing repeats
  * **Bass / Treble**: `40%` / `32%` — "Used tape" top-end roll-off
* **Reverb (FX4)**: **ON** (`Spring` / `StandardSpring`)
  * **Mix**: `24%` (`0.24`) — Authentic Blackface spring wash
  * **Time**: `45%` (`0.45`)
  * **Tone**: `52%` (`0.52`)
* **Noise Gate**: **ON**
  * **Threshold**: `10%` (`-86.4 dB`) — Transparent noise floor
  * **Decay**: `50%` (`0.50`)

---

## Starting Point Guide

- **Guitar Setup**: On a **Telecaster bridge pickup**, roll **Tone back to 8** and **Volume to 8.5** for maximum sweetness. On a **Stratocaster**, use **Position 4 (neck + middle)**.
- **Ambient Adjustment**: If you want deeper ambient immersion, raise the **Echo mix** to `30–35%` in THR Remote.
- **Darker Pickup Option**: If playing a darker neck pickup with flatwounds, nudge **Treble** up to `6.0`.
