# Tremolo — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 15219–15302

Add via: Modulation > Tremolo in a channel strip Audio Effect plug-in menu.

---

## Overview

Tremolo modulates the amplitude (volume) of the incoming signal, producing periodic volume changes. Commonly found in vintage guitar combo amps (where it is sometimes incorrectly called vibrato). The graphic waveform display shows all parameters except Rate.

---

## Parameters

- **Sync button**: Synchronize modulation speed with project tempo. Choose note values with Rate knob.
- **Rate knob and field**: Frequency of the LFO (modulation speed)
- **Depth knob and field**: Modulation amount (intensity of the volume variation)
- **Smoothing slider and field**: Changes the shape of the LFO waveform. Also interacts with Symmetry.
- **Distribution pop-up menu**: How phase offsets between individual channels are distributed in surround field. Options: circular, left↔right, front↔rear, random, new random. Available only in surround instances.
- **Offset field**: Amount of left or right movement for the modulation cycle. Results in small or large tremolo variations.
- **Symmetry field**: Skew the balance toward the upward or downward phase of waveform cycles. Note: If Symmetry is set to 50% and Smoothing to 0%, the LFO waveform becomes rectangular — the highest and lowest volume states have equal timing, with abrupt switching between them.
- **Phase field**: Phase relationship between individual channel modulations in stereo/surround. At 0: modulation values reached simultaneously for all channels. At 180 or −180: greatest possible distance between channel modulation phases.
- **Waveform display**: Shows and lets you edit modulation Offset, Symmetry, and Phase.
  - Green handles control Offset (left handle) and Symmetry (right handle)
  - Blue handles control Phase between channels

---

## Notes for Guitar Use

- Do not use Logic's Tremolo if the Tone King pedal's Tremolo is already active — avoid stacking two tremolos
- **Sync + Rate** set to musical note values (1/4 for quarter-note tremolo, 3/8 for dotted-eighth) locks the effect to the song tempo
- **Depth** around 50–70% creates a classic guitar amp tremolo feel; lower values are subtle
- **Smoothing** at 0% with **Symmetry** at 50% = square wave (hardest chop effect); higher Smoothing = sine wave (gentler)
