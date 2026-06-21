#!/usr/bin/env python3
"""
generate_tonex_amp_viewer.py
Queries the TONEX Library.db for all Amp, Cab, and Rig captures (non-stomps),
normalizes the data, groups them by Amp Model, and produces a self-contained,
high-fidelity web viewer in tone-advisor/tonex-amp-viewer.html.
"""

import os
import json
import sqlite3
import re
from pathlib import Path
from datetime import datetime

# Paths
DB_PATH = Path("/Users/miketremoulet/Documents/IK Multimedia/TONEX/Library.db")
OUTPUT_PATH = Path("/Users/miketremoulet/claude-projects/GuitarSkills/tone-advisor/tonex-amp-viewer.html")
BACKUP_DIR = "/Users/miketremoulet/Documents/IK Multimedia/TONEX/Backup/ToneModels"

# Comprehensive profiles mapping manufacturer:model to description paragraphs
AMP_DESCRIPTIONS = {
    # Benson
    "benson:chimera": "A boutique point-to-point hand-wired 30-watt amplifier utilizing four 6V6 power tubes. It is known for its beautiful, chimey, and three-dimensional clean tones that transition into a warm, harmonic overdrive. Popular in indie, ambient, and neo-soul genres for its responsiveness and note definition.",
    
    # Fender
    "fender:deluxe reverb 1963": "The quintessential 22-watt Blackface clean platform. Favored for its glassy top-end, scooped mids, and rich spring reverb. It is the gold standard for fingerstyle, blues, country, and jazz, providing a transparent canvas that responds beautifully to touch and pedals.",
    "fender:blackface deluxe reverb": "The quintessential 22-watt Blackface clean platform. Favored for its glassy top-end, scooped mids, and rich spring reverb. It is the gold standard for fingerstyle, blues, country, and jazz, providing a transparent canvas that responds beautifully to touch and pedals.",
    "fender:65 deluxe reverb": "The quintessential 22-watt Blackface clean platform. Favored for its glassy top-end, scooped mids, and rich spring reverb. It is the gold standard for fingerstyle, blues, country, and jazz, providing a transparent canvas that responds beautifully to touch and pedals.",
    "fender:vibroverb 1964": "Famous for its single 15-inch speaker setup, providing a deeper, rounder low-end and throatier midrange than a Deluxe Reverb. Made famous by Stevie Ray Vaughan, it offers a legendary blues clean and warm, stinging overdrive with incredible vocal qualities.",
    "fender:bassman 1963": "The legendary 6G6-B Tweed/Blonde Bassman. Known for its thick, punchy midrange, raw power-amp distortion, and robust cabinet thud. Ideal for classic rock, blues, and heavy fingerstyle playing.",
    "fender:tweed deluxe": "A vintage 15-watt Tweed combo utilizing two 6V6 power tubes. Known for its early breakup, highly interactive tone controls, and a fuzzy, saggy compression when pushed, famously utilized by Neil Young for raw rock and blues tones.",
    
    # Ampeg
    "ampeg:gemini i 1965": "A vintage 1960s classic often described as the 'Blue Check' jazz and blues amp. It offers a warm, dark, and smoky clean tone with a unique, luscious tremolo and reverb. Highly prized by jazz guitarists for its thick, woody voice that handles hollowbody guitars without harshness.",
    "ampeg:gemini ii 1965": "A vintage 1960s classic often described as the 'Blue Check' jazz and blues amp. It offers a warm, dark, and smoky clean tone with a unique, luscious tremolo and reverb. Highly prized by jazz guitarists for its thick, woody voice that handles hollowbody guitars without harshness.",
    
    # Henriksen
    "henriksen:bud 6": "An ultra-compact, high-performance solid-state jazz amplifier designed specifically for acoustic and archtop guitars. It delivers a completely flat, warm, and highly detailed sound that represents the natural acoustic voice of the instrument, a staple for modern jazz guitarists.",
    "henriksen:bud 6 - jazz": "An ultra-compact, high-performance solid-state jazz amplifier designed specifically for acoustic and archtop guitars. It delivers a completely flat, warm, and highly detailed sound that represents the natural acoustic voice of the instrument, a staple for modern jazz guitarists.",
    
    # Polytone
    "polytone:minibrute ii": "The legendary solid-state jazz box amp popularized by Joe Pass, Herb Ellis, and Jim Hall. Known for its dark, mid-forward, and extremely warm tone that eliminates fret noise and adds a woody thud to the bass strings. It is the classic sound of mainstream jazz.",
    
    # Two-Rock
    "two-rock:traditional clean": "Boutique high-headroom clean amplifier derived from the Dumble design lineage. Prized for its touch-sensitive performance, immense low-end control, and a glassy, vocal-like sustain. It is the premier platform for neo-soul, modern blues, and fingerstyle (John Mayer, Matt Schofield).",
    "two-rock:sss 2023": "A boutique high-headroom amplifier modeled after the legendary Dumble Steel String Singer. Offers immense low-end punch, incredible clarity across chords, and a glassy top-end that compression pedals love. Ideal for pristine neo-soul and modern blues.",
    "two-rock:ts-1": "Derived from the Dumble Overdrive Special circuit, this 50-watt boutique amp offers a highly dynamic clean channel and a smooth, harmonically rich overdrive channel that sings with vocal-like sustain.",
    "two-rock:ts-1 (dumble ods 50)": "Derived from the Dumble Overdrive Special circuit, this 50-watt boutique amp offers a highly dynamic clean channel and a smooth, harmonically rich overdrive channel that sings with vocal-like sustain.",
    
    # Dumble
    "dumble:ods": "The holy grail of boutique amplifiers. The Overdrive Special (ODS) is famous for its smooth, singing, violin-like overdrive and highly touch-sensitive clean channel, famously utilized by Larry Carlton and Robben Ford.",
    "dumble:overdrive": "The holy grail of boutique amplifiers. The Overdrive Special (ODS) is famous for its smooth, singing, violin-like overdrive and highly touch-sensitive clean channel, famously utilized by Larry Carlton and Robben Ford.",
    "dumble:tweedle dee": "Alexander Dumble's highly modified take on the Fender Tweed Deluxe circuit. Known for its organic compression, touch-sensitive breakup, and vocal qualities.",
    
    # Tone King
    "tone king:imperial mk. ii": "A boutique dual-channel amplifier designed to capture the best of vintage American tones. The rhythm channel delivers a pristine, glassy Blackface clean, while the lead channel offers Tweed-style mid-heavy growl, all running through a built-in attenuator.",
    "tone king:imperial mkii": "A boutique dual-channel amplifier designed to capture the best of vintage American tones. The rhythm channel delivers a pristine, glassy Blackface clean, while the lead channel offers Tweed-style mid-heavy growl, all running through a built-in attenuator.",
    "tone king:imperial preamp pedal": "A capture of the preamp stage of the Tone King Imperial, offering direct tone-shaping from clean Blackface sparkle to cranked Tweed mid-gain drive.",
    
    # Milkman
    "milkman:creamer": "A hand-wired boutique amp that blends a vintage Tweed-style power section with a Blackface-style preamp. It delivers a warm, sweet, and highly musical clean tone that naturally breaks up into a woody, compressed crunch, ideal for fingerstyle, country, and blues.",
    
    # Custom IR
    "custom ir:cabinet irs": "Custom Speaker Cabinet Impulse Responses loaded into your TONEX library. These files represent high-fidelity speaker captures using vintage microphones, designed to replace standard cabinet models.",
}

