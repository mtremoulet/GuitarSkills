import xml.etree.ElementTree as ET
import os
import yaml
import glob
import re

# iD14 Input Pad state at -3.44 dB
VOLUME_PAD_STATE = "84.VMjLgrD....O+fWarAhckI2bo8la8HRLt.iHfTlai8FYo41Y8HRUTYTK3HxO9.BOyQWXzUFH18Fa00VY8HRKy3BMz.CLv.SMyPCL0biMwbiHu3C."

def java_hash(s):
    h = 0
    for char in s:
        h = (31 * h + ord(char)) & 0xffffffff
    return f"{h:x}"

def make_hidden_ports_string(num_controls=300):
    ports = [f"control_{i}" for i in range(num_controls)]
    ports.extend(["midi_in_0", "midi_out_0", "midi_in_1", "midi_out_1", "element_midi_input", "element_midi_output"])
    return ",".join(ports)

def parse_plugins_xml():
    plugins_path = "/Users/miketremoulet/Library/Application Support/Kushview/Element/plugins.xml"
    if not os.path.exists(plugins_path):
        print(f"Could not find plugins.xml at {plugins_path}")
        return {}
    
    tree = ET.parse(plugins_path)
    root = tree.getroot()
    
    db = {}
    for plugin in root.findall('PLUGIN'):
        name = plugin.get('name')
        format_val = plugin.get('format')
        # Prefer AudioUnit on Mac
        if format_val == 'AudioUnit':
            db[name] = {
                'name': name,
                'format': format_val,
                'identifier': plugin.get('file'),
                'uniqueId': plugin.get('uniqueId'),
                'numInputs': int(plugin.get('numInputs', '2')),
                'numOutputs': int(plugin.get('numOutputs', '2'))
            }
        elif name not in db: # Fallback to VST3/VST
            db[name] = {
                'name': name,
                'format': format_val,
                'identifier': plugin.get('file'),
                'uniqueId': plugin.get('uniqueId'),
                'numInputs': int(plugin.get('numInputs', '2')),
                'numOutputs': int(plugin.get('numOutputs', '2'))
            }
            
    # Manually add internal/built-in Element plugins since they might not be in the scanned list
    db['Audio Mixer'] = {
        'name': 'Audio Mixer',
        'format': 'Element',
        'identifier': 'element.audioMixer',
        'uniqueId': '0',
        'numInputs': 8,
        'numOutputs': 2
    }
    db['Volume'] = {
        'name': 'Volume',
        'format': 'Element',
        'identifier': 'element.volume.stereo',
        'uniqueId': '0',
        'numInputs': 2,
        'numOutputs': 2
    }
    return db

def map_amp_plugin(preset_data, amp_name, db):
    amp_platform = preset_data.get('amp_platform')
    
    if amp_platform:
        amp_platform = amp_platform.lower()
        if amp_platform == 'mixwave':
            return db.get("MixWave Two-Rock Bloomfield Drive")
        elif amp_platform == 'neural_dsp':
            return db.get("Archetype Cory Wong X")
        elif amp_platform == 'audio_hertz_ten_piece':
            return db.get("Ten Piece")
        elif amp_platform == 'uad_paradise':
            return db.get("UADx Paradise Guitar Studio")
        elif amp_platform == 'nembrini_jc120':
            return db.get("NA Jazz Chorus")
        elif amp_platform == 'nembrini_mrh810':
            return db.get("NA Mrh810 V2")
        elif amp_platform == 'nembrini_div11':
            return db.get("NA Divided 11")
        elif amp_platform == 'nembrini_puretone':
            return db.get("HK Puretone")
        elif amp_platform == 'nembrini_acoustic_voice' or amp_platform == 'acoustic':
            return db.get("NA Acoustic Voice Pro")
            
    # Direct keys in preset_data
    if 'nembrini_jc120' in preset_data:
        return db.get("NA Jazz Chorus")
    if 'nembrini_mrh810' in preset_data:
        return db.get("NA Mrh810 V2")
    if 'nembrini_div11' in preset_data:
        return db.get("NA Divided 11")
    if 'nembrini_puretone' in preset_data:
        return db.get("HK Puretone")
    if 'nembrini_acoustic_voice' in preset_data or 'nembrini_acoustic' in preset_data:
        return db.get("NA Acoustic Voice Pro")
        
    return None

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
    except Exception as e:
        print(f"Error parsing YAML in {md_path}: {e}")
        return None

