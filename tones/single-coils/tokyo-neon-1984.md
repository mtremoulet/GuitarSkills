---
id: tokyo-neon-1984
preset_name: "Tokyo Neon 1984"
created: 2026-09-06
updated: 2026-09-06
pickup_type: single-coil
guitar: "Mid-1980s Squier Stratocaster Partscaster (Fender Tex-Mex Single-Coils, Position 4)"
target: 'Glassy, percussive, snappy 1980s Japanese City Pop and Neo-Soul funk clean with dimensional studio chorus and console desk compression.'
tags: "city-pop, funk, j-pop, neo-soul, stratocaster, single-coil, cory-wong, tone-king, chorus, slapback"
amp: "Archetype Cory Wong X / Tone King Imperial (Hardware)"
tone-king-channel: rhythm
status: tested
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    cleanVolume: 0.28
    cleanBass: 0.48
    cleanMid: 0.38
    cleanTreble: 0.62
    cleanPresence: 0.52
    cleanOutputLevel: 0.50
  compressor:
    blend: 0.60
    compression: 0.45
    volume: 0.55
    tone: 0.50
  studio_d:
    enabled: true
    mode: 2
  galaxy:
    head_select: 1
    echo_rate: 7.5
    feedback: 1.0
    echo_volume: 2.0
    wet_solo: false
  hardware_settings:
    Channel: Rhythm
    Volume: 3.2
    Attenuation: 5.5
    Bass: 4.8
    Treble: 6.2
    IR: "OH 212 Class A Blue"
    Reverb:
      Level: 1.5
      Dwell: 2.0
    Tremolo: Off
    Guitar_Volume: 8.8
    Guitar_Tone: 7.8
---

# Tokyo Neon 1984

## Target Sound

Captures the sparkling, ultra-clean, percussive studio guitar tones that defined the golden era of 1980s Japanese City Pop and Tokyo studio recordings (Tatsuro Yamashita, Toshiki Kadomatsu, Tomoko Aran, Makoto Matsushita) and modern funk masters (Cory Wong).

This toneprint is built on the lightning-fast transient snap of Position 4 ("Funky Quack" — Neck + Middle parallel) on Mike’s Squier Stratocaster. On the Tone King Imperial Preamp, we pair the Rhythm channel with **Cab 2 (OH 212 Class A Blue)**. The 1963 Vox AC30 open-back 2x12 cab delivers shimmering upper-harmonic air and chime without the brittle ice-pick harshness of a direct line input. In software, this is mirrored in **Archetype Cory Wong X** using **The 4th Position Compressor** (parallel optical compression at 60% blend) into **The Clean Machine**.

---

## Signal Chains

### Option A: Physical Hardware Signal Path (Direct-in / Standalone)
```
[Squier Stratocaster (Pos 4)] ──► [Tone King Imperial Preamp (Hardware)] ──► [Audient iD14 Line In] ──► [Post-Amp DAW/Host FX]
```

| Hardware Control | Setting (1–9 Pips) | Technical Rationale |
|---|---|---|
| **Channel** | **Rhythm** | High-headroom Blackface clean; unyielding transient punch |
| **Volume** | **3.2** | Pristine clean headroom; immediate pick response on 16th-note chucks |
| **Attenuation** | **5.5** | Modern, punchy, forward studio projection |
| **Bass** | **4.8** | Keeps low strings tight and bouncy without sub-bass flub |
| **Treble** | **6.2** | Accentuates the Tex-Mex pickups' out-of-phase glass and air |
| **Cab IR Selector** | **Cab 2 — OH 212 Class A Blue** | **CRITICAL**: 1963 Vox AC30 2x12 with Celestion Blues; top-end chime |
| **Reverb** | **ON** (Level 1.5, Dwell 2.0) | Tight, splashy spring reflection that decays quickly, keeping rhythm uncluttered |
| **Tremolo** | **OFF** | Bypassed |
| **Guitar Controls** | **Position 4 \| Vol 8.8 \| Tone 7.8** | Vol 8.8 maximizes transient snap; Tone 7.8 preserves chime |

---

