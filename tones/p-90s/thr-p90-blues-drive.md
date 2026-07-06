---
amp: "Yamaha THR10II"
created: 2026-06-09
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90 pickups)"
id: thr-p90-blues-drive
pickup_type: p-90
preset_name: "THR P90 Blues Drive"
status: initial
tags: "blues, lead, crunch, edge-of-breakup, spring, tape-echo, compressor, p90, framus, thr10ii"
target: 'A touch-sensitive, lightly broken up blues lead tone for the Framus P-90 single-coils.'
tone-king-channel: bypassed
updated: 2026-06-09
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Boutique
      model: Clean
    cab: Boutique 2x12
    eq:
      gain: 72
      bass: 55
      mid: 60
      treble: 50
      master: 75
    tempo: 120
    compressor:
      enabled: true
      sustain: 30
      level: 68
    modulation:
      enabled: false
      type: Chorus
      mix: 0
      depth: 0
      freq: 0
      pre: 0
    echo:
      enabled: true
      type: Tape
      mix: 15
      feedback: 15
      time: 28
      bass: 30
      treble: 35
    reverb:
      enabled: true
      type: Spring
      mix: 25
      time: 35
      predelay: 0
      tone: 45
    gate:
      enabled: true
      thresh: 15
      decay: 50
---

# THR P90 Blues Drive — Framus P-90s

## Target Sound

This toneprint is voiced to deliver a touch-sensitive, expressive, and lightly broken-up driving blues lead tone directly out of the **Yamaha THR10ii**, specifically tailored for the **Framus Earl Slick Artist Series** (or any guitar fitted with DiMarzio P-90 single-coil pickups).

P-90s have a unique fat midrange and dynamic bite that sits perfectly between a single-coil and a humbucker. To capture this grit, we use the **Boutique Clean** (Fender Blues Junior Modded) engine pushed into the "edge of breakup" zone (Gain at 7.2). A built-in Compressor is enabled with low sustain and a high level, acting as a clean boost that pushes the preamp tubes into natural saturation. The **Boutique 2x12** (Matchless DC30) open-back cabinet emulation provides spacious chimes and bloom, while a splash of spring reverb and subtle tape echo complete the vintage blues vibe.

---

## THR10ii Control Board

### 1. Amplifier Section

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Boutique Clean | Modded Fender Blues Junior voicing; warm, touch-sensitive breakup. |
| Cabinet | Boutique 2x12 | Matchless DC30 open-back cabinet for a wider soundstage and chime. |
| Gain (Drive) | 7.2 / 10 | Pushes the preamp into natural bluesy distortion when picking hard. |
| Master | 7.5 / 10 | Squeezes the virtual power section for compression and warm bloom. |
| Bass | 5.5 / 10 | Tight low end that doesn't get flubby under aggressive pick attack. |
| Middle | 6.0 / 10 | Emphasizes the signature woody throatiness of P-90 pickups. |
| Treble | 5.0 (noon) | Preserves P-90 bite and clarity without harsh high end. |

---

### 2. Dynamics & FX Pedals

#### Compressor (FX1)
* **Status**: **ON**
* **Type**: Stomp Comp
* **Sustain**: 3.0 / 10 — Low compression; keeps the pick dynamics natural.
* **Level**: 6.8 / 10 — High output level (serves as a clean boost to drive the preamp harder).

#### Modulation Effect (FX2)
* **Status**: **OFF**

#### Delay / Echo (FX3)
* **Status**: **ON**
* **Type**: Tape Echo
* **Wet/Dry**: 15% — Parallel dry blend; sits low under the main signal.
* **Feedback**: 15% — Single short tape repeat for spatial depth.
* **Time**: 28% — Fast slapback delay spacing.
* **Bass / Treble**: 3.0 / 3.5 — Rolls off the delay repeats to keep them warm and subtle.

#### Reverb (FX4)
* **Status**: **ON**
* **Type**: Spring Reverb
* **Wet/Dry**: 25% — Classic wet spring drip.
* **Decay (Time)**: 3.5 / 10 — Moderate spring decay.
* **Tone**: 4.5 / 10 — Vintage warm-voiced spring splash.

#### Noise Gate
* **Status**: **ON**
* **Threshold**: 15% — Suppresses P-90 single-coil 60-cycle hum between notes without clipping decay.
* **Decay**: 50% — Natural decay release.

---

## Starting Point Guide

* **Physical Prep**: Play in the **Neck** or **Middle (both pickups)** position of your Framus P-90. Set the guitar's volume knob to **8** for your rhythm parts, and crank it to **10** for your leads to send the amp into full singing overdrive.
* **First Adjustment**: P-90s are highly sensitive to height and output. If you want more grit, raise the **Gain (Drive)** to **8.0**. If the breakup is too fuzzy, lower it to **6.5**.
* **Hum Reduction**: If you are playing in a room with electrical interference, toggle your guitar's pickup selector to the **Middle** position. On most P-90 guitars, the middle position is reverse-wound, reverse-polarity (RWRP), which cancels hum.
