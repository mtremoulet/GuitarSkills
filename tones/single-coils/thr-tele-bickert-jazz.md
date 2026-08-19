---
amp: "Yamaha THR10II"
created: 2026-08-17
guitar: "2024 Fender Player II Telecaster (Neck single-coil pickup)"
id: thr-tele-bickert-jazz
pickup_type: single-coil
preset_name: "THR Tele Bickert Jazz"
status: initial
tags: "jazz, clean, warm, ed-bickert, telecaster, dr-z, carmen-ghia, thr10ii, single-coil"
target: 'Dark, woody, intimate Ed Bickert-style jazz clean on a Telecaster neck pickup using the Modern Clean (Dr. Z) boutique engine.'
tone-king-channel: bypassed
updated: 2026-08-17
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Modern
      model: Clean
    cab: American 1x12
    eq:
      gain: 32
      bass: 62
      mid: 70
      treble: 32
      master: 78
    tempo: 110
    compressor:
      enabled: true
      sustain: 45
      level: 58
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
      type: Plate
      mix: 18
      decay: 38
      predelay: 5
      tone: 35
    gate:
      enabled: true
      thresh: 12
      decay: 50
---

# THR Tele Bickert Jazz — Telecaster

## Target Sound

This toneprint is crafted to transform the single-coil neck pickup of the **2024 Fender Player II Telecaster** into a warm, woody, and intimate jazz box voice, inspired by Canadian jazz icon **Ed Bickert**. 

Solid-body Telecasters can easily sound spiky or thin when playing jazz chord melody. To create the dark "Electronic Veil" character, this toneprint uses the THR's **Modern Clean** (`THR30_Carmen` — Dr. Z Carmen Ghia) boutique engine. The Carmen Ghia's low-watt EL84 topology produces rich even-order harmonic fullness and dynamic compression as the **Master** is pushed high (7.8 / 10). Combined with a prominent midrange push (7.0 / 10), rolled-off highs (3.2 / 10), and an **American 1x12** open-back cabinet emulation, it strips away single-coil snap and replaces it with acoustic depth and round, vocal note separation.

---

## THR10ii Control Board

### 1. Amplifier Section

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Modern Clean (`THR30_Carmen` / Dr. Z) | Boutique low-watt EL84 design; thickens single-coil fundamentals with tube compression. |
| Cabinet | American 1x12 (`DRVB`) | Fender Deluxe Reverb 1x12 open-back for natural acoustic bloom. |
| Gain (Drive) | 3.2 / 10 | High-headroom clean foundation with zero unwanted grit. |
| Master | 7.8 / 10 | Pushed power section to generate warm tube bloom, sustain, and touch-sensitive sag. |
| Bass | 6.2 / 10 | Full, resonant low end for walking basslines and lush root voicings. |
| Middle | 7.0 / 10 | **The "Jazz Middle" boost:** Fills out the body of single notes and removes boxiness. |
| Treble | 3.2 / 10 | **The "High-Cut Veil":** Mellows the single-coil top-end snap for smooth, dark jazz articulation. |

---

### 2. Dynamics & FX Pedals

#### Compressor (FX1)
* **Status**: **ON**
* **Type**: Stomp Comp (`RedComp`)
* **Sustain**: 4.5 / 10 — Gentle leveling that evens out chord melody voicings without pumping.
* **Level**: 5.8 / 10 — Output matching makeup gain.

#### Modulation Effect (FX2)
* **Status**: **OFF**

#### Delay / Echo (FX3)
* **Status**: **OFF**

#### Reverb (FX4)
* **Status**: **ON**
* **Type**: Plate Reverb (`LargePlate1`)
* **Wet/Dry**: 18% — Subtle, warm studio plate resonance that sits behind the dry note.
* **Decay**: 3.8 / 10 — Short-to-medium tail to keep complex jazz chord changes articulate.
* **Tone**: 3.5 / 10 — Darkened high-frequency dampening.

#### Noise Gate
* **Status**: **ON**
* **Threshold**: 12% — Light gating to silence single-coil 60-cycle idle hum.
* **Decay**: 50% — Natural, unclipped chord decay.

---

## Starting Point Guide

* **Physical Prep**: Switch your Telecaster to the **Neck** pickup. Roll the guitar's **Volume** knob back to **7.5–8.0** and roll the **Tone** knob back to **7.0** (the classic "7/7" jazz sweet spot).
* **First Adjustment**: If you want even more acoustic woodiness, swap the Cabinet to **Boutique 1x12** (`SpkSimType: 15`). If the low-end feels too thick on your lower strings, dial the **Bass** knob back to **5.5**.
* **Soloing & Comping**: The high Master volume allows your lighter thumb/fingerstyle comping to remain clean and pillowy, while firmer pick attack yields singing, vocal sustain.
