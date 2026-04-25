# Sound City Studios — UADx

Source: https://help.uaudio.com/hc/en-us/articles/18738187503380-Sound-City-Studios-Manual

---

## Overview

A "studio in a box" built on the "re-miking" concept — plays audio through Sound City Studios' room via loudspeakers and captures it with mic selections. Models the famous Van Nuys, CA studio where Nirvana, Metallica, Fleetwood Mac, and Rage Against the Machine recorded. Includes the iconic Sound City console tone, outboard dynamics, and reverb chamber.

**Key concept**: The plug-in radiates your audio's energy pattern through a modeled room, capturing it with selectable mics. This is fundamentally different from a reverb — the room's response is specific to the source type chosen.

---

## Modes

### Re-Mic
Entirely replaces your recording with Sound City Studios' complete room + mic characteristics. Retains the "direct path" (source-to-mic) component. **Do NOT mix the original dry signal with the Re-Mic output** — phase issues will occur. Predelay and Mix are unavailable in Re-Mic mode.

### Reverb
Works as a short reverb effect. Removes the direct-path component — only early reflections and decay are heard. Predelay, Mix, and Wet Solo are available. Use in a send/return configuration.

---

## Views

### Studio View
Main view showing the room with mic positions. Controls: Mode switch, Source category/type, Room/EQ/Dynamics/Chamber enable toggles, mic selectors (Close/Room 1/Room 2), mic level sliders, mic position (drag to move).

### Mixer View
Per-channel: Distance knob, Align (time-align) button, High Cut + Low Cut filters, Polarity invert, Mute, Balance, Gain fader (off to +10 dB). Master section: Bypass (disables room), L/R Swap, Mono, Master fader.

**Reverb mode only in Mixer**: Predelay (0–125 ms), Mix, Wet Solo.

### Master Effects View
Three effect modules (can be reordered by dragging): Equalizer, Dynamics, Chamber. Toggle each with IN button.

---

## Sources

Source categories: Drums, Acoustic, Speakers, Vocal, Ensemble. Each source models specific radiating energy patterns. **Any audio type can be used with any source** — experimentation encouraged.

When a source is changed, mic options and positions reset to curated defaults.

---

## Microphone Controls

- **Distance knob**: Varies mic-to-source distance. Available range depends on source + mic type. Some mics are FIXED (cannot be moved). Click DISTANCE label to return to default.
- **Align button**: Eliminates time delay between source and mics while maintaining room character. Useful for mixing multiple mic channels.
- **High Cut / Low Cut filters**: Console-derived filters per channel (see filter values below)
- **Polarity**: Inverts channel phase
- **Mute**: Disables channel. Shift-click Mute to solo that channel.
- **Balance**: L/R pan for stereo pairs, mono pan for single mics
- **Gain fader**: Off to +10 dB. Unity = 0.
- **Mic polar patterns**: Some mics switchable between cardioid and omni
- **On/Off-axis**: Speaker (cabinet) sources can be miked on-axis (brighter/edgier) or off-axis (smoother/darker)

---

## Cut Filter Values by Source

### Speaker (2x12 and 4x12 Cabinets)
| Channel | Low Cut | High Cut |
|---------|---------|----------|
| Close | 70 Hz | 8 kHz |
| Room 1 | 160 Hz | 6 kHz |
| Room 2 | 160 Hz | 6 kHz |

### Drums (Live / Tight / Corner)
| Channel | Low Cut | High Cut |
|---------|---------|----------|
| Close | 45 Hz | 10 kHz |
| Room 1 | 70 Hz | 8 kHz |
| Room 2 | 70 Hz | 8 kHz |

### All Other Sources
| Channel | Low Cut | High Cut |
|---------|---------|----------|
| Close | 70 Hz | 10 kHz |
| Room 1 | 160 Hz | 8 kHz |
| Room 2 | 160 Hz | 8 kHz |

---

## Available Microphones

