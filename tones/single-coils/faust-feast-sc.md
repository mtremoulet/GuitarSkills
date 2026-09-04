---
id: faust-feast-sc
preset_name: "Faust Feast SC (Clean Testbed)"
created: 2026-09-02
updated: 2026-09-02
guitar: Fender Player II Telecaster / Squier Stratocaster (Single-Coils)
target: 'High-headroom, unyielding 6L6 clean platform designed as a neutral testbed for SPICEyNAM Faust pedal circuits with single-coils.'
tags: "pedal-platform, testbed, clean, high-headroom, showtime, 6l6, single-coil, telecaster, stratocaster, spiceynam, faust"
tone-king-channel: bypassed
amp: "Showtime '64 (UADx)"
status: initial
pickup_type: single-coil
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Bass: 5.0
    Bright: false
    Middle: 5.0
    Treble: 4.5
    Volume: 4.0
---

# Faust Feast SC (Clean Testbed)

## Target Sound
A pristine, transparent, high-headroom 6L6 pedal testbed specifically voiced to evaluate custom Faust-modeled pedal circuits from the SPICEyNAM project using single-coil guitars. I know that single-coil pickups produce sharper transient spikes and extended high-frequency harmonics compared to humbuckers, which can turn biting or "ice-picky" when pushing non-linear clipping stages.

The Showtime '64 provides an unyielding, muscular clean foundation that will not break up prematurely. The tone stack is tuned specifically for single-coils: Treble is softened slightly to 4.5 to keep bridge and in-between pickup positions musical when driven, Bass is kept full at 5.0 to provide solid acoustic weight and low-frequency foundation, and Volume is lifted to 4.0 to compensate for lower pickup output while preserving abundant clean headroom.

## Signal Chain

```
[Guitar] → [Audient iD14 Input 1 (D.I.)] → [Faust Pedal / Circuit Under Test] → [Showtime '64 (UADx)]
```

### 1. Hardware Front-End & Input Calibration
*   **Tone King Imperial Preamp:** **Bypassed**. Signal path connects directly into the Audient iD14 instrument input 1 (per the Direct Input standard in `tone-advisor/TONEPRINT_GUIDELINES.md`).
*   **Hardware Interface Gain:** Set to minimum (**0 dB** / unity).
*   **DAW Input Offset:** In Showtime '64, set the internal **In** control to **-3.2 dB** (or turn slightly toward Line from center HI-Z). As cited in `tone-advisor/TONEPRINT_GUIDELINES.md`, the Audient iD14 D.I. clips at +9.0 dBu whereas UADx plugins expect a +12.2 dBu reference; the -3.2 dB offset guarantees a calibrated 1:1 analog-equivalent input level.

### 2. UADx Showtime '64 Tube Amp — Clean Anchor

Documented in `tone-advisor/docs/uad/showtime-64-tube-amp.md`.

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **In** | **-3.2 dB** (toward Line) | Interface calibration offset for Audient iD14 (+9.0 dBu D.I. vs +12.2 dBu UADx standard) |
| **Bright / Normal** | **Normal** (Off) | Eliminates bright cap boost to keep high frequencies natural and prevent harshness with single-coil pickups |
| **Volume** | **4.0** | High clean headroom zone; adjusted to match lower single-coil output while staying strictly non-distorting |
| **Treble** | **4.5** | Slightly rounded; prevents top-end harshness or diode buzz on Tele bridge or Strat pickups |
| **Middle** | **5.0** | Flat baseline; transparent midrange preserves the intrinsic voice of pedals under test |
| **Bass** | **5.0** | Full low-end fundamental; provides body and prevents thinness under light drives |
| **Vibrato** | **Off** | Modulation bypassed for clinical testbed neutrality |
| **Room** | **3.0** | Subtle internal room reflection inside the amp model; gives natural three-dimensional air without DAW aux clutter |
| **Cabinet** | **2x12 (fixed)** | Original paired 2x12 speaker cabinet |
| **Mic** | **Condenser 414** | Detailed, transparent, full-frequency capture across lows and highs; reveals subtle harmonics and clipping knee behavior |
| **Out** | **Default (Unity)** | Post-amp track level matching |

---

## Starting Point Guide

- **First adjustment**: If testing brighter circuits (like a treble booster or a high-gain drive) with the Telecaster bridge pickup, you can pull **Treble** down to **4.0** or roll the guitar's physical Tone knob back to **7** (per the "7/7" Baseline in `tone-advisor/TONEPRINT_GUIDELINES.md`).
- **Evaluating Pedal Stacking**: When stacking a clean boost into a low-gain overdrive, listen to string separation on complex chords (e.g. maj7, m9). If high harmonics clash or sound brittle, try switching the Mic selector from **Condenser 414** to **57 + Ribbon 121**, which introduces the natural high-frequency smoothing of the ribbon motor.
- **Dynamic Touch Response**: I know that single-coil pickups are exceptionally sensitive to pick angle and velocity. Use the volume and tone controls on your guitar to test how cleanly the Faust pedal models clean up before reaching the amp.

---

## Feedback History

### 2026-09-02 — initial
Toneprint created as a dedicated neutral pedal testbed for the SPICEyNAM Faust circuit modeling project. Configured with UADx Showtime '64, -3.2 dB iD14 calibration offset, Condenser 414 mic, and internal Room at 3.0. Treble dialed to 4.5 and Volume to 4.0 for single-coil balance.
