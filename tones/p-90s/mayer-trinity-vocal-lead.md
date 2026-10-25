---
id: mayer-trinity-vocal-lead
preset_name: "Mayer Trinity Vocal Lead"
created: 2026-09-06
updated: 2026-09-06
pickup_type: p-90
guitar: "2012 Framus Earl Slick Artist Series (DiMarzio P-90s, Bigsby B500 Vibrato)"
target: 'Singing, horn-like vocal midrange lead sustain with harmonic richness, zero ice-pick treble, and expressive pitch vibrato.'
tags: "blues, lead, dumble, mayer, ods, tone-king, p-90, framus, rotary, sustain"
amp: "Enigmatic '82 (UADx) / Tone King Imperial (Hardware)"
tone-king-channel: lead
status: tested
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    enigmatic_model: 2
    enigmatic_volume: 5.0
    enigmatic_master_gain: 7.8
    enigmatic_middle: 7.0
    enigmatic_treble: 5.0
    enigmatic_bass: 4.4
    enigmatic_presence: 4.2
    cab_and_mic: 2
  prefx:
    slot1:
      pedal: ts_overdrive
      enabled: true
      overdrive: 2.0
      level: 6.0
      tone: 3.9
  hardware_settings:
    Channel: Lead
    Volume: 4.5
    Attenuation: 5.5
    Tone: 4.5
    Mid-Bite: 4.0
    IR: "OH 412 Basketweave M25"
    Reverb:
      Level: 2.0
      Dwell: 2.5
    Tremolo: Off
    Guitar_Volume: 7.0
    Guitar_Tone: 6.5
---

# Mayer Trinity Vocal Lead

## Target Sound

Modeled directly on the singing vocal lead voice from your Mayer Trinity Element session (`docs/mayer-trinity-rig-guide.md:L41, L92-105`) and the expressive soloing styles of John Mayer (*Try!*, *Continuum*), Marcus King, and Stevie Ray Vaughan.

In professional multi-amp rigs, achieving horn-like lead sustain without brittle high-end sizzle relies on pushing an aggressive 800 Hz–2.5 kHz midrange hump while tightening loose sub-bass frequencies. On the physical Tone King Imperial Preamp pedal, we set the **Lead channel with Mid-Bite pushed to 4.0** and pair it with **Cab 3 (OH 412 Basketweave M25)**. This engages the circuit's internal pre-gain bass clamp and upper-mid resonant peak, transforming the pedal into an analog Dumble Overdrive Special (ODS) without requiring an external Tube Screamer in front. In software, this is mirrored in **Paradise Guitar Studio** by loading the **Enigmatic '82 ODS** pushed by the onboard TS Overdrive.

---

## Signal Chains

### Option A: Physical Hardware Signal Path (Direct-in / Standalone)
```
[Framus Earl Slick (Bridge P-90)] ──► [Tone King Imperial Preamp (Hardware)] ──► [Audient iD14 Line In] ──► [Post-Amp DAW/Host FX]
```

| Hardware Control | Setting (1–9 Pips) | Technical Rationale |
|---|---|---|
| **Channel** | **Lead** | Vintage British rock / Dumble vocal lead architecture |
| **Volume** | **4.5** | Pushes the 12AX7 preamp tubes and phase inverter into rich saturation |
| **Attenuation** | **5.5** | High dynamic drive into the IR cabinet engine |
| **Tone** | **4.5** | Rolled back to balance swamp ash snap and DiMarzio P-90 top end |
| **Mid-Bite** | **4.0** | **CRITICAL**: The vocal sweet spot; tightens bass, adds thick vocal sustain |
| **Cab IR Selector** | **Cab 3 — OH 412 Basketweave M25** | **CRITICAL**: Marshall 4x12 Greenbacks; adds massive low-mid authority and girth |
| **Reverb** | **ON** (Level 2.0, Dwell 2.5) | Studio room-like spring decay that sits behind fast, singing lead lines |
| **Tremolo** | **OFF** | Bypassed |
| **Guitar Controls** | **Bridge P-90 (or Middle) \| Vol 7.0–10 \| Tone 6.5** | Vol 7.0 gives dynamic rhythm crunch; rolling to 10 unleashes singing lead sustain |

---

### Option B: Software Signal Path (Standalone Audio / Element)
```
[Guitar D.I.] ──► [Audient iD14 Input 1 (-3.2dB Pad)] ──► [Paradise Guitar Studio (Enigmatic ODS)] ──► [Waterfall Rotary] ──► [Studer A800]
```

