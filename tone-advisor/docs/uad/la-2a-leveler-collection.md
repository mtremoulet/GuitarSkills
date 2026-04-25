# Teletronix LA-2A Leveler Collection — UADx

Source: https://help.uaudio.com/hc/en-us/articles/4419496124180-Teletronix-LA-2A-Leveler-Collection-Manual

---

## Overview

Collection of three optical compressor models based on different eras of the Teletronix LA-2A Leveling Amplifier. Program-dependent optical compression with fixed (non-adjustable) time constants. The compressor responds to both the program material and its frequency content — slower and more musical than VCA/FET designs.

**Internal reference level**: -12 dBFS (allows wider range of Peak Reduction and Gain before I/O distortion occurs)

---

## CRITICAL: Knob Scale

**Peak Reduction and Gain knobs are labeled 0–100 — these are arbitrary, NOT calibrated dB values.** Do not treat them as percentages or dB amounts.

---

## Plugin Variants

| UADx Name | Original Hardware | Era | Time Constant | Character |
|-----------|------------------|-----|---------------|-----------|
| **LA-2A Silver Compressor** | Teletronix LA-2A Silver | Late 1960s | Fastest | Most flexible; handles transient-rich sources (drums, percussion) |
| **LA-2A Gray Compressor** | Teletronix LA-2A Gray | Mid-1960s | Medium | "Medium-speed" compression |
| **LA-2 Compressor** | Teletronix LA-2 | Early 1960s | Slowest | "Mellowed" sound; use with legato tempos and vocals |
| **LA-2A Legacy** | (First-generation UAD model) | — | — | Lower DSP use; no transformer/I/O distortion modeling; useful when DSP is limited |

---

## Controls

### Peak Reduction (0–100 scale, arbitrary)
Sets compression threshold. Increasing the value lowers the threshold, increasing compression amount. Range corresponds approximately to 0 dB (fully counter-clockwise) to -40 dB threshold (fully clockwise).

- Rotate clockwise to increase compression
- Monitor amount using VU Meter set to Gain Reduction
- When at minimum: no compression occurs, but signal is still colored by circuitry
- At extreme high settings: interesting sidechain distortion occurs, primarily affecting low frequencies

### Gain (0–100 scale, arbitrary)
Makeup gain — adds up to 40 dB of output level to compensate for gain reduction. Does NOT affect compression amount. Adjust after Peak Reduction is set.

### Compress / Limit Switch
Sets compression ratio. (Not available on the LA-2 — it is hardwired in Limit mode.)
- **Compress**: ~3:1 ratio
- **Limit**: ~∞:1 ratio
- Note: Ratios are nonlinear and frequency-dependent — these figures are approximations.

### Mix (LA-2 Compressor only)
Parallel compression blend. Not present on original hardware.
- 0% (fully counter-clockwise) = dry signal only
- 100% (fully clockwise, default) = fully wet compressed signal only
- 50% (noon) = equal blend of dry and wet
- Phase-accurate blend throughout range

### Emphasis / HF (R37 sidechain filter)
Shelf filter in the compressor's sidechain. Controls frequency-dependent compression behavior. (Unavailable on LA-2A Legacy.)
- **Fully clockwise (default)**: sidechain unfiltered — all frequencies trigger compression equally
- **Counter-clockwise**: gradually reduces low frequency content in sidechain → compression becomes less sensitive to lows, more sensitive to highs → higher frequencies are compressed more

Original function: FM broadcast pre-emphasis compensation. Useful for de-essing or brightening sources.

### Meter Knob
Sets VU Meter mode:
- **Gain Reduction**: shows dB of gain reduction
- **+10**: output level (0 = +10 dBu)
- **+4**: output level (0 = +4 dBu)

### On/Power Switch
Bypasses plug-in and reduces DSP usage.

---

## Program-Dependent Release

No manual attack or release controls. The T4 photocell design is inherently program-dependent:
- After transients: fast release (avoids prolonged dropouts)
- During sustained heavy compression: slower release (reduces pumping)
- Can take a few minutes to fully recover from heavy incoming signal (true to hardware behavior)

---

## Notes for Guitar Use

- The LA-2A is fundamentally a vocal/bass/strings tool — on guitar it adds subtle optical compression coloring rather than aggressive dynamic control.
- **Best guitar use**: light Peak Reduction (~30–50) in Compress mode, post-amp, to gently smooth dynamics and add tube warmth to the signal.
- **LA-2A Silver** is the best choice for guitar because its faster time constant handles transient-rich picking attack better than the Gray or LA-2 models.
- **Emphasis fully clockwise** (default) for guitar — you want equal frequency sensitivity in the sidechain.
- **Limit mode** at high Peak Reduction values can add a pleasant compression distortion to guitar, especially on sustained notes.
- Unlike the 1176, the LA-2A cannot be pushed for extreme "grit" — it's the warmer, more transparent tool in the pair.
