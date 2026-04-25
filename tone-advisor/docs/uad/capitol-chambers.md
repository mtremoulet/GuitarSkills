# Capitol Chambers — UADx

Source: https://help.uaudio.com/hc/en-us/articles/18741463946516-Capitol-Chambers-Manual

---

## Overview

Emulation of the four echo chambers beneath the Capitol Records Tower in Los Angeles. Not a convolution reverb — uses UA's Dynamic Room Modeling, a hybrid of sampled impulse responses + algorithmic DSP for dynamic customization. Full signal chain emulation including Capitol's custom amplifiers, speakers, preamps, and mics.

**Latency warning**: Capitol Chambers has higher latency than other UAD plug-ins. Use on an aux send/return bus, not as a direct insert on tracks when tracking live.

---

## Chambers

| Chamber | Speaker | Notes |
|---------|---------|-------|
| **2** | Altec 604 Duplex with JBL LE-175 horn + JBL crossover | Rich, low-mid soundfield; era-spanning custom Capitol pairing |
| **4** | Altec A7 Voice of the Theatre with Altec 802 horn | "Al's chamber" — Capitol's most in-demand option. Most balanced sound. Shortest natural decay. |
| **6** | Altec 604 Duplex | Original 1950s installation. Warm, long decay. |
| **7** | Tannoy System 8 | Longest, most linear decay. Full range. English 1980s coaxial speakers. |

Natural decay range: ~5 to 9.5 seconds depending on chamber. Decay control can reduce down to 1 second minimum.

---

## Microphones

| Mic | Type | Notes |
|-----|------|-------|
| **Altec 21D** | Small diaphragm omnidirectional tube condenser | Original installation. Chambers 4 and 6 have historically accurate configurations with band-limited frequency response. |
| **RCA 44** | Figure-8 ribbon | Complex and colored yet controlled. Strong proximity characteristics. |
| **Shure SM80** | Small diaphragm omnidirectional condenser | Current installation (since early 1980s). Broad reach, uniform frequency range. |
| **Sony C37A** | Medium diaphragm tube condenser (cardioid) | Elevated, refined sound. Moderate proximity characteristics. |

---

## Controls

### Chamber Select
Four yellow buttons — selects the active echo chamber. Recalculation occurs on change (flashing antenna indicator).

### Microphones Select
Buttons to choose the stereo mic pair. Recalculation occurs on change. Open door icon appears during recalculation.

### Microphones Position
Slider controlling distance between mic pair and speaker. Also draggable within the Chamber View.
- **MAXIMUM** = original mic positions as captured at Capitol Studios
- Below MAXIMUM = algorithmically adjusted, bringing mics closer to speaker = tighter room, more present source
- Closest positions create proximity gain and bass buildup

**Use Wet Solo active** (or Mix at 100%) when auditioning position changes — subtle when dry signal is audible.

### Predelay
Time between dry signal and onset of reverb. Range: 0–250 ms (logarithmic scale — finer resolution at lower values).

### Decay
Reverberation time. Counter-clockwise = shorter decay. MAX = natural room decay as captured. Minimum = 1 second.
- Recalculation occurs on change (flashing antenna)
- This is a "beyond physics" digital control — not possible with real chambers

### Filter
High-pass filter on the reverb return path. 6 dB/octave. Range: 80 Hz to 750 Hz (continuously variable), or OFF.
- Rotate clockwise to cut more low end
- Click "OFF" label to disable/re-enable

### EQ
Three-band equalization on the reverb return path. ±10 dB per band.

| Band | Center Frequency | Type |
|------|-----------------|------|
| **Bass** | 125 Hz | Baxandall shelf |
| **Mid** | 500 Hz | Proportional Q |
| **Treble** | 5 kHz | Baxandall shelf |

Click a band's frequency label to reset to 0 dB.

### Mix
Blend between dry and wet signals. Range: 0% (dry only) to 100% (wet only).

**CRITICAL**: Mix uses a logarithmic scale. **At noon (12 o'clock), Mix = 15%, not 50%.** For 50% wet, the knob must be set well past noon.

Click "0" or "100" labels to jump to those values.

### Wet Solo
Puts plug-in into 100% wet mode — dry signal muted, Mix has no effect. Use when plug-in is on an aux return bus. State is global (per instance) and does NOT change when a preset is loaded.

### Width
Narrows stereo imaging of the reverb. 0% = mono reverb. 100% = natural stereo as captured.

### Power
Enables/disables the plug-in.

---

## Automation Notes

| Parameter | Automation |
|-----------|-----------|
| Chamber Select, Microphones Select, Decay | Not recommended (time lag / sonic artifacts) |
| Microphones Position | Static snapshot automation only, between audio passages |
| All other parameters | Continuous and static snapshot OK |

---

## Notes for Guitar Use

- **Chamber 4** (Altec A7) is the most versatile starting point — balanced sound, shortest decay, historically accurate.
- **Chamber 7** (Tannoy) is ideal for long ambient guitar reverb tails — the longest, most linear decay.
- **Mix at noon ≠ 50%** — this is the most important thing to know. Start with Mix around 3 o'clock for meaningful reverb presence.
- **Filter**: Use to cut low end of the reverb return (muddiness below 100–200 Hz is common on guitar reverb). Set between 150–300 Hz for guitar.
- **Wet Solo on the send bus**: Capitol Chambers is designed for aux send routing, not direct inserts. Insert on an aux return with Wet Solo enabled; send to it from the guitar channel.
- **Altec 21D mics** in Chamber 4 give the most colored, vintage-sounding result — great for '60s-style guitar reverb.
- **Shure SM80 mics** give the most modern and neutral reverb character.
