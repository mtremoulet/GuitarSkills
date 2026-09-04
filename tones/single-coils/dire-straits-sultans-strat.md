---
id: dire-straits-sultans-strat
preset_name: "Dire Straits Sultans Strat"
created: "2026-06-28"
updated: "2026-06-28"
guitar: "Fender Player II Telecaster / Squier Stratocaster (Middle + Bridge or Neck + Middle position — 'quack')"
target: 'Pristine 1978 Mark Knopfler fingerstyle clean quack on single-coils (''Sultans of Swing''), with dynamic peak leveling and articulate high-end response.'
tags: "dire-straits, single-coil, stratocaster, clean, fingerstyle, rock, knopfler, uad_paradise"
tone-king-channel: bypassed
amp: "Dream '65 (UADx)"
status: initial
pickup_type: single-coil
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 3.5
    Treble: 6.5
    Bass: 4.5
    Bright: true
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  la2a:
    peak_reduction: 40
    gain: 30
    compress: true
  hitsville:
    mix: 0.12
    pre_delay: 10.0
    decay: 1.5

    wet_solo: false
---

# Dire Straits — Sultans Strat Fingerstyle Clean

## Target Sound

This toneprint captures the iconic, percussive single-coil clean tone of Mark Knopfler on Dire Straits' classic 1978 anthem **"Sultans of Swing."** 

Knopfler's signature tone relies on a red 1961 Stratocaster set to the "in-between" pickup positions (Position 2: Bridge + Middle, or Position 4: Neck + Middle) played exclusively with bare fingers rather than a pick. This flesh-on-string contact produces strong transient spikes followed by a warm, woody body. 

Running into high-headroom Fender Blackface circuitry (emulated by the **UADx Dream '65** set clean and crisp), light optical compression, and subtle room acoustics, this chain delivers pristine high-end chime, articulate "quack," and fast dynamic response.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom).

---

### 2. UADx Paradise Guitar Studio / Dream '65 — pristine clean platform

#### Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for solo lift |
| Gain | **0.0** | Zero added distortion |
| Output | **7.5** | Pushes front end for level lift |
| Treble | **4.5** | Smooth boost response |

#### Amp & Cab Settings (Dream '65)

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **Dream '65** | 1965 Fender Deluxe Reverb emulation |
| Volume | **3.5** | High-headroom clean sweet spot; keeps signal uncompressed by power tubes |
| Treble | **6.5** | Elevated treble to highlight single-coil glass and pick/finger attack |
| Bass | **4.5** | Slightly pulled back to prevent low-end boom on finger-picked bass notes |
| Bright Switch | **ON** | Adds top-end sparkle and bite essential for Strat quack |
| Cabinet | **Oxford** | Classic 1965 1x12 sound with articulate high end |
| Room Level | **10%** | Subtle room air to blend mics |

---

### 3. UADx LA-2A Silver Compressor — peak leveling for fingerstyle

Fingerstyle playing inherently produces wider dynamic swings than pick playing. The optical compression of the LA-2A Silver evened out the transients while preserving natural attack.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | **40** | Targets `2–4 dB` of gain reduction on firm finger snaps |
| Gain | **30** | Makeup gain calibrated for healthy DAW level (~ −12 dBFS) |
| Mode | **Compress** (3:1) | Transparent optical leveling |

---

### 4. UADx Hitsville Reverb Chambers — tight acoustic space (Aux 2)

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Tight Detroit room reflections |
| Mix | **Wet Solo (100%)** | Aux send routing |
| Decay | **9:00** | Short decay to prevent rhythm blurring |
| Pre-Delay | **10 ms** | Preserves immediate pick attack before reverb envelope |

---

## Starting Point Guide

- **Pickup Selection:** Set your Stratocaster or Telecaster to an in-between position (Bridge + Middle on Strat, or Middle pickup setting on Tele with dual coils) to engage the signature out-of-phase "quack."
- **Finger Technique:** Play with the flesh of your thumb and fingers rather than a plectrum to match the woody, percussive attack of the record.
- **Variation — The "Money for Nothing" Les Paul Tone:** To jump from 1978 Knopfler to 1985 *Brothers in Arms* era:
  1. Switch to your **Gibson Les Paul Studio** (Bridge pickup).
  2. Engage an overdrive or push amp Volume to **6.5**.
  3. Engage a Wah pedal (or parametric EQ with a high Q boost around 1.2 kHz–1.5 kHz) left rocked halfway forward ("half-cocked wah") for that legendary honky, resonant mid-range crunch!

---

## Feedback History

### 2026-06-28 — initial
Created as a dedicated single-coil toneprint for Mark Knopfler's pristine fingerstyle clean tone on "Sultans of Swing". Uses Dream '65 clean platform with bright switch active, LA-2A Silver peak leveling, and disabled Gold Overdrive pre-amp option.
