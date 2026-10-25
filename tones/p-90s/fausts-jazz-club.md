---
id: "fausts-jazz-club"
preset_name: "Faust's Jazz Club (The Velvet Vanguard)"
created: "2026-09-19"
updated: "2026-09-19"
guitar: "2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90s HSP-90s, Neck Pickup)"
target: "Intimate, warm electric jazz lead with touch-sensitive BiFET compression, woody low-mids, smooth pick attack blunting, and warm club reverberation."
tags: "jazz, lead, p-90, les-paul, polytone, ce1, stasimon, aetheria, warm, velvet, cozy"
tone-king-channel: bypassed
amp: "Polytone Mini Brute IV (Faust & Wagner)"
status: tested
pickup_type: p-90
standalone_preset_id: "C975659F-8CBC-4B42-8B59-B518D4B7A067"
preset_data:
  stasimon:
    level: 3.0
    mode: "Preamp Only (Normal)"
    sensitivity: "High (2SC900 Boost)"
    input_buffer: "Vintage Low-Z (50k)"
    stereo_spread: "Classic Dual Mix"
    volume: 0.0
  polytone_mini_brute:
    volume: 6.0
    voicing: "Dark (3.8kHz Veil)"
    bass: 4.5
    mid: 5.5
    treble: 5.0
    reverb: 0.0
    master: 0.0
    cab_sim: true
  aetheria:
    engine: "Room & Hall (8x8 FDN)"
    rt60_decay: 2.0
    absorption: 4500.0
    diffusion: 25.0
    archetype: 1.00
    pre_delay: 12.0
    level: 0.0
    mix: 35.0
---

# Faust's Jazz Club (The Velvet Vanguard)

## Target Sound

An intimate, warm, velvety electric jazz lead tone specifically tuned for the **2008 Epiphone Les Paul Standard Plus Top** loaded with **Tonerider Rebel 90 (P-90)** pickups (as specified in `tone-advisor/guitar_stable.md`). 

I know that single-coil P-90 pickups naturally possess an extended high-frequency bite and an assertive upper-mid peak around 2.5 kHz to 3.5 kHz compared to traditional humbuckers. To transform this energetic single-coil voice into the dark, smoky, velvety archtop tone heard in legendary late-night jazz clubs (like the Village Vanguard or Smalls), this serial signal chain deploys three symbiotic stages:

1. **Stasimon (CE-1 Digital Twin)**: Engaged in *Preamp Only* mode with *Vintage Low-Z (50kΩ)* loading. The 50kΩ input impedance deliberately loads down the Rebel 90 pickup coils, rounding off ultrasonic pick clicks and damping the resonant peak before the signal reaches the amplifier. The *High Sensitivity (2SC900)* discrete BJT booster injects rich 2nd-harmonic saturation and low-end authority.
2. **Polytone Mini Brute IV**: The quintessential solid-state jazz amplifier. Its *Dark (3.8 kHz Veil)* Sallen-Key low-pass filter eliminates remaining high-frequency edge, while the active gyrator midrange (+1.0 dB @ 650 Hz) pushes single-note lines forward with woody, singing substance. The BiFET preamp is pushed to volume 6.0, providing touch-sensitive soft compression that blossoms under the fingers.
3. **Aetheria (Classical & Ambient Reverb Laboratory)**: An 8x8 Householder Unitary Feedback Delay Network configured for a cozy, plush club room with 4500 Hz absorption, wrapping every note in the acoustic intimacy of velour booths and low ceilings.

---

## Signal Chain

```
[Epiphone Les Paul (Tonerider Rebel 90 Neck)]
  ──► [Audient iD14 Input 1 (D.I. 0 dB)]
  ──► [1. Stasimon] (Discrete BJT Preamp Line Driver & 50kΩ Low-Z Loading)
  ──► [2. Polytone Mini Brute] (110W BiFET Preamp + Dark Sallen-Key Veil + 1x12 Sealed Cab)
  ──► [3. Aetheria] (Spatial: 8x8 Householder FDN Cozy Room & Hall Reverb)
  ──► [Standalone Audio Master Out]
```

### 1. Hardware Front-End & Input Calibration

* **Tone King Imperial Preamp**: **Bypassed** (per the direct input standard in `tone-advisor/TONEPRINT_GUIDELINES.md`). Signal path connects directly into Audient iD14 Instrument Input 1.
* **Hardware Interface Gain**: **0 dB** (unity).
* **Host**: **Standalone Audio (Oort Media)** serial rack preset `Faust's Jazz Club` (`C975659F-8CBC-4B42-8B59-B518D4B7A067.json`).
* **Calibrated Trims**: Both Stasimon and Polytone In/Out trims remain at calibrated unity (0.0 dB).

---

### 2. Stasimon (CE-1 Digital Twin) — Discrete BJT Preamp Line Driver

