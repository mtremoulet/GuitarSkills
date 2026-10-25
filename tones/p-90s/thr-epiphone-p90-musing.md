---
amp: "Yamaha THR10II"
created: 2026-10-03
guitar: "2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90s HSP-90s)"
id: thr-epiphone-p90-musing
pickup_type: p-90
preset_name: "THR Epiphone P90 Musing"
status: initial
tags: "musing, omakase-bento, clean, jazz, p-90, tonerider, rebel-90, brown-sugar, thr10ii"
target: "Acoustic translation of Faust & Wagner's Omakase Bento 'Epiphone P90 Musing' preset onto the Yamaha THR10ii, emulating the Brown Sugar 120pF pickup loading, woody body resonance, and glassy optical leveling."
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
      gain: 30
      bass: 52
      mid: 68
      treble: 42
      master: 80
    tempo: 110
    compressor:
      enabled: true
      sustain: 45
      level: 56
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
      decay: 38
      predelay: 8
      tone: 38
    gate:
      enabled: true
      thresh: 12
      decay: 50
---

# THR Epiphone P90 Musing — Les Paul (Tonerider Rebel 90s)

## Target Sound

This toneprint is an acoustic and technical translation of the **"Epiphone P90 Musing"** reference preset from the sister project's **Faust & Wagner "Omakase Bento"** solid-state amplifier head (`faust-and-wagner/OMAKASE_BENTO_SPECIFICATION.md`) directly into the **Yamaha THR10ii**.

The physical guitar is Mike's 2008 Epiphone Les Paul Standard Plus Top, upgraded with a matched set of Tonerider Rebel 90s (humbucker-sized P-90 single coils with Alnico II magnets, as cataloged in `tone-advisor/guitar_stable.md`). I know that P-90 single coils possess a punchy, wide dynamic range with a characteristic upper-mid presence peak around 3.5–4.0 kHz. In the Omakase Bento DSP circuit (`faust-and-wagner/faust/dsp/omakase_bento.dsp`), the "Epiphone P90 Musing" preset engages the **Brown Sugar** 120pF loading capacitor switch (`sugar_sw = 1`), which mathematically shifts the pickup/cable RLC resonant frequency from 3750 Hz down to 2750 Hz and lowers Q from 1.80 to 1.45. This rounds off abrasive pick click into warm, woody acoustic fundamental energy. Furthermore, Bento boosts the **Wood** gyrator band by `+2.0 dB @ 250 Hz` (bringing out the carved maple cap / mahogany body resonance), keeps the **Cavity** tamer at `-2.0 dB @ 420 Hz`, pushes vocal **Mids** by `+1.0 dB @ 1.6 kHz`, leaves **Treble** flat (`0.0 dB @ 3.2 kHz`), engages moderate optical leveling (`Lev Sens 3.0`), adds the Magnatone Doppler pitch vibrato (3.5 Hz / 2.5 depth), and sets the power section to **Induction** mode for pristine, tight-grip headroom.

On the Yamaha THR10ii, this response is captured using the **Classic Clean** (`THR10C_Deluxe`) amp model with high Master volume (8.0 / 10) and low Gain (3.0 / 10). To emulate the Brown Sugar loading capacitor, the THR's **Treble** knob is rolled down to `4.2 / 10`, while the **Middle** control is pushed to `6.8 / 10` (implementing the "Jazz Middle Rule" to reflect the Wood and vocal Mid boosts). The **California 1x12** (EVM-12L) cabinet emulation provides massive clean headroom and firm low-end control, while the **RedComp** optical compressor translates the Vactrol leveler.

---

## Signal Chain

```
[2008 Epiphone Les Paul Standard (Tonerider Rebel 90s Neck / Both)]
       │
       ▼
[Yamaha THR10ii Input]
       │
       ▼
[Noise Gate: Thresh 12%, Decay 50%]  <-- Tames idle P-90 single-coil hum
       │
       ▼
[RedComp Compressor: Sustain 45%, Level 56%]  <-- Translates Vactrol Leveler (Lev Sens 3.0)
       │
       ▼
[THR Classic Clean Amp Model (Fender Deluxe Reverb)]
• Gain: 3.0 / 10 | Master: 8.0 / 10 (Induction Headroom & Dynamic Weight)
• Bass: 5.2 / 10 | Mid: 6.8 / 10 (Wood & Vocal Body) | Treble: 4.2 / 10 (Brown Sugar Emulation)
       │
       ▼
[California 1x12 Cabinet Simulation (EVM-12L)]
       │
       ▼
[Modulation: StereoSquareChorus (Mix 25%, Depth 30%, Freq 35%)] <-- Translates Magnatone Vibrato (3.5Hz / 2.5)
       │
       ▼
[Reverb: Large Plate (Mix 16%, Decay 38%, Tone 38%)]
       │
       ▼
[Yamaha THR Stereo Speakers / Headphones]
```

