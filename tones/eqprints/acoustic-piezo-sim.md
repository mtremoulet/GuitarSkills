---
id: acoustic-piezo-sim
title: "Acoustic Piezo Simulator"
pedal: "Toneshaper 3000"
pickup_type: single-coil
guitar: "Fender Player II Telecaster (middle/neck blend) / Stratocaster"
target: "Transforms an electric guitar's clean signal into a sparkling, scooped acoustic piezo-like texture."
tags: "acoustic, clean, scoop, sparkle, universal"
pedal_placement: "pre-amp"
bands:
  31.25: -12.0
  62.5: -6.0
  125: 2.0
  250: -2.0
  500: -8.0
  1000: -4.0
  2000: 2.0
  4000: 4.0
  8000: 6.0
  16000: 8.0
bands_7:
  100: 1.0
  200: -2.0
  400: -6.0
  800: -4.0
  1600: 1.0
  3200: 3.5
  6400: 6.5
level: -2.0
---

# Acoustic Piezo Simulator

Electric guitars and acoustic guitars occupy very different sonic spaces. Acoustic guitars have massive cabinet resonance in the low-end, a deep scoop in the middle frequencies, and a very wide, sparkling high-frequency range that extends up to 16kHz. Electric guitar pickups and speakers, on the other hand, concentrate their energy in the midrange and roll off sharply above 5kHz.

This EQprint simulates an acoustic piezo transducer by scooping the core electric midrange and heavily boosting the treble and "air" bands. Best used with clean, high-headroom amp platforms (like the Showtime '64) and a parallel blend.

## Why this curve works (Band-by-Band)

- **31.25 Hz & 62.5 Hz (Cut to -12dB and -6dB)**: Removes unwanted electric cabinet rumble.
- **125 Hz (Boost to +2dB)**: Adds a touch of low-end body to simulate the acoustic guitar's wooden soundboard resonance.
- **250 Hz (Cut to -2dB)**: Prevents the low-end body from sounding boxy or boomy.
- **500 Hz & 1 kHz (Cut to -8dB and -4dB)**: A deep, dramatic scoop. Electric guitars live in the mids, whereas acoustic guitars have a natural mid-dip. Scooping these bands removes the "electric horn" voice.
- **2 kHz & 4 kHz (Boost to +2dB and +4dB)**: Accentuates the pick strike and string definition, mimicking the immediate snap of a piezo saddle transducer.
- **8 kHz & 16 kHz (Boost to +6dB and +8dB)**: The air engine. These bands are normally rolled off in electric setups. Boosting them brings out the ultra-high shimmer and acoustic brilliance.
- **Level (Cut to -2dB)**: Compensates for the high-frequency boost to prevent input clipping.
