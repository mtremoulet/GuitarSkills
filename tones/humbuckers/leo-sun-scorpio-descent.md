---
id: "leo-sun-scorpio-descent"
preset_name: "Leo Sun Scorpio Descent HB"
created: 2026-08-17
updated: 2026-08-17
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (humbuckers)"
target: "Regal, singing British edge-of-breakup lead and chord bloom steeped in deep Capitol chamber ambience — channeling the radiant warmth of Leo and brooding depth of Scorpio."
tags: "edge-of-breakup, chime, vox, ruby-63, humbucker, les-paul, sheraton, capitol-chambers, la2a, leo-scorpio, astrology"
tone-king-channel: "bypassed"
amp: "Ruby '63 (UADx)"
status: "initial"
pickup_type: "humbucker"
preset_data:
  amp_platform: "uad_paradise"
  amp_settings:
    Channel: "Brilliant"
    Volume: 4.8
    Boost: 2.5
    Boost Switch: "ON"
    Cut: "ON"
    Treble: 5.2
    Bass: 4.6
    Tone Cut: 5.8
    Cabinet: "Green"
    Room: 4.0
  la2a:
    peak_reduction: 32.0
    gain: 28.0
    compress: true
  hitsville:
    decay: 3.8
    mix: 0.18
    pre_delay: 24.0

    wet_solo: false
  logic_eq:
    band1:
      on: true
      freq: 80.0
      slope: 24.0
    band4:
      on: true
      freq: 580.0
      gain: -1.5
      q: 1.4
    band7:
      on: true
      freq: 4800.0
      gain: -1.0
---

# Leo Sun Scorpio Descent HB

## Target Sound

Conceived from the cosmic convergence of the **Sun in Leo** (bold, singing harmonic presence and regal warmth) and the **Moon crossing into Scorpio** (deep, introspective, shadowy acoustic depth), this toneprint is designed for rich dual-humbucker guitars like the **Gibson Les Paul Studio** or **Epiphone Sheraton II**.

Built upon the **UADx Ruby '63** (Vox AC30 Top Boost), it uses the **Brilliant channel** with the **EP-III Boost circuit** engaged at a modest setting (2.5). This pushes the virtual EL84 power section into a singing, touch-sensitive edge-of-breakup lead tone that roars when you dig in and purrs when you play softly. The **Cut switch** and **Tone Cut control** tame humbucker low-end flub and digital treble harshness, while the **UADx LA-2A** and a deep **Capitol Chambers / Hitsville** decay envelop the sound in an expansive, mystical twilight.

> [!TIP]
> **Pure Direct Input Path:**
> By connecting your guitar directly to the **Audient iD14 JFET D.I. input** (bypassing the physical Tone King Imperial Preamp), you preserve the natural, vocal midrange of your humbuckers. The internal -3.2 dB input gain calibration ensures the Ruby's Top Boost stage reacts with authentic headroom and dynamic touch.

---

## Signal Chain

```
[Les Paul / Sheraton] → [Audient iD14 DI] → [UADx Ruby '63] → [UADx LA-2A] → [Logic Channel EQ]
                                                                                      ↓
                                                                      [Bus 3: Capitol Chambers / Hitsville]
```

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

| Component | Setting | Purpose |
|---|---|---|
| **Guitar Input** | Instrument Input 1 (JFET D.I.) | Discrete high-impedance JFET input provides tube-like impedance loading |
| **Gain Knob** | Minimum / Set to peak at ~−18 dBFS | Clean, unclipped dynamic headroom |
| **Tone King Imperial** | **Bypassed** | Bypassed — prevents double-preamping and midrange pre-scooping |
| **TONEX One** | **Bypassed** | Fully bypassed transparent route |

---

### 2. UADx Ruby '63 Top Boost Amp — regal chime & vocal grit

