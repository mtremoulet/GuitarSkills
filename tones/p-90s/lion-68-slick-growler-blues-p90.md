---
id: "lion-68-slick-growler-blues-p90"
preset_name: "Lion '68 — Slick Growler Blues P90"
created: "2026-05-31"
updated: "2026-05-31"
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
target: "Dynamic jumped Plexi edge-of-breakup blues growl, utilizing a nested physical TONEX Klon Centaur boost driving the real Tone King Lead tube preamp."
tags: "blues, edge-of-breakup, warm, plexi, framus, p-90, lion-68, marshall, klon"
tone-king-channel: lead
amp: "Lion '68, Tone King Imperial Preamp"
status: initial
pickup_type: "p-90"
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Model: "LEAD"
    Volume I (Bite): 4.5
    Volume II (Body): 5.5
    Treble: 4.5
    Middle: 6.5
    Bass: 4.0
    Presence: 4.5
    Input Routing: "JUMP"
    Ghost Notes: "ON"
    Bright Cap: "OFF"
    Boost: "OFF"
    Cabinet: "D65"
    Room: 3.0
    Noise Gate: 18.0
  tonex_pedal:
    capture: "Klon Centaur (KC Tmid Glow)"
    guid: "569c9910-1c55-b257-047e-1ed801dcbb05"
    type: "physical_stomp_before_preamp"
    gain: 2.5
    volume: 6.5
  logic_eq:
    band1:
      on: true
      freq: 80.0
      slope: 12.0
  la2a:
    peak_reduction: 28.0
    gain: 32.0
    compress: true
  capitol_chambers:
    mix: 1.0
    pre_delay: 10.0
    decay: 1.8
---

# Lion '68 — Slick Growler Blues (P-90 Variant)

## Target Sound

This toneprint is designed for a rich, organic, and highly touch-sensitive edge-of-breakup blues tone that showcases the grit and vocal midrange of the Framus's DiMarzio P-90s. 

Rather than relying purely on software distortion, we leverage your physical signal chain's ultimate secret weapon: nesting a physical overdrive capture inside the TONEX One pedal to drive the physical tube preamp of the Tone King Lead channel, before sending that pre-saturated analog signal into the jumped-channel Marshall Plexi in Logic. 

The result is a dynamic, multi-stage analog gain cascade: soft fingerpicking remains warm and clean, while dig-in picking blooms into a thick, singing blues growl with excellent sustain and note separation.

---

## Signal Chain

### 1. TONEX One (Physical Pedal) — transparent boost boost
*   **Status:** **ACTIVE** (placed physically first, before the Tone King Preamp)
*   **Purpose:** Pushes the physical Tone King tube preamp into early saturation while retaining single-coil clarity.

| Control | Setting | Purpose |
|---------|---------|---------|
| Capture | **KC Tmid Glow** | Klon Centaur transparent overdrive capture |
| GUID | `569c9910-1c55-b257-047e-1ed801dcbb05` | Authoritative factory model ID |
| Gain | **2.5** (approx. 9:00) | Low gain; acts as a transparent, clean-to-mild boost |
| Volume | **6.5** (approx. 1:00) | High output to push the Tone King's input tube stage |

---

### 2. Tone King Imperial Preamp — physical tube pre-gain driver
*   **Status:** **ACTIVE** (Lead channel)
*   **Purpose:** Takes the Klon-boosted signal and adds organic, physical tube preamp clipping.

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Lead** | 50s Tweed + British rock character; adds rich harmonic weight |
| Volume | **2.5** | Low volume; acts as a warm analog buffer and pre-gain saturator |
| Attenuation | **6.0** | High output level driving the Audient iD14 interface |
| Tone | **5.0** | Noon (Flat EQ baseline) |
| Mid-Bite | **2.0** | Subtle upper-mid push and compression; tightens the P-90 low-end |
| Reverb / Tremolo | Off | Bypassed |
| IR | **Bypassed** | Cabinet simulation handled downstream in Logic |

---

### 3. UADx Paradise Guitar Studio: Lion '68 — jumped Plexi crunch

We load the Lion '68 within the Paradise Guitar Studio environment and select the Lead amp variant in jumped-channel routing.

