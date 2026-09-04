---
id: faust-feast-hb
preset_name: "Faust Feast HB (Clean Testbed)"
created: 2026-09-02
updated: 2026-09-02
guitar: Gibson Les Paul Studio / Epiphone Sheraton II (Humbuckers)
target: 'High-headroom, unyielding 6L6 clean platform designed as a neutral testbed for SPICEyNAM Faust pedal circuits with humbuckers.'
tags: "pedal-platform, testbed, clean, high-headroom, showtime, 6l6, humbucker, spiceynam, faust"
tone-king-channel: bypassed
amp: "Showtime '64 (UADx)"
status: initial
pickup_type: humbucker
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Bass: 4.5
    Bright: false
    Middle: 5.0
    Treble: 5.0
    Volume: 3.5
---

# Faust Feast HB (Clean Testbed)

## Target Sound
A pristine, transparent, high-headroom 6L6 pedal testbed specifically dialed to evaluate custom Faust-modeled pedal circuits from the SPICEyNAM project. I know that the early 1960s Showman architecture features massive transformer iron and robust power tubes that resist early sag and saturation, providing an unyielding foundation where upstream boosts, overdrive pedals, and stacking experiments can be auditioned without the amplifier masking circuit artifacts or prematurely clipping.

The tone stack is balanced for humbuckers: Bass is pulled slightly back to 4.5 to keep thicker neck pickups tight and articulate when pushed by boosts, while Middle and Treble remain flat at 5.0 to reveal the true frequency contour and clipping characteristics of the pedals under test.

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
| **Bright / Normal** | **Normal** (Off) | Eliminates bright cap boost to maintain a smooth, linear top end and prevent high-frequency sizzle with clipping diodes |
| **Volume** | **3.5** | High clean headroom zone; allows boost pedals to push signal level without triggering premature power-amp distortion |
| **Treble** | **5.0** | Flat baseline; transparent representation of pedal top-end response |
| **Middle** | **5.0** | Flat baseline; neutral midrange allows true pedal EQ contours to be heard |
| **Bass** | **4.5** | Slightly tightened; I know that humbucker neck pickups have a stronger low-end fundamental that can sound "flubby" when pushed by boost pedals if bass is set too high |
| **Vibrato** | **Off** | Modulation bypassed for clinical testbed neutrality |
| **Room** | **3.0** | Subtle internal room reflection inside the amp model; gives natural three-dimensional air without DAW aux clutter |
| **Cabinet** | **2x12 (fixed)** | Original paired 2x12 speaker cabinet |
| **Mic** | **Condenser 414** | Detailed, transparent, full-frequency capture across lows and highs; reveals subtle harmonics and clipping knee behavior |
| **Out** | **Default (Unity)** | Post-amp track level matching |

---

## Starting Point Guide

- **First adjustment**: When auditioning a high-output clean boost, watch the track meter in Logic/Element. If the boost pushes the overall level hot, adjust the Faust pedal's output or trim Showtime '64's **Out** rather than lowering the amp's **Volume** (which would alter the tone stack response).
- **Evaluating Pedal Stacking**: If stacking two drive pedals (e.g. a transparent boost into a soft-clipping overdrive), listen for low-end definition on the wound strings (E and A). If the low end starts to compress excessively or turn muddy, pull **Bass** down from 4.5 to 4.0.
- **Microphone Alternative**: If a high-gain pedal circuit produces fizzy top end that distracts from core clipping character, switch the Mic from **Condenser 414** to **57 + Ribbon 121** (or **Ribbon 160**) to introduce gentle analog high-frequency smoothing.

---

## Feedback History

### 2026-09-02 — initial
Toneprint created as a dedicated neutral pedal testbed for the SPICEyNAM Faust circuit modeling project. Configured with UADx Showtime '64, -3.2 dB iD14 calibration offset, Condenser 414 mic, and internal Room at 3.0. Bass dialed to 4.5 for humbucker clarity.
