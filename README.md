# 🎸 GuitarSkills

An advanced guitar tone vault, dynamic preset compiler, and host session generator tailored for physical instruments and precision digital modeling.

Designed to eliminate friction from playing and practicing, **GuitarSkills** translates human-readable Markdown tone profiles into native presets for **Standalone Audio** (linear AU racks), **Kushview Element** (parallel/modular graphs), **Yamaha THR10ii**, and major virtual amp platforms (Universal Audio, Neural DSP, MixWave, Nembrini, Valhalla, and Kuassa).

---

## 🌟 Key Features

### 1. 🎛️ The Tone Vault & Interactive Viewers
A curated, calibrated tone database tailored to specific guitars, pickups, and physical front-end hardware:
* **Interactive Web Dashboards**:
  * **Tone Vault (`tone-advisor/tone-viewer.html`)**: Searchable, responsive single-amp dashboard with instant filtering by pickup family (Single-Coil, Humbucker, P-90), amp platform, genre, and guitar.
  * **Dual-Rig Viewer (`tone-advisor/dual-tone-viewer.html`)**: Interactive viewer dedicated to parallel dual-amp rigs (e.g., Fender Blackface clean anchor + Dumble lead bloom).
* **Automated Indexing**: Rebuilt dynamically from frontmatter via Python compilers (`tone-advisor/generate_tone_viewer.py`, `tone-advisor/generate_dual_tone_viewer.py`), automatically maintaining `tones/INDEX.md`.
* **Strict Calibration Standards**: Anchored by rigorous gain-staging and calibration specifications (`tone-advisor/TONEPRINT_GUIDELINES.md`, `tone-advisor/GAIN_STAGING_STANDARDS.md`) for the Audient iD14 mkII interface and Tone King Imperial Preamp.

### 2. ⚡ Dynamic Rig Preset Compiler
A modular Python compilation suite (`scripts/preset_compiler/`) that compiles Markdown tone profiles directly into native preset formats across hosts and plugins:
* **Standalone Audio AU Racks**: Compiles `.aupreset` plugin chains and Standalone session configurations for rapid daily playing.
* **Universal Audio (UADx)**: Generates native JSON presets for **Paradise Guitar Studio** (Dream '65, Ruby '63, Woodrow '55, Enigmatic '82, Showtime '64), **Teletronix LA-2A** (Silver & Gray), **Hitsville Chambers**, **Galaxy Tape Echo**, and **Studio D Chorus**.
* **Third-Party Platforms**: Generates presets for **Neural DSP Archetype Cory Wong X**, **MixWave Two-Rock Bloomfield Drive**, **Valhalla Supermassive**, and **Nembrini Audio** (Jazz Chorus, Divided 11, Mrh810, Acoustic Voice Pro, Puretone).
* **Yamaha THR10ii**: Translates tone parameters directly into `.thrl6p` hardware patch files.

### 3. 🧩 Kushview Element Modular Sessions
For complex parallel setups and dual-amp configurations:
* **Session Compiler**: `scripts/compile_element_session.py` compiles Markdown profiles into ready-to-play `.els` session files.
* **Smart Routing**: Configures input padding (-3.44 dB Audient iD14 calibration), parallel wet/dry summing matrices, and control symbol management.

---

## 📂 Project Structure

```
GuitarSkills/
├── scripts/                # Dynamic preset compilers & utilities
│   ├── preset_compiler/   # Modular preset generation package
│   ├── compile_all_presets.py
│   ├── compile_standalone_presets.py
│   ├── compile_dual_rig_presets.py
│   ├── compile_element_session.py
│   └── sync_toneprints.sh # One-direction sync to iCloud
├── tone-advisor/           # Dashboards, gear inventories & guidelines
│   ├── TONEPRINT_GUIDELINES.md # Calibration, gain staging & documentation rules
│   ├── GAIN_STAGING_STANDARDS.md # Interface & preamp calibration standards
│   ├── PARALLEL_AMP_GUIDE.md # Parallel & dual-amp architecture reference
│   ├── guitar_stable.md    # Canonical inventory of physical guitars, pickups & strings
│   ├── gear-inventory.md   # Complete hardware and plugin inventory
│   ├── generate_tone_viewer.py
│   ├── generate_dual_tone_viewer.py
│   ├── tone-viewer.html    # Interactive single-amp dashboard
│   └── dual-tone-viewer.html # Interactive dual-amp dashboard
├── tones/                  # Markdown tone definitions
│   ├── humbuckers/         # Dual-humbucker profiles (LP, Sheraton)
│   ├── single-coils/       # Single-coil profiles (Tele, Strat)
│   ├── p-90s/              # P-90 profiles (Framus Earl Slick, Epiphone LP Rebel 90)
│   ├── presets/yamaha/     # Compiled Yamaha THR patch files (.thrl6p)
│   └── INDEX.md            # Programmatically maintained master catalog
├── references/             # Format guides and MIDI session references
├── quarantined/            # Archived plugin presets from retired/modified toneprints
└── archive/                # Archived legacy DAW tools (Logic Pro scripts, Space Designer IRs - .gitignored)
```

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* Required packages:
  ```bash
  pip install -r requirements.txt
  ```

### Compiling Presets
To compile all toneprints into their respective native plugin directories:
```bash
python3 scripts/compile_all_presets.py
```
To compile Standalone Audio racks:
```bash
python3 scripts/compile_standalone_presets.py
```
To compile parallel dual-amp presets:
```bash
python3 scripts/compile_dual_rig_presets.py
```

### Building the Tone Viewers
Whenever tone profiles are modified or added in `tones/`:
```bash
# Rebuild single-amp tone viewer and update tones/INDEX.md
python3 tone-advisor/generate_tone_viewer.py --build-only

# Rebuild parallel dual-amp viewer
python3 tone-advisor/generate_dual_tone_viewer.py
```

### Syncing Toneprints to iCloud
To sync tone markdown files, THR patches, and HTML viewers to iCloud:
```bash
bash scripts/sync_toneprints.sh
```

---

## 🎸 Under the Hood: Mike's Stable
GuitarSkills profiles are customized around a real-world stable of physical instruments:
1. **Fender Player II Telecaster** (British Racing Green, Single-Coils, D'Addario XS 10-46)
2. **Gibson Les Paul Studio 120th Anniversary** (Ebony, 490R/490T Humbuckers, D'Addario XS 10-46)
3. **Squier Stratocaster "Partscaster"** (Light Blue, Tex-Mex Single-Coils, D'Addario XS 10-46)
4. **Epiphone Sheraton II** (Natural, Humbuckers, Thomastik Flats 10s)
5. **Epiphone Les Paul Standard Plus Top** (Vintage Sunburst, Tonerider Rebel 90 P-90s, D'Addario XS 10-46)
6. **Framus Earl Slick Artist Series** (Matte Black, DiMarzio P90s, Rotosound Yellows 10-46)
7. **Cort Standard AD Mini** (3/4 Dreadnought, Steel Strings)
8. **Washburn D-12** (Sentimental Dreadnought)
9. **1978 Fender Precision Bass** (3-Color Sunburst)

