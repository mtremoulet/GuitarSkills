#!/usr/bin/env python3
import os
import re

# Directories
TONES_DIR = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"

# --- Parsing Engines (Adapted from compile_all_presets.py) ---

def parse_yaml_frontmatter_flat(content):
    """Simple parser for existing flat frontmatter properties before adding preset_data."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, content
    
    yaml_text = match.group(1)
    body = content[match.end():]
    
    data = {}
    for line in yaml_text.splitlines():
        # Ignore indented properties/subkeys to clean out any old preset_data or overrides
        if line.startswith(" ") or line.startswith("\t"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            
            # Strip quotes
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
                
            # Parse simple types
            if val.lower() == "true":
                val = True
            elif val.lower() == "false":
                val = False
            else:
                try:
                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
            data[key] = val
    return data, body

def find_numeric_parameter(content, param_names):
    for name in param_names:
        pattern = r"\|\s*" + re.escape(name) + r"\s*\|\s*(?:\*\*)?([~0-9.+−-]+)(?:\*\*)?(?:\s*%)?\s*\|"
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            val_str = match.group(1).replace("−", "-").replace("~", "").strip()
            try:
                val = float(val_str)
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
                    bands[1]["on"] = True
                    bands[1]["freq"] = freq
                if slope is not None:
                    bands[1]["gain_or_slope"] = slope
            elif "low-pass" in line_lower or "lpf" in line_lower or "high cut" in line_lower or "high-cut" in line_lower:
                freq = extract_freq(line)
                slope = extract_slope(line)
                if freq is not None:
                    bands[8]["on"] = True
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
            
        bands[band_num]["on"] = True
        if freq is not None:
            bands[band_num]["freq"] = freq
        if gain_or_slope is not None:
            bands[band_num]["gain_or_slope"] = gain_or_slope
        if q is not None:
            bands[band_num]["q"] = q
            
    return bands

# --- YAML Serialization Utility ---

def serialize_yaml(data, indent=0):
    lines = []
    for k, v in data.items():
        prefix = " " * indent
        if isinstance(v, dict):
            if not v:
                lines.append(f"{prefix}{k}: {{}}")
            else:
                lines.append(f"{prefix}{k}:")
                lines.append(serialize_yaml(v, indent + 2))
        elif isinstance(v, bool):
            val_str = "true" if v else "false"
            lines.append(f"{prefix}{k}: {val_str}")
        elif v is None:
            lines.append(f"{prefix}{k}: null")
        else:
            if isinstance(v, float):
                if v.is_integer():
                    lines.append(f"{prefix}{k}: {int(v)}")
                else:
                    lines.append(f"{prefix}{k}: {v}")
            elif isinstance(v, str):
                if ":" in v or "-" in v or "," in v or "#" in v or "'" in v or '"' in v or "?" in v or "\n" in v:
                    escaped = v.replace('"', '\\"')
                    lines.append(f"{prefix}{k}: \"{escaped}\"")
                else:
                    lines.append(f"{prefix}{k}: {v}")
            else:
                lines.append(f"{prefix}{k}: {v}")
    return "\n".join(lines)


# --- Core Migration Logic ---

def process_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        
    frontmatter, body = parse_yaml_frontmatter_flat(content)
    
    amp_str = frontmatter.get("amp", "")
    if not amp_str:
        return False
        
    preset_data = {}
    
    # 1. Amp Platform Classification & Extraction
    if "Cory Wong" in amp_str or "Amp Snob" in amp_str:
        preset_data["amp_platform"] = "neural_dsp"
        amp_settings = {}
        
        comp_active = find_boolean_parameter(body, ["The 4th Position Compressor", "Compressor Active", "Compressor"])
        if comp_active is not None:
            amp_settings["compressorActive"] = "true" if comp_active else "false"
            
        for key in ["Blend", "Tone", "Compression", "Volume"]:
            val = find_numeric_parameter(body, [key])
            if val is not None:
                amp_settings["compressor" + key] = f"{val:.2f}"
                
        amp_settings["selectedAmp"] = "2"
        amp_settings["selectedCab"] = "2"
        amp_settings["ampCabLinkedState"] = "false"
        
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
            val = find_numeric_parameter(body, names)
            if val is not None:
                amp_settings[param] = f"{val:.2f}"
                
        drive = find_boolean_parameter(body, ["Drive Switch", "Drive"])
        if drive is not None:
            amp_settings["snobDrive"] = "true" if drive else "false"
        bright = find_boolean_parameter(body, ["Bright Switch", "Bright"])
        if bright is not None:
            amp_settings["snobBright"] = "true" if bright else "false"
            
        pos = find_numeric_parameter(body, ["Position L", "Position"])
        if pos is not None: amp_settings["leftCabPosition"] = f"{pos:.2f}"
        dist = find_numeric_parameter(body, ["Distance L", "Distance"])
        if dist is not None: amp_settings["leftCabDistance"] = f"{dist:.2f}"
        room = find_numeric_parameter(body, ["Room Send L", "Room Send"])
        if room is not None: amp_settings["leftRoomMicLevel"] = f"{room:.1f}"
        
        amp_settings["leftCabActive"] = "true"
        amp_settings["leftCab0MicType"] = "4"
        amp_settings["rightCabActive"] = "false"
        
        eq_active = find_boolean_parameter(body, ["EQ Status", "EQ Active", "snobEQActive"])
        if eq_active is not None:
            amp_settings["snobEQActive"] = "true" if eq_active else "false"
            
        bands = ["65 Hz", "125 Hz", "250 Hz", "500 Hz", "1 kHz", "2 kHz", "4 kHz", "8 kHz", "16 kHz"]
        for i, band in enumerate(bands, 1):
            val = find_numeric_parameter(body, [band])
            if val is not None:
                amp_settings[f"snobEQBand{i}"] = f"{val:.1f}"
        
        amp_settings["snobEQHpf"] = "20.0"
        amp_settings["snobEQLpf"] = "20000.0"
        
        for pedal in ["tuberActive", "bigRigActive", "postalActive", "delayActive", "washActive", "chorusActive"]:
            amp_settings[pedal] = "false"
            
        preset_data["amp_settings"] = amp_settings
        
    elif "Two Rock" in amp_str or "Bloomfield" in amp_str:
        preset_data["amp_platform"] = "mixwave"
        amp_settings = {}
        
        gain = find_numeric_parameter(body, ["Gain"])
        treble = find_numeric_parameter(body, ["Treble"])
        mid = find_numeric_parameter(body, ["Middle", "Mids"])
        bass = find_numeric_parameter(body, ["Bass"])
        presence = find_numeric_parameter(body, ["Presence"])
        master = find_numeric_parameter(body, ["Master"])
        reverb = find_numeric_parameter(body, ["Reverb"])
        vibe = find_numeric_parameter(body, ["Vibe"])
        bright = find_boolean_parameter(body, ["Bright Switch", "Bright"])
        mid_sw = find_boolean_parameter(body, ["Mid Switch", "Mid"])
        deep = find_boolean_parameter(body, ["Deep Switch", "Deep"])
        bypass_sw = find_boolean_parameter(body, ["Tone Stack Bypass"])
        lead_sw = find_boolean_parameter(body, ["Lead Switch", "Lead"])
        gate_val = find_numeric_parameter(body, ["Noise Gate", "Gate Threshold"])
        input_trim = find_numeric_parameter(body, ["Input Trim"])
        output_trim = find_numeric_parameter(body, ["Output Trim"])
        
        if gain is not None: amp_settings["Gain"] = gain
        if treble is not None: amp_settings["Treble"] = treble
        if mid is not None: amp_settings["Middle"] = mid
        if bass is not None: amp_settings["Bass"] = bass
        if presence is not None: amp_settings["Presence"] = presence
        if master is not None: amp_settings["Master"] = master
        if reverb is not None: amp_settings["Reverb"] = reverb
        if vibe is not None: amp_settings["Vibe"] = vibe
        if bright is not None: amp_settings["Bright"] = bright
        if mid_sw is not None: amp_settings["Mid"] = mid_sw
        if deep is not None: amp_settings["Deep"] = deep
        if bypass_sw is not None: amp_settings["Tone Stack Bypass"] = bypass_sw
        if lead_sw is not None: amp_settings["Lead"] = lead_sw
        if gate_val is not None: amp_settings["Noise Gate"] = gate_val
        if input_trim is not None: amp_settings["Input Trim"] = input_trim
        if output_trim is not None: amp_settings["Output Trim"] = output_trim
        
        preset_data["amp_settings"] = amp_settings
        
    else:
        is_uad = any(x in amp_str for x in ["Dream", "Enigmatic", "Woodrow", "Ruby", "Showtime", "Lion"])
        if is_uad:
            preset_data["amp_platform"] = "uad_paradise"
            amp_settings = {}
            
            vol = find_numeric_parameter(body, ["Volume (Gain)", "Volume", "Volume (Inst)", "inst_volume"])
            vol_mic = find_numeric_parameter(body, ["Volume (Mic)", "mic_volume"])
            treble = find_numeric_parameter(body, ["Treble", "Top Boost Treble", "Tone"])
            mid = find_numeric_parameter(body, ["Middle", "Mids", "Top Boost Mids"])
            bass = find_numeric_parameter(body, ["Bass", "Top Boost Bass"])
            presence = find_numeric_parameter(body, ["Presence"])
            master = find_numeric_parameter(body, ["Master (labeled 6.5)", "Master", "Master volume"])
            tone_cut = find_numeric_parameter(body, ["Tone Cut"])
            bright = find_boolean_parameter(body, ["Bright Switch", "Bright / Normal", "Bright"])
            boost = find_boolean_parameter(body, ["Boost Button", "Boost Switch", "Boost (Stock)", "Boost"])
            cut_sw = find_boolean_parameter(body, ["Cut Switch", "Cut"])
            
            if vol is not None: amp_settings["Volume"] = vol
            if vol_mic is not None: amp_settings["Volume (Mic)"] = vol_mic
            if treble is not None: amp_settings["Treble"] = treble
            if mid is not None: amp_settings["Middle"] = mid
            if bass is not None: amp_settings["Bass"] = bass
            if presence is not None: amp_settings["Presence"] = presence
            if master is not None: amp_settings["Master"] = master
            if tone_cut is not None: amp_settings["Tone Cut"] = tone_cut
            if bright is not None: amp_settings["Bright"] = bright
            if boost is not None: amp_settings["Boost"] = boost
            if cut_sw is not None: amp_settings["Cut"] = cut_sw
            
            preset_data["amp_settings"] = amp_settings

    # 2. UADx LA-2A
    if "la-2a" in body.lower():
        peak_reduction = find_numeric_parameter(body, ["Peak Reduction"])
        gain = find_numeric_parameter(body, ["Gain", "Makeup Gain"])
        mode_compress = find_boolean_parameter(body, ["Compress Mode", "Compress"])
        
        la2a = {}
        if peak_reduction is not None: la2a["peak_reduction"] = peak_reduction
        if gain is not None: la2a["gain"] = gain
        if mode_compress is not None: la2a["compress"] = mode_compress
        
        if la2a:
            preset_data["la2a"] = la2a

    # 3. UADx Hitsville Reverb
    if "hitsville" in body.lower():
        mix = find_numeric_parameter(body, ["Mix", "Room Mix"])
        pre_delay = find_numeric_parameter(body, ["Pre-Delay"])
        decay = find_numeric_parameter(body, ["Decay"])
        
        hitsville = {}
        if mix is not None: hitsville["mix"] = mix
        if pre_delay is not None: hitsville["pre_delay"] = pre_delay
        if decay is not None: hitsville["decay"] = decay
        
        if hitsville:
            preset_data["hitsville"] = hitsville

    # 4. Logic Native Channel EQ
    if "channel eq" in body.lower() or "high-cut" in body.lower() or "low-cut" in body.lower():
        bands = parse_eq_bands(body)
        logic_eq = {}
        for b_num, p in bands.items():
            if p["on"] is None and p["freq"] is None:
                continue
            band_data = {}
            if p["on"] is not None: band_data["on"] = p["on"]
            if p["freq"] is not None: band_data["freq"] = p["freq"]
            if b_num in [1, 8]:
                if p["gain_or_slope"] is not None: band_data["slope"] = p["gain_or_slope"]
            else:
                if p["gain_or_slope"] is not None: band_data["gain"] = p["gain_or_slope"]
                if p["q"] is not None: band_data["q"] = p["q"]
            if band_data:
                logic_eq[f"band{b_num}"] = band_data
        if logic_eq:
            preset_data["logic_eq"] = logic_eq

    # 5. Logic Native Compressor
    if "logic compressor" in body.lower() or "compressor" in body.lower() and "la-2a" not in body.lower():
        threshold = extract_comp_param(body, ["Threshold"])
        ratio = extract_comp_param(body, ["Ratio"])
        attack = extract_comp_param(body, ["Attack"])
        release = extract_comp_param(body, ["Release"])
        gain = extract_comp_param(body, ["Gain", "Makeup Gain"])
        knee = extract_comp_param(body, ["Knee"])
        
        logic_comp = {}
        if threshold is not None: logic_comp["threshold"] = threshold
        if ratio is not None: logic_comp["ratio"] = ratio
        if attack is not None: logic_comp["attack"] = attack
        if release is not None: logic_comp["release"] = release
        if gain is not None: logic_comp["makeup_gain"] = gain
        if knee is not None: logic_comp["knee"] = knee
        
        if logic_comp:
            preset_data["logic_compressor"] = logic_comp

    # Merging and Writing Back
    if preset_data:
        frontmatter["preset_data"] = preset_data
        
    # Serialize frontmatter
    fm_yaml = serialize_yaml(frontmatter)
    new_content = f"---\n{fm_yaml}\n---{body}"
    
    with open(filepath, "w") as f:
        f.write(new_content)
        
    print(f"Migrated: {os.path.basename(filepath)}")
    return True


def main():
    print("Starting automated frontmatter migration...")
    migrated_count = 0
    for root, dirs, files in os.walk(TONES_DIR):
        for f in files:
            if not f.endswith(".md") or f == "INDEX.md":
                continue
            filepath = os.path.join(root, f)
            if process_file(filepath):
                migrated_count += 1
                
    print(f"\nMigration complete! Updated {migrated_count} toneprint files.")

if __name__ == "__main__":
    main()
