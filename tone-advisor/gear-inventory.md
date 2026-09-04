# Gear Inventory — Signal Chain Reference

All hardware, plugins, and signal chain components available in this rig. Organized by category. Use this as a reference when evaluating new additions.

---

## Physical Hardware

| Name | Maker | Description |
|------|-------|-------------|
| Imperial Preamp | Tone King | Two-channel tube preamp pedal. Rhythm channel: 60s American Blackface character (Fender Deluxe Reverb) — controls: Volume, Attenuation, Bass, Treble. Lead channel: 50s Tweed + British rock character — controls: Volume, Attenuation, Tone (high-freq contour), Mid-Bite (simultaneously adds gain, tightens bass, boosts upper mids). No Mid, Presence, or Cut controls on either channel. Shared spring convolution reverb and digital tremolo. Per-channel 3-position IR/cab selector (Tone King Imperial 1x12, Vox AC30 2x12, Marshall 4x12) with bypass. **Physical Knobs**: All knobs feature 9 pips (ticks) representing a continuous 1 to 9 scale. Pip 1 is fully left (minimum/off), Pip 5 is exactly at 12:00 (noon/flat), and Pip 9 is fully right (maximum/on). |
| iD14 mkII | Audient | Desktop USB-C audio interface. 2 mic/line preamps (JFET discrete input stage), 2 instrument inputs, monitor control. Primary analog front-end before Logic. |

---

## Host Environments

| Name | Maker | Status | Description |
|------|-------|--------|-------------|
| Standalone | Oort Media | **Active (Primary)** | Dedicated macOS Audio Unit plugin host. **Primary daily driver** for linear / single-amp signal chains, ultra-low latency practice, and rapid preset auditioning (`~/Library/Application Support/Standalone/Presets/`). |
| Element | Kushview | **Active (Parallel)** | Modular VST/AU plugin host graph environment. **Primary daily driver** for parallel dual-amp rigs, multi-amp routing, and complex signal splitting (`.els` session graphs). |
| Logic Pro | Apple | **Shelved (Legacy)** | Full DAW environment. **Shelved from active toolkit until further notice.** Legacy presets and `.pst` files remain supported in the archive, but no new toneprints are designed for Logic Pro. |

---

## Guitars

*Full specs sourced from `guitar_stable.md`. Tone-advisor notes added here for signal chain reference.*

### Electric Guitars

| # | Name | Finish / Year | Body / Neck | Pickups | Strings | Tone Notes |
|---|------|---------------|-------------|---------|---------|------------|
| 1 | Fender Player II Telecaster | British Racing Green · 2024 | Solid alder / Rosewood fingerboard, six-saddle modern bridge | Single-coil neck and bridge | D'Addario XS 10-46 | "The Home Base." Bridge: bright, percussive, cutting. Neck: warmer than expected for single-coil. Needs significant treble rollback on the Tone King for dark jazz tones. |
| 2 | 2014 Gibson Les Paul Studio | Ebony (Serial: 140020207) | Solid mahogany/maple | **490R neck / 490T bridge — both Alnico II, ~8.5k DCR matched pair** | D'Addario XS 10-46 | 120th Anniversary Edition. "Smooth Refinement" and sustain machine. Both pickups warm and moderate-output — warmer/lower than the 498T in LP Standards. Well-suited for jazz, neo-soul, vintage tones. Classic Rock and blues bridge settings need extra Volume/Mid-Bite to compensate for the 490T's moderate output. |
| 3 | Mid-1980s Squier Stratocaster "Partscaster" | Light Blue / Tortoiseshell pickguard | SQ-series MIJ body / E-series neck | Fender Tex-Mex pre-wired pickguard (3 single-coils) | D'Addario XS 10-46 | "The Funky Quack." Hot, punchy, pure nickel vintage warmth. Tex-Mex pickups are hotter than standard Strat singles. |
| 4 | 2013 Epiphone Sheraton II | Natural | Semi-hollow laminate maple | Humbuckers (neck and bridge) | Thomastik-Infeld Jazz Swing Flats 10s | "The Velvet Jazz Box." Semi-hollow adds acoustic bloom, natural sustain, warmth. Flatwound strings reinforce dark jazz character. More sensitive to feedback at high gain than solid-body. Bridge-neck blend available. |
| 5 | 2008 Epiphone Les Paul Standard Plus Top | Vintage Sunburst · 2008 | Solid mahogany/maple | **Tonerider Rebel 90s** (HSP-90 single-coils, Alnico II, RWRP set) | D'Addario XS 10-46 | "Singing P-90 Workhorse." Upgraded with Tonerider Rebel 90s in modern wiring. Punchy, articulate, and dynamic with rich low-mid weight and singing sustain; huge dynamic range on volume roll-off. |
| 6 | 2012 Framus Earl Slick Artist Series | Matte Black (Serial: L-000047-12) | Flat-top double cutaway swamp ash body / Bolt-in maple neck, rosewood fingerboard, 24.75" scale | **Two DiMarzio P-90 pickups (single-coil wound, soapbar housing)** · 3-way rotary selector · Bigsby B500 vibrato | Rotosound Yellows 10-46 | "The Slick Rocker." **P-90s are NOT humbuckers** — single-coil construction, natural upper-mid spike, brighter and more present than LP 490 series. Less Mid-Bite and treble needed on the Tone King vs humbuckers. Swamp ash body adds snap and clarity. Bigsby adds subtle pitch expression. |

