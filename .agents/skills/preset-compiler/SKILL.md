---
name: preset-compiler
description: >
  Dynamic preset mapping and compiler guide. Use this skill when adding support for a new plugin,
  mapping binary/JSON/XML preset formats (UADx JSON, Valhalla XML, Nembrini XML, Logic PST, Neural DSP XML),
  diagnosing offset shifts, or modifying the rig compilation pipeline.
allowed-tools: Read, Write, Edit, Glob, Bash
---

# GuitarSkills — Preset Compiler & Plugin Mapper

This skill documents and codifies the technical playbook for the rig-wide dynamic preset generation system in Mike's `GuitarSkills` project. Use this guide whenever you need to:
1. Map a new plugin's parameters (finding float/int offsets).
2. Add support for a new plugin or format in `scripts/preset_compiler/`.
3. Use standardized parameter converters from `scripts.utils.param_types`.
4. Understand binary, JSON, or XML-based preset structures.
5. Reference the future backlog for UADx Capitol Chambers and UA 610-B.

---

## 1. System Overview

The core objective of the preset compiler is **rig-wide automation staging**: taking a single descriptive markdown toneprint (under `tones/`) and automatically compiling native user presets for every plugin in the track's signal chain. This allows Mike to load a single tone index and instantly stage all amplifiers, dynamic controllers, EQ settings, and spatial effects in Logic Pro.

```
                      +-------------------------+
                      |  tones/[toneprint].md   |
                      +------------+------------+
                                   |
                       (Recursive Scan Loop)
                                   v
                   +---------------+---------------+
                   | scripts/compile_all_presets.py|
                   +---------------+---------------+
                                   |
       +---------------------------+---------------------------+
       |                           |                           |
       v                           v                           v
 [scripts/preset_compiler/   [scripts/preset_compiler/   [scripts/preset_compiler/
    uad.py, neural.py]          valhalla.py]               nembrini.py, etc.]
       |                           |                           |
       v                           v                           v
[UADx Native JSON]         [Valhalla Plain XML]       [Nembrini Plain XML]
(Galaxy, Studio D)            (Supermassive)         (JC120, MRH810, AVP)
       |                           |                           |
       v                           v                           v
~/Documents/Universal       /Library/Application       ~/Documents/Nembrini
  Audio/Presets/...           Support/Valhalla...           Audio/...
```

---

## 2. Parameter Normalization (`scripts.utils.param_types`)

Always use `scripts.utils.param_types` for safe, strongly-typed parameter parsing in all compiler handlers:

- **`to_float(val, default=0.0, min_val=None, max_val=None, scale_percent=False)`**: Strips units (`dB`, `%`, `Hz`, `ms`), converts unicode minus (`−`), scales percentages (if `scale_percent=True`), handles strings/floats/ints.
- **`to_bool(val, default=False)`**: Safely converts `"ON"`, `"OFF"`, `"TRUE"`, `"FALSE"`, `"BRIGHT"`, `"NORMAL"`, `"YES"`, `"NO"`, `1`, `0` to boolean.
- **`to_db(val, default=0.0)`**: Strips `"dB"`, `"db"`, `"+"`, returning float dB.
- **`to_freq(val, default=1000.0)`**: Parses `"1.5 kHz"`, `"800 Hz"`, returning Hz.
- **`find_numeric_param(content, param_names)`**: Finds table cells matching `param_names` and parses float value with auto percentage scaling.
- **`find_boolean_param(content, param_names)`**: Finds table cells matching `param_names` and parses boolean state.

---

## 3. Playbook for Mapping & Adding a New Plugin

Whenever Mike purchases a new plugin or wants to add a new device to the compiler, follow this standard workflow:

### Step 1: Save Diagnostic Presets
Open **Logic Pro**, load the plugin on a track, and save a series of custom baseline presets **using the plugin's internal preset menu** (not Logic's frame). Save:
1. `Plugin_Base`: Default setting.
2. `Plugin_Control10`: Change only **Control 1** to max value (`10` or `100%`).
3. `Plugin_Control20`: Revert Control 1, change only **Control 2** to max value.
4. `Plugin_PowerOff`: Keep default controls, set main **Power/Bypass** to **OFF**.

### Step 2: Locate User Preset Folder & Config Paths
Locate standard macOS preset directories in `scripts/utils/config.py`:
* **UADx (Native JSON)**: `BASE_UAD_PRESETS_DIR / "uaudio_[plugin_name]"`
* **Valhalla DSP (Plain XML)**: `SYSTEM_APP_SUPPORT / "Valhalla DSP, LLC/[PluginName]/Presets/User/"`
* **Nembrini Audio (Plain XML)**: `NEMBRINI_DOCS_DIR / "[PluginName]"`
* **Logic Pro (Binary PST)**: `LOGIC_SETTINGS_DIR / "[PluginName]"`

### Step 3: Run Binary / Text Diagnostics
Write a targeted mapping script (e.g. `scripts/map_studio_d.py`) to parse diagnostic files:
* **Plaintext XML**: Diff text files to find attribute changes.
* **Binary/JSON Chunks (UADx)**: Decode base64 `"chunk"` string into bytearray, unpack floats with `struct.unpack("f", chunk[offset:offset+4])[0]`, and record offset indices.

### Step 4: Implement Compiler Handler in `scripts/preset_compiler/`
1. Create or extend a module in `scripts/preset_compiler/` (e.g., `uad.py`, `neural.py`, `my_vendor.py`).
2. Use `scripts.utils.param_types` to extract parameters cleanly from frontmatter or Markdown sections (`extract_markdown_section()`).
3. Serialize output preset, write to target path, and export function in `scripts/preset_compiler/__init__.py`.
4. Register call in `scripts/compile_all_presets.py`.

