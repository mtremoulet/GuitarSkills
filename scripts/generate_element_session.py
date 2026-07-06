import xml.etree.ElementTree as ET
import os

def java_hash(s):
    h = 0
    for char in s:
        h = (31 * h + ord(char)) & 0xffffffff
    return f"{h:x}"

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
        # We prefer AudioUnit on Mac
        if format_val == 'AudioUnit':
            db[name] = {
                'name': name,
                'format': format_val,
                'identifier': plugin.get('file'),
                'uniqueId': plugin.get('uniqueId')
            }
        elif format_val == 'Element' and name in ['Audio Mixer', 'Volume']:
            db[name] = {
                'name': name,
                'format': format_val,
                'identifier': plugin.get('file'),
                'uniqueId': plugin.get('uniqueId')
            }
        elif name not in db: # Fallback to VST3 or VST
            db[name] = {
                'name': name,
                'format': format_val,
                'identifier': plugin.get('file'),
                'uniqueId': plugin.get('uniqueId')
            }
    return db

def make_hidden_ports_string(num_controls=300):
    ports = [f"control_{i}" for i in range(num_controls)]
    ports.extend(["midi_in_0", "midi_out_0", "midi_in_1", "midi_out_1", "element_midi_input", "element_midi_output"])
    return ",".join(ports)

def generate_two_rock(db):
    p_two_rock = db.get("MixWave Two-Rock Bloomfield Drive")
    p_la2a = db.get("UADx LA-2A Silver Compressor")
    p_hitsville = db.get("UADx Hitsville Reverb Chambers")
    p_mixer = db.get("Audio Mixer")
    p_volume = db.get("Volume")
    
    if not p_two_rock or not p_la2a or not p_hitsville or not p_mixer or not p_volume:
        print("Error: Could not find all required plugins in plugins.xml for Two-Rock!")
        return
    
    for p in [p_two_rock, p_la2a, p_hitsville, p_mixer, p_volume]:
        p['hash'] = java_hash(p['identifier'])
        p['pluginIdentifierString'] = f"{p['format']}-{p['name']}-{p['hash']}-{p['uniqueId']}"
        
    hidden_ports = make_hidden_ports_string()
    
    session_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<Session version="1" name="Two-Rock Bloomfield Clean" tempo="120.0" notes="" beatsPerBar="4" beatDivisor="2">
  <graphs active="0">
    <Node version="1" type="Graph" uuid="two_rock_bloomfield_clean_graph_uuid"
          name="Graph" bypass="0" persistent="1" renderMode="single" keyStart="0"
          keyEnd="127" transpose="0" delayCompensation="0" tempo="120.0">
      <nodes>
        <!-- Audio Input -->
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
        </Node>

        <!-- iD14 Input Pad (Volume) -->
        <Node id="7" format="{p_volume['format']}" identifier="{p_volume['identifier']}" type="plugin"
              name="iD14 Input Pad" relativeX="0.18" relativeY="0.32"
              pluginIdentifierString="{p_volume['pluginIdentifierString']}"
              uuid="volume_pad_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="180.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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
        </Node>

        <!-- MixWave Two-Rock Bloomfield Drive (Node 3) -->
        <Node id="3" format="{p_two_rock['format']}" identifier="{p_two_rock['identifier']}" type="plugin"
              name="{p_two_rock['name']}" relativeX="0.35" relativeY="0.32"
              pluginIdentifierString="{p_two_rock['pluginIdentifierString']}"
              uuid="two_rock_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="330.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input 2" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="0" type="audio" name="Output 1" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="3" channel="1" type="audio" name="Output 2" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- UADx LA-2A Silver Compressor (Node 4) -->
        <Node id="4" format="{p_la2a['format']}" identifier="{p_la2a['identifier']}" type="plugin"
              name="{p_la2a['name']}" relativeX="0.5" relativeY="0.32"
              pluginIdentifierString="{p_la2a['pluginIdentifierString']}"
              uuid="la2a_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="480.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input 2" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="0" type="audio" name="Output 1" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="3" channel="1" type="audio" name="Output 2" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- UADx Hitsville Reverb Chambers (Node 5) -->
        <Node id="5" format="{p_hitsville['format']}" identifier="{p_hitsville['identifier']}" type="plugin"
              name="{p_hitsville['name']}" relativeX="0.5" relativeY="0.6"
              pluginIdentifierString="{p_hitsville['pluginIdentifierString']}"
              uuid="hitsville_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="480.0" y="380.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input 2" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="0" type="audio" name="Output 1" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="3" channel="1" type="audio" name="Output 2" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- Audio Mixer (Node 6) -->
        <Node id="6" format="{p_mixer['format']}" identifier="{p_mixer['identifier']}" type="plugin"
              name="{p_mixer['name']}" relativeX="0.68" relativeY="0.32"
              pluginIdentifierString="{p_mixer['pluginIdentifierString']}"
              uuid="mixer_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="630.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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
        </Node>

        <!-- Audio Output (Node 2) -->
        <Node id="2" format="Internal" identifier="audio.output" type="plugin"
              name="" relativeX="0.85" relativeY="0.32" pluginIdentifierString="Internal--83a94619-0"
              uuid="output_uuid_node_2" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="780.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Audio Out 1" symbol="audio_out_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Audio Out 2" symbol="audio_out_2" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>
      </nodes>
      <scripts/>
      <ui>
        <Block/>
        <GraphEditorView width="1000" height="600"/>
      </ui>
      <arcs>
        <!-- Input 1 -> Volume Pad Inputs L & R -->
        <Arc sourceNode="1" sourcePort="0" destNode="7" destPort="0"/>
        <Arc sourceNode="1" sourcePort="0" destNode="7" destPort="1"/>

        <!-- Volume Pad Outputs -> Two-Rock Inputs 1 & 2 -->
        <Arc sourceNode="7" sourcePort="2" destNode="3" destPort="0"/>
        <Arc sourceNode="7" sourcePort="3" destNode="3" destPort="1"/>

        <!-- Two-Rock Outputs -> LA-2A Inputs -->
        <Arc sourceNode="3" sourcePort="2" destNode="4" destPort="0"/>
        <Arc sourceNode="3" sourcePort="3" destNode="4" destPort="1"/>

        <!-- LA-2A Outputs -> Mixer Inputs 1/2 (Dry Guitar) -->
        <Arc sourceNode="4" sourcePort="2" destNode="6" destPort="0"/>
        <Arc sourceNode="4" sourcePort="3" destNode="6" destPort="1"/>

        <!-- LA-2A Outputs -> Reverb (Hitsville) Inputs (Parallel Send) -->
        <Arc sourceNode="4" sourcePort="2" destNode="5" destPort="0"/>
        <Arc sourceNode="4" sourcePort="3" destNode="5" destPort="1"/>

        <!-- Reverb (Hitsville) Outputs -> Mixer Inputs 3/4 (Wet Reverb Return) -->
        <Arc sourceNode="5" sourcePort="2" destNode="6" destPort="2"/>
        <Arc sourceNode="5" sourcePort="3" destNode="6" destPort="3"/>

        <!-- Mixer Outputs -> Master Outputs -->
        <Arc sourceNode="6" sourcePort="8" destNode="2" destPort="0"/>
        <Arc sourceNode="6" sourcePort="9" destNode="2" destPort="1"/>
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
    output_path = "/Users/miketremoulet/claude-projects/GuitarSkills/TwoRockBloomfieldClean.els"
    with open(output_path, "w") as f:
        f.write(session_xml)
    print(f"Successfully generated {output_path} with Input Pad, Mixer Block, & hidden control ports!")

