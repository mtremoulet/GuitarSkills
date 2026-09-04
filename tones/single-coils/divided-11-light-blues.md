---
amp: "Divided 11 (Nembrini)"
created: 2026-04-30
guitar: "Fender Player II Telecaster"
id: divided-11-light-blues
pickup_type: single-coil
status: tested
tags: "blues, dynamic, clean, grit, slapback, class-a, divided-11"
target: '"Light, dynamic blues tone through the Divided 11 \u2014 clean when backing\'
tone-king-channel: bypassed
updated: 2026-08-26
preset_data:
  galaxy:
    echo_rate: 6.5
    echo_volume: 3.5
    feedback: 1.5
    head_select: 1
    reverb_volume: 0.0
    tape_age: Used
  la2a:
    gain: 42
    peak_reduction: 20
  nembrini_div11:
    Bass: 4.0
    Boost: 0.0
    CabMode: 0.0
    CabType: 0.0
    Harsh: 1.0
    InLevel: -3.5
    InputMode: 0.0
    Master: 6.5
    Mic1Dist: 2.0
    Mic1Gain: 0.0
    Mic1Mute: 0.0
    Mic1OffAxis: 1.0
    Mic1Pos: 2.5
    Mic1Type: 1.0
    Mic2Dist: 2.5
    Mic2Gain: -9.0
    Mic2Mute: 0.0
    Mic2OffAxis: 1.0
    Mic2Pos: 2.5
    Mic2Type: 0.0
    NgPower: 1.0
    NgThreshold: -70.0
    OutLevel: -6.0
    Rumbling: 1.0
    Tight: 1.0
    Treble: 4.8
    Volume: 4.2
    power: 1.0
---

# Divided 11 Light Blues

## Target Sound

The Divided 11 (Divided by 13 CJ11) is a Class A, tube-rectified 11-watt boutique amp with tweed Fender DNA — built to reward touch dynamics. Class A circuits are always conducting, allowing notes to bloom into smooth harmonic compression rather than harsh clipping. 

To dial in true "light blues" dynamics and eliminate the amp's hyper-aggressive digital gain:
1. **Boost OFF**: The Boost switch slams the preamp with high saturation; keeping it OFF is essential for clean headroom and dynamic touch.
2. **Gain Staging Balance**: Preamp Volume is dialed back to **4.2**, while Master is pushed up to **6.5** to coax warm Class A power tube compression and sag without fizzy preamp buzz. The plugin's utility Input slider is trimmed to **-3.5 dB** to soften front-end sensitivity.
3. **Taming Boom & Sharpness**: Amp Bass is pulled back to **4.0** (Tweed bass adds flub above noon) and Treble smoothed to **4.8**. In the cab section, we pair a warm **Ribbon 121** with a soft **Dynamic 57** blend, engaging the **Rumbling**, **Tight**, and **Harsh** filters.

A subtle Galaxy Tape Echo slapback (~85ms) and a shared Space Designer studio room complete the spacious, organic blues soundstage.

---

## Signal Chain

### Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### Guitar Track → Divided 11

Plugins on the guitar track directly (no Bus routing needed — this tone is a single signal path with a reverb send).

#### 1. Divided 11 — amp

| Control | Setting | Purpose |
|---------|---------|---------|
| Power | On | — |
| Input | **LOW Switch** | Pads the input sensitivity (~-6 dB) to expand dynamic headroom and prevent preamp overload (or use HIGH with Volume at 3.5) |
| Volume | **4.2** | Preamp gain sweet spot — clean on light picking, dynamic bite when digging in |
| Treble | **4.8** | Smoothed slightly below noon to eliminate harsh top-end spank |
| Bass | **4.0** | Kept below noon to eliminate Tweed low-end boominess and mud |
| Master | **6.5** | Pushes the Class A power amp emulation for rich harmonic bloom and sag |
| Boost | **OFF** | **CRITICAL:** Off — Boost adds a heavy saturation stage that destroys dynamic range |
| Input Level | **−3.5 dB** | Utility input trim; prevents hot interface DI signals from overwhelming the modeled 12AX7 grid |
| Output Level | **−6.0 dB** | Final output trim for clean headroom into downstream plugins |

**Cabinet:** **THIRTEEN 1x12 GREEN** (Divided By 13 1x12 combo with Celestion G12M) — woody, focused midrange and smooth high-frequency roll-off.

**Microphone 1:**
- Type: **Ribbon 121** (warm, creamy body, smooth high roll-off)
- Axis: **Off-axis**
- Position: **50%**
- Distance: **40%**
- Level: **0.0 dB**

