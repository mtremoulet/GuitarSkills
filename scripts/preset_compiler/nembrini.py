"""Nembrini Audio and Kuassa XML preset compiler module."""

from __future__ import annotations

import os
import xml.etree.ElementTree as ET
from typing import Dict, Any

from scripts.utils.config import NEMBRINI_DOCS_DIR, HOME_DIR
from scripts.utils.param_types import to_float, to_bool, find_numeric_param, find_boolean_param
from .base import extract_markdown_section


def compile_nembrini_xml_preset(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
    plugin_type: str,
) -> bool:
    """Compile Nembrini Audio XML preset (MRH810, JC120, Div11, Acoustic Voice, Puretone)."""
    if not os.path.exists(base_preset_path):
        print(f"Warning: Nembrini base template missing for {plugin_type}: {base_preset_path}")
        return False

    preset_data = frontmatter.get("preset_data", {})
    yaml_keys = {
        "mrh810": "nembrini_mrh810",
        "jc120": "nembrini_jc120",
        "div11": "nembrini_div11",
        "acoustic_voice": "nembrini_acoustic_voice",
        "puretone": "nembrini_puretone"
    }

    yaml_key = yaml_keys.get(plugin_type)
    plugin_settings = preset_data.get(yaml_key) if isinstance(preset_data, dict) else None

    if not plugin_settings or not isinstance(plugin_settings, dict):
        plugin_settings = {}
        with open(filepath, "r") as f:
            full_content = f.read()

        keywords_map = {
            "mrh810": ["mrh810", "jcm800"],
            "jc120": ["jazz chorus", "jc120", "jc-120"],
            "div11": ["divided 11", "div11", "divided"],
            "acoustic_voice": ["acoustic voice"],
            "puretone": ["puretone", "pure tone"]
        }
        keywords = keywords_map.get(plugin_type, [plugin_type])
        content = extract_markdown_section(full_content, keywords)

        if plugin_type == "mrh810":
            is_clean = "clean channel" in content.lower() and "lead channel" not in content.lower()
            plugin_settings["ChSel"] = 0.0 if is_clean else 1.0

            master = find_numeric_param(content, ["Master", "Volume (master)"])
            presence = find_numeric_param(content, ["Presence"])
            out_level = find_numeric_param(content, ["Output (plugin Output slider)", "Output Level", "Output"])
            harsh = find_boolean_param(content, ["Harsh"])
            rumbling = find_boolean_param(content, ["Rumbling"])

            gate_power = find_boolean_param(content, ["Noise Gate Power", "Noise Gate", "Gate Power"])
            gate_threshold = find_numeric_param(content, ["Noise Gate Threshold", "Threshold"])
            gate_range = find_numeric_param(content, ["Noise Gate Range", "Range"])

            if master is not None: plugin_settings["Master"] = master
            if presence is not None: plugin_settings["Presence"] = presence
            if out_level is not None: plugin_settings["OutLevel"] = out_level
            if harsh is not None: plugin_settings["Harsh"] = 1.0 if harsh else 0.0
            if rumbling is not None: plugin_settings["Rumbling"] = 1.0 if rumbling else 0.0
            if gate_power is not None: plugin_settings["NgPower"] = 1.0 if gate_power else 0.0
            if gate_threshold is not None: plugin_settings["NgThreshold"] = gate_threshold
            if gate_range is not None: plugin_settings["NgRange"] = gate_range

            gain = find_numeric_param(content, ["Gain"])
            volume = find_numeric_param(content, ["Volume (channel)", "Volume"])
            bass = find_numeric_param(content, ["Bass"])
            middle = find_numeric_param(content, ["Middle", "Mids"])
            treble = find_numeric_param(content, ["Treble"])

            if is_clean:
                if volume is not None: plugin_settings["CleanVolume"] = volume
                if bass is not None: plugin_settings["CleanBass"] = bass
                if treble is not None: plugin_settings["CleanTreble"] = treble
            else:
                if gain is not None: plugin_settings["LeadGain"] = gain
                if volume is not None: plugin_settings["LeadVolume"] = volume
                if bass is not None: plugin_settings["LeadBass"] = bass
                if middle is not None: plugin_settings["LeadMid"] = middle
                if treble is not None: plugin_settings["LeadTreble"] = treble

        elif plugin_type == "jc120":
            bass = find_numeric_param(content, ["Bass"])
            middle = find_numeric_param(content, ["Middle", "Mids"])
            treble = find_numeric_param(content, ["Treble"])
            volume = find_numeric_param(content, ["Volume"])
            bright = find_boolean_param(content, ["Bright Switch", "Bright"])
            distortion = find_numeric_param(content, ["Distortion"])
            reverb = find_numeric_param(content, ["Reverb"])
            out_level = find_numeric_param(content, ["Output (plugin Output slider)", "Output Level", "Output", "OutLevel"])

            if bass is not None: plugin_settings["Bass"] = bass
            if middle is not None: plugin_settings["Middle"] = middle
            if treble is not None: plugin_settings["Treble"] = treble
            if volume is not None: plugin_settings["Volume"] = volume
            if bright is not None: plugin_settings["Brigth"] = 1.0 if bright else 0.0
            if distortion is not None: plugin_settings["Distortion"] = distortion
            if reverb is not None: plugin_settings["Reverb"] = reverb
            if out_level is not None: plugin_settings["OutLevel"] = out_level

            mod_depth = find_numeric_param(content, ["Modulation Depth", "Mod Depth"])
            mod_speed = find_numeric_param(content, ["Modulation Speed", "Mod Speed"])
            if "chorus" in content.lower():
                plugin_settings["ModType"] = 2.0
            elif "vibrato" in content.lower():
                plugin_settings["ModType"] = 1.0

            if mod_depth is not None: plugin_settings["ModDepth"] = mod_depth
            if mod_speed is not None: plugin_settings["ModSpeed"] = mod_speed

        elif plugin_type == "div11":
            bass = find_numeric_param(content, ["Bass"])
            master = find_numeric_param(content, ["Master"])
            volume = find_numeric_param(content, ["Volume"])
            treble = find_numeric_param(content, ["Treble"])
            tight = find_numeric_param(content, ["Tight"])
            harsh = find_numeric_param(content, ["Harsh"])
            boost = find_boolean_param(content, ["Boost Switch", "Boost"])
            out_level = find_numeric_param(content, ["Output (plugin Output slider)", "Output Level", "Output", "OutLevel"])

            if bass is not None: plugin_settings["Bass"] = bass
            if master is not None: plugin_settings["Master"] = master
            if volume is not None: plugin_settings["Volume"] = volume
            if treble is not None: plugin_settings["Treble"] = treble
            if tight is not None: plugin_settings["Tight"] = tight
            if harsh is not None: plugin_settings["Harsh"] = harsh
            if boost is not None: plugin_settings["Boost"] = 1.0 if boost else 0.0
            if out_level is not None: plugin_settings["OutLevel"] = out_level

        elif plugin_type == "acoustic_voice":
            gain = find_numeric_param(content, ["DI Preamp Gain", "Preamp Gain", "Gain"])
            notch = find_numeric_param(content, ["DI Preamp Notch", "Preamp Notch", "Notch"])
            comp_power = find_boolean_param(content, ["Compressor Power", "Compressor Active", "Compressor"])
            comp_attack = find_numeric_param(content, ["Compressor Attack"])
            comp_release = find_numeric_param(content, ["Compressor Release"])
            comp_ratio = find_numeric_param(content, ["Compressor Ratio"])
            comp_thresh = find_numeric_param(content, ["Compressor Threshold"])
            comp_out = find_numeric_param(content, ["Compressor Output", "Compressor Gain"])
            reverb_mix = find_numeric_param(content, ["Reverb Mix"])
            reverb_size = find_numeric_param(content, ["Reverb Size"])
            reverb_tone = find_numeric_param(content, ["Reverb Tone"])

            if gain is not None: plugin_settings["DiPreampGain"] = gain
            if notch is not None: plugin_settings["DiPreampNotch"] = notch
            if comp_power is not None: plugin_settings["CompressorPower"] = 1.0 if comp_power else 0.0
            if comp_attack is not None: plugin_settings["CompressorAttack"] = comp_attack
            if comp_release is not None: plugin_settings["CompressorRelease"] = comp_release
            if comp_ratio is not None: plugin_settings["CompressorRatio"] = comp_ratio
            if comp_thresh is not None: plugin_settings["CompressorThreshold"] = comp_thresh
            if comp_out is not None: plugin_settings["CompressorOut"] = comp_out
            if reverb_mix is not None: plugin_settings["ReverbMix"] = reverb_mix
            if reverb_size is not None: plugin_settings["ReverbSize"] = reverb_size
            if reverb_tone is not None: plugin_settings["ReverbTone"] = reverb_tone

        elif plugin_type == "puretone":
            volume = find_numeric_param(content, ["Volume"])
            growl = find_numeric_param(content, ["Growl"])
            bass = find_numeric_param(content, ["Bass"])
            mid = find_numeric_param(content, ["Middle", "Mids", "Mid"])
            treble = find_numeric_param(content, ["Treble"])
            tone = find_numeric_param(content, ["Tone"])
            out_level = find_numeric_param(content, ["Output (plugin Output slider)", "Output Level", "Output", "OutLevel"])

            if volume is not None: plugin_settings["Volume"] = volume
            if growl is not None: plugin_settings["Growl"] = growl
            if bass is not None: plugin_settings["Bass"] = bass
            if mid is not None: plugin_settings["Mid"] = mid
            if treble is not None: plugin_settings["Treble"] = treble
            if tone is not None: plugin_settings["Tone"] = tone
            if out_level is not None: plugin_settings["OutLevel"] = out_level

    if not plugin_settings:
        return False

    alias_map = {
        "puretone": {
            "DelayMix": "Mix", "DelayTime": "Time", "DelayFeedback": "Feedback",
            "DelaySpread": "Spread", "DelayNote": "Note", "DelayHostSync": "Sync",
            "EqHighPass": "EqHp", "EqLowPass": "EqLp", "NoiseGateRelease": "NoiseGateGate",
            "InputLevel": "InLevel", "Mic1Distance": "Mic1Dist", "Mic1Position": "Mic1Pos",
            "Mic2Distance": "Mic2Dist", "Mic2Position": "Mic2Pos", "CabinetMode": "CabMode",
            "CabinetType": "CabType"
        }
    }

    plugin_aliases = alias_map.get(plugin_type, {})
    normalized_settings = {}
    for k, v in plugin_settings.items():
        target_k = plugin_aliases.get(k, k)
        if target_k == "Feedback" and isinstance(v, str):
            if v.lower() in ["off", "none", "0", "0.0"]:
                v = 0.0
        elif target_k in ["CabMode", "CabinetMode"] and isinstance(v, str):
            v = 0.0 if v.lower() == "cabinet" else 1.0
        elif target_k in ["Mic1Type", "Mic2Type"] and isinstance(v, str):
            if "57" in v: v = 0.0
            elif "121" in v: v = 1.0
        elif target_k in ["CabType", "CabinetType"] and isinstance(v, str):
            if "tc 412" in v.lower() or "real" in v.lower() or "hughes" in v.lower():
                v = 1.0
        normalized_settings[target_k] = v

    mapped_settings = {}
    for k, v in normalized_settings.items():
        if isinstance(v, bool):
            mapped_settings[k] = 1.0 if v else 0.0
        else:
            mapped_settings[k] = to_float(v, default=0.0) if not isinstance(v, str) else v

    tree = ET.parse(base_preset_path)
    root = tree.getroot()

    for param in root.findall("PARAM"):
        param_id = param.get("id")
        if param_id in mapped_settings:
            param.set("value", str(mapped_settings[param_id]))

    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.xml")
    tree.write(out_path, encoding="UTF-8", xml_declaration=True)
    print(f"-> Compiled Nembrini {plugin_type.upper()} XML Preset: 'Toneprint - {output_name}'")
    return True


