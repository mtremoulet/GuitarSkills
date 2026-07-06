---
id: henriksen-bud-acwx
preset_name: "Henriksen Bud ACWX"
created: 2026-07-03
updated: 2026-07-03
guitar: "Epiphone Sheraton II (neck humbucker, flatwounds)"
target: 'Henriksen Bud 6 simulation using ACWX D.I. Funk Console and Logic Channel EQ — pristine solid-state headroom with flatwound warmth and 5-band graphic EQ matching.'
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
*   **The EQ Stage**: Routed to post-plugin **Logic Pro Channel EQ** configurations to match the exact center frequencies of the physical Henriksen 5-band graphic EQ (**80 Hz, 420 Hz, 1.6 kHz, 3.5 kHz, 7.28 kHz**).
*   **The Speaker Stage**: Modeled via the ACWX unlinked **Clean Machine Cabinet** running a Ribbon 121 microphone to capture the warm, acoustic-like, punchy response of the Henriksen's small cabinet design.

This setup is ideal for neck-position humbuckers (especially on hollow-body or semi-hollow body guitars) to produce a warm, woody jazz tone with exceptional clarity and transient speed.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Input mode set to **Mono** in Logic Pro).

---

### 2. Archetype Cory Wong X (ACWX) — D.I. Funk Console Preamp
The analog console channel strip is kept flat and linear, delegating all surgical tone-shaping to the downstream EQ stage.

| Control | Setting | Purpose |
|---------|---------|---------|
| **Selected Amp** | D.I. Funk Console | Selects the clean solid-state channel strip (preamp stage) |
| **Output Volume** | 50% | Set to unity gain for clean headroom |
| **Compressor (Comp)** | 0% (Bypassed) | Bypassed to maintain natural string dynamics |
| **Tube Saturation** | 0% (Bypassed) | Bypassed to keep the signal linear and free of distortion |
| **High Pass Filter** | 20 Hz (Open) | High-pass filter kept wide open |
| **Low Pass Filter** | 17.0 kHz (Open) | Low-pass filter kept wide open |
| **Lows (Preamp EQ)** | 0.0 (Flat) | Channel strip low EQ set to neutral |
| **Mids (Preamp EQ)** | 0.0 (Flat) | Channel strip mid EQ set to neutral |
| **Highs (Preamp EQ)** | 0.0 (Flat) | Channel strip high EQ set to neutral |
| **Console EQ Active** | Off (Bypassed) | Preamp graphic EQ bypassed (handled downstream) |

**Cabinet & Microphone Selection (Unlinked)**:
*   **Amp/Cab Link** | Off (Unlinked)
*   **Selected Cabinet** | Clean Machine Cabinet (Fender-style)
*   **Cabinet L (Active)** | Ribbon 121 (Type 4) — Position: **0.60** (off-axis), Distance: **0.25**
*   **Cabinet R (Active)** | Off (Bypassed)

---

### 3. Logic Pro Channel EQ — post-amp surgical shaping
Because the physical Henriksen Bud 6 uses 5 peaking bands, but a single Logic Channel EQ strip only has 4 peaking bands (with Band 2 and Band 7 hardwired as shelves), you can choose between two routing approaches:

#### Option A: The "Dual EQ" Surgical Chain (Recommended for strict accuracy)
Insert **two Channel EQ plugins back-to-back**. This bypasses the shelving bands entirely, using only the peaking bands (Bands 3–6) of both plugins to achieve five true peaking bands plus high/low cuts:

**EQ Plugin 1: Lows & Mids**
*   **Band 1 (HPF)**: On | **50 Hz** | 24 dB/Oct slope (Sub-bass safety cut)
*   **Band 3 (Peak)**: On | **80 Hz** | Gain: **0.0 dB** | Q: `1.0` (Bass Dial)
*   **Band 4 (Peak)**: On | **420 Hz** | Gain: **+2.0 dB** | Q: `1.2` (Low-Mid/Wood Dial)
*   **Band 5 (Peak)**: On | **1.6 kHz** | Gain: **0.0 dB** | Q: `1.2` (Mid/Definition Dial)

