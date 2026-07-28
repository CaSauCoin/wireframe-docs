# Symbol Creator

The Symbol Creator lets you design custom schematic symbols from scratch — either manually with a full interactive editor, or quickly with the wizard that auto-generates common layouts.

---

## Opening the Symbol Creator

Go to **Tools → Symbol Editor** to open the Symbol Creator dialog.

The dialog has two modes:

| Mode | Best for |
|---|---|
| **Wizard** | Standard IC layouts (DIP, SOIC, QFP) — quick auto-generation |
| **Manual Editor** | Complex or non-standard symbols — full creative control |

---

## Wizard Mode

The wizard generates a symbol automatically based on pin count and layout configuration.

### Configuration

| Setting | Description | Example |
|---|---|---|
| **Pin count** | Total number of pins | 8, 14, 28, 48 |
| **Layout** | Pin arrangement pattern | 2-side (DIP), 4-side (QFP) |
| **Pin names** | Names for each pin | VCC, GND, IN, OUT, etc. |
| **Pin types** | Electrical type per pin | Input, Output, Power, Passive |
| **Prefix** | Designator prefix | U, IC, J, Q |

### Preview

A **live preview canvas** renders the symbol in real time as you configure it:

- Pins displayed with numbers and names.
- Body rectangle sized to fit all pins.
- Reference and value text positioned.
- Grid and axis lines for alignment reference.

### Export

Click **Export** to save as a `.kicad_sym` file. The symbol is immediately available for loading into the Library panel.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Symbol Creator in Wizard mode:
     - Left panel: Configuration controls — Pin count (8), Layout dropdown ("2-side"),
       a pin name table showing 8 pins (GND, TRIG, OUT, RESET, CTRL, THRES, DISCH, VCC).
     - Right panel: Live preview canvas showing a rectangular IC symbol with 4 pins
       on each side, pin names visible, pin numbers labeled.
     - An "Export to .kicad_sym" button at the bottom.
     - Dark theme matching the editor.
     SUGGESTED SIZE: 900×550px
-->
![Symbol Wizard](../img/libraries/symbol-wizard.png)

---

## Manual Editor Mode

The manual editor provides a full interactive drawing environment for creating symbols of any shape and complexity.

### Drawing Tools

| Tool | Description |
|---|---|
| **Pin** | Place a pin with configurable name, number, length, type, and direction |
| **Line** | Draw straight lines for the symbol body |
| **Rectangle** | Draw rectangular outlines |
| **Circle** | Draw circles (e.g., for NOT bubbles, LEDs) |
| **Arc** | Draw arcs (e.g., for op-amp triangles, gate shapes) |
| **Polygon** | Draw complex custom shapes |
| **Text** | Add text labels and annotations |

### Pin Configuration

Each pin has detailed properties:

| Property | Description | Example |
|---|---|---|
| **Name** | Signal name | `VCC`, `OUT`, `CLK` |
| **Number** | Physical pin number | 1, 2, 3, … |
| **Length** | Pin stub length | 100 mil |
| **Direction** | Pin orientation (Left, Right, Up, Down) | Right |
| **Electrical type** | Input, Output, Bidirectional, Power, Passive | Input |
| **Visibility** | Whether pin name/number is drawn | Name visible, Number visible |

### Workflow

1. Switch to **Manual** mode in the Symbol Creator.
2. Use **drawing tools** to create the symbol body (lines, rectangles, arcs).
3. Use the **Pin** tool to place pins around the body.
4. Configure each pin's name, number, and type in the properties area.
5. Set the **Reference** prefix (e.g., `U`) and **Value** default.
6. Preview the final symbol in the canvas.
7. Click **Export** to save.

<!-- TODO: Replace with actual video
     SCENARIO: Record a 25-second clip showing:
     1. Open the Symbol Creator → select Manual mode.
     2. Draw a rectangle for the IC body.
     3. Place 4 pins on the left (inputs) and 4 pins on the right (outputs).
     4. Name the pins: VCC, GND, IN1, IN2, OUT1, OUT2, EN, CLK.
     5. Set pin types (power, input, output).
     6. Click Export → save as "MyIC.kicad_sym".
     RESOLUTION: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/libraries/symbol-creator-manual.webm" type="video/webm">
  <source src="../../img/libraries/symbol-creator-manual.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Using Created Symbols

After exporting:

1. Load the `.kicad_sym` file via the Library panel (**Load Symbols…**).
2. The new symbol appears in the symbol list.
3. Double-click to place it on the schematic — just like any library component.

---

## Tips

!!! tip "Pin placement conventions"
    - **Inputs** on the **left** side.
    - **Outputs** on the **right** side.
    - **Power** (VCC) on **top**, **GND** on **bottom**.
    - This follows standard EDA conventions and makes schematics easier to read.

!!! info "Editing existing symbols"
    You can open an existing `.kicad_sym` file in the Symbol Creator for editing. Load it and modify pins, graphics, or properties as needed.

---

## See Also

- [Symbol Libraries](symbols-library.md) — loading and managing symbol libraries.
- [Placing Components](../schematic/placing-components.md) — using your created symbols.
- [AI Component Generator](../ai/component-generator.md) — AI-powered alternative for creating symbols.
