# Candidate Toneprint Concepts: Tone King Imperial & Dream '65 Synthesis

This document specifies **five distinct, production-grade toneprint concepts** designed to bridge the **Tone King Imperial All-Tube Preamp pedal** with software amp engines (**UADx Dream '65**, **Woodrow '55**, **Lion '68**, **Paradise Guitar Studio**, and **Neural DSP Archetype Cory Wong X**).

Each concept adheres to:
1. **The Pedal-Less Constraint**: No physical pedals in front of the Tone King Imperial; guitar Volume and Tone knobs act as the master dynamic controllers.
2. **First-Source Tone Calibration**: All hardware settings use the continuous **1 to 9 pip scale** (Pip 5.0 = 12:00 noon).
3. **Universal 6-Guitar Calibration**: Every toneprint specifies an "anchor" instrument, plus explicit calibration hints and parameter offsets for all 6 physical guitars in Mike's stable.
4. **Exclusion of Default FX**: Sets aside the default LA-2A Silver + Hitsville chamber combo in favor of targeted studio post-FX (Galaxy Tape Echo, Studio D Chorus, Studer A800, Waterfall Rotary, ValhallaSuperMassive, TDR Nova EQ).
5. **Multi-Instrument Bridges**: Pedagogical and musical connections to Mike's violin, alto sax, a cappella arranging, and Irish fiddle background.

---

## Mike's Guitar Stable Reference (D'Addario XS 10-46 Baseline)
*Authoritative source: `tone-advisor/guitar_stable.md`*

| # | Guitar | Body & Scale | Pickups | Strings | Sonic Character & Anchor Role |
|---|---|---|---|---|---|
| **1** | **2013 Epiphone Sheraton II** | Semi-hollow laminate maple | Dual Humbuckers | **Thomastik-Infeld Jazz Flats 10s** | The "Velvet Jazz Box." Warm acoustic bloom, zero string zip, flatwound dark velvet. |
| **2** | **2014 Gibson Les Paul Studio** | Solid mahogany/maple (120th Anniv.) | **490R / 490T** (Alnico II, ~8.5k DCR) | D'Addario XS (10-46) | The "Smooth Refinement." Moderate-output vintage humbuckers, warm, singing sustain. |
| **3** | **2008 Epiphone Les Paul Standard** | Solid mahogany / carved maple | **Tonerider Rebel 90s** (HSP-90s, Alnico II) | D'Addario XS (10-46) | The "Singing P-90 Workhorse." Rich low-mid weight, touch-sensitive dynamic roll-off. |
| **4** | **2012 Framus Earl Slick Artist** | Swamp ash body / Bigsby B500 | **DiMarzio P-90s** (Soapbars) | D'Addario XS (10-46) | The "Slick Rocker." Snappy attack, raw upper-mid bite, pitch expression. |
| **5** | **2024 Fender Player II Telecaster** | Solid alder / Rosewood board | Player II Single-coils | D'Addario XS (10-46) | The "Home Base." Articulate, cutting bridge, warm bell-like neck. |
| **6** | **Mid-1980s Squier Stratocaster** | MIJ SQ body / E neck | **Fender Tex-Mex** Single-coils | D'Addario XS (10-46) | The "Funky Quack." Hot vintage single-coils, punchy, aggressive transient snap. |

---

## Master Comparison & Quick-Reference Matrix

| # | Concept Name | Primary Anchor Guitar | Genre / Vibe | TK Channel & Knobs (1–9 Pips) | Cab IR | Reverb / Tremolo | Software Modeler Engine | Key Post-Amp Studio FX |
|---|---|---|---|---|---|---|---|---|
| **1** | **Midnight Velvet Archtop** | Epiphone Sheraton II (Jazz Flats) | Modern Jazz / Dark Bossa | **Rhythm**: Vol 2.8 / Att 4.5 / Treb 2.5 / Bass 5.5 | **Cab 1** (TK 1x12) | Rev: L2.5 D3.5 / Trem: Off | Dream '65 (Stock/Normal) or Paradise Super Bass | TDR Nova (4.5k High-Cut Veil), Studer A800 (15 IPS), Studio D (Btn 1) |
| **2** | **Tokyo Neon 1984** | Squier Strat MIJ (Tex-Mex SC) | City Pop / Funk Clean | **Rhythm**: Vol 3.2 / Att 5.5 / Treb 6.2 / Bass 4.8 | **Cab 2** (AC30 2x12) | Rev: L1.5 D2.0 / Trem: Off | Cory Wong X (Clean Machine / D.I. Console) | Studio D Chorus (Btn 2), Galaxy Slapback (Head 1), Verve Solid-State |
| **3** | **Smoky Tweed Roots** | Epiphone LP (Rebel 90s) | Folk / Americana Roots | **Lead**: Vol 3.5 / Att 5.0 / Tone 3.5 / Mid-Bite 1.5 | **Cab 1** (TK 1x12) | Rev: L2.5 D3.5 / Trem: Spd 3.2 Dep 2.8 | Woodrow '55 (Jumped 5E3) | Galaxy Tape Echo (Head 2), TDR Nova (75Hz HPF, 420Hz cut), Verve Tape |
| **4** | **Mayer Trinity Vocal Lead** | Framus Earl Slick (DiMarzio P-90s) | Modern Blues-Rock / Lead | **Lead**: Vol 4.5 / Att 5.5 / Tone 4.5 / Mid-Bite 4.0 | **Cab 3** (Marshall 4x12) | Rev: L2.0 D2.5 / Trem: Off | Paradise Guitar Studio (ODS + TS) | Waterfall Rotary (Slow 18%), Studer A800 (30 IPS), Airwindows Console |
| **5** | **Nordic Cathedral** | Fender Player II Tele (Single-Coils) | Ambient / Neo-Classical | **Rhythm**: Vol 2.5 / Att 5.0 / Treb 2.8 / Bass 6.8 | **Cab 1** (TK 1x12) | Rev: L3.5 D4.5 / Trem: Spd 2.2 Dep 3.5 | Dream '65 (High-Headroom Clean) | ValhallaSuperMassive (Lyra), Galaxy Echo (Head 3), TDR Nova (85Hz HPF) |

---

## Concept 1: "Midnight Velvet Archtop" (Modern Jazz / Dark Vocal Bossa Nova)

### 1. Anchor Instrument: 2013 Epiphone Sheraton II
- **Pickups & Strings**: Neck Humbucker; Thomastik-Infeld Jazz Swing Flats (10s).
- **Core Setting (Hardware)**: Rhythm Channel — Volume **2.8**, Attenuation **4.5**, Bass **5.5**, Treble **2.5**, Cab **1 (TK1660)**. Reverb: Level **2.5**, Dwell **3.5**. Tremolo: **OFF**. Guitar Vol: **7.0**, Tone: **5.0–5.5**.
- **Core Setting (Software)**: UADx Dream '65 Normal mode — Volume **2.5**, Treble **3.5**, Bass **4.8**, Reverb **2.5**, Oxford 1x12 cab (or Paradise Lion '68 Super Bass platform with Middle at 7.5).
- **Post-Amp FX**: TDR Nova (HPF 80 Hz, High-Cut Veil 4500 Hz 24 dB/oct, 650 Hz -1.5 dB cut), Studer A800 (15 IPS, Tape 250), Studio D Chorus (Button 1).

