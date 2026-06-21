---
amp: "Enigmatic '82"
created: 2026-05-24
guitar: "Gibson Les Paul Studio (490R neck pickup)"
id: paradise-enigmatic-boutique-clean
pickup_type: humbucker
preset_name: "Enigmatic Boutique Clean HB"
status: refined
tags: "boutique, clean, warm, les-paul, humbucker, dumble, paradise-studio, enigmatic-82"
target: "Boutique ODS warmth inside Paradise Guitar Studio — rich, touch-sensitive clean with full, fat lower-mids and a smooth, saturated-feeling response that mimics the Two Rock Bloomfield."
tone-king-channel: bypassed
updated: 2026-05-25
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Bass: 7
    Boost: false
    Bright: false
    Middle: 7.5
    Master: 7
    Presence: 0.5
    Treble: 3.5
    Volume: 5.5
  hitsville:
    decay: 2.0
    mix: 1.0
    pre_delay: 8.0
  la2a:
    gain: 28
    peak_reduction: 35
---

# Enigmatic '82 — Boutique Warm Clean (Paradise Guitar Studio)

## Target Sound

The Universal Audio Paradise Guitar Studio contains the **Enigmatic '82**, an incredible emulation of the legendary Dumble Overdrive Special (ODS) boutique amplifier. Since Two Rock's amplifier designs are heavily inspired by classic Dumble ODS and Steel String Singer circuits, the Enigmatic '82 is the perfect candidate to capture the Two Rock's signature "saturated but clean" boutique ethos.

The goal of this toneprint is a rich, three-dimensional, and touch-sensitive boutique clean. It provides a fat, warm lower-midrange that fills out the Les Paul Studio's 490R neck humbucker without becoming muddy or boomy. By running the Enigmatic '82 on the **Suede** voice (known for its smooth, round preamp compression) and pushing the Master volume, we achieve that "maxed-out power amp bloom" feeling where notes stay clean but feel incredibly thick and vocal.

This toneprint is designed for direct-in recording (bypassing the Tone King preamp and TONEX One) and pairs with our favorite post-amp optical compression and space plugins.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. UADx Paradise Guitar Studio — boutique character source

To keep the comparison with our Two Rock toneprint completely fair and transparent, we bypass all of Paradise Guitar Studio's internal effects (compression, delay, reverb) and rely on the standalone LA-2A and Hitsville Reverb. This isolates the Enigmatic '82's beautiful amp circuit and cabinet model.

**Switches and Gallery Configuration**

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **Enigmatic '82** | Selected in the amp gallery |
| Voice | **Suede** | "Warm, round, and smooth" boutique character; ideal for rounding off humbucker harshness and adding low-mid weight |
| Input Channel | **NOR** (Normal Jack) | **CRITICAL:** Use the bottom **NOR** input jack. The top **FET** jack is a solid-state transistor-based boost that injects clinical, razor-sharp transients and high-end focus. The Normal input runs directly into warm, saggy tube circuits. |
| Bright Switch | **Off** (Normal) | Down position; tames high-end sizzle and harshness for a smooth, smoky character |
| Mid Switch | **Off** (Normal) | Down position; keeps the midrange balanced and natural |
| Deep Switch | **Off** (Normal) | Down position; preserves lower-midrange presence and keeps the high end integrated |
| Rock / Jazz Switch | **JAZZ** | Down position; provides a smoother, rounder frequency response than the aggressive, mid-forward Rock setting |
| Preamp Mods (Tone Stack) | **SKYLINE** | **CRITICAL:** Use **Skyline** under PREAMP MODS. Skyline contains the famous Dumble ODS midrange bloom that glues the highs and lows together. *Note: If Skyline feels "quieter" or "thinner" than Classic, it is because it rounds off the artificial bass/treble scoop of the Classic stack. We compensate for this by pushing the preamp Volume and Bass EQ (see below).* |
| Boost Button | **OFF** | Disengaged; maintains clean headroom and dynamic range |
| Overdrive Section | **OFF** | Level & Ratio bypassed; we are strictly in the high-headroom Clean channel |

**Amp Controls**

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **5.5** | Preamp volume / input gain sweet spot; pushes the preamp into touch-sensitive saturation |
| Treble | **3.5** | Rolled back to round off the top end and prevent high-frequency harshness |
| Middle | **7.5** | **Pushed to 7.5:** Heavily boosts the Skyline midrange to provide rich, singing, throatier body to the Les Paul neck humbucker |
| Bass | **7.0** | **Pushed to 7.0:** Skyline’s tight EQ allows us to heavily boost the Bass to 7.0, giving immense, warm lower-frequency weight and fullness |
| Level / Ratio (OD) | — | Bypassed; not in use |
| Master (labeled **6.5**) | **7.0** | **Pushed to 7.0:** Simulates maximum power amp saturation and thickness; primary control for "bloom" and sustain |
| Presence | **0.5** | **Pulled down to 0.5:** Kept extremely low to completely smooth out the power amp high-frequency contour and eliminate clinical top-end |

**Cabinet & Microphone (Amp Pane)**

In Universal Audio plugins, the Cabinet and Mic combinations are a single, fixed-selection preset. From the UADx guitar amp plugin choices, we select:

