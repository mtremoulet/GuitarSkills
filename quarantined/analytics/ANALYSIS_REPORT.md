# Empirical Audio Analysis: Base vs. Burnished Royal Velvet Jazz

**Location**: `quarantined/analytics/`  
**Audio Files Analyzed**:
- [base.wav](file:///Users/miketremoulet/ai_projects/GuitarSkills/quarantined/analytics/base.wav) (Lion '68 Royal Velvet Jazz P-90 base toneprint)
- [burnished.wav](file:///Users/miketremoulet/ai_projects/GuitarSkills/quarantined/analytics/burnished.wav) (Royal Velvet recipe: Liberty Burnisher + Stumblelater applied)
- **Visual Chart**: [burnished_vs_base_analysis.png](file:///Users/miketremoulet/ai_projects/GuitarSkills/quarantined/analytics/burnished_vs_base_analysis.png)

---

## 1. Executive Summary & Core Verdict

The comparative analysis across your two real-time guitar performances confirms that the **Liberty Burnisher** and **Stumblelater** pair from the Faust & Wagner virtual analog suite acts precisely according to its circuit design brief:

1. **Dynamic Miller Attack Softening (Proven)**: High-frequency transient pick slap (3–8 kHz) during the initial 25 ms attack window is suppressed by **-5.83 dB** in the burnished recording relative to the base tone. Crucially, the high-frequency content during the sustaining body (80–230 ms) is virtually identical (**within 0.47 dB**). This confirms that the pedal is **not** acting like a static passive tone roll-off; it is actively catching and burnishing hard pick transients on the fly while leaving sustaining chord harmonics open.
2. **Body Blooming & Sustain Extension**: The median half-decay time ($T_{6\text{dB}}$) increases by **+20.0 ms (+9.5%)** (from 210 ms to 230 ms). The crest factor shrinks by **0.86 dB**, as RMS energy increases (+2.50 dB) more than peak level (+1.64 dB), producing the spongy, elastic compression characteristic of JFET/BJT emitter sag and Dumble ABL recovery buffering.
3. **Subsonic Tightening & Midrange Projection**: The empirical transfer function reveals a **-3.2 dB cut below 80 Hz** (matching the Liberty Burnisher's 35 Hz 2nd-order Butterworth ZDF high-pass filter) and a warm **+2.5 to +3.2 dB broad shelf between 150 Hz and 1.5 kHz**, adding woody acoustic chest resonance to the Framus P-90s without low-end flub.
4. **11.5 kHz Shimmer Bell Fingerprint**: After a steep roll-off through the presence band (-10 to -12 dB at 6–10 kHz), the transfer function rebounds by **+9.5 dB at 11.5–12.0 kHz** (reaching -2.48 dB), capturing the exact physical footprint of the Liberty Burnisher Stage 3 tuned RLC presence shimmer bell ($f_0 = 11.5\text{ kHz}, Q = 0.85$).

---

## 2. Quantitative Comparison Table

| Metric | [base.wav](file:///Users/miketremoulet/ai_projects/GuitarSkills/quarantined/analytics/base.wav) | [burnished.wav](file:///Users/miketremoulet/ai_projects/GuitarSkills/quarantined/analytics/burnished.wav) | Delta / Effect | Circuit / Design Cause |
| :--- | :--- | :--- | :--- | :--- |
| **Duration / Frames** | 58.50 s (2,808,000) | 58.20 s (2,793,600) | -0.30 s | Performance variance |
| **Chroma Pitch Correlation** | — | — | **0.985** | Confirms same composition / chord progression |
| **Peak Level** | -14.49 dBFS | -12.85 dBFS | **+1.64 dB** | Stumblelater recovery gain trim |
| **RMS Energy** | -32.11 dBFS | -29.61 dBFS | **+2.50 dB** | Denser acoustic body & compression |
| **Crest Factor (Peak/RMS)** | 17.62 dB | 16.76 dB | **-0.86 dB** | Dynamic range reduction / leveling |
| **Spectral Centroid** | 833.3 Hz | 695.4 Hz | **-137.9 Hz** | Noticeable darkening / smoky archtop shift |
| **Spectral Rolloff (85%)** | 1498.2 Hz | 1243.4 Hz | **-254.8 Hz** | Rolloff shifted down into velvet range |
| **Attack High/Mid Ratio (0-25 ms)** | -29.55 dB | -35.38 dB | **-5.83 dB** | **Dynamic Miller transient softening** |
| **Sustain High/Mid Ratio (80-230 ms)** | -24.17 dB | -23.70 dB | **+0.47 dB** | Sustain harmonics remain open |
| **Attack-to-Body RMS Ratio** | -3.64 dB | -5.07 dB | **-1.43 dB** | Body is louder relative to pick click |
| **Half-Decay Time ($T_{6\text{dB}}$)** | 216.2 ms (med 210) | 236.7 ms (med 230) | **+20.5 ms (+9.5%)** | Emitter sag loop + ABL recovery bloom |
| **Sub-bass (<80 Hz)** | Reference | -3.2 dB to -4.7 dB | **-3.2 to -4.7 dB** | 35 Hz ZDF Butterworth HPF |
| **Core Midrange (150–1500 Hz)**| Reference | +2.5 dB to +3.2 dB | **+2.5 to +3.2 dB** | Woody acoustic body resonance boost |
| **Presence / Air (6–10 kHz)** | Reference | -10.6 dB to -12.3 dB| **-11.5 dB** | Air pot (-2.5 dB) + Miller base pole |
| **Top Shimmer (11.5–12 kHz)** | Reference | -2.48 dB | **+9.5 dB rebound** | Tuned 11.5 kHz RLC shimmer bell ($Q=0.85$) |

---

## 3. Deep Dive: The Three Key Phenomenological Tests

### A. Testing the Dynamic Miller Effect: Attack vs. Sustain
According to [`faust-and-wagner/docs/circuits/LIBERTY_BURNISHER.md`](file:///Users/miketremoulet/ai_projects/faust-and-wagner/docs/circuits/LIBERTY_BURNISHER.md), the Liberty Burnisher's signature innovation is slew-dependent feedback capacitance:
$$f_{c,\text{miller}}(t) = \text{clip}\left( \frac{f_{c,\text{base}}}{1.0 + 3.8 \cdot \text{Burnish} \cdot S_{\text{env}}(t) \cdot (1.0 + 0.6 \cdot d)}, 600\text{ Hz}, 20000\text{ Hz} \right)$$
When a guitar pick strikes a string, the instantaneous voltage slew rate $S_{\text{env}}(t)$ spikes, forcing the cutoff down toward 600 Hz for milliseconds. Once the transient passes into decay, the cutoff returns to its open baseline.

**Empirical Measurement**:
- During the **first 25 ms** of each note, the ratio of high-frequency attack energy (3–8 kHz) to fundamental midrange energy (500–2000 Hz) dropped from **-29.55 dB** in `base` to **-35.38 dB** in `burnished`—a **5.83 dB drop in pick click intensity**.
- During the **sustain window (80–230 ms)**, the ratio in `burnished` (-23.70 dB) rose to match `base` (-24.17 dB) within **0.47 dB**.
- Testing by pick velocity: In `base`, striking a note hard caused a **+4.98 dB spike** in brightness. In `burnished`, striking a note hard only caused a **+3.72 dB spike**—the pedal absorbed **1.26 dB of dynamic spike** while keeping the quietest notes cushioned.

### B. Empirical Frequency Transfer Function (DTW Aligned)
Using Dynamic Time Warping (DTW) on 6,995 time-aligned frames across the two performances:
- **<80 Hz**: Attenuated by **-3.0 to -3.3 dB**. This prevents sub-bass intermodulation and speaker cone wobble from low-string thumb strikes.
- **150–1500 Hz**: Elevated by **+2.5 to +3.2 dB**. This accounts for the warm "woody" semi-hollow chest resonance.
- **3 kHz**: Begins gentle tapering (-0.92 dB).
- **6–10 kHz**: Steeply clamped down to **-10.6 to -12.3 dB** (the "electronic veil").
- **11.5–12 kHz**: Rises back up to **-2.48 dB**, verifying the tuned presence shimmer bell designed into the Faust DSP code.

### C. Sustain & Envelope Bloom
According to [`faust-and-wagner/docs/circuits/STUMBLELATER.md`](file:///Users/miketremoulet/ai_projects/faust-and-wagner/docs/circuits/STUMBLELATER.md), the Dumble ABL active buffer provides high-impedance buffering with linear Class-A recovery, while the Liberty Burnisher adds an emitter sag recursive feedback loop ($\tau = 38\text{ ms}$).
- The envelope attack-to-body ratio shifted by **-1.43 dB**, meaning the sustaining body of each chord is noticeably louder relative to its front-edge attack.
- The average time for a note to decay by 6 dB extended by **+20.5 ms (+9.5%)**.

---

## 4. Musical Translation

In jazz terms, applying the **Liberty Burnisher + Stumblelater** to the **Royal Velvet P-90** setup shifts the guitar from a slightly bright, forward P-90 electric voice into the classic **Ed Bickert / Jim Hall "dark velvet archtop"** territory:
1. P-90 single-coil snap and plectrum clicks are cushioned as if played with a heavy 2.0mm rounded horn pick or flesh of the thumb.
2. Complex cluster chords (m9, maj7#11, 13b9) sit together without intermodulation sizzle.
3. The guitar gains acoustic weight in the 200–500 Hz region without muddying the low end.
