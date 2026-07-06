---
amp: "The Clean Machine (Archetype Cory Wong X)"
created: 2026-07-02
guitar: "Fender Player II Telecaster (Neck position, Flatwounds)"
id: cory-wong-electronic-veil
pickup_type: single-coil
preset_name: "The Electronic Veil ACWX"
status: initial
tags: "jazz, telecaster, dark, warm, bickert, flatwounds, neural-dsp, cory-wong"
target: 'Ed Bickert ''Electronic Veil'' in ACWX — extremely dark, warm, and intimate jazz clean with severe high-cut and transient blunting.'
tone-king-channel: bypassed
updated: 2026-07-02
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: false
    bigRigActive: false
    chorusActive: false
    delayActive: false
    leftCab0MicType: 4
    leftCabActive: true
    leftCabDistance: 0.25
    leftCabPosition: 0.48
    leftRoomMicLevel: -28.0
    postalActive: false
    rightCabActive: false
    selectedAmp: 1
    selectedCab: 1
    compressorActive: true
    compressorVolume: 55.0
    compressorCompression: 35.0
    compressorTone: 40.0
    compressorBlend: 45.0
    cleanVolume: 30.0
    cleanBright: false
    cleanBass: 42.0
    cleanMid: 58.0
    cleanTreble: 30.0
    cleanPresence: 40.0
    cleanOutputLevel: 75.0
    cleanEQActive: true
    cleanEQHpf: 20.0
    cleanEQLpf: 3800.0
    cleanEQBand1: 0.0
    cleanEQBand2: 0.0
    cleanEQBand3: 2.0
    cleanEQBand4: 1.0
    cleanEQBand5: 0.0
    cleanEQBand6: -2.0
    cleanEQBand7: -6.0
    cleanEQBand8: -10.0
    cleanEQBand9: -12.0
    tuberActive: false
    washActive: true
    washMix: 8.0
    washDecay: 20.0
    washShimmer: false
---

# The Electronic Veil — Archetype Cory Wong X

## Target Sound

This toneprint is the Archetype Cory Wong X (ACWX) standalone equivalent of **The Electronic Veil (Ed Bickert Style)**, optimized for your **Fender Player II Telecaster** (Neck position, Flatwounds).

The goal is to recreate the dark, warm, and intimate "veiled" tone that Bickert pioneered by rolling off his Tele's physical tone control and running into a high-headroom, flat amplifier. To replicate this extreme high-cut transient blunting, we use **"The Clean Machine"** with the **Bright switch OFF**, treble rolled back to **30%**, and a custom Graphic EQ setup. We set the Graphic EQ's Low-Pass Filter (LPF) to **3.8 kHz** and roll off the 4 kHz, 8 kHz, and 16 kHz bands by up to **-12 dB**.

We engage **"The 4th Position Compressor"** to level out pick/thumb dynamics and enhance note bloom, pair the amp with a warm Ribbon 121 mic model off-center, and use a dry, subtle reverb level to provide physical air without an obvious spatial tail.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom).

---

### 2. Archetype Cory Wong X — standalone channel strip

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 4th Position Compressor** | **Active** | **ON** | Optical-style compression for note bloom |
| | **Blend** | **45%** | Parallel mix; balances note attack with sustain |
| | **Tone** | **40%** | Darkened compressor tone to match the veil |
| | **Compression**| **35%** | Moderate compression depth |
| | **Volume** | **55%** | Unity level |

*All other Pre FX are bypassed.*

**Amp Section — "The Clean Machine"**

All parameters are specified in percentages (0–100%).

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Clean Machine** | High-headroom tube clean platform |
| Volume (Gain) | **30%** | Clean preamp setting |
| Bright Switch | **OFF** | Essential to prevent high-end transients from popping through |
| Bass | **42%** | Controlled low end; flatwounds already provide plenty of body |
| Middle | **58%** | Slightly pushed to keep the midrange warm and wood-like |
| Treble | **30%** | Rolled back to soften the top-end chime |
| Presence | **40%** | Smooth power amp high end |
| Output | **75%** | Output level trim |

**Cab Section (Unlinked Cabinets)**

We unlink the cabinets to pair the Clean Machine with a warm ribbon mic.

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **Off** | Unlinked for custom mic pairing |
| Cab Type | **Clean** | Matching 2x12 open-back cabinet |
| Cab L | **Active** | Primary mic slot |
| Mic L Type | **Ribbon 121** (Type 4) | Warm mic; natural high-frequency roll-off |
| Position L | **0.48** | Off-center of the speaker cone for smooth response |
| Distance L | **0.25** | Close-mic'd with standard air |
| Room Send L | **−28.0 dB** | Minimal room send to keep the core sound dry and focused |
| Cab R | **BYPASSED** | Mono phase-coherence |

**EQ Section (Clean Machine 9-Band Graphic EQ)**

| Band | Setting | Purpose |
|------|---------|---------|
| EQ Status | **Active** | **The "Veil" — Surgical high-end roll-off** |
| 65 Hz | 0.0 dB | Neutral |
| 125 Hz | 0.0 dB | Neutral |
| 250 Hz | +2.0 dB | **Targeted bump**: Enhances neck pickup woody resonance |
| 500 Hz | +1.0 dB | Fills out lower midrange |
| 1 kHz | 0.0 dB | Neutral |
| 2 kHz | −2.0 dB | Smooths out remaining high pick click |
| 4 kHz | −6.0 dB | **High Cut**: Steeps the high-end roll-off |
| 8 kHz | −10.0 dB | **High Cut**: Mutes digital fizz |
| 16 kHz | −12.0 dB | **High Cut**: Mutes high-frequency air |
| HPF / LPF | **20 Hz / 3.8 kHz** | **Low-Pass Filter**: Sets the ceiling of the veil to 3.8 kHz |

**Post FX Section**

*Chorus and Delay are **BYPASSED**.*

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The Wash** | **Active** | **ON** | Integrated room reverb |
| | **Mix** | **8%** | Extremely subtle; provides physical air without a tail |
| | **Decay** | **20%** | Very short decay |
| | **Shimmer** | **OFF** | Bypassed |

---

## Starting Point Guide

- **Physical Tone Knob:** This is the most critical control in the chain. Start with your Telecaster's neck pickup active and the tone knob rolled back to **3**. If it sounds too muffled, move to **4**. If you want a deeper "veil," roll back to **2**.
- **Picking Technique:** Play with your bare thumb or the flesh of your fingers rather than a pick to get the warmest, roundest attack.
- **Adjusting the Resonance:** If the tone feels too "boxy," pull down the **250 Hz** slider on the Graphic EQ to **0.0 dB** or reduce the amp's **Middle** control to **50%**.

---

## Feedback History

### 2026-07-02 — initial
Created as the ACWX standalone counterpart to the Ed Bickert "Electronic Veil" single-coil preset. Configured with a dark-voiced Clean Machine, Ribbon 121 mic model, custom graphic EQ high-cuts with a 3.8 kHz Low-Pass filter, and subtle room reverb.
