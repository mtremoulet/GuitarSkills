---
id: lion-68-royal-velvet-jazz-p90-faust
preset_name: "Lion '68 — Royal Velvet Jazz P90 (Faust Augmented)"
created: "2026-09-07"
updated: "2026-09-07"
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
genre: jazz
amp: "Lion '68 (UADx)"
status: tested
pickup_type: p-90
tags: "jazz, clean, warm, plexi, framus, p-90, lion-68, marshall, faust, stumblelater, liberty-burnisher"
target: 'Warm, woody Marshall Plexi high-headroom jazz clean optimized for P-90 detail, augmented by Faust Liberty Burnisher harmonic polish and Stumblelater tube buffer smoothing.'
tone-king-channel: bypassed
preset_data:
  amp_platform: uad_paradise
  faust_pedals: "Liberty Burnisher, Stumblelater"
  amp_settings:
    Bass: 4.5
    Boost: false
    Bright Cap: N/A
    Cabinet: EV12
    Ghost Notes: OFF
    Input Routing: LOW
    Middle: 7.5
    Model: BASS
    Noise Gate: 12.0
    Presence: 4.0
    Room: 2.5
    Treble: 4.5
    Volume I (Bite): 3.0
    Volume II (Body): 5.0
  hitsville:
    decay: 1.8
    mix: 0.12
    pre_delay: 15.0
    wet_solo: false
  la2a:
    compress: true
    gain: 23.0
    peak_reduction: 32.0
---

# Lion '68 — Royal Velvet Jazz P90 (Faust Augmented)

## Target Sound

This toneprint enhances the woody, vintage Marshall Plexi jazz clean of the **Lion '68 Royal Velvet Jazz P90** by prepending two specialized Faust virtual analog circuits:
1. **Liberty Burnisher**: Adds discrete Germanium/Silicon harmonic sheen, enhancing the woody acoustic-like chime of the Framus P-90 neck pickup without harshness.
2. **Stumblelater**: Emulates the Dumble ABL passive send attenuator and Class-A tube recovery stage, giving luxurious pick-velocity response and velvety bloom to complex chord melody extensions.

Downstream, the **UADx Lion '68** (Super Bass mode with EV12 cab) delivers a rich, dimensional mid-forward jazz foundation, dynamically polished by the **LA-2A Silver** optical compressor and placed inside the warm confines of **Hitsville Reverb Chambers**.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (gain set to 0).

---

### 2. Faust Virtual Analog Front-End

#### Module 1: Liberty Burnisher
* **Heritage:** Discrete harmonic polisher & Baxandall treble/mid booster.
* **Role:** Enhances pick transient definition and note separation across multi-voice jazz voicings.

#### Module 2: Stumblelater
* **Heritage:** Dumble ABL tube loop buffer & recovery gain stage.
* **Role:** Buffers and rounds the high frequencies, delivering touch-sensitive elastic sag under fingers.

---

### 3. UADx Paradise Guitar Studio / Lion '68 — Super Bass Clean Foundation

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Model** | `BASS` | 1968 Marshall Super Bass circuit (high headroom, round low end). |
| **Input Routing** | `LOW` | P-90 headroom optimization; prevents premature preamp breakup. |
| **Volume I (Bite)**| `3.0` | High-treble channel dialed back to avoid P-90 bite fatigue. |
| **Volume II (Body)**| `5.0` | Normal channel for woody lower-mid weight and body. |
| **Bass** | `4.5` | Controlled low-end response through semi-hollow P-90s. |
| **Middle** | `7.5` | Rich harmonic core for chord melodies. |
| **Treble** | `4.5` | Smooth, non-fatiguing top end. |
| **Presence** | `4.0` | Open air without aggressive edge. |
| **Cabinet** | `EV12` | Electro-Voice EVM12L high-headroom uncolored jazz definition. |
| **Room** | `2.5` | Subtle amp room ambience. |

---

### 4. Post-Amp Dynamic Smoothing: UADx Teletronix LA-2A Silver

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Mode** | `Compress` | Gentle optical peak leveling. |
| **Peak Reduction** | `32.0` | 2–3 dB of gentle optical squeeze on chord accents. |
| **Gain** | `23.0` | Studio makeup gain. |

---

### 5. Acoustic Space: UADx Hitsville Reverb Chambers

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Decay** | `1.8s` | Tight vintage chamber decay. |
| **Mix** | `12%` | Intimate club air without washing out complex chord voicings. |
| **Pre-Delay** | `15.0 ms` | Keeps direct pick attack immediate. |
