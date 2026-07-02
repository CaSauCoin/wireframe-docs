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

```
Example — routing U1 to R1:

  [U1.Pin3]══════════════[R1.Pad1]
               ↑
       completed trace (red = F.Cu)

  ╌╌╌╌╌╌ ratsnest line disappears once routed
```

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

```
  F.Cu:  [U1]══════●
                    │  ← Via (through-hole)
  B.Cu:             ●══════[R5]
```

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

!!! info "Automatic net update"
    Deleting or modifying a trace marks the affected net as dirty → the ratsnest is automatically recomputed to show any missing connections.

---

## Gloss Trace — Cleaning Up

After routing, WireFrame can **automatically clean up** trace geometry:

- Removes **redundant vertices** (collinear points)
- Simplifies short zig-zag segments
- Makes 45° corners clean and precise

```
Before Gloss:          After Gloss:
  ──╮                   ──╲
    ╰──╮                   ╲──
        ╰─                    ─
  (redundant vertices)    (clean 45°)
```

Use: **context menu → Gloss** or the corresponding shortcut.

---

## Smart Drag

WireFrame maintains connections during drag operations:

- **Moving a via** — attached traces keep their endpoints connected to the via
- **Moving a footprint** — connected trace endpoints adjust automatically to maintain pad attachment

---

## See Also

- [Footprints & Placement](footprints-and-placement.md) — place footprints before routing
- [Layers & Views](layers-and-views.md) — manage layers during routing
- [Zones & Planes](zones-and-planes.md) — copper fills interact with trace clearances
- [DFM & DRC](dfm-and-drc.md) — check clearances and widths after routing
