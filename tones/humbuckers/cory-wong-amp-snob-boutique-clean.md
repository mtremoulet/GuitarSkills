---
amp: "Amp Snob (Archetype Cory Wong X)"
created: 2026-05-24
guitar: "Gibson Les Paul Studio (490R neck pickup)"
id: cory-wong-amp-snob-boutique-clean
pickup_type: humbucker
preset_name: "Amp Snob Boutique Clean HB"
status: tested
tags: "boutique, clean, warm, les-paul, humbucker, dumble, neural-dsp, cory-wong, amp-snob"
target: 'Boutique ODS warmth inside Archetype Cory Wong X — rich, touch-sensitive clean using the Amp Snob with a pushed power-amp Master for that saturated-but-clean harmonic bloom.'
tone-king-channel: bypassed
updated: 2026-05-25
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
    selectedAmp: 2
    selectedCab: 2
    compressorActive: true
    compressorVolume: 55.0
    compressorCompression: 35.0
    compressorTone: 50.0
    compressorBlend: 40.0
    snobBass: 46.0
    snobBright: false
    snobDrive: false
    snobEQActive: true
    snobEQHpf: 20.0
    snobEQLpf: 20000.0
    snobEQBand1: 0.0
    snobEQBand2: -0.5
    snobEQBand3: -1.5
    snobEQBand4: 1.0
    snobEQBand5: 1.5
    snobEQBand6: -1.0
    snobEQBand7: 0.0
    snobEQBand8: 0.0
    snobEQBand9: 0.0
    snobMaster: 75.0
    snobMid: 58.0
    snobOutputLevel: 70.0
    snobPresence: 50.0
    snobTreble: 48.0
    snobVolume: 42.0
    tuberActive: false
    washActive: false
  hitsville:
    decay: 2.0
    mix: 0.12
    pre_delay: 8.0

    wet_solo: false
  logic_compressor:
    attack: -1
    makeup_gain: 14
    ratio: 75
---

# Amp Snob — Boutique Warm Clean (Archetype Cory Wong X)

## Target Sound

Neural DSP's Archetype Cory Wong X contains **"The Amp Snob"**, a meticulously modeled boutique amplifier inspired by a clean-voiced Dumble-style head. Known for its incredible harmonic response, touch-sensitive dynamics, and "rubbery" string feel, it is the perfect platform to recreate the Two Rock Bloomfield's "saturated-but-clean" ethos in the Neural DSP environment.

To get that "maxed-out but not distorted" fatness, this toneprint uses a classic studio engineering technique: we keep the **Volume** (which acts as input gain) relatively low to keep the preamp clean, but we push the **Master** (power amp gain) very high. This forces virtual power amp compression and harmonic saturation, making your Les Paul Studio's 490R neck humbucker sound thick, three-dimensional, and sustained without clipping.

We combine this with Cory Wong's excellent parallel compressor ("The 4th Position Compressor") and a warm Ribbon 121 mic model to create an incredibly rich, luxurious clean tone.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. Archetype Cory Wong X — boutique character & compression

This plugin houses our compressor, preamp, cabinet, and graphic EQ in a single highly-optimized window. To keep the comparison fair and allow direct A/B testing with the Two Rock, we bypass the plugin's built-in chorus, delay, and reverb pedals, routing the track instead to our shared Hitsville Reverb Aux bus.

**Pre FX Section**

| Pedal | Control | Setting | Purpose |
|-------|---------|---------|---------|
| **The 4th Position Compressor** | **Active** | **ON** | Essential parallel optical compression |
| | **Blend** | **40%** | Parallel blend; preserves the natural, uncompressed transient attack of your pick, while compressing the tail of the note for "bloom" and sustain |
| | **Tone** | **50%** | Neutral; does not color the high frequencies of the compressed signal |
| | **Compression**| **35%** | Moderate compression depth; acts as the primary sustain engine |
| | **Volume** | **55%** | Calibrated to ensure unity gain through the pedal |

*All other Pre FX (Envelope Filter, Tuber OD, Big Rig OD) are **BYPASSED**.*

**Amp Section — "The Amp Snob"**

All parameters are specified in percentages (0–100%), matching the virtual control ranges.

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **The Amp Snob** | Selects the Dumble-style clean/crunch amp |
| Volume (Gain) | **42%** | Input gain sweet spot; keeps the preamp clean but pushes enough signal to feel dynamic |
| Master | **75%** | **Pushed high**: Pushes the virtual power tubes into warm compression and rich harmonic saturation |
| Drive Switch | **OFF** | Keeps the extra gain stage out of the chain to ensure pristine clean headroom |
| Bright Switch | **OFF** | Removes the bright cap boost, keeping the humbucker's high end smooth and smoky |
| Bass | **46%** | Slightly rolled back to prevent low-end mud from the neck humbucker |
| Middle | **58%** | Slightly pushed to highlight the classic Dumble throatiness and note separation |
| Treble | **48%** | Smooth high-end contour; dark but articulate |
| Presence | **50%** | Neutral power amp high-end air |
| Output | **70%** | Level trim; manages overall plugin output to match our −12 dBFS target |

