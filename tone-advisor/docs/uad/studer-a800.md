# Studer A800 Multichannel Tape Recorder — UADx

Source: https://help.uaudio.com/hc/en-us/articles/4419513099156

---

## Overview

Emulation of the Studer A800 2" analog tape recorder. Fully authenticated by Studer; modeled from Allen Sides' machine at Ocean Way Studios. Captures the full electronic signal chain including input, sync, and repro paths plus tape formulation behavior.

Albums recorded on A800: Metallica (*Black Album*), Stevie Wonder, Tom Petty, A Tribe Called Quest, Jeff Buckley.

**UADx name**: Studer A800 Tape Recorder. **UAD-2 DSP name**: Studer A800.

**Standard use**: Place as the first insert on individual tracks, before other processing. On stereo bus: emulates 2-track mixdown.

---

## Primary Controls

### Path Select

| Mode | Description |
|------|-------------|
| **Thru** | Bypass — processing disabled, DSP reduced. Same as IPS = OFF. |
| **Input** | Machine electronics only, no tape. Live monitoring simulation (transport not running). |
| **Sync** | Records and plays back via sync/record head + electronics. |
| **Repro** | Records via record head, plays back via reproduction head + electronics. Most characteristic tape sound. |

### Tape Type
Selects tape stock formulation. Four 2" tape formulas modeled:

| Formula | Cal Level | Character |
|---------|-----------|-----------|
| **250** | +3 dB (251 nWb/m) | Lower output; reaches saturation earlier |
| **456** | +6 dB (355 nWb/m) | Classic rock tape — Ampex 456 |
| **900** | +9 dB (502 nWb/m) | Higher output; cleaner headroom |
| **GP9** | +9 dB (502 nWb/m) | Higher output; similar headroom to 900 |

Lower Cal Level per formula = higher signal required to reach saturation and distortion.

### Cal Level
Sets tape calibration/fluxivity: **+3, +6, +7.5, or +9 dB**. Matches the reference flux level without changing unity gain. Manufacturer-recommended levels above (under Tape Type). Under-calibrating leaves more headroom; over-calibrating increases saturation characteristics.

Internal operating level: **-12 dBFS = 0 VU on meter**.

### IPS (Tape Speed)
Selects tape transport speed. Each speed has distinct frequency response, head bump, and distortion character.

| Speed | Character |
|-------|-----------|
| **7.5 IPS** | Maximum coloration, most frequency shift, lowest fidelity |
| **15 IPS** | Classic rock/acoustic — prominent low-frequency head bump, warmer |
| **30 IPS** | Classical/jazz standard — flattest response, lowest noise, greatest fidelity. Forces AES EQ. |
| **OFF** | Bypass — same as Thru in Path Select |

Head bump = bass frequency buildup at the tape head. Frequency of the bump shifts with IPS.

### Input
Input gain going into tape circuitry. Range: **-12 dB to +24 dB**. Lower = cleaner; higher = more harmonic saturation. Like an external console fader feeding the tape machine.

### Output
Output gain after tape circuitry. Range: **-24 dB to +12 dB**. Clean trim — does not affect saturation character.

### VU Meter
Displays signal level after the virtual tape. Higher VU = more saturation/distortion. Internal reference: -12 dBFS = 0 VU.

---

## Secondary Controls

Access by clicking the "Studer A800" label or "OPEN" text above it.

### Equaliser (Emphasis EQ)
Selects pre-emphasis/de-emphasis EQ curve standard:

| Setting | Standard | Character |
|---------|----------|-----------|
| **NAB** | American (IEC2) | Available at 7.5 and 15 IPS |
| **CCIR** | European/British (IEC) | Available at 7.5 and 15 IPS; considered technically superior; the "British sound" |
| **AES** | (auto at 30 IPS) | Fixed at 30 IPS; not selectable separately |

Also determines hum noise frequency: NAB = 60 Hz, CCIR = 50 Hz.

### Noise Enable
Global enable/disable for Hum and Hiss noise components. Each component separately controllable.

### Auto Cal
When ON: calibration controls (HF Driver Bias, HF Record EQ, Sync/Repro EQ) are automatically adjusted to manufacturer specs when Tape Type, IPS, or Emphasis EQ changes. After auto-cal, parameters can be further tweaked. When OFF: calibration values stay fixed regardless of other control changes.

### HF Driver Bias
Adjusts HF oscillator voltage to the record head. Affects record sensitivity, distortion, and tape compression character.
- **Ideal bias**: Maximum sensitivity, low distortion
- **Overbias**: Warmer, gentle saturation — classic "tape compression" on drums
- **Underbias**: Distortion, nonlinear response, gate chatter, extreme dropout

### HF Record EQ
Compensates for HF loss due to Bias optimization. Boost filter applied prior to tape non-linearity. Affects saturation characteristics.

### Sync/Repro EQ (HF and LF)
Playback calibration EQs for the sync and repro heads:
- **Sync HF/LF**: Only active when Path Select = Sync
- **Repro HF/LF**: Only active when Path Select = Repro
Can be used for calibration or creative frequency shaping.

### Noise Controls
- **Hum Noise**: ±25 dB. Frequency: 60 Hz (NAB) or 50 Hz (CCIR).
- **Hiss Noise**: ±25 dB. Disabled when Path Select = Input (hiss is a tape playback element).

### Gang Controls (UAD-2 DSP only)
Links all Studer A800 instances for simultaneous parameter adjustment. **Not available in UADx.** Not automatable, not saved with session.

---

## Notes for Guitar Use

- **Place as first insert** on the guitar track, before amp sims and other processing, for the most natural tape behavior.
- **15 IPS + 456 tape**: The classic rock formula combination — adds the head bump and warmth that defined the "analog guitar" era.
- **Input at unity or slightly above**: Gentle tape saturation without obvious distortion. Push higher for tape compression/harmonic coloring on heavy parts.
- **Repro path**: The fullest tape character. Sync = slightly more present. Input path = electronics-only color without tape saturation.
- **30 IPS for clean electric**: When tape color is wanted but head bump would cloud a clean tone — 30 IPS is flatter, tighter, less colored.
- **On the stereo bus**: Useful for the final glue — warm, low-end cohesion across the full mix.
