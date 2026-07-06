---
amp: "Dream '65 (UADx)"
created: 2026-06-21
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s)"
id: soejima-neo-soul-p90
pickup_type: p-90
preset_name: "Soejima Neo-Soul P90"
status: initial
tags: "neo-soul, clean, warm, compressed, chorus, delay, reverb, p-90, dream-65"
target: 'Toshiki Soejima-style warm, articulate neo-soul clean tone for P-90 pickups. Matches his primary tone profile, combining a Vemuram Jan Ray boost, clean Dream ''65, and moderate LA-2A Silver compression.'
tone-king-channel: bypassed
updated: 2026-06-28
preset_data:
  amp_platform: uad_paradise
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  amp_settings:
    Bass: 4.5
    Bright: false
    Reverb: 0
    Treble: 5.0
    Volume: 2.5
  la2a:
    gain: 22
    peak_reduction: 28
    compress: true
  hitsville:
    mix: 1.0
    pre_delay: 10
    decay: 2.0
  logic_eq:
    band1: {on: true, freq: 85.0, slope: 24.0}
    band4: {on: true, freq: 500.0, gain: -1.5, q: 1.5}
    band7: {on: true, freq: 6000.0, gain: -1.0}
---

# Soejima Neo-Soul Clean — P-90

## Target Sound

This toneprint is designed to produce the warm, compressed, highly articulate "Neo-Soul / J-Pop / City Pop" clean tone signature of Toshiki Soejima, specifically calibrated for P-90 pickups (like your Framus Earl Slick Artist Series). P-90s are Soejima's favorite pickup type (he plays them on his Bruno Guitars TN-295). They combine the transient snap and chime of single-coils with the warmth, output, and mid-range growl of humbuckers.

The P-90 hits the front-end of the transparent **Vemuram Jan Ray** capture in TONEX and the **UADx Dream '65** (Volume at 2.5) with exceptional touch-sensitivity. We select the **Boutique D65** (Two-Rock 2x12) cabinet to provide woody midrange warmth and smooth out any upper treble harshness. Moderate **UADx LA-2A Silver** compression (Peak Reduction 28) preserves the snappy "thump" of the P-90 pick attack while sustaining chord voices. A subtle mid-cut in the Logic EQ cleans up boxy nasal frequencies, keeping complex chord voicings transparent.

**Physical Setup & Playing Tip:** Play in the middle position (both P-90s) or neck position. Roll the guitar volume knob to **8** to clean up the input and maximize touch sensitivity. The neck P-90 is woody and vocal; the middle position is bouncey and clear.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).


### 2. IK Multimedia TONEX — pre-amp drive
*   **Status:** **ON**
*   **Capture**: `DPE JAN RAY - G1` (Vemuram Jan Ray - low gain)
*   **Role**: Always-on transparent boost that highlights the woody organic growl of P-90s under a hard pick attack.




### 3. UADx Dream '65 Reverb Amp — clean foundation

*   **Status:** **ON**

#### Amp Settings

| Control | Setting | Purpose |
|---------|---------|---------|
| Bright / Normal | **Normal** | Keeps P-90s warm and organic |
| Mod Circuit | **D-Tex** | Boost OFF. Selected for its mid-range bloom and dynamic touch |
| Volume | 2.5 | Calibrated for P-90 output; provides a highly dynamic, touch-sensitive edge |
| Treble | 5.0 | Neutral setting; lets the P-90's natural chime cut through |
| Bass | 4.5 | Slightly pulled back to prevent the thicker P-90 body from muddying |
| Reverb | 0.0 | Off (reverb is handled on a dedicated parallel bus) |
| Cab | **Boutique D65** | Two-Rock 2x12 cabinet with G12-65s for woody midrange and smooth HF roll-off |

---

#### Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 4. UADx LA-2A Silver Compressor — transient control
*   **Status:** **ON**

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 28 | Moderate compression to balance snappy attack with humbucker-like sustain |
| Gain | 22 | Makeup gain to normalize level going into Logic |
| Mode | Compress | Smooth 3:1 optical compression |

---

### 5. Logic Channel EQ — corrective shaping
*   **Status:** **ON**

| Band | Type | Frequency | Gain / Slope | Q | Purpose |
|------|------|-----------|--------------|---|---------|
| Band 1 | HPF (Low Cut) | 85 Hz | 24 dB/oct | — | Cuts sub-bass rumble and interface hum |
| Band 4 | Peaking | 500 Hz | −1.5 dB | 1.5 | Removes the slight boxy/nasal midrange hump of P-90s |
| Band 7 | LPF (High Cut) | 6.0 kHz | 24 dB/oct | — | Gently smooths out the top-end air for a warmer finish |

---

### 6. Parallel Bus Processing — time & space
Effects are routed via auxiliary channels to preserve the dry signal's punch and clarity.

#### Bus 5: Chorus — UADx Studio D Chorus
*   **Status**: **ON**
*   **Setting**: Push Button 1 (Dimension D mode)
*   **Send Level**: −20 dB
*   **Purpose**: Subtle, wide spatial modulation that thickens the sound without warbling.

#### Bus 4: Delay — UADx Galaxy Tape Echo
*   **Status**: **ON**
*   **Setting**: Head Select: Position 1 (single head), Echo Rate: synced to host, Feedback: 15% (1–2 repeats), Tape Age: Used (adds subtle wow/flutter for organic vintage vibe), Wet Solo: ON, Mix: 100% Wet.
*   **Send Level**: −18 dB
*   **Purpose**: Warm tape slapback repeats that sit neatly behind the dry signal.

#### Bus 3: Reverb — UADx Hitsville Reverb Chambers
*   **Status**: **ON**
*   **Setting**: Chamber: 2648 (Chamber 1), Speaker: Bozak 800, Mic: Unidyne 545, Decay: 9:30 (slightly longer room decay), Pre-Delay: 10 ms, Wet Solo: ON.
*   **Send Level**: −16 dB
*   **Purpose**: Creates an intimate, polished room ambience.

---

## Starting Point Guide

*   **Neck Growl:** If you want a bit more bite when playing leads on the neck P-90, select the neck pickup, raise the Dream '65 **Volume** to 3.0, and dig in with your picking hand.
*   **Modulation Vibe:** Swap the Studio D Chorus on Bus 5 for a subtle **Logic Tremolo** (sine wave, slow rate, low depth) to get a beautiful liquid movement behind your arpeggios.

---

## Feedback History

### 2026-06-21 — initial
Proposed toneprint calibrated for P-90 pickups, featuring a dynamic UADx Dream '65 setting, Two-Rock 2x12 cabinet emulation, moderate LA-2A Silver compression, and corrective EQ.
