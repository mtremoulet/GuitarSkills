---
id: tkip-strat-funky-rhythm
preset_name: "TKIP Strat Funky Rhythm"
created: 2026-06-06
updated: 2026-06-06
guitar: "Squier Stratocaster"
target: "A bright, punchy, percussive funk rhythm tone featuring classic Stratocaster quack and fast FET compression."
tags: "funk, rhythm, single-coil, stratocaster, clean, punchy"
tone-king-channel: rhythm
amp: "Tone King Imperial Preamp (Hardware)"
status: initial
pickup_type: single-coil
preset_data:
  amp_platform: hardware
  amp_settings:
    Channel: Rhythm
    Volume: 4.0
    Attenuation: 5.0
    Bass: 5.0
    Treble: 6.0
    Reverb: Off
    Tremolo: Off
    IR: Active (Vox AC30 2x12 - OH 212 Class A Blue)
  1176:
    input: 28.0
    output: 22.0
    ratio: 4.0
    attack: 6.0
    release: 6.0
  studio_d_chorus:
    mode: 1
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 12.0}
    band4: {on: true, freq: 400.0, gain: -1.5, q: 1.2}
    band6: {on: true, freq: 3000.0, gain: 1.5, q: 1.0}
---

# TKIP Strat Funky Rhythm

## Target Sound
A bright, percussive, and tight funk rhythm tone optimized for a Stratocaster's bridge + middle pickup blend (Position 4 "quack"). The Tone King Rhythm channel is pushed slightly to Volume 4.0 to add a touch of warm blackface harmonic richness without distorting. The built-in Vox AC30 2x12 cabinet IR (OH 212 Class A Blue) is active to provide high-end chime and bite. Logic processing features the UADx 1176LN Compressor set with fast attack and release to squash peaks and deliver that signature rubbery, percussive funk "pop" on chord strums. A wide, subtle chorus adds stereo width.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
Provides the clean blackface base and chimey Vox cabinet simulation.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Clean blackface voicing, excellent clean platform |
| Volume | 4.0 | Slightly pushed clean to add body and compression |
| Attenuation | 5.0 | Unity/moderate output |
| Bass | 5.0 (noon) | Flat response to keep the low end tight for funk rhythm |
| Treble | 6.0 | Slightly elevated treble for string bite and sparkle |
| Reverb | Off | Handled in Logic sends |
| Tremolo | Off | Disabled |
| IR | Active (Vox AC30 2x12 - OH 212 Class A Blue) | Vox 2x12 chime, provides the bright top-end sparkle |

### 2. UADx 1176LN Rev E Compressor — percussive FET compression
Placed inline in Logic to squeeze transients and deliver the classic funk percussive attack.

| Control | Setting | Purpose |
|---------|---------|---------|
| Input | 28.0 | Moderate drive to trigger consistent compression on strums |
| Output | 22.0 | Makeup gain |
| Attack | 6.0 (Fast) | Clamps down quickly on the pick attack for that percussive "pop" |
| Release | 6.0 (Fast) | Recovers quickly to avoid pumping on fast 16th-note patterns |
| Ratio | 4:1 | Standard compression ratio |
| Meter | GR | Target 3–6 dB of gain reduction during rhythmic scratching |

### 3. Logic Channel EQ — corrective pocket carving
Placed after the compressor to keep the rhythm tracks sitting perfectly in the mix.

| Control | Setting | Purpose |
|---------|---------|---------|
| Band 1 (High Pass) | On — 80.0 Hz, 12 dB/oct | Removes unnecessary sub-bass rumble |
| Band 4 (Peak) | On — 400.0 Hz, −1.5 dB, Q: 1.2 | Scoops out boxy midrange to make room for bass/keys |
| Band 6 (Peak) | On — 3.0 kHz, +1.5 dB, Q: 1.0 | Pushes high-mid definition for chord articulation |

### 4. UADx Studio D Chorus — stereophonic width
Adds wide, subtle modulation to make the rhythm guitar sound huge in the stereo field without pitch warble.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Button 1 (Active) | Subtle, classic spatial chorus enhancement |
| Mix | 100% (Default) | Fully wet/dry hardware blend |

### 5. Hitsville Reverb Chambers (Bus 3 Send) — splashy ambience
Set on Bus 3 at **100% Wet** (Wet Solo ON) for a bright, percussive room sound.

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −16.0 dB | Kept low to keep the funk rhythm tight and dry |
| Chamber | Chamber 1 | Small room/chamber for a tight acoustic footprint |
| Mix | 1.0 (100% Wet) | Aux bus blend |
| Decay | 1.2 seconds | Short decay to prevent muddying fast grooves |
| Pre-Delay | 10 ms | Close space simulation |

---

## Starting Point Guide
- **First adjustment:** Guitar Pickup Selector. Select the **bridge + middle** pickup blend (Position 4) on your Strat to maximize the percussive "quack." Keep guitar volume at **10** for maximum funk pop.
- **Key interaction:** The 1176 Attack setting is critical. If the chord scratches feel too compressed or "choked," roll Attack back toward **4.0** to let more of the natural pick snap through.
- **Variations:** Engage a subtle tempo-sync'd delay on a send (e.g. 1/16th note delay) to create Nile Rodgers-style cascading rhythm patterns.