### Acoustic Guitars & Bass

| # | Name | Specs | Notes |
|---|------|-------|-------|
| 7 | 2025 Cort Standard AD Mini | Spruce top, 3/4 size dreadnought · Rotosound Metal (Steel) strings | Travel/couch steel-string. |
| 8 | 1990s Washburn D-12 | Dreadnought | "Tim's Guitar." The sentimental dreadnought foundation. |
| 9 | 1978 Fender Precision Bass | 3-Color Sunburst | The vintage low-end anchor. |

### Former / Sold Instruments (Archive)

| Name | Year Sold | Body / Pickups | Strings | Historical Notes |
|------|-----------|----------------|---------|------------------|
| 2023 Revelation RFT DLX | 2026 | Thinline Tele-style (semi-hollow) / Alan Entwistle H90 pickups | D'Addario XS 10-46 | "The Aggressive Growler." P-90 character in humbucker housings. Sold due to lack of play time and fighting pickup character. Archived for reference. |

---

## UADx — Amp Emulations

| Name | Maker | Description |
|------|-------|-------------|
| Dream '65 Reverb Amp | Universal Audio | Fender Blackface Deluxe Reverb '65. Bright/Normal switch, mod circuit (Stock / Lead / D-Tex), built-in spring reverb, bias tremolo. No Middle control. Three cabinet choices, three mic choices. The quintessential clean-to-edge-of-breakup American amp. |
| Lion '68 Super Lead Amp | Universal Audio | Marshall Super Lead Plexi 1959 100W, '68. Three model variants: Lead (classic Plexi), Bass (rounder, more low-end), Brown (Variac mod, EVH character). Two-channel "jumped" configuration. Ghost Notes and Bright Cap switches. |
| Ruby '63 Top Boost Amp | Universal Audio | Vox AC30 '63. Three channels: VIB-TREM, NORMAL, BRILLIANT. Top Boost EQ (Treble/Bass) on BRILLIANT only. Tone Cut is counterintuitive — higher = fewer highs. Runs hot; low headroom. |
| Woodrow '55 Instrument Amp | Universal Audio | Fender Tweed Deluxe '55. Extremely low headroom — compression and breakup at very low volume. Tone control also affects gain. Two channels can be "jumped" for richness. Boost modes: Stock, KP-3K, EP-III. |
| Enigmatic '82 Overdrive Special Amp | Universal Audio | Four rare ODS-style boutique amps in one plugin. Voices: Suede (warm/round), Silver (bright/articulate), Cream (mid-heavy), Black (aggressive/tight). Very dynamic — cleans up with guitar volume. |
| Showtime '64 Tube Amp | Universal Audio | Fender Showman/Twin-style, high-headroom. Stays clean until 7–8+. Bright/Normal switch. No built-in reverb. Harmonic vibrato (pitch-based, not tremolo). Most neutral and transparent amp in the inventory — good clean platform. |
| Paradise Guitar Studio | Universal Audio | Full guitar studio environment. Multiple amp, cab, and effects configurations in one plugin. |

---

## UADx — Dynamics & Compression

