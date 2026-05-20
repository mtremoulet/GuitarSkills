---
id: sheraton-jazz-acoustic
created: 2026-04-30
updated: 2026-04-30
guitar: Epiphone Sheraton (humbuckers)
target: Warm clean jazz electric tone blended with an acoustic texture from Acoustic
  Voice Pro; reverb on a shared bus
tags: jazz, clean, warm, acoustic-blend, semi-hollow, humbuckers
tone-king-channel: rhythm
amp: Showtime '64
status: tested
pickup_type: humbucker
---

# Sheraton Jazz + Acoustic Blend

## Target Sound

A warm, even-keel jazz electric tone as the foundation, with a lower-level acoustic texture blended underneath it to add body and resonance. The Acoustic Voice Pro processes a parallel copy of the signal to approximate a mic'd acoustic coloring — it won't be a perfect acoustic (the Sheraton has magnetic humbuckers, not a piezo), but used at -8 dB or lower it becomes a supportive presence that thickens the fundamental without drawing attention to itself. Reverb is on a shared send bus, so both the electric and acoustic signals decay together into the same space.

---

## A Note on the Acoustic Voice Pro with Magnetic Pickups

Acoustic Voice Pro is designed for piezo pickup signals. A humbucker signal will not produce a convincing standalone acoustic emulation — but that's not the goal here. At -8 dB under the electric, the processed signal adds body, resonance, and a slightly different harmonic envelope that makes the whole sound feel richer. Think of it as adding a different kind of warmth, not replacing the electric identity.

---

## Logic Routing Setup

This tone requires three Aux channel strips fed from one Guitar Track. Here's how to build it step by step.

### Step 1 — Configure the Guitar Track

- Set your guitar audio track's output to **Bus 1** (click the Output selector in the channel strip I/O section and choose Bus 1)
- Leave the fader at 0 dB
- Add **no plugins** to this track — it's a pure signal router
- Rename the track "Guitar Input"

### Step 2 — Create Aux 1: "Electric Dry"

- Open the Mixer (X key or View > Show Mixer)
- Click the **+** button at the bottom left of the Mixer to add a new Aux channel strip, or use Options menu > Create New Auxiliary Channel Strip
- In the new Aux channel strip, set its **Input** (top of the strip) to **Bus 1**
- This Aux now receives everything that goes into Bus 1
- Rename it "Electric Dry"
- Add the plugins below (in order)
- Set Output: Stereo Out
- **Send**: click an empty Send slot, choose **Bus 3**, set send level to **−20 dB** (this feeds the reverb bus)

### Step 3 — Create Aux 2: "Acoustic"

- Add another Aux channel strip
- Set its **Input** to **Bus 1** as well — Logic correctly sends the same signal to both Aux 1 and Aux 2 simultaneously
- Rename it "Acoustic"
- Add Acoustic Voice Pro (plugin details below)
- Set Output: Stereo Out
- Set **fader to −8 dB** (this is the acoustic blend level — it sits below the electric signal)
- **Send**: Bus 3 at **−22 dB** (acoustic contributes slightly less reverb energy than the electric)

### Step 4 — Create Aux 3: "Reverb Bus"

- Add one more Aux channel strip
- Set its **Input** to **Bus 3**
- Rename it "Reverb Bus"
- Add Capitol Chambers (plugin details below)
- Set Output: Stereo Out
- Set fader to **−12 dB** (starting point — adjust to taste)

### Step 5 — Blend and Adjust

- To change the acoustic/electric balance: move the "Acoustic" Aux fader (−8 dB is a starting point; try −6 to −12 dB)
- To change overall reverb: move the "Reverb Bus" Aux fader, or adjust the send levels from Aux 1 and Aux 2
- To change how much reverb the acoustic vs. electric gets independently: adjust the individual Bus 3 send levels on each Aux

---

## Signal Chain

