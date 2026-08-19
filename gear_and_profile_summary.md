# Guitar Rig & Musician Profile: Mike's Reference Guide
*Optimized for prompt injection and context loading into Large Language Models (like Google Gemini).*

> [!NOTE]
> **How to use this file:** Upload this document or copy-paste its contents into Google Gemini at the beginning of a session. This will instantly give the AI complete context on your physical instruments, hardware, software plugins, tone-shaping standards, and musical background so it can provide tailored guitar advice.

---

## 1. Musician Profile & Preferences

*   **Experience Level:** Advanced beginner on guitar, but with years of broad musical experience on other instruments.
*   **Multi-Instrument Background:** Violin, alto sax, a cappella arranging, bass, and Irish fiddle.
*   **Strengths & Theoretical Foundation:** Strong music reading ability, deep understanding of intervals, chord construction, modes, rhythm, and voice leading.
*   **Growing Edges (Guitar-Specific):** Guitar-specific finger dexterity, fretboard fluency, and translating theoretical knowledge into physical muscle memory.
*   **Preferred Genres:** Jazz, folk/fingerstyle, blues, Latin/bossa nova, rock, J-pop/City Pop, ambient/chillhop, and neo-soul.

### Persona Guidance for the AI
*   Be warm and encouraging but never patronizing—respect the deep musical foundation.
*   Always explain *why* an exercise or setting matters, connecting it back to theory or real music.
*   Draw on the multi-instrument background as a conceptual bridge (e.g., comparing shifting positions to violin, or voice leading to a cappella arranging).
*   Prioritize physical hand comfort and flag challenging stretches when recommending chord fingerings.

---

## 2. Guitar & Bass Stable

Mike owns 9 instruments, categorized by their pickups and primary physical/tonal roles:

### Electric Guitars

| # | Guitar | Pickups | Strings | Tone Notes |
|---|--------|---------|---------|------------|
| **1** | **2024 Fender Player II Telecaster** (British Racing Green) | Single-coil neck & bridge | D'Addario XS (10-46) | **"The Home Base."** Rosewood board, 6-saddle bridge. Bridge is bright, percussive, and cutting. Neck is warm but needs treble rollbacks on the amp/preamp for dark jazz tones. |
| **2** | **2014 Gibson Les Paul Studio** (Ebony, 120th Anniv.) | **490R (neck) & 490T (bridge)** (Alnico II, ~8.5k DCR) | D'Addario XS (10-46) | **"Smooth Refinement."** Sustain machine. Moderate-output humbuckers, warmer than standard LP pickups. Excellent for jazz, neo-soul, and vintage tones. Requires extra volume/gain for classic rock crunch. |
| **3** | **Mid-1980s Squier Stratocaster "Partscaster"** (Light Blue) | **Fender Tex-Mex** (3 single-coils) | D'Addario XS (10-46) | **"The Funky Quack."** Hot, punchy, pure nickel vintage warmth. Tex-Mex pickups are hotter than standard Strat single-coils. |
| **4** | **2013 Epiphone Sheraton II** (Natural) | Humbuckers (neck & bridge) | Thomastik-Infeld Jazz Swing Flats (10s) | **"The Velvet Jazz Box."** Semi-hollow laminate maple. Flatwounds reinforce dark jazz character. Acoustic bloom and natural sustain, but sensitive to feedback at high gain. |
| **5** | **2008 Epiphone Les Paul Standard Plus Top** (Sunburst) | Humbuckers (neck & bridge) | D'Addario XS (10-46) | **"Classic Rock Workhorse."** Brighter, louder, and more aggressive humbucker response than the Gibson LP Studio. |
| **6** | **2012 Framus Earl Slick Artist Series** (Matte Black) | **Two DiMarzio P-90s** (Soapbar single-coils) | Rotosound Yellows (10-46) | **"The Slick Rocker."** Flat-top swamp ash body, bolt-in maple neck, Bigsby B500 Vibrato, 3-way rotary selector. P-90s have a natural upper-mid spike; brighter and punchier than humbuckers. |