| Name | Maker | Description |
|------|-------|-------------|
| 1176 Rev A Compressor | Universal Audio | FET peak limiter — Bluestripe variant. Slower attack range, more harmonic color and "hairiness." Attack 1=fastest, 7=slowest (counterintuitive). Release 7=fastest, 1=slowest. |
| 1176AE Compressor | Universal Audio | FET peak limiter — Anniversary Edition. |
| 1176LN Rev E Compressor | Universal Audio | FET peak limiter — Blackface/Silverface variant. Classic aggressive character. Part of 1176 Classic Limiter Collection. |
| LA-2A Silver Compressor | Universal Audio | Optical tube compressor — Silver panel variant. Program-dependent attack/release. Compress (3:1) and Limit (10:1) modes. Very musical, natural response. Part of Teletronix LA-2A Leveler Collection. |
| LA-2A Gray Compressor | Universal Audio | Optical tube compressor — Gray panel (slightly different circuit voicing from Silver). Part of Teletronix LA-2A Leveler Collection. |
| LA-2 Compressor | Universal Audio | Optical tube compressor — simplified version of Silver LA-2A. Same core character. |
| 175-B Tube Compressor | Universal Audio | Variable-mu tube compressor. Attack/Release clockwise = fastest (opposite of 1176). Gain Hi/Low switch. Gentle tube glue and warmth. Part of 175-B/176 Collection. |
| 176 Tube Compressor | Universal Audio | Variable-mu tube compressor. Ratio switch: 2:1 / 4:1 / 8:1 / 12:1. Parallel Mix control. Part of 175-B/176 Collection. |
| 610-B Tube Preamp & EQ | Universal Audio | Tube preamp with passive EQ. Gain drives harmonic tube coloration. Shelving and mid-peak EQ. Used for warmth, color, and gentle EQ shaping. |

---

## UADx — Reverb Chambers & Spaces

| Name | Maker | Description |
|------|-------|-------------|
| Capitol Chambers | Universal Audio | Four rooms beneath Capitol Tower (Chambers 2, 4, 6, 7). Hybrid IR + algorithmic (Dynamic Room Modeling). Four mic choices. Mix is logarithmic — far more aggressive than it appears; 5–10% is the practical guitar range. |
| Hitsville Reverb Chambers | Universal Audio | Two Motown Studios chambers: 2648 (bright, echo-like, parallel surfaces) and 2644 (smooth, pentagonal). Multiple speaker and mic combinations. Mix is logarithmic — 12 o'clock ≈ 15% wet. |
| Sound City Studios | Universal Audio | Sound City Studios recording environment and reverb space. |

---

## UADx — Tape, Saturation & Modulation

| Name | Maker | Description |
|------|-------|-------------|
| Galaxy Tape Echo | Universal Audio | Roland RE-201 Space Echo emulation. Twelve head-select positions across three playback heads. Built-in spring reverb. Echo Rate, Feedback, Tape Age (New/Used/Old). Wet Solo switch. |
| Studer A800 Multichannel Tape Recorder | Universal Audio | Studer A800 24-track tape machine emulation. Tape saturation, harmonic warmth, subtle wow/flutter. Used as a mix bus or per-track tape coloration. |
| Studio D Chorus | Universal Audio | Roland SDD-320 Dimension D emulation. Fixed modes 1–4 only — no continuous parameters. Mode 1: barely-there; Mode 4: maximum. Stereo output. |
| Verve Analog Machines Essentials | Universal Audio | Ten analog saturation machines: five tape (Edge, Glow, Distort, Overdrive, Fire, Sputter) and five solid-state (Sweeten, Warm, Thicken, Vintagize, Overdrive). Drive, Warble (tape only), Tone (solid-state only), Output controls. |

---

## UADx — Instruments & Other

| Name | Maker | Description |
|------|-------|-------------|
| Electra 88 Vintage Keys | Universal Audio | Rhodes-style electric piano emulation. |
| Waterfall B3 Organ | Universal Audio | Hammond B3 organ emulation with drawbar control and key click. |
| Waterfall Rotary Speaker | Universal Audio | Leslie rotary speaker cabinet emulation. Used with the B3 or as a guitar effect. |

---

## Neural DSP

