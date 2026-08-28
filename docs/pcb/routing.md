# Routing Traces

Trace routing connects pads on the PCB with copper paths, enforcing electrical and design-rule constraints. This page covers the full routing workflow: drawing traces, placing vias, adding holes, and routing helpers.

---

## Starting a Route

Press ++x++ or click **Route Trace** on the PCB toolbar.

### Drawing a trace

1. **Click on a pad** (or an existing trace/via) to start routing
2. The trace follows the cursor with **45° helper points** computed automatically
3. **Left-click** to confirm each corner vertex
4. **Click the destination pad** to complete the trace — the ratsnest line disappears
5. Or **right-click** / ++esc++ to cancel

The ratsnest connection disappears when the destination is electrically complete.

### Image — Completed pad-to-pad route

!!! note "Image needed"
    Capture one short F.Cu route between two pads, with the completed track selected and the corresponding ratsnest connection cleared.

| Action | Input |
|---|---|
| Start on a pad | Left-click |
| Add a corner | Left-click |
| Finish on the destination pad | Left-click on target pad |
| Cancel | Right-click or ++esc++ |
| Switch layer (place via) | ++v++ while routing |

---

## Real-Time Clearance Checking

During routing, WireFrame checks for violations and **warns immediately** if the trace is too close to:

| Check | Example |
|---|---|
| Trace ↔ Trace | Two traces on the same layer too close together |
| Trace ↔ Pad | Trace overlapping a pad from a different net |
| Trace ↔ Via/Hole | Trace crossing through a drill area |
| Trace ↔ Board Edge | Trace too close to Edge.Cuts |

- A **red indicator** appears at the violation point
- The trace cannot be completed while a clearance violation is active

---

## Vias — Switching Layers

A via is a plated hole that connects **F.Cu and B.Cu**, allowing a trace to change board sides.

### Placing a via while routing

1. While routing on **F.Cu**, press ++v++
2. A via is placed at the current cursor position
3. The active routing layer switches to **B.Cu**
4. Continue routing on B.Cu from the via

### Image — Route changing layer through a via

!!! note "Image needed"
    Capture a selected route that begins on F.Cu, changes layer through a via, and continues on B.Cu. Keep both layer colors visible.

### Manual via placement

1. Select the **Draw Via** tool from the toolbar
2. Click on the board to place a via
3. Assign a net in the Properties panel if needed

### Via properties

| Property | Description |
|---|---|
| Diameter | Copper annular ring outer diameter |
| Drill | Drill hole diameter |
| Net | The electrical net the via belongs to |

---

## Mechanical Holes

Use the **Place Hole** tool to add **non-electrical** holes (screws, standoffs):

1. Select Place Hole from the toolbar
2. Click on the board to place it
3. Set parameters in the Properties panel:

| Property | Description | Example |
|---|---|---|
| `diameter` | Hole diameter | 3.2 mm for M3 screws |
| `plated` | Whether the hole has copper plating | Usually `false` |
| `netName` | Net if plated (e.g. for GND stitching) | `GND` |

---

## Editing Existing Traces

| Operation | How |
|---|---|
| **Move an entire trace** | Select + drag |
| **Drag a segment** | Click and drag a segment between two vertices |
| **Delete a trace** | Select + ++delete++ (ratsnest reappears) |
| **Move a segment** | Drag the selected segment; collision checks ignore only the segment being edited |
| **Delete a segment** | Select the segment and delete it without removing unrelated route geometry |
| **Align segments** | Use the alignment action to create a DRC-aware parallel offset |

## Net classes and advanced rules

Open **Design Rules Manager** to assign width and clearance behavior by net class. Automatic rules can classify common power nets and serialize assignments with the board, while a manual net assignment takes precedence.

For dense connections, multi-trace routing can move a group of traces with automatic node snapping and parallel polyline offsets. Always re-run DFM after an aligned or multi-trace edit.

!!! info "Automatic net update"
    Deleting or modifying a trace marks the affected net as dirty → the ratsnest is automatically recomputed to show any missing connections.

---

## Gloss Trace — Cleaning Up

After routing, WireFrame can **automatically clean up** trace geometry:

- Removes **redundant vertices** (collinear points)
- Simplifies short zig-zag segments
- Makes 45° corners clean and precise

### Image — Route before and after Gloss

!!! note "Image needed"
    Use a two-panel image of the same route before and after **Gloss**, clearly showing removed redundant vertices and cleaner 45° corners.

Use: **context menu → Gloss** or the corresponding shortcut.

---

## Smart Drag

WireFrame maintains connections during drag operations:

- **Moving a via** — attached traces keep their endpoints connected to the via
- **Moving a footprint** — connected trace endpoints adjust automatically to maintain pad attachment

---

## Auto-Snapping

While routing, WireFrame automatically **snaps the cursor** to nearby connection targets:

| Target | Behavior |
|---|---|
| **Pad center** | Cursor snaps to the pad center when nearby — ensures perfect connection |
| **Existing via** | Cursor snaps to via center for easy connection |
| **Existing trace** | Cursor snaps to the nearest point on a trace segment of the same net |

Auto-snapping prevents common routing errors like "almost connected" traces that look connected but fail DFM checks.

---

## Segment Merging

When you extend an existing trace or add a segment that continues in the same direction, WireFrame **automatically merges** collinear segments into a single continuous trace:

After merging, consecutive collinear pieces behave as one continuous segment. Verify the result by selecting the route and checking that no unintended corner remains.

This keeps the design clean and reduces the number of trace objects in the file.

---

## Bus Routing (Multi-Trace)

WireFrame supports routing multiple parallel traces simultaneously:

- When routing from a group of pads (e.g., a data bus D0–D7), the router can create **parallel traces** with a consistent offset (Slave-Master pattern).
- Traces maintain equal spacing and follow the same routing path shape.

---

## Double-Click Net Selection

**Double-click** on any trace to select the **entire net** — all trace segments and vias connected to the same net are highlighted at once.

This is useful for:

- Reviewing a complete signal path
- Deleting an entire net's routing
- Checking net connectivity visually

---

## AI Auto-Router

WireFrame includes an AI-powered automatic router that can route **all connections** on the board:

- Proposes routing based on the current board and constraints.
- Requires review of layers, clearances, vias, and remaining ratsnest connections.
- See [Placement and Routing Assistant](../ai/auto-placer-router.md) for the complete guideline.

---

## See Also

- [Footprints & Placement](footprints-and-placement.md) — place footprints before routing
- [Layers & Views](layers-and-views.md) — manage layers during routing
- [Zones & Planes](zones-and-planes.md) — copper fills interact with trace clearances
- [Design Rules & Net Classes](design-rules.md) — configure clearance and trace width rules
- [DFM & DRC](dfm-and-drc.md) — check clearances and widths after routing
- [Placement and Routing Assistant](../ai/auto-placer-router.md) — AI-assisted placement and routing review