*Role: Sweetener & pick-transient conditioner. BBD delay is muted; 100% discrete analog line driver path active.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Level** | **3.0** | Sweeps 50kΩ log pot into subtle Class-A BJT saturation without dirt. |
| **Mode** | **Preamp Only (Normal)** | Mutes BBD delay; engages 100% discrete analog line driver. |
| **Sensitivity** | **High (2SC900 Boost)** | Discrete BJT boost injects warm 2nd harmonics and low-end girth. |
| **Input Buffer** | **Vintage Low-Z (50k)** | Authentic 1976 passive pickup loading; rounds off ultrasonic pick click on P-90s. |
| **Stereo Spread** | **Classic Dual Mix** | Dual mono line driver output. |
| **Volume** | **+0.0 dB** | Unity level trim. |

---

### 3. Polytone Mini Brute — 110W Solid-State Jazz Amplifier Twin

*Role: Core amplifier, active Baxandall/gyrator tone shaping, and sealed 1x12 cabinet.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Volume** | **6.0** | BiFET soft-compression sweet spot for touch-sensitive dynamic bloom. |
| **Voicing Select** | **Dark (3.8kHz Veil)** | 2nd-order Sallen-Key low-pass filter ($f_c \approx 3.8\,\text{kHz}$) eradicates pick ping. |
| **Bass** | **4.5** | Slight low-end taper prevents excessive low-frequency resonance boom. |
| **Mid** | **5.5** | Active gyrator (+1.0 dB @ 650 Hz) pushes singing lead lines forward. |
| **Treble** | **5.0** | Flat baseline. |
| **Reverb** | **0.0** | Internal spring tank off (reverb handled downstream by Aetheria). |
| **Master** | **+0.0 dB** | 110W power amp output level. |
| **Cab Sim** | **ON** | 1x12 sealed acoustic-suspension velvet enclosure with high woofer damping. |

---

### 4. Aetheria — Classical & Ambient Reverb Laboratory

*Role: Cozy jazz club acoustic spatial environment.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Engine** | **Room & Hall (8x8 FDN)** | 8x8 Householder Unitary FDN for dense, uncolored room acoustics. |
| **RT60 (Decay)** | **2.0 s** | Intimate room decay time; cushions notes without cluttering fast runs. |
| **Absorption** | **4500.0 Hz** | Low-pass damping simulating carpet, velour booths, and an intimate crowd. |
| **Diffusion** | **25.0%** | Retains attack clarity on chord comping while smoothing room reflections. |
| **Pre-Delay** | **12.0 ms** | Separates direct note attack from reverberation onset. |
| **Mix** | **35.0%** | 35% wet blend places the guitar inside a cozy physical club space. |

---

## Starting Point Guide

- **Guitar Controls**: Select the **Neck P-90 Pickup**. Set guitar volume to **7–8** and tone to **6–7**. The combined action of the Tonerider Rebel 90's rolled-back tone pot, Stasimon's 50kΩ loading, and Polytone's Dark Veil completely removes brittle single-coil click while leaving warm, singing harmonic substance intact.
- **Touch & Dynamics**: Play with the flesh of the thumb or a thick rounded plectrum ($>1.5\,\text{mm}$). Notice how the BiFET preamp in the Polytone compresses gently when digging into accented double-stops or chord roots.
- **Humbucker Adaptation (e.g. Epiphone Sheraton II)**: When switching to a dual-humbucker semi-hollow with flatwounds (as cataloged in `tone-advisor/guitar_stable.md`), humbuckers have a thicker low-frequency fundamental and darker top end. Drop Polytone **Bass** to **4.0** (or **3.5** to prevent semi-hollow body cavity feedback) and raise Polytone **Mid** to **6.0** (+2 dB @ 650 Hz). If the tone feels overly dark, flip Stasimon's **Input Buffer** to **Modern Hi-Z (1M)** to restore high-frequency acoustic air.
- **Single-Coil Adaptation (e.g. Fender Player II Telecaster Neck)**: Telecaster neck pickups have lower output and tighter low-mids than Rebel 90s. Advance Polytone **Volume** from **6.0 to 6.5** to maintain the BiFET compression threshold, and dial **Bass** up from **4.5 to 5.0** to provide low-end weight. Keep Stasimon's **Input Buffer** firmly on **Vintage Low-Z (50k)** to prevent Telecaster single-coil icepick.

---

## Feedback History

### 2026-09-19 — tested
- Toneprint auditioned and verified in Standalone Audio using the native preset `Faust's Jazz Club` (`C975659F-8CBC-4B42-8B59-B518D4B7A067.json`, PC #65).
- Tested with the 2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90 neck pickup) monitoring through Sennheiser HD660S2 headphones.
- Stasimon 50kΩ loading and Polytone Dark 3.8kHz Veil successfully blunt P-90 pick attack while retaining rich vocal midrange bloom. Aetheria 8x8 FDN at 35% wet provides cozy club space.
