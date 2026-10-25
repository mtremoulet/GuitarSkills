# Software Amp Translation Matrix & Modeling Guide

## 1. Gain Staging & Interface Calibration Standards

### Audient iD14 mkII Hardware Offset Calibration
- **Physical Baseline**: Guitar plugged into the front discrete JFET Instrument Input (D.I.) with physical gain at **minimum (0)** for maximum analog headroom (**+9.0 dBu**) and minimum noise floor.
- **Reference Mismatch**: UADx and Neural DSP calibrate virtual tube models to a **+12.2 dBu** clipping reference (Apollo Twin Hi-Z at minimum gain). Because the iD14 clips at **+9.0 dBu**, the incoming digital signal is **+3.2 dB hotter** than expected.
- **Calibration Standard**:
  - *Bus / Input Fader Calibration*: Set master D.I. input fader (or bus send) to **-3.2 dB** before feeding amp modelers.
  - *Plugin Level Trims*: If routing directly without bus trims, apply **-3.2 dB** via plugin input trim (`IN` knob on UADx or input slider on Neural DSP).
- **Clean Master Level Staging**:
  - In UADx plugins (`Dream '65`, `Woodrow '55`, `Lion '68`), the `Volume` / `Inst Vol` knobs dictate tube saturation, compression, and harmonic bloom.
  - Never adjust interface gain or internal amp volume to balance listening level; use the dedicated **`OUT` knob** on the far right of the plugin GUI to target peak track levels between **-12 dBFS and -10 dBFS**.

---

## 2. UADx Dream '65 Reverb Amp (& Paradise Dream Engine)

### Core Topology
- Emulation of a 1965 Fender Blackface Deluxe Reverb (AB763 circuit, dual 6V6 power section, GZ34 tube rectifier).
- Controls: **Volume**, **Treble**, **Bass**, **Bright/Normal Switch**, **Mod Circuit** (Stock / Lead / D-Tex), **Boost**, **Reverb**, **Vibrato**, **Speaker Cabinet**.

### Mod Voicings vs. Tone King Mid-Bite
1. **Stock**: Clean boost up to +10 dB. Bright cap and tone stack unmodified. Transparent gain boost.
2. **Lead Mod (The Mid-Bite Mirror)**:
   - Removes bright cap and lifts the midrange tone stack ("lead boost"), producing a darker, punchier, mid-forward voice.
   - **Direct Translation to Tone King**: Directly mirrors the Tone King Imperial Preamp Lead channel's `Mid-Bite` circuit at mid-settings (Pip 4.0–6.0), which simultaneously lifts upper midrange, smooths highs, and tightens low-end.
3. **D-Tex Mod**:
   - SRV-inspired mod adding heavy midrange and gain. Bass and Treble controls have reduced effect at higher boost values; Vibrato is disabled when boost is engaged.
   - Mirrors Tone King Lead channel with Mid-Bite pushed high (Pip 7.0–8.5).

### Onboard Reverb & Vibrato (Tremolo)
- **Reverb**: Convolution tube-driven spring reverb. Reverb level compresses with higher amp gain, matching the behavior of the Tone King Imperial spring convolution reverb.
- **Vibrato**: Tube bias tremolo with Speed and Intensity knobs, matching the Tone King Imperial's bias-style tremolo.

### Cabinet Options
- **Oxford 12K5-6**: Stock 1965 sound; scooped mids, biting highs.
- **GB25**: Celestion Greenback 25W; warm, mid-focused British bark.
- **EV12**: Electro-Voice EVM12L; massive clean headroom, tight percussive low end.
- **Boutique D65**: Two-Rock 2x12 with G12-65s; smooth vocal mids, round highs.
- **S-Verb**: 1966 4x10 Super Reverb; fast punch, surf/R&B chime.
- **JBF120**: 1968 Twin Reverb 2x12 with JBL D-120Fs; ultra-clean hi-fi glass, unyielding headroom.
- **Direct**: Complete cabinet bypass (essential when using Tone King hardware IRs).

---

## 3. UADx Woodrow '55 Instrument Amp (& Paradise Woodrow Engine)