### Acoustic Guitars & Bass

| # | Instrument | Specs | Notes |
|---|------------|-------|-------|
| **7** | **2025 Cort Standard AD Mini** | 3/4 Size Dreadnought, Spruce top | Rotosound Metal (Steel) strings. Travel/couch steel-string. |
| **8** | **1990s Washburn D-12** | Dreadnought | "Tim's Guitar." Sentimental dreadnought acoustic foundation. |
| **9** | **1978 Fender Precision Bass** | 3-Color Sunburst | Vintage low-end anchor. |

*(Former / Sold: 2023 Revelation RFT DLX Thinline sold in 2026).*

---

## 3. Physical Hardware & Gain Staging

### Front-End Signal Path
1.  **Audient iD14 mkII USB-C Audio Interface:** The primary analog-to-digital front-end. Preamps feature discrete JFET instrument inputs.
2.  **Tone King Imperial Preamp Pedal (Two-Channel Tube Preamp):**
    *   *Rhythm Channel:* 60s Blackface (Fender Deluxe Reverb style) — Volume, Attenuation, Bass, Treble.
    *   *Lead Channel:* 50s Tweed + British Rock style — Volume, Attenuation, Tone (high contour), Mid-Bite (adds gain, tightens bass, boosts upper mids).
    *   *Shared:* Spring convolution reverb and digital tremolo. Cab/IR selector (Imperial 1x12, AC30 2x12, Marshall 4x12) with bypass.
    *   *Knob Scale:* 1 to 9 (Pip 1 = Min, Pip 5 = Noon/Flat, Pip 9 = Max).

### Physical Hardware Routing
*   **Direct Input (DI) Route (Default):** Guitar -> Audient iD14 instrument input. The cleanest, most neutral path for software amp modelers.
*   **Hardware Preamp Route:** Guitar -> Tone King Preamp -> XLR-to-TRS balanced cable -> iD14 back combo jacks (line-in). Set iD14 gain to minimum (0 dB) to bypass interface mic preamps. Control gain/volume purely via Tone King (transparency zone is Volume 2.0 to 3.0, Attenuation 5.0, EQ at noon). Bypass the Tone King's onboard cab IRs if using software amp/cab modelers.

### Digital Calibration Offsets
To match the software plugins' expected analog input level (+12.2 dBu clipping point) with the Audient iD14's hardware input (+9.0 dBu clipping point):
*   **UADx & Neural DSP Plugins:** Set the plugin's internal **Input Gain (IN)** control to **-3.2 dB** (3.2 dB digital reduction).
*   **IK Multimedia TONEX:** Set typical input trim offset to **-3 dB to 0 dB** for humbuckers, and **+2 dB to +5 dB** for single-coils.

---

## 4. Software Host & Plugin Inventory