def generate_cory_wong(db):
    p_cory_wong = db.get("Archetype Cory Wong X")
    p_hitsville = db.get("UADx Hitsville Reverb Chambers")
    p_mixer = db.get("Audio Mixer")
    p_volume = db.get("Volume")
    
    if not p_cory_wong or not p_hitsville or not p_mixer or not p_volume:
        print("Error: Could not find required plugins in plugins.xml for Cory Wong!")
        return
    
    for p in [p_cory_wong, p_hitsville, p_mixer, p_volume]:
        p['hash'] = java_hash(p['identifier'])
        p['pluginIdentifierString'] = f"{p['format']}-{p['name']}-{p['hash']}-{p['uniqueId']}"
        
    hidden_ports = make_hidden_ports_string()
    
    session_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<Session version="1" name="Cory-Wong Amp Snob Clean" tempo="120.0" notes="" beatsPerBar="4" beatDivisor="2">
  <graphs active="0">
    <Node version="1" type="Graph" uuid="cory_wong_amp_snob_clean_graph_uuid"
          name="Graph" bypass="0" persistent="1" renderMode="single" keyStart="0"
          keyEnd="127" transpose="0" delayCompensation="0" tempo="120.0">
      <nodes>
        <!-- Audio Input -->
        <Node id="1" format="Internal" identifier="audio.input" type="plugin"
              name="" relativeX="0.08" relativeY="0.32" pluginIdentifierString="Internal--da9d27b2-0"
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
        </Node>

        <!-- iD14 Input Pad (Volume) -->
        <Node id="7" format="{p_volume['format']}" identifier="{p_volume['identifier']}" type="plugin"
              name="iD14 Input Pad" relativeX="0.18" relativeY="0.32"
              pluginIdentifierString="{p_volume['pluginIdentifierString']}"
              uuid="volume_pad_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="180.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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
        </Node>

        <!-- Archetype Cory Wong X (Node 3) -->
        <Node id="3" format="{p_cory_wong['format']}" identifier="{p_cory_wong['identifier']}" type="plugin"
              name="{p_cory_wong['name']}" relativeX="0.35" relativeY="0.32"
              pluginIdentifierString="{p_cory_wong['pluginIdentifierString']}"
              uuid="cory_wong_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="330.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input 2" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="0" type="audio" name="Output 1" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="3" channel="1" type="audio" name="Output 2" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- UADx Hitsville Reverb Chambers (Node 4 - Parallel Send) -->
        <Node id="4" format="{p_hitsville['format']}" identifier="{p_hitsville['identifier']}" type="plugin"
              name="{p_hitsville['name']}" relativeX="0.35" relativeY="0.6"
              pluginIdentifierString="{p_hitsville['pluginIdentifierString']}"
              uuid="hitsville_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="330.0" y="380.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input 2" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="0" type="audio" name="Output 1" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="3" channel="1" type="audio" name="Output 2" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- Audio Mixer (Node 5) -->
        <Node id="5" format="{p_mixer['format']}" identifier="{p_mixer['identifier']}" type="plugin"
              name="{p_mixer['name']}" relativeX="0.55" relativeY="0.32"
              pluginIdentifierString="{p_mixer['pluginIdentifierString']}"
              uuid="mixer_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="480.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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
        </Node>

        <!-- Audio Output (Node 2) -->
        <Node id="2" format="Internal" identifier="audio.output" type="plugin"
              name="" relativeX="0.75" relativeY="0.32" pluginIdentifierString="Internal--83a94619-0"
              uuid="output_uuid_node_2" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="630.0" y="200.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Audio Out 1" symbol="audio_out_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Audio Out 2" symbol="audio_out_2" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>
      </nodes>
      <scripts/>
      <ui>
        <Block/>
        <GraphEditorView width="1000" height="600"/>
      </ui>
      <arcs>
        <!-- Input 1 -> Volume Pad Inputs L & R -->
        <Arc sourceNode="1" sourcePort="0" destNode="7" destPort="0"/>
        <Arc sourceNode="1" sourcePort="0" destNode="7" destPort="1"/>

        <!-- Volume Pad -> Cory Wong Inputs 1 & 2 -->
        <Arc sourceNode="7" sourcePort="2" destNode="3" destPort="0"/>
        <Arc sourceNode="7" sourcePort="3" destNode="3" destPort="1"/>

        <!-- Cory Wong Outputs -> Mixer Inputs 1/2 (Dry Guitar) -->
        <Arc sourceNode="3" sourcePort="2" destNode="5" destPort="0"/>
        <Arc sourceNode="3" sourcePort="3" destNode="5" destPort="1"/>

        <!-- Cory Wong Outputs -> Reverb (Hitsville) Inputs (Parallel Send) -->
        <Arc sourceNode="3" sourcePort="2" destNode="4" destPort="0"/>
        <Arc sourceNode="3" sourcePort="3" destNode="4" destPort="1"/>

        <!-- Reverb (Hitsville) Outputs -> Mixer Inputs 3/4 (Wet Reverb Return) -->
        <Arc sourceNode="4" sourcePort="2" destNode="5" destPort="2"/>
        <Arc sourceNode="4" sourcePort="3" destNode="5" destPort="3"/>

        <!-- Mixer Outputs -> Master Outputs -->
        <Arc sourceNode="5" sourcePort="8" destNode="2" destPort="0"/>
        <Arc sourceNode="5" sourcePort="9" destNode="2" destPort="1"/>
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
    output_path = "/Users/miketremoulet/claude-projects/GuitarSkills/CoryWongAmpSnobClean.els"
    with open(output_path, "w") as f:
        f.write(session_xml)
    print(f"Successfully generated {output_path} with Input Pad, Mixer Block, & hidden control ports!")

if __name__ == "__main__":
    db = parse_plugins_xml()
    generate_two_rock(db)
    generate_cory_wong(db)
