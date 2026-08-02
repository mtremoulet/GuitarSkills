#!/usr/bin/env python3
"""
compile_dual_rig_presets.py

Dedicated preset generator for Dual-Amp Parallel Rigs.
Reads dual-amp toneprint markdown files (with dual_rig: true, amp_a, amp_b) and compiles:
  1. Amp A preset: Toneprint - [Preset Name] - Amp A ([Model])
  2. Amp B preset: Toneprint - [Preset Name] - Amp B ([Model])
  3. Shared Bus FX presets: Toneprint - [Preset Name] - Bus LA-2A / Bus Hitsville

Usage:
  python3 scripts/compile_dual_rig_presets.py [--file tones/path/to/dual-rig.md]
"""

import os
import sys
import re
import json
import uuid
import base64
import struct
import argparse

TONES_DIR = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"
BASE_UAD_PRESETS_DIR = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins"
PARADISE_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_paradise_guitar_studio")
PARADISE_TEMPLATE = os.path.join(PARADISE_DIR, "Non-Toneprints", "Boutique Warm Clean - Enigmatic.json")

LA2A_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_teletronix_la-2a_silver/Mike - Alternative.json")
HITSVILLE_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_hitsville_chambers/Mike Live Strings.json")

AMP_MODEL_INDEXES = {
    "dream": (0, "Dream '65", 29),
    "enigmatic": (1, "Enigmatic '82", 2),
    "lion": (2, "Lion '68", 2),
    "ruby": (3, "Ruby '63", 1),
    "showtime": (4, "Showtime '64", 29),
    "woodrow": (5, "Woodrow '55", 2)
}

def parse_yaml_frontmatter(content):
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    body = content[match.end():]
    
    lines = yaml_text.splitlines()
    parsed_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith('"') and val.endswith('"'): val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"): val = val[1:-1]
            
            if val == "": val = None
            elif isinstance(val, str) and val.lower() == "true": val = True
            elif isinstance(val, str) and val.lower() == "false": val = False
            else:
                try:
                    if "." in str(val): val = float(val)
                    else: val = int(val)
                except ValueError:
                    pass
            parsed_lines.append((indent, key, val))

    def build_tree(start_idx, parent_indent):
        result = {}
        idx = start_idx
        while idx < len(parsed_lines):
            indent, key, val = parsed_lines[idx]
            if indent <= parent_indent:
                break
            
            next_idx = idx + 1
            has_children = False
            if next_idx < len(parsed_lines):
                next_indent, _, _ = parsed_lines[next_idx]
                if next_indent > indent:
                    has_children = True
            
            if has_children:
                child_dict, next_idx = build_tree(next_idx, indent)
                result[key] = child_dict
                idx = next_idx
            else:
                result[key] = val
                idx += 1
        return result, idx

    tree, _ = build_tree(0, -1)
    return tree, body


def get_amp_info(model_str):
    ms = str(model_str).lower()
    for key, info in AMP_MODEL_INDEXES.items():
        if key in ms:
            return key, info[0], info[1], info[2]
    return "dream", 0, "Dream '65", 29