| Name | Maker | Description |
|------|-------|-------------|
| Archetype Cory Wong X | Neural DSP | Cory Wong signature plugin. Signal chain: Pre FX (4th Position optical compressor) → The Clean Machine amp → Cab section (mic, position, room send) → Post FX (The Wash reverb/shimmer). All controls expressed as 0–100%. Three EQ instances (one per amp section), each independently activated. |

---

## Nembrini Audio — Amp Emulations

| Name | Maker | Description |
|------|-------|-------------|
| Mrh810 V2 | Nembrini Audio | Marshall JCM800 2210 emulation. Two channels: Lead (4x12AX7 + 4x EL34; classic British rock-to-metal gain) and Clean (crystal clean to crunch, ideal pedal platform). Six built-in cabinet choices, four mic emulations with on/off-axis + position/distance control, mixer section (blend two mics + ambience), and a 3-slot IR loader with blending. Filters, Noise Gate, and I/O sections included. |
| Divided 11 | Nembrini Audio | Divided by 13 CJ11 emulation. Class A, tube-rectified, 11W boutique combo — a modern take on a 1950s tweed design. Single channel: Volume, Treble, Bass, Master; Boost switch; High/Low input sensitivity switches. Crisp and clear, saturates beautifully and evenly. Six cabinet choices, four mic emulations, position/distance control, 3-slot IR loader. Filters, Noise Gate, I/O sections included. |
| Hughes & Kettner Puretone | Nembrini Audio | H&K Puretone Guitar Amplifier emulation. Clean, hi-fi, transparent character with excellent headroom. Touch-sensitive dynamics; smooth natural breakup at higher volumes. Studio-quality tone platform well suited to clean and edge-of-breakup work. |
| Jazz Chorus Solid State | Nembrini Audio | Roland JC-120 Jazz Chorus emulation. Pristine solid-state clean tone that doesn't break up. Built-in stereo chorus. Iconic platform for jazz, funk, R&B, and any context requiring ultra-clean, uncolored amplification. |
| Crunck V2 | Nembrini Audio | Original Nembrini design (freeware). Single high-gain channel: Gain, Master, Presence, EQ. Built-in 4x12 V30 cabinet (bypassable). Wide gain range — clean blues through modern metal. |

> **Gain staging note (all Nembrini amp plugins):** Default Master/Volume of 5 clips the Stereo Out. Pull amp volume to ~2.5 and trim −4 dB on the cab section Output slider. Target: −11 to −12 dBFS on hard strums. The Output slider is a transparent post-model trim; use it first. Master/Volume lives inside the amp model and affects feel — use it last.

---

## Nembrini Audio — Acoustic

| Name | Maker | Description |
|------|-------|-------------|
| Acoustic Voice Pro | Nembrini Audio | Acoustic guitar preamplifier for direct piezo/pickup signals. 10 guitar body emulations, 5 mic models (Audix ADX51, Beyerdynamic M210, Shure SM57, EV RE20, AKG C414). IR loader with factory + third-party IR support. Visual EQ, pedal section for clarity/dynamics/depth, and a post-effects rack (Analog Delay, Room Reverb, Modulation). |

---

## Nembrini Audio — Stomp Effects (Free)

| Name | Maker | Description |
|------|-------|-------------|
| 808 | Nembrini Audio | Ibanez TS-808 Tube Screamer emulation. JRC4558D IC circuit. Classic mid-hump overdrive — the standard boost-into-amp or standalone drive pedal. |
| Big Stuff | Nembrini Audio | Electro-Harmonix Big Muff emulation. Harmonic distortion and sustain; violin-like sustain character. |
| Black | Nembrini Audio | Pro Co RAT2 distortion emulation. Aggressive, compressed distortion with Filter control for tone shaping. |
| Clon Minotaur | Nembrini Audio | Klon Centaur transparent overdrive emulation. Adds gain without significantly altering the underlying guitar tone. |
| Wah | Nembrini Audio | Wah pedal. |

  
---

## Kuassa — Stomp Effects

| Name | Maker | Description |
|------|-------|-------------|
| Efektor Blues Barker | Kuassa | Marshall Bluesbreaker-style overdrive pedal emulation. Provides smooth, dynamic, tube-like overdrive with high touch-sensitivity. Retains the guitar's natural tone and dynamics while adding warm grit. |
| Efektor Blues River | Kuassa | Ibanez TS-9 / Tube Screamer-style overdrive pedal emulation. Features the classic mid-range hump, low-end roll-off, and smooth clipping. Ideal for boosting amp stages or adding singing vocal sustain to lead lines. |

