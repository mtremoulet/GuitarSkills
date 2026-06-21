---
id: two-rock-singing-blues-p90
preset_name: "Two-Rock Singing Blues P90"
created: "2026-06-18"
updated: "2026-06-18"
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
target: "A singing, touch-sensitive Mayer-style blues tone with a compressed clean foundation, subtle edge-of-breakup, and lush spatial delay/reverb."
tags: "boutique, clean, blues, singing, compression, two-rock, p-90, framus, delay, reverb"
tone-king-channel: bypassed
amp: "Two-Rock Bloomfield"
status: initial
pickup_type: "p-90"
preset_data:
  amp_platform: mixwave
  amp_settings:
    Gain: 5.5
    Treble: 5.0
    Middle: 5.2
    Bass: 4.5
    Presence: 5.5
    Master: 6.0
    Reverb: 0
    Vibe: 4.8
    Bright: false
    Mid: false
    Deep: false
    Tone Stack Bypass: false
    Lead: false
    Noise Gate: 0.35
  la2a:
    peak_reduction: 35.0
    gain: 28.0
    compress: true
  hitsville:
    mix: 1.0
    decay: 2.4
    pre_delay: 15.0
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 18.0}
    band4: {on: true, freq: 400.0, gain: -1.5, q: 1.0}
    band8: {on: true, freq: 6800.0, slope: 24.0}
preset_overrides:
  OverdriveOnOff: true
  OverdriveOverdrive: 2.2
  OverdriveTone: 5.5
  OverdriveBalance: 6.2
  OverdriveMix: 4.0
---

# Two Rock Bloomfield — Singing Blues (P-90 Variant)

## Target Sound

This toneprint is designed to capture a John Mayer-style "singing blues" tone—modeled after his live clean/lead dynamic balance in performances like "Free Fallin'" and "Human Nature." The core philosophy is a high-fidelity, compressed clean platform that has just enough "hair" and sustain to sing like a lead voice, without turning into heavy overdrive.

By pairing the MixWave Two-Rock Bloomfield Drive (EQ 2 structure) with the direct JFET input path of the Audient iD14, we retain the fast transient snap of the Framus's maple neck and swamp ash body. The built-in overdrive pedal is engaged with low gain and a blended mix (40% wet) to act as a parallel clean boost, adding vocal midrange focus and singing sustain. A post-amp LA-2A compressor glues the dynamics, while a bused Hitsville Reverb and Galaxy Tape Echo provide the lush, wide stereo wash typical of Mayer's live arenas.

---

## Signal Chain

```
[Guitar Direct JFET] 
       ↓
[MixWave Two-Rock Bloomfield Drive (Amp & Cab)] 
       ↓
[UADx LA-2A Silver Compressor (Insert 1 - Post-Amp)] 
       ↓
[Logic Channel EQ (Insert 2 - Post-Amp / Post-Comp)]
       ↓
[Aux Send 2: Hitsville Reverb] & [Aux Send 3: Galaxy Tape Echo]
```

---

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed** (direct JFET path for absolute transparency and dynamic range; iD14 Input 1 gain set to **0**; Guitar bus set to **Mono** in Logic Pro).
*   **Physical Guitar Settings:** Set your Framus to the **neck/middle pickup blend** (or pure neck for more throatiness). Roll your guitar volume back to **8** to clean up the input gain and tone back to **7** to take the edge off the swamp ash high-end.

---

### 2. MixWave Two-Rock Bloomfield Drive — boutique character source

The settings utilize **EQ 2** to provide a touch more compression and preamp gain, letting notes compress and sing when dug into, while staying clean on soft fingerpicking.

**Switches and Configuration**

| Control | Setting | Purpose |
|---------|---------|---------|
| EQ Selection | **EQ 2** | More available gain and earlier compression while retaining clean headroom |
| Bright Switch | Off | Keeps the high-end smooth; prevents the swamp ash spank from becoming glassy |
| Mid Switch | Off | Bypassed; the DiMarzio P-90s provide plenty of singing midrange on their own |
| Deep Switch | Off | Avoids low-mid boominess in the resonant swamp ash body |
| Tone Stack Bypass | Off | Keep the EQ knobs active |
| Lead Switch | Off | Clean channel only |
| Tube Select | **6L6** | Big, bold American clean headroom and punchy bass |
| Full/Half Power | **Full (100w)** | Maximum clean headroom and transient response |

**Amp Controls**

| Control | Setting | Purpose |
|---------|---------|---------|
| Gain | 5.5 | Touch-sensitive gain; light picking is clean, hard attack blooms and breaks up slightly |
| Treble | 5.0 | Noon; allows the swamp ash snap to speak naturally |
| Middle | 5.2 | Slight boost to keep the P-90 vocal throatiness centered |
| Bass | 4.5 | Pulled back slightly to control the swamp ash body's resonant low end |
| Presence | 5.5 | Subtle high-frequency air to emulate the Strat-like clarity of "Human Nature" |
| Master | 6.0 | Pushed to drive the power amp stage into natural tube compression |
| Reverb | 0 | Off — Hitsville handles the space |
| Vibe | 4.8 | Slightly reduced to roll off extreme high-frequency harmonics |
| Noise Gate | **0.350** | **CRITICAL:** High-quality gate engaged to block idle P-90 single-coil hum |

