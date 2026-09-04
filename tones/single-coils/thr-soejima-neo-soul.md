---
amp: "Yamaha THR10II"
created: 2026-08-28
guitar: "Fender Player II Telecaster / Squier Stratocaster (single-coils)"
id: thr-soejima-neo-soul
pickup_type: single-coil
preset_name: "THR Soejima Neo Soul"
status: initial
tags: "neo-soul, clean, warm, chorus, tape-echo, soejima, single-coil, thr10ii"
target: "Toshiki Soejima-style warm, compressed, and articulate neo-soul clean with subtle Dimension chorus widening, slapback tape echo, and chamber ambience."
tone-king-channel: bypassed
updated: 2026-08-28
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Clean
    cab: American 2x12
    eq:
      gain: 32
      bass: 52
      mid: 52
      treble: 46
      master: 68
    tempo: 95
    compressor:
      enabled: true
      sustain: 65
      level: 55
    modulation:
      enabled: true
      type: Chorus
      mix: 22
      depth: 35
      freq: 22
      pre: 50
    echo:
      enabled: true
      type: Tape
      mix: 22
      feedback: 18
      time: 28
      bass: 35
      treble: 35
    reverb:
      enabled: true
      type: Hall
      mix: 18
      decay: 42
      predelay: 10
      tone: 48
    gate:
      enabled: true
      thresh: 12
      decay: 50
---

# THR Soejima Neo-Soul — Single-Coils

## Target Sound

This toneprint translates the Toshiki Soejima Neo-Soul architecture from the UADx Dream '65 / Vemuram Jan Ray signal chain directly into the **Yamaha THR10ii**.

Designed for modern Japanese neo-soul, R&B, and City Pop chord-melody styles, this tone pairs a high-headroom Blackface clean foundation with fast optical compression, subtle stereo chorus widening (Dimension D style), and a warm slapback tape echo halo. Pick attacks turn into smooth, percussive "pops" while chord extensions sustain effortlessly.

---

## THR10ii Control Board

### 1. Physical Top Panel Knobs (Quick Reference)

| Knob | Physical Position (0–10) | Clock Setting |
|---|---|---|
| **Amp Select** | **CLASSIC / CLEAN** | — |
| **Gain** | **3.2** | ~9:30 |
| **Master** | **6.8** | ~2:00 |
| **Bass** | **5.2** | ~12:30 |
| **Middle** | **5.2** | ~12:30 |
| **Treble** | **4.6** | ~11:30 |
| **Effect** | **~2.2 (Chorus)** | ~8:30 (Chorus zone) |
| **Echo/Rev** | **~2.0 (Echo/Rev)** | ~8:30 (Echo/Rev zone) |

---

### 2. THR Remote App Deep Parameters

#### Amplifier Section
* **Amp Model**: `Classic Clean` (`THR10C_Deluxe` — Fender Deluxe Reverb clean platform)
* **Cabinet**: `American 2x12` (Fender Twin Reverb 2x12 Jensen speakers — matches the JBF120 cab in the UADx rig for wide, articulate dispersion)
* **Gain (Drive)**: `32%` (`0.32`) — Pristine, transparent clean floor
* **Master**: `68%` (`0.68`) — Pushes virtual power section for tube warmth and harmonic bloom
* **Bass**: `52%` (`0.52`) — Warm, firm bass response for fingerstyle root notes
* **Middle**: `52%` (`0.52`) — Balanced midrange to counteract digital mid-scoop
* **Treble**: `46%` (`0.46`) — Softens glassy single-coil transients

#### Dynamics & FX Pedals
* **Compressor (FX1)**: **ON** (`RedComp`)
  * **Sustain**: `65%` (`0.65`) — Essential for Soejima style: clamps pick transients into a rounded percussive "thwack" with singing sustain
  * **Level**: `55%` (`0.55`) — Unity makeup gain
* **Modulation (FX2)**: **ON** (`Chorus` / `StereoSquareChorus`)
  * **Mix**: `22%` (`0.22`) — Low blend for Dimension D style widening without overt pitch detuning
  * **Depth**: `35%` (`0.35`)
  * **Speed (Freq)**: `22%` (`0.22`) — Slow, elegant spatial movement
  * **Pre-Delay**: `50%` (`0.50`)
* **Echo / Delay (FX3)**: **ON** (`Tape Echo` / `TapeEcho`)
  * **Mix**: `22%` (`0.22`) — Subtle parallel slapback cushion
  * **Time**: `28%` (`0.28`) — Short slapback delay time (~120–140 ms)
  * **Feedback**: `18%` (`0.18`) — 1–2 gentle repeats
  * **Bass / Treble**: `35%` / `35%` — Rolled-off tape warmth
* **Reverb (FX4)**: **ON** (`Hall` / `ReallyLargeHall`)
  * **Mix**: `18%` (`0.18`) — Intimate studio halo
  * **Decay**: `42%` (`0.42`) — Smooth, spacious room tail
  * **Pre-Delay**: `10 ms` (`0.10`) — Keeps note definitions crisp
  * **Tone**: `48%` (`0.48`)
* **Noise Gate**: **ON**
  * **Threshold**: `12%` (`-84.5 dB`) — Eliminates single-coil idle buzz
  * **Decay**: `50%` (`0.50`)

---

## Starting Point Guide

- **Guitar Setup**: Play in **Strat Position 4 (bridge + middle)** or **Tele Neck position**. Set guitar volume to **8** and tone to **7** (the "7/7 Baseline").
- **Playing Nuance**: Essential for modern neo-soul hammer-ons, pull-offs, slides, and double stops. The high compressor setting keeps gentle legato runs at the exact same perceived volume as accented thumb slaps.
