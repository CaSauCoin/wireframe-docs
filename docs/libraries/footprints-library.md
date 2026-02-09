# Footprint Libraries (PCB)

Footprint libraries define physical packages for PCB components.

---

## Loading footprint libraries

From the PCB Library panel:

1. Click **Load Footprints…**.
2. Select one or more KiCad `.kicad_mod` or `.kicad_mod` library files.
3. `LibraryManager::queueLoadFootprintsFromFiles`:
   - Runs parsing via `KicadFootprintParser` in the background.
   - On completion, `loadFootprints` merges parsed footprints.

Available footprint names appear and can be filtered.

---

## Footprint data

`FootprintData` contains:

- Name and library name.
- Description and tags.
- Pads:
  - Number, position (in mm converted to mils).
  - Size.
  - Shape (circle, rect, oval, roundrect, trapezoid, custom).
  - Drill size / shape (for through‑hole).
  - Layer list (e.g. F.Cu, F.Mask, F.Paste).
  - Net name (if imported with netlist).
- Graphics:
  - Lines, circles, arcs, polygons.
  - Reference and value text with sizes and layers.
- 3D model:
  - File path.
  - Offset, scale, rotation.

These are converted into **PlacedFootprint** instances when placed on the PCB.

---

## Footprint generator (PCB Create Lib)

`Pcb_Create_Lib` is a footprint generator/wizard for common footprints:

- Supports:
  - Through‑hole and SMD packages.
  - Single, dual‑row, grid, and quad layouts.
- Settings (`FootprintSettings`):
  - Pin count and layout.
  - Pad size, hole size.
  - Vertical and horizontal pitch.
  - Body margin.

The wizard:

1. Lets you configure pins and pitch.
2. Generates pad positions into `GeneratedPad` list.
3. Shows a preview canvas:
   - Pads on a green background.
   - Grid and axis.
   - Pin numbers and body outline.
4. Exports to KiCad `.kicad_mod` via `saveToKicadMod`.

> **Image placeholder**  
> `![Footprint wizard](img/libraries/footprint-wizard.png)`  
> _Wizard page with controls for pin count, pitch and pad size on the left, and a graphical preview of the generated footprint on the right._

---

## 3D model alignment

3D parameters for footprints are edited via `ModelAlignmentDialog`:

- Select a footprint.
- Open model alignment dialog from PCB properties or context menu.
- Dialog shows:
  - 3D preview of footprint and model (via `Pcb3D_Renderer`).
  - Fields to edit:
    - Model file path.
    - Offset (xyz).
    - Scale (xyz).
    - Rotation (xyz).

`SaveModelToKicadModFile` can write updated 3D model parameters back into the KiCad footprint file.

> **Video placeholder**  
> _Short clip: user adjusts 3D model offset and rotation and sees the model align correctly with the footprint pads in the 3D preview._