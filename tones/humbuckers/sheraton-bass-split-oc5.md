---
id: sheraton-bass-split-oc5
preset_name: "Sheraton OC-5 Bass Split"
created: 2026-06-06
updated: 2026-06-06
guitar: "Epiphone Sheraton II (humbuckers, neck position)"
target: "A polyphonic octave-split signal chain replicating the Boss OC-5 pedal range setting to direct the lower two strings (E and A) to a bass path."
tags: "jazz, hybrid, octave-split, bass, humbuckers, sheraton"
tone-king-channel: bypassed
amp: "Dream '65 (UADx) & Bass Amp Designer (Logic)"
status: initial
pickup_type: humbucker
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 4.5
    Treble: 4.0
    Middle: 7.0
    Bass: 4.5
    Bright: false
    Boost: false
  la2a:
    peak_reduction: 25.0
    gain: 40.0
    compress: true
  logic_eq:
    band1:
      on: true
      freq: 100.0
      slope: 18.0
    band4:
      on: true
      freq: 650.0
      gain: -1.5
      q: 1.5
  bass_eq:
    band8:
      on: true
      freq: 150.0
      slope: 48.0
  bass_pitch_shifter:
    semitones: -12
    cents: 0
    mix: 100
    mode: "Pitch Tracking"
    latency_comp: true
  bass_amp_designer:
    amp_model: "Flip Top"
    cabinet: "Flip Top 1x15"
    gain: 3.5
    master: 6.0
    bass: 6.5
    mids: 5.5
    treble: 3.0
    blend: 50.0
---

# Sheraton OC-5 Bass Split

## Target Sound

This toneprint mimics the behavior of a Boss OC-5 polyphonic octave pedal set to only process the lowest notes. By filtering the signal path, we isolate the fundamental frequencies of the low E and A strings (below 150 Hz) and pitch-shift them down a full octave. The shifted signal runs into a warm, vintage bass amp model, while the rest of the guitar signal remains clean, warm, and untouched. 

This creates a highly convincing "hybrid" instrument, allowing you to walk bass lines on the lower strings while playing chords and melodies on the upper strings, with no glitching or muddy octave artifacts on your high voicings.

---

## Logic Routing Setup

This setup uses two physical Audio Tracks in Logic Pro routed to the same physical interface channel to allow low-latency live monitoring.

### Step 1 — Create and Configure the "Guitar Track"

1. Create a new Audio Track in Logic (`Option-Command-A`).
2. Rename the track to **"Guitar Track"**.
3. Set its input to **Input 1** (or whichever physical input your guitar is plugged into on the iD14).
4. Add the plugins (detailed below) to its inserts:
   - **Insert 1**: Channel EQ (HPF at 100 Hz to clear space for the bass).
   - **Insert 2**: Dream '65 Amp (UADx) (classic clean jazz platform).
   - **Insert 3**: Teletronix LA-2A Tube Compressor (UADx) (smooth dynamics).
5. Set the fader to **0 dB**.

### Step 2 — Create and Configure the "Bass Track"

1. Create a second Audio Track.
2. Rename it to **"Bass Track"**.
3. Set its input to the **same physical channel** (Input 1). Logic allows multiple tracks to monitor the same physical input simultaneously.
4. Add the plugins (detailed below) to its inserts:
   - **Insert 1**: Channel EQ (steep LPF at 150 Hz to act as the "Range" filter).
   - **Insert 2**: Logic Pitch Shifter (set to -12 semitones, 100% wet).
   - **Insert 3**: Bass Amp Designer (Flip Top B-15 model + 1x15 cab).
5. Set the fader starting point to **-4 dB** to let it sit supportively underneath the guitar.

### Step 3 — Monitor & Group

1. Select both tracks in the Track Header, right-click, and choose **Create Track Stack** (`Shift-Command-D`).
2. Select **Summing Stack** and click Create.
3. Rename the stack to **"Hybrid Guitar/Bass"**. This master channel allows you to control the overall volume or add master EQ/bus compression.
4. Click the **Input Monitoring (I)** or **Record Enable (R)** buttons on **both** child tracks so you can hear both paths in real time as you play.

---

## Signal Chain

### 1. Hardware Front-End (Physical Input)