| Control | Setting | Purpose |
|---------|---------|---------|
| Model | **LEAD** | Classic 100W Super Lead Plexi; bright, punchy, and aggressive |
| Input Routing | **JUMP** | **CRITICAL:** Activates jumped-channel interaction, blending both volumes |
| Volume I (Bite) | **4.5** | Adjusts high-frequency drive; adds upper-mid bite and string articulation |
| Volume II (Body) | **5.5** | Adjusts low-mid drive; adds woodiness and muscular Plexi cabinet thump |
| Treble | **4.5** | Slightly rolled back to prevent high-frequency single-coil fizz |
| Middle | **6.5** | Pushed to focus the singing, vocal throatiness of the DiMarzio P-90s |
| Bass | **4.0** | Rolled back to prevent low-end mud in the swamp ash swamp body |
| Presence | **4.5** | Softens the extreme power-amp high-frequency cap |
| Ghost Notes | **ON** | **CRITICAL:** Original transformer intermodulation adds harmonic "scream" to leads |
| Bright Cap | **OFF** | **CRITICAL:** Prevents roundwound strings from sounding glassy under gain |
| Boost | **OFF** | Bypassed (gain cascading handled physically by TONEX + Tone King) |
| Cabinet | **D65** | Custom 2x12 British 65W speakers; tight, woody, and favored by blues-rock players |
| Mic L (Left) | **Condenser 414** | Placed detailed on-axis; captures the swamp ash body's organic acoustic snap |
| Mic R (Right) | **Ribbon 121** | Placed off-axis; captures smooth, warm low-mid chest resonance |
| Room | **3.0** | Subtle room sound to place the cabinet in a natural recording space |
| Noise Gate | **18.0** | Gate engaged to suppress idle single-coil hum under dual analog gain stages |

---

### 4. Logic Channel EQ — sub-bass cleanup
Placed inline on the channel insert to keep the low end tight.

| Band | State | Frequency | Setting / Slope | Purpose |
|------|-------|-----------|-----------------|---------|
| Band 1 (Low-Cut) | ON | **80.0 Hz** | **12 dB/oct** | Filters out physical low-frequency cabinet rumble |

---

### 5. UADx LA-2A Silver Compressor — optical leveling
Placed inline after the EQ to provide warm tube compression and musical sustain.

| Control | Setting | Purpose |
|---------|---------|---------|
| Peak Reduction | **28.0** | Musical optical compression (~2-3 dB on firm digs); smooths pick transient |
| Gain | **32.0** | Balanced makeup gain |
| Mode | **Compress (3:1)** | Soft-knee optical leveling; adds natural, singing decay |

---

### 6. UADx Capitol Chambers — premium studio space (Bus Send)
Placed on a dedicated Aux Track (**Bus 3**) set to **100% Wet**. Track send level: **−16.0 dB**.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **Chamber 4** | Historic warm, deep chamber space beneath Capitol Tower |
| Speaker | **Altec 605A** | Coaxial speaker voicing with beautiful vintage midrange |
| Mic | **Unidyne 545** | Detailed dynamic mic capture |
| Mix | **Wet Solo (ON)** | 100% Wet output configuration on Bus |
| Decay | **1.8s** (approx. 11:00) | Lush, spacious room decay that blooms behind your single notes |
| Pre-Delay | **10 ms** | Natural gap letting your pick dynamics stay crisp and direct |

---

## Starting Point Guide

- **Physical Guitar Setup:** Switch your Framus to the **Neck/Bridge blend** (middle rotary position) for a beautifully balanced, wide, and snappy rhythm tone. For crying, singing blues leads, switch to the **Neck P-90** and roll the guitar's Tone knob to **7** (our classic **7/7 Baseline**).
- **Gain Staging Interaction:** This setup is incredibly touch-sensitive. If you want a perfectly clean tone, simply pick lighter or roll your guitar's Volume knob back to **6**. When you need a singing solo voice, push your guitar Volume to **8 or 9** and dig in with your pick.
- **Bigsby vibrato:** Let a chord ring out, let the physical tube preamp and the LA-2A compress and sustain the notes, and use your Bigsby arm for slow, expressive pitch sweeps that bloom beautifully in the Capitol Chambers decay.

---

## Feedback History

### 2026-05-31 — initial
Created as the initial "Slick Growler" edge-of-breakup blues toneprint for the Framus Earl Slick Artist Series and its DiMarzio P-90s. Implements a multi-stage gain cascade: physical TONEX One pedal running Klon Centaur stomp capture physically driving the Tone King Lead preamp channel, leading into the jumped-channel LEAD model of the UADx Lion '68 inside Paradise Guitar Studio. Post-processing includes an 80 Hz low-cut, LA-2A Silver leveling, and Capitol Chambers reverb on Bus 3.
