# Yamaha THR-II Preset Format (.thrl6p)

The Yamaha THR-II series (THR10II, THR30II) uses a JSON-based format for its presets, typically with the `.thrl6p` extension. These files are compatible with the **THR Remote** app.

**Note:** The extension is written as `.thrl6p` (with a lowercase 'L' and the number '6').

---

## Core Schema
- **Schema Name:** `L6Preset`
- **Format:** JSON
- **Version:** `5` for THR-II
- **Device ID:** `2359296` (Default for THR10II / THR30II Wireless).
  - *Note:* The `device` ID in the preset **must** match the connected amplifier. If it doesn't match, the THR Remote application will import the EQ/FX parameters but **silently ignore** the amp and cabinet settings!

---

## File Structure

```json
{
  "schema": "L6Preset",
  "version": 5,
  "data": {
    "device": 2359296,
    "device_version": 22020194,
    "meta": {
      "name": "Preset Name",
      "tnid": 0
    },
    "tone": {
      "THRGroupAmp": {
        "@asset": "THR10C_BJunior2",
        "Drive": 0.35,
        "Bass": 0.60,
        "Mid": 0.50,
        "Treble": 0.45,
        "Master": 0.60
      },
      "THRGroupCab": {
        "@asset": "speakerSimulator",
        "SpkSimType": 10
      },
      "THRGroupFX1Compressor": {
        "@asset": "RedComp",
        "@enabled": true,
        "Level": 0.55,
        "Sustain": 0.60
      },
      "THRGroupFX2Effect": {
        "@asset": "StereoSquareChorus",
        "@enabled": true,
        "@wetDry": 0.35,
        "Depth": 0.40,
        "Feedback": 0.0,
        "Freq": 0.25,
        "Pre": 0.50
      },
      "THRGroupFX3EffectEcho": {
        "@asset": "TapeEcho",
        "@enabled": true,
        "@wetDry": 0.25,
        "Bass": 0.30,
        "Feedback": 0.20,
        "Time": 0.30,
        "Treble": 0.35
      },
      "THRGroupFX4EffectReverb": {
        "@asset": "ReallyLargeHall",
        "@enabled": true,
        "@wetDry": 0.20,
        "Decay": 0.45,
        "PreDelay": 0.05,
        "Tone": 0.50
      },
      "THRGroupGate": {
        "@asset": "noiseGate",
        "@enabled": true,
        "Thresh": -33.00,
        "Decay": 0.50
      },
      "global": {
        "THRPresetParamTempo": 110
      }
    }
  },
  "meta": {
    "original": 0,
    "pbn": 0,
    "premium": 0
  }
}
```

---

## Parameter Keys by Group

### 1. THRGroupAmp (Amplifier)
All control knobs are scaled as normalized floats from `0.0` to `1.0`.
- `@asset`: The exact amp identifier string (see lookup table below).
- `Drive`: Mapped to the physical **Gain** knob.
- `Master`: Mapped to the physical **Master** knob.
- `Bass`, `Mid`, `Treble`: Mapped to the EQ knobs.

### 2. THRGroupCab (Cabinet)
- `@asset`: Must always be `"speakerSimulator"`.
- `SpkSimType`: **Integer** index from `0` to `16` (16 = BYPASS / flat).

### 3. THRGroupFX1Compressor
- `@asset`: Must always be `"RedComp"`.
- `@enabled`: `true` / `false`.
- `Sustain`, `Level`: Normalized floats `0.0` to `1.0`.

### 4. THRGroupFX2Effect (Modulation)
- `@enabled`: `true` / `false`.
- `@wetDry`: Effect blend/mix (normalized float).
- Types and Asset Names:
  - **Chorus**: `"StereoSquareChorus"` (Params: `Depth`, `Feedback`, `Freq`, `Pre`)
  - **Tremolo**: `"BiasTremolo"` (Params: `Depth`, `Speed`)
  - **Flanger**: `"L6Flanger"` (Params: `Depth`, `Freq`)
  - **Phaser**: `"Phaser"` (Params: `Feedback`, `Speed`)

### 5. THRGroupFX3EffectEcho (Delay)
- `@enabled`: `true` / `false`.
- `@wetDry`: Delay blend/mix.
- Types and Asset Names:
  - **Tape Echo**: `"TapeEcho"` (Params: `Time`, `Bass`, `Treble`, `Feedback`)
  - **Digital Delay**: `"L6DigitalDelay"` (Params: `Time`, `Bass`, `Treble`, `Feedback`)

