---
amp: "Yamaha THR10II"
created: 2026-06-09
guitar: "Gibson Les Paul Studio / Epiphone Les Paul Standard (bridge humbucker)"
id: thr-singing-lp-lead
pickup_type: humbucker
preset_name: "THR Singing LP Lead"
status: initial
tags: "rock, lead, high-gain, delay, reverb, humbucker, les-paul, thr10ii"
target: "A smooth, highly-sustaining, and smoothly distorted singing rock lead tone for a Les Paul."
tone-king-channel: bypassed
updated: 2026-06-09
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Special
    cab: British 4x12
    eq:
      gain: 62
      bass: 50
      mid: 72
      treble: 48
      master: 60
    tempo: 110
    compressor:
      enabled: false
      sustain: 0
      level: 0
    modulation:
      enabled: false
      type: Chorus
      mix: 0
      depth: 0
      freq: 0
      pre: 0
    echo:
      enabled: true
      type: "Digital Delay"
      mix: 24
      feedback: 25
      time: 40
      bass: 35
      treble: 35
    reverb:
      enabled: true
      type: Hall
      mix: 20
      decay: 50
      predelay: 5
      tone: 40
    gate:
      enabled: true
      thresh: 25
      decay: 50
---

# THR Singing LP Lead — Les Paul

## Target Sound

This toneprint is designed to deliver a smooth, high-gain, singing rock lead tone directly out of the **Yamaha THR10ii**, optimized for a humbucker-equipped guitar (such as a **Gibson Les Paul Studio** or **Epiphone Les Paul Standard** in the bridge position). 

Voiced after the classic hard rock lead sounds of Slash and Ritchie Sambora, it uses the **Classic Special** (`THR10X_Brown1` - EVH 5150-III Channel 2 "Brown Sound") emulation. Rather than a harsh, scoopy metal distortion, this profile provides a saturated, rich, midrange-heavy sound that compresses naturally as you dig in, sustaining beautifully. Paired with a **British 4x12** (Marshall 1960A) cabinet and a polished digital delay, it creates a massive "arena lead" projection.

---

## THR10ii Control Board

### 1. Amplifier Section

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Classic Special | Voiced after the EVH Brown sound; provides rich preamp drive and warm mid-heavy saturation. |
| Cabinet | British 4x12 | Marshall 1960A 4x12 cabinet emulation with Celestion G12T-75 speakers for classic punch. |
| Gain (Drive) | 6.2 / 10 | The sweet spot for smooth, singing distortion and liquid sustain. |
| Master | 6.0 / 10 | Sets the virtual power section push to round out the high end. |
| Bass | 5.0 (noon) | Balances low-end chunk without muddying fast runs. |
| Middle | 7.2 / 10 | Boosts the essential frequencies that help your single notes cut through a band mix. |
| Treble | 4.8 / 10 | Mellows the high-end fizz for a liquid, non-fatiguing lead tone. |

---

### 2. Dynamics & FX Pedals

#### Compressor (FX1)
* **Status**: **OFF** (Preamp saturation provides all the compression required).

#### Modulation Effect (FX2)
* **Status**: **OFF**

#### Delay / Echo (FX3)
* **Status**: **ON**
* **Type**: Digital Delay
* **Wet/Dry**: 24% — Parallel dry blend to keep the primary note in front.
* **Feedback**: 25% — Multiple smooth, falling echo repeats (~3-4 repeats).
* **Time**: 40% — Approximately 380ms spacing (provides a lush, modern lead spacing).
* **Bass / Treble**: 3.5 / 10 — Keeps the echo reflections dark and soft.

#### Reverb (FX4)
* **Status**: **ON**
* **Type**: Hall Reverb
* **Wet/Dry**: 20% — Lower-level return for spatial depth.
* **Decay**: 5.0 / 10 — Large hall space.
* **Tone**: 4.0 / 10 — Warm reverb tone profile.

#### Noise Gate
* **Status**: **ON**
* **Threshold**: 25% — Moderately high to silence high-gain pickup hum between phrases.
* **Decay**: 50% — Smooth decay.

---

## Starting Point Guide

* **Physical Prep**: Flip your Les Paul's pickup toggle switch to the **Bridge** position. Max out your volume and tone controls on the guitar to feed the preamp a full, hot signal.
* **First Adjustment**: If your guitar's bridge pickup is extremely hot or bright, roll back the guitar's **Tone** knob to **8** to smooth out the transients further, or reduce the **Treble** control on the THR to **4.0**.
* **Delay Adjustment**: To customize the delay to your tempo, tap the **Tap Tempo** button on your THR physical chassis, or modify the **Time** parameter via the THR Remote app.
