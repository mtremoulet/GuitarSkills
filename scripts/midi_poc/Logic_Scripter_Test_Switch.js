// =========================================================================
// LOGIC PRO SCRIPTER: TONEPRINT SWITCHER & MORPHER (PROOF OF CONCEPT)
// =========================================================================
// Target: Amp Snob (Neural DSP) or Dream '65 / Showtime '64 (UADx)
// Physical Input: Guitar via Side-Chain
// =========================================================================

// 1. Define MIDI CC Assignments
const CC_MAP = {
    volume:  30, // Amp Input Volume / Gain
    bass:    31, // EQ Bass
    mids:    32, // EQ Mids
    treble:  33  // EQ Treble
};

// 2. Define Sweet-Spot Configurations (MIDI 0-127 scales to plugin 0-100%)
// Formula: MIDI Value = Math.round((Percent / 100) * 127)
const CONFIGURATIONS = {
    1: { 
        name: "1. Dumble Clean Vocal (Warm & Round)",
        volume:  51, // 40% (Keeps preamp clean, warm neck pickup focus)
        bass:    57, // 45% (Tight low-end, no mud)
        mids:    83, // 65% (Pushed midrange for vocal note detail)
        treble:  61  // 48% (Smooth highs, dark but articulate)
    },
    2: { 
        name: "2. Scooped Funk Quack (Snappy & Bright)",
        volume:  44, // 35% (Slightly cleaner head-room for fast rhythm)
        bass:    70, // 55% (Full bottom-end snap)
        mids:    44, // 35% (Scooped mids to highlight Strat/Tele position quack)
        treble:  95  // 75% (Cutting high-end for funk scratching)
    },
    3: { 
        name: "3. Pushed Edge-of-Breakup (Harmonic Bloom)",
        volume:  76, // 60% (Pushed input gain to force slight tube grit)
        bass:    51, // 40% (Rolled back to prevent low-end wooliness)
        mids:    74, // 58% (Throaty, rich vocal mids)
        treble:  64  // 50% (Clear, singing high-end)
    }
};

// 3. Generate Logic Pro UI Dropdown Menu
var PluginParameters = [{
    name: "Toneprint Select", 
    type: "menu", 
    valueStrings: [
        "Select Snapshot...", 
        CONFIGURATIONS[1].name, 
        CONFIGURATIONS[2].name, 
        CONFIGURATIONS[3].name
    ], 
    defaultValue: 0
}];

// 4. Handle Menu Selection & Emit MIDI CC Packets
function ParameterChanged(param, value) {
    // Check if the dropdown changed and a valid preset was selected (> 0)
    if (param === 0 && value > 0) {
        var config = CONFIGURATIONS[value];
        
        Trace("--------------------------------------------------");
        Trace("Morphing rig to: " + config.name);
        Trace("-> Volume: " + Math.round((config.volume/127)*100) + "% (CC " + CC_MAP.volume + " = " + config.volume + ")");
        Trace("-> Bass:   " + Math.round((config.bass/127)*100) + "% (CC " + CC_MAP.bass + " = " + config.bass + ")");
        Trace("-> Mids:   " + Math.round((config.mids/127)*100) + "% (CC " + CC_MAP.mids + " = " + config.mids + ")");
        Trace("-> Treble: " + Math.round((config.treble/127)*100) + "% (CC " + CC_MAP.treble + " = " + config.treble + ")");
        
        // Fire the CC burst to morph the plugin instantly
        sendCC(CC_MAP.volume, config.volume);
        sendCC(CC_MAP.bass,   config.bass);
        sendCC(CC_MAP.mids,   config.mids);
        sendCC(CC_MAP.treble, config.treble);
    }
}

// Helper function to bundle and send standard MIDI CC events
function sendCC(ccNumber, ccValue) {
    var ccMessage = new ControlChange();
    ccMessage.number = ccNumber;
    ccMessage.value = ccValue;
    MIDI.send(ccMessage);
}
