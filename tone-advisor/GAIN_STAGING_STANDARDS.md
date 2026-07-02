# GuitarSkills — Gain Staging & Calibration Standards

This reference guide establishes the target levels and configuration standards for using your guitar plugins with the **Audient iD14** audio interface. 

---

## 1. The Physical Baseline (Audient iD14 Setup)

Your approach of plugging your guitar directly into the front **FET Instrument Input (D.I.)** with the **physical gain knob set to its absolute minimum (0)** is **100% correct and is the industry best practice**.

### Why This is Correct:
*   **Maximum Headroom**: Setting the physical preamp gain to minimum gives you the maximum possible analog headroom before the interface clips (**+9.0 dBu**).
*   **Lowest Noise Floor**: Pushing the analog preamp gain amplifies the thermal noise of the interface's circuitry. Keeping it at zero ensures the cleanest, highest signal-to-noise ratio.
*   **Impedance Matching**: The iD14's discrete JFET D.I. input presents a high impedance (>500kΩ) to your guitar pickups, preserving your high-end chime and dynamics.

### The Digital Consequence (The Mismatch):
Most major plugin developers (Neural DSP, Universal Audio) calibrate their virtual amp models assuming an interface clipping point of **+12.2 dBu** (matching a UAD Apollo Twin's Hi-Z input at minimum gain). 
Because your iD14's clipping point is **+9.0 dBu**, the digital signal entering Logic Pro is **3.2 dB louder (hotter)** than the plugins expect. Your guitar will hit virtual preamps too hard, causing clean amps to distort too early.

## 2. Universal Calibration: The Bus-Based Distribution Method (Recommended)

In your template routing, your physical guitar track ("Guitar") acts as a distribution splitter:
*   **Input**: Physical input `In 1`
*   **Output**: Mapped to **Bus 1** (instead of Stereo Out)
*   **Aux Tracks**: "Electric Dry" and "Acoustic Voice" take **Bus 1** as their inputs, where the amp and processing plugins live.

### The Fader Calibration Trick:
Because 100% of the "Guitar" track's signal is routed directly to Bus 1, the **Guitar track fader** acts as a global master input level control before the signal splits.

To calibrate the entire rig:
1.  Leave the "Guitar" track's Audio FX slots completely empty (no gain or EQ plugins needed).
2.  Set the **Guitar track fader to -3.2 dB**.
3.  This applies exactly 3.2 dB of attenuation to the Bus 1 stream. 

As a result, both the "Electric Dry" and "Acoustic Voice" aux tracks automatically receive a calibrated, +12.2 dBu-normalized signal. You do not need to adjust the input controls inside individual plugins.

*Note: If you record on the "Guitar" track, the raw D.I. audio file is captured pre-fader (standard behavior). During monitoring and playback, the signal passes through the fader to Bus 1, ensuring the plugins always receive the calibrated level.*

---

## 3. Per-Plugin Gain Staging Standards

Below are the default input calibration offsets and output level standards for each major manufacturer in your setup, assuming you are direct-injecting (D.I.) into the iD14 at minimum gain.

```
[Guitar] -> [iD14 D.I. (Min Gain)] -> [Guitar Fader (-3.2 dB)] -> [Bus 1] -> [Amp Plugin] -> [Output Level Staging]
```
## 3. Per-Plugin Gain Staging Standards

With the **Guitar** track fader set to **-3.2 dB**, your plugins are already receiving the calibrated reference signal. Therefore, you do not need to apply any input offsets inside the plugins themselves.

Below are the default settings and output staging guidelines for each manufacturer, assuming the D.I. fader calibration is active:

```
[Guitar] -> [iD14 D.I. (Min Gain)] -> [Guitar Fader (-3.2 dB)] -> [Bus 1] -> [Amp Plugin] -> [Output Level Staging]
```

### A. Neural DSP (Archetype: Cory Wong X)
*   **Input Calibration**: Keep the plugin's header **Input** knob at **0.0 dB (Default)**.
*   **Output Staging**: 
    *   Set the active amp's **Output Level** knob (on the far right of the amp panel) so that your hardest strums peak between **-12 dBFS and -10 dBFS** on your Logic track meter.
    *   Avoid using the plugin header's master output slider.

### B. Universal Audio (UADx Standalones: Dream '65, Lion '68, Ruby '63, Woodrow '55)
*   **Input Calibration**: Keep the plugin's **IN** knob/slider at its default **Hi-Z (center / 0.0 dB)** position.
*   **Output Staging**:
    *   **The "Quiet" Marshall (Lion '68)**: Plexi amps have huge clean headroom. If a preset sounds quiet, do *not* increase the interface gain or the amp's internal Volume knobs (which would add grit). Instead, turn up the plugin's dedicated **Output** knob (on the far right of the plugin GUI). This is a clean digital master volume and will not affect the tone.
    *   Set the **Output** knob so that the track peaks between **-12 dBFS and -10 dBFS**.

### C. UAD Paradise Guitar Studio (Wrapper)
*   **Input Calibration**: Keep all settings clean; no adjustment needed inside the plugin since Bus 1 is already calibrated.
*   **Output Staging**:
    *   Adjust the global **Output** slider (found in the status bar of the wrapper) to level-match the active preset with your bypassed signal.

### D. IK Multimedia (TONEX)
*   **Input Calibration**: Keep the Global/Preset **Input Trim** at **0.0 dB** as your calibrated baseline.
*   **Pickup Calibration (Trim Offsets)**:
    *   *Vintage Single-Coils*: Add **+2.0 to +5.0 dB** of Input Trim inside TONEX to drive the capture into its sweet spot (since single-coils naturally output less voltage than the humbuckers used for calibration).
    *   *Humbuckers*: Keep the Input Trim at **0.0 dB** (or up to **+2.0 dB** for low-output vintage humbuckers).

### E. Nembrini Audio (JC120, MRH810, Divided 11)
*   **Input Calibration**: Keep the plugin's input level slider at **0.0 dB**.
*   **Output Staging**:
    *   Nembrini plugins tend to run very hot. Always turn down the plugin's **Output** or **Master** control to prevent clipping, aiming for track peaks not exceeding **-10 dBFS**.

### F. MixWave (Two-Rock Bloomfield Drive)
The Two-Rock Bloomfield Drive is modeled as a high-headroom, highly dynamic boutique amplifier. However, it can run *exceptionally* hot and easily clip your DAW output if the gain stages aren't managed correctly.
*   **Input Calibration**: Keep the plugin's global **Input Level** slider (in the top utility bar) at **0.0 dB (unity)**, since your Bus 1 fader is already handling the -3.2 dB calibration.
*   **EQ1 / EQ2 Switch Warning**: Toggling between EQ1 and EQ2 shifts the amp's internal gain structure. You will need to readjust your Gain/Master settings to maintain your clean headroom and volume balance when toggling this switch.
*   **Output Staging**: 
    *   *The Master Volume Rule*: The amp's **Master** knob controls the power-tube emulation (adding power section color and sag). Turning down the Master knob will thin out your tone. 
    *   *The Headroom Solution*: To reduce the plugin's output level without losing your power amp tone, **do not turn down the Master knob**. Instead, open the **Cabinet section** and pull down the **individual Mic Faders** to around **-6.0 dB or -8.0 dB**. You can also use the global **Output Level** slider in the top utility bar to trim the final signal before it hits the DAW.

---

## 4. Dynamics & Effects Staging (Post-Amp / Bus)

### UAD 1176 & Teletronix LA-2A (Silver/Gray)
These compressors react dynamically to the level they receive. If your input signal is too hot, they will compress constantly and squash your transients, raising the noise floor.
*   **Gain Staging**:
    *   Ensure the signal entering the compressor peaks around **-18 dBFS** (a typical clean D.I. or post-amp level).
    *   Adjust **Peak Reduction** (LA-2A) or **Input** (1176) so that the gain reduction meter only pulls back by **1 to 3 dB** on normal playing, and up to **5 to 6 dB** on hard strums (for squashed funk/rhythm tones).
    *   Use the **Gain** (LA-2A) or **Output** (1176) knob to match the compressed volume to the bypassed volume (unity gain).

### Spatial Effects (Capitol Chambers, Hitsville Reverb, Space Designer)
*   **The Bus Standard**: Always run these plugins on a **Bus/Aux Send** rather than as inline inserts.
*   **Plugin Setup**: Set the plugin's internal Mix to **100% Wet** (or turn **Wet Solo ON**).
*   **Level Control**: Control the blend exclusively via the **Logic Send knob** (usually starting between **-18 dB and -12 dB**). This keeps your dry signal punchy and center-focused while avoiding complex gain-matching inside the reverb plugin itself.
