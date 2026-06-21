#!/usr/bin/env python3
"""
generate_tonex_stomp_viewer.py
Queries the TONEX Library.db for all Stomp captures, normalizes the pedal data,
and produces a self-contained, high-fidelity web viewer in tone-advisor/tonex-stomp-viewer.html.
"""

import os
import json
import sqlite3
from pathlib import Path
from datetime import datetime

# Paths
DB_PATH = Path("/Users/miketremoulet/Documents/IK Multimedia/TONEX/Library.db")
OUTPUT_PATH = Path("/Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/tonex-stomp-viewer.html")
BACKUP_DIR = "/Users/miketremoulet/Documents/IK Multimedia/TONEX/Backup/ToneModels"

# Comprehensive profiles mapping manufacturer:model to description paragraphs
PEDAL_DESCRIPTIONS = {
    # AC Noises
    "ac noises:cats on amps": "A boutique fuzz pedal combining high-gain silicon fuzz with a unique EQ contour, designed for fuzzy, thick garage rock and doom tones.",
    
    # Analogman
    "analogman:king of tone": "A legendary dual-channel overdrive designed in collaboration with Jim Weider. Based on a heavily modified Marshall Bluesbreaker circuit, it offers a highly transparent, touch-sensitive drive that preserves the natural tone of the guitar and amp. It is prized for its organic voice-like clipping and clean boost capabilities.",
    "analogman:prince of tone": "The single-channel version of the famous King of Tone, featuring a three-way toggle switch to select between Clean, OD, and Distortion modes, providing the same transparent, amp-like clipping in a compact format.",
    
    # Arion
    "arion:metal master": "A vintage 1980s high-gain plastic enclosure pedal known for its extreme, aggressive distortion and raw, scooped-mid metal tones popularized in underground grunge and metal scenes.",
    
    # Beetronics
    "beetronics:royal jelly": "A unique dual-channel overdrive/fuzz blender that lets you mix overdrive and fuzz circuits in parallel, creating everything from warm boost to thick, synth-like fuzz with rich analog texture.",
    
    # Boss
    "boss:bd-2 blues driver": "A classic overdrive designed to emulate the natural, dynamic crunch of a warm tube amplifier. It is highly touch-sensitive and responds beautifully to guitar volume adjustments, offering a bright, clear clipping structure ideal for blues, classic rock, and indie genres.",
    "boss:ce-1 chorus ensemble": "A capture of the iconic 1976 chorus ensemble preamp. In addition to its legendary modulation, its preamp stage has a famous analog grit and warmth that adds character, thickness, and vintage compression to clean and crunch signals.",
    "boss:ds-1 distortion": "The definitive orange distortion pedal introduced in 1978. It features a hard-clipping circuit that delivers a tight, focused distortion with a scooped midrange, widely used by Kurt Cobain, Joe Satriani, and John Frusciante for alternative rock and lead tones.",
    "boss:ds-2 turbo distortion": "An expansion of the DS-1, featuring two modes: Mode 1 delivers the classic DS-1 sound, while Mode 2 ('Turbo') adds a mid-range boost that cuts through the mix for screaming solos.",
    "boss:fz-1w": "A premium Waza Craft fuzz that pays homage to vintage fuzz circuits. It offers a vintage mode with a classic spitty, saggy germanium character and a modern mode providing a smoother, higher-gain silicon fuzz with tighter bass.",
    "boss:fz-5 (mode o)": "A digital modeling fuzz set to Mode O (Octavia), emulating the classic octave-up fuzz tones made famous by Jimi Hendrix, offering high-gain vintage fuzz with a pronounced upper-octave whistle.",
    "boss:hm-2": "The legendary Heavy Metal pedal introduced in 1983. When all knobs are turned to max (the 'chainsaw' setting), it delivers the crushing, grinding buzzsaw guitar tone that defined the Swedish Death Metal scene (Entombed, Dismember) and shoegaze/indie rock.",
    "boss:mt-2 metal zone": "One of the most famous high-gain pedals of all time. It features a dual-stage gain circuit and a powerful 3-band parametric EQ, allowing for deep mid-scooping and tight bass, ideal for thrash and modern metal.",
    "boss:od-1": "The first compact pedal from Boss, introduced in 1977. It pioneered asymmetrical clipping, which produces smooth, tube-like second-harmonic distortion. It is a highly sought-after vintage overdrive with a prominent mid-range hump.",
    "boss:sd-1 super overdrive": "Introduced in 1981, this pedal uses Boss's patented asymmetrical clipping circuit to deliver a warm, smooth overdrive with a mid-range hump. It is a staple overdrive used to tighten high-gain tube amplifiers by cutting sub-bass and boosting mids.",

    # Cornerstone
    "cornerstone:gladio sc": "A high-end boutique overdrive designed to capture the legendary, smooth, compressy tones of a Dumble amp (specifically the clean/crunch channel). It offers an extremely touch-sensitive, woody, and dynamic drive.",
    
    # DOD
    "dod:boneshaker": "A specialized distortion pedal designed for low-tuned guitars and basses, featuring a 3-band parametric EQ that allows for precise control of the low-end clipping and mid frequencies without getting muddy.",
    "dod:fx86b death metal": "An aggressive, ultra-high-gain distortion pedal designed for extreme metal. It features active EQ controls for bass, mid, and treble, and lacks a gain knob because it is permanently locked at maximum gain for maximum brutality.",

    # Darkglass
    "darkglass:alpha omicron": "A premium bass distortion pedal designed in collaboration with Jon Stockman. It features two distinct distortion circuits (Alpha for punchy/defined, Omega for raw/brutal) that can be blended together, delivering modern metal bass crunch.",
    "darkglass:microtubes b7k": "A modern standard for heavy bass tones. Combining a powerful preamp with a dynamic overdrive, it features 4-band EQ and toggle switches to control high-mid attack and low-end saturation, delivering clanky, aggressive metal bass tones.",
    "darkglass:microtubes x ultra": "A bass machine that splits the signal into low and high frequencies, compressing the lows for massive sustain and distorting the highs for clarity and grind. It yields clean, massive, defined bass tones under high distortion.",
    "darkglass:omicron": "A compact version of the Darkglass bass distortion line, providing aggressive modern bass saturation with a focus on mid-range cut and clarity.",

    # Dunable
    "dunable:skeleton key": "A heavy-duty distortion pedal designed for doom, stoner rock, and metal, offering a massive wall of sound with heavy low-end saturation and amp-like gain characteristics.",

    # Dunlop
    "dunlop:band of gypsys fuzz": "A specialized silicon fuzz face circuit designed to capture the aggressive, bitey, and wild fuzz tones Jimi Hendrix used at the famous Band of Gypsys concerts in 1970.",

    # Electro-Harmonix
    "electro-harmonix:big muff": "The legendary Pi circuit, offering a massive, saturated fuzz-distortion sound with rich sustain and a heavily scooped midrange. It produces a thick wall of sound favored by David Gilmour, Smashing Pumpkins, and Jack White.",
    "electro-harmonix:graphic fuzz vintage": "A vintage EHX distortion combined with a graphic EQ, allowing you to sculpt the frequency response pre- and post-distortion for unique, filtered fuzz and drive textures.",
    "electro-harmonix:russian big muff": "Based on the famous 1990s military-grade Russian-made Big Muffs. It is known for having a smoother high-end, a less scooped midrange, and a massive, boomy bass response, highly popular for both guitar and bass.",

    # FLB
    "flb:1991": "A boutique pedal designed to emulate the classic Marshall JCM900 high-gain amp tones of the early 90s, delivering tight, crunch-to-lead hard rock and grunge distortion.",

    # Fender
    "fender:blender": "A legendary vintage octave fuzz pedal known for its harsh, metallic, and chaotic octave-up tones. It features a blend knob to mix the clean signal with the fuzz, utilized by Billy Corgan for biting leads.",
    "fender:sub-lime": "A massive bass fuzz pedal offering deep, sub-bass retaining fuzz with an expressive envelope and active EQ controls, keeping the low-end clean while distorting the mids and highs.",

    # Frantone
    "frantone:peach fuzz": "A high-end boutique fuzz pedal designed by Fran Blanche. It is highly regarded for its smooth, creamy, muff-style distortion with an incredibly thick low-end and singing, violin-like sustain.",

    # Fryer
    "fryer:treble booster deluxe": "A classic treble booster designed specifically to pair with Vox AC30 amps to capture Brian May's (Queen) signature screaming, mid-focused vocal lead tone.",

    # Fulltone
    "fulltone:'70 bc-108c": "A classic 1970 silicon fuzz face clone using BC-108 transistors. It offers a bright, aggressive fuzz with a 'Mids' control to cut through the mix, cleaning up nicely with the guitar's volume knob.",
    "fulltone:full-drive 2": "A classic dual-channel overdrive featuring a clean boost and a tube-screamer style mid-hump overdrive. It uses a toggle switch for Vintage, Flat Mids, and Comp-Cut modes, offering great versatility.",
    "fulltone:ocd": "The Obsessive Compulsive Drive. A highly popular overdrive/distortion that uses MOSFET transistors to deliver amp-like, touch-sensitive overdrive. It offers a wide dynamic range and features a High Peak/Low Peak switch for transparent boost or Marshall-style crunch.",
    "fulltone:plimsoul": "A unique dual-stage clipping pedal combining soft-clipping (like a Tube Screamer) and hard-clipping (like an OCD) in parallel, allowing you to blend between the two for a custom drive character.",

    # GCI
    "gci:brutalist jr": "A high-gain distortion pedal designed by Kurt Ballou of GodCity Instruments. Based on the classic MXR Distortion+ circuit but heavily modernized, it delivers aggressive, bitey hardcore punk and metal crunch.",

    # Greer
    "greer:lightspeed": "Widely considered one of the finest transparent overdrives ever made. It adds a natural, organic grit to the signal, maintaining the exact tone of your guitar and amplifier while adding a touch of sweet, tube-like compression.",

    # Hudson
    "hudson:broadcast": "A boutique preamp/drive based on the discrete Class-A console strip of a vintage 1960s Neve recording desk. Using a germanium transistor and a steel-core transformer, it delivers everything from clean console warmth to heavy console saturation.",

    # Ibanez
    "ibanez:ts808 tube screamer": "The legendary green overdrive pedal introduced in 1979. It features a prominent mid-range hump, a soft bass roll-off, and symmetrical clipping. It is the gold standard for boosting dirty tube amps, cutting muddy bass, and pushing solos through the mix.",

    # JHS
    "jhs:at+": "The Andy Timmons signature drive pedal. It features a high-gain distortion channel designed to sound like a British tube amplifier, along with an independent clean boost channel. A toggle switch simulates 25W, 50W, or 100W power-amp compression.",
    "jhs:charlie brown": "A pedal designed to replicate the classic, warm, saggy tone of a vintage Marshall JTM45 amplifier. It offers low-to-medium gain overdrive with a classic rock British vibe.",
    "jhs:charlie brown v4": "The updated version of the Charlie Brown, adding a full 3-band EQ to replicate the JTM45 amp controls, offering precise sculpting of vintage Marshall rock tones.",
    "jhs:hard drive": "An original JHS high-gain distortion pedal, offering modern, hard-clipping amp-like distortion with a versatile active EQ, geared for hard rock and metal rhythm and lead tones.",
    "jhs:morning glory": "One of the most popular transparent overdrives, based on the classic Marshall Bluesbreaker circuit. It offers light, transparent grit and features a high-gain toggle switch to add crunch and body without coloring your core tone.",
    "jhs:notadumble": "A Dumble-in-a-box style pedal, designed to replicate the smooth, singing, mid-rich sustain and highly touch-sensitive drive of the mythical Dumble Overdrive Special amplifier.",

    # Joyo
    "joyo:dark flame": "A budget-friendly modern high-gain metal distortion designed to emulate the tight, aggressive, and highly detailed high-gain tones of modern metal amps, featuring a 3-band EQ.",

    # Klon
    "klon:centaur": "The holy grail of overdrive pedals. Designed by Bill Finnegan, it uses a unique charge pump to increase internal voltage and blends clean signal with distorted signal. Prized as a transparent clean boost to push tube amps, or as a sweet, harmonic mid-gain overdrive.",

    # Landgraff
    "landgraff:dynamic overdrive": "A legendary, hand-wired boutique overdrive based on a highly modified Tube Screamer circuit. It features a three-way toggle switch for different clipping options (LED, MOSFET, or None) and is prized for its high-fidelity articulation.",

    # Lovepedal
    "lovepedal:jtm": "A compact overdrive designed to recreate the plexi-style, dynamic crunch and sag of a mid-60s Marshall JTM45 amplifier, cleaning up nicely with the guitar volume control.",

    # MXR
    "mxr:bass di+": "A staple bass preamp and DI pedal. It features an independent clean channel with a 'Color' switch for EQ-contouring, and a dedicated distortion channel with a blend control and gate to deliver tight, heavy rock bass tones.",
    "mxr:distortion +": "Introduced in the late 1970s, this pedal uses hard germanium clipping to deliver a fuzzy, bitey distortion. Popularized by Randy Rhoads, it works great as a dirty boost in front of a Marshall amp.",
    "mxr:overdrive": "A simple, classic overdrive offering smooth clipping with a moderate mid-range boost, useful as a clean boost or light crunch pedal.",

    # Maestro
    "maestro:fuzz tone fz-1b": "An updated version of the historic FZ-1 fuzz (the pedal behind the Stones' 'Satisfaction'). Using silicon transistors, it offers a bright, bitey, and nasal vintage buzz-fuzz tone.",

    # Marshall
    "marshall:drivemaster": "Introduced in the 90s as a successor to the Guv'nor. It features a full 3-band EQ and gain controls, replicating the classic Marshall JCM800 Plexi drive tones in a stompbox.",
    "marshall:shredmaster": "A 90s Marshall distortion pedal designed for high-gain thrash and hard rock. It offers a thick, scooped-mid distortion with a 'Contour' control, famous for its use by Jonny Greenwood of Radiohead.",
    "marshall:the guv'nor": "The original 1980s Marshall amp-in-a-box pedal. It features an effects loop and a powerful 3-band EQ, delivering the classic British crunch and roar of a Marshall stack.",

    # Maxon
    "maxon:od-808 overdrive": "The sister pedal to the Ibanez TS808, manufactured by the same company (Maxon) that originally built the Tube Screamer. It offers the same iconic mid-hump and compression for tightening high-gain amplifiers.",

    # Mosrite
    "mosrite:fuzzrite": "A legendary 1960s silicon fuzz pedal offering a buzzy, spitty, and razor-sharp fuzz. It is the signature sound of 60s surf rock, garage punk, and spaghetti western soundtracks.",

    # Nobels
    "nobels:odr-1": "The secret weapon of Nashville session guitarists. It is a highly natural, open overdrive that does not roll off bass frequencies, making it incredibly transparent. It features a unique 'Spectrum' control to sculpt treble and upper mids.",

    # Paul Cochrane
    "paul cochrane:tim": "A legendary boutique transparent overdrive and clean boost. Featuring an active 2-band EQ and a built-in effects loop, it offers an incredibly open, amp-like grit without adding a mid-hump or rolling off bass.",

    # Pete Cornish
    "pete cornish:tb-83": "An ultra-premium, hand-built treble booster based on the classic germanium Rangemaster circuit, customized for Queen's Brian May to deliver vocal, sustain-heavy lead tones.",

    # ProAnalog
    "proanalog:manticore": "A boutique overdrive loosely based on the Klon Centaur circuit, but modernized with extra controls to shape the low-end and midrange, offering everything from clean boost to rich, thick overdrive.",

    # ProCo
    "proco:rat": "The definitive distortion pedal introduced in 1978. Using an LM308 op-amp, it bridges the gap between distortion and fuzz. It features a unique 'Filter' control (a reverse tone control) and delivers everything from bitey crunch to thick, sludge-metal fuzz.",

    # Roger Mayer
    "roger mayer:classic fuzz": "A high-fidelity silicon fuzz pedal designed by Roger Mayer, the electronics guru who built custom fuzz pedals for Jimi Hendrix, offering rich, sustaining vintage fuzz.",

    # Seymour Duncan
    "seymour duncan:805": "An updated take on the classic Tube Screamer circuit, adding a full 3-band active EQ. This allows you to sculpt the mids, bass, and treble precisely, fixing the traditional Tube Screamer's loss of low-end.",
    "seymour duncan:power grid": "A high-gain distortion pedal featuring a multi-stage gain circuit and active 3-band EQ, designed for chunking rhythm and sustaining lead metal tones.",
    "seymour duncan:tweakfuzz": "A vintage-style silicon fuzz pedal featuring a 6-position 'Tweak' knob that changes the input capacitor, altering the bass response from thin and bitey to thick and muddy.",

    # Soldano
    "soldano:slo od": "A stompbox capture designed to emulate the legendary overdrive/lead channel of the Soldano SLO-100 tube amplifier, delivering singing, high-gain liquid leads and tight metal rhythm.",

    # Strymon
    "strymon:sunset": "A capture of Strymon's dual-channel digital drive pedal. It combines different classic drive circuits (Germanium, Texas, Treble Booster, 2-Stage, Hard Clipping, JFET) for endless stacking options.",

    # Suhr
    "suhr:riot": "A modern classic high-gain distortion pedal. It is designed to sound like a 100W high-gain tube amplifier, offering rich, modern distortion with excellent articulation, tight bass, and singing sustain, ideal for soloing and hard rock.",

    # Supro
    "supro:drive": "A pedal designed to replicate the power-amp saturation of a vintage Supro tube amplifier. It uses a custom-wound transformer to deliver rich, saggy, and gritty blues/rock crunch.",

    # T-Rex
    "t-rex:moller": "A classic dual-channel overdrive and clean boost pedal, featuring a mix control to blend the clean signal with the overdrive, offering transparent amp-like drive.",
    "t-rex:mudhoney": "A versatile distortion/fuzz pedal offering everything from vintage warm overdrive to thick, saturated fuzz, popular in the European indie and alternative rock scenes.",

    # Tech21
    "tech21:dp-3x": "The dUg Pinnick (King's X) signature bass preamp. It combines massive, compressed low-end with aggressive, growling high-end distortion, producing a heavy, bi-amped bass tone in a single pedal.",
    "tech21:sh1": "The Steve Harris (Iron Maiden) signature bass preamp, designed to capture his famous clanky, finger-style rock bass tone with a mid-forward bite and tight compression.",
    "tech21:sansamp": "The original analog amp simulator introduced in 1989. It uses a series of character switches to simulate vintage Fender, Marshall, and Mesa Boogie amplifiers, serving as a clean DI or amp-like drive.",
    "tech21:sansamp rbi": "A rackmount version of the famous SansAmp Bass Driver DI, offering deep controls for drive, presence, and blend to deliver warm, tube-like bass tones and modern rock grit.",
    "tech21:yyz": "The Geddy Lee (Rush) signature bass preamp, allowing you to blend clean bass compression ('Deep') with growly, saturated tube-style drive ('Drive') for a punchy, punchy rock tone.",

    # Vemuram
    "vemuram:jan ray": "A high-end boutique overdrive designed to recreate the clear, warm, and natural 'blackface' Fender amp tones of the 1960s. It features controls to adjust the bass and saturation, offering extremely transparent drive.",

    # Vertex
    "vertex:sss srv": "The Steel String Clean Drive. Designed to capture the glass, compression, and clean-drive characteristics of the legendary Steel String Singer Dumble amplifier popularized by Stevie Ray Vaughan.",

    # Walrus Audio
    "walrus audio:badwater": "A premium bass preamp and DI pedal featuring an opto-compressor, a 4-band active EQ, and a dedicated drive engine with a blend control, offering modern metal and rock bass tones.",

    # Wampler
    "wampler:leviathan": "A highly versatile fuzz pedal utilizing both silicon and germanium transistors. It features a toggle switch to select between the two, offering everything from smooth, gated fuzz to modern high-gain fuzz.",
    "wampler:moxie": "A boutique overdrive based on the classic TS9 Tube Screamer, but featuring Voice and Fat switches to add low-end and change the clipping style to a more transparent, amp-like character.",
    "wampler:plexi drive": "A pedal designed to replicate the legendary Marshall Plexi amplifier tones. It features a Bass Boost and a Bright switch to simulate the sound of a vintage 4x12 cabinet and Plexi head.",
    "wampler:slostortion": "A pedal designed to capture the aggressive, high-gain crunch and liquid leads of the Soldano SLO-100 amplifier, featuring an independent clean boost switch.",
    "wampler:triple wreck": "A massive high-gain distortion pedal designed to emulate a Mesa Boogie Triple Rectifier. It delivers modern, scooped metal rhythm and massive leads, featuring a switchable boost channel.",
    "wampler:tumnus": "A highly accurate recreation of the legendary Klon Centaur in a mini pedal format, delivering the same transparent boost and mid-range richness.",
    "wampler:tumnus deluxe": "An expanded version of the Tumnus, adding a full 3-band active EQ, a hot/normal gain switch, and a buffer bypass switch, providing ultimate control over the Klon drive.",
    "wampler:tumnus deluxe germanium": "A limited-edition version of the Tumnus Deluxe utilizing rare, hand-selected vintage Germanium diodes to deliver a warmer, smoother, and more compressed clipping character.",

    # Wattson
    "wattson:classic electronics fuzz": "A high-fidelity recreation of the legendary Shin-ei FY-6 companion fuzz, offering buzzy, octave-rich, and heavily filtered 1960s Japanese fuzz tones.",

    # Xotic
    "xotic:rc booster": "The industry standard for clean boost. It offers up to 20dB of completely transparent boost, paired with an active 2-band EQ (±15dB) to shape the tone without adding any compression or coloring.",
    
    # ZVex
    "zvex:distortron": "Based on ZVex's Box of Rock, this pedal is designed to simulate the sound of a vintage Marshall JTM45 amp turned to 10. It features a sub-bass control and a gain switch, offering rich, saggy plexi drive.",
}

