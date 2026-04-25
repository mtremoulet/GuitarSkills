# Vibe Analog Machines — UADx

Source: https://help.uaudio.com/hc/en-us/articles/25190283956500-Vibe-Analog-Machines-Manual

**Note**: The plugin was renamed from "Verve Analog Machines" to "Vibe Analog Machines." The plugin_index_with_manuals.csv may still list it as "Verve."

---

## Overview

Tape and solid-state saturation/coloration plugin. Two versions available:

- **Full version**: 10 machines (6 tape + 4 solid state), controls: Drive + Tone/Warble + Output trim
- **Essentials**: 4 tape machines, control: Drive only

Target use cases: hip-hop, lo-fi, electronic, rock, experimental. Gain-compensated Drive control.

---

## Controls

### Drive
Adjusts overdrive and distortion amount. **Gain-compensated** — level stays consistent as Drive increases.

### Tone (solid state machines only)
EQ character adjustment for solid state machines.

### Warble (tape machines only)
Amount of tape-style modulation (wow/flutter). Applies to tape machines.

### Output Level Trim
Output level adjustment: **±12 dB**. Full version only. **Global** — not retained per-machine (all other controls are retained per-machine when switching).

---

## Machines

Drive, tone, and warble settings are **retained per machine** when switching. Output level is global.

**Warning**: Automating drive/tone/warble then switching machines can produce unpredictable results — parameter ranges behave very differently per machine.

### Tape Machines (all use Warble control)

| Machine | Character |
|---------|-----------|
| **Sweeten** | Studio tape gloss and warmth, gently overdriven. Essentials. |
| **Warm** | Vintage studio tape character. Essentials. |
| **Thicken** | Sounds like a 50-year-old recording. Essentials. |
| **Vintagize** | Lo-fi, older than your grandparents. Essentials. |
| **Overdrive** | Vintage tape machine pushed to its limits. Full version only. |
| **Fire** | Studio tape in extreme distortion. Full version only. |

### Solid State Machines (all use Tone control, full version only)

| Machine | Character |
|---------|-----------|
| **Edge** | Subtle crunch from gentle harmonics. |
| **Glow** | Subtle warmth from gentle harmonics. |
| **Distort** | Vintage tube preamp into heavy roar. |
| **Sputter** | Transistor preamp on the verge of blowing up. |

---

## Notes for Guitar Use

- **Sweeten / Warm** at low Drive: adds gentle tape color and body without audible saturation — useful after amp sims to add analog feel to an otherwise clean-sounding chain.
- **Overdrive / Fire** at higher Drive: tape machine saturation as an additional coloring layer on top of amp sim breakup.
- **Edge / Glow** (solid state): harmonic enhancement without pitch or time modulation — cleaner alternative to tape warble for tightening a guitar tone.
- **Warble on tape machines**: can add vintage tape wobble to delays or reverb returns for a more organic feel.
- Output trim useful for gain-staging when drive is pushed hard.
