---
amp: "Jazz Chorus"
created: 2026-05-09
guitar: "Epiphone Sheraton (humbuckers)"
id: jc120-pristine-jazz-clean
pickup_type: humbucker
status: initial
tags: "jazz, clean, solid-state, chorus, jc120, nembrini, pristine"
target: "Pristine, glassy solid-state jazz clean through the Nembrini JC120; focused"
tone-king-channel: bypassed
updated: 2026-05-09
preset_data:
  nembrini_jc120:
    Bass: 5.0
    Distortion: 0.0
    Middle: 7.5
    Reverb: 0.0
    Treble: 4.0
    Volume: 3.0
---

# JC120 Pristine Jazz Clean

## Target Sound
The goal is the "glassy" but warm clean tone synonymous with the Roland JC-120. Unlike tube amps, this doesn't "bloom" or "sag"—it remains perfectly articulate and frequency-rich from the lowest note to the highest. We use the **Epiphone Sheraton** humbuckers to provide the body, while the JC120 provides the hi-fi definition. This is the "blank canvas" for modern jazz and fusion.

**Gain Staging Focus**: Per Mike's feedback, this toneprint uses explicit Input/Output trims within the Nembrini plugin to prevent clipping the DAW and the THR10ii monitoring path.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. Nembrini Jazz Chorus Solid State

#### Gain Staging & Input/Output
*These settings are critical for preventing digital harshness in solid-state emulations.*

| Control | Setting | Purpose |
|---------|---------|---------|
| Input Slider | −6.0 dB | Padding the input to ensure humbuckers don't clip the virtual preamp |
| Output Slider | −8.0 dB | Final trim to protect the THR10ii monitoring path |

#### Amplifier Section
| Control | Setting | Purpose |
|---------|---------|---------|
| Bright | OFF | Warmth is prioritized over "snap" for jazz |
| Volume | 3.0 | High headroom; stay well within the clean zone |
| Middle | 7.5 | **Jazz Middle Rule**: Fills in the midrange for a vocal character |
| Treble | 4.0 | Slightly rolled off to soften the solid-state "edge" |
| Bass | 5.0 | Balanced low end |
| Distortion | 0.0 | OFF |
| Reverb | 0.0 | OFF (using Capitol Chambers on a Bus) |
| Mode | OFF / CHORUS | Set to OFF for pure clean; flip to CHORUS for the "Space Chorus" |

#### Cabinet & Mic Section
| Control | Setting | Purpose |
|---------|---------|---------|
| Cabinet | RLD 2x12 JC120 | The iconic matching cab for this amp |
| Microphone | Ribbon 121 | **Dark/Warm choice**: Rounds off the high-end transients |
| Position | 0.45 | Off-center for smoothness |
| Distance | 0.25 | Natural air without becoming "roomy" |

---

### Send from Guitar Track → Bus 3 (Reverb): −15 dB

---

### Reverb Aux — Capitol Chambers (Lush Space)

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | Chamber 4 | Large, lush room sound |
| Mic | Condenser | Maximum detail and "air" |
| Mix | 100% | **Bus-First Standard**: Full wet on the Bus |
| Wet Solo | ON | Fader controls the mix |

---

## Starting Point Guide

- **Finding the "Edge"**: If the tone feels too "sterile," try switching the **Bright** switch to ON, but roll your guitar's tone knob back to 6. This creates a "hi-fi" dark tone with more harmonic content.
- **The Chorus Interaction**: When you flip the Mode to **CHORUS**, the JC120 splits the signal internally. It may feel slightly "wider" but quieter—adjust the plugin's Output slider by +1 or +2 dB if you intend to leave the chorus on full-time.
- **Midrange Sculpting**: If the Sheraton sounds too "boxy," pull the **Middle** back to 6.0. If it feels like it's getting lost in a backing track, push it to 8.0.

---

## Feedback History

### 2026-05-09 — initial
Designed to address Mike's request for a JC120 jazz tone with specific focus on Nembrini gain staging. Uses the "Jazz Middle" rule and Ribbon 121 mic choice to keep the solid-state character warm. Follows the "Bus-First" standard for spatial effects to avoid the sensitive UADx Mix dials.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