def compile_session(md_path, db):
    data = parse_toneprint(md_path)
    if not data:
        return False
        
    preset_name = data.get('preset_name', os.path.basename(md_path).replace('.md', ''))
    preset_data = data.get('preset_data', {})
    if not preset_data:
        return False
        
    amp_platform = preset_data.get('amp_platform')
    if amp_platform in ['hardware', 'yamaha_thr']:
        return False
        
    amp_name = data.get('amp', '')
    
    # Build signal chains
    series_plugins = []
    parallel_plugins = []
    
    # 1. Drive Pedal (Boost/OD)
    drive_plugins = []
    if 'clon_minotaur' in preset_data:
        clon_plugin = db.get("NA Clon Minotaur")
        if clon_plugin:
            drive_plugins.append(clon_plugin)
            
    if 'kuassa_blues_barker' in preset_data:
        barker_plugin = db.get("Efektor Blues Barker")
        if barker_plugin:
            drive_plugins.append(barker_plugin)
            
    if 'kuassa_blues_river' in preset_data:
        river_plugin = db.get("Efektor Blues River")
        if river_plugin:
            drive_plugins.append(river_plugin)
            
    # 2. Compressor (LA-2A / 1176 / AUDynamicsProcessor)
    comp_plugins = []
    has_comp = False
    if 'la2a' in preset_data:
        la2a_plugin = db.get("UADx LA-2A Silver Compressor")
        if la2a_plugin:
            comp_plugins.append(la2a_plugin)
            has_comp = True
            
    if '1176' in preset_data or 'pgs_1176' in preset_data or 'standalone_1176' in preset_data:
        fet_plugin = db.get("UADx 1176LN Rev E Compressor")
        if fet_plugin:
            comp_plugins.append(fet_plugin)
            has_comp = True
            
    if 'logic_compressor' in preset_data and not has_comp:
        au_comp = db.get("AUDynamicsProcessor")
        if au_comp:
            comp_plugins.append(au_comp)
            
    # 3. Preamp Stage (UADx 610-B)
    preamp_plugins = []
    if 'ua_610b' in preset_data:
        preamp_plugin = db.get("UADx 610-B Preamp and EQ")
        if preamp_plugin:
            preamp_plugins.append(preamp_plugin)
            
    # 4. Amp Simulator
    amp_plugins = []
    amp_plugin = map_amp_plugin(preset_data, amp_name, db)
    if amp_plugin:
        amp_plugins.append(amp_plugin)
    elif preset_data.get('amp_platform') == 'tonex' or 'tonex' in preset_data or 'tonex_pedal' in preset_data:
        # Resolve TONEX amp simulator
        tonex_plugin = db.get("TONEX")
        if tonex_plugin:
            amp_plugins.append(tonex_plugin)

    # Auto-detect if compressor should go before amp
    comp_before_amp = False
    if has_comp or 'logic_compressor' in preset_data:
        if data.get('la2a_before_amp') or preset_data.get('la2a_before_amp') or data.get('compressor_before_amp') or preset_data.get('compressor_before_amp'):
            comp_before_amp = True
        else:
            try:
                with open(md_path, 'r') as f:
                    content = f.read()
                
                headers = re.findall(r'^###\s+(.*)$', content, re.MULTILINE)
                comp_idx = -1
                amp_idx = -1
                
                comp_keywords = ['la-2a', 'la2a', 'compressor', '1176', 'comp']
                amp_keywords = [
                    'ruby', 'two rock', 'bloomfield', 'cory wong', 'showtime', 
                    'dream', 'lion', 'woodrow', 'jazz chorus', 'mrh810', 
                    'divided 11', 'puretone', 'acoustic voice', 'tonex', 'paradise'
                ]
                
                for idx, header in enumerate(headers):
                    header_lower = header.lower()
                    if any(kw in header_lower for kw in comp_keywords) and comp_idx == -1:
                        comp_idx = idx
                    if any(kw in header_lower for kw in amp_keywords) and amp_idx == -1:
                        amp_idx = idx
                        
                if comp_idx != -1 and amp_idx != -1:
                    comp_before_amp = comp_idx < amp_idx
                else:
                    # Fallback to signal chain line check
                    for line in content.splitlines():
                        if '→' in line or '->' in line:
                            comp_pos = -1
                            amp_pos = -1
                            for kw in comp_keywords:
                                pos = line.lower().find(kw)
                                if pos != -1 and (comp_pos == -1 or pos < comp_pos):
                                    comp_pos = pos
                            for kw in amp_keywords:
                                pos = line.lower().find(kw)
                                if pos != -1 and (amp_pos == -1 or pos < amp_pos):
                                    amp_pos = pos
                            if comp_pos != -1 and amp_pos != -1:
                                comp_before_amp = comp_pos < amp_pos
                                break
            except Exception as e:
                print(f"Error auto-detecting plugin ordering: {e}")

    # Assemble series signal chain in correct order
    series_plugins.extend(drive_plugins)
    if comp_before_amp:
        series_plugins.extend(comp_plugins)
        series_plugins.extend(preamp_plugins)
        series_plugins.extend(amp_plugins)
    else:
        series_plugins.extend(preamp_plugins)
        series_plugins.extend(amp_plugins)
        series_plugins.extend(comp_plugins)
            
    # 5. Modulation (Studio D)
    if 'studio_d' in preset_data or 'studio_d_chorus' in preset_data:
        chorus_plugin = db.get("UADx Studio D Chorus")
        if chorus_plugin:
            series_plugins.append(chorus_plugin)
            
    # 6. Equalizer (Logic EQ / TDR Nova / MEqualizer / AUNBandEQ)
    if 'logic_eq' in preset_data:
        eq_plugin = db.get("TDR Nova") or db.get("Nova") or db.get("MEqualizer") or db.get("AUNBandEQ")
        if eq_plugin:
            series_plugins.append(eq_plugin)
            
    # 7. Studer Tape
    if 'studer' in preset_data:
        studer_plugin = db.get("UADx Studer A800 Tape Recorder")
        if studer_plugin:
            series_plugins.append(studer_plugin)
            
    # 7. Parallel Reverbs/Delays
    if 'hitsville' in preset_data:
        reverb_plugin = db.get("UADx Hitsville Reverb Chambers")
        if reverb_plugin:
            parallel_plugins.append(reverb_plugin)
    elif 'capitol' in preset_data or 'capitol_chambers' in preset_data:
        reverb_plugin = db.get("UADx Capitol Chambers")
        if reverb_plugin:
            parallel_plugins.append(reverb_plugin)
            
    if 'galaxy' in preset_data:
        delay_plugin = db.get("UADx Galaxy Tape Echo")
        if delay_plugin:
            parallel_plugins.append(delay_plugin)
            
    if 'supermassive' in preset_data:
        delay_plugin = db.get("ValhallaSupermassive")
        if delay_plugin:
            parallel_plugins.append(delay_plugin)
            
    # If no plugins resolved, it's hardware-only or skipped completely
    if not series_plugins and not parallel_plugins:
        return False
            
    # Determine output path
    category = os.path.basename(os.path.dirname(md_path))
    slug = os.path.basename(md_path).replace('.md', '')
    
    output_dir = f"/Users/miketremoulet/Music/Element/Sessions/Toneprints/{category}"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{slug}.els")
    
    # Generate the XML
    hidden_ports = make_hidden_ports_string()
    session_uuid = f"{slug}_graph_uuid"
    
    nodes_xml = []
    arcs_xml = []
    
    # Node 1: Audio Input (Internal)
    nodes_xml.append(f"""        <!-- Audio Input -->
        <Node id="1" format="Internal" identifier="audio.input" type="plugin"
              name="" relativeX="0.05" relativeY="0.32" pluginIdentifierString="Internal--da9d27b2-0"
              uuid="input_uuid_node_1" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="50.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Audio In 1" symbol="audio_in_1" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>""")
        
    # Set starting ID for plugins (leaving 1 for Input, 2 for Output)
    next_node_id = 3
    pad_node_id = next_node_id
    next_node_id += 1

    # Node: iD14 Input Pad (Volume)
    volume_plugin = db.get("Volume")
    volume_plugin['hash'] = java_hash(volume_plugin['identifier'])
    volume_plugin['pluginIdentifierString'] = f"{volume_plugin['format']}-{volume_plugin['name']}-{volume_plugin['hash']}-{volume_plugin['uniqueId']}"
    
    nodes_xml.append(f"""        <!-- iD14 Input Pad -->
        <Node id="{pad_node_id}" format="{volume_plugin['format']}" identifier="{volume_plugin['identifier']}" type="plugin"
              name="iD14 Input Pad" relativeX="0.15" relativeY="0.32"
              pluginIdentifierString="{volume_plugin['pluginIdentifierString']}"
              uuid="volume_pad_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="180.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1"
              state="{VOLUME_PAD_STATE}" programState="{VOLUME_PAD_STATE}">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input L" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input R" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="0" type="audio" name="Output L" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="3" channel="1" type="audio" name="Output R" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>""")
        
    # Connect input to pad
    arcs_xml.append(f'        <Arc sourceNode="1" sourcePort="0" destNode="{pad_node_id}" destPort="0"/>')
    arcs_xml.append(f'        <Arc sourceNode="1" sourcePort="0" destNode="{pad_node_id}" destPort="1"/>')
    
    current_src_node = pad_node_id
    current_src_port_l = 2
    current_src_port_r = 3
    
    # Add series plugins
    for i, plugin in enumerate(series_plugins):
        plugin['hash'] = java_hash(plugin['identifier'])
        plugin['pluginIdentifierString'] = f"{plugin['format']}-{plugin['name']}-{plugin['hash']}-{plugin['uniqueId']}"
        
        node_id = next_node_id
        next_node_id += 1
        x_pos = 180 + (i + 1) * 150
        
        oversample_factor = "1"
        if any(keyword in plugin['name'] for keyword in ["Bloomfield", "Efektor", "Minotaur", "808"]):
            oversample_factor = "8"
            
        num_in = plugin.get('numInputs', 2)
        num_out = plugin.get('numOutputs', 2)
        
        ports_list = []
        for p_idx in range(num_in):
            ports_list.append(f'            <Port index="{p_idx}" channel="{p_idx}" type="audio" name="Input {p_idx+1}" symbol="audio_in_{p_idx+1}" flow="input" hiddenOnBlock="0"/>')
        for p_idx in range(num_out):
            ports_list.append(f'            <Port index="{num_in + p_idx}" channel="{p_idx}" type="audio" name="Output {p_idx+1}" symbol="audio_out_{p_idx+1}" flow="output" hiddenOnBlock="0"/>')
        ports_str = "\n".join(ports_list)
            
        nodes_xml.append(f"""        <!-- {plugin['name']} -->
        <Node id="{node_id}" format="{plugin['format']}" identifier="{plugin['identifier']}" type="plugin"
              name="{plugin['name']}" relativeX="{(x_pos/1000):.2f}" relativeY="0.32"
              pluginIdentifierString="{plugin['pluginIdentifierString']}"
              uuid="node_uuid_{node_id}" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="{x_pos:.1f}" y="200.0" mute="0" muteInput="0" oversamplingFactor="{oversample_factor}" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
{ports_str}
          </ports>
        </Node>""")
        
        # Connect previous to this
        arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_l}" destNode="{node_id}" destPort="0"/>')
        arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_r}" destNode="{node_id}" destPort="1"/>')
        
        current_src_node = node_id
        current_src_port_l = num_in
        current_src_port_r = num_in + 1
        
    last_series_x = 180 + len(series_plugins) * 150
    mixer_needed = len(parallel_plugins) > 0
    
    if mixer_needed:
        parallel_nodes = []
        for i, plugin in enumerate(parallel_plugins):
            plugin['hash'] = java_hash(plugin['identifier'])
            plugin['pluginIdentifierString'] = f"{plugin['format']}-{plugin['name']}-{plugin['hash']}-{plugin['uniqueId']}"
            
            node_id = next_node_id
            next_node_id += 1
            parallel_nodes.append(node_id)
            
            x_pos = last_series_x + i * 150
            
            oversample_factor = "1"
            if any(keyword in plugin['name'] for keyword in ["Bloomfield", "Efektor", "Minotaur", "808"]):
                oversample_factor = "8"
                
            num_in = plugin.get('numInputs', 2)
            num_out = plugin.get('numOutputs', 2)
            
            ports_list = []
            for p_idx in range(num_in):
                ports_list.append(f'            <Port index="{p_idx}" channel="{p_idx}" type="audio" name="Input {p_idx+1}" symbol="audio_in_{p_idx+1}" flow="input" hiddenOnBlock="0"/>')
            for p_idx in range(num_out):
                ports_list.append(f'            <Port index="{num_in + p_idx}" channel="{p_idx}" type="audio" name="Output {p_idx+1}" symbol="audio_out_{p_idx+1}" flow="output" hiddenOnBlock="0"/>')
            ports_str = "\n".join(ports_list)
                
            nodes_xml.append(f"""        <!-- Parallel {plugin['name']} -->
        <Node id="{node_id}" format="{plugin['format']}" identifier="{plugin['identifier']}" type="plugin"
              name="{plugin['name']}" relativeX="{(x_pos/1000):.2f}" relativeY="0.6"
              pluginIdentifierString="{plugin['pluginIdentifierString']}"
              uuid="node_uuid_{node_id}" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="{x_pos:.1f}" y="380.0" mute="0" muteInput="0" oversamplingFactor="{oversample_factor}" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
{ports_str}
          </ports>
        </Node>""")
        
            # Connect end of series to parallel input
            arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_l}" destNode="{node_id}" destPort="0"/>')
            arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_r}" destNode="{node_id}" destPort="1"/>')
            
        # Add Audio Mixer
        mixer_plugin = db.get("Audio Mixer")
        mixer_plugin['hash'] = java_hash(mixer_plugin['identifier'])
        mixer_plugin['pluginIdentifierString'] = f"{mixer_plugin['format']}-{mixer_plugin['name']}-{mixer_plugin['hash']}-{mixer_plugin['uniqueId']}"
        
        mixer_node_id = next_node_id
        next_node_id += 1
        mixer_x = last_series_x + 150
        
        nodes_xml.append(f"""        <!-- Audio Mixer -->
        <Node id="{mixer_node_id}" format="{mixer_plugin['format']}" identifier="{mixer_plugin['identifier']}" type="plugin"
              name="{mixer_plugin['name']}" relativeX="{(mixer_x/1000):.2f}" relativeY="0.32"
              pluginIdentifierString="{mixer_plugin['pluginIdentifierString']}"
              uuid="mixer_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="{mixer_x:.1f}" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input L 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input R 1" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="2" type="audio" name="Input L 2" symbol="audio_in_3" flow="input" hiddenOnBlock="0"/>
            <Port index="3" channel="3" type="audio" name="Input R 2" symbol="audio_in_4" flow="input" hiddenOnBlock="0"/>
            <Port index="8" channel="0" type="audio" name="Output L" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="9" channel="1" type="audio" name="Output R" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>""")
        
        # Connect end of series to Mixer Channel 1 (Dry)
        arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_l}" destNode="{mixer_node_id}" destPort="0"/>')
        arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_r}" destNode="{mixer_node_id}" destPort="1"/>')
        
        # Connect parallel outputs to Mixer Channels 2 & 3
        for idx, (p_node, p_plugin) in enumerate(zip(parallel_nodes, parallel_plugins)):
            dest_port_l = 2 + idx * 2
            dest_port_r = 3 + idx * 2
            p_in = p_plugin.get('numInputs', 2)
            arcs_xml.append(f'        <Arc sourceNode="{p_node}" sourcePort="{p_in}" destNode="{mixer_node_id}" destPort="{dest_port_l}"/>')
            arcs_xml.append(f'        <Arc sourceNode="{p_node}" sourcePort="{p_in + 1}" destNode="{mixer_node_id}" destPort="{dest_port_r}"/>')
            
        output_x = mixer_x + 150
        
        nodes_xml.append(f"""        <!-- Audio Output -->
        <Node id="2" format="Internal" identifier="audio.output" type="plugin"
              name="" relativeX="{(output_x/1000):.2f}" relativeY="0.32" pluginIdentifierString="Internal--83a94619-0"
              uuid="output_uuid_node_2" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="{output_x:.1f}" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Audio Out 1" symbol="audio_out_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Audio Out 2" symbol="audio_out_2" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>""")
        
        # Connect Mixer to physical output
        arcs_xml.append(f'        <Arc sourceNode="{mixer_node_id}" sourcePort="8" destNode="2" destPort="0"/>')
        arcs_xml.append(f'        <Arc sourceNode="{mixer_node_id}" sourcePort="9" destNode="2" destPort="1"/>')
        
    else:
        output_x = last_series_x + 150
        nodes_xml.append(f"""        <!-- Audio Output -->
        <Node id="2" format="Internal" identifier="audio.output" type="plugin"
              name="" relativeX="{(output_x/1000):.2f}" relativeY="0.32" pluginIdentifierString="Internal--83a94619-0"
              uuid="output_uuid_node_2" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="{output_x:.1f}" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Audio Out 1" symbol="audio_out_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Audio Out 2" symbol="audio_out_2" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>""")
        
        # Connect end of series directly to output
        arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_l}" destNode="2" destPort="0"/>')
        arcs_xml.append(f'        <Arc sourceNode="{current_src_node}" sourcePort="{current_src_port_r}" destNode="2" destPort="1"/>')

    # Join XML blocks
    nodes_str = "\n".join(nodes_xml)
    arcs_str = "\n".join(arcs_xml)
    
    session_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<Session version="1" name="{preset_name}" tempo="120.0" notes="" beatsPerBar="4" beatDivisor="2">
  <graphs active="0">
    <Node version="1" type="Graph" uuid="{session_uuid}"
          name="Graph" bypass="0" persistent="1" renderMode="single" keyStart="0"
          keyEnd="127" transpose="0" delayCompensation="0" tempo="120.0">
      <nodes>
{nodes_str}
      </nodes>
      <scripts/>
      <ui>
        <Block/>
        <GraphEditorView width="1000" height="600"/>
      </ui>
      <arcs>
{arcs_str}
      </arcs>
      <ports>
        <Port index="0" channel="0" type="audio" name="Audio In 1" symbol="audio_in_1" flow="input"/>
        <Port index="1" channel="0" type="audio" name="Audio Out 1" symbol="audio_out_1" flow="output"/>
        <Port index="2" channel="1" type="audio" name="Audio Out 2" symbol="audio_out_2" flow="output"/>
      </ports>
    </Node>
  </graphs>
  <controllers/>
  <maps/>
