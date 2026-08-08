#!/usr/bin/env python3
"""
Rig-Wide Toneprint Compiler & Preset Generator.

Scans toneprints in `tones/` and compiles native presets across Neural DSP, UAD,
MixWave, Logic Pro native PSTs, Yamaha THR, Nembrini, Kuassa, and Valhalla.
"""

from __future__ import annotations

import os
import sys
import json
import argparse
from pathlib import Path

# Add workspace root to sys.path for package imports
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from scripts.utils.config import (
    TONES_DIR,
    NEURAL_TEMPLATE,
    NEURAL_TEMPLATE_ALT,
    NEURAL_OUTPUT_DIR,
    PARADISE_DIR,
    PARADISE_TEMPLATE,
    LA2A_BASE,
    LA2A_GRAY_BASE,
    HITSVILLE_BASE,
    GALAXY_BASE,
    STUDIO_D_BASE,
    VALHALLA_BASE,
    LOGIC_EQ_BASE,
    LOGIC_COMP_BASE,
    LOGIC_SPACEDESIGNER_BASE,
    MIXWAVE_TEMPLATE,
    MIXWAVE_TEMPLATE_ALT,
    MIXWAVE_TEMPLATE_FACTORY,
    MIXWAVE_OUTPUT_DIR,
    YAMAHA_THR_OUTPUT_DIR,
    NEMBRINI_TEMPLATES,
)

from scripts.preset_compiler import (
    parse_yaml_frontmatter,
    compile_neural_toneprint,
    compile_uad_toneprint,
    compile_la2a_toneprint,
    compile_hitsville_toneprint,
    compile_galaxy_toneprint,
    compile_studio_d_toneprint,
    compile_mixwave_toneprint,
    compile_supermassive_toneprint,
    compile_logic_eq_toneprint,
    compile_logic_compressor_toneprint,
    compile_logic_space_designer_toneprint,
    compile_yamaha_thr_toneprint,
    compile_nembrini_xml_preset,
    compile_nembrini_stomp_presets,
    compile_kuassa_stomp_presets,
)


