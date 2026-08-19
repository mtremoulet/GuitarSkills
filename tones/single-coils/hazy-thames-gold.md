---
id: "hazy-thames-gold"
preset_name: "Hazy Thames Gold SC"
created: 2026-08-17
updated: 2026-08-17
guitar: "Fender Player II Telecaster / Squier Stratocaster (single-coils)"
target: "Shimmering, airy Blackface clean with warm tape bloom and subtle dimensional widening — inspired by London's warm August sun breaking through Thames morning haze."
tags: "clean, ambient, dream-65, single-coil, telecaster, stratocaster, tape-echo, dimension-d, sparkle, blackface, london-weather"
tone-king-channel: "bypassed"
amp: "Dream '65 (UADx)"
status: "initial"
pickup_type: "single-coil"
preset_data:
  amp_platform: "uad_paradise"
  amp_settings:
    Volume: 3.2
    Treble: 5.4
    Bass: 4.8
    Reverb: 2.5
    Bright: false
    Mod: "D-Tex"
  la2a:
    peak_reduction: 25.0
    gain: 25.0
    compress: true
  galaxy:
    echo_rate: 4.5
    feedback: 2.2
    echo_volume: 2.0
    reverb_volume: 0.0
    head_select: 1
    tape_age: "used"
  studio_d:
    mode: "1"
    power: true
  logic_eq:
    band1:
      on: true
      freq: 75.0
      slope: 24.0
    band4:
      on: true
      freq: 340.0
      gain: -1.8
      q: 1.5
    band7:
      on: true
      freq: 10000.0
      gain: 1.5
---

# Hazy Thames Gold SC

## Target Sound

Inspired by London's warm August afternoon weather — 26°C sunny intervals cutting through lingering morning river haze with a gentle breeze — **Hazy Thames Gold** captures a sparkling, high-headroom American Blackface clean tone wrapped in vintage tape warmth and acoustic dimension.

Rather than a dry, sterile DI clean, this toneprint uses the **UADx Dream '65** (Fender Deluxe Reverb '65) with the **D-Tex mod** engaged to add rich harmonic overtones and round off single-coil glassiness. An inline **UADx Studio D Chorus** in Dimension Mode 1 provides a subtle, phase-coherent stereo spread without feeling chorus-heavy, while a dedicated parallel **Galaxy Tape Echo** bus adds an organic, fluttering ambient cushion that mirrors sunlight dancing on shifting water.

> [!TIP]
> **Pure Direct Input Path:**
> To ensure optimal dynamic response and pristine gain staging, this toneprint routes your guitar directly into the **Audient iD14 JFET D.I. input** (bypassing the Tone King Imperial Preamp entirely). The iD14 input calibration (-3.2 dB plugin input trim) gives you the exact headroom intended by UAD's analog modeling.

---

## Signal Chain

```
[Telecaster/Strat] → [Audient iD14 DI] → [UADx Dream '65] → [UADx Studio D] → [UADx LA-2A] → [Logic Channel EQ]
                                                                                                    ↓
                                                                                        [Bus 4: Galaxy Tape Echo]
```

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

| Component | Setting | Purpose |
|---|---|---|
| **Guitar Input** | Instrument Input 1 (JFET D.I.) | Dedicated discrete high-impedance input stage with natural tube-like harmonic warmth |
| **Gain Knob** | Minimum / Set to peak at ~−18 dBFS | Bypasses interface coloration and preserves full clean headroom |
| **Tone King Imperial** | **Bypassed** | Bypassed — software amp simulation runs standalone |
| **TONEX One** | **Bypassed** | Completely transparent pass-through |

---

### 2. UADx Dream '65 Reverb Amp — character & core chime

The Dream '65 delivers articulate Blackface snap with warm low-end sag and authentic spring reverb.

| Control | Setting | Purpose |
|---|---|---|
| **Channel / Bright** | **Normal (Bright OFF)** | Tames single-coil ice-pick frequencies on the Tele bridge/neck |
| **Mod Circuit** | **D-Tex** | Adds warm, woody midrange overtones and tube saturation |
| **Volume** | **3.2** | Clean foundation with touch-sensitive bloom on harder strums |
| **Treble** | **5.4** | Clear, airy top-end definition without harshness |
| **Bass** | **4.8** | Tight, rounded low-end that stays firm under chord work |
| **Reverb** | **2.5** | Subtle onboard spring reverb wash for vintage depth |
| **Cabinet** | **GB25 (1x12 Celestion Greenback)** | Warms up the high frequencies compared to the Oxford 12K5 |
| **Input Gain (IN)** | **−3.2 dB** | Calibrates Audient iD14 DI level (+9 dBu) to UAD standard (+12.2 dBu) |

---

### 3. UADx Studio D Chorus — subtle spatial widening

| Control | Setting | Purpose |
|---|---|---|
| **Mode** | **1** | Lowest intensity dimension spread; enhances width without pitch warble |
| **Power** | **ON** | Active |

---

### 4. UADx LA-2A Silver Compressor — smooth optical leveling

| Control | Setting | Purpose |
|---|---|---|
| **Peak Reduction** | **25.0** | Gentle 1.5–2.5 dB gain reduction on peaks; stabilizes note decays |
| **Gain** | **25.0** | Clean makeup gain to maintain target DAW level (~−12 dBFS) |
| **Mode** | **Compress** | Smooth 3:1 optical leveling curve |

---

### 5. Post-FX Polish — Logic Channel EQ

| Band | Frequency | Gain / Slope | Q / Role |
|---|---|---|---|
| **High-Pass (Band 1)** | 75 Hz | 24 dB/oct | Removes sub-low rumble and unwanted boominess |
| **Low-Mid Notch (Band 4)** | 340 Hz | −1.8 dB | 1.5 Q — clears out cloudy boxiness in the low-mids |
| **High-Shelf Air (Band 7)** | 10.0 kHz | +1.5 dB | Adds open, shimmering golden air to the single-coil decay |

---

### 6. Spatial Effects — Dedicated Aux Bus

#### Bus 4 (Tape Echo): UADx Galaxy Tape Echo (100% Wet on Aux Return)
* **Head Select**: **1** (single clean repeat).
* **Echo Rate**: **4.5** (~240 ms slap-ambient tempo sync).
* **Feedback**: **2.2** (2 gentle trailing repeats that melt into the background).
* **Tape Age**: **Used** (introduces warm top-end damping and slight motor wow/flutter).
* **Logic Send Level**: **−20 dB** (sits behind the dry tone as an airy haze).

---

## Starting Point Guide

- **Guitar Controls**: On a Telecaster bridge pickup, roll the **Tone knob back to 8** and **Volume to 8.5** for maximum sweetness. On a Stratocaster, the **neck + middle (position 4)** is liquid gold with this chain.
- **First adjustment**: If you want a more ethereal, washed-out ambient sound, increase the Send to **Bus 4 (Galaxy Echo)** up to **−14 dB**.
- **Bright switch**: If playing a darker neck pickup with flatwounds, engage the **Bright switch** on the Dream '65 to restore snap.

---

## Feedback History

### 2026-08-17 — initial
Designed to capture the London late-summer weather aesthetic: warm sunshine breaking through Thames haze. Calibrated for single-coil guitars (Telecaster/Stratocaster) using the UADx Dream '65 (D-Tex mod), subtle Studio D spatial spreading, gentle LA-2A optical leveling, and a parallel Galaxy Tape Echo ambient bed. Direct Input into Audient iD14 DI with -3.2 dB calibration offset.
