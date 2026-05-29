# Logic Pro Universal Rig Template — Workflow Guide

This guide describes how to build and operate your **"Universal Rig Template"** in Logic Pro. 

By saving a baseline Logic template project with your core plugins pre-routed and loaded in a deactivated state, you eliminate almost all friction from practicing. When you want to explore a new toneprint, you simply open your template, activate the specified plugins, select the prefix-grouped **`Toneprint - [Tone Name]`** presets, and play.

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

To handle both electric and parallel acoustic blends with high-fidelity spatial reverbs, construct a 4-Aux routing bus matrix.

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
* **Plugins (Load all in a Bypassed/Deactivated state)**:
  1. **Logic Compressor** (Native)
  2. **LA-2A Tube Compressor** (UADx)
  3. **UA 610-B Tube Preamp & EQ** (UADx)
  4. **Logic Channel EQ** (Native)
  5. **Archetype Cory Wong X** (Neural DSP)
  6. **MixWave Two-Rock Bloomfield Drive** (MixWave)
  7. **Paradise Guitar Studio** (UADx)
* **Sends**:
  * **Bus 3** (Parallel Reverb Return) -> Set starting fader send to **−20 dB**.
  * **Bus 4** (Parallel Delay Return) -> Set starting fader send to **−20 dB**.
* **Fader**: 0 dB.

### Channel Strip 3: "Acoustic" (Aux Channel)
* **Input**: **Bus 1**.
* **Output**: Stereo Out.
* **Plugins (Load Bypassed/Deactivated)**:
  1. **Nembrini Acoustic Voice Pro** (or Logic equivalent)
  2. **Logic Channel EQ** (Native)
* **Sends**:
  * **Bus 3** (Parallel Reverb Return) -> Set starting fader send to **−22 dB**.
  * **Bus 4** (Parallel Delay Return) -> Set starting fader send to **−22 dB**.
* **Fader**: **−8 dB** (sets parallel blend level below the dry electric).

### Channel Strip 4: "Reverb Bus" (Aux Channel)
* **Input**: **Bus 3**.
* **Output**: Stereo Out.
* **Plugins (Load Bypassed/Deactivated)**:
  1. **Capitol Chambers** (UADx) -> *CRITICAL: Set Wet Solo to **ON**.*
  2. **Hitsville Reverb Chambers** (UADx) -> *CRITICAL: Set Wet Solo to **ON**.*
  3. **Logic Space Designer** (Native) -> *CRITICAL: Set Dry fader to −∞ (100% Wet).*
* **Fader**: **−12 dB** (starting point return level).

### Channel Strip 5: "Delay Bus" (Aux Channel)
* **Input**: **Bus 4**.
* **Output**: Stereo Out.
* **Plugins (Load Bypassed/Deactivated)**:
  1. **Galaxy Tape Echo** (UADx) -> *CRITICAL: Set Wet Solo to **ON**.*
  2. **Logic Tape Delay** (Native) -> *CRITICAL: Set Mix to 100% (Dry Off).*
* **Fader**: **−15 dB** (starting point return level).

---

## 3. Operating the Template (The 3-Step Dial-in)

When you choose a toneprint (e.g., *Sheraton Jazz + Acoustic Blend*), perform these three steps to load the complete tone in under 15 seconds:

### Step 1 — De-Bypass the Signal Chain
Inspect the toneprint's **Signal Chain** tables. Activate only the plugins mentioned:
* On **Electric Dry**: Activate **Logic Channel EQ**, **LA-2A**, and **UA Paradise Showtime '64**. Keep Cory Wong and Bloomfield bypassed.
* On **Acoustic**: Activate **Acoustic Voice Pro** and **Logic Channel EQ**.
* On **Reverb Bus**: Activate **Capitol Chambers**.

### Step 2 — Load the "Toneprint - [Name]" Presets
Click the preset selection menu on each activated plugin window and select the matching compiled file:
* On **Logic Channel EQ** -> Select `Toneprint - Sheraton Jazz Acoustic`
* On **LA-2A** -> Select `Toneprint - Sheraton Jazz Acoustic`
* On **UA Paradise** -> Select `Toneprint - Sheraton Jazz Acoustic`
* On **Capitol Chambers** -> Select `Toneprint - Sheraton Jazz Acoustic`

*Note: All compiled user presets are automatically prefix-isolated with `Toneprint -` so they group together in your menus.*

### Step 3 — Calibrate the Fader Blends
Align the Aux faders to match the toneprint's recommended baseline:
* Set the **Acoustic** Aux fader to **−8 dB** (or adjust to taste to control the parallel blend warmth).
* Set the **Reverb Bus** fader to **−12 dB**.
* Pick up your guitar, roll the tone knob to **7** for vintage warmth, and start practicing!
