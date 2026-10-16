---
description: What is new in WireFrame EDA — the AI Copilot's placement review, edits that flow back into the plan, reference designs, and the release status of each version.
---

# Release Notes

!!! info "Release status"
    The public download is **v1.3.8** (March 2026). Everything below it — v1.5.47 and the development builds after it — is in beta testing for the next public release, including the AI Copilot and SPICE simulation.

## In development — October 2026

Measured on 20 designs driven end to end through the real Copilot panel (36–106 parts, up to 597 pins: MCUs, an FPGA, SDRAM and eMMC, Ethernet, CAN/RS-485, a BLDC driver, a Raspberry Pi CM4 carrier): a requirement became a checked BOM and netlist in 6–17 minutes, and no design was left with nothing it could draw (two runs cut short by the model provider's quota were repeated).

### AI Copilot

- **Placement review (Penalty).** Blocks are placed with findings still open, each marked on the canvas with its number from `/issues`. Only a part the drawing would get wrong holds its block, and a minor part that cannot be drawn yet is left off its block and added later. Critical findings and unconfirmed parts are covered by you with **Place with issues** or `/place now`. See [Placement Review](ai/placement-review.md).
- **Your edits flow back.** Values, footprints, deletions, rewired pins and renamed nets you change on the sheet update the BOM plan and the netlist, and the repair agents are told never to undo them.
- **`/reference`** lifts a part's support circuit from a built KiCad or Altium design — a folder, a project or a GitHub repository — and adds it as a revision, with the source's licence named. See [Reference Designs](ai/reference-designs.md).
- **Numbered findings.** `fix 2`, `explain 3` and `accept 4 because …` act on the numbers `/issues` and the canvas share. A new instruction is no longer mistaken for the answer to a pending question.
- Revisions that name a part by what it does ("the RS-485 transceiver") reach that part.
- Wiring no longer waits for every confirmation: parts awaiting your look are wired, and their land problems are marked rather than parked.

### Libraries

- Better binding for RGB LEDs (`LED_RGBA`/`LED_RGBK`), D-sub connectors (`DB9-M-RA` → `DE9_Pins` + `DSUB-9`), RJ45 jacks (never a header of the same pin count), FFC/FPC connectors named by series (Hirose FH12…), JST SH/PH/XH including Qwiic and STEMMA QT, and two-row headers (`Conn_02xNN_Odd_Even`).
- A confirmation survives the part being copied into the project library.

### Speed and reliability

- The local agyserve bridge no longer hangs on tool servers or half-read answers; a 30-part design that took 16–25 minutes now takes under 10.
- A provider out of quota is not called again every frame.

## v1.5.47 (beta)

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