def compile_nembrini_stomp_presets(filepath: str, output_name: str, frontmatter: Dict[str, Any]) -> bool:
    preset_data = frontmatter.get("preset_data", {})
    if not isinstance(preset_data, dict):
        return False

    compiled_any = False

    if "clon_minotaur" in preset_data:
        clon_info = preset_data["clon_minotaur"]
        if isinstance(clon_info, dict):
            out_dir = str(NEMBRINI_DOCS_DIR / "NA Clon Minotaur")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"Toneprint - {output_name}.xml")

            gain_val = to_float(clon_info.get("gain", 0.0))
            treble_val = to_float(clon_info.get("treble", 4.5))
            output_val = to_float(clon_info.get("output", 7.5))

            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>

<ClonMinotaur version="1.0.5" lastUIWidth="667" lastUIHeight="467" CurrentPreset="{out_path}">
  <PARAM id="Gain" value="{gain_val}"/>
  <PARAM id="Output" value="{output_val}"/>
  <PARAM id="Treble" value="{treble_val}"/>
  <PARAM id="power" value="1.0"/>
</ClonMinotaur>
"""
            with open(out_path, "w") as f:
                f.write(xml_content)
            print(f"-> Compiled Nembrini Clon Minotaur XML Preset: 'Toneprint - {output_name}.xml'")
            compiled_any = True

    if "nembrini_808" in preset_data or "808" in preset_data:
        t808_info = preset_data.get("nembrini_808") or preset_data.get("808")
        if isinstance(t808_info, dict):
            out_dir = str(NEMBRINI_DOCS_DIR / "NA 808")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"Toneprint - {output_name}.xml")

            drive_val = to_float(t808_info.get("drive", t808_info.get("gain", 3.0)))
            tone_val = to_float(t808_info.get("tone", 5.0))
            level_val = to_float(t808_info.get("level", t808_info.get("output", 7.0)))

            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>

<NA808 lastUIWidth="536" lastUIHeight="605" CurrentPreset="{out_path}"
       version="1.0.6">
  <PARAM id="Drive" value="{drive_val}"/>
  <PARAM id="Level" value="{level_val}"/>
  <PARAM id="Tone" value="{tone_val}"/>
  <PARAM id="power" value="1.0"/>
</NA808>
"""
            with open(out_path, "w") as f:
                f.write(xml_content)
            print(f"-> Compiled Nembrini 808 XML Preset: 'Toneprint - {output_name}.xml'")
            compiled_any = True

    return compiled_any


