# Pedalboard — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 2382–2826

Add via: Amps and Pedals > Pedalboard in a channel strip Audio Effect plug-in menu.

---

## Overview

Pedalboard simulates famous "stompbox" pedal effects. Combine, reorder, and automate multiple pedals. Signal flows left to right in the Pedal area. Two discrete busses (Bus A and Bus B) with Splitter and Mixer utilities allow parallel signal processing. All knobs, switches, and sliders can be automated. Eight Macro Controls allow MIDI controller mapping.

Individual stompboxes can also be inserted directly as channel strip effects: Amps and Pedals > Stompboxes > [Category] > [Stompbox name].

---

## Interface Sections

- **Pedal Browser**: Shows all available pedal effects and utilities by category. Drag into Pedal area or double-click to add.
- **Pedal area**: Arrange and set parameters for stompboxes. Signal runs left to right.
- **Router**: Controls signal flow between Bus A (lower) and Bus B (upper). Appears when a stompbox is added; move pointer above Pedal area to show.
- **Macro Controls**: Eight Macro Targets (A–H) mapped to any stompbox parameter for real-time MIDI control.

---

## Pedal Management

- **Add a pedal**: Drag from Pedal Browser to desired position, or double-click to add at the right end
- **Replace a pedal**: Drag a new pedal from the Browser over the existing one; or select the existing pedal, then double-click the replacement in the Browser
- **Move a pedal**: Drag to new position. Automation and bus routings move with it.
- **Remove a pedal**: Drag downward out of the Pedal area, or select and press Delete

---

## Router (Bus Routing)

- **Bus A** (lower, default): All pedals added go to Bus A by default
- **Bus B** (upper): Create a second bus by clicking a pedal name in the Router
- **Splitter utility**: Splits signal between busses. Can split equally or by frequency (Freq mode).
- **Mixer utility**: Combines Bus A and Bus B signals. Automatically added when Splitter is inserted.

**Create a second bus:**
- Move pointer above Pedal area to open Router, then click the name of a stompbox — it moves to Bus B; Mixer utility is added at the end

**Splitter utility controls:**
- Frequency knob: Set the frequency for Freq mode splitting
- Split/Freq mode switch: Split = equal routing to both buses; Freq = signals above Frequency → Bus B, below → Bus A

**Mixer utility controls:**
- Mix fader: Level or level balance between buses
- A/Mix/B switch: Solo Bus A, mix both, or solo Bus B
- Pan A/B knobs: Pan position for each bus

---

## Macro Controls

Eight Macro Targets (A–H) for MIDI mapping:
- **Macro Target pop-up menus**: Choose parameter to control (shown as: Slot number — Pedal Name — Parameter)
- **Macro Value sliders**: Set/display current value for the parameter
- Click the disclosure arrow (lower left) to show/hide Macro Controls area
- Auto-assign: Choose "Auto assign" from any Macro Target menu, then click the parameter in any pedal

---

## Stompboxes: Delay Pedals

| Pedal | Controls | Character |
|-------|----------|-----------|
| **Blue Echo** | Time, Repeats, Mix, Tone Cut (Lo/Hi/Off), Mute, Sync | Simple delay effect |
| **Spring Box** | Time, Tone, Style (Boutique/Simple/Vintage/Bright/Resonant), Mix | Spring reverb emulation |
| **Tie Dye Delay** | Time, Feedback, Tone, Bright/Dark switch, Mix, Listen, Sync | Warm reverse delay; 1960s–70s psychedelic |
| **Tru-Tape Delay** | Norm/Reverse switch, Lo/Hi Cut, Dirt, Flutter, Time, Feedback, Mix, Sync | Vintage tape echo emulation |

---

## Stompboxes: Distortion Pedals

