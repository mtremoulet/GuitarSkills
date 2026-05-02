# Acoustic Voice Pro — Nembrini Audio

Source: https://nembriniaudiodownload.blob.core.windows.net/installer/AcousticVoicePro/Manual.pdf

---

## Overview

Acoustic guitar preamplifier plugin that transforms direct pickup signals into studio-quality acoustic performances. Combines body modeling, microphone simulation, IR loading, EQ, stomp pedals, and a post-effects rack. Designed for both piezo and magnetic pickups — selectable via Input Mode.

---

## Top Toolbar

| Control | Function |
|---------|---------|
| INPUT LEVEL knob | Overall input gain into the plugin |
| FIX INPUT button | Locks input level constant when switching presets |
| Navigation icons | Switch between Guitar/IR Loader, Stomp, Graphic EQ, and FX views |
| OUTPUT LEVEL knob | Overall output level leaving the plugin |

---

## GUITARS View — Core Acoustic Modeling

### 1. Input Mode

**Critical for correct processing** — select the mode matching your pickup type.

| Mode | Use for |
|------|---------|
| AC Magnetic | Acoustic guitar with magnetic soundhole pickup |
| Single | Electric guitar with single-coil pickups |
| Humbucker | Electric guitar with humbuckers |
| Piezo | Acoustic guitar with undersaddle piezo pickup |

Use left/right arrows to scroll through modes.

*For Sheraton (humbuckers): set Input Mode to **Humbucker**.*

### 2. Guitar Models

10 acoustic body emulations. Use left/right arrows to scroll.

| ID | Based On | Character |
|----|----------|-----------|
| MART 1936 0-17 | Martin 1936 0-17 | Small vintage parlor — dry, intimate, very woody |
| WEISS LAP-SLIDE | Weissenborn hollow-neck | Lap steel resonance — unusual, not suited for standard blend |
| MART 0028 | Martin 0028EC (Eric Clapton sig) | Medium body, balanced, slightly warm |
| MART HD28V | Martin HD-28V | Dreadnought — full projection, strong low end |
| GIB 00 | Gibson L-00 | Small parlor, warm low-mids, intimate — good for blending under electric |
| LAND 80 | Landola J80E | Jumbo — large, boomy, lots of low end |
| GUI 140 | Guild D140CE | Dreadnought — clear and projecting |
| AY DSR | Ayers DSR | Dreadnought — balanced and articulate |
| TAY 814 | Taylor 814ce Deluxe | Grand Auditorium — balanced, neutral, modern voicing |
| TAY GTK21E | Taylor Grand Theater K21e | Small parlor-sized Taylor — focused and clear |

*For jazz blend under humbuckers: GIB 00 (first choice) or TAY 814 (second). Avoid dreadnoughts and jumbos when blending under electric — too much competing low end.*

### 3. Microphone

Five mic emulations. Each has adjustable Position and Distance.

| ID | Based On | Character |
|----|----------|-----------|
| CONDENSER 51 | Audix ADX51 | Clear and detailed — small diaphragm condenser |
| DYNAMIC 201 | Beyerdynamic M201 | Dynamic — focused, present |
| DYNAMIC 57 | Shure SM57 | Punchy and controlled — universal workhorse |
| DYNAMIC RE20 | Electro-Voice RE20 | Natural, extended low end |
| CONDENSER 414 | AKG C414 | Open and polished — large diaphragm condenser |

- **Position**: moves mic along guitar body (neck → soundhole → bridge)
- **Distance**: controls proximity to guitar body — affects presence and room ambience

### 4. Mixer

| Control | Function |
|---------|---------|
| Gain | Output level of the processed acoustic signal |
| Pan | Stereo position |
| Blend | Mix between original pickup signal and modeled acoustic sound. 0% = dry pickup only; 100% = full acoustic modeling |

*Blend is the primary dry/wet control for the acoustic model.*

---

## IR LOADER View

Single IR slot. Controls:
- **Empty**: unload current IR
- **Load**: file browser for custom IR files
- **Blend**: mixes IR signal with original signal
- **Pan**: stereo position of IR signal
- **Level Slider**: output level of IR
- **Frequency Response Display**: visual curve of loaded IR
- **IR Browser**: Factory (built-in IRs) or Browse (custom folder) modes

---

## GRAPHIC EQ View — 6-Band Equalizer

6 independent bands. Each band is fully configurable.

