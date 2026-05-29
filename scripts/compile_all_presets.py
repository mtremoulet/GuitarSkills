#!/usr/bin/env python3
import os
import json
import re
import uuid
import xml.etree.ElementTree as ET
import base64
import struct

# Directories & Path Configurations
TONES_DIR = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"

# Neural DSP Paths
NEURAL_TEMPLATE = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/User/Telecaster Tones.xml"
NEURAL_TEMPLATE_ALT = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Default.xml"
NEURAL_OUTPUT_DIR = "/Library/Audio/Presets/Neural DSP/Archetype Cory Wong X/Toneprints"

# Universal Audio Paths
BASE_UAD_PRESETS_DIR = "/Users/miketremoulet/Documents/Universal Audio/Presets/Plug-Ins"
PARADISE_DIR = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_paradise_guitar_studio")
PARADISE_TEMPLATE = os.path.join(PARADISE_DIR, "Boutique Warm Clean - Enigmatic.json")

LA2A_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_teletronix_la-2a_silver/Mike - Alternative.json")
HITSVILLE_BASE = os.path.join(BASE_UAD_PRESETS_DIR, "uaudio_hitsville_chambers/Mike Live Strings.json")

# Logic Pro Native Paths
LOGIC_EQ_BASE = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Channel EQ/FlatEQ.pst"
LOGIC_COMP_BASE_ALT = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Compressor/CompThreshNeg35.pst"
LOGIC_COMP_BASE_DEFAULT = "/Users/miketremoulet/Music/Audio Music Apps/Plug-In Settings/Compressor/DefaultComp.pst"
LOGIC_COMP_BASE = LOGIC_COMP_BASE_ALT if os.path.exists(LOGIC_COMP_BASE_ALT) else LOGIC_COMP_BASE_DEFAULT

# MixWave Paths
MIXWAVE_TEMPLATE = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/User/ToneprintTemplate.xml"
MIXWAVE_TEMPLATE_ALT = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/User/Mike's Two Rocks.xml"
MIXWAVE_TEMPLATE_FACTORY = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/Factory/LUSH CLEAN.xml"
MIXWAVE_OUTPUT_DIR = "/Library/Audio/Presets/MixWave/MixWave Two-Rock Bloomfield Drive/Presets/User"

# Custom Binary Parameter Replacer for Neural DSP (TLV format)
def replace_binary_parameter(data, param_name, new_val_str):
    search_bytes = param_name.encode("utf-8") + b"\x00\x01"
    idx = data.find(search_bytes)
    if idx == -1:
        return data
    
    length_byte_idx = idx + len(search_bytes)
    old_length = data[length_byte_idx]
    
    replace_start = length_byte_idx
    replace_end = length_byte_idx + 1 + old_length
    
    new_val_bytes = new_val_str.encode("utf-8")
    new_length = len(new_val_bytes) + 2
    new_block = bytes([new_length, 0x05]) + new_val_bytes + b"\x00"
    
    return data[:replace_start] + new_block + data[replace_end:]

# Robust Standard Library YAML Frontmatter Parser
def parse_yaml_frontmatter(content):
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    body = content[match.end():]
    
    data = {}
    lines = yaml_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
            
        indent = len(line) - len(line.lstrip())
        if indent > 0:
            i += 1
            continue
            
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            
            # If value is empty, check for nested block
            if not val:
                nested_dict = {}
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    if not next_line.strip() or next_line.strip().startswith("#"):
                        i += 1
                        continue
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent == 0:
                        break
                    
                    if ":" in next_line:
                        nk, _, nv = next_line.partition(":")
                        nk = nk.strip()
                        nv = nv.strip()
                        
                        # Strip quotes
                        if nv.startswith('"') and nv.endswith('"'):
                            nv = nv[1:-1]
                        elif nv.startswith("'") and nv.endswith("'"):
                            nv = nv[1:-1]
                            
                        # Parse types
                        if nv.lower() == "true":
                            nv = True
                        elif nv.lower() == "false":
                            nv = False
                        else:
                            try:
                                if "." in nv:
                                    nv = float(nv)
                                else:
                                    nv = int(nv)
                            except ValueError:
                                pass
                        nested_dict[nk] = nv
                    i += 1
                data[key] = nested_dict
                continue
            else:
                # Strip quotes
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                elif val.startswith("'") and val.endswith("'"):
                    val = val[1:-1]
                    
                # Parse types
                if val.lower() == "true":
                    val = True
                elif val.lower() == "false":
                    val = False
                data[key] = val
        i += 1
    return data, body

