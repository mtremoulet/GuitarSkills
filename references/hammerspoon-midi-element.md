# Hammerspoon MIDI Controller Guide for Kushview Element

This guide documents the setup for using **Hammerspoon** keyboard shortcuts to trigger **MIDI Program Change (snapshot/preset)** messages into **Kushview Element** via macOS's built-in **IAC Driver**.

---

## 1. System Architecture

```
[Mac Keyboard: Keys 1, 2, 3, 5]
             │ (Only active when Element is frontmost)
             ▼
      [Hammerspoon]
             │ (MIDI Program Change over IAC Driver Bus 1)
             ▼
   [macOS IAC Driver Bus 1]
             │
             ▼
   [Element: MIDI In Node]
             ├──► [NA Clon Minotaur]     (MIDI Ch 1: Prog 1 = ON, Prog 2 = OFF)
             ├──► [Efektor Blues Barker] (MIDI Ch 2: Prog 1 = ON, Prog 2 = OFF)
             ├──► [NA 808 Screamer]      (MIDI Ch 3: Prog 1 = ON, Prog 2 = OFF)
             └──► [Efektor Blues River]  (Future expansion: MIDI Ch 4, Key 4)
```

---

## 2. macOS & Element Configuration

### A. macOS IAC Driver (One-time check)
1. Open **Audio MIDI Setup** (`/Applications/Utilities/Audio MIDI Setup.app`).
2. Go to **Window → Show MIDI Studio**.
3. Double-click the red **IAC Driver** icon.
4. Ensure **"Device is online"** is checked and at least one port (**"Bus 1"**) exists.

### B. Element MIDI Setup
1. In Element, go to **Options → Audio / MIDI Settings → MIDI**.
2. Check **`IAC Driver Bus 1`** under **Active MIDI Inputs**.
3. In your Element graph:
   * Ensure a **`MIDI In`** node exists on the canvas.
   * On each pedal plugin block, open its port list (right-click → Ports) and ensure the **`MIDI In` (Orange Pin)** is checked.
   * Connect patch cables from **`MIDI In` (orange pin)** → to each pedal's **`MIDI In` (orange pin)**.

### C. Saving Snapshots (MIDI Programs) in Element
In Element's left **`NODE`** sidebar for each pedal:
* **`NA Clon Minotaur`**:
  * Set **MIDI Channel** = **`1`**
  * Turn pedal **ON** → Set Program to **`1`**, name `"Clon ON"`, click save.
  * Turn pedal **OFF** (Bypass) → Set Program to **`2`**, name `"Clon OFF"`, click save.
* **`Efektor Blues Barker`**:
  * Set **MIDI Channel** = **`2`**
  * Program **`1`** = `"Barker ON"`, Program **`2`** = `"Barker OFF"`.
* **`NA 808`**:
  * Set **MIDI Channel** = **`3`**
  * Program **`1`** = `"808 ON"`, Program **`2`** = `"808 OFF"`.

---

## 3. Working Hammerspoon Script (`~/.hammerspoon/init.lua`)

```lua
-- ============================================================================
-- GUITAR PEDALBOARD MIDI PROGRAM CONTROLLER (HAMMERSPOON)
-- ============================================================================

local midiOut = hs.midi.new("IAC Driver Bus 1")

-- Track state: true = ON (Program 1), false = OFF (Program 2)
local pedalState = {
    clon   = false,
    barker = false,
    ts808  = false
}

-- Helper function to send MIDI Program Change
-- Note: Channels in Lua hs.midi are 0-indexed: Ch 1 = 0, Ch 2 = 1, Ch 3 = 2, Ch 4 = 3
local function sendProgramChange(channelIndex, programNumber)
    if midiOut then
        midiOut:sendCommand("programChange", {
            ["programNumber"] = programNumber, -- 0 for Prog 1 (ON), 1 for Prog 2 (OFF)
            ["channel"]       = channelIndex
        })
    end
end

-- ============================================================================
-- HOTKEYS (Keys 1, 2, 3, 5)
-- ============================================================================

-- Key 1: Toggle Clon (Channel 1)
local k1 = hs.hotkey.new({}, "1", function()
    pedalState.clon = not pedalState.clon
    local prog = pedalState.clon and 0 or 1
    sendProgramChange(0, prog)
    hs.alert.show(pedalState.clon and "🟢 Clon: ON" or "⚪ Clon: OFF", 0.4)
end)

-- Key 2: Toggle Blues Barker (Channel 2)
local k2 = hs.hotkey.new({}, "2", function()
    pedalState.barker = not pedalState.barker
    local prog = pedalState.barker and 0 or 1
    sendProgramChange(1, prog)
    hs.alert.show(pedalState.barker and "🟢 Blues Barker: ON" or "⚪ Blues Barker: OFF", 0.4)
end)

-- Key 3: Toggle NA 808 (Channel 3)
local k3 = hs.hotkey.new({}, "3", function()
    pedalState.ts808 = not pedalState.ts808
    local prog = pedalState.ts808 and 0 or 1
    sendProgramChange(2, prog)
    hs.alert.show(pedalState.ts808 and "🟢 NA 808: ON" or "⚪ NA 808: OFF", 0.4)
end)

-- Key 5: Master Toggle All Pedals
local k5 = hs.hotkey.new({}, "5", function()
    local anyOn = pedalState.clon or pedalState.barker or pedalState.ts808
    local newState = not anyOn

    pedalState.clon   = newState
    pedalState.barker = newState
    pedalState.ts808  = newState

    local prog = newState and 0 or 1
    sendProgramChange(0, prog) -- Ch 1 (Clon)
    sendProgramChange(1, prog) -- Ch 2 (Barker)
    sendProgramChange(2, prog) -- Ch 3 (808)

    hs.alert.show(newState and "🔥 ALL PEDALS: ON" or "🧹 ALL PEDALS: OFF", 0.6)
end)

-- ============================================================================
-- APP-SPECIFIC ENABLER (Only active when Element is the frontmost window)
-- ============================================================================
local allHotkeys = { k1, k2, k3, k5 }

local elementWatcher = hs.application.watcher.new(function(appName, eventType, app)
    if appName == "Element" then
        if eventType == hs.application.watcher.activated then
            for _, hk in ipairs(allHotkeys) do hk:enable() end
        elseif eventType == hs.application.watcher.deactivated then
            for _, hk in ipairs(allHotkeys) do hk:disable() end
        end
    end
end)
elementWatcher:start()

local frontApp = hs.application.frontmostApplication()
if frontApp and frontApp:name() == "Element" then
    for _, hk in ipairs(allHotkeys) do hk:enable() end
end

print("🎸 Element MIDI Program Snapshot Controller Loaded!")
```

---

## 4. Future Expansion: Adding the Blues Driver (Key 4)

When you are ready to integrate the **`Efektor Blues River` (Boss BD-2)**:
1. In Element `NODE` panel for `Blues River`: Set **MIDI Channel = `4`**.
2. Save Program **`1`** as `"River ON"` and Program **`2`** as `"River OFF"`.
3. Add Key 4 to the script:
   ```lua
   -- Key 4: Toggle Blues River (Channel 4 -> index 3)
   local k4 = hs.hotkey.new({}, "4", function()
       pedalState.river = not pedalState.river
       local prog = pedalState.river and 0 or 1
       sendProgramChange(3, prog)
       hs.alert.show(pedalState.river and "🟢 Blues River: ON" or "⚪ Blues River: OFF", 0.4)
   end)
   ```
4. Include `k4` in `allHotkeys` and update `k5` (All-On/All-Off) to send to channel index `3`.
