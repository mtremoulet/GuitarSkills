---
id: cory-wong-funk-envelope
preset_name: "Funk Envelope"
created: 2026-06-23
updated: 2026-06-23
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s)"
target: 'Percussive, dynamic funk and R&B tone featuring an active envelope filter (''The Postal Service'') that triggers based on your picking velocity.'
tags: "clean, funk, envelope-filter, r&b, p-90, framus"
tone-king-channel: bypassed
amp: "The Clean Machine (Archetype Cory Wong X)"
status: initial
pickup_type: p-90
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: true
    selectedAmp: 1
    selectedCab: 1
    compressorActive: false
    tuberActive: false
    bigRigActive: false
    postalActive: true
    postalSensitivity: 40.0
    postalDecay: 250.0
    postalAttack: 150.0
    postalRange: 800.0
    cleanVolume: 30.0
    cleanBright: false
    cleanBass: 50.0
    cleanMid: 50.0
    cleanTreble: 50.0
    cleanPresence: 50.0
    cleanOutputLevel: 70.0
    delayActive: false
    washActive: false
    chorusActive: false
---

# Funk Envelope — Dynamic R&B Filter

## Target Sound

This toneprint is designed for classic percussive funk and R&B rhythm work, using the **Postal Service** envelope filter. Rather than a static wah, an envelope filter sweeps its cutoff frequency dynamically in response to your picking strength.

We load **"The Clean Machine"** (Amp 1) for its transparent, high-headroom character. We intentionally **bypass the compressor** in the plugin because compression squashes the dynamics that the envelope filter needs to trigger correctly. 

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed** (direct direct-in is critical here so that the full dynamic range of your picking hand hits the envelope filter).

---

### 2. Archetype Cory Wong X — Envelope Rig

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The Postal Service** | **Active** | **ON** | Envelope/Auto-Wah sweep |
| | **Sensitivity** | **40%** | Threshold trigger; calibrated to open up on hard pick strikes and stay closed on light picking |
| | **Attack** | **150 ms** | How fast the filter opens up |
| | **Decay** | **250 ms** | How fast the filter sweeps back down |
| | **Range** | **800 Hz** | Frequency sweep width |

*All other Pre FX (Compressor, Overdrives) are **BYPASSED**.*

**Amp Section — "The Clean Machine"**

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Clean Machine** | Transparent clean Fender-style head |
| Volume | **30%** | Keeps the input clean and dynamic |
| Bright Switch | **OFF** | Removes high-end clickiness |
| Bass / Mid / Treble | **50%** | Neutral baseline |
| Presence | **50%** | Neutral high air |
| Output | **70%** | Clean trim |

**Cab Section (Linked)**

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **On** | Matches cabinet to Clean Machine |
| Cab Type | **Clean** | Matching 1x12 open-back cabinet |

---

## Starting Point Guide

- **Fine-Tuning the Trigger:** The **Sensitivity** knob on the filter is the most important control. P-90s have healthy output, but if you find the filter is "quacking" too easily on soft notes, roll the sensitivity down to **30–35%**. If you have to strike the strings too hard to open the filter, raise it to **45–50%**.
- **Guitar Settings:** Use the **Bridge P-90** or **Middle position** for the snappiest filter trigger. Keep your volume knob on the guitar at **10** so the filter gets the maximum transient spike to open up.
- **Sax-Like Articulation:** Think like a horn player. Staccato notes and muted scratch strums will make the envelope open and shut quickly, creating that classic percussive funk "chank."