MANUFACTURER_PROFILES = {
    "Fender": "American-voiced classics known for high-end sparkle, scooped mids, and touch-sensitive cleans. Ideal for blues, country, jazz, and fingerstyle.",
    "Benson": "Boutique, hand-wired vintage-inspired circuits with rich second-harmonic content, saggy compression, and pristine chord clarity.",
    "Ampeg": "Mid-century American tone, highly regarded for dark, smoky jazz cleans and round, warm bass lines.",
    "Two-Rock": "High-end, Dumble-inspired boutique clean platforms with immense headroom, deep low-end definition, and glass-like highs.",
    "Dumble": "Extremely rare, highly customized amps known for vocal-like sustain, singing midrange, and touch-sensitive overdrive.",
    "Tone King": "Boutique designs blending Blackface sparkle and Tweed growl with modern attenuation.",
    "Henriksen": "State-of-the-art solid-state acoustic/jazz amps focusing on flat, uncolored frequency response to represent the guitar's raw tone.",
    "Polytone": "Vintage solid-state standard for archtop guitars, producing a dark, warm, mid-heavy thud.",
    "Milkman": "Boutique American-voiced tube amps optimized for clean headroom, sweet reverb, and dynamic fingerstyle response.",
    "Marshall": "British-voiced rock standard, characterized by a mid-forward bite, crunch, and Plexi scream.",
    "VOX": "Chimey British-voiced circuits utilizing EL84 tubes, providing a bright jangle and harmonic compression perfect for City Pop and indie rock.",
    "Orange": "Dark, thick British distortion with massive low-end and fuzzy crunch.",
    "Mesa Boogie": "Versatile American high-gain designs, ranging from smooth California cleans to aggressive modern metal rhythm.",
    "Custom IR": "High-fidelity impulse responses capturing specific speaker cabinets, speakers, and microphones.",
}

