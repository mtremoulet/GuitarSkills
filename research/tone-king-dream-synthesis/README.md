# Tone King Imperial Preamp & Dream '65 Tone Synthesis

## Research Working Directory

This directory contains comprehensive research, circuit validation, software translation matrices, and candidate toneprint designs for bridging the **Tone King Imperial All-Tube Preamp pedal** with software amp modelers (**UADx Dream '65**, **Woodrow '55**, **Lion '68**, **Paradise Guitar Studio**, and **Neural DSP Archetype Cory Wong X**).

---

## Background & Objectives

1. **Hardware Context**:
   - Mike owns the **Tone King Imperial All-Tube Preamp pedal** (3x 12AX7 tubes running at high plate voltage, Ironman II reactive attenuation simulation, convolution spring reverb, bias-style digital tremolo, and three pre-loaded OwnHammer speaker IRs).
   - Mike has **no physical pedals** in front of the Tone King Imperial. The toneprints must exploit the pedal's onboard gain stages, channel voicings, attenuation, reverb, tremolo, cab selections, and guitar volume/tone pot dynamics.
2. **Software Modeler Context**:
   - Mike wants to embrace **Dream '65** (Fender Blackface Deluxe Reverb '65) as well as its relatives in Paradise Guitar Studio and Archetype Cory Wong X.
   - We need exact 1-to-1 mappings so any toneprint created can be played natively in software (Standalone host or Element) OR dialed into the physical pedal direct into the Audient iD14 line input.
3. **Toneprint Heritage & Preferences**:
   - Mike has loved the high-headroom woody clean jazz thump of `lion-68-royal-velvet-jazz-p90.md` (Jazz Middle Rule, High-Cut Veil at 4.5 kHz, touch-sensitive P-90 detail).
   - Mike has loved the 3-amp parallel architecture of the Mayer Trinity rig in Element (`Parallel_Mayer_Trinity_3Amp.els`: Showtime SSS clean glass + Dream '65 Blackface spring bloom + Enigmatic '82 Dumble ODS vocal mids).
   - Mike's guitar stable:
     - 2024 Fender Player II Telecaster (Single-coils)
     - 2014 Gibson Les Paul Studio (490R/490T Alnico II humbuckers)
     - Mid-1980s Squier Stratocaster Partscaster (Tex-Mex single-coils)
     - 2013 Epiphone Sheraton II (Thomastik flatwounds, neck humbucker jazz box)
     - 2008 Epiphone Les Paul Standard Plus Top (Tonerider Rebel 90 HSP-90s)
     - 2012 Framus Earl Slick Artist Series (DiMarzio P-90s, swamp ash, Bigsby)
4. **Post-Amp Effects (Computer)**:
   - Setting aside the default LA-2A Silver + Hitsville chamber combo.
   - Leveraging post-amp computer effects where helpful (UADx Galaxy Tape Echo, Studio D Chorus, Studer A800, Verve Analog Machines, Waterfall Rotary, ValhallaSuperMassive, TDR Nova EQ).

---

## Documents in this Research Package

1. **`tone-king-hardware-validation.md`**: Comprehensive circuit validation of the Tone King Imperial Preamp pedal (Rhythm AB763 Blackface channel, Lead Tweed-to-Plexi Mid-Bite circuit analysis, Ironman II attenuation behavior, spring convolution reverb, bias tremolo, OwnHammer IR details, and 9-pip dial mechanics).
2. **`software-amp-translation-matrix.md`**: Technical translation matrix between the Tone King Imperial Preamp pedal and software engines (UADx Dream '65, Woodrow '55, Lion '68, Paradise Guitar Studio, Archetype Cory Wong X).
3. **`candidate-toneprint-concepts.md`**: Detailed specifications for a minimum of 5 candidate toneprints that translate between the hardware pedal and software modelers, tailored to Mike's guitars and preferred genres.