### 2. Universal 6-Guitar Calibration Guide (Midnight Velvet)

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Epiphone Sheraton II** *(Anchor)* | Neck HB, Vol 7, Tone 5.5 | Baseline: Vol 2.8, Bass 5.5, Treb 2.5 | Baseline: Vol 2.5, Treb 3.5, Bass 4.8 | Pure flatwound acoustic bloom; zero pick click; pillowy low-mids. |
| **Gibson Les Paul Studio** | Neck 490R, Vol 7, Tone 5.5 | **Bass +0.5 (6.0), Treble +0.5 (3.0)** | **Bass +0.4 (5.2), Treble +0.5 (4.0)** | Solid mahogany/maple provides faster transient attack and longer sustain. Treble 3.0 restores top air lost with roundwounds. |
| **Epiphone Les Paul (Rebel 90s)** | Neck P-90, Vol 6.5, Tone 5.0 | **Bass -1.0 (4.5), Treble 2.5** | **Bass -0.8 (4.0), Treble 3.5** | Tonerider Rebel 90s have massive lower-mid inductive energy. Pulling Bass to 4.5 prevents low-end boom on drop-2 jazz chords. |
| **Framus Earl Slick (DiMarzio P-90s)** | Neck P-90, Vol 6.5, Tone 4.5 | **Bass 5.5, Treble -0.5 (2.0)** | **Treble -0.5 (3.0), Bass 4.8** | Swamp ash body and DiMarzio P-90s have a sharper attack. Roll guitar tone to 4.5 and TKIP Treble to 2.0 to maintain the "velvet" cushion. |
| **Fender Player II Telecaster** | Neck Single-Coil, Vol 7.5, Tone 5.0 | **Bass +1.0 (6.5), Treble 2.5** | **Bass +1.0 (5.8), Treble 3.0** | Single-coil requires elevated Bass (6.5) to simulate the round body of an archtop humbucker (Ed Bickert style). |
| **Squier Stratocaster (Tex-Mex)** | Position 1 (Neck SC), Vol 7, Tone 4.5 | **Bass +1.0 (6.5), Treble -0.5 (2.0)** | **Bass +1.0 (5.8), Treble 2.5** | Tex-Mex single-coils have hot upper-mids. Tame with Treble 2.0 and rely on the neck pickup's woody warmth. |

