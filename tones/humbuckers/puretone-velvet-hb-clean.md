---
id: "puretone-velvet-hb-clean"
preset_name: "Puretone Velvet Humbucker Clean"
created: "2026-06-27"
updated: "2026-06-27"
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (neck or neck+bridge humbuckers)"
target: 'Lush, ultra-clear hi-fi humbucker clean with integrated 150ms slap echo, transient softening, and an optional Klon-style clean boost for polished studio clarity.'
tags: "boutique, clean, warm, humbucker, puretone, delay, slapback, clon, transient-softener"
tone-king-channel: bypassed
amp: "H&K Puretone (Nembrini)"
status: initial
pickup_type: humbucker
preset_data:
  logic_enveloper:
    attack_time: 12.0
    attack_gain: -30.0
    lookahead: 2.0
    release_time: 200.0
    release_gain: 0.0
    threshold: -100.0
    out_level: 0.0
  clon_minotaur:
    power: true
    gain: 0.0
    output: 7.6
    treble: 3.8
  nembrini_puretone:
    Volume: 3.5
    Growl: 0.0
    Bass: 4.5
    Mid: 5.5
    Treble: 4.0
    Tone: 5.0
    OutLevel: -4.0
    InputLevel: 0.0
    NoiseGatePower: true
    NoiseGateThreshold: -89.7
    NoiseGateRange: 40.5
    NoiseGateRelease: 38.7
    EqPower: true
    EqHighPass: 80.0
    EqLowPass: 10002.0
    DelayPower: true
    DelayMix: 15.0
    DelaySpread: 54.0
    DelayNote: "1/4"
    DelayHostSync: false
    DelayTime: 150.0
    DelayTone: 5.0
    DelayFeedback: "Off"
    ReverbPower: true
    ReverbMix: 15.0
    ReverbSize: 2.5
    ReverbTone: 3.5
    CabinetMode: "Cabinet"
    CabinetType: "Hughes & Kettner TC 412 Real"
    Mic1Type: "DYNAMIC 57"
    Mic1Distance: 1.5
    Mic1Position: 3.8
    Mic1Gain: -18.7
    Mic1OffAxis: true
    Mic2Type: "RIBBON 121"
    Mic2Distance: 3.1
    Mic2Position: 6.6
    Mic2Gain: -13.5
    Mic2OffAxis: false
---

# Puretone Velvet Humbucker Clean

## Target Sound

This toneprint represents the ultimate hi-fi humbucker clean platform built around the **Nembrini Hughes & Kettner Puretone**. Designed specifically for double-humbucker guitars like the **Gibson Les Paul Studio** or **Epiphone Sheraton II**, it delivers transparent, velvety note definition with an organic acoustic-like bloom and zero lower-mid mud.

The signal chain incorporates two key front-end elements:
1. **Logic Enveloper (Transient Softener)**: Transparently shaves off the initial pick click spike (-30% Attack Gain, 12ms attack) so DI pick strikes never sound clicky or synthetic.
2. **Nembrini NA Clon Minotaur (Clean Boost Buffer)**: Positioned right before the amp with Gain at `0.0`, Output pushed to `7.6`, and Treble warmed to `3.8`. This acts as a classic transparent buffer, adding subtle mid-harmonic density and driving the Puretone's front end with effortless touch sensitivity.

Inside the Puretone engine, a meticulously dialed built-in FX section provides a 15% mix, 150ms single-repeat slap delay (54% stereo spread) alongside a smooth 15% reverb chamber bloom. An 80Hz HPF and 10kHz LPF ensure high-end fizziness and low-end thrum are kept completely out of your DAW mix.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for uncolored headroom).

---

### 2. Logic Enveloper — "Transient Softener"
Positioned first in the DAW insert chain to blunt raw DI pick attack spikes before reaching drive or amp modeling.

