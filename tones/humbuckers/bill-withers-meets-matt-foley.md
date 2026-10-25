---
id: bill-withers-meets-matt-foley
preset_name: "Bill Withers Meets Matt Foley"
created: "2026-09-07"
updated: "2026-09-07"
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (Neck or Neck+Bridge blend)"
target: 'Warm, percussive 1970s soul and funk rhythm guitar tone ("Use Me", "Lean On Me") augmented with Faust Liberty Burnisher front-end polish and MattFoley dual-J201 parallel boost into Woodrow ''55 Tweed warmth, optical compression, and tight chamber room.'
tags: "bill-withers, soul, funk, rhythm, humbucker, les-paul, sheraton, 70s, uad_paradise, faust, matt-foley, liberty-burnisher"
tone-king-channel: bypassed
amp: "Woodrow '55 (UADx)"
status: refined
pickup_type: humbucker
preset_data:
  amp_platform: uad_paradise
  faust_pedals: "Liberty Burnisher, MattFoley"
  amp_settings:
    Instrument_Volume: 4.5
    Mic_Volume: 3.0
    Tone: 5.5
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  la2a:
    peak_reduction: 35
    gain: 28
    compress: true
  hitsville:
    mix: 0.15
    pre_delay: 12.0
    decay: 1.8
    wet_solo: false
---

# Bill Withers Meets Matt Foley

## Target Sound

This toneprint extends the warm, syncopated 1970s rhythm foundation of the classic **Bill Withers 70s Soul Rhythm** toneprint by front-loading two dedicated Faust virtual analog pedals:
1. **Liberty Burnisher** (Germanium/Silicon harmonic polisher and Baxandall EQ shelf) for sparkling string separation and articulate chord definition.
2. **MattFoley** (dual-J201 parallel boost modeled after the Wampler Talent Booster / Speaker Motivator) to give punchy, tactile touch sensitivity to muted funk scratching and thumb-plucked soul chords.

Downstream, the **UADx Woodrow '55** Tweed Deluxe provides saturated vintage warmth, smoothed dynamically by the **LA-2A Silver** optical compressor and placed in the acoustic space of **Hitsville Reverb Chambers**.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (gain set to 0).

---

### 2. Faust Virtual Analog Front-End

#### Module 1: Liberty Burnisher
* **Heritage:** Discrete harmonic polisher & Baxandall treble/mid booster.
* **Role:** Enhances pick attack transients, clears mud from the humbucker neck position, and adds airy 70s studio sparkle.

#### Module 2: MattFoley
* **Heritage:** Parallel dual-J201 JFET discrete boost.
* **Role:** Adds dynamic tactile punch and harmonic motivation ahead of the Tweed tube stage.

---

### 3. UADx Paradise Guitar Studio / Woodrow '55 — Tweed Soul Foundation

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Instrument Volume** | `4.5` | Sweet edge-of-breakup harmonic compression. |
| **Mic Volume** | `3.0` | Blended secondary gain channel for body. |
| **Tone** | `5.5` | Balanced top-end roll-off retaining vocal warmth. |

---

### 4. Post-Amp Dynamic Smoothing: UADx Teletronix LA-2A Silver

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Mode** | `Compress` | Smooth optical gain reduction for funk strum consistency. |
| **Peak Reduction** | `35` | 2–3 dB of optical compression on strong chord chops. |
| **Gain** | `28` | Clean studio makeup gain. |

---

### 5. Acoustic Space: UADx Hitsville Reverb Chambers

| Control | Setting | Purpose |
| :--- | :--- | :--- |
| **Decay** | `1.8s` | Tight Detroit Motown/Stax chamber reflection. |
| **Mix** | `15%` | Subtle three-dimensional depth without cluttering rhythmic syncopation. |
| **Pre-Delay** | `12.0 ms` | Preserves immediacy of the pick stroke before reverb bloom. |
