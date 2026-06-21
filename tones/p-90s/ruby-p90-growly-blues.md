---
id: "ruby-p90-growly-blues"
preset_name: "Ruby P-90 Growly Blues"
created: "2026-06-01"
updated: "2026-06-01"
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s)"
target: "Raw, woody, mid-forward growly blues with a classic Germanium treble-booster bite; optimized for dynamic P-90 pickups."
tags: "vox, ac30, ruby-63, framus, p-90, edge-of-breakup, overdrive, blues, blues-rock, growly, germanium"
tone-king-channel: "bypassed"
amp: "Ruby '63"
status: "tested"
pickup_type: "p-90"
preset_data:
  amp_platform: "uad_paradise"
  amp_settings:
    Channel: "Normal"
    Volume: 5.5
    Boost: 4.0
    Boost Switch: "ON"
    Cut: "OFF"
    Treble: 5.0
    Bass: 5.0
    Tone Cut: 6.5
    Cabinet: "Green"
    Room: 5.0
  la2a:
    peak_reduction: 35.0
    gain: 15.0
    compress: true
  logic_eq:
    band1:
      on: true
      freq: 85.0
      slope: 12.0
    band8:
      on: true
      freq: 5500.0
      slope: 12.0
  galaxy:
    head_select: 1
    echo_rate: 4.0
    feedback: 1.5
    echo_volume: 5.0
    reverb_volume: 0.0
    tape_age: "Used"
---

# Ruby P-90 Growly Blues

## Target Sound

This toneprint is designed specifically to capture the raw, tactile, and woody midrange "growl" of your **Framus Earl Slick Artist Series** (loaded with DiMarzio P-90s) interacting with the **UADx Ruby '63** (Vox AC30). 

Unlike humbuckers, P-90s are single-coils at heart, but with a wider coil that provides a dense, snarling midrange and an aggressive, snapping transient response. To unlock their full potential, this toneprint uses the Ruby's **Normal channel**—which bypasses the Top Boost's interactive EQ completely, resulting in a flatter, wider, and throatier mid-range. We couple this with the built-in **Germanium Treble Booster** at a moderate setting to tighten the low-end mud *before* it hits the preamp and push a vocal, biting upper-mid edge into the virtual tubes. 

