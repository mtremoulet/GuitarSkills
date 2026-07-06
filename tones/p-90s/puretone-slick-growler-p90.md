---
id: "puretone-slick-growler-p90"
preset_name: "Puretone Slick Growler P90"
created: "2026-06-02"
updated: "2026-06-02"
guitar: "Framus Earl Slick (DiMarzio P-90s) / Gibson LP Studio (490 series)"
target: 'Organic, touch-sensitive edge-of-breakup grit using the Puretone''s tone stack bypass, delivering a roaring, singing vintage lead and woody chord melody.'
tags: "boutique, edge-of-breakup, grit, p-90, framus, les-paul, humbucker, blues, rock"
tone-king-channel: bypassed
amp: "H&K Puretone (Nembrini)"
status: initial
pickup_type: p-90
preset_data:
  nembrini_puretone:
    Volume: 6.5
    Growl: 5.0
    Bass: 5.0
    Mid: 5.0
    Treble: 5.0
    Tone: 5.0
    OutLevel: -6.0
  la2a:
    peak_reduction: 35
    gain: 18
  hitsville:
    mix: 1.0
    decay: 2.5
    pre_delay: 8.0
---

# Puretone Slick Growler — P-90s & Humbuckers

## Target Sound

This toneprint is designed for Mike's **Framus Earl Slick Artist Series** (featuring DiMarzio soapbar P-90s) and also functions beautifully as a hot blues-jazz overdrive for the **Gibson Les Paul Studio** (490R/490T humbuckers).

The sonic goal is an organic, highly expressive, touch-sensitive edge-of-breakup grit modeled after:
- **Expressive Vocal Blues-Jazz**: Singing single-note lines and double-stops reminiscent of Larry Carlton, Robben Ford, or blues-period acoustic-electric hybrids.
- **Dynamic Fretboard Dexterity**: Translating the physical speed and pressure of your fingers. When you play lightly, the tone is warm and woody; when you dig in, it growls with natural power-tube saturation.
- **Classic Rock & Soul Crunch**: A thick, wide-range crunch that cleans up cleanly via your guitar's volume knob.

By setting the **Growl** knob to **5.0**, we partially bypass the passive EQ circuit. This unchains the H&K Puretone's raw midrange and gain, creating a thick, harmonically rich, and touch-sensitive drive that captures the tactile feedback of shifting positions on a violin—a literal, physical connection between your picking velocity and the amp's virtual tube sag.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. Nembrini H&K Puretone
The amplifier platform. The Growl knob is pushed to 5.0 to engage the tone-stack bypass, delivering roaring midrange crunch.

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 6.5 | Drives the virtual preamp tubes into soft compression and grit |
| Growl | 5.0 | **Critical**: Bypasses 50% of the EQ stack to flood the circuit with rich midrange gain |
| Bass | 5.0 | Kept neutral (Growl 5.0 overrides extreme EQ, but keep flat for standard voice) |
| Middle | 5.0 | Kept neutral |
| Treble | 5.0 | Kept neutral |
| Tone | 5.0 | Neutral power-amp contour |
| OutLevel | −6.0 | **Critical**: More attenuation needed here due to the hot Growl gain boost |

**Cabinet & Microphone Selection**:
*   **Cabinet**: HK **2x12 V30** (delivers thick, present mids and a tight rock/blues low end)
*   **Microphone**: Blend of **Dynamic 57** (on-axis, for bite and cut) and **Ribbon 121** (off-axis, for warm, fat body)

---

### 3. UADx LA-2A Silver Compressor
Applied as an insert to act as a leveling amplifier, smooth out the P-90 attack transients, and provide singing, violin-like sustain.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Compress | Standard 3:1 opto-compression |
| Peak Reduction | 35 | Targets ~2–3 dB of optical compression on solid strums for singing lead lines |
| Gain | 18 | Makeup gain adjusted to drive output to target |

---

### 4. UADx Hitsville Reverb Chambers
Reverb applied via parallel Send on Bus 3.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | Chamber 2648 | Motown Room: Echo-like, parallel surfaces; cuts beautifully for lead lines |
| Mix | Wet Solo (100%) | Parallel routing |
| Decay | 9:00 (2.5s) | Classic room decay that gives the overdrive a live, spatial "in-the-room" feel |
| Pre-Delay | 8 ms | Standard separation |

**Logic Fader Blends**:
*   **Reverb Bus Send**: −18 dB
*   **Reverb Bus Fader**: −12 dB

---

## Dial-in Workflow & Tips

- **Guitar Controls**: Select the **Neck Pickup** (or **Middle blend**) on your Framus or Les Paul. Roll the guitar volume knob back to **6** to play clean, woody rhythm/chord melodies. Roll the volume up to **8.5 or 9** to push the virtual tubes into a roaring, vocal overdrive.
- **Violin-like Expressiveness**: Because of the high Growl setting, the amp reacts intensely to pick attack and vibrato. Experiment with left-hand finger vibrato and varying your pick stroke angles to hear how the harmonics shift and sing.
- **DAW Clip Management**: Pushing Growl to 5.0 significantly boosts the overall output. Ensure the Nembrini **OutLevel** is pulled back to **-6.0 dB** or lower so that hard strums do not clip the stereo bus.

---

## Feedback History

### 2026-06-02 — initial
Toneprint created for P-90 and humbucker edge-of-breakup grit. Configured with a high Growl factor (5.0) for a dynamic, touch-sensitive crunch that cleans up beautifully on the guitar volume knob.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
