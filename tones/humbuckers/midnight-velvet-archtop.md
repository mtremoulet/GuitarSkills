---
id: midnight-velvet-archtop
preset_name: "Midnight Velvet Archtop"
created: 2026-09-06
updated: 2026-09-06
pickup_type: humbucker
guitar: "2013 Epiphone Sheraton II (Thomastik-Infeld Jazz Flats 10s, Neck Humbucker)"
target: 'Dark, pillowy, woody jazz and bossa nova clean with zero transient click, flattened mid-scoop, and acoustic archtop bloom.'
tags: "jazz, bossa, dark, warm, velvet, sheraton, humbucker, dream-65, tone-king, flatwounds"
amp: "Dream '65 (UADx) / Tone King Imperial (Hardware)"
tone-king-channel: rhythm
status: tested
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 2.5
    Treble: 3.5
    Bass: 4.8
    Bright: false
    Reverb: 2.5
    Mod: Stock
    Cabinet: "1x12 EV12"
    Output: 12.0
  studio_d:
    enabled: true
    mode: 1
  hardware_settings:
    Channel: Rhythm
    Volume: 2.8
    Attenuation: 4.5
    Bass: 5.5
    Treble: 2.5
    IR: "OH 112 Imperial TK1660"
    Reverb:
      Level: 2.5
      Dwell: 3.5
    Tremolo: Off
    Guitar_Volume: 7.0
    Guitar_Tone: 5.5
---

# Midnight Velvet Archtop

## Target Sound

Inspired directly by the high-headroom woody thump of `lion-68-royal-velvet-jazz-p90.md` and classic jazz box legends (Ed Bickert, Jim Hall, Paul Desmond cool jazz), this toneprint turns the 1960s Fender Blackface circuit into a warm, dark, intimate jazz archtop voice.

