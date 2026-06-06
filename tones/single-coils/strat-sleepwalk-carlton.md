---
amp: "Enigmatic '82"
created: 2026-05-31
guitar: "Mid-1980s Squier Stratocaster Partscaster (Neck or Neck+Middle position)"
id: strat-sleepwalk-carlton
pickup_type: single-coil
preset_name: "Strat Sleepwalk Carlton SC"
status: initial
tags: "surf, clean, chorus, stratocaster, carlton, dumble, delay, reverb, single-coil"
target: "Larry Carlton 'Sleepwalk' — Liquid, singing Stratocaster neck tone with touch-sensitive Dumble-style sustain, 3D chorus, and lush studio chamber reverb."
tone-king-channel: bypassed
updated: 2026-05-31
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Amp Model: "Enigmatic '82"
    Bass: 4.5
    Boost: false
    Boost Button: OFF
    Bright: false
    Bright Switch: Off
    Cab & Mics: "2×12 Boutique D65"
    Deep Switch: Off
    Input Channel: NOR
    Master: 6.5
    Mid Switch: Off
    Middle: 7.0
    Overdrive: 4.0
    Preamp Mods: SKYLINE
    Presence: 1.5
    Ratio: 4.0
    Rock/Jazz: JAZZ
    Room Level: "35%"
    Treble: 4.5
    Voice: Silver
    Volume: 4.5
  galaxy:
    echo_rate: 120.0
    feedback: 1.0
  la2a:
    gain: 40
    peak_reduction: 35
  studio_d:
    mode: "Mode 2"
---

# Strat Sleepwalk Carlton (Larry Carlton Style)

## Target Sound

This toneprint is designed specifically for the Squier Stratocaster (Neck or Neck+Middle pickup positions) to capture Larry Carlton's iconic 1981 recording of "Sleepwalk." Since Carlton famously utilized a custom Valley Arts Stratocaster-style guitar for this session rather than his signature ES-335, this tone focuses on single-coil articulation, bell-like clarity, and woodiness, combined with a highly touch-sensitive, singing sustain that emulates slide guitar. 

By utilizing the **Enigmatic '82** (Dumble Overdrive Special) within **UADx Paradise Guitar Studio**, this preset balances clean, pristine chords with a rich, mid-forward lead voice that blooms when you pick harder. Combined with a transparent peak limiter (LA-2A), a subtle non-warbling 3D chorus (Studio D), and a bused tape echo and chamber reverb, it creates a three-dimensional, "sleepy" studio landscape that responds beautifully to volume swells.

*Required Physical Setup:* To get the intended response, roll the Squier's volume knob back to **7 or 8** for clean chord work, and push to **10** for leads. Keep the guitar's neck tone knob at **7** to round off the single-coil "ice-pick" high-end.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. UADx Paradise Guitar Studio (Enigmatic '82) — the amp & cab

The heart of the singing lead voice. Set to the **Silver** voice to provide high-end clarity and articulation that prevents single-coils from getting muddy, while using the **Skyline** tone stack mod to provide the vocal mid-range bloom.

#### Gallery Configuration & Switches

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **Enigmatic '82** | Selected in the gallery |
| Voice | **Silver** | Bright, articulate Dumble voicing; matches single-coil pickups |
| Input Channel | **NOR** (Normal) | Bypasses the clinical, transistor-based FET input for warm tube sag |
| Bright Switch | **Off** (Down) | Tames harsh single-coil transients and high-end sizzle |
| Mid Switch | **Off** (Down) | Natural midrange balance |
| Deep Switch | **Off** (Down) | Keeps the low-end tight and integrated |
| Rock / Jazz | **JAZZ** | Smoother, rounder frequency response |
| Preamp Mods | **SKYLINE** | Engages the legendary Dumble midrange bloom and vocal character |
| Boost Button | **OFF** | Preserves headroom and dynamic range |

#### Amp Controls

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 4.5 | Preamp sensitivity; sets the edge-of-breakup threshold |
| Overdrive | 4.0 | Engages the overdrive circuit for touch-sensitive sustain |
| Ratio | 4.0 | Blends clean and overdriven signals for dynamic pick response |
| Treble | 4.5 | Slightly rolled back to smooth the Strat's high end |
| Middle | 7.0 | **Jazz Middle:** Fills in the single-coil scoop for a vocal sing |
| Bass | 4.5 | Warm but tight; prevents flubby low-frequency resonance |
| Master (6.5) | 6.5 | Simulates power tube saturation and bloom |
| Presence | 1.5 | Kept very low to smooth high frequencies and prevent fizz |

#### Cabinet & Room (Amp Pane)

| Component | Setting | Sonic Character & Aesthetic Profile |
|-----------|---------|-------------------------------------|
| Cab & Mics | **2×12 Boutique D65** | Emulates a 2x12 cabinet with G12-65 speakers mic'd with a pre-blended SM57 and Royer 121 ribbon. Provides smooth treble compression and thick midrange body. |
| Room Level | **35%** | Introduces natural cabinet room reflections and air, taming the "clinical precision" of the model. |

---

### 3. UADx LA-2A Silver Compressor — peak leveling

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 35 | Yields `1 to 2dB` of smooth compression on hard picking; sustains the tail of volume swells |
| Gain | 40 | Makeup gain |
| Mode | Compress | Natural, musical optical tube compression |

---

### 4. UADx Studio D Chorus — liquid width

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | **Mode 2** | Subtle, 3D spatial widening; adds a "liquid" quality without warbling the pitch |

---

### 5. UADx Galaxy Tape Echo — slapback depth (Bus 4)

Set up on an Aux/Bus track to preserve dry signal punch.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | **Mode 1** | Single playback head tape echo |
| Echo Rate | ~120ms | Short slapback to add physical, double-tracked depth |
| Feedback | 1.0 | Single repeat |
| Mix / Wet Solo | 100% / **Wet Solo ON** | Bypasses dry signal on the Aux track |
| Send Level | **−15 dB** | Tucked subtly behind the primary guitar signal |

---

### 6. UADx Hitsville Reverb Chambers — studio space (Bus 3)

Bused to allow precise mix blending and maintain dry attack clarity.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648** | Motown Studio chamber; bright, echo-like space with excellent depth |
| Mix / Wet Solo | 100% / **Wet Solo ON** | Bypasses dry signal on the Aux track |
| Send Level | **−12 dB** | Provides the lush, "sleepy," wet atmospheric landscape |

---

## Starting Point Guide

- **Volume Swell Technique**: Coordinate your picking hand with your volume pedal (or physical volume knob). Strike the note with the volume at zero, then roll it up immediately to eliminate the pick transient and let the note bloom.
- **Mid-Bite Adjustment**: If your Squier's pickups sound too bright or "hollow" for the vocal melody, increase the **Middle** control on the Enigmatic '82 to **7.5** or **8.0** to add throaty body.
- **Vibrato Timing**: Let the note bloom clean first using your volume swell, and only begin your slow, wide hand-vibrato as the note begins to sustain. This mirrors Larry Carlton's vocal singing style.

---

## Feedback History

### 2026-05-31 — initial
Designed specifically for the mid-1980s Squier Stratocaster "Partscaster" neck pickup to replicate the custom Valley Arts Strat tone Carlton utilized on the original *Sleepwalk* title track recording. Configures Paradise Guitar Studio's Enigmatic '82 in the "Silver" ODS voice with a Skyline tone stack to balance single-coil chime with a rich, vocal midrange. Incorporates Studio D chorus for liquid width, and bused slapback tape echo and Hitsville reverb chambers to complete the 3D studio landscape.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
