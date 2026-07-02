# Footprints and Placement

Footprints are the **physical packages** placed on the PCB — pads, drill holes, silkscreen graphics, and optional 3D models. This page covers loading libraries, placing, moving, rotating, and flipping footprints.

---

## Loading Footprint Libraries

From the **Library panel** while a PCB tab is active:

1. Click **Load Footprints…**
2. Select one or more KiCad footprint files (`.kicad_mod`)
3. WireFrame parses the footprint data in the background
4. After parsing, footprint names appear in the list and can be filtered

Each loaded footprint contains:

| Data | Description |
|---|---|
| **Pads** | Number, position, shape (circle/rect/oval), drill size, layers |
| **Graphics** | Lines, arcs, circles, polygons, reference and value text |
| **3D model** | Optional STEP/OBJ file path with offset, scale, and rotation |

!!! info "Free KiCad footprint libraries"
    Download from [https://www.kicad.org/libraries/](https://www.kicad.org/libraries/) — WireFrame is fully compatible.

---

## Placing Footprints

### Method 1: From schematic conversion (recommended)

After running **Project → Convert to PCB**, an **Available Footprints** list shows all unplaced schematic components:

1. Open the "Available Footprints" dialog (appears automatically after conversion)
2. Select a component from the list
3. Click on the board to place it
4. The footprint appears with its ID matching the schematic component (e.g. `U1`, `R3`)

### Method 2: Directly from the library

1. In the **Library panel**, double-click a footprint name
2. The PCB enters **placement mode** — the footprint preview follows the cursor
3. Press ++r++ to rotate before placing (if needed)
4. **Left-click** to place at the desired position

| Action | Input |
|---|---|
| Place footprint | Left-click |
| Rotate before placing | ++r++ |
| Cancel placement | Right-click or ++esc++ |

---

## Moving and Rotating Footprints

### Moving

1. **Select** one or more footprints
2. **Click and drag** to move them on the board
3. Connected traces and vias **automatically update their endpoints** to maintain pad connections

All move operations support full **Undo** (++ctrl+z++).

### Rotating

| Action | Input |
|---|---|
| Rotate 90° | ++r++ or context menu → Rotate |

After rotating:
- The footprint angle is updated
- All pad positions are recomputed
- Connected trace endpoints adjust to the new pad locations

---

## Flipping Footprints (Front ↔ Back)

To move a component to the **opposite side of the board**:

1. Select one or more footprints
2. Press ++f++ or **context menu → Flip**
3. Layers are swapped:
    - `F.Cu` → `B.Cu`, `F.SilkS` → `B.SilkS`, and so on

```
Before flip (top layer):      After flip (bottom layer):
  ┌─[R1]─┐                      ┌─[1R]─┐   ← text mirrors
  │ F.Cu  │                      │ B.Cu  │   ← color changes
  └───────┘                      └───────┘
```

!!! info "Visual feedback"
    Flipped footprints change color (e.g. red F.Cu → blue B.Cu) and the designator text may mirror — this is the expected behavior and matches the physical reality of a bottom-side component.

---

## Adjusting Designator Text Position

Each footprint has a designator label (e.g. "R1", "U3") that can be repositioned independently:

| Feature | Description |
|---|---|
| Position | Drag the designator text separately from the footprint body |
| Rotation | Rotate the label independently |
| Selection | Click directly on the text to select only the text |

Use this when the designator overlaps a trace or pad — drag it to a clear area nearby.

---

## Unplace vs. Delete

| Operation | Result |
|---|---|
| **Unplace** | Removes from the board, returns it to the "Available" list — can be placed again later |
| **Delete** | Permanently removes the footprint (and connected traces) — fully undoable |

!!! tip "When to use Unplace"
    Use **Unplace** if the component still exists in the schematic and you want to place it again later. Use **Delete** to remove it from the PCB entirely.

---

## See Also

- [Routing](routing.md) — route traces between placed footprints
- [Footprint Libraries](../libraries/footprints-library.md) — create and manage footprint libraries
- [3D Viewer](../advanced/3d-viewer.md) — preview footprints with 3D models
