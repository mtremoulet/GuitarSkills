---
id: smoky-tweed-roots
preset_name: "Smoky Tweed Roots"
created: 2026-09-06
updated: 2026-09-06
pickup_type: p-90
guitar: "2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90s HSP-90s, Neck Pickup)"
target: 'Touch-sensitive 1950s Tweed edge-of-breakup saturation; pristine on soft fingerstyle, blooming with rich harmonic overtones on firm low-string thumb snaps.'
tags: "roots, folk, americana, tweed, woodrow, tone-king, p-90, edge-of-breakup, fingerstyle, tremolo"
amp: "Woodrow '55 (UADx) / Tone King Imperial (Hardware)"
tone-king-channel: lead
status: tested
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    woodrow_inst_volume: 3.2
    woodrow_mic_volume: 2.5
    woodrow_tone: 5.0
    woodrow_boost_enable: false
    woodrow_boost_type: 0
    woodrow_boost_amount: 1.0
    cab_and_mic: 32
  galaxy:
    head_select: 2
    echo_rate: 5.5
    feedback: 2.0
    echo_volume: 2.5
    tape_age: 1
    wet_solo: false
  hardware_settings:
    Channel: Lead
    Volume: 3.5
    Attenuation: 5.0
    Tone: 3.5
    Mid-Bite: 1.5
    IR: "OH 112 Imperial TK1660"
    Reverb:
      Level: 2.5
      Dwell: 3.5
    Tremolo:
      Speed: 3.2
      Depth: 2.8
    Guitar_Volume: 6.8
    Guitar_Tone: 6.0
---

# Smoky Tweed Roots

## Target Sound

Designed for expressive, roots-oriented Americana, fingerstyle folk, and acoustic-electric blues (Ry Cooder, Richard Thompson, Blake Mills, Jason Isbell).

This toneprint harnesses the loose, spongy, tactile bloom of a 1950s Fender Tweed Deluxe (5E3 circuit). On the physical Tone King Imperial Preamp pedal, we set the **Lead channel with Mid-Bite dialed back to 1.5**. At this low setting, the circuit leaves modern crunch behind and behaves as an authentic 5E3: unconstrained low-mid warmth, soft high-frequency contour, and immediate dynamic sag. Engaging the pedal's onboard bias-style tremolo at a gentle rate (Speed 3.2, Depth 2.8) adds an organic, swampy undulation that breathes with chord decays.

---

## Signal Chains

### Option A: Physical Hardware Signal Path (Direct-in / Standalone)
```
[Epiphone LP (Rebel 90s)] ──► [Tone King Imperial Preamp (Hardware)] ──► [Audient iD14 Line In] ──► [Post-Amp DAW/Host FX]
```

| Hardware Control | Setting (1–9 Pips) | Technical Rationale |
|---|---|---|
| **Channel** | **Lead** | 1950s American Tweed combo character |
| **Volume** | **3.5** | The Tweed sweet spot: clean under gentle touch, blooming under firm pick attack |
| **Attenuation** | **5.0** | Unity output level structure into interface/monitors |
| **Tone** | **3.5** | Smooths high-frequency bite for warm fingerstyle flesh-of-the-finger attack |
| **Mid-Bite** | **1.5** | **CRITICAL**: Keeps circuit in pure 50s Tweed mode; loose, fat, organic sag |
| **Cab IR Selector** | **Cab 1 — OH 112 Imperial TK1660** | Open-back 1x12 pine combo response; deep, resonant wooden warmth |
| **Reverb** | **ON** (Level 2.5, Dwell 3.5) | Tube-driven spring decay that blooms behind fingerpicked notes |
| **Tremolo** | **ON** (Speed 3.2, Depth 2.8) | Gentle bias-style pulse for authentic roots undulation |
| **Guitar Controls** | **Neck Pickup \| Vol 6.8 \| Tone 6.0** | Vol 6.8 is the master dynamic sweet spot: roll to 6.5 for clean, 8.5 for grit |

---

### Option B: Software Signal Path (Standalone Audio / Element)
```
[Guitar D.I.] ──► [Audient iD14 Input 1 (-3.2dB Pad)] ──► [UADx Woodrow '55] ──► [Galaxy Tape Echo] ──► [TDR Nova / Verve]
```

