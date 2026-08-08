"""Valhalla Supermassive XML VPRESET compiler module."""

from __future__ import annotations

import os
import re
import xml.etree.ElementTree as ET
from typing import Dict, Any

from scripts.utils.param_types import to_float, find_numeric_param
from .base import extract_markdown_section

VALHALLA_MODES = [
    "gemini", "hydra", "centaurus", "sagittarius", "great orion",
    "great annihilator", "andromeda", "lyra", "capricorn",
    "large magellanic cloud", "small magellanic cloud", "triangulum",
    "cirrus major", "cirrus minor", "cassiopeia", "ursa major",
    "ursa minor", "scorpio", "leo", "virgo"
]


def compile_supermassive_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile Valhalla Supermassive XML VPRESET file."""
    preset_data = frontmatter.get("preset_data", {})
    supermassive_data = preset_data.get("supermassive") if isinstance(preset_data, dict) else None

    mix = None
    delay_ms = None
    warp = None
    feedback = None
    density = None
    mode = None

    if supermassive_data and isinstance(supermassive_data, dict):
        mix = supermassive_data.get("mix")
        delay_ms = supermassive_data.get("delay")
        warp = supermassive_data.get("warp")
        feedback = supermassive_data.get("feedback")
        density = supermassive_data.get("density")
        mode = supermassive_data.get("mode")
    else:
        with open(filepath, "r") as f:
            full_content = f.read()

        content = extract_markdown_section(full_content, ["ValhallaSuperMassive", "SuperMassive", "Valhalla Super Massive"])
        mix = find_numeric_param(content, ["Mix"])

        m_delay = re.search(r"\|\s*(?:Delay|Delay time)\s*\|\s*(?:\*\*)?([~0-9.+−-]+)(?:ms|s)?(?:\*\*)?\s*\|", content, re.IGNORECASE)
        if m_delay:
            delay_ms = to_float(m_delay.group(1))
        else:
            delay_ms = find_numeric_param(content, ["Delay", "Delay time"])

        warp = find_numeric_param(content, ["Warp"])
        feedback = find_numeric_param(content, ["Feedback"])
        density = find_numeric_param(content, ["Density"])

        m_mode = re.search(r"\|\s*Mode\s*\|\s*(?:\*\*)?([^|]+?)(?:\*\*)?\s*\|", content, re.IGNORECASE)
        if m_mode:
            mode = m_mode.group(1).strip()

    if mix is None and delay_ms is None and feedback is None:
        return False

    try:
        with open(base_preset_path, "r") as f:
            preset_text = f.read()
    except Exception as e:
        print(f"Error: Failed to read Valhalla Supermassive base template: {e}")
        return False

    try:
        root_node = ET.fromstring(preset_text.encode("utf-8"))
        if root_node.tag != "ValhallaSupermassive":
            return False

        root_node.set("presetName", f"Toneprint - {output_name}")

        if mix is not None:
            val = mix / 100.0 if mix > 1.0 else mix
            root_node.set("Mix", f"{val:.15f}".rstrip("0").rstrip("."))

        if delay_ms is not None:
            val = delay_ms / 1000.0 if delay_ms > 2.0 else delay_ms
            root_node.set("Delay_Ms", f"{val:.15f}".rstrip("0").rstrip("."))

        if warp is not None:
            val = warp / 100.0 if warp > 1.0 else warp
            root_node.set("DelayWarp", f"{val:.15f}".rstrip("0").rstrip("."))

        if feedback is not None:
            val = feedback / 100.0 if feedback > 1.0 else feedback
            root_node.set("Feedback", f"{val:.15f}".rstrip("0").rstrip("."))

        if density is not None:
            val = density / 100.0 if density > 1.0 else density
            root_node.set("Density", f"{val:.15f}".rstrip("0").rstrip("."))

        if mode is not None:
            mode_str = str(mode).lower().strip()
            mode_idx = -1
            for idx, m in enumerate(VALHALLA_MODES):
                if m in mode_str or mode_str in m:
                    mode_idx = idx
                    break
            if mode_idx != -1:
                root_node.set("Mode", f"{mode_idx / 24.0:.15f}".rstrip("0").rstrip("."))
            else:
                f_mode = to_float(mode, default=0.0)
                root_node.set("Mode", f"{f_mode:.15f}".rstrip("0").rstrip("."))

        root_node.set("ModRate", "0.0")
        root_node.set("ModDepth", "0.0")

        out_xml = ET.tostring(root_node, encoding="utf-8").decode("utf-8")
        out_content = '<?xml version="1.0" encoding="UTF-8"?>\n\n' + out_xml + '\n'

        output_dir = os.path.dirname(base_preset_path)
        out_path = os.path.join(output_dir, f"Toneprint - {output_name}.vpreset")
        with open(out_path, "w") as f:
            f.write(out_content)

        print(f"-> Compiled ValhallaSupermassive Preset: 'Toneprint - {output_name}'")
        return True
    except Exception as e:
        print(f"Error: Failed to compile Supermassive preset: {e}")
        return False