def build_paradise_json(base_preset, amp_info, amp_block, preset_title):
    key_name, amp_idx, folder_name, default_cab_idx = amp_info
    preset_data_json = json.loads(json.dumps(base_preset))
    preset_data_json["name"] = preset_title
    preset_data_json["uid"] = uuid.uuid4().hex
    
    controls = preset_data_json["chunk"]["controls"]
    controls["amp"] = {"real_value": amp_idx}
    controls["cab_and_mic"] = {"real_value": default_cab_idx}
    
    amp_settings = amp_block.get("amp_settings", {})
    if isinstance(amp_settings, dict):
        vol = amp_settings.get("Volume")
        vol_mic = amp_settings.get("Volume (Mic)")
        treble = amp_settings.get("Treble")
        mid = amp_settings.get("Middle")
        bass = amp_settings.get("Bass")
        presence = amp_settings.get("Presence")
        master = amp_settings.get("Master")
        tone_cut = amp_settings.get("Tone Cut")
        bright = amp_settings.get("Bright")
        cut_sw = amp_settings.get("Cut")
        out_gain = amp_settings.get("Output Gain") or amp_settings.get("Output") or amp_settings.get("output_gain")
        if out_gain is not None:
            controls["output"] = {"real_value": float(out_gain)}

        if key_name == "dream":
            if vol is not None: controls["dream_volume"] = {"real_value": float(vol)}
            if treble is not None: controls["dream_treble"] = {"real_value": float(treble)}
            if bass is not None: controls["dream_bass"] = {"real_value": float(bass)}
            if bright is not None: controls["dream_bright"] = {"real_value": bool(bright)}
            controls["dream_reverb_enable"] = {"real_value": True}
            controls["dream_reverb"] = {"real_value": float(amp_settings.get("Reverb", 0.0))}
        elif key_name == "enigmatic":
            if vol is not None: controls["enigmatic_volume"] = {"real_value": float(vol)}
            if treble is not None: controls["enigmatic_treble"] = {"real_value": float(treble)}
            if mid is not None: controls["enigmatic_middle"] = {"real_value": float(mid)}
            if bass is not None: controls["enigmatic_bass"] = {"real_value": float(bass)}
            if presence is not None: controls["enigmatic_presence"] = {"real_value": float(presence)}
            if master is not None: controls["enigmatic_master_gain"] = {"real_value": float(master)}
            if bright is not None: controls["enigmatic_bright_enable"] = {"real_value": bool(bright)}
            controls["enigmatic_channel"] = {"real_value": 1}
            controls["enigmatic_tone_stack_type"] = {"real_value": 0}
            controls["enigmatic_tone_stack_eq"] = {"real_value": 0}
            controls["enigmatic_overdrive_enable"] = {"real_value": False}
        elif key_name == "ruby":
            if vol is not None: controls["ruby_volume"] = {"real_value": float(vol)}
            if treble is not None: controls["ruby_treble"] = {"real_value": float(treble)}
            if bass is not None: controls["ruby_bass"] = {"real_value": float(bass)}
            if tone_cut is not None: controls["ruby_cut"] = {"real_value": float(tone_cut)}
            controls["ruby_channel"] = {"real_value": 2}
            if cut_sw is not None: controls["ruby_tone_cut"] = {"real_value": 5.0 if cut_sw else 0.0}
        elif key_name == "woodrow":
            if vol is not None: controls["woodrow_inst_volume"] = {"real_value": float(vol)}
            if vol_mic is not None: controls["woodrow_mic_volume"] = {"real_value": float(vol_mic)}
            if treble is not None: controls["woodrow_tone"] = {"real_value": float(treble)}
            if "Boost" in amp_settings: controls["woodrow_boost_enable"] = {"real_value": bool(amp_settings["Boost"])}
        elif key_name == "lion":
            vol1 = amp_settings.get("Volume I (Bite)") or amp_settings.get("Volume 1") or amp_settings.get("Volume I")
            vol2 = amp_settings.get("Volume II (Body)") or amp_settings.get("Volume 2") or amp_settings.get("Volume II")
            if vol1 is not None: controls["lion_volume_1"] = {"real_value": float(vol1)}
            if vol2 is not None: controls["lion_volume_2"] = {"real_value": float(vol2)}
            if treble is not None: controls["lion_treble"] = {"real_value": float(treble)}
            if mid is not None: controls["lion_middle"] = {"real_value": float(mid)}
            if bass is not None: controls["lion_bass"] = {"real_value": float(bass)}
            if presence is not None: controls["lion_presence"] = {"real_value": float(presence)}
            controls["lion_model"] = {"real_value": 0}
            controls["lion_input_routing"] = {"real_value": 0}

    controls["prefx_power"] = {"real_value": True}
    controls["postfx_power"] = {"real_value": True}

    out_dir = os.path.join(PARADISE_DIR, folder_name)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{preset_title}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data_json, f, indent=4)
    
    print(f"-> Compiled Dual Rig Amp Preset: '{preset_title}' in '{folder_name}'")
    return out_path