def main():
    parser = argparse.ArgumentParser(description="Compile guitar toneprints into DAW plugin presets.")
    parser.add_argument("-f", "--filter", help="Filter target toneprints by filename, path, ID, or preset name substring (case-insensitive).")
    parser.add_argument("--file", help="Compile only a single specific toneprint file path (e.g. tones/humbuckers/my-tone.md).")
    args = parser.parse_args()

    filter_arg = args.filter.lower() if args.filter else None
    file_arg = args.file if args.file else None

    print("==================================================")
    print("RIG-WIDE TONEPRINT COMPILER & PRESET GENERATOR (V2)")
    if filter_arg:
        print(f"Filter active: compiling matching '{filter_arg}'")
    if file_arg:
        print(f"File active: compiling only '{file_arg}'")
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
            mixwave_base_xml = str(t_path)
            break
    if not mixwave_base_xml:
        print("Warning: MixWave Bloomfield base template missing. Skipping MixWave compile.")

    # Counters
    compiled = {
        "neural": 0, "uad": 0, "mixwave": 0, "la2a": 0, "hitsville": 0,
        "logiceq": 0, "logiccomp": 0, "thr": 0, "mrh810": 0, "jc120": 0,
        "div11": 0, "acoustic": 0, "puretone": 0, "galaxy": 0, "studiod": 0,
        "supermassive": 0, "spacedesigner": 0,
    }

    # Recursively Scan Tones Directory
    for root, dirs, files in os.walk(TONES_DIR):
        for f in files:
            if not f.endswith(".md") or f == "INDEX.md":
                continue

            filepath = os.path.join(root, f)
            if file_arg and os.path.abspath(filepath) != os.path.abspath(file_arg):
                continue

            with open(filepath, "r") as file:
                content = file.read()

            frontmatter, _ = parse_yaml_frontmatter(content)
            amp_str = frontmatter.get("amp", "")
            if not amp_str:
                continue

            if "preset_name" in frontmatter:
                clean_name = frontmatter["preset_name"]
            else:
                name_parts = f.replace(".md", "").split("-")
                clean_name = " ".join([p.capitalize() for p in name_parts])

            if filter_arg:
                t_id = str(frontmatter.get("id", "")).lower()
                if filter_arg not in f.lower() and filter_arg not in filepath.lower() and filter_arg not in clean_name.lower() and filter_arg not in t_id:
                    continue

            # Target Amp Platform Compilation
            if "Cory Wong" in amp_str or "Amp Snob" in amp_str:
                if neural_base_data and compile_neural_toneprint(filepath, neural_base_data, clean_name, frontmatter):
                    compiled["neural"] += 1
            elif "Two Rock" in amp_str or "Bloomfield" in amp_str:
                if mixwave_base_xml and compile_mixwave_toneprint(filepath, mixwave_base_xml, clean_name, frontmatter):
                    compiled["mixwave"] += 1
            elif any(x in amp_str for x in ["THR10", "THR30", "Yamaha THR", "THR-II", "THR II"]):
                if compile_yamaha_thr_toneprint(filepath, clean_name, frontmatter):
                    compiled["thr"] += 1
            elif any(x in amp_str.lower() for x in ["mrh810", "jcm800", "mrh"]):
                if compile_nembrini_xml_preset(filepath, str(NEMBRINI_TEMPLATES["mrh810"]), clean_name, frontmatter, "mrh810"):
                    compiled["mrh810"] += 1
            elif "Jazz Chorus" in amp_str or "JC120" in amp_str or "JC-120" in amp_str:
                if compile_nembrini_xml_preset(filepath, str(NEMBRINI_TEMPLATES["jc120"]), clean_name, frontmatter, "jc120"):
                    compiled["jc120"] += 1
            elif "Divided 11" in amp_str or "Div11" in amp_str or "Divided" in amp_str:
                if compile_nembrini_xml_preset(filepath, str(NEMBRINI_TEMPLATES["div11"]), clean_name, frontmatter, "div11"):
                    compiled["div11"] += 1
            elif "Acoustic Voice" in amp_str:
                if compile_nembrini_xml_preset(filepath, str(NEMBRINI_TEMPLATES["acoustic_voice"]), clean_name, frontmatter, "acoustic_voice"):
                    compiled["acoustic"] += 1
            elif "Puretone" in amp_str or "HK Puretone" in amp_str:
                if compile_nembrini_xml_preset(filepath, str(NEMBRINI_TEMPLATES["puretone"]), clean_name, frontmatter, "puretone"):
                    compiled["puretone"] += 1
            else:
                is_uad = any(x in amp_str for x in ["Dream", "Enigmatic", "Woodrow", "Ruby", "Showtime", "Lion"])
                if is_uad and uad_base_json and compile_uad_toneprint(filepath, uad_base_json, clean_name, frontmatter):
                    compiled["uad"] += 1

            # Auxiliary Signal Chain Effects
            if "la-2a" in content.lower():
                compiled_any_la2a = False
                if ("gray" in content.lower() or "grey" in content.lower()) and os.path.exists(LA2A_GRAY_BASE):
                    if compile_la2a_toneprint(filepath, str(LA2A_GRAY_BASE), clean_name, frontmatter):
                        compiled["la2a"] += 1
                        compiled_any_la2a = True
                if ("silver" in content.lower() or not compiled_any_la2a) and os.path.exists(LA2A_BASE):
                    if compile_la2a_toneprint(filepath, str(LA2A_BASE), clean_name, frontmatter):
                        compiled["la2a"] += 1

            if os.path.exists(HITSVILLE_BASE) and "hitsville" in content.lower():
                if compile_hitsville_toneprint(filepath, str(HITSVILLE_BASE), clean_name, frontmatter):
                    compiled["hitsville"] += 1

            if os.path.exists(GALAXY_BASE) and "galaxy" in content.lower():
                if compile_galaxy_toneprint(filepath, str(GALAXY_BASE), clean_name, frontmatter):
                    compiled["galaxy"] += 1

            if os.path.exists(STUDIO_D_BASE) and any(x in content.lower() for x in ["studio d", "dimension d", "dimension chorus"]):
                if compile_studio_d_toneprint(filepath, str(STUDIO_D_BASE), clean_name, frontmatter):
                    compiled["studiod"] += 1

            if os.path.exists(VALHALLA_BASE) and any(x in content.lower() for x in ["supermassive", "valhallasupermassive"]):
                if compile_supermassive_toneprint(filepath, str(VALHALLA_BASE), clean_name, frontmatter):
                    compiled["supermassive"] += 1

            if os.path.exists(LOGIC_EQ_BASE) and any(x in content.lower() for x in ["channel eq", "high-cut", "low-cut"]):
                if compile_logic_eq_toneprint(filepath, str(LOGIC_EQ_BASE), clean_name, frontmatter):
                    compiled["logiceq"] += 1

            if os.path.exists(LOGIC_COMP_BASE) and ("logic compressor" in content.lower() or ("compressor" in content.lower() and "la-2a" not in content.lower())):
                if compile_logic_compressor_toneprint(filepath, str(LOGIC_COMP_BASE), clean_name, frontmatter):
                    compiled["logiccomp"] += 1

            if os.path.exists(LOGIC_SPACEDESIGNER_BASE) and ("space designer" in content.lower() or "reverb aux" in content.lower()):
                if compile_logic_space_designer_toneprint(filepath, str(LOGIC_SPACEDESIGNER_BASE), clean_name, frontmatter):
                    compiled["spacedesigner"] += 1

            base_avp = NEMBRINI_TEMPLATES["acoustic_voice"]
            if os.path.exists(base_avp) and "acoustic voice" in content.lower():
                if compile_nembrini_xml_preset(filepath, str(base_avp), clean_name, frontmatter, "acoustic_voice"):
                    compiled["acoustic"] += 1

            compile_nembrini_stomp_presets(filepath, clean_name, frontmatter)
            compile_kuassa_stomp_presets(filepath, clean_name, frontmatter)

    print("\n==================================================")
    print("Rig Compilation Complete! Injected:")
    print(f"  -> {compiled['neural']} Neural DSP presets in {NEURAL_OUTPUT_DIR}")
    print(f"  -> {compiled['uad']} UAD Paradise presets in {PARADISE_DIR}")
    print(f"  -> {compiled['mixwave']} MixWave Two-Rock presets in {MIXWAVE_OUTPUT_DIR}")
    print(f"  -> {compiled['la2a']} UADx LA-2A presets in Silver/Gray folders")
    print(f"  -> {compiled['hitsville']} UADx Hitsville presets in {HITSVILLE_BASE.parent}")
    print(f"  -> {compiled['logiceq']} Logic Channel EQ presets in {LOGIC_EQ_BASE.parent}")
    print(f"  -> {compiled['logiccomp']} Logic Compressor presets in {LOGIC_COMP_BASE.parent}")
    print(f"  -> {compiled['spacedesigner']} Logic Space Designer presets in {LOGIC_SPACEDESIGNER_BASE.parent}")
    print(f"  -> {compiled['thr']} Yamaha THR presets in {YAMAHA_THR_OUTPUT_DIR}")
    print(f"  -> {compiled['mrh810']} Nembrini MRH810 XML presets in {NEMBRINI_TEMPLATES['mrh810'].parent}")
    print(f"  -> {compiled['jc120']} Nembrini Jazz Chorus XML presets in {NEMBRINI_TEMPLATES['jc120'].parent}")
    print(f"  -> {compiled['div11']} Nembrini Divided 11 XML presets in {NEMBRINI_TEMPLATES['div11'].parent}")
    print(f"  -> {compiled['acoustic']} Nembrini Acoustic Voice XML presets in {NEMBRINI_TEMPLATES['acoustic_voice'].parent}")
    print(f"  -> {compiled['puretone']} Nembrini Puretone XML presets in {NEMBRINI_TEMPLATES['puretone'].parent}")
    print(f"  -> {compiled['galaxy']} UADx Galaxy Tape Echo presets in {GALAXY_BASE.parent}")
    print(f"  -> {compiled['studiod']} UADx Studio D Chorus presets in {STUDIO_D_BASE.parent}")
    print(f"  -> {compiled['supermassive']} Valhalla Supermassive presets in {VALHALLA_BASE.parent}")
    print("==================================================")


if __name__ == "__main__":
    main()
