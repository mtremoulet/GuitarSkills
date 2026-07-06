---
amp: "Yamaha THR10II"
created: 2026-06-09
guitar: "Epiphone Sheraton II (neck humbucker, flatwound strings)"
id: thr-velvet-hb-jazz
pickup_type: humbucker
preset_name: "THR Velvet Humbucker Jazz"
status: initial
tags: "jazz, clean, warm, plate, compressor, humbucker, semihollow, thr10ii"
target: 'A warm, woody, and mellow jazz clean tone for the semihollow Sheraton''s neck humbucker.'
tone-king-channel: bypassed
updated: 2026-06-09
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Clean
    cab: Boutique 1x12
    eq:
      gain: 30
      bass: 65
      mid: 45
      treble: 35
      master: 75
    tempo: 120
    compressor:
      enabled: true
      sustain: 50
      level: 55
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
      mix: 20
      decay: 40
      predelay: 5
      tone: 40
    gate:
      enabled: true
      thresh: 10
      decay: 50
---

# THR Velvet Humbucker Jazz — Sheraton II

## Target Sound

This toneprint is designed to produce a warm, woody, and mellow jazz tone directly out of the **Yamaha THR10ii**, specifically voiced for the neck humbucker of the **Epiphone Sheraton II** semi-hollow body guitar fitted with flatwound strings. 

Flatwounds naturally emphasize fundamental tones and roll off the top-end click, but can sometimes sound overly dark or tubby on a humbucker neck position. To combat this, we use the **Classic Clean** (Fender Deluxe Reverb) engine which has a natural midrange focus and slight scoop. When combined with a **Boutique 1x12** open-back cabinet emulation, the tone blooms with woody resonance and acoustic depth without becoming muddy.

---

## THR10ii Control Board

### 1. Amplifier Section

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Classic Clean | Bright Fender Deluxe voicing; high headroom keeps the neck pickup clean. |
| Cabinet | Boutique 1x12 | Adds custom open-back cabinet wood resonance and warm projection. |
| Gain (Drive) | 3.0 / 10 | Completely clean headroom zone — zero preamp breakup. |
| Master | 7.5 / 10 | Pushes the power section simulation to compress pick attacks and add richness. |
| Bass | 6.5 / 10 | Rich low-end body for chords and single-note walkups. |
| Middle | 4.5 / 10 | Slightly pulled back to keep the low-mids from getting boxy. |
| Treble | 3.5 / 10 | Mellows the pick snap on the flatwounds for a velvety, dark jazz response. |

---

### 2. Dynamics & FX Pedals

#### Compressor (FX1)
* **Status**: **ON**
* **Type**: Stomp Comp
* **Sustain**: 5.0 / 10 — Levels string volume during jazz runs and balances arpeggio voices.
* **Level**: 5.5 / 10 — Output matching makeup gain.

#### Modulation Effect (FX2)
* **Status**: **OFF**

#### Delay / Echo (FX3)
* **Status**: **OFF**

#### Reverb (FX4)
* **Status**: **ON**
* **Type**: Plate Reverb
* **Wet/Dry**: 20% — Lower-level return for a natural studio plate reflection.
* **Decay**: 4.0 / 10 — Mellow, warm reverb decay tail that doesn't muddy complex chords.
* **Tone**: 4.0 / 10 — Warm reverb tone profile.

#### Noise Gate
* **Status**: **ON**
* **Threshold**: 10% — Minimal gate just to keep the signal path pristine.
* **Decay**: 50% — Smooth release.

---

## Starting Point Guide

* **Physical Prep**: Select the neck pickup on your Sheraton II. Keep the guitar's volume at **10** for maximum dynamics, and roll the tone knob down to **7** if you want to emphasize the woody fundamental even more.
* **First Adjustment**: If your flatwound strings feel a bit too dark or lack clarity in the lower registers, bump the **Treble** control up to **4.0** or shift the **Middle** down to **4.0** to clear space.
* **Alternative Cabinet**: Swap to the **American 1x12** (Fender Deluxe Reverb 1x12) cabinet for a more classic, tighter, and direct blackface response.
