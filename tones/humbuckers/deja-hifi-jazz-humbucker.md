---
amp: "JC120 Jazz Chorus (Nembrini)"
created: 2026-08-08
guitar: "Gibson Les Paul / Epiphone Sheraton II (humbuckers)"
id: deja-hifi-jazz-humbucker
pickup_type: humbucker
preset_name: "Deja HiFi Jazz Clean HB"
status: initial
tags: "jazz, hifi, solid-state, humbucker, deja, les-paul, sheraton, cheek-to-cheek, nembrini, jc120"
target: "Hi-fi, well-rounded, precise jazz warmth inspired by 'Deja' (Dancing Cheek to Cheek). High clarity solid-state response with zero clack or brittleness for Les Paul & Sheraton II humbuckers."
tone-king-channel: bypassed
updated: 2026-08-08
preset_data:
  nembrini_jc120:
    Bass: 5.5
    Distortion: 0.0
    Middle: 6.8
    Reverb: 0.0
    Treble: 4.2
    Volume: 3.5
  la2a:
    compress: true
    gain: 35.0
    peak_reduction: 30.0
  logic_eq:
    band1:
      freq: 80.0
      on: true
      slope: 12.0
    band4:
      freq: 280.0
      gain: 1.8
      on: true
      q: 1.0
    band8:
      freq: 5800.0
      on: true
      slope: 12.0
  logic_compressor:
    attack: 25.0
    knee: 0.7
    makeup_gain: 0.0
    ratio: 2.5
    release: 120.0
    threshold: -18.0
  hitsville:
    chamber: "Chamber 1"
    decay: 2.8
    mic: "Unidyne 545"
    mix: 100.0
    pre_delay: 20.0
    speaker: "Set 1"
---

# Deja HiFi Jazz Clean HB

## Target Sound
Inspired by the lush, sophisticated French jazz arrangement of *"Déjà"* (*Dancing Cheek to Cheek*). Designed specifically for humbucker instruments (**Gibson Les Paul** on the neck/middle positions and **Epiphone Sheraton II** semi-hollowbody).

The goal is to recreate the sound of a premium archtop/hollowbody playing through a pristine, high-headroom solid-state jazz amplifier:
- **Hi-Fi Precision**: Every note in complex 4-note jazz voicings (ma7, m9, 13b9) is distinct, balanced, and articulate without sagging into tube saturation.
- **Controlled Transients**: Softens initial pick click ("clacking trebleness") using gentle LA-2A optical peak reduction before the amp, while retaining note attack.
- **Round & Warm Midrange**: Uses a dedicated 280 Hz low-mid bloom and a smooth 5.8 kHz high-cut filter to eliminate glassy digital top-end without dampening overall clarity.

---

## Signal Chain

### 1. Hardware Interface & Front-End
*   **Physical Setup:** Guitar connected directly to **Audient iD14 Instrument Input 1** (D.I. Route).
*   **Tone King Imperial Preamp:** **Bypassed** (clean, transparent digital signal path).
*   **iD14 Calibration Offset:** Set plugin Input Gain (IN) to **−3.2 dB** (or compensate via track input trim) to align Audient D.I. headroom (+9 dBu) with plugin modeling standards (+12.2 dBu).

---

### 2. Pre-Amp Dynamics — UADx Teletronix LA-2A Silver
*Smooths sharp pick attacks and rounds transient clicks before the solid-state input stage.*

| Control | Setting | Technical Rationale |
|---------|---------|---------------------|
| Peak Reduction | 30.0 (30%) | Soft 1.5–2.0 dB peak leveling on initial pick contact to remove "clack" |
| Gain | 35.0 (35%) | Unity gain makeup matching dry bypass level |
| Mode | Compress | Smooth 3:1 optical compression curve rather than hard limiting |

---

### 3. Primary Amplifier — Nembrini JC120 (Roland Jazz Chorus 120)
*Pristine, zero-sag solid-state clean engine providing fast note separation and hi-fi detail.*