# Robust Markdown Parameter Extractor
def find_numeric_parameter(content, param_names):
    for name in param_names:
        # Match standard decimals like 5.5, 3.0, -1.5, −1.5 (with Unicode minus)
        # Put the hyphen at the end of the character class to prevent range interpretation
        pattern = r"\|\s*" + re.escape(name) + r"\s*\|\s*(?:\*\*)?([~0-9.+−-]+)(?:\*\*)?(?:\s*%)?\s*\|"
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            val_str = match.group(1).replace("−", "-").replace("~", "").strip()
            try:
                val = float(val_str)
                # Check if this line contains a % symbol (percentages are scaled to 0.0 - 1.0)
                full_line = content[max(0, match.start()-10) : min(len(content), match.end()+25)]
                if "%" in full_line:
                    return val / 100.0
                return val
            except ValueError:
                pass
    return None

def find_boolean_parameter(content, param_names):
    for name in param_names:
        pattern = r"\|\s*" + re.escape(name) + r"\s*\|\s*(?:\*\*)?([A-Za-z/ ]+)(?:\*\*)?\s*\|"
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            val = match.group(1).strip().upper()
            if val in ["ON", "ACTIVE", "BRIGHT", "YES", "TRUE"]:
                return True
            if val in ["OFF", "NORMAL", "BYPASSED", "NO", "FALSE"]:
                return False
    return None

