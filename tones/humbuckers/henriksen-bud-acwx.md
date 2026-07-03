---
id: henriksen-bud-acwx
preset_name: "Henriksen Bud ACWX"
created: 2026-07-03
updated: 2026-07-03
guitar: "Epiphone Sheraton II (neck humbucker, flatwounds)"
target: "Henriksen Bud 6 simulation using ACWX D.I. Funk Console and Logic Channel EQ — pristine solid-state headroom with flatwound warmth and 5-band graphic EQ matching."
tags: "clean, warm, humbucker, flatwounds, jazz, neural-dsp, cory-wong, henriksen"
tone-king-channel: bypassed
amp: "D.I. Funk Console (Archetype Cory Wong X)"
status: initial
pickup_type: humbucker
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: false
    selectedAmp: 0
    selectedCab: 1
    leftCabActive: true
    leftCab0MicType: 4
    leftCabDistance: 0.25
    leftCabPosition: 0.60
    rightCabActive: false
    compressorActive: false
    tuberActive: false
    bigRigActive: false
    postalActive: false
    chorusActive: false
    delayActive: false
    washActive: false
    funkVolume: 50.0
    funkTubeSat: 0.0
    funkComp: 0.0
    funkHighPass: 20.0
    funkLowPass: 17000.0
    funkLows: 0.0
    funkMids: 0.0
    funkHighs: 0.0
    funkEQActive: false
  logic_eq:
    band1: {on: true, freq: 50.0, slope: 24.0}
    band2: {on: true, freq: 80.0, gain: 0.0, q: 1.0}
    band3: {on: true, freq: 420.0, gain: 2.0, q: 1.2}
    band4: {on: true, freq: 1600.0, gain: 0.0, q: 1.2}
    band5: {on: true, freq: 3500.0, gain: -2.0, q: 1.0}
    band6: {on: true, freq: 7280.0, gain: -5.0, q: 1.0}
    band8: {on: true, freq: 5500.0, slope: 12.0}
---

# Henriksen Bud 6 — D.I. Funk Console (ACWX)

## Target Sound

This toneprint replicates the clean, warm, linear, and high-fidelity signature of the solid-state **Henriksen Bud 6** (and Blu 6) amplifier. 

To achieve this, the signal path is kept entirely linear and high-headroom, bypassing all forms of tube preamp coloration, power-amp sag, compression, and saturation. 
*   **The Preamp Stage**: Modeled via the **D.I. Funk Console** in Archetype Cory Wong X, acting as a clean solid-state analog channel strip.
*   **The EQ Stage**: Routed to a post-plugin **Logic Pro Channel EQ** configured to match the exact center frequencies of the physical Henriksen 5-band graphic EQ (**80 Hz, 420 Hz, 1.6 kHz, 3.5 kHz, 7.28 kHz**).
*   **The Speaker Stage**: Modeled via the ACWX unlinked **Clean Machine Cabinet** running a Ribbon 121 microphone to capture the warm, acoustic-like, punchy response of the Henriksen's small cabinet design.

This setup is ideal for neck-position humbuckers (especially on hollow-body or semi-hollow body guitars) to produce a warm, woody jazz tone with exceptional clarity and transient speed.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Input mode set to **Mono** in Logic Pro).

---

### 2. Archetype Cory Wong X (ACWX) — D.I. Funk Console Preamp
The analog console channel strip is kept flat and linear, delegating all surgical tone-shaping to the Logic Channel EQ.

| Control | Setting | Purpose |
|---------|---------|---------|
| Latch Switch | Bypassed | Pre FX compressor and drives are turned OFF |
| selectedAmp | 0 (D.I. Funk Console) | Selects the clean solid-state channel strip |
| funkVolume | 50.0 | Set to unity gain for maximum clean headroom |
| funkComp | 0.0 | Bypassed (no compression to maintain pure dynamics) |
| funkTubeSat | 0.0 | Bypassed (no harmonic distortion) |
| funkHighPass | 20 Hz | Set fully open (handled downstream) |
| funkLowPass | 17.0 kHz | Set fully open (handled downstream) |
| funkLows | 0.0 (Flat) | Console EQ lows set to neutral |
| funkMids | 0.0 (Flat) | Console EQ mids set to neutral |
| funkHighs | 0.0 (Flat) | Console EQ highs set to neutral |
| funkEQActive | Bypassed (Off) | ACWX Graphic EQ turned off (handled by Logic EQ) |