| Software Plugin | Control | Setting | Purpose |
|---|---|---|---|
| **UADx Woodrow '55** | Input Routing | **High Input (Jumped)** | Drives both channels for rich vintage body |
| | INST VOL (Instrument) | **3.2** | Controls edge-of-breakup clarity and bite |
| | MIC VOL (Mic) | **2.5** | Adds warm low-frequency body without flubbing the Rebel 90s |
| | Tone | **5.0** | Interactive tone/gain control centered at noon |
| | Boost Circuit | **OFF (Stock)** | Preserves organic touch-sensitivity |
| | Cabinet | **GB25 (or 1x12 5E3)** | 1x12 Celestion Greenback keeps low-mids articulate |
| **UADx Galaxy Tape Echo** | Head Select / Rate | **Head 2 / Rate 5.5** | Medium analog tape echo (~240 ms) |
| | Feedback / Volume | **Feedback 2.0 / Echo Vol 2.5** | 2–3 musical, decaying tape repeats |
| | Tape Age | **Used** | Introduces subtle tape wow, flutter, and warmth |
| **TDR Nova Dynamic EQ** | High-Pass Filter | **75.0 Hz (12 dB/oct)** | Cleans up low-frequency thumb-slap rumble |
| | Dynamic Bell Cut | **420 Hz (-2.0 dB, Q 1.2)** | Clamps down on P-90 boxiness only on hard strums |
| **UADx Verve Analog Machines** | Model / Drive | **Tape Glow / Drive 2.0** | Warm tape saturation across decaying note tails |

---

## Universal 6-Guitar Calibration Guide

Switching between guitars while dialing in the touch-sensitive "Smoky Tweed Roots" edge-of-breakup:

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Epiphone Les Paul (Rebel 90s)** *(Anchor)* | Neck P-90, Vol 6.5–7, Tone 6 | Baseline: Vol 3.5, Tone 3.5, Mid-Bite 1.5 | Baseline: Woodrow Inst 3.2, Mic 2.5 | Organic 5E3 Tweed sag; clean on finger plucks, hairing up on firm thumb snaps. |
| **Gibson Les Paul Studio** | Neck 490R (or Middle), Vol 7, Tone 6 | **Volume +0.5 (4.0), Tone +0.5 (4.0)** | **Inst Vol +0.4 (3.6), Mic Vol 2.5** | 490R humbucker has smoother top and moderate output. Nudging Volume to 4.0 restores the edge-of-breakup threshold. |
| **Framus Earl Slick (DiMarzio P-90s)** | Neck P-90, Vol 7.0, Tone 5.5 | **Tone 3.5, Mid-Bite 1.2** | **Woodrow Tone 4.5, Inst Vol 3.0** | DiMarzios are slightly hotter with more upper-mid bite. Keep Mid-Bite low (1.2) to stay firmly in Tweed territory without crunch. |
| **Fender Player II Telecaster** | Neck Pickup, Vol 8.0, Tone 6.5 | **Tone +1.0 (4.5), Mid-Bite +0.5 (2.0)** | **Woodrow Tone 5.5, Inst Vol 3.5** | Telecaster neck pickup has less output than P-90s. Advance Mid-Bite to 2.0 and Tone to 4.5 to give fingerstyle lines body and grit. |
| **Squier Stratocaster (Tex-Mex)** | Position 5 (Neck SC), Vol 8.0, Tone 6.5 | **Tone +0.8 (4.3), Mid-Bite +0.5 (2.0)** | **Woodrow Tone 5.2, Inst Vol 3.5** | Woody Ry Cooder / Bonnie Raitt slide and fingerstyle tone. Spongy tube sag cushions single-coil dynamics. |
| **Epiphone Sheraton II** | Neck Humbucker, Vol 7.0, Tone 6.5 | **Volume 3.5, Tone +0.5 (4.0), Mid-Bite 1.2** | **Woodrow Mic Vol -0.5 (2.0)** | Semi-hollow body adds deep woody resonance. Flatwounds sound earthy and dark; reduce Mic Vol in software to prevent bottom-end mud. |

---

## Musical Rationale & Multi-Instrument Bridge

