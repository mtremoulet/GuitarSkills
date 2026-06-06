# Toneprint Best Practices & Guidelines

This document establishes the standards for creating, refining, and documenting guitar tones in the `tones/` directory. All agents and skills generating tone recommendations should adhere to these principles to ensure consistency across Mike's sessions.

---

## 1. Core Philosophy: The "Clean Foundation"
Mike's rig is designed for high-fidelity monitoring (Sennheiser HD660S2). The goal is clarity and touch-sensitivity, even in high-gain contexts.
- **Transparency First**: Start with the most neutral signal path possible. Only add color (amps, drives) once the gain staging is solid.
- **Explain the "Why"**: Always provide a technical rationale for a setting (e.g., "Set Peak Reduction to 40 to avoid raising the noise floor during note decay").

---

## 2. Physical Hardware Standards

### Input Path Priority
- **Default (Direct Input)**: Connect the guitar direct to the iD14 interface (bypassing the Tone King Imperial Preamp entirely). This is the cleanest, most neutral starting point for software amp modelers.
- **Tone King Preamp (Optional Coloration)**: Only route through the physical Tone King Imperial Preamp if you explicitly want the natural scooped flavor of its Rhythm channel or the mid-forward tweed crunch of its Lead channel as a foundation.

### Tone King Imperial Preamp (If Route Active)
If the Tone King is necessary for the vibe of the toneprint, follow these settings:
- **Channel**: Rhythm (cleanest headroom).
- **Volume**: **2.0 to 3.0**. This is the transparency zone; higher values start adding early Blackface preamp color.
- **Attenuation**: **5.0** (unity/moderate).
- **EQ**: **5.0 (Noon)** for flat response.
- **IR**: **Bypassed** if using any Logic/UAD/Nembrini amp or cabinet simulation. Active ONLY if the Tone King is providing the final speaker character.
- **Effects**: Off (unless specifically requested).

### TONEX One
- **Default**: Bypassed (Stomp mode).
- **Usage**: Only active when a specific hardware capture (e.g., "Klon Centaur", "Dumble ODS") is requested as a "pre-pedal" boost or a complex rig replacement.

---

## 3. Gain Staging & Levels (Reference Only)
While preventing clipping across the Logic signal chain is a priority, Mike manages plugin-level gain stages (Input/Output sliders) manually during the session. These utility trims **should not** be included as fixed settings in the toneprint's Signal Chain tables unless specifically requested to solve a unique interaction.

### Target Baselines (For Reference)
- **Interface Input (iD14)**: Aim for peaks around **−18 dBFS**.
- **DAW Track Output**: Aim for **−12 dBFS** to **−10 dBFS** on hard strums.
- **Plugin Context**: When recommending a tone, the advisor should focus on the **character controls** (Volume, Master, Drive, EQ). If a model is known to run hot (e.g., Nembrini or Ruby '63), simply add a brief note: *"Note: This model runs hot; check plugin output levels to ensure headroom in Logic."*

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
Every toneprint MUST include the following metadata in its YAML frontmatter to support filtering and search:
- **`pickup_type`**: Primary classification (Options: `humbucker`, `single-coil`). Note: "Universal" tones are not permitted; create distinct variants for each pickup type to ensure proper gain staging and EQ.
- **`guitar`**: The specific guitar used for testing/intended character (e.g., "Gibson Les Paul Studio").
- **`target`**: A concise description of the intended sound.
- **`tags`**: Descriptive keywords for discovery.
- **`preset_data`**: A structured, machine-readable YAML block serving as the single source of truth for the automated preset compilers. If this block is missing or incomplete, compilers will fall back to their regex engines to extract parameters from the Markdown body.

Schema structure under `preset_data`:
* `amp_platform`: Platforms include `uad_paradise`, `neural_dsp`, or `mixwave`.
* `amp_settings`: Key-value control mappings corresponding to the platform's specific amp model controls.
* `la2a`: Custom settings for UADx Teletronix LA-2A (keys: `peak_reduction`, `gain`, `compress`).
* `hitsville`: Custom settings for UADx Hitsville Reverb (keys: `mix`, `pre_delay`, `decay`).
* `logic_eq`: Logic native Channel EQ bands (keys: `band1` to `band8`, each specifying `on`, `freq`, `gain` or `slope`, and optionally `q` for bands 2–7).
* `logic_compressor`: Logic native Compressor controls (keys: `threshold`, `ratio`, `attack`, `release`, `makeup_gain`, `knee`).

### Signal Chain Format
Always present the chain in order:
`[Hardware] → [Dynamics/Pre-FX] → [Amp] → [Cab/Mics] → [Post-FX EQ/Comp] → [Spatial/Reverb]`

---

## 5. The Feedback Loop & Lifecycle

Tones evolve through three states, tracked in the `status` frontmatter:

1.  **`initial`**: Proposed by the advisor but not yet tested in a DAW session.
2.  **`tested`**: Verified in a session. Levels are confirmed, and the character matches the target.
3.  **`refined`**: Adjusted after actual practice/playing. The "sweet spots" have been found.

**Feedback History Rules**:
- Never delete old feedback.
- Append new entries with the date and status change.
- Note specific monitoring (e.g., "Tested on HD660S2", "Verified on THR10ii").

---

## 6. Comparison Protocol
When creating a tone to compare against an existing one (e.g., "Showtime vs Dream '65"):
- **Isolate the Variable**: Keep the Tone King, Guitar, and Post-FX identical.
- **Document the Difference**: Explicitly state what the new amp/plugin adds or takes away compared to the baseline.
