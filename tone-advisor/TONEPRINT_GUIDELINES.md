# Toneprint Best Practices & Guidelines

This document establishes the standards for creating, refining, and documenting guitar tones in the `tones/` directory. All agents and skills generating tone recommendations should adhere to these principles to ensure consistency across Mike's sessions.

---

## 1. Core Philosophy: The "Clean Foundation"
Mike's rig is designed for high-fidelity monitoring (Sennheiser HD660S2). The goal is clarity and touch-sensitivity, even in high-gain contexts.
- **Transparency First**: Start with the most neutral signal path possible. Only add color (amps, drives) once the gain staging is solid.
- **Explain the "Why"**: Always provide a technical rationale for a setting (e.g., "Set Peak Reduction to 40 to avoid raising the noise floor during note decay").
- **Host Architecture (Standalone Audio & Element)**: Logic Pro is shelved from Mike's active toolkit until further notice. All new toneprints must be designed for:
  - **Standalone Audio (by Oort Media)**: Primary host for linear, single-amp AU plugin chains (compiled via `scripts/compile_standalone_presets.py`).
  - **Kushview Element**: Primary host for modular parallel and dual-amp signal chains (`.els` session graphs).
  - *Legacy Logic Presets*: Existing Logic Pro presets (`.pst`) and toneprints remain preserved as legacy artifacts, but do not design new toneprints that require Logic-native plugins (native Channel EQ, Logic Compressor) or Logic bus architecture.
- **Evidence-Based Recommendations & Knowledge Qualification**:
  - **Pre-Trained Knowledge Qualification**: Any historical amplifier context, hardware/component behavior, cabinet and speaker acoustic characteristics, microphone response tendencies, guitar pickup/pot interactions, or technical audio engineering claims originating from internal parametric memory (and not directly extracted from user inputs, workspace files, or executed live searches) must be prefaced with *"I know that..."* or *"My trained knowledge includes that..."*.
  - **First-Source Evidence Citation**: Facts, parameter names, valid control ranges, interface calibration offsets, plugin specifications, or preset schema definitions extracted from workspace documents (e.g., `tone-advisor/docs/`, `tone-advisor/gear-inventory.md`, `tone-advisor/GAIN_STAGING_STANDARDS.md`, `tones/INDEX.md`, CSV indices, XML/JSON presets) or executed searches must cite the exact workspace file path or search source.

---

## 2. Physical Hardware Standards

### Input Path & Amp Architecture (Tone King vs. Amp Plugins)
- **Mutual Exclusivity (Tone King Preamp OR Software Amp)**: A toneprint uses **EITHER** the physical Tone King Imperial Preamp **OR** a software amp modeler (UADx, Neural DSP, Nembrini, MixWave), **never both**. Do not run the Tone King Preamp into an amp simulation plugin (avoid double-preamping / double-amping).
  - **Direct Input Path (Default for Amp Plugins)**: `[Guitar] → [iD14 Input 1 (D.I.)] → [Host: Standalone Audio or Kushview Element]`. Software amp modelers receive a pure, uncolored Hi-Z instrument signal.
  - **Hardware Preamp Path (Tone King Preamp as Amp Foundation)**: `[Guitar] → [Tone King Imperial Preamp] → [iD14 Line In / Direct Monitoring]`. When the Tone King is active, any software plugins are restricted to transparent post-processing (no software amp sim).

### Tone King Imperial Preamp (If Route Active)
If the Tone King is used as the primary amplifier/preamp foundation:
- **Channel**: Rhythm (clean American Blackface) or Lead (tweed/rock crunch).
- **Volume**: Dial for desired clean headroom or preamp breakup.
- **Attenuation**: **5.0** (unity/moderate).
- **EQ**: **5.0 (Noon)** for flat baseline, adjust as needed.
- **IR**: Active (select desired built-in IR) or use a dedicated IR loader / cab plugin in Logic. Never run into a full amp modeler.
- **Effects**: Reverb/Tremolo as dialed.

