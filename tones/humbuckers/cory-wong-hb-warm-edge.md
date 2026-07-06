---
amp: "Amp Snob (Archetype Cory Wong X)"
created: 2026-06-07
guitar: "Epiphone Les Paul Standard ('57CH neck pickup) / Epiphone Sheraton II"
id: cory-wong-hb-warm-edge
pickup_type: humbucker
preset_name: "HB Warm Edge"
status: tested
tags: "clean, edge-of-breakup, warm, les-paul, sheraton, humbucker, neural-dsp, cory-wong, amp-snob"
target: 'Warm, touch-sensitive clean tone with a hint of grit/breakup on the neck pickup, dialed in for dual-humbucker guitars like the Epiphone Les Paul and Sheraton.'
tone-king-channel: bypassed
updated: 2026-06-07
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: true
    selectedAmp: 2
    selectedCab: 2
    compressorActive: true
    compressorVolume: 55.0
    compressorCompression: 48.6
    compressorTone: 50.0
    compressorBlend: 35.0
    bigRigActive: true
    bigRigDrive: 67.4
    bigRigLevel: 26.9
    bigRigTone: 25.5
    tuberActive: false
    postalActive: false
    delayActive: false
    chorusActive: false
    washActive: true
    washShimmer: false
    washLowCut: 0.0
    washHighCut: 100.0
    washDecay: 9.2
    washMix: 24.5
    leftCabActive: true
    leftCab0MicType: 4
    leftCabMicLevel: 2.0
    leftCabDistance: 0.25
    leftCabPosition: 0.50
    leftRoomMicLevel: -28.0
    rightCabActive: false
    snobVolume: 38.0
    snobMaster: 75.0
    snobBass: 44.0
    snobMid: 52.0
    snobTreble: 50.0
    snobPresence: 50.0
    snobBright: false
    snobDrive: false
    snobOutputLevel: 70.0
    snobEQActive: true
    snobEQHpf: 20.0
    snobEQLpf: 20000.0
    snobEQBand1: 0.0
    snobEQBand2: 0.0
    snobEQBand3: -1.0
    snobEQBand4: 0.5
    snobEQBand5: 1.0
    snobEQBand6: -1.5
    snobEQBand7: 0.5
    snobEQBand8: 0.0
    snobEQBand9: 0.0
---

# HB Warm Edge — Boutique Warm Clean (Humbucker Variant)

## Target Sound

