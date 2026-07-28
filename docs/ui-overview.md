# User Interface Overview

This page provides a detailed tour of every part of the WireFrame interface. Understanding the layout helps you work efficiently across schematics and PCBs.

---

## Menu Bar

Located at the **very top** of the window. Every feature is accessible from here.

### File Menu

| Item | Shortcut | Action |
|---|---|---|
| New Project… | — | Create a new `.prjxml` project |
| Open Project… | — | Open an existing project |
| Open… | ++ctrl+o++ | Open a schematic or PCB file |
| New Schematic | ++ctrl+n++ | Create a new schematic document tab |
| New PCB | — | Create a new PCB document tab |
| Save | ++ctrl+s++ | Save the active document |
| Save As… | ++ctrl+shift+s++ | Save with a new filename |
| Close Project | — | Close the active project |
| Export → | — | Sub-menu: PDF, Gerber, BOM export |

### Edit Menu

| Item | Shortcut | Action |
|---|---|---|
| Undo | ++ctrl+z++ | Undo the last action |
| Redo | ++ctrl+y++ | Redo the last undone action |
| Cut | ++ctrl+x++ | Cut selected items to clipboard |
| Copy | ++ctrl+c++ | Copy selected items |
| Paste | ++ctrl+v++ | Paste from clipboard |
| Delete | ++delete++ | Delete selected items |

### View Menu

| Item | Action |
|---|---|
| Toggle Library | Show/hide the Library panel |
| Toggle Layers | Show/hide the Layer panel (PCB) |
| Toggle Properties | Show/hide the Properties panel |
| AI Copilot | Show/hide the AI Copilot chat panel |
| 3D Viewer… | Open the 3D PCB viewer |
| Fit to Screen | Zoom to fit all content in view |

### Tools Menu

| Item | Action |
|---|---|
| Symbol Editor | Open the symbol library editor / creator |
| Footprint Wizard | Open the footprint generator wizard |
| Design Rules | Configure design rule settings (clearance, trace width, etc.) |
| ERC Check | Run Electrical Rules Check on the active schematic |
| DFM Check | Run DFM/DRC checks on the active PCB |
| Simulation | Open the Simulation Controls panel (SPICE) |
| Board Template | Open the PCB Template Builder |
| Gerber Viewer | Open the built-in Gerber file viewer |
| Keymap… | Customize keyboard shortcuts |

---

## Docking Layout

WireFrame uses a **docking layout** — you have full control over panel arrangement:

- **Drag a panel tab** to any edge or corner to reposition it
- **Float a panel** by dragging it outside the docking area — it becomes an independent window
- **Layout is saved automatically** and restored on next launch

Default panel positions:

| Panel | Default position |
|---|---|
| Project Structure | Left |
| Editor (canvas) | Center |
| Library | Right (top) |
| Properties | Right (bottom) |
| Layers *(PCB only)* | Right (middle) |
| AI Copilot | Left (bottom) or docked alongside Project Structure |
| ERC Panel *(Schematic only)* | Bottom or floating |
| Simulation Controls *(Schematic)* | Bottom or floating |
| Waveform Viewer *(after simulation)* | Bottom-center or floating |
| DFM Panel *(PCB only)* | Bottom or floating |
| Logger / Notifications | Bottom-right overlay |

---

## Project Structure Panel

Shows the **project file tree** on the left side:

```
📁 MyBoard.prjxml           ← Project root node
   ├─ 📄 Schematics
   │    ├─ main.schxml      ← Click to open
   │    └─ power.schxml
   └─ 📄 PCBs
        └─ MyBoard.pcbxml   ← Click to open
```

**Interactions:**

| Action | How |
|---|---|
| Open a document | Click a schematic or PCB entry |
| Add a new file | Right-click on the project → Add New… |
| Rename a file | Right-click → Rename |
| Remove from project | Right-click → Remove |
| Delete from disk | Right-click → Delete (requires confirmation) |

!!! info "Standalone mode"
    You can open `.schxml` or `.pcbxml` files without a project. They appear as standalone tabs in the editor but are not shown in the Project Structure tree.

---

## Editor Panel (Canvas)

The **central area** where you design. Each open file is a separate **tab**.

- Tab label = filename (or `Untitled-SCH-1` / `Untitled-PCB-1` for new files)
- A `*` next to the tab name indicates unsaved changes
- Right-click a tab → Close / Close Others / Close All

### Canvas navigation (common to Schematic and PCB)

| Action | Input |
|---|---|
| Pan (move the view) | Hold middle mouse button and drag |
| Zoom in / out | Scroll wheel (zoom centered on cursor) |
| Fit to screen | Press ++f++ |
| Zoom to selection | Press ++shift+f++ |

---

## Library Panel

The Library panel **changes content** based on the active document type:

### When a Schematic is active

Displays **symbol libraries** loaded for the current session.

```
🔍 [filter: "STM32"     ]      ← Type to filter quickly

  STM32F103C8               ← Double-click to place on schematic
  STM32F103RB
  STM32F407VG
  STM32F411CE

  Status: Ready — 150 symbols
```

