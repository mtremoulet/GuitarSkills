# Rotor Cabinet — Logic Pro

Source: logic-pro-mac-effects-user-guide.txt, lines 14941–15219

Add via: Modulation > Rotor Cabinet in a channel strip Audio Effect plug-in menu.

---

## Overview

Emulates the rotating loudspeaker cabinet of a Hammond organ (Leslie effect). Simulates both the rotating speaker cabinet (with and without deflectors) and the microphones that pick up the sound. Full control over motor speeds and microphone types.

---

## Basic Parameters

- **Rotation switch**: Change rotor speed between **Slow**, **Brake**, or **Fast**
- **Cabinet Type pop-up menu**: Choose cabinet model:
  - **Wood**: Mimics a Leslie with wooden enclosure (Leslie 122 or 147)
  - **Proline**: More open enclosure (Leslie 760)
  - **Single**: Full-range single rotor (Leslie 825)
  - **Split**: Bass rotor signal slightly left, treble rotor signal toward right
  - **Wood & Horn IR**: Impulse response of Leslie with wooden enclosure
  - **Proline & Horn IR**: Impulse response of Leslie with more open enclosure
  - **Split & Horn IR**: Impulse response of split routing Leslie
- **Deflector switch**: Emulate Leslie cabinet with horn deflectors removed or attached. Removing deflector increases amplitude modulation, decreases frequency modulation.

---

## Motor Control Parameters

- **Acceleration knob**: Time to get rotors up to speed (set by Max Rate) and time to slow down.
  - Far left: switches to preset speed immediately
  - Rotating right: takes more time to hear speed changes
  - Default center position: Leslie-like behavior
- **Max Rate knob**: Maximum possible rotor speed
- **Motor Control pop-up menu**: Choose different speeds for bass and treble rotors:
  - **Normal**: Both rotors use the speed from the Rotation switch
  - **Inv (inverse)**: In fast mode, bass rotates fast while horn rotates slowly. Reversed in slow mode. Both stop in brake mode.
  - **910**: ("Memphis") — stops bass drum rotation at slow speed, while horn compartment speed can be switched. Good for solid bass + treble movement.
  - **Sync**: Acceleration and deceleration of horn and bass drums are roughly the same (locked feel; audible mainly during acceleration/deceleration)
  - Note: Motor Control not relevant for Single Cabinet (no separate bass/treble rotors)

---

## Microphone Types (when Real Cabinet is selected)

- **Upper/Lower Microphones pop-up menus**: Choose microphone for horn and drum speakers:
  - **Dynamic**: Brighter and more cutting than Condenser
  - **Condenser**: Fine, transparent, well-balanced
  - **Mid-Side Mic**: MS configuration — cardioid faces cabinet, bidirectional at 90°; cardioid captures middle signal, bidirectional captures side signal

---

## Mic Processing Parameters

- **Mic Position switch**: Front or rear position for virtual microphone
- When Real Cabinet is selected:
  - **Horn knob**: Stereo width of Horn deflector microphone
  - **Drum knob**: Stereo width of Drum deflector microphone
- When other cabinets are selected:
  - **Distance knob and field**: Distance of virtual microphones from speaker cabinet. Turning right = darker and less defined sound.
  - **Angle knob and field**: Stereo image — simulated microphone angle between 0 and 180 degrees
- **Balance knob and field**: Balance between horn and drum microphone signals

---

## Notes for Guitar Use

- Rotor Cabinet is primarily an organ effect but can be used on guitar for a rotating speaker simulation
- **Acceleration** at its default center position produces the most realistic Leslie-like speed transitions
- **Slow → Fast transitions** are the signature Leslie sound — use the Rotation switch to automate
- For guitar, **Proline** type tends to sound less dark/tubby than Wood
- The **910** motor mode is useful when you want treble shimmer without wobbly bass
