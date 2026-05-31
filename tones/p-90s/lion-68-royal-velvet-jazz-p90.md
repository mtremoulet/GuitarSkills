---
id: "lion-68-royal-velvet-jazz-p90"
preset_name: "Lion '68 — Royal Velvet Jazz P90"
created: "2026-05-30"
updated: "2026-05-30"
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
target: "Warm, woody Marshall Plexi high-headroom jazz clean optimized for P-90 detail, touch-sensitive Dumble-style pre-compression, and a vintage chamber room."
tags: "jazz, clean, warm, plexi, framus, p-90, lion-68, marshall, dumble"
tone-king-channel: rhythm
amp: "Lion '68, Tone King Imperial Preamp"
genre: "jazz"
status: initial
pickup_type: "p-90"
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Model: "BASS"
    Volume I (Bite): 3.0
    Volume II (Body): 5.0
    Treble: 4.5
    Middle: 7.5
    Bass: 4.5
    Presence: 4.0
    Input Routing: "LOW"
    Ghost Notes: "OFF"
    Bright Cap: "N/A"
    Boost: "OFF"
    Cabinet: "EV12"
    Room: 2.5
    Noise Gate: 12.0
  tonex:
    capture: "SSS SRV AlmostClean"
    guid: "c823f6ce-6820-1fe7-7000-3d20f31add5a"
    gain: 3.0
    volume: 6.0
    bass: 5.0
    mid: 6.0
    treble: 4.5
  logic_eq:
    band1:
      on: true
      freq: 80.0
      slope: 12.0
    band4:
      on: true
      freq: 650.0
      gain: -1.5
      q: 1.5
    band8:
      on: true
      freq: 4500.0
      slope: 24.0
  la2a:
    peak_reduction: 25.0
    gain: 35.0
    compress: true
  hitsville:
    mix: 1.0
    pre_delay: 15.0
    decay: 1.5
---

# Lion '68 — Royal Velvet Jazz (P-90 Variant)

## Target Sound

This toneprint turns the Marshall Super Lead Plexi (specifically the Super Bass variant inside Paradise Guitar Studio) into a stunning, high-fidelity clean jazz platform. While Marshalls are rarely the first choice for jazz, their massive power section headroom (100W running EL34s) delivers a tight, robust transient response that keeps complex chords and close-interval voicings perfectly clear and articulate. Combined with the mid-forward voicing of a Marshall, this toneprint delivers a gorgeous, woody "thump" with beautiful vocal warmth.

To optimize this for the Framus Earl Slick Artist Series and its DiMarzio P-90s:
1.  **Tube Preamp Buffer:** We use the physical Tone King Rhythm channel set to its "Transparency Floor" (Volume **2.0**, Attenuation **5.0**) as an analog tube buffer. This sweetens the single-coil direct signal, preventing it from sounding clinical before it hits Logic.
2.  **Dumble-style Pre-compression:** We run the virtual TONEX plugin in Logic loaded with a **Vertex SSS SRV (Steel String Supreme)** stomp capture. This adds subtle, glassy tube sag and dynamic compression that responds beautifully to delicate fingerpicking.
3.  **Super Bass Platform:** We load the **BASS model** of the Lion '68 using the **LOW input routing**. This provides the cleanest, roundest, and least aggressive voicing, and naturally removes the bright cap to keep the P-90 single coils smooth.
4.  **Jazz Middle Push:** Following the "Jazz Middle Rule," we push the amp's Middle control to **7.5** to fill in the midrange scoop, while applying the **"High-Cut Veil"** at **4.5 kHz** via Logic's EQ to round off modern transient click and simulate a classic vintage jazz box.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **ACTIVE** (analog tube buffer stage)
*   **Purpose:** Enriches the Framus's direct signal with warm tube character and dynamic sensitivity.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Rhythm** | 60s Blackface character; clean, natural baseline |
| Volume | **2.0** | Transparency zone; keeps the preamp clean and dynamic |
| Attenuation | **5.0** | Unity output level driving the Audient iD14 |
| Bass | **5.0** | Noon (Flat EQ response) |
| Treble | **5.0** | Noon (Flat EQ response) |
| Reverb / Tremolo | Off | Bypassed |
| IR | **Bypassed** | Cabinet simulation handled downstream in Logic |

---

### 2. IK Multimedia TONEX (Plugin) — Dumble-style pre-compression
Placed as the first insert on the Logic channel to shape the direct tube signal.

| Control | Setting | Purpose |
|---------|---------|---------|
| Capture | **SSS SRV AlmostClean** | Vertex Steel String Supreme; Dumble-style glassiness and body |
| GUID | `c823f6ce-6820-1fe7-7000-3d20f31add5a` | Authoritative factory model ID |
| Gain | **3.0** | Kept low; acts as a clean boost and light optical-like leveler |
| Volume | **6.0** | Balanced output level |
| Bass | **5.0** | Neutral low end |
| Mid | **6.0** | Subtle mid push to round out single-coil thunk |
| Treble | **4.5** | Slightly rolled back to prevent high-frequency glassiness |

---

### 3. UADx Paradise Guitar Studio: Lion '68 — high-headroom platform