### Option B: Software Signal Path (Standalone Audio / Element)
```
[Guitar D.I.] ──► [Audient iD14 Input 1 (-3.2dB Pad)] ──► [Archetype Cory Wong X] ──► [Studio D Chorus] ──► [Galaxy Slapback]
```

| Software Plugin | Control | Setting | Purpose |
|---|---|---|---|
| **Archetype Cory Wong X** | Pre-FX: 4th Pos Comp | **Blend 60%, Comp 45%, Vol 55%** | Parallel optical squash; lifts sustain while preserving percussive pick attack |
| | Amp: The Clean Machine | **Volume 28%, Bass 48%, Mid 38%** | Classic Blackface mid-scoop with high headroom |
| | Amp: Treble / Presence | **Treble 62%, Presence 52%** | Crystalline top-end sparkle |
| | Amp: Output Level | **50%** | Normalized output level staging |
| | Cab: Clean 1x12 | **Dynamic 57 + Ribbon 121** | Balanced close-mic'd punch |
| **UADx Studio D Chorus** | Mode | **Button 2** (or 1+4) | **CRITICAL**: Authentic Roland Dimension D stereo widening without pitch vibrato |
| **UADx Galaxy Tape Echo** | Head Select / Rate | **Head 1 / Rate 7.5** | Short 100 ms slapback shadow behind dry attack |
| | Feedback / Volume | **Feedback 1.0 / Echo Vol 2.0** | Single discrete repeat; sits tucked in the groove |
| **UADx Verve Analog Machines** | Model / Drive | **Solid-State Sweeten / Drive 2.5** | High-end console transformer punch and harmonic excitation |

---

## Universal 6-Guitar Calibration Guide

Switching between guitars while dialing in the crisp "Tokyo Neon 1984" funk sheen:

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Squier Stratocaster** *(Anchor)* | Position 4 (Neck+Mid), Vol 9, Tone 8 | Baseline: Vol 3.2, Treb 6.2, Bass 4.8 | Baseline: Cory Wong X (Blend 60%) | The classic out-of-phase "quack"; crisp, percussive, snappy 16th-note chucks. |
| **Fender Player II Telecaster** | Position 2 (Neck+Bridge), Vol 8.5, Tone 7.5 | **Treble -0.5 (5.7), Bass +0.5 (5.3)** | **Clean Machine: Treble 55%, Presence 50%** | Parallel neck+bridge on Tele gives a slightly wider, fatter funk snap. Pull Treble back to 5.7 to tame bridge pickup edge. |
| **Epiphone Les Paul (Rebel 90s)** | Middle (Both P-90s RWRP), Vol 8, Tone 7 | **Bass -0.5 (4.3), Treble +0.5 (6.7)** | **Comp Blend 50%, High-Pass 80 Hz** | RWRP middle position is hum-canceling with distinct hollow quack. Boosting Treble to 6.7 restores single-coil sparkle on mahogany body. |
| **Framus Earl Slick (DiMarzio P-90s)** | Middle Position, Vol 8.5, Tone 7.0 | **Bass 4.8, Treble 6.0** | **Clean Machine: Treble 58%, Mid 40%** | Swamp ash body provides immediate, percussive snap that rivals a Stratocaster. Keep settings close to baseline. |
| **Gibson Les Paul Studio** | Middle (Both Humbuckers), Vol 7.5, Tone 8 | **Bass -1.0 (3.8), Treble +0.8 (7.0)** | **Bright Switch ON, Bass 35%** | To funk on humbuckers, scoop low end heavily (Bass 3.8) and boost Treble to 7.0. Roll guitar volume to 7.5 to clean input stage. |
| **Epiphone Sheraton II** | Middle (Both Humbuckers), Vol 8, Tone 8.5 | **Bass -1.2 (3.6), Treble +0.8 (7.0)** | **Bright Switch ON, High-Pass 100 Hz** | Flatwounds naturally mute top string snap. Engage Bright switch in software or push Treble to 7.0; yields an ultra-smooth, polished 70s soul rhythm. |

---

## Musical Rationale & Multi-Instrument Bridge