| Component | Setting (PGS Label) | Sonic Character & Aesthetic Profile |
|-----------|---------------------|-------------------------------------|
| Cab & Mics Preset | **2×12 Boutique D65** | **The Dumble/Two-Rock Sweet Spot:** Emulates a 2x12 cabinet with Celestion G12-65 speakers mic'd with a pre-blended Shure SM57 (dynamic) and Royer 121 (ribbon). Provides dense lower-midrange "meat," smooth treble compression, and an organic, chewy feel that perfectly matches our Two Rock target. |
| Room Level | **32%** | **CRITICAL:** Set the Room dial to **32%** (as discovered in feedback). This introduces natural cabinet room reflections and air, blending the pre-blended mics together in an organic acoustic space and taming the "clinical precision." |

---

### 3. UADx LA-2A Silver Compressor — organic optical glue

The optical compression of the LA-2A Silver is crucial to this tone. It evens out the Les Paul’s picking dynamics, adds sustain, and provides that polished, finished "studio record" feel.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | **35** | Targets `1–3 dB` of compression on firm strums; glues the notes together |
| Gain | **28** | Makeup gain calibrated for healthy, clean output target (~ −12 dBFS) |
| Mode | **Compress** (3:1) | Gentle optical compression; preserves natural picking dynamics |

---

### 4. UADx Hitsville Reverb Chambers — shared room space (Aux 2)

By using the exact same reverb auxiliary bus as our Two Rock Bloomfield print, you can A/B test the two amps in the identical acoustic environment!

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Present, rich room reflections |
| Speaker | **Bozak 800** | Classic Detroit chamber speaker setup |
| Mic | **Unidyne 545** | Articulate guitar reverb mic |
| Mix | **Wet Solo (100%)** | Placed on Aux 2; fader controls blend |
| Decay | **9:00** | Tight, short room reflection for rhythm clarity |
| Pre-Delay | **8 ms** | Slight separation between dry pick attack and room response |

**Logic Send Routing**
*   **Send Level (Aux 2):** −12 dB
*   **Bus Fader (Aux 2):** −8 dB

---

## Starting Point Guide

- **First adjustment (Bloom / Headroom):** The **Master** control on the Enigmatic '82 (labeled **6.5** on the faceplate). If the tone feels too stiff or direct, push the Master to **7.0** or **7.5** and pull back the plugin's Output Trim to compensate. Pushing the Master increases the virtual power tube compression.
- **Taming Humbucker Boom:** If the low-end feels "flubby" on low E-string chords, roll the **Bass** control back to **4.0** or make a small 2-3dB cut at 125 Hz in your Logic channel EQ.
- **The Voice Switch Alternative:** While **Suede** is the default for this warm, smoky vibe, switching to the **Cream** voice will push the midrange focus slightly higher, creating a singing, vocal quality that is incredible for melodic lead playing or bossa nova chord voicings.

---

## Feedback History

### 2026-05-25 — refined (addressing high-frequency harshness)
Tested in session. Bypassed internal Reverb, Compressor, and EQ pedals in PGS to isolate the amp circuit. Added **Room level at 32%** to blend the mics together and soften the DAW clinical precision. Addressed a major "high-frequency harshness / over-sharpened photo" issue through a calibration loop:
1. **NOR Input:** Switched from the clinical solid-state FET input back to the bottom **NOR** (Normal) input for warm tube preamp compression.
2. **Toggle Alignment:** Confirmed Bright and Deep switches are indeed **OFF (Down)**.
3. **Skyline Midrange Calibration:** Resolved the Skyline vs. Classic tone stack tradeoff. Classic has a deep Fender mid-scoop that pushes the bass/treble extremes (making it sound "big" but harsh on the top end). Skyline brings the mids forward and tightens the extremes (which psychoacoustically makes it sound "quieter" or "thin"). We countered this by pushing the preamp **Volume to 5.5**, **Bass to 7.0**, and **Middle to 7.5**. This drives the virtual tubes into a thick, organic, and beautifully compressed saturation without losing that crucial boutique warmth.
4. Set **Treble to 3.5** and **Presence to 0.5** to perfectly roll off the clinical edge.
5. **Final Touch:** Locked in the dialed-in values: **Volume 5.5, Treble 3.5, Middle 7.5, Bass 7.0, Master 7.0, Presence 0.5**. These parameters push the low-mids and vocal midrange of the Skyline stack to the max, providing incredible body and richness. Note: The Mixwave Two Rock still retains a slightly tamer/smokier high end, which can be further tweaked in the future, but these settings get Enigmatic in the exact close ballpark. Status updated to `refined`.

### 2026-05-24 — initial
Created as part of a dual-preset boutique Dumble-style clean exploration. Bypasses physical front-end (Tone King & TONEX One) to run direct into the iD14 interface. Uses Paradise Guitar Studio's Enigmatic '82 on the Suede voice to match the warm, saturated-but-clean ethos of the Two Rock Bloomfield. Bypasses all internal plugin effects to isolate the amp circuit, using our signature standalone LA-2A Silver and Hitsville Reverb Aux bus for an exact, fair comparison against the Two Rock.
