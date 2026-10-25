---
id: nordic-cathedral
preset_name: "Nordic Cathedral"
created: 2026-09-06
updated: 2026-09-06
pickup_type: single-coil
guitar: "2024 Fender Player II Telecaster (Single-Coils, Neck or Middle Position)"
target: 'Ethereal, three-dimensional spatial soundscape with slow undulating modulation blooming into infinite ambient cathedral reverb.'
tags: "ambient, neo-classical, chillhop, telecaster, single-coil, dream-65, tone-king, valhalla, delay, modulation"
amp: "Dream '65 (UADx) / Tone King Imperial (Hardware)"
tone-king-channel: rhythm
status: tested
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    dream_volume: 2.5
    dream_treble: 3.5
    dream_bass: 6.0
    dream_bright: false
    dream_reverb: 3.5
    dream_reverb_enable: true
    dream_vibrato_enable: true
    dream_speed: 2.5
    dream_intensity: 3.5
    dream_amp_mod: 0
    cab_and_mic: 29
  valhalla:
    mode: "Lyra"
    mix: 0.38
    delay: 0.35
    feedback: 0.70
    warp: 0.35
  galaxy:
    head_select: 3
    echo_rate: 4.5
    feedback: 3.5
    echo_volume: 3.0
    tape_age: 2
    wet_solo: false
  hardware_settings:
    Channel: Rhythm
    Volume: 2.5
    Attenuation: 5.0
    Bass: 6.8
    Treble: 2.8
    IR: "OH 112 Imperial TK1660"
    Reverb:
      Level: 3.5
      Dwell: 4.5
    Tremolo:
      Speed: 2.2
      Depth: 3.5
    Guitar_Volume: 7.0
    Guitar_Tone: 5.0
---

# Nordic Cathedral

## Target Sound

Designed for expansive, cinematic, and meditative musical landscapes (Bill Frisell, Jakob Bro, Julian Lage, Brian Eno, modern Lo-Fi chillhop).

This toneprint transforms the Fender Player II Telecaster into an ethereal, orchestral sound generator. On the physical Tone King Imperial Preamp pedal, we dial the **Rhythm channel with Bass elevated to 6.8** to give the neck single-coil the round, resonant low-end fundamental of a concert grand piano or cello, while **Treble is pulled back to 2.8** to eliminate pick click. Engaging both the onboard spring convolution reverb (Level 3.5, Dwell 4.5) and the digital bias-style tremolo at a slow, oceanic rate (Speed 2.2, Depth 3.5) establishes a hypnotic, breathing pulse that feeds downstream into long tape echoes and the infinite, stone-cathedral spatial wash of ValhallaSuperMassive.

---

## Signal Chains

### Option A: Physical Hardware Signal Path (Direct-in / Standalone)
```
[Player II Telecaster] ──► [Tone King Imperial Preamp (Hardware)] ──► [Audient iD14 Line In] ──► [Post-Amp DAW/Host FX]
```

| Hardware Control | Setting (1–9 Pips) | Technical Rationale |
|---|---|---|
| **Channel** | **Rhythm** | Pristine 1960s Blackface clean platform; maximum linear headroom |
| **Volume** | **2.5** | Ultra-clean input; prevents intermodulation distortion on complex cluster voicings |
| **Attenuation** | **5.0** | Calibrated unity output into interface and studio monitors |
| **Bass** | **6.8** | **CRITICAL**: Fills out low-string body, giving single-coils the weight of an archtop |
| **Treble** | **2.8** | Softens single-coil transient spank for a bow-like note attack |
| **Cab IR Selector** | **Cab 1 — OH 112 Imperial TK1660** | Intimate 1x12 open-back pine combo dispersion |
| **Reverb** | **ON** (Level 3.5, Dwell 4.5) | Generous spring convolution wash that floats behind the notes |
| **Tremolo** | **ON** (Speed 2.2, Depth 3.5) | Slow, deep, lapping-wave amplitude modulation; rhythmic breathing cycle |
| **Guitar Controls** | **Neck (or Middle) \| Vol 7.0 \| Tone 5.0** | Rolling Tone to 5.0 creates a pad-like, bowed-string envelope |

---

### Option B: Software Signal Path (Standalone Audio / Element)
```
[Guitar D.I.] ──► [Audient iD14 Input 1 (-3.2dB Pad)] ──► [UADx Dream '65] ──► [Galaxy Tape Echo] ──► [ValhallaSuperMassive]
```

