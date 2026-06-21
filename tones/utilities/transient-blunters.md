# Transient Blunting Utility Presets

Transient blunting is a highly advisable technique when playing electric guitars direct-to-interface (DI). Natively mic'd guitar cabinets and tube amplifiers have natural compression and air resistance that round off the sharp "click" of a pick striking the string. A pure DI signal lacks this softening, often leading to piercing, clicky transients ("ice-pick" tones), especially on single-coil pickups.

This document records the design and settings for three distinct transient-blunting utility presets that can be dropped into your signal chain (usually right after the input gate/EQ and before the amp emulator).

---

## 1. Choosing Your Tool: Enveloper vs. 1176

| Tool | Mechanism | Best Used For | Pros & Cons |
| :--- | :--- | :--- | :--- |
| **Logic Enveloper** | Level-Independent Transient Shaping | Surgical, consistent reduction of pick attack regardless of how hard you play. | **Pros**: Completely consistent; does not affect sustain or color the tone.<br>**Cons**: Can sound slightly synthetic if over-applied. |
| **1176 FET Compressor** | Level-Dependent Peak Limiting | Musical, dynamic rounding of pick attacks that only kicks in when you dig in hard. | **Pros**: Warm, classic analog grit and saturation; very interactive.<br>**Cons**: Requires proper gain staging; light playing won't trigger it. |

---

## 2. Preset Configurations

### A. Logic Enveloper — "Transient Softener"
This preset provides level-independent pick softening, transparently shaving off the initial spike of the note.
* **File Path**: `~/Music/Audio Music Apps/Plug-In Settings/Enveloper/Transient Softener.pst`
* **Configuration**:
  * **Attack Time**: `12.0 ms` (captures the duration of the pick strike)
  * **Attack Gain**: `-4.0 dB` (reduces the pick click amplitude)
  * **Lookahead**: `2.0 ms` (forces the enveloper to scan ahead to catch the transient perfectly)
  * **Release Time**: `200.0 ms` (default, leaves note decay untouched)
  * **Release Gain**: `0.0 dB` (leaves sustain untouched)
  * **Threshold**: `-100.0 dB` (default, ensures it triggers on all notes)
  * **Out Level**: `0.0 dB` (unity gain)

### B. UADx 1176LN — "Transient Tamer"
This preset emulates the classic blackface FET limiter, clamping down on transients within microseconds and adding analog warmth.
* **File Path**: `~/Documents/Universal Audio/Presets/Plug-Ins/uaudio_ua_1176ln_rev_e/Toneprint - Transient Tamer.json`
* **Configuration**:
  * **Ratio**: `8:1` (provides firm peak limiting)
  * **Attack**: `7` (fully clockwise - fastest attack, `20 microseconds`, to clamp transients instantly)
  * **Release**: `5` (moderately fast recovery to prevent pumping)
  * **Input**: Adjusted so that normal playing barely moves the needle, but heavy picking triggers `3 dB` to `5 dB` of gain reduction.
  * **Output**: Adjusted for unity gain output.

### C. Logic Compressor (Studio FET) — "Transient Tamer"
A stock Logic alternative that emulates the 1176 FET circuit topology.
* **File Path**: `~/Music/Audio Music Apps/Plug-In Settings/Compressor/Transient Tamer.pst`
* **Configuration**:
  * **Circuit Type**: `Studio FET` (1176 emulation)
  * **Threshold**: `-18.0 dB`
  * **Ratio**: `4.0:1`
  * **Attack**: `0.1 ms` (extremely fast)
  * **Release**: `50.0 ms` (fast recovery)
  * **Knee**: `0.5`
  * **Mix**: `100.0%` (fully wet insert)

---

## 3. Technical Parameter Mappings

### A. Logic Enveloper `.pst` (Little-Endian)
* `offset 28 (Param 1)`: Attack time (`12.0`)
* `offset 32 (Param 2)`: Attack Gain (`-4.0`)
* `offset 48 (Param 6)`: Lookahead (`2.0`)

### B. Logic Compressor `.pst` (Little-Endian)
* `offset 28 (Param 1)`: Threshold (`-18.0`)
* `offset 32 (Param 2)`: Ratio (`4.0`)
* `offset 36 (Param 3)`: Attack (`0.1`)
* `offset 40 (Param 4)`: Release (`50.0`)
* `offset 64 (Param 10)`: Circuit Type (`2.0` = Studio FET)
* `offset 124 (Param 25)`: Mix (`100.0`)

### C. UADx 1176LN `.json`
* `offset 0 (Int Index 0)`: Ratio (`1` = 8:1)
* `offset 40 (Float Index 10)`: Input Level (`0.40`)
* `offset 44 (Float Index 11)`: Output Level (`0.55`)
* `offset 48 (Float Index 12)`: Attack (`1.0` = fastest)
* `offset 52 (Float Index 13)`: Release (`0.7` = fast)