- **Default**: Guitar direct into **Audient iD14 Input 1** (bypassing the Tone King Imperial Preamp entirely for maximum transparency).
- **Optional Tone King Preamp Route**: If you route through the physical Tone King Preamp to add its Rhythm channel scooped flavor as a foundation, use these settings:
  
| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Fender Blackface clean character |
| Volume | 2.5 | Low level to keep signal transparent |
| Attenuation | 5.0 | Unity output |
| Bass / Treble | 5.0 (noon) | Flat response |
| IR | Bypassed | Essential since Logic handles cab emulations |
| Effects | Off | — |

---

### 2. "Guitar Track" Inserts

#### I. Channel EQ (High-Pass & Warmth)

| Band | Setting | Purpose |
|------|---------|---------|
| Band 1 (HPF) | 100 Hz, Slope 18 dB/oct | Removes sub-bass muddy buildup |
| Band 4 (Bell) | 650 Hz, −1.5 dB, Q 1.5 | Smoothes out Sheraton mid-range honk |

#### II. Dream '65 Amp (UADx)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 4.5 | Warm, clean preamp response |
| Treble | 4.0 | Smooth top-end |
| Middle | 7.0 | Fills the Fender mid-scoop (Jazz Middle Rule) |
| Bass | 4.5 | Balanced low-end |
| Bright / Boost | Off | Keeps the tone round and clean |
| Cab / Mic | GB25 / Ribbon 121 | Warm speaker voicing with ribbon mic warmth |

#### III. LA-2A Tube Compressor (UADx)

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 25 | Light compression to smooth out pick dynamics |
| Gain | 40 | Restores level post-compression |
| Compress/Limit | Compress | Standard optical compression curves |

---

### 3. "Bass Track" Inserts

#### I. Channel EQ (Low-Pass Filter)

| Band | Setting | Purpose |
|------|---------|---------|
| Band 8 (LPF) | 150 Hz, Slope 48 dB/oct | Steep cutoff to ensure only E & A string fundamentals reach the Pitch Shifter |

#### II. Pitch Shifter (Logic Pro Native)

| Control | Setting | Purpose |
|---------|---------|---------|
| Semitones | -12 | Pitch shifted down one octave |
| Cents | 0 | Flat |
| Mix | 100% (Wet) | Octave-only signal output |
| Timing / Mode | Pitch Tracking | Optimized monophonic algorithm |
| Latency Comp | ON | Keeps phase aligned |

#### III. Bass Amp Designer (Logic Pro Native)

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | Flip Top | Ampeg B-15 Portaflex emulation for vintage roundness |
| Cabinet | Flip Top 1x15 | Warm, resonant single-15 speaker voicing |
| Mic | Ribbon 121 | Captures smooth, non-fizzy low end |
| Gain | 3.5 | Clean tube preamp behavior |
| Master | 6.0 | Warm output transformer saturation |
| Bass | 6.5 | Boosts deep bass fundamentals |
| Mids | 5.5 | Keeps low mids present but clear |
| Treble | 3.0 | Rolls off artificial high-frequency tracking harmonics |
| Blend | 50% Amp / 50% D.I. | Blends D.I. definition with amp character |

---

## Starting Point Guide

- **First adjustment**: The fader level of the **"Bass Track"** relative to the **"Guitar Track"** (start at -4 dB and adjust to taste). It should support, not overwhelm.
- **Key interaction**: The steepness and frequency of the LPF on the Bass Track's Channel EQ. If you find the D string (146.8 Hz) is triggering the pitch shifter, lower the LPF frequency to **135 Hz** or increase the slope. If your low A string (110 Hz) feels too weak, raise it to **165 Hz**.
- **Variations**:
  - *Electric Bass Overdrive*: Switch the Bass Amp Designer to **Classic** (Ampeg SVT) and push the Gain to **5.5** for a slightly gritty, aggressive bass line.

---

## Feedback History

### 2026-06-06 — initial
Initial dual-track hybrid design. Designed for Sheraton humbuckers. Features a default direct-input path to the iD14, steep LPF filtering on the bass path, Logic's Pitch Shifter in Pitch Tracking mode, and Bass Amp Designer (B-15 model) blended with D.I.
