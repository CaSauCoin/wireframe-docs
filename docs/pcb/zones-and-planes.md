# Zones and Copper Planes

Copper zones (fills/pours) cover board areas with copper, typically for ground planes or power distribution. Zones are managed by the zone engine.

---

## Basic Concepts

A a copper zone includes:

| Property | Description |
|---|---|
| `id` | Unique zone identifier |
| `netName` | Assigned net (e.g., `GND`, `VCC`) |
| `layerId` | Copper layer (e.g., F.Cu, B.Cu) |
| `priority` | Higher-priority zones override lower ones where they overlap |
| `outline` | User-drawn polygon defining the zone boundary |
| `cutouts` | Shapes excluded from the fill (circles, rectangles, capsules) |
| `minClearance` | Minimum clearance from pads and traces |

### Computed output

After fill computation, each zone contains **islands**:

| Structure | Description |
|---|---|
| Outer boundary | Outer polygon of the filled copper area |
| Internal holes | Hole polygons inside the island (clearance areas) |

---

## Creating a Zone

### Manual zone creation

1. Select a copper layer (e.g., **F.Cu**) as the active layer.
2. Use the **Draw Polygon** tool to draw a closed polygon.
3. Assign zone properties:
    - **Net name** (e.g., `GND`).
    - **Clearance** (e.g., 8 mil).
    - **Priority** (default: 0).
4. WireFrame computes the filled copper islands.

### Quick ground plane

Use **Tools → Fill GND Plane** (or equivalent menu action):

1. WireFrame infers the board outline from Edge.Cuts geometry.
2. Generates a GND zone covering the entire board interior.
3. Clearances are computed around all pads and traces.

<!-- TODO: Replace with actual screenshot
     Capture a zone being created or just after creation:
     - _The zone polygon outline visible on F.Cu (dashed or highlighted border)._
     - _The zone assigned to "GND" net (visible in Properties panel or as text on the zone)._
     - _Inside the zone: filled copper area with clearance gaps around pads of other nets._
     - _Thermal connections visible on GND pads (spoke-style connections)._
     Suggested size: 700×500px.
-->
![Zone Outline](../img/pcb/zone-outline.png)


---

## Zone Fill Computation

WireFrame uses the **Clipper2** library for polygon boolean operations:

### Process

1. Convert zone outline points to Clipper `Path64` with scaling.
2. Apply **boolean subtraction** for:
    - Clearances around pads and traces of **different** nets.
    - User-defined cutouts.
    - Other zones with higher priority.
3. Convert results back to zone island structures.

### Rendered result

- Filled islands are drawn as **semi-transparent polygons** on the PCB canvas.
- Clearance gaps appear around non-matching pads and traces.
- Same-net pads connect to the zone (with thermal relief, when supported).

!!! info "Performance"
    Zone fill computation can be intensive for complex boards with many pads and traces. The fill is rebuilt when you explicitly trigger it or when relevant objects change.

---

## Ground Plane from Board Outline

the ground plane fill feature automates ground plane creation:

1. Infers board outline geometry from:
    - Closed polygons on Edge.Cuts.
    - Board boundary settings.
2. Creates a GND zone covering the entire board interior.
3. Uses the zone engine to compute islands.

From the user's perspective:

- Click **"Fill GND Plane"** → the board fills with copper.
- All non-GND pads show clearance gaps.
- GND pads have thermal connections (spokes).

<!-- TODO: Replace with actual video
     Record a 15-second clip:
     1. _A PCB with placed footprints and routed traces, but no copper fill._
     2. _Click "Tools → Fill GND Plane" from the menu._
     3. _The board fills with a semi-transparent copper overlay on the active layer._
     4. _Zoom in to show clearance gaps around non-GND pads._
     5. _Show thermal connections (spokes) on a GND pad if visible._
     Resolution: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/pcb/fill-gnd-plane.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

## Zone Interaction with Nets

the PCB netlist engine integrates zones into the connectivity graph:

| Rule | Description |
|---|---|
| Same-net pads | Pads touching a same-net zone are treated as connected |
| Same-net traces | Traces entering the zone area connect to the net |
| Different-net pads | Clearance gap is maintained around the pad |
| Different-net traces | Clearance gap is maintained around the trace |

zone membership testing tests if a location is inside a same-net copper area — useful for routing constraints and DFM checks.

---

## Zone Properties and Editing

| Property | Editable | Description |
|---|---|---|
| Net name | Yes | Assign which net the zone belongs to |
| Layer | Yes | Which copper layer the zone fills |
| Priority | Yes | Higher values override lower priority zones |
| Clearance | Yes | Minimum gap from other-net copper |
| Outline | Yes | Drag vertices to reshape the zone boundary |
| Cutouts | Yes | Add shapes to exclude from the fill |

!!! tip "Zone priority"
    Use priority to create nested zones — for example, a VCC island inside a GND plane. The VCC zone should have a higher priority number than the GND zone.

---

## See Also

- [Routing](routing.md) — traces interact with zone clearances.
- [DFM & DRC](dfm-and-drc.md) — zone connectivity is checked during DRC.
- [Layers & Views](layers-and-views.md) — zone visibility follows layer settings.
