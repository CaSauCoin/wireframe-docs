# User Interface Overview

This page explains the main parts of the WireFrame UI.

> **Image placeholder**  
> `![UI overview](img/ui-overview/layout-annotated.png)`  
> _Annotated screenshot labeling menu bar, project tree, editor tabs, library panel, properties panel, layer panel, and status/notification area._

---

## Menu bar

Located at the top of the window, providing:

- **File**
  - New Project, Open Project, Open, Save, Save As, Close Project.
  - Project‑level export (PDF, Gerber, BOM, etc. when a PCB is active).
- **Edit**
  - Undo, Redo, Cut, Copy, Paste, Delete.
- **View**
  - Toggle panels (Library, Layers, Properties, etc.).
  - Open 3D viewer.
- **Tools**
  - Schematic symbol editor.
  - PCB footprint wizard.
  - Design rules panel.
  - Gerber viewer.
- **Help**
  - About dialog.
  - Update checks, if enabled.

---

## Docking layout

WireFrame uses ImGui docking:

- You can **drag tabs** to move panels around.
- Layout is persistent via ImGui configuration.
- Common panels:
  - Project Structure.
  - Editor (center).
  - Library.
  - Properties.
  - Layers (PCB only).
  - Logger notification overlay (non‑docked, top‑over‑content).

---

## Project Structure panel

Shows:

- Open projects (`.prjxml`), each as a root node.
- Under each project:
  - **Schematics** (`.schxml`).
  - **PCBs** (`.pcbxml`).

Features:

- Click a schematic or PCB file to open/focus its document.
- Right‑click project/file for context actions:
  - Add new schematic/PCB.
  - Rename.
  - Remove from project (or delete from disk, depending on dialog).
- When opened without a project, you can still recursively browse a folder.

> **Image placeholder**  
> `![Project tree](img/ui-overview/project-tree.png)`  
> _Project panel showing one project with two schematics and one PCB under it._

See [Projects & Files](projects.md) for more.

---

## Editor panel

The central area holds:

- One tab per open **Document**.
- Supported document types:
  - **SchematicDocument** (schematic editor).
  - **PcbDocument** (PCB editor).

Common behavior:

- Tabs show filename or "Untitled".
- Dirty state is tracked; closing a dirty tab prompts to save.
- Right‑click a tab to close or manage.

Within each document:

- A **canvas** (schematic or PCB) that:
  - Shows a grid and page/board outline.
  - Supports pan (middle‑button drag) and zoom (mouse wheel).
- A **floating toolbar** specific to the document type.

---

## Library panel

Context‑sensitive:

- **When a schematic is active**:
  - Shows loaded symbol libraries.
  - Filter bar for symbol names.
  - Double‑click a symbol to start placing it in the schematic.
  - Right‑click to unload symbols or manage symbol libraries.

- **When a PCB is active**:
  - Shows loaded footprint libraries.
  - Filter bar for footprint names.
  - Double‑click to place a footprint or assign to a selected schematic component (depending on workflow).

> **Image placeholder**  
> `![Library panel schematic](img/ui-overview/library-panel-schematic.png)`  
> _Library panel listing symbols with a search box and status bar for loading._

---

## Properties panel

Displays information about the current selection and active document:

- **Schematic**:
  - Component properties (designator, value, footprint, rotation, attributes).
  - Wire/net properties (net name, connections).
  - Page settings (title, revision, sheet number, paper size).

- **PCB**:
  - Footprint properties (value, reference, layer, description).
  - Pad parameters, 3D model alignment.
  - Trace properties (width, net, layer).
  - Board boundary and DRC/DFM settings.

Edits are applied via *command objects* and are undoable.

> **Image placeholder**  
> `![Properties panel schematic](img/ui-overview/properties-schematic.png)`  
> _Properties panel showing a resistor’s designator, value, footprint and text attribute controls._

---

## Toolbars

### Schematic toolbar

A floating toolbar over the schematic canvas (center top) with tools such as:

- Select.
- Wire.
- Net label.
- Text.
- Line, Rectangle, Circle, Arc, Polygon.
- Junction.
- Harness.
- GND, VCC placement.

The current drawing mode is highlighted.

### PCB toolbar

A similar floating toolbar over the PCB canvas, with tools:

- Select.
- Place footprint.
- Route trace.
- Draw via.
- Place mechanical hole.
- Draw line, rect, circle, arc, polygon, text.
- Measure.

---

## Layer panel (PCB only)

Shows a table of PCB layers:

- Visibility eye icon (toggle per layer).
- Color patch (editable).
- Layer name; clicking selects current routing layer.

> **Image placeholder**  
> `![Layer panel](img/ui-overview/layer-panel.png)`  
> _Layer list with eye icons, color squares, and active routing layer highlighted._

---

## Notifications and logger

The **Logger** overlay shows transient messages at the bottom or corner of the editor panel:

- Info, Success, Warning, Error with icons.
- Auto‑fades after a few seconds.
- Used for:
  - File I/O success/fail.
  - Project operations.
  - DFM/DRC results summary.

> **Video placeholder**  
> _Short video showing a user deleting a footprint and a yellow warning toast appearing at the bottom of the editor, then fading out._

---

Next: see [Projects and Files](projects.md) for how projects are structured and linked to documents.