---

## Concept 2: "Tokyo Neon 1984" (80s Japanese City Pop / Funk Clean)

### 1. Anchor Instrument: Mid-1980s Squier Stratocaster Partscaster
- **Pickups & Strings**: Fender Tex-Mex Single-Coils, Position 4 (Neck + Middle); D'Addario XS (10-46).
- **Core Setting (Hardware)**: Rhythm Channel — Volume **3.2**, Attenuation **5.5**, Bass **4.8**, Treble **6.2**, Cab **2 (OH 212 Class A Blue)**. Reverb: Level **1.5**, Dwell **2.0**. Tremolo: **OFF**. Guitar Vol: **8.5–9.0**, Tone: **7.5–8.0**.
- **Core Setting (Software)**: Neural DSP Archetype Cory Wong X — D.I. Funk Console + The 4th Position Compressor (Blend 60%, Comp 45%, Volume 55%).
- **Post-Amp FX**: Studio D Chorus (Button 2), Galaxy Tape Echo (Head 1 slapback, Echo Rate 7.5, Echo Vol 2.0), Verve Solid-State Sweeten (Drive 2.5).

### 2. Universal 6-Guitar Calibration Guide (Tokyo Neon 1984)

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Squier Stratocaster** *(Anchor)* | Position 4 (Neck+Mid), Vol 9, Tone 8 | Baseline: Vol 3.2, Treb 6.2, Bass 4.8 | Baseline: Cory Wong X (Blend 60%) | The classic out-of-phase "quack"; crisp, percussive, snappy 16th-note chucks. |
| **Fender Player II Telecaster** | Position 2 (Neck+Bridge), Vol 8.5, Tone 7.5 | **Treble -0.5 (5.7), Bass +0.5 (5.3)** | **Clean Machine: Treble 55%, Presence 50%** | Parallel neck+bridge on Tele gives a slightly wider, fatter funk snap. Pull Treble back to 5.7 to tame bridge pickup edge. |
| **Epiphone Les Paul (Rebel 90s)** | Middle (Both P-90s RWRP), Vol 8, Tone 7 | **Bass -0.5 (4.3), Treble +0.5 (6.7)** | **Comp Blend 50%, High-Pass 80 Hz** | RWRP middle position is hum-canceling with distinct hollow quack. Boosting Treble to 6.7 restores single-coil sparkle on mahogany body. |
| **Framus Earl Slick (DiMarzio P-90s)** | Middle Position, Vol 8.5, Tone 7.0 | **Bass 4.8, Treble 6.0** | **Clean Machine: Treble 58%, Mid 40%** | Swamp ash body provides immediate, percussive snap that rivals a Stratocaster. Keep settings close to baseline. |
| **Gibson Les Paul Studio** | Middle (Both Humbuckers), Vol 7.5, Tone 8 | **Bass -1.0 (3.8), Treble +0.8 (7.0)** | **Bright Switch ON, Bass 35%** | To funk on humbuckers, scoop low end heavily (Bass 3.8) and boost Treble to 7.0. Roll guitar volume to 7.5 to clean input stage. |
| **Epiphone Sheraton II** | Middle (Both Humbuckers), Vol 8, Tone 8.5 | **Bass -1.2 (3.6), Treble +0.8 (7.0)** | **Bright Switch ON, High-Pass 100 Hz** | Flatwounds naturally mute top string snap. Engage Bright switch in software or push Treble to 7.0; yields an ultra-smooth, polished 70s soul rhythm. |