**Microphone 2 (Blend):**
- Type: **Dynamic 57**
- Axis: **Off-axis**
- Position: **50%**
- Distance: **50%**
- Level: **−9.0 dB** (soft background blend for pick attack definition without ice-pick treble)

**Filters (Cab Section):**
- Rumbling: **ON** (cuts sub-100Hz cabinet boominess)
- Tight: **ON** (tightens low-mid response)
- Harsh: **ON** (shelves aggressive 4–6kHz digital fizz)

**Noise Gate:** Active (Power: ON, Threshold: −70 dB, Range: 38 dB, Gate: 35) to eliminate idle circuit hiss.

---

#### 2. UADx LA-2A Silver Compressor — light optical smoothing

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Compress | Gentle 3:1 optical ratio — the T4 photocell won't clamp the attack the way an 1176 would |
| Peak Reduction | 20 | Light compression — the goal is to smooth note-to-note level differences, not to squash the dynamic range that makes this tone work |
| Gain | 42 | Makeup gain |
| Emphasis / HF | Fully Clockwise (default) | Equal frequency sensitivity in the sidechain |
| Meter | Gain Reduction | Watch the meter: at these settings you should see 1–3 dB of reduction on hard picks |

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

- **First adjustment**: Input Switch vs Preamp Volume. Low input at Volume 4.2 gives a smooth, open dynamic range. If you prefer High input, lower Volume to 3.2–3.5 to preserve clean-to-grit headroom.
- **Tone Stack Balance**: Bass at 4.0 and Treble at 4.8 keep the Tweed circuit balanced. If switching guitars (e.g. darker humbuckers vs bright bridge single-coil), nudge Treble up to 5.2 or down to 4.5.
- **Variations**:
  - *More grit on demand*: Add the Nembrini Clon Minotaur (transparent overdrive) before the Divided 11 at low Gain. It raises the dynamic floor — light picks get a hint of grit, hard picks get a bit more push.
  - *Blues lead mode*: Engage Divided 11 Boost switch only when high saturation and sustained compression are explicitly desired.

---

## Feedback History

### 2026-04-30 — initial
Designed for Sheraton humbuckers into Divided 11 Class A boutique amp emulation. Tone King kept at Volume 2 as a transparent front-end (no character contribution intended). Key design choice: Low input switch on Divided 11 to avoid overloading the input stage with humbuckers, then Volume 5 to sit at the Class A edge-of-breakup. Galaxy Tape Echo Head 1 slapback at ~85ms provides blues dimension without clutter. Reverb on a send bus — Space Designer small room for ambient support only.

### 2026-05-03 — first test (Gibson, THR10ii monitoring)
Output is very hot — Mike pulled plugin Output slider to −8dB to prevent blowing out THR10ii. All Nembrini Audio plugins have plugin-level Input and Output sliders as transparent gain trims at the plugin boundary (not part of the amp or cab model). The tone file does not specify the Input slider value (likely defaulted to 0dB). Recommend pairing Input reduction (−4 to −6dB) with Output compensation rather than only trimming Output — this changes how hard the virtual preamp works and may lower the amp's own modeled noise floor. Boost switch confirmed non-starter: acts as a force multiplier on an already hot signal — reserve for high-headroom contexts only. Not much grit at Volume 5 with Low input for lead work; options are Volume 5.5–6 or switch to High input at Volume 3.5–4 for a different edge-of-breakup feel. Noise/hum present even with humbuckers: attributed to Class A / tube rectifier character modeled by Nembrini (amp self-noise, not pickup hum) — noise gate engaged and appropriate.

### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.

### 2026-07-20 — re-tested on Strat (borderline unusably bad/hot)
Re-tested on Strat single-coils. Tone is super hot, distorted, and unpleasant. Nembrini's modeling of this Class A Divided by 13 circuit is aggressively gain-staged by default. Requires heavy internal Input trim (−6 to −10 dB) or lower preamp Volume (2.5–3.5) if retained, or pivoting to a smoother Class A / tweed alternative (e.g. Woodrow '55 or Dream '65).

### 2026-08-26 — recalibration (gain architecture, boost off, filters on)
Recalibrated toneprint after testing notes confirmed the amp is hyper-reactive and gained too aggressively with Boost on. Set Boost explicitly to OFF, set Input to Low, lowered Preamp Volume to 4.2 while pushing Master to 6.5 for warm Class A power tube sag instead of buzzy preamp distortion. Trimmed plugin InLevel to -3.5 dB and OutLevel to -6.0 dB. Reconfigured the cab section with Ribbon 121 as primary (off-axis) and Dynamic 57 blended down (-9 dB), and engaged all three cabinet corrective filters (Rumbling, Tight, Harsh) to completely eliminate boomy low-end flub and treble sharpness.

