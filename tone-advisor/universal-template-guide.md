# Logic Pro Universal Rig Template — Workflow Guide

This guide describes how to build and operate your **"Universal Rig Template"** in Logic Pro. 

By saving a baseline Logic template project with your core plugins pre-routed and loaded in a deactivated (bypassed) state, you eliminate all friction from practicing. When you want to explore a new toneprint, you simply open your template, activate the specified plugins, select the prefix-grouped **`Toneprint - [Tone Name]`** presets, and play.

---

## 1. Physical Signal Chain & Baseline Gain Staging

Before the signal ever reaches Logic Pro, ensure your physical hardware is set to the standard transparency baseline:

```
[Guitar] → [TONEX One (Bypass)] → [Tone King Imperial Preamp] → [iD14 Input 1] → [Logic Pro]
```

### Hardware Transparency Checklist:
* **TONEX One**: Set to **Bypass** (unless a specific stomp capture is required by the toneprint).
* **Tone King Imperial Preamp**:
  * **Channel**: Rhythm.
  * **Volume**: **2.0 to 3.0** (The transparency clean headroom zone).
  * **Attenuation**: **5.0** (unity/moderate).
  * **Bass / Treble**: **5.0 (Noon)** for flat response.
  * **IR Switch**: **Bypassed** (since speaker cabinet modeling is handled in Logic).
  * **Reverb & Tremolo**: **Off**.
* **Audient iD14 Interface**: Set preamp input level so your loudest strums peak around **−18 dBFS** in Logic.

---

## 2. Logic Pro Routing Architecture

To handle both electric and parallel acoustic blends with high-fidelity spatial reverbs and delays, construct a 4-Aux routing bus matrix.

```
                  [Guitar Input Track] (Output to Bus 1)
                                   |
                  +----------------+----------------+
                  |                                 |
        [Aux 1: Electric Dry]             [Aux 2: Acoustic Voice]
        (Input: Bus 1, Output: St Out)    (Input: Bus 1, Output: St Out)
        (Fader: 0 dB)                     (Fader: −8 dB)
                  |                                 |
        +---------+---------+             +---------+---------+
        |                   |             |                   |
  (Send to Bus 3)     (Send to Bus 4)   (Send to Bus 3)     (Send to Bus 4)
  (Level: −20 dB)     (Level: −20 dB)   (Level: −22 dB)     (Level: −22 dB)
        |                   |             |                   |
  [Aux 3: Reverb]     [Aux 4: Delay]      |                   |
  (Input: Bus 3)      (Input: Bus 4)      |                   |
  (Output: Stereo Out)(Output: Stereo Out)|                   |
        +-------------------+-------------+-------------------+
                                   |
                          [Stereo Main Output]
```

### Channel Strip 1: "Guitar Input" (Audio Track)
* **Input**: Input 1 (from Audient iD14).
* **Output**: **Bus 1** (The main Dry Router).
* **Plugins**: None.
* **Fader**: 0 dB (unity).

### Channel Strip 2: "Electric Dry" (Aux Channel)
* **Input**: **Bus 1**.
* **Output**: Stereo Out.
* **Plugins (Load all in a Bypassed/Deactivated state in this exact top-to-bottom order)**:
  1. **Logic Noise Gate** (Native) — Tames P-90/single-coil hum under gain.
  2. **Logic Compressor** (Native) — Clean transient control.
  3. **UADx UA 610-B Preamp & EQ** — Tube coloring, harmonic drive, and preamp impedance warmth.
  4. **Logic Channel EQ** (Native) — Surgical EQ cuts and high-cut veils.
  5. **Nembrini Clon Minotaur** (Nembrini) — Klon transparent boost.
  6. **Nembrini 808** (Nembrini) — TS-808 mid-hump overdrive.
  7. **Nembrini Black** (Nembrini) — RAT2 high-sustain lead and grit.
  8. **Logic Pedalboard** (Native) — Access to native Wah, Fuzz, and modulation stompboxes.
  9. **UADx Showtime '64 Tube Amp** — Fender Twin/Showman ultra-high-headroom clean.
  10. **UADx Dream '65 Reverb Amp** — Fender Blackface Deluxe clean/tremolo.
  11. **UADx Woodrow '55 Instrument Amp** — Fender Tweed Deluxe sag and compression.
  12. **UADx Enigmatic '82 Overdrive Special Amp** — Dumble ODS boutique warm clean & dynamics.
  13. **UADx Ruby '63 Top Boost Amp** — Vox AC30 chime and Top Boost jangle.
  14. **UADx Lion '68 Super Lead Amp** — Marshall Plexi classic rock crunch.
  15. **UADx Paradise Guitar Studio** — Universal Audio multi-amp / studio platform.
  16. **MixWave Two-Rock Bloomfield Drive** — Boutique high-headroom warm clean and smooth lead.
  17. **Neural DSP Archetype Cory Wong X** — Pristine funk/fusion clarity and clean machine.
  18. **Nembrini Jazz Chorus SS** — Roland JC-120 solid-state clean (no break up).
  19. **Nembrini Divided 11** — Boutique Class A Tweed-style sag.
  20. **Nembrini H&K Puretone** — High-headroom transparent hi-fi tube clean.
  21. **Nembrini Mrh810 V2** — Marshall JCM800 high-gain rock lead.
  22. **UADx LA-2A Silver Compressor** — Vintage optical leveling and sustain (essential for jazz box).
  23. **UADx 1176LN Rev E Compressor** — FET fast peak limiting and harmonic color.
  24. **UADx Studer A800 Tape Recorder** — Analog tape saturation, warmth, and glue.
  25. **UADx Verve Analog Machines Essentials** — Instant solid-state saturation and tape warble texture.
  26. **UADx Studio D Chorus** — Classic Dimension D chorus-less stereo widening.
  27. **Logic Tremolo** (Native) — Amplitude modulation for neo-soul/ambient.
