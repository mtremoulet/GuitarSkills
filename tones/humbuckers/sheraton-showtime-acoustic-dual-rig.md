---
amp: "Showtime '64 + Acoustic Voice Pro (UADx / Nembrini)"
created: 2026-04-30
guitar: "Epiphone Sheraton II (Humbuckers)"
id: sheraton-showtime-acoustic-dual-rig
pickup_type: humbucker
preset_name: "Sheraton Showtime Acoustic Dual Rig"
status: tested
tags: "dual-amp, humbucker, sheraton, jazz, warm-clean, acoustic-blend, showtime, acoustic-voice, semi-hollow, parallel"
target: 'Warm clean jazz electric foundation (Showtime 64) blended in parallel with an acoustic body texture (Nembrini Acoustic Voice Pro) for semi-hollow humbuckers.'
tone-king-channel: bypassed
updated: 2026-08-23
dual_rig: true
amp_a:
  name: "Amp A — Showtime '64 (Warm Jazz Clean Anchor)"
  model: "Showtime '64 (UADx)"
  platform: uad_paradise
  pan: -12
  amp_settings:
    Volume: 3.0
    Treble: 4.0
    Middle: 5.0
    Bass: 5.0
    Bright: false
    Cab: "2x12 Showman (UADx)"
    Output Gain: 8.0
amp_b:
  name: "Amp B — Acoustic Voice Pro (Acoustic Texture Blend)"
  model: "Acoustic Voice Pro (Nembrini Audio)"
  platform: nembrini_acoustic_voice
  pan: 12
  amp_settings:
    InputMode: 0.0
    MicType: 4.0
    DiPreampPower: true
    DiPreampGain: 0.0
    DiPreampBlend: 60.0
    DiPreampNotch: 360.0
    DiPreampOut: 1.0
    CompressorPower: false
    ModPower: false
    DelayPower: false
    ReverbPower: false
  nembrini_acoustic_voice:
    DiPreampGain: 0.0
    DiPreampNotch: 360.0
    DiPreampBlend: 60.0
    DiPreampOut: 1.0
    DiPreampPower: true
    CompressorPower: false
    DelayPower: false
    ModPower: false
    ReverbPower: false
    InputMode: 0.0
    MicType: 4.0
shared_fx:
  la2a:
    gain: 45.0
    peak_reduction: 28.0
  hitsville:
    decay: 1.8
    mix: 0.15
    pre_delay: 20.0

    wet_solo: false
  logic_eq:
    band1: { freq: 80.0, on: true, slope: 4.0 }
    band4: { freq: 650.0, gain: -2.0, on: true, q: 1.5 }
    band7: { freq: 5000.0, gain: -1.5, on: true }
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
---

# Sheraton Showtime + Acoustic Voice Pro — Warm Jazz & Acoustic Blend (Humbuckers)

## Target Sound

A warm, even-keel jazz electric tone as the foundation, blended in parallel with an acoustic body texture to add wood, acoustic envelope, and resonant dimension for the **Epiphone Sheraton II**:

