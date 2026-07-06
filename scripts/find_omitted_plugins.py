import os
import yaml
import glob
import re

def parse_toneprint(md_path):
    with open(md_path, 'r') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
        
    try:
        data = yaml.safe_load(match.group(1))
        return data
    except Exception:
        return None

def analyze_omitted():
    tones_dir = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"
    md_files = glob.glob(os.path.join(tones_dir, "**/*.md"), recursive=True)
    
    # Supported keys in our updated compile_element_session.py:
    supported_keys = {
        'amp_platform', 'la2a', 'studer', 'hitsville', 'capitol', 'galaxy',
        'gold_overdrive', 'clon_minotaur', '1176', 'pgs_1176', 'standalone_1176',
        'logic_compressor', 'studio_d', 'studio_d_chorus', 'logic_eq',
        'supermassive', 'tonex', 'tonex_pedal', 'capitol_chambers', 'ua_610b',
        'nembrini_jc120', 'nembrini_mrh810', 'nembrini_div11', 'nembrini_puretone',
        'nembrini_acoustic_voice', 'nembrini_acoustic'
    }
    
    omitted_by_file = {}
    
    for md_file in md_files:
        if os.path.basename(md_file).lower() == 'index.md':
            continue
            
        # Skip directories that are not actual toneprints
        if 'eqprints' in md_file or 'transient-blunters' in md_file or 'slapback-defaults' in md_file:
            continue
            
        data = parse_toneprint(md_file)
        if not data:
            continue
            
        preset_data = data.get('preset_data', {})
        if not preset_data:
            continue
            
        file_omitted = []
        for key in preset_data.keys():
            if str(key) not in supported_keys and str(key) != 'amp_settings':
                file_omitted.append(str(key))
                
        # Also check if it's a hardware/yamaha_thr platform and skips the amp plugin entirely
        amp_platform = preset_data.get('amp_platform')
        if amp_platform in ['hardware', 'yamaha_thr']:
            file_omitted.append(f"amp_platform_skipped({amp_platform})")
            
        if file_omitted:
            category = os.path.basename(os.path.dirname(md_file))
            rel_path = f"{category}/{os.path.basename(md_file)}"
            omitted_by_file[rel_path] = file_omitted
            
    print("--- GENUINELY OMITTED PLUGINS REPORT ---")
    for file, keys in sorted(omitted_by_file.items()):
        print(f"{file}: {', '.join(keys)}")

if __name__ == "__main__":
    analyze_omitted()
