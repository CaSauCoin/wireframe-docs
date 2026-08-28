# Selection and Editing

Selection behavior is shared by the schematic and PCB editors. Use it to move, copy, rotate, flip, or delete one item or a related group while preserving the ability to undo.

## Select items

| Goal | Action |
|---|---|
| Select one item | Click it |
| Add or remove an item from the selection | Use the platform modifier while clicking |
| Select an area | Drag a selection box on empty canvas |
| Clear selection | Click empty canvas or press ++esc++ |
| Select all visible editable items | ++ctrl+a++ |

Before a group edit, zoom in and confirm every highlighted object. Hidden or locked layers may affect what can be selected on a PCB.

## Move and transform

Drag a selected object or group to move it. Use ++r++ for rotation where available and ++f++ to move a selected PCB footprint between board sides.

After a transform, inspect connected wires or tracks, pad endpoints, text orientation, and board-side layer mapping. Use ++ctrl+z++ immediately if the result is not intended.

## Copy, cut, and paste

| Operation | Shortcut |
|---|---|
| Copy | ++ctrl+c++ |
| Cut | ++ctrl+x++ |
| Paste | ++ctrl+v++ |
| Delete | ++delete++ or ++backspace++ |
| Undo | ++ctrl+z++ |
| Redo | ++ctrl+y++ or ++ctrl+shift+z++ |

Pasted groups preserve their relative geometry and follow the cursor until placed. WireFrame assigns new object identities; review component designators, net attachment, and footprint references after copying between design areas.

### Short video — Copy, place, and undo a group

!!! note "Video review needed"
    Capture a 15–20 second v1.5.47 example: box-select a small group, copy/paste it, place the copy, inspect updated designators, then undo. Replace older media if selection styling or behavior differs.

## Context actions

Right-click the selected object to see actions valid for its type. Typical actions include properties, rotate, flip, change layer or net, unplace, edit 3D model, and delete. The exact list depends on the active editor and object.

## Safe editing checklist

- Confirm the active document and PCB layer before editing.
- Save before a large multi-object operation.
- Review wire/track endpoints after moving connected objects.
- Re-run ERC or DFM/DRC after structural edits.
- Avoid treating Undo history as a substitute for a saved revision.

## Related guidelines

- [Keyboard Shortcuts](shortcuts.md)
- [Schematic Editor](../schematic/index.md)
- [PCB Editor](../pcb/index.md)