### Core Topology
- Emulation of a 1955 Fender Tweed Deluxe (narrow-panel 5E3 circuit, dual 6V6 cathode-biased, no negative feedback).
- Controls: **INST VOL**, **MIC VOL**, **Tone** (interactive with gain), **Inputs (High/Low)**, **Boost** (Stock / KP-3K / EP-III), **Speaker Cabinet**.

### Channel Jumping & Tone Interaction
- **Jumped Mode**: When both `INST VOL` and `MIC VOL` are above zero, channels are blended in parallel.
- **Interactive Tone Control**: Turning `Tone` up increases both treble and preamp overdrive. Treat as combined Treble + Gain.

### Sonic Translation to Tone King Lead Channel (Low Mid-Bite)
- The Tone King Lead channel at low Mid-Bite (Pip 1.0–3.0) is voiced directly after the **1950s American Tweed 5E3**:
  - Spongy, blooming low-end, soft high-frequency contour, and dynamic tube sag.
  - In Woodrow '55: Low Input, `INST VOL` 3.5, `MIC VOL` 3.0, `Tone` 4.5–5.0, `Boost` Stock (or EP-III for extra low-mid bloom).

---

## 4. Neural DSP Archetype Cory Wong X

### Structure
- **Wah $\rightarrow$ Pre FX $\rightarrow$ Amp $\rightarrow$ Cab (+ Room Reverb) $\rightarrow$ 9-Band Graphic EQ $\rightarrow$ Post FX**.

### Amp Models
1. **The Clean Machine**: Sparkling Fender-style / modern clean platform. Pristine headroom, Bright switch, 4-band EQ + Presence. Translates to **Tone King Rhythm Channel**.
2. **The Amp Snob**: Boutique Dumble ODS clean/crunch. Warm vocal midrange, Master volume sag, Drive switch (additional tube stage). Translates to **Tone King Lead Channel** (Drive OFF for low Mid-Bite Tweed; Drive ON for high Mid-Bite British rock).
3. **D.I. Funk Console**: Direct solid-state channel strip with optical compression and tube saturation.

### Pre-FX & Post-FX
- **Pre-FX**: "The 4th Position Compressor" (parallel blend), "The Postal Service" (envelope filter), "The Tuber" (TS-style OD), "The Big Rig" (fat high-gain OD).
- **Post-FX**: "The 80s" Chorus, "Delay-Y-Y" (dual/single delay with HPF/LPF), "The Wash" Reverb (ambient shimmer).
- **9-Band Graphic EQ**: Dedicated per amp model (65 Hz, 125 Hz, 250 Hz, 500 Hz, 1 kHz, 2 kHz, 4 kHz, 8 kHz, 16 kHz $\pm 12$ dB).

---

## 5. UADx Paradise Guitar Studio

### Studio Environment
- 11 amps (Dream '65, Woodrow '55, Lion '68, Ruby '63, Showtime '64, Enigmatic '82, etc.) and 35 cabinet/mic configurations.
- **Pre-FX Stompboxes**: TS Overdrive, Nashville OD (Nobels ODR-1), Gold Overdrive (Klon Centaur), Metal Box (ProCo RAT), Uni-Vibe, Brigade Chorus (CE-1).
- **Post-FX Units**: 1176 FET compressor, studio reverbs (plate/spring), tape delay, studio EQ, tube tremolo, multi-tap chorus.

---

## 6. Comprehensive 1-to-1 Translation Matrices

### A. Tone King Rhythm Channel $\longleftrightarrow$ Software Translation Matrix

