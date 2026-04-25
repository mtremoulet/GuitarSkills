# Dream '65 Reverb Amp — UADx

Source: https://help.uaudio.com/hc/en-us/articles/30847237412500-Dream-65-Reverb-Amp-Manual

---

## Overview

Emulation of a 1965 Fender Deluxe Reverb. Includes six speaker cabinet options, three mod voicings, tube-driven spring reverb, and vibrato circuit.

---

## Controls

### Input / Output

- **IN**: Input level. Hi-Z (center/default position) to LINE (minimum). Does not change when loading presets.
- **OUT**: Output level. At noon ≈ bypassed level. Use for clean level adjustments (Volume changes character/overdrive/compression).
- **On/Off**: Bypasses the plug-in and reduces processing load.

---

### Presets

- **Preset bar**: Click to open preset browser
- **< > arrows**: Step through presets

---

### MOD (Voicing Modes)

Three mod options — select the voicing character before engaging Boost:

- **Stock**: Clean boost of up to 10 dB. Bright cap and tone stack unmodified. Bright on by default.
- **Lead**: Removes bright cap; applies midrange tone stack lift ("lead boost"). Produces a slightly darker, more mid-forward character. Bright off by default.
- **D-Tex**: SRV-inspired mod — adds more midrange and gain. Bass and Treble have reduced effect at higher Boost values. Vibrato circuit is **unavailable** when Boost is enabled in D-Tex mode. Bright on by default.

- **Boost button**: Enables the selected mod voicing
- **Boost knob**: Rotate clockwise to increase gain/effect amount (up to 10 dB in Stock mode)

---

### Tone Controls

- **Volume**: Amp gain stage. Changing Volume changes character, overdrive amount, and compression — not just level. For clean level adjustment use OUT instead.
- **Treble**: High frequency tone stack
- **Bass**: Low frequency tone stack
- **Bright/Normal switch**: High-end boost (bright cap effect). Most noticeable at lower Volume settings.
  - Default state: Bright ON for Stock and D-Tex mods; Bright OFF for Lead mod

---

### Reverb

- **Reverb LED button**: Enable/disable reverb
- **Reverb Level knob**: Mix amount. Tube-driven spring reverb emulation. Reverb is more noticeable when the amp is clean; appears less prominent as gain and compression increase.

---

### Vibrato

- **Vibrato LED button**: Enable/disable vibrato
- **Speed knob**: Vibrato rate
- **Intensity knob**: Vibrato depth
- **Note**: Vibrato is unavailable when MOD = D-Tex and Boost is enabled.

---

## Speaker Cabinets

| Cabinet | Description |
|---------|-------------|
| **GB25** | Celestion Greenback + M160 ribbon mic |
| **Oxford** | Oxford 12K5-6 + 57 mic — "classic 1965 sound" (default) |
| **EV12** | EV EVM12L + 414 condenser — thick, tight bottom end |
| **Boutique D65** | Two-Rock 2×12 with G12-65s + 57 & 121 ribbon |
| **S-Verb** | 1966 4×10 Fender Super Reverb + 414 — lo-fi, surf character |
| **JBF120** | 1968 Twin Reverb 2×12 with JBL D-120Fs + 57 & 121 ribbon — clean, fingerstyle |
| **Direct** | No cabinet simulation |

---

## Notes for Guitar Use

- **Volume vs. OUT**: Always distinguish between these two — Volume changes the amp's gain character and compression, OUT is a neutral post-amp level trim.
- **Boost with Stock mod** is the cleanest boost path — transparent up to 10 dB, good for solos.
- **Lead mod** is the better choice for a darker, more mid-present crunch without the D-Tex gain boost.
- **D-Tex** pairs well with Tone King Lead channel (Mid-Bite up) if you want stacked midrange push; use cautiously as both circuits add mids.
- **Reverb behavior**: Because tube-driven reverb is compressed by the gain stage, reverb level needs to be set higher on crunchier settings to hear the same apparent mix.
- **Oxford cabinet** is closest to the stock 1965 Deluxe Reverb sound. **JBF120** is cleaner with more headroom — useful when Tone King is providing the breakup.
- **Tone King IR active + Dream '65**: If Tone King's IR is active, do NOT also use Dream '65's cabinet selection (set to Direct). Use the Tone King IR as the cabinet.
