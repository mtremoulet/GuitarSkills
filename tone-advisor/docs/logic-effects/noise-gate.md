# Noise Gate — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 5995–6143

---

## Overview

Noise Gate suppresses unwanted noise audible when the audio signal is at a low level. Passes signals above the threshold unimpeded; reduces signals below the threshold. Common uses: background noise removal, crosstalk, low-level hum.

**Ducker mode**: Reduces source signal level in response to a side chain (e.g., DJ/announcer speech ducking music).

Add via: Dynamics > Noise Gate in a channel strip Audio Effect plug-in menu.

---

## Parameters

- **Gate/Ducker buttons**: Set operating mode
- **Threshold knob and field**: Signals below this are reduced in level
- **Reduction/Ducking knob and field**: Amount of signal reduction. Set to lowest value for complete suppression; higher values reduce but still pass lower-level sounds. Can also boost up to +20 dB (useful for ducking effects).
- **Hysteresis slider and field**: Difference (in dB) between threshold values that open and close the gate. Prevents rapid chattering when signal level hovers near threshold. Always negative; −6 dB is a good starting point.
- **Open/Close indicators**: Current gate state display
- **Attack knob and field**: Time to fully open gate after signal exceeds threshold. Lower = faster, good for percussive signals (drums). Higher = slower, good for signals with slow attack (pads, strings).
- **Hold knob and field**: Minimum time gate remains open after signal falls below threshold. Prevents abrupt level changes (chattering) from rapid open/close cycling.
- **Release knob and field**: Time to reach maximum attenuation after signal falls below threshold. Higher = allows signal to fade out naturally (longer reverb tails). Lower = abrupt cutoff.
- **Lookahead slider and field**: How far ahead the gate analyzes incoming signal — allows faster response to peak levels.
- **Characteristics pop-up menu**: Bandpass or Band Reject filter type for side chain
- **Monitor button**: Hear the side chain signal (including effect of High/Low Cut filters)
- **Filter button**: Turn on to access High/Low Cutoff parameters
- **High Cutoff slider and field**: Upper cutoff frequency for side chain signal. Trigger signals above this are filtered out.
- **Low Cutoff slider and field**: Lower cutoff frequency for side chain signal. Trigger signals below this are filtered out.

---

## Key Behaviors

- **Hysteresis** sets gate to open at the Threshold and stay open until level drops below a second, lower level. Effective against chattering when signal hovers near threshold.
- **Side chain filters** (High/Low Cutoff) affect only the detection/trigger signal — they do NOT filter the actual audio passing through the gate. Use them to isolate the desired trigger frequency.
- When no external side chain is selected, the input signal is used as the side chain control signal.

---

## Using Side Chain Filters (example: isolating snare drum trigger)

1. Click Monitor button to hear how filters affect the trigger signal
2. Drag High Cutoff slider to remove high-frequency triggers (e.g., hi-hat bleed)
3. Drag Low Cutoff slider to set the lower boundary
4. Turn off monitoring, then set an appropriate Threshold level

## Ducker Mode Setup

1. Insert Noise Gate into an aux channel strip; click Ducker button
2. Assign all channel strips to duck to a bus routed to that aux
3. Choose the "control" signal (e.g., vocal) from the Side Chain pop-up menu
4. The ducked side chain signal is mixed with output after the plug-in — the control signal is still heard at output

---

## Notes for Guitar Use

- For live guitar with amp sim: set Threshold just below the guitar's natural sustain floor, Reduction to −60 dB or lower, Attack to 5–10 ms, Release to 150–300 ms
- Hysteresis is essential — start at −6 dB to prevent gate chattering during natural note decay
- Hold can help retain the feel of pick attack on single notes before the gate re-closes