### Tone King Imperial Preamp — hardware front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Blackface American clean character |
| Volume | 3 | Low — keep the preamp from coloring the signal too much before Acoustic Voice Pro |
| Attenuation | 5 | Moderate output level to interface |
| Bass | 5 (noon) | Flat |
| Treble | 4 | Slightly warm — removes a touch of hardness from the humbucker top end |
| Reverb | Off | Reverb is on the bus |
| Tremolo | Off | — |
| IR | Bypassed | Both signal paths will be processed without cab IR baked in; this keeps the acoustic path cleaner |

---

### Guitar Track → Bus 1

No plugins. Signal router only.

---

### Aux 1: "Electric Dry" — warm jazz electric chain

#### 1. Channel EQ

| Band | Setting | Purpose |
|------|---------|---------|
| Band 1 (HPF) | 80 Hz, Slope 24 dB/oct | Remove low rumble and resonance below the guitar's useful range |
| Band 4 (Bell) | 650 Hz, −2 dB, Q 1.5 | Soften the honky upper-midrange common in semi-hollow humbuckers |
| Band 7 (Hi Shelf) | 5 kHz, −1.5 dB | Gentle top-end rolloff for jazz warmth — takes the edge off without going dull |

*Note: For Band 1 HPF, the "Gain/Slope" field controls filter steepness, not boost — 24 dB/oct gives a clean, modern roll-off.*

#### 2. LA-2A Tube Compressor

| Control | Setting | Purpose |
|---------|---------|---------|
| Compress/Limit | Compress (~3:1) | Gentle optical compression — natural, musical response |
| Peak Reduction | 28 | Light compression; just evening out the dynamics of chord playing |
| Gain | 45 | Makeup gain to restore level post-compression |
| Meter | Gain Reduction | Shows you how much the compressor is working |

*The T4 optical response suits jazz well: it doesn't clamp transients like an 1176 would. You want the pick attack to come through — the compressor smooths out the sustain tail, not the attack.*

#### 3. UA 610-B Tube Preamp & EQ

| Control | Setting | Purpose |
|---------|---------|---------|
| Input Select | Line | Guitar from Logic is already at line level |
| Input Gain | 0 dB | No additional tube gain at the input stage — keep clean |
| LO Shelf | 200 Hz, +1.5 dB | Add a small amount of low-mid body — the jazz warmth that humbuckers do well |
| HI Shelf | 10 kHz, −3 dB | Significant high-frequency roll-off — the single biggest thing that makes it sound like jazz, not rock |
| Level | 5.0 (on 0–10 dial) | Moderate output tube coloring — adds even harmonics and warmth without audible saturation |
| Output | Adjust to unity | Trim until the Aux 1 fader sits at 0 dB without clipping |

*The 610-B's EQ interacts with the output tube stage — that HI Shelf cut at 10 kHz isn't just EQ, it also changes how the tube saturates. This is what makes the 610-B sound like vintage warmth rather than a digital shelf.*

**Send from Aux 1 → Bus 3: −20 dB**

---

### Aux 2: "Acoustic" — Acoustic Voice Pro blend

**Aux Fader: −8 dB** (starting point — this is your primary blend knob for the acoustic texture)

#### Acoustic Voice Pro

