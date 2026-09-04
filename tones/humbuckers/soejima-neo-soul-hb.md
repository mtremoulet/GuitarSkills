---
amp: "Dream '65 (UADx)"
created: 2026-06-21
guitar: "Epiphone Sheraton II / Gibson Les Paul Studio"
id: soejima-neo-soul-hb
pickup_type: humbucker
preset_name: "Soejima Neo-Soul HB"
status: initial
tags: "neo-soul, clean, warm, compressed, chorus, delay, reverb, humbucker, dream-65"
target: 'Toshiki Soejima-style warm, articulate neo-soul clean tone for humbuckers using a low-gain Vemuram Jan Ray boost, Dream ''65, and LA-2A.'
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
    Bass: 4.0
    Bright: false
    Reverb: 0
    Treble: 5.5
    Volume: 2.2
  la2a:
    gain: 20
    peak_reduction: 20
    compress: true
  hitsville:
    mix: 0.12
    pre_delay: 12
    decay: 1.8

    wet_solo: false
  logic_eq:
    band1: {on: true, freq: 90.0, slope: 24.0}
    band4: {on: true, freq: 350.0, gain: -2.0, q: 1.2}
    band7: {on: true, freq: 4000.0, gain: 1.5, q: 1.0}
---

# Soejima Neo-Soul Clean — Humbucker

## Target Sound

This toneprint is designed to produce the warm, compressed, highly articulate "Neo-Soul / J-Pop / City Pop" clean tone signature of Toshiki Soejima, specifically calibrated for dual-humbucker guitars (like the Epiphone Sheraton II or Gibson Les Paul Studio). Humbuckers naturally output a warmer, thicker, mid-heavy signal with slower transients. In a neo-soul context, humbuckers risk sounding boxy, muddy, or pushing clean amps into clipping.

To address this, the architecture uses a low-gain **Vemuram Jan Ray** capture in TONEX to add tube-like dynamic feel without distortion. The **UADx Dream '65**'s volume is backed down to **2.2** to preserve clean headroom, and the bright, articulate **JBF120** Twin Reverb cabinet is loaded. The **UADx LA-2A Silver** is set to light compression (Peak Reduction 20) to keep the humbuckers from sounding squeezed and flat, while Logic EQ cleans up the low-mid "wooliness" and boosts high-end definition to make neck-pickup arpeggios chime.

**Physical Setup & Playing Tip:** Select the neck pickup (or middle neck/bridge position for a woodier, funkier bounce). Roll the guitar volume knob to **7 or 8** to maximize touch sensitivity and headroom. Keep the tone knob around **8** to preserve high-end clarity.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).


### 2. IK Multimedia TONEX — pre-amp drive
*   **Status:** **ON**
*   **Capture**: `DPE JAN RAY - G1` (Vemuram Jan Ray - low gain)
*   **Role**: Always-on transparent boost, kept low to prevent humbuckers from clipping the amp.




### 3. UADx Dream '65 Reverb Amp — clean foundation

*   **Status:** **ON**

#### Amp Settings

| Control | Setting | Purpose |
|---------|---------|---------|
| Bright / Normal | **Normal** | Keeps the top-end organic |
| Mod Circuit | **Stock** | Boost OFF. Highest clean headroom setting to prevent clipping |
| Volume | 2.2 | Calibrated for humbuckers; maximizes clean headroom |
| Treble | 5.5 | Pushed slightly to add bite and chime to humbucker neck pickups |
| Bass | 4.0 | Rolled back to keep the low end tight and clean |
| Reverb | 0.0 | Off (reverb is handled on a dedicated parallel bus) |
| Cab | **JBF120** | 1968 Twin Reverb 2x12 cabinet for bright, pristine note definition |

---

#### Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 4. UADx LA-2A Silver Compressor — dynamic leveling
*   **Status:** **ON**

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 20 | Light compression to preserve humbucker dynamic range and prevent mud |
| Gain | 20 | Makeup gain to normalize level going into Logic |
| Mode | Compress | Smooth 3:1 optical compression |

---

### 5. Logic Channel EQ — corrective shaping
*   **Status:** **ON**

| Band | Type | Frequency | Gain / Slope | Q | Purpose |
|------|------|-----------|--------------|---|---------|
| Band 1 | HPF (Low Cut) | 90 Hz | 24 dB/oct | — | Cuts sub-bass mud and interface hum |
| Band 4 | Peaking | 350 Hz | −2.0 dB | 1.2 | Clears out the boxy "wooliness" of neck humbuckers |
| Band 7 | Peaking | 4.0 kHz | +1.5 dB | 1.0 | Restores pick attack and high-end string definition |

---

### 6. Parallel Bus Processing — time & space
Effects are routed via auxiliary channels to preserve the dry signal's punch and clarity.

#### Bus 5: Chorus — UADx Studio D Chorus
*   **Status**: **ON**
*   **Setting**: Push Button 1 (Dimension D mode)
*   **Send Level**: −22 dB (slightly lower return to keep the thicker humbucker tone focused)
*   **Purpose**: Subtle, wide spatial modulation that thickens the sound without warbling.

#### Bus 4: Delay — UADx Galaxy Tape Echo
*   **Status**: **ON**
*   **Setting**: Head Select: Position 1 (single head), Echo Rate: synced to host, Feedback: 12% (1 short repeat), Tape Age: New, Wet Solo: ON, Mix: 100% Wet.
*   **Send Level**: −20 dB
*   **Purpose**: Clean tape slapback to add body without muddying the decay.

#### Bus 3: Reverb — UADx Hitsville Reverb Chambers
*   **Status**: **ON**
*   **Setting**: Chamber: 2648 (Chamber 1), Speaker: Bozak 800, Mic: Unidyne 545, Decay: 9:00 (short/tight), Pre-Delay: 12 ms (slightly longer to separate humbucker attack), Wet Solo: ON.
*   **Send Level**: −15 dB
*   **Purpose**: Creates an intimate, polished room ambience.

---

## Starting Point Guide- **Neck + Bridge Blend:** For a snappier, more percussive funk-soul tone, select both humbuckers and roll the bridge volume back to 8 and the neck volume to 7.
- **High-End Sparkle:** If the neck humbucker still feels too dark, raise the Dream '65 **Treble** control to 6.0 or enable the **Bright** switch on the amp.

---

## Feedback History

### 2026-06-21 — initial
Proposed toneprint calibrated for humbucker pickups, featuring a low-volume UADx Dream '65 setting, light LA-2A Silver compression, low-mid EQ cuts, and parallel bus effects.