def compile_kuassa_stomp_presets(filepath: str, output_name: str, frontmatter: Dict[str, Any]) -> bool:
    preset_data = frontmatter.get("preset_data", {})
    if not isinstance(preset_data, dict):
        return False

    compiled_any = False

    if "kuassa_blues_barker" in preset_data or "blues_barker" in preset_data:
        barker_info = preset_data.get("kuassa_blues_barker") or preset_data.get("blues_barker")
        if isinstance(barker_info, dict):
            out_dir = str(HOME_DIR / "Music" / "Kuassa" / "Presets" / "EfektorBluesBarker")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"Toneprint - {output_name}.kebbp")

            gain_val = to_float(barker_info.get("gain", 3.5)) / 10.0
            tone_val = to_float(barker_info.get("tone", 5.0)) / 10.0
            level_val = to_float(barker_info.get("level", 6.0)) / 10.0
            bypass_val = "true" if not to_bool(barker_info.get("enabled", False)) else "false"

            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>

<kuassaPatch version="1.0">
  <DeviceName>Efektor BluesBarker</DeviceName>
  <Properties deviceProductID="com.kuassa.EfektorBluesBarker" deviceVersion="1.0.0"
              presetVersion="1.0">
    <Value property="onBypass" type="boolean">{bypass_val}</Value>
    <Value property="inputVol" type="number">0.50000</Value>
    <Value property="type" type="number">0</Value>
    <Value property="gain" type="number">{gain_val:.5f}</Value>
    <Value property="tone" type="number">{tone_val:.5f}</Value>
    <Value property="level" type="number">{level_val:.5f}</Value>
    <Value property="dryWet" type="number">1.00000</Value>
    <Value property="oversampling" type="number">0</Value>
  </Properties>
