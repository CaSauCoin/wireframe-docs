# Placing Components (Symbols)

Components in the schematic are **symbol instances** from loaded libraries. This page covers loading libraries, finding symbols, placing them, and editing their properties.

---

## Loading Symbol Libraries

Before placing components, load at least one symbol library:

1. Make sure a **Schematic** tab is active (the Library panel shows symbols)
2. In the **Library panel**, click **Load Symbols…**
3. Select one or more KiCad symbol files (`.kicad_sym`)
4. WireFrame parses the library in the background
5. Once complete, symbol names appear in the list

While loading:
- The panel shows a status line: `Loading: Parsing symbols…`
- Any parsing errors are shown in the **Logger** after completion

!!! tip "Quick search"
    Type in the filter box at the top of the Library panel. For example: type `STM32` to filter MCUs, `R_06` for 0603 resistors, `LED` for LEDs.

!!! info "Free KiCad libraries"
    Download from [https://www.kicad.org/libraries/](https://www.kicad.org/libraries/) — WireFrame is fully compatible.

---

## Placing a Symbol

**Workflow:**

1. Type in the filter box to narrow the list (e.g. `R_0603`)
2. **Double-click** the symbol name (e.g. `R_0603`, `MCU_STM32`, `C_0805`)
3. The canvas enters **placement mode**:
    - The symbol preview follows the cursor, semi-transparent
    - Snaps automatically to the grid
4. **Left-click** to place the symbol at the current position
5. The component is placed and you return to **Select** mode

Each placed component has:

| Property | Example | Description |
|---|---|---|
| **Designator** | `R1`, `U3` | Unique identifier — auto-incremented or editable |
| **Value** | `10kΩ`, `100nF` | Electrical value |
| **Footprint** | `R_0603_1608Metric` | Associated PCB footprint package |

---

## Editing Designators and Values

After placing a component, click it to select. The **Properties panel** shows editable fields:

| Field | Description | Note |
|---|---|---|
| **Designator** | Unique identifier (e.g. R1 → R2) | Updating this remaps all connected wires |
| **Value** | Electrical value (e.g. 10kΩ, 100nF) | Appears on the schematic and in the BOM |
| **Comment** | Optional note | Free-form text |
| **Footprint** | PCB package name | Required for PCB conversion |

!!! info "Designator remapping"
    When you change a designator (e.g. `U1` → `U3`), WireFrame automatically updates:
    - The component ID in the internal registry
    - All wires that were connected to the old ID
    - Any selection sets referencing the component

All changes fully support **Undo** (++ctrl+z++).

---

## Rotating Components

With one or more components selected:

- Press ++r++ (or **context menu → Rotate**)
- The component rotates **90° per keypress**
- **Connected wires automatically adjust** to the new pin positions

Rotation is fully undoable and redoable.

---

## Moving Components

1. **Select** one or more components (click or drag a selection box)
2. **Click and drag** to move them on the canvas
3. Connected wires **update in real time** to follow the pin positions

On mouse release:
- A move command is recorded, storing both old and new positions
- **Undo** (++ctrl+z++) restores everything — components and wires — to their previous state

---

## Deleting Components

1. Select the component(s)
2. Press ++delete++ or **context menu → Delete**
3. The component and all its connected wires are removed

**Undo** (++ctrl+z++) restores the deleted components and wires.

---

## Copy, Cut, Paste

| Operation | Shortcut | Behavior |
|---|---|---|
| **Copy** | ++ctrl+c++ | Copies components and wires with relative positions |
| **Cut** | ++ctrl+x++ | Copies then removes the selection |
| **Paste** | ++ctrl+v++ | Places copies at the cursor, assigns new IDs to avoid conflicts |

During paste:
- New component IDs are generated (e.g. R1 → R5) to avoid duplicates
- Wire pin attachments are remapped to the new IDs
- The pasted group follows the cursor until you click to place

---

## See Also

- [Wiring & Nets](wiring-and-nets.md) — connect your placed components
- [Properties & Attributes](properties-and-attributes.md) — edit component and page settings
- [Symbol Libraries](../libraries/symbols-library.md) — manage and create symbol libraries