</Session>
"""
    with open(output_path, "w") as f:
        f.write(session_xml)
    return True

def sweep_all_toneprints():
    db = parse_plugins_xml()
    if not db:
        print("Error loading plugin cache database.")
        return
        
    tones_dir = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"
    md_pattern = os.path.join(tones_dir, "**/*.md")
    md_files = glob.glob(md_pattern, recursive=True)
    
    success_count = 0
    skipped_count = 0
    
    print(f"Found {len(md_files)} Markdown files in tones/ directory.")
    
    for md_file in md_files:
        if os.path.basename(md_file).lower() == 'index.md':
            continue
            
        success = compile_session(md_file, db)
        if success:
            success_count += 1
            print(f"Generated Element session for: {os.path.basename(md_file)}")
        else:
            skipped_count += 1
            print(f"Skipped file (no supported blocks): {os.path.basename(md_file)}")
            
    print(f"\nSweep complete! Generated {success_count} sessions. Skipped {skipped_count} files.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 compile_element_session.py <path_to_toneprint_markdown> [--all]")
        print("To run the full sweep, explicitly pass the --all flag.")
        sys.exit(1)
        
    db = parse_plugins_xml()
    if not db:
        print("Error loading plugin cache database.")
        sys.exit(1)
        
    arg = sys.argv[1]
    if arg == '--all':
        sweep_all_toneprints()
    else:
        # Resolve target path
        if not os.path.exists(arg):
            print(f"Error: File not found at {arg}")
            sys.exit(1)
            
        success = compile_session(arg, db)
        if success:
            print(f"Successfully generated Element session for: {os.path.basename(arg)}")
        else:
            print(f"Failed or skipped generating session for: {os.path.basename(arg)}")
