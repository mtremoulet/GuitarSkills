---
id: "retro-memorex-showtime-hb"
preset_name: "Retro Memorex"
created: "2026-09-04"
updated: "2026-09-04"
guitar: "Epiphone Sheraton II / Gibson Les Paul Studio (Humbuckers)"
target: "Worn-tape lo-fi warmth and lush 80s algorithmic digital hall reverb anchored on the high-headroom Showtime '64 clean platform; inspired by the zero-delay El Capistan hack and Flint 80s hall on Charlie Parker bebop phrasing."
tags: "jazz, bebop, lo-fi, tape, echoplex, showtime, lexicon-224, 80s-hall, sheraton, les-paul, humbucker, clean, paradise-studio"
tone-king-channel: bypassed
amp: "Showtime '64 (UADx)"
status: initial
pickup_type: "humbucker"
preset_overrides:
  cab_and_mic: 29
preset_data:
  amp_platform: uad_paradise
  cab_and_mic: 29
  amp_settings:
    Volume: 3.8
    Treble: 5.0
    Middle: 6.5
    Bass: 4.5
    Bright: false
  prefx: {}
  postfx:
    slot1:
      pedal: ep_iii_tape_echo
      enabled: true
      time: 0.02
      feedback: 0.0
      mix: 100.0
      wonk: 6.0
      age: 2
      rec_level: 0.5
      preamp_color: true
      tone: -2.0
    slot2:
      pedal: reverb_224
      enabled: true
      program: 1
      mid_reverb_time: 14000
      bass_reverb_time: 12000
      treble_reverb_time: 16000
      pre_delay: 1200
      mix: 8000
      input: 3.0
      output: 3.0
      pitch: 1
---

# Retro Memorex — Worn Tape & 80s Hall Showtime Clean (Humbuckers)

## Target Sound

The sonic vision of **Retro Memorex** is inspired by a creative pedal hack: taking a tape delay (like the Strymon El Capistan) and dialing the delay time down to absolute minimum with repeats at zero and the mix at 100% wet. Rather than generating repeats, the delay processor's tape simulation becomes the fundamental tone itself. The guitar sound inherits the mechanical wow and flutter, tape saturation, and bandwidth rolloff of worn magnetic tape, dissolving pick transients into a warm, wobbly, nostalgic aura. This tape-aged signal then blooms into an expansive, modulating 1980s algorithmic digital hall reverb (modeled on the Lexicon 224, matching the Strymon Flint's 80s mode).

To achieve this without muddying or breaking up complex jazz chord voicings and fast bebop lines (such as Charlie Parker phrases over *"Cherokee"*), this toneprint is anchored on the ultra-clean, high-headroom **Showtime '64** amplifier model inside **UADx Paradise Guitar Studio**. 

Tested with humbuckers — especially the **Epiphone Sheraton II** strung with **Thomastik-Infeld Jazz Swing Flatwound 10s** (and equally adaptable to the 2014 **Gibson Les Paul Studio** 490R neck humbucker) — this tone delivers a thick, woody acoustic bloom, pillowy transients, and lush, three-dimensional stereo depth under headphones.

---

## Signal Chain

```
[Sheraton II / Les Paul] → [Audient iD14 (JFET DI)] → [Standalone Audio / Kushview Element] 
  → [UADx Paradise Guitar Studio (Showtime '64 → 2x12 Showman Cab → EP-III Tape Echo → Reverb 224)]
```

### 1. Physical Hardware & Interface Front-End — Audient iD14 mkII

