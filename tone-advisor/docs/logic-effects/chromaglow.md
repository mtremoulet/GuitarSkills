# ChromaGlow — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 4516–4720

**Requires Apple M1 or later.**

Add via: Distortion > ChromaGlow in a channel strip Audio Effect plug-in menu.

---

## Overview

ChromaGlow is a saturation plugin that replicates warmth and coloration of analog audio equipment. Introduces harmonic distortion to emulate the nonlinear response and subtle compression of analog gear. Enriches harmonic content, adds texture and depth. Subtle compression effect helps smooth dynamics and tame transients.

---

## Parameters

- **Model pop-up menu**: Choose the saturation model (see below)
- **Style pop-up menu**: Choose an alternative style for the selected model (see below)
- **Drive knob and field**: Amount of saturation applied to the signal
- **Bypass Below button**: Turn the Bypass Below control on or off
- **Bypass Below field**: Frequency threshold below which the effect is bypassed — frequencies below this remain unaffected
- **Level In field**: Gain applied to the plug-in input signal
- **Level Out field**: Gain applied to the plug-in output signal
- **Mix field**: Percentage of effect signal mixed with original signal
- **Display**: Shows intensity of saturation settings on signal

---

## Models and Styles

### Retro Tube
Replicates warmth and even-order harmonics of vacuum tube equipment. Smooth, pleasant distortion; adds warmth and vintage ambiance.
- **Clean**: Subtly and smoothly adds a touch of warmth with a slight muddiness
- **Colorful**: Introduces significant character while imparting a noticeable sense of muddiness

### Modern Tube
Harmonic richness, gentle compression, and pleasing distortion typical of tube-based gear. Adds warmth, character, and vintage vibe with improved fidelity.
- **Clean**: Pristine and transparent with a touch of warmth; preserves clarity while subtly enhancing with tube characteristics
- **Colorful**: Classic warmth blended with modern clarity; rich, harmonically nuanced; reminiscent of vintage amps

### Magnetic
Mimics saturation and compression of analog tape machines. Warm, organic, slightly compressed sound with added harmonics. Great for vintage, analog feel.
- **Colorful**: Transformer component ON — saturated, warm, character-rich
- **Clean**: Transformer component OFF — cleaner signal with less harmonic content

### Squeeze
Replicates saturation from intentionally pushing a compressor. Introduces harmonic distortion; imparts warmth, character, and color.
- **Soft Press**: Smooth, natural compression with gentle characteristics; enhances warmth and richness; ideal for subtle, musical compression
- **Hard Press**: Assertive, punchy compression with evident distortion; dramatic impact on percussive sounds or for pronounced vocal presence

### Analog Preamp
Assertive, vibrant, punchy sound with a sharp, edgy quality — in contrast to smoother tube or gentle tape saturation.
- **Clean**: Transistor-based saturation circuit — cleaner signal with reduced distortion
- **Colorful**: Vintage, woolly sound with soft clipping; subtly compressed and warm

---

## Low Cut Section

- **Low Cut button**: On/off
- **Slope pop-up menu**: Higher slope = more extreme filtering
- **Frequency field**: Cutoff frequency for the lowpass filter (note: this is a low cut = high pass filter)
- **Resonance field**: Emphasize frequencies around the cutoff frequency
- **Pre/Post buttons**: Apply low cut before or after the saturation effect

## High Cut Section

- **High Cut button**: On/off
- **Slope pop-up menu**: Higher slope = more extreme filtering
- **Frequency field**: Cutoff frequency
- **Resonance field**: Emphasize frequencies around the cutoff
- **Pre/Post buttons**: Apply high cut before or after the saturation effect

---

## Notes for Guitar Use

- **Retro Tube / Modern Tube**: Most musical for guitar; even-order harmonics sit naturally in a mix
- **Magnetic**: Good for adding tape-style glue after a guitar amp sim
- **Drive** is the primary saturation control — start low and increase until character appears without audible harshness
- **Mix** enables parallel saturation — useful for preserving transient attack while adding warmth in the low-mids
- **Bypass Below**: Set around 80–120 Hz to avoid muddying the low end while saturating the upper frequencies
