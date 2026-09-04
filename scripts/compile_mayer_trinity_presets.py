#!/usr/bin/env python3
"""
compile_mayer_trinity_presets.py

Dedicated preset generator for the 3-Amp Parallel John Mayer Trinity setup.
Generates all 9 individual plugin presets into their respective factory preset directories:
  1. UADx Paradise: Showtime '64 (SSS Clean Anchor)
  2. UADx Paradise: Dream '65 (1964 Blackface Reverb Bloom)
  3. UADx Paradise: Enigmatic '82 (Dumble ODS Vocal Lead)
  4. Nembrini Audio: NA Clon Minotaur (Klon Centaur)
  5. Kuassa: Efektor Blues Barker (Marshall Bluesbreaker)
  6. Kuassa: Efektor Blues River (Boss BD-2 Keeley Phat Mod)
  7. Nembrini Audio: NA 808 (TS-10 / TS-808)
  8. UADx: LA-2A Silver Compressor (Submix Glue)
  9. UADx: Hitsville Reverb Chambers (Parallel Acoustic Room)

Usage:
  python3 scripts/compile_mayer_trinity_presets.py
"""

import os
import json
import uuid
import base64
import struct

BASE_UAD_PRESETS_DIR = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins"
PARADISE_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_paradise_guitar_studio")
PARADISE_TEMPLATE = os.path.join(PARADISE_DIR, "Non-Toneprints", "Boutique Warm Clean - Enigmatic.json")

LA2A_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_teletronix_la-2a_silver")
LA2A_BASE = os.path.join(LA2A_DIR, "Mike - Alternative.json")

HITSVILLE_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_hitsville_chambers")
HITSVILLE_BASE = os.path.join(HITSVILLE_DIR, "Mike Live Strings.json")

CLON_DIR = "/Users/miketremoulet/Documents/Nembrini Audio/NA Clon Minotaur"
NA808_DIR = "/Users/miketremoulet/Documents/Nembrini Audio/NA 808"
BARKER_DIR = "/Users/miketremoulet/Music/Kuassa/Presets/EfektorBluesBarker"
RIVER_DIR = "/Users/miketremoulet/Music/Kuassa/Presets/EfektorBluesRiver"

def compile_paradise_amp_preset(base_json, amp_idx, folder_name, cab_idx, title, settings):
    preset = json.loads(json.dumps(base_json))
    preset["name"] = title
    preset["uid"] = uuid.uuid4().hex
    
    controls = preset["chunk"]["controls"]
    controls["amp"] = {"real_value": amp_idx}
    controls["cab_and_mic"] = {"real_value": cab_idx}
    controls["output"] = {"real_value": float(settings.get("Output", 12.0))}
    controls["prefx_power"] = {"real_value": True}
    controls["postfx_power"] = {"real_value": True}

    if amp_idx == 4:  # Showtime '64
        controls["showtime_volume"] = {"real_value": float(settings.get("Volume", 3.6))}
        controls["showtime_treble"] = {"real_value": float(settings.get("Treble", 6.2))}
        controls["showtime_middle"] = {"real_value": float(settings.get("Middle", 4.2))}
        controls["showtime_bass"] = {"real_value": float(settings.get("Bass", 4.6))}
        controls["showtime_bright"] = {"real_value": bool(settings.get("Bright", True))}
    elif amp_idx == 0:  # Dream '65
        controls["dream_volume"] = {"real_value": float(settings.get("Volume", 4.0))}
        controls["dream_treble"] = {"real_value": float(settings.get("Treble", 5.6))}
        controls["dream_bass"] = {"real_value": float(settings.get("Bass", 4.8))}
        controls["dream_bright"] = {"real_value": bool(settings.get("Bright", False))}
        controls["dream_reverb_enable"] = {"real_value": True}
        controls["dream_reverb"] = {"real_value": float(settings.get("Reverb", 2.4))}
    elif amp_idx == 1:  # Enigmatic '82
        controls["enigmatic_volume"] = {"real_value": float(settings.get("Volume", 5.0))}
        controls["enigmatic_treble"] = {"real_value": float(settings.get("Treble", 5.0))}
        controls["enigmatic_middle"] = {"real_value": float(settings.get("Middle", 7.0))}
        controls["enigmatic_bass"] = {"real_value": float(settings.get("Bass", 4.4))}
        controls["enigmatic_presence"] = {"real_value": float(settings.get("Presence", 4.2))}
        controls["enigmatic_master_gain"] = {"real_value": float(settings.get("Master", 7.8))}
        controls["enigmatic_bright_enable"] = {"real_value": bool(settings.get("Bright", False))}
        controls["enigmatic_channel"] = {"real_value": 1}
        controls["enigmatic_tone_stack_type"] = {"real_value": 0}
        controls["enigmatic_tone_stack_eq"] = {"real_value": 0}
        controls["enigmatic_overdrive_enable"] = {"real_value": False}

    out_dir = os.path.join(PARADISE_DIR, folder_name)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{title}.json")
    with open(out_path, "w") as f:
        json.dump(preset, f, indent=4)
    print(f"✓ Compiled UADx Paradise: '{title}' -> {out_path}")
    return out_path