To round off any harsh high-end single-coil "fizz," we route through the **Green cabinet** (mic'd with a classic G12H and an M160 ribbon mic), which tames top-end transients and highlights a thick, organic midrange. The result is a highly tactile, "woolly" blues-rock grit that responds beautifully to your picking dynamics on the Sennheiser HD660S2 headphones.

---

## Signal Chain

```
[Framus P-90] → [Audient iD14 (JFET DI)] → [LA-2A Silver Comp] → [Ruby '63 (Normal + Germanium)] → [2x12 Green Cab] → [Post-EQ] → [Aux Spatial Buses]
```

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

To get the pure, dynamic midrange interaction of your P-90s and the AC30, plug your guitar straight into the high-headroom JFET Instrument Input (DI) of the Audient iD14, bypassing the physical pedal chain.

| Component / Setting | Target Level / Option | Purpose |
|---------|---------|---------|
| **Guitar Input** | JFET Instrument Input (DI) | Discretely voiced JFET stage adds subtle harmonic warmth, acting like a classic tube DI front-end |
| **Preamp Gain** | Set to target peaks around −18 dBFS | Bypasses physical color. Provides the pure, uncolored dynamic output of the P-90s to the DAW |
| **Tone King Imperial** | **Bypassed** | Preserves the natural, snarling P-90 midrange rather than pre-scooping it |
| **TONEX One** | **Bypassed** | Bypassed — transparent signal path starting at the interface DI |

---

### 2. UADx LA-2A Silver Compressor — dynamic smoothing

P-90s are incredibly dynamic and tactile. The Silver variant has a slightly slower, more musical/blooming response than the Gray, which works beautifully to catch hard picking peaks without flattening your raw dynamics.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Compress | Gentle 3:1 optical compression ratio |
| Peak Reduction | 35 | Target 2–3 dB of gain reduction on hard strums. Smooths out extreme transient peaks while preserving raw tactile feel. |
| Gain | 15 | Makeup gain dialed back to preserve perfect headroom into the hot virtual amp |

---

### 3. UADx Ruby '63 Normal Channel — throatier mids & germanium bite

The Normal channel is a classic secret weapon for P-90s. With only the Tone Cut active for EQ, we let the raw midrange of the guitar shine, and push it into thick power-amp sag.

| Control | Setting | Purpose |
|---------|---------|---------|
| **IN (Input Trim)** | **−4 dB to −6 dB** | Preamp input trim. **CRITICAL for P-90s** — tames the hot input level to prevent overloading the virtual tubes up front and reduces touch-sensitivity of controls. |
| **Channel** | **Normal** | Bypasses Top Boost EQ. Offers a wider, throating mid-range response with great headroom. |
| **Volume** | **5.5** | Pushed hard into the power amp sweet spot for natural power-tube grit and rich harmonic sag |
| **Boost Switch** | **ON** | Engages the Germanium Treble Booster model |
| **Boost Control** | **4.0** | Germanium boost pushes a gorgeous, vocal upper-mid bite into the preamp, cutting through low-end mud. |
| **Cut Switch** | **OFF** | Bypassed — the Germanium boost naturally cuts sub-bass, so the Cut switch isn't needed. |
| **Treble** | *Inactive* | No effect on the Normal channel. |
| **Bass** | *Inactive* | No effect on the Normal channel. |
| **Tone Cut** | **6.5** | *Inverse control (clockwise = cut)*. Set to 6.5 to roll off high-end single-coil "fizz," keeping your headphones smooth. |
| **Cabinet** | **Green** | Modern 2x12 Celestion G12Hs mic'd with a Beyerdynamic M160 ribbon. The ribbon naturally tames high-end sizzle and highlights a thick, organic midrange. |
| **Room** | **5.0** | Noon setting creates a beautiful, dimensional room environment on headphones |

---

### 4. Post-FX surgical EQ (Logic Channel EQ)

A safety net to clean up room frequencies and polish the high-end.

* **High-Pass Filter (Band 1)**: 85 Hz (12 dB/octave) to remove unnecessary low-end rumble.
* **Low-Pass Filter (Band 8)**: 5.5 kHz (smooth 12 dB/octave slope) to act as a gentle "electronic veil," smoothing out top-end single-coil transients and highlighting woody resonance.

---

### 5. Spatial Effects — Bus-First Aux Routing

To maintain maximum clarity and prevent the raw P-90 bite from getting "smeared," all spatial effects are run on parallel buses.

#### Bus 3 (Reverb): Logic ChromaVerb (100% Wet)
* **Room Type**: Dark Room (adds an intimate, warm, vintage live-room character).
* **Decay Time**: 1.2 seconds (slightly shorter decay for a tighter, raw feel).
* **Logic Send Level**: `-16 dB` (adjust to taste for depth).

#### Bus 4 (Delay): UADx Galaxy Tape Echo (100% Wet)
* **Head Select**: 1 (focused single repeat).
* **Echo Rate**: 4 (~180ms; a tight, slap-adjacent tape echo).
* **Feedback**: 1.5 (1 to 2 warm, decaying tape repeats).
* **Tape Age**: Used (adds gentle wow/flutter and rolls off highs on the repeats).
* **Logic Send Level**: `-20 dB` (very subtle slap back to add depth without cluttering the raw tone).

---

## Starting Point Guide

- **First adjustment**: If the tone feels a bit thin or too bright, **lower the Germanium Boost control** from `4.0` down to `2.0` or `1.5`. The Germanium booster is a *treble booster* and cuts low end aggressively; dropping it restores your natural P-90 bottom-end warmth and woodiness.
- **Input Trim & Knob Sensitivity**: Set the Ruby's **IN (Input Trim)** knob to between **−4 dB and −6 dB**. The Ruby is extremely sensitive to knob placement; padding the input stage lets you dial in the volume and booster sweet spots with much greater precision without blowing out the front end.
- **Taming the "Top Boost" / Tone Cut**: Because the AC30 has a prominent high-end chime, roll the **Tone Cut** clockwise to **7.0 or 7.5** to darken the power amp and bring back the fat, warm bottom-end throatiness of your P-90s.
- **Key interaction**: Pick lightly for a woody, clean-ish edge-of-breakup tone; dig in aggressively to trigger the Germanium compression and hear the midrange bark!
- **Variations**: For a tighter, more modern Matchless-style blues-rock bark, switch the cabinet to **Match**.

---

## Feedback History

### 2026-06-01 — tested
Tested and verified in a session with the Framus Earl Slick (DiMarzio P-90s, guitar knobs at 7/7). Levels are confirmed and gain staging is completely dialed. Because UADx runs hot, the LA-2A Silver makeup gain was dialed way back to 15 (from 38) and Peak Reduction raised to 35 to catch transients smoothly.

Logged key session refinement notes:
1. Set the **Ruby IN (Input Trim)** to **−4 dB to −6 dB** to prevent overloading the virtual tubes up front and reduce the high sensitivity of the controls.
2. Dialed back the Germanium treble boost to restore the P-90's warm bottom end, and rolled the **Tone Cut** clockwise to tame the top-end chime.

Session metering baseline:
- Raw JFET Input: −12.5 dBFS
- Guitar Bus Out (LA-2A + Ruby '63): −5.8 dBFS
- ChromaVerb (Dark Room) Return (Bus 3): −18.0 dBFS
- Galaxy Tape Echo Return (Bus 4): −26.0 dBFS
- Master Stereo Out: −5.6 dBFS (ideal headroom of ~6 dB)

### 2026-06-01 — initial
Created specifically for the Framus Earl Slick Artist Series (DiMarzio P-90s) to capture a raw, growly, mid-forward blues-rock tone. Runs directly into the Audient iD14's JFET DI. Leverages the Normal channel (Volume 5.5) pushed by the Germanium Treble Booster (4.0) and running into the G12H/M160 Green ribbon-mic cab. Smooths the single-coil snap with an LA-2A Silver compressor, a 5.5 kHz high-cut veil, and a tight Bus 3/Bus 4 parallel space.
