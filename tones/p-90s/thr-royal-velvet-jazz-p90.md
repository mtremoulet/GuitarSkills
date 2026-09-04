---
amp: "Yamaha THR10II"
created: 2026-08-28
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s) / Les Paul P-90s"
id: thr-royal-velvet-jazz-p90
pickup_type: p-90
preset_name: "THR Royal Velvet P90 Jazz"
status: initial
tags: "jazz, clean, warm, plexi, p-90, framus, ev12, thr10ii"
target: "Warm, woody Marshall Plexi high-headroom jazz clean with EVM-12L projection, optical compression, and vintage room depth."
tone-king-channel: bypassed
updated: 2026-08-28
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Lead
    cab: California 1x12
    eq:
      gain: 22
      bass: 46
      mid: 75
      treble: 38
      master: 78
    tempo: 110
    compressor:
      enabled: true
      sustain: 48
      level: 56
    modulation:
      enabled: false
      type: Chorus
      mix: 0
      depth: 0
      freq: 0
      pre: 0
    echo:
      enabled: false
      type: Tape
      mix: 0
      feedback: 0
      time: 0
      bass: 0
      treble: 0
    reverb:
      enabled: true
      type: Room
      mix: 16
      decay: 38
      predelay: 15
      tone: 42
    gate:
      enabled: true
      thresh: 12
      decay: 50
---

# THR Royal Velvet Jazz — P-90s

## Target Sound

This toneprint translates the high-headroom Marshall Super Bass / Plexi jazz architecture from the UADx Lion '68 "Royal Velvet Jazz" toneprint directly to the **Yamaha THR10ii**.

While Marshalls are typically known for rock crunch, their high-power EL34 output section provides immense clean headroom and a fast, tight transient response. When paired with P-90 single coils, high Master volume, low Preamp Gain, and the **"Jazz Middle Rule"** (pushing the Mid control to **7.5** while rolling off high-end click), the result is a gorgeous, woody "thump" with deep vocal warmth and zero digital harshness.

---

## THR10ii Control Board

### 1. Physical Top Panel Knobs (Quick Reference)

| Knob | Physical Position (0–10) | Clock Setting |
|---|---|---|
| **Amp Select** | **CLASSIC / LEAD** | — |
| **Gain** | **2.2** | ~8:30 |
| **Master** | **7.8** | ~3:30 |
| **Bass** | **4.6** | ~11:30 |
| **Middle** | **7.5** | ~3:00 |
| **Treble** | **3.8** | ~10:30 |
| **Effect** | **OFF** | Min |
| **Echo/Rev** | **~2.0 (Room)** | ~8:30 (Room zone) |

---

### 2. THR Remote App Deep Parameters

#### Amplifier Section
* **Amp Model**: `Classic Lead` (`THR10_Lead` — Marshall 1959 Plexi / Super Lead circuit)
* **Cabinet**: `California 1x12` (Mesa 1x12 loaded with Electro-Voice EVM-12L, directly matching the EV12 cab in the UADx rig)
* **Gain (Drive)**: `22%` (`0.22`) — Low preamp gain for pure clean headroom
* **Master**: `78%` (`0.78`) — Pushes the virtual power section for rich harmonic bloom
* **Bass**: `46%` (`0.46`) — Tight low-end body without swamp-ash or mahogany mud
* **Middle**: `75%` (`0.75`) — **CRITICAL:** "Jazz Middle Rule" push for woody acoustic resonance
* **Treble**: `38%` (`0.38`) — Simulates the "High-Cut Veil" at 4.5 kHz, rolling off sharp P-90 pick click

#### Dynamics & FX Pedals
* **Compressor (FX1)**: **ON** (`RedComp`)
  * **Sustain**: `48%` (`0.48`) — Gentle optical leveling (~1–2 dB peak reduction)
  * **Level**: `56%` (`0.56`) — Clean unity makeup gain
* **Modulation (FX2)**: **OFF**
* **Echo / Delay (FX3)**: **OFF**
* **Reverb (FX4)**: **ON** (`Room` / `SmallRoom1`)
  * **Mix**: `16%` (`0.16`) — Subtle studio chamber air
  * **Decay**: `38%` (`0.38`) — Warm, intimate room decay
  * **Pre-Delay**: `15 ms` (`0.15`) — Keeps dry P-90 attack clear and upfront
  * **Tone**: `42%` (`0.42`) — Rolled-off high end for dark chamber warmth
* **Noise Gate**: **ON**
  * **Threshold**: `12%` (`-84.5 dB`) — Tames idle P-90 single-coil hum
  * **Decay**: `50%` (`0.50`) — Smooth, natural release

---

## Starting Point Guide

- **Guitar Setup**: Switch to the **Neck P-90**. Roll guitar Volume to **7–8** and Tone to **6–7** (the 7/7 baseline) to shave off raw single-coil bite.
- **Touch Dynamics**: Play chord-melody and walking basslines with your thumb and fingers. The high Master volume compresses notes dynamically without clipping into distortion.
- **Tonal Adjustment**: If using darker roundwounds or playing in an acoustically damped room, nudge **Treble** up from `3.8` to `4.2` rather than touching the Mid control.
