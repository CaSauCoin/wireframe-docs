# AI Component Generator

When the AI Design Agent generates a circuit that includes components **not found in your local library**, the AI Component Generator can automatically create the missing symbol and footprint — using datasheet analysis and AI-powered pin mapping.

---

## When It Activates

The AI Component Generator is triggered when:

1. The [AI Library Reviewer](design-agent.md#library-pool-check) finds a component marked ⚠ **Missing**.
2. You click **Generate** next to the missing component in the Component Review window.

---

## How It Works

### Step 1: Datasheet Analysis

The AI reads the component's datasheet (or uses its training knowledge) to extract:

| Data | Example |
|---|---|
| **Pin count** | 8 pins |
| **Pin names** | VCC, GND, OUT, TRIG, THRES, DISCH, CTRL, RST |
| **Pin functions** | Power, Input, Output, Control |
| **Package** | DIP-8 / SOIC-8 |
| **Electrical specs** | Operating voltage, max current |

### Step 2: Symbol Generation

Based on the extracted data, the AI generates a schematic symbol:

- Pin positions calculated for clean schematic layout (inputs left, outputs right, power top/bottom).
- Pin electrical types assigned (input, output, power, passive).
- Symbol body rectangle sized to fit all pins.
- Reference and value text positioned.

### Step 3: Footprint Generation

The AI generates a matching PCB footprint:

- Pad positions calculated from the package dimensions.
- Pad shapes and sizes configured for the package type.
- Silkscreen outline and pin 1 marker added.
- Courtyard and fabrication layer outlines computed.

### Step 4: Review and Edit

A preview popup shows the generated component:

```
┌─────────────────────────────────────────────────────┐
│  AI Component Generator — NE555 (DIP-8)             │
│                                                      │
│  ┌───────────────┐    ┌───────────────┐             │
│  │   Symbol       │    │   Footprint   │             │
│  │   ┌───────┐    │    │   ○ ○ ○ ○    │             │
│  │ ──┤ NE555 ├──  │    │   DIP-8      │             │
│  │ ──┤       ├──  │    │   ○ ○ ○ ○    │             │
│  │   └───────┘    │    │              │             │
│  └───────────────┘    └───────────────┘             │
│                                                      │
│  Pins: 8/8 mapped ✅   Package: DIP-8 ✅            │
│                                                      │
│  [Edit Symbol]  [Edit Footprint]  [Accept & Add]    │
└─────────────────────────────────────────────────────┘
```

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the AI Gen Popup showing:
     - A component name header (e.g., "NE555 DIP-8").
     - Side-by-side preview: symbol on the left, footprint on the right.
     - Pin mapping table showing all 8 pins with names and types.
     - Status indicators: "Pins: 8/8 mapped ✅", "Package: DIP-8 ✅".
     - Action buttons: "Edit Symbol", "Edit Footprint", "Accept & Add".
     - Dark theme, clean layout.
     SUGGESTED SIZE: 800×500px
-->
![AI Gen Popup](../img/ai/ai-gen-popup.png)

---

## Datasheet-Powered Generation

For components with well-known datasheets, the AI applies specific rules:

| Component Type | Special Handling |
|---|---|
| **MCUs** | SWD/JTAG pins grouped, power pins with decoupling requirements noted |
| **Voltage Regulators** | Input/Output/GND/Enable pin assignment following datasheet pinout |
| **Op-Amps** | Non-inverting/Inverting/Output/V+/V- standard pin arrangement |
| **Connectors** | Pin numbering following physical header layout |
| **Passive Components** | 2-pin symbols with correct prefix (R, C, L) |

---

## After Generation

Once you accept the generated component:

1. The symbol and footprint are **added to your project's local library**.
2. The component status in the Component Review changes to ✅ **Found**.
3. The design workflow can proceed with placement and routing.

---

## Manual Editing

If the AI-generated component needs adjustment:

- Click **Edit Symbol** → opens the [Symbol Creator](../libraries/symbol-creator.md) with the generated symbol pre-loaded.
- Click **Edit Footprint** → opens the [Footprint Wizard](../libraries/footprints-library.md#footprint-generator-footprint-wizard) with the generated footprint.

---

## See Also

- [AI Design Agent](design-agent.md) — triggers the component generator when library items are missing.
- [Symbol Creator](../libraries/symbol-creator.md) — manual symbol creation and editing.
- [Footprint Libraries](../libraries/footprints-library.md) — footprint management and the Footprint Wizard.