---

## IK Multimedia

| Name | Maker | Description |
|------|-------|-------------|
| AmpliTube 5 | IK Multimedia | Guitar amp and effects suite. Large library of amp, cab, and stompbox models. Signal chain with up to 3 amps, 8 effects slots, cab/mic section. |
| TONEX | IK Multimedia | Neural amp/tone capture player. Plays back machine-learning captures (Tone Models) of real amps, pedals, and rigs. |
| MODO DRUM | IK Multimedia | Physics-based virtual drum instrument. Real-time simulation of drum physics rather than samples. |

---

## MixWave

MixWave plugins use a common interface: knob up = clockwise, double-click resets to default, Cmd (Mac) / Ctrl (Win) = fine adjustment. Signal flow: Input Volume → Noise Gate → processing chain (drag-and-drop reorderable) → Output Volume. White frame = active module; gray = bypassed.

### Two-Rock Bloomfield Drive

A "powerful and high headroom amplifier" known for "rich cleans, harmonic overdrive, and smooth transitions between tones." Has a clean channel and a separate lead channel.

**EQ Selection (switch)**
- **EQ 1**: Lower gain structure with enhanced headroom — the clean-tone choice; extended midrange, fuller bass
- **EQ 2**: More available gain but still clean headroom; preferred by most players for general use

**Tone Switches** (each boosts independently)
- **Bright**: Boosts high-frequency response
- **Mid**: Boosts midrange frequency response
- **Deep**: Boosts lower bass frequencies and smooths midrange
- **Tone Stack Bypass**: Bypasses Bass/Middle/Treble controls entirely

**Channel Controls**
- **Lead Switch**: Engages/disengages lead channel
- **Gain**: Overall gain of the amp (clean channel)
- **Lead Gain**: Lead channel input level
- **Lead Master**: Lead channel output level

**EQ Knobs**
- **Treble**: Lower = warmer and smoother; higher = more prominence and aggressiveness
- **Middle**: Lower = scooped; higher = increases midrange and body
- **Bass**: Full CCW cuts lows; turning up increases bass passed to next gain stage

**Output Controls**
- **Master**: Overall output level of the clean channel
- **Presence**: "Adjusts the contour of the high-frequency response" — subtle control for brightness or smoothing
- **Reverb**: Mixes reverb effect with dry signal (works with Reverb Send)
- **Vibe**: Affects top end harmonics

**Power and Tubes**
- **Full/Half Power**: 100w/50w (6L6) or 40w/20w (6V6)
- **Tube Select**: 6L6 = more headroom, cleaner; 6V6 = earlier breakup, warmer
- **Reverb Send**: Lower = short decay times; higher = longer decay times

**Built-in Overdrive Pedal** (separate section in UI)
- Drive, Balance, Tone, Bypass switch, Dry/Wet knob
- This is integrated into the plugin; can substitute for or stack with an external OD

**Cabinet**: 2x12 Two-Rock Vertical Cabinet with TR12 (Top) and TR12 (Bottom) speakers

**Microphones (21 options)**
- Dynamic: 57, 7B, 409, 421, 441, R20
- Tube: 47, 251, C12, 800g
- Condenser: Fet 47, 32, 4011, 2011, 4099, 450
- Ribbon: 122, 84, 42Bn
- Creative: Copper (lo-fi, midrange-focused, unique honky character)

**Gain staging note**: If input isn't clipping but output clips, adjust Master, cab mic level, and global output — more common with ultra-clean settings.

---

## Two Notes Audio Engineering

| Name | Maker | Description |
|------|-------|-------------|
| Torpedo Wall of Sound | Two Notes | Speaker cabinet IR loader and room simulator. Microphone placement control. Used for amp head → direct recording without a physical cabinet. |

---

## Valhalla DSP

| Name | Maker | Description |
|------|-------|-------------|
| ValhallaSuperMassive | Valhalla DSP | Free reverb and delay plugin. Eleven modes ranging from subtle room to massive infinite wash. Dense reverb tails, shimmer, and spatial effects. |

---

## Other Third-Party

