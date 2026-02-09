# Footprints and Placement

Footprints are packages placed onto the PCB, managed by `FootprintManager`.

---

## Loading footprint libraries

From the **Library panel** while a PCB is active:

1. Use a “Load Footprints…” control to select KiCad footprint libraries.
2. WireFrame parses footprint data through `KicadFootprintParser`.
3. Parsed footprints appear by name.

Footprint data includes:

- Pads (number, position, shape, drill, layers).
- Graphics (lines, arcs, circles, polygons, reference text, value text).
- Optional 3D model (file path and transform).

> **Image placeholder**  
> `![Footprint library panel](img/pcb/footprint-library.png)`  
> _Panel showing a list of footprints, search filter and a preview area._

---

## Placing footprints

### From “available footprints” list

`PcbDocument` maintains `m_availableFootprints`:

- A map from schematic‑linked component IDs to footprint library names.
- Represents footprints waiting to be placed.

Use commands such as:

- `PlaceFootprintCommand` or `AddFootprintCommand` to:
  - Add a footprint at a given world position.
  - Remove it from the available list.

User flow:

1. In a PCB document, open a dialog listing unplaced schematic components and their footprints.
2. Select an item, then click on the board to place.
3. The footprint appears at that location with its `id` equal to the schematic component ID (e.g. `U1`).

### Direct placement

You can also place generic footprints from library without schematic linkage:

1. In Library panel, double‑click a footprint name.
2. The PCB enters placement mode with that footprint attached to the mouse.
3. Click to place at desired location.

---

## Moving and rotating footprints

With footprints selected:

- **Move**:
  - Drag with the mouse.
  - `PcbMoveCommand` captures:
    - Old and new positions of footprints.
    - Associated trace/via/hole positions (if moving them together).
    - On execute/undo, trace endpoints and via positions are updated accordingly.

- **Rotate**:
  - Use rotation shortcut or menu.
  - `PcbRotateCommand`:
    - Adjusts footprint rotations.
    - Recomputes pads and updates traces connected to those pads.
    - Restores trace point arrays on undo.

> **Video placeholder**  
> _Short clip showing multiple footprints rotated together by 90°, with connected traces moving to stay attached to their pads._

---

## Flipping footprints (front ↔ back)

For selected footprints and other board items:

- `PcbFlipItemsCommand` toggles their side:
  - Flips footprints across board center axis (updates their layer IDs).
  - Flips vias, holes and graphics if selected.
- Executing the command again (undo) flips them back.

---

## Editing footprint designators

Each `PlacedFootprint` has:

- `id` – designator (e.g. `R1`).
- `designator` text graphic (if defined in footprint).
- Calculation of text bounds via `calculateDesignatorBounds`.

You can:

- Click on designator text to select and drag it (adjusting its position relative to the footprint).
- Rotate the designator text.
- Check if a mouse point hits a designator via `checkDesignatorHit`.

> **Image placeholder**  
> `![Footprint designator editing](img/pcb/designator-editing.png)`  
> _User dragging a resistor reference text slightly away from the pad so it does not overlap traces._

---

## Unplacing and deleting footprints

- **Unplace** (`Unplace_Footprint_Command`):
  - Removes footprint from board.
  - Puts it back into `m_availableFootprints` of the `PcbDocument`.
  - Rebuilds connectivity afterwards.

- **Delete** (`DeleteFootprintCommand` or `DeletePcbItemsCommand`):
  - Permanently removes footprints, their associated traces (if selected) and possibly graphics.
  - Undo restores them.

Choosing between unplace and delete:

- Use **Unplace** when you want the component to remain in the schematic and be re‑placed later.
- Use **Delete** when you intend to remove it from the PCB entirely (and later sync with schematic).