</kuassaPatch>
"""
            with open(out_path, "w") as f:
                f.write(xml_content)
            print(f"-> Compiled Kuassa Efektor Blues Barker Preset: 'Toneprint - {output_name}.kebbp'")
            compiled_any = True

    if "kuassa_blues_river" in preset_data or "blues_river" in preset_data:
        river_info = preset_data.get("kuassa_blues_river") or preset_data.get("blues_river")
        if isinstance(river_info, dict):
            out_dir = str(HOME_DIR / "Music" / "Kuassa" / "Presets" / "EfektorBluesRiver")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"Toneprint - {output_name}.kebrp")

            gain_val = to_float(river_info.get("gain", 3.0)) / 10.0
            tone_val = to_float(river_info.get("tone", 5.0)) / 10.0
            level_val = to_float(river_info.get("level", 7.0)) / 10.0
            bypass_val = "true" if not to_bool(river_info.get("enabled", False)) else "false"

            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>

<kuassaPatch version="1.0">
  <DeviceName>Efektor BluesRiver</DeviceName>
  <Properties deviceProductID="com.kuassa.EfektorBluesRiver" deviceVersion="1.0.0"
              presetVersion="1.0">
    <Value property="onBypass" type="boolean">{bypass_val}</Value>
    <Value property="inputVol" type="number">0.50000</Value>
    <Value property="type" type="number">0</Value>
    <Value property="gain" type="number">{gain_val:.5f}</Value>
    <Value property="tone" type="number">{tone_val:.5f}</Value>
    <Value property="level" type="number">{level_val:.5f}</Value>
    <Value property="dryWet" type="number">1.00000</Value>
    <Value property="oversampling" type="number">0</Value>
  </Properties>
</kuassaPatch>
"""
            with open(out_path, "w") as f:
                f.write(xml_content)
            print(f"-> Compiled Kuassa Efektor Blues River Preset: 'Toneprint - {output_name}.kebrp'")
            compiled_any = True

    return compiled_any
