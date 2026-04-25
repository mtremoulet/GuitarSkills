# Galaxy Tape Echo — UADx

Source: https://help.uaudio.com/hc/en-us/articles/4419513003668-Galaxy-Tape-Echo-Manual

---

## Overview

Emulation of the Roland RE-201 Space Echo (1973) — a tape delay + spring reverb unit. Captures physical behavior including distortion, wow and flutter, pitch shifting, self-oscillation, and tape splice artifacts.

**Note**: This plug-in is not affiliated with or endorsed by Roland. The RE-201 and Space Echo names identify the hardware studied.

---

## Controls

### Input Volume
Signal level going into the plug-in. Unity gain at 12 o'clock. Clipping distortion at the input affects the echo and reverb tone (often a desired effect). For cleaner sound: reduce Input Volume, increase Output Volume.

Peak lamp illuminates at approximately -2 dB to -1.5 dB, gets brighter as level increases.

### Head Select (12 positions)
Selects which tape heads and/or spring reverb are active.

| Position | Description |
|----------|-------------|
| 1 | Head 1 only (echo) |
| 2 | Head 2 only (echo) |
| 3 | Head 3 only (echo) |
| 4 | Heads 1+2 (echo) |
| 5 | Heads 1+2 + reverb |
| 6 | Head 3 + reverb |
| 7 | Heads 1+3 + reverb |
| 8 | Heads 2+3 + reverb |
| 9 | Head 1 + reverb |
| 10 | Heads 1+2+3 + reverb |
| 11 | Head 2 + reverb |
| Reverb | Spring reverb only (no tape echo) |

### Echo Rate
Delay time control. **Counter-clockwise = longer delay; clockwise = shorter delay** (inverse of most controls).

Available delay time ranges by head:
- Head 1: 69–177 ms
- Head 2: 131–337 ms  
- Head 3: 189–489 ms

When Tempo Sync is active, quantized to rhythmic note values at the leading head. Adjusting this control varies tape playback speed in realtime — produces musical ramp-up/ramp-down pitch shift effect.

### Feedback
Repeat level of echo signals. Rotate clockwise to increase repeats. High values → self-oscillation.

Self-oscillation is a key creative feature. Different Head Select modes produce different oscillation qualities (single head = simpler, multiple heads = more complex). Also achieves oscillation with no input signal.

### Treble
Adjusts high frequency response of the **tape echo signal only** (not dry signal, not reverb). Cut/boost; no effect at 12 o'clock position.

### Bass
Adjusts low frequency response of the **tape echo signal only**. Cut/boost; no effect at 12 o'clock position.

### Echo Pan
Stereo placement of the echo signal. Unavailable in mono-in/mono-out configuration.

### Echo Volume
Volume of the tape echo effect. Clockwise = louder. Minimum = echo disabled. No effect when Head Select is in REVERB ONLY position.

### Reverb Pan
Stereo placement of the spring reverb signal. Unavailable in mono-in/mono-out.

### Reverb Volume
Volume of the spring reverb effect. Clockwise = more reverb. Minimum = reverb disabled. No effect when Head Select is in positions 1–4 (echo-only positions).

### Input Send (Echo / Mute)
**The "dub" switch.** When MUTE: disables signal sent to the echo processor. Used to automate echo in/out (classic dub technique). No effect when Head Select is in REVERB ONLY.

### Tape Loop Controls

**Splice**: Resets/triggers the tape splice point. Momentary button — pops back to off immediately. Effect is delayed — splice is written at the write head, then travels over read heads (dropout), then through tape capstan (wow/flutter).

**Tape Age**: New / Used / Old tape cartridge emulation.
- New tape: pristine, less flutter
- Old tape: more character, increased wow and flutter, more chaos

### Wet Solo
ON = 100% wet (processed signal only). OFF = dry + wet mixed. Use ON when plug-in is on an aux return bus for send/return routing.

### Output Volume
Overall output level. Range: ±20 dB from unity gain. Affects both dry and wet signals. Some signal still passes at minimum.

### Tempo Sync
Synchronizes delay times to host DAW tempo.

### Power
Overall bypass. ON = processing active. OFF = dry signal passes, no processing. Toggling power also **clears the tape echo** — useful for stopping runaway self-oscillation.

### VU Meter
Displays average signal level recorded to tape (input meter). Feedback affects meter readings.

---

## Head Select Mode Summary (Simple View)

- **Positions 1–4**: Echo only, no reverb
- **Positions 5–11**: Echo + spring reverb combined
- **Reverb position**: Spring reverb only

---

## Notes for Guitar Use

- **Position 1** (single head) is the cleanest slapback delay — classic rockabilly. Set Echo Rate fully CCW for longer slap, CW for tight slap.
- **Position 5** (Heads 1+2 + reverb) gives a complex multi-tap delay with ambient spring reverb — very usable for live-sounding guitar.
- **Echo Rate knob direction**: Counter-clockwise = LONGER delay time. This is opposite of most gear and a common source of confusion.
- **Input Volume above unity**: Pushes the tape input into saturation — adds hair and warmth to guitar. Use Peak lamp as guide.
- **Treble/Bass only affect echoes**: Use them to roll off brightness on repeats for a natural tape echo decay, without affecting the dry tone.
- **Input Send (Mute)**: Automate this switch to cut guitar into the echo loop — classic David Gilmour delay technique.
- **Tape Age = Old** on guitar adds wow/flutter character that makes delays feel more alive and less grid-locked.
- **Self-oscillation at high Feedback**: Controllable runaway delay — dial Feedback to just below oscillation threshold, then push over it on held notes.