---

## Concept 3: "Smoky Tweed Roots" (Fingerstyle Folk & Americana Edge-of-Breakup)

### 1. Anchor Instrument: 2008 Epiphone Les Paul Standard Plus Top
- **Pickups & Strings**: Tonerider Rebel 90s (Alnico II HSP-90s, Neck Pickup); D'Addario XS (10-46).
- **Core Setting (Hardware)**: Lead Channel — Volume **3.5**, Attenuation **5.0**, Tone **3.5**, Mid-Bite **1.5 (Tweed 5E3 mode)**, Cab **1 (TK1660)**. Reverb: Level **2.5**, Dwell **3.5**. Tremolo: Speed **3.2**, Depth **2.8**. Guitar Vol: **6.5–7.0**, Tone: **6.0**.
- **Core Setting (Software)**: UADx Woodrow '55 — High Input, Inst Vol **3.2**, Mic Vol **2.5** (jumped), Tone **5.0**, Cab GB25 Greenback.
- **Post-Amp FX**: Galaxy Tape Echo (Head 2, Echo Rate 5.5, Feedback 2.0, Tape Age Used), TDR Nova (75 Hz HPF, 420 Hz dynamic cut), Verve Tape Glow (Drive 2.0).

### 2. Universal 6-Guitar Calibration Guide (Smoky Tweed Roots)

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Epiphone Les Paul (Rebel 90s)** *(Anchor)* | Neck P-90, Vol 6.5–7, Tone 6 | Baseline: Vol 3.5, Tone 3.5, Mid-Bite 1.5 | Baseline: Woodrow Inst 3.2, Mic 2.5 | Organic 5E3 Tweed sag; clean on finger plucks, hairing up on firm thumb snaps. |
| **Gibson Les Paul Studio** | Neck 490R (or Middle), Vol 7, Tone 6 | **Volume +0.5 (4.0), Tone +0.5 (4.0)** | **Inst Vol +0.4 (3.6), Mic Vol 2.5** | 490R humbucker has smoother top and moderate output. Nudging Volume to 4.0 restores the edge-of-breakup threshold. |
| **Framus Earl Slick (DiMarzio P-90s)** | Neck P-90, Vol 7.0, Tone 5.5 | **Tone 3.5, Mid-Bite 1.2** | **Woodrow Tone 4.5, Inst Vol 3.0** | DiMarzios are slightly hotter with more upper-mid bite. Keep Mid-Bite low (1.2) to stay firmly in Tweed territory without crunch. |
| **Fender Player II Telecaster** | Neck Pickup, Vol 8.0, Tone 6.5 | **Tone +1.0 (4.5), Mid-Bite +0.5 (2.0)** | **Woodrow Tone 5.5, Inst Vol 3.5** | Telecaster neck pickup has less output than P-90s. Advance Mid-Bite to 2.0 and Tone to 4.5 to give fingerstyle lines body and grit. |
| **Squier Stratocaster (Tex-Mex)** | Position 5 (Neck SC), Vol 8.0, Tone 6.5 | **Tone +0.8 (4.3), Mid-Bite +0.5 (2.0)** | **Woodrow Tone 5.2, Inst Vol 3.5** | Woody Ry Cooder / Bonnie Raitt slide and fingerstyle tone. Spongy tube sag cushions single-coil dynamics. |
| **Epiphone Sheraton II** | Neck Humbucker, Vol 7.0, Tone 6.5 | **Volume 3.5, Tone +0.5 (4.0), Mid-Bite 1.2** | **Woodrow Mic Vol -0.5 (2.0)** | Semi-hollow body adds deep woody resonance. Flatwounds sound earthy and dark; reduce Mic Vol in software to prevent bottom-end mud. |