| Control | Function |
|---------|---------|
| POWER | Enables/bypasses the entire EQ section |
| BAND POWER / Filter LED | Enables/bypasses the selected band |
| GAIN | Gain of selected band (dB) |
| Q FACTOR | Bandwidth of selected band |
| FREQUENCY | Center frequency of selected band (Hz) |
| Filter Type | Click arrows or band name to cycle: High Pass, Low Pass, Notch, Peak, High Shelf, Low Shelf |
| RESET | Resets selected band to default |
| RESET ALL | Resets all 6 bands |

**Interaction:** Grab a band point to adjust Gain and Frequency simultaneously. CTRL+drag to adjust Q Factor.

*Notch is a proper filter type in this EQ — it is distinct from a Peak filter with negative gain.*

---

## STOMP View — Pedal Section

Four pedal-style processors, used before the main effects stage. Each has a Switch to activate/bypass.

### Noise Gate

| Control | Function |
|---------|---------|
| RANGE | Amount of signal reduction when gate is closed |
| GATE | Attack time — how quickly gate responds (faster = immediate clamp; slower = natural fade) |
| THRESHOLD | Signal level at which gate activates |
| SWITCH | On/off |

### Compressor

| Control | Function |
|---------|---------|
| THRESHOLD | Level at which compression begins |
| RATIO | Compression amount above threshold |
| OUTPUT | Output level after gain reduction |
| ATTACK | How quickly compressor reacts to signal exceeding threshold |
| RELEASE | How quickly compressor stops compressing after signal drops below threshold |
| GAIN REDUCTION | LED indicator of active compression amount |
| SWITCH | On/off |

### Doubler

Stereo widening via dynamic panning and pitch detuning.

| Control | Function |
|---------|---------|
| SENSITIVITY | Sensitivity of transient detector that triggers stereo panning |
| PITCH | Amount of pitch detuning applied to stereo channels |
| MONO | Cutoff frequency below which low end is summed to mono |
| OFFSET | Maximum time offset between L and R channels |
| SWITCH | On/off |

### DI Preamp

**Contains a dedicated Notch filter for resonance removal** — this is the designed tool for notching problematic frequencies (humbucker nasal peaks, feedback resonances), not the EQ.

| Control | Function |
|---------|---------|
| GAIN | Input gain of the preamp stage |
| NOTCH | Sweeps notch filter across frequency spectrum — set at the resonance frequency you want to remove |
| BLEND | Mixes direct input with processed signal |
| OUTPUT | Output level of DI preamp stage |
| SWITCH | On/off |

---

## FX View — Post Effects

### Analog Delay

| Control | Function |
|---------|---------|
| TIME | Delay time (interval between dry and delayed signal) |
| SYNC | Sync delay time to host DAW tempo |
| SWELL | Shapes how delayed signal fades in and blends |
| FEEDBACK | How much delayed signal feeds back — higher = more repeats |
| SPREAD | Stereo width of delay repeats |
| TONE | Tonal character of delayed signal (lower = darker; higher = brighter) |
| SMEAR | Diffusion of repeats — higher = more ambient/softer echoes |
| MIX | Dry/wet balance |
| POWER | On/off |

### Reverb

| Control | Function |
|---------|---------|
| PRE DELAY | Time between dry signal and onset of reverb reflections |
| SIZE | Size of virtual room — lower = smaller/tighter; higher = larger |
| TONE | Tonal character of reverb tail |
| MIX | Dry/wet balance |
| POWER | On/off |

### Modulation

| Control | Function |
|---------|---------|
| SPEED | Modulation rate |
| SYNC | Sync to host DAW tempo |
| DEPTH | Modulation depth |
| INTENSITY | Overall strength/character of modulation |
| TYPE | Select: Chorus (detuned copies, wider sound) / Flanger (sweeping jet effect) / Tremolo (rhythmic volume variation) |
| POWER | On/off |

---

## Notes for Guitar Use

- **Always set Input Mode first** — incorrect mode will produce incorrect body modeling. For humbuckers (Sheraton), always select Humbucker mode.
- **DI Preamp Notch vs EQ Notch**: The DI Preamp has a dedicated swept notch for resonance removal — use it for tracking down and eliminating specific problem frequencies. The EQ provides a full 6-band parametric EQ with all filter types for broader tone shaping. Both can be used together.
- **Mixer Blend control**: This is the dry/wet for the entire acoustic modeling — set to taste between dry pickup and processed acoustic sound.
- **Post-Effects (FX) for this rig**: When reverb is handled externally (on a Logic bus), leave the internal Reverb Power OFF. Use internal Reverb only for a quick standalone preset.
- **Beyerdynamic mic is M201** (Dynamic 201), not M210 — the plugin name is DYNAMIC 201.