#### Gain Staging & Input/Output
| Control | Setting | Technical Rationale |
|---------|---------|---------------------|
| Input Slider | −3.2 dB | Level matching for humbuckers |
| Output Slider | −6.0 dB | Headroom protection for downstream DAW & Sennheiser HD660S2 monitoring |

#### Amp Controls
| Control | Setting | Technical Rationale |
|---------|---------|---------------------|
| Volume | 3.5 | Clean, linear headroom; zero power section breakdown |
| Bright Switch | OFF | Prevents harsh glassy top-end; warmth is prioritized |
| Middle | 6.8 | **Jazz Middle Rule**: Fills in natural humbucker body and vocal midrange |
| Treble | 4.2 | Softened high-end; clear without sizzle |
| Bass | 5.5 | Tight, well-rounded low end; avoids boominess on low E/A strings |
| Distortion | 0.0 | OFF |
| Reverb | 0.0 | OFF (using Hitsville Reverb on Bus 3) |
| Mode | OFF / CHORUS | OFF for intimate solo/duo work; switch to CHORUS for subtle stereo width |

#### Cabinet & Microphone
| Control | Setting | Technical Rationale |
|---------|---------|---------------------|
| Cabinet | RLD 2x12 JC120 | Factory 2x12 aluminum-cap speaker cabinet |
| Microphone | Ribbon 121 | **Dark/Warm choice**: High-frequency roll-off native to ribbon capsule |
| Position | 0.40 | Off-center positioning to smooth out direct cone sizzle |
| Distance | 0.25 | Balanced proximity effect |

---

### 4. Post-Amp Sculpting — Logic Channel EQ
*Polishes the solid-state response to deliver a dark, hi-fi archtop acoustic veil.*

| Band | Type | Frequency | Gain / Slope | Q | Technical Rationale |
|------|------|-----------|--------------|---|---------------------|
| Band 1 | High-Pass (Low Cut) | 80 Hz | 12 dB/oct | — | Cleans up sub-bass rumble below low E (82 Hz) |
| Band 4 | Low-Mid Bell | 280 Hz | +1.8 dB | 1.0 | Enhances woody body resonance of Les Paul / Sheraton body |
| Band 8 | Low-Pass (High Cut) | 5.8 kHz | 12 dB/oct | — | **The High-Cut Veil**: Removes clacking digital glassiness above 6 kHz |

---

### 5. Spatial Environment — Send to Bus 3 (Reverb): −16 dB

#### Aux Track Plugin — UADx Hitsville Reverb Chambers
*Creates the acoustic illusion of an un-miked hollowbody guitar in Motown's historic Studio A.*

| Control | Setting | Technical Rationale |
|---------|---------|---------------------|
| Chamber | Chamber 1 (2648) | Warm, dense natural reverb chamber |
| Speaker | Set 1 (Altec/Bozak) | Smooth frequency decay |
| Mic | Unidyne 545 | Dynamic microphone character for controlled upper-end decay |
| Pre-Delay | 20 ms | Separates direct pick articulation from chamber bloom |
| Decay | 2.8 s | Moderate tail length that doesn't muddy chord changes |
| Mix | 100% | **Bus-First Standard**: Full wet signal on Aux bus |
| Wet Solo | ON | Fader controls send balance |

---

## Performance & Guitar Setup Notes

1. **Guitar Controls (The "7/7" Rule)**:
   - **Neck Pickup**: Primary choice for *Déjà*. Set Volume to **7.5** and Tone to **7.0**. Rolling off the tone knob slightly on the guitar works in synergy with the LA-2A and 5.8 kHz high-cut filter.
   - **Middle Position (Both Pickups)**: Toggle both humbuckers on, with Neck at **8** and Bridge at **6**, for a sparkling, acoustic-like rhythmcomping texture.
2. **Right-Hand Dynamics**:
   - Use thumb-and-fingers style (or a 1.0mm-1.5mm thick acrylic/delrin pick) for smooth, woody attacks.

---

## Preset Compilation

Run the compiler to build native DAW user presets for all chain components:
```bash
python3 scripts/compile_all_presets.py -f deja
```
