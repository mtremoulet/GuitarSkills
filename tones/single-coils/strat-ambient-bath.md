---
id: "strat-ambient-bath"
created: "2026-05-02"
updated: "2026-05-02"
guitar: Squier Stratocaster (single coils)
target: "Lush, lingering ambient soundscape; massive reverb wash, stereo chorus, and"
tags: "ambient, lush, sound-bath, strat, clean, delay, reverb, modulation"
tone-king-channel: rhythm
amp: "Showtime '64"
status: initial
pickup_type: "single-coil"
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Volume: 2
    Treble: 5
    Middle: 5
    Bass: 5
    Bright: true
  la2a:
    peak_reduction: 45
    gain: 40
---

# Strat Ambient Bath

## Target Sound

This tone is designed to transform the Squier Strat into an ambient soundscape machine. The goal is a "sound bath" experience where notes linger and blend into a rich, harmonic wash. This requires a very clean, high-headroom platform that won't distort even when hit with massive spatial effects.

We use the **Showtime '64** for its transparent, high-headroom character, providing the perfect canvas. **LA-2A Silver** provides the essential "glue" and sustain, leveling out the Strat's sharp transients and allowing notes to bloom. The stereo width comes from the **Studio D Chorus**, while the "wash" is provided by a combination of **Galaxy Tape Echo** and the massive **ValhallaSuperMassive**.

Best played with the Neck pickup (Pos 5) or Neck/Middle (Pos 4) with the guitar's tone knob rolled back slightly (to 7–8) if it feels too "pokey."

---

## Signal Chain

### Tone King Imperial Preamp — transparent front-end

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Cleanest available Tone King voicing |
| Volume | 2 | Acting as a high-quality buffer/DI |
| Attenuation | 5 | Moderate output |
| Bass | 5 | Flat |
| Treble | 5 | Flat |
| IR | Bypassed | Showtime '64 handles the cab |

---

### Guitar Track → Ambient Chain

#### 1. LA-2A Silver Compressor — Optical Sustain

| Control | Setting | Purpose |
|---------|---------|---------|
| Compress/Limit | Compress | 3:1 optical ratio for smooth leveling |
| Peak Reduction | 45 | Significant compression to increase sustain and "linger" time |
| Gain | 40 | Makeup gain to keep the signal healthy |
| Meter | Gain Reduction | Look for 5–7 dB of reduction on peaks; let the note decay naturally |

---

#### 2. Showtime '64 — Transparent Clean Platform

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 3.5 | Clean and clear; stay well below the breakup point |
| Bright | ON | Retains the Strat's characteristic sparkle through the effects |
| Treble | 6 | Clarity in the top end |
| Middle | 5 | Neutral |
| Bass | 4 | Tamed low end to prevent "mud" once the reverb wash starts |
| Vibrato | OFF | We'll use Studio D for modulation |

**Cabinet:** **JBF120** (Vintage JBL D-120F 1x12) — Bright, hi-fi, and wide-range.
**Microphone:** Fixed **Condenser 414** pairing.

---

#### 3. Studio D Chorus — Stereo Width

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | 4 | Maximum Dimension D width; creates a massive stereo image |

---

#### 4. Galaxy Tape Echo — Warm Repeats

| Control | Setting | Purpose |
|---------|---------|---------|
| Head Select | 1+2+3 | Multi-tap for a rhythmic, dense echo bed (Position 10). |
| Echo Rate | 5.0 | **Clockwise = shorter.** Medium-slow repeats. |
| Feedback | 6.0 | Higher feedback for repeats that blend into each other. |
| Echo Volume | 3.5 | Supportive — feeds the Valhalla wash. |
| Tape Age | Old | Adds subtle pitch drift and warmth. |

---

#### 5. ValhallaSuperMassive — The Wash

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Great Andromeda | Massive, dense, and lush reverb/delay hybrid |
| Mix | 45% | Significant wet signal; notes should feel like they are floating |
| Delay | 800ms | Long delay time for the "lingering" effect |
| Warp | 50% | Adds density to the reverb tail |
| Feedback | 85% | Very high — the sound should linger for several seconds |
| Density | 100% | Maximum smoothness |

---

### Send from Guitar Track → Bus 4 (Capitol Chambers): −12 dB

---

### Reverb Aux — Capitol Chambers (Lush Space)

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | Chamber 4 | Large, lush room sound |
| Mic | Condenser | Maximum detail and "air" |
| Mix | 100% | Full wet on the Bus |
| Decay | 4.0s | Long decay to match the SuperMassive wash |

---

## Starting Point Guide

- **The Linger**: If the sound dies out too quickly, increase the **Feedback** on ValhallaSuperMassive or the **Peak Reduction** on the LA-2A.
- **Taming the Highs**: Strats can get "ice-picky" with this much processing. If it's too bright, toggle the **Bright** switch on Showtime '64 to OFF, or use the **Tone** knob on the guitar.
- **Dynamics**: This tone is highly sensitive to input volume. Try using a volume pedal (or your guitar's volume knob) to "swell" into notes, hiding the attack and letting only the lush wash bloom.

---

## Feedback History

### 2026-05-02 — initial
Designed for Squier Strat single coils. Focuses on high-headroom clean (Showtime '64) and massive spatial effects (Studio D + Galaxy + SuperMassive). Designed for "sound bath" experiences and slow, ambient playing.