### 6. THRGroupFX4EffectReverb
- `@enabled`: `true` / `false`.
- `@wetDry`: Reverb blend/mix.
- Types and Asset Names:
  - **Hall**: `"ReallyLargeHall"` (Params: `Decay`, `PreDelay`, `Tone`)
  - **Plate**: `"LargePlate1"` (Params: `Decay`, `PreDelay`, `Tone`)
  - **Room**: `"SmallRoom1"` (Params: `Decay`, `PreDelay`, `Tone`)
  - **Spring**: `"StandardSpring"` (Params: `Time`, `Tone`)

### 7. THRGroupGate (Noise Gate)
- `@asset`: Must always be `"noiseGate"`.
- `@enabled`: `true` / `false`.
- `Decay`: Normalized float `0.0` to `1.0`.
- `Thresh`: **Decibel float** value from `-96.0` to `0.0`.
  - *Note:* The physical UI value (0-100) maps to decibels via: `dB = (ui_value - 100) * 0.96`.

---

## Lookup Tables

### Amp Mappings & Real-World Inspiration

| Category & Model | Engine `@asset` Key | Real-World Inspiration | Details & Tonal Character | Spreadsheet Discrepancies / Notes |
|:---|:---|:---|:---|:---|
| **Classic Clean** | `THR10C_Deluxe` | Fender Deluxe Reverb | Low-gain preamp for sparkling American-style cleans. 6L6 output stage voicing for brightness and a strong midrange. | None |
| **Boutique Clean** | `THR10C_BJunior2` | Fender Blues Junior (Modded) | Low-watt EL34-based boutique voicing. Higher gain settings thicken cleans and push into warm, bluesy overdrive. | None |
| **Modern Clean** | `THR30_Carmen` | Dr. Z Carmen Ghia | Boutique, low-watt EL84 design. Adds fullness, compression, and sustain as Master is turned up; excellent for neck pickups. | None |
| **Classic Crunch** | `THR10C_DC30` | Matchless DC30 (Modded) | EL84 power tubes in Class-A configuration. Highly responsive EQ with rich, complex harmonic tones and warm British chime overdrive. | Labeled `THR10_DC30` in sheet. |
| **Boutique Crunch** | `THR30_SR101` | Vox AC30 & Matchless DC30 | Mid-volume boutique design with 6550 power tubes voicing. Delivers tight bass response and a singing sustain. | Labeled **Modern Crunch** and associated with `THR30_SR101` in sheet. |
| **Modern Crunch** | `THR10C_Mini` | Dr. Z Mini Z (Modded) | Deceptively simple amp circuit (single 12AX7 & EL84). Full, no-frills tone highly responsive to picking dynamics. | Labeled **Boutique Crunch** and associated with `THR10C_Mini` in sheet. |
| **Classic Lead** | `THR10_Lead` | Marshall Plexi / Super Lead | Low-gain preamp with EL34-based power section. Breaks into classic British classic rock overdrive as Master is pushed. | None |
| **Boutique Lead** | `THR30_Blondie` | Marshall 1987X 50W Plexi (Modded) | Modified version of the Classic Lead circuit with extra gain, darker tone, and scooped midrange. | None |
| **Modern Lead** | `THR10_Brit` | Marshall JCM800 (Hot Rodded) | High-gain design with 12AX7s into EL34s. The classic hot-rodded British sound that defined 1980s hard rock. | None |
| **Classic Hi Gain** | `THR10_Modern` | Mesa/Boogie Dual Rectifier | Powerful modern high-gain distortion with thick low-end. Fills out significantly as Gain is pushed (use caution past 12 o'clock). | None |
| **Boutique Hi Gain** | `THR30_FLead` | German High Gain Amps | ECC83 preamp and 6L6 output voicing for tight modern metal/prog with a highly responsive EQ. | Inspired by Engl/Diezel. |
| **Modern Hi Gain** | `THR10X_Brown2` | EVH 5150-III Channel 3 (Modded) | Boosted/searing version of the Classic Special/Brown sound with massive gain for aggressive rhythms and leads. | None |
| **Classic Special** | `THR10X_Brown1` | EVH 5150-III Channel 2 (Modded) | Mid-to-high gain "Brown sound" voicing (12AX7/6L6). Clean/crunch rock to saturated rhythm/leads. | None |
| **Boutique Special** | `THR10X_South` | Krank Krankenstein (Modded) | Saturated metal voicing (four 12AX7s and 6L6s). Extremely tight, fast tracking for heavy down-tuned riffs. | None |
| **Modern Special** | `THR30_Stealth` | EVH 5150-III Stealth Channel 3 | Pre-boosted high-gain voicing with an overdrive circuit in front. Tightens low-end response, perfect for extended-range guitars. | None |
| **Classic Bass** | `THR10_Bass_Eden_Marcus` | Eden Terra Nova / Markbass Little Marcus | Woody, vintage bass preamp voicing with late breakup and clean articulation. | None |
| **Boutique Bass** | `THR10_Bass_Mesa` | Mesa/Boogie Subway | Full, modern bass tone that breaks into a rich, fuzzy overdrive when pushed hard. | None |
| **Modern Bass** | `THR30_JKBass2` | Marshall Bass Circuit | Vintage bass voicing with early breakup; overdrive character works exceptionally well for both bass and guitar. | None |
| **Acoustic Condenser** | `THR10_Aco_Condenser1` | Boutique Condenser Mic | Studio microphone emulation for acoustic-electric, providing airy, detailed, and pristine acoustic tone. | None |
| **Acoustic Tube** | `THR10_Aco_Tube1` | Boutique Tube Mic | Studio microphone emulation for acoustic-electric, adding warmth, harmonic saturation, and vintage depth. | None |
| **Acoustic Dynamic** | `THR10_Aco_Dynamic1` | Boutique Dynamic Mic | Studio microphone emulation for acoustic-electric, producing a direct, punchy, and feedback-resistant acoustic tone. | None |
| **Acoustic Nylon** | `THR10_Aco_Nylon1` | Nylon-string Preamp | Optimized frequency response and gain staging for nylon-string acoustic guitars. | Labeled as Nylon-string preamp. |
| **Flat Default** | `THR10_Flat` | Flat Line Input | Completely neutral line input response with no amp or speaker modeling. Excellent for acoustic modeling or keys. | None |
| **Flat Boutique** | `THR10_Flat_B` | Flat Line (Bass Boost) | Neutral line response with a slight bass boost to add body to auxiliary devices or keyboards. | None |
| **Flat Modern** | `THR10_Flat_V` | Flat Line (Mid Scoop) | Neutral line response with a slight midrange scoop for a hi-fi playback character. | Labeled `THR_Flat_V` in sheet. |

*Note: The physical preset spreadsheet and the app/hardware engine have a few naming/category swaps. For instance, the sheet swaps Boutique and Modern Crunch slots (`THR30_SR101` and `THR10C_Mini`) and swaps Classic Special and Modern Lead slots (`THR10_Brit` and `THR10X_Brown1`). The generator and tables above align with the app's internal naming scheme while documenting the sheet's designations.*

---

### Cabinet Mappings & Real-World Inspiration

| Index | Cabinet Name | Real-World Cabinet Model / Inspiration | Sheet Code / Based On |
|:---:|:---|:---|:---|
| **0** | British 4x12 | Marshall 1960A 4x12 (Celestion G12T-75) | `1960A` |
| **1** | American 4x12 | Mesa/Boogie Rectifier 4x12 (Celestion Vintage 30) | `MB PLATE 4x12` |
| **2** | Brown 4x12 | Peavey 5150 4x12 (Sheffield 1200) | `PV 5150` |
| **3** | Vintage 4x12 | Bogner 4x12 | `BGNR 4x12` |
| **4** | Fuel 4x12 | Diezel 4x12 | `DZL 4x12` |
| **5** | Juicy 4x12 | Orange 4x12 | `ORG 4x12` |
| **6** | Mods 4x12 | Hiwatt 4x12 (Fane speakers) | `HWT 4x12` |
| **7** | American 2x12 | Fender Twin Reverb 2x12 (Jensens) | `TRVB` |
| **8** | British 2x12 | Vox AC30 2x12 (Celestion Alnico Blues) | `AC3` |
| **9** | British Blues 2x12 | Marshall Bluesbreaker 2x12 | `BBRKR` |
| **10** | Boutique 2x12 | Matchless DC30 2x12 (Custom Celestion drivers) | `DC3` |
| **11** | Yamaha 2x12 | Yamaha F100-212 2x12 | `Yamaha F100-212` |
| **12** | California 1x12 | Mesa/Boogie Mark III 1x12 | `MB Mk3` |
| **13** | American 1x12 | Fender Deluxe Reverb 1x12 (Jensen C12K) | `DRVB` |
| **14** | American 4x10 | Fender Bassman 4x10 Tweed (Jensens) | `TWEED` |
| **15** | Boutique 1x12 | Boutique Japanese Custom Build 1x12 | `Boutique Japanese custom build cabinet` |
| **16** | None / BYPASS | Bypass / Flat response (No speaker simulation) | N/A |
