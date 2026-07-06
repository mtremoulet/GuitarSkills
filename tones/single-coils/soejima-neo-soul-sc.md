---
amp: "Dream '65 (UADx)"
created: 2026-06-21
guitar: "Fender Player II Telecaster / Squier Stratocaster"
id: soejima-neo-soul-sc
pickup_type: single-coil
preset_name: "Soejima Neo-Soul SC"
status: initial
tags: "neo-soul, clean, warm, compressed, chorus, delay, reverb, single-coil, dream-65"
target: 'Toshiki Soejima-style warm, compressed, and articulate neo-soul clean tone for single-coils using a Vemuram Jan Ray boost, Dream ''65, and LA-2A.'
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
    Bass: 5.0
    Bright: false
    Reverb: 0
    Treble: 4.5
    Volume: 2.8
  la2a:
    gain: 24
    peak_reduction: 35
    compress: true
  hitsville:
    mix: 1.0
    pre_delay: 10
    decay: 1.8
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 24.0}
    band4: {on: true, freq: 400.0, gain: -1.0, q: 1.0}
    band5: {on: true, freq: 1500.0, gain: 1.5, q: 0.8}
    band7: {on: true, freq: 5000.0, gain: -2.0}
---

# Soejima Neo-Soul Clean — Single-Coil

## Target Sound

This toneprint is designed to produce the warm, compressed, highly articulate "Neo-Soul / J-Pop / City Pop" clean tone signature of Toshiki Soejima, specifically calibrated for single-coil pickups (like the Fender Player II Telecaster or Squier Stratocaster). Single-coils have rapid, snappy pick transients and a natural mid-scoop that can sound cold or glassy in digital environments. 

To counteract this, the architecture uses an always-on **Vemuram Jan Ray** capture in TONEX to thicken the lower-mids and add subtle harmonic sweetness. The **UADx Dream '65** runs on the cleaner, high-headroom **JBF120** Twin Reverb cabinet, while a fast-reacting **UADx LA-2A Silver** compressor rounds off transient spikes into a smooth, percussive "pop." Subtle Dimension D chorus, tape echo, and chamber reverb are placed on parallel buses to create a lush, spacious halo around the dry signal.

**Physical Setup & Playing Tip:** Play in Strat Position 4 (bridge + middle) or Tele neck position. Roll the guitar volume knob to **8** to clean up the input and maximize touch sensitivity, and the tone knob to **7** (the "7/7 Baseline") to take the edge off the high frequencies.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).


### 2. IK Multimedia TONEX — pre-amp drive
*   **Status:** **ON**
*   **Capture**: `DPE JAN RAY - G1` (Vemuram Jan Ray - low gain)
*   **Role**: Always-on transparent saturation to add harmonic warmth and compression before the amplifier.




### 3. UADx Dream '65 Reverb Amp — clean foundation

*   **Status:** **ON**

#### Amp Settings

| Control | Setting | Purpose |
|---------|---------|---------|
| Bright / Normal | **Normal** | Keeps single-coils from getting ice-picky |
| Mod Circuit | **D-Tex** | Boost OFF. Selected for its richer midrange profile |
| Volume | 2.8 | Calibrated for single-coils; high-headroom clean with dynamic bloom |
| Treble | 4.5 | Pulled back slightly from noon to smooth the high end |
| Bass | 5.0 | Neutral baseline |
| Reverb | 0.0 | Off (reverb is handled on a dedicated parallel bus) |
| Cab | **JBF120** | 1968 Twin Reverb 2x12 cabinet for wide, clean fingerstyle projection |

---

#### Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 4. UADx LA-2A Silver Compressor — transient smoothing
*   **Status:** **ON**

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 35 | Fast optical compression to tame sharp single-coil pick attacks |
| Gain | 24 | Makeup gain to normalize level going into Logic |
| Mode | Compress | Smooth 3:1 optical compression |

---

### 5. Logic Channel EQ — corrective shaping
*   **Status:** **ON**

| Band | Type | Frequency | Gain / Slope | Q | Purpose |
|------|------|-----------|--------------|---|---------|
| Band 1 | HPF (Low Cut) | 80 Hz | 24 dB/oct | — | Cuts sub-bass rumble and interface hum |
| Band 4 | Peaking | 400 Hz | −1.0 dB | 1.0 | Subtle cleanup of lower-mid mud |
| Band 5 | Peaking | 1.5 kHz | +1.5 dB | 0.8 | Gentle midrange push to counteract Fender scoop and define chords |
| Band 7 | LPF (High Cut) | 5.0 kHz | 24 dB/oct | — | Smooths out harsh digital "air" and fizz |

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
*   **Setting**: Head Select: Position 1 (single head), Echo Rate: synced to host (e.g. 1/8 note), Feedback: 15% (1–2 repeats), Tape Age: New, Wet Solo: ON, Mix: 100% Wet.
*   **Send Level**: −18 dB
*   **Purpose**: Warm tape slapback repeats that sit neatly behind the dry signal.

#### Bus 3: Reverb — UADx Hitsville Reverb Chambers
*   **Status**: **ON**
*   **Setting**: Chamber: 2648 (Chamber 1), Speaker: Bozak 800, Mic: Unidyne 545, Decay: 9:00 (short/tight), Pre-Delay: 10 ms, Wet Solo: ON.
*   **Send Level**: −16 dB
*   **Purpose**: Creates an intimate, polished room ambience.

---

## Starting Point Guide

*   **Stratocaster Adjustments:** If using a Stratocaster and the tone feels slightly too dark, flip the Dream '65 to **Bright** and raise **Treble** to 5.0. 
*   **Dialing the Compression:** If you play with a very heavy touch and the compressor feels like it's pumping, roll the LA-2A **Peak Reduction** down to 30.

---

## Feedback History

### 2026-06-21 — initial
Proposed toneprint calibrated for single-coil pickups, featuring an always-on Vemuram Jan Ray TONEX capture, UADx Dream '65 (JBF120 cab), LA-2A Silver compression, and bus-routed chorus, delay, and reverb.
