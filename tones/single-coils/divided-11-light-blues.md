---
id: "divided-11-light-blues"
created: "2026-04-30"
updated: "2026-05-03"
guitar: Fender Player II Telecaster
target: "\"Light, dynamic blues tone through the Divided 11 \u2014 clean when backing\"
tags: "blues, dynamic, clean, grit, slapback, class-a, divided-11"
tone-king-channel: rhythm
amp: Divided 11
status: tested
pickup_type: "single-coil"
preset_data:
  la2a:
    peak_reduction: 20
    gain: 42
---

# Divided 11 Light Blues

## Target Sound

The Divided 11 (Divided by 13 CJ11) is a Class A, tube-rectified 11-watt boutique amp with tweed Fender DNA — exactly the kind of amp that rewards dynamics. Class A output tubes are always conducting, which means as you push into them, the compression comes on gradually and musically, not all at once. At Volume 5 with Low input (humbuckers), the amp sits at the clean edge: back off your picking hand and it's clear and chimey; dig in and it blooms into a slightly gritty, compressed texture. It cleans up significantly with guitar volume knob as well.

The Tone King sits in front as a clean signal driver only — Volume kept very low, IR bypassed. All amp and cab character comes from the Divided 11.

A Galaxy Tape Echo slapback (single short repeat, ~85ms) adds the signature blues dimension — time, space, and a touch of tape character — before the signal goes to a shared reverb bus with a small studio room.

---

## Signal Chain

### Tone King Imperial Preamp — transparent front-end only

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Cleanest available Tone King voicing |
| Volume | 2 | Very low — the Tone King here is a signal buffer, not a character amp |
| Attenuation | 5 | Moderate output to interface |
| Bass | 5 (noon) | Flat |
| Treble | 5 (noon) | Flat — no coloration intended |
| Reverb | Off | — |
| Tremolo | Off | — |
| IR | Bypassed | Divided 11 handles the full amp + cab simulation |

*At Volume 2, the Tone King Rhythm channel adds negligible preamp coloring — it's acting like a high-quality buffer driving the interface input cleanly.*

---

### Guitar Track → Divided 11

Plugins on the guitar track directly (no Bus routing needed — this tone is a single signal path with a reverb send).

#### 1. Divided 11 — amp

| Control | Setting | Purpose |
|---------|---------|---------|
| Power | On | — |
| Input | Low switch | Humbuckers have hotter output; Low pads the input for better dynamic headroom — the grit comes from Volume, not from overloading the input |
| Volume | 5 | Edge-of-breakup territory for Class A + humbuckers — clean on a light touch, bloom on a hard pick |
| Treble | 6 | Slightly above noon for note definition and presence in the upper mids |
| Bass | 5 (noon) | Even, natural low end — don't push more bass than needed |
| Master | 5 | Moderate output level — adjust relative to your listening level |
| Boost | Off | Off — Boost adds a gain stage that pushes into more obvious saturation; this tone is about subtlety |

**Cabinet:** Start with **THIRTEEN 1x12 GREEN** (Divided By 13 1x12 combo with Celestion G12M) — this is the reference cab for the amp, the most accurate to the original hardware character. If you want more Vox-adjacent chime, try VOICE 2x12 BLUE (Celestion Blues). Avoid the 4x12s for this tone — too much weight and low-end mass for a light blues sound.

**Microphone 1:**
- Axis: Off-axis
- Position: 50% (centered-ish on the cone — balanced warmth and definition)
- Distance: 40% (not too near-field — avoids excessive low-end proximity build-up)

**Microphone 2 (optional blend):**
- Axis: On-axis
- Level: −6 dB (adds a touch of brightness and attack definition without dominating)
- Pan: center (or slight stereo offset if you want width)

**Filters** (toggle switches — on/off only, not parameterized):
- Rumbling: ON (cuts low-frequency boominess — keeps the Class A bloom tight and focused)
- Tight: OFF (leave off unless the low end feels loose or undefined)
- Harsh: OFF (leave off unless the top end becomes abrasive — start without it)

**Noise Gate:** Set threshold just below the noise floor when playing — enough to gate hum between chords, not so sensitive it clips the decay of notes.

---

#### 2. LA-2A Tube Compressor — light optical smoothing

| Control | Setting | Purpose |
|---------|---------|---------|
| Compress/Limit | Compress | Gentle 3:1 optical ratio — the T4 photocell won't clamp the attack the way an 1176 would |
| Peak Reduction | 20 | Light compression — the goal is to smooth note-to-note level differences, not to squash the dynamic range that makes this tone work |
| Gain | 42 | Makeup gain |
| Meter | Gain Reduction | Watch the meter: at these settings you should see 2–4 dB of reduction on hard picks — more than that and you're squashing the grit response |