| Software Plugin | Control | Setting | Purpose |
|---|---|---|---|
| **Paradise: Pre-FX** | TS Overdrive | **Drive 2.0, Level 6.0, Tone 3.9** | Tightens low end and injects focused 720 Hz vocal mid-hump |
| **Paradise: Amp** | Enigmatic '82 (Model: Cream) | **Volume 5.0, Master 7.8** | Saturated tube gain stage with power section sag |
| | Tone Stack | **Middle 7.0, Treble 5.0, Bass 4.4, Pres 4.2** | Thick vocal core filling the 800 Hz–2 kHz frequency band |
| | Cab / Mic | **2x12 Boutique D65 (or 4x12 Greenback)** | Smooth rolled highs, singing Celestion response |
| **UADx Waterfall Rotary** | Speed / Mix | **Slow (Chorale) / Mix 18%** | Parallel Doppler swirl making single notes sound like a vocal choir |
| **UADx Studer A800** | Tape Speed / Formula | **30 IPS / Tape 900 (+9 dB)** | Musical tape compression smoothing transients on fast pick runs |
| **Element Airwindows** | Module / Mode | **Console7 / StereoEnsemble** | Subtle analog console summing and stereo soundstage widening |

---

## Universal 6-Guitar Calibration Guide

Switching between guitars while dialing in the singing "Mayer Trinity Vocal Lead" sustain:

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Framus Earl Slick (DiMarzio P-90s)** *(Anchor)* | Bridge P-90, Vol 7–10, Tone 6.5 | Baseline: Vol 4.5, Tone 4.5, Mid-Bite 4.0 | Baseline: Enigmatic ODS Mid 7.0 + TS | Singing horn-like vocal midrange sustain; Bigsby B500 adds expressive violin-like vibrato. |
| **Gibson Les Paul Studio** | Bridge 490T, Vol 8–10, Tone 7.0 | **Volume +1.0 (5.5), Mid-Bite +1.0 (5.0)** | **ODS Drive +10%, Mid 7.5** | **CRITICAL CALIBRATION**: 490T Alnico II is moderate output (~8.5k). Pushing Volume to 5.5 and Mid-Bite to 5.0 restores liquid Dumble sustain. |
| **Epiphone Les Paul (Rebel 90s)** | Bridge P-90, Vol 7–9.5, Tone 6.0 | **Tone -0.5 (4.0), Mid-Bite 4.0** | **ODS Presence -5%, Treble 4.8** | Tonerider Rebel 90 bridge is fat and creamy. Pulling Tone to 4.0 yields a thick Santana / Gary Moore vocal lead. |
| **Fender Player II Telecaster** | Bridge (or Neck), Vol 8–10, Tone 5.5 | **Tone -0.8 (3.7), Mid-Bite +0.5 (4.5)** | **TS Tone 2.5, ODS Treble 4.5** | Tele bridge pickup has sharp treble. Roll guitar tone to 5.5 and TKIP Tone to 3.7; Mid-Bite 4.5 provides thick, biting Texas blues grind. |
| **Squier Stratocaster (Tex-Mex)** | Position 1 (Bridge) or Pos 5 (Neck), Vol 8.5–10 | **Tone -0.5 (4.0), Mid-Bite +0.5 (4.5)** | **TS Drive 2.5, Level 6.5, ODS Mid 7.2** | The quintessential SRV / John Mayer "Gravity" solo voice. Neck pickup with Mid-Bite 4.5 gives thick, fluty, horn-like sustain. |
| **Epiphone Sheraton II** | Bridge Humbucker, Vol 7.5–9, Tone 6.5 | **Mid-Bite -0.5 (3.5), Attenuation 5.0 max** | **ODS Master Gain -10%** | Semi-hollow body can take off into uncontrolled feedback if Mid-Bite exceeds 4.0. Keep Attenuation $\le 5.0$ for controllable singing sustain. |

---

## Musical Rationale & Multi-Instrument Bridge