def parse_stomp_name(stomp_name):
    """
    Normalizes a raw stomp name to a standard (Manufacturer, Pedal Model) tuple.
    Also corrects typos and merges name variations.
    """
    name = " ".join(stomp_name.split()).strip()
    lower = name.lower()
    
    manufacturer = "Other"
    model = name
    
    # 1. Start with prefix checks
    if lower.startswith("ac noises"):
        manufacturer = "AC Noises"
        model = name[9:].strip()
    elif lower.startswith("analogman") or lower.startswith("analog man") or lower.startswith("analohman"):
        manufacturer = "Analogman"
        if lower.startswith("analogman"):
            model = name[9:].strip()
        elif lower.startswith("analog man"):
            model = name[10:].strip()
        else:
            model = name[9:].strip()
    elif lower.startswith("arion"):
        manufacturer = "Arion"
        model = name[5:].strip()
    elif lower.startswith("beetronics") or lower.startswith("buzztronics"):
        manufacturer = "Beetronics"
        if lower.startswith("beetronics"):
            model = name[10:].strip()
        else:
            model = name[11:].strip()
    elif lower.startswith("boss"):
        manufacturer = "Boss"
        model = name[4:].strip()
    elif lower.startswith("ce1") or lower.startswith("ce-1"):
        manufacturer = "Boss"
        model = "CE-1 Chorus Ensemble"
    elif lower.startswith("cornerstone"):
        manufacturer = "Cornerstone"
        model = name[11:].strip()
    elif lower.startswith("cornish"):
        manufacturer = "Pete Cornish"
        model = name[7:].strip()
    elif lower.startswith("dod"):
        manufacturer = "DOD"
        model = name[3:].strip()
    elif lower.startswith("darkglass"):
        manufacturer = "Darkglass"
        model = name[9:].strip()
    elif lower.startswith("dunlop"):
        manufacturer = "Dunlop"
        model = name[6:].strip()
    elif lower.startswith("ehx"):
        manufacturer = "Electro-Harmonix"
        model = name[3:].strip()
    elif "big muff" in lower:
        manufacturer = "Electro-Harmonix"
        model = name
    elif lower.startswith("fender"):
        manufacturer = "Fender"
        model = name[6:].strip()
    elif lower.startswith("frantone"):
        manufacturer = "Frantone"
        model = name[8:].strip()
    elif lower.startswith("fryer"):
        manufacturer = "Fryer"
        model = name[5:].strip()
    elif lower.startswith("fulltone"):
        manufacturer = "Fulltone"
        model = name[8:].strip()
    elif lower.startswith("gci"):
        manufacturer = "GCI"
        model = name[3:].strip()
    elif lower.startswith("greer"):
        manufacturer = "Greer"
        model = name[5:].strip()
    elif lower.startswith("hudson"):
        manufacturer = "Hudson"
        model = name[6:].strip()
    elif lower.startswith("ibanez"):
        manufacturer = "Ibanez"
        model = name[6:].strip()
    elif lower.startswith("jhs"):
        manufacturer = "JHS"
        model = name[3:].strip()
    elif "notadumble" in lower:
        manufacturer = "JHS"
        model = "NotaDumble"
    elif lower.startswith("joyo"):
        manufacturer = "Joyo"
        model = name[4:].strip()
    elif lower.startswith("klon"):
        manufacturer = "Klon"
        model = name[4:].strip()
    elif lower.startswith("landgraff"):
        manufacturer = "Landgraff"
        model = name[9:].strip()
    elif lower.startswith("lovepedal"):
        manufacturer = "Lovepedal"
        model = name[9:].strip()
    elif lower.startswith("mxr") or lower.startswith("bas di+"):
        manufacturer = "MXR"
        if lower.startswith("bas di+"):
            model = "Bass DI+"
        else:
            model = name[3:].strip()
    elif lower.startswith("maestro"):
        manufacturer = "Maestro"
        model = name[7:].strip()
    elif lower.startswith("marshall") or lower.startswith("the guv'nor"):
        manufacturer = "Marshall"
        if lower.startswith("marshall"):
            model = name[8:].strip()
        else:
            model = name
    elif lower.startswith("maxon"):
        manufacturer = "Maxon"
        model = name[5:].strip()
    elif lower.startswith("mosrite"):
        manufacturer = "Mosrite"
        model = name[7:].strip()
    elif lower.startswith("nobels"):
        manufacturer = "Nobels"
        model = name[6:].strip()
    elif lower.startswith("proanalog"):
        manufacturer = "ProAnalog"
        model = name[9:].strip()
    elif lower.startswith("proco") or lower.startswith("pro co") or lower.startswith("rat") or lower == "proco rat":
        manufacturer = "ProCo"
        if lower.startswith("proco"):
            model = name[5:].strip()
        elif lower.startswith("pro co"):
            model = name[6:].strip()
        else:
            model = name
    elif lower.startswith("roger mayer"):
        manufacturer = "Roger Mayer"
        model = name[11:].strip()
    elif lower.startswith("sansamp"):
        manufacturer = "Tech21"
        model = "SansAmp " + name[7:].strip()
    elif lower.startswith("seymour duncan"):
        manufacturer = "Seymour Duncan"
        model = name[14:].strip()
    elif lower.startswith("soldano"):
        manufacturer = "Soldano"
        model = name[7:].strip()
    elif lower.startswith("strymon"):
        manufacturer = "Strymon"
        model = name[7:].strip()
    elif lower.startswith("suhr"):
        manufacturer = "Suhr"
        model = name[4:].strip()
    elif lower.startswith("supro"):
        manufacturer = "Supro"
        model = name[5:].strip()
    elif lower.startswith("t-rex") or lower.startswith("t rex"):
        manufacturer = "T-Rex"
        if lower.startswith("t-rex"):
            model = name[5:].strip()
        else:
            model = name[5:].strip()
    elif lower.startswith("tech21") or lower.startswith("tech 21"):
        manufacturer = "Tech21"
        if lower.startswith("tech21"):
            model = name[6:].strip()
        else:
            model = name[7:].strip()
    elif lower.startswith("vemuram"):
        manufacturer = "Vemuram"
        model = name[7:].strip()
    elif lower.startswith("vertex"):
        manufacturer = "Vertex"
        model = name[6:].strip()
    elif lower.startswith("walrus audio") or lower.startswith("walrus auidio") or lower.startswith("walrus"):
        manufacturer = "Walrus Audio"
        if lower.startswith("walrus audio"):
            model = name[12:].strip()
        elif lower.startswith("walrus auidio"):
            model = name[13:].strip()
        else:
            model = name[6:].strip()
    elif lower.startswith("wampler"):
        manufacturer = "Wampler"
        model = name[7:].strip()
    elif lower.startswith("wattson"):
        manufacturer = "Wattson"
        model = name[7:].strip()
    elif lower.startswith("xotic"):
        manufacturer = "Xotic"
        model = name[5:].strip()
    elif lower.startswith("zvex"):
        manufacturer = "ZVex"
        model = name[4:].strip()
    
    # 2. Standalone fallback checks for matching models
    if manufacturer == "Other":
        if lower == "tim" or lower == "tim " or lower == "tm":
            manufacturer = "Paul Cochrane"
            model = "Tim"
        elif "tumnus" in lower:
            manufacturer = "Wampler"
            model = "Tumnus" + (" Deluxe" if "deluxe" in lower or "dlx" in lower else "") + (" Germanium" if "germanium" in lower or "ger" in lower else "")
        elif "skeleton key" in lower:
            manufacturer = "Dunable"
            model = "Skeleton Key"
        elif "life pedal" in lower or lower == "lifepedal":
            manufacturer = "EarthQuaker Devices"
            model = "Life Pedal"
        elif "flb 1991" in lower:
            manufacturer = "FLB"
            model = "1991"
        elif "lightspeed" in lower:
            manufacturer = "Greer"
            model = "Lightspeed"
        elif "broadcast" in lower:
            manufacturer = "Hudson"
            model = "Broadcast"
        elif "jan ray" in lower:
            manufacturer = "Vemuram"
            model = "Jan Ray"
        elif "peach fuzz" in lower:
            manufacturer = "Frantone"
            model = "Peach Fuzz"
        elif "fuzzrite" in lower:
            manufacturer = "Mosrite"
            model = "Fuzzrite"
        elif "manticore" in lower:
            manufacturer = "ProAnalog"
            model = "Manticore"
        elif "boneshaker" in lower:
            manufacturer = "DOD"
            model = "Boneshaker"
        elif "brutalist" in lower:
            manufacturer = "GCI"
            model = "Brutalist JR"
        elif "dark flame" in lower:
            manufacturer = "Joyo"
            model = "Dark Flame"

    # 3. Model Name Cleanup & Normalization
    model = model.strip()
    if model.startswith("-"):
        model = model[1:].strip()
        
    # Replace typos inside models
    model_lower = model.lower()
    if model_lower == "bas di+":
        model = "Bass DI+"
    elif model_lower in ("ens crunch", "es crunch"):
        model = "CE-1 Chorus Ensemble"
    elif model_lower == "galdio sc":
        model = "Gladio SC"
    elif model_lower == "fz-5 mod o":
        model = "FZ-5 (Mode O)"
    elif model_lower in ("mt2", "mt-2", "metal zone"):
        model = "MT-2 Metal Zone"
    elif model_lower == "sd-1":
        model = "SD-1 Super Overdrive"
    elif model_lower == "ds-1":
        model = "DS-1 Distortion"
    elif model_lower in ("ds-2 dist1", "ds-2 dist2", "ds2 turbo"):
        model = "DS-2 Turbo Distortion"
    elif model_lower in ("blues driver bd-2", "blues driver"):
        model = "BD-2 Blues Driver"
    elif model_lower == "od808":
        model = "OD-808 Overdrive"
    elif model_lower == "ts808":
        model = "TS808 Tube Screamer"
    elif model_lower in ("ocd v1.7", "ocd"):
        model = "OCD"
    elif model_lower in ("tumnus ger dlx", "tumnus germanium dlx", "tumnus germanium dlx with tim", "tim into tumnus germanium dlx"):
        model = "Tumnus Deluxe Germanium"
    elif model_lower == "king of tone":
        model = "King of Tone"
    elif model_lower == "prince of tone":
        model = "Prince of Tone"
        
    # Capitalize model if needed
    if model and model[0].islower() and not model.startswith("v1") and not model.startswith("v2"):
        model = model[0].upper() + model[1:]
        
    return manufacturer, model