---

## 4. Format Blueprint & Reference Mappings

### A. UADx Native JSON Format
UADx plugins use a lightweight JSON wrapper containing metadata (`plugin_id`, `version`, `uid`, `name`) and a base64-encoded `"chunk"` representing a binary array of Float32/Int32 values.

#### Studio D Chorus (13 float / 52-byte chunk)
* **Float Index 10 (Offset 40)**: `Dimension Mode` button states (mapped as a 4-bit binary bitmask scaled between `0.0` and `1.0` in steps of `1/15`):
  * `Off` (No buttons pressed) = `0.0`
  * `1` = `1 / 15.0` (`0.0667`)
  * `2` = `2 / 15.0` (`0.1333`)
  * `3` = `4 / 15.0` (`0.2667`)
  * `4` = `8 / 15.0` (`0.5333`)
  * `All / Secret Mode` (All buttons pushed) = `15 / 15.0` (`1.0`)
  * *Summing rule*: Custom multiple button pushes (e.g. `1+4`) can be mapped as their sum weight (e.g. `1 + 8 = 9 -> 9 / 15.0 = 0.6`).
* **Float Index 12 (Offset 48)**: `Power Switch` (`ON` = `1.0`, `OFF` = `0.0`).
* **Float Index 11 (Offset 44)**: Constant `1.0` (Stereo bypass).

#### Galaxy Tape Echo (27 float / 108-byte chunk)
* **Int Index 0 (Offset 0)**: `Head Select` Mode selector.
* **Float Index 19 (Offset 76)**: `Echo Rate` (scaled `0.0` to `1.0`).
* **Float Index 20 (Offset 80)**: `Reverb Volume` (scaled `0.0` to `1.0`).
* **Float Index 21 (Offset 84)**: `Feedback` (scaled `0.0` to `1.0`).
* **Float Index 22 (Offset 88)**: `Echo Volume` (scaled `0.0` to `1.0`).
* **Float Index 23 (Offset 92)**: `Tape Age` (`New` = `0.0`, `Used` = `0.5`, `Old` = `1.0`).

### B. Valhalla DSP XML Format
Valhalla plugins save natively as simple, standard XML text files with attribute keys.

#### Valhalla Supermassive (`.vpreset`)
* **Mix, DelayWarp, Feedback, Density**: Floats `0.0` to `1.0` (direct percentage division).
* **Delay_Ms**: Scaled by dividing ms by `1000.0` (e.g., `800ms` delay = `0.8`).
* **Mode**: Scaled by dividing active mode index by `24.0` (Andromeda at Index 6 = `0.25`).
* **Modulation**: `ModRate` and `ModDepth` set to `"0.0"` in all generated presets to prevent detuning.

### C. Logic Pro ProjectData Audio Unit Signatures
When parsing the binary `ProjectData` file of a Logic Pro project/template package, the embedded Audio Unit plug-in descriptions use standard macOS Four-Character Codes (FourCC) encoded as big-endian integers:

| Manufacturer Code | Subtype Code | Type | Plug-in Name |
| :--- | :--- | :--- | :--- |
| `Ikmm` | `Txmm` | `aufx` | IK Multimedia TONEX |
| `UADx` | `UI24` | `aumf` | UADx Paradise Guitar Studio |
| `MxWv` | `MTRA` | `aumf` | MixWave Two-Rock Bloomfield Drive |
| `NDSP` | `NCWX` | `aumf` | Neural DSP Archetype: Cory Wong |
| `NmAd` | `M812` | `aufx` | Nembrini MRH810 V2 (Marshall 800 style) |
| `NmAd` | `JzCh` | `aumf` | Nembrini JC120 (Jazz Clean) |
| `NmAd` | `Dv11` | `aumf` | Nembrini Divided 11 (Divided by 13 style) |
| `NmAd` | `Prtn` | `aumf` | Nembrini HK Puretone (Hughes & Kettner style) |
| `AhdS` | `TPie` | `aufx` | Audio Hertz Ten Piece (10-band saturator) |
| `UADx` | `U3A9` | `aufx` | UADx LA-2A Gray/Silver Compressor |
| `NmAd` | `Acvp` | `aufx` | Nembrini Acoustic Voice Pro |
| `UADx` | `U3CI` | `aufx` | UADx Capitol Chambers |
| `UADx` | `U3D7` | `aufx` | UADx Hitsville Reverb Chambers |
| `UADx` | `U3DF` | `aufx` | UADx Sound City Studios |
| `oDin` | `sMas` | `aufx` | Valhalla Supermassive |
| `UADx` | `U3BK` | `aufx` | UADx Galaxy Tape Echo |

---

## 5. Backlog & Future Phases

The following plugins are noted on the project backlog for future preset compilation phases:

### A. UADx Capitol Chambers
* **Target Directory**: `/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins/uaudio_capitol_chambers/`
* **Baseline File**: Create a base template named `whereami.json` inside this folder.
* **Controls to Map**:
  * Chamber Select (Chambers 1–4)
  * Microphone Type & Position (0.0 to 1.0)
  * Decay time (ms / seconds)
  * Pre-delay time (ms)
  * EQ controls (Bass, Mid, Treble, and cutoffs)
  * Wet Solo toggle

### B. UADx UA 610-B Tube Preamp & EQ
* **Target Directory**: `/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins/uaudio_610_b/`
* **Baseline File**: Create a base template named `whereami.json` inside this folder.
* **Controls to Map**:
  * Input selector (Mic/Line)
  * Input Gain stepped control
  * Low Shelf Boost/Cut
  * High Shelf Boost/Cut
  * Output Level
