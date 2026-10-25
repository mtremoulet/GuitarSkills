---
id: "fausts-jazz-hotel"
preset_name: "Faust's Jazz Hotel"
created: "2026-09-21"
updated: "2026-09-21"
guitar: "2013 Epiphone Sheraton II (Neck Humbucker, Thomastik-Infeld Flatwounds)"
target: "Velvety, high-headroom solid-state jazz clean and singing fusion lead with dual-stage BJT/JFET pre-buffering, active 251Hz low-mid parametric warmth, and lush club reverberation."
tags: "jazz, fusion, lead, humbucker, semi-hollow, sheraton, pearce-g2r, holdsworth, liberty-burnisher, stasimon, aetheria, velvet"
tone-king-channel: bypassed
amp: "Pearce G2r (Faust & Wagner)"
status: tested
pickup_type: humbucker
standalone_preset_id: "CC4F8345-F96F-499E-896F-C393BE0E97A6"
preset_data:
  liberty_burnisher:
    drive: 0.15
    burnish: 82.0
    air: -2.5
    ge_warmth: 40.0
    master_volume: 0.0
    charge_pump_18v: false
  stasimon:
    level: 3.0
    mode: "Preamp Only (Normal)"
    sensitivity: "High (2SC900 Boost)"
    input_buffer: "Vintage Low-Z (50k)"
    stereo_spread: "Classic Dual Mix"
    volume: 0.0
  pearce_g2r:
    channel_mode: "Channel 1 (Clean)"
    ch1_bright: true
    ch1_volume: 7.0
    ch1_bass: 6.0
    ch1_freq: 251.0
    ch1_mid: 6.5
    ch1_treble: 4.2
    ch2_bright: false
    ch2_drive: 5.5
    ch2_volume: 3.6
    ch2_bass: 6.5
    ch2_freq: 1200.0
    ch2_mid: 4.0
    ch2_treble: 5.7
    limiter_on: false
    limiter_threshold: 6.0
    presence: 5.0
    reverb: 1.5
    master: 0.0
    cab_sim: true
  aetheria:
    engine: "Room & Hall (8x8 FDN)"
    rt60_decay: 2.0
    absorption: 4500.0
    diffusion: 25.0
    archetype: 1.00
    pre_delay: 12.0
    level: 0.0
    mix: 35.0
---

# Faust's Jazz Hotel

## Target Sound

A sophisticated, velvety jazz clean and fluid fusion lead tone tailored specifically for the **2013 Epiphone Sheraton II** strung with **Thomastik-Infeld Jazz Swing Flatwound 10s** (as cataloged in `tone-advisor/guitar_stable.md`).

I know that the Pearce G2r (engineered by Dan Pearce in the late 1980s) achieved cult status among jazz and fusion masters—most prominently Allan Holdsworth—for its extraordinary solid-state clean headroom, active Baxandall tone stacks, fully parametric midrange equalization, and vocal cascaded FET overdrive. 

In **Faust's Jazz Hotel**, the front-end signal path establishes an unprecedented dual-stage pre-buffering foundation:
1. **Liberty Burnisher**: Deployed first in the chain with heavy **Burnish at 82%** (dynamic Miller capacitance slew softening) and passive **Air rolled back to −2.5 dB**. This gently rounds off the initial pick transient spike while injecting subtle 1N34A Germanium 2nd-harmonic warmth (40%).
2. **Stasimon (CE-1 Digital Twin)**: Operating in *Preamp Only* mode with *Vintage Low-Z (50kΩ)* input loading. The 50kΩ impedance loads down the neck humbucker coils, while the discrete Class-A 2SC900 booster stage adds low-end girth and analog punch.
3. **Pearce G2r Core Amplifier**:
   - **Channel 1 (Clean — Primary Performance Mode)**: With Ch1 Bright engaged, Bass lifted to +2.3 dB @ 80 Hz, and Treble smoothed to −1.9 dB @ 3.5 kHz, the tone is centered around an active **+4.4 dB parametric midrange boost at 251 Hz**. This directly bolsters the lower-mid fundamental of the Sheraton's semi-hollow body and flatwound strings, creating an acoustic, woody authority reminiscent of an archtop in a luxurious hotel lounge.
   - **Channel 2 (Lead — Dialed-In Soloing Mode)**: Pre-dialed for seamless switching during performance. Delivers creamy, singing cascaded FET/diode drive with a 1.2 kHz mid contour notch and smooth top end for fluid legato lines.
4. **Aetheria (8x8 Householder FDN)**: Encapsulates the rig in an intimate, plush acoustic room with 4500 Hz high-frequency absorption at a 35% wet blend.

---

## Signal Chain

