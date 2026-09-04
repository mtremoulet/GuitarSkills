#!/usr/bin/env python3
"""
generate_mayer_trinity_element_session.py

Generates the canonical 3-Amp Parallel Mayer Trinity session for Kushview Element:
  - Node 1: Audio In
  - Node 18: Lookahead Limiter / Input protection
  - Node 7: Guitar In Pad (-3.4 dB)
  - Pre-Split Overdrive Staging:
      - Node 12: NA Clon Minotaur (Klon Centaur)
      - Node 10: Efektor Blues Barker (Marshall Bluesbreaker)
      - Node 11: Efektor Blues River (Boss BD-2 Keeley Phat Mod)
      - Node 13: NA 808 (Ibanez TS-10 / TS-808)
  - 3-Way Parallel Amp Matrix:
      - Node 3: UADx Paradise Guitar Studio (Showtime '64 — SSS Clean Anchor)
      - Node 14: UADx Paradise Guitar Studio (Dream '65 — 1964 Blackface Reverb Bloom)
      - Node 20: UADx Paradise Guitar Studio (Enigmatic '82 — Dumble ODS Vocal Mids)
  - Airwindows Consolidated Stereo Panning:
      - Node 15: Airwindows Pan (Showtime L12)
      - Node 16: Airwindows Pan (Dream Center)
      - Node 21: Airwindows Pan (Enigmatic R12)
  - Summing & Studio Post-FX:
      - Node 6: 3-Channel Amp Bus Mixer (-8 dB Pad)
      - Node 4: UADx LA-2A Silver Compressor (Master Submix Glue)
      - Node 5: UADx Hitsville Reverb Chambers (Parallel Room Reverb)
      - Node 8: Master Output Mixer (Dry Submix + Wet Hitsville Reverb)
      - Node 2: Audio Out (Headphone / Main Monitors)
      - Node 22: MIDI In (MIDI Automation Bus)
"""

import os
import xml.etree.ElementTree as ET

