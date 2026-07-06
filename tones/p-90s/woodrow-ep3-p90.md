---
amp: "Woodrow '55 (UADx)"
created: 2026-06-04
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
id: woodrow-ep3-p90
pickup_type: p-90
preset_name: "Woodrow EP3 P90"
preset_overrides:
  cab_and_mic: 32
  output: 3.84
  room: 20.0
  woodrow_boost_amount: 3.03
  woodrow_boost_type: 2
status: tested
tags: "tweed, woodrow, blues, classic-rock, framus, p-90, compressed, mid-forward, ep-iii"
target: 'Tweed Deluxe "Sweet Spot" paired with the EP-III preamp booster: thick, warm, and highly touch-sensitive tone optimized to keep the P-90 neck pickup clear yet vocal.'
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
    Boost: true
    Treble: 5.18
    Volume: 3.15
    Volume (Mic): 1.93
  galaxy:
    echo_rate: 6.5
    echo_volume: 2.0
    feedback: 1.5
    head_select: 1
    tape_age: New
  la2a:
    gain: 25.0
    peak_reduction: 30.0
---

# Woodrow EP-III Sweet Spot (P-90)

## Target Sound

This toneprint is reverse-engineered from Mike's customized Woodrow preset, designed to solve the classic Tweed Deluxe dilemma with hot pickups. 

Because P-90 neck pickups have a high output with thick low-mids, they easily push a jumped Tweed Deluxe (UADx Woodrow '55) into premature compression and muddy bass collapse ("farting out"). 

This preset solves this through two main techniques:
1. **EP-III Pre-Saturation:** Engaging the virtual EP-III tape preamp booster (Boost Type 2 at 3.0) colors the signal with tape warmth and soft-clipping, rounding off the harsh transients of swamp ash/roundwounds and adding sustain before the signal even hits the amp's preamp.
2. **Asymmetric Channel Blending:** Rolling the bass-heavy Mic channel back to **1.93** and leaning on the brighter Instrument channel at **3.15** cleans up the low-end mud, providing a vocal, throat-like midrange chime that cleans up beautifully with light picking and growls when you dig in.

This raw Tweed tone is paired with a subtle tape slapback and a fast LA-2A Gray compressor to keep the final dynamics in check.

---

## Signal Chain

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

Plugging your Framus P-90 neck pickup directly into the high-headroom JFET instrument input on the front of the interface. This bypasses any external preamp coloration and allows the raw signal to interact dynamically with the Woodrow '55 engine.

| Component / Control | Setting | Purpose |
|---------------------|---------|---------|
| **Guitar Input** | JFET Instrument Input (DI) | Discretely voiced JFET stage adds subtle harmonic warmth |
| **Preamp Gain** | Set to target peaks around −18 dBFS | Target input level for Logic |
| **Tone King Imperial** | **Bypassed** | Bypassed entirely |


### 2. Guitar Track → UADx Woodrow '55 (PGS Container)

#### Amp Settings
Both Volume channels are run simultaneously above 0 to enable the hardwired "jumped" configuration.

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume (Inst) | **3.15** | Primary bite and gain; drives the preamp tubes into their sweet spot |
| Volume (Mic) | **1.93** | Rolled back to prevent hot P-90 neck bass from muddying |
| Tone | **5.18** | Interactive gain and treble contour |
| Boost (EP-III) | **ACTIVE** | **Type 2 (EP-III)**; adds vintage tape preamp coloration and fatness |
| Boost Amount | **3.03** | Moderate boost; smooths transients and thickens notes |
| Input | **High (Input 1)** | Sets primary gain stage |
| Room | **20%** | Blends the speaker mics in a tighter, drier acoustic space |
| Cabinet | **Index 32** | Custom speaker/mic combo providing mid-forward clarity |
| Output | **3.84** | **Padded down** to compensate for the massive gain boost of the EP-III preamp |

---

#### Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

### 3. UADx Galaxy Tape Echo — subtle depth

The tape saturation complements the amp's vocal midrange, and a subtle slapback adds classic space.

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 1 | Single head for focused slapback |
| Echo Rate | 6.5 | **Clockwise = Shorter.** ~100ms on Head 1 for classic depth |
| Feedback | 1.5 | Set low for essentially a single ghost repeat |
| Echo Volume | 2.0 | Supportive; a subtle "shadow" behind the note |
| Tape Age | New | Keeps the repeats clean and distinct |

---

### 4. UADx LA-2A Silver Compressor — post-amp glue

Because the Woodrow is already compressing heavily in its virtual power tubes, we use the Silver LA-2A (which has the fastest response in the collection) very lightly, just to catch any stray peaks and glue the tape echo to the amp decay without introducing sluggish recovery.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | **30** | Slightly firmer squeeze; catches peaks and glues the sound |
| Gain | **25** | Makeup gain |
| Mode | Compress | Gentle optical compression |

---

## Starting Point Guide

- **Clean-to-Grit Dynamic Test:** Set the Framus to the **Neck pickup**. Play a sustained chord softly—it should sound warm, woody, and clean. Now, dig in hard on a double-stop. The notes should bloom into a vocal, fuzzy hair. 
- **Headroom Adjustment:** If the P-90 neck is still breaking up too quickly or compressing too heavily for your taste, switch the plug-in's **Input setting from 1 (High) to 2 (Low)**. This pads the input by 6dB, instantly restoring clean headroom and making the breakup transition much subtler.
- **Taming the Low E:** If the low strings sound mushy, roll the **Volume (Mic)** down further to **1.5** while keeping the Instrument channel at **3.15**.

---

## Feedback History

### 2026-06-04 — reverse-engineered
Reverse-engineered from Mike's saved session preset "TP Input - P90 Woodrow". Status set to `tested`. Adds the EP-III tape booster to add pre-saturation warmth, leans heavily on the Instrument channel (3.15) over the Mic channel (1.93) to keep P-90 neck clarity, and pads the output to 3.84 to maintain a steady -12 dBFS output level.