This toneprint is built around **"The Amp Snob"** (Dumble-style head) inside Archetype Cory Wong X, specifically dialed in for dual-humbucker guitars like the Epiphone Les Paul Standard (with the '57CH neck pickup) and the Epiphone Sheraton II. It creates a thick, compressed, and warm clean tone that sits right on the edge of breakup.

By combining the **Big Rig Overdrive** pedal as a low-gain boost with moderate parallel compression, the neck humbucker gets a very smooth, full, and singing sustain. The compression helps smooth out rougher edges and transients, making it highly forgiving and warm. While it lacks some of the sharp articulation of the Framus P-90, it provides a incredibly fat and creamy response.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed** (direct iD14 JFET Input 1 for maximum clarity and modeling transparency).

---

### 2. Archetype Cory Wong X — boutique character & drive

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 4th Position Compressor** | **Active** | **ON** | Adds parallel sustain and smooths out transients |
| | **Blend** | **35%** | Parallel mix; keeps the pick attack snappy |
| | **Tone** | **50%** | Flat treble response |
| | **Compression** | **48.6%** | Pushed dynamic control |
| | **Volume** | **55%** | Gain matching |
| **Big Rig Overdrive** | **Active** | **ON** | Low-gain clean drive adding the edge-of-breakup grit |
| | **Drive** | **67.4%** | Gain structure sweet spot |
| | **Level** | **26.9%** | Master output level matching |
| | **Tone** | **25.5%** | Darker voicing to roll off potential digital fizz |

*All other Pre FX (Envelope Filter, Tuber OD, Wah, Envelope) are **BYPASSED**.*

**Amp Section — "The Amp Snob"**

All parameters are specified in percentages (0–100%).

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Amp Snob** | Clean Dumble-style head |
| Volume (Gain) | **38%** | Keeps the preamp clean, passing drive duties to the Big Rig pedal |
| Master | **75%** | virtual power amp saturation and warmth |
| Drive Switch | **OFF** | Bypasses high gain mode |
| Bright Switch | **OFF** | Smooth, rounded high end |
| Bass | **44%** | Tightens low end, preventing mud on humbuckers |
| Middle | **52%** | Throatiness and vocal midrange projection |
| Treble | **50%** | Neutral high frequencies |
| Presence | **50%** | Power-amp air |
| Output | **70%** | Level trim |

**Cab Section (Unlinked Cabinets)**

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **On** | Matches speaker cabinet to active amp |
| Cab Type | **Snob** | 2x12 open-back boutique cabinet |
| Cab L | **Active** | Primary mic |
| Mic L Type | **Ribbon 121** | Creamy, warm character; softens transients |
| Position L | **0.50** | Placed off-center for balanced warmth |
| Distance L | **0.25** | Standard distance to capture cabinet air |
| Room Send L | **−28.0 dB** | Keeps the tone direct, tight, and dry |
| Cab R | **BYPASSED** | Single mic for perfect phase coherence |

**EQ Section (Amp Snob 9-Band Graphic EQ)**

| Band | Setting | Purpose |
|------|---------|---------|
| EQ Status | **Active** | Corrective voicing curve |
| 65 Hz | 0.0 dB | Neutral |
| 125 Hz | 0.0 dB | Neutral |
| 250 Hz | −1.0 dB | Cleans up muddy build-up from neck pickup |
| 500 Hz | +0.5 dB | Boosts lower midrange woodiness |
| 1 kHz | +1.0 dB | Pushes vocal midrange |
| 2 kHz | −1.5 dB | Smooths pick-attack harshness |
| 4 kHz | +0.5 dB | Retains natural body chime |
| 8 kHz | 0.0 dB | Neutral |
| 16 kHz | 0.0 dB | Neutral |
| HPF / LPF | Default | 20 Hz High-Pass / 20.0 kHz Low-Pass |

**Post FX Section**

| Device | Control | Setting | Purpose |
|--------|---------|---------|---------|
| **The Wash** | **Active** | **ON** | Adds a touch of spatial delay/reverb wash |
| | **Mix** | **24.5%** | Blend level |
| | **Decay** | **9.2%** | Short spatial trails |
| | **High Cut** | **100.0%** | Unfiltered high frequencies |
| | **Low Cut** | **0.0%** | Unfiltered low frequencies |
| | **Shimmer** | **OFF** | Bypasses pitch shifting |

---

## Starting Point Guide

- **Controlling the Breakup**: Humbuckers will drive this preset a bit harder than P-90s. Use your **Guitar Volume knob** (rolled back to **6 or 7**) to clean up the tone for a rounder, warm jazz-box sound, and raise it for a punchier, bluesy crunch.
- **Tone Knob Calibration**: The '57CH neck humbucker is dark by nature. If the tone feels a bit too dark or compressed, roll your **Guitar Tone knob** up to **10**, or try bypassing the graphic EQ to let more high end breathe.
- **Recovering Nuance (Compressor Trim)**: Because humbuckers naturally compress, the current parallel compressor settings (35% Blend, 48.6% Comp) can squash your picking dynamics. To let the LP's woodiness breathe, roll the **Blend back to 20-25%** and lower **Compression to 30%**.
- **Gain-Staging Rollback**: Humbuckers run hotter than P-90s. If the tone breaks up too early, lower the Amp Snob **Volume (Gain)** from **38% to 32-35%** to recover headroom and restore touch-sensitive nuance.
- **The Wash Bypass**: If you prefer to use external reverbs (like UAD Hitsville), bypass the internal **Wash** block and route the track to your shared reverb bus in Logic Pro.

---

## Feedback History

### 2026-06-07 — tested
Tested on the Epiphone Les Paul Standard with the 57CH neck pickup. Sounds surprisingly good and full. The compression helps smooth out rougher playing edges, providing a very warm, thick, and responsive jazz-blues voice. Articulation is slightly less clear than the Framus, but it has excellent body and warmth. Status set to `tested`.

*Note: Added tuning recommendations to Starting Point Guide to roll back parallel compression (Blend to 20-25%) and amp input gain (Volume to 32-35%) to avoid the "compression trap" and let the humbucker's natural woody character shine.*
