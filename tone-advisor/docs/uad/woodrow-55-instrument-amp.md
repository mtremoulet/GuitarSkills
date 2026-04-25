# Woodrow '55 Instrument Amp — UADx

Source: https://help.uaudio.com/hc/en-us/articles/34758701036308-Woodrow-55-Instrument-Amp-Manual

---

## Overview

Emulation of a 1955 Fender Tweed Deluxe. Two channels (Instrument and Mic) that can be "jumped" together. Three boost options. Controls are standard (clockwise = more).

---

## Input Level Setup

- Connect guitar to audio interface Hi-Z input
- Set hardware preamp gain to minimum
- Set IN to center (Hi-Z) position
- For hotter signals (humbuckers, active pickups): reduce IN toward LINE

---

## Controls

### IN
Input level to plug-in. Center = Hi-Z (default). Minimum = LINE. Does not change when loading presets.

### OUT
Output level. At noon ≈ bypassed level. Use for clean level adjustment (not INST VOL or MIC VOL, which change amp character).

### Room
Amount of room tone mixed in. Only active when a speaker cabinet is selected. Noon is a good starting point.

### Tone
Adjusts treble frequencies. **Interactive with amp gain** — turning Tone up also increases overdrive and distortion. Start at noon for cleaner sounds; increase for more gain and brightness.

### INST VOL (Instrument Volume)
Instrument channel gain. Brighter and more aggressive as it increases. As volume increases, character changes — more overdrive and compression. **Not a post-amp level control; use OUT for that.**

### MIC VOL (Mic Volume)
Mic channel gain. Darker and cleaner than the Instrument channel, with more bottom end. Same gain/compression behavior as INST VOL at higher levels.

**Jumping behavior**: When both volumes are above 0, the channels are automatically "jumped" (ganged) together — you hear both simultaneously. To hear one channel alone, turn the other all the way down.

Clean range has been expanded from original hardware; more clean headroom is available than the original amp.

### Inputs (High / Low)

| Input | Description |
|-------|-------------|
| **High** | More gain and thickness. Both channels combined when both volumes > 0. |
| **Low** | Cleaner, slightly brighter. Both channels combined when both volumes > 0. |

Input setting is saved with presets (not global).

### Boost button + knob
Enable the selected boost circuit. Rotate Boost knob clockwise for more gain/effect.

### Speaker Cabinet
Select from drop-down or < > arrows. See Cabinets table below.

### On / Off
Bypasses plug-in and reduces processing load.

---

## Boost Circuits

| Boost | Description | Notes |
|-------|-------------|-------|
| **Stock** | Clean "curve" boost. Clean gain without added distortion. Midrange and treble increase slightly, bass decreases slightly as boost level increases (prevents flubby distortion). | Start here for a neutral gain boost. |
| **KP-3K** | Preamp from an 80s digital delay, made famous by The Edge. Bright and detailed. | For clean, sparkling detail: use with Low input. |
| **EP-III** | Preamp section from an EP-III tape echo. Thick and warm with plenty of additional gain. | Thickens the sound as soon as boost knob moves past zero. |

---

## Tone Shortcuts

- **JP12 + Stock**: Stock factory pairing — start with Tone halfway up
- **V30 + EP-III**: Fat lead setting — turn up boost and gain for fuzz-like qualities
- **B-Man + KP-3K**: Clean hi-fi sound with gain set low

---

## Speaker Cabinets

| Cabinet | Speaker/Cab/Mic | Notes |
|---------|-----------------|-------|
| **Blu15** | 15W Celestion Blue in 1x12 tweed combo, mic'd with 67 condenser | Darker than stock speaker |
| **JP12** | Stock Jensen P12R in 1x12 tweed combo, mic'd with 57 dynamic | Stock speaker, thinner and less aggressive |
| **GB25** | 25W Celestion Greenback in 1x12 tweed combo, mic'd with 57 dynamic | More modern, thick, clear high end; fuller with distortion |
| **V30** | Marshall 4x12 with Celestion V30s, mic'd with 421 dynamic | More bottom end chunk and fullness; great for big lead or thick rhythm |
| **B-Man** | Fender 4x10 Bassman cab with Jensen P10R, mic'd with 57 dynamic | Scooped, hi-fi clean sound; pair with KP-3K + Low input + low gain |
| **JBF120** | Fender 1x12 with vintage JBL D-120F, mic'd with 414 condenser | Bright, hi-fi, midrangey |
| **Direct** | No cabinet | Use with external cabinet emulation |

---

## Notes for Guitar Use

- **Tone King + Woodrow '55**: Tone King Rhythm channel (blackface American) into a Woodrow (tweed) creates a complex character stack. Keep Tone King Volume low to pass cleaner signal to Woodrow.
- **Tone knob warning**: The Tone control does double duty — it's not just a brightness trimmer. Cranking Tone also drives the preamp harder. Treat it like a combined Treble + Gain control.
- **Jumped channels**: The most characteristic tweed sound comes from running both INST VOL and MIC VOL together (jumped mode). The Instrument channel's brightness and the Mic channel's warmth combine into the classic tweed texture.
- **V30 cabinet** is the most versatile choice for modern guitar tones from this amp — it handles crunch and higher gain better than the stock tweed speakers.
- **Tone King IR active**: Set Woodrow cabinet to Direct and use the Tone King IR as the cab.
