---
id: "a-night-settling-in"
preset_name: "A Night Settling In"
created: "2026-10-19"
updated: "2026-10-19"
guitar: "2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90s HSP-90s, Neck Pickup)"
target: "Intimate, warm nocturnal jazz & neo-soul clean tone combining optical leveling, discrete harmonic saturation, custom wood/cavity EQ sculpting, pitch vibrato, OwnHammer 1x10 Thiele IR with speaker dynamics, and asymmetric unitary matrix diffusion."
tags: "jazz, neo-soul, p-90, les-paul, omakase-bento, faust-and-wagner, virtual-pedalboard, liberty-burnisher, mechanica, aesthetica, irdx-studio, ownhammer, thiele, warm, nocturnal"
tone-king-channel: bypassed
amp: "Omakase Bento (Faust & Wagner)"
status: tested
pickup_type: p-90
virtual_pedalboard_preset_id: "6D6EE798-013A-4BC1-9062-B5A22159271B"
preset_data:
  homunculus:
    boost: 0.0
    ref_pitch: 440.0
    tuning_mode: "Chromatic / Strobe (1)"
    output_mode: "Through (0)"
    in_trim: 0.0
    out_trim: 0.0
  seven_samurai:
    eq_100hz: 0.0
    eq_200hz: 0.0
    eq_400hz: 0.0
    eq_800hz: 0.0
    eq_1600hz: 0.0
    eq_3200hz: 0.0
    eq_6400hz: 0.0
    level: 0.0
  liberty_burnisher:
    drive: 0.15
    burnish: 45.0
    air: -2.5
    ge_warmth: 30.0
    master: 0.0
    charge_pump_18v: false
  stumblelater:
    input_send: 0.6
    output_return: 0.7
    master: 0.0
  mechanica:
    engine: "Spring / Mechanical (0)"
    mix: 15.0
    pre_delay: 10.0
    decay: 2.2
    tone: 3800.0
    modulation: 15.0
    character: 0.0
    level: 0.0
  omakase_bento:
    leveler_on: true
    leveler_sensitivity: 3.0
    brown_sugar_on: false
    solo: 0.0
    sea_salt: 4.0
    drive: 7.0
    bass: 0.0
    wood: 2.0
    cavity: -2.0
    mids: 1.0
    treble: 0.0
    volume: 6.0
    vibrato_on: true
    vibrato_speed: 3.5
    vibrato_depth: 2.5
    heat_source: 0.0
    master: 8.0
    cab_sim: false
  irdx_studio:
    plugin_name: "IRDX Studio Free"
    loaded_ir: "OwnHammer 1x10 Thiele"
    speaker_dynamics_on: true
    speaker_dynamics_value: 100.0
    autoalign: true
    multimix_x: 0.360
    multimix_y: 0.428
    output: 0.0
  aesthetica:
    matrix: "Givens SO(8) - Asymmetric Realism (2)"
    mix: 20.0
    pre_delay: 10.0
    decay: 1.25
    tone: 5500.0
    room_size: 30.0
    diffusion: 40.0
    er_late: 55.0
    modulation: 18.0
    level: 0.0
---

# A Night Settling In

## Target Sound

An intimate, velvety nocturnal jazz and neo-soul clean tone dialed specifically for the **2008 Epiphone Les Paul Standard Plus Top** loaded with **Tonerider Rebel 90 (P-90)** pickups (as cataloged in `tone-advisor/guitar_stable.md`).