| Control | Setting | Purpose |
|---|---|---|
| **Channel** | **Brilliant** | Top Boost circuit provides rich harmonic overtone bloom on humbuckers |
| **Volume** | **4.8** | Edge-of-breakup sweet spot: cleans up with volume rollback, sings under attack |
| **Boost Switch** | **ON** | Engages the modeled EP-III tape echo preamp boost |
| **Boost Level** | **2.5** | Adds velvety tube saturation and sustain without fizzy clipping |
| **Cut Switch** | **ON** | **Crucial for humbuckers:** cuts sub-bass mud before the preamp stage |
| **Top Boost Treble** | **5.2** | Balances high-mid presence and vowel-like clarity |
| **Top Boost Bass** | **4.6** | Tight, focused low end that won't overwhelm headphone monitoring |
| **Tone Cut** | **5.8** | *(Clockwise = roll-off)* Smooths out high-frequency transient bite |
| **Cabinet** | **Green (2x12 Celestion G12H)** | Mic'd with ribbon; warms the midrange and rounds off aggressive highs |
| **Input Gain (IN)** | **−3.2 dB** | Calibrates iD14 (+9 dBu) to UAD analog modeling reference (+12.2 dBu) |

---

### 3. UADx LA-2A Silver Compressor — smooth vocal sustain

| Control | Setting | Purpose |
|---|---|---|
| **Peak Reduction** | **32.0** | Provides 2–4 dB of smooth opto-compression, enhancing singing sustain |
| **Gain** | **28.0** | Restores level for an authoritative, forward mix presence (~−11 dBFS) |
| **Mode** | **Compress** | Gentle optical leveling preserving expressive touch sensitivity |

---

### 4. Post-FX Polish — Logic Channel EQ

| Band | Frequency | Gain / Slope | Q / Role |
|---|---|---|---|
| **High-Pass (Band 1)** | 80 Hz | 24 dB/oct | Cleans sub-bass rumble to keep the mix tight |
| **Mid Notch (Band 4)** | 580 Hz | −1.5 dB | 1.4 Q — carves a slight dip in nasal lower-mid frequencies |
| **High Tame (Band 7)** | 4.8 kHz | −1.0 dB | Subtle softening of aggressive pick transients on headphones |

---

### 5. Spatial Effects — Bus-First Aux Routing

#### Bus 3 (Chamber Reverb): UADx Capitol Chambers / Hitsville (100% Wet on Aux Return)
* **Space / Chamber**: **Chamber 4 (or Hitsville Chamber 1)**.
* **Decay Time**: **3.8 seconds** (vast, dark acoustic space representing Scorpio's depths).
* **Pre-Delay**: **24 ms** (keeps the guitar attack dry and articulate before the reverb blooms).
* **Tone / Filter**: Slightly darkened top-end roll-off to avoid metallic reflections.
* **Logic Send Level**: **−16 dB** (creates a luxurious, atmospheric depth behind lead lines).

---

## Starting Point Guide

- **Guitar Volume & Tone Sweet Spot**: Set your neck pickup **Volume to 7.5** and **Tone to 7**. This brings out an astonishingly woody, vocal tone. Roll Volume to **10** when you want a rich, saturated Leo roar.
- **First adjustment**: If the tone feels too warm for rhythm chords, flip the **Cut Switch to OFF** or reduce **Tone Cut to 4.5** to reintroduce classic British chime.
- **Sheraton II vs. Les Paul**: On semi-hollow guitars like the Sheraton II, the acoustic body adds extra low-mid resonance; try nudging the **Treble up to 5.6** if needed.

---

## Feedback History

### 2026-08-17 — initial
Created around the astrological dynamic of the Sun in Leo and Moon transitioning into Scorpio. Calibrated for dual-humbucker guitars (Gibson Les Paul Studio / Epiphone Sheraton II) running Direct Input into the Audient iD14. Utilizes UADx Ruby '63 on the Brilliant channel with EP-III boost, LA-2A optical sustain, and a cavernous Capitol/Hitsville chamber reverb on Aux Bus 3.