* **Amp A (Left, Pan -12 — Showtime '64 High-Headroom Foundation)**: Provides unyielding clean headroom, piano-like fundamental clarity, and sweet top end without flubbing or sagging on neck humbuckers.
* **Amp B (Right, Pan +12 — Nembrini Acoustic Voice Pro Texture)**: Processes a parallel copy of the signal through Gibson L-00 body modeling and AKG C414 condenser mic emulation to add acoustic presence and wood resonance under the electric tone.

The Acoustic Voice Pro sits at a lower level under the electric foundation (felt more than heard) to thicken the fundamental note attack, while shared LA-2A bus compression and Capitol/Hitsville chamber reverb glue the stereo soundstage together.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Pre-Split Option (Guitar Input Track)

| Plugin / Pedal | Control | Setting | Purpose |
|----------------|---------|---------|---------|
| **Logic Channel EQ** | HPF (Band 1) | **80 Hz, 24 dB/oct** | Removes sub-low rumble below guitar range |
| **Logic Channel EQ** | Bell (Band 4) | **650 Hz, −2.0 dB (Q 1.5)** | Tames boxy upper midrange in semi-hollow humbuckers |
| **Logic Channel EQ** | Hi Shelf (Band 7) | **5 kHz, −1.5 dB** | Gentle high-frequency smoothing for jazz warmth |
| **Gold Overdrive** | State / Gain / Treble / Output | **Off / 0.0 / 4.5 / 7.5** | Transparent solo clean boost on standby |

---

### 3. Parallel Amp Configuration

#### Channel Strip A: Showtime '64 — Warm Jazz Clean Foundation (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **3.0** | Clean, uncompressed jazz headroom |
| Treble | **4.0** | Warm top end without bright cap bite |
| Middle | **5.0** | Balanced, full frequency response |
| Bass | **5.0** | Solid low-end body for jazz chord melody |
| Bright | **Off** | Smooth, rounded high frequencies |
| Cab | **2x12 Showman (UADx)** | High-headroom clean projection |
| Output Gain | **8.0 dB** | Level matched with Amp B |

#### Channel Strip B: Acoustic Voice Pro — Acoustic Texture Blend (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Input Mode | **Humbucker (0.0)** | Matches Sheraton pickup impedance and transient envelope |
| Body Model | **GIB 00 (Gibson L-00)** | Small parlor body, warm low-mids, intimate resonance |
| Microphone | **Condenser 414 (AKG C414)** | Transparent, neutral condenser character for smooth blend |
| DI Preamp Power | **On** | Enables DI preamp circuit and notch filter |
| DI Preamp Notch | **3.5 kHz (360.0)** | Notches out nasal resonance activated by humbuckers |
| DI Preamp Blend | **60.0%** | Blends preamp body modeling with direct signal |
| DI Preamp Gain / Out | **0.0 / 1.0** | Unity gain structure |
| Compressor / FX | **Off** | Compression and spatial effects handled on shared bus |

---

### 4. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Metering**: Solo Amp A and Amp B independently using Logic's Loudness Meter. Confirm balanced parity with Amp B blended subtly beneath Amp A.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **28.0**, Gain **45.0**) gently gluing the acoustic and electric layers together.
* **Spatial Reverb**: UAD Capitol Chambers / Hitsville (Mix **15%**, Decay **1.8s**, Pre-Delay **20ms**) on parallel aux send.

---

## Starting Point Guide

- **Acoustic Blend Balance**: Adjust Amp B channel fader (starting at −8 dB relative to Amp A). The acoustic model should be felt as resonance and harmonic depth rather than a distinct acoustic guitar.
- **Body Model Alternatives**: If GIB 00 feels too dark or warm, switch Amp B Body Model to **TAY 814 (Taylor 814ce)** for a more modern, balanced string presence.
- **Jazz Top-End Contour**: To darken further for vintage Joe Pass warmth, adjust the pre-split Channel EQ Band 7 Hi Shelf or roll the Sheraton neck tone pot to **6–7**.

---

## Feedback History

### 2026-04-30 — initial → tested
Designed for Sheraton humbuckers. Tone King Rhythm channel at very low Volume (3) to minimize preamp coloring going into Acoustic Voice Pro. Full Logic routing via Bus 1 → two parallel Aux strips → shared reverb bus. Acoustic Voice Pro is used as a texture blend, not a full acoustic emulation — at −8 dB it adds body and harmonic dimension without competing with the electric signal. 610-B HI Shelf at 10 kHz, −3 dB is the primary voicing choice for jazz warmth.

### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.

### 2026-08-23 — refactored to parallel dual-rig architecture
Transitioned from legacy single-amp toneprint format into the standardized parallel dual-rig architecture (`dual_rig: true`, `amp_a`, `amp_b`, `shared_fx`). Amp A runs Showtime '64 (Pan −12 L) and Amp B runs Nembrini Acoustic Voice Pro (Pan +12 R) with shared LA-2A bus glue and chamber reverb.
