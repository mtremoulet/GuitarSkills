---
amp: "Enigmatic '82 (UADx)"
created: 2026-07-26
guitar: "Gibson Les Paul Studio (490R neck pickup)"
id: paradise-enigmatic-dual-rig-driven
pickup_type: humbucker
preset_name: "Enigmatic Dual Rig Driven HB"
status: initial
tags: "dual-amp, driven, dumble, paradise-studio, enigmatic-82, humbucker, drive-pedals"
target: 'Vocal mid-range and driven lead amp for the parallel dual-amp setup. Features Enigmatic 82 Dumble ODS on Cream voicing with a 3-stage pre-amp drive block (Nashville OD / Blues Barker, Gold OD / Klon, TS OD / TS-808) disabled by default.'
tone-king-channel: bypassed
updated: 2026-07-26
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Voice: Cream
    Bass: 7.0
    Boost: false
    Bright: false
    Middle: 7.5
    Master: 6.0
    Presence: 0.5
    Treble: 3.5
    Volume: 5.5
  kuassa_blues_barker:
    enabled: false
    gain: 5.5
    tone: 5.0
    level: 1.5
  kuassa_blues_river:
    enabled: false
    gain: 4.5
    tone: 5.0
    level: 1.5
  clon_minotaur:
    enabled: false
    gain: 7.5
    output: 4.0
    treble: 4.5
  nembrini_808:
    enabled: false
    drive: 7.0
    level: 3.0
    tone: 5.0
  gold_overdrive:
    enabled: false
    gain: 7.5
    output: 4.0
    treble: 4.5
  nashville_overdrive:
    enabled: false
    gain: 5.5
    output: 1.5
    tone: 5.0
  ts_overdrive:
    enabled: false
    drive: 7.0
    level: 3.0
    tone: 5.0
  hitsville:
    decay: 2.0
    mix: 0.10
    pre_delay: 8.0
  la2a:
    gain: 28.0
    peak_reduction: 32.0
---

# Enigmatic '82 — Dual Rig Driven & Vocal Mids

## Target Sound

This toneprint represents **Path B (Driven Vocal Mids & Lead)** in our parallel dual-amp rig. 

Hosted inside **UAD Paradise Guitar Studio**, the **Enigmatic '82** (Dumble Overdrive Special emulation on Cream voice) provides dense lower-midrange body, vocal sustain, and tube sag. Path B is equipped with a 3-stage pre-amp drive pedal block (Pre FX) that is set **bypassed (off) by default**, allowing you to engage transparent soft-clipping, Klon boost, or Tube Screamer mid-push on demand while Path A maintains a pristine clean foundation.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0**; D.I. offset **-3.2 dB**).

---

### 2. UADx Paradise Guitar Studio — Pre FX Drive Block & Enigmatic '82

#### Pre FX Drive Block (All Disabled by Default)

| Order | Stompbox Module | Setting | Purpose |
|-------|-----------------|---------|---------|
| **Stage 1** | **Nashville OD / Blues Barker** | Disabled (Off) · Gain 2.5, Tone 5.0, Output 6.0 | Open, soft-clipping overdrive; adds smooth grit without cutting bass |
| **Stage 2** | **Gold Overdrive (Klon)** | Disabled (Off) · Gain 0.0, Output 7.5, Treble 4.5 | Transparent clean boost; adds high-mid sheen and level push |
| **Stage 3** | **TS Overdrive (TS-808)** | Disabled (Off) · Drive 3.0, Tone 5.0, Level 7.0 | Mid-hump boost with low-end roll-off; pushes Enigmatic into singing lead sustain |

#### Amp & Cabinet Settings

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **Enigmatic '82** | Dumble ODS circuit in Paradise Guitar Studio |
| Voice | **Cream** | Extended low-end response with singing upper-mid push |
| Input Jack | **NOR** (Normal) | Warm, saggy tube input stage (bypasses clinical solid-state FET input) |
| Skyline Mod | **On** | Skyline tone stack for famous Dumble midrange bloom |
| Preamp Volume | **5.5** | Preamp sweet spot for touch-sensitive breakup |
| Bass | **7.0** | Deep lower-mid weight |
| Middle | **7.5** | Heavily boosted midrange body (fills in Dream '65 scoop) |
| Treble | **3.5** | Smooths top end and tames harshness |
| Master | **6.0** | Power-amp tube bloom and sustain |
| Presence | **0.5** | Keeps top end round and silky |
| Cab | **2x12 Boutique D65** | Celestion G12-65 2x12 cab (SM57 + R121 mic blend) |
| Room Level | **10%** | Subtle room acoustics |

---

### 3. Amp Bus Mixer Gain Staging & Post-Summing LA-2A

* **Channel Parity Balance:** Trim the Enigmatic (Path B) channel by approximately **-5.5 dB** (keeping Dream '65 Path A at 0.0 dB) in the Element `Amp Bus Mixer` so both paths show visual level parity on the meters.
* **Master Summation Level:** Set the `Amp Bus Mixer` Master output fader to **-8.0 dB** to compensate for parallel dual-amp summation and prevent digital ceiling clipping.
* **Compressor:** UAD Teletronix LA-2A Silver (Peak Reduction 32, Gain 28) placed *after* the `Amp Bus Mixer`. Receives the -8 dB attenuated sum to hit target **-1 to -3 dB GR** on hard strums.
* **Reverb:** UAD Capitol Chambers / Hitsville (Mix 10%, Decay 2.0s, Pre-Delay 8ms) placed on parallel aux send.

---

## Starting Point Guide

- **Mixer Gain Staging**: In Element's `Amp Bus Mixer`, set the Master fader to **-8.0 dB** and trim Path B (Enigmatic) down to **-5.5 dB** for meter parity with Path A.
- **Drive Stacking Experiment**:
  1. Try turning on **Stage 1 (Nashville OD / Blues Barker)** alone for edge-of-breakup rhythm.
  2. Engage **Stage 2 (Klon / Gold OD)** into Stage 1 for a high-headroom solo volume lift.
  3. Turn on **Stage 3 (TS-808)** to tighten the bottom end and sail into violin-like Dumble lead sustain!
