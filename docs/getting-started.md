# Getting Started

This page walks you through:

1. Launching WireFrame EDA.
2. Understanding the main layout.
3. Creating your first project.
4. Creating the first schematic and PCB files.

> **Image placeholder**  
> `![Initial layout](img/getting-started/initial-layout.png)`  
> _The UI showing Menu bar at the top, project tree on the left, central editor area with docking, and secondary panels on the right._

---

## Launching the application

On Linux, assuming you have built the project:

```bash
./wireframe
```

Internally, the app:

- Initializes a GLFW window and OpenGL context.
- Initializes Dear ImGui and docking.
- Enters the main loop calling `GUIManager::render()` every frame.

If you see a blank dark window, the GUI manager will create the main layout on the next frame.

---

## Activation / sign‑in (if enabled)

If activation is required, an overlay dialog will guide you to:

1. Enter an activation token or log in.
2. Wait while the tool contacts the server.
3. Once activated, the overlay disappears and normal editing is enabled.

> **Image placeholder**  
> `![Activation dialog](img/getting-started/activation-dialog.png)`  
> _Full‑window overlay asking for email/token, with a status indicator for activation requests._

You can change or reset activation data later by removing the user config file (see [Config & Session](reference/config-and-session.md)).

---

## Main layout concepts

The UI uses **ImGui docking**:

- **Menu bar** (top): File, Edit, View, Project, Tools, Help.
- **Project Structure panel**: explores projects, schematics, and PCBs.
- **Editor panel**: central tabbed area where each document opens as a tab.
- **Library panel**: lists symbols or footprints depending on active document.
- **Properties panel**: shows properties of the selected schematic/PCB items.
- Optional panels:
  - Layer panel (PCB).
  - Design rules panel.
  - 3D viewer.
  - Logger / notifications overlay.

You can rearrange panels by dragging tabs and saving the layout via your ImGui configuration.

---

## Creating a new project

1. Open **File → New Project…** from the main menu.
2. Choose a `.prjxml` filename (e.g. `MyBoard.prjxml`).
3. WireFrame creates:
   - A project file describing:
     - Linked schematics.
     - Linked PCBs.
     - Library folder name.
   - A project root folder if needed.
4. The **Project Structure** panel shows the new project as a node.

> **Image placeholder**  
> `![New project dialog](img/getting-started/new-project-dialog.png)`  
> _Dialog for selecting path and name for the new `.prjxml` file._

Project files manage:

- Lists of schematic files.
- Lists of PCB files.
- Library references used by the project.

See [Projects and Files](projects.md) for details.

---

## Creating a new schematic file

1. In the menu: **File → New Schematic**.
2. A new untitled schematic document appears as a tab:
   - Name like `Untitled-SCH-1`.
   - Type: Schematic.
3. The central canvas shows:
   - Schematic grid.
   - Floating schematic toolbar.
   - Empty page outline (A4 by default).

You can save it via **File → Save** or **Save As…** to create a `.schxml`.

> **Image placeholder**  
> `![Empty schematic](img/getting-started/empty-schematic.png)`  
> _Shows an empty sheet with schematic toolbar centered at top, ready for placing components._

---

## Creating a new PCB file

1. In the menu: **File → New PCB**.
2. A new PCB document tab appears:
   - Empty board area with grid.
   - PCB toolbar at the top of the canvas.
   - Default 2‑layer stack (F.Cu / B.Cu) plus silks, mask, etc.

You can later **convert** a schematic to PCB using the Project/Document manager (see [PCB Editor](pcb/index.md)).

> **Image placeholder**  
> `![Empty PCB](img/getting-started/empty-pcb.png)`  
> _Empty board with grid and PCB toolbar, no footprints placed yet._

---

## Opening an existing project or file

### Open project (`.prjxml`)

1. **File → Open Project…**
2. Select a `.prjxml` file.
3. WireFrame loads:
   - Project properties.
   - Registered schematic and PCB paths.
   - Library references.
4. The **Project Structure** panel shows the project tree; clicking a schematic/PCB opens it in the editor.

### Open a single schematic or PCB

1. **File → Open…**
2. Select a `.schxml` or `.pcbxml`.
3. The file is opened as a document tab, even if not part of a project.

---

## Next steps

- Learn the UI layout in more detail in [User Interface Overview](ui-overview.md).
- Start drawing a circuit in [Schematic Editor](schematic/index.md).
- Move to PCB layout in [PCB Editor](pcb/index.md).