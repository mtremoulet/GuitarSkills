---
amp: "Yamaha THR10II"
created: 2026-10-03
guitar: "2014 Gibson Les Paul Studio (490R neck / 490T bridge humbuckers)"
id: thr-gibson-hb-musing
pickup_type: humbucker
preset_name: "THR Gibson HB Musing"
status: initial
tags: "musing, omakase-bento, clean, jazz, vocal-mids, humbucker, les-paul, 490r, thr10ii"
target: "Acoustic translation of Faust & Wagner's Omakase Bento 'Gibson HB Musing' preset onto the Yamaha THR10ii, delivering vocal midrange clarity, subtle optical compression cushion, and lush Doppler pitch shimmer."
tone-king-channel: bypassed
updated: 2026-10-03
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Clean
    cab: California 1x12
    eq:
      gain: 28
      bass: 46
      mid: 62
      treble: 58
      master: 78
    tempo: 110
    compressor:
      enabled: true
      sustain: 38
      level: 58
    modulation:
      enabled: true
      type: Chorus
      mix: 25
      depth: 30
      freq: 35
      feedback: 0
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
      mix: 16
      decay: 36
      predelay: 5
      tone: 40
    gate:
      enabled: true
      thresh: 10
      decay: 50
---

# THR Gibson HB Musing — Les Paul Studio

## Target Sound

This toneprint is an acoustic and technical translation of the **"Gibson HB Musing"** reference preset from the sister project's **Faust & Wagner "Omakase Bento"** solid-state amplifier head (`faust-and-wagner/OMAKASE_BENTO_SPECIFICATION.md`) directly into the **Yamaha THR10ii**.

The physical Gibson Les Paul Studio (Ebony, 120th Anniversary Edition, detailed in `tone-advisor/guitar_stable.md`) is equipped with matched Alnico II 490R/490T humbuckers (~8.5k DCR). These pickups have a naturally warm, rounded top end with rich low-mid density. In the original Omakase Bento DSP circuit (`faust-and-wagner/faust/dsp/omakase_bento.dsp`), the "Gibson HB Musing" preset leaves the 120pF **Brown Sugar** capacitor off (as humbuckers do not require high-frequency loading), applies subtle optical leveling (`Lev Sens 2.2`), carves low-mid mud via the Cavity gyrator (`-2.0 dB @ 420 Hz`), pushes upper vocal clarity (`+1.5 dB @ 1.6 kHz`) and treble snap (`+1.2 dB @ 3.2 kHz`), engages the Magnatone true pitch vibrato (3.5 Hz rate, 2.5 depth), and sets the power section to **Induction** mode for ultra-high damping and pristine transient headroom.

On the Yamaha THR10ii, this response is captured by running the **Classic Clean** (`THR10C_Deluxe`) amp model with low preamp gain (2.8 / 10) and high Master volume (7.8 / 10), paired with the **California 1x12** (EVM-12L) cabinet emulation for punchy, uncolored projection. The Vactrol optical leveler is translated via the THR's **RedComp** stomp compressor, and the Magnatone Doppler pitch modulation is recreated via a gentle **StereoSquareChorus** shimmer.

---

## Signal Chain

```
[2014 Gibson Les Paul Studio (490R Neck / Both)]
       │
       ▼
[Yamaha THR10ii Input]
       │
       ▼
[Noise Gate: Thresh 10%, Decay 50%]
       │
       ▼
[RedComp Compressor: Sustain 38%, Level 58%]  <-- Translates Vactrol Leveler (Lev Sens 2.2)
       │
       ▼
[THR Classic Clean Amp Model (Fender Deluxe Reverb)]
• Gain: 2.8 / 10 | Master: 7.8 / 10 (Induction Headroom & Damping)
• Bass: 4.6 / 10 | Mid: 6.2 / 10 (Vocal Push) | Treble: 5.8 / 10 (Snap & Articulation)
       │
       ▼
[California 1x12 Cabinet Simulation (EVM-12L)]
       │
       ▼
[Modulation: StereoSquareChorus (Mix 25%, Depth 30%, Freq 35%)] <-- Translates Magnatone Vibrato (3.5Hz / 2.5)
       │
       ▼
[Reverb: Large Plate (Mix 16%, Decay 36%, Tone 40%)]
       │
       ▼
[Yamaha THR Stereo Speakers / Headphones]
```

---

