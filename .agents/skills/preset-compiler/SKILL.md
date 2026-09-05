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

The core objective of the preset compiler is **rig-wide automation staging**: taking a single descriptive markdown toneprint (under `tones/`) and automatically compiling native user presets for every plugin in the track's signal chain. This allows Mike to load a single tone index and instantly stage all amplifiers, dynamic controllers, EQ settings, and spatial effects in **Standalone Audio (by Oort Media)** for linear single-amp chains or **Kushview Element** for parallel modular rigs. *(Note: Logic Pro is shelved from the active toolkit; legacy `.pst` support remains preserved in archive).*

### Knowledge Qualification & Evidence Citation Standards
- **Pre-Trained Knowledge Qualification**: Any historical amplifier/plugin context, circuit/component emulation behavior, format architecture claims, or parameter behavior originating from internal parametric memory (and not directly extracted from user inputs, workspace files, diagnostic scripts, or executed live searches) must be prefaced with *"I know that..."* or *"My trained knowledge includes that..."*.
- **First-Source Evidence Citation**: Facts, parameter names, byte offsets, FourCC codes, scaling equations, or preset schema definitions extracted from workspace documents (e.g., `tone-advisor/docs/`, `scripts/preset_compiler/`, `scripts/utils/param_types.py`, XML/JSON preset templates, diagnostic diffs) or executed searches must cite the exact workspace file path or search source.

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
        +--------------------------+--------------------------+---------------------------+
        |                          |                          |                           |
        v                          v                          v                           v
 [scripts/preset_compiler/  [scripts/preset_compiler/  [scripts/preset_compiler/   [scripts/preset_compiler/
    standalone.py]             uad.py, neural.py]         valhalla.py]               nembrini.py, etc.]
        |                          |                          |                           |
        v                          v                          v                           v
 [Standalone Host JSON]     [UADx Native JSON]        [Valhalla Plain XML]        [Nembrini Plain XML]
 (~/Library/App Support/   (Paradise, LA-2A,          (Supermassive)             (JC120, MRH810, AVP,
   Standalone/Presets)        Galaxy, Studio D)                                       Puretone, Div11)
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
Open **Standalone Audio** or **Kushview Element**, load the plugin on a track, and save a series of custom baseline presets **using the plugin's internal preset menu** (not the host's frame). Save:
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

#### Hitsville Reverb Chambers (23 float / 92-byte chunk)
* **Float Index 10 (Offset 40)**: `Chamber` (`0.0` = Chamber 1 [2648], `1.0` = Chamber 2 [2644]).
* **Float Index 11 (Offset 44)**: `Dist 2648` (Distance slider for Chamber 1).
* **Float Index 12 (Offset 48)**: `Dist 2644` (Distance slider for Chamber 2).
* **Float Index 13 (Offset 52)**: `Speakers` (`0.0` = Bozak, `1.0` = Altec 605A / Set 2).
* **Float Index 14 (Offset 56)**: `Microphones` (`0.0` = Unidyne 545, `0.3333` = RCA 44, `0.6667` = EV 631, `1.0` = Neumann KM86).
* **Float Index 15 (Offset 60)**: `Width` (`1.0` = 100% stereo).
* **Float Index 16 (Offset 64)**: `Mono` toggle (`0.0` = Stereo, `1.0` = Mono).
* **Float Index 17 (Offset 68)**: `Predelay` (log-scaled `0.0` to `1.0`: `math.log(ms / 22.9 + 1.0) / math.log(250.0 / 22.9 + 1.0)`).
* **Float Index 18 (Offset 72)**: `Low EQ` (`0.5` = 0.0 dB flat).
* **Float Index 19 (Offset 76)**: `High EQ` (`0.5` = 0.0 dB flat).
* **Float Index 20 (Offset 80)**: `Decay` (`decay_sec / 10.0`, e.g., `0.18` = 1.8s, `0.36` = 3.6s).
* **Float Index 21 (Offset 84)**: `Mix` (`0.0` to `1.0`, e.g., `0.12` = 12%).
* **Float Index 22 (Offset 88)**: `Power Switch` (`1.0` = ON, `0.0` = OFF).
#### UADx Teletronix LA-2A Silver & Gray (14 float / 56-byte chunk)
* **Base Presets**:
  * Silver Panel: `BASE_UAD_PRESETS_DIR / "uaudio_teletronix_la-2a_silver" / "Mike - Alternative.json"`
  * Gray Panel: `BASE_UAD_PRESETS_DIR / "uaudio_teletronix_la-2a_gray" / "Mike - Adjusting Gain Staging.json"`
