---
id: "ruby-hb-velvet-blues"
preset_name: "Ruby LP Velvet Blues HB"
created: "2026-06-01"
updated: 2026-07-12
guitar: "Gibson Les Paul Studio / Epiphone Les Paul Standard"
target: 'Warm, vocal Class A overdrive with smooth tape compression; optimized for expressive humbucker blues-rock leads.'
tags: "vox, ac30, ruby-63, les-paul, humbucker, edge-of-breakup, overdrive, blues, blues-rock, velvet"
tone-king-channel: "bypassed"
amp: "Ruby '63 (UADx)"
status: "refined"
pickup_type: "humbucker"
preset_data:
  amp_platform: "uad_paradise"
  gold_overdrive:
    enabled: true
    gain: 0.0
    output: 7.5
    treble: 4.5
  amp_settings:
    Channel: "Brilliant"
    Volume: 4.8
    Boost: 3.0
    Boost Switch: "ON"
    Cut: "ON"
    Treble: 5.0
    Bass: 5.2
    Tone Cut: 6.4
    Cabinet: "Green"
    Room: 4.5
  red_comp:
    enabled: true
    output: 1.0
    mix: 80.0
    sensitivity: 2.5
  logic_eq:
    band1:
      on: true
      freq: 80.0
      slope: 12.0
    band8:
      on: true
      freq: 6000.0
      slope: 12.0
  galaxy:
    head_select: 1
    echo_rate: 5.0
    feedback: 2.0
    echo_volume: 5.0
    reverb_volume: 0.0
    tape_age: "Used"
---

# Ruby LP Velvet Blues HB

## Target Sound

This toneprint is designed to find the absolute "sweet spot" for a dual-humbucker guitar (like your **Epiphone Les Paul Standard** or **Gibson Les Paul Studio**) running into the **UADx Ruby '63** (Vox AC30). Instead of the bright, jangly, classic-rock chime, this chain is dialed for a warm, vocal, and compressed **Velvet Blues-Rock overdrive**. 

By leveraging the **Brilliant channel** with a low-gain **EP-III tape echo preamp boost**, we smooth out the sharp high-mid spikes of the Top Boost circuit, resulting in a thick, singing overdrive. To accommodate the thick Alnico humbuckers, we engage the **Cut switch** to roll off muddy sub-bass before the preamp, and turn the **Tone Cut** clockwise to act as a gentle "electronic veil" for high-frequency transients. The result is a smooth, liquid sustain that is highly expressive, touch-sensitive, and perfectly tuned for headphone monitoring on your Sennheiser HD660S2.

> [!TIP]
> **The Midrange Purist Approach:**
> Plugging your guitar **directly into the Audient iD14's JFET DI input (bypassing the Tone King entirely)** is the core foundation of this toneprint. The JFET stage adds a subtle, tube-like warmth, while bypassing the Tone King prevents pre-scooping the natural vocal midrange of your humbuckers. This allows the raw, wood-flavored impedance to interact directly and dynamically with the Ruby's EL84 virtual tubes.

---

## Signal Chain

```
[Les Paul] → [Audient iD14 (JFET DI)] → [Red Comp (PGS Pre-FX 5)] → [Ruby '63 (Brilliant)] → [2x12 Silver Cab] → [Post-EQ] → [Aux Spatial Buses]
```

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

To get the pure, dynamic midrange interaction of your humbuckers and the AC30, plug your guitar straight into the JFET Instrument Input (DI) of the Audient iD14, bypassing the physical pedal chain.

| Component / Setting | Target Level / Option | Purpose |
|---------|---------|---------|
| **Guitar Input** | JFET Instrument Input (DI) | Discretely voiced JFET stage adds subtle harmonic warmth, acting like a classic tube DI front-end |
| **Preamp Gain** | Set to target peaks around −18 dBFS | Bypasses physical color. Provides the pure, uncolored dynamic output of the humbuckers to the DAW |
| **Tone King Imperial** | **Bypassed** | Preserves the natural humbucker midrange rather than pre-scooping it |
| **TONEX One** | **Bypassed** | Bypassed — transparent signal path starting at the interface DI |


### 2. Pre-FX: Red Comp Compressor (Paradise Guitar Studio) — dynamic smoothing

Placed in the final pre-FX slot (Slot 5) of Paradise Guitar Studio to tame humbucker transients and add singing sustain. It runs parallel with a mix of 80% to keep a little dry signal in and maintain picking dynamics.

| Control | Setting | Purpose |
|---------|---------|---------|
| Output | 1.0 | Low output to prevent immediately pushing the amp into harsh clipping |
| Sensitivity | 2.5 | Fairly low sensitivity for a natural, dynamic compression response |
| Mix | 80% | Parallel compression: retains 20% dry transient detail |

---

### 3. Pre-FX Option: Gold Overdrive

Loaded in pre-FX Slot 1. Enabled by default for a bit of clean boost/sustain.

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost |
| State | **Enabled** (On) | Can be bypassed if a completely clean response is desired |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 3. UADx Ruby '63 Brilliant Channel — chime & velvet overdrive