| Name | Maker | Description |
|------|-------|-------------|
| Neural Amp Modeler | Steven Atkinson | Open-source neural network amp modeler. Loads .NAM model files (captures of real amps and pedals from the NAM community). |
| LAM16 | Tone Empire | Channel strip plugin — EQ and compression in one unit. |
| LockOn | SubMission Audio | Low-end/sub frequency processor and management tool. |
| Vinyl | iZotope | Vinyl record degradation simulator. Crackle, noise, warp, mechanical artifacts. Lo-fi and vintage character. |
| SongEngine | FeelYourSound | Chord progression and song arrangement generator. MIDI-based, outputs chord voicings and progressions. |
| COSMOS Sample Finder | Waves | AI-powered sample finder and organizer. |
| Groove Agent SE | Steinberg | Loop-based virtual drummer and beat player. Pattern-based drum programming. |
| HALion Sonic | Steinberg | Sample-based virtual instrument workstation. Large library of sounds. |
| TDR Nova | Tokyo Dawn Labs | Free parallel dynamic/parametric equalizer. Features 4 parametric bands + HPF/LPF. Native/internal preset manager (saves to `~/Library/Application Support/Tokyo Dawn Labs/TDR Nova/UserData.xml`). |
| MEqualizer | MeldaProduction | Free 6-band parametric equalizer with adjustable band shapes and an internal preset database. |

---

## Logic Pro — Guitar & Amp Effects

| Name | Description |
|------|-------------|
| Amp Designer | Full guitar amp + cabinet + microphone simulation. Models include Blackface (Fender clean), Brownface (warm vintage), British Bright (Marshall), Boutique 1/2 (complex), AC Boost (Vox-style), Stadium (high-gain British). |
| Bass Amp Designer | Bass guitar amp simulation. Dedicated bass amp models and cabinet options. |
| Pedalboard | Virtual stompbox pedalboard. Houses Logic's collection of modeled pedals (see stompboxes below). Up to 9 pedals in a chain. |

**Pedalboard Stompboxes** — all accessible inside the Pedalboard plugin:

| Name | Type |
|------|------|
| Auto-Funk | Auto-wah / envelope filter |
| Blue Echo | Tape-style echo/delay |
| Candy Fuzz | Fuzz distortion |
| Classic Wah | Wah pedal |
| Double Dragon | Dual overdrive |
| Dr. Octave | Octave effect |
| Flange Factory | Flanger |
| Fuzz Machine | Fuzz distortion |
| Grinder | Distortion |
| Grit | Overdrive/saturation |
| Happy Face Fuzz | Muff-style fuzz |
| Heavenly Chorus | Chorus |
| Hi-Drive | High-gain overdrive |
| Modern Wah | Wah pedal (modern voiced) |
| Monster Fuzz | Heavy fuzz |
| OctaFuzz | Octave fuzz |
| Phase Tripper | Phaser |
| Rawk! Distortion | Rock distortion |
| Retro Chorus | Vintage chorus |
| Robo Flanger | Flanger |
| Roswell Ringer | Ring modulator |
| Roto Phase | Phaser |
| Spring Box | Spring reverb |
| Squash Compressor | Compressor pedal |
| The Vibe | Uni-Vibe style modulation |
| Tie Dye Delay | Delay |
| Total Tremolo | Tremolo |
| Trem-O-Tone | Tremolo |
| Tru-Tape Delay | Tape delay |
| Tube Burner | Tube overdrive |
| Vintage Drive | Overdrive |
| Wham | Pitch shift / whammy |

---

## Logic Pro — Dynamics, Compression & EQ

