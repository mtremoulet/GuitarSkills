---
amp: "The Clean Machine (Archetype Cory Wong X)"
created: 2026-07-02
guitar: "Fender Player II Telecaster / Squier Stratocaster"
id: cory-wong-soejima-neo-soul
pickup_type: single-coil
preset_name: "Soejima Neo-Soul Clean ACWX"
status: initial
tags: "neo-soul, clean, warm, compressed, chorus, delay, reverb, single-coil, neural-dsp, cory-wong"
target: "Toshiki Soejima-style warm, compressed, and articulate neo-soul clean tone for single-coils using a simulated Jan Ray boost, Clean Machine, compression, chorus, delay, and reverb in ACWX."
tone-king-channel: bypassed
updated: 2026-07-02
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: false
    bigRigActive: false
    chorusActive: true
    chorusMix: 25.0
    chorusRate: 1.2
    chorusWidth: 50.0
    delayActive: true
    delayMix: 20.0
    delayFeedback: 15.0
    delayTimeL: 350.0
    delayTimeR: 350.0
    delayMode: 0
    leftCab0MicType: 4
    leftCabActive: true
    leftCabDistance: 0.20
    leftCabPosition: 0.45
    leftRoomMicLevel: -28.0
    postalActive: false
    rightCabActive: false
    selectedAmp: 1
    selectedCab: 1
    compressorActive: true
    compressorVolume: 55.0
    compressorCompression: 45.0
    compressorTone: 55.0
    compressorBlend: 50.0
    cleanVolume: 32.0
    cleanBright: false
    cleanBass: 48.0
    cleanMid: 55.0
    cleanTreble: 45.0
    cleanPresence: 50.0
    cleanOutputLevel: 65.0
    cleanEQActive: true
    cleanEQHpf: 20.0
    cleanEQLpf: 20000.0
    cleanEQBand1: 0.0
    cleanEQBand2: 0.0
    cleanEQBand3: -1.0
    cleanEQBand4: 1.0
    cleanEQBand5: 1.5
    cleanEQBand6: -1.0
    cleanEQBand7: 0.0
    cleanEQBand8: 0.0
    cleanEQBand9: 0.0
    tuberActive: true
    tuberDrive: 5.0
    tuberLevel: 60.0
    tuberTone: 45.0
    washActive: true
    washMix: 22.0
    washDecay: 40.0
    washShimmer: false
---

# Soejima Neo-Soul Clean — Archetype Cory Wong X

## Target Sound

This toneprint is the Archetype Cory Wong X (ACWX) standalone equivalent of the **Soejima Neo-Soul Clean** preset, optimized for single-coil pickups (like the Fender Player II Telecaster or Squier Stratocaster).

Soejima's signature sound relies on heavy compression, warm lower-mids to counteract single-coil "glassiness," and a lush spatial halo. To emulate the physical Vemuram Jan Ray boost, we engage **"The Tuber"** overdrive pedal set to a very clean, high-output level (**5% Drive, 60% Level**). This adds warm harmonic saturation and slight compression to the front end of **"The Clean Machine"** amp.

We use **"The 4th Position Compressor"** with a 50% parallel blend and 45% compression for that classic percussive, snappy "pop." We then stack **"The 80s"** Chorus (subtle Dimension D mode emulation), the **Delay-Y-Y** (slapback tape delay), and **"The Wash"** Reverb internally to create the deep, spacious modern neo-soul vibe, completely DAW-free.

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
| **The 4th Position Compressor** | **Active** | **ON** | Optical-style compression for percussive neo-soul pop |
| | **Blend** | **50%** | Parallel mix; balances direct transient punch with compressed bloom |
| | **Tone** | **55%** | Keeps the high-end snap present |
| | **Compression**| **45%** | Deeper compression level for standard R&B/neo-soul squash |
| | **Volume** | **55%** | Unity level |
| **The Tuber** | **Active** | **ON** | **Jan Ray Emulation**: Acts as an always-on tube sweetener |
| | **Drive** | **5%** | Pristine clean saturation; no harsh clipping |
| | **Level** | **60%** | Pushes the front of the Clean Machine amp for sustain |
| | **Tone** | **45%** | Slightly rolled back to prevent single-coil harshness |

