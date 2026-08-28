# Wiring and Nets

Wires connect component pins into **electrical nets**. This page covers drawing wires, connecting pins, placing net labels, and using power symbols.

---

## Drawing Wires

### Activating the Wire tool

Press ++w++ or click the **Wire** button on the toolbar.

### How to draw a wire

1. **Click** on a component pin (or any point on the canvas) to start a wire
2. A temporary wire follows the cursor — drawn **orthogonally** (horizontal and vertical segments only)
3. **Left-click** to add each corner vertex
4. **Right-click** or press ++esc++ to end the wire

![Wire attached to component pins](../img/schematic/wire-attachment.png)

| Action | Input |
|---|---|
| Start a wire | Click on a pin or canvas point |
| Add a corner | Left-click |
| End the wire | Right-click or ++esc++ |
| Cancel before starting | ++esc++ |

!!! tip "Starting from a pin snaps automatically"
    When you click on a pin tip, WireFrame snaps the first vertex precisely to that pin — no manual alignment needed.

---

## Connecting Wires to Pins and Existing Wires

### To another pin

- The final vertex **snaps** to the target pin position
- Both pins are now on the same net

### To an existing wire

- The new wire shares the meeting point with the existing wire
- WireFrame merges them into a **single net**

Use the shared GND net label or power symbol at the intended connection points. WireFrame merges connected wire segments and matching global power labels into the same net.

---

## Junction Dots

A **junction dot** appears when three or more wires meet at a single point:

```
  With junction:           Without junction (wires cross, not connected):
  ───●───                  ───┼───
     │                        │ (not connected)
```

- Junction dots are **placed automatically** when three or more connections share a point
- You can also place them manually with the **Junction** tool
- Two crossing wires **without** a junction are not electrically connected

---

## Editing Existing Wires

| Operation | How |
|---|---|
| **Move a vertex** | Drag a point on the wire |
| **Drag a segment** | Click and drag a segment between two vertices → adds two new vertices, moves orthogonally |
| **Delete a wire** | Select + ++delete++ |

!!! info "Auto-simplification"
    After dragging a segment, WireFrame automatically removes redundant collinear vertices — keeping the wire geometry clean.

---

## Net Labels

Net labels allow you to **connect two points electrically without drawing a wire between them**. Labels with the same name belong to the same net.

### How to place a net label

1. Press ++l++ or click the **Label** tool
2. Click on the canvas to place a label
3. Edit the **Value** in the Properties panel (e.g. `SDA`, `SCL`, `+3V3`, `RESET`)
4. All wires connected to that label share the **same net name**

```
Example — connecting without a direct wire:

  MCU U1                Sensor U2
  ──[SDA]               ──[SDA]
  ──[SCL]               ──[SCL]

  → SDA and SCL are automatically connected
    even though no wire runs between them
```

!!! tip "Use consistent names"
    All labels with the same name (e.g. `+3V3`) merge into a single net — even on different parts of the sheet. This is the cleanest way to distribute power to multiple components.

---

## Power Symbols (GND, VCC)

| Symbol | Shortcut | Description |
|---|---|---|
| **GND** | ++g++ | Ground reference — implicitly connects all GND pins |
| **VCC** | — (toolbar) | Positive supply rail |

Power symbols are single-pin components that automatically assign a net name to any wire connected to them.

```
Example power connections:

   +5V
    ↑ VCC
    │
   [C1] 100nF
    │
   ─┴─ GND ⏚
```

---

## Net Highlighting

Click on any wire or net label:
- **All wires and pins on that net** are highlighted in a distinct color
- Useful for tracing connectivity in complex schematics

Click on empty canvas to clear the highlight.

---

## How the Netlist is Built

WireFrame automatically constructs the netlist from all wires, pins, and labels:

1. Groups all wires that share vertices into **clusters**
2. Collects all pins attached to each cluster
3. Determines the net name by priority:
    1. **Net label / power symbol** values (highest priority)
    2. Pin-based default names (e.g. `Net_U1_1`)
    3. Wire-based fallback names (e.g. `Net_Wire_42`)

This netlist is used for:
- Net highlighting on the canvas
- PCB netlist generation when converting to PCB
- DRC consistency checks between schematic and PCB

---

## See Also

- [Placing Components](placing-components.md) — place the symbols that wires connect
- [Properties & Attributes](properties-and-attributes.md) — edit net names and component values
- [PCB Editor](../pcb/index.md) — the netlist built here drives PCB routing
