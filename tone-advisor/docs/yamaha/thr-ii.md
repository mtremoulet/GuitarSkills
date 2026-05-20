# Yamaha THR-II Preset Format (.thrl6p)

The Yamaha THR-II series (THR10II, THR30II) uses a JSON-based format for its presets, typically with the `.thrl6p` extension. These files are compatible with the **THR Remote** app.

**Note:** The extension is often written as `.thrl6p` (with a lowercase 'L' and the number '6'), which is sometimes mistaken for `.thr16p`.

## Core Schema
- **Schema Name:** `L6Preset`
- **Format:** JSON
- **Version:** Commonly `5` for THR-II

## File Structure

```json
{
  "schema": "L6Preset",
  "version": 5,
  "data": {
    "device": 48,
    "device_version": 65536,
    "meta": {
      "name": "Preset Name",
      "tnid": 0
    },
    "tone": {
      "THRGroupAmp": { ... },
      "THRGroupCab": { ... },
      "THRGroupFX1Compressor": { ... },
      "THRGroupFX2Effect": { ... },
      "THRGroupFX3EffectEcho": { ... },
      "THRGroupFX4EffectReverb": { ... },
      "THRGroupGate": { ... },
      "global": { ... }
    }
  }
}
```

## Parameter Keys by Group

### 1. THRGroupAmp (Amplifier)
| Key | Description | Type |
|-----|-------------|------|
| `@asset` | Amp model identifier | string |
| `Bass` | Bass level | number (0.0 - 1.0) |
| `Drive` | Gain/Drive level | number (0.0 - 1.0) |
| `Master` | Master volume | number (0.0 - 1.0) |
| `Mid` | Middle frequencies | number (0.0 - 1.0) |
| `Treble` | Treble frequencies | number (0.0 - 1.0) |

### 2. THRGroupCab (Cabinet)
| Key | Description | Type |
|-----|-------------|------|
| `@asset` | Cabinet model identifier | string |
| `SpkSimType` | Speaker simulation type | string |

### 3. THRGroupFX1Compressor
| Key | Description | Type |
|-----|-------------|------|
| `@asset` | Compressor type | string |
| `@enabled` | On/Off toggle | boolean |
| `Level` | Output level | number |
| `Sustain` | Compression sustain | number |

### 4. THRGroupFX2Effect (Modulation)
| Key | Description | Type |
|-----|-------------|------|
| `@asset` | Effect type (Chorus, Flanger, Phaser, Tremolo) | string |
| `@enabled` | On/Off toggle | boolean |
| `@wetDry` | Mix ratio | number |
| `Depth` | Modulation depth | number |
| `Feedback` | Feedback amount | number |
| `Freq` | Frequency/Speed | number |
| `Pre` | Pre-delay / Initial param | number |

### 5. THRGroupFX3EffectEcho (Delay)
| Key | Description | Type |
|-----|-------------|------|
| `@asset` | Delay type | string |
| `@enabled` | On/Off toggle | boolean |
| `@wetDry` | Mix ratio | number |
| `Bass` | Low-end of echo | number |
| `Feedback` | Number of repeats | number |
| `Time` | Delay time | number |
| `Treble` | High-end of echo | number |

### 6. THRGroupFX4EffectReverb
| Key | Description | Type |
|-----|-------------|------|
| `@asset` | Reverb type | string |
| `@enabled` | On/Off toggle | boolean |
| `@wetDry` | Mix ratio | number |
| `Decay` | Reverb tail length | number |
| `PreDelay` | Delay before reverb starts | number |
| `Tone` | Reverb brightness | number |

### 7. THRGroupGate (Noise Gate)
| Key | Description | Type |
|-----|-------------|------|
| `@asset` | Gate identifier | string |
| `@enabled` | On/Off toggle | boolean |
| `Decay` | Release speed | number |
| `Thresh` | Threshold level | number |

### 8. Global
| Key | Description | Type |
|-----|-------------|------|
| `THRPresetParamTempo` | BPM/Tempo setting | number |

---

## Technical Context
The parameter values are typically normalized between `0.0` and `1.0`. These files are interpreted by the THR Remote app and sent to the amplifier via MIDI SysEx commands.