def compile_all():
    print("==================================================")
    print("Compiling 3-Amp Parallel Mayer Trinity Presets")
    print("==================================================")

    # 1. Base Paradise Template
    if not os.path.exists(PARADISE_TEMPLATE):
        raise FileNotFoundError(f"Missing Paradise base template: {PARADISE_TEMPLATE}")
    with open(PARADISE_TEMPLATE, "r") as f:
        paradise_base = json.load(f)

    # 2. UADx Paradise Presets (3 Amps - Calibrated for Parity & Distinct Spectrum)
    # Amp 1: Showtime '64 (SSS Clean Glass Anchor)
    compile_paradise_amp_preset(
        base_json=paradise_base,
        amp_idx=4,
        folder_name="Showtime '64",
        cab_idx=29, # 2x12 Showman
        title="Toneprint - Mayer Trinity - Amp 1 (Showtime SSS Clean)",
        settings={"Volume": 3.6, "Treble": 6.2, "Middle": 4.2, "Bass": 4.6, "Bright": True, "Output": 12.0}
    )

    # Amp 2: Dream '65 (1964 Blackface Reverb Bloom)
    compile_paradise_amp_preset(
        base_json=paradise_base,
        amp_idx=0,
        folder_name="Dream '65",
        cab_idx=29, # 1x12 EV12
        title="Toneprint - Mayer Trinity - Amp 2 (Dream 65 Bloom)",
        settings={"Volume": 4.0, "Treble": 5.6, "Bass": 4.8, "Reverb": 2.4, "Bright": False, "Output": 12.0}
    )

    # Amp 3: Enigmatic '82 (Dumble ODS Vocal Lead Engine)
    compile_paradise_amp_preset(
        base_json=paradise_base,
        amp_idx=1,
        folder_name="Enigmatic '82",
        cab_idx=2, # 2x12 Boutique D65
        title="Toneprint - Mayer Trinity - Amp 3 (Enigmatic 82 Lead)",
        settings={"Volume": 5.0, "Treble": 5.0, "Middle": 7.0, "Bass": 4.4, "Presence": 4.2, "Master": 7.8, "Bright": False, "Output": 12.0}
    )

    # 3. Nembrini NA Clon Minotaur
    os.makedirs(CLON_DIR, exist_ok=True)
    clon_path = os.path.join(CLON_DIR, "Toneprint - Mayer Trinity - Klon Centaur.xml")
    clon_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<ClonMinotaur version="1.0.5" lastUIWidth="667" lastUIHeight="467" CurrentPreset="{clon_path}">
  <PARAM id="Gain" value="2.2"/>
  <PARAM id="Output" value="6.1"/>
  <PARAM id="Treble" value="4.6"/>
  <PARAM id="power" value="1.0"/>
</ClonMinotaur>
"""
    with open(clon_path, "w") as f:
        f.write(clon_xml)
    print(f"✓ Compiled Nembrini Clon: 'Toneprint - Mayer Trinity - Klon Centaur' -> {clon_path}")

    # 4. Kuassa Efektor Blues Barker (Marshall Bluesbreaker)
    os.makedirs(BARKER_DIR, exist_ok=True)
    barker_path = os.path.join(BARKER_DIR, "Toneprint - Mayer Trinity - Blues Barker.kebbp")
    barker_xml = """<?xml version="1.0" encoding="UTF-8"?>

<kuassaPatch version="1.0">
  <DeviceName>Efektor BluesBarker</DeviceName>
  <Properties deviceProductID="com.kuassa.EfektorBluesBarker" deviceVersion="1.0.0" presetVersion="1.0">
    <Value property="onBypass" type="boolean">true</Value>
    <Value property="inputVol" type="number">0.50000</Value>
    <Value property="type" type="number">0</Value>
    <Value property="gain" type="number">0.28600</Value>
    <Value property="tone" type="number">0.55400</Value>
    <Value property="level" type="number">0.33300</Value>
    <Value property="dryWet" type="number">1.00000</Value>
    <Value property="oversampling" type="number">0</Value>
  </Properties>
