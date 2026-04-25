# EP-34 Tape Echo — UADx

Source: https://help.uaudio.com/hc/en-us/articles/33141081493012-EP-34-Tape-Echo-Manual

---

## Overview

Emulation of the Maestro Echoplex EP-3/EP-4 tape echo. Used by Jimmy Page, Brian May, Eddie Van Halen, Andy Summers, Eric Johnson, Chick Corea. Captures idiosyncrasies of vintage units: distortion, wow and flutter, self-oscillation, squelch effects, and analog randomness. Modern additions: Tempo Sync, Wet/Solo, Pan, Tape Tension.

**Note**: EP-34 Tape Echo is not affiliated with companies currently using the Echoplex name. EP-3/EP-4 names identify the hardware studied.

---

## Controls

### Echo Delay
Delay time control. Range: **80–700 ms**. When Sync is active: 1/64 to 1/2 note values. Controlled by two sliders (metallic "slider handle" and "slider nose") — both control the same parameter.

When Sync is on, beat values exceeding 700 ms are shown in parentheses. Use keyboard arrow keys while clicking slider for fine sync value adjustment.

The slider can be moved in realtime for pitch shifting effects. The character of this pitch shift is controlled by the **Tension** switch.

### Echo Display
Shows current delay time. Values can be entered directly via text entry. Displays ms (Sync off) or fractional bar value (Sync on).

### Echo Repeats
Feedback knob. Fully counter-clockwise = one repeat only. Clockwise = more repeats. High values → self-oscillation.

Self-oscillation is a core creative feature. Character varies with program material, gain, tone, rate, and input settings. Can achieve oscillation with no input signal. Use subtly (gentle oscillation on held notes) or extremely ("over the top" chaos).

### Echo Volume
Wet/dry mix of the delayed signal. **CRITICAL: The hardware taper is emulated — 85–95% range gives approximately 50/50 wet/dry balance**. Minimum = echo muted. No effect when Wet switch is On.

At minimum position, dry signal is still colored by the modeled circuitry.

### Recording Volume
Input gain and clipping of the tape signal. Increasing adds tape distortion and "grit" — an important part of the Echoplex's character. Level indicated by Input Meter.

### Input Meter
Three-segment horizontal LED array (two green, one red). Monitors recording level at tape input. Yellow LED = plug-in active (Power on).

### Echo Tone
Frequency response of the delayed (wet) signal only. **Does not affect the dry signal.** Cut/boost; no effect at 12 o'clock. Range: ±10 dB.

**Treble**: High frequency response of delayed signals.

**Bass**: Low frequency response of delayed signals.

### Echo Pan
Stereo position of the delayed (wet) signal only. Does not affect dry signal. Click "Echo" label text to return to center. Unavailable in mono-in/mono-out configuration.

### Input (LO / HI)
Toggles between Instrument (LO) and Microphone (HI) gain structures from the original hardware.
- **LO**: Instrument input — cleaner
- **HI**: Microphone input — dirtier, more gain

**Warning**: Switching between LO and HI may cause a significant jump in output levels.

### Tension (LO / HI)
Emulates the tension adjustment screw on the Echo Delay slider. Controls the slew rate (pitch shifting character) when Echo Delay is moved in realtime.
- **LO** (loose tension): Faster slew rate — "snappier" pitch shifting
- **HI** (tight tension): Slower slew rate — "sluggish" pitch shifting

### Send (ON / OFF)
The "dub switch." OFF = signal sent to the echo portion is disabled. Classic dub technique for dropping signal in and out of the echo loop.

### Sync
Engages Tempo Sync mode. Delay times lock to host DAW tempo. When toggled, parameter values convert between ms and beats to the nearest matching value.

### Wet (ON / OFF)
100% Wet mode — mutes the dry unprocessed signal. Use On when plug-in is on an aux return bus for send/return routing. Leave Off when used as a channel insert.

**Note**: Wet is a global per-instance control. Saved in the project/session but NOT within individual preset files.

**Warning**: Engaging Wet may cause a significant jump in output levels.

### Power
Enables/disables the plug-in. Yellow LED in Input Meter illuminates when active.

---

## Notes for Guitar Use

- **Echo Volume taper**: The most common mistake — the control must be at 85–95% for a balanced wet/dry mix. 50% sounds nearly dry.
- **Recording Volume for grit**: Push Recording Volume up for Echoplex preamp saturation on guitar. This is a prized part of the original hardware tone, not a side effect.
- **Input HI for dirtier repeats**: HI switch adds preamp character to the echo signal. Useful when you want the repeats to feel alive, not just the dry tone.
- **Echo Delay realtime movement**: Moving the slider while playing creates pitch-bending effects (classic tape echo manipulation). Tension LO = faster/snappier pitch shifts; Tension HI = slower/more gradual sweeps.
- **Self-oscillation technique**: Bring Echo Repeats to the edge of oscillation, then push over it on held notes. Echo Volume controls how loud the runaway gets. Power cycling clears the tape.
- **Treble/Bass only affect echoes**: Use to roll off brightness on repeats — creates natural tape echo decay without affecting the dry guitar tone.
- **Send (dub switch)**: Classic David Gilmour technique — automate Send OFF to cut guitar into the echo loop cleanly.