| TKIP Rhythm Control | Setting (Pip) | UADx Dream '65 Equivalent | Neural DSP Cory Wong X (Clean Machine) | Paradise Guitar Studio (Dream '65) |
|---|---|---|---|---|
| **Channel** | Rhythm | Dream '65 Normal | The Clean Machine | Dream '65 Amp Engine |
| **Volume** | **2.5 – 3.5** (Clean) | `Volume`: **2.5 – 3.0** | `volume`: **25% – 32%** | `Volume`: **2.5 – 3.0** |
| **Volume** | **4.0 – 5.5** (Breakup) | `Volume`: **4.0 – 5.5** | `volume`: **45% – 55%** | `Volume`: **4.0 – 5.5** |
| **Bass** | **3.0 – 7.0** | `Bass`: **3.0 – 7.0** | `BASS`: **35% – 65%** | `Bass`: **3.0 – 7.0** |
| **Treble** | **2.0 – 7.0** | `Treble`: **2.0 – 7.0** | `TREBLE`: **25% – 70%** | `Treble`: **2.0 – 7.0** |
| *(Fixed Mid)* | *Internal Scoop* | *(Fixed Mid)* | `MIDDLE`: **35% – 42%** (Scooped) | *(Fixed Mid)* |
| *(Fixed Bright)* | *Circuit Cap* | `Bright`: ON (SC) / OFF (HB) | `BRIGHT`: UP (SC) / DOWN (HB) | `Bright`: ON (SC) / OFF (HB) |
| **Attenuation** | **5.0** (Unity) | `OUT`: Noon (0.0 dB trim) | `OUTPUT`: **50% – 55%** | Status Bar `Output`: Unity |
| **Reverb Level** | **2.0 – 3.5** | `Reverb`: **2.0 – 3.5** | The Wash: Mix **15%**, Decay **30%** | Post-FX Spring: Mix **20%** |
| **Tremolo** | Speed / Depth | Vibrato: Speed / Intensity | Post-FX Chorus / Mod | Post-FX Tube Tremolo |
| **Cab Selector** | Pos 1 (TK1660) | Cab: **Oxford 12K5-6** (or EV12) | Cab: **Clean 1x12** (57 + 121) | Cab: **Oxford 1x12** |

---

### B. Tone King Lead Channel (Low Mid-Bite / Tweed) $\longleftrightarrow$ Software Translation Matrix

| TKIP Lead Control | Setting (Pip) | UADx Woodrow '55 Equivalent | Neural DSP Cory Wong X (Amp Snob) | Paradise Guitar Studio (Woodrow) |
|---|---|---|---|---|
| **Channel** | Lead | Woodrow '55 (Low Input) | The Amp Snob (`DRIVE`: OFF) | Woodrow '55 Amp Engine |
| **Volume** | **3.0 – 4.5** | `INST VOL`: **3.5**, `MIC VOL`: **3.0** | `VOLUME`: **45%**, `MASTER`: **65%** | `INST VOL`: **3.5**, `MIC VOL`: **3.0** |
| **Tone** | **4.0 – 6.0** | `Tone`: **4.5 – 5.5** (Interactive) | `TREBLE`: **45%**, `PRESENCE`: **40%** | `Tone`: **4.5 – 5.5** |
| **Mid-Bite** | **1.0 – 2.5** (Low) | `Boost`: Stock (Knob @ 2.0) | `MIDDLE`: **55% – 62%** | `Boost`: Stock |
| **Attenuation** | **5.0** (Unity) | `OUT`: Noon (0.0 dB trim) | `OUTPUT`: **50%** | Status Bar `Output`: Unity |
| **Reverb** | Level / Dwell | Room: **2.5 – 3.5** | Room Reverb / The Wash | Post-FX Spring / Plate |
| **Cab Selector** | Pos 1 (TK1660) | Cab: **JP12** (or Blu15) | Cab: **Clean 1x12** or **Snob 2x12** | Cab: **JP12 1x12** |

---

### C. Tone King Lead Channel (High Mid-Bite / Plexi) $\longleftrightarrow$ Software Translation Matrix

