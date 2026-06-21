# Slapback Delay Default Presets

These utility presets provide a standard, "always-on" slapback tape delay to add depth, space, and a 3D shadow behind the dry guitar signal without creating a muddy or repeating echo trail.

---

## 1. Preset Details

### A. Logic Pro Stock Tape Delay
* **Preset Name**: `Slapback Default`
* **File Path**: `~/Music/Audio Music Apps/Plug-In Settings/Tape Delay/Slapback Default.pst`
* **Configuration**:
  * **Tempo Sync**: OFF (crucial for keeping the delay locked to a constant millisecond time regardless of project tempo)
  * **Delay Time**: `90.0 ms`
  * **Feedback**: `0.0%` (strictly a single repeat shadow)
  * **Low Cut Filter**: `150.0 Hz` (prevents low-end boominess from repeating)
  * **High Cut Filter**: `3000.0 Hz` (darkens the repeat so it sits naturally behind the dry note attack)
  * **Smoothing**: `260.0 ms`
  * **Dry Level**: `100.0%`
  * **Wet Level**: `12.0%`
  * **Clip Threshold**: `0.0 dB` (clean tape emulation)

### B. UADx Galaxy Tape Echo
* **Preset Name**: `Toneprint - Slapback Default`
* **File Path**: `~/Documents/Universal Audio/Presets/Plug-Ins/uaudio_galaxy_tape_echo/Toneprint - Slapback Default.json`
* **Configuration**:
  * **Head Select**: Position 1 (single playback head for the shortest and cleanest slapback path)
  * **Echo Rate**: `6.5` (corresponds to approximately `85.0 ms` - `90.0 ms` on Head 1)
  * **Feedback**: `12.0%` (produces exactly one clear ghost repeat that quickly dissolves)
  * **Echo Volume**: `3.0` (blended subtly as a background shadow)
  * **Treble**: `4.0` (slightly rolled back to keep repeats warmer than the dry signal)
  * **Bass**: `5.0` (flat EQ)
  * **Tape Age**: Used (adds gentle, organic wow and flutter)
  * **Wet Solo**: OFF (insert configuration)
  * **Reverb Volume**: `0.0` (reverb is bypassed; spatial reverb lives on the shared Aux bus)

---

## 2. Technical Parameter Mappings

### A. Logic Tape Delay `.pst` Format (Big-Endian)
The Logic `.pst` binary file is written in legacy big-endian format. Parameters start at byte offset 24 (following the 24-byte header), and map as `offset = 24 + (Parameter Index + 1) * 4`:
* `offset 32 (Param 2)`: Delay time coarse (`90.0`)
* `offset 40 (Param 4)`: Feedback Left (`0.0`)
* `offset 44 (Param 5)`: High Cut Filter (`3000.0`)
* `offset 48 (Param 6)`: Low Cut Filter (`150.0`)
* `offset 52 (Param 7)`: Tempo Sync Switch (`0.0` = OFF)
* `offset 56 (Param 8)`: Synced Note Value (`0.0`)
* `offset 64 (Param 10)`: Smoothing (`260.0`)
* `offset 104 (Param 20)`: Dry level (`100.0`)
* `offset 108 (Param 21)`: Wet level (`12.0`)
* `offset 112 (Param 22)`: Clip Threshold / Distortion (`0.0`)

### B. UADx Galaxy Tape Echo `.json` Format
UADx presets are JSON files wrapping a base64-encoded binary chunk (27 little-endian Float32 values / 108 bytes):
* `offset 0 (Int Index 0)`: Head Select Mode (`0` = Head 1, `1` = Head 2, etc.)
* `offset 76 (Float Index 19)`: Echo Rate (`0.0` to `1.0` scale)
* `offset 80 (Float Index 20)`: Reverb Volume (`0.0` to `1.0` scale)
* `offset 84 (Float Index 21)`: Feedback (`0.0` to `1.0` scale)
* `offset 88 (Float Index 22)`: Echo Volume (`0.0` to `1.0` scale)
* `offset 92 (Float Index 23)`: Tape Age (`0.0` = New, `0.5` = Used, `1.0` = Old)