| Software Plugin | Control | Setting | Purpose |
|---|---|---|---|
| **UADx Dream '65** | Volume | **2.5** | Unyielding clean headroom |
| | Treble / Bass | **Treble 3.5, Bass 6.0** | Round, piano-like fundamental balance |
| | Bright Switch | **OFF (Normal)** | Prevents high-frequency clatter in downstream reverb |
| | Reverb | **3.5** | Modeled spring tank reflection |
| | Vibrato (Tremolo) | **Speed 2.5, Depth 3.5** | Bias-style throbbing modulation |
| | Cabinet | **1x12 Oxford (or EV12)** | Articulate, warm 1x12 dispersion |
| **UADx Galaxy Tape Echo** | Head Select / Rate | **Head 3 / Rate 4.5** | Long analog tape echo (~320 ms) |
| | Feedback / Volume | **Feedback 3.5 / Echo Vol 3.0** | Warm repeats that gently dissolve into tape compression |
| | Tape Age | **Old** | Introduces gentle analog wow & flutter |
| **ValhallaSuperMassive** | Mode | **Lyra (or Capricorn)** | Dense, blooming, non-metallic ambient clouds |
| | Mix / Delay / Feedback | **Mix 38%, Delay 350 ms, Fdbk 70%** | Massive reverberant wash with slow, infinite decay |
| | Warp | **35%** | Subtle pitch detune and choral shimmer in reverb tail |
| **TDR Nova EQ** | High-Pass / Low-Pass | **HPF 85 Hz (24 dB/oct) / LPF 5.5 kHz** | Prevents subsonic buildup and maintains vintage cinematic aesthetic |

---

## Universal 6-Guitar Calibration Guide

Switching between guitars while dialing in the ethereal "Nordic Cathedral" soundscape:

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Fender Player II Telecaster** *(Anchor)* | Neck (or Middle), Vol 7, Tone 5 | Baseline: Vol 2.5, Bass 6.8, Treb 2.8 | Baseline: Dream '65 Vol 2.5, Bass 6.0 | Ethereal cathedral soundscape; piano-like low-end foundation with breathing tremolo pulse. |
| **Epiphone Sheraton II** | Neck Humbucker, Vol 6.5, Tone 6.0 | **Bass -1.5 (5.3), Treble +0.5 (3.3)** | **Dream '65 Bass 4.8, Treble 4.0** | Flatwounds and semi-hollow construction have massive natural low frequencies. Pull Bass to 5.3 to prevent ambient reverb from blooming into mud. |
| **Gibson Les Paul Studio** | Neck 490R (or Middle), Vol 7, Tone 5.5 | **Bass -1.0 (5.8), Treble +0.5 (3.3)** | **Dream '65 Bass 5.0, Treble 4.0** | Humbuckers produce dense harmonic weight. Treble at 3.3 adds delicate chime to open-voiced chord voicings. |
| **Epiphone Les Paul (Rebel 90s)** | Neck P-90, Vol 6.5, Tone 4.5 | **Bass -1.2 (5.6), Treble 2.8** | **Dream '65 Bass 4.8, Treble 3.5** | Tonerider Rebel 90s provide rich cello-like fundamental. Rolling guitar volume to 6.5 keeps the Blackface preamp pristine and unclipped. |
| **Framus Earl Slick (DiMarzio P-90s)** | Middle Position, Vol 7.0, Tone 5.0 | **Bass -0.8 (6.0), Treble 2.8** | **Dream '65 Bass 5.2, Treble 3.5** | Bigsby vibrato allows slow, subtle chord shimmering before hitting ValhallaSuperMassive, creating lush pedal steel-like pads. |
| **Squier Stratocaster (Tex-Mex)** | Position 4 (Neck+Mid), Vol 7.5, Tone 5.5 | **Bass 6.5, Treble 3.0** | **Dream '65 Bass 5.8, Treble 3.8** | Out-of-phase Position 4 adds hollow, bell-like clarity that dissolves into the delay repeats with stone-cathedral depth. |

---

## Musical Rationale & Multi-Instrument Bridge

