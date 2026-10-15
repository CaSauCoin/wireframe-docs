# Release Notes

## v1.5.47

### Simulation and verification

- Simulation Workbench with six tabs: **Setup**, **Blocks**, **Testbench**, **Signals**, **Models**, and **AI**.
- ngspice built in; Xyce, LTspice, and an external ngspice selectable, with configurable executable paths, analysis defaults, and preflight readiness checks.
- Functional-block scope, sources and loads, reusable testbench assertions, signal selection, SPICE model management, A/B cursor measurements, and explicit **Pass / Fail / Not measured** results.
- Simulations are files of their own (`.simxml`): **Simulation → Simulate a Block of This Sheet...** copies a block once, or **New Simulation (.simxml)** starts an empty one. Sheets of the design are no longer simulated.
- **Probe Signal** tool on the toolbar of a simulation.
- AI assistance for simulation setup and result explanation.

### AI Copilot

- Project-aware Copilot sessions with retained design context and project memory (`/memory`, `/remember`, `/forget`).
- Clarifying questions before a design is planned, with suggested answers kept as explicit assumptions.
- Component Review (**AI Planned BOM & Schematic Review**) with BOM, connections, blocks, Board Fit, System, netlist check, simulation, design analysis, and local-pool tabs.
- Part repair and creation through `/fix <refdes> …` with an attached datasheet; the plan is shown before anything is written.
- `/layout` for assisted placement, planes, vias, routing, and stitching on a copy of the board, applied only on request; `/board` and `/topology` for the board shape and multi-board products.
- Provider presets (OpenRouter, agyserve) and separate design and fast model tiers.

### Libraries and import

- **Library Manager** with **My libraries** (KiCad folders and symbol files, converted Altium `.SchLib` / `.PcbLib` / `.IntLib` / `.LibPkg`) and the **Online catalog**.
- **Online Store** tab in the Library panel to install parts with symbol, footprint, and 3D model.
- **Footprint Library Editor** with templates, parametric generation, AI datasheet parsing with evidence review, layer completion, and symbol sync.
- KiCad project import with progress feedback.
- CAD outline import from SVG and ASCII DXF, with a board-size verdict before importing.

### PCB and manufacturing

- Interactive routing with walk-around, per-class violation handling (Allow / Warn / Block), layer switching while routing, and a routing readout.
- Trace context menu: select chain or net, move to layer, width, corners, merge collinear segments, bus spacing, high-speed tools.
- Design Rules Manager with net classes, high-speed pairs and length groups, stackup and impedance calculator, fabrication constraints, and name-based assignment.
- Zone Manager with whole-board pours, GND planes, keepouts, and per-zone settings.
- DFM & DRC with configurable checks, severity changes, and AI explanations.
- Fabrication package as one `.zip`: Gerber X2, plated and non-plated Excellon drill files, IPC-D-356A, BOM, pick-and-place, job file, and README.
- 1:1 PCB-to-PDF printing per layer.

### Interface and platform

- Preferences reorganised into General, Appearance, Workspace, Grid & Snap, Editing, Keyboard Shortcuts, Simulation, Libraries, 3D Viewer, AI Assistant, and Updates.
- Panel docking, layout presets, multi-monitor panels, notifications, and **Help → Report a Bug...** / **Request a Feature...** inside the app.
- Community mode: free local use, sign-in optional.
