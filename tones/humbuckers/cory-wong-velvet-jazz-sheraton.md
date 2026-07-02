---
amp: "The Clean Machine (Archetype Cory Wong X)"
created: 2026-07-02
guitar: "Epiphone Sheraton II (neck humbucker, flatwounds)"
id: cory-wong-velvet-jazz-sheraton
pickup_type: humbucker
preset_name: "Velvet Jazz Sheraton ACWX"
status: initial
tags: "boutique, clean, warm, humbucker, flatwounds, jazz, bossa, neural-dsp, cory-wong"
target: "Pristine, high-fidelity jazz clean using Archetype Cory Wong X's Clean Machine — warm, articulate humbucker response with flatwound smoothness and optical leveling."
tone-king-channel: bypassed
updated: 2026-07-02
preset_data:
  amp_platform: neural_dsp
  amp_settings:
    ampCabLinkedState: false
    bigRigActive: false
    chorusActive: false
    delayActive: false
    leftCab0MicType: 4
    leftCabActive: true
    leftCabDistance: 0.25
    leftCabPosition: 0.48
    leftRoomMicLevel: -28.0
    postalActive: false
    rightCabActive: false
    selectedAmp: 1
    selectedCab: 2
    compressorActive: true
    compressorVolume: 55.0
    compressorCompression: 30.0
    compressorTone: 45.0
    compressorBlend: 45.0
    cleanVolume: 30.0
    cleanBright: false
    cleanBass: 45.0
    cleanMid: 65.0
    cleanTreble: 40.0
    cleanPresence: 50.0
    cleanOutputLevel: 70.0
    cleanEQActive: true
    cleanEQHpf: 20.0
    cleanEQLpf: 20000.0
    cleanEQBand1: 0.0
    cleanEQBand2: -0.5
    cleanEQBand3: -2.0
    cleanEQBand4: 1.5
    cleanEQBand5: 1.0
    cleanEQBand6: -1.0
    cleanEQBand7: -1.5
    cleanEQBand8: 0.0
    cleanEQBand9: 0.0
    tuberActive: false
    washActive: true
    washMix: 15.0
    washDecay: 35.0
    washShimmer: false
---

# Velvet Jazz Sheraton — Archetype Cory Wong X

## Target Sound

This toneprint is the Archetype Cory Wong X (ACWX) standalone equivalent of the **Puretone Velvet Jazz** preset, optimized for your **Epiphone Sheraton II** strung with flatwound strings. 

The goal is an upscale, high-fidelity jazz clean that keeps complex chord voicings and shell voicings perfectly articulate with zero muddy buildup. We use **"The Clean Machine"** amp model for its high-headroom, American clean platform, but we compensate for its natural mid-scoop by pushing the amp's midrange control and adding a subtle graphic EQ boost in the woody vocal frequencies (500 Hz and 1 kHz).

To mimic the optical leveling of the LA-2A Silver compressor, we engage **"The 4th Position Compressor"** with a moderate compression setting and a 45% parallel blend. This maintains your natural finger/pick attack while gluing chord changes together. The signal is rounded out with a warm Ribbon 121 mic model on a boutique open-back cab, and a touch of the integrated **"The Wash"** Reverb to provide natural acoustic bloom.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom).

---

### 2. Archetype Cory Wong X — standalone channel strip

This self-contained suite provides all necessary dynamics, tone shaping, and spatial effects.

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 4th Position Compressor** | **Active** | **ON** | Essential parallel optical-style leveling |
| | **Blend** | **45%** | Preserves immediate pick attack while smoothing tails |
| | **Tone** | **45%** | Slightly rolled back to sweeten high-end transients |
| | **Compression**| **30%** | Moderate leveling depth |
| | **Volume** | **55%** | Calibrated for unity gain through the pedal |

*All other Pre FX are bypassed.*

**Amp Section — "The Clean Machine"**

