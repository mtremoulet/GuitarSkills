---
amp: "Lion '68 (UADx)"
created: 2026-05-30
genre: jazz
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
id: lion-68-royal-velvet-jazz-p90
pickup_type: p-90
preset_name: "Lion '68 — Royal Velvet Jazz P90"
status: tested
tags: "jazz, clean, warm, plexi, framus, p-90, lion-68, marshall, dumble"
target: 'Warm, woody Marshall Plexi high-headroom jazz clean optimized for P-90 detail, touch-sensitive Dumble-style pre-compression, and a vintage chamber room.'
tone-king-channel: bypassed
updated: 2026-08-30
preset_data:
  amp_platform: uad_paradise
  prefx:
    slot1:
      pedal: gold_overdrive
      enabled: false
      gain: 1.0
      output: 3.0
      treble: 4.5
    slot2:
      pedal: ts_overdrive
      enabled: false
      overdrive: 1.0
      tone: 2.5
      level: 5.8
    slot3:
      pedal: nashville_overdrive
      enabled: false
      drive: 5.9
      spectrum: 4.0
      level: 7.2
      bass: 10.0
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
  logic_eq:
    band1:
      freq: 80.0
      on: true
      slope: 12.0
    band4:
      freq: 650.0
      gain: -1.5
      on: true
      q: 1.5
    band8:
      freq: 4500.0
      on: true
      slope: 24.0
---

# Lion '68 — Royal Velvet Jazz (P-90 Variant)

## Target Sound

This toneprint turns the Marshall Super Lead Plexi (specifically the Super Bass variant inside Paradise Guitar Studio) into a stunning, high-fidelity clean jazz platform. While Marshalls are rarely the first choice for jazz, their massive power section headroom (100W running EL34s) delivers a tight, robust transient response that keeps complex chords and close-interval voicings perfectly clear and articulate. Combined with the mid-forward voicing of a Marshall, this toneprint delivers a gorgeous, woody "thump" with beautiful vocal warmth.

To optimize this for the Framus Earl Slick Artist Series and its DiMarzio P-90s:
1.  **Tube Preamp Buffer:** We use the physical Tone King Rhythm channel set to its "Transparency Floor" (Volume **2.0**, Attenuation **5.0**) as an analog tube buffer. This sweetens the single-coil direct signal, preventing it from sounding clinical before it hits Logic.
2.  **Pre-FX Drive Palette:** Pre-configured with three complementary, switchable pre-amp overdrive/boost flavors inside Paradise Guitar Studio (all bypassed by default):
    *   **Gold Overdrive (Klon):** Transparent clean boost / harmonic sweetener.
    *   **TS Overdrive (Tube Screamer):** Mid-focused vocal push with smooth, rounded high end.
    *   **Nashville Overdrive (Nobels ODR-1):** Open, uncompressed amp-like drive with warm Spectrum voicing.
3.  **Super Bass Platform:** We load the **BASS model** of the Lion '68 using the **LOW input routing**. This provides the cleanest, roundest, and least aggressive voicing, and naturally removes the bright cap to keep the P-90 single coils smooth.
4.  **Jazz Middle Push:** Following the "Jazz Middle Rule," we push the amp's Middle control to **7.5** to fill in the midrange scoop, while applying the **"High-Cut Veil"** at **4.5 kHz** via Logic's EQ to round off modern transient click and simulate a classic vintage jazz box.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).


### 2. UADx Paradise Guitar Studio: Lion '68 — high-headroom platform

We load the Lion '68 within the Paradise Guitar Studio environment and select the Bass amp variant.

#### Pre-FX Palette (Slots 1–3)

All three pedals are loaded in the Pre-FX pedalboard and set to **Bypassed** by default so the core jazz clean is pristine. Engage individually as desired for different solo and rhythm flavors:

| Slot | Pedal Model | State | Settings | Musical Character & Role |
|------|-------------|-------|----------|--------------------------|
| **Pre-FX 1** | **Gold Overdrive** *(Klon)* | **Disabled** (Off) | Gain **1.0**, Treble **4.5**, Output **3.0** | **Transparent Clean Boost / Sweetener:** Adds subtle diode thickness and sustain without coloring the Marshall Super Bass response. |
| **Pre-FX 2** | **TS Overdrive** *(Tube Screamer)* | **Disabled** (Off) | Overdrive **1.0**, Tone **2.5**, Level **5.8** | **Smooth Vocal Mid-Push:** Mild drive with the Tone rolled back to 2.5 to tame harsh bite on the neck P-90 while punching through in a mix. |
| **Pre-FX 3** | **Nashville Overdrive** *(Nobels ODR-1)* | **Disabled** (Off) | Drive **5.9**, Spectrum **4.0**, Level **7.2**, Bass **10.0** | **Natural Open Amp Breakup:** Rich, singing drive. The **Spectrum** control at **4.0** warms up the lower-mids (~500 Hz) while rolling back glassy highs for an exceptionally musical, creamy overdrive. |

---

