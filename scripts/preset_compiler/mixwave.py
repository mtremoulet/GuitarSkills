"""MixWave Two-Rock Bloomfield Drive XML preset compiler module."""

from __future__ import annotations

import os
import xml.etree.ElementTree as ET
from typing import Dict, Any

from scripts.utils.config import MIXWAVE_OUTPUT_DIR
from scripts.utils.param_types import to_float, to_bool, find_numeric_param, find_boolean_param


def compile_mixwave_toneprint(
    filepath: str,
    base_xml_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile MixWave Two-Rock Bloomfield Drive XML preset."""
    if not os.path.exists(base_xml_path):
        print(f"Warning: MixWave base template missing: {base_xml_path}")
        return False

    preset_data = frontmatter.get("preset_data", {})
    amp_settings = preset_data.get("amp_settings") if isinstance(preset_data, dict) else None

    tree = ET.parse(base_xml_path)
    root = tree.getroot()

    global_vars = root.find("Variables")
    amp_module = root.find(".//Module[@moduleName='Amp']")
    amp_vars = amp_module.find("Variables") if amp_module is not None else None
    cab_module = root.find(".//Module[@moduleName='Cab']")
    cab_vars = cab_module.find("Variables") if cab_module is not None else None
    od_module = root.find(".//Module[@moduleName='Overdrive']")
    od_vars = od_module.find("Variables") if od_module is not None else None

    if amp_settings and isinstance(amp_settings, dict):
        gain = to_float(amp_settings.get("Gain"))
        treble = to_float(amp_settings.get("Treble"))
        mid = to_float(amp_settings.get("Middle"))
        bass = to_float(amp_settings.get("Bass"))
        presence = to_float(amp_settings.get("Presence"))
        master = to_float(amp_settings.get("Master"))
        reverb = to_float(amp_settings.get("Reverb"))
        vibe = to_float(amp_settings.get("Vibe"))
        bright = to_bool(amp_settings.get("Bright"))
        mid_sw = to_bool(amp_settings.get("Mid"))
        deep = to_bool(amp_settings.get("Deep"))
        bypass_sw = to_bool(amp_settings.get("Tone Stack Bypass"))
        lead_sw = to_bool(amp_settings.get("Lead"))
        gate_val = to_float(amp_settings.get("Noise Gate"))
        input_trim = to_float(amp_settings.get("Input Trim"))
        output_trim = to_float(amp_settings.get("Output Trim"))
    else:
        with open(filepath, "r") as f:
            content = f.read()
        gain = find_numeric_param(content, ["Gain"])
        treble = find_numeric_param(content, ["Treble"])
        mid = find_numeric_param(content, ["Middle", "Mids"])
        bass = find_numeric_param(content, ["Bass"])
        presence = find_numeric_param(content, ["Presence"])
        master = find_numeric_param(content, ["Master"])
        reverb = find_numeric_param(content, ["Reverb"])
        vibe = find_numeric_param(content, ["Vibe"])
        bright = find_boolean_param(content, ["Bright Switch", "Bright"])
        mid_sw = find_boolean_param(content, ["Mid Switch", "Mid"])
        deep = find_boolean_param(content, ["Deep Switch", "Deep"])
        bypass_sw = find_boolean_param(content, ["Tone Stack Bypass"])
        lead_sw = find_boolean_param(content, ["Lead Switch", "Lead"])
        gate_val = find_numeric_param(content, ["Noise Gate", "Gate Threshold"])
        input_trim = find_numeric_param(content, ["Input Trim"])
        output_trim = find_numeric_param(content, ["Output Trim"])

    if amp_vars is not None:
        if gain is not None: amp_vars.set("AmpGain", f"{gain:.3f}")
        if treble is not None: amp_vars.set("AmpTreble", f"{treble:.3f}")
        if mid is not None: amp_vars.set("AmpMiddle", f"{mid:.3f}")
        if bass is not None: amp_vars.set("AmpBass", f"{bass:.3f}")
        if presence is not None: amp_vars.set("AmpPresence", f"{presence:.3f}")
        if master is not None: amp_vars.set("AmpMaster", f"{master:.3f}")
        if reverb is not None: amp_vars.set("AmpReverb", f"{reverb:.3f}")

        if bright is not None: amp_vars.set("AmpBrightOnOff", "1" if bright else "0")
        if mid_sw is not None: amp_vars.set("AmpMidOnOff", "1" if mid_sw else "0")
        if deep is not None: amp_vars.set("AmpDeepOnOff", "1" if deep else "0")
        if bypass_sw is not None: amp_vars.set("AmpToneBypassOnOff", "1" if bypass_sw else "0")
        if lead_sw is not None: amp_vars.set("AmpType", "1" if lead_sw else "0")

    if cab_vars is not None and vibe is not None:
        cab_vars.set("Cab1Vibe", f"{vibe:.3f}")

    if global_vars is not None:
        if gate_val is not None:
            global_vars.set("GateOnOff", "1")
            global_vars.set("GateThreshold", f"{gate_val:.3f}")
        if input_trim is not None:
            global_vars.set("InputLevel", f"{input_trim:.3f}")
        if output_trim is not None:
            global_vars.set("OutputLevel", f"{output_trim:.3f}")

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

    os.makedirs(MIXWAVE_OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(MIXWAVE_OUTPUT_DIR, f"{output_name}.xml")
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"-> Compiled MixWave Preset: '{output_name}'")
    return True