**Cabinet & Microphone Selection (Unlinked)**:
*   **ampCabLinkedState**: False (Unlinked)
*   **selectedCab**: 1 (Clean Machine Cabinet)
*   **leftCabActive**: True
*   **leftCab0MicType**: 4 (Ribbon 121)
*   **leftCabDistance**: 0.25 (Slight room distance for air)
*   **leftCabPosition**: 0.60 (Off-axis to roll off harsh high-end sizzle)
*   **rightCabActive**: False

---

### 3. Logic Pro Channel EQ — post-amp surgical shaping
Placed immediately after ACWX to act as the Bud 6's physical 5-band EQ and cabinet roll-off.

| Band | Type | Frequency | Gain | Q-Factor | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Band 1** | High Cut (HPF) | **50 Hz** | *n/a* | 24 dB/Oct slope | **Sub-bass safety cut**; removes sub-low mud and room rumble. |
| **Band 2** | Peaking | **80 Hz** | **0.0 dB** | `1.0` | **Bass**; set to 0.0 dB (flat). Adjust to taste for low-end body. |
| **Band 3** | Peaking | **420 Hz** | **+2.0 dB** | `1.2` | **Low-Mid (The "Wood")**; boosts woody archtop resonance. |
| **Band 4** | Peaking | **1.6 kHz** | **0.0 dB** | `1.2` | **Mid**; set to 0.0 dB (flat). Boost for note articulation. |
| **Band 5** | Peaking | **3.5 kHz** | **-2.0 dB** | `1.0` | **High-Mid**; softens pick attack and harsh solid-state click. |
| **Band 6** | Peaking | **7.28 kHz** | **-5.0 dB** | `1.0` | **Treble (The "Tweeter")**; simulates **Tweeter Defeat** mode. |
| **Band 8** | Low Cut (LPF) | **5.5 kHz** | *n/a* | 12 dB/Oct slope | **Cabinet Roll-off**; rolls off digital air for warm jazz warmth. |

---

### 4. Logic Pro Reverb Bus — spatial ambience
Parallel send routed to **Bus 3** to simulate the Bud 6's onboard digital reverb, keeping the dry signal front and center.

| Control | Setting | Purpose |
|---------|---------|---------|
| Plugin | Logic ChromaVerb or Space Designer | Set to a warm, transparent Room or Plate |
| Mix | Wet Solo (100% Wet) | Parallel routing |
| Decay | 1.4s | Simulates a small, woody acoustic room |
| Pre-Delay | 15 ms | Separates dry pick attack from the room reflections |

*Logic Fader Blend:*
*   *Reverb Bus Send:* `-15 dB` (starting point)
*   *Reverb Bus Fader:* `-6 dB`

---

## Dial-in Workflow & Tips

*   **Audient iD14 D.I. Calibration**: To correct for the iD14's hotter JFET input (+9.0 dBu clipping point vs. the +12.2 dBu standard modeled by Neural DSP), set the **INPUT** gain knob at the top left of the ACWX plugin window to **-3.2 dB**.
*   **Tweeter Active Mode (Acoustic Sheen)**: If you are playing fingerstyle or want a modern, acoustic-like hi-fi response, bypass the LPF (**Band 8**) on the Logic Channel EQ and set the Treble band (**Band 6**) to **0.0 dB**.
*   **Guitar Controls**: Select the neck humbucker. Roll back the guitar volume to **8** and the tone knob to **7**. This rolls off the raw pickup edge, allowing the simulated cabinet and EQ curve to shape the acoustic-like jazz character naturally.

---

## Feedback History

### 2026-07-03 — initial
Toneprint created to model the Henriksen Bud 6 using the D.I. Funk Console in ACWX and post-plugin Logic Channel EQ. Configured as a fully linear, compression-free, high-headroom preset.