In stock Blackface amplifiers (and UADx Dream '65), a fixed resistor creates an inherent midrange scoop at ~500 Hz. On the physical Tone King Imperial Preamp pedal, we defeat this scoop and flatten the frequency curve by rolling **Treble down to 2.5** and setting **Bass to 5.5** on the 1–9 pip scale. Coupled with the Thomastik-Infeld flatwound strings on the Epiphone Sheraton II, all modern high-frequency pick click and transient bite are eliminated, leaving a pillowy, acoustic cushion that lets close-interval chords and drop-2 voicings ring with warmth and voice separation.

---

## Signal Chains

### Option A: Physical Hardware Signal Path (Direct-in / Standalone)
```
[Epiphone Sheraton II] ──► [Tone King Imperial Preamp (Hardware)] ──► [Audient iD14 Line In] ──► [Post-Amp DAW/Host FX]
```

| Hardware Control | Setting (1–9 Pips) | Technical Rationale |
|---|---|---|
| **Channel** | **Rhythm** | Pure 1960s Blackface AB763 high-headroom clean platform |
| **Volume** | **2.8** | Keeps 12AX7 triodes in linear, unclipped operation; fast transient recovery |
| **Attenuation** | **4.5** | Intimate room-level monitoring output; sets output gain structure |
| **Bass** | **5.5** | Balanced low-end fundamental; prevents semi-hollow body resonant boom |
| **Treble** | **2.5** | **CRITICAL**: Rolled back to flatten the 500 Hz mid-notch; delivers dark, woody jazz body |
| **Cab IR Selector** | **Cab 1 — OH 112 Imperial TK1660** | Open-back 1x12; warm, intimate, 3D acoustic dispersion |
| **Reverb** | **ON** (Level 2.5, Dwell 3.5) | Tube spring convolution tail breathes naturally with the semi-hollow body |
| **Tremolo** | **OFF** | Bypassed |
| **Guitar Controls** | **Neck Pickup \| Vol 7.0 \| Tone 5.5** | Rolling Volume to 7.0 activates touch-sensitivity; Tone at 5.5 rounds high attack |

---

### Option B: Software Signal Path (Standalone Audio / Element)
```
[Guitar D.I.] ──► [Audient iD14 Input 1 (-3.2dB Pad)] ──► [UADx Dream '65 / Paradise] ──► [Studio D Chorus] ──► [TDR Nova / Studer A800]
```

| Software Plugin | Control | Setting | Purpose |
|---|---|---|---|
| **UADx Dream '65** | Volume | **2.5** | Maximum clean headroom; zero preamp distortion |
| | Treble | **3.5** | Softens blackface bright cap and transient click |
| | Bass | **4.8** | Tight, uncompressed bottom end |
| | Bright Switch | **OFF (Normal)** | Eliminates high-end glass |
| | Reverb | **2.5** | Subtle mechanical spring reflection |
| | Mod Circuit | **Stock / Normal** | Transparent clean floor |
| | Cabinet / Mic | **1x12 EV12 (or Oxford)** | High-headroom speaker keeps humbucker bass articulate |
| | OUT | **0.0 dB (Noon)** | Neutral output level trim |
| **UADx Studio D Chorus** | Mode | **Button 1** | Transparent spatial widening without audible pitch modulation |
| **TDR Nova (Post-FX)** | High-Pass Filter | **80.0 Hz (12 dB/oct)** | Filters sub-frequency stage rumble and semi-hollow low flub |
| | High-Cut Veil | **4500.0 Hz (24 dB/oct)** | **CRITICAL**: Eliminates modern digital fizz, creating vintage archtop warmth |
| | Parametric Cut | **650 Hz (-1.5 dB, Q 1.5)** | Clears boxy cabinet resonance |
| **UADx Studer A800** | Tape Speed / Formula | **15 IPS / Tape 250** | Analog tape saturation with warm low-frequency head-bump |

---

## Universal 6-Guitar Calibration Guide

Switching between guitars while preserving the dark "Midnight Velvet" acoustic aesthetic:

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Epiphone Sheraton II** *(Anchor)* | Neck HB, Vol 7.0, Tone 5.5 | Baseline: Vol 2.8, Bass 5.5, Treb 2.5 | Baseline: Vol 2.5, Treb 3.5, Bass 4.8 | Pure flatwound acoustic bloom; zero pick click; pillowy low-mids. |
| **Gibson Les Paul Studio** | Neck 490R, Vol 7.0, Tone 5.5 | **Bass +0.5 (6.0), Treble +0.5 (3.0)** | **Bass +0.4 (5.2), Treble +0.5 (4.0)** | Solid mahogany/maple provides faster transient attack and longer sustain. Treble 3.0 restores top air lost with roundwounds. |
| **Epiphone Les Paul (Rebel 90s)** | Neck P-90, Vol 6.5, Tone 5.0 | **Bass -1.0 (4.5), Treble 2.5** | **Bass -0.8 (4.0), Treble 3.5** | Tonerider Rebel 90s have massive lower-mid inductive energy. Pulling Bass to 4.5 prevents low-end boom on drop-2 jazz chords. |
| **Framus Earl Slick (DiMarzio P-90s)** | Neck P-90, Vol 6.5, Tone 4.5 | **Bass 5.5, Treble -0.5 (2.0)** | **Treble -0.5 (3.0), Bass 4.8** | Swamp ash body and DiMarzio P-90s have a sharper attack. Roll guitar tone to 4.5 and TKIP Treble to 2.0 to maintain the "velvet" cushion. |
| **Fender Player II Telecaster** | Neck Single-Coil, Vol 7.5, Tone 5.0 | **Bass +1.0 (6.5), Treble 2.5** | **Bass +1.0 (5.8), Treble 3.0** | Single-coil requires elevated Bass (6.5) to simulate the round body of an archtop humbucker (Ed Bickert style). |
| **Squier Stratocaster (Tex-Mex)** | Position 1 (Neck SC), Vol 7.0, Tone 4.5 | **Bass +1.0 (6.5), Treble -0.5 (2.0)** | **Bass +1.0 (5.8), Treble 2.5** | Tex-Mex single-coils have hot upper-mids. Tame with Treble 2.0 and rely on the neck pickup's woody warmth. |

---

## Musical Rationale & Multi-Instrument Bridge

- **The Alto Saxophone Embouchure Bridge**: In its lower register, an alto saxophonist produces a pillowy, woody "sub-tone" by dropping jaw pressure and relaxing the lower lip on the reed. This preset mimics that exact acoustic phenomenon by filtering harsh high frequencies and letting the lower-mid fundamental blossom.
- **A Cappella Voice Leading**: In 4-part or 8-part a cappella vocal arrangements, close intervals (minor and major seconds in maj7 or min9 chords) quickly become muddy if the baritone or bass range is congested. The 80 Hz high-pass and 650 Hz scoop ensure drop-2 chord voicings (e.g. Cmaj9: `8-x-9-7-8-x` or Dm9: `10-x-10-10-10-x`) speak with pristine harmonic clarity.
- **Fretboard Ergonomics**: The flatwound 10s on the Sheraton have higher tension than roundwounds. Because the dynamic floor is cushioned by the high-cut veil, Mike does not need to press hard with the fretting hand to produce a rich, authoritative tone, reducing hand strain during extended jazz practice.

---

## Optional Footnote: All-Digital Workflow & Three-Way Cross-Amp Comparison

For an all-digital workflow or when A/B/C testing across hardware and software platforms, load the generated native presets below:

### 1. UADx Paradise Guitar Studio Preset (`Toneprint - Midnight Velvet Archtop.json`)
- **Location**: `uaudio_paradise_guitar_studio/Dream '65/` and `tones/presets/paradise/`
- **Amp Engine**: **Dream '65** (Model 0)
- **Amp Controls**: Volume **2.5**, Treble **3.5**, Bass **4.8**, Bright **OFF**, Mod **Stock**, Reverb **2.5** (ON), Boost **OFF**, Output **12.0**
- **Cabinet / Mic**: **1x12 EV12** (`cab_and_mic`: 29)
- **Pre-FX**: None (pure clean dynamic headroom)
- **Post-FX**: Slot 1: **Brigade Chorus** (Button 1 style subtle stereo spread)

### 2. Neural DSP Archetype Cory Wong X Preset (`Midnight Velvet Archtop.xml`)
- **Location**: `/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints/` and `tones/presets/neural/`
- **Amp Engine**: **The Clean Machine** (Amp 1)
- **Amp Controls**: `volume`: **30%**, `BASS`: **45%**, `MIDDLE`: **65%**, `TREBLE`: **40%**, `PRESENCE`: **50%**, `BRIGHT`: **OFF**, `OUTPUT`: **70%**
- **9-Band Graphic EQ**: **Active** — 250 Hz: **-2.0 dB**, 500 Hz: **+1.5 dB**, 1 kHz: **+1.0 dB**, 2 kHz: **-1.0 dB**, 4 kHz: **-1.5 dB** (Shapes flat Blackface scoop into dark archtop wood)
- **Pre-FX**: **The 4th Position Compressor** (Active — Blend 45%, Compression 30%, Tone 45%, Volume 55%)
- **Cabinet**: Cab 2 (Clean 1x12), Mic: Dynamic 57 (Pos 0.48, Dist 0.25) + Room Mic Level -28 dB
- **Post-FX**: **The Wash** (Active — Mix 15%, Decay 35%, Shimmer OFF)

### 3. Three-Way Cross-Amp Comparison Matrix

| Dimension | Tone King Imperial Preamp (Physical Tube) | UADx Paradise Guitar Studio (Dream '65) | Archetype Cory Wong X (Clean Machine) |
|---|---|---|---|
| **Core Circuit & Architecture** | 3x 12AX7 high-voltage tubes (~250–300V), AB763 Blackface tone stack, Ironman II reactive attenuator | Component-level analog circuit emulation of 1965 AB763 Deluxe Reverb | High-headroom modern pristine clean amplifier with active 9-band EQ |
| **Midrange Voicing** | Natural 500 Hz Blackface scoop flattened physically by setting Treble to 2.5 and Bass to 5.5 | Emulated AB763 scoop warmed via Treble 3.5 and 1x12 EV12 speaker pairing | Active Graphic EQ (+1.5 dB @ 500 Hz, +1.0 dB @ 1 kHz) creates direct woody archtop acoustic hump |
| **Feel & Dynamic Sag** | Instant physical tube plate recovery; zero digital latency; spongy physical 12AX7 compression under firm thumb strokes | Modeled tube/rectifier sag; smooth high-frequency roll-off into EV12 | Ultra-fast, immediate transient response; optical compressor provides smooth, studio-grade leveling |
| **Acoustic Bloom & Resonance** | Real-world tube warmth synergizes with semi-hollow body air and Thomastik flatwounds | Rich harmonic bloom across sustained chord voicings; vintage spring reflection | Extremely quiet noise floor; laser-focused note separation for complex extended jazz harmony |