---

## Concept 4: "Mayer Trinity Vocal Lead" (Modern Singing Blues-Rock / ODS Lead)

### 1. Anchor Instrument: 2012 Framus Earl Slick Artist Series
- **Pickups & Strings**: DiMarzio P-90s; Bigsby B500 Vibrato; D'Addario XS (10-46).
- **Core Setting (Hardware)**: Lead Channel — Volume **4.5**, Attenuation **5.5**, Tone **4.5**, Mid-Bite **4.0 (the vocal sweet spot)**, Cab **3 (OH 412 Basketweave M25)**. Reverb: Level **2.0**, Dwell **2.5**. Tremolo: **OFF**. Bridge P-90 (or Middle); Guitar Vol: **7.0** for rhythm crunch, **9.5–10** for soaring lead, Tone: **6.5**.
- **Core Setting (Software)**: Paradise Guitar Studio — Enigmatic '82 ODS (Cream/Suede model, Mid 7.0) pushed by TS Overdrive in Pre-FX through a 4x12 Greenback cab.
- **Post-Amp FX**: Waterfall Rotary Speaker (Slow/Chorale at 15–20% parallel mix), Studer A800 (30 IPS, +9 dB hot tape compression), Airwindows Console.

### 2. Universal 6-Guitar Calibration Guide (Mayer Trinity Lead)

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Framus Earl Slick (DiMarzio P-90s)** *(Anchor)* | Bridge P-90, Vol 7–10, Tone 6.5 | Baseline: Vol 4.5, Tone 4.5, Mid-Bite 4.0 | Baseline: Enigmatic ODS Mid 7.0 + TS | Singing horn-like vocal midrange sustain; Bigsby B500 adds expressive violin-like vibrato. |
| **Gibson Les Paul Studio** | Bridge 490T, Vol 8–10, Tone 7.0 | **Volume +1.0 (5.5), Mid-Bite +1.0 (5.0)** | **ODS Drive +10%, Mid 7.5** | **CRITICAL CALIBRATION**: 490T Alnico II is moderate output (~8.5k). Pushing Volume to 5.5 and Mid-Bite to 5.0 restores liquid Dumble sustain. |
| **Epiphone Les Paul (Rebel 90s)** | Bridge P-90, Vol 7–9.5, Tone 6.0 | **Tone -0.5 (4.0), Mid-Bite 4.0** | **ODS Presence -5%, Treble 4.8** | Tonerider Rebel 90 bridge is fat and creamy. Pulling Tone to 4.0 yields a thick Santana / Gary Moore vocal lead. |
| **Fender Player II Telecaster** | Bridge (or Neck), Vol 8–10, Tone 5.5 | **Tone -0.8 (3.7), Mid-Bite +0.5 (4.5)** | **TS Tone 2.5, ODS Treble 4.5** | Tele bridge pickup has sharp treble. Roll guitar tone to 5.5 and TKIP Tone to 3.7; Mid-Bite 4.5 provides thick, biting Texas blues grind. |
| **Squier Stratocaster (Tex-Mex)** | Position 1 (Bridge) or Pos 5 (Neck), Vol 8.5–10 | **Tone -0.5 (4.0), Mid-Bite +0.5 (4.5)** | **TS Drive 2.5, Level 6.5, ODS Mid 7.2** | The quintessential SRV / John Mayer "Gravity" solo voice. Neck pickup with Mid-Bite 4.5 gives thick, fluty, horn-like sustain. |
| **Epiphone Sheraton II** | Bridge Humbucker, Vol 7.5–9, Tone 6.5 | **Mid-Bite -0.5 (3.5), Attenuation 5.0 max** | **ODS Master Gain -10%** | Semi-hollow body can take off into uncontrolled feedback if Mid-Bite exceeds 4.0. Keep Attenuation $\le 5.0$ for controllable singing sustain. |