---

## THR10ii Control Board

### 1. Physical Top Panel Knobs (Quick Reference)

| Knob | Physical Position (0–10) | Clock Setting | Purpose |
|---|---|---|---|
| **Amp Select** | **CLASSIC / CLEAN** | — | Clean, high-headroom American blackface platform. |
| **Gain** | **3.0** | ~9:00 | Preserves dynamic touch sensitivity and pure clean headroom. |
| **Master** | **8.0** | ~3:45 | Pushes power-amp simulation for warm optical bloom and string give. |
| **Bass** | **5.2** | ~12:15 | Warm lower fundamental support for P-90 single notes. |
| **Middle** | **6.8** | ~2:15 | **The "Jazz Middle" boost:** Simulates Bento's +2.0 dB Wood and +1.0 dB Mid gyrators. |
| **Treble** | **4.2** | ~11:00 | **Brown Sugar emulation:** Rolls off high P-90 click without dulling the note. |
| **Effect** | **~2.0 (Chorus zone)** | ~8:30 | Subtle Magnatone Doppler pitch shimmer. |
| **Echo/Rev** | **~1.8 (Plate zone)** | ~8:15 | Warm, intimate studio plate reflection. |

---

### 2. THR Remote App Deep Parameters

#### Amplifier Section
* **Amp Model**: `Classic Clean` (`THR10C_Deluxe`, cited in `scripts/preset_compiler/yamaha.py`)
* **Cabinet**: `California 1x12` (`SpkSimType: 12`, Mesa 1x12 loaded with Electro-Voice EVM-12L for tight grip and broad frequency response)
* **Gain (Drive)**: `30%` (`0.30`) — Clean headroom baseline
* **Master**: `80%` (`0.80`) — Generates tactile string compression and bloom
* **Bass**: `52%` (`0.52`) — Solid low-E fundamental
* **Middle**: `68%` (`0.68`) — Emphasizes woody top-plate and vocal chord extensions
* **Treble**: `42%` (`0.42`) — Smooth top-end curve recreating Brown Sugar loading

#### Dynamics & FX Pedals
* **Compressor (FX1)**: **ON** (`RedComp`)
  * **Sustain**: `45%` (`0.45`) — Translates Bento's Vactrol leveler (`Lev Sens 3.0`)
  * **Level**: `56%` (`0.56`) — Clean makeup gain
* **Modulation (FX2)**: **ON** (`StereoSquareChorus`)
  * **Mix**: `25%` (`0.25`) — Subtle acoustic shimmer
  * **Depth**: `30%` (`0.30`) — Translates Bento's `Vib Depth 2.5`
  * **Freq**: `35%` (`0.35`) — Translates Bento's `Vib Speed 3.5 Hz`
  * **Feedback**: `0%` (`0.00`) — Pure phase modulation without comb filter artifacts
  * **Pre**: `0%` (`0.00`) — Zero pre-delay
* **Delay / Echo (FX3)**: **OFF**
* **Reverb (FX4)**: **ON** (`Plate` / `LargePlate1`)
  * **Mix**: `16%` (`0.16`) — Natural room presence
  * **Decay**: `38%` (`0.38`) — Warm plate tail
  * **Pre-Delay**: `8 ms` (`0.08`) — Keeps P-90 attack upfront
  * **Tone**: `38%` (`0.38`) — Rolled-off high frequency damping
* **Noise Gate**: **ON**
  * **Threshold**: `12%` (`-84.5 dB`) — Effectively silences P-90 single-coil 60Hz hum at idle
  * **Decay**: `50%` (`0.50`) — Smooth, unchoked release

---

## Starting Point Guide

- **Guitar Setup**: Select the **Neck Rebel 90** (or both pickups in parallel for hollow chime). Roll the guitar's **Volume** knob back to **7.5–8.0** and the **Tone** knob to **7.0** (the classic 7/7 baseline). P-90s are famously touch-sensitive to volume pot taper; rolling back slightly cleans up the input and elevates lower-mid creaminess.
- **Picking Dynamics**: Play chord-melody and walking basslines with your thumb and flesh of your fingers. The high Master setting cushions hard transients, yielding a cello-like bloom on sustained double-stops.
- **Alternative Cabinet**: For a looser, more open-back vintage response, swap to the **Boutique 1x12** (`SpkSimType: 15`).

---

## Feedback History

### 2026-10-03 — initial
* Toneprint formulated from the reference `Epiphone P90 Musing.json` preset of Faust & Wagner's Omakase Bento solid-state amplifier head.
* Configured specifically for the 2008 Epiphone Les Paul Standard Plus Top upgraded with Tonerider Rebel 90s.
