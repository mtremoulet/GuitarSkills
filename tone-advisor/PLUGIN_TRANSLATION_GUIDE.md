# Plugin Translation & Scaling Guide

This guide documents the native parameter scales, ranges, and formats expected by each plugin in the `GuitarSkills` preset compilation pipeline. 

Use this document to verify scaling equations in `scripts/compile_all_presets.py` or to correctly format values in `preset_data.amp_settings` inside your toneprint markdown files.

---

## 1. Neural DSP — Archetype Cory Wong X

Neural DSP presets are binary-wrapped XML files. Parameters are represented as UTF-8 keys with a string value.

### Knob Percentage Scaling (0.0 - 1.0)
Most standard knobs in the UI (Volume, Master, Bass, Mid, Treble, Presence, Compressor Blend, Wash Reverb Mix, etc.) are displayed as **0% to 100%** to the guitarist. In the native preset XML, these must be scaled to a float between **`0.0` and `1.0`**.
* **Equation:** `plugin_value = percentage_value / 100.0`
* **Target Keys:**
  * **Pre FX (Compressor):** `compressorBlend`, `compressorCompression`, `compressorTone`, `compressorVolume`
  * **Pre FX (Big Rig OD):** `bigRigDrive`, `bigRigLevel`, `bigRigTone`
  * **Pre FX (Tuber OD):** `tuberDrive`, `tuberLevel`, `tuberTone`
  * **Amps (Amp Snob):** `snobVolume`, `snobMaster`, `snobBass`, `snobMid`, `snobTreble`, `snobPresence`, `snobOutputLevel`
  * **Amps (Clean Machine):** `cleanVolume`, `cleanBass`, `cleanMid`, `cleanTreble`, `cleanPresence`, `cleanOutputLevel`
  * **Post FX (The Wash):** `washMix`, `washDecay`

### Raw DB (Decibel) Parameters
Cabinet room mic sends and EQ band gains are specified directly in decibels (dB) in the UI, and are written as raw numbers in the XML. Do **not** divide these by 100.
* **Graphic EQ bands:** `snobEQBand1` to `snobEQBand9` (Range: `-12.0` to `12.0`)
* **Cabinet room level:** `leftRoomMicLevel`, `rightRoomMicLevel` (Range: `-40.0` to `0.0`)
* **Output Trim:** `outputGain` (Range: `-24.0` to `24.0`)

### Frequency (Hz) Parameters
High-pass and low-pass filters are written directly in Hz.
* **Graphic EQ filters:** `snobEQHpf` (e.g. `20.0`), `snobEQLpf` (e.g. `20000.0`)

### Integer / Menu Index Mappings
Stepped selectors use zero-based integer index strings:
* **Selected Amp:** `selectedAmp` (`0` = D.I. Funk Console, `1` = Clean Machine, `2` = Amp Snob)
* **Selected Cab:** `selectedCab` (`0` = Console/Direct, `1` = Clean 1x12, `2` = Snob 2x12)
* **Mic Types:** `leftCab0MicType` / `rightCab0MicType` (`4` = Ribbon 121, `0` = Dynamic 57)

---

## 2. MixWave — Two-Rock Bloomfield Drive

MixWave presets are XML-based. 

### Direct Knob Scale (0.0 - 10.0)
MixWave parameters map directly to the physical knob labels on a **0 to 10** scale (represented as float strings in the XML). Do **not** scale these to 0.0 - 1.0.
* **Equation:** `plugin_value = float_value` (e.g., `Bass: 5.5` is written as `AmpBass="5.500"`)
* **Keys:** `Gain`, `Treble`, `Middle`, `Bass`, `Presence`, `Master`, `Reverb`, `Vibe`

### Boolean Switches (0 or 1)
Switches are stored as binary integer strings in XML attributes:
* **Equation:** `"1"` for true/On, `"0"` for false/Off.
* **Keys:** `Bright`, `Mid`, `Deep`, `Tone Stack Bypass`, `Lead`

---

## 3. Valhalla DSP — Supermassive

Valhalla presets are stored as plain XML (`.vpreset`) files.

### Knob Percentage Scaling (0.0 - 1.0)
Most standard parameters are written as floats between `0.0` and `1.0`.
* **Equation:** `plugin_value = percentage_value / 100.0`
* **Keys:** `Mix`, `DelayWarp`, `Feedback`, `Density`

### Time (Seconds) Scaling
Delay times in milliseconds must be converted to seconds:
* **Equation:** `plugin_value = ms_value / 1000.0` (e.g., `800ms` = `0.8000`)
* **Keys:** `Delay_Ms`

### Mode Index Mappings
The active mode is calculated as an index divided by the total number of modes (`24.0`):
* **Equation:** `plugin_value = mode_index / 24.0` (e.g., Andromeda at Index 6 = `0.25`)

---

## 4. UADx — Native JSON Presets

Universal Audio native JSON presets contain metadata and a base64-encoded binary chunk. The compiler unpacks this chunk into a Float32 array, replaces target offsets, and re-encodes.

### LA-2A Compressor
* **Peak Reduction:** Offset 12 (scaled 0.0 to 100.0)
* **Gain:** Offset 16 (scaled 0.0 to 100.0)
* **Compress/Limit:** Offset 20 (`1.0` = Compress, `0.0` = Limit)

### Studio D Chorus
* **Dimension Mode Buttons:** Offset 40 (summed button weights divided by `15.0`)
  * `Off` = `0.0`
  * Button `1` = `0.0667` (1/15)
  * Button `2` = `0.1333` (2/15)
  * Button `3` = `0.2667` (4/15)
  * Button `4` = `0.5333` (8/15)
  * Secret Mode (All buttons) = `1.0` (15/15)

### Galaxy Tape Echo
* **Tape Age:** Offset 92 (`0.0` = New, `0.5` = Used, `1.0` = Old)
* **Feedback:** Offset 84 (scaled 0.0 to 1.0)
* **Echo Volume:** Offset 88 (scaled 0.0 to 1.0)
