---
amp: "Dream '65 (UADx)"
created: 2026-07-26
guitar: "Gibson Les Paul Studio (490R neck pickup)"
id: dream-65-dual-rig-clean
pickup_type: humbucker
preset_name: "Dream 65 Dual Rig Clean HB"
status: initial
tags: "dual-amp, clean, blackface, dream-65, humbucker, glass, foundation"
target: 'Clean foundation amp for the parallel dual-amp setup. Provides glassy high-end air, deep tight bass, and uncompromised pick-attack transients alongside the Enigmatic 82.'
tone-king-channel: bypassed
updated: 2026-07-26
preset_data:
  amp_platform: uad_paradise
  amp_settings:
    Bass: 5.5
    Bright: false
    Cab: "2x12 JBF120"
    Reverb: 0.0
    Treble: 5.0
    Volume: 2.8
  nashville_overdrive:
    enabled: false
    gain: 2.5
    output: 6.0
    tone: 5.0
  gold_overdrive:
    enabled: false
    gain: 0.0
    output: 7.5
    treble: 4.5
  ts_overdrive:
    enabled: false
    drive: 3.0
    level: 7.0
    tone: 5.0
  hitsville:
    decay: 2.0
    mix: 0.10
    pre_delay: 8.0
  la2a:
    gain: 28.0
    peak_reduction: 32.0
---

# Dream '65 — Dual Rig Clean Foundation

## Target Sound

This toneprint represents **Path A (Clean Foundation)** in our parallel dual-amp rig. 

While Amp B (Enigmatic '82 inside Paradise) handles driven warmth, mid-range body, and overdrive pedals, the **UAD Dream '65** remains 100% clean, uncompressed, and pristine at all times. Paired with the **2x12 JBF120** (JBL D120F 2x12 cab), it delivers crystalline Fender Blackface top-end glass, open 3D air, and tight low-end authority, guaranteeing that chord articulation and transient pick attack are never lost even when the secondary amp is pushed into heavy drive.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean headroom; D.I. offset **-3.2 dB**).

---

### 2. UADx Dream '65 Reverb Amp — clean glass platform

| Control | Setting | Purpose |
|---------|---------|---------|
| Bright / Normal | **Normal** | Keeps top end smooth and prevents harshness with humbuckers |
| Mod Circuit | **Stock** | Cleanest, most linear Deluxe Reverb response |
| Volume | **2.8** | Maximum clean headroom; zero breakup |
| Treble | **5.0** | Crystalline top-end air |
| Bass | **5.5** | Tight, authoritative low-end fundamental |
| Reverb | **0.0** (Off) | Internal spring reverb off (relying on shared post-summing room reverb) |
| Tremolo | **Off** | — |
| Input Trim | **-3.2 dB** | Interface calibration offset |
| Cab | **2x12 JBF120** | JBL D120F 2x12 speaker cabinet (open, glassy top-end and 3D width) |

---

### 3. Amp Bus Mixer Gain Staging & Post-Summing LA-2A

* **Channel Parity Balance:** Trim the Enigmatic (Path B) channel by approximately **-5.5 dB** (keeping Dream '65 Path A at 0.0 dB) in the Element `Amp Bus Mixer` so both paths show visual level parity on the meters.
* **Master Summation Level:** Set the `Amp Bus Mixer` Master output fader to **-8.0 dB** to compensate for parallel dual-amp summation and prevent digital ceiling clipping.
* **Compressor:** UAD Teletronix LA-2A Silver (Peak Reduction 32, Gain 28) placed *after* the `Amp Bus Mixer`. Receives the -8 dB attenuated sum to hit target **-1 to -3 dB GR** on hard strums.
* **Reverb:** UAD Capitol Chambers / Hitsville (Mix 10%, Decay 2.0s, Pre-Delay 8ms) placed on parallel aux send.

---

## Starting Point Guide

- **Volume Sweet Spot:** Keep Volume below 3.0 to ensure zero distortion occurs on Path A when playing hard strums.
- **Cab Choice:** Use **2x12 JBF120** for maximum high-frequency glass and 3D separation around Path B's mid-range.
- **Mixer Faders:** Set `Amp Bus Mixer` Master fader to **-8.0 dB** and trim Path B by **-5.5 dB** for clean gain staging into the LA-2A compressor.