### TONEX One
- **Default**: Bypassed (Stomp mode).
- **Usage**: Only active when a specific hardware capture (e.g., "Klon Centaur", "Dumble ODS") is requested as a "pre-pedal" boost or a complex rig replacement.

---

## 3. Gain Staging & Levels (Reference Only)
While preventing clipping across the Logic signal chain is a priority, Mike manages plugin-level gain stages (Input/Output sliders) manually during the session. These utility trims **should not** be included as fixed settings in the toneprint's Signal Chain tables unless specifically requested to solve a unique interaction.

### Target Baselines (For Reference)
- **Interface Input (iD14)**: Aim for peaks around **−18 dBFS** for raw DI tracks.
- **DAW Track Output**: Aim for **−12 dBFS** to **−10 dBFS** on hard strums.
- **Plugin Context**: When recommending a tone, the advisor should focus on the **character controls** (Volume, Master, Drive, EQ). If a model is known to run hot (e.g., Nembrini or Ruby '63), simply add a brief note: *"Note: This model runs hot; check plugin output levels to ensure headroom in Logic."*

### Audio Interface Calibration Offsets (D.I. Route)
Amp sim manufacturers model their virtual components based on a specific analog-to-digital hardware reference level.
- **Neural DSP & UADx Standard**: Modeled around a **+12.2 dBu** clipping point (matching UAD Apollo Twin Hi-Z input at minimum gain).
- **Audient iD14 D.I. Input**: Clips at **+9.0 dBu** at minimum gain.
- **Calibration Correction**: The Audient iD14 D.I. input delivers a digital signal that is **3.2 dB hotter** than the plugins expect. To achieve a true 1:1 hardware-accurate response:
  - **Neural DSP & UADx Plugins**: Set the plugin's internal **Input Gain (IN)** control to **-3.2 dB**.
  - **IK Multimedia (TONEX)**: Offset the typical input trim (use **-3 dB to 0 dB** for humbuckers, and **+2 dB to +5 dB** for single-coils).
  
### Tone King Preamp Routing (Hardware Preamp Route)
The Tone King Imperial Preamp output is a balanced, line-level signal.
- **Connection**: Connect the Tone King's XLR balanced output to the back combo jacks of the iD14 using an **XLR-to-TRS (1/4") cable**. This forces the iD14 to treat the signal as a **Line input**, bypassing the microphone preamp circuitry.
- **Gain Staging**: Set the iD14 input gain to **minimum (unity/0 dB)**. Control the signal level exclusively from the Tone King's **Volume** and **Attenuation** dials, aiming for peaks between **-12 dBFS and -10 dBFS** in Logic.

---

## 4. Routing & Spatial Effects (Reverb/Delay)

### The "Bus-First" Standard
For all spatial effects (Reverb, Delay), the preferred practice is to use a **Bus/Aux Send** rather than an inline Insert. 

- **Why**:
    - **Linear Control**: UADx plugins (like Capitol Chambers and Hitsville) use logarithmic Mix dials that are extremely sensitive. It is far easier to dial in a precise blend using a Logic Send knob or an Aux fader.
    - **Clarity & Punch**: Keeping the dry signal on the main track ensures the guitar's attack and core tone stay centered and "un-smeared."
    - **Consistency**: Using a standard bus (e.g., **Bus 3 for Reverb**, **Bus 4 for Delay**) allows you to swap different toneprints while keeping a consistent spatial environment.
    - **Independent Processing**: Allows for EQing the reverb return (e.g., rolling off lows to prevent "mud") without affecting the primary guitar signal.

### The "Internal" Exception
Reverb or Tremolo that is **part of the amp model** (e.g., the spring reverb in the Dream '65 or the Tone King's built-in spring reverb) should stay internal. These are part of the "instrument" and the modeled gain stage.

### Setup Instructions
When recommending a bused effect:
1.  **Plugin Setting**: Set the plugin on the Aux track to **100% Wet**.
2.  **CRITICAL (UADx/Neural DSP)**: In many UADx plugins (like Hitsville) and Neural DSP, the **"Wet Solo"** button must be **OFF** if you want to use the plugin's own Mix dial for blending on the bus. If it's ON, the Mix dial is bypassed. Conversely, if using the Bus Fader for the mix, set Mix to 100% and Wet Solo to ON.
3.  **Send Level**: Suggest a starting send level (e.g., `-12 dB` to `-18 dB`).

---

## 5. Tone Sculpting & Problem Solving

### The "Jazz Middle" Rule
The Tone King Rhythm channel and many UADx Fender models have a natural "mid-scoop." To achieve a warm, vocal jazz tone:
- **Amp Middle**: Set to **7.0 (70%)** or higher to fill in the midrange.
- **Problem**: If the tone feels "thin" or "plucky," it's usually a lack of mids, not a lack of bass.

### The "High-Cut Veil"
To remove digital "fizz" or "air" and simulate a dark jazz box:
- **Logic EQ**: Apply a high-cut (low-pass) filter at **4.0 kHz** or **5.0 kHz** with a 24 dB/oct slope.
- **Why**: This creates the "electronic veil" (Ed Bickert style) that rounds off the transients.

### Microphone Selection
- **Dark/Warm**: Use **Ribbon 121** or **Ribbon 160**.
- **Balanced/Detailed**: Use **Condenser 414** or **U67**.
- **Punchy/Bright**: Use **Dynamic 57** or **421**.

---

## 6. Performance & Guitar Interactions

### The "7/7" Baseline
For almost all jazz and edge-of-breakup tones:
- **Guitar Tone Knob**: Roll back to **7** to take the edge off the high-end.
- **Guitar Volume Knob**: Roll back to **7 or 8** to clean up the input and increase touch-sensitivity.
- **Advisor Note**: Always state if a toneprint *requires* these physical adjustments to sound as intended.

### Picking Dynamics
Class A amps (Divided 11) and boutique drives (ODS) are built for dynamics.
- **Note**: If a tone feels "too gritty," suggest lighter picking before changing plugin settings.

---

## 7. Hybrid & Multi-Layer Tones

When blending acoustic and electric textures (e.g., **Acoustic Voice Pro**):
- **Isolation**: Keep the acoustic processing on its own track or a parallel bus to avoid "muddying" the electric amp's character.
- **Phase**: Be aware that layering multiple cab/IR simulations can cause phase issues. If the sound feels "hollow," try a different IR on one of the layers.

---

## 8. Documentation & Nomenclature

### Exact Labels
- Never guess a control name. Use the exact label from the documentation (e.g., "Mid-Bite" for Tone King Lead channel, "Echo Rate" for Galaxy Echo).
- If a control is stepped (e.g., "Head 1", "Normal/Bright"), use the exact labels.

### Tone Metadata (Frontmatter)
Every toneprint MUST include the following metadata in its YAML frontmatter to support filtering, preset compilation, and the Vault Viewer:
- **`id`**: Unique kebab-case slug matching the filename (without `.md`).
- **`pickup_type`**: Primary classification (Options: `humbucker`, `single-coil`, `p-90`). Note: "Universal" tones are not permitted; create distinct variants for each pickup type to ensure proper gain staging and EQ.
- **`guitar`**: The specific guitar used for testing/intended character (e.g., "Gibson Les Paul Studio", "Framus Earl Slick (DiMarzio P-90s)").
- **`target`**: A concise one-sentence description of the intended sound.
- **`tags`**: Comma-separated descriptive keywords for discovery and genre inference.
- **`amp`**: Human-readable amp name (e.g., "Dream '65 (UADx)", "Two-Rock Bloomfield (MixWave)").
- **`tone-king-channel`**: `bypassed` for all software amp plugin rigs; `rhythm` or `lead` when Tone King Imperial Preamp pedal is the physical front-end.
- **`status`**: Lifecycle state (Options: `initial`, `tested`, `refined`, `archived`).
- **`preset_data`**: A structured, machine-readable YAML block serving as the single source of truth for the automated preset compilers. Ensure closing `---` frontmatter delimiter is always preceded by a newline.

Schema structure under `preset_data`:
* `amp_platform`: Platforms include `uad_paradise`, `neural_dsp`, `mixwave`, or Nembrini platforms (`nembrini_jc120`, `nembrini_mrh810`, `nembrini_div11`, `nembrini_puretone`, `nembrini_acoustic_voice`).
* `amp_settings`: Key-value control mappings corresponding to the platform's specific amp model controls.
* `prefx`: Structured slots for host/plugin rack pedals (`slot1`–`slot5`, each specifying `pedal`, `enabled`, and pedal-specific parameters).
* `la2a`: Custom settings for UADx Teletronix LA-2A (keys: `peak_reduction`, `gain`, `compress`).
* `hitsville`: Custom settings for UADx Hitsville Reverb (keys: `mix`, `pre_delay`, `decay`, `wet_solo`).
* `logic_eq`: Logic native Channel EQ bands (keys: `band1` to `band8`, each specifying `on`, `freq`, `gain` or `slope`, and optionally `q` for bands 2–7).
* `logic_compressor`: Logic native Compressor controls (keys: `threshold`, `ratio`, `attack`, `release`, `makeup_gain`, `knee`).
* `kuassa_blues_barker`: Custom settings for Kuassa Efektor Blues Barker (keys: `gain`, `tone`, `level`, `type`).
* `kuassa_blues_river`: Custom settings for Kuassa Efektor Blues River (keys: `gain`, `tone`, `level`, `type`).
* `clon_minotaur` / `gold_overdrive`: Custom settings for Nembrini Clon Minotaur Klon emulation (keys: `gain`, `tone`, `level`).

### Markdown Body Structure (Vault Viewer Schema)
To ensure consistent parsing and clean rendering in the Vault Viewer, every toneprint markdown body must strictly follow this H2 section hierarchy:

1. **`# <Tone Title>`**: H1 title at the root of the markdown body.
2. **`## Target Sound`**: Sonic vision, reference artist/recording, dynamic response, and aesthetic profile.
3. **`## Signal Chain`**: Ordered plugin and hardware chain.
   - Format plugins as `### [Number]. [Plugin Name] — [Role]`
   - Parameter tables must use the standard 3-column header: `| Control | Setting | Purpose |`
4. **`## Starting Point Guide`**: Practical dialing guide, knob interactions, pickup positions, and touch-dynamics advice.
   - Bullet items must use dash notation with bold label: `- **Control / Focus**: Advice...`
5. **`## Feedback History`**: Chronological log of testing, monitoring environment, and refinements.
   - Entries must be formatted as: `### YYYY-MM-DD — status` (e.g. `### 2026-06-28 — refined`)

### Signal Chain Format
Always present the chain in order:
`[Hardware] → [Dynamics/Pre-FX] → [Amp] → [Cab/Mics] → [Post-FX EQ/Comp] → [Spatial/Reverb]`

---

## 5. The Feedback Loop & Lifecycle

Tones evolve through distinct lifecycle states, tracked in the `status` frontmatter:

1.  **`initial`**: Proposed by the advisor but not yet tested in a DAW session.
2.  **`tested`**: Verified in a session. Levels are confirmed, and the character matches the target.
3.  **`refined`**: Adjusted after actual practice/playing. The "sweet spots" have been found.
4.  **`archived`**: Retires a toneprint from the active library. The tone file remains intact in `tones/`, but is hidden by default in the HTML viewer. Its compiled plugin presets are moved into `quarantined/` to keep DAW/plugin preset menus clean and unburdened.

**Feedback History Rules**:
- Never delete old feedback.
- Append new entries with the date and status change.
- Note specific monitoring (e.g., "Tested on HD660S2", "Verified on THR10ii").

---

## 6. Comparison Protocol
When creating a tone to compare against an existing one (e.g., "Showtime vs Dream '65"):
- **Isolate the Variable**: Keep the Tone King, Guitar, and Post-FX identical.
- **Document the Difference**: Explicitly state what the new amp/plugin adds or takes away compared to the baseline.