**EQ Plugin 2: Highs & Cabinet Roll-off**
*   **Band 3 (Peak)**: On | **3.5 kHz** | Gain: **-2.0 dB** | Q: `1.0` (High-Mid Dial)
*   **Band 4 (Peak)**: On | **7.28 kHz** | Gain: **-5.0 dB** | Q: `1.0` (Treble/Tweeter Dial)
*   **Band 8 (LPF)**: On | **5.5 kHz** | 12 dB/Oct slope (Cabinet roll-off/Tweeter Defeat)

#### Option B: The "Single EQ" Hybrid Chain (Compiled Preset Default)
A single Channel EQ plugin where the $80\text{ Hz}$ band is mapped to Band 2 (Low Shelf) and kept flat (0 dB). The remaining four bands are mapped to peaking bands:
*   **Band 1 (HPF)**: On | **50 Hz** | 24 dB/Oct slope (Sub-bass safety cut)
*   **Band 2 (Low Shelf)**: On | **80 Hz** | Gain: **0.0 dB** | Q: `1.0` (A shelving bass adjustment)
*   **Band 3 (Peak)**: On | **420 Hz** | Gain: **+2.0 dB** | Q: `1.2` (Low-Mid/Wood Dial)
*   **Band 4 (Peak)**: On | **1.6 kHz** | Gain: **0.0 dB** | Q: `1.2` (Mid/Definition Dial)
*   **Band 5 (Peak)**: On | **3.5 kHz** | Gain: **-2.0 dB** | Q: `1.0` (High-Mid Dial)
*   **Band 6 (Peak)**: On | **7.28 kHz** | Gain: **-5.0 dB** | Q: `1.0` (Treble/Tweeter Dial)
*   **Band 8 (LPF)**: On | **5.5 kHz** | 12 dB/Oct slope (Cabinet roll-off/Tweeter Defeat)

---

### 4. Logic Pro Reverb Bus — spatial ambience
Parallel send routed post-EQ to **Bus 3** to simulate the Bud 6's onboard digital reverb, keeping the dry signal front and center.

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

*   **Audient iD14 D.I. Calibration**: Set the **INPUT** gain slider at the top left of the ACWX plugin window to **-3.2 dB** to calibrate for your Audient iD14's JFET input.
*   **Tweeter Tone Shaping (Tweeter Defeat vs. Tweeter Active)**:
    *   **Tweeter Defeat (Warm, Classic Jazz)**: Keep the LPF (Band 8) active at **5.5 kHz** and set the Treble band (7.28 kHz) to **-5.0 dB**. This rolls off the high-end air, focusing the sound entirely on the warm, woody mid-range of the 6" speaker.
    *   **Tweeter Active (Modern Acoustic Sheen)**: Bypass the LPF (Band 8) entirely and set the Treble band (7.28 kHz) to **0.0 dB** (or boost slightly for acoustic fingerstyle). This allows high-frequency air to bloom naturally up to 20 kHz.
*   **How to Dial in Tone (Like the Physical Amp)**: Because the D.I. Funk Console is set completely flat, do not touch the amp settings to adjust your tone. To dial in the amplifier, adjust the **Gain** sliders of the 5 EQ bands in your Logic Channel EQ plugins. These act directly as the physical dials on the Henriksen:
    *   *Need more body?* Raise the **420 Hz** band.
    *   *Too boomy?* Lower the **80 Hz** band.
    *   *Too clicky or clunky?* Dip the **3.5 kHz** band.
*   **Reverb Routing Logic**: Routing your reverb via a parallel Logic Bus Send (post-EQ) is far more accurate than using ACWX's internal cabinet room send. The Room Send inside ACWX is situated before the Logic EQ, which means your reverb tail would get heavily filtered by the steep low-pass filter (LPF) and EQ cuts. A post-EQ bus send keeps the reverb tail lush, clear, and un-muffled.
*   **Guitar Controls**: Select the neck humbucker. Roll back the guitar volume to **8** and the tone knob to **7** to soften the pickup transients.

---

## Feedback History

### 2026-07-03 — initial
Toneprint created to model the Henriksen Bud 6 using the D.I. Funk Console in ACWX and post-plugin Logic Channel EQ. Configured as a fully linear, compression-free, high-headroom preset. Updated to include clean GUI control descriptors, Tweeter configuration guides, and the surgical Dual-EQ routing option.