---

## Concept 5: "Nordic Cathedral" (Ambient / Chillhop / Modern Neo-Classical)

### 1. Anchor Instrument: 2024 Fender Player II Telecaster
- **Pickups & Strings**: Single-coils (Neck or Middle Position); Alder / Rosewood; D'Addario XS (10-46).
- **Core Setting (Hardware)**: Rhythm Channel — Volume **2.5**, Attenuation **5.0**, Bass **6.8**, Treble **2.8**, Cab **1 (TK1660)**. Reverb: Level **3.5**, Dwell **4.5**. Tremolo: Speed **2.2**, Depth **3.5**. Guitar Vol: **7.0**, Tone: **5.0**.
- **Core Setting (Software)**: UADx Dream '65 — Volume **2.5**, Bright **OFF**, Bass **6.0**, Treble **3.5**, Reverb **3.5**, Tremolo Speed **2.5**, Depth **3.5**.
- **Post-Amp FX**: ValhallaSuperMassive (Lyra/Capricorn mode, 35–40% mix, 350 ms delay, 70% feedback, 35% warp), Galaxy Tape Echo (Head 3, Echo Rate 4.5), TDR Nova (HPF 85 Hz, LPF 5500 Hz).

### 2. Universal 6-Guitar Calibration Guide (Nordic Cathedral)

| Guitar | Pickup & Tone Dial-In | Hardware TKIP Adjustments | Software Amp Adjustments | Sonic Adaptation & Playing Notes |
|---|---|---|---|---|
| **Fender Player II Telecaster** *(Anchor)* | Neck (or Middle), Vol 7, Tone 5 | Baseline: Vol 2.5, Bass 6.8, Treb 2.8 | Baseline: Dream '65 Vol 2.5, Bass 6.0 | Ethereal cathedral soundscape; piano-like low-end foundation with breathing tremolo pulse. |
| **Epiphone Sheraton II** | Neck Humbucker, Vol 6.5, Tone 6.0 | **Bass -1.5 (5.3), Treble +0.5 (3.3)** | **Dream '65 Bass 4.8, Treble 4.0** | Flatwounds and semi-hollow construction have massive natural low frequencies. Pull Bass to 5.3 to prevent ambient reverb from blooming into mud. |
| **Gibson Les Paul Studio** | Neck 490R (or Middle), Vol 7, Tone 5.5 | **Bass -1.0 (5.8), Treble +0.5 (3.3)** | **Dream '65 Bass 5.0, Treble 4.0** | Humbuckers produce dense harmonic weight. Treble at 3.3 adds delicate chime to open-voiced chord voicings. |
| **Epiphone Les Paul (Rebel 90s)** | Neck P-90, Vol 6.5, Tone 4.5 | **Bass -1.2 (5.6), Treble 2.8** | **Dream '65 Bass 4.8, Treble 3.5** | Tonerider Rebel 90s provide rich cello-like fundamental. Rolling guitar volume to 6.5 keeps the Blackface preamp pristine and unclipped. |
| **Framus Earl Slick (DiMarzio P-90s)** | Middle Position, Vol 7.0, Tone 5.0 | **Bass -0.8 (6.0), Treble 2.8** | **Dream '65 Bass 5.2, Treble 3.5** | Bigsby vibrato allows slow, subtle chord shimmering before hitting ValhallaSuperMassive, creating lush pedal steel-like pads. |
| **Squier Stratocaster (Tex-Mex)** | Position 4 (Neck+Mid), Vol 7.5, Tone 5.5 | **Bass 6.5, Treble 3.0** | **Dream '65 Bass 5.8, Treble 3.8** | Out-of-phase Position 4 adds hollow, bell-like clarity that dissolves into the delay repeats with stone-cathedral depth. |