VOLUME_PAD_STATE = "84.VMjLgrD....O+fWarAhckI2bo8la8HRLt.iHfTlai8FYo41Y8HRUTYTK3HxO9.BOyQWXzUFH18Fa00VY8HRKy3BMz.CLv.SMyPCL0biMwbiHu3C."
AMP_BUS_MIXER_STATE = "422.VMjLgzY....O+fWarAhckI2bo8la8HRLt.iHfTlai8FYo41Y8HRUTYTK3HxO9.BOgUGYo8VaogWYxAhcuwVcsUVOhzxMtjCNv.CLxPCLyHSM4HyM2HBHsUGck0iHvHhO7PmbgM1ZfjlajUFd8HBLh.hX0MWRjgWOh.iHf3VcskjavUGcy0iHxHBHtUWaOUGcvUGcy0iHxHBHmEVZt0iHw3BLh.Ra0QWY8HBLh7hO7PmbgM1ZfjlajUFd8HRLh.hX0MWRjgWOhDiHf3VcskjavUGcy0iHxHBHtUWaOUGcvUGcy0iHxHBHmEVZt0iHw3BLh.Ra0QWY8HBLh7hO7PmbgM1ZfjlajUFd8HhLh.hX0MWRjgWOhHiHf3VcskjavUGcy0iHxHBHtUWaOUGcvUGcy0iHxHBHmEVZt0iHw3BLh.Ra0QWY8HBLh7hO7PmbgM1ZfjlajUFd8HxLh.hX0MWRjgWOhLiHf3VcskjavUGcy0iHxHBHtUWaOUGcvUGcy0iHxHBHmEVZt0iHw3BLh.Ra0QWY8HBLh7hO77RX0QVZu0VZ3Ulb9.."
AIRWINDOWS_PAN_L12_STATE = "716.hAGaoMGcv.C1AHv.DTfAGfPBJrvDTTgEWvUag4VclE1XzUmbkIGUjEFcgwUYrUVak4Fcs3VXsU1UyUmXzkGbkckckI2bo8laTQWdvU1WP7fZ0MVYPwVcmklaSQWXzUFUtEVakIAQzglbOAAe..............fCEruQX+C.M4bJmzfF.....3BFrgN.....ub32b8C...vKG9cW+....7xge60O....ub32e8Cf..vKG9MX+.H..7xgeGF.....ub32hA....vKG98X.....7xgeSF.....ub32kA.....QQfvC+.PSNKMCM3PDQESTxD8CPDELUkjavUGcQ+fDV8TczAWczIQXrYDVP.fDgUmY38TDAzkUCISHTE...vyO30FafXWYxMWZu4VOhDiKvHBHk41XuQVZtcVOhTEUF0BNh7iOfvSX2M1atM2arkFYgQWYjAxbzIWYg0VZtclUkI2bo8la8HBN0HCMh.xX0Imbk4FcPI2aiU1by8lbNEVak0iHPUmbkMGcDUWXrAUXtIBHgcGbeASOh.iK0HBHgcGbeESOh.iKybSN4jSN4jSMxLSL1HCNzHBHgcGbeISOh.iK0HBHgcGbeMSOh.iKzDSN4jSN4fiM3fiM4bCNwHBHgcGbeQSOh.iKvHBHgcGbeUSOh.iKvHBHgcGbeYSOh.iKvHBHgcGbecSOh.iKvHBHgcGbegSOh.iKvHBHgcGbekSOh.iKvHBHo4FakYWOh.iK0.SLwfyMx.SMyDCM1LiMxHBHuUGcrUlc8HBLtTCLwDCN2HCL0LSLzXyL1HiHfz1at8lPkgVX1k1a0IWOh.iHu3C.XUkazkFcrUFY.f..Y.fI.rB.3..P.fD.MAvW.PF.oA.5.zN.uCP7.PO.1C.+.7e.FDvBAzP.RHvb........BD..........X...................BvG"
AIRWINDOWS_PAN_R12_STATE = "716.hAGaoMGcv.C1AHv.DTfAGfPBJrvDTTgEWvUag4VclE1XzUmbkIGUjEFcgwUYrUVak4Fcs3VXsU1UyUmXzkGbkckckI2bo8laTQWdvU1WP7fZ0MVYPwVcmklaSQWXzUFUtEVakIAQzglbOAAe..............fCEruQX+C.M4bJmzfF.....3BFrgN.....ub32b8C...vKG9cW+....7xge60O....ub32e8Cf..vKG9MX+.H..7xgeGF.....ub32hA....vKG98X.....7xgeSF.....ub32kA.....QQfvC+.PSNKMCM3PDQESTxD8CPDELUkjavUGcQ+fDV8TczAWczIQXrYDVP.fDgUmY38TDAzkUCISHTE...vyO30FafXWYxMWZu4VOhDiKvHBHk41XuQVZtcVOhTEUF0BNh7iOfvSX2M1atM2arkFYgQWYjAxbzIWYg0VZtclUkI2bo8la8HBN0HCMh.xX0Imbk4FcPI2aiU1by8lbNEVak0iHPUmbkMGcDUWXrAUXtIBHgcGbeASOh.iK0HBHgcGbeESOh.iKyXSN4jSN4jSMxLSL1HCNzHBHgcGbeISOh.iK0HBHgcGbeMSOh.iKzPSN4jSN4fiM3fiM4bCNwHBHgcGbeQSOh.iKvHBHgcGbeUSOh.iKvHBHgcGbeYSOh.iKvHBHgcGbecSOh.iKvHBHgcGbegSOh.iKvHBHgcGbekSOh.iKvHBHo4FakYWOh.iK0.SLwfyMx.SMyDCM1LiMxHBHuUGcrUlc8HBLtTCLwDCN2HCL0LSLzXyL1HiHfz1at8lPkgVX1k1a0IWOh.iHu3C.XUkazkFcrUFY.f..Y.fI.rB.3..P.fD.MAvW.PF.oA.5.zN.uCP7.PO.1C.+.7e.FDvBAzP.RHvb........BD..........X...................BvG"
AIRWINDOWS_PAN_CTR_STATE = "716.hAGaoMGcv.C1AHv.DTfAGfPBJrvDTTgEWvUag4VclE1XzUmbkIGUjEFcgwUYrUVak4Fcs3VXsU1UyUmXzkGbkckckI2bo8laTQWdvU1WP7fZ0MVYPwVcmklaSQWXzUFUtEVakIAQzglbOAAe..............fCEruQX+C.M4bJmzfF.....3BFrgN.....ub32b8C...vKG9cW+....7xge60O....ub32e8Cf..vKG9MX+.H..7xgeGF.....ub32hA....vKG98X.....7xgeSF.....ub32kA.....QQfvC+.PSNKMCM3PDQESTxD8CPDELUkjavUGcQ+fDV8TczAWczIQXrYDVP.fDgUmY38TDAzkUCISHTE...vyO30FafXWYxMWZu4VOhDiKvHBHk41XuQVZtcVOhTEUF0BNh7iOfvSX2M1atM2arkFYgQWYjAxbzIWYg0VZtclUkI2bo8la8HBN0HCMh.xX0Imbk4FcPI2aiU1by8lbNEVak0iHPUmbkMGcDUWXrAUXtIBHgcGbeASOh.iK0HBHgcGbeESOh.iK0HBHgcGbeISOh.iK0HBHgcGbeMSOh.iK0HBHgcGbeQSOh.iKvHBHgcGbeUSOh.iKvHBHgcGbeYSOh.iKvHBHgcGbecSOh.iKvHBHgcGbegSOh.iKvHBHgcGbekSOh.iKvHBHo4FakYWOh.iK0.SLwfyMx.SMyDCM1LiMxHBHuUGcrUlc8HBLtTCLwDCN2HCL0LSLzXyL1HiHfz1at8lPkgVX1k1a0IWOh.iHu3C.XUkazkFcrUFY.f..Y.fI.rB.3..P.fD.MAvW.PF.oA.5.zN.uCP7.PO.1C.+.7e.FDvBAzP.RHvb........BD..........X...................BvG"