*All other Pre FX (Envelope Filter, Big Rig OD) are bypassed.*

**Amp Section — "The Clean Machine"**

All parameters are specified in percentages (0–100%).

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Clean Machine** | Twin Reverb high-headroom platform |
| Volume (Gain) | **32%** | Input gain calibrated for single-coil headroom |
| Bright Switch | **OFF** | Smooths out pick transients |
| Bass | **48%** | Controlled low end |
| Middle | **55%** | Slightly pushed to fill in Fender mid-scoop |
| Treble | **45%** | Smooth, rounded high end |
| Presence | **50%** | Neutral power amp presence |
| Output | **65%** | Output volume level trim |

**Cab Section (Unlinked Cabinets)**

We unlink the cabinets to pair the Clean Machine with a warm mic arrangement.

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **Off** | Unlinked for custom mic placement |
| Cab Type | **Clean** | Matching 2x12 open-back cabinet |
| Cab L | **Active** | Primary mic |
| Mic L Type | **Ribbon 121** | Rounds off high-end transients and fattens low-mids |
| Position L | **0.45** | Balanced placement for note articulation |
| Distance L | **0.20** | Direct mic'ing with standard air |
| Room Send L | **−28.0 dB** | Low send to prevent room mud |
| Cab R | **BYPASSED** | Mono phase-coherence |

**EQ Section (Clean Machine 9-Band Graphic EQ)**

| Band | Setting | Purpose |
|------|---------|---------|
| EQ Status | **Active** | Corrective curves for single-coils |
| 65 Hz | 0.0 dB | Neutral |
| 125 Hz | 0.0 dB | Neutral |
| 250 Hz | −1.0 dB | Cleans up muddy build-up from neck/middle positions |
| 500 Hz | +1.0 dB | Boosts lower midrange body |
| 1 kHz | +1.5 dB | Highlight vocal midrange presence for chord solos |
| 2 kHz | −1.0 dB | Smooths out high pick click |
| 4 kHz | 0.0 dB | Neutral |
| 8 kHz | 0.0 dB | Neutral |
| 16 kHz | 0.0 dB | Neutral |
| HPF / LPF | Default | 20 Hz High-Pass / 20.0 kHz Low-Pass |

**Post FX Section**

All post-effects are active to build the characteristic spacious "halo."

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 80s (Chorus)** | **Active** | **ON** | Dimension D style stereo thickening |
| | **Mix** | **25%** | Subtle thickening; no obvious pitch warble |
| | **Rate** | **1.2 Hz** | Slow, lush sweep |
| | **Width** | **50%** | Standard stereo spread |
| **Delay-Y-Y** | **Active** | **ON** | Integrated tape delay emulation |
| | **Mix** | **20%** | Subtle repeats sitting behind the note |
| | **Feedback** | **15%** | Tight slapback (1–2 repeats) |
| | **Time L/R** | **350 ms** | 1/8 note host sync/slapback speed |
| | **Mode** | **Single** | Clean, central delay repeats |
| **The Wash** | **Active** | **ON** | Lush room reverb |
| | **Mix** | **22%** | Intimate room presence |
| | **Decay** | **40%** | Moderate decay to let notes float |
| | **Shimmer** | **OFF** | Bypassed for organic soul tone |

---

## Starting Point Guide

- **Physical Setup:** Select Strat Position 4 (bridge + middle) or Tele neck pickup. Play with your guitar volume at **8** and tone at **7** (the "7/7 Baseline") to optimize input dynamics and sweeten high-frequency transients.
- **Taming the Compression:** If you pick aggressively and the compressor feels too squashed, roll the **Compression** dial down to **35%** or pull the **Blend** to **40%**.
- **Adjusting Modulation:** To get a drier, more direct rhythm tone, bypass **The 80s** Chorus pedal while leaving the delay and reverb active.

---

## Feedback History

### 2026-07-02 — initial
Created as the ACWX standalone counterpart to the Soejima Neo-Soul Clean single-coil preset. Integrates clean TS-style front-end boost, Clean Machine amp, parallel compression, chorus, slapback delay, and reverb.
