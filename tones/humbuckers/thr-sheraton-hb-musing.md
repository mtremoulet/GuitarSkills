---
amp: "Yamaha THR10II"
created: 2026-10-03
guitar: "2013 Epiphone Sheraton II (Thomastik-Infeld Flatwound 10s, Neck Humbucker)"
id: thr-sheraton-hb-musing
pickup_type: humbucker
preset_name: "THR Sheraton HB Musing"
status: initial
tags: "musing, omakase-bento, jazz, flatwounds, velvet, semi-hollow, sheraton, humbucker, thr10ii"
target: "Acoustic translation of Faust & Wagner's Omakase Bento 'Sheraton HB Musing' preset onto the Yamaha THR10ii, taming semi-hollow cavity wolf tones while delivering smoky velvet jazz comping on flatwound strings."
tone-king-channel: bypassed
updated: 2026-10-03
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Clean
    cab: Boutique 1x12
    eq:
      gain: 28
      bass: 56
      mid: 48
      treble: 36
      master: 76
    tempo: 110
    compressor:
      enabled: true
      sustain: 52
      level: 55
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
      mix: 18
      decay: 40
      predelay: 5
      tone: 35
    gate:
      enabled: true
      thresh: 10
      decay: 50
---

# THR Sheraton HB Musing — Epiphone Sheraton II

## Target Sound

This toneprint is an acoustic and technical translation of the **"Sheraton HB Musing"** reference preset from the sister project's **Faust & Wagner "Omakase Bento"** solid-state amplifier head (`faust-and-wagner/OMAKASE_BENTO_SPECIFICATION.md`) directly into the **Yamaha THR10ii**.

The physical guitar is the 2013 Epiphone Sheraton II semi-hollow body, strung with Thomastik-Infeld Jazz Swing Flatwound 10s (the "Velvet Jazz Box", cataloged in `tone-advisor/guitar_stable.md`). I know that semi-hollow guitars with flatwounds produce rich acoustic air and fundamental warmth, but are notoriously prone to internal f-hole / cavity wolf-tone resonance around 400–450 Hz, which can easily turn low-register chord comping boomy and muddy.

In the Omakase Bento DSP circuit (`faust-and-wagner/faust/dsp/omakase_bento.dsp`), the "Sheraton HB Musing" preset solves this through surgical active filtering:
1. **Cavity Tamer Notch (`-3.5 dB @ 420 Hz, Q = 1.85`)**: Aggressively scoops out the Helmholtz cavity resonance of the semi-hollow box.
2. **Wood Resonance Boost (`+2.5 dB @ 250 Hz, Q = 1.30`)**: Injects rich acoustic top-plate bloom and lower-string warmth.
3. **Brown Sugar Switch (`sugar_sw = 1`)**: Engages the 120pF loading capacitor to soften pick attack on flatwound strings.
4. **Treble Contour (`-1.0 dB @ 3.2 kHz`)**: Rolls off top-end clack for dark, velvety jazz articulation.
5. **Vactrol Optical Leveler (`Lev Sens 4.0`)**: Provides a generous dynamic compression cushion that lifts soft chord inner voices.
6. **Magnatone True Pitch Vibrato (3.5 Hz / 2.5 depth)**: Subtle Doppler motion for floating ballad chords.
7. **Heat Source (Induction)**: Ultra-high damping factor ($D > 200$) for pristine transient grip and tight bass fundamentals.

On the Yamaha THR10ii, this profile is realized through the **Classic Clean** (`THR10C_Deluxe`) amp model paired with the **Boutique 1x12** (`SpkSimType: 15`) open-back cabinet emulation. The **Middle** knob is dialed to `4.8 / 10` (slightly below noon) to emulate Bento's -3.5 dB cavity notch, the **Bass** is set to `5.6 / 10` for warm body, and **Treble** is rolled back to `3.6 / 10` to produce the dark "Electronic Veil" velvet jazz contour.

---

## Signal Chain

```
[2013 Epiphone Sheraton II (Neck Humbucker, Flatwound 10s)]
       │
       ▼
[Yamaha THR10ii Input]
       │
       ▼
[Noise Gate: Thresh 10%, Decay 50%]
       │
       ▼
[RedComp Compressor: Sustain 52%, Level 55%]  <-- Translates Vactrol Leveler (Lev Sens 4.0)
       │
       ▼
[THR Classic Clean Amp Model (Fender Deluxe Reverb)]
• Gain: 2.8 / 10 | Master: 7.6 / 10 (Induction Headroom & Dynamic Cushion)
• Bass: 5.6 / 10 | Mid: 4.8 / 10 (Cavity Notch Emulation) | Treble: 3.6 / 10 (Velvet High-Cut)
       │
       ▼
[Boutique 1x12 Cabinet Simulation (Open-Back Wood Air)]
       │
       ▼
[Modulation: StereoSquareChorus (Mix 25%, Depth 30%, Freq 35%)] <-- Translates Magnatone Vibrato (3.5Hz / 2.5)
       │
       ▼
[Reverb: Large Plate (Mix 18%, Decay 40%, Tone 35%)]
       │
       ▼
[Yamaha THR Stereo Speakers / Headphones]
```

