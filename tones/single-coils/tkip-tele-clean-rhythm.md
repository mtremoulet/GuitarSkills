---
id: tkip-tele-clean-rhythm
preset_name: "TKIP Tele Clean Rhythm"
created: 2026-06-06
updated: 2026-06-06
guitar: "Fender Player II Telecaster"
target: 'An ultra-clean, transparent, high-headroom rhythm tone with sweet, warm optical compression.'
tags: "country, clean, rhythm, single-coil, telecaster, transparent"
tone-king-channel: rhythm
amp: "Tone King Imperial Preamp (Hardware)"
status: initial
pickup_type: single-coil
preset_data:
  amp_platform: hardware
  amp_settings:
    Channel: Rhythm
    Volume: 2.5
    Attenuation: 5.0
    Bass: 5.5
    Treble: 5.0
    Reverb: Off
    Tremolo: Off
    IR: Active (Imperial 1x12 - OH 112 Imperial TK1660)
  la2a:
    peak_reduction: 30.0
    gain: 42.0
    compress: true
  studio_d_chorus:
    mode: 1
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 12.0}
    band7: {on: true, freq: 8000.0, gain: -1.5}
  hitsville:
    mix: 0.12
    pre_delay: 15.0
    decay: 1.5
    wet_solo: false
---

# TKIP Tele Clean Rhythm

## Target Sound
An ultra-clean, pristine rhythm tone featuring the chime and clarity of the Fender Player II Telecaster. The hardware Tone King Rhythm channel is dialed for maximum headroom and transparency (Volume 2.5, Attenuation 5.0, Bass 5.5, Treble 5.0) with the built-in Imperial 1x12 speaker IR (OH 112 Imperial TK1660) active for intimate, close-mic'd warmth. Logic processing uses the UADx LA-2A Silver Compressor to smooth out pick transients with fast, clean, and transparent optical compression. A touch of Studio D chorus adds subtle stereophonic width, while the Hitsville chamber reverb places the guitar in a beautiful, open studio space.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
Provides the pristine, high-headroom blackface clean platform and warm speaker character.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Clean blackface voicing at maximum headroom |
| Volume | 2.5 | Kept very low to prevent any preamp clipping or saturation |
| Attenuation | 5.0 | Unity/moderate output |
| Bass | 5.5 | Slightly boosted for round, full low-end body |
| Treble | 5.0 (noon) | Flat response; Tele pickups provide natural high-end clarity |
| Reverb | Off | Handled in Logic sends |
| Tremolo | Off | Disabled |
| IR | Active (Imperial 1x12 TK1660) | Voiced for intimate warmth and balanced midrange |

### 2. UADx LA-2A Silver Compressor — smooth optical leveler
Placed inline in Logic to smooth out dynamic peaks transparently without changing the Tele's transparent chime or slowing down picking transients.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 30.0 | Soft leveling (1.5–2 dB of gain reduction on peaks) |
| Gain | 42.0 | Makeup gain |
| Compress/Limit | Compress | Soft 3:1 ratio |
| Emphasis / HF | Fully Clockwise (default) | Equal frequency sensitivity |

### 3. Logic Channel EQ — subtle sweetness
Placed after the compressor to keep the high-end sweet and clean.

| Control | Setting | Purpose |
|---------|---------|---------|
| Band 1 (High Pass) | On — 80.0 Hz, 12 dB/oct | Cleans up cabinet sub-bass rumble |
| Band 7 (High Shelf) | On — 8.0 kHz, −1.5 dB | Gently sweetens the high end to eliminate digital harshness |

### 4. UADx Studio D Chorus — stereophonic width
Adds wide, subtle spatial enhancement to make the dry Tele clean tone bloom in stereo.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Button 1 (Active) | Subtle, classic spatial chorus enhancement |
| Mix | 100% (Default) | Fully wet/dry hardware blend |

### 5. Hitsville Reverb Chambers (Bus 3 Send) — space reverb
Set on Bus 3 at **100% Wet** (Wet Solo ON) to put the clean chords in a warm, open chamber.

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −14.0 dB | Present, sitting beautifully under the dry Tele notes |
| Chamber | Chamber 2 | Mellow chamber voicing |
| Mix | 1.0 (100% Wet) | Aux bus blend |
| Decay | 1.5 seconds | Shorter tail for clear, defined rhythm playing |
| Pre-Delay | 15 ms | Separates dry picking attack from the room bloom |

---

## Starting Point Guide
- **First adjustment:** Guitar Pickup Selector & Volume. Select the **middle** position (both pickups blend) on your Telecaster for classic clean rhythm quack. Roll guitar Volume to **7** to make it touch-sensitive.
- **Key interaction:** If you want a punchier, country-style clean, swap the compressor inline to the **1176** with medium-fast settings, or swap the TKIP cabinet IR to the **Marshall 4x12** for a bolder midrange focus.
- **Variations:** Push the TKIP Volume to **3.5** to introduce a tiny bit of edge-of-breakup color if the rhythm needs to bite harder in the mix.
