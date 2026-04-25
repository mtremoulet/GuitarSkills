# UA 610 Tube Preamp & EQ Collection — UADx

Source: https://help.uaudio.com/hc/en-us/articles/17475989779860-UA-610-Tube-Preamp-EQ-Collection-Manual

---

## Overview

Two tube preamp emulations based on Bill Putnam's 1960-era 610 modular console channel strips. Full signal path modeling including tube amplifiers, transformers, phase shift, and distortion characteristics. The input and output stages each have their own tube gain stage — tuning the I/O gain structure is how you dial in the coloration, from clean to clipped.

**UADx Plugin Names**: 610-A Preamp and EQ / 610-B Preamp and EQ

---

## Two Variants

### 610-A (Vintage)
Based on the original 1960s 610-A module from the Wally Heider "Green Board" console. Fixed EQ frequencies. More vintage character.

### 610-B (Modern)
Based on the Universal Audio 2-610 Dual Channel Tube Preamplifier hardware. Adjustable EQ frequencies, expanded features for modern use.

---

## Input Controls

### Input Select (Line / Mic)

| Setting | Effect |
|---------|--------|
| **Line** | Signal enters as line level. Less tube gain, cleaner sound. |
| **Mic** | ~30 dB additional tube gain applied. Signal from DAW is already at line level, so this readily produces tube color, saturation, and clipping. |

Use caution switching from Line to Mic — output level increases significantly.

**610-B only**: Mic impedance switch (500 Ω or 2K Ω) — different impedances have subtle effects on signal color.

### Input Gain

Controls the signal level at the tube input stage. Higher input gain = more tube color and distortion.

**610-A**: Three-position LO/OFF/HI switch
- HI adds approximately +8 dB and changes distortion characteristics
- OFF bypasses the plug-in and reduces DSP usage

**610-B**: Five-position rotary: -10 dB, -5 dB, 0, +5 dB, +10 dB

### Mic Input Pad
Additional attenuation for Mic input (not available for Line input):
- **610-A**: -20 dB available
- **610-B**: -15 dB available

### Polarity
Inverts signal polarity (phase). Up position = inverted. Down = normal.

---

## EQ Controls

The 610 EQs use a feedback-style design — EQ settings affect the distortion characteristics of the output stage, not just frequency balance.

### 610-A EQ (Fixed Frequencies)

| Band | Fixed Frequency | Available Gain Values |
|------|----------------|----------------------|
| **L.F. Shelf** | 100 Hz | -6, 0, +6 dB |
| **H.F. Shelf** | 10 kHz | -6, 0, +3, +6 dB |

### 610-B EQ (Adjustable Frequencies)

| Band | Frequency Options | Gain Options |
|------|------------------|--------------|
| **LO Shelf** | 70, 100, or 200 Hz | ±1.5, ±3, ±4.5, ±6, ±9 dB (or 0 dB) |
| **HI Shelf** | 4.5, 7, or 10 kHz | ±1.5, ±3, ±4.5, ±6, ±9 dB (or 0 dB) |

When gain is set to 0 dB, the filter is inactive.

---

## Output Controls

### Level ("The Big Knob")
Controls the tube output stage gain. Higher values = more tube coloration and saturation.
- Range: approximately 0 to 61 dB of gain
- This control affects signal character — use it to dial in tube color
- Counteract level increases using the Output control (see below)

**Technique**: Crank Gain and Level for more distortion/color, then use Output to normalize the level. This is how you maximize tube character while maintaining controllable output.

### Output
Clean gain control at the plug-in output — does NOT affect sonic character. Range: -∞ dB (off) to +12 dB.
- Click "0" label text to reset to 0 dB
- Set to Off: disables plug-in and reduces DSP usage (Off cannot be reached by rotating knob unless in Gain Stage Mode)
- Not on original hardware — digital-only control

---

## Gain Staging Strategy

The 610 has three gain-affecting controls that interact:
1. **Input Gain** — first tube stage (affects color early in chain)
2. **Level** — output tube stage (affects color at the end)
3. **Output** — clean post-tube trim (no character effect)

The combination of Input Gain and Level determines the tube saturation character. Output is just a level trim. Different combinations of high Input + lower Level vs. lower Input + higher Level produce different saturation textures.

---

## Notes for Guitar Use

- The 610 is primarily a preamp/EQ coloring tool, not a dynamic controller. It adds tube warmth and harmonic content.
- **610-A is simpler to use for guitar**: fixed EQ frequencies (100 Hz shelf, 10 kHz shelf) map cleanly to a typical guitar EQ approach — bass body and top-end air.
- **610-B gives more surgical control**: adjustable shelf frequencies let you target the 200 Hz muddiness area or the 4.5 kHz presence area specifically.
- **Line mode** is almost always correct for guitar DI signals going into the 610 plug-in. Mic mode is for simulating a mic'd source going through the preamp.
- **The EQ-affects-distortion interaction is musically important**: adding +6 dB HF boost doesn't just brighten the signal — it also changes how the output stage saturates. Use this for creative harmonic shaping.
- Place the 610 post-amp (after Amp Designer or UA amp sim) to add preamp warmth and broad EQ strokes to the already-processed guitar signal.