## THR10ii Control Board

### 1. Physical Top Panel Knobs (Quick Reference)

| Knob | Physical Position (0–10) | Clock Setting | Purpose |
|---|---|---|---|
| **Amp Select** | **CLASSIC / CLEAN** | — | High-headroom Fender Deluxe Reverb clean topology. |
| **Gain** | **2.8** | ~8:45 | Clean preamp baseline; preserves clarity on dense chords. |
| **Master** | **7.8** | ~3:30 | Pushes virtual power amp into dynamic punch without clipping. |
| **Bass** | **4.6** | ~11:30 | Controlled low end; prevents solid mahogany body mud. |
| **Middle** | **6.2** | ~1:30 | Upper-mid push translating Bento's +1.5 dB @ 1.6 kHz gyrator. |
| **Treble** | **5.8** | ~1:15 | Clean snap and pick definition to offset 490R warmth. |
| **Effect** | **~2.0 (Chorus zone)** | ~8:30 | Recreates the subtle Magnatone Doppler pitch shimmer. |
| **Echo/Rev** | **~1.8 (Plate zone)** | ~8:15 | Intimate ambient plate reflection. |

---

### 2. THR Remote App Deep Parameters

#### Amplifier Section
* **Amp Model**: `Classic Clean` (`THR10C_Deluxe`, cited in `scripts/preset_compiler/yamaha.py`)
* **Cabinet**: `California 1x12` (`SpkSimType: 12`, Mesa 1x12 loaded with Electro-Voice EVM-12L for wide, uncolored frequency response)
* **Gain (Drive)**: `28%` (`0.28`) — Pure clean headroom
* **Master**: `78%` (`0.78`) — Dynamic power amp weight and touch sensitivity
* **Bass**: `46%` (`0.46`) — Tight low end
* **Middle**: `62%` (`0.62`) — Articulate vocal midrange boost
* **Treble**: `58%` (`0.58`) — Clear pickup snap and string definition

#### Dynamics & FX Pedals
* **Compressor (FX1)**: **ON** (`RedComp`)
  * **Sustain**: `38%` (`0.38`) — Translates Bento's gentle Vactrol optical leveler (`Lev Sens 2.2`)
  * **Level**: `58%` (`0.58`) — Clean unity makeup gain
* **Modulation (FX2)**: **ON** (`StereoSquareChorus`)
  * **Mix**: `25%` (`0.25`) — Subtle blend
  * **Depth**: `30%` (`0.30`) — Translates Bento's `Vib Depth 2.5`
  * **Freq**: `35%` (`0.35`) — Translates Bento's `Vib Speed 3.5 Hz`
  * **Feedback**: `0%` (`0.00`) — Pure pitch modulation without metallic comb filtering
  * **Pre**: `0%` (`0.00`) — Zero pre-delay for immediate Doppler phase response
* **Delay / Echo (FX3)**: **OFF**
* **Reverb (FX4)**: **ON** (`Plate` / `LargePlate1`)
  * **Mix**: `16%` (`0.16`) — Intimate studio room air
  * **Decay**: `36%` (`0.36`) — Controlled plate tail
  * **Pre-Delay**: `5 ms` (`0.05`)
  * **Tone**: `40%` (`0.40`) — Warm high-frequency rolloff
* **Noise Gate**: **ON**
  * **Threshold**: `10%` (`-86.4 dB`) — Transparent floor protection
  * **Decay**: `50%` (`0.50`) — Natural chord ring-out

---

## Starting Point Guide

- **Guitar Setup**: Switch to the **Neck 490R** pickup (or Neck + Bridge middle position for rhythm comping). Keep guitar Volume at **8–9** and Tone at **8–9**.
- **Touch Dynamics**: The subtle optical compression evens out fingerstyle chord voicings while allowing harder pick attacks to leap forward with punch and clarity.
- **Modulation Taste**: If you prefer a completely dry, stationary tone for classical or strict jazz study, turn the physical **Effect** knob fully counter-clockwise (OFF). To lean into vintage vibrato ballad textures, nudge the Effect knob to ~9:00.

---

## Feedback History

### 2026-10-03 — initial
* Toneprint formulated from the reference `Gibson HB Musing.json` preset of Faust & Wagner's Omakase Bento solid-state amplifier head.
* Configured specifically for the 2014 Gibson Les Paul Studio 490R/490T humbuckers.