All parameters are specified in percentages (0–100%).

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Clean Machine** | High-headroom tube clean platform |
| Volume (Gain) | **30%** | Clean preamp setting; maintains pure headroom |
| Bright Switch | **OFF** (Down) | Keeps flatwound strings warm and smoky |
| Bass | **45%** | Slightly rolled back to prevent low-end mud on the neck humbucker |
| Middle | **65%** | **Jazz Middle Rule**: Fills in the midrange scoop of the Fender model |
| Treble | **40%** | Gently rolled back to smooth out the top end |
| Presence | **50%** | Neutral power amp high end |
| Output | **70%** | Plugin level output trim |

**Cab Section (Unlinked Cabinets)**

We unlink the cabinets to pair the Clean Machine with the warm, vintage-voiced boutique cabinet from the Amp Snob.

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **Off** | Allows custom cab/mic combinations |
| Cab Type | **Snob** | 2x12 boutique open-back cabinet |
| Cab L | **Active** | Primary mic slot |
| Mic L Type | **Ribbon 121** | Creamy, warm mic; rolls off high-end fizz and fattens low-mids |
| Position L | **0.48** | Off-center of the speaker cone for warm definition |
| Distance L | **0.25** | Close-mic'd with room to let the low-end bloom breathe |
| Room Send L | **−28.0 dB** | Low send level to keep the core sound dry and focused |
| Cab R | **BYPASSED** | Single mic setup for phase coherence |

**EQ Section (Clean Machine 9-Band Graphic EQ)**

| Band | Setting | Purpose |
|------|---------|---------|
| EQ Status | **Active** | Core corrective shaping for humbucker jazz |
| 65 Hz | 0.0 dB | Neutral |
| 125 Hz | −0.5 dB | Subtle cleanup of sub-bass resonance |
| 250 Hz | −2.0 dB | **Targeted cut**: Cleans up muddy build-up from the neck humbucker |
| 500 Hz | +1.5 dB | Boosts lower midrange woody warmth |
| 1 kHz | +1.0 dB | Adds chord presence and definition |
| 2 kHz | −1.0 dB | Smooths out pick-attack transients |
| 4 kHz | −1.5 dB | Gently rounds off the high-end air |
| 8 kHz | 0.0 dB | Neutral |
| 16 kHz | 0.0 dB | Neutral |
| HPF / LPF | Default | 20 Hz High-Pass / 20.0 kHz Low-Pass |

**Post FX Section**

*Chorus and Delay are **BYPASSED**.*

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The Wash** | **Active** | **ON** | Integrated room reverb |
| | **Mix** | **15%** | Intimate room depth |
| | **Decay** | **35%** | Short, warm room space |
| | **Shimmer** | **OFF** | Bypassed for traditional jazz styles |
| | **Low Cut** | **120 Hz** | Prevents low-frequency build-up in the reverb trail |
| | **High Cut** | **4.5 kHz** | Keeps the reverb space dark and warm |

---

## Starting Point Guide

- **Neck Pickup Selection:** Select the neck humbucker on your Sheraton II. Roll the guitar volume knob back to **8** and the tone knob to **7** to sweeten the transients and highlight the flatwound character.
- **Adjusting the Feel:** To alter the touch-sensitivity of your picking hand, tweak the **Blend** control on **The 4th Position Compressor**. At **30%**, it is highly dynamic. At **50%**, it provides a thicker, more even "velvet" response.
- **Midrange Control:** If the Sheraton sounds too "boxy," pull the amp's **Middle** control back to **55%**. If you need more vocal cut, push the **1 kHz** slider on the Graphic EQ to **+2.0 dB**.

---

## Feedback History

### 2026-07-02 — initial
Created as the ACWX standalone counterpart to the Puretone Velvet Jazz Sheraton preset. Modeled on "The Clean Machine" with corrective mid-boost EQ, parallel optical compression, a Ribbon 121 mic model, and warm room reverb.
