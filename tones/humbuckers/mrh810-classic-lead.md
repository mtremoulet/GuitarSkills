---
id: mrh810-classic-lead
created: 2026-04-30
updated: 2026-05-07
guitar: Epiphone Les Paul Standard
target: "Moderate-gain JCM800 lead \u2014 singing sustain and clear articulation in\
  \ the GN'R ballad / Bon Jovi / Poison tradition"
tags: lead, classic-rock, british, jcm800, moderate-gain, ballad, sustain
tone-king-channel: rhythm/lead
amp: MRH810 V2
status: tested
pickup_type: humbucker
---

# MRH810 Classic Lead

## Target Sound

The JCM800 Lead channel at moderate gain — the sound of Slash on November Rain and Civil War, Jon Bon Jovi on I'll Be There For You, Bret Michaels on Every Rose Has Its Thorn. This is the amp's singing, sustaining sweet spot: enough gain for notes to bloom and hold, not so much that it becomes a wash of distortion. Pick attack is audible and responds to your touch. Notes are warm, round, and clear — the amp is doing compression work, not the pedals.

The hardware signal chain (TONEX One and Tone King) provides the base analog texture and initial gain stages. The MRH810 plugin provides the core Marshall amp character and power amp/cabinet modeling.

---

## About the MRH810 Lead Channel at This Gain Setting

The JCM800 2210 is a two-stage preamp — the Gain knob drives the first stage hard before the signal hits the second preamp stage and then the EL34 power section. At Gain 5 (moderate), you're getting:
- Natural amp compression from the preamp stages working without being overloaded
- Sustain that blooms on held notes without sounding synthetic
- Enough harmonic content for warmth, not so much that individual note definition blurs
- The characteristic British midrange presence — it sits differently in a mix than a Fender

The Middle control is the most powerful EQ control on this channel — more so than Bass or Treble. The British tone stack puts Middle at the center of the sound. Pulling it back slightly opens up the response; pushing it forward thickens the mids.

---

## Signal Chain

### TONEX One — first in chain

The TONEX One provides a digital capture of a Boss BD-2 Blues Driver, acting as a versatile boost/overdrive before the preamp.

| Control | Setting | Purpose |
|---------|---------|---------|
| Capture | BD-2 | Blues Driver grit; works great with or without for added texture |
| Tone | 7 | Clear and biting top end |
| Gain | 5 | Moderate gain for push |

### Tone King Imperial Preamp — hardware preamp

The hardware Tone King pedal sits before the interface, providing the primary analog front-end.

**Option 1: Rhythm Channel (Clean/Edge)**

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Cleanest Tone King voicing |
| Volume | 5.5 | Pushing the preamp for warmth and body |
| Attenuation | 7.5 | High attenuation for output level management |
| Bass | 5 (noon) | Flat |
| Treble | 5 (noon) | Flat |

**Option 2: Lead Channel (Tweed-style Crunch)**

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Lead | Mid-forward Tweed voicing |
| Volume | 6 | Pushed gain for thicker lead lines |
| Attenuation | 5 | Moderate output |
| Mid-bite | 3 | Slightly clamped mids for tighter crunch |
| Tone | 6 | Slightly brightened top end |

---

### Guitar Track → MRH810 V2

#### MRH810 V2 — amp

**Channel Selector: Lead Channel**

**Lead Channel:**

| Control | Setting | Purpose |
|---------|---------|---------|
| Gain | 5 | Moderate — the ballad/singing-lead sweet spot. Enough preamp drive for sustain and bloom; notes stay clear and individually defined. This is where GN'R and Bon Jovi lived, not the metal-gain end. |
| Volume (channel) | 5 | Preamp stage output before master — balanced with master for even response |
| Bass | 4 | Slightly below noon — Marshall tone stacks interact inversely; too much bass muddies the low strings. Pull back slightly to keep definition. |
| Middle | 5 (noon) | The most important EQ control on this channel. Noon is a neutral starting point. Move this first when adjusting character. |
| Treble | 6 | Slightly above noon — British presence and note definition. Raises clarity without becoming harsh. |

**Master Section:**