| Name | Description |
|------|-------------|
| Channel EQ | 8-band parametric/shelving EQ. High-pass, low shelf, 4 peak bands, high shelf, low-pass. Primary surgical EQ tool. |
| Linear Phase EQ | Same as Channel EQ with linear phase response — zero phase shift. Higher latency; use for mastering or when phase accuracy matters. |
| Vintage Console EQ | Vintage-character console EQ emulation. |
| Vintage Graphic EQ | Vintage graphic EQ emulation. |
| Vintage Tube EQ | Vintage tube EQ emulation (Pultec-style character). |
| Graphic EQ | 31-band graphic equalizer. |
| Single Band EQ | Simple one-band EQ. |
| Match EQ | Analyzes and matches the spectral character of a reference track. |
| Compressor | Multi-circuit compressor. Models: Platinum Digital (transparent), Classic VCA (punchy), Studio VCA (dense), Vintage VCA (glued), Vintage FET (1176-style), Studio FET (aggressive), Vintage Opto (LA-2A-style). |
| Adaptive Limiter | Loudness limiter with look-ahead. Mastering and output ceiling use. |
| Limiter | Simple brickwall limiter. |
| Multipressor | Multiband compressor. Up to 4 bands with independent compression and gain. |
| Noise Gate | Threshold-based gate with variable range. |
| Expander | Downward expander — opens dynamic range below threshold. |
| DeEsser 2 | De-esser. Frequency-selective compression to control sibilance. |
| Enveloper | Transient designer. Independent attack and release shape control. |
| ChromaGlow | Harmonic saturation with 5 styles: Vintage, Modern, Tube, Tape, Solid State. Drive, Character, and Mix controls. |
| Exciter | Harmonic exciter. Adds high-frequency presence and air. |
| SubBass | Sub-bass synthesizer. Generates sub frequencies from existing audio. |

---

## Logic Pro — Reverb & Spatial

| Name | Description |
|------|-------------|
| Space Designer | Convolution reverb with large IR library (rooms, halls, plates, spaces, impulses). Pre-Delay, Size, Stereo Width, Mix. The most versatile reverb in Logic. |
| ChromaVerb | Modern algorithmic reverb. 14 room types. Visual display of decay. Built-in EQ and damping. |
| SilverVerb | Classic algorithmic reverb with modulation on the reverb tail. |
| Quantec Room Simulator | Vintage algorithmic room simulation. |
| Enverly | Reverb with envelope follower — reverb amount responds to signal dynamics. |
| Stereo Spread | Stereo widening. Adds frequency-based stereo separation. |
| Binaural Post-Processing | Binaural spatial audio processor. |
| Direction Mixer | M/S (mid-side) matrix for stereo manipulation. |
| Spreader | Widens mono sources into a stereo field. |

---

## Logic Pro — Delay

| Name | Description |
|------|-------------|
| Delay Designer | Step-based delay with up to 26 individually configurable taps. Complex rhythmic delay patterns. |
| Tape Delay | Vintage tape delay emulation. Delay time, feedback, tone filters, wow/flutter. |
| Stereo Delay | Independent left and right channel delay times. Cross-feedback option. |
| Echo | Simple, classic echo/slapback. |
| Sample Delay | Millisecond-precise sample offset. Phase alignment utility, not a musical delay. |
| Modulation Delay | Short delay with modulation — chorus and flanging-adjacent. |

---

## Logic Pro — Modulation

| Name | Description |
|------|-------------|
| Chorus | Classic chorus. Rate, Depth, Delay, Spread, Mix. |
| Flanger | Flanger. Rate, Depth, Feedback, Manual (center phase position). |
| Phaze 2 | Phaser. 4, 8, or 12-stage. Rate, Depth, Feedback. |
| Ensemble | Rich chorus/ensemble. Multiple modulated voices. |
| Tremolo | Amplitude modulation. Rate, Depth, Waveform, Smoothing. |
| Scanner Vibrato | Hammond-style scanner vibrato. Pitch modulation via rotating scanner circuit. |
| Rotor Cabinet | Leslie rotary speaker cabinet simulation. Speed control (Slow/Fast/Brake). |
| AutoFilter | Envelope follower or LFO-driven filter. Wah, filter sweep, and step-filter effects. |
| Ringshifter | Ring modulator and frequency shifter. |
| EVOC 20 FilterBank | Vocoder filterbank — analyzes audio and applies formant-based filtering. |
| EVOC 20 TrackOscillator | Pitch-tracking vocoder with internal oscillator. |

---

## Logic Pro — Distortion & Drive

| Name | Description |
|------|-------------|
| Overdrive | Soft-knee tube-style overdrive. |
| Distortion | Guitar-style distortion. Hard clipping character. |
| Distortion II | Alternate distortion circuit character. |
| Clip Distortion | Hard and soft clipping with tone shaping. |
| Bitcrusher | Bit-depth reduction and sample-rate crushing. Digital lo-fi, glitch, and crunch. |
| Phase Distortion | Phase-based distortion. |
| Fuzz-Wah | Combined fuzz and wah in one plugin. |
| Phat FX | Multi-effect processor — combines drive, filter, modulation, and compression in one unit. |
| Step FX | Multi-effect with step sequencer modulation. Rate-synced patterns control effects parameters. |
| Remix FX | DJ/performance effect unit — gating, tape stop, reverb throw, filter, etc. |

