# Selection and Editing

Selection and editing are unified across schematic and PCB via `SelectionManager`.

---

## Selection basics

- **Click**:
  - Left‑click on an object selects it.
  - Clicking empty space clears selection (unless a tool is active).
- **Box selection**:
  - Left‑click and drag on empty area.
  - Draws a semi‑transparent rectangle.
  - On release, selects items whose bounding boxes intersect the rectangle.

Selections are stored as:

- `m_selectedCompIds` – schematic component IDs.
- `m_selectedWireIds` – schematic wire IDs.
- `m_selectedGraphicIds` – graphic object IDs.
- `m_selectedViaIds`, `m_selectedHoleIds`, `m_selectedTraceIds` – PCB objects.
- `m_selectedLibrarySymbol` – currently highlighted symbol in library.

---

## Moving selection

1. Select items.
2. Click and drag them on the canvas.
3. During drag:
   - Positions update in real time for feedback.
4. On release:
   - For schematic: `MoveCommand` stored (components + wires).
   - For PCB: `PcbMoveCommand` stored (footprints, traces, vias and holes).

Undo/redo returns items exactly to their previous positions and wire/trace shapes.

---

## Context menus

Right‑click on:

- Component:
  - Rotate, Flip (schematic), Edit properties, Delete.
- Wire or trace:
  - Delete, Change net, Start dragging segment.
- Graphics:
  - Delete, Change layer, Flip (PCB).
- Footprint:
  - Rotate, Flip, Unplace, Edit 3D model, Delete.

`SelectionManager::renderContextMenu` coordinates these operations and triggers appropriate commands.

---

## Copy, cut, paste (schematic and PCB)

### Schematic

- `handleCopySchematic`:
  - Fills `m_copiedComponents` and `m_copiedWires`.
- `handlePasteSchematic`:
  - Executes `PasteCommand`:
    - Creates new components via `ComponentManager::pasteNewComponent`.
    - Adds new wires via `WireManager::addWire`.
    - Remaps component IDs and pin attachments.

### PCB

- `handlePcbCopy` / `handlePcbPaste`:
  - Copy footprints, traces, vias, holes and graphics into clipboard structures.
  - Paste at the mouse world position with preserved relative geometry.

---

## Keyboard operations

Operations that rely on keyboard shortcuts:

- **Undo / Redo** – uses `CommandHistory`:
  - `executeCommand` pushes a command on the undo stack and clears the redo stack.
- **Delete** – mapped to Delete or Backspace:
  - Calls `SelectionManager::handleDelete`.
- **Copy / Cut / Paste** – map to `Ctrl+C`, `Ctrl+X`, `Ctrl+V` equivalents.
- **Rotate**, **Flip**, **Align** – triggered via mapping in `Key_Map`.

See [Shortcuts](shortcuts.md) for a more detailed overview.

> **Video placeholder**  
> _Short clip: user selects mixed schematic elements (components, wires and graphics), hits Copy, clicks elsewhere, hits Paste and sees a cloned group appear._