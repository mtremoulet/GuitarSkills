---
amp: "Dream '65 (UADx)"
created: 2026-06-10
guitar: "Universal (Tested with Archtop/Humbucker jazz guitars and Single-Coils)"
id: dream-65-warm-clean
pickup_type: universal
preset_name: "Dream 65 Warm Clean"
status: initial
tags: "blackface, clean, warm, jazz, dream-65, ev12, universal"
target: 'Warm, high-headroom clean tone with rolled-off treble and the linear, neutral EV12 cabinet'
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
    Volume: 2.5
    Reverb: 0.0
    Output: 7.5
    Bass: 5.0
    Treble: 3.0
    Boost: 0.0
    Speaker: "EV12 (Red LED / Down)"
    Mod: "Stock"
    AltMode: false
  la2a:
    gain: 20
    peak_reduction: 40
---

# Dream '65 — Warm Clean

## Target Sound

The **Dream '65 Warm Clean** is a linear, high-headroom, warm clean platform designed for jazz, fingerstyle, and clean comparison work. It is inspired by settings used to compare the UAFX Dream '65 pedal directly to solid-state jazz amplification (like a Henriksen).

Unlike the classic scooped, sparkly Fender Blackface sound, this preset configures the Dream '65 to be as flat and neutral as possible. It is highly responsive to the guitar's natural tone, absorbing harsh transients and delivering a thick, warm, woody voice.

### Key Settings & Design Decisions
*   **Maximum Headroom (Volume 10:00 / ~2.5, Boost 7:00 / Off):** Preserves the pure clean signal of the preamp. Any breakup or compression is avoided.
*   **The Treble Roll-Off (Treble 10:00 / ~3.0):** Pulls back the typical Deluxe Reverb high-end "chime" and "glassiness." This rounds off the top end of the notes, giving single-coils a warm warmth and humbuckers/archtops a deep, smoky jazz voice.
*   **Flat Low-End (Bass 11:30-12:00 / ~4.5-5.0):** Maintains a solid, supportive bass response without pushing the amp into boomy or flubby territory.
*   **The EV12 Cabinet (Speaker Switch DOWN / Red LED):** The Electro-Voice EVM12L speaker emulation is the backbone of this tone. It provides massive clean headroom, tight and deep bass response, and a very flat, uncolored frequency curve that prevents the typical speaker breakup or mid-scoop of standard Fender cabinets.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom).


### 2. UADx Dream '65 Reverb Amp — character source

#### Amp Settings
| Control | Clock Setting | Value (0-10) | Purpose |
|---------|---------------|--------------|---------|
| **Volume** | 10:00 | 2.5 | Kept low for maximum clean preamp headroom |
| **Reverb** | 7:00 | 0.0 | Turned off for direct dry comparison (add external reverb as desired) |
| **Output** | 2:30 | 7.5 | Pushed past noon to compensate for low preamp gain and boost overall signal |
| **Bass** | 11:30 | 4.8 | Flat/neutral response for a full-bodied low end |
| **Treble** | 10:00 | 3.0 | Rolled off to warm up the highs and remove glassy chime |
| **Boost** | 7:00 | 0.0 | Turned off to ensure no preamp color or mid-hump |
| **Speaker** | DOWN (Red LED) | EV12 | 1x12 Electro-Voice speaker for flat, clean, linear response |
| **Mod** | Center/UP | Stock | Stock circuit for the most uncolored response |
| **ALT** | Center (AMP) | Off | Standard knob controls active |

---

#### Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 3. UADx LA-2A Silver Compressor — optical dynamics

| Control | Setting | Purpose |
|---------|---------|---------|
| **Peak Reduction** | 40 | Gentle peak control (0-1dB reduction) to smooth out picking attack transients |
| **Gain** | 20 | Makeup gain |
| **Mode** | Compress (3:1) | Retains acoustic pick dynamics |

---

## Starting Point Guide

*   **Reverb Integration:** This preset is configured dry. To add space, use a high-quality studio plate or hall reverb in post, or slowly dial the pedal's **Reverb** up to **9:00 (~2.0)** for a touch of spring.
*   **Instrument Matching:** 
    *   *Humbucker/Archtop:* This setting allows the natural woody, acoustic qualities of an archtop or neck humbucker to shine through cleanly.
    *   *Single-Coils:* Warm clean platform for jazz, bossa nova, or fingerstyle. If the tone feels a bit too dark on a Tele or Strat neck pickup, nudge the **Treble** up to **11:00 (~4.0)**.
