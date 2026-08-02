---
amp: "Lion '68 + Dream '65 (UADx)"
created: 2026-08-02
guitar: "Squier Stratocaster (Single-Coils)"
id: strat-lion-dream-dual-rig
pickup_type: single-coil
preset_name: "Strat Lion Dream Dual Rig SC"
status: initial
tags: "dual-amp, stratocaster, single-coil, plexi, blackface, lion-68, dream-65, john-mayer, eric-johnson, parallel"
target: 'Mayer and Eric Johnson-inspired Texas-Plexi dual rig pairing British Marshall crunch (Lion 68) with American high-headroom clean (Dream 65) for Stratocaster.'
tone-king-channel: bypassed
updated: 2026-08-02
dual_rig: true
amp_a:
  name: "Amp A — Lion '68 (Plexi Crunch)"
  model: "Lion '68 (UADx)"
  platform: uad_paradise
  pan: -12
  amp_settings:
    Model: "Super Lead"
    Volume I (Bite): 4.2
    Volume II (Body): 3.8
    Input Routing: Low
    Treble: 5.5
    Middle: 5.2
    Bass: 4.5
    Presence: 4.0
    Cab: "4x12 GB25"
amp_b:
  name: "Amp B — Dream '65 (Fender Clean)"
  model: "Dream '65 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 2.8
    Treble: 5.0
    Bass: 5.2
    Bright: false
    Reverb: 0.0
    Cab: "2x12 JBF120"
shared_fx:
  la2a:
    gain: 30.0
    peak_reduction: 30.0
  hitsville:
    decay: 2.2
    mix: 0.12
    pre_delay: 12.0
---

# Lion '68 + Dream '65 — Stratocaster Dual Rig (Single-Coils)

## Target Sound

This toneprint implements **Approach 3 (British Plexi Crunch + High-Headroom American Clean)** from our [Parallel Dual-Amp Guide](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/PARALLEL_AMP_GUIDE.md), tailored for the **Squier Stratocaster** (Neck & "Quack" positions).

Inspired by the dual-rig architecture of **John Mayer**, **Eric Johnson**, and **Stevie Ray Vaughan**, this setup merges heavy British Plexi wallop with pristine Fender Blackface headroom.

* **Amp A (Left, Pan -12)**: **UAD Lion '68** (Super Lead Plexi) delivers punchy mid-range growl, dynamic distortion, and rich harmonic overtones.
* **Amp B (Right, Pan +12)**: **UAD Dream '65** (Deluxe Reverb) stays wide open, providing 3D spatial depth, tight low end, and articulate pick snapping.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Parallel Amp Configuration (UADx Paradise / Plugin Suite)

#### Channel Strip A: Lion '68 — Super Lead Plexi Crunch (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Model | **Super Lead** | Vintage 100W Plexi punch |
| Volume I (Bite) | **4.2** | Harmonic crunch and upper-mid response |
| Volume II (Body) | **3.8** | Low-mid thickness |
| Input Routing | **Low** | Keeps clean headroom intact for pedal stacking |
| Treble | **5.5** | High-end bite for Strat neck pickup |
| Middle | **5.2** | Warm Marshall midrange density |
| Bass | **4.5** | Tightened low end (prevents 4x12 cab mud) |
| Presence | **4.0** | Tames harsh upper harmonics |
| Cab | **4x12 GB25** | Vintage 25W Greenback basketweave cab |

#### Channel Strip B: Dream '65 — Fender Headroom Clean (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | **2.8** | Pristine clean platform |
| Treble | **5.0** | Smooth, uncolored top end |
| Bass | **5.2** | Authoritative bottom-end fundamental |
| Bright Switch | **Normal** | Keeps single coils balanced |
| Cab | **2x12 JBF120** | JBL D120F cab for open stereo width |

---

### 3. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Alignment**: Level Amp A and Amp B to match at **-19.5 Short-Term LUFS**. Note: Trim Lion '68 channel fader by `-2.5 dB` to compensate for Greenback cabinet density.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **30.0**, Gain **30.0**).
* **Spatial Ambience**: UAD Hitsville Chambers (Mix **12%**, Decay **2.2s**).

---

## Starting Point Guide

- **Pickup Selection**: Use **Position 4 (Neck + Middle "quack")** for funk/rhythm, and **Position 1 (Neck)** for bold Texas blues leads.
- **Single-Amp Drive Staging**: Feed a Klon Centaur (Clon Minotaur) into **Lion '68 (Amp A) only** to turn Amp A into a high-gain lead voice while Amp B maintains clean string definition.
