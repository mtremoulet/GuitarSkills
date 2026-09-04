---
id: lion-68-clapton-woman-tone
preset_name: "Lion '68 Clapton Woman Tone"
created: "2026-06-28"
updated: "2026-06-28"
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (Neck Humbucker, Vol 10, Tone 0)"
target: 'Iconic 1967–1968 Eric Clapton Cream ''Woman Tone'' using cranked Marshall Plexi saturation, EP-3 preamp boost, 1176 sustain glue, and rolled-off guitar tone control.'
tags: "clapton, cream, woman-tone, humbucker, plexi, marshall, lion-68, paradise-studio, uad_paradise"
tone-king-channel: bypassed
amp: "Lion '68 (UADx)"
status: initial
pickup_type: humbucker
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Model: Lead
    Volume_1: 5.5
    Volume_2: 3.5
    Treble: 6.0
    Middle: 7.0
    Bass: 4.5
    Presence: 6.5
    Room: 25.0
    "Input Routing": Low
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  ep3_boost:
    enabled: true
    boost: 1.5
  pgs_1176:
    enabled: true
    ratio: "4:1"
  standalone_1176:
    input: 30.0
    output: 18.0
    ratio: 4
    attack: 3
    release: 5
---

# Lion '68 — Eric Clapton "Woman Tone" (Paradise Guitar Studio)

## Target Sound

This toneprint captures the legendary **"Woman Tone"** pioneered by Eric Clapton during Cream's 1967–1968 era on tracks like *"Sunshine of Your Love,"* *"SWLABR,"* and *"I Feel Free."*

The hallmark of the Woman Tone is a singing, vocal, horn-like or cello-like sustain where all high-frequency picking harshness is removed at the instrument, while the cranked amplifier generates rich, blooming upper harmonics. 

By running your humbucker guitar's **tone control turned down to 0** into a cranked 100-watt Marshall Plexi stack (**UADx Lion '68** hosted in **Paradise Guitar Studio**), pushed by vintage tape preamp color and smoothed by studio 1176 FET compression, this self-contained chain produces infinite sustain and vocal clarity.

---

## Guitar Physical Setup (CRITICAL)

To achieve the Woman Tone, the physical guitar setup is **non-negotiable**:

| Control | Setting | Purpose |
|---------|---------|---------|
| Pickup | **Neck Humbucker** (or Neck + Bridge blend) | Captures fat fundamental string vibrations |
| Guitar Volume | **10** (Dimed) | Delivers maximum signal level to drive the preamp |
| Guitar Tone | **0** (Rolled completely off) | Applies a steep low-pass filter (~400 Hz) eliminating high-frequency glare |

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom).

---

### 2. UADx Lion '68 Super Lead — character source

