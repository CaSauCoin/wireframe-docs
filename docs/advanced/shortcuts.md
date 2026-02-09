# Keyboard Shortcuts and Key Map

WireFrame uses a configurable key map managed by `Key_Map`.

---

## Key Map basics

- `AppAction` enum lists actions such as:
  - File operations (New, Open, Save).
  - Navigation (FitToScreen, Zoom100, ZoomToSelection).
  - Placement (PlaceWire, PlaceNetLabel, PlaceGND, PlaceText, etc.).
  - Editing (Cut, Copy, Paste, Delete, Undo, Redo).
  - Transformations (Rotate, Flip, Move, DragWithWires).
  - Wiring (EndWire, AutoRoute, DeleteLastSegment).
  - Alignment (AlignHorizontal, AlignVertical).

- `KeyBinding`:
  - ImGui key code (e.g., `ImGuiKey_N`).
  - Modifiers: `ctrl`, `shift`, `alt`.

Defaults are loaded by `Key_Map::loadDefaults`. For example:

- New file: `Ctrl + N`.

Other defaults can be inspected or changed through the key map editor.

---

## Key map editor

Accessible from the main menu (e.g., **Edit → Keymap…**):

1. List of actions with:
   - Action name.
   - Current binding.
2. Clicking a binding:
   - Starts recording new binding (using `startRecording`).
   - Next key press (e.g., `Ctrl+R`) becomes the new shortcut.
3. Pressing Escape cancels recording.

Bindings are stored in memory and can be persisted in config in future versions.

> **Image placeholder**  
> `![Keymap editor](img/advanced/keymap-editor.png)`  
> _Table listing actions such as "Place Wire" and "Rotate", with editable shortcut cells._

---

## Recommended core shortcuts (suggested)

While exact bindings can be customized, a typical scheme might be:

- **Global**
  - Ctrl+N – New schematic / PCB.
  - Ctrl+O – Open file.
  - Ctrl+S – Save.
  - Ctrl+Shift+S – Save As.

- **Editing**
  - Ctrl+Z – Undo.
  - Ctrl+Y / Ctrl+Shift+Z – Redo.
  - Ctrl+C – Copy.
  - Ctrl+X – Cut.
  - Ctrl+V – Paste.
  - Delete – Delete selected.

- **Navigation**
  - F – Fit to screen.
  - 1 – Zoom 100%.
  - Shift+F – Zoom to selection.

- **Schematic**
  - W – Place wire.
  - L – Place label.
  - G – Place GND.
  - R – Rotate component.

- **PCB**
  - X – Route trace.
  - V – Place via or change layer during routing.
  - M – Move selection.
  - F – Flip footprint.

You can adapt these in the keymap editor to match your workflow or other EDA tools you are used to.