* **Float Index 10 (Offset 40)**: `Peak Reduction` (`0.0` to `1.0`, e.g., `35.0 -> 0.35`).
* **Float Index 11 (Offset 44)**: `Gain` (`0.0` to `1.0`, e.g., `40.0 -> 0.40`).
* **Float Index 13 (Offset 52)**: `Mode Switch` (`1.0` = Compress, `0.0` = Limit).

#### UADx Paradise Guitar Studio (461 Controls Dictionary Schema)
Unlike simple UAD plugins that use binary byte chunks, Paradise Guitar Studio uses a high-level JSON structure where `chunk["controls"]` is a key-value dictionary containing 461 named controls, each storing `{"real_value": <val>}`.

* **Target Directory**: `USER_DOCS / "Universal Audio" / "Presets" / "Plug-Ins" / "uaudio_paradise_guitar_studio"`
* **Repo Mirror**: `WORKSPACE_ROOT / "quarantined" / "Documents" / "Universal Audio" / "Presets" / "Plug-Ins" / "uaudio_paradise_guitar_studio"`
* **Base Template**: `PARADISE_DIR / "Non-Toneprints" / "Boutique Warm Clean - Enigmatic.json"`

##### 1. Amplifier Model Index (`controls["amp"]`)
* `0`: **Dream '65** (Fender Blackface Deluxe Reverb)
  * Controls: `dream_volume`, `dream_treble`, `dream_bass`, `dream_bright` (bool), `dream_boost_enable` (bool), `dream_boost_amount`, `dream_reverb`, `dream_amp_mod` (`0`=Stock, `1`=Lead, `2`=D-Tex)
* `1`: **Enigmatic '82** (Dumble Overdrive Special)
  * Controls: `enigmatic_volume`, `enigmatic_treble`, `enigmatic_middle`, `enigmatic_bass`, `enigmatic_presence`, `enigmatic_master_gain`, `enigmatic_bright_enable` (bool), `enigmatic_boost_enable` (bool)
  * Voice Models (`enigmatic_model`): `0`=Suede, `1`=Santa Cruz / Silver, `2`=Cream, `3`=HRM / Black
* `2`: **Lion '68** (Marshall Super Lead / Super Bass Plexi)
  * Controls: `lion_lead_amp_bright_cap`, `lion_brown_amp_bright_cap`
* `3`: **Ruby '63** (Vox AC30 Top Boost)
  * Controls: `ruby_volume`, `ruby_treble`, `ruby_bass`, `ruby_cut`, `ruby_boost_enable`, `ruby_boost_amount`, `ruby_channel` (`2`=Brilliant), `ruby_tone_cut` (`5.0` when cut engaged)
* `4`: **Showtime '64** (Fender Showman / Twin 6L6 high-headroom clean)
  * Controls: `showtime_volume`, `showtime_treble`, `showtime_middle`, `showtime_bass`, `showtime_bright` (bool), `showtime_vibrato_enable` (bool)
* `5`: **Woodrow '55** (Fender Tweed Deluxe)
  * Controls: `woodrow_inst_volume`, `woodrow_mic_volume`, `woodrow_tone`, `woodrow_boost_enable`, `woodrow_boost_amount`, `woodrow_boost_type` (`0`=Stock, `1`=KP-3K, `2`=EP-III)