def parse_amp_name(amp_name, model_name, target_order):
    """
    Normalizes raw amp names to a standard (Manufacturer, Amp Model) tuple.
    Handles empty/blank amp names (often Custom IRs) and abbreviations.
    """
    if target_order == "5 - CustomIR" or not amp_name:
        return "Custom IR", "Cabinet IRs"
        
    name = " ".join(amp_name.split()).strip()
    lower = name.lower()
    
    manufacturer = "Other"
    model = name
    
    # Start with prefix checks
    if lower.startswith("fender") or lower.startswith("fndr") or lower.startswith("ally") or lower.startswith("alessandro") or lower.startswith("bassmin"):
        manufacturer = "Fender"
        if lower.startswith("fender"):
            model = name[6:].strip()
        elif lower.startswith("fndr"):
            model = name[4:].strip()
        elif lower.startswith("ally"):
            model = name[4:].strip()
        elif lower.startswith("alessandro"):
            model = name[10:].strip()
        elif lower.startswith("bassmin"):
            model = "Bassman 1963"
    elif lower.startswith("benson") or lower.startswith("ben"):
        manufacturer = "Benson"
        if lower.startswith("benson"):
            model = name[6:].strip()
        elif lower.startswith("ben"):
            model = name[3:].strip()
    elif lower.startswith("ampeg") or lower.startswith("ampg"):
        manufacturer = "Ampeg"
        if lower.startswith("ampeg"):
            model = name[5:].strip()
        elif lower.startswith("ampg"):
            model = name[4:].strip()
    elif lower.startswith("two-rock") or lower.startswith("two rock") or lower.startswith("trck"):
        manufacturer = "Two-Rock"
        if lower.startswith("two-rock"):
            model = name[8:].strip()
        elif lower.startswith("two rock"):
            model = name[8:].strip()
        elif lower.startswith("trck"):
            model = name[4:].strip()
    elif lower.startswith("dumble") or lower.startswith("dmbl"):
        manufacturer = "Dumble"
        if lower.startswith("dumble"):
            model = name[6:].strip()
        elif lower.startswith("dmbl"):
            model = name[4:].strip()
    elif lower.startswith("tone king") or lower.startswith("toneking") or lower.startswith("tk ") or lower.startswith("js imp") or lower.startswith("neural tk"):
        manufacturer = "Tone King"
        if lower.startswith("tone king"):
            model = name[9:].strip()
        elif lower.startswith("toneking"):
            model = name[8:].strip()
        elif lower.startswith("tk "):
            model = name[3:].strip()
        elif lower.startswith("js imp"):
            model = "Imperial Mk. II"
        elif lower.startswith("neural tk"):
            model = "Imperial MkII"
    elif lower.startswith("henriksen") or lower.startswith("mc henriksen"):
        manufacturer = "Henriksen"
        if lower.startswith("henriksen"):
            model = name[9:].strip()
        elif lower.startswith("mc henriksen"):
            model = name[12:].strip()
    elif lower.startswith("polytone") or lower.startswith("mc polytone"):
        manufacturer = "Polytone"
        if lower.startswith("polytone"):
            model = name[8:].strip()
        elif lower.startswith("mc polytone"):
            model = name[11:].strip()
    elif lower.startswith("milkman"):
        manufacturer = "Milkman"
        model = name[7:].strip()
    elif lower.startswith("joyo"):
        manufacturer = "Joyo"
        model = name[4:].strip()
    elif lower.startswith("vox") or lower.startswith("vx"):
        manufacturer = "VOX"
        if lower.startswith("vox"):
            model = name[3:].strip()
        elif lower.startswith("vx"):
            model = name[2:].strip()
    elif lower.startswith("marshall") or lower.startswith("ms"):
        manufacturer = "Marshall"
        if lower.startswith("marshall"):
            model = name[8:].strip()
    elif lower.startswith("mesa") or lower.startswith("mkv"):
        manufacturer = "Mesa Boogie"
        if lower.startswith("mesa"):
            model = name[4:].strip()
    elif lower.startswith("orange"):
        manufacturer = "Orange"
        model = name[6:].strip()
    elif lower.startswith("aguilar"):
        manufacturer = "Aguilar"
        model = name[7:].strip()
    elif lower.startswith("friedman"):
        manufacturer = "Friedman"
        model = name[8:].strip()
        
    # Standalone checks
    if manufacturer == "Other":
        if "deluxe reverb" in lower or "dlx" in lower:
            manufacturer = "Fender"
            model = "Deluxe Reverb"
        elif "bassman" in lower:
            manufacturer = "Fender"
            model = "Bassman"
        elif "twin" in lower:
            manufacturer = "Fender"
            model = "Twin Reverb"
        elif "princeton" in lower:
            manufacturer = "Fender"
            model = "Princeton Reverb"
        elif "chimera" in lower or "chime" in lower:
            manufacturer = "Benson"
            model = "Chimera"
        elif "gemini" in lower:
            manufacturer = "Ampeg"
            model = "Gemini"
        elif "two-rock" in lower or "two rock" in lower:
            manufacturer = "Two-Rock"
            model = "Traditional Clean"
        elif "dumble" in lower:
            manufacturer = "Dumble"
            model = "Overdrive Special"
        elif "imperial" in lower or "imp king" in lower:
            manufacturer = "Tone King"
            model = "Imperial Mk. II"
        elif "henriksen" in lower:
            manufacturer = "Henriksen"
            model = "Bud 6"
        elif "creamer" in lower:
            manufacturer = "Milkman"
            model = "Creamer"

    # Clean up model name
    model = model.strip()
    if model.startswith("-"):
        model = model[1:].strip()
    if model.startswith(":") :
        model = model[1:].strip()
        
    # Standardize
    if manufacturer == "Fender":
        if "bfdlx" in lower or "deluxe reverb" in lower:
            model = "Deluxe Reverb 1963"
        elif "bfvrb" in lower or "vibroverb" in lower:
            model = "Vibroverb 1964"
        elif "twdlx" in lower:
            model = "Tweed Deluxe"
        elif "bassman" in lower:
            model = "Bassman 1963"
    elif manufacturer == "Benson":
        if "chimera" in lower or "chime" in lower:
            model = "Chimera"
    elif manufacturer == "Ampeg":
        if "gemi" in lower or "gemini" in lower:
            if "gemi ii" in lower or "gemini ii" in lower:
                model = "Gemini II 1965"
            else:
                model = "Gemini I 1965"
    elif manufacturer == "Two-Rock":
        if "sss" in lower:
            model = "SSS 2023"
        elif "od50" in lower or "ts-1" in lower or "ts1" in lower:
            model = "TS-1 (Dumble ODS 50)"
        elif "tcl" in lower or "traditional clean" in lower:
            model = "Traditional Clean"
    elif manufacturer == "Dumble":
        if "ods" in lower or "overdrive" in lower:
            model = "ODS"
        elif "td" in lower or "tweedle" in lower:
            model = "Tweedle Dee"
            
    # Capitalize model if needed
    if model and model[0].islower() and not model.startswith("v1") and not model.startswith("v2"):
        model = model[0].upper() + model[1:]
        
    return manufacturer, model

