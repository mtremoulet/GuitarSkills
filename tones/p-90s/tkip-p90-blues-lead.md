---
id: tkip-p90-blues-lead
preset_name: "TKIP P-90 Blues Lead"
created: 2026-06-06
updated: 2026-06-06
guitar: "Framus Earl Slick Artist Series"
target: 'A warm, dynamic, responsive blues lead tone with tweed-like edge of breakup.'
tags: "blues, lead, p-90, dynamic, crunch, warm"
tone-king-channel: lead
amp: "Tone King Imperial Preamp (Hardware)"
status: initial
pickup_type: p-90
preset_data:
  amp_platform: hardware
  amp_settings:
    Channel: Lead
    Volume: 3.0
    Attenuation: 7.0
    Tone: 2.5
    Mid-Bite: 2.0
    Reverb: Off
    Tremolo: Off
    IR: Active (Imperial 1x12 TK1660)
  la2a:
    peak_reduction: 35.0
    gain: 40.0
    compress: true
  hitsville:
    mix: 0.12
    pre_delay: 20.0
    decay: 1.8
    wet_solo: false
  galaxy:
    head_select: 1
    echo_rate: 8.0
    feedback: 1.0
    echo_volume: 2.5
    wet_solo: true
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 12.0}
    band3: {on: true, freq: 250.0, gain: 1.5, q: 1.0}
    band7: {on: true, freq: 7000.0, gain: -2.0}
---

# TKIP P-90 Blues Lead

## Target Sound
A touch-sensitive, highly dynamic blues lead tone built for DiMarzio P-90 single-coils. The hardware Tone King Lead channel is dialed into its lower-gain tweed zone (Volume 3.0, Mid-Bite 2.0, Tone 2.5), producing a clean foundation that transitions smoothly into organic power-amp-style crunch when you dig in. Post-amp compression from the UADx LA-2A Silver smooths the picking dynamics, while a subtle slapback delay and warm Hitsville chamber reverb add space and depth.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
The physical front-end provides the core tube preamp character and speaker emulation.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Lead | Tweed character, mid-forward and responsive |
| Volume | 3.0 | Low preamp volume to keep the base tone clean/edge of breakup |
| Attenuation | 7.0 | Pushes the power-amp emulation stage for dynamic warmth |
| Tone | 2.5 | Rolled back to round off the inherent bright spank of P-90s |
| Mid-Bite | 2.0 | Adds a touch of midrange punch and compression without going into rock crunch |
| Reverb | Off | Handled in Logic sends |
| Tremolo | Off | Disabled |
| IR | Active (Imperial 1x12 TK1660) | High-fidelity, close-mic'd speaker character |

### 2. Logic Channel EQ — corrective sculpting
Placed first in the DAW track to clean up sub-lows and shape the P-90 body before compression.

| Control | Setting | Purpose |
|---------|---------|---------|
| Band 1 (High Pass) | On — 80.0 Hz, 12 dB/oct | Cleans up low-end cabinet rumble |
| Band 3 (Peak) | On — 250.0 Hz, +1.5 dB, Q: 1.0 | Fills out the lower-mid body of the P-90 |
| Band 7 (High Shelf) | On — 7.0 kHz, −2.0 dB | Softens the extreme high-end pick click |

### 3. UADx LA-2A Silver Compressor — post-amp dynamic smoothing
Placed inline on the track to glue notes together and add tube warmth.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 35.0 | Light optical compression (2–3 dB gain reduction on peaks) |
| Gain | 40.0 | Makeup gain |
| Compress/Limit | Compress | Soft 3:1 ratio |
| Emphasis / HF | Fully Clockwise (default) | Equal frequency sensitivity |

### 4. Galaxy Tape Echo (Bus 4 Send) — slapback delay
Set on Bus 4 at **100% Wet** (Wet Solo ON) to keep the dry signal centered.

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −18.0 dB | Sits subtly behind the dry signal |
| Head Select | 1 | Short slapback delay range |
| Echo Rate | 8.0 | Slapback tempo (approx. 120ms) |
| Feedback | 1.0 | Single clean repeat |
| Echo Volume | 2.5 | Blended low |
| Tape Age | New | Clear articulation |

### 5. Hitsville Reverb Chambers (Bus 3 Send) — room chamber
Set on Bus 3 at **100% Wet** (Wet Solo ON).

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −15.0 dB | Natural room bloom |
| Chamber | Chamber 1 | Small, warm acoustic space |
| Mix | 1.0 (100% Wet) | Aux bus blend |
| Decay | 1.8 seconds | Moderate, smooth tail |
| Pre-Delay | 20 ms | Separates dry note attack from reverb bloom |

---

## Starting Point Guide
- **First adjustment:** Guitar Volume knob. Set the guitar volume to **7** to get a dynamic edge-of-breakup clean; roll to **10** for full-throated blues lead crunch.
- **Key interaction:** The Mid-Bite control on the Lead channel is highly interactive. If the P-90 mids feel too aggressive, pull Mid-Bite down to **1.5**; if you want more Texas-style grind, push it up to **3.0**.
- **Variations:** Swap the built-in cabinet IR to **Marshall 4x12 (OH 412 Basketweave M25)** on the TKIP pedal to add heavy girth and authority for a broader blues-rock tone.

---

## Feedback History

### 2026-06-06 — initial
Designed as a dedicated blues-y lead tone for the Framus Earl Slick (DiMarzio P-90s). Utilizes the physical TKIP Lead channel dialed into a dynamic tweed zone (Volume 3.0, Attenuation 7.0, Mid-Bite 2.0). Post-FX includes LA-2A Silver for dynamic smoothing, a short slapback tape delay on Bus 4, and Hitsville Chamber 1 on Bus 3.
