# Zones and Copper Planes

Copper zones (fills / pours) cover a board area with copper — typically used for **ground planes** or **power planes**. This is a standard practice in professional PCB design.

---

## Why Use Zones?

- **Ground plane** — reduces EMI noise and improves RF signal integrity
- **Power plane** — reduces voltage drop on power rails
- **Larger copper area** → lower impedance → better heat dissipation

---

## What Is a Zone?

![Copper zone outline](../img/pcb/zone-outline.png)

A filled zone follows its outline while maintaining clearance around objects on other nets. Pads on the zone net connect according to the configured zone connection style.

Each zone has:

| Property | Description |
|---|---|
| **Net** | The net name (e.g. `GND`, `VCC`) |
| **Layer** | Copper layer (e.g. F.Cu, B.Cu) |
| **Priority** | Higher-priority zones override lower ones where they overlap |
| **Clearance** | Minimum gap from pads and traces on other nets |
| **Outline** | The polygon you draw to define the zone boundary |

---

## Quick Ground Plane

The fastest way is the **Zone Manager** (**View → Zone Manager**, or **Shift+B**):

1. In **Quick Actions**, choose the layer — **Both (Top & Bottom)**, **F.Cu**, or **B.Cu**.
2. Select **Fill GND**. WireFrame creates a `GND` zone on that layer (see [where the outline comes from](#where-a-quick-zone-gets-its-outline)).
3. Select **Apply (Rebuild All Zones)** to compute the copper. Until you apply, the new zone exists but holds no copper — this lets you set priorities first.

The fill keeps clearance around pads and traces on other nets and connects `GND` pads into the copper. **Fill GND** is one undo step.

### Short video — Fill a ground plane from the Zone Manager

!!! note "Video production brief"
    1. **Prepare:** Open the sample PCB with a board outline and no copper zones.
    2. **Opening shot (1–2 s):** Show the board with the **Zone Manager** open and its table empty.
    3. **Action shot (5–8 s):** Choose **Both (Top & Bottom)**, select **Fill GND**, then **Apply (Rebuild All Zones)** and wait for the fill.
    4. **Result shot (2–3 s):** Hold on the filled board with the two `GND` rows in the Zone Manager table readable.
    5. **Deliver:** Export a **10–15 second** 1080p MP4.

---

## Zone Manager

**View → Zone Manager** (**Shift+B**) lists every copper zone of the active board and is the fastest place to create, adjust, and remove pours. Each board has its own Zone Manager window.

### Quick Actions

| Control | What it does |
|---|---|
| Layer + **Fill GND** | Adds a `GND` zone on **F.Cu**, **B.Cu**, or **Both (Top & Bottom)** |
| Net + layer + **Fill Net** | Adds a zone for any net on any copper layer, inner layers included. The net list has a search box |
| **Unfill All** | Clears the computed copper of every zone; the zones themselves stay. Use **Apply** to fill them again |
| **Apply (Rebuild All Zones)** | Recomputes every fill in the background; the button reads **Rebuilding...** until it finishes |

Quick actions add zones; they never replace existing ones. Pressing **Fill GND** twice creates two overlapping `GND` zones — delete the extra row.

!!! note "Ground plane on an inner layer"
    **Fill GND** handles **F.Cu**, **B.Cu**, and **Both**. For an inner layer such as **In2.Cu**, choose the net `GND` and that layer next to **Fill Net** instead.

#### Where a quick zone gets its outline

**Fill GND** and **Fill Net** take the zone outline from the first of these that exists:

1. Polygons or rectangles you have drawn **on that copper layer** — each one becomes a zone. Draw the area first when a plane should cover only part of the board.
2. The board outline on **Edge.Cuts**.
3. Without an outline: a rectangle around the placed footprints, with a 200 mil margin.

### The zone table

| Column | Meaning |
|---|---|
| **ID** | The zone's id. Zones with the same layer, net, priority, and name are shown as one row: `12 (+3)` means four zones edited together |
| **Layer** | Copper layer; change it from the list |
| **Net Name** | The zone's net, with a search box; `<No Net>` for an unconnected copper area |
| **Priority** | Higher wins where zones overlap — see [Zone Priority](#zone-priority) |
| **Clearance** | Minimum gap to other nets, in mil |
| **Thermal** | Thermal-relief spokes on pads of the zone's net instead of a solid connection |
| **Actions** | **Find** centres and zooms the canvas on the zone; **Del** removes it |

Every edit in the table is undoable with **Ctrl+Z**, one step per change — dragging a number field's stepper is a single step. After changing net, layer, priority, clearance, or thermal settings, select **Apply (Rebuild All Zones)** to see the new copper.

### Image — Zone Manager with two planes

!!! note "Image capture brief"
    1. **Prepare:** Open the sample PCB, create `GND` zones on both outer layers with **Fill GND**, and apply.
    2. **Build the frame:** Capture the **Zone Manager** window with **Quick Actions** and the zone table (ID, Layer, Net Name, Priority, Clearance, Thermal, Actions) readable. Suggested size: **900 × 360 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

---

## Creating a Zone Manually

1. Select a copper layer (e.g. **F.Cu**) in the Layer panel
2. Use the **Draw Polygon** tool to draw a closed polygon boundary
3. Assign zone properties:
    - **Net name** (e.g. `GND`)
    - **Clearance** (e.g. 0.2 mm)
    - **Priority** (default: 0)
4. WireFrame computes and renders the copper fill

---

## Zone Priority

When two zones overlap, the zone with the **higher priority** wins:

The higher-priority zone owns the overlapping copper area; the lower-priority zone remains in the rest of its valid outline.

### Image — Overlapping zones with different priorities

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture a GND zone at priority 0 and a smaller VCC island at priority 1. Show the zone outlines, net labels, and resulting filled overlap.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

!!! tip "Priority guidelines"
    - Ground plane → priority **0** (lowest)
    - VCC island inside the GND plane → priority **1**
    - Zone nested inside VCC → priority **2**, and so on

---

## How Zones Interact with Nets

| Situation | Result |
|---|---|
| Pad on the **same net** as the zone | Pad connects directly to the fill (no ratsnest) |
| Trace on the **same net** passing through | Trace connects to the zone |
| Pad on a **different net** inside the zone | Clearance gap is maintained around the pad |
| Trace on a **different net** inside the zone | Clearance gap is maintained around the trace |

---

## Editing Zones

| Property | Editable |
|---|---|
| Net name | ✅ — in the Properties panel or the Zone Manager |
| Layer | ✅ |
| Priority | ✅ |
| Clearance | ✅ |
| Outline (vertices) | ✅ — drag vertices to reshape the boundary |
| Cutouts | ✅ — add excluded shapes inside the zone |

---

## See Also

- [Routing](routing.md) — traces interact with zone clearances
- [DFM & DRC](dfm-and-drc.md) — zone connectivity is validated during DRC
- [Layers & Views](layers-and-views.md) — zone visibility follows layer settings