```
[Epiphone Sheraton II (Neck Humbucker, Flatwounds)]
  ──► [Audient iD14 Input 1 (D.I. 0 dB)]
  ──► [1. Liberty Burnisher] (Discrete JFET/BJT Transient Polisher: Burnish 82%, Air -2.5dB)
  ──► [2. Stasimon]          (Discrete BJT Preamp Line Driver & 50kΩ Low-Z Loading)
  ──► [3. Pearce G2r]        (Dual-Channel Solid-State Pro Amp Twin & 2x12 Cab Damping)
  ──► [4. Aetheria]          (Spatial: 8x8 Householder FDN Cozy Room Reverb)
  ──► [Standalone Audio Master Out]
```

### 1. Hardware Front-End & Input Calibration

* **Tone King Imperial Preamp**: **Bypassed** (per the direct input standard in `tone-advisor/TONEPRINT_GUIDELINES.md`). Signal path connects directly into Audient iD14 Instrument Input 1.
* **Hardware Interface Gain**: **0 dB** (unity).
* **Host**: **Standalone Audio (Oort Media)** serial rack preset `Faust's Jazz Hotel` (`CC4F8345-F96F-499E-896F-C393BE0E97A6.json`, PC #67).
* **Calibrated Trims**: Both Stasimon and Pearce G2r In/Out trims remain at calibrated unity (0.0 dB).

---

### 2. Liberty Burnisher — Discrete JFET/BJT Pre-Conditioner & Transient Softener

*Role: Upstream pick-transient conditioner and harmonic polisher.*

| Control | Setting | Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Drive** | **1.5** | `0.15` | Subtle Class-A JFET gain boost; warms the front end without introducing overdrive. |
| **Burnish** | **82.0%** | `82.0` | Heavy dynamic Miller feedback; softens aggressive pick attacks into smooth acoustic blooms. |
| **Air** | **−2.5 dB** | `-2.5` | Passive high-frequency presence cut; eliminates brittle ultrasonic clatter. |
| **Ge Warmth** | **40.0%** | `40.0` | 1N34A Germanium soft-knee asymmetric branch; adds even-order harmonic sweetness. |
| **Master Volume** | **0.0 dB** | `0.0` | Unity output trim. |
| **18V Charge Pump** | **OFF (9V)** | `0` | Operates on standard 9V rail for earlier soft saturation under dynamic spikes. |

---

### 3. Stasimon (CE-1 Digital Twin) — Discrete BJT Preamp Line Driver

*Role: Discrete Class-A line driver & 1976 Boss CE-1 passive pickup coil loading.*

| Control | Setting | Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Level** | **3.0** | `0.30` | Sweeps 50kΩ log pot into subtle Class-A BJT saturation without dirt. |
| **Mode** | **Preamp Only (Normal)** | `0` | BBD delay engine muted; 100% discrete analog line driver path active. |
| **Sensitivity** | **High (2SC900 Boost)** | `1` | Engages discrete 2SC900/2SC945 BJT booster for punchy low-end girth. |
| **Input Buffer** | **Vintage Low-Z (50k)** | `0` | Authentic 1976 passive pickup loading; rounds off high-frequency pick snap. |
| **Stereo Spread** | **Classic Dual Mix** | `0` | Dual mono line driver output. |
| **Volume** | **+0.0 dB** | `0.0` | Unity level trim. |

---

### 4. Pearce G2r — Professional Solid-State Amplifier Digital Twin (Dual-Channel)

*Role: Core amplifier, dual-channel active tone shaping, and 2x12 open-back cab.*

#### Channel 1 (Clean — Primary Performance Mode)
*Active by default (`Channel Select: Channel 1`). Delivers pristine, articulate jazz clean.*

| Control | Setting | Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Ch1 Bright** | **ON** | `1` | High-frequency shelf (+9 dB @ 2 kHz) adds air to flatwound strings. |
| **Ch1 Volume** | **7.0** | `0.70` | Pre-EQ input gain; drives active tone stack with healthy dynamic punch. |
| **Ch1 Bass** | **6.0** | `0.595` | Active Baxandall shelf (+2.3 dB @ 80 Hz) provides rich low-end foundation. |
| **Ch1 Mid Freq** | **251 Hz** | `251.0` | Parametric frequency sweep targeted directly at woody lower-mid body. |
| **Ch1 Mid Gain** | **6.5** | `0.648` | **+4.4 dB parametric boost**; pushes flatwound melody lines forward with authority. |
| **Ch1 Treble** | **4.2** | `0.421` | Active Baxandall shelf (−1.9 dB @ 3.5 kHz); smooths upper register. |

#### Channel 2 (Lead — Dialed-In Soloing Mode)
*Pre-dialed for instant recall. Switch `Channel Select` to `Channel 2 (Lead)` for singing fusion overdrive.*

| Control | Setting | Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Ch2 Bright** | **OFF** | `0` | Disengages bright cap to keep cascaded overdrive creamy and non-fatiguing. |
| **Ch2 Drive** | **5.5** | `0.547` | Cascaded FET/diode overdrive sweet spot; violin-like sustain. |
| **Ch2 Volume** | **3.6** | `0.356` | Post-drive level matching Channel 1 output. |
| **Ch2 Bass** | **6.5** | `0.651` | Active Baxandall shelf (+3.6 dB @ 80 Hz) keeps single-note leads thick. |
| **Ch2 Mid Freq** | **1200 Hz** | `1200.0`| Parametric frequency sweep focused on upper-mid clarity. |
| **Ch2 Mid Gain** | **4.0** | `0.396` | Gentle −3.1 dB mid notch; carves out honk for liquid Holdsworth lead voice. |
| **Ch2 Treble** | **5.7** | `0.572` | Active Baxandall shelf (+1.7 dB @ 3.5 kHz); provides smooth overtone bite. |
| **Limiter On** | **OFF** | `0` | OTA ceiling limiter dormant (engage if compressing legato runs). |
| **Limiter Thresh** | **6.0** | `0.600` | Standby ceiling sensitivity. |

#### Master & Cabinet Section (Shared)

| Control | Setting | Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Channel Select** | **Channel 1 (Clean)** | `0` | Performance routing (switch to `1` for Lead, or `2` for Parallel Blend). |
| **Presence** | **5.0** | `0.50` | Flat baseline contour at 5.5 kHz. |
| **Reverb** | **1.5** | `0.15` | 15% internal digital plate/room ambience. |
| **Master** | **+0.0 dB** | `0.0` | 100W/ch stereo power amp level trim. |
| **Cab Sim** | **ON** | `1` | 2x12 open-back cabinet with current-feedback speaker damping. |

---

### 5. Aetheria — Classical & Ambient Reverb Laboratory

*Role: Cozy hotel lounge and jazz club spatial acoustics.*

| Control | Setting | Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Engine** | **Room & Hall (8x8 FDN)** | `2` | Lossless 8x8 Householder unitary matrix for dense, uncolored room reflections. |
| **Mix** | **35.0%** | `35.0` | 35% wet blend places the guitar inside a luxurious physical hall. |
| **Pre-Delay** | **12.0 ms** | `12.0` | 12 ms offset separates direct string attack from room bloom. |
| **RT60 (Decay)** | **2.0 s** | `2.0` | Intimate room decay time; cushions chords without cluttering fast runs. |
| **Tone (Absorption)**| **4500.0 Hz** | `4500.0`| High-frequency damping simulating plush carpet, curtains, and low ceilings. |
| **Diffusion** | **25.0%** | `25.0` | Preserves transient separation during complex four-note chord comping. |
| **Character** | **1.00** | `1.0` | Standard chamber geometry. |
| **Level** | **+0.0 dB** | `0.0` | Master output level. |

---

## Starting Point Guide

- **Guitar Controls**: Select the **Neck Humbucker**. Set guitar volume to **7.5–8.5** and guitar tone to **7**. The flatwound strings combined with the dual front-end softening (Liberty Burnisher at 82% Burnish and Stasimon at 50kΩ) eliminate string squeak and pick ping while retaining acoustic wood bloom.
- **Channel Switching During Performance**:
  - For chord melody, comping, and velvety walking basslines, keep the Pearce G2r on **Channel 1 (Clean)**.
  - When taking an expressive single-note solo or blues/fusion chorus, flip the Pearce G2r **Channel Select** switch from `Channel 1 (0)` to `Channel 2 (1)`. Notice how Channel 2's drive (5.5) and 1.2 kHz mid notch produce a liquid, vocal lead that sustains effortlessly without needing an external boost pedal.
  - *Optional Parallel Fusion Blend*: Switching to `Both (2)` blends Channel 1 and Channel 2 in parallel, layering a clean acoustic attack over the singing saturated core.
- **Musical Bridge**: Think of Channel 1 like the dark, round fundamental of an alto saxophone in a quiet register, and Channel 2 like leaning into the reed with full breath support. On violin, Channel 1 mirrors wide, relaxed bow strokes near the fingerboard (*sul tasto*), while Channel 2 mirrors the concentrated harmonic bite of drawing the bow closer to the bridge (*sul ponticello*).

---

## Feedback History

### 2026-09-21 — tested
- Toneprint created and verified in Standalone Audio using the native preset `Faust's Jazz Hotel` (`CC4F8345-F96F-499E-896F-C393BE0E97A6.json`, PC #67).
- Built around the 2013 Epiphone Sheraton II (Thomastik-Infeld Jazz Swing Flatwounds 10s) monitoring through Sennheiser HD660S2 headphones.
- Confirmed Pearce G2r as the dedicated amplifier core (Polytone holdover bypassed and retired).
- Captured and verified both Channel 1 (Clean @ 251 Hz mid boost) and Channel 2 (Lead @ 1.2 kHz mid notch) settings for dynamic in-performance channel switching.