| Control | Setting | Purpose |
|---------|---------|---------|
| Attack Time | 12.0 ms | Covers the exact duration of the physical pick strike |
| Attack Gain | −30.0 % | Shaves off sharp transients for smooth fingerstyle/pick transitions |
| Lookahead | 2.0 ms | Pre-scans digital audio to capture instantaneous peak attack |
| Release Time / Gain | 200 ms / 0.0 % | Leaves note decay and natural body untouched |
| Threshold / Out | −100 dB / 0.0 dB | Triggers consistently across all playing dynamics at unity gain |

---

### 3. Nembrini NA Clon Minotaur (Optional Clean Boost)
Placed after the Enveloper to provide transparent Klon buffer warmth and clean output boost.

| Control | Setting | Purpose |
|---------|---------|---------|
| Power | On | Active transparent clean boost / buffer |
| Gain | 0.0 | Zero drive added; maintains 100% clean headroom |
| Output | 7.6 | Pushes extra clean level into the Puretone front end |
| Treble | 3.8 | Rolled back slightly to smooth out high-frequency edge |

---

### 4. Nembrini H&K Puretone
The primary boutique amp platform. The Growl knob is kept at zero to keep the tone stack fully active.

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 3.5 | Clean headroom sweet spot; highly touch-sensitive |
| Growl | 0.0 | Full active EQ stack for maximum polish and refinement |
| Bass | 4.5 | Rolled back slightly to prevent humbucker low-end mud |
| Middle | 5.5 | Boosted slightly for vocal midrange warmth |
| Treble | 4.0 | Smooth high end, complemented by Clon Treble at 3.8 |
| Input Level / OutLevel | 0.0 dB / −4.0 dB | Post-amp trim preventing digital master bus clipping |

#### Internal FX & Filters Section:
*   **Noise Gate**: On | Threshold: `-89.7 dB` | Range: `40.5 dB` | Gate/Release: `38.7 %`
*   **EQ Filters**: On | High Pass: `80.0 Hz` (cleans sub-bass) | Low Pass: `10002.0 Hz` (10 kHz smooth air cap)
*   **Delay**: On | Mix: `15.0 %` | Spread: `54.0 %` | Note: `1/4` (Sync Off) | Time: `150.0 ms` | Tone: `5.0` | Feedback: `Off`
*   **Reverb**: On | Mix: `15.0 %` | Size: `2.5` | Tone: `3.5`

#### Cabinet & Dual-Microphone Selection:
*   **Cabinet Type**: Hughes & Kettner TC 412 Real
*   **Mic 1**: **DYNAMIC 57** — Distance: `1.5` | Position: `3.8` | Gain: `-18.7 dB` | **Off Axis: On** *(Tames high-frequency pick transients)*
*   **Mic 2**: **RIBBON 121** — Distance: `3.1` | Position: `6.6` | Gain: `-13.5 dB` | **Off Axis: Off** *(Provides rich, dark low-mid body)*

---

## Starting Point Guide

- **First adjustment**: If swapping between a low-output neck humbucker (e.g. 490R) and a hot bridge humbucker (e.g. 498T), adjust the **Output** knob on the NA Clon Minotaur between `6.5` and `7.6` to keep the front-end boost perfectly balanced.
- **Key interaction**: The dual mic array (off-axis D57 + on-axis R121) combined with the Enveloper ensures that even aggressive chord stabs remain smooth and wide without harshness.
- **Variations**: Toggle the NA Clon Minotaur **Power: Off** for a purely linear, unbuffered Puretone clean.

---

## Feedback History

### YYYY-MM-DD — initial (2026-06-27)
Created custom humbucker toneprint based on Mike's tuned H&K Puretone settings. Integrates 150ms 1/4 slap delay (15% mix), 15% reverb chamber bloom, 80Hz/10kHz filtering, front-end Enveloper Transient Softener (-30%), and NA Clon Minotaur clean boost (Gain 0.0, Output 7.6, Treble 3.8).