def fetch_data():
    """Queries SQLite for stomp captures and returns structured data."""
    if not DB_PATH.exists():
        raise FileNotFoundError(f"TONEX Library database not found at {DB_PATH}")
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = """
        SELECT 
          tm.GUID,
          tm.Tag_ModelName,
          tm.Tag_StompName,
          tm.Tag_ModelCategory,
          tm.Skin,
          tm.Factory,
          tm.Tag_Description,
          tm.Tag_ModelComment,
          tm.DateTimeAdded,
          nm.Nickname
        FROM ToneModels tm
        LEFT JOIN ToneModelsUserIDMatch um ON tm.GUID = um.GUID
        LEFT JOIN UserIDNicknameMatch nm ON um.UserID = nm.UserID
        WHERE tm.TargetOrder = '2 - Stomp'
        ORDER BY tm.Tag_StompName, tm.Tag_ModelName
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    
    captures = []
    for r in rows:
        guid, model_name, stomp_name, category, skin, factory, desc, comment, dt_added, nickname = r
        
        # Clean up category name (remove 'STOMP - ')
        cat_clean = category or ""
        if cat_clean.startswith("STOMP - "):
            cat_clean = cat_clean[8:]
        if not cat_clean:
            cat_clean = "UTILITY"
            
        mfg, pedal_model = parse_stomp_name(stomp_name or "Unknown Stomp")
        
        # Determine creator name
        if factory == 1:
            creator = "IK Multimedia"
        elif nickname:
            creator = nickname
        else:
            creator = "Unknown / Imported"
            
        # File Path
        file_path = f"{BACKUP_DIR}/{guid}.txm"
        file_exists = os.path.exists(file_path)
        
        captures.append({
            "guid": guid,
            "name": model_name or "Unnamed Capture",
            "raw_stomp_name": stomp_name,
            "manufacturer": mfg,
            "pedal_model": pedal_model,
            "category": cat_clean.title(),
            "skin": skin or "MXRSingleRed",
            "factory": bool(factory),
            "description": desc or "",
            "comment": comment or "",
            "added": dt_added or "",
            "creator": creator,
            "file_path": file_path,
            "file_exists": file_exists
        })
        
    return captures

def generate_html(captures):
    """Generates the HTML file containing the web viewer."""
    # Organize data for JS
    # stats
    total_captures = len(captures)
    factory_count = sum(1 for c in captures if c["factory"])
    community_count = total_captures - factory_count
    
    categories = {}
    for c in captures:
        cat = c["category"]
        categories[cat] = categories.get(cat, 0) + 1
        
    # Group by manufacturer -> pedal, attaching profiles
    grouped = {}
    for c in captures:
        mfg = c["manufacturer"]
        pedal = c["pedal_model"]
        
        # Resolve descriptive profile paragraph
        key = f"{mfg.lower()}:{pedal.lower()}"
        description = PEDAL_DESCRIPTIONS.get(key, "Boutique stompbox capture local to your library.")
        
        if mfg not in grouped:
            grouped[mfg] = {}
        if pedal not in grouped[mfg]:
            grouped[mfg][pedal] = {
                "description": description,
                "captures": []
            }
            
        grouped[mfg][pedal]["captures"].append(c)
        
    # Build list of manufacturers with counts
    mfg_list = []
    for mfg, pedals in grouped.items():
        pedal_count = len(pedals)
        cap_count = sum(len(p_info["captures"]) for p_info in pedals.values())
        mfg_list.append({
            "name": mfg,
            "pedal_count": pedal_count,
            "capture_count": cap_count
        })
    mfg_list.sort(key=lambda x: x["name"].lower())

    # Build the HTML template
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TONEX Stomp Vault — Local Pedal Captures</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0f1115;
      --panel-bg: #161a22;
      --panel-alt: #1f2430;
      --border: #2a303c;
      --border-focus: #3d4659;
      --text: #e2e8f0;
      --text-muted: #8a99ad;
      --accent: #ff7b00;
      --accent-glow: rgba(255, 123, 0, 0.15);
      --accent-secondary: #00bcd4;
      --success: #10b981;
      
      --chip-bg: rgba(255, 255, 255, 0.02);
      --chip-hover: rgba(255, 255, 255, 0.06);
      --hover-bg: rgba(255, 255, 255, 0.03);
      
      --badge-od-bg: rgba(255, 123, 0, 0.12);
      --badge-od-text: #ff9100;
      --badge-od-border: rgba(255, 123, 0, 0.2);
      
      --badge-dist-bg: rgba(244, 63, 94, 0.12);
      --badge-dist-text: #f43f5e;
      --badge-dist-border: rgba(244, 63, 94, 0.2);
      
      --badge-fuzz-bg: rgba(168, 85, 247, 0.12);
      --badge-fuzz-text: #a855f7;
      --badge-fuzz-border: rgba(168, 85, 247, 0.2);
      
      --badge-eq-bg: rgba(14, 165, 233, 0.12);
      --badge-eq-text: #0ea5e9;
      --badge-eq-border: rgba(14, 165, 233, 0.2);
      
      --badge-utility-bg: rgba(100, 116, 139, 0.12);
      --badge-utility-text: #94a3b8;
      --badge-utility-border: rgba(100, 116, 139, 0.2);
      
      --welcome-glow: radial-gradient(circle at top right, rgba(255, 123, 0, 0.03), transparent 40%);
      
      --pedal-boss-yellow: #f1cd03;
      --pedal-boss-orange: #f7630c;
      --pedal-boss-green: #008751;
      --pedal-boss-black: #1a1a1a;
      --pedal-ibanez-green: #76a337;
      --pedal-klon-gold: #d4af37;
      --pedal-rat-black: #1f1f1f;
      --pedal-red: #c62828;
      --pedal-blue: #1565c0;
      --pedal-dark-blue: #0d47a1;
      --pedal-white: #eeeeee;
      --pedal-silver: #b0bec5;
      --pedal-orange: #e65100;
      --pedal-purple: #6a1b9a;
    }}

    html[data-theme="light"] {{
      --bg: #f8fafc;
      --panel-bg: #ffffff;
      --panel-alt: #f1f5f9;
      --border: #e2e8f0;
      --border-focus: #cbd5e1;
      --text: #0f172a;
      --text-muted: #64748b;
      --accent: #ea580c;
      --accent-glow: rgba(234, 88, 12, 0.12);
      --accent-secondary: #0891b2;
      --success: #059669;
      
      --chip-bg: rgba(0, 0, 0, 0.02);
      --chip-hover: rgba(0, 0, 0, 0.05);
      --hover-bg: rgba(0, 0, 0, 0.03);
      
      --badge-od-bg: rgba(234, 88, 12, 0.08);
      --badge-od-text: #ea580c;
      --badge-od-border: rgba(234, 88, 12, 0.15);
      
      --badge-dist-bg: rgba(225, 29, 72, 0.08);
      --badge-dist-text: #e11d48;
      --badge-dist-border: rgba(225, 29, 72, 0.15);
      
      --badge-fuzz-bg: rgba(147, 51, 234, 0.08);
      --badge-fuzz-text: #9333ea;
      --badge-fuzz-border: rgba(147, 51, 234, 0.15);
      
      --badge-eq-bg: rgba(2, 132, 199, 0.08);
      --badge-eq-text: #0284c7;
      --badge-eq-border: rgba(2, 132, 199, 0.15);
      
      --badge-utility-bg: rgba(71, 85, 105, 0.08);
      --badge-utility-text: #475569;
      --badge-utility-border: rgba(71, 85, 105, 0.15);
      
      --welcome-glow: radial-gradient(circle at top right, rgba(234, 88, 12, 0.02), transparent 40%);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: background-color 0.25s, color 0.25s;
    }}

    h1, h2, h3, h4 {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
    }}

    /* --- App Layout --- */
    header {{
      height: 70px;
      background-color: var(--panel-bg);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 30px;
      flex-shrink: 0;
      transition: background-color 0.25s, border-color 0.25s;
    }}

    .logo-container {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, var(--accent), #ff5100);
      color: #000;
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 14px;
      padding: 6px 10px;
      border-radius: 6px;
      letter-spacing: 0.05em;
    }}

    header h1 {{
      font-size: 20px;
      letter-spacing: -0.02em;
    }}

    /* --- Stats Dashboard --- */
    .header-stats {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .stat-chip {{
      background-color: var(--chip-bg);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      transition: background-color 0.2s, border-color 0.2s;
    }}

    .stat-chip .val {{
      font-weight: 700;
      color: var(--accent-secondary);
      font-size: 14px;
    }}

    /* --- Layout scroll adjustments --- */
    .app-body {{
      display: flex;
      flex: 1;
      height: calc(100vh - 70px);
      max-height: calc(100vh - 70px);
      min-height: 0;
      overflow: hidden;
    }}

    /* --- Sidebar (Navigation) --- */
    .sidebar {{
      width: 320px;
      height: calc(100vh - 70px);
      max-height: calc(100vh - 70px);
      background-color: var(--panel-bg);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      flex-shrink: 0;
      transition: background-color 0.25s, border-color 0.25s;
    }}

    .search-panel {{
      padding: 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: border-color 0.25s;
    }}

    .search-wrapper {{
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background-color: var(--bg);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 13px;
      outline: none;
      transition: all 0.2s;
    }}

    .search-input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px var(--accent-glow);
    }}

    .filter-btn-group {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
    }}

    .filter-btn {{
      background-color: var(--chip-bg);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }}

    .filter-btn:hover {{
      background-color: var(--chip-hover);
      color: var(--text);
    }}

    .filter-btn.active {{
      background-color: var(--accent-glow);
      border-color: var(--accent);
      color: var(--accent);
    }}

    .source-filter {{
      display: flex;
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: hidden;
      font-size: 11px;
    }}

    .source-btn {{
      flex: 1;
      background-color: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 4px;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
      font-weight: 500;
    }}

    .source-btn:not(:last-child) {{
      border-right: 1px solid var(--border);
    }}

    .source-btn:hover {{
      background-color: var(--chip-hover);
      color: var(--text);
    }}

    .source-btn.active {{
      background-color: var(--border);
      color: var(--text);
    }}

    .nav-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px;
    }}

    .mfg-group {{
      margin-bottom: 8px;
    }}

    .mfg-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-muted);
      cursor: pointer;
      user-select: none;
    }}

    .mfg-header:hover {{
      color: var(--text);
    }}

    .mfg-pedals {{
      margin-top: 2px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .pedal-nav-item {{
      background-color: transparent;
      border: none;
      color: var(--text);
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      text-align: left;
      cursor: pointer;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.12s;
    }}

    .pedal-nav-item:hover {{
      background-color: var(--hover-bg);
    }}

    .pedal-nav-item.active {{
      background-color: var(--accent-glow);
      color: var(--accent);
      font-weight: 600;
    }}

    .pedal-nav-item .badge {{
      background-color: var(--chip-bg);
      color: var(--text-muted);
      font-size: 10px;
      font-weight: 600;
      padding: 2px 6px;
      border-radius: 10px;
    }}

    .pedal-nav-item.active .badge {{
      background-color: var(--accent);
      color: #000;
    }}

    /* --- Main Workspace Panel --- */
    .main-workspace {{
      flex: 1;
      height: calc(100vh - 70px);
      max-height: calc(100vh - 70px);
      overflow-y: auto; /* Enable scroll ability in the main window */
      padding: 40px;
      background: var(--welcome-glow), var(--bg);
      transition: background-color 0.25s;
    }}

    /* --- Welcome State --- */
    .welcome-card {{
      max-width: 600px;
      margin: 80px auto;
      text-align: center;
      background-color: var(--panel-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 40px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
      transition: background-color 0.25s, border-color 0.25s;
    }}

    .welcome-card h2 {{
      font-size: 26px;
      margin-bottom: 12px;
      color: var(--text);
    }}

    .welcome-card p {{
      color: var(--text-muted);
      font-size: 14px;
      line-height: 1.6;
      margin-bottom: 24px;
    }}

    .welcome-icon {{
      font-size: 48px;
      margin-bottom: 20px;
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0% {{ transform: scale(1); opacity: 0.8; }}
      50% {{ transform: scale(1.05); opacity: 1; }}
      100% {{ transform: scale(1); opacity: 0.8; }}
    }}

    /* --- Pedal Card Detail --- */
    .pedal-detail-card {{
      background-color: var(--panel-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
      transition: background-color 0.25s, border-color 0.25s;
      margin-bottom: 20px;
    }}

    /* Visual Pedal Graphic Mockup */
    .pedal-visual-header {{
      height: 180px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 30px 40px;
      overflow: hidden;
      border-bottom: 1px solid var(--border);
    }}

    .pedal-visual-header::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      opacity: 0.15;
      background: radial-gradient(circle at 70% 30%, rgba(255,255,255,0.4), transparent 60%);
      z-index: 1;
    }}

    .pedal-visual-details {{
      position: relative;
      z-index: 2;
    }}

    .pedal-visual-mfg {{
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      opacity: 0.8;
      margin-bottom: 4px;
    }}

    .pedal-visual-name {{
      font-size: 32px;
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      letter-spacing: -0.01em;
    }}

    .pedal-controls {{
      display: flex;
      gap: 16px;
      position: relative;
      z-index: 2;
    }}

    .pedal-knob {{
      width: 44px;
      height: 44px;
      border-radius: 50px;
      background: radial-gradient(circle, #333 40%, #111 80%);
      border: 3px solid #222;
      box-shadow: 0 4px 6px rgba(0,0,0,0.4), inset 0 2px 2px rgba(255,255,255,0.1);
      position: relative;
    }}

    .pedal-knob::after {{
      content: '';
      width: 3px;
      height: 15px;
      background-color: #eee;
      position: absolute;
      top: 3px;
      left: calc(50% - 1.5px);
      border-radius: 2px;
      transform-origin: bottom center;
    }}

    .knob-1::after {{ transform: rotate(-45deg); }}
    .knob-2::after {{ transform: rotate(15deg); }}
    .knob-3::after {{ transform: rotate(80deg); }}

    .pedal-footswitch {{
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: linear-gradient(135deg, #bbb, #777);
      border: 3px solid #555;
      box-shadow: 0 3px 5px rgba(0,0,0,0.3);
      position: relative;
    }}

    /* Stompbox Skins CSS Styles mapping to TONEX Skins */
    .skin-BossYellow {{ background-color: var(--pedal-boss-yellow); color: #000; }}
    .skin-BossYellow .pedal-knob {{ background: radial-gradient(circle, #444 30%, #000 80%); border-color: #111; }}
    .skin-BossYellow .pedal-knob::after {{ background-color: #f1cd03; }}

    .skin-BossOrange {{ background-color: var(--pedal-boss-orange); color: #000; }}
    .skin-BossOrange .pedal-knob {{ background: radial-gradient(circle, #444 30%, #000 80%); border-color: #111; }}
    .skin-BossOrange .pedal-knob::after {{ background-color: #f7630c; }}

    .skin-BossSilver {{ background-color: var(--pedal-boss-silver); color: #000; }}
    .skin-BossSilver .pedal-knob {{ background: radial-gradient(circle, #ddd 30%, #999 80%); border-color: #bbb; }}
    .skin-BossSilver .pedal-knob::after {{ background-color: #111; }}

    .skin-BossBlack {{ background-color: var(--pedal-boss-black); color: #fff; border-bottom: 5px solid #222; }}
    .skin-BossBlack .pedal-knob {{ background: radial-gradient(circle, #ff5722 30%, #c2185b 80%); border-color: #000; }}

    .skin-BossWhite {{ background-color: var(--pedal-white); color: #000; }}
    .skin-BossWhite .pedal-knob {{ background: radial-gradient(circle, #444 30%, #000 80%); border-color: #111; }}

    .skin-IbanezGreen {{ background-color: var(--pedal-ibanez-green); color: #fff; }}
    .skin-IbanezGreen .pedal-knob {{ background: radial-gradient(circle, #76a337 30%, #3e5a17 80%); border-color: #222; }}
    .skin-IbanezGreen .pedal-knob::after {{ background-color: #fff; }}

    .skin-KlonGold {{ background: linear-gradient(135deg, #e5c060, #b08a26); color: #402302; }}
    .skin-KlonGold .pedal-knob {{ background: radial-gradient(circle, #5d4037 35%, #3e2723 80%); border-color: #271410; }}
    .skin-KlonGold .pedal-knob::after {{ background-color: #e5c060; }}

    .skin-KlonSilver {{ background: linear-gradient(135deg, #eceff1, #b0bec5); color: #263238; }}
    .skin-KlonSilver .pedal-knob {{ background: radial-gradient(circle, #37474f 35%, #21272a 80%); border-color: #1c2124; }}

    .skin-MXRSingleRed {{ background-color: var(--pedal-red); color: #fff; }}
    .skin-MXRSingleGreen {{ background-color: var(--pedal-boss-green); color: #fff; }}
    .skin-MXRSingleOrange {{ background-color: var(--pedal-orange); color: #fff; }}
    .skin-MXRSingleBlue {{ background-color: var(--pedal-blue); color: #fff; }}
    .skin-MXRSingleDarkBlu {{ background-color: var(--pedal-dark-blue); color: #fff; }}
    .skin-MXRSingleYellow {{ background-color: #e0a904; color: #000; }}
    .skin-MXRSingleBlack {{ background-color: #1e1e1e; color: #e2e8f0; border: 1px solid #333; }}
    .skin-MXRSingleWhite {{ background-color: #f9f9f9; color: #111; }}
    .skin-MXRSingleSilver {{ background-color: #b0bec5; color: #111; }}
    .skin-MXRSingleGold {{ background-color: #c5a059; color: #000; }}
    .skin-MXRDoubleBlack {{ background-color: #111; color: #fff; border-bottom: 4px solid #333; }}
    .skin-MXRDoubleRed {{ background-color: #880e4f; color: #fff; }}

    .skin-RATBlack, .skin-RATYellow, .skin-RATWhite {{ background-color: var(--pedal-rat-black); color: #fff; border: 1px solid #333; }}
    .skin-RATBlack .pedal-knob::after {{ background-color: #fff; }}
    .skin-RATYellow .pedal-knob::after {{ background-color: #ffd600; }}

    .skin-BigMuff {{ background: linear-gradient(to bottom, #cfd8dc, #90a4ae); color: #b71c1c; border-bottom: 6px solid #455a64; }}
    .skin-BigMuff .pedal-knob {{ background: radial-gradient(circle, #111 40%, #000 80%); border-color: #333; width: 48px; height: 48px; }}
    .skin-BigMuff .pedal-knob::after {{ background-color: #ff1744; }}

    .skin-LifePedal {{ background-color: #000; color: #ff1744; border: 2px solid #ff1744; }}
    .skin-Blender {{ background-color: #b0bec5; color: #212121; }}
    .skin-ToneXPedalBlack {{ background-color: #181818; color: #fff; border-bottom: 4px solid #000; }}

    /* --- Pedal Details Metadata --- */
    .pedal-meta-details {{
      background-color: var(--panel-alt);
      padding: 18px 30px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 30px;
      font-size: 13px;
      transition: background-color 0.25s, border-color 0.25s;
    }}

    .pedal-meta-item {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .pedal-meta-item .label {{
      font-size: 10px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .pedal-meta-item .val {{
      font-weight: 600;
      color: var(--text);
    }}

    /* --- Capture List --- */
    .captures-section-header {{
      padding: 24px 30px 10px;
      font-size: 16px;
      color: var(--text);
      font-weight: 600;
    }}

    .capture-list {{
      padding: 0 20px 20px;
    }}

    .capture-row {{
      background-color: var(--chip-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 10px;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1.5fr;
      align-items: center;
      gap: 16px;
      transition: all 0.15s;
    }}

    .capture-row:hover {{
      background-color: var(--hover-bg);
      border-color: var(--border-focus);
    }}

    .capture-name-desc {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .capture-title {{
      font-size: 14px;
      font-weight: 600;
      color: var(--text);
    }}

    .capture-desc {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    .capture-category {{
      display: flex;
    }}

    .cat-badge {{
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }}

    .cat-Overdrive {{ background-color: var(--badge-od-bg); color: var(--badge-od-text); border: 1px solid var(--badge-od-border); }}
    .cat-Distortion {{ background-color: var(--badge-dist-bg); color: var(--badge-dist-text); border: 1px solid var(--badge-dist-border); }}
    .cat-Fuzz {{ background-color: var(--badge-fuzz-bg); color: var(--badge-fuzz-text); border: 1px solid var(--badge-fuzz-border); }}
    .cat-Eq {{ background-color: var(--badge-eq-bg); color: var(--badge-eq-text); border: 1px solid var(--badge-eq-border); }}
    .cat-Utility {{ background-color: var(--badge-utility-bg); color: var(--badge-utility-text); border: 1px solid var(--badge-utility-border); }}

    .capture-creator {{
      font-size: 12px;
      color: var(--text);
    }}

    .creator-sub {{
      font-size: 10px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .capture-actions {{
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 8px;
    }}

    .btn {{
      background-color: var(--panel-alt);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.12s;
    }}

    .btn:hover {{
      background-color: var(--border);
      border-color: var(--border-focus);
    }}

    .btn-primary {{
      background-color: var(--accent);
      border-color: var(--accent);
      color: #000;
      font-weight: 600;
    }}

    .btn-primary:hover {{
      background-color: #ff9100;
      border-color: #ff9100;
    }}

    /* Copy Feedback Toast */
    .toast {{
      position: fixed;
      bottom: 30px;
      right: 30px;
      background-color: var(--success);
      color: #fff;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
      z-index: 1000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    .toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    /* Local File Path Panel */
    .filepath-panel {{
      background-color: rgba(0, 0, 0, 0.08);
      border-top: 1px solid var(--border);
      padding: 8px 16px;
      font-family: monospace;
      font-size: 11px;
      color: var(--text-muted);
      word-break: break-all;
      grid-column: 1 / -1;
      margin-top: 10px;
      border-radius: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    
    html[data-theme="dark"] .filepath-panel {{
      background-color: rgba(0, 0, 0, 0.2);
    }}

    .filepath-panel .copy-path-btn {{
      background: transparent;
      border: none;
      color: var(--accent-secondary);
      cursor: pointer;
      font-weight: 600;
    }}

    .filepath-panel .copy-path-btn:hover {{
      text-decoration: underline;
    }}

    /* Custom Webkit Scrollbars for Premium Aesthetics */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
      background: transparent;
    }}
    
    ::-webkit-scrollbar-thumb {{
      background: var(--border);
      border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
      background: var(--border-focus);
    }}
  </style>
</head>
<body>

  <header>
    <div class="logo-container">
      <div class="logo-badge">TONEX</div>
      <h1>Stomp Vault</h1>
    </div>
    
    <div class="header-stats">
      <div class="stat-chip">
        <span>Stomps:</span>
        <span class="val">{len(mfg_list)} Pedals</span>
      </div>
      <div class="stat-chip">
        <span>Captures:</span>
        <span class="val" id="total-captures-val">{total_captures}</span>
      </div>
      <div class="stat-chip">
        <span>Overdrives:</span>
        <span class="val">{categories.get("Overdrive", 0)}</span>
      </div>
      <div class="stat-chip">
        <span>Distortions:</span>
        <span class="val">{categories.get("Distortion", 0)}</span>
      </div>
      <div class="stat-chip">
        <span>Fuzzes:</span>
        <span class="val">{categories.get("Fuzz", 0)}</span>
      </div>
      
      <!-- Design Theme Toggle -->
      <button id="theme-toggle" class="btn" style="background-color: var(--chip-bg); border-color: var(--border); color: var(--text); padding: 6px 12px; border-radius: 8px; font-size: 12px; cursor: pointer; display: flex; align-items: center; gap: 6px;">
        <span id="theme-toggle-icon">☀️</span>
        <span id="theme-toggle-text">Light Mode</span>
      </button>
    </div>
  </header>

  <div class="app-body">
    <!-- Sidebar Navigation -->
    <div class="sidebar">
      <div class="search-panel">
        <div class="search-wrapper">
          <input type="text" class="search-input" id="search-input" placeholder="Search pedals, captures, creators...">
        </div>
        
        <div class="filter-btn-group">
          <button class="filter-btn active" data-cat="all">All Types</button>
          <button class="filter-btn" data-cat="overdrive">Overdrive</button>
          <button class="filter-btn" data-cat="distortion">Distortion</button>
          <button class="filter-btn" data-cat="fuzz">Fuzz</button>
        </div>
        
        <div class="source-filter">
          <button class="source-btn active" data-source="all">All Sources</button>
          <button class="source-btn" data-source="factory">Factory</button>
          <button class="source-btn" data-source="community">Community</button>
        </div>
      </div>
      
      <div class="nav-list" id="nav-list">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- Main Content Workspace -->
    <div class="main-workspace" id="main-workspace">
      <!-- Welcome Screen by Default -->
      <div class="welcome-card">
        <div class="welcome-icon">🔌</div>
        <h2>TONEX Stomp Vault</h2>
        <p>Explore your library of locally-saved stomp captures. This vault details your physical pedal acquisitions, including their factory settings and downloaded community variants stored on your hard drive.</p>
        <p style="font-size: 12px; margin-bottom: 0;">Select a pedal manufacturer and model in the sidebar to view detailed captures and copy GUIDs directly into TONEX or Logic Pro.</p>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">GUID copied to clipboard!</div>

  <script>
    // Injected JSON data
    const STOMP_DATA = {json.dumps(grouped)};
    
    // Global state
    let activeMfg = "";
    let activePedal = "";
    let currentSearch = "";
    let currentCategory = "all";
    let currentSource = "all";

    // DOM Elements
    const searchInput = document.getElementById("search-input");
    const navList = document.getElementById("nav-list");
    const mainWorkspace = document.getElementById("main-workspace");
    const toast = document.getElementById("toast");
    
    // Theme Toggle Logic
    const themeToggle = document.getElementById("theme-toggle");
    const themeToggleIcon = document.getElementById("theme-toggle-icon");
    const themeToggleText = document.getElementById("theme-toggle-text");

    // Init
    window.addEventListener("DOMContentLoaded", () => {{
      renderNav();
      
      // Load saved theme
      const savedTheme = localStorage.getItem("tonex-stomp-theme") || "dark";
      setTheme(savedTheme);
      
      themeToggle.addEventListener("click", () => {{
        const currentTheme = document.documentElement.getAttribute("data-theme") || "dark";
        const newTheme = currentTheme === "dark" ? "light" : "dark";
        setTheme(newTheme);
      }});

      // Search event
      searchInput.addEventListener("input", (e) => {{
        currentSearch = e.target.value.toLowerCase();
        renderNav();
      }});

      // Category filters
      document.querySelectorAll(".filter-btn").forEach(btn => {{
        btn.addEventListener("click", (e) => {{
          document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
          e.target.classList.add("active");
          currentCategory = e.target.getAttribute("data-cat");
          renderNav();
        }});
      }});

      // Source filters
      document.querySelectorAll(".source-btn").forEach(btn => {{
        btn.addEventListener("click", (e) => {{
          document.querySelectorAll(".source-btn").forEach(b => b.classList.remove("active"));
          e.target.classList.add("active");
          currentSource = e.target.getAttribute("data-source");
          renderNav();
        }});
      }});
    }});

    function setTheme(theme) {{
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("tonex-stomp-theme", theme);
      
      if (theme === "light") {{
        themeToggleIcon.innerText = "🌙";
        themeToggleText.innerText = "Dark Mode";
      }} else {{
        themeToggleIcon.innerText = "☀️";
        themeToggleText.innerText = "Light Mode";
      }}
    }}

    // Filtering logic helper
    function getFilteredData() {{
      const filtered = {{}};
      let totalCount = 0;
      
      for (const mfg in STOMP_DATA) {{
        const filteredPedals = {{}};
        for (const pedal in STOMP_DATA[mfg]) {{
          const pedalObj = STOMP_DATA[mfg][pedal];
          const matches = pedalObj.captures.filter(cap => {{
            // Search text filter
            const matchesSearch = 
              pedal.toLowerCase().includes(currentSearch) ||
              mfg.toLowerCase().includes(currentSearch) ||
              cap.name.toLowerCase().includes(currentSearch) ||
              cap.creator.toLowerCase().includes(currentSearch) ||
              cap.guid.toLowerCase().includes(currentSearch);
            
            // Category filter
            const matchesCat = currentCategory === "all" || cap.category.toLowerCase() === currentCategory;
            
            // Source filter
            const matchesSource = 
              currentSource === "all" || 
              (currentSource === "factory" && cap.factory) ||
              (currentSource === "community" && !cap.factory);
              
            return matchesSearch && matchesCat && matchesSource;
          }});
          
          if (matches.length > 0) {{
            filteredPedals[pedal] = {{
              description: pedalObj.description,
              captures: matches
            }};
            totalCount += matches.length;
          }}
        }}
        if (Object.keys(filteredPedals).length > 0) {{
          filtered[mfg] = filteredPedals;
        }}
      }}
      
      document.getElementById("total-captures-val").innerText = totalCount;
      return filtered;
    }}

    // Sidebar navigation rendering
    function renderNav() {{
      const data = getFilteredData();
      navList.innerHTML = "";
      
      const sortedMfgs = Object.keys(data).sort((a, b) => a.localeCompare(b));
      
      if (sortedMfgs.length === 0) {{
        navList.innerHTML = `<div style="padding: 20px; color: var(--text-muted); text-align: center; font-size: 13px;">No matching stompboxes.</div>`;
        return;
      }}
      
      sortedMfgs.forEach(mfg => {{
        const mfgGroup = document.createElement("div");
        mfgGroup.className = "mfg-group";
        
        const mfgHeader = document.createElement("div");
        mfgHeader.className = "mfg-header";
        
        // Calculate captures count for this manufacturer
        let count = 0;
        for (const pedal in data[mfg]) {{
          count += data[mfg][pedal].captures.length;
        }}
        
        mfgHeader.innerHTML = `<span>${{mfg}}</span> <span style="opacity: 0.5; font-size: 10px;">${{count}}</span>`;
        mfgGroup.appendChild(mfgHeader);
        
        const mfgPedals = document.createElement("div");
        mfgPedals.className = "mfg-pedals";
        
        const sortedPedals = Object.keys(data[mfg]).sort((a, b) => a.localeCompare(b));
        sortedPedals.forEach(pedal => {{
          const item = document.createElement("button");
          item.className = "pedal-nav-item";
          if (activeMfg === mfg && activePedal === pedal) {{
            item.classList.add("active");
          }}
          
          const capCount = data[mfg][pedal].captures.length;
          item.innerHTML = `<span>${{pedal}}</span> <span class="badge">${{capCount}}</span>`;
          
          item.addEventListener("click", () => {{
            // Select pedal
            document.querySelectorAll(".pedal-nav-item").forEach(b => b.classList.remove("active"));
            item.classList.add("active");
            activeMfg = mfg;
            activePedal = pedal;
            showPedalDetail(mfg, pedal);
          }});
          
          mfgPedals.appendChild(item);
        }});
        
        mfgGroup.appendChild(mfgPedals);
        navList.appendChild(mfgGroup);
      }});
    }}

    // Display pedal details in the main workspace
    function showPedalDetail(mfg, pedal) {{
      const pedalObj = STOMP_DATA[mfg][pedal];
      if (!pedalObj) return;
      
      const captures = pedalObj.captures;
      if (!captures || captures.length === 0) return;
      
      const description = pedalObj.description;
      
      // Determine dominant skin
      const skin = captures[0].skin;
      
      // Count types
      const types = [...new Set(captures.map(c => c.category))].join(", ");
      
      // Render details
      let capturesHtml = "";
      captures.forEach(cap => {{
        const isFactory = cap.factory;
        const sourceLabel = isFactory ? "Factory Model" : `Community (${{cap.creator}})`;
        const commentHtml = cap.comment || cap.description ? 
          `<div class="capture-desc" style="grid-column: 1 / -1; margin-top: 4px; border-left: 2px solid var(--border); padding-left: 10px;">
             ${{cap.comment || cap.description}}
           </div>` : "";
           
        capturesHtml += `
          <div class="capture-row">
            <div class="capture-name-desc">
              <span class="capture-title">${{cap.name}}</span>
            </div>
            
            <div class="capture-category">
              <span class="cat-badge cat-${{cap.category}}">${{cap.category}}</span>
            </div>
            
            <div class="capture-creator">
              <div>${{sourceLabel}}</div>
              <div class="creator-sub">${{cap.added.split(" ")[0] || "Saved Locally"}}</div>
            </div>
            
            <div class="capture-actions">
              <button class="btn btn-primary" onclick="copyGUID('${{cap.guid}}')">
                <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                Copy GUID
              </button>
            </div>

            ${{commentHtml}}

            <div class="filepath-panel">
              <span>File: ${{cap.file_path}}</span>
              <button class="copy-path-btn" onclick="copyText('${{cap.file_path.replace(/'/g, "\\'")}}', 'Path copied!')">Copy Path</button>
            </div>
          </div>
        `;
      }});

      mainWorkspace.innerHTML = `
        <div class="pedal-detail-card">
          <!-- Visually Rich Pedal Header -->
          <div class="pedal-visual-header skin-${{skin}}">
            <div class="pedal-visual-details">
              <div class="pedal-visual-mfg">${{mfg}}</div>
              <div class="pedal-visual-name">${{pedal}}</div>
            </div>
            <div class="pedal-controls">
              <div class="pedal-knob knob-1"></div>
              <div class="pedal-knob knob-2"></div>
              <div class="pedal-knob knob-3"></div>
              <div style="display: flex; flex-direction: column; align-items: center; gap: 4px;">
                <div class="pedal-footswitch"></div>
              </div>
            </div>
          </div>
          
          <!-- Metadata strip -->
          <div class="pedal-meta-details">
            <div class="pedal-meta-item">
              <span class="label">Skins Code</span>
              <span class="val" style="font-family: monospace;">${{skin}}</span>
            </div>
            <div class="pedal-meta-item">
              <span class="label">Primary Category</span>
              <span class="val">${{types}}</span>
            </div>
            <div class="pedal-meta-item">
              <span class="label">Total Variants</span>
              <span class="val">${{captures.length}} captures</span>
            </div>
            <div class="pedal-meta-item">
              <span class="label">Location</span>
              <span class="val">Documents/IK Multimedia/TONEX/Backup/ToneModels/</span>
            </div>
          </div>
          
          <!-- Pedal Description Profile Block -->
          <div class="pedal-description-box" style="padding: 24px 30px; border-bottom: 1px solid var(--border); background-color: var(--panel-alt); font-size: 13.5px; line-height: 1.65; color: var(--text-muted); transition: background-color 0.25s, border-color 0.25s;">
            <strong style="color: var(--text); display: block; margin-bottom: 6px; font-family: 'Outfit', sans-serif; font-size: 14px; letter-spacing: 0.02em; text-transform: uppercase;">Pedal Profile</strong>
            ${{description}}
          </div>

          <!-- Capture List Header -->
          <h3 class="captures-section-header">Available Captures & Variants</h3>
          
          <!-- Capture Rows -->
          <div class="capture-list">
            ${{capturesHtml}}
          </div>
        </div>
      `;
    }}

    // Clipboard copy helpers
    function copyGUID(guid) {{
      navigator.clipboard.writeText(guid).then(() => {{
        showToast("GUID copied to clipboard!");
      }}).catch(err => {{
        console.error("Failed to copy GUID: ", err);
      }});
    }}

    // General text copy helper
    function copyText(text, msg) {{
      navigator.clipboard.writeText(text).then(() => {{
        showToast(msg);
      }}).catch(err => {{
        console.error("Failed to copy text: ", err);
      }});
    }}

    function showToast(message) {{
      toast.innerText = message;
      toast.classList.add("show");
      setTimeout(() => {{
        toast.classList.remove("show");
      }}, 2500);
    }}
  </script>

</body>
</html>
"""
    with open(OUTPUT_PATH, "w") as f:
        f.write(html)
        
    print(f"Generated web viewer at {OUTPUT_PATH}")

def main():
    print("Reading TONEX Library and gathering Stomp captures...")
    try:
        captures = fetch_data()
        print(f"Loaded {len(captures)} local stomp captures successfully.")
        generate_html(captures)
    except Exception as e:
        print(f"Error compiling TONEX stomp captures: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