I know that humbucker-sized P-90 single coils like the Tonerider Rebel 90 blend the fat lower-mid punch of a Gibson-scale solid mahogany body with the open top-end attack and string definition of a single-coil. In this toneprint, the signal undergoes layered staging designed for relaxed late-night playing:
1. **Preamplification & Conditioning**: Clean line driving through **Homunculus**, flat baseline inductor EQ with **7 Samurai**, followed by **Liberty Burnisher** providing gentle Germanium warmth and rolling off harsh air (-2.5 dB).
2. **Dynamic Smoothing & FX Buffering**: Tube impedance buffering with **Stumblelater**, feeding into subtle mechanical spring reflections via **Mechanica** (15% mix, 2.2s decay) before the primary preamp stage.
3. **Core Tone Machine — Omakase Bento**: Smooth optical compression (**Leveler** Sensitivity 3.0), rich harmonic overdrive (Drive 7.0, Sea Salt 4.0), specialized body resonance shaping (Wood +2.0 dB for acoustic roundness, Cavity -2.0 dB to scoop muddy low-mids, Mids +1.0 dB for vocal authority), and lush analog pitch modulation (**Vibrato** at 3.5 Hz, Depth 2.5). The internal 10-inch cab is bypassed.
4. **Dynamic Speaker Response & Acoustic Space**: **IRDX Studio Free** hosts the **OwnHammer 1x10 Thiele** cabinet impulse and imparts dynamic speaker cone nonlinearities (100% Speaker Dynamics) with MultiMix cabinet blending, cascading into **Aesthetica** set to an asymmetric Givens SO(8) unitary matrix for plush, uncolored spatial depth.

---

## Signal Chain

```
[2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90 Neck)]
  ──► [Audient iD14 Input 1 (D.I. 0 dB)]
  ──► [Host: Virtual Pedalboard (6D6EE798-013A-4BC1-9062-B5A22159271B.vpreset)]
        ├── [1. Homunculus] (Master Strobe Tuner & Discrete Line Driver)
        ├── [2. 7 Samurai] (7-Band Graphic Inductor EQ — Unity Flat)
        ├── [3. Liberty Burnisher] (Discrete Class-A Preamp & Germanium Burnish)
        ├── [4. Stumblelater] (Tube Buffered FX Loop Level Matcher)
        ├── [5. Mechanica] (Mechanical & Spring Reverb Tank)
        ├── [6. Omakase Bento] (Optical Leveler + Drive + Wood/Cavity EQ + Vibrato)
        ├── [7. IRDX Studio Free] (Bogren Dynamic Speaker Nonlinearity + OwnHammer 1x10 Thiele IR)
        └── [8. Aesthetica] (Givens SO(8) Asymmetric Matrix Room Diffusion)
  ──► [Output Monitoring: Sennheiser HD660S2]
```

### 1. Hardware Front-End & Input Calibration

* **Tone King Imperial Preamp**: **Bypassed** (per the direct input standard in `tone-advisor/TONEPRINT_GUIDELINES.md`). Signal path connects directly into Audient iD14 Instrument Input 1.
* **Hardware Interface Gain**: **0 dB** (unity).
* **Host**: **Virtual Pedalboard** serial rig preset `A Night Settling In` (`6D6EE798-013A-4BC1-9062-B5A22159271B.vpreset`).
* **Routing**: 2→2 Stereo across all active slots.

---

### 2. Homunculus — Master Polyphonic Strobe Tuner & Line Driver

*Role: High-impedance discrete instrument buffer, line driver, and silent reference tuner.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Boost** | **0.0 dB** | Transparent unity buffer. |
| **Reference Pitch** | **440.0 Hz** | Concert pitch standard. |
| **Tuning Mode** | **1 (Chromatic/Strobe)** | Precision strobe detection. |
| **Output Mode** | **0 (Through)** | Unmuted audio pass-through. |
| **In Trim / Out Trim** | **0.0 dB / 0.0 dB** | Calibrated unity. |
| **Bypass** | **0 (Active)** | Line driver engaged. |

---

### 3. 7 Samurai — 7-Band Graphic Inductor EQ

*Role: System EQ baseline and precision frequency utility.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **100 Hz** | **0.0 dB** | Flat low-end baseline. |
| **200 Hz** | **0.0 dB** | Flat warm baseline. |
| **400 Hz** | **0.0 dB** | Flat body baseline. |
| **800 Hz** | **0.0 dB** | Flat vocal mid baseline. |
| **1.6 kHz** | **0.0 dB** | Flat bite baseline. |
| **3.2 kHz** | **0.0 dB** | Flat presence baseline. |
| **6.4 kHz** | **0.0 dB** | Flat air baseline. |
| **Level** | **0.0 dB** | Master unity level. |
| **Bypass** | **0 (Active)** | Circuit active. |