### Software Hosts & Workflow
* **Kushview Element (Daily Driver):** Lightweight, modular VST/AU plugin host graph environment. Used for daily practice, quick preset recall, low-latency monitoring, and modular signal chain experimentation. Primary environment for fast configuration loading.
  * *Dual-Amp Routing:* Parallel amp graphs use Airwindows Consolidated `PurestDualPan` utility blocks for clean stereo positioning (-12 L / +12 R) before submix busing.
  * *Hammerspoon MIDI Controller:* Number keys (`1`, `2`, `3`, `5`) map to MIDI Program Change snapshots over macOS `IAC Driver Bus 1` to toggle pedalboards instantly with zero MIDI controller hardware (documented in [hammerspoon-midi-element.md](file:///Users/miketremoulet/claude-projects/GuitarSkills/references/hammerspoon-midi-element.md)).
* **Logic Pro (Production & High-Horsepower DAW):** Reserved for multi-track recording, complex bused routing (e.g. Aux sends, spatial mixing), heavy production, or when maximum processing horsepower is required.

> [!NOTE]
> **Host File Format Note:** Logic Pro project templates (`.logicx`) are binary/proprietary macOS bundle packages that cannot be programmatically generated via scripts. Host configurations for daily practice are managed via Kushview Element graphs (`.els`) or target plugin preset definitions.

### Amp Emulations

*   **UADx (Universal Audio):**
    *   *Dream '65 Reverb Amp:* Fender Blackface Deluxe Reverb '65. Clean-to-edge-of-breakup, spring reverb, bias tremolo.
    *   *Woodrow '55 Instrument Amp:* Fender Tweed Deluxe '55. Low headroom, saggy compression, and vintage tweed crunch.
    *   *Ruby '63 Top Boost Amp:* Vox AC30 '63. Chiming, brilliant Top Boost channel and classic Normal/Vib-Trem channels. Runs hot.
    *   *Lion '68 Super Lead Amp:* Marshall Super Lead Plexi 1959. Jumped channel routing, classic 60s British rock.
    *   *Enigmatic '82 Overdrive Special Amp:* Boutique Dumble-style amp. Extremely dynamic, highly responsive to guitar volume.
    *   *Showtime '64 Tube Amp:* Fender Showman/Twin high-headroom platform. Harmonic vibrato, stays clean and transparent.
    *   *Paradise Guitar Studio:* Premium virtual studio environment combining various amps, cabs, and stompboxes.
*   **MixWave:**
    *   *Two-Rock Bloomfield Drive:* Dynamic boutique amplifier with rich cleans, harmonic overdrive, and 6L6/6V6 tube switching. Includes a dedicated 2x12 vertical cabinet and 21 microphone options (including dynamic, ribbon, condenser, and "Copper").
*   **Neural DSP:**
    *   *Archetype Cory Wong X:* Clean/funk signature suite. Amps (Clean Machine, Amp Snob), 4th-position compressor, "The Wash" reverb/shimmer.
*   **Nembrini Audio:**
    *   *Mrh810 V2:* Marshall JCM800 2210 emulation. High-gain British rock.
    *   *Divided 11:* Divided by 13 CJ11 emulation. Class-A tube combo, tweed-adjacent mid growl.
    *   *Hughes & Kettner Puretone:* Hi-fi, ultra-transparent clean tone platform.
    *   *Jazz Chorus Solid State:* Roland JC-120 emulation. Pristine, uncolored solid-state clean with built-in chorus.
    *   *Crunck V2:* Original Nembrini design high-gain head.
*   **Other:**
    *   *Neural Amp Modeler (NAM):* Open-source player for community-captured profiles of real amplifiers and drive pedals.
    *   *Logic Amp Designer:* Apple's native amp, cabinet, and microphone simulation.

> [!WARNING]
> **Nembrini Gain Staging:** Nembrini plugins run hot. To prevent digital clipping on the stereo out, pull the plugin's internal Amp Master/Volume to ~2.5 and trim −4 dB on the cabinet Output slider (Target −11 to −12 dBFS on hard strums).

### Dynamics & Compression
*   **UADx Compressor Collections:**
    *   *Teletronix LA-2A (Silver, Gray, LA-2):* Optical tube compressors. Natural, program-dependent leveling. Smooth, warm glue.
    *   *1176 Classic Limiter (Rev A, Rev E/LN, AE):* FET peak limiters. Fast, aggressive, adds harmonic grit and "hair" when pushed.
    *   *175-B / 176 Collection:* Variable-mu tube compressors. Warm, gentle tube glue.
    *   *UA 610-B:* Tube preamp and EQ emulation. Drives harmonic tube coloration.
*   **Logic Pro Native Compressor:** Multi-circuit emulation containing models for Platinum Digital, VCA (Classic, Studio, Vintage), FET (Vintage, Studio), and Opto (Vintage LA-2A style).
*   **Others:** *LAM16* (Channel strip EQ/comp), *LockOn* (Sub-bass processor), *Logic Enveloper* (Transient shaper).

### Reverbs, Spaces & Delays
*   **UADx Capitol Chambers:** Four physical reverb chambers beneath Capitol Tower (Chambers 2, 4, 6, 7). Dense, acoustic space. Mix scale is logarithmic; keep mix between **5% and 10%** for guitar.
*   **UADx Hitsville Reverb Chambers:** Two Motown Studios chambers. Bright, rhythmic echo-like rooms. Mix is logarithmic (12:00 noon is ~15% wet).
*   **UADx Sound City Studios:** Simulation of the legendary Sound City live room and reverb chambers.
*   **UADx Galaxy Tape Echo:** Roland RE-201 Space Echo emulation. Warm analog delay, multi-head configurations, built-in spring reverb.
*   **ValhallaSuperMassive:** Algorithmic delay and massive, infinite reverb/shimmer washes.
*   **Logic Space Designer:** Convolution reverb with a massive library of rooms, plates, halls, and synthetic spaces.
*   **Logic ChromaVerb:** Modern algorithmic reverb with visual decay and 14 room templates.
*   **Logic Tape Delay:** Warm, filtered tape delay emulation with wow/flutter modulation.

### Tape, Saturation & Modulation
*   **UADx Studer A800:** Multichannel tape recorder simulation. Introduces tape compression and subtle high-frequency smoothing.
*   **UADx Studio D Chorus:** Roland SDD-320 Dimension D. Fixed push-button modes 1 to 4 (Mode 1 is subtle; Mode 4 is maximum).
*   **UADx Verve Analog Machines Essentials:** Ten vintage analog tape and solid-state saturation machines.
*   **Logic modulation tools:** Scanner Vibrato (Hammond style), Rotor Cabinet (Leslie rotary speaker), Ensemble, Chorus, Flanger, Tremolo.

### Acoustic & Utilities
*   **Nembrini Acoustic Voice Pro:** Acoustic guitar preamp. Body emulations, mic models, visual EQ, and post-effects rack for piezo/DI pickups.
*   **Logic Channel EQ:** 8-band parametric EQ (with high/low-pass filters). The primary surgical EQ tool.
*   **Logic Vintage EQ Collection:** Pulsing emulations of Vintage Console (Neve), Graphic (API), and Tube (Pultec) EQs.
*   **Logic Pedalboard:** Houses Apple's native guitar stompbox emulations (e.g., Tube Burner, Grit, Blue Echo, Retro Chorus, The Vibe, Squash Compressor).

---

## 5. Core Tone-Shaping Guidelines (Mike's "Tone Bible")

When designing or evaluating tones, follow these rules:

1.  **The "Clean Foundation" Philosophy:** Mike monitors via high-fidelity Sennheiser HD660S2 headphones. Tones must maintain high clarity, string separation, and touch sensitivity. Avoid masking deficiencies with heavy distortion or washing out details.
2.  **The "7/7" Guitar Volume/Tone Setting:** For jazz, blues, and touch-sensitive cleans, roll back the physical guitar Volume to **7 or 8** (to increase preamp headroom and clarity) and roll the Tone knob to **7** (to take the "edge" off the highs).
3.  **The "Jazz Middle" Scoop Correction:** The Tone King Rhythm channel and Fender Blackface models (Dream '65) have inherent mid-scoops. To achieve warm, vocal jazz tones, boost the Midrange control on the amp to **7.0 (70%)** or higher. "Plucky" or thin tones are corrected with mid-boosts, not bass-boosts.
4.  **The "High-Cut Veil" (Ed Bickert style):** To simulate a warm archtop jazz box on solid-body or thinline guitars, place a native Logic Channel EQ at the end of the track insert chain. Apply a low-pass (high-cut) filter at **4.0 kHz or 5.0 kHz** with a 24 dB/oct slope to remove digital fizz.
5.  **The "Bus-First" Spatial Routing Standard:**
    *   Place all Reverb (e.g., Capitol Chambers) and Delay (e.g., Galaxy Echo) on **Logic Aux sends/busses** (e.g., Bus 3 / Bus 4) instead of inline inserts.
    *   Set the plugin inside the Aux channel to **100% Wet** (or Wet Solo ON).
    *   Control the wet blend using Logic's track send knob (e.g., starting between `-12 dB` and `-18 dB`) to keep the primary guitar signal sharp, punchy, and centered.
    *   *Exception:* Built-in amp reverb/tremolo (like the spring reverb in the Dream '65 or physical Tone King) should remain inline inside the amp simulator.

---

## 6. Tone Preset Library (Reference Index)

Below are some of Mike's established guitar presets, mapped by category and target guitar. You can use these as reference points when suggesting tone adjustments.

### Warm Jazz & Clean Tones
*   **Dream '65 — Blackface Jazz:** Optimized for Gibson LP Studio (490R neck pickup). Clean, warm Blackface tone with tube compression.
*   **Jazz Clean — Intimate Les Paul:** Optimized for Gibson LP Studio (490R neck pickup). Close-miked, dry, clear jazz voicing.
*   **Puretone Velvet Jazz:** Optimized for Epiphone Sheraton II (neck pickup, flatwounds). Muted, resonant, traditional jazz box tone.
*   **JC120 Pristine Jazz Clean:** Optimized for Epiphone Sheraton. Nembrini Jazz Chorus solid-state clean, glassy and uncolored.
*   **The Electronic Veil (Ed Bickert Style):** Optimized for Telecaster (neck, flatwounds). Employs the 4.0 kHz high-cut EQ trick.
*   **TKIP Sheraton Jazz Clean:** Epiphone Sheraton routed through the Tone King Imperial Preamp (Rhythm channel).

### Boutique & Edge-of-Breakup Cleans
*   **Two-Rock Bloomfield — Boutique Warm Clean:** Gibson LP Studio (490R neck). Rich, high-headroom MixWave clean. (P-90 variant exists for Framus Earl Slick).
*   **Amp Snob — Boutique Clean:** Cory Wong X Amp Snob. Optimized for Gibson LP Studio 490R neck (humbucker variant) or Framus Earl Slick DiMarzio P-90s (P-90 variant).
*   **Enigmatic '82 — Boutique Warm Clean:** Dumble ODS style clean via UAD Enigmatic '82. Highly dynamic, neck pickup focus.
*   **Dream '65 — Blackface Sparkle:** Fender Player II Telecaster (bridge pickup). Clear, sparkling country/rock clean.

### Blues, Crunch & Classic Rock
*   **Lion '68 — Jumped Plexi Crunch:** Epiphone LP Standard (humbuckers, bridge/blend). Classic Marshall Plexi overdrive. (P-90 variant exists for Framus).
*   **Ruby '63 — Vox Top Boost Jangle:** Squier Stratocaster (bridge+middle "quack" position). Chiming British top-end grit.
*   **Woodrow Sweet Spot:** Squier Stratocaster or Framus P-90. Tweed Deluxe edge-of-breakup grit, compression, and mid warmth.
*   **Divided 11 Light Blues:** Fender Player II Telecaster (single-coils). Class-A touch-sensitive Tweed-style grit.
*   **Puretone Slick Growler:** Framus Earl Slick P-90s. Raw, punchy single-coil bite with minimum preamp coloration.
*   **Lion '68 — Clapton "Woman Tone":** Gibson LP Studio (neck pickup, guitar tone knob at 0). Cream-era vocal sustain.

### Ambient & Chillhop
*   **Lofi Vinyl:** Gibson LP Studio (neck). Uses iZotope Vinyl for warble and crackle; Cory Wong X for clean base.
*   **Strat Ambient Bath:** Squier Stratocaster. Heavy modulation, long ValhallaSuperMassive delays, and shimmering reverbs.
