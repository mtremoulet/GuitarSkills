---
id: "puretone-bossa-fingerstyle-sc"
preset_name: "Puretone Bossa Fingerstyle SC"
created: "2026-06-02"
updated: "2026-07-20"
guitar: "Fender Player II Telecaster (neck pickup) / Squier Stratocaster (neck/middle)"
target: 'Sparkling, pristine, touch-sensitive clean for bossa nova chord plucking and modern chillhop/folk fingerstyle.'
tags: "boutique, clean, sparkle, single-coil, telecaster, stratocaster, fingerstyle, bossa, chillhop"
tone-king-channel: bypassed
amp: "H&K Puretone (Nembrini)"
status: archived
pickup_type: single-coil
preset_data:
  nembrini_puretone:
    Volume: 4.5
    Growl: 2.0
    Bass: 5.5
    Mid: 4.5
    Treble: 6.0
    Tone: 5.0
    OutLevel: -2.0
    DelayPower: 0.0
    ReverbPower: 0.0
    Mix: 0.0
  la2a:
    peak_reduction: 20
    gain: 12
---

# Puretone Bossa Fingerstyle — Single-Coils

## Target Sound

This toneprint is designed for Mike's single-coil electrics: the **Fender Player II Telecaster** (using the neck pickup) and the SQ/E-Series **Squier Stratocaster** (using the neck-middle "quack" position).

The sonic goal is a hyper-responsive, shimmering, high-fidelity acoustic-like clean tone optimized for:
- **Bossa Nova & Latin Strumming**: The rapid thumb-bass and finger-plucked chord changes that require absolute clarity, fast transient recovery, and balanced frequency ranges.
- **Fingerstyle Folk & Acoustic-Electric Crossing**: Translating every subtle pluck of the fingers, keeping nail/flesh attack distinct and present.
- **Ambient Chillhop & Neo-Soul**: A pristine canvas for sparkling clean chord hierarchies.

In this toneprint, we run the **Nembrini Clon Minotaur** in front of the amp. The Clon is configured as a transparent, high-headroom boost—not a heavy distortion—which helps drive the H&K Puretone's virtual input tubes just enough to extract maximum touch sensitivity. We push the **Growl** knob on the Puretone to **2.0**, which introduces a very subtle, organic midrange thickness and dynamic density without sacrificing the sparkling treble and full-bodied bass EQ filters.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. Nembrini Clon Minotaur (Pedal Insert)
Loaded as an active stompbox plugin on the "Electric Dry" channel strip before the amp.

| Control | Setting | Purpose |
|---------|---------|---------|
| Gain | 1.5 | Minimal grit; acts primarily as a clean driver |
| Treble | 5.0 | Noon (neutral transparency) |
| Output | 6.0 | Pushes the virtual preamp stage of the H&K Puretone |

---

### 3. Nembrini H&K Puretone
The high-fidelity amplifier platform. A small amount of Growl is introduced to add body to the single-coils.

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 4.5 | Preamp gain pushed to the edge where harder plucks bloom beautifully |
| Growl | 2.0 | Introduces subtle midrange density while keeping the EQ stack highly active |
| Bass | 5.5 | Slight boost to add deep "acoustic" body and cabinet thumb-plucked resonance |
| Middle | 4.5 | Scooped slightly to let the high single-coil jangle and chime breathe |
| Treble | 6.0 | Boosted for sparkling, crisp top-end definition |
| Tone | 5.0 | Neutral |
| OutLevel | −4.0 | Post-amp fader trim to prevent digital clipping inside Logic |

**Cabinet & Microphone Selection**:
*   **Cabinet**: Divided 11's **1x12 Alnico Gold** (delivers sweet, glassy highs and open woodiness)
*   **Microphone**: **Ribbon 121** (on-axis, distance ~1.5 to smooth out the transients of single-coils)

---

### 4. UADx LA-2A Silver Compressor
Applied as an insert to tame the sudden spikes of fingerplucking and keep the overall dynamic sweep balanced.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Compress | Standard 3:1 opto-compression |
| Peak Reduction | 20 | Targets ~1 dB of peak leveling on hard plucks, preserving pick velocity |
| Gain | 12 | Makeup gain adjusted for natural session level |

---

### 5. UADx Capitol Chambers
Reverb applied via parallel Send on Bus 3.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | Chamber 2 | Glassy, highly three-dimensional room with exceptional stereo image |
| Mix | Wet Solo (100%) | Parallel routing |
| Decay | 1.8s | Clear room reflection that decays quickly enough to keep complex tempos dry |
| Pre-Delay | 10 ms | Short separation for immediate acoustic depth |

**Logic Fader Blends**:
*   **Reverb Bus Send**: −15 dB
*   **Reverb Bus Fader**: −10 dB

---

## Dial-in Workflow & Tips

- **Guitar Controls**: Select the **Neck Pickup** on your Telecaster (or **Position 4 [Neck + Middle]** on your Stratocaster). Keep the guitar volume wide open at **10** to feed the Clon Minotaur a full-fidelity signal, and set your guitar tone knob to **8.5** to retain all of the single-coil sparkle without harshness.
- **Plucking Technique**: Use the flesh of your fingers for a warm, pillowy bossa strum, or engage your nails for a sudden, cutting acoustic snap. The amp's slight Growl factor (2.0) and the Klon boost will translate this contrast with extreme expressiveness.
- **DAW Clip Management**: Since single-coils have rapid transient peaks, ensure your interface preamp gain is dialed so you peak at −18 dBFS before the signal hits the plugins. Adjust **OutLevel** on the Nembrini cabinet if necessary.

---

## Feedback History

### 2026-06-02 — initial
Toneprint created for single-coil bossa plucking and fingerstyle folk. Configured with a transparent Clon boost in front of a slightly growling H&K Puretone (Growl 2.0) and UAD dynamics.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
### 2026-07-20 — tested on Strat (quiet level + repeating delay bug identified)
Tested on Strat. Identified that Nembrini's internal FX rack (`DelayPower`) was defaulting to ON in the base XML template (`HK_Base.xml`), introducing an unrequested 477 ms repeating delay on top of the UAD Capitol Chambers bus. Updated `preset_data` to explicitly set `DelayPower: 0.0`, `ReverbPower: 0.0`, `Mix: 0.0` to bypass Nembrini internal FX. Also bumped `OutLevel` from −4.0 to −2.0 dB to address the low level on lower-output Strat single-coils.

