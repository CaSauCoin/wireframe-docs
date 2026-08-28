# Selection and Editing

Selection and editing operations are unified across schematic and PCB editors via the selection system. This page covers selection basics, moving, context menus, clipboard, and keyboard operations.

---

## Selection Basics

| Action | Input | Result |
|---|---|---|
| Select one item | Left-click on it | Single selection (previous cleared) |
| Add to selection | ++ctrl++"Click"++ | Add item to existing selection |
| Box select | Left-click + drag on empty area | Selects all items whose bounds intersect the box |
| Clear selection | Click on empty area | Deselects everything |

### Selection storage

Items are tracked by type:

| Selection set | Editor | Stored items |
|---|---|---|
| Components | Schematic | Component IDs |
| Wires | Schematic | Wire IDs |
| Graphics | Both | Graphic object IDs |
| Traces | PCB | Trace IDs |
| Vias | PCB | Via IDs |
| Holes | PCB | Hole IDs |

---

## Moving Selection

1. Select one or more items.
2. Click and drag them on the canvas.
3. Items follow the cursor in real time.
4. On mouse release:

| Editor | Command | What's captured |
|---|---|---|
| Schematic | an undoable move command | Component positions + wire geometries |
| PCB | an undoable move command | Footprint, trace, via, and hole positions |

**Undo** (++ctrl+z++) restores all items to their exact previous positions, including wire/trace shapes.

---

## Context Menus

Right-click on any object to open a context-specific menu:

### Schematic context menus

| Object | Available actions |
|---|---|
| Component | Rotate, Edit Properties, Delete |
| Wire | Delete, Change Net, Start Dragging Segment |
| Graphic | Delete, Change Layer, Change Color |
| Net label | Edit Net Name, Delete |
| Empty canvas | Paste (if clipboard has content) |

### PCB context menus

| Object | Available actions |
|---|---|
| Footprint | Rotate, Flip, Unplace, Edit 3D Model, Delete |
| Trace | Delete, Change Net |
| Via | Delete, Edit Properties |
| Graphic | Delete, Change Layer |
| Empty canvas | Paste |

---

## Copy, Cut, Paste

### Schematic clipboard

| Operation | Shortcut | Handler |
|---|---|---|
| Copy | ++ctrl+c++ | Copy handler — stores selected components and wires |
| Cut | ++ctrl+x++ | Copy + Delete |
| Paste | ++ctrl+v++ | Paste handler → a paste command |

During schematic paste:

- New components are created via the paste operation.
- New wires are added via the wire system.
- Component IDs are **remapped** (R1 → R5) to avoid conflicts.
- Wire pin attachments are **remapped** from old to new IDs.

### PCB clipboard

| Operation | Shortcut | Handler |
|---|---|---|
| Copy | ++ctrl+c++ | Copy handler — stores footprints, traces, vias, holes, graphics |
| Cut | ++ctrl+x++ | Copy + Delete |
| Paste | ++ctrl+v++ | Paste handler — places at mouse position with preserved geometry |

During PCB paste:

- Relative positions between items are preserved.
- New IDs are generated for all pasted items.
- The pasted group follows the mouse until you click to place.

<video controls width="100%">
  <source src="../img/advanced/copy-paste-demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Keyboard Operations

| Operation | Shortcut | Description |
|---|---|---|
| Undo | ++ctrl+z++ | Reverts the last command from the command history system |
| Redo | ++ctrl+y++ or ++ctrl+shift+z++ | Re-applies the last undone command |
| Delete | ++delete++ or ++backspace++ | Deletes the current selection |
| Copy | ++ctrl+c++ | Copy selection to clipboard |
| Cut | ++ctrl+x++ | Cut selection |
| Paste | ++ctrl+v++ | Paste from clipboard |
| Rotate | ++r++ | Rotate selected items |
| Flip | ++f++ | Flip selected items (PCB: front/back) |
| Select All | ++ctrl+a++ | Select all items on the canvas |

All operations go through the **Command pattern** — every mutation pushes to the undo stack, enabling full undo/redo history.

See [Keyboard Shortcuts](shortcuts.md) for the complete key binding reference.

---

## See Also

- [Schematic Editor](../schematic/index.md) — schematic-specific interactions.
- [PCB Editor](../pcb/index.md) — PCB-specific interactions.
- [Keyboard Shortcuts](shortcuts.md) — customize all key bindings.