| Control | Setting | Purpose |
|---------|---------|---------|
| Presence | 5 (noon) | Power amp high-frequency content — neutral starting point. Raise slightly (to 6) if the tone feels dark; lower if it feels edgy. |
| Volume (master) | 2.5 | Power amp output level — see gain staging note below |
| Reverb | 0 (minimum) | Built-in reverb off — reverb is on the Capitol Chambers bus |

**Cabinet: MRH 4x12 T75** (Marshall 1960B with Celestion G12T-75W speakers)

This is the canonical Marshall 4x12 sound — what the JCM800 was designed around. G12T-75 speakers are the British classic: tight low end, strong mids, slightly scooped upper mids compared to Vintage 30s.

**Microphones:**

| | Setting | Purpose |
|---|---------|---------|
| Mic 1 | Dynamic 57, On-Axis, Position 50%, Distance 40% | SM57 on-axis mid-cone — the workhorse Marshall recording position. Clear, present, punchy. |
| Mic 2 | Ribbon 121, Off-Axis, Level −6 dB | Royer R-121 ribbon, blended in low — adds warmth and low-mid body that softens the SM57's brightness. Together they're fuller than either alone. |
| Ambience fader | ~25% | Adds slight room bloom — keeps the tone from sounding too dry and close-mic'd |

**Cleaner (filter toggles):**
- Rumbling: OFF (start here — engage only if low strings feel boomy or undefined)
- Harsh: OFF (start here — engage only if the top end becomes unpleasant)

**Noise Gate:**
- Power: ON
- Threshold: set just below the noise floor with guitar not playing — gate closes on hum between phrases, opens cleanly when you play
- Range: moderate

**Levels:**
- Input: 0 dB
- Output (plugin Output slider): −4 dB

> **Gain staging note**: All Nembrini Audio plugins have a plugin-level Input and Output slider — these are transparent gain trims at the plugin boundary, not part of the amp or cab model. The Output slider is the right place to trim overall level without touching amp character. Master/Volume at 5 (original setting) caused the Stereo Out to clip at −0.9 dBFS. The corrected settings (Master/Volume 2.5, plugin Output −4 dB) land harder regular strums at −11 to −12 dBFS on the Stereo Out — a healthy tracking level with headroom for transients. Clipping on the Stereo Out manifests as fizz/crackle on single notes above the noise gate threshold.

---

#### LA-2A Tube Compressor — sustain smoothing

| Control | Setting | Purpose |
|---------|---------|---------|
| Compress/Limit | Compress | Gentle 3:1 optical — smooths note-to-note level variation without killing dynamics |
| Peak Reduction | 25 | Very light. The JCM800 preamp is already compressing the signal — this is just evening out the sustain tail. More than 30 and you'll start to hear the compressor working against the amp's natural feel. |
| Gain | 42 | Makeup gain |
| Meter | Gain Reduction | Watch for 2–3 dB on attack — if you're seeing more, back off Peak Reduction |

---

#### Galaxy Tape Echo — ballad lead delay

For classic rock ballad leads, a longer single-tap delay (250–400ms range) is the signature move. It adds harmonic depth and makes single-note lines feel fuller without adding clutter.

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 3 | Single head, 189–489ms range — the ballad delay range |
| Echo Rate | 5.0 | **Clockwise = shorter.** 5.0 on Head 3 gives ~330ms (dotted-eighth feel at moderate tempos). |
| Feedback | 2.5 | 2–3 audible repeats, naturally fading. |
| Treble | 4.0 | Roll off brightness on repeats for a natural tape decay. |
| Bass | 5.0 | Flat |
| Echo Volume | 3.5 | Supportive — repeats sit under the dry signal. |
| Reverb Volume | 0.0 | No Galaxy spring reverb. |
| Tape Age | New | Cleaner repeats for lead coherence. |
| Input Volume | 5.0 | Clean input (unity). |
| Input Send | Echo | Normal routing. |
| Wet Solo | OFF | Insert effect. |

**Send from Guitar Track → Bus 3 (Reverb): −16 dB** (more reverb send than the blues tone — this is a ballad, it wants to breathe)

---