| Section | Setting | Notes |
|---------|---------|-------|
| Input Mode | Humbucker | Critical — must match pickup type. The Sheraton has humbuckers; this optimizes the body modeling processing for that pickup character. |
| Body Model | GIB 00 (Gibson L-00) — first choice; TAY 814 (Taylor 814ce) — second | GIB 00: small parlor body, warm low-mids, intimate — adds body without projecting an acoustic sound. TAY 814: more balanced/neutral if GIB 00 feels too warm. Avoid dreadnoughts/jumbos (HD28V, GUI 140, LAND 80) — too much competing low end. |
| Microphone | CONDENSER 414 (AKG C414) | Open and polished — most neutral character for blending |
| Mic Position | Soundhole area (center of position range) | Balanced warmth and body |
| Mic Distance | 40–50% | Moderate — not too near-field |
| Mixer Blend | Start at 100% (full acoustic modeling) | This is the primary dry/wet for the acoustic model — pull toward 50% if the acoustic character is too strong |
| DI Preamp | Switch: ON; Notch: sweep to ~3.5 kHz; Blend: 60%; Gain: 0; Output: 0 | Use the DI Preamp's built-in Notch control (designed for resonance removal) rather than the EQ. Sweep the Notch to find and notch the nasal frequency your humbucker activates in the chosen body model. |
| Compressor (Stomp) | Switch: OFF | Not needed — compression is handled by LA-2A on the Electric dry bus |
| EQ (Graphic EQ view) | HP filter ~100 Hz active; remaining bands flat | High-pass only — low-end cleanup. Let the DI Preamp Notch handle the resonance removal. |
| FX (Delay/Reverb/Mod) | All Power: OFF | Reverb is on the shared bus |
| IR Loader | Bypass (start here; experiment with factory IRs later) | Start clean, add an IR only if the tone feels too thin |

**Send from Aux 2 → Bus 3: −22 dB**

---

### Aux 3: "Reverb Bus" — Capitol Chambers

**Aux Fader: −12 dB** (adjust to taste — this is your overall reverb return level)

Capitol Chambers must be in **Wet Solo: ON** when on an aux return bus. The Mix knob has no effect when Wet Solo is active.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | 4 (Altec A7) | Most balanced sound, shortest natural decay — versatile and clean |
| Microphones | Altec 21D | Vintage character, colored in the classic way — matches jazz recording aesthetics |
| Microphones Position | 70% | Slightly pulled back from max — adds a touch of room character without feeling too close |
| Predelay | 20 ms | Separates the reverb tail from the dry signal; gives the note time to speak before decay begins |
| Decay | Counter-clockwise to ~1.8 sec | Short-ish decay for jazz — intimate, not cathedral |
| Filter | 200 Hz | Cut low-end muddiness from the reverb return — important with humbuckers |
| EQ Bass | 0 dB | Flat |
| EQ Mid | −1 dB | Gently smooth the reverb's midrange — keeps it from sounding boxy |
| EQ Treble | −1.5 dB | Remove reverb brightness; keeps the jazz warmth consistent |
| Width | 80% | Nearly full stereo — gives the reverb a natural open feel |
| Wet Solo | ON | Required for aux bus routing — disables the dry signal in the plugin output |
| Power | ON | — |

*Important: Mix at noon on Capitol Chambers ≈ 15%, NOT 50%. With Wet Solo on, Mix has no effect — the aux fader and send levels control everything.*

---

## Starting Point Guide

- **First adjustment**: Aux 2 fader (the acoustic blend). Pull it down if it's fighting the electric. It should be felt more than heard.
- **Key interaction**: The 610-B's HI Shelf at 10 kHz, −3 dB is the most important single setting in this chain. It's what makes this sound warm and dark rather than bright and modern. Move it in either direction first if you want more or less of that character.
- **Variations**:
  - *More acoustic presence*: Raise Aux 2 fader from −8 to −4 dB, switch Acoustic Voice Pro mic from C414 to SM57 for more body/punch
  - *Brighter jazz*: Reduce 610-B HI Shelf cut to −1.5 dB and remove the Channel EQ Band 7 Hi Shelf — more Pat Metheny, less Joe Pass

---

## Feedback History

### 2026-04-30 — initial → tested
Designed for Sheraton humbuckers. Tone King Rhythm channel at very low Volume (3) to minimize preamp coloring going into Acoustic Voice Pro. Full Logic routing via Bus 1 → two parallel Aux strips → shared reverb bus. Acoustic Voice Pro is used as a texture blend, not a full acoustic emulation — at −8 dB it adds body and harmonic dimension without competing with the electric signal. 610-B HI Shelf at 10 kHz, −3 dB is the primary voicing choice for jazz warmth.