- **The Irish Fiddle & Upright Bass Bridge**: On Irish fiddle, rhythmic drive and emotional expression are shaped by bow pressure (*cuts*, *rolls*, and *crashes*). On an upright bass, the thumb anchors alternating root-five pulses while fingers pluck melodic syncopations.
- **Dynamic Interaction**: Setting the guitar volume to 6.8 activates the tube preamp's dynamic threshold: an alternating thumb bassline on the lower strings remains clean, round, and woody, while fingerpicked melody notes on higher strings push into soft harmonic overdrive.

---

## Optional Footnote: All-Digital Workflow & Three-Way Cross-Amp Comparison

For an all-digital workflow or when A/B/C testing across hardware and software platforms, load the generated native presets below:

### 1. UADx Paradise Guitar Studio Preset (`Toneprint - Smoky Tweed Roots.json`)
- **Location**: `uaudio_paradise_guitar_studio/Woodrow '55/` and `tones/presets/paradise/`
- **Amp Engine**: **Woodrow '55** (Model 5)
- **Amp Controls**: Instrument Volume **3.2**, Mic Volume **2.5** (jumped blending), Tone **5.0**, Boost **OFF**, Output **12.0**
- **Cabinet / Mic**: **1x12 GB25 / Oxford** (`cab_and_mic`: 32)
- **Pre-FX**: None (preserves unbuffered guitar pot impedance and dynamic touch-sensitivity)
- **Post-FX**: Slot 1: **Trem '65** (Active — Speed 3.2, Depth 2.8), Slot 2: **EP-III Tape Delay** (Active — 240 ms, 20% mix)

### 2. Neural DSP Archetype Cory Wong X Preset (`Smoky Tweed Roots.xml`)
- **Location**: `/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints/` and `tones/presets/neural/`
- **Amp Engine**: **The Amp Snob** (Amp 2, `DRIVE`: **OFF**)
- **Amp Controls**: `VOLUME`: **58%** (drives input stage into touch-sensitive Tweed saturation), `MASTER`: **70%**, `BASS`: **58%**, `MIDDLE`: **55%**, `TREBLE`: **42%**, `PRESENCE`: **38%**, `BRIGHT`: **OFF**, `OUTPUT`: **55%**
- **9-Band Graphic EQ**: **Active** — 125 Hz: **+1.5 dB**, 250 Hz: **+1.5 dB**, 500 Hz: **+1.0 dB**, 4 kHz: **-1.5 dB** (Shapes boutique Dumble clean into spongy 50s Tweed cone response)
- **Cabinet**: Cab 2 (Snob 2x12), Mic: Dynamic 57 + Ribbon 121 (Room Mic -22 dB)
- **Post-FX**: **Delay-Y-Y** (Active — Mix 22%, Feedback 20%, 240 ms) + **The Wash** (Active — Mix 15%, Decay 25%, Shimmer OFF)

### 3. Three-Way Cross-Amp Comparison Matrix

| Dimension | Tone King Imperial Preamp (Physical Tube) | UADx Paradise Guitar Studio (Woodrow '55) | Archetype Cory Wong X (Amp Snob) |
|---|---|---|---|
| **Core Circuit & Architecture** | Lead channel with Mid-Bite dialed low to 1.5; 3x 12AX7 all-tube preamp + Ironman II reactive attenuator | Emulated 1955 narrow-panel Fender Tweed Deluxe (5E3 circuit) with jumped channels | Boutique Dumble Overdrive Special clean channel (Drive switch OFF) revoiced via 9-band EQ |
| **Edge-of-Breakup Transition** | Spongy, organic analog sag; cleans up completely on gentle fingerpicking; blooms into harmonic overtone fur on hard thumb snaps | Thick, uncompressed vintage 5E3 low-mid bloom; highly interactive volume/tone circuit modeling | Controlled, polished edge-of-breakup; slightly faster transient recovery than 5E3 with very predictable dynamic threshold |
| **Midrange Bloom & Warmth** | Woody, loose, harmonic resonance centered around 400–800 Hz; zero modern fizz | Earthy, lo-fi vintage character; lush harmonic blur when chords decay | Smooth, vocal, studio-grade midrange focus; exceptionally low noise floor for single-coil P-90s |
| **Modulation & Ambience** | Built-in analog-style bias tremolo + tube spring convolution; breathes with playing dynamics | Modeled tube tremolo + EP-III tape slapback; authentic vintage tape warmth | Digital delay + ambient wash room reverb; pristine, expansive, modern indie-folk spatial depth |

