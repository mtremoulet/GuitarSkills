# Tone King Imperial Preamp — Full Documentation

Source: TONE-KING-IMPERIAL-PREAMP-INSTRUCTION-MANUAL-BOOKLET.txt

---

## Overview

The Imperial All-Tube Preamp pedal delivers Tone King's legendary MKII amplifier's '50s tweed, '60s blackface, and vintage British rock tones in a compact, pedalboard-friendly format. Features the exact preamp section and phase inverter circuitry of the Imperial MKII amp, plus Reverb, Tremolo and Attenuation. Powered by three 12AX7 preamp tubes running at high voltage.

---

## Channels

### Rhythm Channel (top)
- '60s-era American blackface combo tone character
- **VOLUME**: Controls the volume of the Rhythm channel
- **ATTENUATION**: Determines how much the signal is attenuated after the phase inverter (poweramp simulation). Use as master volume control.
- **BASS**: Controls the amount of low frequencies
- **TREBLE**: Controls the amount of high frequencies
- **CAB SWITCH**: 3-way Cabinet/IR Preset Selector (programmable via software)

### Lead Channel (bottom)
- '50s-era American tweed combo and British rock tones character
- **VOLUME**: Controls the volume of the Lead channel
- **ATTENUATION**: Determines how much the signal is attenuated after the phase inverter (poweramp simulation). Use as master volume control.
- **TONE**: Controls the amount of high frequency contour
- **MID-BITE**: Transforms the basic tweed tone to more of a crunchy rock tone as it is turned up. Accomplished by simultaneously: tightening up the bass, rolling off the very high frequencies, increasing the gain, resulting in a pronounced upper midrange peak.
- **CAB SWITCH**: 3-way Cabinet/IR Preset Selector (programmable via software)

---

## Shared Effects (independently assignable per channel)

### Reverb (spring convolution)
- **LEVEL**: Mix control for the Reverb
- **DWELL**: Decay time control for the Reverb
- Engage: Long press the TREMOLO button to activate Reverb. LED indicates ON/OFF.
- Independently assignable to each channel — can be on for one channel, off for the other.

### Tremolo (digital)
- **DEPTH**: Sets the intensity of the Tremolo effect
- **SPEED**: Sets the speed of the modulation. Lower settings produce a smooth, floating sound. Higher settings produce a rotor-like effect.
- Engage: Press the TREMOLO button. LED indicates ON/OFF.
- Independently assignable to each channel.

---

## IR/Cabinet Simulation

- **CAB SWITCH** (per channel): 3-position selector for Cabinet/IR preset
- **IR BYPASS**: Long press BYPASS footswitch to toggle IR bypass. Can also be controlled via software.
- IR simulation can be bypassed — use when running into a guitar amp's power amp section, or when using Logic amp/cab simulations instead.

### Included IRs (pre-loaded)
1. **OH 112 Imperial TK1660** — Tone King TK1660 in a Tone King Imperial 1x12 combo. Captured by Kevin Rowe (OwnHammer) using SM57, Neumann U87, Royer 121 through API 312 preamps.
2. **OH 212 Class A Blue** — Celestion Blues from 1963 in a Vox AC30 2x12. Captured using SM57, Neumann U87, Royer 121 through API 312 preamps.
3. **OH 412 Basketweave M25** — Celestion G12M-25s from 1971 in a basketweave 1960B 4x12. Captured using SM57, Telefunken MD421, Royer 121 through API 312 preamps.

Additional IRs can be loaded via Tone King Editor software (15 OwnHammer custom IRs included in internal library; external WAV files 44.1K–96K supported).

---

## Footswitches

- **CHANNEL FOOTSWITCH**: Short press — toggle Rhythm/Lead channel. Long press — Loop Bypass.
- **TREMOLO FOOTSWITCH**: Short press — activate Tremolo. Long press — activate Reverb.
- **BYPASS FOOTSWITCH**: Short press — True Bypass the preamp (channel indicator pulses). Long press — IR Bypass.

---

## MIDI / Presets

- Save up to 128 presets for instant recall via external MIDI switcher
- Presets save: channel selection, master bypass, IR selection, IR bypass, FX loop bypass, reverb bypass/tails, tremolo bypass
- STORE: Simultaneously long press TREMOLO and CHANNEL buttons to store current preset on active MIDI preset number
- **MIDI CHANNEL**: Default is OMNI (receives on all channels)
- Supports MIDI CC commands (listed in Editor software)

---

## Software Controls (Tone King Editor, powered by SYNERGY)

- **HF COMP** (per channel): Compensates for high frequency loss caused by the attenuator
- **LOWPASS** (per channel): 3 levels of lowpass filtering
- **REVERB TAILS**: Select whether reverb tails continue when switching presets or channels
- **BYPASS LOCK**: Lock the bypass switch to prevent accidental bypassing
- **BYPASS toggle**: Select bypass mode on/off
- IR loading, preset programming, MIDI configuration, firmware updates

---

## Connections

### Front Panel
- **INPUT**: Guitar input jack
- **HEADPHONES**: ¼" headphone output (lower volume before wearing, then raise slowly)

### Rear Panel
- **BALANCED OUTPUTS**: Dual stereo XLR — post-IR and poweramp sim — direct to interface/PA
- **GND LIFT**: Eliminates ground loops on balanced outputs
- **EFFECTS SEND**: Master FX loop send
- **STEREO RETURN JACKS**: FX loop return (use LEFT jack for mono)
- **MIDI IN**: 5-pin standard connector
- **USB-C**: Software updates, remote programming, USB audio streaming
- **DC INPUT**: 9–12V, minimum 9W

### Expansion Jacks (for adding channels to external amp)
- **TO AMP IN**: True bypass output to external amp input (active in BYPASS mode only)
- **FROM AMP SEND**: Connect to amp's FX loop send (active in BYPASS mode only)
- **TO AMP RETURN**: Connect to amp's FX loop return (always active regardless of bypass)

---

## Key Notes for Logic Integration

- **IR active**: Do NOT simultaneously use Logic amp/cab simulations. Double-cabbing degrades tone. Use either Tone King IR with Logic post-FX only, or bypass Tone King IR and use Logic amp + cab.
- **Rhythm channel** into Logic: signal already has '60s blackface character. Logic amps add on top, not from scratch.
- **Lead channel + Mid-Bite raised**: signal is mid-forward and crunching before Logic sees it.
- **Reverb active on pedal**: avoid stacking Logic reverb unless intentional.
- **Tremolo active on pedal**: don't add Logic tremolo simultaneously.
- **Noise with headphones only**: Connect SEND, RETURN, XLR OUT, or USB to an earthed device for noise-free operation (non-earthed power supply + guitar pickups = hum pickup from environment).