---

### 4. Liberty Burnisher — Discrete Preamp & Harmonic Saturator

*Role: Pick-attack rounding, Germanium warmth, and high-frequency softening.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Drive** | **0.15** | Subtle discrete saturation edge on pick dig. |
| **Burnish** | **45.0%** | Rich even-order harmonic coloration. |
| **Air** | **-2.5 dB** | Shelves ultrasonic frequencies to tame P-90 single-coil snap. |
| **Ge Warmth** | **30.0%** | Germanium soft-knee compression and symmetry. |
| **Master Volume** | **0.0 dB** | Unity output trim. |
| **18V Charge Pump** | **0 (Off)** | Vintage 9V headroom with earlier harmonic compression. |
| **Bypass** | **0 (Active)** | Circuit active. |

---

### 5. Stumblelater — Tube FX Loop Buffer & Level Matcher

*Role: Impedance transformation and inter-stage analog gain buffering.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Input / Send** | **0.6** | Controlled send level to prevent inter-stage overloading. |
| **Output / Return** | **0.7** | Calibrated recovery gain restoring dynamic impact. |
| **Master Volume** | **0.0 dB** | Master level trim. |
| **Bypass** | **0 (Active)** | Tube buffer stage engaged. |

---

### 6. Mechanica — Reverb & Resonance Laboratory

*Role: Pre-amp spring and mechanical reverb wash.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Engine** | **0 (Spring/Mechanical)** | Vintage mechanical spring tank emulation. |
| **Mix** | **15.0%** | Subtle pre-amp spatial depth without obscuring chord voicing. |
| **Pre-Delay** | **10.0 ms** | Clean pick-attack separation before spring splash. |
| **Decay** | **2.2 s** | Moderate tank decay time. |
| **Tone** | **3800.0 Hz** | Warm high-cut damping preventing metallic ping. |
| **Modulation** | **15.0%** | Tank chorus flutter dispersing stationary modes. |
| **Character** | **0.0** | Linear vintage tank response. |
| **Level** | **0.0 dB** | Unity output trim. |

---

### 7. Omakase Bento — Complete Preamp, Leveler & Tone Machine

*Role: Primary amplifier foundation, optical dynamic leveling, harmonic tone sculpting, and power section vibrato.*

| Section / Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Sweetener / Leveler** | **ON (1)** | Optical compressor smoothing single-note peaks. |
| **Sweetener / Lev Sens** | **3.0** | Gentle leveling threshold preserving touch-sensitivity. |
| **Sweetener / Brown Sugar** | **OFF (0)** | Pre-compression boost bypassed for clean headroom. |
| **Seasoning / Drive** | **7.0** | Rich preamp harmonic saturation at edge-of-breakup. |
| **Seasoning / Sea Salt** | **4.0** | Upper-mid harmonic chime and presence. |
| **Seasoning / Bass** | **0.0 dB** | Tight, unhyped bass response. |
| **Seasoning / Wood** | **+2.0 dB** | Emphasizes carved maple cap and mahogany body acoustic resonance. |
| **Seasoning / Cavity** | **-2.0 dB** | Scoops boxy lower-mid clutter (350–450 Hz). |
| **Seasoning / Mids** | **+1.0 dB** | Active gyrator boost centering solo single notes. |
| **Seasoning / Treble** | **0.0 dB** | Flat treble baseline. |
| **Seasoning / Volume** | **+6.0 dB** | Preamp push into the output stage. |
| **Sizzle / Vib On** | **ON (1)** | True pitch-shifting analog vibrato circuit. |
| **Sizzle / Vib Speed** | **3.5 Hz** | Slow, relaxed, swaying nocturnal modulation. |
| **Sizzle / Vib Depth** | **2.5** | Subtle pitch movement adding organic dimensional life. |
| **Sizzle / Heat Source** | **0 (Standard)** | Standard power stage configuration. |
| **Sizzle / Master** | **8.0** | Power amplifier saturation sweet spot. |
| **10-Inch Cab Sim** | **OFF (0)** | Internal cab bypassed; speaker simulation handled downstream by IRDX Studio Free. |