| TKIP Lead Control | Setting (Pip) | UADx Lion '68 Equivalent | Neural DSP Cory Wong X | Paradise Guitar Studio (Lion '68) |
|---|---|---|---|---|
| **Channel** | Lead | Lion '68 (LEAD or BROWN model) | Amp Snob (`DRIVE`: ON) + Tuber | Lion '68 Lead Engine |
| **Volume** | **5.5 – 7.5** | `Vol 1`: **7.0**, `Vol 2`: **5.5** (Jumped) | `VOLUME`: **65%**, `MASTER`: **70%** | `Vol 1`: **7.0**, `Vol 2`: **5.5** |
| **Tone** | **6.0 – 7.0** | `Treble`: **6.0**, `Presence`: **6.5** | `TREBLE`: **65%**, `PRESENCE`: **65%** | `Treble`: **6.0**, `Presence`: **6.5** |
| **Mid-Bite** | **5.5 – 7.5** (High) | `Middle`: **7.0 – 8.0**, `Bass`: **4.0** | `MIDDLE`: **75%**, `BASS`: **38%** | `Middle`: **7.5**, `Bass`: **4.0** |
| **Mid-Bite Boost** | Harmonic Peak | `Boost`: ON (EP-III, Knob @ 3.5) | Pre-FX: **The Tuber** (Drive 20%) | Pre-FX: **Gold OD** or **TS OD** |
| **Attenuation** | **5.0 – 6.0** | `OUT`: Balanced to -10 dBFS | `OUTPUT`: **45% – 50%** | Status Bar `Output`: -10 dBFS |
| **Cab Selector** | Pos 3 (Basketweave) | Cab: **Stripped On-Axis 4x12** | Cab: Custom Greenback IR / Snob 2x12 | Cab: **1968 Basketweave 4x12** |

---

### D. Cabinet IR Cross-Translation Matrix

| Hardware IR (Tone King Preamp) | Real-World Cabinet Origin | UADx Dream '65 / Woodrow Equivalent | UADx Lion '68 Equivalent | Neural DSP Cory Wong X Equivalent |
|---|---|---|---|---|
| **OH 112 Imperial TK1660** (Pos 1) | Tone King Imperial 1x12 (Eminence TK1660, SM57/U87/R121 via API 312) | **Oxford 12K5-6** (or **EV12** for tighter bass response) | **EV12 1x12** (C414) | **Clean 1x12** (Dynamic 57 + Ribbon 121) |
| **OH 212 Class A Blue** (Pos 2) | 1963 Vox AC30 2x12 (Celestion Alnico Blues, SM57/U87/R121 via API 312) | **Boutique D65** (or Woodrow **Blu15**) | **Brown JB** (Celestion + JBL blend) | **Snob 2x12** (Ribbon 121 + Dynamic 421) |
| **OH 412 Basketweave M25** (Pos 3) | 1971 Marshall 1960B 4x12 (Celestion G12M-25 Greenbacks, SM57/MD421/R121 via API 312) | **GB25** (Celestion Greenback 1x12) | **Stripped On-Axis 4x12** (Greenbacks, M160 + 57) or **GB30 4x12** | Custom 4x12 IR (or Snob 2x12 with Ribbon mic centered) |

---

## 7. Guitar-Specific Dialing Rules

1. **Gibson Les Paul Studio (490R neck / 490T bridge — Alnico II, ~8.5k DCR)**:
   - Matched vintage-output pair. In Classic Rock and Blues settings, the 490T bridge needs **+0.5 to +1.0 more Volume or Mid-Bite** than hot pickups. In clean jazz, pair 490R neck with guitar volume at 7, guitar tone at 6, and Tone King Treble at 2.5–3.0 (Dream '65 Treble 3.5–4.5, Normal mode).
2. **Framus Earl Slick Artist Series (DiMarzio P-90 single-coils)**:
   - Soapbar single-coils with natural upper-mid peak and snappy swamp ash attack. Mid-Bite is cumulative: use **0.5 to 1.0 less Mid-Bite** (or pull plugin Middle back by ~10%) to avoid harsh clatter. Roll guitar tone to 5–6 for jazz and clean blues.
3. **Epiphone Sheraton II (Semi-hollow humbuckers, flatwound 10s)**:
   - Prone to acoustic feedback when Mid-Bite exceeds 5.0. On high-gain Lead settings, keep TKIP Attenuation at **5.5 max**. On the Rhythm channel, semi-hollow warmth allows Treble to sit at 6.0–7.0 without harshness.
4. **Fender Player II Telecaster (Single-coils)**:
   - Reaches edge-of-breakup with less Mid-Bite (2.5–3.0). On the Rhythm channel, roll Treble back to 1.5–2.5 on TKIP (or 3.0 on Dream '65) and push Bass to 6.5–7.0 to give single-coils the low-end authority of a humbucker.
