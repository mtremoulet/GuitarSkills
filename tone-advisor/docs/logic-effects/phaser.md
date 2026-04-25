# Phaser — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 14568–14662

Add via: Modulation > Phaser in a channel strip Audio Effect plug-in menu.

---

## Overview

Combines original signal with a copy slightly out of phase. Timing differences between the two signals are modulated by two independent LFOs. Includes a filter circuit and built-in envelope follower. Creates whooshing, sweeping sounds wandering through the frequency spectrum. Common guitar effect, suitable for many signal types.

---

## Parameters

- **Stages knob and field**: Phaser algorithms (even numbers) or comb filtering (odd numbers).
  - Settings 4, 6, 8, 10, 12: Five different phaser algorithms modeled on analog circuits, each for a specific application
  - Settings 5, 7, 9, 11: More subtle comb filtering effects (not actual phasing)
- **Sweep Mode pop-up menu**: Determines impact of incoming signal levels on the frequency range. Set frequency range with Ceiling and Floor controls.
- **Ceiling/Floor sliders and fields**: Frequency range affected by LFO modulations. Drag the green slider area between Ceiling and Floor to move the entire range.
- **Rate 1/2 knobs and fields**: Speed for each independent LFO
- **Sync buttons**: Synchronize modulation speed of each LFO with project tempo. Choose note values with Rate 1 and Rate 2 knobs.
- **Phase knob and field**: Phase relationship between channel modulations (stereo/surround only). At 0°: extreme modulation values achieved simultaneously for all channels. At 180° or −180°: greatest possible distance between channel modulation phases.
- **(LFO) Mix slider and fields**: Ratio between the two LFOs
- **Distribution pop-up menu**: Phase offset distribution in surround field — circular, left↔right, front↔rear, random, new random. (Surround instances only)
- **Level knob and field**: Amount of effect signal routed back to input (feedback)
- **Warmth button**: Turn on distortion circuit for warm overdrive effects
- **Low/High Cut sliders and fields**: Cutoff frequency of lowpass (LP) and highpass (HP) filters
- **Filter button**: Turn filter section on or off
- **(Out) Mix slider and field**: Balance of dry and wet signals. Negative values produce a phase-inverted mix of effect and direct signal.

---

## Notes for Guitar Use

- Stages 4 or 6 are most common for classic guitar phasing
- **Warmth** button adds a subtle overdrive character — useful for warm, vintage phaser tones
- Low Rate settings (slow sweep) produce the classic "slow gear" phaser feel
- High Feedback (Level) makes the effect more pronounced and resonant
