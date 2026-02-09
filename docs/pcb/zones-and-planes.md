# Zones and Copper Planes

Copper zones (fills) are managed by `ZoneManager` and `PcbZone`.

---

## Basic concepts

A `PcbZone` includes:

- `id`
- `netName` (e.g., `GND`)
- `layerId` (e.g., F.Cu)
- `priority` (for overlapping zones)
- `outline` – user‑drawn polygon.
- `cutouts` – shapes to be excluded (circles, rectangles, capsules).
- **Computed islands**:
  - `vector<ZoneIsland>` each with:
    - `outer` – outer polygon (filled copper area).
    - `holes` – polygons representing holes inside the island.

Clearance and style parameters:

- `minClearance` – clearance from pads/traces.
- `thermalSpokeWidth` – for thermals on pads (future/partial support).

---

## Creating a zone

1. Draw a polygon on the desired copper layer.
2. Assign:
   - Net name.
   - Layer.
   - Clearance and priority.

Internally:

- `ZoneManager::addZone` assigns a new ID and keeps track of the zone.
- `ZoneManager::rebuildZoneFills` processes:
  - Original outline.
  - Cutouts.
  - Interactions with pads, traces and other zones.

> **Image placeholder**  
> `![Zone outline](img/pcb/zone-outline.png)`  
> _User selecting an area with a polygon outline representing the top copper GND pour._

---

## Zone fill computation

`ZoneManager::rebuildZoneFills` uses Clipper2:

- Converts ImGui `ImVec2` points to Clipper `Path64` with scaling.
- Applies boolean operations to:
  - Subtract clearances around pads/traces (same or different nets).
  - Apply cutouts (user‑defined shapes).
- Converts results back to sets of `ZoneIsland` structures.

Islands are then:

- Rendered as filled polygons in the PCB view.
- Used during DFM/DRC and ratsnest connectivity checks.

---

## Ground plane from board outline

`PcbDocument::fillGroundPlane`:

- Attempts to infer board outline geometry from:
  - Closed polygons.
  - Edge.Cuts graphics.
- Generates a GND zone covering the board interior.
- Uses `ZoneManager` to build actual islands.

From the user’s perspective:

- A menu action like “Fill Ground Plane” triggers this.
- The board is filled with a semi‑transparent copper area attached to `GND` net.

> **Video placeholder**  
> _Short clip: user clicks "Fill GND Plane" and the entire board inside Edge.Cuts is filled with a hatched/solid copper zone, showing thermals around pads._

---

## Zone interaction with nets

`PcbNetlistManager` integrates zones when building connectivity graphs:

- Pads touching same‑net zones are treated as connected.
- Traces entering the zone area also connect to that net (with clearance constraints).

Additionally:

- `ZoneManager::isPointInsideSameNetZone` can be used to test if a location is inside a same‑net copper area, useful for routing constraints and DFM checks.