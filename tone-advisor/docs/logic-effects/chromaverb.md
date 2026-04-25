# ChromaVerb — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 17835–18270

Add via: Reverb > ChromaVerb in a channel strip Audio Effect plug-in menu.

---

## Overview

ChromaVerb features 14 discrete room type algorithms. Based on circular sound absorption principle — sound is gradually absorbed like in a real room. Each room type offers a unique tonal color, from dense rooms to wide spaces and large halls.

---

## Interface

Two views, switched with Main/Details buttons at upper right:
- **Main view**: Common reverb parameters (Attack, Size, Density, Distance, Decay) + Damping EQ graphic display
- **Details view**: Advanced parameters (Width, Quality, Modulation) + Output EQ graphic display

---

## Main View Parameters

- **Room Type pop-up menu**: Choose the reverb space algorithm (see room types below)
- **Attack knob and field**: Attack phase of the reverb.
  - Increases volume over time for: Theatre, Dense Room, Smooth Space, Reflective Hall, Strange Room, Airy
  - Sets time to reach maximum density (set by Density knob) for: Room, Chamber, Concert Hall, Synth Hall, Digital, Dark Room, Vocal Hall, Bloomy
- **Size knob and field**: Dimensions of the room. Higher = larger space.
- **Density knob and field**: Density of early and late reflections simultaneously. Behavior depends on room type.
- **Predelay field**: Time between start of original signal and arrival of early reflections.
  - Short predelay: pushes sounds away
  - Longer predelay: brings sounds more to the forefront
  - Too short: can color sound and obscure source position
  - Too long: perceived as unnatural echo, audible gap between original and reflections
  - Good method: use longest possible Predelay before hearing side effects, then reduce slightly
  - Percussive signals generally need shorter predelays; signals with gradual attacks can use longer
- **Predelay sync button**: Restrict Predelay values to tempo-synchronized divisions
- **Decay knob and field**: Decay time. Decay for certain frequencies depends on Damping EQ settings.
- **Decay sync button**: Restrict Decay values to tempo-synchronized divisions
- **Freeze button**: Recirculate signal infinitely inside the chosen room type
- **Distance knob and field**: Perceived distance from the source by altering early and late energy
- **Dry/Wet sliders and fields**: Independently set levels of source and effect signals

---

## Damping EQ (shown in Main view graphic display)

4-band EQ that adjusts the decay frequencies:
- **Low shelving EQ** (band 1)
- **Low parametric EQ** (band 2)
- **High parametric EQ** (band 3)
- **High shelving EQ** (band 4)

Edit by dragging EQ dots in the display. For each band:
- Drag horizontally → adjust frequency
- Drag vertically → adjust ratio (how much this frequency's decay is affected)
- Option-Command drag vertically → change Q value
- Option-click → reset to defaults

Parameters: **Frequency field**, **Ratio field** (Decay timing ratio), **Q field** (band width)

---

## Details View Parameters

- **Quality pop-up menu**: Low (grainy, noisy modulation), High (clean and precise), Ultra (smooth, expensive-sounding)
- **Mod Speed slider and field**: Speed of built-in LFO
- **Mod Depth slider and field**: Depth of LFO modulation. Range determined by chosen room type.
- **Mod Source buttons**: Choose sine, random, or noise waveform for LFO
- **Smoothing slider and field**: Changes LFO waveform shape. Random waveform is smoothed; sine and noise waveforms are saturated.
- **Early/Late Mix slider and field**: Level of early vs. late reflections (varies with Distance parameter)
- **Width slider and field**: Stereo width of the reverb
- **Mono Maker on/off button**: Remove stereo information below the frequency set by corresponding slider
- **Mono Maker slider and field**: Frequency below which stereo information is removed. Compensates for perceived level losses in the low frequency range.

---

## Output EQ (shown in Details view)

6-band EQ shaping the combined reverb + source output signal.

| Band | Type | Color |
|------|------|-------|
| 1 | High pass filter | Red |
| 2 | Low shelving filter | Orange |
| 3 | Low parametric | Green |
| 4 | High parametric | Blue |
| 5 | High shelving filter | Purple |
| 6 | Low pass filter | Pink |

- **Output EQ on/off button**: Enable/disable the Output EQ
- Each band: Frequency field, Gain field (bands 2–5), Order field (bands 1 and 6 — filter slope), Q field

---

## Room Types

| Room Type | Character |
|-----------|-----------|
| **Room** | Natural-sounding; rapid build-up of dense reflections |
| **Chamber** | Punchy; small to medium room; fast attack, high echo density, low coloration |
| **Concert Hall** | Large space; long delays in initial sound; slow build; minimal high-end; moderate diffusion |
| **Theater** | Medium to large dry room; medium reflection density |
| **Synth Hall** | Wider than Room; sparsest reflections of all room types |
| **Digital** | Medium room; midrange reflection density; slower attack than Room; brighter decay, lush chorus-like; dense tail with extended high and low response |
| **Dark Room** | Small to medium; dark sounding; less dense |
| **Dense Room** | Small room; dense reflection pattern that builds very quickly |
| **Smooth Space** | Smooth; medium size space |
| **Vocal Hall** | Medium to large; smooth; midrange number of reflections |
| **Reflective Hall** | Medium to large; highly reflective; low reflection density |
| **Airy** | Large space; sparse reflections |
| **FX - Strange Room** | Medium space; midrange reflection density; distinct color |
| **FX - Bloomy** | Large space; moderate reflection density; blooming decays |

---

## Notes for Guitar Use

- For guitar reverb, **Room** and **Chamber** types tend to provide the most natural amp-in-a-room feel
- **Decay** + **Damping EQ** interact: rolling off high frequencies in the Damping EQ creates a reverb that darkens over time, simulating a real room
- **Predelay** (15–30 ms) is very effective for preserving guitar pick attack before the reverb kicks in
- **Dry/Wet** uses independent sliders — can set Dry to 0 dB and Wet to taste without affecting dry signal level
- If Tone King reverb is active, do not add ChromaVerb (avoid double-reverb stacking unless intentional)