The Brilliant channel engages the classic '63 Top Boost preamp. We balance this hot channel with a low boost setting to add smooth tape saturation.

| Control | Setting | Purpose |
|---------|---------|---------|
| **Channel** | **Brilliant** | Engages the Top Boost preamp circuit, providing high-mid definition |
| **Volume** | **4.8** | Humbucker sweet spot: warm, compressed, singing overdrive that cleans up with a lighter touch |
| **Boost Switch** | **ON** | Engages the EP-III Tape Echo preamp model |
| **Boost Control** | **3.0** | Adds a smooth, warm tape saturation that rounds out humbucker transients |
| **Cut Switch** | **ON** | Low-frequency cut. **CRITICAL for humbuckers** — filters out flubby bass before the preamp to prevent mud. |
| **Top Boost Treble** | **5.0** | *Inverse control (clockwise = cut)*. Counterclockwise boost set to 5.0 to tame high-end spikes. |
| **Top Boost Bass** | **5.2** | *Inverse control (clockwise = cut)*. Set to 5.2 to subtly roll off low-end mud under high-output strumming. |
| **Tone Cut** | **6.4** | *Inverse control (clockwise = cut)*. Set to 6.4 to roll off digital "fizz" and soften transients on your HD660S2 headphones. |
| **Cabinet** | **Green** | Modern 2x12 Celestion G12H speakers, mic'd with M160 ribbon. Tames Vox high-end harshness, adds midrange warmth, and thickens the tone. |
| **Room** | **4.5** | Adds a natural acoustic room reflection, essential for a premium headphone experience |

---

### 4. Post-FX surgical EQ (Logic Channel EQ)

A safety net to clean up room frequencies and polish the high-end.

* **High-Pass Filter (Band 1)**: 80 Hz (12 dB/octave) to remove unnecessary low-end rumble.
* **Low-Pass Filter (Band 8)**: 6.0 kHz (smooth 12 dB/octave slope) to act as a gentle "electronic veil," smoothing out top-end transients and creating a cohesive, organic texture.

---

### 5. Spatial Effects — Bus-First Aux Routing

To maintain maximum clarity and prevent the Les Paul's thick midrange from getting "smeared" or muddy, all spatial effects are run on parallel buses.

#### Bus 3 (Reverb): Logic ChromaVerb (100% Wet)
* **Room Type**: Chamber or Dark Room (adds a lush, reflective, vintage room character).
* **Decay Time**: 1.4 seconds.
* **Logic Send Level**: `-15 dB` (adjust to taste for depth).

#### Bus 4 (Delay): UADx Galaxy Tape Echo (100% Wet)
* **Head Select**: 1 (focused single repeat).
* **Echo Rate**: 5 (~220ms; a subtle slap/room delay).
* **Feedback**: 2.0 (2 to 3 quiet, warm tape repeats).
* **Tape Age**: Used (adds gentle wow/flutter and high-end roll-off to the repeats).
* **Logic Send Level**: `-18 dB` (sits quietly in the background as an ambient pillow).

---

## Starting Point Guide

- **First adjustment**: If the tone feels a bit too dark or muffled, roll the **Tone Cut** counterclockwise (e.g., to **5.5**) to open up the high-mids, or lower the **Boost control** to **2.0**.
- **Key interaction**: Set your physical **Guitar Volume to 7** and **Tone to 7** on the neck pickup. This takes the high-output "edge" off the humbuckers, expanding the clean headroom and bringing out a glassy, woody quality. Roll it up to 10 for thick, creamy, singing leads.
- **Variations**: For a brighter, more classic rock "jangle" crunch, switch the cabinet to **Silver**, **Blue**, or **Blue Mod**.

---

## Feedback History

### 2026-06-01 — initial
Created specifically for the Gibson/Epiphone Les Paul Standard to find the bluesy "sweet spot" on the Ruby's Brilliant channel. Uses the JFET DI input directly. Blends a gentle LA-2A Gray Compressor, a low EP-III tape boost (3.0), and a smooth 2x12 Silver cabinet to create a creamy, singing velvet overdrive that cleans up beautifully by rolling back the guitar's volume. Optimized for the Sennheiser HD660S2 headphones.

### 2026-07-12 — refined
Refined the toneprint based on testing. The previous standalone LA-2A placement before the amp was very loud and required an unusually high Peak Reduction (77) and very low Gain (19) to tame the picking attack without immediate harsh breakup. Switched to the built-in Red Comp compressor pedal inside Paradise Guitar Studio (placed in the final pre-FX slot 5). Dialed with low output (1.0) and sensitivity (2.5) at an 80% mix to keep dry dynamics. Enabled the Gold Overdrive in Slot 1 for a clean boost. To address the Ruby's brightness, swapped the speaker cabinet from Silver to Green (Celestion G12Hs mic'd with an M160 ribbon microphone), rolled Treble back to 5.0, and dialed the Tone Cut to 6.4. This creates a much warmer, vocal overdrive that is smoother on headphones.
