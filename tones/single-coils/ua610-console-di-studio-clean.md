---
id: ua610-console-di-studio-clean
preset_name: "UA 610 Console DI — 80s Studio Clean"
created: 2026-08-08
updated: 2026-08-08
guitar: Squier Stratocaster / Fender Player II Telecaster (Single-Coils — Middle + Bridge "Quack" or Neck position)
target: Pristine 80s direct-to-console studio clean tone (Nile Rodgers, Gilmour Floyd DI solo, 80s LA session style) using a UA 610 tube preamp, FET compression, and Dimension D stereo chorus without a guitar amp or speaker cabinet.
tags: 80s, console-di, direct-input, funk, clean, pristine, chorus, studio, single-coil, ua610
tone-king-channel: bypassed
amp: UA 610-B Tube Preamp (Console Direct DI)
status: initial
pickup_type: single-coil
preset_data:
  amp_platform: none
  amp_settings:
    Input_Select: "Line"
    Input_Gain: 0.0
    Level: 6.0
    LO_Shelf_Freq: 100
    LO_Shelf_Gain: -1.5
    HI_Shelf_Freq: 7000
    HI_Shelf_Gain: 1.5
    Output: -2.0
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 24.0}
    band7: {on: true, freq: 10000.0, slope: 12.0}
  logic_compressor:
    threshold: -18.0
    ratio: 4.0
    attack: 25.0
    release: 60.0
    makeup_gain: 0.0
    knee: 0.7
---

# UA 610 Console DI — 80s Studio Clean

## Target Sound
Pristine, hyper-articulate direct-to-console studio clean tone modeled after iconic 80s "desk direct" production techniques (Nile Rodgers "Chucking" rhythm, David Gilmour's crushed 1176 direct solo on *Another Brick in the Wall Pt 2*, and 80s LA session guitarists). Bypassing the guitar amplifier and speaker cabinet entirely reveals an extended high-frequency response, glass-like pick transients, and zero low-end speaker mud. Warmth and depth are supplied by tube saturation in the UA 610-B preamp, fast peak control via FET/opto compression, and spatial 3D widening via the Studio D Chorus.

## Signal Chain

### 1. Physical Interface Input — Direct Injection (DI)

| Control | Setting | Purpose |
|---------|---------|---------|
| Hardware Path | Direct into Audient iD14 (Input 1) | Cleanest, uncolored path; Tone King Imperial Preamp bypassed |
| iD14 Input Gain | Minimum (Unity / 0 dB) | Peaks at −18 dBFS in Logic |
| DAW Calibration Trim | −3.2 dB | Corrects iD14 +9.0 dBu clip level to match UAD +12.2 dBu standard |

### 2. UA 610-B Preamp and EQ — Console Channel Strip

| Control | Setting | Purpose |
|---------|---------|---------|
| Input Select | Line | Standard line-level tube gain stage for clean studio headroom |
| Input Gain | 0 dB | Neutral first-stage tube gain |
| Mic Impedance | 2K Ω | Smooth, open input impedance response |
| Level ("Big Knob") | 6.0 | Drives output tube stage into gentle, harmonic warmth |
| LO Shelf Freq | 100 Hz | Targets low-frequency sub rumble |
| LO Shelf Gain | −1.5 dB | Cleans up low-end build-up without thinning the core tone |
| HI Shelf Freq | 7 kHz | Targets air and presence zone |
| HI Shelf Gain | +1.5 dB | Adds signature 80s console high-frequency "glass" sheen |
| Output | −2.0 dB | Clean post-tube trim to normalize DAW track output level |

### 3. UADx 1176 Classic FET Compressor — Peak & Dynamic Control

| Control | Setting | Purpose |
|---------|---------|---------|
| Ratio | 4:1 | Gentle peak control and leveling |
| Input | 30.0 | Set for 3–5 dB of peak gain reduction on hard strums |
| Output | 24.0 | Unity makeup gain |
| Attack | 3 o'clock (Fast/Medium) | Allows initial pick attack to snap through before compressing |
| Release | 5 o'clock (Fast) | Fast recovery between percussive rhythm hits |
| Meter | GR | Monitors gain reduction |

### 4. Logic Channel EQ — Bandwidth Shaping

| Band | Frequency | Gain / Slope | Purpose |
|------|-----------|--------------|---------|
| Band 1 (HPF) | 80 Hz | 24 dB/oct | Eliminates sub-audible thumps |
| Band 7 (LPF) | 10.0 kHz | 12 dB/oct | Gently tames harsh digital spatter while preserving desk air |

### 5. Spatial & Depth (Bus Sends)

| Bus | Plugin | Setting | Purpose |
|-----|--------|---------|---------|
| Aux 1 (Send −14 dB) | UADx Studio D Chorus | Mode 2 or 3 (100% Wet) | Roland Dimension D spatial widening without obvious pitch modulation |
| Aux 2 (Send −18 dB) | UADx Hitsville Reverb Chambers | Decay 1.5s, Pre-delay 20ms | Natural studio chamber ambience for physical space |

---

## Starting Point Guide

- **First adjustment**: Adjust the **UA 610 Level knob** between 5.0 (pristine/hi-fi) and 7.5 (rich tube saturation).
- **Key interaction**: The 1176 Attack setting dictates your pick transient: turn counter-clockwise toward 12 o'clock for more transient "pop" on funk chords, or clockwise for a smoother, rounded attack.
- **Variations**:
  - *Nile Rodgers Funk*: Roll back guitar Tone knob to 7, set 1176 ratio to 4:1, and engage Studio D Chorus Mode 2.
  - *Gilmour DI Lead*: Swap 1176 for UADx LA-2A (Peak Reduction ~35), add 300ms tape delay on Send Bus 3, and bump 610 HI Shelf to 4.5 kHz (+3 dB).

---

## Feedback History

### 2026-08-08 — initial
Created straight-to-console DI toneprint exploring amp-less studio production techniques with UA 610-B tube preamp, 1176 FET compression, and Studio D Chorus.
