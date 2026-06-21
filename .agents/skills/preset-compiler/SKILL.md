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
2. Write a new compiler function in `scripts/compile_all_presets.py`.
3. Understand binary, JSON, or XML-based preset structures.
4. Reference the future backlog for UADx Capitol Chambers and UA 610-B.

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
               | scripts/compile_all_presets.py |
               +---------------+---------------+
                               |
       +-----------------------+-----------------------+
       |                       |                       |
       v                       v                       v
[UADx Native JSON]     [Valhalla Plain XML]     [Nembrini Plain XML]
(Galaxy, Studio D)        (Supermassive)       (JC120, MRH810, AVP)
       |                       |                       |
       v                       v                       v
~/Documents/Universal   /Library/Application   ~/Documents/Nembrini
  Audio/Presets/...       Support/Valhalla...       Audio/...
```

---

## 2. Playbook for Mapping a New Plugin

Whenever Mike purchases a new plugin or wants to add a new device to the compiler, follow this standard, structured mapping workflow:

### Step 1: Save Diagnostic Presets
Open **Logic Pro**, load the plugin on a track, and save a series of custom baseline presets **using the plugin's internal preset menu** (not Logic's frame). This ensures the preset is written natively in the plugin's native user folder. Save exactly:
1. `Plugin_Base`: A default, basic setting.
2. `Plugin_Control10`: Change only **Control 1** to its maximum value (`10` or `100%`).
3. `Plugin_Control20`: Revert Control 1, and change only **Control 2** to its maximum value.
4. `Plugin_PowerOff`: Keep all controls at default, but toggle the plugin's main **Power/Bypass** switch to **OFF**.

### Step 2: Locate User Preset Folder
Natively saved user presets reside in standard macOS folders:
* **UADx (Native JSON)**: `~/Documents/Universal Audio/Presets/Plug-Ins/uaudio_[plugin_name]/`
* **Valhalla DSP (Plain XML)**: `/Library/Application Support/Valhalla DSP, LLC/[PluginName]/Presets/User/`
* **Nembrini Audio (Plain XML)**: `~/Documents/Nembrini Audio/[PluginName]/`
* **Logic Pro (Binary PST)**: `~/Music/Audio Music Apps/Plug-In Settings/[PluginName]/`

### Step 3: Run Binary / Text Diagnostics
Write a targeted mapping script (like `scripts/map_studio_d.py`) to parse and compare your diagnostic files.
* **If Plaintext XML (Valhalla/Nembrini)**: Open the files in a text editor and diff them. Look for attribute changes (e.g. `Mix="0.5"` vs `Mix="1.0"`).
* **If Binary/JSON Chunks (UADx)**: Decode the base64 `"chunk"` string into a bytearray, unpack it into an array of floats/ints using Python's `struct.unpack()`, and print index differences:
```python
# Unpacking 4-byte floating point offsets
for offset in range(0, len(bytes_payload), 4):
    val_f = struct.unpack("f", bytes_payload[offset:offset+4])[0]
```

### Step 4: Write and Hook the Compiler
Add the template configuration and compiler routine in `scripts/compile_all_presets.py`:
1. **Declare the Base Path**: Add the path to `whereami` template under global configurations (e.g. `STUDIO_D_BASE`).
2. **Implement Parameter Extractors**: Use `extract_markdown_section()` to isolate the plugin's table in the markdown file to prevent collisions. Use `find_numeric_parameter()` and `find_boolean_parameter()` for quick, standard table parsing.
3. **Scale Values Safely**:
   * Scale percentages: `val = percent / 100.0`
   * Handle unit suffixes (like `ms`, `s`, `dB`) using custom regex (e.g., `re.search(r"([0-9.]+)\s*ms", ...)`).
4. **Serialize the Output**: Generate a unique UUID (`uid = uuid.uuid4().hex`) for JSON presets, rebuild the base64 payload or XML tree, and write out to the native directory under the name `Toneprint - [Tone Name]`.
5. **Register in `main()`**: Increment the counters, hook the scanner into the recursive directory traversal, and print the success summary at completion.

---

## 3. Format Blueprint & Reference Mappings

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
When parsing the binary `ProjectData` file of a Logic Pro project/template package, the embedded Audio Unit plug-in descriptions use standard macOS Four-Character Codes (FourCC) encoded as big-endian integers. Below is the mapping of these signatures to the user's specific plugins:

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

## 4. Backlog & Future Phases

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
