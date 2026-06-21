---
amp: "Dream '65"
created: 2026-06-10
guitar: "Squier Stratocaster (neck or neck/middle positions)"
id: dream-65-srv-texas-growl
pickup_type: single-coil
preset_name: "Dream 65 SRV Texas Growl"
status: initial
tags: "blackface, srv, blues, texas-blues, single-coil, dream-65, d-tex, spring-reverb"
target: "Fat, midrange-forward Texas blues tone with dynamic edge-of-breakup response and lush spring reverb"
tone-king-channel: bypassed
updated: 2026-06-10
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 4.0
    Reverb: 4.0
    Output: 7.0
    Bass: 3.5
    Treble: 5.5
    Boost: 7.0
    Speaker: "GB25 (Red LED)"
    Mod: "D-Tex"
    AltMode: false
  la2a:
    gain: 20
    peak_reduction: 40
---

# Dream '65 — SRV Texas Growl

## Target Sound

The **SRV Texas Growl** is designed to capture the iconic "Texas Blues" tone associated with Stevie Ray Vaughan. It uses the Dream '65's **D-TEX** modification, which emulates a classic Texas-blues style amp mod that boosts midrange, fatness, and gain sensitivity. 

While the stock Deluxe Reverb is known for its mid-scoop and glassy top-end, this preset reshapes the amp into a mid-forward, punchy blues machine that growls when you dig in with single-coil pickups (specifically a Stratocaster in the neck or neck/middle position). 

### Nudges from the Visual Guess
To make this tone more authentic and dynamic:
*   **Volume Nudge (from 10:00 to 11:00/11:30 - ~4.0):** Raising the preamp volume slightly past the edge-of-breakup allows the amp model to compress and bloom organically under a heavy picking attack.
*   **Reverb Nudge (from 1:00 to 11:30 - ~4.0):** Deluxe Reverb spring tanks get splashy quickly. Bringing this back slightly keeps the notes clear and punchy while retaining a warm, ambient space.
*   **Bass Nudge (to 10:30 - ~3.5):** Kept tight to prevent the low-end from flubbing out under the high boost level.
*   **Treble Nudge (to 12:30 - ~5.5):** Adds just enough snap to cut through the heavy midrange boost of the D-TEX circuit.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom).

---

### 2. UADx Dream '65 Reverb Amp — character source

| Control | Clock Setting | Value (0-10) | Purpose |
|---------|---------------|--------------|---------|
| **Volume** | 11:30 | 4.0 | Pushes the preamp to the edge of breakup |
| **Reverb** | 11:30 | 4.0 | Lush spring reverb decay without drowning the notes |
| **Output** | 2:00 | 7.0 | Master output level to feed downstream effects |
| **Bass** | 10:30 | 3.5 | Rolled back to keep the low end tight |
| **Treble** | 12:30 | 5.5 | Brightness and snap to balance the mid-heavy boost |
| **Boost** | 2:00 | 7.0 | Controls the D-TEX modification's gain/mid push |
| **Speaker** | UP (Red LED) | GB25 | 1x12 Greenback cab adds woody midrange and smooths highs |
| **Mod** | DOWN | D-TEX | Engages the Texas mid-boost circuit modification |
| **ALT** | Center (AMP) | Off | Standard knob controls active |

---

### 3. UADx LA-2A Silver Compressor — optical sustain

| Control | Setting | Purpose |
|---------|---------|---------|
| **Peak Reduction** | 40 | Yields subtle `0 to 1dB` of compression, smoothing out transients and extending sustain |
| **Gain** | 20 | Makeup gain |
| **Mode** | Compress (3:1) | Retains pick dynamics |

---

## Starting Point Guide

*   **Guitar Position:** Use a Stratocaster. The neck pickup (Position 5) is the primary target for that fat, woody rhythm growl. Switch to the neck/middle blend (Position 4) for a hollower, quackier blues tone.
*   **Alternative Speaker Choice:** If you want a tighter, cleaner, and louder response with massive headroom (similar to SRV's actual JBL/EV speaker setups), toggle the **Speaker Switch DOWN** to select the **EV12** cabinet.
*   **Dynamics Control:** Control your gain with your hand. Soft fingerpicking stays warm and clean; digging in with a heavy pick will activate the D-TEX growl.
