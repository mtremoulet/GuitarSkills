---
amp: "Yamaha THR10II"
created: 2026-08-17
guitar: "Epiphone Les Paul Standard / Gibson Les Paul Studio / Framus P-90s"
id: thr-bluesbreaker-crunch
pickup_type: humbucker
preset_name: "THR Bluesbreaker Crunch"
status: initial
tags: "blues, rock, vintage, marshall, bluesbreaker, plexi, crunch, thr10ii, humbucker, p-90"
target: 'Dynamic, touch-sensitive 1960s British blues-rock crunch via the Classic Lead engine and British Blues 2x12 open-back cab.'
tone-king-channel: bypassed
updated: 2026-08-17
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Lead
    cab: British Blues 2x12
    eq:
      gain: 56
      bass: 52
      mid: 68
      treble: 52
      master: 75
    tempo: 115
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
      type: Tape
      mix: 14
      feedback: 15
      time: 28
      bass: 30
      treble: 35
    reverb:
      enabled: true
      type: Spring
      mix: 20
      time: 35
      predelay: 0
      tone: 45
    gate:
      enabled: true
      thresh: 20
      decay: 50
---

# THR Bluesbreaker Crunch — Les Paul / P-90s

## Target Sound

This toneprint delivers the organic, touch-responsive British tube overdrive of the iconic 1960s **Marshall JTM45 / Bluesbreaker** combo, as heard on Eric Clapton's landmark 1966 *John Mayall & the Bluesbreakers* (Beano) album and classic Peter Green/Paul Kossoff records.

Instead of a tight, aggressive closed-back 4x12 stack, this patch routes the **Classic Lead** (`THR10_Lead` — Marshall Plexi / 1959 Super Lead) preamp into the **British Blues 2x12** (`BBRKR` — Marshall 1962 Bluesbreaker 2x12 open-back) cabinet emulation. The open-back cabinet provides wide stereo air, warm lower-mid bloom, and harmonic chime without ear-piercing top-end rasp. The power section is pushed to 7.5 / 10 to recreate natural tube rectifier sag and compression.

---

## THR10ii Control Board

### 1. Amplifier Section

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Classic Lead (`THR10_Lead` / Marshall Super Lead) | Low-gain British preamp section with warm, touch-sensitive breakup. |
| Cabinet | British Blues 2x12 (`BBRKR`) | 1962 open-back 2x12 cabinet emulation with Celestion speakers for classic warmth. |
| Gain (Drive) | 5.6 / 10 | The edge-of-crunch sweet spot — cleans up when picking gently, roars when digging in. |
| Master | 7.5 / 10 | Pushes the virtual power section for classic British harmonic saturation and compression. |
| Bass | 5.2 / 10 | Balanced low end with vintage looseness and body. |
| Middle | 6.8 / 10 | Punchy British midrange focus to ensure single-note leads sing through a mix. |
| Treble | 5.2 / 10 | Sweet, smooth top end that retains bite without harsh fizz. |

---

### 2. Dynamics & FX Pedals

#### Compressor (FX1)
* **Status**: **OFF** (The pushed Master volume provides all the natural tube compression needed).

#### Modulation Effect (FX2)
* **Status**: **OFF**

#### Delay / Echo (FX3)
* **Status**: **ON**
* **Type**: Tape Echo (`TapeEcho`)
* **Wet/Dry**: 14% — Subtle vintage slapback that adds room dimension and space.
* **Feedback**: 15% — 1 to 2 soft falling echoes.
* **Time**: 28% — Short slapback spacing (~140ms).
* **Bass / Treble**: 3.0 / 3.5 — Filtered dark repeats that stay out of the guitar's path.

#### Reverb (FX4)
* **Status**: **ON**
* **Type**: Spring Reverb (`StandardSpring`)
* **Wet/Dry**: 20% — Vintage studio spring tank splash.
* **Decay (Time)**: 3.5 / 10 — Moderate spring decay.
* **Tone**: 4.5 / 10 — Warm vintage spring tone.

#### Noise Gate
* **Status**: **ON**
* **Threshold**: 20% — Tames pickup idle hum without cutting off trailing note sustain.
* **Decay**: 50% — Smooth release.

---

## Starting Point Guide

* **Physical Prep**: 
  * On a **Les Paul**: Select the **Bridge** or **Middle (both pickups)** position. Set guitar **Volume** to **7–8** for a warm rhythm crunch, and push to **10** for full singing lead overdrive.
  * On **Framus P-90s**: The P-90s' natural midrange snarl interacts aggressively with this circuit. Dial the guitar volume to **7** for glassy rhythm and **10** for raw, punchy blues growl.
* **First Adjustment**: If you want a tighter, heavier hard rock sound, swap the cabinet to **British 4x12** (`1960A`). For a slightly brighter, chimier British invasion bite, try **British 2x12** (`AC3`).
