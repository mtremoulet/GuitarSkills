# Delay Designer — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 3387–4132

Add via: Delay > Delay Designer in a channel strip Audio Effect plug-in menu.

---

## Overview

Delay Designer is a multitap delay with up to 26 individual taps (delays), all fed from the source signal. Each tap can be independently edited for level, pan position, pitch transposition, and lowpass/highpass filtering. Can also function as an audio pattern sequencer. Maximum delay time: 10 seconds.

---

## Interface Sections

1. **Main display**: Visual representation of all taps; view and edit tap parameters
2. **Tap parameter bar**: Numeric overview of current settings for the selected tap
3. **Tap pads**: Create taps using mouse/trackpad or MIDI controller
4. **Sync section**: Synchronization and quantization settings
5. **Master section**: Global Mix and Feedback parameters

---

## Main Display Controls

- **View buttons**: Select the parameter shown in the Tap display:
  - **Cutoff**: Highpass and lowpass filter cutoff frequencies
  - **Reso(nance)**: Filter resonance value
  - **Transp(ose)**: Pitch transposition per tap
  - **Pan**: Pan position (mono→stereo) or stereo balance (stereo→stereo)
  - **Level**: Relative volume of each tap (Tip: Option-Command temporarily switches to Level view from any view)
- **Autozoom button**: Zoom Tap display to show all taps visible. Turn off to manually zoom.
- **Overview display**: Shows all taps in the full time range. Drag highlighted section to zoom/navigate.
- **Toggle bar**: Turn parameters on/off per tap. The parameter being toggled matches the active view button:
  - Cutoff view: filter on/off
  - Reso view: filter slope (6 dB / 12 dB)
  - Pitch view: pitch transposition on/off
  - Pan view: Flip mode switching
  - Level view: mute/unmute tap
- **Tap display**: Each tap shown as a shaded line with a bright bar indicating the parameter value. Directly editable.
- **Identification bar**: Shows letter label for each tap; serves as timeline. Drag tap letters to move in time.

---

## Tap Parameter Bar Controls

Provides access to all parameters of the selected tap. Also shows parameters not available in the Tap display (Transpose, Flip).

- **Filter On/Off button**: Turn highpass/lowpass filters on or off for selected tap
- **Cutoff HP/LP fields**: Cutoff frequencies (Hz) for highpass and lowpass filters
- **Slope buttons**: Filter slope steepness — 6 dB (gentler) or 12 dB (more pronounced). Note: HP and LP filters cannot be set to different slopes.
- **Reso(nance) field**: Filter resonance for both filters
- **Tap Delay fields**: Tap number/name (upper) and delay time (lower)
- **Pitch On/Off button**: Turn pitch transposition on or off for selected tap
- **Transp(ose) fields**: Left field = semitones (drag to transpose). Right field = fine-tune in cents (1/100 semitone).
- **Flip buttons**: Swap left and right side of stereo/surround image for the tap. Reverses left/right position.
- **Pan field**: Pan position (mono) or stereo balance (stereo) or surround angle. Values: 100% = full left, −100% = full right, 0% = center.
- **Spread field**: Width of stereo spread for selected tap (stereo-to-stereo or stereo-to-surround instances)
- **Mute button**: Mute/unmute selected tap
- **Level field**: Output level for selected tap

---

## Creating Taps

### Via Tap Pads
1. Click **Start** pad (erases all existing taps — use Identification bar for subsequent taps)
2. Pad label changes to **Tap**; red recording bar appears
3. Click **Tap** button to create each tap at the exact moment of each click
4. Click **Last Tap** button to finish. Last tap is designated as the feedback tap.
- Note: If Last Tap is not clicked, recording stops after 10 seconds or 26 taps, whichever comes first.

### Via Identification Bar
- Click a position in the Identification bar to create a tap at that point
- Option-drag one or more taps to copy them to a new position

---

## Editing Taps

- **Select a tap**: Click it in the Tap display, click its letter in the Identification bar, or use the arrows/pop-up menu in the Tap parameter bar
- **Select multiple taps**: Drag across the Tap display background, or Shift-click individual taps
- **Move a tap**: Drag its letter in the Identification bar (left = forward in time, right = backward in time)
- **Delete a tap**: Select it, press Delete; or drag the letter downward out of the Tap display
- **Delete all selected taps**: Control-click a tap → "Delete tap(s)"
- **Edit a parameter value**: In the Tap display, drag the bright line of the tap vertically
- **Command-drag**: Draws value curves across multiple taps simultaneously
- **Option-click**: Reset a parameter to its default value

### Filter Cutoff Editing in Tap Display
In Cutoff view: upper line = lowpass cutoff, lower line = highpass cutoff. Drag in the area between them to adjust both simultaneously.
- When HP cutoff < LP cutoff: acts as bandpass filter (serial operation)
- When HP cutoff > LP cutoff: acts as band-rejection filter (parallel operation)

---

## Tap Shortcut Menu Commands (Control-click a tap)
- **Copy sound parameters**: Copies all parameters except delay time to Clipboard
- **Paste sound parameters**: Pastes from Clipboard into selected tap(s)
- **Reset sound parameters to default values**: Resets all selected tap parameters (except delay time)
- **2× delay time**: Doubles delay time of all selected taps (half-time effect)
- **½× delay time**: Halves delay time of all selected taps (double-time effect)
- **Delete tap(s)**: Deletes all selected taps

---

## Sync Parameters

- **Sync button**: Turn synchronized mode on or off. When on, taps snap to a grid of musically relevant positions.
- **Grid pop-up menu**: Choose grid resolution (musical note durations). Sets step size for all taps. Example: at 120 bpm with 1/16 grid, each increment = 125 ms.
- **Swing field**: Varies timing of every second grid increment:
  - 50% = every increment has the same value
  - Below 50% = every second increment is shorter in time
  - Above 50% = every second increment is longer in time
  - Subtle values (45–55%) create a less rigid, more relaxed feel

---

## Master Parameters

- **Feedback button**: Turn the feedback tap on or off
- **Feedback Tap pop-up menu**: Choose which tap is the feedback tap
- **Feedback Level knob and field**: Output level of feedback tap before routing back to input. 0% = no feedback; 100% = full volume feedback. Note: Feedback turns off automatically when creating taps with the Tap pads; turns back on when done.
- **Mix sliders**: Independently set levels of dry input signal and wet (post-processing) signal

---

## Notes for Guitar Use

- For simple delay use, create a single tap at the desired timing — functions like a traditional delay pedal
- **Pitch transposition per tap** enables cascading harmonized delays — set Tap B a 5th above the source, Tap C an octave, etc.
- **Filter per tap** allows high-frequency rolloff on repeats — simulates analog delay degradation
- **Swing** set to ~55% gives a subtle shuffle feel to rhythmic delay patterns