---

### 8. IRDX Studio Free — Dynamic Impulse Response & Speaker Nonlinearity

*Role: Dynamic speaker cabinet emulation with OwnHammer Thiele impulse loading.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Loaded IR** | **OwnHammer 1x10 Thiele** | Ported 1x10 Thiele enclosure impulse providing tight, extended low-end response and vocal midrange clarity. |
| **Speaker Dynamics On** | **ON (1.0)** | Enables dynamic speaker distortion and impedance interaction. |
| **Speaker Dynamics Value** | **100.0%** | Full acoustic speaker cone breath under picking dynamics. |
| **Speaker Dynamics Mode** | **0.0** | Standard dynamic profile. |
| **AutoAlign** | **1.0 (ON)** | Phase-coherent impulse alignment. |
| **IR Slot 1** | **Enabled** | Primary cabinet impulse active. |
| **MultiMix X / Y** | **0.360 / 0.428** | Multi-cabinet acoustic blend coordinates. |
| **Output Trim** | **0.0 dB** | Unity level into spatial processor. |

---

### 9. Aesthetica — Room Reverb & Matrix Diffusion Laboratory

*Role: Late-chain acoustic diffusion and room wrapping.*

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Matrix** | **2 (Givens SO(8))** | Asymmetric SO(8) Givens rotation matrix for natural, non-repeating modal dispersion. |
| **Mix** | **20.0%** | Ambient club atmosphere without washing out front-end definition. |
| **Pre-Delay** | **10.0 ms** | Distinct transient clearance before diffusion tank onset. |
| **Decay** | **1.25 s** | Intimate room reflection time. |
| **Tone** | **5500.0 Hz** | Acoustic boundary absorption modeling soft room surfaces. |
| **Room Size** | **30.0%** | Intimate room geometry. |
| **Diffusion** | **40.0%** | Balances specular reflection detail with smooth diffuse tail. |
| **ER / Late Blend** | **55.0%** | Subtle late-field emphasis. |
| **Modulation** | **18.0%** | Tank detuning to eradicate static room resonances. |
| **Level** | **0.0 dB** | Unity output. |

---

## Starting Point Guide

- **Guitar Controls**: Select the **Neck Rebel 90 P-90 Pickup**. Keep guitar volume around **7–8** for a warm, touch-responsive clean tone with blooming sustain; rolling up to **10** pushes Omakase Bento's Drive (set at 7.0) into expressive, singing blues-jazz breakup. Keep tone around **7** to complement Liberty Burnisher's -2.5 dB Air shelf.
- **Dynamic Touch**: The optical Leveler on Omakase Bento (Sensitivity 3.0) together with the Germanium warmth of Liberty Burnisher produces an elastic, responsive spongy feel under the fingers. Digging in compresses transients and swells with harmonic sustain, while light fingerpicking rings clear and articulate.
- **Vibrato Pulse**: Sizzle Vibrato is dialed to a relaxed 3.5 Hz rate with moderate depth (2.5), creating a gentle shimmer that gives held chords and slow vibrato tail notes a vintage tape-like soul.
- **Dual Reverb Staging**: Mechanica is positioned pre-amp (Engine 0 at 15% mix) providing subtle metallic spring tank slap into the overdrive circuit, while Aesthetica is placed post-cab (Givens SO(8) matrix at 20% mix) to place the entire rig inside an intimate acoustic room.

---

## Feedback History

### 2026-10-19 — tested
- Created and auditioned in Virtual Pedalboard using native preset `A Night Settling In` (`6D6EE798-013A-4BC1-9062-B5A22159271B.vpreset`).
- Tested with the 2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90 neck pickup) monitoring through Sennheiser HD660S2 headphones.
- Signal chain features Omakase Bento (optical leveler, wood/cavity EQ, 3.5Hz vibrato) paired with Liberty Burnisher, Mechanica pre-reverb, Bogren IRDX Studio Free hosting the OwnHammer 1x10 Thiele IR with 100% speaker dynamics, and Aesthetica Givens SO(8) matrix diffusion.
