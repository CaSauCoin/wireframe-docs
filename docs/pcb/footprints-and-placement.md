# Footprints and Placement

Footprints are the **physical packages** placed on the PCB — pads, drill holes, silkscreen graphics, and optional 3D models. This page covers how footprints reach the board, and how to move, rotate, flip, and remove them.

---

## Where Footprints Come From

Every footprint on a board belongs to a component of the project's schematic. The footprint itself is the one assigned to that symbol (see [Symbols Library](../libraries/symbols-library.md)).

| Data | Description |
|---|---|
| **Pads** | Number, position, shape, drill size, layers |
| **Graphics** | Silkscreen, fabrication, and courtyard outlines; reference and value text |
| **3D model** | Optional STEP or other 3D file with offset, scale, and rotation |

Footprint sources are managed in **View → Local Library Manager** — KiCad footprint folders, single `.kicad_mod` files, and converted Altium libraries. **Load Footprints...** at the top of the PCB **Footprints** panel adds one `.kicad_mod` file to the library.

!!! info "Free KiCad footprint libraries"
    The official KiCad libraries at [https://www.kicad.org/libraries/](https://www.kicad.org/libraries/) can be added as a footprint source.

---

## Placing Footprints

### From the schematic (the normal way)

With a schematic of the project active, run **Tools → Update Schematic to PCB** (choose the target board when the project has several PCBs). WireFrame then:

1. collects every sheet of the design, starting from the top sheet;
2. loads each component's footprint, assigning one from the library symbol when the field is empty, and lists components whose footprint cannot be found;
3. **keeps** footprints that are already on the board — position, rotation, and side — when their footprint did not change;
4. **removes** footprints whose component no longer exists in the schematic;
5. places **new** footprints in a grid, 200 mil apart, starting at the board origin;
6. updates the nets and saves the PCB.

Drag the new footprints from the grid to their places on the board. A project is required: a standalone schematic cannot be converted.

### Placing an unplaced footprint again

The **Footprints** panel (right side, with a PCB active) lists footprints that belong to the design but are not on the board — for example ones you removed with ++delete++. It reads **All components placed.** when there are none.

1. Type in **Filter...** to find the footprint.
2. **Drag** its row onto the canvas. It lands at the drop point, at 0°, on the top side.

---

## Moving, Rotating, and Flipping

| Action | How |
|---|---|
| Select | Click a footprint; drag a box over several |
| Move | Drag the selection, or nudge with the arrow keys (5 mil per press) |
| Rotate | ++space++ — by the step set in **Preferences → Editing** (90° by default) |
| Flip to the other side | ++f++, or **Flip Layer (F)** in Properties |
| Exact position | **Properties → Footprint Properties → Transform**: **X**, **Y**, **Rotation** |

Connected traces and vias keep their endpoints on the pads while you move or rotate. All of these are undoable (++ctrl+z++).

### Flipping (Front ↔ Back)

Flipping moves a footprint to the opposite side of the board. Its copper and silkscreen move to the back-layer set (`F.Cu` → `B.Cu`, `F.SilkS` → `B.SilkS`, and so on), and the footprint is mirrored as seen from the top. **Properties** shows **(Current: Top)** or **(Current: Bottom)**.

!!! info "Visual feedback"
    Flipped footprints change color (e.g. red F.Cu → blue B.Cu) and the designator mirrors — this matches the physical reality of a bottom-side component.

---

## Footprint Properties

Select one footprint to see **Footprint Properties**:

| Field | Description |
|---|---|
| **Reference** | Designator, e.g. `R1` |
| **Value** | Value text, e.g. `10k` |
| Library | The footprint it was built from (read-only) |
| **Transform** | **X**, **Y** (mil, with mm beside), **Rotation** |
| **Flip Layer (F)** | Moves it to the other side |

---

## Adjusting Designator Text

Each footprint has a designator label (e.g. "R1", "U3") that can be moved on its own:

| Action | How |
|---|---|
| Select only the text | Click directly on the designator |
| Move | Drag it |
| Rotate | ++space++ with the designator selected |
| Align several | Select the designators, right-click → **Align Designators ▸** (**Align Left**, **Align Right**, **Align Center (H)**, **Align Top**, **Align Bottom**, **Align Center (V)**), or ++shift+y++ / ++shift+x++ |

Use this when the designator overlaps a trace or pad.

---

## Removing a Footprint

Select a footprint and press ++delete++. The footprint leaves the board and goes back to the **Footprints** panel, so you can drag it in again. Its traces stay where they are. Removing it is undoable.

To remove a component from the design for good, delete it in the schematic and run **Update Schematic to PCB** again.

---

## See Also

- [Routing](routing.md) — route traces between placed footprints
- [Footprint Libraries](../libraries/footprints-library.md) — create and manage footprint libraries
- [3D Viewer](../advanced/3d-viewer.md) — preview footprints with 3D models
- [Placement and Routing Assistant](../ai/auto-placer-router.md) — AI-assisted placement
