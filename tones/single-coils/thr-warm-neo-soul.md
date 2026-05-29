---
id: thr-warm-neo-soul
preset_name: "THR Warm Neo Soul"
created: 2026-05-29
updated: 2026-05-29
guitar: "Squier Stratocaster (bridge + middle pickup position)"
target: "A warm, compressed neo-soul clean tone for the Yamaha THR10ii with gentle chorus and slapback tape echo."
tags: neo-soul, clean, warm, chorus, echo, thr10ii, single-coil
tone-king-channel: bypassed
amp: Yamaha THR10ii
status: initial
pickup_type: single-coil
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      model: "Clean"
      drive: 0.35
      bass: 0.60
      mid: 0.50
      treble: 0.45
      master: 0.60
    cab:
      model: "2x12"
    compressor:
      enabled: true
      model: "Stomp Comp"
      level: 0.55
      sustain: 0.60
    effect:
      enabled: true
      model: "Chorus"
      wet_dry: 0.35
      depth: 0.40
      freq: 0.25
    echo:
      enabled: true
      model: "Tape Echo"
      wet_dry: 0.25
      time: 0.30
      feedback: 0.20
    reverb:
      enabled: true
      model: "Hall"
      wet_dry: 0.20
      decay: 0.45
      pre_delay: 0.05
      tone: 0.50
    gate:
      enabled: true
      thresh: 0.12
      decay: 0.50
---

# THR Warm Neo-Soul — Stratocaster

## Target Sound

This toneprint is voiced to produce a warm, compressed, dynamic neo-soul clean tone directly out of the **Yamaha THR10ii**, optimized for a Stratocaster in the bridge + middle position (position 4 "quack"). It blends a high-headroom "Clean" boutique preamp emulation with deep compression, lush wide-spectrum chorus, and a short slapback tape echo return to add depth and body. 

Because single-coils naturally have sharp, snappy transients, the built-in compressor is engaged to round out the plucks musically, converting fast pick strikes into warm, percussive "pops" with a long, singing sustain tail.

---

## THR10ii Control Board

### 1. Amplifier Section

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Clean | High-headroom clean platform with rich, transparent high-mids. |
| Cabinet | 2x12 | Open-back cabinet emulation for wide dispersion and wood resonance. |
| Gain (Drive) | 3.5 / 10 | Transparency zone — keeps the input clean with high dynamic range. |
| Master | 6.0 / 10 | Pushes the power amp emulation for rich even-order harmonics. |
| Bass | 6.0 / 10 | Fills out the low-end body of single-coil pickups. |
| Middle | 5.0 (noon) | Flat baseline — keeps the mids balanced and punchy. |
| Treble | 4.5 / 10 | Gently takes the edge off single-coil high-end transients. |

---

### 2. Dynamics & FX Pedals

#### Compressor (FX1)
* **Status**: **ON**
* **Type**: Stomp Comp
* **Sustain**: 6.0 / 10 — Solid compression that smooths arpeggio pick attacks.
* **Level**: 5.5 / 10 — Output matching makeup gain.

#### Modulation Effect (FX2)
* **Status**: **ON**
* **Type**: Chorus
* **Wet/Dry**: 35% — Keeps the chorus under the dry tone for subtle thickening.
* **Depth**: 40% — Wide mod envelope.
* **Speed (Freq)**: 25% — Slow, liquid movement.

#### Delay / Echo (FX3)
* **Status**: **ON**
* **Type**: Tape Echo
* **Wet/Dry**: 25% — Parallel dry blend.
* **Feedback**: 20% — 1 to 2 short slapback repeats.
* **Time**: 30% — Low ms range slapback spacing.

#### Reverb (FX4)
* **Status**: **ON**
* **Type**: Hall Reverb
* **Wet/Dry**: 20% — Lower-level return so the dry guitar remains in focus.
* **Decay**: 4.5 / 10 — Intimate room scale.

#### Noise Gate
* **Status**: **ON**
* **Threshold**: 12% — Light gating to suppress single-coil hum.
* **Decay**: 50% — Natural, unclipped note release.

---

## Starting Point Guide

* **Physical Prep**: Play in Strat position 4 (bridge + middle). Roll the guitar volume knob to **8** to clean up the input and maximize touch-sensitivity.
* **First Adjustment**: Adjust the **Gain (Drive)** control on your amp or THR Remote app if your pickups run hotter. Raise to 4.5 if you want a subtle "hairy" crunch when digging in.
* **Modulation Shift**: Bypass the **Chorus** if you prefer a drier, modern chillhop arpeggio tone, or swap to **Tremolo** for organic, watery movement.
