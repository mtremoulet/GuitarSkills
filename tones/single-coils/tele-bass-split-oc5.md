---
id: tele-bass-split-oc5
preset_name: "Telecaster OC-5 Bass Split"
created: 2026-06-06
updated: 2026-06-28
guitar: "Fender Player II Telecaster (single-coils, neck position)"
target: 'A polyphonic octave-split signal chain replicating the Boss OC-5 pedal range setting to direct the lower two strings (E and A) to a bass path.'
tags: "jazz, hybrid, octave-split, bass, single-coils, telecaster"
tone-king-channel: bypassed
amp: "Dream '65 (UADx), Bass Amp Designer (Logic)"
status: initial
pickup_type: single-coil
preset_data:
  amp_platform: uad_paradise
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  amp_settings:
    Volume: 5.0
    Treble: 3.5
    Middle: 7.5
    Bass: 5.0
    Bright: false
    Boost: false
  la2a:
    peak_reduction: 28.0
    gain: 42.0
    compress: true
  logic_eq:
    band1:
      on: true
      freq: 100.0
      slope: 18.0
    band7:
      on: true
      freq: 5000.0
      gain: -1.5
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
    gain: 3.8
    master: 6.0
    bass: 7.0
    mids: 5.5
    treble: 2.5
    blend: 60.0
---

# Telecaster OC-5 Bass Split

## Target Sound

This toneprint replicates the Boss OC-5 polyphonic range split specifically voiced for single-coil pickups (like a Telecaster neck pickup). Because single-coils have a leaner low-end fundamental and a brighter, punchier attack than humbuckers, the settings here are adjusted to compensate: the guitar amp platform is boosted in volume and mids to fill out the body, while the bass track gets a small gain and bass boost in the Bass Amp Designer (with a larger bias toward the cabinet blend) to ensure the octave-down notes sound round, thick, and supportive.

---

## Logic Routing Setup

This setup uses two physical Audio Tracks in Logic Pro routed to the same physical interface channel to allow low-latency live monitoring.

### Step 1 — Create and Configure the "Guitar Track"

1. Create a new Audio Track in Logic (`Option-Command-A`).
2. Rename the track to **"Guitar Track"**.
3. Set its input to **Input 1** (or whichever physical input your guitar is plugged into on the iD14).
4. Add the plugins (detailed below) to its inserts:
   - **Insert 1**: Channel EQ (HPF at 100 Hz to clear space for the bass, and a gentle high-cut filter for jazz warmth).
   - **Insert 2**: Dream '65 Amp (UADx) (classic clean jazz platform, voiced with extra mids).
   - **Insert 3**: Teletronix LA-2A Silver Compressor (UADx) (smooths pick dynamics).
5. Set the fader to **0 dB**.

### Step 2 — Create and Configure the "Bass Track"

1. Create a second Audio Track.
2. Rename it to **"Bass Track"**.
3. Set its input to the **same physical channel** (Input 1). Logic allows multiple tracks to monitor the same physical input simultaneously.
4. Add the plugins (detailed below) to its inserts:
   - **Insert 1**: Channel EQ (steep LPF at 150 Hz to act as the "Range" filter).
   - **Insert 2**: Logic Pitch Shifter (set to -12 semitones, 100% wet).
   - **Insert 3**: Bass Amp Designer (Flip Top B-15 model + 1x15 cab, voiced for extra low-end weight).
5. Set the fader starting point to **-3 dB** to let it sit supportively underneath the guitar (compensated for single-coil bass output).

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


### 2. "Guitar Track" Inserts

#### I. Channel EQ (High-Pass & Warmth)

| Band | Setting | Purpose |
|------|---------|---------|
| Band 1 (HPF) | 100 Hz, Slope 18 dB/oct | Removes sub-bass muddy buildup |
| Band 7 (Hi Shelf) | 5.0 kHz, −1.5 dB | Roll off excessive single-coil "air" (High-Cut Veil rule) |

#### II. Dream '65 Amp (UADx)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 5.0 | Raised slightly to compensate for single-coil output |
| Treble | 3.5 | Rolled back to tame single-coil bite |
| Middle | 7.5 | Extra mid-range boost to fill the single-coil body |
| Bass | 5.0 | Balanced low-end |
| Bright / Boost | Off | Keeps the tone round and clean |
| Cab / Mic | GB25 / Ribbon 121 | Warm speaker voicing with ribbon mic warmth |

#### III. LA-2A Silver Compressor (UADx)

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | 28 | Slight peak reduction increase to level out transient single-coil snap |
| Gain | 42 | Restores level post-compression |
| Mode | Compress | Standard optical compression curves |
| Emphasis / HF | ~75% (3:00) | Rolled back slightly to prevent single-coil low fundamental thump from over-compressing high strings |

---

#### IV. Pre-FX Option: Gold Overdrive

| Control | Setting | Purpose |
|---------|---------|---------|
| Pedal | **Gold Overdrive** | Transparent clean boost on hand |
| State | **Disabled** (Off) | Bypass by default; engage for clean solo boost or pushing front end |
| Gain | **0.0** | Zero added distortion; pure clean boost |
| Output | **7.5** | Pushes front end of amp for singing sustain and level lift |
| Treble | **4.5** | Slightly rounded high end for smooth boost response |

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
| Gain | 3.8 | Gain bumped slightly to drive the tube emulation with a leaner single-coil input |
| Master | 6.0 | Warm output transformer saturation |
| Bass | 7.0 | Extra bass boost to thicken the thin single-coil fundamental |
| Mids | 5.5 | Keeps low mids present but clear |
| Treble | 2.5 | Extra high-cut to eliminate single-coil treble bleed |
| Blend | 60% Amp / 40% D.I. | Larger bias toward the warm cabinet to add body |

---

## Starting Point Guide

- **First adjustment**: The fader level of the **"Bass Track"** relative to the **"Guitar Track"** (start at -3 dB and adjust to taste). 
- **Key interaction**: The steepness and frequency of the LPF on the Bass Track's Channel EQ. If you find the D string (146.8 Hz) is triggering the pitch shifter, lower the LPF frequency to **135 Hz** or increase the slope. If your low A string (110 Hz) feels too weak, raise it to **165 Hz**.
- **Variations**:
  - *Slightly Brighter Bass*: Increase the D.I. Blend in Bass Amp Designer to **50% Amp / 50% D.I.** for a tighter, more articulate bass attack.

---

## Feedback History

### 2026-06-06 — initial
Initial dual-track hybrid design. Voiced specifically for single-coil Telecaster pickups. Features a default direct-input path to the iD14, steep LPF filtering on the bass path, Logic's Pitch Shifter, and a warm B-15 Bass Amp Designer setup with boosted bass and gain parameters to compensate for single-coil leanness.