#### Amp Settings

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
| Peak Reduction | **32.0** | Program-dependent optical leveling (~2–3 dB on firm chords) for extra warmth and dynamic glue |
| Gain | **23.0** | Balanced makeup gain matched to the 32.0 peak reduction setting |
| Mode | **Compress (3:1)** | Soft-knee optical leveling; keeps the jazz rhythm perfectly even |

---

### 6. UADx Hitsville Reverb Chambers — vintage room (Bus Send)
Placed inline as post-amp studio chamber ambience (Wet Solo **OFF**, Mix **12%**) to provide natural three-dimensional depth in both Standalone rack and Logic channel strips.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2644 (Chamber 2)** | Pentagonal room; extremely smooth, warm, and natural decay envelope |
| Speaker | **Altec 605A** | Classic vintage duplex cabinet (15" woofer + integrated horn) exclusive to Chamber 2 |
| Mic | **Neumann KM86** | Multi-pattern small-diaphragm condenser (Blumlein figure-8 pair) exclusive to Chamber 2 |
| Mix | **12% (0.12)** | Serial insert blend — calibrated for Standalone rack & Logic channel |
| Decay | **1.8s** (natural decay) | Intimate chamber space halved from 3.6s for tighter chord clarity and definition |
| Pre-Delay | **15 ms** | Natural gap letting the P-90 neck pick-attack stay completely dry and centered |

---

## Starting Point Guide

- **Physical Guitar Setup:** Switch to the **Neck P-90** pickup. Roll the guitar's physical Volume knob to **7–8** (or **3–5** on hot/vintage-wind P-90s) and Tone knob to **6–7** to roll off raw direct bite.
- **Hardware D.I. Calibration:** When plugging direct into the Audient iD14 JFET D.I., dial back the plugin host / DAW track input trim by **−3.2 dB** to offset the hot instrument input and align with UAD modeling reference specs.
- **Taming Breakup on Warmer / Hotter P-90s (e.g. Tonerider Rebel 90s):** If the high-inductance low-mid energy pushes the amp into edge-of-breakup fur, nudge Lion '68 **Volume II (Body)** down from `5.0` to **`3.5 – 4.0`**, and bump **Volume I (Bite)** up to **`3.5`** to retain articulation.
- **Adjusting the Warmth:** If the tone feels too dark under late-night monitoring on your Sennheiser HD660S2s, do not increase the amp Treble; instead, raise the **High-Cut frequency** on Logic's EQ from `4.5 kHz` to `5.2 kHz`.
- **String Interaction:** This setup is voiced beautifully for both flatwounds and roundwounds (like your Rotosound Yellows). The combination of the LOW-input Bass model, EV12 cab, and the 4.5 kHz high-cut keeps the roundwounds feeling highly warm and woody.

---

## Feedback History

### 2026-05-30 — initial
Created as the initial "Royal Velvet" jazz clean toneprint for the Framus and its DiMarzio P-90s. Employs the physical Tone King Rhythm channel as an active tube buffer, the TONEX plugin running the Vertex SSS SRV stomp capture in Logic for pre-compression, and UADx Lion '68 set to the Bass model with LOW input routing inside Paradise Guitar Studio. Post-processing includes an EQ "High-Cut Veil" at 4.5 kHz, LA-2A Silver optical glue, and Hitsville Reverb on Bus 3.

### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.

### 2026-08-24 — refined LA-2A calibration & P-90 gain staging
Tested with Les Paul (Tonerider Rebel 90s in standalone rig). Calibrated LA-2A Peak Reduction from 35.0 down to 22.0 to prevent dynamic choke/distortion and maintain transparent 1–2 dB optical leveling. Added iD14 -3.2 dB D.I. trim calibration notes and guidance on adjusting Lion '68 Volume II (3.5–4.0) vs Volume I (3.5) for high low-mid output P-90s.

### 2026-08-27 — integrated 3-pedal Paradise Pre-FX palette
Reverse-engineered and updated the front-end drive section inside Paradise Guitar Studio to a versatile 3-pedal palette (bypassed by default for pristine jazz clean):
1. **Slot 1 (Gold Overdrive / Klon):** Calibrated clean boost (`Gain 1.0`, `Treble 4.5`, `Output 3.0`).
2. **Slot 2 (TS Overdrive / Tube Screamer):** Mid-focused solo push with rounded treble (`Overdrive 1.0`, `Tone 2.5`, `Level 5.8`).
3. **Slot 3 (Nashville Overdrive / Nobels ODR-1):** Open, singing breakup with low-mid warming (`Drive 5.9`, `Spectrum 4.0`, `Level 7.2`, `Bass 10.0`).

### 2026-08-29 — updated LA-2A Silver calibration
Updated LA-2A Silver settings from saved preset: Peak Reduction adjusted to **32.0** for richer optical compression and dynamic control; Gain dialed back to **23.0** to keep the signal path cleanly gain-staged without clipping downstream effects.

### 2026-08-30 — calibrated Hitsville chamber decay & enforced wet solo off
Ensured Wet Solo is permanently OFF across preset files and templates for serial rack insertion. Halved Hitsville natural decay from 3.6s down to 1.8s (at 12% mix) for a tighter, cleaner room envelope that preserves note separation on fast chord changes.
