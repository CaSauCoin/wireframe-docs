---
description: What is new in WireFrame EDA — the High-Speed Workbench, the Power Analyzer, multi-board products, schematic/board/3D side by side, free routing with Route Assist, KiCad/Altium/EasyEDA export, and the AI Copilot — with the release status of each version.
---

# Release Notes

!!! info "Release status"
    The public download is **v1.3.8** (March 2026). Everything below it — v1.5.47 and the development builds after it — is in beta testing for the next public release, including the AI Copilot and SPICE simulation.

## In development — mid to late October 2026

### Signal and power integrity

- **High-Speed Workbench** (**View ▸ High-Speed Workbench**): stack-up with a laminate library and fab tolerance, calculators (impedance with a 2D field solver, delay, reflection, bandwidth, loss, via stub, crosstalk, PDN, track current, emission), simulation of one line, a coupled pair, fly-by and tee nets and Touchstone channels, checks with full evidence, interface profiles (USB 2.0/3.x, PCIe, Ethernet, HDMI, MIPI, LVDS, SATA, DDR3/4, RGMII, QSPI, SD/eMMC) with cited sources, EMI screening against CISPR 32 and FCC, reviewed fixes, and an HTML/Markdown/JSON report. See [High-Speed Workbench](high-speed/index.md).
- Matching **in time** as well as length, fab-tolerance corners on every impedance, and the controlled-impedance table for the board house.
- The routing readout shows the return path, plane edge and crosstalk of the track being drawn.
- **Power Analyzer** (**View ▸ Power Analyzer (DC IR drop)**): each load's voltage through the real copper, where its drop is lost, current density, via and track currents, rails sharing a ground, the power tree and self-heating — with fixes previewed by a solve and approved by you. See [Power Analyzer](power/power-analyzer.md).
- The Copilot can use both, through the same approval gate: it proposes, a person approves.

### Boards and views

- **Multi-board products**: one project, a PCB per board drawn from its own root sheet, and one assembly (`.asmxml`) checking every connection pin by pin — with bought boards (Raspberry Pi, BeagleBone, HC-SR04, GY-521, servo, A4988) from their published pinouts. **File ▸ New / Open / Close Assembly**, **View ▸ Assembly View**. See [Multi-Board Products](advanced/multi-board.md).
- **View ▸ Schematic | PCB | 3D**: the three side by side, with cross-probing — a part picked in one is highlighted in the other two. See [Side by Side](advanced/side-by-side-views.md).
- **3D**: physically based rendering, true STEP colours, a product-shot camera, mask colour and surface finish presets, pin-1 and assembly-layer toggles, and picking a part with a click.
- Board Fit sizes a board from the BOM when nothing mechanical fixes it, asks for the copper layers first, and exports the board for the case maker as STEP.

### Routing

- **Free routing** (default): a click lays exactly the leg the preview shows; clashes are drawn and reported instead of refused. **Walkaround** remains as a mode.
- **Route Assist**: auto-route a net or a bus, reroute tracks, reroute only the clashing ones — in the background, one undo step (++ctrl+shift+w++, right-click, toolbar). Double-click finishes a connection.
- Routing keys rebuilt: ++backspace++ steps the whole route back (via included), ++esc++ ends the track and keeps the tool, ++slash++ flips the corner order, ++h++ places a hole, ++ctrl+shift+p++ draws a polygon. Keys never act from text fields.
- A bus finishes together: each follower lands on its own pad.

### Import and export

- **File ▸ Import ▸ Altium Project** (PrjPcb, SchDoc, PcbDoc, libraries, zip).
- **File ▸ Export ▸ KiCad Project / Altium Designer Project / EasyEDA Project (Standard)**, each checked net by net against WireFrame's own netlist. See [Import and Export](import-export.md).

### AI Copilot

- **Who pays**: your plan's WireFrame credit, or your own key at OpenRouter, DeepSeek or Google AI — each provider with its own key, refused before sending when the choice and the key disagree. See [Models, Credit and Your Data](ai/models-and-credits.md).
- The AI knows what you changed in what it made: a change that keeps the checks is your decision and is never reverted; a change that breaks a check is pointed out and asked about.

### Interface

- A **Light** theme that reads: soft grey, legible colours, redone dialogs; the schematic canvas has Auto / Paper / Dark.
- The **Library Workspace** edits a library in place, with the Copilot in library mode (`/review`, `/check-physics`, `/contract`…). One land-pattern audit, calibrated on KiCad's 15,447 footprints, behind every footprint check.

## In development — early October 2026

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

- AI requests no longer hang on tool servers or half-read answers; a 30-part design that took 16–25 minutes now takes under 10.
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
- Provider presets and separate design and fast model tiers.

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