def compile_dual_rig_file(filepath, paradise_base):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    frontmatter, _ = parse_yaml_frontmatter(content)
    if not frontmatter.get("dual_rig") and "amp_a" not in frontmatter:
        return False
    
    preset_name = frontmatter.get("preset_name", os.path.splitext(os.path.basename(filepath))[0])
    amp_a = frontmatter.get("amp_a", {})
    amp_b = frontmatter.get("amp_b", {})
    shared_fx = frontmatter.get("shared_fx", {})
    
    print(f"\n==================================================")
    print(f"COMPILING DUAL-AMP RIG PRESETS: '{preset_name}'")
    print(f"==================================================")

    # 1. Compile Amp A Preset
    if amp_a:
        amp_a_model = amp_a.get("model", "Dream '65")
        amp_a_info = get_amp_info(amp_a_model)
        title_a = f"Toneprint - {preset_name} - Amp A ({amp_a_info[2]})"
        build_paradise_json(paradise_base, amp_a_info, amp_a, title_a)

    # 2. Compile Amp B Preset
    if amp_b:
        amp_b_model = amp_b.get("model", "Ruby '63")
        amp_b_info = get_amp_info(amp_b_model)
        title_b = f"Toneprint - {preset_name} - Amp B ({amp_b_info[2]})"
        build_paradise_json(paradise_base, amp_b_info, amp_b, title_b)

    # 3. Shared Bus LA-2A
    if shared_fx and isinstance(shared_fx, dict):
        la2a_info = shared_fx.get("la2a")
        if la2a_info and os.path.exists(LA2A_BASE):
            with open(LA2A_BASE, "r") as f: base_la2a = json.load(f)
            title_la2a = f"Toneprint - {preset_name} - Bus LA-2A"
            base_la2a["name"] = title_la2a
            base_la2a["uid"] = uuid.uuid4().hex
            
            chunk_bytes = bytearray(base64.b64decode(base_la2a["chunk"]))
            if "peak_reduction" in la2a_info:
                val_scaled = float(la2a_info["peak_reduction"]) / 100.0
                struct.pack_into("f", chunk_bytes, 10 * 4, val_scaled)
            if "gain" in la2a_info:
                val_scaled = float(la2a_info["gain"]) / 100.0
                struct.pack_into("f", chunk_bytes, 11 * 4, val_scaled)
            base_la2a["chunk"] = base64.b64encode(chunk_bytes).decode("ascii")
            
            la2a_dir = os.path.dirname(LA2A_BASE)
            out_la2a = os.path.join(la2a_dir, f"{title_la2a}.json")
            with open(out_la2a, "w") as f: json.dump(base_la2a, f, indent=4)
            print(f"-> Compiled Dual Rig Bus Preset: '{title_la2a}'")

        hits_info = shared_fx.get("hitsville")
        if hits_info and os.path.exists(HITSVILLE_BASE):
            with open(HITSVILLE_BASE, "r") as f: base_hits = json.load(f)
            title_hits = f"Toneprint - {preset_name} - Bus Hitsville"
            base_hits["name"] = title_hits
            base_hits["uid"] = uuid.uuid4().hex
            
            chunk_bytes = bytearray(base64.b64decode(base_hits["chunk"]))
            if "decay" in hits_info:
                struct.pack_into("f", chunk_bytes, 20 * 4, float(hits_info["decay"]) / 10.0)
            if "mix" in hits_info:
                mix_val = float(hits_info["mix"])
                val_scaled = mix_val / 100.0 if mix_val > 1.0 else mix_val
                struct.pack_into("f", chunk_bytes, 21 * 4, val_scaled)
            # Force Power Switch to 1.0 (Power ON)
            struct.pack_into("f", chunk_bytes, 22 * 4, 1.0)
            base_hits["chunk"] = base64.b64encode(chunk_bytes).decode("ascii")
            
            hits_dir = os.path.dirname(HITSVILLE_BASE)
            out_hits = os.path.join(hits_dir, f"{title_hits}.json")
            with open(out_hits, "w") as f: json.dump(base_hits, f, indent=4)
            print(f"-> Compiled Dual Rig Bus Preset: '{title_hits}'")

    # 4. Stompbox / Drive Pedal Presets
    stomp_dict = {}
    stomp_dict.update(frontmatter.get("preset_data", {}))
    if isinstance(amp_a, dict): stomp_dict.update(amp_a)
    if isinstance(amp_b, dict): stomp_dict.update(amp_b)
    if isinstance(shared_fx, dict): stomp_dict.update(shared_fx)

    # Nembrini Clon Minotaur
    if "clon_minotaur" in stomp_dict:
        c_info = stomp_dict["clon_minotaur"]
        if isinstance(c_info, dict):
            c_dir = "/Users/miketremoulet/Documents/Nembrini Audio/NA Clon Minotaur"
            os.makedirs(c_dir, exist_ok=True)
            c_title = f"Toneprint - {preset_name}"
            c_path = os.path.join(c_dir, f"{c_title}.xml")
            c_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<ClonMinotaur version="1.0.0">
  <PARAM id="Gain" value="{float(c_info.get('gain', 6.0))}"/>
  <PARAM id="Treble" value="{float(c_info.get('treble', 4.5))}"/>
  <PARAM id="Output" value="{float(c_info.get('output', 4.5))}"/>
  <PARAM id="power" value="1.0"/>
