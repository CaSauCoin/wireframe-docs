# Routing Traces

Tracing connects pads on the PCB, enforcing electrical and design‑rule constraints.

---

## Routing mode

Select **Route Trace** tool from the PCB toolbar.

Behavior:

- Click on a pad or existing trace segment to start routing.
- The active trace follows the mouse with 45° helper points computed by `TraceManager::calculate45DegreeRoute` or `computePath`.
- Left‑click to confirm each vertex.
- Right‑click or an end‑route shortcut finishes the current trace.

Trace data:

- Each `Trace` holds:
  - `id`
  - `netName`
  - `layer`
  - `width`
  - `points` (polyline in board units, typically mils)

---

## Collision and clearance checks

`TraceManager::isSegmentColliding` checks:

- Clearance against:
  - Other traces on the same layer (width and min distance).
  - Footprint pads.
  - Holes and vias.
  - Board outline and copper zones.

Routing helpers:

- Prevent dropping segments too close to other copper.
- Can be extended with "shove" algorithms (some basic shoving is hinted in comments).

> **Image placeholder**  
> `![Routing collision](img/pcb/routing-collision.png)`  
> _Routing a trace where a red warning indicator appears if the route gets too close to another trace._

---

## Editing existing traces

Operations:

- **Move entire trace**:
  - Select trace(s), drag them via the selection move handler.
  - `PcbMoveCommand` stores start and end points per trace.

- **Drag a trace segment**:
  - SelectionManager supports dragging a single segment while keeping adjacent segments constrained.
  - Useful to tidy up the route without re‑routing everything.

- **Delete traces**:
  - Select trace(s) and press Delete.
  - `DeleteTraceCommand` and/or `DeletePcbItemsCommand`:
    - Remove traces.
    - Mark corresponding nets dirty for ratsnest recomputation.

---

## Vias and layer changes

To switch layers within a route:

1. While routing, place a **via** using:
   - A key (e.g. `V`) or
   - Switching to **Draw Via** tool and clicking.

2. `TraceManager::addVia` creates a `Via` at the current mouse position:
   - Stores net name.
   - Diameter and drill (default from design rules).

3. Continue routing on the new layer from the via point.

Vias are objects with:

- `id`, `position`, `netName`.
- `diameter`, `drill`.
- `isOrphaned` flag (for DFM checks).

---

## Mechanical holes

Use **Place Hole** tool:

- `TraceManager::addHole` adds a `Hole` with:
  - `id`, `position`, `diameter`, `plated` flag, `netName` (if plated).

Holes are typically used for:

- Mounting.
- Non‑plated holes for mechanical fixtures.
- Occasionally net‑connected plating (e.g., GND slotted holes).

> **Image placeholder**  
> `![Vias and holes](img/pcb/vias-holes.png)`  
> _A board with multiple vias along a trace and four mechanical mounting holes at the corners._

---

## Sticky endpoints and advanced dragging

For advanced operations:

- `TraceManager::updateTraceEndpointsForVia` updates traces when vias move.
- `SelectionManager` uses `StickyEndpoint` structures to keep trace endpoints snapped to pads or vias during drag operations.

From a user perspective:

- When you drag a via, traces attached to it remain connected.
- When you move a footprint, connected traces endpoints are adjusted accordingly (via `TraceManager::updateTraceEndpoints`).

---

## Autorouting helpers (45° paths, mitering, gloss)

Supporting functions:

- `TraceManager::calculate45DegreeRoute` – generates 45° path between start and end.
- `TraceManager::applyMitering` and `performMiteringOnPoints` – clean up corners with mitering.
- `TraceManager::glossTrace` – attempts to simplify trace geometry.

These are used to:

- Suggest or finalize clean 45° routes.
- Remove redundant vertices and smooth the trace.

> **Video placeholder**  
> _Short clip where a user routes a trace, then a "Gloss" action simplifies corners and short zig‑zags into smooth 45° segments._