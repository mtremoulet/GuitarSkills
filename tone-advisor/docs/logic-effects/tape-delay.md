# Tape Delay — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 4301–4515

Add via: Delay > Tape Delay in a channel strip Audio Effect plug-in menu.

---

## Overview

Simulates vintage tape echo machines. Runs at free rate or synchronized with project tempo. Equipped with a highpass and lowpass filter in the feedback loop (easy to create dub echo effects). Includes LFO for delay time modulation — can produce chorus effects even on long delays.

---

## Parameters

- **Tempo Sync button**: Synchronize delay repeats with project tempo (including tempo changes). Current tempo shown below button. Set note values with Note pop-up or Delay Time knob.
- **Delay Time knob and field**: Delay time in milliseconds. Notes/dots displayed around knob when tempo-synced. Click buttons/dots or rotate knob to choose exact sync value.
- **÷2 and ×2 buttons**: Halve or double current delay time
- **Note pop-up menu**: Grid resolution for delay time
- **Deviation field**: Amount of deviation from the grid
- **Smoothing slider and field**: Evens out the LFO and flutter effect
- **Clip Threshold knob**: Level of distorted tape saturation signal.
  - Higher values: no additional audible distortion
  - Lower values: aggressive distortion
  - High Feedback values cause eventual distortion regardless of Clip Threshold
  - Aggressive distortion and signal breakup happen much more rapidly with low Clip Threshold + high Feedback
- **Spread knob and field**: Width of effect signal in stereo instances. Not available in mono instances.
- **Tape Head Mode buttons**: Choose Clean or Diffuse mode to emulate a different tape head position. Affects behavior of Flutter, Feedback, and other parameters.
- **Low Cut slider and field**: Cut frequencies below this value from the effect signal, shaping the sound of delay repeats. **Filter is in the feedback circuit** — filtering effect increases with each repeat. Moving Low Cut slider right = ever thinner echoes.
- **High Cut slider and field**: Cut frequencies above this value from the effect signal. **Filter is in the feedback circuit** — filtering intensifies with each repeat. Moving High Cut slider left = increasingly muddy and confused tone.
- **LFO Rate knob and field**: Speed of the LFO (for delay time modulation)
- **LFO Intensity knob and field**: Amount of LFO modulation. A value of 0 turns off delay modulation.
- **Flutter Rate knob and field**: Speed variation of tape transport irregularities
- **Flutter Intensity knob and field**: Intensity of the "flutter" effect (simulates tape transport speed irregularities)
- **Feedback knob**: Amount of delayed and filtered signal routed back to input.
  - Lowest value = single echo
  - 100% = endless repetition
  - High Feedback levels tend to accumulate signal and cause distortion — use Character (Clip Threshold) to control color
- **Freeze button**: Capture current delay repeats and sustain them until turned off
- **Dry slider and field**: Amount of original signal
- **Wet slider and field**: Amount of effect signal

---

## Notes for Guitar Use

- The **feedback-loop filters** (Low/High Cut) are the key to authentic tape echo character — as delay repeats accumulate, they get progressively darker/thinner, simulating tape degradation
- **Clip Threshold** adds tape saturation to the repeats — lower settings give a gritty, vintage-tape-breakup character
- **LFO Intensity** set low (5–15%) adds a subtle warble that mimics tape wow and flutter without being obvious
- **Flutter Rate/Intensity** for classic tape echo feel — subtle settings; extreme settings become obvious pitch wobble
- Classic dub echo setup: High Feedback, High Cut rolled off, Low Cut raised, low Dry, high Wet
