---
amp: "Ten Piece (Audio Hertz)"
created: 2026-06-26
guitar: "Framus Earl Slick Artist Series (DiMarzio P-90s, D'Addario XS 10s)"
id: audio-hertz-ten-piece-bell
pickup_type: p-90
preset_name: "Ten Piece Bell P90"
status: initial
tags: "solid-state, decade, clean, chime, lo-fi, p-90, bright"
target: 'A glassy, clean, and articulate tone modeled on the Peavey Decade''s clean channel, optimized for snappy P-90 transients.'
tone-king-channel: bypassed
updated: 2026-06-26
preset_data:
  amp_platform: audio_hertz_ten_piece
  amp_settings:
    Channel: Normal
    Gain: 4.5
    Saturation: false
    Low: 4.5
    Mid: 3.5
    High: 7.5
    Post: 7.0
---

# Ten Piece Bell (P-90 Variant)

## Target Sound

The Audio Hertz **Ten Piece Bedroom Amp** is a detailed neural model of the legendary Peavey Decade practice amplifier. While most players associate this solid-state box with Josh Homme's fuzzy, lo-fi, mid-saturated "secret weapon" drive, it can also produce a surprisingly chimey, glassy, and articulate clean tone. 

Because the DiMarzio P-90s in your Framus Earl Slick Artist Series guitar have a very fat midrange and a hot output, they will quickly push a solid-state clean channel into boxiness and muddy compression. To achieve a sparkling, "bell-like" clean:
1. **Normal Channel (No Saturation)**: We keep Saturation **OFF** and run on the Normal channel, setting the Gain to **4.5** to find the boundary of clean headroom and solid-state compression.
2. **Scoop the Midrange Honk**: The Peavey Decade has a very prominent and honky midrange. Pulling the Mid control back to **3.5** cleans up the solid-state boxiness, sweetens the tone, and prevents your P-90s from sounding nasal.
3. **Push the High End for Chime**: We boost the High control to **7.5** to highlight the snappy, metallic transients of your swamp ash body and roundwound strings, bringing out that glass-like clarity.
4. **Clean Power Stage**: We push the Post Gain (master volume) to **7.0** to drive the output stage cleanly.

We route this direct input signal to a parallel bus loaded with a short, clean space (Space Designer) to give the solid-state dry signal a three-dimensional room bloom.

---

## Signal Chain

### 1. Physical Front-End

| Control | Setting | Purpose |
|---------|---------|---------|
| Route | Direct Input | Direct to iD14 JFET input for cleanest DI path |
| Tone King Imperial Preamp | Bypassed | N/A |
| TONEX One | Bypassed | N/A |

### 2. Audio Hertz Ten Piece — Bedroom Amp

| Control | Setting | Purpose |
|---------|---------|---------|
| Channel | Normal | Selects the clean channel |
| Saturation | Off (Bypassed) | Disengages the solid-state clipping circuit |
| Gain | 4.5 | Sets input sensitivity for maximum clean headroom with hot P-90s |
| Low | 4.5 | Tightens up the low-end mud on hum-canceling P-90 pickups |
| Mid | 3.5 | Scoops the honky midrange to sweeten the tone and prevent boxiness |
| High | 7.5 | Highlights the glassy, chimey transients of the single-coil construction |
| Post | 7.0 | Drives the virtual solid-state power amp output cleanly |

---

## Starting Point Guide

- **First adjustment**: If the tone feels a bit too glassy or scratchy with your P-90 bridge pickup, roll your guitar's **Tone knob** back to **7** to sweeten the high end.
- **Key interaction**: The Mid control on this amp is extremely sensitive. If you switch to the neck pickup and it feels boxy, pull the Mid control down to **3.0** to clear up the lower-mid congestion.
- **Gain Staging Note**: Since the Audient iD14 JFET DI input delivers a digital signal that is **3.2 dB hotter** than standard DAW calibration, adjust the input trim or lower your guitar's volume knob to **8** to maintain clean headroom.

---

## Feedback History

### 2026-06-26 — initial
- Toneprint proposed to match the "Bell" clean theme on the Audio Hertz Ten Piece (Peavey Decade) for Framus P-90s.
