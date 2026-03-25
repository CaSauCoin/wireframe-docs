# PCB Editor Overview

The PCB editor handles board layout — from component placement to trace routing, copper zones, design rule checks, and manufacturing file export.

---

## What You Can Do

| Task | Tool / Feature |
|---|---|
| Place footprints from libraries or schematic | Library panel / Available Footprints dialog |
| Route traces between pads | Route Trace tool with 45° guidance |
| Place vias and change routing layers | Via tool / ++v++ during routing |
| Add mechanical holes | Place Hole tool |
| Define the board outline | Edge.Cuts layer + drawing tools |
| Fill copper zones (ground planes) | Zone Manager / Fill GND Plane |
| Run DFM/DRC checks | DFM panel |
| Export Gerber, drill, BOM | Fabrication dialog |
| Preview the board in 3D | 3D Viewer |

---

## PCB Workspace

The workspace consists of:

- **Canvas** — the board area with grid, showing footprints, traces, zones, and ratsnest lines.
- **PCB toolbar** — floating at the top of the canvas.
- **Layer panel** — toggle visibility and select the active routing layer.
- **Library panel** — lists loaded footprint libraries.
- **Properties panel** — edits properties of the selected PCB item.

<!-- TODO: Replace with actual screenshot
     Capture a PCB board at a mid-design stage:
     - _8–12 footprints placed on the board (mix of SMD and through-hole)._
     - _Several routed traces visible in red (F.Cu) and blue (B.Cu) colors._
     - _A few remaining **ratsnest lines** (thin, dashed) showing unrouted connections._
     - _A **copper zone** (GND) fill visible on one layer with clearance gaps around pads._
     - _The **board outline** visible in magenta (Edge.Cuts)._
     - _The PCB toolbar at the top with the Select tool active._
     - _Layer panel on the right showing F.Cu highlighted._
     Suggested size: 1280×720px.
-->
![Workspace](../img/pcb/workspace.png)


---

## PCB Toolbar Tools

| Tool | Icon | Mode | Shortcut |
|---|---|---|---|
| **Select** | Arrow | Default selection and move | ++esc++ |
| **Place Footprint** | IC package | Place from library or available list | — |
| **Route Trace** | Trace path | Route traces between pads | ++x++ |
| **Draw Via** | Via circle | Place vias manually | ++v++ |
| **Place Hole** | Drill circle | Place mechanical holes | — |
| **Draw Line** | Line | Draw graphic lines | — |
| **Draw Rect** | Rectangle | Draw rectangles (board outline, etc.) | — |
| **Draw Circle** | Circle | Draw circles | — |
| **Draw Arc** | Arc | Draw arcs | — |
| **Draw Polygon** | Pentagon | Draw polygons | — |
| **Draw Text** | "T" | Place text on silk/fab layers | — |
| **Measure** | Ruler | Measure distances between points | — |

---

## Board Boundary

Each the PCB document includes a board boundary:

- Defined by a board boundary definition (simple rectangular min/max) or by **Edge.Cuts** drawing objects (rectangles/polygons).
- Used for:
    - DFM checks (footprints inside board area).
    - Zone fill clipping.
    - Gerber export (board outline layer).

!!! tip "Defining the board outline"
    Switch to the **Edge.Cuts** layer and use the Rectangle or Polygon drawing tool. This creates the physical board shape that manufacturers will cut.

---

## Nets and Ratsnests

WireFrame manages electrical connectivity:

| Concept | Description |
|---|---|
| **PcbNet** | A named net with a set of pin references (footprint ID + pad number) |
| **Pad-to-net map** | Maps each pad to its net name |
| **Connectivity graph** | Includes traces, vias, and zones |
| **Ratsnest lines** | Thin lines drawn between unconnected endpoints of the same net |

Ratsnest lines:

- Are **rebuilt automatically** when nets are marked dirty (after edits).
- **Disappear** as you route traces to complete connections.

<!-- TODO: Replace with actual video
     Record a 15-second clip:
     1. _A PCB with several unrouted ratsnest lines visible._
     2. _Route one trace from pad to pad — the ratsnest line between them disappears._
     3. _Route another trace — another line vanishes._
     4. _Briefly zoom out to show the remaining ratsnest lines._
     Resolution: 1280×720 at 30fps.
-->

[//]: # (<video controls width="100%">)

[//]: # (  <source src="../../img/pcb/ratsnest-demo.webm" type="video/webm">)

[//]: # (  <source src="../../img/pcb/ratsnest-demo.mp4" type="video/mp4">)

[//]: # (  Your browser does not support the video tag.)

[//]: # (</video>)


---

## Section Pages

| Page | What you'll learn |
|---|---|
| [Footprints & Placement](footprints-and-placement.md) | Load libraries, place and arrange footprints |
| [Routing](routing.md) | Route traces, manage vias and holes |
| [Layers & Views](layers-and-views.md) | Layer management, visibility, navigation |
| [Zones & Planes](zones-and-planes.md) | Copper fills, ground planes, zone priorities |
| [DFM & DRC](dfm-and-drc.md) | Design rule and manufacturability checks |
| [Fabrication & Export](fabrication-and-export.md) | Gerber, drill, BOM, PDF export |