- **The A Cappella Choral Arranging Bridge**: In 8-part vocal arranging, suspended chords (sus2, sus4, add9, maj7#11) require expansive acoustic space to evolve and resolve without frequency clashes. The slow tremolo acts like a choral breathing cycle, providing rhythmic pulse while notes sustain infinitely in the reverb.
- **Fretboard Voice Leading**: When Mike plays open-string chord voicings on the Telecaster (e.g., Emaj9: `0-7-6-8-0-0` or Dadd9/F#: `2-x-0-2-3-0`), the notes bloom like a pipe organ or chamber choir. The extended decay lets the ear follow individual inner voice movements smoothly across chord transitions.

---

## Optional Footnote: All-Digital Workflow & Three-Way Cross-Amp Comparison

For an all-digital workflow or when A/B/C testing across hardware and software platforms, load the generated native presets below:

### 1. UADx Paradise Guitar Studio Preset (`Toneprint - Nordic Cathedral.json`)
- **Location**: `uaudio_paradise_guitar_studio/Dream '65/` and `tones/presets/paradise/`
- **Amp Engine**: **Dream '65** (Model 0)
- **Amp Controls**: Volume **2.5**, Treble **3.5**, Bass **6.0**, Bright **OFF**, Reverb **3.5** (ON), Vibrato Speed **2.5**, Depth **3.5** (ON), Mod **Stock**, Output **12.0**
- **Cabinet / Mic**: **1x12 EV12 / Oxford** (`cab_and_mic`: 29)
- **Pre-FX**: None (preserves pristine dynamic headroom for extended chord clusters)
- **Post-FX**: Slot 1: **EP-III Tape Delay** (Active — 350 ms, 30% mix), Slot 2: **Reverb 224** (Active — Concert Hall mode, 40% mix)

### 2. Neural DSP Archetype Cory Wong X Preset (`Nordic Cathedral.xml`)
- **Location**: `/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints/` and `tones/presets/neural/`
- **Amp Engine**: **The Clean Machine** (Amp 1)
- **Amp Controls**: `volume`: **25%**, `BASS`: **68%** (piano-like bottom fundamental), `MIDDLE`: **45%**, `TREBLE`: **32%** (eliminates pick click), `PRESENCE`: **25%**, `BRIGHT`: **OFF**, `OUTPUT`: **55%**
- **Pre-FX**: **The 4th Position Compressor** (Active — Blend 50%, Compression 35%, Tone 45%, Volume 55% for long ambient swelling)
- **Cabinet**: Cab 1 (Clean 1x12), Mic: Ribbon 121 + Condenser 414 (Room Mic -18 dB)
- **Post-FX**: **Delay-Y-Y** (Active — Mix 30%, Feedback 45%, 350 ms) + **The Wash** (Active — Shimmer ON, Mix 45%, Decay 70%, Low Cut 120 Hz, High Cut 5 kHz)

### 3. Three-Way Cross-Amp Comparison Matrix

| Dimension | Tone King Imperial Preamp (Physical Tube) | UADx Paradise Guitar Studio (Dream '65) | Archetype Cory Wong X (Clean Machine) |
|---|---|---|---|
| **Core Circuit & Architecture** | 3x 12AX7 all-tube preamp + Ironman II reactive attenuator + onboard spring convolution & bias tremolo | Emulated AB763 Blackface with modeled bias vibrato + 224 digital hall reverb | High-headroom modern clean platform with dual delay and "The Wash" shimmer engine |
| **Low-End Foundation** | Physical Bass dialed up to 6.8 gives the Telecaster neck pickup the deep, resonant weight of a cello or upright piano | Rich, warm modeled Blackface low end (Bass 6.0) that supports wide-interval open chords without flub | Incredibly clean, extended sub-bass fundamental (Bass 68%); perfectly flat, hi-fi foundation for synth-like guitar pads |
| **Transient Response** | Soft physical tube attack; pick transient dissolves immediately into the warm spring reverb tank | Component-modeled tube sag cushions pick strikes; smooth, natural bloom into downstream delay | The 4th Position Compressor gently compresses transients and creates continuous, singing sustain |
| **Ambient Space & Shimmer** | Analog direct out feeds downstream ValhallaSuperMassive for stone-cathedral stone-reverberant realism | Dream '65 vibrato + Reverb 224 Concert Hall yields warm, authentic 1980s cinematic ambience | "The Wash" shimmer algorithm injects ethereal, pitch-shifted octave halos, turning the guitar into an ambient synthesizer |