def make_hidden_ports_string(num_controls=300):
    ports = [f"control_{i}" for i in range(num_controls)]
    ports.extend(["midi_in_0", "midi_out_0", "midi_in_1", "midi_out_1", "element_midi_input", "element_midi_output"])
    return ",".join(ports)

def generate_mayer_trinity_session():
    hidden_ports = make_hidden_ports_string()

    # Authoritative plugin definitions from Element template
    p_paradise = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aumf,UI24,UADx",
        "pluginIdentifierString": "AudioUnit-UADx Paradise Guitar Studio-9ff1ac24-617d1b2a",
        "name": "UADx Paradise Guitar Studio"
    }
    p_barker = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,KEBB,KSS_",
        "pluginIdentifierString": "AudioUnit-Efektor Blues Barker-de3cf4ed-61637765",
        "name": "Efektor Blues Barker"
    }
    p_river = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,KEBR,KSS_",
        "pluginIdentifierString": "AudioUnit-Efektor Blues River-f98a7edd-61637775",
        "name": "Efektor Blues River"
    }
    p_clon = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,Nclm,NmAd",
        "pluginIdentifierString": "AudioUnit-NA Clon Minotaur-be955bff-617b4b71",
        "name": "NA Clon Minotaur"
    }
    p_808 = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,N808,NmAd",
        "pluginIdentifierString": "AudioUnit-NA 808-bd964bf9-617b4b71",
        "name": "NA 808"
    }
    p_airwindows = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,alFX,Dthr",
        "pluginIdentifierString": "AudioUnit-Airwindows Consolidated-688d2f90-616c4658",
        "name": "Airwindows Consolidated"
    }
    p_la2a = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,U3A9,UADx",
        "pluginIdentifierString": "AudioUnit-UADx LA-2A Silver Compressor-74b7858c-617d1b32",
        "name": "UADx LA-2A Silver Compressor"
    }
    p_hitsville = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,U3D7,UADx",
        "pluginIdentifierString": "AudioUnit-UADx Hitsville Reverb Chambers-2a4b868e-617d1b34",
        "name": "UADx Hitsville Reverb Chambers"
    }
    p_limiter = {
        "format": "AudioUnit",
        "identifier": "AudioUnit:Effects/aufx,Lkon,SBMA",
        "pluginIdentifierString": "AudioUnit-Lookahead Limiter-a8b23c91-617a7833",
        "name": "Lookahead Limiter"
    }
    p_mixer = {
        "format": "Element",
        "identifier": "element.audioMixer",
        "pluginIdentifierString": "Element-Audio Mixer-7ec0005-0",
        "name": "Audio Mixer"
    }
    p_volume = {
        "format": "Element",
        "identifier": "element.volume.stereo",
        "pluginIdentifierString": "Element-Volume-b98d75da-0",
        "name": "Volume"
    }

    session_xml = f"""<?xml version="1.0" encoding="UTF-8"?>

<Session version="1" name="Parallel Mayer Trinity 3-Amp" tempo="120.0" notes="Canonical 3-Amp Parallel John Mayer Trinity setup (Showtime '64 SSS Clean + Dream '65 1964 Blackface Bloom + Enigmatic '82 Dumble ODS Lead) with pre-split overdrive pedalboard (Clon, Blues Barker, Blues River BD-2, NA 808), Airwindows panning, 3-channel Amp Bus Mixer, LA-2A submix glue, and parallel Hitsville Reverb." beatsPerBar="4" beatDivisor="2">
  <graphs active="0">
    <Node version="1" type="Graph" uuid="mayer_trinity_3amp_graph_uuid"
          name="Graph" bypass="0" persistent="1" renderMode="single" keyStart="0"
          keyEnd="127" transpose="0" delayCompensation="0" tempo="120.0">
      <nodes>
        <!-- Audio Input (Node 1) -->
        <Node id="1" format="Internal" identifier="audio.input" type="plugin"
              name="" relativeX="0.04" relativeY="0.32" pluginIdentifierString="Internal--da9d27b2-0"
              uuid="input_uuid_node_1" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="40.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Audio In 1" symbol="audio_in_1" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- Input Protection / Limiter (Node 18) -->
        <Node id="18" format="{p_limiter['format']}" identifier="{p_limiter['identifier']}"
              type="plugin" name="Lookahead Limiter" relativeX="0.10" relativeY="0.32"
              pluginIdentifierString="{p_limiter['pluginIdentifierString']}"
              uuid="limiter_node_uuid" bypass="1" persistent="1" renderMode="single"
              keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="120.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- iD14 Input Pad (Node 7) -->
        <Node id="7" format="{p_volume['format']}" identifier="{p_volume['identifier']}" type="plugin"
              name="Guitar In Pad (-3.4dB)" relativeX="0.16" relativeY="0.32"
              pluginIdentifierString="{p_volume['pluginIdentifierString']}"
              uuid="volume_pad_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="200.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1"
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

        <!-- STOMP 1: NA Clon Minotaur (Klon Centaur - Node 12) -->
        <Node id="12" format="{p_clon['format']}" identifier="{p_clon['identifier']}" type="plugin"
              name="{p_clon['name']}" relativeX="0.23" relativeY="0.32"
              pluginIdentifierString="{p_clon['pluginIdentifierString']}"
              uuid="clon_minotaur_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="280.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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
            <Port index="8" channel="0" type="midi" name="MIDI In" symbol="element_midi_input" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- STOMP 2: Efektor Blues Barker (Marshall Bluesbreaker - Node 10) -->
        <Node id="10" format="{p_barker['format']}" identifier="{p_barker['identifier']}" type="plugin"
              name="{p_barker['name']}" relativeX="0.30" relativeY="0.32"
              pluginIdentifierString="{p_barker['pluginIdentifierString']}"
              uuid="blues_barker_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="360.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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
            <Port index="12" channel="0" type="midi" name="MIDI In" symbol="element_midi_input" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- STOMP 3: Efektor Blues River (Boss BD-2 Keeley Phat Mod - Node 11) -->
        <Node id="11" format="{p_river['format']}" identifier="{p_river['identifier']}" type="plugin"
              name="{p_river['name']}" relativeX="0.37" relativeY="0.32"
              pluginIdentifierString="{p_river['pluginIdentifierString']}"
              uuid="blues_river_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="440.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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
            <Port index="12" channel="0" type="midi" name="MIDI In" symbol="element_midi_input" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- STOMP 4: NA 808 (TS-10 / TS-808 - Node 13) -->
        <Node id="13" format="{p_808['format']}" identifier="{p_808['identifier']}" type="plugin"
              name="{p_808['name']}" relativeX="0.44" relativeY="0.32"
              pluginIdentifierString="{p_808['pluginIdentifierString']}"
              uuid="na_808_node_uuid" bypass="1" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="520.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="8" enabled="1">
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
            <Port index="8" channel="0" type="midi" name="MIDI In" symbol="element_midi_input" flow="input" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- PARALLEL AMP 1: UADx Paradise (Showtime '64 — SSS Clean Anchor - Node 3) -->
        <Node id="3" format="{p_paradise['format']}" identifier="{p_paradise['identifier']}" type="plugin"
              name="UADx Paradise (Showtime SSS Clean)" relativeX="0.55" relativeY="0.12"
              pluginIdentifierString="{p_paradise['pluginIdentifierString']}"
              uuid="showtime_paradise_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="620.0" y="100.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- Airwindows Pan (Amp 1: Showtime L12 - Node 15) -->
        <Node id="15" format="{p_airwindows['format']}" identifier="{p_airwindows['identifier']}" type="plugin"
              name="Airwindows Pan (Showtime L12)" relativeX="0.68" relativeY="0.12"
              pluginIdentifierString="{p_airwindows['pluginIdentifierString']}"
              uuid="showtime_airwindows_pan_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="760.0" y="100.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1"
              state="{AIRWINDOWS_PAN_L12_STATE}" programState="{AIRWINDOWS_PAN_L12_STATE}">
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

        <!-- PARALLEL AMP 2: UADx Paradise (Dream '65 — 1964 Blackface Bloom - Node 14) -->
        <Node id="14" format="{p_paradise['format']}" identifier="{p_paradise['identifier']}" type="plugin"
              name="UADx Paradise (Dream 65 Bloom)" relativeX="0.55" relativeY="0.32"
              pluginIdentifierString="{p_paradise['pluginIdentifierString']}"
              uuid="dream65_paradise_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="620.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- Airwindows Pan (Amp 2: Dream Center - Node 16) -->
        <Node id="16" format="{p_airwindows['format']}" identifier="{p_airwindows['identifier']}" type="plugin"
              name="Airwindows Pan (Dream Center)" relativeX="0.68" relativeY="0.32"
              pluginIdentifierString="{p_airwindows['pluginIdentifierString']}"
              uuid="dream_airwindows_pan_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="760.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1"
              state="{AIRWINDOWS_PAN_CTR_STATE}" programState="{AIRWINDOWS_PAN_CTR_STATE}">
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

        <!-- PARALLEL AMP 3: UADx Paradise (Enigmatic '82 — Dumble ODS Vocal Lead - Node 20) -->
        <Node id="20" format="{p_paradise['format']}" identifier="{p_paradise['identifier']}" type="plugin"
              name="UADx Paradise (Enigmatic 82 Lead)" relativeX="0.55" relativeY="0.52"
              pluginIdentifierString="{p_paradise['pluginIdentifierString']}"
              uuid="enigmatic_paradise_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="620.0" y="400.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- Airwindows Pan (Amp 3: Enigmatic R12 - Node 21) -->
        <Node id="21" format="{p_airwindows['format']}" identifier="{p_airwindows['identifier']}" type="plugin"
              name="Airwindows Pan (Enigmatic R12)" relativeX="0.68" relativeY="0.52"
              pluginIdentifierString="{p_airwindows['pluginIdentifierString']}"
              uuid="enigmatic_airwindows_pan_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="760.0" y="400.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1"
              state="{AIRWINDOWS_PAN_R12_STATE}" programState="{AIRWINDOWS_PAN_R12_STATE}">
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

        <!-- 3-Channel Amp Bus Mixer (Summing Showtime, Dream, Enigmatic - Node 6) -->
        <Node id="6" format="{p_mixer['format']}" identifier="{p_mixer['identifier']}" type="plugin"
              name="Amp Bus Mixer (-8dB Pad)" relativeX="0.77" relativeY="0.32"
              pluginIdentifierString="{p_mixer['pluginIdentifierString']}"
              uuid="amp_bus_mixer_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="890.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1"
              state="{AMP_BUS_MIXER_STATE}" programState="{AMP_BUS_MIXER_STATE}">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input #0 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input #0 2" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="2" type="audio" name="Input #1 3" symbol="audio_in_3" flow="input" hiddenOnBlock="0"/>
            <Port index="3" channel="3" type="audio" name="Input #1 4" symbol="audio_in_4" flow="input" hiddenOnBlock="0"/>
            <Port index="4" channel="4" type="audio" name="Input #2 5" symbol="audio_in_5" flow="input" hiddenOnBlock="0"/>
            <Port index="5" channel="5" type="audio" name="Input #2 6" symbol="audio_in_6" flow="input" hiddenOnBlock="0"/>
            <Port index="6" channel="6" type="audio" name="Input #3 7" symbol="audio_in_7" flow="input" hiddenOnBlock="0"/>
            <Port index="7" channel="7" type="audio" name="Input #3 8" symbol="audio_in_8" flow="input" hiddenOnBlock="0"/>
            <Port index="8" channel="0" type="audio" name="Master 1" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="9" channel="1" type="audio" name="Master 2" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- UADx LA-2A Silver Compressor (Master Glue - Node 4) -->
        <Node id="4" format="{p_la2a['format']}" identifier="{p_la2a['identifier']}" type="plugin"
              name="{p_la2a['name']}" relativeX="0.84" relativeY="0.32"
              pluginIdentifierString="{p_la2a['pluginIdentifierString']}"
              uuid="la2a_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="990.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- UADx Hitsville Reverb Chambers (Parallel Room Reverb - Node 5) -->
        <Node id="5" format="{p_hitsville['format']}" identifier="{p_hitsville['identifier']}" type="plugin"
              name="{p_hitsville['name']}" relativeX="0.91" relativeY="0.55"
              pluginIdentifierString="{p_hitsville['pluginIdentifierString']}"
              uuid="hitsville_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="1080.0" y="430.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- Master Output Mixer (Dry Dual/Triple-Amp vs Wet Reverb Return - Node 8) -->
        <Node id="8" format="{p_mixer['format']}" identifier="{p_mixer['identifier']}" type="plugin"
              name="Master Output Mixer" relativeX="0.95" relativeY="0.32"
              pluginIdentifierString="{p_mixer['pluginIdentifierString']}"
              uuid="master_output_mixer_node_uuid" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="1170.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block portAlignment="before" hiddenPorts="{hidden_ports}"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="audio" name="Input #0 1" symbol="audio_in_1" flow="input" hiddenOnBlock="0"/>
            <Port index="1" channel="1" type="audio" name="Input #0 2" symbol="audio_in_2" flow="input" hiddenOnBlock="0"/>
            <Port index="2" channel="2" type="audio" name="Input #1 3" symbol="audio_in_3" flow="input" hiddenOnBlock="0"/>
            <Port index="3" channel="3" type="audio" name="Input #1 4" symbol="audio_in_4" flow="input" hiddenOnBlock="0"/>
            <Port index="8" channel="0" type="audio" name="Master 1" symbol="audio_out_1" flow="output" hiddenOnBlock="0"/>
            <Port index="9" channel="1" type="audio" name="Master 2" symbol="audio_out_2" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>

        <!-- Audio Output (Node 2) -->
        <Node id="2" format="Internal" identifier="audio.output" type="plugin"
              name="" relativeX="1.0" relativeY="0.32" pluginIdentifierString="Internal--83a94619-0"
              uuid="output_uuid_node_2" bypass="0" persistent="1"
              renderMode="single" keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="1280.0" y="250.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
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

        <!-- MIDI Input (Node 22) -->
        <Node id="22" format="Internal" identifier="midi.input" type="plugin"
              name="" relativeX="0.23" relativeY="0.08" pluginIdentifierString="Internal--8883bb51-0"
              uuid="midi_input_node_22" bypass="0" persistent="1" renderMode="single"
              keyStart="0" keyEnd="127" transpose="0" delayCompensation="0.0"
              tempo="120.0" x="280.0" y="60.0" mute="0" muteInput="0" oversamplingFactor="1" enabled="1">
          <nodes/>
          <scripts/>
          <ui>
            <Block displayMode="compact" portAlignment="before"/>
          </ui>
          <ports>
            <Port index="0" channel="0" type="midi" name="MIDI In 1" symbol="midi_in_1" flow="output" hiddenOnBlock="0"/>
          </ports>
        </Node>
      </nodes>

      <arcs>
        <!-- 1. Input Routing: Audio In 1 -> Limiter -> Guitar In Pad -->
        <Arc sourceNode="1" sourcePort="0" destNode="18" destPort="0"/>
        <Arc sourceNode="1" sourcePort="0" destNode="18" destPort="1"/>
        <Arc sourceNode="18" sourcePort="2" destNode="7" destPort="0"/>
        <Arc sourceNode="18" sourcePort="3" destNode="7" destPort="1"/>

        <!-- 2. Pedalboard In-Line Chain: Pad -> Clon -> Blues Barker -> Blues River -> NA 808 -->
        <Arc sourceNode="7" sourcePort="2" destNode="12" destPort="0"/>
        <Arc sourceNode="7" sourcePort="3" destNode="12" destPort="1"/>

        <Arc sourceNode="12" sourcePort="2" destNode="10" destPort="0"/>
        <Arc sourceNode="12" sourcePort="3" destNode="10" destPort="1"/>

        <Arc sourceNode="10" sourcePort="2" destNode="11" destPort="0"/>
        <Arc sourceNode="10" sourcePort="3" destNode="11" destPort="1"/>

        <Arc sourceNode="11" sourcePort="2" destNode="13" destPort="0"/>
        <Arc sourceNode="11" sourcePort="3" destNode="13" destPort="1"/>

        <!-- 3. Pre-Split Pedalboard Output -> 3 Parallel Paradise Instances -->
        <!-- Feeding Amp 1: Showtime '64 SSS Clean (Node 3) -->
        <Arc sourceNode="13" sourcePort="2" destNode="3" destPort="0"/>
        <Arc sourceNode="13" sourcePort="3" destNode="3" destPort="1"/>

        <!-- Feeding Amp 2: Dream '65 Blackface Bloom (Node 14) -->
        <Arc sourceNode="13" sourcePort="2" destNode="14" destPort="0"/>
        <Arc sourceNode="13" sourcePort="3" destNode="14" destPort="1"/>

        <!-- Feeding Amp 3: Enigmatic '82 Dumble ODS Lead (Node 20) -->
        <Arc sourceNode="13" sourcePort="2" destNode="20" destPort="0"/>
        <Arc sourceNode="13" sourcePort="3" destNode="20" destPort="1"/>

        <!-- 4. Amps -> Airwindows Panners -->
        <Arc sourceNode="3" sourcePort="2" destNode="15" destPort="0"/>
        <Arc sourceNode="3" sourcePort="3" destNode="15" destPort="1"/>

        <Arc sourceNode="14" sourcePort="2" destNode="16" destPort="0"/>
        <Arc sourceNode="14" sourcePort="3" destNode="16" destPort="1"/>

        <Arc sourceNode="20" sourcePort="2" destNode="21" destPort="0"/>
        <Arc sourceNode="20" sourcePort="3" destNode="21" destPort="1"/>

        <!-- 5. Airwindows Panners -> 3-Channel Amp Bus Mixer -->
        <!-- Showtime L12 -> Input #0 (Ch 1: ports 0, 1) -->
        <Arc sourceNode="15" sourcePort="2" destNode="6" destPort="0"/>
        <Arc sourceNode="15" sourcePort="3" destNode="6" destPort="1"/>

        <!-- Dream Center -> Input #1 (Ch 2: ports 2, 3) -->
        <Arc sourceNode="16" sourcePort="2" destNode="6" destPort="2"/>
        <Arc sourceNode="16" sourcePort="3" destNode="6" destPort="3"/>

        <!-- Enigmatic R12 -> Input #2 (Ch 3: ports 4, 5) -->
        <Arc sourceNode="21" sourcePort="2" destNode="6" destPort="4"/>
        <Arc sourceNode="21" sourcePort="3" destNode="6" destPort="5"/>

        <!-- 6. Amp Bus Mixer Master Output -> LA-2A Silver Glue Compressor -->
        <Arc sourceNode="6" sourcePort="8" destNode="4" destPort="0"/>
        <Arc sourceNode="6" sourcePort="9" destNode="4" destPort="1"/>

        <!-- 7. LA-2A Outputs -> Master Output Mixer (Dry Ch 1) & Hitsville Reverb -->
        <Arc sourceNode="4" sourcePort="2" destNode="8" destPort="0"/>
        <Arc sourceNode="4" sourcePort="3" destNode="8" destPort="1"/>
        <Arc sourceNode="4" sourcePort="2" destNode="5" destPort="0"/>
        <Arc sourceNode="4" sourcePort="3" destNode="5" destPort="1"/>

        <!-- 8. Hitsville Reverb Output -> Master Output Mixer (Wet Ch 2) -->
        <Arc sourceNode="5" sourcePort="2" destNode="8" destPort="2"/>
        <Arc sourceNode="5" sourcePort="3" destNode="8" destPort="3"/>

        <!-- 9. Master Output Mixer -> Physical Audio Output (Node 2) -->
        <Arc sourceNode="8" sourcePort="8" destNode="2" destPort="0"/>
        <Arc sourceNode="8" sourcePort="9" destNode="2" destPort="1"/>

        <!-- 10. MIDI In -> Pedal Bypass Automation -->
        <Arc sourceNode="22" sourcePort="0" destNode="12" destPort="8"/>
        <Arc sourceNode="22" sourcePort="0" destNode="10" destPort="12"/>
        <Arc sourceNode="22" sourcePort="0" destNode="11" destPort="12"/>
        <Arc sourceNode="22" sourcePort="0" destNode="13" destPort="8"/>
      </arcs>

      <ports>
        <Port index="0" channel="0" type="audio" name="Audio In 1" symbol="audio_in_1" flow="input"/>
        <Port index="1" channel="0" type="audio" name="Audio Out 1" symbol="audio_out_1" flow="output"/>
        <Port index="2" channel="1" type="audio" name="Audio Out 2" symbol="audio_out_2" flow="output"/>
        <Port index="3" channel="0" type="midi" name="MIDI In 1" symbol="midi_in_1" flow="input"/>
      </ports>
    </Node>
  </graphs>
  <controllers/>
  <maps/>
</Session>
"""

    output_dir = "/Users/miketremoulet/Music/Element/Sessions/Toneprints"
    os.makedirs(output_dir, exist_ok=True)
    canonical_path = os.path.join(output_dir, "Parallel_Mayer_Trinity_3Amp.els")

    with open(canonical_path, "w") as f:
        f.write(session_xml)

    print(f"Successfully generated Kushview Element 3-Amp Parallel Mayer Trinity session at:\n  -> {canonical_path}")
    return canonical_path

if __name__ == "__main__":
    generate_mayer_trinity_session()