*First-Source Citation*: Baseline levels and hardware calibration offsets are sourced from [`tone-advisor/GAIN_STAGING_STANDARDS.md`](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/GAIN_STAGING_STANDARDS.md) and [`tone-advisor/TONEPRINT_GUIDELINES.md`](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/TONEPRINT_GUIDELINES.md#L51-L58).

| Component / Control | Setting | Purpose |
|---|---|---|
| **Guitar Input** | JFET Instrument Input 1 (D.I.) | Discrete JFET high-impedance instrument stage provides natural musical buffer |
| **iD14 Input Gain** | Minimum (0 dB) | Sets cleanest digital headroom; prevents digital clipping before host processing |
| **Tone King Imperial Preamp** | **Bypassed** | Direct instrument feed into software modeler to avoid double-preamping |
| **Plugin Input Trim** | **-3.2 dB** | Corrects Audient +9.0 dBu clipping point to match UAD's modeled +12.2 dBu calibration standard |

---

### 2. UADx Paradise Guitar Studio — Showtime '64 & Post-FX Rack

*First-Source Citation*: Control names, internal parameter trees, and routing architecture are extracted from [`tone-advisor/docs/uad/paradise-guitar-studio.md`](file:///Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/docs/uad/paradise-guitar-studio.md) and the plugin's schema definitions in [`scripts/preset_compiler/uad.py`](file:///Users/miketremoulet/claude-projects/GuitarSkills/scripts/preset_compiler/uad.py).

#### A. Pre-FX Menu (Pedals In Front of Amp)
- **All Pre-FX Slots (1–5)**: **Disabled (Off)**. *I know that* putting tape flutter or intense modulation in front of the amplifier causes the amp's preamp tubes to distort the tape noise and narrows the frequency range before the power section. Bypassing all pre-amp stompboxes preserves the pristine guitar signal.

#### B. Amplifier: Showtime '64 (Clean Platform)
*I know that* the Showtime '64 is modeled after high-power Fender Showman/Twin style circuits with 6L6 power tubes, known for massive clean headroom and firm transient punch.

| Control | Setting | Purpose |
|---|---|---|
| **Volume** | **3.8** | Clean sweet spot. Stays completely linear and headroom-rich; accommodates firm humbucker plucks without clipping or rasp |
| **Treble** | **5.0** | Flat baseline. Keeps string definition intact without adding glassy spike |
| **Middle** | **6.5** | **The Jazz Middle Rule**: Counteracts the natural mid-scoop of American blackface circuits, thickening the fundamental of bebop lines |
| **Bass** | **4.5** | Tightens the low-end so flatwounds or neck humbuckers stay articulate and woody without tubbiness |
| **Bright Switch** | **OFF** | Disables the bright cap to avoid brittle high-frequency hiss or exaggerated tape noise |

#### C. Cabinet & Mics
*First-Source Citation*: Cabinet pairing index `cab_and_mic: 29` documented in [`docs/mayer-trinity-rig-guide.md`](file:///Users/miketremoulet/claude-projects/GuitarSkills/docs/mayer-trinity-rig-guide.md#L78).

| Component | Setting | Purpose |
|---|---|---|
| **Cabinet** | **2x12 Showman** (`cab_and_mic: 29`) | High-headroom 2x12 enclosure with open, uncompressed projection and fast transient response |
| **Mics** | Ribbon 121 + Dynamic / Condenser blend | Ribbon mic rounds off fast pick clicks and imparts smooth, woody low-mids |

#### D. Post-FX Studio Rack: EP-III Tape Echo & Reverb 224
*Conceptual & Architectural Note*: Conceptually, the Post-FX section in Paradise Guitar Studio represents studio rack gear applied after the mic'd speaker cabinet at the mixing console. Patching the tape machine and digital reverb post-cab ensures that the entire mic'd amplifier sound gets printed to the tape medium, and the Lexicon 224 digital reverb blooms in full, unclipped stereo across your headphones.

##### Post-FX Slot 1: EP-III Tape Echo (The Tape Hack)
*I know that* the Maestro Echoplex EP-3 is the quintessential solid-state tape delay. By running at minimum delay time and 100% wet, we convert it into a real-time tape coloration unit.

| Control | Setting | Purpose |
|---|---|---|
| **Power** | **ON** | Engaged |
| **Time** | **0.02s (~20 ms)** | Minimum delay time. Psychoacoustically perceived as instantaneous playing rather than an echo |
| **Feedback** | **0.0%** | Zero repeats. Every plucked note makes a single pass across the tape loop |
| **Mix** | **100.0%** | **Kill Dry**: Forces the full guitar signal through the tape circuit, completely avoiding comb filtering |
| **Wonk** | **6.0** | UAD's tape wow and flutter parameter. Introduces vintage tape motor drift, capstan irregularities, and pitch warble |
| **Age** | **2 (Used/Old)** | Simulates an aged tape cartridge: rolls off extreme highs, adds low-mid compression and tape saturation |
| **Rec Level** | **+0.5 dB** | Pushes the tape formulation slightly into harmonic tape compression |
| **Preamp Color** | **ON** | Engages the iconic EP-3 discrete JFET preamp circuit, adding thickness and warmth |
| **Tone** | **-2.0** | Darkens the tape playback response for an intimate, vintage jazz aesthetic |

##### Post-FX Slot 2: Reverb 224 (Lush 80s Digital Hall)
*I know that* the Strymon Flint's 80s reverb mode was inspired by the late-70s / early-80s Lexicon 224 digital microprocessor reverberator, famous for rich, modulating reverb tails that wrap around the instruments without cluttering the center image.

| Control | Setting | Purpose |
|---|---|---|
| **Power** | **ON** | Engaged |
| **Program** | **1 (Concert Hall)** | Classic 80s algorithmic hall program with wide stereo diffusion and subtle tail modulation |
| **Mid Reverb Time** | **14000 (~2.8s)** | Expansive, lush decay tail that hangs delicately behind sustained chord voicings |
| **Bass Reverb Time** | **12000 (~2.2s)** | Slightly tighter low-frequency decay to prevent boominess on the low E and A strings |
| **Treble Reverb Time** | **16000** | Warm top-end damping on the reflections, keeping the tail velvety and non-metallic |
| **Pre-Delay** | **1200 (~20 ms)** | Leaves a tiny pocket of breathing room after the initial pick strike before the hall blooms |
| **Mix** | **8000 (~20%)** | Creates a wide, atmospheric halo in stereo headphones while keeping the primary guitar voice forward |

---

## Starting Point Guide

- **Guitar Physical Baseline**:
  - **Epiphone Sheraton II**: Select the **Neck Humbucker**. Set physical **Guitar Volume to 7.5** and **Tone to 6.0–6.5**. *Why*: Rolling back the guitar tone knob at the instrument level tames high-frequency bite before the signal hits the Audient DI, giving the flatwounds that classic dark, velvet jazz "thump."
  - **Gibson Les Paul Studio**: Select the **490R Neck Humbucker**. Set physical **Guitar Volume to 7.0** and **Tone to 6.5**.
- **Adjusting Tape Wobble**:
  - If the pitch drift feels too seasick or dramatic for fast chord changes, dial the **Wonk** slider in the EP-III Tape Echo down to **3.5–4.5**. If you want a more extreme lo-fi, warped-cassette aesthetic (e.g., J-Dilla / Chillhop vibes), push **Wonk to 7.5–8.0**.
- **Controlling Reverb Density**:
  - In fast tempo bebop lines (like "Cherokee" at 200+ BPM), pull the Reverb 224 **Mix** back to **5000 (~12%)** or **Mid Reverb Time** to **10000 (~1.8s)** to prevent fast 8th-note runs from blurring together. For slow ballad chord-melody playing, push the Mix to **12000 (~25%)**.
- **Headphone Listening**:
  - *My trained knowledge includes that* the Lexicon 224 algorithm utilizes complex cross-channel all-pass diffusion networks. On Sennheiser HD660S2 headphones, the stereo image will feel remarkably deep and immersive, mimicking the wide stereo Flint setup heard in the reference video.

---

## Feedback History

### 2026-09-04 — initial
Created as the dedicated "Retro Memorex" toneprint for humbuckers (Epiphone Sheraton II and Gibson Les Paul Studio). Employs the zero-delay / 100% wet tape delay hack using Paradise Guitar Studio's internal EP-III Tape Echo (Wonk 6.0, Age 2, Preamp Color ON) into the vintage Reverb 224 (Concert Hall program) running post-cabinet. Grounded on the ultra-clean, high-headroom Showtime '64 amplifier and 2x12 Showman cabinet to provide a pristine, unclipped canvas for bebop phrasing and tape-warmed warmth.