- **The Alto Saxophone Breath & Violin Vibrato Bridge**: A saxophone soloist shapes vocal phrasing by modulating breath support—notes attack with reed bite and bloom into clean fundamental sustain. Similarly, a violinist uses continuous wrist-driven vibrato to maintain harmonic richness across bow reversals.
- **Physical Expression**: DiMarzio P-90 single-coils have immediate pick attack that simulates an alto sax reed tongue. Setting Mid-Bite to 4.0 introduces analog compression that catches the note as the initial pick transient decays. Mike can use the physical **Bigsby B500 vibrato arm** to apply subtle, continuous pitch modulation—mirroring violin vibrato—without destabilizing tuning.

---

## Optional Footnote: All-Digital Workflow & Three-Way Cross-Amp Comparison

For an all-digital workflow or when A/B/C testing across hardware and software platforms, load the generated native presets below:

### 1. UADx Paradise Guitar Studio Preset (`Toneprint - Mayer Trinity Vocal Lead.json`)
- **Location**: `uaudio_paradise_guitar_studio/Enigmatic '82/` and `tones/presets/paradise/`
- **Amp Engine**: **Enigmatic '82 ODS** (Model: Cream / 2)
- **Amp Controls**: Volume **5.0**, Master Gain **7.8**, Middle **7.0**, Treble **5.0**, Bass **4.4**, Presence **4.2**, Output **12.0**
- **Cabinet / Mic**: **2x12 Boutique D65** (`cab_and_mic`: 2)
- **Pre-FX**: Slot 1: **TS Overdrive** (Active — Drive 2.0, Level 6.0, Tone 3.9)
- **Post-FX**: Slot 1: **Plate 140 Reverb** (Active — Decay 2.5s, Mix 20%)

### 2. Neural DSP Archetype Cory Wong X Preset (`Mayer Trinity Vocal Lead.xml`)
- **Location**: `/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints/` and `tones/presets/neural/`
- **Amp Engine**: **The Amp Snob** (Amp 2, `DRIVE`: **ON**)
- **Amp Controls**: `VOLUME`: **62%**, `MASTER`: **65%**, `BASS`: **42%**, `MIDDLE`: **75%**, `TREBLE`: **48%**, `PRESENCE`: **45%**, `BRIGHT`: **OFF**, `OUTPUT`: **50%**
- **Pre-FX**: **The Tuber** (Active — Drive 25%, Level 70%, Tone 40%)
- **9-Band Graphic EQ**: **Active** — 125 Hz: **-2.0 dB**, 1 kHz: **+2.5 dB**, 2 kHz: **+1.5 dB** (Shapes classic Dumble singing vocal formant)
- **Cabinet**: Cab 2 (Snob 2x12), Mic: Dynamic 57 + Ribbon 121 (Room Mic -20 dB)
- **Post-FX**: **Delay-Y-Y** (Active — Mix 25%, Feedback 28%, 350 ms) + **The 80s Chorus** (Active — Mix 15%, Rate 15%, Width 40% subtle widening)

### 3. Three-Way Cross-Amp Comparison Matrix

| Dimension | Tone King Imperial Preamp (Physical Tube) | UADx Paradise Guitar Studio (Enigmatic ODS) | Archetype Cory Wong X (Amp Snob Drive ON) |
|---|---|---|---|
| **Core Circuit & Architecture** | Lead channel with Mid-Bite pushed to 4.0; all-tube high-voltage 12AX7 stages + Cab 3 (OH 412 Basketweave M25) | Emulated Dumble Overdrive Special (HRM/Cream voice) driven by TS Overdrive | High-gain tube stage of The Amp Snob driven by The Tuber overdrive |
| **Midrange Vocal Formant** | Mid-Bite circuit simultaneously clamps low frequencies and boosts 1.5–2.5 kHz; aggressive, organic, biting saxophone reed attack | Warm, thick, horn-like 800 Hz–1.5 kHz singing bloom; classic John Mayer / Larry Carlton Dumble voice | Tight, focused, hyper-articulate modern fusion lead; 9-band EQ carves surgical vocal midrange |
| **Sustain & Compression** | True analog tube compression; notes sustain smoothly into feedback as the physical guitar top resonates | Smooth, musical power amp sag; long, singing note sustain with rich second and third harmonics | Highly consistent, polished sustain; very forgiving on fast legato runs with minimal noise floor |
| **Bottom-End Tightness** | Cab 3 4x12 Greenbacks provide massive low-mid punch while internal high-pass filter eliminates flub | Tightened low end via Pre-FX TS Overdrive; round, articulate low-string riffing | The Tuber bass cut + Graphic EQ -2 dB at 125 Hz keeps palm-muted low notes razor-sharp |