</kuassaPatch>
"""
    with open(barker_path, "w") as f:
        f.write(barker_xml)
    print(f"✓ Compiled Kuassa Blues Barker: 'Toneprint - Mayer Trinity - Blues Barker' -> {barker_path}")

    # 5. Kuassa Efektor Blues River (Boss BD-2 Keeley Phat Mod)
    os.makedirs(RIVER_DIR, exist_ok=True)
    river_path = os.path.join(RIVER_DIR, "Toneprint - Mayer Trinity - Blues River.kebrp")
    river_xml = """<?xml version="1.0" encoding="UTF-8"?>

<kuassaPatch version="1.0">
  <DeviceName>Efektor BluesRiver</DeviceName>
  <Properties deviceProductID="com.kuassa.EfektorBluesRiver" deviceVersion="1.0.0" presetVersion="1.0">
    <Value property="onBypass" type="boolean">true</Value>
    <Value property="inputVol" type="number">0.50000</Value>
    <Value property="type" type="number">3</Value>
    <Value property="gain" type="number">0.30000</Value>
    <Value property="tone" type="number">0.50000</Value>
    <Value property="level" type="number">0.22000</Value>
    <Value property="dryWet" type="number">1.00000</Value>
    <Value property="oversampling" type="number">0</Value>
  </Properties>
</kuassaPatch>
"""
    with open(river_path, "w") as f:
        f.write(river_xml)
    print(f"✓ Compiled Kuassa Blues River: 'Toneprint - Mayer Trinity - Blues River' -> {river_path}")

    # 6. Nembrini NA 808 (TS-10 / TS-808)
    os.makedirs(NA808_DIR, exist_ok=True)
    na808_path = os.path.join(NA808_DIR, "Toneprint - Mayer Trinity - NA 808.xml")
    na808_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<NA808 lastUIWidth="536" lastUIHeight="605" CurrentPreset="{na808_path}"
       version="1.0.6">
  <PARAM id="Drive" value="2.0"/>
  <PARAM id="Level" value="4.1"/>
  <PARAM id="Tone" value="3.9"/>
  <PARAM id="power" value="1.0"/>
</NA808>
"""
    with open(na808_path, "w") as f:
        f.write(na808_xml)
    print(f"✓ Compiled Nembrini NA 808: 'Toneprint - Mayer Trinity - NA 808' -> {na808_path}")

    # 7. UADx LA-2A Silver
    if os.path.exists(LA2A_BASE):
        with open(LA2A_BASE, "r") as f:
            base_la2a = json.load(f)
        base_la2a["name"] = "Toneprint - Mayer Trinity - Bus LA-2A"
        base_la2a["uid"] = uuid.uuid4().hex
        chunk_bytes = bytearray(base64.b64decode(base_la2a["chunk"]))
        struct.pack_into("f", chunk_bytes, 10 * 4, 0.29)  # Peak Reduction 29.0%
        struct.pack_into("f", chunk_bytes, 11 * 4, 0.24)  # Gain 24.0%
        struct.pack_into("f", chunk_bytes, 13 * 4, 1.0)   # Compress Mode (1.0)
        base_la2a["chunk"] = base64.b64encode(chunk_bytes).decode("ascii")
        la2a_path = os.path.join(LA2A_DIR, "Toneprint - Mayer Trinity - Bus LA-2A.json")
        with open(la2a_path, "w") as f:
            json.dump(base_la2a, f, indent=4)
        print(f"✓ Compiled UADx LA-2A: 'Toneprint - Mayer Trinity - Bus LA-2A' -> {la2a_path}")

    # 8. UADx Hitsville Reverb Chambers (Tuned Room: Decay 2.0, Dist Min, Mix 100%)
    if os.path.exists(HITSVILLE_BASE):
        with open(HITSVILLE_BASE, "r") as f:
            base_hits = json.load(f)
        base_hits["name"] = "Toneprint - Mayer Trinity - Bus Hitsville"
        base_hits["uid"] = uuid.uuid4().hex
        chunk_bytes = bytearray(base64.b64decode(base_hits["chunk"]))
        struct.pack_into("f", chunk_bytes, 20 * 4, 0.195)  # Decay 2.0
        struct.pack_into("f", chunk_bytes, 21 * 4, 1.0)    # Mix 100% (Wet Return)
        struct.pack_into("f", chunk_bytes, 22 * 4, 1.0)    # Power ON
        base_hits["chunk"] = base64.b64encode(chunk_bytes).decode("ascii")
        hits_path = os.path.join(HITSVILLE_DIR, "Toneprint - Mayer Trinity - Bus Hitsville.json")
        with open(hits_path, "w") as f:
            json.dump(base_hits, f, indent=4)
        print(f"✓ Compiled UADx Hitsville: 'Toneprint - Mayer Trinity - Bus Hitsville' -> {hits_path}")

    print("==================================================")
    print("Mayer Trinity Preset Compilation Finished Successfully!")
    print("==================================================")

if __name__ == "__main__":
    compile_all()
