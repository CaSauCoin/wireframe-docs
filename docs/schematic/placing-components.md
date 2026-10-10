# Placing Components

Place schematic symbols from approved local libraries and assign the exact value and PCB footprint required by the selected physical part.

## Prepare the library

1. Open **View → Local Library Manager**.
2. Add the KiCad symbol file or containing library folder.
3. Confirm the source and symbol in the active inventory.
4. Activate the target schematic and search its Component Library.

If the exact part is missing, import an approved library, create it in Symbol Library Editor, or use the [Fix or Create a Component](../ai/component-generator.md) with full datasheet review.

## Place a symbol

1. In the **Library** panel (**Local Library** tab), type the part family or symbol name in **Filter...**. Tick **Hide Power/Logo** to hide power symbols and logos from the list.
2. Click a symbol to preview it in **Properties** (**Symbol**, **Footprint**, and **3D Model** tabs) before placing it. A warning icon means *No footprint linked*.
3. **Drag** the symbol from the list onto a clear spot of the sheet and release.
4. Rotate with ++space++ (or ++r++ while it is selected).
5. Press ++esc++ to return to selection.

### Short video — Find and place a symbol

!!! note "Video production brief"
    1. **Prepare:** Load one approved public symbol and open an empty, grid-visible schematic area.
    2. **Opening shot (1–2 s):** Show the approved source in **Component Library** and an empty search field.
    3. **Action shot (5–8 s):** Search for the symbol, double-click or drag it into placement mode, move to the canvas, and left-click on a grid point.
    4. **Result shot (2–3 s):** Exit placement mode with ++esc++ and hold on the selected placed symbol.
    5. **Deliver:** Export a **10–15 second** 1080p MP4; replace older media if the library UI differs.

<!-- wf:video id=find-and-place-a-symbol
caption: Filter the Library for AMS1117, drag it onto the sheet, press Esc
setup:
- open_project
- ensure_schematic
- wait: 1
- action:
    action: mouse_move_to
    x: 1000
    y: 12
steps:
- wait: 1
- type:
    ref: //Library/##FilterSym
    text: AMS
- wait: 1.5
- drag_to_canvas:
    from: //Library/{fa:microchip} AMS1117-3.3@1
    to:
    - 1300
    - 540
- wait: 1.5
- keys:
  - Escape
- canvas_click: U3
- wait: 2
brief_sha256: ae328a0a2c365469
-->
<!-- wf:out id=find-and-place-a-symbol sha=4caabf831614 -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/schematic/placing-components/find-and-place-a-symbol.mp4" title="Filter the Library for AMS1117, drag it onto the sheet, press Esc"></video>
<!-- /wf:out -->

## Complete component properties

Select the component and verify:

**Properties → Component Properties** has three tabs:

| Tab | Fields |
|---|---|
| **General** | **Info**: **Designator**, **Value**, **Comment**, **Exclude from PCB**. **Location**: **Position**, **Rotation**. **Linked Footprint** with **Link Footprint & Save to File** |
| **3D Model** | Preview of the linked footprint's 3D model |
| **Pins** | Each pin's **No**, **Name**, position, and **Show Num** / **Show Name** |

Review each one:

| Field | Review |
|---|---|
| Designator | Unique and appropriate prefix |
| Value | Electrical value or exact orderable part number |
| Footprint | Exact package variant and pad count |
| Comment | Useful design or sourcing note, when required |
| Exclude from PCB | Only for parts that are not on this board (test points on a fixture, off-board items) |

The eye button beside a field shows or hides that text on the sheet.

Changing a designator can affect connected references. Review the updated item and run ERC before PCB update.

## Move, rotate, copy, or delete

Drag to move (or nudge with the arrow keys), ++space++ to rotate, ++ctrl+c++ / ++ctrl+v++ to duplicate, and ++delete++ to remove — the wires attached to a deleted component are removed with it. Right-click a component for **Move ▸** (10 px steps), **Rotate (90)**, **Reload from Library**, and **Sync Attributes to Similar Components**. After moving or rotating a connected component, inspect each wire endpoint at the pin tip.

Pasted components receive new identities to avoid duplicates, but you must still review their values, footprint assignments, and connections.

## Pre-ERC checklist

- Exact device and package variant are known.
- Designator is unique.
- Value and rating are correct.
- Footprint pad numbering matches symbol pins.
- Polarity and orientation are clear.
- Every used pin is connected intentionally; unused pins are handled explicitly.

## Related guidelines

- [Symbol Libraries](../libraries/symbols-library.md)
- [Wiring and Nets](wiring-and-nets.md)
- [Properties and Attributes](properties-and-attributes.md)
- [ERC](erc.md)