We load the Lion '68 within the Paradise Guitar Studio environment and select the Bass amp variant.

| Control | Setting | Purpose |
|---------|---------|---------|
| Model | **BASS** | Classic 100W Super Bass; smooth, warm, and highly pedal-friendly |
| Input Routing | **LOW** | **CRITICAL:** Utilizes Low inputs for a cleaner, darker, and rounder response |
| Volume I (Bite) | **3.0** | High-frequency channel; kept low to maintain crystal-clean headroom |
| Volume II (Body) | **5.0** | Low-frequency channel; turned up to provide full, woody bass character |
| Treble | **4.5** | Rolled back to smooth out the DiMarzio neck P-90's high end |
| Middle | **7.5** | **CRITICAL:** Pushed to satisfy the "Jazz Middle Rule," giving rich midrange body |
| Bass | **4.5** | Pulled back slightly to prevent low-end mud in the swamp ash body |
| Presence | **4.0** | Smooths power amp brilliance; rounds off transient "click" |
| Ghost Notes | **OFF** | Eliminates intermodulation hum for a modern, quiet clean floor |
| Bright Cap | **N/A** | Bypassed by default on Bass model (protects P-90s from harshness) |
| Boost | **OFF** | Bypassed (pre-comp handled by the TONEX Vertex SSS capture) |
| Cabinet | **EV12** | 200W Electro-Voice EVM12L 1x12; tight bottom-end and focused single-speaker thump |
| Room | **2.5** | Subtle studio room microphones blend to add space without muddying |
| Noise Gate | **12.0** | Light gate engaged to quiet idle single-coil hum |

---

### 4. Logic Channel EQ — surgical shaping & "High-Cut Veil"
Placed inline on the channel insert to remove muddy sub-lows and round off modern digital fizz.

| Band | State | Frequency | Setting / Slope | Purpose |
|------|-------|-----------|-----------------|---------|
| Band 1 (Low-Cut) | ON | **80.0 Hz** | **12 dB/oct** | Filters out sub-frequency mud and low-end rumble |
| Band 4 (Peak) | ON | **650.0 Hz** | **−1.5 dB** (Q: 1.5) | Gentle cut to clear up nasal cabinet honk |
| Band 8 (High-Cut) | ON | **4500.0 Hz** | **24 dB/oct** | **CRITICAL:** Engaging the "High-Cut Veil" to round off transients |

---

### 5. UADx LA-2A Silver Compressor — optical leveling
Placed inline after the EQ to provide warm tube leveling and musical dynamics.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | **25.0** | Smooth, program-dependent optical leveling (~2 dB on firm chords) |
| Gain | **35.0** | Balanced makeup gain |
| Mode | **Compress (3:1)** | Soft-knee optical leveling; keeps the jazz rhythm perfectly even |

---

### 6. UADx Hitsville Reverb Chambers — vintage room (Bus Send)
Placed on a dedicated Aux Track (**Bus 3**) set to **100% Wet** to preserve dry transient punch. Track send level: **−14.0 dB**.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2644 (Chamber 2)** | Pentagonal room; extremely smooth, warm, and natural decay envelope |
| Speaker | **Altec 605A** | Classic vintage duplex cabinet (15" woofer + integrated horn) exclusive to Chamber 2 |
| Mic | **Neumann KM86** | Multi-pattern small-diaphragm condenser (Blumlein figure-8 pair) exclusive to Chamber 2 |
| Mix | **Wet Solo (ON)** | 100% Wet output configuration on Bus |
| Decay | **1.5s** (approx. 10:00) | Short, intimate room space that provides three-dimensional depth |
| Pre-Delay | **15 ms** | Natural gap letting the P-90 neck pick-attack stay completely dry and centered |

---

## Starting Point Guide

- **Physical Guitar Setup:** Switch your Framus to the **Neck P-90** pickup. Roll the guitar's physical Volume knob to **8** and the Tone knob to **7** (complying with the "7/7 Baseline"). This rolls off raw direct bite, sweetening the signal.
- **Adjusting the Warmth:** If the tone feels too dark under late-night monitoring on your Sennheiser HD660S2s, do not increase the amp Treble; instead, raise the **High-Cut frequency** on Logic's EQ from `4.5 kHz` to `5.2 kHz`.
- **String Interaction:** This setup is voiced beautifully for both flatwounds and roundwounds (like your Rotosound Yellows). The combination of the LOW-input Bass model, EV12 cab, and the 4.5 kHz high-cut keeps the roundwounds feeling highly warm and woody.

---

## Feedback History

### 2026-05-30 — initial
Created as the initial "Royal Velvet" jazz clean toneprint for the Framus and its DiMarzio P-90s. Employs the physical Tone King Rhythm channel as an active tube buffer, the TONEX plugin running the Vertex SSS SRV stomp capture in Logic for pre-compression, and UADx Lion '68 set to the Bass model with LOW input routing inside Paradise Guitar Studio. Post-processing includes an EQ "High-Cut Veil" at 4.5 kHz, LA-2A Silver optical glue, and Hitsville Reverb on Bus 3.
