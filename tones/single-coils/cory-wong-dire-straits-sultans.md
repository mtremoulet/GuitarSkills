---
amp: "The Clean Machine (Archetype Cory Wong X)"
created: 2026-07-02
guitar: "Fender Player II Telecaster / Squier Stratocaster (Middle + Bridge or Neck + Middle position — 'quack')"
id: cory-wong-dire-straits-sultans
pickup_type: single-coil
preset_name: "Dire Straits Sultans Clean ACWX"
status: initial
tags: "dire-straits, single-coil, stratocaster, clean, fingerstyle, rock, knopfler, neural-dsp, cory-wong"
target: 'Mark Knopfler 1978 fingerstyle clean quack in ACWX — highly compressed, bright, and articulate standalone tone for single-coils.'
tone-king-channel: bypassed
updated: 2026-07-02
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: false
    bigRigActive: false
    chorusActive: false
    delayActive: false
    leftCab0MicType: 1
    leftCabActive: true
    leftCabDistance: 0.15
    leftCabPosition: 0.42
    leftRoomMicLevel: -24.0
    postalActive: false
    rightCabActive: false
    selectedAmp: 1
    selectedCab: 1
    compressorActive: true
    compressorVolume: 55.0
    compressorCompression: 45.0
    compressorTone: 60.0
    compressorBlend: 55.0
    cleanVolume: 35.0
    cleanBright: true
    cleanBass: 40.0
    cleanMid: 50.0
    cleanTreble: 65.0
    cleanPresence: 55.0
    cleanOutputLevel: 70.0
    cleanEQActive: true
    cleanEQHpf: 20.0
    cleanEQLpf: 20000.0
    cleanEQBand1: 0.0
    cleanEQBand2: -1.0
    cleanEQBand3: -2.0
    cleanEQBand4: 0.0
    cleanEQBand5: 1.5
    cleanEQBand6: 1.0
    cleanEQBand7: 1.0
    cleanEQBand8: 0.0
    cleanEQBand9: 0.0
    tuberActive: false
    washActive: true
    washMix: 12.0
    washDecay: 25.0
    washShimmer: false
---

# Dire Straits — Sultans Clean (Archetype Cory Wong X)

## Target Sound

This toneprint is the Archetype Cory Wong X (ACWX) standalone equivalent of the **Dire Straits Sultans Strat** preset. It captures the pristine, percussive single-coil clean tone of Mark Knopfler on the 1978 classic **"Sultans of Swing."**

Knopfler's signature tone relies on fingerstyle playing (flesh-on-string) which creates significant transient spikes. To control these spikes while keeping the sound incredibly bright and snappy, we use **"The Clean Machine"** with the **Bright switch ON** and elevated treble (65%). 

We pair this with **"The 4th Position Compressor"** set with a high compression depth (45%) and high parallel blend (55%) to act as a brickwall peak-leveler. The cab is unlinked and paired with a crisp dynamic microphone model close-mic'd (**Distance L at 0.15**) for immediate transient snap, with no modulation or delay and a dry room reverb.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom).

---

### 2. Archetype Cory Wong X — standalone channel strip

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 4th Position Compressor** | **Active** | **ON** | Brickwall peak-leveling for fingerstyle transients |
| | **Blend** | **55%** | Higher mix to smooth wide dynamic swings |
| | **Tone** | **60%** | Elevated compressor treble to keep pick attack crisp |
| | **Compression**| **45%** | Deep compression depth to mimic studio optical limiter |
| | **Volume** | **55%** | Unity level |

*All other Pre FX are bypassed.*

**Amp Section — "The Clean Machine"**

All parameters are specified in percentages (0–100%).

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Clean Machine** | Twin Reverb high-headroom platform |
| Volume (Gain) | **35%** | High headroom sweet spot |
| Bright Switch | **ON** (Up) | Vital high-end bite and chime for Strat "quack" |
| Bass | **40%** | Rolled back to keep fingerpicked bass lines tight |
| Middle | **50%** | Balanced midrange |
| Treble | **65%** | Elevated treble for high-end glass and definition |
| Presence | **55%** | Pushed power-amp presence for bite |
| Output | **70%** | Plugin level output trim |

**Cab Section (Unlinked Cabinets)**

We unlink the cabinets to pair the Clean Machine with a punchy dynamic mic setup.

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **Off** | Unlinked for custom mic pairing |
| Cab Type | **Clean** | Matching 2x12 open-back cabinet |
| Cab L | **Active** | Primary mic slot |
| Mic L Type | **Dynamic 57** (Type 1) | Punchy, mid-forward dynamic mic; highlights transient bite |
| Position L | **0.42** | Close to speaker center for crisp treble response |
| Distance L | **0.15** | Close-mic'd for immediate, dry note attack |
| Room Send L | **−24.0 dB** | Dry room environment |
| Cab R | **BYPASSED** | Mono phase-coherence |

**EQ Section (Clean Machine 9-Band Graphic EQ)**

| Band | Setting | Purpose |
|------|---------|---------|
| EQ Status | **Active** | Sculpting the "quack" resonance |
| 65 Hz | 0.0 dB | Neutral |
| 125 Hz | −1.0 dB | Rolled back to clear low-end resonance |
| 250 Hz | −2.0 dB | **Targeted cut**: Cleans up muddy build-up from neck/middle positions |
| 500 Hz | 0.0 dB | Neutral |
| 1 kHz | +1.5 dB | **Targeted push**: Enhances out-of-phase "quack" honk |
| 2 kHz | +1.0 dB | Pushes snappy transient attack |
| 4 kHz | +1.0 dB | Enhances single-coil high-end chime |
| 8 kHz | 0.0 dB | Neutral |
| 16 kHz | 0.0 dB | Neutral |
| HPF / LPF | Default | 20 Hz High-Pass / 20.0 kHz Low-Pass |

**Post FX Section**

*Chorus and Delay are **BYPASSED**.*

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The Wash** | **Active** | **ON** | Integrated room reverb |
| | **Mix** | **12%** | Dry room depth |
| | **Decay** | **25%** | Short room space to keep rhythm tight |
| | **Shimmer** | **OFF** | Bypassed |

---

## Starting Point Guide

- **Physical Technique:** Select the **Bridge + Middle** (Position 2) or **Neck + Middle** (Position 4) on your Stratocaster. Play with the flesh of your fingers and thumb rather than a pick to replicate Mark Knopfler's warm but snappy attack.
- **Tuning the Bite:** If the tone feels too ice-picky, do not roll back Treble on the amp. Instead, turn your guitar's tone knob down to **7 or 8** to take the edge off the high-end spikes.
- **Dynamic Control:** Adjust the **Blend** control on **The 4th Position Compressor** to find the sweet spot for your hand's physical playing dynamics.

---

## Feedback History

### 2026-07-02 — initial
Created as the ACWX standalone counterpart to the Dire Straits Sultans Strat single-coil preset. Configured with a bright Twin-style clean amp, close-mic'd dynamic mic, high parallel compression, and dry room reverb.
