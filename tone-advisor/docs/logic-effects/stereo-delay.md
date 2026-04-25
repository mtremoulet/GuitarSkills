# Stereo Delay — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 4195–4300

Add via: Delay > Stereo Delay in a channel strip Audio Effect plug-in menu.

---

## Overview

Sets Delay, Feedback, and Mix parameters separately for left and right channels. Crossfeed knob routes each channel's feedback to the opposite stereo side. Can be used on mono tracks or busses — when inserted on a mono channel strip, the track switches to stereo operation from that point forward.

---

## Channel Parameters (identical for left and right)

- **Input pop-up menu**: Choose input signal for each stereo side. Options: Off, Left, Right, L+R, L−R
- **Delay Time knob and field**: Delay time in milliseconds, or in note values when tempo-synced. Notes/dots displayed around the knob.
- **Note pop-up menu**: Grid resolution for delay time when Tempo Sync is active
- **Deviation field**: Amount of deviation from the grid
- **÷2 and ×2 buttons**: Halve or double current delay time
- **Low/High Cut slider and field**: Cut frequencies below Low Cut and above High Cut from the effect signal
- **Feedback knob and field**: Amount of feedback for each delay channel
- **Feedback Phase button**: Invert the phase of the corresponding channel feedback signal
- **Crossfeed Left to Right (Right to Left) knob and field**: Transfer the feedback signal of one channel to the opposite channel. Creates ping-pong and circular delay effects.
- **Crossfeed Phase button**: Invert phase of the crossfed feedback signals

---

## Global and Output Mix Parameters

- **Routing pop-up menu**: Internal signal routing. Options: Customized, Straight, Crossfeed, 90/10, 10/90, Ping Pong L/R, Pan L/R, Rotate L/R
- **Tempo Sync button**: Synchronize delay repeats with project tempo. Set note values with Note pop-up or Delay Time knob.
- **Stereo Link button**: Link corresponding parameters for both channels — adjusting one adjusts the other. Relative values maintained. Command-drag to adjust a single channel while in Stereo Link mode. Press Command to temporarily flip stereo linking behavior.
- **Output Mix sliders and fields**: Independently control level of left and right channel signals

---

## Notes for Guitar Use

- **Stereo Link** is useful for classic quarter-note delays where both sides are identical; turn it off for ping-pong effects
- **Low/High Cut** on the effect signal (not feedback path) shapes the timbre of the delay repeats without affecting the dry signal
- **Routing: Ping Pong L/R** bounces repeats left and right — effective for wide spatial effects in headphones
