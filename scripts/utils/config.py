"""Centralized path configuration and workspace environment resolution for GuitarSkills."""

import os
from pathlib import Path

# Workspace root
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent

# Tones directory
TONES_DIR = WORKSPACE_ROOT / "tones"

# Home & Library directories
HOME_DIR = Path.home()
USER_DOCS = HOME_DIR / "Documents"
USER_MUSIC = HOME_DIR / "Music"
USER_APP_SUPPORT = HOME_DIR / "Library" / "Application Support"
SYSTEM_AUDIO_PRESETS = Path("/Library/Audio/Presets")
SYSTEM_APP_SUPPORT = Path("/Library/Application Support")

# Neural DSP Paths
NEURAL_CORY_WONG_DIR = SYSTEM_AUDIO_PRESETS / "Neural DSP" / "Archetype Cory Wong X"
NEURAL_TEMPLATE = NEURAL_CORY_WONG_DIR / "User" / "Telecaster Tones.xml"
NEURAL_TEMPLATE_ALT = NEURAL_CORY_WONG_DIR / "Default.xml"
NEURAL_OUTPUT_DIR = NEURAL_CORY_WONG_DIR / "Toneprints"

# Universal Audio Paths
BASE_UAD_PRESETS_DIR = USER_DOCS / "Universal Audio" / "Presets" / "Plug-Ins"
PARADISE_DIR = BASE_UAD_PRESETS_DIR / "uaudio_paradise_guitar_studio"
PARADISE_TEMPLATE = PARADISE_DIR / "Non-Toneprints" / "Boutique Warm Clean - Enigmatic.json"
LA2A_BASE = BASE_UAD_PRESETS_DIR / "uaudio_teletronix_la-2a_silver" / "Mike - Alternative.json"
LA2A_GRAY_BASE = BASE_UAD_PRESETS_DIR / "uaudio_teletronix_la-2a_gray" / "Mike - Adjusting Gain Staging.json"
HITSVILLE_BASE = BASE_UAD_PRESETS_DIR / "uaudio_hitsville_chambers" / "Mike Live Strings.json"
GALAXY_BASE = BASE_UAD_PRESETS_DIR / "uaudio_galaxy_tape_echo" / "WhereAmI.json"
STUDIO_D_BASE = BASE_UAD_PRESETS_DIR / "uaudio_studio_d_chorus" / "whereami.json"

# Valhalla DSP Paths
VALHALLA_BASE = SYSTEM_APP_SUPPORT / "Valhalla DSP, LLC" / "ValhallaSupermassive" / "Presets" / "User" / "whereami.vpreset"

# Logic Pro Native Paths
LOGIC_SETTINGS_DIR = USER_MUSIC / "Audio Music Apps" / "Plug-In Settings"
LOGIC_EQ_BASE = LOGIC_SETTINGS_DIR / "Channel EQ" / "FlatEQ.pst"
LOGIC_COMP_BASE_ALT = LOGIC_SETTINGS_DIR / "Compressor" / "CompThreshNeg35.pst"
LOGIC_COMP_BASE_DEFAULT = LOGIC_SETTINGS_DIR / "Compressor" / "DefaultComp.pst"
LOGIC_COMP_BASE = LOGIC_COMP_BASE_ALT if LOGIC_COMP_BASE_ALT.exists() else LOGIC_COMP_BASE_DEFAULT
LOGIC_SPACEDESIGNER_BASE = LOGIC_SETTINGS_DIR / "Space Designer" / "TP-Wooden Studio Default.pst"

# MixWave Paths
MIXWAVE_DIR = SYSTEM_AUDIO_PRESETS / "MixWave" / "MixWave Two-Rock Bloomfield Drive" / "Presets"
MIXWAVE_TEMPLATE = MIXWAVE_DIR / "User" / "ToneprintTemplate.xml"
MIXWAVE_TEMPLATE_ALT = MIXWAVE_DIR / "User" / "Mike's Two Rocks.xml"
MIXWAVE_TEMPLATE_FACTORY = MIXWAVE_DIR / "Factory" / "LUSH CLEAN.xml"
MIXWAVE_OUTPUT_DIR = MIXWAVE_DIR / "User"

# Yamaha THR-II Paths
YAMAHA_THR_OUTPUT_DIR = TONES_DIR / "presets" / "yamaha"

# Nembrini Audio Paths
NEMBRINI_DOCS_DIR = USER_DOCS / "Nembrini Audio"
NEMBRINI_TEMPLATES = {
    "mrh810": NEMBRINI_DOCS_DIR / "NA Mrh810 V2" / "MRH810-All5.xml",
    "jc120": NEMBRINI_DOCS_DIR / "NA Jazz Chorus" / "JC_Base.xml",
    "div11": NEMBRINI_DOCS_DIR / "NA Divided 11" / "Div11-All5.xml",
    "acoustic_voice": NEMBRINI_DOCS_DIR / "NA Acoustic Voice Pro" / "AVP_Base.xml",
    "puretone": NEMBRINI_DOCS_DIR / "HK Puretone" / "HK_Base.xml",
}
