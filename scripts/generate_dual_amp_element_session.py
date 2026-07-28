import xml.etree.ElementTree as ET
import os

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
        if format_val == 'AudioUnit':
            db[name] = {
                'name': name,
                'format': format_val,
                'identifier': plugin.get('file'),
                'uniqueId': plugin.get('uniqueId'),
                'numInputs': int(plugin.get('numInputs', '2')),
                'numOutputs': int(plugin.get('numOutputs', '2'))
            }
        elif name not in db:
            db[name] = {
                'name': name,
                'format': format_val,
                'identifier': plugin.get('file'),
                'uniqueId': plugin.get('uniqueId'),
                'numInputs': int(plugin.get('numInputs', '2')),
                'numOutputs': int(plugin.get('numOutputs', '2'))
            }
            
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

def generate_dual_amp_session():
    db = parse_plugins_xml()
    if not db:
        print("Error: Could not load plugins.xml!")
        return

    p_paradise = db.get("UADx Paradise Guitar Studio")
    p_barker = db.get("Efektor Blues Barker")
    p_river = db.get("Efektor Blues River")
    p_clon = db.get("NA Clon Minotaur")
    p_808 = db.get("NA 808")
    p_la2a = db.get("UADx LA-2A Silver Compressor")
    p_hitsville = db.get("UADx Hitsville Reverb Chambers")
    p_mixer = db.get("Audio Mixer")
    p_volume = db.get("Volume")

    plugins = [p_paradise, p_barker, p_river, p_clon, p_808, p_la2a, p_hitsville, p_mixer, p_volume]
    for p in plugins:
        if p:
            p['hash'] = java_hash(p['identifier'])
            p['pluginIdentifierString'] = f"{p['format']}-{p['name']}-{p['hash']}-{p['uniqueId']}"

    hidden_ports = make_hidden_ports_string()

    session_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<Session version="1" name="Dual-Amp Dream 65 + Enigmatic 82" tempo="120.0" notes="" beatsPerBar="4" beatDivisor="2">
  <graphs active="0">
    <Node version="1" type="Graph" uuid="dual_amp_dream65_enigmatic82_graph_uuid"
          name="Graph" bypass="0" persistent="1" renderMode="single" keyStart="0"
          keyEnd="127" transpose="0" delayCompensation="0" tempo="120.0">
      <nodes>
        <!-- Audio Input (Node 1) -->
        <Node id="1" format="Internal" identifier="audio.input" type="plugin"
              name="" relativeX="0.05" relativeY="0.32" pluginIdentifierString="Internal--da9d27b2-0"
              uuid="input_uuid_node_1" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="50.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Audio In 1" symbol="audio_in_1" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- iD14 Input Pad (Node 7) -->
        <Node id="7" format="{p_volume['format']}" identifier="{p_volume['identifier']}" type="plugin"
              name="iD14 Input Pad" relativeX="0.15" relativeY="0.32"
              pluginIdentifierString="{p_volume['pluginIdentifierString']}"
              uuid="volume_pad_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="180.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1"
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
        </Node>

        <!-- PATH A: UADx Paradise Guitar Studio (Clean Dream '65 - Node 3) -->
        <Node id="3" format="{p_paradise['format']}" identifier="{p_paradise['identifier']}" type="plugin"
              name="UADx Paradise (Dream 65 Clean)" relativeX="0.35" relativeY="0.18"
              pluginIdentifierString="{p_paradise['pluginIdentifierString']}"
              uuid="dream65_paradise_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="400.0" y="120.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- PATH B - STAGE 1: Efektor Blues Barker (Marshall Bluesbreaker - Node 10) -->
        <Node id="10" format="{p_barker['format']}" identifier="{p_barker['identifier']}" type="plugin"
              name="{p_barker['name']}" relativeX="0.25" relativeY="0.48"
              pluginIdentifierString="{p_barker['pluginIdentifierString']}"
              uuid="blues_barker_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="280.0" y="380.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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

        <!-- PATH B - STAGE 1 (ALT): Efektor Blues River (TS-9 - Node 11) -->
        <Node id="11" format="{p_river['format']}" identifier="{p_river['identifier']}" type="plugin"
              name="{p_river['name']}" relativeX="0.33" relativeY="0.48"
              pluginIdentifierString="{p_river['pluginIdentifierString']}"
              uuid="blues_river_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="380.0" y="380.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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

        <!-- PATH B - STAGE 2: NA Clon Minotaur (Klon Centaur - Node 12) -->
        <Node id="12" format="{p_clon['format']}" identifier="{p_clon['identifier']}" type="plugin"
              name="{p_clon['name']}" relativeX="0.41" relativeY="0.48"
              pluginIdentifierString="{p_clon['pluginIdentifierString']}"
              uuid="clon_minotaur_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="480.0" y="380.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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

        <!-- PATH B - STAGE 3: NA 808 (Tube Screamer TS-808 - Node 13) -->
        <Node id="13" format="{p_808['format']}" identifier="{p_808['identifier']}" type="plugin"
              name="{p_808['name']}" relativeX="0.49" relativeY="0.48"
              pluginIdentifierString="{p_808['pluginIdentifierString']}"
              uuid="na_808_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="580.0" y="380.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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

        <!-- PATH B: UADx Paradise Guitar Studio (Driven Enigmatic '82 - Node 14) -->
        <Node id="14" format="{p_paradise['format']}" identifier="{p_paradise['identifier']}" type="plugin"
              name="UADx Paradise (Enigmatic 82 Driven)" relativeX="0.57" relativeY="0.48"
              pluginIdentifierString="{p_paradise['pluginIdentifierString']}"
              uuid="paradise_enigmatic_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="680.0" y="380.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- Amp Bus Mixer (Summing Path A & Path B - Node 6) -->
        <Node id="6" format="{p_mixer['format']}" identifier="{p_mixer['identifier']}" type="plugin"
              name="Amp Bus Mixer" relativeX="0.68" relativeY="0.32"
              pluginIdentifierString="{p_mixer['pluginIdentifierString']}"
              uuid="amp_bus_mixer_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="800.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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
            <Port index="4" channel="4" type="audio" name="Input L 3" symbol="audio_in_5" flow="input" hiddenOnBlock="0"/>
            <Port index="5" channel="5" type="audio" name="Input R 3" symbol="audio_in_6" flow="input" hiddenOnBlock="0"/>
            <Port index="8" channel="0" type="audio" name="Output L" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="9" channel="1" type="audio" name="Output R" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- UADx LA-2A Silver Compressor (Master Glue - Node 4) -->
        <Node id="4" format="{p_la2a['format']}" identifier="{p_la2a['identifier']}" type="plugin"
              name="{p_la2a['name']}" relativeX="0.78" relativeY="0.32"
              pluginIdentifierString="{p_la2a['pluginIdentifierString']}"
              uuid="la2a_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="920.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- UADx Hitsville Reverb Chambers (Shared Room - Node 5) -->
        <Node id="5" format="{p_hitsville['format']}" identifier="{p_hitsville['identifier']}" type="plugin"
              name="{p_hitsville['name']}" relativeX="0.86" relativeY="0.6"
              pluginIdentifierString="{p_hitsville['pluginIdentifierString']}"
              uuid="hitsville_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="1030.0" y="450.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- Master Output Mixer (Dry Dual-Amp vs Wet Reverb Return Blend - Node 8) -->
        <Node id="8" format="{p_mixer['format']}" identifier="{p_mixer['identifier']}" type="plugin"
              name="Master Output Mixer" relativeX="0.94" relativeY="0.32"
              pluginIdentifierString="{p_mixer['pluginIdentifierString']}"
              uuid="master_output_mixer_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="1140.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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
            <Port index="4" channel="4" type="audio" name="Input L 3" symbol="audio_in_5" flow="input" hiddenOnBlock="0"/>
            <Port index="5" channel="5" type="audio" name="Input R 3" symbol="audio_in_6" flow="input" hiddenOnBlock="0"/>
            <Port index="8" channel="0" type="audio" name="Output L" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="9" channel="1" type="audio" name="Output R" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- Audio Output (Node 2) -->
        <Node id="2" format="Internal" identifier="audio.output" type="plugin"
              name="" relativeX="1.0" relativeY="0.32" pluginIdentifierString="Internal--83a94619-0"
              uuid="output_uuid_node_2" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="1270.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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
        <GraphEditorView width="1400" height="700"/>
      </ui>
      <arcs>
        <!-- Input 1 -> Volume Pad Inputs L & R -->
        <Arc sourceNode="1" sourcePort="0" destNode="7" destPort="0"/>
        <Arc sourceNode="1" sourcePort="0" destNode="7" destPort="1"/>

        <!-- Volume Pad -> Path A: Paradise (Dream '65) -->
        <Arc sourceNode="7" sourcePort="2" destNode="3" destPort="0"/>
        <Arc sourceNode="7" sourcePort="3" destNode="3" destPort="1"/>

        <!-- Volume Pad -> Path B: Efektor Blues Barker (Stage 1) -->
        <Arc sourceNode="7" sourcePort="2" destNode="10" destPort="0"/>
        <Arc sourceNode="7" sourcePort="3" destNode="10" destPort="1"/>

        <!-- Path B Pedal Chain: Barker (10) -> River (11) -> Clon (12) -> 808 (13) -> Paradise (14) -->
        <Arc sourceNode="10" sourcePort="2" destNode="11" destPort="0"/>
        <Arc sourceNode="10" sourcePort="3" destNode="11" destPort="1"/>

        <Arc sourceNode="11" sourcePort="2" destNode="12" destPort="0"/>
        <Arc sourceNode="11" sourcePort="3" destNode="12" destPort="1"/>

        <Arc sourceNode="12" sourcePort="2" destNode="13" destPort="0"/>
        <Arc sourceNode="12" sourcePort="3" destNode="13" destPort="1"/>

        <Arc sourceNode="13" sourcePort="2" destNode="14" destPort="0"/>
        <Arc sourceNode="13" sourcePort="3" destNode="14" destPort="1"/>

        <!-- Path A: Paradise (Dream '65) Outputs -> Amp Bus Mixer Ch 1 (Inputs 0 & 1) -->
        <Arc sourceNode="3" sourcePort="2" destNode="6" destPort="0"/>
        <Arc sourceNode="3" sourcePort="3" destNode="6" destPort="1"/>

        <!-- Path B: Paradise Enigmatic Outputs -> Amp Bus Mixer Ch 2 (Inputs 2 & 3) -->
        <Arc sourceNode="14" sourcePort="2" destNode="6" destPort="2"/>
        <Arc sourceNode="14" sourcePort="3" destNode="6" destPort="3"/>

        <!-- Amp Bus Mixer Outputs -> LA-2A Silver Inputs (Master Glue) -->
        <Arc sourceNode="6" sourcePort="8" destNode="4" destPort="0"/>
        <Arc sourceNode="6" sourcePort="9" destNode="4" destPort="1"/>

        <!-- LA-2A Outputs -> Master Output Mixer Ch 1 (Dry Dual-Amp Sum) -->
        <Arc sourceNode="4" sourcePort="2" destNode="8" destPort="0"/>
        <Arc sourceNode="4" sourcePort="3" destNode="8" destPort="1"/>

        <!-- LA-2A Outputs -> Hitsville Reverb Inputs (Parallel Room Send) -->
        <Arc sourceNode="4" sourcePort="2" destNode="5" destPort="0"/>
        <Arc sourceNode="4" sourcePort="3" destNode="5" destPort="1"/>

        <!-- Hitsville Reverb Outputs -> Master Output Mixer Ch 2 (Wet Reverb Return) -->
        <Arc sourceNode="5" sourcePort="2" destNode="8" destPort="2"/>
        <Arc sourceNode="5" sourcePort="3" destNode="8" destPort="3"/>

        <!-- Master Output Mixer Outputs -> Physical Audio Output Node 2 -->
        <Arc sourceNode="8" sourcePort="8" destNode="2" destPort="0"/>
        <Arc sourceNode="8" sourcePort="9" destNode="2" destPort="1"/>
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
    output_dir = "/Users/miketremoulet/Music/Element/Sessions/Toneprints/humbuckers"
    os.makedirs(output_dir, exist_ok=True)
    out_path_1 = os.path.join(output_dir, "dual-amp-dream65-enigmatic82.els")
    out_path_2 = "/Users/miketremoulet/claude-projects/GuitarSkills/DualAmp_Dream65_Enigmatic82.els"

    with open(out_path_1, "w") as f:
        f.write(session_xml)
    with open(out_path_2, "w") as f:
        f.write(session_xml)

    print(f"Successfully generated Kushview Element dual-amp session with Master Output Mixer at:\n  - {out_path_1}\n  - {out_path_2}")

if __name__ == "__main__":
    generate_dual_amp_session()
