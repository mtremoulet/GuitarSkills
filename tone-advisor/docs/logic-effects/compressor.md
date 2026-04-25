# Compressor — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 5118–5729

---

## Overview

Compressor emulates several professional-level compressors. Reduces sounds that exceed a threshold, smoothing dynamics and increasing perceived loudness. Useful on individual tracks or the overall mix.

Add via: Dynamics > Compressor in a channel strip Audio Effect plug-in menu.

Interface divided into: **Main parameters** (meters + core controls) and **Output or Side Chain parameters** (right side, toggled by button).

---

## Circuit Types

Choose via Circuit Type buttons. Interface updates with each selection. Not all parameters available in every model.

| Circuit Type | Character | Best For |
|---|---|---|
| **Platinum Digital** | Clean, fast transient response | Versatile, general purpose |
| **FET** | Fast transient response; clean to warm midrange; can push to "crunchy" on transients; can only attenuate (not amplify) | Drums, vocals, guitars, fast-attack signals |
| **VCA** | Slow or fast response; clean tone; can attenuate or amplify | Bass guitars, low-frequency signals |
| **Opto** | Fast transient response; non-linear release; very clean | Vocals, guitars; also used as limiting amplifier across buses/outputs |
| **Studio VCA** | VCA variant | — |
| **Classic VCA** | VCA variant | — |
| **Vintage VCA** | VCA variant | — |
| **Vintage FET** | FET variant | — |
| **Vintage Opto** | Opto variant | — |

---

## Main Parameters

- **Input Gain knob**: Set level at compressor input
- **Threshold knob**: Set threshold level — signals above this are reduced
- **Ratio knob**: Compression ratio. Example: 4:1 means a 4 dB increase above threshold results in 1 dB output increase.
- **Knee knob**: Strength of compression near threshold.
  - Near 0: hard knee — no compression just below threshold, full Ratio at threshold; abrupt transition
  - Higher values: soft knee — compression increases gradually as signal approaches threshold; smoother
- **Attack knob**: Time for Compressor to start reacting after signal exceeds threshold. Higher values preserve attack transients; lower values maximize overall level compression.
- **Release knob**: Time for Compressor to stop reducing after signal falls below threshold. Higher = smoother dynamics; lower = emphasizes dynamic differences.
- **Auto Release button**: Release time dynamically adjusts to audio material. Interacts with Release knob value.
- **Make Up knob**: Gain applied to the compressed signal (compensates for level reduction)
- **Auto Gain buttons**: Off / 0 dB / −12 dB — automatic compensation for volume reductions caused by compression. Note: If Auto Gain + RMS together cause distortion, turn off Auto Gain and adjust Make Up manually.
- **Gain Reduction meter/graph**: Real-time compression amount. Click Meter or Graph button to toggle display type.
- **Input Peak indicator**: Peak level at input
- **Output Peak indicator**: Peak level at output
- **Output Gain knob**: Overall output level

---

## Output Parameters (click Output button)

- **Limiter button**: Integrated limiter on/off — prevents output from exceeding threshold
- **Limiter Threshold knob**: Threshold for the integrated limiter
- **Distortion knob**: Clipping type above 0 dB:
  - **Soft**: Rounds off signal as it approaches 0 dB — smoothed distortion
  - **Hard**: Transistor-style abrupt limiting above 0 dB
  - **Clip**: Limits at 0 dB; can be punchier than Hard depending on material
- **Mix knob**: Dry/wet balance. Dry reduces signal peaks; wet increases level of softer signals (parallel compression).

---

## Side Chain Parameters (click Side Chain button)

Side chain is always active even with no external source — input is "normaled" as side chain when nothing is patched (like hardware VCA compressors).

- **Detection buttons**:
  - **Max**: Compresses both channels if either stereo channel exceeds threshold
  - **Sum**: Combined level of both channels must exceed threshold before compression
- **Peak/RMS buttons**: Use with Max/Sum. Peak = technically accurate; RMS = better indication of perceived loudness. Helps avoid artifacts (clicks) depending on material and Attack setting.
- **Filter button**: Turn on/off side chain filter. **Listen**: monitor the side chain signal.
- **Filter mode knob**: LP (lowpass), BP (bandpass), HP (highpass), ParEQ (parametric), HS (high shelving)
- **Frequency knob**: Center frequency for side chain filter
- **Q knob**: Width of frequency band affected by side chain filter
- **Gain knob**: Gain applied to side chain signal

---

## Key Behaviors

- **Threshold + Ratio** are the most important controls. Threshold sets the floor; Ratio determines how much the excess is reduced.
- **Platinum Digital only**: Can analyze using Peak or RMS. Peak = technically accurate; RMS = better for perceived loudness.
- **Attack** at lower values = more compression of overall level. Higher values preserve transient character of instruments and voices.
- **Knee at 0** = hard knee (most severe). Increasing Knee = progressively softer, more gradual compression onset.
