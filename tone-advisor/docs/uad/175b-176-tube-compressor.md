# UA 175-B & 176 Tube Compressor Collection — UADx

Source: https://help.uaudio.com/hc/en-us/articles/15707665525780

---

## Overview

Two plugins based on UA's 1960s tube compressor/limiter hardware — among the first compressors purpose-built for studio recording. Prized for tube gain reduction character, harmonic saturation, and tonal coloring. Used with or without compression (Attack = OFF bypasses compression but retains tube coloring).

**UADx names**: 175-B Compressor, 176 Compressor. **UAD-2 names**: UA 175-B, UA 176.

---

## 175-B vs 176 Differences

| Feature | 175-B | 176 |
|---------|-------|-----|
| **Ratio** | Fixed 12:1 (limiter behavior) | 2:1, 4:1, 8:1, 12:1 (switchable) |
| **Gain switch** | Low/High (+10 dB in High) | Not present |
| **Balance default** | -7.0 | -6.0 |

The 175-B's 12:1 fixed ratio gives a sharper knee — behaves more as a limiter. The 176's lower ratios provide gentler compression curves. At 12:1, both sound similar.

---

## Controls

### Gain (175-B only)
Two-position rotary: **Low / High**. High = +10 dB input gain. On the hardware, this is an internal jumper; the plug-in exposes it on the front panel.

### Ratio (176 only)
Compression ratio: **2:1, 4:1, 8:1, 12:1**. Lower ratios = gentler knee and more natural compression. 12:1 = peak limiting behavior.

### Input
Simultaneously controls: input gain, compression threshold, and gain reduction amount. **Rotate clockwise to increase compression.** Stepped control (2 dB increments by default). Knob is calibrated to 2 dB values.

The feedback compression circuit means: softer compression at lower input levels, harder/brickwall limiting as levels increase.

### Output
Final output level of the plug-in. Does not affect compression amount. Stepped control (2 dB increments by default). Use to make up gain lost from gain reduction.

### Vernier
Changes Input and Output behavior:
- **Left (default)**: Stepped mode — 2 dB increments
- **Right**: Continuous mode — full range of fine adjustment

### Attack
Time for compressor to begin gain reduction. Range: **100 µs to 1000 µs** (all extremely fast). Continuous.

- Fast attack = catches transients, softens the sound
- Slower attack = lets transients pass before compression

**Attack OFF position**: Bypasses compression circuit entirely. Input/output tube amplifiers remain active — use for tonal coloring/saturation without dynamics processing. Click the "OFF" text label to engage (to prevent accidental activation).

**Grit technique**: Attack and Release both at fastest settings — compression distortion from rapid level fluctuations. Adds gritty saturation. Works well on bass and lead vocals.

### Release
Time to return to pre-gain-reduction level. Range: **27 ms to 527 ms**. Continuous. Actual times may vary with program material.

- Fast release: pumping/breathing artifacts, compression distortion
- Slow release: gain reduction persists through quiet sections

### Sidechain Link (S.C. Link)
When **UP (engaged)**: Stereo signals compressed equally in both channels — prevents stereo panorama shift. When **down**: Independent L/R gain reduction.

### VU Meter
Displays Input, Output, or GR (gain reduction). Switch selects mode. GR = gain reduction in dB. Input/Output metering is relative, not calibrated.

### Headroom (H.R.)
Adjusts internal operating reference level. **Counter-clockwise = more headroom** (signals pushed higher before compression starts). **Clockwise = less headroom** (more gain reduction and harmonic color at lower signal levels). Use for operating level matching or creative expansion of sonic range.

### Balance (BAL.)
Set-screw control. Adjusts amalgam of plate and cathode bias current trims from original hardware. Changes the "thump" (additive signal deflection) on signal attacks. Default: 175-B = -7.0, 176 = -6.0. Leave at default unless intentionally tuning the compression character.

### Mix
Parallel compression blend. **0% = dry only. 100% (default) = wet only. 50% = equal blend.** Phase-accurate throughout range. Eliminates need for separate parallel compression routing in the DAW.

### Power
Bypass switch. Down = processing disabled, DSP reduced.

---

## Key Character Notes

- Input and Output controls may yield different levels at the same positions on 175-B vs 176 — they have different gain, threshold, and compression knee characteristics. Don't assume settings transfer between units.
- Compression/distortion onset is also different per unit.
- **Tone-box use**: Attack = OFF, input driven into tube saturation without compression. Adds harmonic color to any source.

---

## Notes for Guitar Use

- **Attack OFF**: Use the 175-B or 176 purely as a tube coloring device at the end of a guitar chain — adds harmonic richness and transformer saturation without squashing dynamics.
- **176 at 4:1 or 8:1**: Natural-feeling guitar compression — not as aggressive as 1176 at 20:1, with warmer tube character.
- **175-B at 12:1**: Peak limiting on picked guitar parts — catches transient spikes while the tube character smooths the attack envelope.
- **Grit technique on guitar**: Both Attack and Release fastest — compression distortion that adds grit to clean or slightly driven tones.
- **Mix at 50–70%**: Parallel compression on guitar — keeps pick attack intact while evening out sustain.
- **Input gain-staging**: The feedback circuit means the compression character changes with input level, not just threshold setting. Experiment with Input for the right balance of coloring vs. limiting.