def detect_version(model_name, creator):
    """
    Determines if a model is V1 or V2.
    TONEX Factory has explicit 'v2' in name.
    Tone Junkie uses 'V2 ET' or 'v2' in name.
    """
    lower = model_name.lower()
    
    # Check for V2 indications (word boundary or specific suffix)
    # Don't match V followed by number for Volume settings (like V2.5 or V6)
    if "v2.0" in lower or "v2 et" in lower:
        return "V2"
        
    # Check for standalone V2 or v2 (case-sensitive or insensitive word)
    if re.search(r'\bv2\b', lower):
        return "V2"
    if lower.endswith(" v2") or lower.endswith(" - v2") or lower.endswith(" v2.0") or lower.endswith("v2"):
        return "V2"
        
    # Special rule: Tone Junkie TS CHIME Benson captures in Mike's library are all V2 ET captures
    if creator == "Tone Junkie" and "chime" in lower:
        return "V2"
        
    # Check for V1
    if re.search(r'\bv1\b', lower) or lower.endswith(" v1") or lower.endswith(" v1.0") or lower.endswith("v1"):
        return "V1"
        
    return "V1"

def fetch_data():
    """Queries SQLite for all non-stomp captures and returns structured data."""
    if not DB_PATH.exists():
        raise FileNotFoundError(f"TONEX Library database not found at {DB_PATH}")
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = """
        SELECT 
          tm.GUID,
          tm.Tag_ModelName,
          tm.Tag_AmpName,
          tm.Tag_CabName,
          tm.Tag_ModelCategory,
          tm.Skin,
          tm.Factory,
          tm.Tag_Description,
          tm.Tag_ModelComment,
          tm.DateTimeAdded,
          tm.TargetOrder,
          nm.Nickname
        FROM ToneModels tm
        LEFT JOIN ToneModelsUserIDMatch um ON tm.GUID = um.GUID
        LEFT JOIN UserIDNicknameMatch nm ON um.UserID = nm.UserID
        WHERE tm.TargetOrder != '2 - Stomp'
        ORDER BY tm.Tag_AmpName, tm.Tag_ModelName
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    
    # TargetOrder mapping
    target_labels = {
        "0 - AmpAndCab": "Amp + Cab",
        "1 - ComplexRig": "Complex Rig",
        "2 - Stomp": "Stompbox",
        "3 - Amp": "Amp Only",
        "4 - StompAndAmp": "Stomp + Amp",
        "5 - CustomIR": "Custom IR",
    }
    
    captures = []
    for r in rows:
        guid, model_name, amp_name, cab_name, category, skin, factory, desc, comment, dt_added, target_order, nickname = r
        
        # Clean up category name
        cat_clean = category or ""
        if not cat_clean:
            # Try to infer from model name
            if "clean" in (model_name or "").lower():
                cat_clean = "CLEAN"
            elif "drive" in (model_name or "").lower() or "crunch" in (model_name or "").lower():
                cat_clean = "DRIVE"
            elif "lead" in (model_name or "").lower():
                cat_clean = "LEAD"
            else:
                cat_clean = "CLEAN"
        
        cat_clean = cat_clean.upper()
        if "HI-GAIN" in cat_clean or "HIGAIN" in cat_clean:
            cat_clean = "Hi-Gain"
        elif "CLEAN" in cat_clean:
            cat_clean = "Clean"
        elif "DRIVE" in cat_clean or "CRUNCH" in cat_clean:
            cat_clean = "Drive"
        elif "LEAD" in cat_clean:
            cat_clean = "Lead"
        else:
            cat_clean = "Clean"
            
        mfg, amp_model = parse_amp_name(amp_name or "", model_name or "", target_order)
        
        # Determine creator name
        if factory == 1:
            creator = "IK Multimedia"
        else:
            # Check prefixes in name
            first_word = (model_name or "").split()[0] if (model_name or "").split() else ""
            if first_word in ("TS", "TJ"):
                creator = "Tone Junkie"
            elif first_word == "AA" or nickname == "Amalgam Audio":
                creator = "Amalgam Audio"
            elif nickname:
                creator = nickname
            else:
                creator = "Imported / Community"
                
        version = detect_version(model_name or "", creator)
        
        # File Path
        file_path = f"{BACKUP_DIR}/{guid}.txm"
        file_exists = os.path.exists(file_path)
        
        captures.append({
            "guid": guid,
            "name": model_name or "Unnamed Capture",
            "raw_amp_name": amp_name or "",
            "cab_name": cab_name or "No Cab (DI)",
            "manufacturer": mfg,
            "amp_model": amp_model,
            "category": cat_clean,
            "skin": skin or "AmpCleanState",
            "factory": bool(factory),
            "description": desc or "",
            "comment": comment or "",
            "added": dt_added or "",
            "creator": creator,
            "version": version,
            "type": target_labels.get(target_order, target_order),
            "file_path": file_path,
            "file_exists": file_exists
        })
        
    return captures

def generate_html(captures):
    """Generates the HTML file containing the web viewer."""
    total_captures = len(captures)
    factory_count = sum(1 for c in captures if c["factory"])
    community_count = total_captures - factory_count
    v1_count = sum(1 for c in captures if c["version"] == "V1")
    v2_count = sum(1 for c in captures if c["version"] == "V2")
    
    categories = {}
    for c in captures:
        cat = c["category"]
        categories[cat] = categories.get(cat, 0) + 1
        
    # Group by manufacturer -> amp_model, attaching profiles
    grouped = {}
    for c in captures:
        mfg = c["manufacturer"]
        amp = c["amp_model"]
        
        # Resolve descriptive profile paragraph
        key = f"{mfg.lower()}:{amp.lower()}"
        description = AMP_DESCRIPTIONS.get(key) or AMP_DESCRIPTIONS.get(f"{mfg.lower()}:*") or MANUFACTURER_PROFILES.get(mfg) or "Boutique amplifier capture local to your library."
        
        if mfg not in grouped:
            grouped[mfg] = {}
        if amp not in grouped[mfg]:
            grouped[mfg][amp] = {
                "description": description,
                "captures": []
            }
            
        grouped[mfg][amp]["captures"].append(c)
        
    # Build list of manufacturers with counts
    mfg_list = []
    for mfg, amps in grouped.items():
        amp_count = len(amps)
        cap_count = sum(len(a_info["captures"]) for a_info in amps.values())
        mfg_list.append({
            "name": mfg,
            "amp_count": amp_count,
            "capture_count": cap_count
        })
    mfg_list.sort(key=lambda x: x["name"].lower())

    # Build the HTML template
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TONEX Amp Vault — Local Amps & Rigs</title>
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
      --accent: #5ba4c8;
      --accent-glow: rgba(91, 164, 200, 0.15);
      --accent-secondary: #00bcd4;
      --success: #10b981;
      
      --chip-bg: rgba(255, 255, 255, 0.02);
      --chip-hover: rgba(255, 255, 255, 0.06);
      --hover-bg: rgba(255, 255, 255, 0.03);
      
      --badge-clean-bg: rgba(16, 185, 129, 0.12);
      --badge-clean-text: #10b981;
      --badge-clean-border: rgba(16, 185, 129, 0.2);
      
      --badge-drive-bg: rgba(245, 158, 11, 0.12);
      --badge-drive-text: #f59e0b;
      --badge-drive-border: rgba(245, 158, 11, 0.2);
      
      --badge-lead-bg: rgba(239, 68, 68, 0.12);
      --badge-lead-text: #ef4444;
      --badge-lead-border: rgba(239, 68, 68, 0.2);
      
      --badge-higain-bg: rgba(168, 85, 247, 0.12);
      --badge-higain-text: #a855f7;
      --badge-higain-border: rgba(168, 85, 247, 0.2);
      
      --welcome-glow: radial-gradient(circle at top right, rgba(91, 164, 200, 0.03), transparent 40%);
    }}

    html[data-theme="light"] {{
      --bg: #f8fafc;
      --panel-bg: #ffffff;
      --panel-alt: #f1f5f9;
      --border: #e2e8f0;
      --border-focus: #cbd5e1;
      --text: #0f172a;
      --text-muted: #64748b;
      --accent: #0284c7;
      --accent-glow: rgba(2, 132, 199, 0.12);
      --accent-secondary: #0891b2;
      --success: #059669;
      
      --chip-bg: rgba(0, 0, 0, 0.02);
      --chip-hover: rgba(0, 0, 0, 0.05);
      --hover-bg: rgba(0, 0, 0, 0.03);
      
      --badge-clean-bg: rgba(5, 150, 105, 0.08);
      --badge-clean-text: #059669;
      --badge-clean-border: rgba(5, 150, 105, 0.15);
      
      --badge-drive-bg: rgba(217, 119, 6, 0.08);
      --badge-drive-text: #d97706;
      --badge-drive-border: rgba(217, 119, 6, 0.15);
      
      --badge-lead-bg: rgba(220, 38, 38, 0.08);
      --badge-lead-text: #dc2626;
      --badge-lead-border: rgba(220, 38, 38, 0.15);
      
      --badge-higain-bg: rgba(147, 51, 234, 0.08);
      --badge-higain-text: #9333ea;
      --badge-higain-border: rgba(147, 51, 234, 0.15);
      
      --welcome-glow: radial-gradient(circle at top right, rgba(2, 132, 199, 0.02), transparent 40%);
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

    /* --- App Header --- */
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
      background: linear-gradient(135deg, var(--accent), #0284c7);
      color: #fff;
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
      color: var(--accent);
      font-size: 14px;
    }}

    /* --- App Layout --- */
    .app-body {{
      display: flex;
      flex: 1;
      height: calc(100vh - 70px);
      max-height: calc(100vh - 70px);
      min-height: 0;
      overflow: hidden;
    }}

    /* --- Sidebar --- */
    .sidebar {{
      width: 330px;
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

    .mfg-amps {{
      margin-top: 2px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .amp-nav-item {{
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

    .amp-nav-item:hover {{
      background-color: var(--hover-bg);
    }}

    .amp-nav-item.active {{
      background-color: var(--accent-glow);
      color: var(--accent);
      font-weight: 600;
    }}

    .amp-nav-item .badge {{
      background-color: var(--chip-bg);
      color: var(--text-muted);
      font-size: 10px;
      font-weight: 600;
      padding: 2px 6px;
      border-radius: 10px;
    }}

    .amp-nav-item.active .badge {{
      background-color: var(--accent);
      color: #000;
    }}

    /* --- Main Workspace Panel --- */
    .main-workspace {{
      flex: 1;
      height: calc(100vh - 70px);
      max-height: calc(100vh - 70px);
      overflow-y: auto;
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

    /* --- Amp Detail Card --- */
    .amp-detail-card {{
      background-color: var(--panel-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
      transition: background-color 0.25s, border-color 0.25s;
      margin-bottom: 20px;
    }}

    /* Visual Amp Face Header */
    .amp-visual-header {{
      height: 180px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 30px 40px;
      overflow: hidden;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(135deg, #2b303c, #1a1e26);
    }}

    .amp-visual-header::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      opacity: 0.08;
      background: repeating-linear-gradient(90deg, transparent, transparent 4px, #fff 4px, #fff 8px);
      z-index: 1;
    }}

    .amp-visual-details {{
      position: relative;
      z-index: 2;
    }}

    .amp-visual-mfg {{
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      color: var(--accent);
      margin-bottom: 4px;
    }}

    .amp-visual-name {{
      font-size: 32px;
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      letter-spacing: -0.01em;
      color: #fff;
    }}

    .amp-controls {{
      display: flex;
      gap: 12px;
      position: relative;
      z-index: 2;
    }}

    .amp-knob-wrapper {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }}

    .amp-knob {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: radial-gradient(circle, #444 40%, #111 85%);
      border: 2px solid #000;
      box-shadow: 0 4px 6px rgba(0,0,0,0.5);
      position: relative;
    }}

    .amp-knob::after {{
      content: '';
      width: 2.5px;
      height: 12px;
      background-color: #ffaa00;
      position: absolute;
      top: 2px;
      left: calc(50% - 1.25px);
      border-radius: 1px;
      transform-origin: bottom center;
    }}

    .amp-knob-label {{
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      color: #8a99ad;
      letter-spacing: 0.05em;
    }}

    .knob-val-1::after {{ transform: rotate(-60deg); }}
    .knob-val-2::after {{ transform: rotate(10deg); }}
    .knob-val-3::after {{ transform: rotate(45deg); }}
    .knob-val-4::after {{ transform: rotate(-30deg); }}
    .knob-val-5::after {{ transform: rotate(80deg); }}

    /* Amp Brand Visual Themes */
    .theme-Fender {{ background: linear-gradient(135deg, #444, #1a1a1a); border-bottom: 6px solid #b0bec5; }}
    .theme-Fender .amp-visual-mfg {{ color: #b0bec5; }}
    .theme-Fender .amp-knob::after {{ background-color: #fff; }}

    .theme-Benson {{ background: linear-gradient(135deg, #c5a059, #5d4037); }}
    .theme-Benson .amp-visual-mfg {{ color: #fff; }}
    .theme-Benson .amp-knob::after {{ background-color: #ff5722; }}

    .theme-Two-Rock {{ background: linear-gradient(135deg, #263238, #10171d); border-bottom: 6px solid #00bcd4; }}
    .theme-Two-Rock .amp-visual-mfg {{ color: #00bcd4; }}
    .theme-Two-Rock .amp-knob::after {{ background-color: #00bcd4; }}

    .theme-Ampeg {{ background: linear-gradient(135deg, #0d47a1, #1a1a1a); border-bottom: 6px solid #cfd8dc; }}
    .theme-Ampeg .amp-visual-mfg {{ color: #90caf9; }}

    .theme-VOX {{ background: linear-gradient(135deg, #b71c1c, #2c3e50); }}
    .theme-VOX .amp-visual-mfg {{ color: #ffd54f; }}
    .theme-VOX .amp-knob::after {{ background-color: #fff; }}

    /* --- Amp Details Metadata --- */
    .amp-meta-details {{
      background-color: var(--panel-alt);
      padding: 18px 30px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 30px;
      font-size: 13px;
      transition: background-color 0.25s, border-color 0.25s;
    }}

    .amp-meta-item {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .amp-meta-item .label {{
      font-size: 10px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .amp-meta-item .val {{
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
      grid-template-columns: 2fr 1fr 1fr 1fr 1.2fr;
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

    .capture-subtitle {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    .cat-badge {{
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      display: inline-block;
      text-align: center;
    }}

    .cat-Clean {{ background-color: var(--badge-clean-bg); color: var(--badge-clean-text); border: 1px solid var(--badge-clean-border); }}
    .cat-Drive {{ background-color: var(--badge-drive-bg); color: var(--badge-drive-text); border: 1px solid var(--badge-drive-border); }}
    .cat-Lead {{ background-color: var(--badge-lead-bg); color: var(--badge-lead-text); border: 1px solid var(--badge-lead-border); }}
    .cat-Hi-Gain {{ background-color: var(--badge-higain-bg); color: var(--badge-higain-text); border: 1px solid var(--badge-higain-border); }}

    .capture-creator {{
      font-size: 12px;
      color: var(--text);
    }}

    .creator-sub {{
      font-size: 10px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .version-badge {{
      font-size: 10px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 12px;
      text-transform: uppercase;
      text-align: center;
      width: fit-content;
    }}

    .ver-V2 {{ background-color: rgba(0, 188, 212, 0.12); color: #00bcd4; border: 1px solid rgba(0, 188, 212, 0.2); }}
    .ver-V1 {{ background-color: rgba(120, 144, 156, 0.12); color: #78909c; border: 1px solid rgba(120, 144, 156, 0.2); }}

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
      color: #fff;
      font-weight: 600;
    }}

    html[data-theme="light"] .btn-primary {{
      color: #fff;
    }}

    .btn-primary:hover {{
      background-color: var(--border-focus);
      border-color: var(--border-focus);
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
      color: var(--accent);
      cursor: pointer;
      font-weight: 600;
    }}

    .filepath-panel .copy-path-btn:hover {{
      text-decoration: underline;
    }}

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
      <h1>Amp & Rig Vault</h1>
    </div>
    
    <div class="header-stats">
      <div class="stat-chip">
        <span>Amps:</span>
        <span class="val" id="amps-count-val">{sum(len(amps) for amps in grouped.values())} Models</span>
      </div>
      <div class="stat-chip">
        <span>Captures:</span>
        <span class="val" id="total-captures-val">{total_captures}</span>
      </div>
      <div class="stat-chip">
        <span>V2 Captures:</span>
        <span class="val" id="v2-captures-val">{v2_count}</span>
      </div>
      <div class="stat-chip">
        <span>Factory:</span>
        <span class="val">{factory_count}</span>
      </div>
      <div class="stat-chip">
        <span>Community:</span>
        <span class="val">{community_count}</span>
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
          <input type="text" class="search-input" id="search-input" placeholder="Search amps, cabinets, creators...">
        </div>
        
        <div class="filter-btn-group">
          <button class="filter-btn active" data-ver="all">All Versions</button>
          <button class="filter-btn" data-ver="V2">V2 Only</button>
          <button class="filter-btn" data-ver="V1">V1 Only</button>
          <button class="filter-btn" data-ver="factory">Factory</button>
        </div>
        
        <div class="source-filter">
          <button class="source-btn active" data-type="all">All Types</button>
          <button class="source-btn" data-type="Amp + Cab">Amp+Cab</button>
          <button class="source-btn" data-type="Amp Only">Amp Only</button>
          <button class="source-btn" data-type="Complex Rig">Rig</button>
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
        <div class="welcome-icon">🔊</div>
        <h2>TONEX Amp & Rig Vault</h2>
        <p>Welcome, Mike. This vault indexes your locally-saved TONEX amplifier and rig captures. It groups them by hardware model, identifies Tone Junkie V2 ET (Extended Training) versus V1 captures, and details their acoustic profiles.</p>
        <p style="font-size: 12px; margin-bottom: 0;">Select an amplifier model in the sidebar to view its captures and copy GUIDs directly into your Logic Pro templates or TONEX plugin.</p>
      </div>
    </div>
  </div>

  <div class="toast" id="toast">GUID copied to clipboard!</div>

  <script>
    // Injected JSON data
    const AMP_DATA = {json.dumps(grouped)};
    
    // Global state
    let activeMfg = "";
    let activeAmp = "";
    let currentSearch = "";
    let currentVersion = "all";
    let currentType = "all";

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
      const savedTheme = localStorage.getItem("tonex-amp-theme") || "dark";
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

      // Version filters
      document.querySelectorAll(".filter-btn").forEach(btn => {{
        btn.addEventListener("click", (e) => {{
          document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
          e.target.classList.add("active");
          currentVersion = e.target.getAttribute("data-ver");
          renderNav();
        }});
      }});

      // Type filters
      document.querySelectorAll(".source-btn").forEach(btn => {{
        btn.addEventListener("click", (e) => {{
          document.querySelectorAll(".source-btn").forEach(b => b.classList.remove("active"));
          e.target.classList.add("active");
          currentType = e.target.getAttribute("data-type");
          renderNav();
        }});
      }});
    }});

    function setTheme(theme) {{
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("tonex-amp-theme", theme);
      
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
      let uniqueAmps = 0;
      
      for (const mfg in AMP_DATA) {{
        const filteredAmps = {{}};
        for (const amp in AMP_DATA[mfg]) {{
          const ampObj = AMP_DATA[mfg][amp];
          const matches = ampObj.captures.filter(cap => {{
            // Search text filter
            const matchesSearch = 
              amp.toLowerCase().includes(currentSearch) ||
              mfg.toLowerCase().includes(currentSearch) ||
              cap.name.toLowerCase().includes(currentSearch) ||
              cap.creator.toLowerCase().includes(currentSearch) ||
              cap.guid.toLowerCase().includes(currentSearch) ||
              cap.cab_name.toLowerCase().includes(currentSearch);
            
            // Version / Factory filter
            let matchesVer = true;
            if (currentVersion === "V2") {{
              matchesVer = cap.version === "V2";
            }} else if (currentVersion === "V1") {{
              matchesVer = cap.version === "V1";
            }} else if (currentVersion === "factory") {{
              matchesVer = cap.factory === true;
            }}
            
            // Type filter
            const matchesType = currentType === "all" || cap.type === currentType;
              
            return matchesSearch && matchesVer && matchesType;
          }});
          
          if (matches.length > 0) {{
            filteredAmps[amp] = {{
              description: ampObj.description,
              captures: matches
            }};
            totalCount += matches.length;
            uniqueAmps++;
          }}
        }}
        if (Object.keys(filteredAmps).length > 0) {{
          filtered[mfg] = filteredAmps;
        }}
      }}
      
      document.getElementById("total-captures-val").innerText = totalCount;
      document.getElementById("amps-count-val").innerText = `${{uniqueAmps}} Models`;
      return filtered;
    }}

    // Sidebar navigation rendering
    function renderNav() {{
      const data = getFilteredData();
      navList.innerHTML = "";
      
      const sortedMfgs = Object.keys(data).sort((a, b) => a.localeCompare(b));
      
      if (sortedMfgs.length === 0) {{
        navList.innerHTML = `<div style="padding: 20px; color: var(--text-muted); text-align: center; font-size: 13px;">No matching amplifiers.</div>`;
        return;
      }}
      
      sortedMfgs.forEach(mfg => {{
        const mfgGroup = document.createElement("div");
        mfgGroup.className = "mfg-group";
        
        const mfgHeader = document.createElement("div");
        mfgHeader.className = "mfg-header";
        
        // Calculate captures count for this manufacturer
        let count = 0;
        for (const amp in data[mfg]) {{
          count += data[mfg][amp].captures.length;
        }}
        
        mfgHeader.innerHTML = `<span>${{mfg}}</span> <span style="opacity: 0.5; font-size: 10px;">${{count}}</span>`;
        mfgGroup.appendChild(mfgHeader);
        
        const mfgAmps = document.createElement("div");
        mfgAmps.className = "mfg-amps";
        mfgAmps.style.display = "flex";
        mfgAmps.style.flexDirection = "column";
        mfgAmps.style.gap = "2px";
        
        const sortedAmps = Object.keys(data[mfg]).sort((a, b) => a.localeCompare(b));
        sortedAmps.forEach(amp => {{
          const item = document.createElement("button");
          item.className = "amp-nav-item";
          if (activeMfg === mfg && activeAmp === amp) {{
            item.classList.add("active");
          }}
          
          const capCount = data[mfg][amp].captures.length;
          item.innerHTML = `<span>${{amp}}</span> <span class="badge">${{capCount}}</span>`;
          
          item.addEventListener("click", () => {{
            document.querySelectorAll(".amp-nav-item").forEach(b => b.classList.remove("active"));
            item.classList.add("active");
            activeMfg = mfg;
            activeAmp = amp;
            showAmpDetail(mfg, amp);
          }});
          
          mfgAmps.appendChild(item);
        }});
        
        mfgGroup.appendChild(mfgAmps);
        navList.appendChild(mfgGroup);
      }});
    }}

    // Display amp details in the main workspace
    function showAmpDetail(mfg, amp) {{
      const ampObj = AMP_DATA[mfg][amp];
      if (!ampObj) return;
      
      const captures = ampObj.captures;
      if (!captures || captures.length === 0) return;
      
      const description = ampObj.description;
      
      // Count types
      const types = [...new Set(captures.map(c => c.type))].join(", ");
      
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
              <span class="capture-subtitle">Cab: ${{cap.cab_name}}</span>
            </div>
            
            <div class="capture-category">
              <span class="cat-badge cat-${{cap.category}}">${{cap.category}}</span>
            </div>
            
            <div class="capture-creator">
              <span class="version-badge ver-${{cap.version}}">${{cap.version}}</span>
            </div>
            
            <div class="capture-creator">
              <div>${{sourceLabel}}</div>
              <div class="creator-sub">${{cap.type}}</div>
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
        <div class="amp-detail-card">
          <!-- Visual Amp Face Header -->
          <div class="amp-visual-header theme-${{mfg}}">
            <div class="amp-visual-details">
              <div class="amp-visual-mfg">${{mfg}}</div>
              <div class="amp-visual-name">${{amp}}</div>
            </div>
            <div class="amp-controls">
              <div class="amp-knob-wrapper">
                <div class="amp-knob knob-val-1"></div>
                <span class="amp-knob-label">Gain</span>
              </div>
              <div class="amp-knob-wrapper">
                <div class="amp-knob knob-val-2"></div>
                <span class="amp-knob-label">Treble</span>
              </div>
              <div class="amp-knob-wrapper">
                <div class="amp-knob knob-val-3"></div>
                <span class="amp-knob-label">Mids</span>
              </div>
              <div class="amp-knob-wrapper">
                <div class="amp-knob knob-val-4"></div>
                <span class="amp-knob-label">Bass</span>
              </div>
              <div class="amp-knob-wrapper">
                <div class="amp-knob knob-val-5"></div>
                <span class="amp-knob-label">Vol</span>
              </div>
            </div>
          </div>
          
          <!-- Metadata strip -->
          <div class="amp-meta-details">
            <div class="amp-meta-item">
              <span class="label">Amplifier Manufacturer</span>
              <span class="val">${{mfg}}</span>
            </div>
            <div class="amp-meta-item">
              <span class="label">Primary Formats</span>
              <span class="val">${{types}}</span>
            </div>
            <div class="amp-meta-item">
              <span class="label">Total Variants</span>
              <span class="val">${{captures.length}} captures</span>
            </div>
            <div class="amp-meta-item">
              <span class="label">Location</span>
              <span class="val">Documents/IK Multimedia/TONEX/Backup/ToneModels/</span>
            </div>
          </div>
          
          <!-- Amp Description Profile Block -->
          <div class="amp-description-box" style="padding: 24px 30px; border-bottom: 1px solid var(--border); background-color: var(--panel-alt); font-size: 13.5px; line-height: 1.65; color: var(--text-muted); transition: background-color 0.25s, border-color 0.25s;">
            <strong style="color: var(--text); display: block; margin-bottom: 6px; font-family: 'Outfit', sans-serif; font-size: 14px; letter-spacing: 0.02em; text-transform: uppercase;">Acoustic Profile</strong>
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

    // Global Action Helpers
    function copyGUID(guid) {{
      navigator.clipboard.writeText(guid).then(() => {{
        showToast("GUID copied to clipboard!");
      }}).catch(err => {{
        console.error("Failed to copy GUID: ", err);
      }});
    }}

    function copyText(text, message) {{
      navigator.clipboard.writeText(text).then(() => {{
        showToast(message);
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
    return html

def main():
    print("Fetching TONEX captures...")
    try:
        captures = fetch_data()
        print(f"Loaded {len(captures)} non-stomp captures from Library.db.")
    except Exception as e:
        print(f"Error reading TONEX database: {e}")
        return
        
    print("Generating HTML...")
    html_content = generate_html(captures)
    
    # Ensure directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_PATH, "w") as f:
        f.write(html_content)
        
    print(f"Success! TONEX Amp Vault compiled at {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
