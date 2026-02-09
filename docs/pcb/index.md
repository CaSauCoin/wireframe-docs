# PCB Editor Overview

The PCB editor manages board layout and routing:

- Footprint placement.
- Trace routing (with 45° helpers and collision checks).
- Via and hole placement.
- Layer management.
- Zones (copper pours).
- DFM/DRC checks.
- Fabrication exports (Gerber, BOM, drill).

Key components:

- `PcbDocument` – main document model.
- `FootprintManager` – placed footprints.
- `TraceManager` – traces, vias, holes and routing helpers.
- `LayerManager` – layer definitions and colors.
- `DrawingManager` – PCB drawing graphics.
- `PcbNetlistManager` – PCB net connectivity and ratsnests.
- `ZoneManager` – copper zone fills.

> **Image placeholder**  
> `![PCB workspace](img/pcb/workspace.png)`  
> _A PCB board with components, routed traces, zones and ratsnest lines visible._

---

## PCB toolbar tools

`PcbTool` enum defines modes:

- `SELECT`
- `PLACE_FOOTPRINT`
- `ROUTE_TRACE`
- `DRAW_VIA`
- `PLACE_HOLE`
- `DRAW_LINE`
- `DRAW_RECT`
- `DRAW_CIRCLE`
- `DRAW_ARC`
- `DRAW_POLY`
- `DRAW_TEXT`
- `MEASURE`

The active tool is highlighted in the floating toolbar. Mouse and keyboard behavior change based on the current tool.

---

## Board boundary

Each `PcbDocument` includes:

- `BoardBoundary` (simple min/max rectangle, with enable flag).
- Board can also be defined by `Edge.Cuts` drawing objects (rectangles/polygons).

Ratsnest computations and some DFM checks use the board boundary to:

- Determine if footprints lie inside the board.
- Clip certain operations to board area.

---

## Nets and ratsnests

`PcbNetlistManager` manages:

- `PcbNet` structures: net name + set of `PcbPinRef` (footprint ID + pad number).
- Map from pads to net names.
- Connectivity graph including traces, vias, zones.

Ratsnests:

- Lines drawn between unconnected net endpoints.
- Rebuilt when nets are marked dirty (`markNetDirty`).
- Visualized in `Pcb_Panel::renderRatsnest`.

Next:

- [Footprints & Placement](footprints-and-placement.md)
- [Routing](routing.md)
- [Layers & Views](layers-and-views.md)
- [Zones & Planes](zones-and-planes.md)
- [DFM & DRC](dfm-and-drc.md)
- [Fabrication & Export](fabrication-and-export.md)