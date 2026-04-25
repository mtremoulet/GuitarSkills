# LA-2A Tube Compressor — UADx

Source: https://help.uaudio.com/hc/en-us/articles/19378009641748-LA-2A-Tube-Compressor-Manual

---

## Overview

A simplified version of the Teletronix LA-2A Silver plug-in from the [LA-2A Leveler Collection](la-2a-leveler-collection.md). Same underlying model, reduced controls. Optical gain reduction using the T4 photocell design. Program-dependent and frequency-dependent compression — not fully adjustable attack/release.

Primary use: nominal transparent gain reduction on vocals, bass, strings, horns. Can also function as a tube coloring device with Peak Reduction at minimum.

---

## Controls

**CRITICAL: Peak Reduction and Gain knobs range from 0–100 and are ARBITRARY SCALE — they do not reflect any dB value.**

### Peak Reduction
Controls compression threshold. Increasing lowers the threshold, increasing compression. Range: 0 dB (fully CCW) to -40 dB (fully CW).

At minimum value: no compression, but signal is still colored by the tube circuitry. Can be used purely for tube tone.

**At extreme settings**: an interesting sidechain distortion occurs, primarily affecting low frequencies.

### Gain
Output level makeup after compression. Up to +40 dB increase. **Does not affect compression amount.** Adjust after dialing in Peak Reduction. Knob is 0–100 arbitrary scale.

### Meter Knob
Selects VU meter mode:
- **Gain Reduction**: Shows amount of compression in dB
- **+10**: Output level (0 = +10 dBu output reference)
- **+4**: Output level (0 = +4 dBu output reference)

### VU Meter
Displays gain reduction or output level per Meter Knob setting.

### Compress/Limit
- **Compress**: ~3:1 ratio
- **Limit**: ~∞:1 ratio

Note: ratios are nonlinear and frequency-dependent — not absolute values.

### On/Power
Enables/disables the plug-in. Off = CPU usage reduced.

---

## Key Characteristics

- **T4 photocell response**: Multi-stage release, frequency-dependent. The cell can take minutes to fully recover from heavy compression.
- **Program-dependent**: Attack and release behavior change based on the signal. No manual attack/release controls.
- **Compression distortion at extreme Peak Reduction**: A creative low-frequency sidechain effect at maximum settings.
- **Internal reference level**: -12 dBFS (same as LA-2A Leveler Collection variants)

---

## Difference from LA-2A Leveler Collection

The LA-2A Tube Compressor is a **simplified version of the Silver Compressor** from the Leveler Collection. What it lacks:
- No Emphasis (HF sidechain filter) control
- No Mix control (unlike the LA-2 Compressor in the collection)
- Fewer meter reference options

If you need Emphasis or parallel mix blend, use the LA-2A Silver Compressor from the Leveler Collection instead.

---

## Notes for Guitar Use

- **Peak Reduction at minimum**: Tube amplifier coloring without compression — adds warmth and harmonic body to a guitar chain as a final stage.
- **Compress mode at moderate Peak Reduction**: Gentle even-harmonic compression, less aggressive than 1176. Good for clean guitar leveling.
- **Limit mode**: Peak control without the character of 1176's FET circuit — the optical response is slower and warmer.
- **Avoid for fast transient control**: The T4 optical response is not designed for fast attack. For picking attack control, use 1176.