**Cab Section (Unlinked Cabinets)**

We unlink the cabinet from the amp to pair the Amp Snob with a dark, warm, vintage-voiced mic setup.

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp/Cab Link | **Off** (Unlinked) | Allows custom mic/cab configuration |
| Cab Type | **Snob** | Matching 2x12 open-back boutique cabinet |
| Cab L | **Active** | Primary mic slot |
| Mic L Type | **Ribbon 121** | Creamy, warm, vintage character; rounds off high-end transients and fattens low-mids |
| Position L | **0.48** | Just off-center of the speaker cone; balances warmth with note definition |
| Distance L | **0.25** | Close-mic'd with a tiny bit of "air" to let the low-end bloom breathe |
| Room Send L | **−28.0 dB** | Kept extremely low to prevent room mud and keep the core tone focused |
| Cab R | **BYPASSED** | Single mic setup keeps the phase perfectly coherent |

**EQ Section (Amp Snob 9-Band Graphic EQ)**

| Band | Setting | Purpose |
|------|---------|---------|
| EQ Status | **Active** | Subtle custom corrective curves |
| 65 Hz | 0.0 dB | Neutral |
| 125 Hz | −0.5 dB | Extremely subtle cleanup of sub-bass resonance |
| 250 Hz | −1.5 dB | **Targeted cut**: Cleans up muddy build-up from the LP humbucker's neck pickup |
| 500 Hz | +1.0 dB | Boosts lower midrange woodiness and vocal warmth |
| 1 kHz | +1.5 dB | Pushes the Dumble-style "singing" midrange character |
| 2 kHz | −1.0 dB | Smooths out pick-attack harshness |
| 4 kHz | 0.0 dB | Neutral |
| 8 kHz | 0.0 dB | Neutral |
| 16 kHz | 0.0 dB | Neutral |
| HPF / LPF | Default | 20 Hz High-Pass / 20.0 kHz Low-Pass |

---

### 3. UADx Hitsville Reverb Chambers — shared room space (Aux 2)

By routing this Archetype Cory Wong X track to the exact same Hitsville Reverb bus as our other boutique presets, you can test both plugins back-to-back under identical room acoustics!

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | **2648 (Chamber 1)** | Present, rich room reflections |
| Speaker | **Bozak 800** | Classic Detroit chamber speaker setup |
| Mic | **Unidyne 545** | Articulate guitar reverb mic |
| Mix | **Wet Solo (100%)** | Placed on Aux 2; fader controls blend |
| Decay | **9:00** | Tight, short room reflection for rhythm clarity |
| Pre-Delay | **8 ms** | Separation between dry note and room reflections |

**Logic Send Routing**
*   **Send Level (Aux 2):** −12 dB
*   **Bus Fader (Aux 2):** −8 dB

---

## Starting Point Guide

- **First adjustment (Parallel Comp Blend):** The **Blend** knob on **The 4th Position Compressor**. Moving it between **30% and 50%** is the ultimate dial for the "feel" of your picking hand. At 30%, it feels like a standard direct amp—highly dynamic. At 50%, it feels incredibly compressed and thick (excellent for smooth fingerstyle or melodic lines).
- **Drive Switch Exploration (Alternative):** If you want to push the Amp Snob into a slightly grittier "Texas Blues" territory (think SRV or John Mayer's slightly driven solos), toggle the **Drive Switch to ON**, pull the **Volume** down to **25%**, and roll your guitar's volume knob back to **7**. The amp will clean up but retain a singing, harmonic edge.
- **Graphic EQ Bypass:** If you want to hear the raw, uncorrected voice of the Amp Snob, simply toggle the **EQ Active** switch to OFF. The graphic EQ cuts are subtle but highly effective at adapting the plugin to the Gibson Les Paul's specific humbucker profile.

---

## Feedback History

### 2026-05-25 — tested (nailed the boutique tone)
Tested in session. Bypassed internal time-based effects and routed track to shared Hitsville Reverb Aux. Confirmed this tone absolutely "nailed" the boutique Two Rock Bloomfield clean vibe on your Les Paul neck humbucker without any changes needed to the amp settings. The only refinement was pulling back the cabinet **Room Send L to −28.0 dB** (down from −12.0 dB) to keep the acoustic space tightly focused and dry. Status updated to `tested`.

### 2026-05-24 — initial
Created as part of a dual-preset boutique Dumble-style clean exploration. Bypasses physical front-end (Tone King & TONEX One) to run direct into the iD14 interface. Uses Archetype Cory Wong X's "The Amp Snob" with a pushed Master volume (75%) and low Volume (42%) to capture the virtual power amp compression and harmonic saturation of the Two Rock. Employs "The 4th Position Compressor" at 40% Blend for dynamic parallel compression, and pairs the amp with a Ribbon 121 mic and a subtle 9-band EQ curve for maximum humbucker clarity. Bypasses internal time-based effects in favor of the shared Hitsville Reverb Aux bus.