| Action | How |
|---|---|
| Load a library | Click **Load Symbols…** → select `.kicad_sym` |
| Search | Type a partial name (e.g. `R_06`, `LED`, `STM32`) |
| Place on schematic | **Double-click** the symbol name |
| Other options | Right-click → Unload / Reload / Link Footprint |

### When a PCB is active

Displays **footprint libraries** loaded for the current session.

```
🔍 [filter: "SOT"       ]

  SOT-23
  SOT-23-5
  SOT-223

  Status: Ready — 85 footprints
```

| Action | How |
|---|---|
| Load a library | Click **Load Footprints…** → select `.kicad_mod` |
| Place on PCB | **Double-click** the footprint name |

---

## Properties Panel

Displays and allows editing of **properties** for the currently selected object.

### In the Schematic editor

| Selection | Properties shown |
|---|---|
| **Component** | Designator (R1), Value (10kΩ), Comment, Footprint, Rotation, Position |
| **Net label** | Net name, Position, Font size, Visibility |
| **Wire** | Net name, List of connected pins |
| **Graphic object** | Position, Size, Color, Layer, Line width |
| **Nothing selected** | Page settings (paper size, title, company, revision, date) |

### In the PCB editor

| Selection | Properties shown |
|---|---|
| **Footprint** | Designator, Value, Layer, Position, Rotation, 3D model |
| **Trace** | Net name, Layer, Width, Length |
| **Via** | Net name, Position, Diameter, Drill size |
| **Pad** | Pad number, Net, Shape, Size, Drill, Layers |
| **Zone** | Net name, Layer, Priority, Clearance |
| **Nothing selected** | Board boundary, Design rules summary |

!!! tip "All edits support Undo"
    Every change made in the Properties panel is fully undoable with ++ctrl+z++.

---

## Schematic Toolbar

A floating toolbar at the **top of the schematic canvas**:

```
[▷ Select] [─ Wire] [🏷 Label] [T Text] [╱ Line] [□ Rect] [○ Circle] [⌒ Arc] [⬠ Poly] [• Junction] [⏚ GND] [↑ VCC]
```

| Tool | Shortcut | Function |
|---|---|---|
| **Select** | ++esc++ | Select and move objects |
| **Wire** | ++w++ | Draw wires connecting component pins |
| **Label** | ++l++ | Place a net label (SDA, SCL, GND…) |
| **Text** | — | Place text annotation |
| **Line** | — | Draw a straight line (decorative) |
| **Rectangle** | — | Draw a rectangle |
| **Circle** | — | Draw a circle |
| **Arc** | — | Draw an arc |
| **Polygon** | — | Draw a polygon (click vertices, right-click to finish) |
| **Junction** | — | Place a junction dot manually |
| **GND** | ++g++ | Place a GND power symbol |
| **VCC** | — | Place a VCC power symbol |

The active tool is **highlighted with a cyan background**. Press ++esc++ to return to Select mode.

---

## PCB Toolbar

A floating toolbar at the **top of the PCB canvas**:

```
[▷ Select] [📦 Place] [─ Route] [● Via] [○ Hole] [╱][□][○][⌒][⬠] [T Text] [📏 Measure]
```

| Tool | Shortcut | Function |
|---|---|---|
| **Select** | ++esc++ | Select and move objects |
| **Place Footprint** | — | Place a footprint from the library |
| **Route Trace** | ++x++ | Route copper traces between pads |
| **Draw Via** | ++v++ | Place a via manually |
| **Place Hole** | — | Place a mechanical hole (screw, standoff) |
| **Draw Line/Rect/Circle/Arc/Polygon** | — | Draw graphic shapes on any layer |
| **Draw Text** | — | Place text on silkscreen or fab layers |
| **Measure** | — | Measure distances on the board |

---

## Layer Panel (PCB only)

Visible when a PCB document is active. Lists all board layers:

```
👁  🟥  F.Cu       ← Active layer (highlighted)
👁  🟦  B.Cu
👁  🟡  F.SilkS
    🟣  B.SilkS    ← Hidden (eye icon off)
👁  🟪  F.Mask
👁  🟢  B.Mask
👁  🟫  Edge.Cuts
```

| Column | Interaction |
|---|---|
| **👁 Eye icon** | Click to **show / hide** that layer |
| **Color swatch** | Click to **change the layer color** |
| **Layer name** | Click to set as the **active routing/drawing layer** |

The active layer is **highlighted** with a brighter background.

---

## Logger (Notification Overlay)

Appears in the bottom-right corner of the canvas. Messages appear briefly then fade.

| Type | Color | Example |
|---|---|---|
| Info | Blue | "Project loaded successfully" |
| Success | Green | "File saved: main.schxml" |
| Warning | Yellow | "Library: 2 symbols skipped" |
| Error | Red | "Cannot save: permission denied" |

---

## See Also

- [Getting Started](getting-started.md) — quick-start guide
- [Schematic Editor](schematic/index.md) — schematic design guide
- [PCB Editor](pcb/index.md) — PCB layout guide
- [Keyboard Shortcuts](advanced/shortcuts.md) — full shortcut reference
