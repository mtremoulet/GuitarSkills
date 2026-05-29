---
id: two-rock-bloomfield-p90
preset_name: "Two-Rock Bloomfield Boutique Clean P90"
created: 2026-05-26
updated: 2026-05-26
guitar: Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)
target: "High-end boutique warm clean tailored for the Framus's resonant swamp ash snap and DiMarzio P-90 vocal midrange."
tags: boutique, clean, warm, framus, p-90, two-rock, jazz-blues, neo-soul, bloomfield
tone-king-channel: bypassed
amp: Two Rock
status: initial
pickup_type: p-90
---

# Two Rock Bloomfield — Boutique Warm Clean (P-90 Variant)

## Target Sound

The MixWave Two Rock Bloomfield Drive is a high-end boutique amplifier known for extraordinary note separation, very touch-sensitive dynamics, and a signature midrange bloom. This variant is specifically tailored to the bolt-on maple neck and swamp ash body of the Framus Earl Slick Artist Series, maximizing the sweet, vocal growl of the DiMarzio P-90 pickups.

By bypassing the physical Tone King front-end to leverage the direct Audient iD14 JFET transparency, we highlight the fast pick attack of the Framus. We replace the standard SM57 mic with a warm, detailed **Condenser 414** to translate the acoustic "spank" of the ash body into a three-dimensional, studio-quality bloom, while utilizing a **Ribbon 84** to retain fat low-mid resonance. 

An active noise gate is essential to control the single-coil idle hum of the hot DiMarzio P-90s during late-night monitoring on Sennheiser HD660S2 headphones.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed** (direct JFET path for absolute transparency and quick transient response; iD14 Input 1 gain set to **0**; Guitar bus set to **Mono** in Logic Pro).

---

### 2. MixWave Two Rock Bloomfield Drive — boutique character source

Small EQ adjustments have noticeable effects. The settings below are balanced to allow the DiMarzio P-90 midrange to stand out without muddying, while sweetening the snappy swamp ash high-end.

**Switches and Configuration**

| Control | Setting | Purpose |
|---------|---------|---------|
| EQ Selection | **EQ 1** | Clean-tone EQ: extended midrange, full bass, high headroom |
| Bright Switch | Off | Keeps the high-end smooth; prevents the swamp ash spank from becoming glassy |
| Mid Switch | Off | Rolled back to allow the P-90's natural vocal mid-range to carry the weight |
| Deep Switch | Off | Avoids low-mid boominess in the resonant swamp ash body |
| Tone Stack Bypass | Off | Keep the EQ knobs active |
| Lead Switch | Off | Clean channel only |
| Tube Select | **6L6** | Maximum clean headroom |
| Full/Half Power | **Full (100w)** | Maximum clean headroom and transient response |

**Amp Controls**

| Control | Setting | Purpose |
|---------|---------|---------|
| Gain | 4.8 | Clean but highly touch-sensitive; light picking stays clean, hard attack blooms |
| Treble | 4.8 | Pushed slightly from original humbucker settings to let the swamp ash chime breathe without harshness |
| Middle | 5.0 | Kept flat at noon; the DiMarzio P-90s provide plenty of singing midrange on their own |
| Bass | 4.5 | Pulled back slightly to control the swamp ash body's resonant low end |
| Presence | 5.0 | Neutral power amp high-end contour |
| Master | 5.0 | Clean channel output level |
| Reverb | 0 | Off — Hitsville handles the space |
| Vibe | 4.5 | Slightly reduced to roll off extreme high-frequency harmonics, sweetening the roundwounds |

**Plugin I/O Trims**

| Control | Setting | Purpose |
|---------|---------|---------|
| Input Trim | −8.0 dB | Virtual preamp input pad; keeps the hot P-90s from early preamp clipping |
| Output Trim | −6.25 dB | Calibrated output trim for a targeted −12 dBFS level |
| Noise Gate | **0.380** | **CRITICAL:** High-quality gate engaged to block idle P-90 single-coil hum |

**Cabinet and Mic**

| Control | Setting | Purpose |
|---------|---------|---------|
| Cabinet | 2x12 Two-Rock Vertical | Standard vertical cab pairing |
| Mic L (Bottom) | **Ribbon 84** | Captures fat low-mids and provides a smooth high-frequency roll-off |
| Mic R (Top) | **Condenser 414** | Replaces the SM57 to provide a detailed, three-dimensional acoustic spank |

---

### 3. UADx LA-2A Silver Compressor — organic glue

Provides subtle optical leveling to glue the swamp ash pick attack to the warm amp decay.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 32 | Gentle optical smoothing (~2-3 dB of reduction on firm picks) |
| Gain | 28 | Calibrated makeup gain |
| Mode | Compress (3:1) | Slower, musical optical compression |

---

### 4. UADx Hitsville Reverb Chambers — intimate space
Placed on **Bus 2** (Reverb bus). Channel send: **−12 dB**, Aux Bus Fader: **−8 dB**.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Present, rich room reflections |
| Speaker | **Bozak 800** | Classic chamber setup |
| Mic | **Unidyne 545** | Articulate guitar reverb mic |
| Mix | **Wet Solo (100%)** | Aux send configuration |
| Decay | **9:00** | Tight, short room reflection for rhythm clarity |
| Pre-Delay | 8 ms | Dynamic separation from pick attack |

---

## Starting Point Guide

- **Physical Pickup Position**: Start with the **Middle (neck/bridge blend)** position. The swamp ash snap blends beautifully with the P-90 body here. If you want more vocal throatiness, switch to the Neck pickup and roll your guitar volume back to **8**.
- **Adjusting the Snappy Attack**: If the bolt-on maple neck has too much "spank" for your late-night mood, lower the **Vibe** control on the Two Rock to **4.0** or increase the **Ribbon 84** microphone blend in the cabinet section.
- **The Noise Gate**: If you notice notes cutting off too abruptly during delicate fingerpicking, lower the Two Rock **Noise Gate** to `0.300` or play with the guitar's physical volume knob rolled down to `7`.

---

## Feedback History

### 2026-05-26 — initial
Ported from the humbucker LP variant. Bypasses Tone King to run direct JFET, lowers Two Rock Gain to 4.8 for the hotter P-90s, flattens Mid to 5.0, slightly boosts Treble to 4.8, and swaps the top cabinet mic to a Condenser 414 to capture the three-dimensional acoustic snap of the swamp ash body. Noise gate set to `0.380` to manage P-90 hum.