#### Amp & Cabinet Settings
(UADx Lion '68 Super Lead)

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **Lion '68 (LEAD)** | 100W Super Lead Plexi model |
| Input Routing | **HIGH** | High-sensitivity input for maximum saturation |
| Volume 1 (Bright) | **8.0** | **Pushed to 8.0:** Drives virtual power tubes into thick, singing saturation |
| Volume 2 (Normal) | **6.0** | **Pushed to 6.0:** Blends in deep low-end body and sustain |
| Treble | **6.0** | High-frequency tone stack contour |
| Middle | **7.5** | **Pushed to 7.5:** Provides dense vocal midrange weight |
| Bass | **5.0** | Keeps low end tight and controlled |
| Presence | **6.0** | Adds power-amp brilliance to balance the zeroed guitar tone knob |
| Cabinet | **4×12 Stripped On-Axis** | Celestion Greenbacks mic'd with Ribbon 160 + Dynamic 57 blend |
| Room Level | **25%** (`2.5`) | Integrated room acoustic reflections; provides natural spatial air without external reverbs |

---

#### Pre-FX Option: Gold Overdrive & EP-3 Boost
We configure two classic pre-amp drive options in the Pre-FX slots so you can toggle between them:

| Control | Setting | Default State | Purpose & Aesthetic Profile |
|---------|---------|---------------|-----------------------------|
| **EP-3 Preamp / Boost** | **Boost: 3.5** | **ENABLED (ON)** | **Primary Historical Choice:** Emulates vintage Echoplex EP-3 tape preamp saturation. Adds organic harmonic girth and pushes tube front-end for authentic 60s Cream roar. |
| **Gold Overdrive** | `Gain: 0.0`, `Output: 7.5`, `Treble: 4.5` | **DISABLED (OFF)** | **Transparent Boost Option:** Engage as an alternative to add clean level lift and focused midrange punch for modern solo projection. |

*Note: For authentic Cream tone, keep EP-3 Boost ON and Gold Overdrive OFF.*

---


### 3. Amp & Cabinet Pane (UADx Lion '68 Super Lead)

| Control | Setting | Purpose |
|---------|---------|---------|
| Amp Model | **Lion '68 (LEAD)** | 100W Super Lead Plexi model |
| Input Routing | **HIGH** | High-sensitivity input for maximum saturation |
| Volume 1 (Bright) | **8.0** | **Pushed to 8.0:** Drives virtual power tubes into thick, singing saturation |
| Volume 2 (Normal) | **6.0** | **Pushed to 6.0:** Blends in deep low-end body and sustain |
| Treble | **6.0** | High-frequency tone stack contour |
| Middle | **7.5** | **Pushed to 7.5:** Provides dense vocal midrange weight |
| Bass | **5.0** | Keeps low end tight and controlled |
| Presence | **6.0** | Adds power-amp brilliance to balance the zeroed guitar tone knob |
| Cabinet | **4×12 Stripped On-Axis** | Celestion Greenbacks mic'd with Ribbon 160 + Dynamic 57 blend |
| Room Level | **25%** (`2.5`) | Integrated room acoustic reflections; provides natural spatial air without external reverbs |

---

### 4. Post-FX Dynamics (1176FET Compression & A/B Options)

We provide two compression routing paths so you can A/B test between the internal all-in-one workflow and a standalone plugin insert:

#### Primary Workflow: Internal PGS 1176 (Self-Contained)
*   **Module**: **1176 Compression** in Paradise Guitar Studio Post-FX Slot 1
*   **State**: **ENABLED (ON)**
*   **Ratio**: **4:1**
*   **Attack / Release**: Medium-Fast attack, fast release
*   **Purpose**: Squeezes out endless sustain right inside the single plugin window.

#### Optional A/B Alternative: Standalone UADx 1176LN Plugin Insert
If you prefer to A/B test against a standalone compressor insert in Logic Pro:
1. Turn **OFF** the internal 1176 module in Paradise Guitar Studio's Post-FX tab.
2. Insert **UADx 1176LN (Rev E or Bluestripe)** immediately after Paradise Guitar Studio on your DAW track:

| Control | Setting | Purpose |
|---------|---------|---------|
| Input | **30** (Adjust for `4–6 dB` GR) | Peak reduction threshold |
| Output | **18** | Makeup gain calibration (~ −12 dBFS) |
| Ratio | **4:1** | Smooth FET peak control |
| Attack | **3** (~9 o'clock) | Allows pick attack transient through |
| Release | **5** (~3 o'clock) | Fast recovery for maximum sustain bloom |

---

## Starting Point Guide

- **The "Tone Knob" Dial-In:** If setting your guitar tone to exact **0** feels slightly too dark on your neck humbucker, crack it open slightly to **1.5 or 2.0** until the vocal resonance hits the sweet spot.
- **Solo Boost Switch:** To push from rhythm warmth into soaring lead sustain, engage the **Gold Overdrive** pedal in the Pre-FX slot alongside the EP-3 Boost.

---

## Feedback History

### 2026-06-28 — initial
Created as a dedicated humbucker toneprint for Eric Clapton's Cream "Woman Tone". Uses Lion '68 Super Lead inside Paradise Guitar Studio, dual Pre-FX boost options (EP-3 Boost enabled by default, Gold Overdrive disabled), 25% internal room level, and built-in 1176 Post-FX compression with standalone UADx 1176LN A/B documentation.
