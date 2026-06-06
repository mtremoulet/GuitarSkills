---
id: tkip-sheraton-jazz-clean
preset_name: "TKIP Sheraton Jazz Clean"
created: 2026-06-06
updated: 2026-06-06
guitar: "Epiphone Sheraton II"
target: "A warm, dark, woody jazz tone with suppressed transients and a rolled-off high end."
tags: "jazz, clean, humbucker, warm, dark, mellow"
tone-king-channel: rhythm
amp: "Tone King Imperial Preamp (Hardware)"
status: initial
pickup_type: humbucker
preset_data:
  amp_platform: hardware
  amp_settings:
    Channel: Rhythm
    Volume: 3.0
    Attenuation: 5.0
    Bass: 6.0
    Treble: 3.0
    Reverb: Off
    Tremolo: Off
    IR: Active (Imperial 1x12 TK1660)
  logic_enveloper:
    attack_gain: -6.0
    attack_time: 20.0
    release_gain: 0.0
    release_time: 150.0
  logic_compressor:
    threshold: -22.0
    ratio: 2.5
    attack: 15.0
    release: 150.0
    makeup_gain: 2.0
    knee: 0.8
    circuit_type: Vintage Opto
  hitsville:
    mix: 1.0
    pre_delay: 15.0
    decay: 1.5
    wet_solo: true
  logic_eq:
    band1: {on: true, freq: 80.0, slope: 12.0}
    band4: {on: true, freq: 650.0, gain: 2.0, q: 1.5}
    band7: {on: true, freq: 4000.0, slope: 24.0}
---

# TKIP Sheraton Jazz Clean

## Target Sound
A warm, classic jazz box tone tailored for the Epiphone Sheraton II neck humbucker. Built on the hardware Tone King Rhythm channel (blackface flavor) kept in its cleanest, high-headroom transparency zone (Volume 3.0, Attenuation 5.0). To soften the typical "plucky" pick attack of humbuckers, Logic's native Enveloper is used to suppress the initial transient, and a high-cut low-pass filter at 4.0 kHz creates the classic "electronic veil" (Ed Bickert style). Midrange frequencies are boosted in Logic EQ to counteract the Rhythm channel's natural mid-scoop.

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
Provides the base clean tube preamp foundation and warm cabinet simulation.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Rhythm | Clean blackface character with high headroom |
| Volume | 3.0 | Keeps the preamp in the cleanest zone |
| Attenuation | 5.0 | Unity/moderate output |
| Bass | 6.0 | Thickens the low end |
| Treble | 3.0 | Rolled back to tame high-end brightness |
| Reverb | Off | Handled in Logic sends |
| Tremolo | Off | Disabled |
| IR | Active (Imperial 1x12 TK1660) | Voiced for dark, intimate, close-mic'd character |

### 2. Logic Enveloper — transient shaper (transient suppression)
Placed first in the DAW insert chain to round off the sharp pick attack and create a soft, woody voice.

| Control | Setting | Purpose |
|---------|---------|---------|
| Attack Gain | −6.0 dB | Clamps down on the initial pick transient |
| Attack Time | 20 ms | Quick reaction window to target the attack |
| Release Gain | 0.0 dB | Preserves the natural ring and decay of the chord |
| Release Time | 150 ms | Smooth return to unity |

### 3. Logic Compressor — dynamic smoothing
Placed inline to gently control dynamics and add vintage optical character.

| Control | Setting | Purpose |
|---------|---------|---------|
| Circuit Type | Vintage Opto | Emulates classic optical compression response |
| Threshold | −22.0 dB | Light leveling |
| Ratio | 2.5:1 | Gentle compression ratio |
| Attack | 15.0 ms | Lets the initial (already softened) transient pass before compressing |
| Release | 150.0 ms | Natural, breathing recovery time |
| Make Up | +2.0 dB | Makeup gain |
| Knee | 0.8 | Soft compression transition |

### 4. Logic Channel EQ — mid-boosting & "high-cut veil"
Sculpts the frequency response to emulate a dark, vintage hollow-body jazz amplifier (like a Polytone).

| Control | Setting | Purpose |
|---------|---------|---------|
| Band 1 (High Pass) | On — 80.0 Hz, 12 dB/oct | Removes sub-bass muddy rumble |
| Band 4 (Peak) | On — 650.0 Hz, +2.0 dB, Q: 1.5 | Boosts low-mids to fill in the Rhythm channel's natural scoop |
| Band 7 (High Cut) | On — 4.0 kHz, 24 dB/oct slope | Low-pass filter (high-cut veil) to eliminate digital air and fizz |

### 5. Hitsville Reverb Chambers (Bus 3 Send) — space reverb
Set on Bus 3 at **100% Wet** (Wet Solo ON) to keep the dry tone close and intimate.

| Control | Setting | Purpose |
|---------|---------|---------|
| Send Level | −16.0 dB | Adds subtle, supportive acoustic environment |
| Chamber | Chamber 2 | Mellow chamber voicing |
| Mix | 1.0 (100% Wet) | Aux bus blend |
| Decay | 1.5 seconds | Shorter tail for clarity on fast jazz lines |
| Pre-Delay | 15 ms | Small pre-delay for note clarity |

---

## Starting Point Guide
- **First adjustment:** Guitar Volume & Tone controls. Roll guitar Volume to **7** and Tone to **6** to activate the touch-sensitivity of the Tone King preamp and round off the top end.
- **Key interaction:** If the pick attack still feels too sharp, increase the Enveloper's Attack Gain reduction (e.g., to **−8.0 dB**). If it feels too dead, raise it toward **−4.0 dB**.
- **Variations:** To get an even warmer, acoustic-leaning tone, blend in a very low parallel dry track, but ensure the high-cut veil remains active on the primary electric track.

---

## Feedback History

### 2026-06-06 — initial
Designed as a warm, dark jazz box toneprint for the Epiphone Sheraton II neck humbucker. Uses the physical TKIP Rhythm channel (Volume 3.0, Attenuation 5.0, Bass 6.0, Treble 3.0) and uses Logic's Enveloper to suppress pick transients. A 4.0 kHz high-cut EQ filter serves as the "electronic veil," and a +2.0 dB EQ boost at 650 Hz fills in the mid scoop.
