# Channel EQ — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 6338–6806

---

## Overview

Channel EQ is a versatile multiband EQ with eight color-coded frequency bands, including lowpass and highpass filters, low and high shelving filters, and four flexible parametric bands. Features a real-time FFT Analyzer.

Parameters of Channel EQ and Linear Phase EQ are identical — settings can be freely copied between them.

Add via: Equalizers > Channel EQ in a channel strip Audio Effect plug-in menu.

---

## Bands

| Band | Type | Color | Description |
|------|------|-------|-------------|
| Band 1 | High Pass Filter | Red | Passes only frequencies above the set frequency |
| Band 2 | Low Shelf | Orange | Cuts or boosts frequencies below the set frequency |
| Band 3 | Parametric | Yellow | Bell curve: Frequency, Q (bandwidth), Gain |
| Band 4 | Parametric | Green | Bell curve: Frequency, Q (bandwidth), Gain |
| Band 5 | Parametric | Aqua | Bell curve: Frequency, Q (bandwidth), Gain |
| Band 6 | Parametric | Blue | Bell curve: Frequency, Q (bandwidth), Gain |
| Band 7 | High Shelf | Purple | Cuts or boosts frequencies above the set frequency |
| Band 8 | Low Pass Filter | Pink | Passes only frequencies below the set frequency |

**Note:** For bands 1 and 8 (HPF/LPF), the Q parameter has no effect when slope is set to 6 dB/octave. When Q is set to an extremely high value (such as 100), these filters affect only a very narrow frequency band.

---

## Core Parameters

- **Frequency control**: Drag to set the frequency of the selected band
- **Gain/Slope control**: Drag to set the gain for the selected band. For bands 1 and 8, this changes the **slope of the filter** (not gain — important distinction for HPF/LPF)
- **Q control**: Drag to set the Q factor (resonance / bandwidth around center frequency)
- **Master Gain slider**: Set the overall output level after boosting/cutting individual bands

---

## Analyzer and Display Controls

- **Analyzer button**: Turn FFT real-time frequency analysis on/off. Shows peaks and troughs in the incoming signal superimposed on EQ curves.
- **Analyzer (Pre/Post) button**: Show frequency curve before or after EQ is applied
- **Q-Couple button**: Gain-Q coupling — automatically adjusts Q when you change gain on any band. Preserves perceived bandwidth of the bell curve.
- **HQ button**: Turn on oversampling. Useful when EQing above 5kHz with project sample rate below 96kHz. Without oversampling, filters can sound harsh at high frequencies due to narrowing and asymmetric slope.
- **Processing pop-up menu**: Choose stereo, Left Only, Right Only, Mid Only, or Side Only processing

---

## Shortcut Menu Parameters (Control-click display or buttons)

### Graphic Display Scaling
- Linear 12 dB, 30 dB, 60 dB mode
- Warped: Logarithmic, non-linear scale

### Analyzer Mode
- Peak or RMS

### Analyzer Resolution
- Low (2048 points), Medium (4096 points), High (8192 points)
- High resolution requires significantly more processing power; only needed for very low bass frequency analysis

### Gain-Q Couple Strength
- **Proportional**: Widens bandwidth at lower cut/boost, narrows at higher settings
- **Light or Medium**: Some change as gain is raised or lowered
- **Strong**: Preserves most of perceived bandwidth
- **Asymmetric**: Stronger coupling for negative gain (cuts) than positive (boosts)

---

## Extended Parameters (disclosure arrow, lower left)

- **Analyzer Decay slider and field**: Set decay rate (dB per second) of the Analyzer curve — peak decay in Peak mode, averaged decay in RMS mode

---

## Graphic Display Interaction

- Drag anywhere in a band: adjust gain and center frequency simultaneously
- Drag the vertical lines (band edges): adjust Q only
- Drag the horizontal line: adjust gain only
- Drag the control point: adjust center frequency only
- Hold Option-Command + drag: adjust Q and center frequency simultaneously
- Two-finger vertical swipe (trackpad) or single-finger swipe (Magic Mouse): adjust Q
- Hold Command during any drag: limit to vertical or horizontal movement only
- Horizontally dragging the control point in bands 1 and 8: adjusts both frequency AND Q

---

## Key Notes for Guitar Use

- **Gain/Slope field on HPF (Band 1) and LPF (Band 8)**: This column sets the **filter slope**, not gain dB. Do not confuse with the parametric band Gain column.
- The HQ button is worth activating when shaping guitar presence frequencies (3–8kHz range).
- Q-Couple is useful for natural-sounding boosts; disable it when making surgical cuts.
- Analyzer burns CPU — turn it off when not actively using it for analysis.
