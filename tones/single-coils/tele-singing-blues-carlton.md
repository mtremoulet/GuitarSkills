---
amp: "Enigmatic '82 (UADx)"
created: 2026-05-02
guitar: "Fender Player II Telecaster (Neck position, Flatwounds/Pure Nickels)"
id: tele-singing-blues-carlton
pickup_type: single-coil
status: initial
tags: "jazz, blues, telecaster, carlton, dumble, sustain"
target: "\\"Larry Carlton \\\"Singing Blues-Jazz\\\" \u2014 Mellow chords with touch-sensitive,\"
tone-king-channel: bypassed
updated: 2026-06-28
preset_data:
  amp_platform: uad_paradise
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  amp_settings:
    Bass: 4
    Middle: 7
    Treble: 5
    Volume: 4.0
  galaxy:
    echo_rate: 120.0
    feedback: 1.0
  hitsville:
    mix: 0.08
  logic_compressor:
    makeup_gain: 6
    ratio: 4
---

# Singing Blues-Jazz (Larry Carlton Style)

## Target Sound
Targeting the "335 through an ODS" sound on a Telecaster platform. This tone is dual-natured: it stays warm and mellow for jazz chordal work when playing with a light touch or lower guitar volume, but "sings" and sustains with a characteristic mid-hump when you dig in for leads. It captures that touch-sensitive, "rubbery" overdrive that defines Larry Carlton's work with The Crusaders and on *Royal Scam*.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

**Pre-FX / Pre-Amp Stompbox Option**

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 2. UADx Enigmatic '82 Overdrive Special — the "Sing"

The heart of the tone. Set to the 'Suede' voicing for a warmer, rounder character that suits the Tele's neck pickup.

| Control | Setting | Purpose |
|---------|---------|---------|
| Voice | **Suede** | Warm, round boutique character |
| Volume | 4 | Input sensitivity |
| Overdrive | 6 | **Key control:** Engages the gain stage for touch-sensitive sustain |
| Ratio | 4 | Balances the clean and overdriven signals |
| Treble | 5 | Neutral |
| Middle | 7 | **Mid-hump:** Essential for the vocal Carlton lead sound |
| Bass | 4 | Keeps the low end tight |
| Cab | **GB25 / Ribbon 121** | Warm Greenback character with a smooth ribbon mic |

### 3. UADx 175-B Tube Compressor — harmonic glue

| Control | Setting | Purpose |
|---------|---------|---------|
| Input | 18 | Gentle tube saturation and compression |
| Output | 20 | Makeup gain |
| Attack/Release | Fast | Smooths out the transition from chords to singing leads |

### 4. UADx Galaxy Tape Echo — slapback depth

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | 1 | Single head echo |
| Echo Rate | ~120ms | Short slapback to add physical depth to lead lines |
| Feedback | 1 | Single repeat |
| Mix | 10% | Subtle; sits behind the note to add "3D" quality |

### 5. UADx Hitsville Reverb Chambers — studio space

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | 2648 | Brighter, more "echoey" chamber for a professional studio feel |
| Mix | 8% | Adds a sense of space without washing out the overdrive |

---

## Starting Point Guide

- **Touch Sensitivity**: This tone lives in your right hand. Play softly for warm jazz chords; dig in to trigger the "singing" sustain on lead notes.
- **Guitar Volume**: Roll back to **7–8** for a cleaner jazz sound. Push to **10** for the full Carlton lead bloom.
- **Mid-Bite**: If the leads aren't cutting through or don't feel "vocal" enough, increase the **Middle** control on the Enigmatic '82.

---

## Feedback History

### 2026-05-02 — initial
Built for the BRG Player II Telecaster. Uses Enigmatic '82 'Suede' voice for Dumble-style touch sensitivity. 175-B added for tube warmth and Galaxy Tape Echo for subtle slapback depth.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
