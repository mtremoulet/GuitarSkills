---
amp: "Yamaha THR10II"
created: 2026-08-17
guitar: "2024 Fender Player II Telecaster (Neck, Middle, or Bridge single-coils)"
id: thr-tele-blackface-sparkle
pickup_type: single-coil
preset_name: "THR Tele Blackface Sparkle"
status: initial
tags: "clean, sparkle, blackface, fender, deluxe-reverb, telecaster, spring-reverb, thr10ii, single-coil"
target: 'Pristine, dynamic American Blackface clean tone with sparkling highs, tight low-end, and lush spring reverb for the Telecaster.'
tone-king-channel: bypassed
updated: 2026-08-17
preset_data:
  amp_platform: yamaha_thr
  yamaha_thr:
    amp:
      category: Classic
      model: Clean
    cab: American 1x12
    eq:
      gain: 36
      bass: 54
      mid: 52
      treble: 55
      master: 72
    tempo: 120
    compressor:
      enabled: true
      sustain: 35
      level: 60
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
      type: Spring
      mix: 24
      time: 40
      predelay: 0
      tone: 50
    gate:
      enabled: true
      thresh: 10
      decay: 50
---

# THR Tele Blackface Sparkle — Telecaster

## Target Sound

This toneprint captures the quintessential, pure American tube clean sound: a **1965 Fender Blackface Deluxe Reverb** paired with the **Fender Player II Telecaster**. 

It delivers sparkling, crystalline top-end chime, firm low-end definition, and crystalline dynamic headroom that instantly reacts to picking nuances. Using the **Classic Clean** (`THR10C_Deluxe`) model and the matching **American 1x12** (`DRVB` — Jensen C12K speaker) cabinet, it is dialed to highlight the Telecaster's bell-like neck warmth, funky middle position, and twangy bridge bite without any harsh ice-pick transients. A touch of optical-style compression softens fast transients and adds singing sustain, while the classic Fender spring reverb tank provides lush spatial depth.

---

## THR10ii Control Board

### 1. Amplifier Section

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Classic Clean (`THR10C_Deluxe` / '65 Deluxe Reverb) | Iconic 6V6/6L6 Blackface preamp with high headroom and sparkling harmonic sheen. |
| Cabinet | American 1x12 (`DRVB`) | Fender Deluxe Reverb 1x12 open-back cab with Jensen C12K speaker emulation. |
| Gain (Drive) | 3.6 / 10 | Crystal-clear clean baseline with sweet harmonic presence on harder strums. |
| Master | 7.2 / 10 | High output setting to allow full dynamic range and uncompressed headroom. |
| Bass | 5.4 / 10 | Tight, percussive low end that keeps chord bass notes clear and punchy. |
| Middle | 5.2 / 10 | Balanced midrange baseline that preserves natural Blackface scoop while maintaining body. |
| Treble | 5.5 / 10 | Sparkling high-end air and bell-like chime without piercing treble spikes. |

---

### 2. Dynamics & FX Pedals

#### Compressor (FX1)
* **Status**: **ON**
* **Type**: Stomp Comp (`RedComp`)
* **Sustain**: 3.5 / 10 — Mild optical-style compression to cushion string pick attack transients and enhance sustain.
* **Level**: 6.0 / 10 — Clean unity output level.

#### Modulation Effect (FX2)
* **Status**: **OFF** *(Tip: Turn on `BiasTremolo` with Depth 50% / Speed 45% for vintage Fender tube tremolo vibe!)*

#### Delay / Echo (FX3)
* **Status**: **OFF**

#### Reverb (FX4)
* **Status**: **ON**
* **Type**: Spring Reverb (`StandardSpring`)
* **Wet/Dry**: 24% — Classic Fender spring reverb tank drip and bloom.
* **Decay (Time)**: 4.0 / 10 — Medium spring decay.
* **Tone**: 5.0 (noon) — Balanced, authentic spring sparkle.

#### Noise Gate
* **Status**: **ON**
* **Threshold**: 10% — Transparent gating to eliminate 60-cycle single-coil hum while idling.
* **Decay**: 50% — Smooth decay release.

---

## Starting Point Guide

* **Physical Prep**: 
  * **Neck Pickup**: Thick, glassy, bell-like tones ideal for blues, soul, or clean rhythm.
  * **Middle (Both Pickups)**: Balanced, sparkling funk and pop rhythm comping.
  * **Bridge Pickup**: Roll guitar **Tone** knob back to **7.5–8.0** for sweet country twang, chicken pickin', or crisp rock rhythm without harsh high frequencies.
* **First Adjustment**: If you want a wider, more expansive stereo clean, swap the Cabinet to **American 2x12** (`TRVB` — Twin Reverb 2x12).