</ClonMinotaur>
"""
            with open(c_path, "w") as f: f.write(c_xml)
            print(f"-> Compiled Nembrini Clon Minotaur Preset: '{c_title}'")

    # Nembrini 808
    if "nembrini_808" in stomp_dict or "808" in stomp_dict:
        n_info = stomp_dict.get("nembrini_808") or stomp_dict.get("808")
        if isinstance(n_info, dict):
            n_dir = "/Users/miketremoulet/Documents/Nembrini Audio/NA 808"
            os.makedirs(n_dir, exist_ok=True)
            n_title = f"Toneprint - {preset_name}"
            n_path = os.path.join(n_dir, f"{n_title}.xml")
            n_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Nembrini808 version="1.0.0">
  <PARAM id="Drive" value="{float(n_info.get('drive', 5.4))}"/>
  <PARAM id="Tone" value="{float(n_info.get('tone', 5.0))}"/>
  <PARAM id="Level" value="{float(n_info.get('level', 3.5))}"/>
  <PARAM id="power" value="1.0"/>
</Nembrini808>
"""
            with open(n_path, "w") as f: f.write(n_xml)
            print(f"-> Compiled Nembrini 808 Preset: '{n_title}'")

    # Kuassa Efektor Blues Barker
    if "kuassa_blues_barker" in stomp_dict:
        kb_info = stomp_dict["kuassa_blues_barker"]
        if isinstance(kb_info, dict):
            kb_dir = "/Users/miketremoulet/Music/Kuassa/Presets/EfektorBluesBarker"
            os.makedirs(kb_dir, exist_ok=True)
            kb_title = f"Toneprint - {preset_name}"
            kb_path = os.path.join(kb_dir, f"{kb_title}.kebbp")
            g_scaled = float(kb_info.get("gain", 3.5)) / 10.0
            t_scaled = float(kb_info.get("tone", 5.0)) / 10.0
            l_scaled = float(kb_info.get("level", 2.75)) / 10.0
            kb_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<kuassaPatch version="1.0">
  <DeviceName>Efektor BluesBarker</DeviceName>
  <Properties deviceProductID="com.kuassa.EfektorBluesBarker" deviceVersion="1.0.0" presetVersion="1.0">
    <Value property="onBypass" type="boolean">true</Value>
    <Value property="inputVol" type="number">0.50000</Value>
    <Value property="type" type="number">0</Value>
    <Value property="gain" type="number">{g_scaled:.5f}</Value>
    <Value property="tone" type="number">{t_scaled:.5f}</Value>
    <Value property="level" type="number">{l_scaled:.5f}</Value>
    <Value property="dryWet" type="number">1.00000</Value>
    <Value property="oversampling" type="number">0</Value>
  </Properties>
</kuassaPatch>
"""
            with open(kb_path, "w") as f: f.write(kb_xml)
            print(f"-> Compiled Kuassa Efektor Blues Barker Preset: '{kb_title}'")

    # Kuassa Efektor Blues River
    if "kuassa_blues_river" in stomp_dict:
        kr_info = stomp_dict["kuassa_blues_river"]
        if isinstance(kr_info, dict):
            kr_dir = "/Users/miketremoulet/Music/Kuassa/Presets/EfektorBluesRiver"
            os.makedirs(kr_dir, exist_ok=True)
            kr_title = f"Toneprint - {preset_name}"
            kr_path = os.path.join(kr_dir, f"{kr_title}.kebrp")
            g_scaled = float(kr_info.get("gain", 3.0)) / 10.0
            t_scaled = float(kr_info.get("tone", 5.0)) / 10.0
            l_scaled = float(kr_info.get("level", 2.2)) / 10.0
            kr_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<kuassaPatch version="1.0">
  <DeviceName>Efektor BluesRiver</DeviceName>
  <Properties deviceProductID="com.kuassa.EfektorBluesRiver" deviceVersion="1.0.0" presetVersion="1.0">
    <Value property="onBypass" type="boolean">true</Value>
    <Value property="inputVol" type="number">0.50000</Value>
    <Value property="type" type="number">0</Value>
    <Value property="gain" type="number">{g_scaled:.5f}</Value>
    <Value property="tone" type="number">{t_scaled:.5f}</Value>
    <Value property="level" type="number">{l_scaled:.5f}</Value>
    <Value property="dryWet" type="number">1.00000</Value>
    <Value property="oversampling" type="number">0</Value>
  </Properties>
</kuassaPatch>
"""
            with open(kr_path, "w") as f: f.write(kr_xml)
            print(f"-> Compiled Kuassa Efektor Blues River Preset: '{kr_title}'")

    return True


def main():
    parser = argparse.ArgumentParser(description="Dedicated Dual-Amp Preset Generator")
    parser.add_argument("--file", help="Path to specific dual-amp tone file", default=None)
    args = parser.parse_args()

    if not os.path.exists(PARADISE_TEMPLATE):
        print(f"Error: Paradise base template not found at '{PARADISE_TEMPLATE}'")
        sys.exit(1)

    with open(PARADISE_TEMPLATE, "r") as f:
        paradise_base = json.load(f)

    if args.file:
        filepaths = [args.file]
    else:
        filepaths = []
        for root, _, files in os.walk(TONES_DIR):
            for file in files:
                if file.endswith(".md") and file != "INDEX.md":
                    filepaths.append(os.path.join(root, file))

    count = 0
    for fp in filepaths:
        if compile_dual_rig_file(fp, paradise_base):
            count += 1
            
    print(f"\n==================================================")
    print(f"Dual Rig Preset Generation Complete! Processed {count} dual-amp toneprints.")
    print(f"==================================================")

if __name__ == "__main__":
    main()
