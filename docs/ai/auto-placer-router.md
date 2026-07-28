# Auto-Placer & Auto-Router

After the AI Design Agent generates a BOM and netlist, the **Auto-Placer** and **Auto-Router** handle the physical implementation — positioning components on the board and routing copper traces between them.

---

## AI Auto-Placer

The Auto-Placer takes the AI-generated component list and arranges them intelligently on the schematic and PCB.

### Placement Strategy

Components are organized using **logical grouping**:

| Group | Strategy | Example |
|---|---|---|
| **Power section** | Clustered together, input near edge connector | Voltage regulators, inductors, bulk capacitors |
| **MCU section** | Central position | Microcontroller with nearby decoupling caps |
| **Interface section** | Near board edges | Connectors, headers, USB ports |
| **Analog section** | Separated from digital | Op-amps, ADC reference circuits |
| **Decoupling** | Adjacent to IC power pins | 100nF capacitors placed as close as possible |

### Block-Based Decomposition

For complex designs, the AI breaks the circuit into **functional blocks**:

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Power      │  │     MCU      │  │  Interface   │
│              │  │              │  │              │
│  LM2596      │  │  STM32F103   │  │  USB-C       │
│  L1, D1      │  │  C3, C4, C5  │  │  J1          │
│  C1, C2      │  │  R3 (pull-up)│  │  ESD prot.   │
└──────────────┘  └──────────────┘  └──────────────┘
```

Each block is placed as a unit, then blocks are arranged relative to each other based on signal flow.

### Placement Preview

Before applying the placement, you can preview it in the **Placement Copilot** tab of the Component Review window:

- **Block View**: Shows each functional block separately with component positions.
- **Whole Circuit View**: Shows the complete layout with all blocks arranged.
- Supports **zoom and pan** (same controls as the schematic canvas).

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Placement Preview canvas showing:
     - 3-4 functional blocks arranged on a dark canvas.
     - Each block labeled (e.g., "Power", "MCU", "Sensors").
     - Components visible within each block with designators.
     - Connection lines between blocks showing signal flow.
     - View mode toggle: "Block View" / "Whole Circuit" buttons visible.
     SUGGESTED SIZE: 800×500px
-->
![Placement Preview](../img/ai/placement-preview.png)

---

## AI Auto-Router

The Auto-Router uses a **sequential A* pathfinding algorithm** on a grid to route all PCB traces automatically.

### Algorithm Overview

```
For each unrouted connection (ratsnest line):
  1. Create a grid representation of the board
  2. Mark obstacles (existing traces, pads, vias, board edge)
  3. Apply penalty weights:
     - Via cost (discourage unnecessary layer changes)
     - Crossing penalty (avoid parallel runs on same layer)
     - Corner penalty (prefer smooth routing)
  4. Run A* from source pad to destination pad
  5. Convert the grid path to trace segments
  6. Update the grid with the new trace
```

### Route Order

The router processes nets in a strategic order:

1. **Power nets** (GND, VCC) — routed first for lowest impedance paths.
2. **Short connections** — easy routes that reduce congestion early.
3. **Long connections** — complex routes that need the most flexibility.

### Via Management

When a trace cannot reach its destination on the current layer:

- The router automatically inserts a **via** to switch layers.
- Via placement is optimized to minimize total via count.
- Annular ring and drill sizes follow the design rules.

### Progress Visualization

During auto-routing, you can see:

- A **progress bar** showing percentage of connections routed.
- Traces appearing on the PCB canvas in real time.
- Status messages: `"Routing net GND (15/42)"`.

<!-- TODO: Replace with actual video
     SCENARIO: Record a 15-second clip showing:
     1. A PCB with 10-15 footprints placed, ratsnest lines visible.
     2. Click "Auto-Route" — the progress bar starts.
     3. Traces appear on the board one by one, routing between pads.
     4. Vias appear when traces switch layers (red F.Cu → blue B.Cu).
     5. Progress bar reaches 100% — all ratsnest lines gone.
     RESOLUTION: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/ai/auto-routing.webm" type="video/webm">
  <source src="../../img/ai/auto-routing.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Manual Overrides

After auto-placement and auto-routing, you retain **full manual control**:

| Action | How |
|---|---|
| **Move a component** | Select + drag — traces auto-adjust |
| **Re-route a trace** | Delete the trace, manually route with ++x++ |
| **Adjust placement** | Drag footprints to preferred positions |
| **Add manual vias** | Press ++v++ to place vias where needed |

!!! tip "AI preserves your edits"
    The AI system uses **coordinate locking** — if you manually move a component, subsequent AI regenerations will preserve your position. This enables non-destructive iterative design.

---

## GNN-Based Placement (Advanced)

WireFrame includes an experimental **Graph Neural Network (GNN)** model for intelligent component placement:

- **Technology**: Graph Attention Network (GAT) for functional clustering.
- **Training data**: Parsed from real KiCad and Altium projects.
- **Inference**: Runs locally via ONNX runtime — low latency, no server required.
- **Purpose**: Groups components into functional clusters (power, digital, analog) for optimal board-level placement.

!!! note "Experimental feature"
    GNN placement is under active development. It works alongside the heuristic-based placer and may be activated in future releases.

---

## See Also

- [AI Design Agent](design-agent.md) — generates the BOM and netlist that feed the placer/router.
- [PCB Routing](../pcb/routing.md) — manual routing workflow.
- [Design Rules](../pcb/design-rules.md) — rules that constrain auto-routing.