### Reverb Aux — Capitol Chambers

**Aux Fader: −10 dB** (more open than the blues or jazz tones — ballad leads sit in a big room)

Capitol Chambers, **Wet Solo: ON**.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | 4 (Altec A7) | Most balanced starting point — good for lead guitar reverb |
| Microphones | Altec 21D | Vintage character — complements the British amp character |
| Microphones Position | 75% | Slightly pulled back — a bit more room to breathe |
| Predelay | 25 ms | Longer pre-delay than the blues tone — lets the note speak fully before reverb starts. Important for lead clarity. |
| Decay | ~2.5 seconds | Bigger and more open than the jazz or blues tones — this is ballad territory |
| Filter | 200 Hz | Cut low-end muddiness from the reverb return |
| EQ Bass | 0 dB | Flat |
| EQ Mid | −1 dB | Smooth the reverb midrange |
| EQ Treble | −1 dB | Keep reverb warmth in line with the amp character |
| Width | 90% | Wide and open |
| Wet Solo | ON | Required for aux bus routing |

---

## Starting Point Guide

- **First adjustment**: MRH810 Gain knob. This is the most consequential control. 5 is the starting point for ballad lead. Push toward 6–7 for more classic rock saturation (Guns N' Roses rhythm, AC/DC). Pull to 3–4 for a cleaner, more edge-of-breakup character (Poison's Every Rose is actually quite clean — try 3 with the same chain).
- **Key interaction**: Middle controls the character of the Lead channel more than any other EQ control. Pull to 4 for a slightly open, more scooped classic rock sound. Push to 6 for a thicker, more mid-heavy British crunch. This is where you find the difference between Slash and AC/DC.
- **Learning the MRH810 — what to explore from here**:
  - *Higher gain (7–8)*: Crosses into actual metal/hard rock rhythm territory — Metallica early albums, aggressive rock rhythm. The tone gets more compressed and less note-defined.
  - *Clean channel instead*: Drop the Channel Selector to Clean, set Clean Volume to match, and you have a pure clean platform for pedals. Use the Clon Minotaur or 808 in Logic (or TONEX One) in front of the Clean channel to build your own pushed-lead chain.
  - *808 in front of this Lead channel*: Add the Nembrini 808 plugin before the MRH810 in the chain. Keep 808 Drive low (level boost, not distortion). This tightens the low end, pushes the amp slightly harder, and adds the classic Slash/EVH pre-amp boost trick. Volume up, Gain/Drive minimum.
  - *Different cabinets*: Try ORANGE 4x12 V30 for a slightly more compressed, scooped character. MB RECT 4x12 V30 for a tighter, more modern tone. TWEED 4x10 P10Q for a warmer, softer British/American hybrid — a surprising and musical option.

---

## Feedback History

### 2026-04-30 — initial
Designed as a starting point for learning the MRH810 V2 capabilities. Lead channel at Gain 5 — the moderate-gain ballad-lead sweet spot referenced in GN'R, Bon Jovi, and Poison classic rock ballad tones. MRH 4x12 T75 (canonical Marshall cabinet) with Dynamic 57 + Ribbon 121 blend. Galaxy Tape Echo on Head 3 for ballad-style delay (~330ms). Capitol Chambers for reverb. Notes cover how to explore the plugin from this starting point — higher gain, clean channel, different cabs.

### 2026-05-03 — gain staging fix, status: tested
Master/Volume at 5 caused Stereo Out to clip at −0.9 dBFS, producing fizz/crackle on single notes above the noise gate threshold. Fixed by pulling Master/Volume to 2.5 and adding −4 dB on the plugin Output slider (transparent plugin-level trim, no effect on amp character). Result: harder regular strums sit at −11 to −12 dBFS on Stereo Out — healthy headroom for transient peaks. Status updated to tested.

### 2026-05-07 — hardware chain update
Updated signal chain to include hardware TONEX One (BD-2 capture) and specific hardware Tone King Imperial Preamp settings (Rhythm and Lead options). Guitar specified as Epiphone Les Paul Standard. These hardware settings provide the base analog texture before hitting the MRH810 plugin.
