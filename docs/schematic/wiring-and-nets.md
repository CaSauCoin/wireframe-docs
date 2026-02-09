# Wiring and Nets

Wiring connects component pins into electrical nets. Wire behavior is controlled by `WireManager`, `WireRenderer`, and `SchNetlistManager`.

---

## Wire drawing mode

Select the **Wire** tool in the schematic toolbar.

Behavior:

1. Click on:
   - A pin tip, or
   - An empty point on the canvas
   to start a wire.
2. A temporary wire follows the mouse.
3. Each left‑click adds a vertex.
4. Right‑click or an end‑wire shortcut ends the wire.

When started from a pin:

- `WireManager::startWireFromPin` locates the pin tip in world coordinates.
- The first vertex is attached to that pin in `Wire::pinAttachments`.

---

## Connecting to pins and existing wires

When you click to finish a wire on:

- **Another pin**:
  - The final vertex is snapped to the pin tip.
  - `pinAttachments` records the component ID and pin number.

- **An existing wire vertex/segment**:
  - The new wire shares that vertex position.
  - `WireRenderer` visually merges them; `SchNetlistManager` treats them as a single net.

> **Image placeholder**  
> `![Wire attachment](img/schematic/wire-attachment.png)`  
> _A demonstration where a wire is drawn from one pin, clicks into another pin, and a junction dot is automatically added when multiple wires meet._

---

## Wire geometry and editing

Each `Wire` stores:

- `id`: unique wire ID.
- `points`: ordered list of vertices (ImVec2 in world coordinates).
- `pinAttachments`: map from point index → attached pin (componentId, pinNumber).
- `netName`: optional explicit net name.

Editing operations:

- **Move vertex**:
  - Drag a wire vertex within a small radius (`findDraggableVertexAt`).
  - `WireManager::moveVertex` updates position and may detach pin attachments if moved away.
- **Drag segment**:
  - Click and drag a segment (between two vertices).
  - `Interactive_Wire_Dragger` inserts two new vertices and allows orthogonal dragging.
  - On release, `simplifyWirePath` removes redundant collinear vertices.

All edits are captured by commands like `ModifyWireCommand`.

---

## Junctions

When three or more connections meet at a point:

- `WireRenderer` counts occurrences of each wire vertex (and pin positions).
- If a point has connectivity ≥ 3, a junction circle is drawn.

You can also explicitly place junctions via the **Junction** tool (graphics).

---

## Net labels and power symbols

Net naming is driven by:

- **NetLabel components** (`type == "NetLabel"`) and their value.
- **Power symbols** (VCC, GND, VDD) that may imply specific net names.

Workflow:

1. Use **Label** mode to place a `NetLabel`.
2. Edit its value in the Properties panel (e.g. `SCL`, `+5V`).
3. All connected wires to that label share the same net name.

Power symbols:

- Placed via **PlacingVCC** / **PlacingGND** modes.
- `Component_Library` defines single‑pin components for VCC, GND, etc.

`ChangeNetNameCommand` and `ChangeComponentValueCommand` synchronize displayed text and actual net names.

> **Image placeholder**  
> `![Net labels](img/schematic/net-labels.png)`  
> _Labels on different parts of a schematic all use the same name (e.g., +3V3) and highlight as one net._

---

## Schematic netlist

`SchNetlistManager::rebuild` constructs a net graph from:

- All wires and their attached pins.
- Shared vertices between wires.
- Net labels and power symbols.

Rules:

- Wires sharing vertices form a **cluster**.
- Cluster net names are determined by priority:
  1. Net labels (and certain power symbols) with user values.
  2. Pin‑based default names (“Net_U1_1”).
  3. If still unnamed, a generic wire‑based name (e.g., `Net_Wire_X`).

The result is a map:

```text
netName -> SchNet { name, set<PinRef> }
```

This netlist is used for:

- Schematic net highlighting.
- PCB netlist generation.
- DRC/DFM consistency checks between schematic and PCB.

---

## Net highlighting

Using `WireRenderer::renderNetHighlight`:

- Highlight a selected net name across:
  - Wires.
  - Connected pins.
  - Net labels.

From the UI:

- Selecting a `NetLabel` or choosing a net from a list (when implemented) can set the highlighted net.
- The schematic canvas shows that net in a distinct color overlay.

> **Video placeholder**  
> _Short clip where user clicks a net label, and all wires/pins on that net are softly highlighted across the sheet._