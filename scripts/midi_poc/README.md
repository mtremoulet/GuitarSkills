# Proof of Concept: Real-Time MIDI Tone Switcher

This folder contains a fully functional test script to demonstrate real-time tone morphing in Logic Pro. This script targets four core parameters: **Volume/Gain, Bass, Mids, and Treble**.

You can run this test using **either** your **Neural DSP Archetype Cory Wong X** (specifically the *Amp Snob* head) or **any UADx amp** (like *Dream '65* or *Showtime '64*).

---

## The Files
*   **[Logic_Scripter_Test_Switch.js](file:///Users/miketremoulet/claude-projects/GuitarSkills/scripts/midi_poc/Logic_Scripter_Test_Switch.js)**: The JavaScript source code for Logic's Scripter.

---

## Setup Walkthrough (10-Minute Task)

### Step 1: Create a Software Instrument Track in Logic
Because standard Audio tracks do not support MIDI FX plugins, we must route your guitar through a Software Instrument track.
1. Open a Logic Pro project.
2. Create a new track and select **Software Instrument**.
3. Under the **Instrument slot** on the channel strip (in the Inspector), click the selector:
   *   **For Neural DSP:** Navigate to **AU MIDI-controlled Effects → Neural DSP → Archetype Cory Wong X** and load it.
   *   **For UADx:** Navigate to **AU MIDI-controlled Effects → Universal Audio → [Dream '65 or Showtime '64]** and load it.

### Step 2: Route Your Guitar Input (Side-Chain)
1. Open the plugin window you just loaded.
2. In the top-right corner of the plugin window frame, look for the **Side Chain** dropdown menu.
3. Select the physical input where your guitar is plugged in on your Audient iD14 (typically **Input 1** or **Input 2**).
4. Mute direct physical monitoring on your iD14 mixer software, and turn on **input monitoring** (the `I` button) on your new Logic Software Instrument track. You should now hear your raw guitar processing through the amp plugin.

### Step 3: Deploy the Logic Scripter
1. On the same track's channel strip in the Inspector, locate the **MIDI FX** slot (directly above the Instrument slot).
2. Select **Scripter**.
3. In the Scripter Editor window, delete any default code.
4. Copy the complete code from **[Logic_Scripter_Test_Switch.js](file:///Users/miketremoulet/claude-projects/GuitarSkills/scripts/midi_poc/Logic_Scripter_Test_Switch.js)** and paste it into the editor.
5. Click **Run Script** in the top right. You will see a dropdown menu labeled **Toneprint Select** appear!

---

## Step 4: Map the Controls (The MIDI Learn step)

To teach the plugin which knob matches which Scripter command, we perform a quick 1-minute mapping.

### A. For Neural DSP (Archetype Cory Wong X)
1. In the plugin interface, select the **Amp Snob** (Amp 3).
2. **Volume Knob:** Right-click the **Volume** knob and click **Enable MIDI Learn**. In the Logic Scripter window, change the dropdown from "Select Snapshot..." to **"1. Dumble Clean Vocal"**. The Volume knob will instantly lock onto the script (you will see it jump and a MIDI connection icon appear).
3. **Bass Knob:** Right-click the **Bass** knob and click **Enable MIDI Learn**. In Scripter, cycle the dropdown to "Select Snapshot..." and then back to **"1. Dumble Clean Vocal"**. It will map instantly.
4. **Middle Knob:** Right-click the **Middle** knob and click **Enable MIDI Learn**. Cycle the Scripter dropdown again to map it.
5. **Treble Knob:** Right-click the **Treble** knob and click **Enable MIDI Learn**. Cycle the Scripter dropdown.

*Done! All four controls are now globally mapped.*

### B. For UADx (Dream '65 / Showtime '64)
1. Click the **••• Options** menu in the top bar of the UADx plugin and select **MIDI Learn**.
2. **Volume:** Click the **Volume** knob in the UADx GUI. Cycle your Logic Scripter dropdown. The knob will instantly bind to CC 30.
3. **Bass:** Click the **Bass** knob in the UADx GUI. Cycle the Scripter dropdown to bind to CC 31.
4. **Mids:** (If using a plugin with a middle control like Showtime or Lion) Click **Middle** and cycle Scripter to bind to CC 32.
5. **Treble:** Click **Treble** and cycle Scripter to bind to CC 33.
6. Click the **••• Options** menu again, select **MIDI**, and click **Save MIDI Mappings**.

*Done! You can now load this map on any instance of this UADx plugin.*

---

## The Fun Part: Testing the Morph

With mapping complete:
1. Keep the plugin window and the Logic Scripter window side-by-side on your screen.
2. Select **1. Dumble Clean Vocal (Warm & Round)**: Watch all four knobs instantly fly to their designated warm clean spots!
3. Select **2. Scooped Funk Quack (Snappy & Bright)**: Watch the knobs instantly morph to scooped mids and high treble!
4. Select **3. Pushed Edge-of-Breakup (Harmonic Bloom)**: Watch the knobs morph to a high volume and throaty mid structure!

### Taking It Further (Timeline Automation)
If you want to see the real power of this:
1. Press `A` in Logic to open **Automation**.
2. Select the Software Instrument track. Click the automation parameter list, find **MIDI FX → Scripter → Toneprint Select**.
3. Draw automation nodes on your timeline.
4. Hit Play: Watch the knobs on your Neural DSP or UADx amp **automatically dance and morph in real-time** as the playhead sweeps across your timeline!
