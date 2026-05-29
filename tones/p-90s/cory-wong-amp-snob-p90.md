---
id: cory-wong-amp-snob-p90
preset_name: "Amp Snob Boutique Clean P90"
created: 2026-05-26
updated: 2026-05-27
guitar: Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)
target: "Boutique Dumble-style ODS warmth inside Archetype Cory Wong X — adapted for the Framus's fast swamp ash transients and singing DiMarzio P-90 midrange."
tags: boutique, clean, warm, framus, p-90, dumble, neural-dsp, cory-wong, amp-snob
tone-king-channel: bypassed
amp: The Amp Snob
status: tested
pickup_type: p-90
---

# Amp Snob — Boutique Warm Clean (P-90 Variant)

## Target Sound

This toneprint adapts Neural DSP's **"The Amp Snob"** (a clean-voiced Dumble-style head) to the snappy, resonant footprint of the Framus Earl Slick Artist Series. P-90 pickups through a Dumble-style circuit create a rich, singing "woody" response with incredible note definition and touch-sensitivity.

To optimize the chain for the Framus's bolt-on maple neck and roundwound strings, we make three critical adjustments:
1.  **Parallel Compression Calibration**: We back off the parallel compressor's depth and blend slightly to ensure the fast pick attack of the swamp ash body isn't squashed, while maintaining that Dumble "rubbery" sustain in the tail.
2.  **Gain-Staging Rollback**: Because the DiMarzio P-90s are hotter than traditional single-coils, we roll the Amp Snob's input volume (Gain) down to **38%** to protect clean headroom.
3.  **Corrective Graphic EQ**: We employ a custom 9-band EQ curve to highlights the P-90's vocal 1 kHz midrange while smoothing out the snappy 2 kHz pick attack and retaining the ash body's 4 kHz chime.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed** (direct JFET path for maximum transparency; iD14 Input 1 gain set to **0**; Guitar bus set to **Mono** in Logic Pro).

---

### 2. Archetype Cory Wong X — boutique character & compression

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 4th Position Compressor** | **Active** | **ON** | Essential parallel optical compression |
| | **Blend** | **35%** | Preserves the snappy pick attack of the bolt-on maple neck |
| | **Tone** | **50%** | Neutral high frequencies |
| | **Compression**| **30%** | Slightly lower depth to prevent the hot P-90s from over-squashing |
| | **Volume** | **55%** | Unity gain calibration |

*All other Pre FX (Envelope Filter, Tuber OD, Big Rig OD) are **BYPASSED**.*

**Amp Section — "The Amp Snob"**

All parameters are specified in percentages (0–100%).

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Amp Snob** | Clean Dumble-style head |
| Volume (Gain) | **38%** | Input gain sweet spot; keeps the preamp clean with the hotter P-90 pickups |
| Master | **75%** | **Pushed high**: Drives virtual power tubes into warm compression and saturation |
| Drive Switch | **OFF** | Bypasses extra gain stage to maximize clean headroom |
| Bright Switch | **OFF** | Keeps the high-end smooth and warm |
| Bass | **44%** | Rolled back to prevent low-end rumble in the swamp ash body |
| Middle | **52%** | Balanced; allows the DiMarzio P-90's natural mids to dominate |
| Treble | **50%** | Neutral, smooth chime |
| Presence | **50%** | Power amp high-end air |
| Output | **70%** | Manages plugin output level to match our −12 dBFS target |

**Cab Section (Unlinked Cabinets)**

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **Off** | Custom mic/cab configuration |
| Cab Type | **Snob** | Matching 2x12 open-back boutique cabinet |
| Cab L | **Active** | Primary mic |
| Mic L Type | **Ribbon 121** | Creamy, warm, vintage character; rounds off high transients |
| Position L | **0.50** | Shifted slightly closer to the center cone for enhanced woody warmth |
| Distance L | **0.25** | Close-mic'd with a touch of air |
| Room Send L | **−28.0 dB** | Kept low to keep the core tone tight and dry |
| Cab R | **BYPASSED** | Avoids phase alignment issues |

**EQ Section (Amp Snob 9-Band Graphic EQ)**

| Band | Setting | Purpose |
|------|---------|---------|
| EQ Status | **Active** | Corrective voicing curve |
| 65 Hz | 0.0 dB | Neutral |
| 125 Hz | 0.0 dB | Neutral |
| 250 Hz | −1.0 dB | **Targeted cut**: Cleans up muddy build-up from the neck P-90 |
| 500 Hz | +0.5 dB | Boosts lower midrange warmth and woodiness |
| 1 kHz | +1.0 dB | Accentuates the singing, vocal midrange of the DiMarzio P-90s |
| 2 kHz | −1.5 dB | **CRITICAL CUT**: Softens pick-attack harshness from the bolt-on maple neck |
| 4 kHz | +0.5 dB | Highlights the natural chime of the swamp ash body |
| 8 kHz | 0.0 dB | Neutral |
| 16 kHz | 0.0 dB | Neutral |
| HPF / LPF | Default | 20 Hz High-Pass / 20.0 kHz Low-Pass |

---

### 3. UADx Hitsville Reverb Chambers — shared room space (Aux 2)
Placed on **Bus 2** (Reverb bus). Channel send: **−12 dB**, Aux Bus Fader: **−8 dB**.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Present, rich room reflections |
| Speaker | **Bozak 800** | Classic Detroit chamber speaker setup |
| Mic | **Unidyne 545** | Articulate guitar reverb mic |
| Mix | **Wet Solo (100%)** | Aux send configuration |
| Decay | **9:00** | Tight room reflection for rhythm clarity |
| Pre-Delay | **8 ms** | separation between dry note and room reflections |

---

## Starting Point Guide

- **Fine-Tuning the Compression**: The **Blend** knob on **The 4th Position Compressor** controls the feel of your picking hand. If you want a more traditional jazz "acoustic" response, pull the blend down to **25%**. For highly sustained, fluid melodic lines, raise it to **40%**.
- **Guitar Controls**: For the sweet, woody jazz-fusion tone (Larry Carlton/Robben Ford style), set the Framus to the **Neck pickup**, roll your **Guitar Volume knob** back to **7 or 8**, and keep your picking hand light.
- **Graphic EQ bypass**: To hear the raw, unshaped voice of the Amp Snob on your P-90s, simply toggle the **EQ Active** switch to OFF. You will immediately notice the 2 kHz pick attack return, showing how the EQ softens the bolt-on neck.

---

## Feedback History

### 2026-05-27 — tested
Tested by Mike with no notes. Nailed the boutique clean sound on the Framus P-90. Status updated to `tested`.

### 2026-05-26 — initial
Ported from the humbucker LP variant. Lowers Amp Snob Volume to 38% for hotter P-90s, adjusts parallel compression blend to 35% and compression depth to 30% to preserve swamp ash pick attack, and optimizes the graphic EQ (notably taming 2 kHz by −1.5 dB to smooth out bolt-on neck transients).
