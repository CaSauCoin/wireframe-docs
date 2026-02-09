# Placing Components (Symbols)

Components in the schematic are instances of library symbols managed by `ComponentManager` and `LibraryManager`.

---

## Loading symbol libraries

From the **Library panel** when a schematic is active:

1. Click **Load Symbols…**.
2. Choose KiCad‑style symbol library files.
3. Libraries are parsed asynchronously.
4. Available symbol names appear in the list.

While loading:

- The panel may show a spinner or "Loading…" message.
- Errors are listed once parsing completes.

> **Image placeholder**  
> `![Symbol loading](img/schematic/symbol-loading.png)`  
> _Library panel with a "Load Symbols" button and a status line indicating symbol parsing progress._

---

## Placing a symbol from the library

1. In the **Library panel**, type a filter in the search box to narrow symbols.
2. Double‑click a symbol name (e.g. `R_0603`, `MCU_STM32`, etc.).
3. The schematic canvas enters *component placement* mode:
   - The symbol is attached to the mouse cursor.
   - A preview follows the mouse.
4. Left‑click to place the symbol on the grid.

The symbol instance becomes a `PlacedComponent` with:

- Unique `id` (designator like `R1`).
- Type, value, footprint property if present.
- Pin list with positions and names.

---

## Assigning / changing designators and values

Select a component:

- The **Properties panel** shows:
  - **Designator** (component ID).
  - **Value**.
  - **Comment**.
  - **Footprint name** (if defined in symbol properties).
- Editing these fields creates undoable commands:
  - Changing value uses `ChangeComponentValueCommand`.
  - Changing comment uses `ChangeComponentCommentCommand`.
  - Changing designator uses `ChangeComponentIdCommand`:
    - Updates ID in `ComponentManager`.
    - Remaps wire attachments and selection sets.

> **Image placeholder**  
> `![Component properties](img/schematic/component-properties.png)`  
> _Properties panel for a selected resistor showing editable designator, value, comment and footprint fields._

---

## Rotating components

With a component selected:

- Use the rotation shortcut (e.g. `R` by default if configured) or rotate buttons/context menu.
- This triggers `ChangeComponentRotationCommand`:
  - Updates the component’s rotation.
  - Calls `WireManager::updateWireEndpointsForComponent` so connected wires keep touching the pins.

Rotation is undoable and redoable.

---

## Moving components

1. Select one or more components.
2. Click‑and‑drag to move them on the canvas.
3. Connected wires are updated to maintain endpoint attachment.

On mouse release:

- A `MoveCommand` is created capturing:
  - Initial positions of components and wires.
  - Final positions.
- Undo/redo restores previous geometry including wire endpoints.

> **Video placeholder**  
> _Short clip: user drags a group of components; attached wires bend and follow; undo returns all components and wires to original positions._

---

## Deleting components

1. Select components (individually or via selection box).
2. Press Delete, or use context menu → Delete.
3. A `DeleteCommand`:
   - Removes selected components by ID.
   - Removes selected wires.
   - Stores full copies for undo.

Undo restores components and wires to the schematic.

---

## Copy, cut, paste

The schematic supports structured copy/paste:

- **Copy**:
  - Gathers selected components and wires.
  - Copies relative positions and pin/wire attachments into clipboard structures.
- **Paste**:
  - Places copies at the mouse world position.
  - Reassigns component IDs.
  - Reattaches wires using `WireManager::addWire` and mapping from original to new component IDs.

See [Advanced Editing](../advanced/selection-and-editing.md) for more on selection and clipboard behavior.