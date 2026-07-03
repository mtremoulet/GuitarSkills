---
id: cory-wong-lofi-vinyl
preset_name: "Lofi Vinyl"
created: 2026-06-23
updated: 2026-06-23
guitar: "Gibson Les Paul Studio (490R neck / 498T bridge humbuckers)"
target: "Bandpass-filtered lo-fi clean tone resembling a sampled vinyl record, using active chorus and slapback delay for neo-soul chord loops."
tags: "clean, lo-fi, chillhop, delay, eq, humbucker, les-paul"
tone-king-channel: bypassed
amp: "D.I. Funk Console (Archetype Cory Wong X)"
status: initial
pickup_type: humbucker
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: true
    selectedAmp: 0
    selectedCab: 0
    compressorActive: true
    compressorVolume: 55.0
    compressorCompression: 25.0
    compressorTone: 50.0
    compressorBlend: 30.0
    tuberActive: false
    bigRigActive: false
    postalActive: false
    funkVolume: 45.0
    funkTubeSat: 25.0
    funkComp: 20.0
    funkHighPass: 52.0
    funkLowPass: 10500.0
    funkLows: 0.0
    funkMids: 0.0
    funkHighs: 0.0
    funkEQActive: true
    funkEQBand1: -12.0
    funkEQBand2: -8.0
    funkEQBand3: 0.0
    funkEQBand4: 1.0
    funkEQBand5: 2.0
    funkEQBand6: 1.0
    funkEQBand7: -2.0
    funkEQBand8: -8.0
    funkEQBand9: -12.0
    funkEQHpf: 150.0
    funkEQLpf: 4000.0
    chorusActive: true
    chorusMix: 15.0
    chorusWidth: 30.0
    chorusRate: 15.0
    delayActive: true
    delayMix: 20.0
    delayFeedback: 15.0
    delayTimeL: 200.0
    delayTimeR: 200.0
    washActive: false
---

# Lofi Vinyl — Sampled Chillhop Clean

## Target Sound

This toneprint is designed for lo-fi beats, chillhop, and neo-soul chord looping. It mimics the restricted frequency range and slight warble of a sampled vintage vinyl record. 

By applying an aggressive bandpass filter curve on **The D.I. Funk Console's Graphic EQ** (rolling off everything below 150 Hz and above 4 kHz), we strip out the modern hi-fi bass and treble. We then pair it with a light chorus (to simulate vinyl pitch warble/wow-and-flutter) and a short 200ms slapback delay to add spatial depth.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed** (direct direct-in is used to capture the raw humbucker character for digital filtering).

---

### 2. Archetype Cory Wong X — Lo-Fi Filter Rig

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 4th Position Compressor** | **Active** | **ON** | Subtle parallel compression |
| | **Blend** | **30%** | Keeps the touch dynamics natural |
| | **Tone** | **50%** | Neutral |
| | **Compression** | **25%** | Light dynamic smoothing |
| | **Volume** | **55%** | Gain matching |

*All other Pre FX are **BYPASSED**.*

**Amp Section — "The D.I. Funk Console"**

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **D.I. Funk Console** | Analog channel strip |
| Volume (Gain) | **45%** | Keeps the preamp clean with the hotter humbuckers |
| Tube Saturation | **25%** | Adds subtle analog harmonic warmth |
| Compression | **20%** | Light power amp squash |
| High Pass / Low Pass | **Default** | 52 Hz HPF / 10.5 kHz LPF |
| Low / Mid / High | **0.0 dB** | Kept flat |

**Cab Section (Linked)**

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **On** | Matches cabinet to D.I. Funk Console |

**EQ Section (D.I. Funk Console 9-Band Graphic EQ)**

We use the EQ to establish a radio/vinyl bandpass filter:
*   **65 Hz:** `−12.0 dB` (Maximum cut to remove sub-bass rumble)
*   **125 Hz:** `−8.0 dB` (Cuts low-end mud)
*   **250 Hz:** `0.0 dB` (Neutral)
*   **500 Hz:** `+1.0 dB` (Slight boost to woody midrange)
*   **1 kHz:** `+2.0 dB` (Vocal focus boost)
*   **2 kHz:** `+1.0 dB` (Presence boost)
*   **4 kHz:** `−2.0 dB` (Softens high-end transient edge)
*   **8 kHz:** `−8.0 dB` (Heavy roll-off of high chime)
*   **16 kHz:** `−12.0 dB` (Maximum cut to remove modern air/fizz)
*   **HPF / LPF:** `150 Hz` High-Pass / `4.0 kHz` Low-Pass

**Post FX Section**

| Device | Control | Setting | Purpose |
|--------|---------|---------|---------|
| **Chorus** | **Active** | **ON** | Simulates vinyl pitch wow-and-flutter |
| | **Mix** | **15%** | Low mix keeps it subtle |
| | **Width** | **30%** | Narrower spread for a vintage focus |
| | **Rate** | **15%** | Slow warble |
| **Delay** | **Active** | **ON** | Slapback delay |
| | **Mix** | **20%** | Low mix sits behind the note |
| | **Feedback** | **15%** | 1 to 2 repeats max |
| | **Time L / R** | **200 ms** | Short slapback delay time |

---

## Starting Point Guide

- **Guitar Pickups:** The **Middle position** (both humbuckers combined) is excellent for this tone, but the **Neck pickup** rolled back to **8** volume gives an incredibly warm, round, lo-fi jazz-box vibe.
- **Adjusting the Lo-Fi filter:** If the tone feels *too* thin or restricted, bypass the **Graphic EQ** block. This restores the full bandwidth of the D.I. Funk Console while keeping the delay/chorus effects active.