*The single most important thing about this compressor in this chain: keep Peak Reduction low. The Divided 11's dynamics are the whole point — compress too much and you lose the clean-to-gritty response.*

---

#### 3. Galaxy Tape Echo — slapback

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 1 | Single head — the shortest, cleanest path; classic slapback |
| Echo Rate | 6.5 | **Clockwise = shorter.** ~85ms on Head 1 for classic blues slapback. |
| Feedback | 1.5 | Just below one audible repeat; the echo fades after a single ghost. |
| Treble | 4.0 | Roll off brightness on the repeats — should sound warmer than the dry signal. |
| Bass | 5.0 | Flat — no bass change on repeats. |
| Echo Volume | 3.5 | Supportive — slapback adds space without competing with the dry signal. |
| Reverb Volume | 0.0 | No spring reverb from Galaxy; reverb is on the bus. |
| Tape Age | Used | Light wow/flutter character — organic feel. |
| Input Volume | 5.0 | Clean input — unity gain. |
| Input Send | Echo | Normal routing. |
| Wet Solo | Off | Insert effect. |

*The slapback is subtle — if you can clearly hear two separate note attacks, the Echo Volume is too high. It should feel like the room is giving your note back, not like a distinct second note.*

---

### Send from Guitar Track → Bus 3 (Reverb): −18 dB

---

### Reverb Aux — Space Designer (small studio room)

Add an Aux channel strip with Input = Bus 3. On this Aux, add Space Designer.

| Control | Setting | Purpose |
|---------|---------|---------|
| IR | Rooms folder — choose a small to medium studio room | The slapback already adds time dimension; the reverb just adds a sense of space, not more echo |
| Predelay | 8 ms | Brief gap before the room bloom — sounds natural, not washy |
| Size | 75% | A room, not a hall |
| Lo Spread | 70% | Moderate stereo width in the lows |
| Hi Spread | 75% | Slightly more open in the highs |
| Dry | −inf dB | No dry signal on the aux return — the dry signal stays on the guitar track |
| Wet | 0 dB | Full wet on the aux; the Aux fader then controls reverb return level |
| Quality | Medium | — |

**Aux Fader: −14 dB** (starting point — a subtle room, not a concert hall)

---

## Starting Point Guide

- **First adjustment**: Divided 11 Volume knob. Volume 5 is the recommendation, but the right position depends on how hot your signal hits the plugin's input. If it's already breaking up at light picks, go to 4. If it stays clean even when digging in hard, try 5.5–6.
- **Key interaction**: The Low/High input switch and the Volume knob work together. If you switch to High input, drop Volume to 3–4 to land in the same dynamic range. High input will give a slightly more alive, fizzy character; Low gives a rounder, more polished edge-of-breakup.
- **Variations**:
  - *More grit on demand*: Add the Nembrini Clon Minotaur (transparent overdrive) before the Divided 11 at low Gain. It raises the dynamic floor — light picks get a hint of grit, hard picks get a bit more push. Does not change the amp's clean headroom dramatically, just raises the floor.
  - *Blues lead mode*: Engaged Divided 11 Boost switch. This adds a gain stage that pushes into more obvious saturation and sustain — usable for single-note lead lines over a blues backing.

---

## Feedback History

### 2026-04-30 — initial
Designed for Sheraton humbuckers into Divided 11 Class A boutique amp emulation. Tone King kept at Volume 2 as a transparent front-end (no character contribution intended). Key design choice: Low input switch on Divided 11 to avoid overloading the input stage with humbuckers, then Volume 5 to sit at the Class A edge-of-breakup. Galaxy Tape Echo Head 1 slapback at ~85ms provides blues dimension without clutter. Reverb on a send bus — Space Designer small room for ambient support only.

### 2026-05-03 — first test (Gibson, THR10ii monitoring)
Output is very hot — Mike pulled plugin Output slider to −8dB to prevent blowing out THR10ii. All Nembrini Audio plugins have plugin-level Input and Output sliders as transparent gain trims at the plugin boundary (not part of the amp or cab model). The tone file does not specify the Input slider value (likely defaulted to 0dB). Recommend pairing Input reduction (−4 to −6dB) with Output compensation rather than only trimming Output — this changes how hard the virtual preamp works and may lower the amp's own modeled noise floor. Boost switch confirmed non-starter: acts as a force multiplier on an already hot signal — reserve for high-headroom contexts only. Not much grit at Volume 5 with Low input for lead work; options are Volume 5.5–6 or switch to High input at Volume 3.5–4 for a different edge-of-breakup feel. Noise/hum present even with humbuckers: attributed to Class A / tube rectifier character modeled by Nembrini (amp self-noise, not pickup hum) — noise gate engaged and appropriate.
