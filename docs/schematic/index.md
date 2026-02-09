# Schematic Editor Overview

The schematic editor is used to:

- Place components (symbols).
- Draw wires and manage nets.
- Add text and drawing primitives.
- Configure sheet properties.

Core elements:

- **Canvas** with grid and page outline.
- **Schematic toolbar** (`Sch_Toolbar`).
- **Properties panel** (`Sch_Properties`).
- **Selection and interaction system** (`SelectionManager`).

> **Image placeholder**  
> `![Schematic workspace](img/schematic/workspace.png)`  
> _A mid‑complexity schematic with several components, wires, labels and annotations, and the toolbar visible at top._

---

## Schematic toolbar modes

The **DrawingMode** enum underpins toolbar behavior:

- `Select` – default selection/move mode.
- `Wire` – draw orthogonal wires between pins or arbitrary points.
- `Label` – place net labels (NetLabel symbols).
- `Text` – place text graphics.
- `Line`, `Rectangle`, `Circle`, `Arc`, `Polygon` – drawing primitives.
- `Junction` – place junction dots.
- `Harness` – draw net harness graphics.
- `PlacingGND`, `PlacingVCC` – place power symbols (GND, VCC).

Clicking a toolbar button changes the current mode; the status is reflected in the UI and in how mouse events are interpreted.

---

## Interaction model (schematic)

The schematic interaction state is managed by `SelectionManager`:

- States (simplified):
  - None
  - MovingSelection
  - DrawingSelectionBox
  - DrawingWire
  - DraggingWireVertex
  - DraggingWireSegment
  - MovingAttribute
  - DrawingPrimitiveShape
  - ResizingGraphicObject

User input handled:

- Mouse clicks, drags and release in the canvas.
- Keyboard shortcuts (Undo, Redo, Delete, Copy, Paste, Rotate, etc.).
- Context menus for components, wires and graphics.

High‑level operations:

- Click on component to select.
- Drag selected items to move (with attached wires updating).
- Draw wire from pin to pin or to an existing wire vertex.
- Right‑click for object‑specific context actions.

Next pages detail how to place components and draw wiring.

- [Placing Components](placing-components.md)
- [Wiring and Nets](wiring-and-nets.md)
- [Graphics & Annotations](graphics-and-annotations.md)
- [Properties & Attributes](properties-and-attributes.md)