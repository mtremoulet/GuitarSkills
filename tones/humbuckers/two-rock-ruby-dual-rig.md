---
amp: "Two-Rock Bloomfield (MixWave) + Ruby '63 (UADx)"
created: 2026-08-08
guitar: "Gibson Les Paul Studio / Epiphone Sheraton II (Humbuckers)"
id: two-rock-ruby-dual-rig
pickup_type: humbucker
preset_name: "Two-Rock Ruby Dual Rig HB"
status: initial
tags: "dual-amp, humbucker, les-paul, sheraton, mixwave, two-rock, bloomfield, ruby, vox, chime, parallel"
target: 'High-contrast dual rig pairing plush boutique Dumble-style clean depth (Two-Rock Bloomfield) with glassy upper-mid Vox AC30 Top Boost chime (Ruby 63).'
tone-king-channel: bypassed
updated: 2026-08-08
dual_rig: true
amp_a:
  name: "Amp A — Two-Rock Bloomfield Drive (Boutique Clean)"
  model: "Two-Rock Bloomfield (MixWave)"
  platform: mixwave
  pan: -12
  amp_settings:
    Gain: 4.5
    Master: 6.5
    Treble: 4.5
    Middle: 5.5
    Bass: 5.0
    Presence: 5.0
    Reverb: 0
    Bright: false
    Deep: false
    Mid: false
amp_b:
  name: "Amp B — Ruby '63 (Vox Top Boost Chime)"
  model: "Ruby '63 (UADx)"
  platform: uad_paradise
  pan: 12
  amp_settings:
    Volume: 3.2
    Treble: 5.5
    Bass: 4.5
    Tone Cut: 4.5
    Cut: false
    Boost: false
    Cab: "2x12 Silver 15"
    Output Gain: 8.0
shared_fx:
  la2a:
    gain: 30.0
    peak_reduction: 40.0
  hitsville:
    decay: 2.0
    mix: 0.12
    pre_delay: 10.0

    wet_solo: false
---

# Two-Rock Bloomfield + Ruby '63 — Boutique Velvet & Vox Chime Dual Rig (Humbuckers)

## Target Sound

This dual-rig toneprint pairs two iconic boutique and vintage amplifier voices for humbucker guitars (**Gibson Les Paul Studio** and **Epiphone Sheraton II**):

* **Amp A (Left, Pan -12 — Plush Boutique Clean Anchor)**: The **MixWave Two-Rock Bloomfield Drive** supplies a deep, plush lower-midrange foundation, smooth note separation, and high-headroom Dumble-style warmth.
* **Amp B (Right, Pan +12 — Glassy Vox Harmonic Halo)**: The **UAD Ruby '63** (Vox AC30 Top Boost) adds brilliant high-frequency chime, upper-mid bite, and immediate pick attack.

Together, the Two-Rock eliminates humbucker dark mud while the Vox supplies a sparkling harmonic halo around every note.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
* **Status:** **Bypassed**
* **Signal Path:** Guitar direct into Audient iD14 Input 1 (Preamp gain at 0 dB).

---

### 2. Parallel Amp Configuration

#### Channel Strip A: Two-Rock Bloomfield Drive — Boutique Clean (Pan: -12 L)

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Clean** | High-headroom boutique clean platform |
| Gain | **4.5** | Touch-sensitive warm clean |
| Master | **6.5** | Clean power amp drive |
| Treble | **4.5** | Smooth, unharsh top end |
| Middle | **5.5** | Rich, vocal lower-mid body |
| Bass | **5.0** | Deep, tight fundamental |
| Presence | **5.0** | Natural air |

#### Channel Strip B: Ruby '63 — Vox Top Boost Chime (Pan: +12 R)

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | **Top Boost** | Brilliant harmonic chime |
| Volume | **3.2** | Clean Top Boost sweet spot for humbuckers |
| Treble | **5.5** | High-frequency jangle and string definition |
| Bass | **4.5** | Tightened low end |
| Tone Cut | **4.5** | Smooths out top-end glass |
| Boost | **Off** | Linear headroom |
| Cab | **2x12 Silver 15** | Vintage Vox Silver Bulldog cab |
| Output Gain | **8.0 dB** | Trimmed -4.0 dB inside Paradise plugin to match Amp A |

---

### 3. Parallel Submix Bus & Level Parity

* **Short-Term LUFS Metering**: Solo Amp A and Amp B independently using Logic's Loudness Meter. Adjust Amp B output so both read **-20.0 Short-Term LUFS**.
* **Submix Bus Compressor**: UAD LA-2A Silver (Peak Reduction **40.0**, Gain **30.0**) pulling **-1.5 to -3.0 dB GR**.
* **Spatial Reverb**: UAD Hitsville Chambers (Mix **12%**, Pre-Delay **10ms**) on parallel aux send.

---

## Starting Point Guide

- **Les Paul Neck Pickup**: Set neck volume to **8.0** for warm jazz-blues rhythm, roll up to **10** for singing lead notes.
- **Sheraton Flatwounds**: The Vox Top Boost on Amp B restores string clarity and harmonic air to flatwound strings without needing treble boost on the amp.