---

## Logic Pro — Instruments

| Name | Description |
|------|-------------|
| Alchemy | Sample manipulation and synthesis workstation. Import, granular, additive, spectral synthesis. |
| ES1 | Analog-style subtractive synth. Single oscillator. |
| ES2 | Analog-style polyphonic synth. Three oscillators, ring mod, FM, wavetable. |
| ES E / ES M / ES P | Simpler ES-series synths (Ensemble, Mono, Poly). |
| EFM1 | FM synthesis. One carrier + one modulator. |
| Retro Synth | Four synthesis types: Analog, Table (wavetable), FM, Sync. |
| Sculpture | Physical modeling synthesizer. String/object-based synthesis. |
| Sample Alchemy | Sample-based synthesis with granular and spectral manipulation. |
| EVOC 20 PolySynth | Polyphonic synthesizer with integrated vocoder. |
| Ultrabeat | Drum machine and synthesizer. Step sequencer with individual drum synth voices. |
| Vintage B3 | Hammond B3 organ emulation with drawbars, percussion, and scanner vibrato. |
| Vintage Clav | Hohner Clavinet D6 emulation. Pickup configuration and tone options. |
| Vintage Electric Piano | Rhodes Suitcase and Wurlitzer 200 emulations. |
| Vintage Mellotron | Mellotron M400 emulation. Tape-based orchestral sounds. |
| Drum Kit Designer | Acoustic drum kit player using Apple Loops drum content. |
| Drum Synth | Synthesized drum sounds. Individual voice synthesis per drum element. |
| Studio Bass | Session-quality upright and electric bass instrument. |
| Studio Horns | Session brass instrument patches. |
| Studio Piano | Acoustic grand and upright piano samples. |
| Studio Strings | Session string ensemble patches. |
| Quick Sampler | One-shot sample player. Quick drag-and-drop audio to instrument. |
| Sampler | Full sample instrument editor and player. |
| Auto Sampler | Automatically samples external hardware instruments. |

---

## Logic Pro — MIDI & Utility

| Name | Description |
|------|-------------|
| Pitch Correction | Monophonic pitch correction (Auto-Tune style). |
| Pitch Shifter | Pitch transposition with formant options. |
| Vocal Transformer | Pitch and formant manipulation for voice transformation. |
| Arpeggiator | MIDI arpeggiator with multiple pattern modes. |
| Beat Breaker | Beat slicer and re-arranger. Pattern-based audio manipulation. |
| Chord Trigger | Assigns chords to single MIDI notes. |
| Note Repeater | MIDI note repetition with rate and velocity control. |
| Randomizer | MIDI parameter randomization. |
| Modifier | MIDI data transformation and mapping. |
| Modulator | LFO and envelope generator for MIDI parameter modulation. |
| Velocity Processor | MIDI velocity scaling, compression, and offset. |
| Transposer | Real-time MIDI transposition. |
| Scripter | JavaScript-based MIDI processor. Custom MIDI logic via scripting. |
| Tuner | Chromatic guitar/instrument tuner. |
| BPM Counter | Tempo detection from audio. |
| Correlation Meter | Stereo phase correlation display. |
| Level Meter | Peak/RMS level metering. |
| Loudness Meter | LUFS integrated loudness measurement. |
| MultiMeter | Combined spectrum analyzer, goniometer, and level meters. |
| Mastering Assistant | AI-assisted mastering with EQ and limiting suggestions. |
| Gain | Simple level utility. |
| Multichannel Gain | Multi-channel level utility. |
| I/O | Hardware insert send/return. |
| Test Oscillator | Sine/noise test signal generator. |
| Down Mixer | Surround-to-stereo fold-down. |
| Spatial Audio Monitoring | Dolby Atmos monitoring and binaural render. |
| Dolby Atmos | Dolby Atmos spatial audio renderer. |
| Spectral Gate | Frequency-selective gating. Noise reduction via spectral analysis. |
| Sample Delay | Sub-millisecond phase offset utility. |