##### 2. Cabinet & Microphone Combinations (`controls["cab_and_mic"]`)
* `29`: **2x12 Showman** (Showtime '64 default) / **1x12 EV12** (Dream alternate)
* `2`: **2x12 Boutique D65** (Enigmatic '82 default, Celestion G12-65 response)
* `1`: **2x12 Celestion Alnico Blue** (Ruby '63 default)
* `32`: **1x12 Tweed Oxford** (Woodrow '55 alternate, tight vintage tweed)
* `23`: **Boutique 1x12 EV** (High-headroom articulate clean)

##### 3. Slot Architecture & Master Power Controls
Paradise Guitar Studio provides **5 Pre-FX slots** (front of amp) and **5 Post-FX slots** (post-cab studio rack):
* **Master Toggles**: `amp_power` (bool), `prefx_power` (bool), `postfx_power` (bool)
* **Pre-FX Routing**: Slots `prefx_1` through `prefx_5` (integer pedal ID 0–26) and power toggles `prefx_1_power` through `prefx_5_power` (bool).
* **Post-FX Routing**: Slots `postfx_1` through `postfx_5` (integer pedal ID 0–26) and power toggles `postfx_1_power` through `postfx_5_power` (bool).
* **Parameter Naming Standard**:
  * Pre-FX: `prefx_{pedal_name}_{param_name}`
  * Post-FX: `postfx_{pedal_name}_{param_name}`

##### 4. Complete 26-Effect Pedal & Studio Rack ID Map
| ID | Model Name | Emulated Hardware / Circuit | Primary Controls |
|---|---|---|---|
| `0` | `none` | Empty slot | — |
| `1` | `big_fuzz` | Electro-Harmonix Big Muff | `sustain`, `tone`, `level` |
| `2` | `gold_overdrive` | Klon Centaur Professional Overdrive | `gain`, `output`, `treble` |
| `3` | `nashville_overdrive` | Nobels ODR-1 Natural Overdrive | `drive`, `level`, `spectrum` |
| `4` | `raw_distortion` | Pro Co RAT2 Distortion | `distortion`, `filter`, `volume` |
| `5` | `ts_overdrive` | Ibanez TS808 / TS9 Tube Screamer | `overdrive`, `level`, `tone` |
| `6` | `vintage_fuzz` | Arbiter Fuzz Face | `fuzz`, `level`, `sputter` |
| `7` | `blue_flanger` | MXR M117 Flanger | `speed`, `width`, `manual`, `regen`, `mode`, `invert` |
| `8` | `brigade_chorus` | Boss CE-1 Chorus Ensemble | `intensity`, `level`, `mod_select`, `stereo_mode` |
| `9` | `micropitch_shifter` | Eventide H910 / H949 MicroPitch Detune | `pitch_a` (cents), `pitch_b` (cents), `delay_a`, `delay_b`, `mix`, `filter`, `stereo_mod` |
| `10` | `multi_chorus` | Multi-Tap Six-Voice Studio Chorus | `level`, `delay`, `regen`, `taps`, `filter`, `mod_type` |
| `11` | `orange_phaser` | MXR Phase 90 | `speed`, `era` (script vs block) |
| `12` | `trem_65` | Fender '65 Blackface Opto/Bias Tremolo | `speed`, `intensity`, `shape`, `output`, `stereo_mod` |
| `13` | `vintage_vibrato` | Magnatone / True Pitch Vibrato | `rate`, `depth`, `mode`, `wave`, `filter`, `stereo_mod`, `output` |
| `14` | `1176_compressor` | UREI 1176LN Peak Limiter (Blackface) | `input` (dB), `output` (dB), `attack` (1=slow to 7=fast), `release` (1=slow to 7=fast), `ratio` (0=4:1, 1=8:1, 2=12:1, 3=20:1) |
| `15` | `red_comp` | MXR Dyna Comp | `sensitivity`, `output` |
| `16` | `memory_delay` | EHX Deluxe Memory Man BBD Delay | `level`, `blend`, `feedback`, `time`, `tone`, `mod_depth`, `mod_speed`, `cho_vib` (0=cho, 1=vib), `preamp_color` |
| `17` | `digital_delay` | 80s Studio Digital Rack Delay | `time_a`, `time_b`, `mix`, `feedback`, `low_cut`, `high_cut`, `modulation_depth`, `modulation_rate`, `link` |
| `18` | `ep_iii_tape_echo` | Maestro Echoplex EP-3 Solid-State Tape | `time` (0.02–0.8s), `feedback`, `wonk` (0–10), `age` (0–2), `rec_level`, `preamp_color` (bool), `tone`, `mix` |
| `19` | `pitch_shift_delay` | Pitch-Shifting Harmonized Delay | `time`, `mix`, `feedback`, `sync_pitch`, `dirt`, `mod_depth`, `mod_speed` |
| `20` | `digital_reverb` | Modern Algorithmic Reverb | `decay`, `predelay`, `mix`, `brightness`, `mode` |
| `21` | `plate_140_reverb` | EMT 140 Classic Studio Plate Reverb | `decay` (s), `predelay` (ms), `mix` (0–100%), `bass`, `treble`, `low_cut`, `mod_depth`, `mod_rate` |
| `22` | `reverb_224` | Lexicon 224 Digital Reverb (1978) | `program` (1=Concert Hall), `bass_reverb_time`, `mid_reverb_time`, `treble_reverb_time` (raw 16-bit ints 0–32768), `pre_delay`, `mix` (0–32768), `pitch`, `input`, `output` |
| `23` | `drip_spring_65_reverb`| Fender Outboard Spring Reverb Tank | `mix`, `bass`, `treble`, `tank` |
| `24` | `10_band_graphic_eq` | MXR 10-Band Graphic EQ | 10 frequency sliders (`31hz` to `16khz`), `output`, `phase`, `mono` |
| `25` | `studio_eq` | Console Parametric Channel EQ | `low_frequency`, `low_cut_filter`, `high_frequency`, `high_cut_filter`, `output` |
| `26` | `volume_pedal` | Passive Volume Pedal | `position`, `minimum_volume` |


---

### B. Valhalla DSP XML Format
Valhalla plugins save natively as simple, standard XML text files with attribute keys.

#### Valhalla Supermassive (`.vpreset`)
* **Mix, DelayWarp, Feedback, Density**: Floats `0.0` to `1.0` (direct percentage division).
* **Delay_Ms**: Scaled by dividing ms by `1000.0` (e.g., `800ms` delay = `0.8`).
* **Mode**: Scaled by dividing active mode index by `24.0` (Andromeda at Index 6 = `0.25`).
* **Modulation**: `ModRate` and `ModDepth` set to `"0.0"` in all generated presets to prevent detuning.

---

### C. MixWave Two-Rock Bloomfield Drive XML Format
MixWave plugins save presets as standard ElementTree XML documents structured into nested modules (`<Module moduleName="...">`) with child `<Variables>` nodes:

* **Target Directory**: `SYSTEM_AUDIO_PRESETS / "MixWave" / "MixWave Two-Rock Bloomfield Drive" / "Presets" / "User"`
* **Amp Module Variables**:
  * Continuous Knobs: `Gain`, `Treble`, `Middle`, `Bass`, `Presence`, `Master`, `Reverb`, `Vibe` (floats `0.0` to `10.0`).
  * Voicing Switches: `Bright`, `Mid`, `Deep`, `Tone Stack Bypass`, `Lead` (`1.0` for active, `0.0` for bypassed).
* **Cabinet Module Variables**: Controls mic selection and level for top and bottom 12" speakers.
* **Overdrive Module Variables**: Built-in front-end drive with `Drive`, `Balance`, `Tone`, `Bypass`, `Dry/Wet`.
* **Global Variables**: `Noise Gate`, `Input Trim`, `Output Trim`.

---

### D. Nembrini Audio Plain XML Format
Nembrini Audio and Kuassa plugins store user presets in plaintext XML files using `<param name="..." value="..."/>` tags:

* **Target Directory**: `USER_DOCS / "Nembrini Audio" / [PluginName]`
* **MRH810 V2 (Marshall JCM800 2210)**:
  * `ChSel`: Channel select (`0.0` = Clean Channel, `1.0` = Lead Channel).
  * Clean: `CleanVolume`, `CleanBass`, `CleanTreble`.
  * Lead: `LeadGain`, `LeadVolume`, `LeadBass`, `LeadMid`, `LeadTreble`.
  * Master & Filters: `Master`, `Presence`, `OutLevel`, `Harsh` (filter), `Rumbling` (filter), `NgPower`, `NgThreshold`, `NgRange`.
* **Jazz Chorus JC-120 (Roland JC-120)**:
  * Amp Controls: `Volume`, `Bass`, `Middle`, `Treble`, `Distortion`, `Reverb`, `OutLevel`.
  * **CRITICAL TYPO IN VENDOR SCHEMA**: The Bright switch is spelled `Brigth` in Nembrini XML (`1.0` = ON, `0.0` = OFF).
  * Modulation: `ChorusDepth`, `ChorusSpeed`, `VibratoDepth`, `VibratoSpeed`, `ModType` (`0.0`=Manual, `1.0`=Chorus, `2.0`=Vibrato).
* **Divided 11 (Divided by 13 CJ11)**:
  * Controls: `Volume`, `Treble`, `Bass`, `Master`, `Boost`, `High` (input sensitivity), `Low` (input sensitivity), `OutLevel`.
* **HK Puretone (Hughes & Kettner Puretone)**:
  * Controls: `Volume`, `Bass`, `Middle`, `Treble`, `Growl`, `OutLevel`.
* **Acoustic Voice Pro**:
  * Controls: `BodyType` (0–9), `MicType` (0–4), `CompThresh`, `CompRatio`, `OutLevel`.

---

### E. Neural DSP Archetype: Cory Wong X XML Format
Neural DSP plugins store presets as XML files with attribute-based parameter mappings:

* **Target Directory**: `SYSTEM_AUDIO_PRESETS / "Neural DSP" / "Archetype Cory Wong X" / "Toneprints"`
* **Percentage Scaling Rule**: All percentage controls must be normalized to floats between `0.0` and `1.0` (formatted to 4 decimal places). If a toneprint specifies `85%`, the XML value is `"0.8500"`.
* **The Clean Machine (Fender clean)**:
  * `cleanVolume`, `cleanBass`, `cleanMid`, `cleanTreble`, `cleanPresence`, `cleanOutputLevel`.
* **Amp Snob (Two-Rock boutique clean/lead)**:
  * `snobVolume`, `snobMaster`, `snobBass`, `snobMid`, `snobTreble`, `snobPresence`, `snobOutputLevel`.
* **D.I. Funk Console (Direct console preamp)**:
  * `funkVolume`, `funkTubeSat`, `funkComp`.
* **Stompboxes & Post-FX**:
  * 4th Position Compressor: `compressorBlend`, `compressorCompression`, `compressorVolume`, `compressorTone`.
  * Overdrives: `bigRigDrive`, `bigRigLevel`, `bigRigTone`, `tuberDrive`, `tuberLevel`, `tuberTone`.
  * The Wash Reverb: `washMix`, `washDecay`, `washLowCut`, `washHighCut`.
  * Modulation: `chorusMix`, `chorusWidth`, `chorusRate`, `delayMix`, `delayFeedback`.

---

### F. Yamaha THR-II L6Preset JSON Format
Yamaha THR-II hardware and app patches use native Line 6 JSON `.thrl6p` files:

* **Target Directory**: `TONES_DIR / "presets" / "yamaha"`
* **Envelope Metadata**: `device: 2359296`, `device_version: 22020194`, `schema: "L6Preset"`, `version: 5`.
* **Amp Models**:
  * Classic: `THR10C_Deluxe` (Clean), `THR10C_DC30` (Crunch), `THR10_Lead` (Lead), `THR10_Modern` (Hi Gain), `THR10X_Brown1` (Special).
  * Boutique: `THR10C_BJunior2` (Clean), `THR30_SR101` (Crunch), `THR30_Blondie` (Lead), `THR30_FLead` (Hi Gain), `THR10X_South` (Special).
  * Modern: `THR30_Carmen` (Clean), `THR10C_Mini` (Crunch), `THR10_Brit` (Lead), `THR10X_Brown2` (Hi Gain), `THR30_Stealth` (Special).
* **Cabinets (0–16)**: `0`=British 4x12, `1`=American 4x12, `7`=American 2x12, `10`=Boutique 2x12, `15`=Boutique 1x12, `16`=Flat/Bypass.
* **FX Groups**:
  * Gate: `THRGroupGate` (`Thresh`, `Decay`).
  * Compressor: `THRGroupFX1Compressor` (`RedComp` with `Sustain`, `Level`).
  * Modulation: `THRGroupFX2Effect` (`StereoSquareChorus`, `BiasTremolo`, `L6Flanger`, `Phaser`).
  * Delay & Reverb: `THRGroupDelay`, `THRGroupReverb`.

---

### G. Logic Pro ProjectData Audio Unit Signatures (Legacy Reference)
When parsing the binary `ProjectData` file of a legacy Logic Pro project/template package, the embedded Audio Unit plug-in descriptions use standard macOS Four-Character Codes (FourCC) encoded as big-endian integers:

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

---

## 6. Standalone Host Preset Architecture & Repo Mirroring

Standalone (by Oort Media) presets are stored in:
`~/Library/Application Support/Standalone/Presets/<UUID>.json`

* **CLI Runner**: `python3 scripts/compile_standalone_presets.py`
* **Deterministic UUID Generation**: All preset IDs are computed deterministically using `uuid.uuid5` from a fixed project namespace (`3d3a34b7-43f9-4c61-be5b-580a4e6f880d`) and the toneprint ID:
  ```python
  preset_uuid = str(uuid.uuid5(standalone_ns, f"guitar-skills.toneprint.{pid}")).upper()
  ```
  This ensures re-compilation updates the existing preset file in place without producing duplicate IDs or breaking MIDI Program Change (PC) associations.
* **Input/Output Channel Layout**:
  * Slot 0: Always forced to `inputChannels: 1` (Mono instrument DI input).
  * Slot 1+: Always configured for `inputChannels: 2` (Stereo serial effects/bus).
* **State Preservation**: Individual module states are saved as Base64-encoded Apple `.aupreset` binary property lists (`statePlistBase64`) extracted from verified host templates (`scripts/preset_compiler/templates/standalone_templates.json`).
* **Repository Mirroring & Sandboxing Rule**:
  Due to macOS application sandboxing, background command runners may encounter `PermissionError [Errno 1]` when attempting to write directly to `~/Library/Application Support/Standalone/Presets/` or `~/Documents/Universal Audio/Presets/`. 
  To prevent compilation failures:
  1. The compiler automatically writes a version-controlled repository mirror to `tones/presets/standalone/<UUID>.json` and `quarantined/Documents/...`.
  2. Live system directory injection is attempted in a `try...except` block, gracefully alerting if elevated unsandboxed execution (`BypassSandbox: true`) is required to update the active live directories.