| Mic | Type | Character |
|-----|------|-----------|
| **77DX** | Figure-8 ribbon (mono) | American classic; found on many SCS sessions |
| **C12** | Large-diaphragm condenser (mono cardioid) | Clear and present |
| **C24** | Stereo large-diaphragm condenser | Fantastic off-axis response; stereo omni |
| **C414** | Large-diaphragm condenser | Studio staple since early '70s; versatile |
| **U67** | Tube large-diaphragm condenser | Warm, smooth; stereo pairs or close cabinet |
| **KM54** | Tube medium-diaphragm cardioid | Max on-axis sensitivity; vintage tone |
| **KM84** | Small-diaphragm condenser | Incredible transient response; fine detail |
| **M160** | Double-ribbon (mono) | Vintage vibe; good on/off-axis on cabs |
| **SM57** | Cardioid dynamic | 50+ year studio workhorse for guitar cabs |

---

## Equalizer (3-Band Semi-Parametric, based on Sound City console)

| Band | Stepped Frequencies | Gain Range |
|------|-------------------|-----------|
| **Low Shelf** | 35, 60, 110, 220 Hz | ±15 dB |
| **Mid** | 350, 700, 1.6k, 3.2k, 4.8k, 7.2 kHz | ±20 dB |
| **High Shelf** | 10, 12, 16 kHz | ±20 dB |

---

## Dynamics Module (6 Types)

| Type | Description |
|------|-------------|
| **Excite** | Dolby A noise reduction engaged on input only — multi-band dynamic effect similar to an exciter |
| **Air** | "Stretch mod" — disables two lower Dolby A bands for airy, hyped multi-band expansion. Use Mix control to blend. |
| **Crush** | Modified single-band Dolby A — 4:1 compression, aggressive but transparent room crush |
| **Gated** | Gate before Crush compressor. Gate not affected by Mix — set Mix to 0% for gate-only |
| **Bus** | Diode-based console compressor — 2:1 ratio, multi-stage auto release. Transparent bus or vocal compression. |
| **1176LN** | Classic UA 1176 FET limiter at 20:1. Progressively faster attack + release as Amount increases. |

**Amount**: Dial in gain reduction/expansion amount (clockwise = more)
**Mix**: Parallel wet/dry blend for the dynamics processor
**SC Link**: Linked (stereo) or Unlinked (dual mono) sidechain
**SC Filter**: Tilt (3dB/oct), Off, or Low Cut (12dB/oct at 150 Hz)

---

## Chamber (Sound City Studios Reverb Chamber)

Built-in reverb chamber from Sound City Studios' own chamber space.

| Control | Description |
|---------|-------------|
| **Mics** | KM84 (spaced cardioid condensers — crisp detail), R121 (Blumlein ribbon — natural balance), RE50 (spaced omni dynamic — wide reach, natural rolloff) |
| **Amount** | Chamber return level 0–100% (not a dry/wet mix — a reverb return level) |
| **Decay** | Five positions: Long → Short (Long = natural Sound City chamber) |
| **Predelay** | 0–250 ms |
| **Width** | 0% (mono) to 100% (full stereo) |

---

## Mix Control (Reverb Mode Only)

Controls dry/wet balance when used as an insert. Uses logarithmic taper: **at noon (12 o'clock), Mix = approximately 15%**, not 50%. When Wet Solo is enabled, Mix has no effect.

---

## Notes for Guitar Use

- **Speakers source + 2x12 or 4x12 cabinet**: This is the primary guitar use case — Sound City Studios re-mics your guitar signal through the studio room. Choose the SM57 or M160 for close mics.
- **On-axis vs off-axis Close mic**: On-axis = more bite and presence; off-axis = smoother. Most useful A/B decision for guitar cabinet tones.
- **Re-Mic mode for guitar re-amping**: Place on a direct guitar track or already-effected guitar bus to push it through the room. Do NOT mix with the dry signal.
- **Reverb mode for guitar ambience**: Place on a send bus with Wet Solo enabled. Adds room sound without replacing the original tone.
- **Dynamics: 1176LN type** is the most predictable for guitar — same character as the standalone 1176 at 20:1.
- **Dynamics: Excite type** on guitar adds harmonic enhancement similar to a treble booster or exciter — useful for adding air to already-processed guitar tones.
- **Chamber with KM84 mics + Short decay**: The most guitar-friendly chamber setting — tight, bright, present reverb tail without excessive wash.