---

## THR10ii Control Board

### 1. Physical Top Panel Knobs (Quick Reference)

| Knob | Physical Position (0–10) | Clock Setting | Purpose |
|---|---|---|---|
| **Amp Select** | **CLASSIC / CLEAN** | — | Clean, transparent American blackface foundation. |
| **Gain** | **2.8** | ~8:45 | High-headroom clean platform; zero preamp grit. |
| **Master** | **7.6** | ~3:15 | Dynamic power section compression for warm chord bloom. |
| **Bass** | **5.6** | ~12:45 | Warm, woody low-end foundation for flatwound walkups. |
| **Middle** | **4.8** | ~11:45 | **Cavity Notch Emulation:** Scooped below noon to prevent 420 Hz semi-hollow boxiness. |
| **Treble** | **3.6** | ~10:15 | **The Velvet High-Cut:** Removes flatwound pick click; delivers dark smokey jazz tone. |
| **Effect** | **~2.0 (Chorus zone)** | ~8:30 | Gentle Magnatone Doppler pitch shimmer. |
| **Echo/Rev** | **~2.0 (Plate zone)** | ~8:30 | Warm studio plate reverb tail with darkened tone. |

---

### 2. THR Remote App Deep Parameters

#### Amplifier Section
* **Amp Model**: `Classic Clean` (`THR10C_Deluxe`, cited in `scripts/preset_compiler/yamaha.py`)
* **Cabinet**: `Boutique 1x12` (`SpkSimType: 15`, Matchless open-back 1x12 for natural acoustic wood resonance and air)
* **Gain (Drive)**: `28%` (`0.28`) — Uncompromised clean headroom
* **Master**: `76%` (`0.76`) — Tight-grip dynamic weight and tactile string give
* **Bass**: `56%` (`0.56`) — Warm acoustic low-E support
* **Middle**: `48%` (`0.48`) — Compensates for semi-hollow f-hole cavity resonance
* **Treble**: `36%` (`0.36`) — Velvet jazz response with softened transients

#### Dynamics & FX Pedals
* **Compressor (FX1)**: **ON** (`RedComp`)
  * **Sustain**: `52%` (`0.52`) — Translates Bento's Vactrol optical leveler (`Lev Sens 4.0`)
  * **Level**: `55%` (`0.55`) — Clean makeup gain
* **Modulation (FX2)**: **ON** (`StereoSquareChorus`)
  * **Mix**: `25%` (`0.25`) — Subtle pitch shimmer
  * **Depth**: `30%` (`0.30`) — Translates Bento's `Vib Depth 2.5`
  * **Freq**: `35%` (`0.35`) — Translates Bento's `Vib Speed 3.5 Hz`
  * **Feedback**: `0%` (`0.00`) — Pure phase modulation without comb filter artifacts
  * **Pre**: `0%` (`0.00`) — Zero pre-delay
* **Delay / Echo (FX3)**: **OFF**
* **Reverb (FX4)**: **ON** (`Plate` / `LargePlate1`)
  * **Mix**: `18%` (`0.18`) — Lush studio ambiance
  * **Decay**: `40%` (`0.40`) — Smooth, warm decay that floats behind complex chord voicings
  * **Pre-Delay**: `5 ms` (`0.05`)
  * **Tone**: `35%` (`0.35`) — Darkened high dampening for vintage salon mood
* **Noise Gate**: **ON**
  * **Threshold**: `10%` (`-86.4 dB`) — Pristine, silent background
  * **Decay**: `50%` (`0.50`) — Smooth, natural chord sustain

---

## Starting Point Guide

- **Guitar Setup**: Switch to the **Neck** humbucker. Set guitar **Volume** to **8.0** and **Tone** to **7.0**. This rolls off any remaining high-frequency bite from the Alnico magnet, allowing the flatwound fundamental to speak with velvety authority.
- **Chord Extensions**: When playing 4-to-6 note chord extensions (drop-2 voicings, m7b5, 13ths), the combination of the scooped Mid setting and the optical leveler keeps the interior voices distinct and transparent without intermodulation clutter.
- **Alternate Pickup Blend**: Switch to the middle toggle position (Neck + Bridge humbuckers in parallel). This adds a delicate acoustic snap to bossa nova and rhythm comping while retaining the warm low-end anchor.

---

## Feedback History

### 2026-10-03 — initial
* Toneprint formulated from the reference `Sheraton HB Musing.json` preset of Faust & Wagner's Omakase Bento solid-state amplifier head.
* Configured specifically for the 2013 Epiphone Sheraton II strung with Thomastik-Infeld Jazz Swing Flatwound 10s.