* **Sends**:
  * **Bus 3** (Parallel Reverb Return) -> Set starting fader send to **−20 dB**.
  * **Bus 4** (Parallel Delay Return) -> Set starting fader send to **−20 dB**.
* **Fader**: 0 dB (unity).

### Channel Strip 3: "Acoustic" (Aux Channel)
* **Input**: **Bus 1**.
* **Output**: Stereo Out.
* **Plugins (Load Bypassed/Deactivated)**:
  1. **Nembrini Acoustic Voice Pro** — Dynamic acoustic body modeling.
  2. **Logic Channel EQ** (Native) — Acoustic resonance balancing.
* **Sends**:
  * **Bus 3** (Parallel Reverb Return) -> Set starting fader send to **−22 dB**.
  * **Bus 4** (Parallel Delay Return) -> Set starting fader send to **−22 dB**.
* **Fader**: **−8 dB** (sets parallel acoustic blend level below the dry electric).

### Channel Strip 4: "Reverb Bus" (Aux Channel)
* **Input**: **Bus 3**.
* **Output**: Stereo Out.
* **Plugins (Load Bypassed/Deactivated)**:
  1. **UADx Capitol Chambers** — *CRITICAL: Set Wet Solo to **ON**.*
  2. **UADx Hitsville Reverb Chambers** — *CRITICAL: Set Wet Solo to **ON**.*
  3. **UADx Sound City Studios** — *CRITICAL: Set Wet Solo to **ON**.*
  4. **Logic Space Designer** (Native) — *CRITICAL: Set Dry fader to −∞ (100% Wet).*
  5. **Logic ChromaVerb** (Native) — *CRITICAL: Set Dry fader to −∞ (100% Wet).*
  6. **ValhallaSuperMassive** — *CRITICAL: Set Mix to 100% Wet.*
* **Fader**: **−12 dB** (starting point return level).

### Channel Strip 5: "Delay Bus" (Aux Channel)
* **Input**: **Bus 4**.
* **Output**: Stereo Out.
* **Plugins (Load Bypassed/Deactivated)**:
  1. **UADx Galaxy Tape Echo** — *CRITICAL: Set Wet Solo to **ON**.*
  2. **Logic Tape Delay** (Native) — *CRITICAL: Set Mix to 100% (Dry Off).*
  3. **Logic Stereo Delay** (Native) — *CRITICAL: Set Mix to 100% (Dry Off).*
* **Fader**: **−15 dB** (starting point return level).

---

## 3. Operating the Template (The 3-Step Dial-in)

When you choose a toneprint (e.g., *Sheraton Jazz + Acoustic Blend*), perform these three steps to load the complete tone in under 15 seconds:

### Step 1 — De-Bypass the Signal Chain
Inspect the toneprint's **Signal Chain** tables. Activate only the plugins mentioned:
* On **Electric Dry**: Activate **Logic Channel EQ**, **LA-2A**, and **UADx Showtime '64**. Keep all other amp and pedal slots bypassed.
* On **Acoustic**: Activate **Acoustic Voice Pro** and **Logic Channel EQ** (if blend is active).
* On **Reverb Bus**: Activate **Capitol Chambers**.

### Step 2 — Load the "Toneprint - [Name]" Presets
Click the preset selection menu on each activated plugin window and select the matching compiled file:
* On **Logic Channel EQ** -> Select `Toneprint - Sheraton Jazz Acoustic`
* On **LA-2A** -> Select `Toneprint - Sheraton Jazz Acoustic`
* On **UADx Showtime '64** -> Select `Toneprint - Sheraton Jazz Acoustic`
* On **Capitol Chambers** -> Select `Toneprint - Sheraton Jazz Acoustic`

*Note: All compiled user presets are automatically prefix-isolated with `Toneprint -` so they group together in your menus.*

### Step 3 — Calibrate the Fader Blends
Align the Aux faders to match the toneprint's recommended baseline:
* Set the **Acoustic** Aux fader to **−8 dB** (or adjust to taste to control the parallel blend warmth).
* Set the **Reverb Bus** fader to **−12 dB**.
* Pick up your guitar, roll the tone knob to **7** for vintage warmth, volume to **8** for touch-sensitivity, and start practicing!
