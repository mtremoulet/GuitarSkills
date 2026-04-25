# 1176 Classic FET Compressor — UADx

Source: https://help.uaudio.com/hc/en-us/articles/34530260482324-1176-Classic-FET-Compressor-Manual

---

## Overview

Based on the classic early 70s / Brad Plunkett "LN" (Low Noise) era 1176 circuit. Features linear compression response, transistor gain amplification, and program-dependent release. The most famous studio compressor in the world — used on nearly every hit recording of our time.

---

## CRITICAL: Attack and Release Direction (Counterintuitive)

**Attack and Release knobs are BACKWARDS from every other compressor:**
- Fully **clockwise** = **fastest** attack/release time
- Fully **counter-clockwise** = **slowest** attack/release time

This matches original hardware behavior. Always remember: clockwise = fast.

---

## Controls

### Input
Sets gain reduction amount AND compression threshold simultaneously. Rotate clockwise to increase compression. Label values are arbitrary (not calibrated to dB values). Even at "∞" position, signal still passes and is compressed.

**Note:** Increasing Input also increases distortion.

### Output
Final output level. Use to make up gain lost through gain reduction. Does NOT affect compression amount. Monitor using VU meter set to +8 or +4.

**Note:** Increasing Output also increases distortion.

### Attack
Time for 1176 to respond to incoming signal and begin gain reduction. Range: 20 microseconds to 800 microseconds (both extremely fast — this is a fast compressor).

- **Clockwise** = fastest attack (~20 µs) — catches transients almost immediately, softens sound
- **Counter-clockwise** = slowest attack (~800 µs) — lets transients pass before compression begins
- Actual attack time varies slightly with selected ratio; lower ratios maintain fastest attack times

### Release
Time to return to initial (pre-gain-reduction) level. Range: 50 ms to 1100 ms (1.1 sec).

- **Clockwise** = fastest release
- **Counter-clockwise** = slowest release

Fast release = "pumping" and "breathing" effects. Slow release = gain reduction persisting into quiet sections. Small adjustments make significant differences.

**Program-dependent release**: The 1176 automatically adjusts release behavior based on the program material:
- After transients: fast release (avoids prolonged dropouts)
- During sustained heavy compression: slower release (reduces pumping and harmonic distortion)
- The "transition time" determines how long signal must be compressed before the slow release activates

### Ratio
Four pushbutton switches — select one:
- **4:1** — Compression (most gentle)
- **8:1** — Compression
- **12:1** — Compression to Limiting
- **20:1** — Peak limiting (hardest)

### All Button Mode
Shift-click any ratio button to engage All Button Mode (also called "British Mode"). All four ratio buttons light up.
- Ratio goes to approximately 12:1–20:1
- Bias points change throughout the circuit, altering attack and release times
- Distortion increases radically
- Unique, constantly shifting compression curve → trademark overdriven tone
- Ideal for: drums/room mics, bass, guitars needing both compression and distortion, vocals "in your face"

### Grit Technique
Set both Attack and Release to their fastest settings (fully clockwise). Causes compression distortion from minute level fluctuations — very fast attack/release cycle sounds like distortion. Even more pronounced in All Button Mode. Useful on: bass (compression + grit simultaneously), screaming lead vocals, guitars needing an aggressive edge.

### VU Meter
Displays gain reduction (GR) or output level depending on Meter Function switch.

### Meter Function Switches
Four buttons to the right of VU meter:
- **GR**: Meter shows gain reduction in dB
- **+8**: Meter shows output level (0 = +8 dBu)
- **+4**: Meter shows output level (0 = +4 dBu)
- **OFF**: Plug-in disabled, processing reduced

**Note**: In GR mode with All Button engaged, meter will appear to behave strangely — this is correct hardware behavior.

---

## Primary Use Cases

- Individual inserts: snare, vocal, guitar, bass
- Stereo bus: drums
- Range: transparent limiting → crushed and distorted

---

## Notes for Guitar Use

- **The most common guitar use**: light compression (4:1 or 8:1, moderate Input, moderate Attack/Release) to control dynamics while preserving pick attack
- **Preserve pick attack**: Set Attack at ~11 o'clock (medium-slow in 1176 terms, i.e., counter-clockwise from fully fast). This lets the initial transient through before compression kicks in.
- **All Button on guitar**: adds a compressed, edgy, "in your face" quality. Works especially well on lead guitar tracks.
- **All Button + fast Attack + fast Release (grit technique)**: pushes guitar toward compression distortion — pairs well with other gain stages for layered saturation.
- **Post-amp use**: Place after Amp Designer / UA amp plug-ins to control the output level and add compression coloration to the already-overdriven signal.