- **The Violin Bowing (*Spiccato* / *Martelé*) Bridge**: On violin, rapid 16th notes require the bow to rebound dynamically off the string (*spiccato*). In funk rhythm guitar, the fretting hand performs the damping: triads are gripped and instantly released to shape percussive envelopes.
- **Arrangement Voice-Leading**: In City Pop arrangements, rhythm guitar sits between the bassline and the horn/synth stabs. By using 3-note triads on the G, B, and E strings (e.g., G9: `x-x-7-7-6-5` or Dm7: `x-x-10-10-10-10`), the guitar cuts through the pocket without cluttering the mid-frequency vocal canvas.

---

## Optional Footnote: All-Digital Workflow & Three-Way Cross-Amp Comparison

For an all-digital workflow or when A/B/C testing across hardware and software platforms, load the generated native presets below:

### 1. UADx Paradise Guitar Studio Preset (`Toneprint - Tokyo Neon 1984.json`)
- **Location**: `uaudio_paradise_guitar_studio/Dream '65/` and `tones/presets/paradise/`
- **Amp Engine**: **Dream '65** (Model 0)
- **Amp Controls**: Volume **3.2**, Treble **6.5**, Bass **4.8**, Bright **ON**, Mod **Stock**, Reverb **1.5** (ON), Boost **OFF**, Output **12.0**
- **Cabinet / Mic**: **2x12 Silver 120 / EV12** (`cab_and_mic`: 29)
- **Pre-FX**: Slot 1: **1176 Compressor** (Active — fast attack, medium release, 4:1 parallel squash)
- **Post-FX**: Slot 1: **Brigade Chorus** (Active), Slot 2: **Digital Delay** (Active — Slapback 105 ms, 18% mix)

### 2. Neural DSP Archetype Cory Wong X Preset (`Tokyo Neon 1984.xml`)
- **Location**: `/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints/` and `tones/presets/neural/`
- **Amp Engine**: **The Clean Machine** (Amp 1)
- **Amp Controls**: `volume`: **28%**, `BASS`: **48%**, `MIDDLE`: **38%**, `TREBLE`: **62%**, `PRESENCE`: **52%**, `BRIGHT`: **ON**, `OUTPUT`: **50%**
- **Pre-FX**: **The 4th Position Compressor** (Active — Blend 60%, Compression 45%, Tone 50%, Volume 55%)
- **Cabinet**: Cab 2 (Clean 1x12), Mic: Dynamic 57 + Ribbon 121 (Room Mic -24 dB)
- **Post-FX**: **The 80s Chorus** (Active — Mix 40%, Rate 25%, Width 35%) + **Delay-Y-Y** (Active — Mix 20%, Feedback 10%, Slapback 105 ms)

### 3. Three-Way Cross-Amp Comparison Matrix

| Dimension | Tone King Imperial Preamp (Physical Tube) | UADx Paradise Guitar Studio (Dream '65) | Archetype Cory Wong X (Clean Machine) |
|---|---|---|---|
| **Core Circuit & Architecture** | 3x 12AX7 all-tube preamp into Cab 2 (OH 212 Class A Blue — 1963 AC30 Celestion Blues) | Emulated AB763 Blackface with Bright switch engaged into 2x12 Silver 120 | Pristine solid-state/tube hybrid clean machine designed specifically for modern funk rhythm |
| **High-End Chime & Glass** | Analog chime from the Class A Blue 2x12 IR; crisp, metallic, uncompressed top end without digital harshness | Bell-like Blackface top end with bright cap engaged; slightly softer transients than hardware | Maximum sparkle, hyper-defined 16th-note chucks; surgical transient snap engineered for Nile Rodgers & Cory Wong styles |
| **Compression & Dynamics** | Natural tube sag and Ironman II reactive attenuation cushion the hardest pick slashes | 1176 FET compressor in Pre-FX provides classic analog peak limiting with fast transient grab | The 4th Position Compressor (parallel optical) retains 100% of the pick transient while lifting chord tails |
| **Stereo Image & Space** | Mono tube direct into host stereo Dimension D chorus; warm, 3D analog presence | Modeled Brigade Chorus adds authentic 1970s analog bucket-brigade spatial swirl | The 80s Chorus provides ultra-wide, ultra-clean modern stereo chorus imaging without pitch wobble |

