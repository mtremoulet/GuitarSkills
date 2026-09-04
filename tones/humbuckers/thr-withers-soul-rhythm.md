---
amp: "Yamaha THR10II"
created: 2026-08-28
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (neck or neck+bridge blend)"
id: thr-withers-soul-rhythm
pickup_type: humbucker
preset_name: "THR Withers Soul Rhythm"
status: initial
tags: "soul, funk, rhythm, tweed, humbucker, withers, thr10ii"
target: "Warm, percussive 1970s Tweed soul and funk rhythm guitar tone with organic tube sag, snappy optical compression, and Motown room reflections."
tone-king-channel: bypassed
updated: 2026-08-28
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Boutique
      model: Clean
    cab: American 4x10
    eq:
      gain: 36
      bass: 54
      mid: 58
      treble: 44
      master: 72
    tempo: 105
    compressor:
      enabled: true
      sustain: 62
      level: 54
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
      mix: 15
      decay: 28
      predelay: 12
      tone: 45
    gate:
      enabled: true
      thresh: 10
      decay: 50
---

# THR Withers Soul Rhythm — Humbuckers

## Target Sound

This toneprint translates the 1970s soul and funk rhythm architecture from the UADx Woodrow '55 "Bill Withers Soul Rhythm" toneprint directly into the **Yamaha THR10ii**.

Voiced for classic funk and soul vamps ("Use Me", "Lean On Me"), this preset emulates a vintage low-watt Tweed amplifier running hot into multi-speaker Jensen cabinets. The sound balances warm, woody chord resonance with crisp, percussive attack on muted scratching and syncopated stabs.

---

## THR10ii Control Board

### 1. Physical Top Panel Knobs (Quick Reference)

| Knob | Physical Position (0–10) | Clock Setting |
|---|---|---|
| **Amp Select** | **BOUTIQUE / CLEAN** | — |
| **Gain** | **3.6** | ~10:00 |
| **Master** | **7.2** | ~2:30 |
| **Bass** | **5.4** | ~12:30 |
| **Middle** | **5.8** | ~1:00 |
| **Treble** | **4.4** | ~11:00 |
| **Effect** | **OFF** | Min |
| **Echo/Rev** | **~1.8 (Room)** | ~8:30 (Room zone) |

---

### 2. THR Remote App Deep Parameters

#### Amplifier Section
* **Amp Model**: `Boutique Clean` (`THR10C_BJunior2` — modded Tweed/EL84 low-watt boutique clean)
* **Cabinet**: `American 4x10` (Fender Tweed Bassman 4x10 with Jensen speakers — delivers bouncy, percussive low-mid punch)
* **Gain (Drive)**: `36%` (`0.36`) — Touch-sensitive clean that develops subtle harmonic hair when digging in
* **Master**: `72%` (`0.72`) — Pushes virtual power tube sag for organic vintage soul compression
* **Bass**: `54%` (`0.54`) — Warm rhythmic foundation without flub
* **Middle**: `58%` (`0.58`) — Rich lower-mid body for funk chord stabs and double stops
* **Treble**: `44%` (`0.44`) — Smooth, rounded top end that eliminates harsh humbucker glare

#### Dynamics & FX Pedals
* **Compressor (FX1)**: **ON** (`RedComp`)
  * **Sustain**: `62%` (`0.62`) — Fast, bouncy optical leveling that tightens percussive funk scratches
  * **Level**: `54%` (`0.54`) — Unity gain matching
* **Modulation (FX2)**: **OFF**
* **Echo / Delay (FX3)**: **OFF**
* **Reverb (FX4)**: **ON** (`Room` / `SmallRoom1`)
  * **Mix**: `15%` (`0.15`) — Tight Motown studio room reflections
  * **Decay**: `28%` (`0.28`) — Short, articulate room tail that never interferes with syncopation
  * **Pre-Delay**: `12 ms` (`0.12`) — Preserves upfront transient punch
  * **Tone**: `45%` (`0.45`) — Warm room acoustic profile
* **Noise Gate**: **ON**
  * **Threshold**: `10%` (`-86.4 dB`) — Transparent noise floor control
  * **Decay**: `50%` (`0.50`)

---

## Starting Point Guide

- **Guitar Setup**: Select your **Epiphone Sheraton II** or **Gibson Les Paul Studio** neck pickup (or middle position with neck volume at 8, bridge volume at 6). Set tone knob to **7**.
- **Playing Technique**: Relax the picking hand for sixteenth-note funk scratches. Let the compressor and Tweed sag provide the percussive "pop".
- **Breakup Tuning**: For more grit on solo fills, push **Gain** up to `4.2–4.5`.