# Dynamic Neural DSP Parser & Compiler
def compile_neural_toneprint(filepath, base_data, output_name, frontmatter):
    with open(filepath, "r") as f:
        content = f.read()

    settings = {}
    settings["name"] = output_name
    
    # 1. Parse Compressor (The 4th Position Compressor)
    comp_active = find_boolean_parameter(content, ["The 4th Position Compressor", "Compressor Active", "Compressor"])
    if comp_active is not None:
        settings["compressorActive"] = "true" if comp_active else "false"
        
    for key in ["Blend", "Tone", "Compression", "Volume"]:
        val = find_numeric_parameter(content, [key])
        if val is not None:
            settings["compressor" + key] = f"{val:.2f}"

    # 2. Parse Amp Knobs (The Amp Snob / Amp 3)
    settings["selectedAmp"] = "2"  # Amp 3 (index 2)
    settings["selectedCab"] = "2"  # Snob 2x12 Cab (index 2)
    settings["ampCabLinkedState"] = "false"
    
    knobs = {
        "snobBass": ["Bass"],
        "snobMid": ["Middle", "Mids"],
        "snobTreble": ["Treble"],
        "snobPresence": ["Presence"],
        "snobMaster": ["Master"],
        "snobVolume": ["Volume (Gain)", "Volume"],
        "snobOutputLevel": ["Output"]
    }
    
    for param, names in knobs.items():
        val = find_numeric_parameter(content, names)
        if val is not None:
            settings[param] = f"{val:.2f}"
            
    drive = find_boolean_parameter(content, ["Drive Switch", "Drive"])
    if drive is not None:
        settings["snobDrive"] = "true" if drive else "false"
        
    bright = find_boolean_parameter(content, ["Bright Switch", "Bright"])
    if bright is not None:
        settings["snobBright"] = "true" if bright else "false"

    # 3. Parse Cabinet settings
    pos = find_numeric_parameter(content, ["Position L", "Position"])
    if pos is not None: settings["leftCabPosition"] = f"{pos:.2f}"
    
    dist = find_numeric_parameter(content, ["Distance L", "Distance"])
    if dist is not None: settings["leftCabDistance"] = f"{dist:.2f}"
    
    room = find_numeric_parameter(content, ["Room Send L", "Room Send"])
    if room is not None: settings["leftRoomMicLevel"] = f"{room:.1f}"

    settings["leftCabActive"] = "true"
    settings["leftCab0MicType"] = "4"   # Ribbon 121
    settings["rightCabActive"] = "false" # Bypassed

    # 4. Parse EQ Bands (1 to 9)
    eq_active = find_boolean_parameter(content, ["EQ Status", "EQ Active", "snobEQActive"])
    if eq_active is not None:
        settings["snobEQActive"] = "true" if eq_active else "false"
        
    bands = ["65 Hz", "125 Hz", "250 Hz", "500 Hz", "1 kHz", "2 kHz", "4 kHz", "8 kHz", "16 kHz"]
    for i, band in enumerate(bands, 1):
        val = find_numeric_parameter(content, [band])
        if val is not None:
            settings[f"snobEQBand{i}"] = f"{val:.1f}"

    settings["snobEQHpf"] = "20.0"
    settings["snobEQLpf"] = "20000.0"

    # 5. Default bypassed pedals
    for pedal in ["tuberActive", "bigRigActive", "postalActive", "delayActive", "washActive", "chorusActive"]:
        settings[pedal] = "false"

    # Inject overrides from frontmatter (supporting custom studio FX/cabs/etc.)
    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            if isinstance(v, bool):
                settings[k] = "true" if v else "false"
            else:
                settings[k] = str(v)

    # Inject into binary preset
    preset_data = base_data
    for key, val in settings.items():
        preset_data = replace_binary_parameter(preset_data, key, val)
        
    # Save preset
    os.makedirs(NEURAL_OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(NEURAL_OUTPUT_DIR, f"{output_name}.xml")
    with open(out_path, "wb") as f:
        f.write(preset_data)
    print(f"-> Compiled Neural Preset: '{output_name}'")
    return True

# Dynamic UADx Parser & Compiler
def compile_uad_toneprint(filepath, base_preset, output_name, frontmatter):
    with open(filepath, "r") as f:
        content = f.read()
        
    amp_str = frontmatter.get("amp", "")
    
    # Identify target amp type and indexes
    amp_type = None
    amp_index = None
    cab_index = 2 # default open back Boutique D65
    
    if "Dream" in amp_str:
        amp_type = "dream"
        amp_index = 0
        cab_index = 29
    elif "Enigmatic" in amp_str:
        amp_type = "enigmatic"
        amp_index = 1
        cab_index = 2
    elif "Woodrow" in amp_str:
        amp_type = "woodrow"
        amp_index = 5
        cab_index = 2
    elif "Ruby" in amp_str:
        amp_type = "ruby"
        amp_index = 3
        cab_index = 1
    elif "Showtime" in amp_str:
        amp_type = "showtime"
        amp_index = 4
        cab_index = 29
    elif "Lion" in amp_str:
        amp_type = "lion"
        amp_index = 2
        cab_index = 2
        
    if amp_type is None: return

    # Extract common knobs
    vol = find_numeric_parameter(content, ["Volume (Gain)", "Volume", "Volume (Inst)", "inst_volume"])
    vol_mic = find_numeric_parameter(content, ["Volume (Mic)", "mic_volume"])
    treble = find_numeric_parameter(content, ["Treble", "Top Boost Treble", "Tone"])
    mid = find_numeric_parameter(content, ["Middle", "Mids", "Top Boost Mids"])
    bass = find_numeric_parameter(content, ["Bass", "Top Boost Bass"])
    presence = find_numeric_parameter(content, ["Presence"])
    master = find_numeric_parameter(content, ["Master (labeled 6.5)", "Master", "Master volume"])
    tone_cut = find_numeric_parameter(content, ["Tone Cut"])
    
    # Extract switches
    bright = find_boolean_parameter(content, ["Bright Switch", "Bright / Normal", "Bright"])
    boost = find_boolean_parameter(content, ["Boost Button", "Boost Switch", "Boost (Stock)", "Boost"])
    cut_sw = find_boolean_parameter(content, ["Cut Switch", "Cut"])

    # Map settings into Paradise Guitar Studio JSON
    preset_data = json.loads(json.dumps(base_preset)) # deep copy
    preset_data["name"] = f"Toneprint - {output_name}"
    preset_data["uid"] = uuid.uuid4().hex
    
    controls = preset_data["chunk"]["controls"]
    
    # Inject amp and cabinet selection
    controls["amp"] = {"real_value": amp_index}
    controls["cab_and_mic"] = {"real_value": cab_index}
    
    # Inject mapped parameters
    if amp_type == "dream":
        if vol is not None: controls["dream_volume"] = {"real_value": vol}
        if treble is not None: controls["dream_treble"] = {"real_value": treble}
        if bass is not None: controls["dream_bass"] = {"real_value": bass}
        if bright is not None: controls["dream_bright"] = {"real_value": bright}
        if boost is not None: controls["dream_boost_enable"] = {"real_value": boost}
        controls["dream_reverb_enable"] = {"real_value": True}
        controls["dream_reverb"] = {"real_value": 2.5}
    elif amp_type == "enigmatic":
        if vol is not None: controls["enigmatic_volume"] = {"real_value": vol}
        if treble is not None: controls["enigmatic_treble"] = {"real_value": treble}
        if mid is not None: controls["enigmatic_middle"] = {"real_value": mid}
        if bass is not None: controls["enigmatic_bass"] = {"real_value": bass}
        if presence is not None: controls["enigmatic_presence"] = {"real_value": presence}
        if master is not None: controls["enigmatic_master_gain"] = {"real_value": master}
        if bright is not None: controls["enigmatic_bright_enable"] = {"real_value": bright}
        if boost is not None: controls["enigmatic_boost_enable"] = {"real_value": boost}
        controls["enigmatic_model"] = {"real_value": 0}            # Suede
        controls["enigmatic_channel"] = {"real_value": 1}          # NOR
        controls["enigmatic_tone_stack_type"] = {"real_value": 0}  # Skyline
        controls["enigmatic_tone_stack_eq"] = {"real_value": 0}    # Jazz
        controls["enigmatic_overdrive_enable"] = {"real_value": False}
    elif amp_type == "ruby":
        if vol is not None: controls["ruby_volume"] = {"real_value": vol}
        if treble is not None: controls["ruby_treble"] = {"real_value": treble}
        if bass is not None: controls["ruby_bass"] = {"real_value": bass}
        if tone_cut is not None: controls["ruby_tone_cut"] = {"real_value": tone_cut}
        if boost is not None: controls["ruby_boost_enable"] = {"real_value": boost}
        controls["ruby_channel"] = {"real_value": 2} # Brilliant
        controls["ruby_cut"] = {"real_value": 5.0 if cut_sw else 0.0}
    elif amp_type == "woodrow":
        if vol is not None: controls["woodrow_inst_volume"] = {"real_value": vol}
        if vol_mic is not None: controls["woodrow_mic_volume"] = {"real_value": vol_mic}
        if treble is not None: controls["woodrow_tone"] = {"real_value": treble}
        if boost is not None: controls["woodrow_boost_enable"] = {"real_value": boost}
    elif amp_type == "showtime":
        if vol is not None: controls["showtime_volume"] = {"real_value": vol}
        if treble is not None: controls["showtime_treble"] = {"real_value": treble}
        if mid is not None: controls["showtime_middle"] = {"real_value": mid}
        if bass is not None: controls["showtime_bass"] = {"real_value": bass}
        if bright is not None: controls["showtime_bright"] = {"real_value": bright}

    # Bypassed post-amp effects for clean platform comparison (defaults)
    controls["prefx_power"] = {"real_value": False}
    controls["postfx_power"] = {"real_value": False}

    # Inject overrides from frontmatter (supporting 1176, delays, plate reverbs, etc.)
    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            controls[k] = {"real_value": v}

    # Write output JSON preset file
    os.makedirs(PARADISE_DIR, exist_ok=True)
    out_path = os.path.join(PARADISE_DIR, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data, f, indent=4)
        
    print(f"-> Compiled UAD Paradise Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic MixWave Two-Rock Bloomfield Drive XML Parser & Compiler
def compile_mixwave_toneprint(filepath, base_xml_path, output_name, frontmatter):
    with open(filepath, "r") as f:
        content = f.read()

    # Parse XML Template using Standard ElementTree
    tree = ET.parse(base_xml_path)
    root = tree.getroot()

    # Find the variables blocks
    global_vars = root.find("Variables")
    amp_module = root.find(".//Module[@moduleName='Amp']")
    amp_vars = amp_module.find("Variables") if amp_module is not None else None
    cab_module = root.find(".//Module[@moduleName='Cab']")
    cab_vars = cab_module.find("Variables") if cab_module is not None else None
    od_module = root.find(".//Module[@moduleName='Overdrive']")
    od_vars = od_module.find("Variables") if od_module is not None else None

    # Extract amp values from Markdown
    gain = find_numeric_parameter(content, ["Gain"])
    treble = find_numeric_parameter(content, ["Treble"])
    mid = find_numeric_parameter(content, ["Middle", "Mids"])
    bass = find_numeric_parameter(content, ["Bass"])
    presence = find_numeric_parameter(content, ["Presence"])
    master = find_numeric_parameter(content, ["Master"])
    reverb = find_numeric_parameter(content, ["Reverb"])
    vibe = find_numeric_parameter(content, ["Vibe"])

    # Switches
    bright = find_boolean_parameter(content, ["Bright Switch", "Bright"])
    mid_sw = find_boolean_parameter(content, ["Mid Switch", "Mid"])
    deep = find_boolean_parameter(content, ["Deep Switch", "Deep"])
    bypass_sw = find_boolean_parameter(content, ["Tone Stack Bypass"])
    lead_sw = find_boolean_parameter(content, ["Lead Switch", "Lead"])

    # Global Gate & Levels
    gate_val = find_numeric_parameter(content, ["Noise Gate", "Gate Threshold"])
    input_trim = find_numeric_parameter(content, ["Input Trim"])
    output_trim = find_numeric_parameter(content, ["Output Trim"])

    # Map settings to Amp Variables XML attributes
    if amp_vars is not None:
        if gain is not None: amp_vars.set("AmpGain", f"{gain:.3f}")
        if treble is not None: amp_vars.set("AmpTreble", f"{treble:.3f}")
        if mid is not None: amp_vars.set("AmpMiddle", f"{mid:.3f}")
        if bass is not None: amp_vars.set("AmpBass", f"{bass:.3f}")
        if presence is not None: amp_vars.set("AmpPresence", f"{presence:.3f}")
        if master is not None: amp_vars.set("AmpMaster", f"{master:.3f}")
        if reverb is not None: amp_vars.set("AmpReverb", f"{reverb:.3f}")
        
        # Switches: MixWave uses "1" for On, "0" for Off
        if bright is not None: amp_vars.set("AmpBrightOnOff", "1" if bright else "0")
        if mid_sw is not None: amp_vars.set("AmpMidOnOff", "1" if mid_sw else "0")
        if deep is not None: amp_vars.set("AmpDeepOnOff", "1" if deep else "0")
        if bypass_sw is not None: amp_vars.set("AmpToneBypassOnOff", "1" if bypass_sw else "0")
        if lead_sw is not None: amp_vars.set("AmpType", "2" if lead_sw else "1")

    # Map Vibe to Cab 1 Vibe in the cabinet section
    if cab_vars is not None and vibe is not None:
        cab_vars.set("Cab1Vibe", f"{vibe:.3f}")

    # Global Variables
    if global_vars is not None:
        if gate_val is not None:
            global_vars.set("GateOnOff", "1")
            global_vars.set("GateThreshold", f"{gate_val:.3f}")
        if input_trim is not None:
            global_vars.set("InputLevel", f"{input_trim:.3f}")
        if output_trim is not None:
            global_vars.set("OutputLevel", f"{output_trim:.3f}")

    # Inject overrides from frontmatter (pedals, custom mic placements, etc.)
    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            val_str = "1" if isinstance(v, bool) and v else ("0" if isinstance(v, bool) else str(v))
            if k.startswith("Overdrive") and od_vars is not None:
                od_vars.set(k, val_str)
            elif k.startswith("Amp") and amp_vars is not None:
                amp_vars.set(k, val_str)
            elif k.startswith("Cab") and cab_vars is not None:
                cab_vars.set(k, val_str)
            elif global_vars is not None:
                global_vars.set(k, val_str)

    # Save XML preset directly in the user-level folder
    os.makedirs(MIXWAVE_OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(MIXWAVE_OUTPUT_DIR, f"{output_name}.xml")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"-> Compiled MixWave Preset: '{output_name}'")
    return True

# Robust parameter extractor for Compressor that falls back to cell regex if find_numeric_parameter fails
def extract_comp_param(content, keywords):
    val = find_numeric_parameter(content, keywords)
    if val is not None:
        return val
        
    for line in content.split("\n"):
        line_lower = line.lower()
        if any(kw.lower() in line_lower for kw in keywords):
            parts = [p.strip() for p in line.split("|")]
            text_to_search = parts[2] if len(parts) >= 3 else line
            match = re.search(r"([+-]?\d+(?:\.\d+)?)\s*(?:db|ms|:1)?\b", text_to_search.replace("−", "-"), re.IGNORECASE)
            if match:
                return float(match.group(1))
    return None

def extract_freq(text):
    freq_match = re.search(r"(\d+(?:\.\d+)?)\s*(k?Hz)\b", text, re.IGNORECASE)
    if freq_match:
        val = float(freq_match.group(1))
        unit = freq_match.group(2).lower()
        if unit == "khz" or (val < 22.0 and unit == "hz"):
            val *= 1000.0
        return val
    return None

def extract_slope(text):
    slope_match = re.search(r"(\d+)\s*db", text, re.IGNORECASE)
    if slope_match:
        db_val = int(slope_match.group(1))
        mapping = {6: 1.0, 12: 2.0, 18: 3.0, 24: 4.0, 30: 5.0, 36: 6.0, 48: 7.0}
        if db_val in mapping:
            return mapping[db_val]
        return float(db_val // 6)
    return None

def parse_eq_bands(content):
    bands = {i: {"on": None, "freq": None, "gain_or_slope": None, "q": None} for i in range(1, 9)}
    in_eq_section = False
    
    for line in content.split("\n"):
        line_lower = line.lower()
        
        if line.strip().startswith("#"):
            if "channel eq" in line_lower or "surgical shaping" in line_lower:
                in_eq_section = True
                continue
            else:
                in_eq_section = False
                continue
            
        if not in_eq_section:
            continue
            
        if "|" not in line:
            if "high-pass" in line_lower or "hpf" in line_lower or "low cut" in line_lower:
                freq = extract_freq(line)
                slope = extract_slope(line)
                if freq is not None:
                    bands[1]["on"] = 1.0
                    bands[1]["freq"] = freq
                if slope is not None:
                    bands[1]["gain_or_slope"] = slope
            elif "low-pass" in line_lower or "lpf" in line_lower or "high cut" in line_lower or "high-cut" in line_lower:
                freq = extract_freq(line)
                slope = extract_slope(line)
                if freq is not None:
                    bands[8]["on"] = 1.0
                    bands[8]["freq"] = freq
                if slope is not None:
                    bands[8]["gain_or_slope"] = slope
            continue
            
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            continue
            
        first_col = parts[1].lower()
        band_num = None
        if "band 1" in first_col or "low cut" in first_col or "hpf" in first_col or "high-pass" in first_col:
            band_num = 1
        elif "band 2" in first_col or "low shelf" in first_col:
            band_num = 2
        elif "band 3" in first_col or "peak 1" in first_col:
            band_num = 3
        elif "band 4" in first_col or "peak 2" in first_col or ("peak" in first_col and "250 hz" in line_lower):
            band_num = 4
        elif "band 5" in first_col or "peak 3" in first_col:
            band_num = 5
        elif "band 6" in first_col or "peak 4" in first_col:
            band_num = 6
        elif "band 7" in first_col or "high shelf" in first_col:
            band_num = 7
        elif "band 8" in first_col or "high cut" in first_col or "lpf" in first_col or "low-pass" in first_col or "high-cut" in first_col:
            band_num = 8
        elif "peak" in first_col:
            band_num = 3
            
        if band_num is None:
            continue
            
        col_text = " ".join(parts[2:])
        freq = extract_freq(col_text)
        gain_or_slope = None
        q = None
        
        if band_num in [1, 8]:
            gain_or_slope = extract_slope(col_text)
        else:
            gain_match = re.search(r"([+-]?\d+(?:\.\d+)?)\s*db\b", col_text.replace("−", "-"), re.IGNORECASE)
            if gain_match:
                gain_or_slope = float(gain_match.group(1))
                
        q_match = re.search(r"\bq(?:-factor)?(?:\s*:\s*|\s+)(\d+(?:\.\d+)?)\b", col_text, re.IGNORECASE)
        if q_match:
            q = float(q_match.group(1))
            
        bands[band_num]["on"] = 1.0
        if freq is not None:
            bands[band_num]["freq"] = freq
        if gain_or_slope is not None:
            bands[band_num]["gain_or_slope"] = gain_or_slope
        if q is not None:
            bands[band_num]["q"] = q
            
    return bands

# Dynamic UADx Teletronix LA-2A JSON Compiler (Silver / Gray)
def compile_la2a_toneprint(filepath, base_preset_path, output_name, frontmatter):
    with open(filepath, "r") as f:
        content = f.read()

    # Extract Peak Reduction and Gain
    peak_reduction = find_numeric_parameter(content, ["Peak Reduction"])
    gain = find_numeric_parameter(content, ["Gain", "Makeup Gain"])
    mode_compress = find_boolean_parameter(content, ["Compress Mode", "Compress"]) # True = Compress, False = Limit
    
    # If not found in tables, check overrides or skip
    if peak_reduction is None and gain is None:
        return False

    # Load base template JSON
    with open(base_preset_path, "r") as f:
        preset_data = json.load(f)

    # Decode chunk
    chunk_bytes = bytearray(base64.b64decode(preset_data["chunk"]))
    
    # Surgically patch floats
    # Float 10: Gain (0.0 to 1.0)
    if gain is not None:
        val_scaled = gain / 100.0 if gain > 1.0 else gain
        struct.pack_into("f", chunk_bytes, 10 * 4, val_scaled)
    # Float 11: Peak Reduction (0.0 to 1.0)
    if peak_reduction is not None:
        val_scaled = peak_reduction / 100.0 if peak_reduction > 1.0 else peak_reduction
        struct.pack_into("f", chunk_bytes, 11 * 4, val_scaled)
    # Float 13: Mode (1.0 = Compress, 0.0 = Limit)
    if mode_compress is not None:
        struct.pack_into("f", chunk_bytes, 13 * 4, 1.0 if mode_compress else 0.0)

    # Re-encode chunk
    preset_data["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data["name"] = f"Toneprint - {output_name}"
    preset_data["uid"] = uuid.uuid4().hex

    # Write output
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data, f, indent=4)
        
    print(f"-> Compiled UADx LA-2A Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic UADx Hitsville Reverb Chambers JSON Compiler
def compile_hitsville_toneprint(filepath, base_preset_path, output_name, frontmatter):
    with open(filepath, "r") as f:
        content = f.read()

    mix = find_numeric_parameter(content, ["Mix", "Room Mix"])
    pre_delay = find_numeric_parameter(content, ["Pre-Delay"])
    decay = find_numeric_parameter(content, ["Decay"])

    if mix is None and pre_delay is None and decay is None:
        return False

    # Load base template JSON
    with open(base_preset_path, "r") as f:
        preset_data = json.load(f)

    # Decode chunk
    chunk_bytes = bytearray(base64.b64decode(preset_data["chunk"]))

    # Float 21: Mix (0.0 to 1.0)
    if mix is not None:
        val_scaled = mix / 100.0 if mix > 1.0 else mix
        struct.pack_into("f", chunk_bytes, 21 * 4, val_scaled)
    # Float 12: Pre-Delay (ms scaled to 0.0-1.0, e.g. 8ms -> 0.08)
    if pre_delay is not None:
        val_scaled = pre_delay / 100.0
        struct.pack_into("f", chunk_bytes, 12 * 4, val_scaled)

    preset_data["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data["name"] = f"Toneprint - {output_name}"
    preset_data["uid"] = uuid.uuid4().hex

    # Write output
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data, f, indent=4)

    print(f"-> Compiled UADx Hitsville Reverb Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic Logic Pro Native Channel EQ PST Compiler
def compile_logic_eq_toneprint(filepath, base_preset_path, output_name, frontmatter):
    with open(filepath, "r") as f:
        content = f.read()

    # Parse all bands from toneprint markdown
    bands = parse_eq_bands(content)

    # Check if any band is active/configured
    any_configured = any(p["on"] is not None for p in bands.values())
    if not any_configured:
        return False

    # Load base .pst template
    with open(base_preset_path, "rb") as f:
        preset_bytes = bytearray(f.read())

    # surgically patch the float values
    for band_num, params in bands.items():
        if params["on"] is None and params["freq"] is None:
            continue
            
        if band_num == 1:
            # Low Cut: On/Off = Float 5, Freq = Float 6, Slope = Float 7
            if params["on"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 5 * 4, params["on"])
            if params["freq"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 6 * 4, params["freq"])
            if params["gain_or_slope"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 7 * 4, params["gain_or_slope"])
        elif band_num == 8:
            # High Cut: On/Off = Float 33, Freq = Float 34, Slope = Float 35
            if params["on"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 33 * 4, params["on"])
            if params["freq"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 34 * 4, params["freq"])
            if params["gain_or_slope"] is not None:
                struct.pack_into("f", preset_bytes, 8 + 35 * 4, params["gain_or_slope"])
        else:
            # Bands 2 to 7
            base_idx = 9 + (band_num - 2) * 4
            
            if params["on"] is not None:
                struct.pack_into("f", preset_bytes, 8 + base_idx * 4, params["on"])
            if params["freq"] is not None:
                struct.pack_into("f", preset_bytes, 8 + (base_idx + 1) * 4, params["freq"])
            if params["gain_or_slope"] is not None:
                struct.pack_into("f", preset_bytes, 8 + (base_idx + 2) * 4, params["gain_or_slope"])
            if params["q"] is not None:
                struct.pack_into("f", preset_bytes, 8 + (base_idx + 3) * 4, params["q"])

    # Save preset
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(preset_bytes)

    print(f"-> Compiled Logic Channel EQ Preset: 'Toneprint - {output_name}'")
    return True

# Dynamic Logic Pro Native Compressor PST Compiler
def compile_logic_compressor_toneprint(filepath, base_preset_path, output_name, frontmatter):
    with open(filepath, "r") as f:
        content = f.read()

    # Search for Compressor settings using robust helper
    threshold = extract_comp_param(content, ["Threshold"])
    ratio = extract_comp_param(content, ["Ratio"])
    attack = extract_comp_param(content, ["Attack"])
    release = extract_comp_param(content, ["Release"])
    gain = extract_comp_param(content, ["Gain", "Makeup Gain"])
    knee = extract_comp_param(content, ["Knee"])

    # If all are None, skip compressor generation
    if threshold is None and ratio is None and attack is None and release is None:
        return False

    # Load base .pst template
    with open(base_preset_path, "rb") as f:
        preset_bytes = bytearray(f.read())

    # Float 5: Threshold
    if threshold is not None:
        struct.pack_into("f", preset_bytes, 8 + 5 * 4, threshold)
    # Float 6: Ratio
    if ratio is not None:
        struct.pack_into("f", preset_bytes, 8 + 6 * 4, ratio)
    # Float 7: Attack
    if attack is not None:
        struct.pack_into("f", preset_bytes, 8 + 7 * 4, attack)
    # Float 8: Release
    if release is not None:
        struct.pack_into("f", preset_bytes, 8 + 8 * 4, release)
    # Float 9: Makeup Gain
    if gain is not None:
        struct.pack_into("f", preset_bytes, 8 + 9 * 4, gain)
    # Float 10: Knee
    if knee is not None:
        struct.pack_into("f", preset_bytes, 8 + 10 * 4, knee)

    # Save preset
    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(preset_bytes)

    print(f"-> Compiled Logic Compressor Preset: 'Toneprint - {output_name}'")
    return True


def main():
    print("==================================================")
    print("RIG-WIDE TONEPRINT COMPILER & PRESET GENERATOR (V2)")
    print("==================================================")
    
    # 1. Load Neural DSP Base DNA Data
    neural_template_file = NEURAL_TEMPLATE if os.path.exists(NEURAL_TEMPLATE) else NEURAL_TEMPLATE_ALT
    if os.path.exists(neural_template_file):
        with open(neural_template_file, "rb") as f:
            neural_base_data = f.read()
    else:
        print("Warning: Neural DSP base template missing. Skipping Neural compile.")
        neural_base_data = None
        
    # 2. Load UAD Paradise Base DNA JSON
    if os.path.exists(PARADISE_TEMPLATE):
        with open(PARADISE_TEMPLATE, "r") as f:
            uad_base_json = json.load(f)
    else:
        print("Warning: UAD Paradise template missing. Skipping UAD compile.")
        uad_base_json = None

    # 3. Load MixWave Two-Rock Bloomfield Drive Base DNA XML
    mixwave_base_xml = None
    for t_path in [MIXWAVE_TEMPLATE, MIXWAVE_TEMPLATE_ALT, MIXWAVE_TEMPLATE_FACTORY]:
        if os.path.exists(t_path):
            mixwave_base_xml = t_path
            break
    if not mixwave_base_xml:
        print("Warning: MixWave Bloomfield base template missing. Skipping MixWave compile.")

    # 4. Recursively Scan Tones Directory
    compiled_neural = 0
    compiled_uad = 0
    compiled_mixwave = 0
    compiled_la2a = 0
    compiled_hitsville = 0
    compiled_logiceq = 0
    compiled_logiccomp = 0
    
    for root, dirs, files in os.walk(TONES_DIR):
        for f in files:
            if not f.endswith(".md") or f == "INDEX.md":
                continue
            
            filepath = os.path.join(root, f)
            with open(filepath, "r") as file:
                content = file.read()
                
            frontmatter, _ = parse_yaml_frontmatter(content)
            
            amp_str = frontmatter.get("amp", "")
            if not amp_str:
                continue
            
            # Determine beautiful preset name
            if "preset_name" in frontmatter:
                clean_name = frontmatter["preset_name"]
            else:
                # Fallback to standard word capitalization from filename
                name_parts = f.replace(".md", "").split("-")
                clean_name = " ".join([p.capitalize() for p in name_parts])
                
            # Compile based on target amp platform
            if "Cory Wong" in amp_str or "Amp Snob" in amp_str:
                if neural_base_data:
                    if compile_neural_toneprint(filepath, neural_base_data, clean_name, frontmatter):
                        compiled_neural += 1
            elif "Two Rock" in amp_str or "Bloomfield" in amp_str:
                if mixwave_base_xml:
                    if compile_mixwave_toneprint(filepath, mixwave_base_xml, clean_name, frontmatter):
                        compiled_mixwave += 1
            else:
                # Check if it is a UADx model
                is_uad = any(x in amp_str for x in ["Dream", "Enigmatic", "Woodrow", "Ruby", "Showtime", "Lion"])
                if is_uad and uad_base_json:
                    if compile_uad_toneprint(filepath, uad_base_json, clean_name, frontmatter):
                        compiled_uad += 1

            # Compile LA-2A Presets if UADx templates exist
            if os.path.exists(LA2A_BASE):
                # Only compile if LA-2A is in the toneprint content
                if "la-2a" in content.lower():
                    if compile_la2a_toneprint(filepath, LA2A_BASE, clean_name, frontmatter):
                        compiled_la2a += 1

            # Compile Hitsville Reverb Presets if UADx templates exist
            if os.path.exists(HITSVILLE_BASE):
                # Only compile if Hitsville is in the toneprint content
                if "hitsville" in content.lower():
                    if compile_hitsville_toneprint(filepath, HITSVILLE_BASE, clean_name, frontmatter):
                        compiled_hitsville += 1

            # Compile Logic Channel EQ Presets if native templates exist
            if os.path.exists(LOGIC_EQ_BASE):
                # Check if Logic Channel EQ is in toneprint
                if "channel eq" in content.lower() or "high-cut" in content.lower() or "low-cut" in content.lower():
                    if compile_logic_eq_toneprint(filepath, LOGIC_EQ_BASE, clean_name, frontmatter):
                        compiled_logiceq += 1

            # Compile Logic Compressor Presets if native templates exist
            if os.path.exists(LOGIC_COMP_BASE):
                # Only compile if Logic Compressor is in toneprint
                if "logic compressor" in content.lower() or "compressor" in content.lower() and "la-2a" not in content.lower():
                    if compile_logic_compressor_toneprint(filepath, LOGIC_COMP_BASE, clean_name, frontmatter):
                        compiled_logiccomp += 1

    print("\n==================================================")
    print(f"Rig Compilation Complete! Injected:")
    print(f"  -> {compiled_neural} Neural DSP presets in {NEURAL_OUTPUT_DIR}")
    print(f"  -> {compiled_uad} UAD Paradise presets in {PARADISE_DIR}")
    print(f"  -> {compiled_mixwave} MixWave Two-Rock presets in {MIXWAVE_OUTPUT_DIR}")
    print(f"  -> {compiled_la2a} UADx LA-2A presets in {os.path.dirname(LA2A_BASE)}")
    print(f"  -> {compiled_hitsville} UADx Hitsville presets in {os.path.dirname(HITSVILLE_BASE)}")
    print(f"  -> {compiled_logiceq} Logic Channel EQ presets in {os.path.dirname(LOGIC_EQ_BASE)}")
    print(f"  -> {compiled_logiccomp} Logic Compressor presets in {os.path.dirname(LOGIC_COMP_BASE)}")
    print("==================================================")

if __name__ == "__main__":
    main()
