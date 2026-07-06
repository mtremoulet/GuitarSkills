import re
import glob

def clean_value(val_part):
    clean_val = val_part
    # strip outer quotes if present
    if clean_val.startswith('"') and clean_val.endswith('"'):
        clean_val = clean_val[1:-1]
    elif clean_val.startswith("'") and clean_val.endswith("'"):
        clean_val = clean_val[1:-1]
        
    # Replace escaped double quotes with regular double quotes
    clean_val = clean_val.replace('\\"', '"').replace('\\\\"', '"').replace('\\\"', '"').replace('\"', '"')
    
    # Wrap in single quotes, escaping internal single quotes
    clean_val = clean_val.replace("'", "''")
    return f"'{clean_val}'"

def fix_file(path):
    with open(path, 'r') as f:
        content = f.read()
        
    # Find frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return
        
    frontmatter = match.group(1)
    
    # We search for lines starting with target: or guitar:
    lines = frontmatter.split('\n')
    changed = False
    for i, line in enumerate(lines):
        striped = line.strip()
        if striped.startswith('target:') or striped.startswith('guitar:'):
            key = 'target' if striped.startswith('target:') else 'guitar'
            # Extract raw string after key:
            val_part = line.split(f'{key}:', 1)[1].strip()
            
            # Only fix if it contains double quotes or escape sequences inside
            if '\\"' in val_part or '\\\\' in val_part or ('"' in val_part and (val_part.startswith('"') and val_part.count('"') > 2)):
                new_val = clean_value(val_part)
                new_line = f"{key}: {new_val}"
                # Indentation preservation
                indent = line[:len(line) - len(striped)]
                new_line = indent + new_line
                
                if lines[i] != new_line:
                    lines[i] = new_line
                    changed = True
                
    if changed:
        new_frontmatter = '\n'.join(lines)
        new_content = content.replace(match.group(1), new_frontmatter, 1)
        with open(path, 'w') as f:
            f.write(new_content)
        print(f"Fixed YAML quotes in {path}")

if __name__ == "__main__":
    tones_dir = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"
    for p in glob.glob(f"{tones_dir}/**/*.md", recursive=True):
        if 'INDEX.md' not in p:
            fix_file(p)