**Built-in Overdrive Pedal (The Parallel Boost)**

| Control | Setting | Purpose |
|---------|---------|---------|
| OverdriveOnOff | **On** | Engaged |
| OverdriveOverdrive | **2.2** | Very low gain; acts as a clean boost to extend note sustain |
| OverdriveTone | **5.5** | Slight midrange push to focus the blues lead |
| OverdriveBalance | **6.2** | Boosts the level hitting the preamp |
| OverdriveMix | **4.0 (40%)** | Blends 40% driven signal with 60% clean signal, preserving the snappy pick attack while extending the notes' decay |

**Cabinet and Mic**

| Control | Setting | Purpose |
|---------|---------|---------|
| Cabinet | 2x12 Two-Rock Vertical | Standard vertical cab pairing |
| Mic L (Bottom) | **Ribbon 122** | Royer-style ribbon on-axis; captures warm low-mids and provides a smooth high-frequency roll-off |
| Mic R (Top) | **Dynamic 57** | SM57-style off-axis; captures the biting, throatier upper-mid punch of the P-90s |

---

### 3. UADx LA-2A Silver Compressor — post-amp organic glue (Insert 1)
Placing the compressor *after* the amp model is critical. It acts as a "studio mix compressor" to glue the overall recorded sound of the mic'd amplifier. Placing it before the amp would squash your guitar's direct signal, reducing your control over the touch-sensitive breakup of the amp. Placing it after the amp allows you to dig in for natural amp grit while keeping the overall signal leveled and adding vocal-like sustain.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 35 | Gentle optical smoothing (~2-3 dB of reduction on firm picks) |
| Gain | 28 | Calibrated makeup gain |
| Mode | Compress (3:1) | Slower, musical optical compression |

---

### 4. Logic Channel EQ — post-amp / post-comp corrective shaping (Insert 2)
Placing the EQ at the very end of the insert chain allows you to cleanly roll off subsonic rumble and high-frequency digital fizz / P-90 single-coil buzz generated by both the amp modeler and the compressor.

| Band | Frequency | Setting / Gain | Q | Purpose |
|------|-----------|----------------|---|---------|
| Band 1 (HPF) | 80 Hz | On (18 dB/oct slope) | — | Cleans up subsonic rumble and low-end mud |
| Band 4 (Notch) | 400 Hz | −1.5 dB | 1.0 | Removes slight boxiness from the swamp ash wood resonance |
| Band 8 (LPF) | 6.8 kHz | On (24 dB/oct slope) | — | The "high-cut veil"; rolls off P-90 single-coil buzz and high-frequency digital fizz |

---

### 5. Reverb & Delay Aux Sends — lush space

**Aux 2: UADx Hitsville Reverb Chambers — shared room space**
*   **Logic Send Level (Aux 2):** −12 dB
*   **Bus Fader (Aux 2):** −8 dB

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Present, rich room reflections |
| Speaker | **Bozak 800** | Classic Detroit chamber speaker setup |
| Mic | **Unidyne 545** | Articulate guitar reverb mic |
| Mix | **Wet Solo (100%)** | Aux send configuration |
| Decay | **10:30 (~2.4s)** | Lush, three-dimensional room bloom |
| Pre-Delay | 15 ms | Dynamic separation between pick attack and room response |

**Aux 3: UADx Galaxy Tape Echo (Optional "Human Nature" Wash)**
*   **Logic Send Level (Aux 3):** −18 dB
*   **Bus Fader (Aux 3):** 100% Wet on Bus

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | **5 (Echo Only)** | Tape Heads 1 & 2 active |
| Echo Rate | **420 ms** | Sycned to 1/4 note for rhythmic depth |
| Feedback | **3.5** | Emits 3-4 soft, analog repeats |
| Tape Age | **New** | Keeps the repeats clean and clear |
| Wet Solo | **ON** | Placed on Aux Bus |

---

## Starting Point Guide

- **Physical Pick Dynamics**: The magic of this tone lies in your hands. Pick lightly to let the delay and reverb carry a glassy, ambient bed (like the "Human Nature" verses). Dig in firmly to force the Two-Rock's EQ 2 preamp and the parallel overdrive pedal to compress and "sing" for lead lines.
- **The "Mayer Stack" Overdrive**: If you want more growl, increase the **OverdriveMix** to `5.5 (55%)` or push the **OverdriveOverdrive** (Gain) control to `3.5`. This increases the presence of the overdrive circuit relative to your clean tone.
- **Taming the High-End Chime**: If the bridge pickup is too bright, check that your physical guitar tone knob is rolled back to `7`. You can also lower the Two-Rock **Vibe** control to `4.0` or roll the Logic EQ LPF back to `6.0 kHz`.

---

## Feedback History

### 2026-06-18 — initial
Created to capture a John Mayer-style clean-to-singing-edge tone for the Framus Earl Slick. Uses the Mixwave Two-Rock Bloomfield on EQ 2 with the built-in overdrive engaged at 40% mix for a parallel clean boost. Placed UADx LA-2A Silver and Logic EQ post-amp in the inserts chain to ensure transparent picking dynamics and corrective cleanup of P-90 hum. Added a UADx Galaxy Tape Echo bus alongside Hitsville Reverb to replicate the lush live ambiance of "Human Nature."
