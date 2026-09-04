---
id: "puretone-velvet-jazz-sheraton"
preset_name: "Puretone Velvet Jazz Sheraton"
created: "2026-06-02"
updated: "2026-06-02"
guitar: "Epiphone Sheraton II (neck humbucker, flatwounds)"
target: 'Warm, ultra-clear hi-fi jazz clean using the Hughes & Kettner Puretone platform — smooth note definition, organic woody resonance, and flatwound warmth with pristine note separation.'
tags: "boutique, clean, warm, humbucker, flatwounds, puretone, jazz, bossa"
tone-king-channel: bypassed
amp: "H&K Puretone (Nembrini)"
status: initial
pickup_type: humbucker
preset_data:
  nembrini_puretone:
    Volume: 3.5
    Growl: 0.0
    Bass: 4.5
    Mid: 5.5
    Treble: 4.0
    Tone: 5.0
    OutLevel: -4.0
  la2a:
    peak_reduction: 25
    gain: 15
---

# Puretone Velvet Jazz — Sheraton II

## Target Sound

This toneprint is designed specifically for Mike's **Epiphone Sheraton II** semi-hollow body guitar, strung with **Thomastik-Infeld Jazz Swing Flatwound 10s**. 

The goal is an upscale, high-fidelity jazz clean that excels at:
- **Complex Chord Voicings & Shell Voicings**: Standard 4-note voicings, drop-2, and drop-3 chord changes. The high headroom ensures that even dense voice-leading choices remain perfectly clear, with zero intermodulation mush.
- **Acoustic Bloom & Resonance**: Leveraging the semi-hollow construction of the Sheraton to deliver an organic "acoustic guitar in a warm room" character.
- **Classic Jazz and Bossa Nova**: High-end flatwound response modeled after smooth, smoky hollow-body tones but with contemporary hi-fi clarity.

Because the Sheraton with flatwounds is inherently thick and warm, running it into a standard Fender-style amp can sometimes result in muddy lower mids. The **Nembrini Hughes & Kettner Puretone** is a pristine, ultra-linear handwired tube emulation. By keeping the **Growl** knob at **0.0**, the tone stack remains fully active, providing a beautifully voiced, highly polished studio canvas that highlights the woody, rich tone of the semi-hollow body without getting dark or muddy.

---

## Signal Chain

### 1. Tone King Imperial Preamp — physical front-end
*   **Status:** **Bypassed**
*   **Signal Path:** Guitar direct into Audient iD14 Instrument Input 1 (Preamp gain set to **0** for clean, uncolored headroom; Guitar bus set to **Mono** in Logic Pro).

---

### 2. Nembrini H&K Puretone
The primary boutique amp platform. The Growl knob is kept at zero to ensure maximum EQ filter precision and pristine headroom.

| Control | Setting | Purpose |
|---------|---------|---------|
| Volume | 3.5 | Preamp gain set to clean headroom sweet spot; highly touch-sensitive |
| Growl | 0.0 | Keeps the tone stack fully active for maximum EQ polish and refinement |
| Bass | 4.5 | Rolled back slightly to prevent the flatwound low-end from overwhelming the mix |
| Middle | 5.5 | Boosted slightly to provide warm, vocal midrange thickness and presence |
| Treble | 4.0 | Gently rolled back to smooth out any ice-pick highs, letting the TI flats sing |
| Tone | 5.0 | Neutral power-amp contour |
| OutLevel | −4.0 | **Critical**: Post-amp level trim to prevent digital clipping inside Logic |

**Cabinet & Microphone Selection**:
*   **Cabinet**: Divided 11's **1x12 Alnico Gold** (or HK 4x12)
*   **Microphone**: **Ribbon 121** off-axis (provides natural high-frequency roll-off and warm, full body)

---

### 3. UADx LA-2A Silver Compressor
Applied as an insert to provide optical leveling, smoothing the wide transients of flatwounds and gluing the chord changes together.

| Control | Setting | Purpose |
|---------|---------|---------|
| Mode | Compress | Standard 3:1 opto-compression |
| Peak Reduction | 25 | Targets ~1–2 dB of gain reduction on firm strums; provides gentle dynamic glue |
| Gain | 15 | Makeup gain adjusted for natural session level |

---

### 4. UADx Capitol Chambers
Reverb applied via parallel Send on Bus 3 to create an organic, luxurious spatial environment.

| Control | Setting | Purpose |
|---------|---------|---------|
| Chamber | Chamber 4 | Warm, dark wood room with massive acoustic decay bloom |
| Mix | Wet Solo (100%) | Parallel routing |
| Decay | 2.0s | Provides a luxurious, lingering tail suitable for slow jazz tempos |
| Pre-Delay | 20 ms | Separates the dry note attack from the acoustic room reflection |

**Logic Fader Blends**:
*   **Reverb Bus Send**: −12 dB
*   **Reverb Bus Fader**: −8 dB

---

## Starting Point Guide

- **Guitar Controls**: Select the **Neck Pickup** on your Sheraton. Start with your guitar volume at **8** and the tone knob at **7**. This rolls off just enough of the high-end transients to achieve that smokey, classic jazz club character while keeping the high-fidelity clarity of the Puretone platform.
- **Dynamic Control**: Because the Puretone has very fast transients, your physical picking velocity will directly influence the note projection. Soft thumb-plucks will yield a delicate, velvety acoustic-like texture, while solid pick strikes will project crisp chord melodies.
- **DAW Clip Management**: If you notice the red clip indicators on the Master Out, do not touch the amp's Volume knob (which alters the preamp coloration). Instead, lower the **OutLevel** slider in the Nembrini cab section by an additional 1–2 dB.

---

## Feedback History

### 2026-06-02 — initial
Toneprint created to capture the high-fidelity velvet jazz clean for Mike's Epiphone Sheraton II flatwound setup. Configured with a fully active EQ stack (Growl 0.0) and optical LA-2A Silver glue.
### 2026-06-06 — bypassed Tone King Preamp (direct-in default)
Bypassed the Tone King Imperial Preamp by default in frontmatter and signal chain to align with updated toneprint guidelines. The direct Audient iD14 JFET input is now the primary signal path.