| Pedal | Controls | Character |
|-------|----------|-----------|
| **Candy Fuzz** | Drive, Level | Bright, nasty distortion |
| **Double Dragon** | Drive, Tone, Level, Input, Squash, Contour, Mix, Bright/Fat | Deluxe distortion with compression |
| **Fuzz Machine** | Fuzz, Level, Tone (increases treble, reduces lows at higher values) | American fuzz distortion |
| **Grinder** | Grind, Filter, Level, Full/Scoop switch | Lo-fi metal distortion |
| **Grit** | Volume, Filter, Distortion | Hard, nasty filtered distortion |
| **Happy Face Fuzz** | Fuzz, Volume | Softer, full-sounding distortion |
| **Hi-Drive** | Level, Treble/Full switch | Overdrive emphasizing high frequency content |
| **Monster Fuzz** | Roar, Growl, Tone, Texture, Grain, Level | Saturated, slightly harsh distortion |
| **Octafuzz** | Fuzz, Level, Tone (highpass filter cutoff) | Fat fuzz with soft saturated distortion |
| **Rawk! Distortion** | Crunch, Level, Tone | Metal/hard rock distortion |
| **Tube Burner** | Fat switch, Low, Mid Freq, Mid Gain, High, Tone, Bias, Squash, Drive, Output | Wide palette: warm grain to crispy overdrive; tube emulation |
| **Vintage Drive** | Tone, Drive, Level, Fat switch | FET overdrive; warmer distortion than bipolar transistor emulation |

---

## Stompboxes: Dynamics Pedals

| Pedal | Controls | Character |
|-------|----------|-----------|
| **Squash Compressor** | Sustain (threshold), Level, Attack (Fast/Slow) | Simple compressor |

---

## Stompboxes: Filter Pedals

| Pedal | Controls | Character |
|-------|----------|-----------|
| **Auto-Funk** | Sensitivity, Cutoff, BP/LP switch, Hi/Lo switch, Up/Down switch | Auto-wah (filter) effect |
| **Classic Wah** | Drag vertically to control filter cutoff | 1970s-style wah; classic TV police show sound |
| **Graphic EQ** | 7 frequency sliders, Level slider | Classic 7-band EQ pedal |
| **Modern Wah** | Drag vertically for cutoff; Q knob, Mode knob | More aggressive wah; adjustable Q and type |

---

## Stompboxes: Modulation Pedals

| Pedal | Controls | Character |
|-------|----------|-----------|
| **Flange Factory** | Rate, Depth, Reso, Mix, Wave, Symmetry, Curve, Manual, Low, High, Sync | Deluxe flanging; precise sound control |
| **Heavenly Chorus** | Rate, Depth, Bright switch, Feedback, Density, Sync | Rich, sweet chorus; thickens sound |
| **Phase Tripper** | Rate, Depth, Feedback, Sync | Simple phasing |
| **Phaze 2** | LFO 1/2 Rate, Floor/Ceiling, Order, Feedback, Tone; LFO Mix, Sync | Flexible dual phaser |
| **Retro Chorus** | Rate, Depth, Sync | Subtle vintage chorus |
| **Robo Flanger** | Rate, Depth, Feedback, Manual, Sync | Flexible flanging; high Feedback + Manual = metallic modulations |
| **Roswell Ringer** | Lin/Exp switch, Freq, Fine, FB (Feedback), Mix | Ring modulation; metallic tones, tremolos, pitch brightening |
| **Roto Phase** | Rate, Intensity, Vintage/Modern switch, Sync | Phaser with signal movement; Vintage mode adds fixed-frequency EQ |
| **Spin Box** | Cabinet, Fast Rate, Response, Drive, Bright, Slow/Brake/Fast buttons | Leslie rotor speaker cabinet emulation |
| **The Vibe** | Rate, Depth, Type (V1–3, C1–3), Sync | Vibrato/chorus based on Hammond B3 Scanner Vibrato |
| **Total Tremolo** | Rate, Depth, Wave, Smooth, Volume, ½ Speed, 2× Speed, Speed Up, Slow Down, Sync | Flexible tremolo with waveform control |
| **Trem-O-Tone** | Rate, Depth, Level, Sync | Simple tremolo |

---

## Stompboxes: Pitch Pedals

| Pedal | Controls | Character |
|-------|----------|-----------|
| **Dr. Octave** | Octave 1/2 knobs, Direct, Drive | Classic octaver with two independent octave controls + overdrive |
| **Wham** | Drag vertically for pitch shift; Tune, Mix | Pedal-controlled pitch shifter |

---

## Notes for Guitar Use

- Use Pedalboard **before** Amp Designer in the signal chain for pre-amp effects (drives, wahs)
- Use Pedalboard **after** Amp Designer for post-amp modulation and delay (or use individual effect slots)
- The **Tube Burner** is the most versatile distortion pedal — covers warm grain to crispy overdrive and includes internal compression (Squash) and 3-band EQ
- **Vintage Drive** is closest to classic FET overdrive pedal emulation (TS-808 territory)
- **Bus A/B parallel routing** with the Splitter is useful for running a clean dry signal alongside an effected signal
