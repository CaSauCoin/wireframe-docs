---
description: What is new in WireFrame EDA 2.0.4 back to 2.0.1 — your own agent in command over MCP, datasheets read on every computer, an MCP server for your own agent, Live Checks, push-and-shove routing, the High-Speed Workbench and Power Analyzer, multi-board products, KiCad and Altium round trips, IPC-2581 and ODB++ — and the release status of each version.
---

# Release Notes

<!-- wf:before-release -->

!!! info "Release status"
    The public download is **v1.3.8** (March 2026). Everything below it — v1.5.47 and the 2.0.1 builds after it — is in beta testing for **2.0.1**, the next public release, including the AI Copilot and SPICE simulation.

<!-- wf:after-release -->

!!! info "Release status"
    **WireFrame 2.0.4** is the current release — get it from the [download page](https://wireframe.com.vn/download). The notes below are what changed since **v1.3.8** (March 2026): 2.0.4 back to 2.0.1, then v1.5.47, the beta on the way to 2.0.1.

<!-- wf:end-release -->

## 2.0.4

- **Windows: datasheets are read on every computer.** In 2.0.3 the PDF readers that come with WireFrame could not start on a computer without Microsoft's Visual C++ Redistributable, so an attached datasheet gave no text and no page images. They now carry what they need. Nothing else changes from 2.0.3.

## 2.0.3

### Your agent in command

- **The agent you connect over MCP now does the design work itself.** It opens or starts the project, writes the BOM, the wiring and the sheets, lays out the board and judges whether it is done; Penalty, WireFrame's own agent, takes the jobs it is handed with `ask_penalty`, `run_command` and `build_blocks`. See [Your agent in command](ai/mcp.md#your-agent-in-command).
- **33 tools**, and through `call_tool` the **117** design tools WireFrame's Copilot works with, on a project with its schematic and board open. See [The 33 tools](ai/mcp.md#the-33-tools) and the [MCP tool reference](ai/mcp-tools.md).
- **Reading is free.** Only a call that changes the design or puts Penalty to work counts as an MCP call; reading, checking and analysing do not. WireFrame 2.0.1 and 2.0.2 count every call. See [How calls are counted](ai/mcp.md#how-calls-are-counted).
- **What an agent needs to finish a board, without a shell:** `read_guide` and the guides as MCP resources, `design_status` (ERC, checks, open connections, signal integrity and manufacturability in one answer), long tools that run as jobs so no client times out, checkpoints of the board, and checks of current, heat, noise and manufacturability. See [How your agent learns the way, and knows it is done](ai/mcp.md#how-your-agent-learns-the-way-and-knows-it-is-done).
- **Projects:** `list_projects`, `open_project`, `new_project` and `close_project`. Closing never discards anything: it is refused while a sheet or board has unsaved changes.

### Datasheets and the Copilot

- **PDF datasheets are read on a customer's computer.** The Windows and macOS installers carry the PDF readers WireFrame uses; on Linux the package installs them from the distribution. Before, a datasheet came back empty unless the computer already had them.
- A real board's requirements give a complete BOM; a part's **Import** reads the file before it says it worked, and **Manage** opens the Footprint Editor as well as the Symbol Editor.
- **Account & usage** shows your MCP calls, and every allowance turns amber, then red, as it runs low.

### Boards

- Through-hole wire pads for power leads, rated by the wire their hole takes: 1.7 mm for 16 AWG (22 A), 2.5 mm for 12 AWG (60 A).
- The 3D view orbits over the top and bottom, so a board can be turned over.

## 2.0.2

- **The AI panel holds still while the agent works:** a message near the top edge no longer jumps as new lines arrive.
- **Windows without OpenGL:** instead of closing without a word, WireFrame says the graphics driver is missing and offers to open the [graphics driver guide](installation.md#graphics-driver).
- The ngspice source published with the macOS installer is the version the application carries.

## 2.0.1

### Your own agent, over MCP

- **WireFrame speaks the Model Context Protocol.** Claude, Codex, Cursor or any other MCP client can work on the project open in front of you: fourteen tools of its own, and through `call_tool` the design tools WireFrame's Copilot works with — 95 with a board open. Every answer comes from the application you have open, by the same code that answers the Copilot panel. See [Use WireFrame from your own agent](ai/mcp.md).
- **Nothing runs until you allow it.** The first call puts an **Allow** / **Decline** card in WireFrame's AI panel. Tools that would move a part, lay copper or rewrite a rule work on a copy first, and a high-speed patch or a power fix is applied only once you approve it in WireFrame's own window. See [What waits for your approval](ai/approvals.md).
- **One bridge, `wf-mcp-server`, installed beside WireFrame.** Set it up in a few lines for Claude Desktop, Claude Code, Codex, Cursor or VS Code, or install it in Claude Desktop as an extension (`.mcpb`). It talks to WireFrame over a local socket in your user folder; there is no network port. See [Connect Claude, Codex, Cursor or another agent](ai/mcp-connect.md) and the [MCP tool reference](ai/mcp-tools.md).
- MCP comes with **Pro** (500 tool calls a month) and **Max** (no monthly ceiling) — see [how calls are counted](ai/mcp.md#how-calls-are-counted).

### Checks while you draw

- **Live Checks** (**View ▸ Live Checks**): the parts' electrical contracts, the power tree, the high-speed rules, the DC drop of the rails you set up and the parts' lifecycle run each time an edit settles, and what an edit breaks is said at once — with **Show** to find it, and `/alternative` for a part that is obsolete. See [Live Checks](live-checks.md).

### Signal and power integrity

- **High-Speed Workbench** (**View ▸ High-Speed Workbench**): stack-up with a laminate library and fab tolerance, calculators (impedance with a 2D field solver, delay, reflection, bandwidth, loss, via stub, crosstalk, PDN, track current, emission), simulation of one line, a coupled pair, fly-by and tee nets and Touchstone channels, checks with full evidence, interface profiles (USB 2.0/3.x, PCIe, Ethernet, HDMI, MIPI, LVDS, SATA, DDR3 / DDR4, RGMII, QSPI, SD/eMMC) with cited sources, EMI screening against CISPR 32 and FCC, reviewed fixes, and an HTML/Markdown/JSON report. See [High-Speed Workbench](high-speed/index.md).
- Matching **in time** as well as length, fab-tolerance corners on every impedance, and the controlled-impedance table for the board house.
- The routing readout shows the return path, plane edge and crosstalk of the track being drawn.
- **Power Analyzer** (**View ▸ Power Analyzer (DC IR drop)**): each load's voltage through the real copper, where its drop is lost, current density, via and track currents, rails sharing a ground, the power tree and self-heating — with fixes previewed by a solve and approved by you. See [Power Analyzer](power/power-analyzer.md).
- The Copilot can use both, through the same approval gate: it proposes, a person approves.

### Routing

- **Free routing** (default): a click lays exactly the leg the preview shows; clashes are drawn and reported instead of refused. **Walkaround** remains as a mode.
- **Shove (push tracks)**, a third mode: the tracks of other nets in the way are pushed off by their clearance, and the preview draws them where they will go before you click. The route and every track it pushed are one undo step. See [Route modes and clashes](pcb/routing.md#route-modes-and-clashes).
- **Length and delay made up while routing.** The readout gives the delay routed so far, in picoseconds from the stack-up, and the skew in ps when a pair's or a group's rule is set in time. When the net is short, ++7++ adds the meanders that make up the difference, as part of the route. See [Tune while you route](pcb/length-tuning.md#tune-while-you-route).
- **Route Assist**: auto-route a net or a bus, reroute tracks, reroute only the clashing ones — in the background, one undo step (++ctrl+shift+w++, right-click, toolbar). Double-click finishes a connection.
- Routing keys rebuilt: ++backspace++ steps the whole route back (via included), ++esc++ ends the track and keeps the tool, ++slash++ flips the corner order, ++h++ places a hole, ++ctrl+shift+p++ draws a polygon. Keys never act from text fields.
- A bus finishes together: each follower lands on its own pad.

### Reuse, channels and variants

- **Design blocks** in KiCad 9/10's own format: keep a piece of circuit — with its PCB layout — and place it again. A block made in WireFrame opens in KiCad, and a KiCad block places in WireFrame. See [Design Blocks and Channel Reuse](schematic/design-blocks.md).
- **Tools ▸ Repeat Channel Layout**: lay out one channel of a multi-channel design, and the other channels are placed — and, with **Copy routing**, routed — as it is. See [Repeat a channel's layout](schematic/design-blocks.md#repeat-a-channels-layout).
- **Design variants**: for each build, parts fitted or not, values changed, parts kept out of the BOM or the position files. The fabrication outputs build the variant you pick, and a KiCad 10 or Altium project's variants come in and go back out with it. See [Design Variants](pcb/design-variants.md).

### Boards and views

- **Multi-board products**: one project, a PCB per board drawn from its own root sheet, and one assembly (`.asmxml`) checking every connection pin by pin — with bought boards (Raspberry Pi, BeagleBone, HC-SR04, GY-521, servo, A4988) from their published pinouts. **File ▸ New / Open / Close Assembly**, **View ▸ Assembly View**. See [Multi-Board Products](advanced/multi-board.md).
- **View ▸ Schematic | PCB | 3D**: the three side by side, with cross-probing — a part picked in one is highlighted in the other two. See [Side by Side](advanced/side-by-side-views.md).
- **3D**: physically based rendering, true STEP colours, a product-shot camera, mask colour and surface finish presets, pin-1 and assembly-layer toggles, and picking a part with a click.
- Board Fit sizes a board from the BOM when nothing mechanical fixes it, asks for the copper layers first, and exports the board for the case maker as STEP.

### Import and export

- **File ▸ Import ▸ Altium Project** (PrjPcb, SchDoc, PcbDoc, libraries, zip).
- **File ▸ Export ▸ KiCad Project / Altium Designer Project / EasyEDA Project (Standard)**, each checked net by net against WireFrame's own netlist. See [Import and Export](import-export.md).
- **A round trip gives the same design back.** Export to KiCad or Altium Designer and import it again: every part, pin and net, every pad, track, pour and rule, and the design variants come back. On 36 of the demo projects that ship with KiCad, all 72 round trips — 36 through KiCad, 36 through Altium — are identical. See [A round trip loses nothing](import-export.md#a-round-trip-loses-nothing).
- A KiCad export writes the sheets' bus aliases and real buses, and bus aliases are read in from KiCad sheets.

### KiCad's checks, as KiCad makes them

- **ERC**: KiCad's rules on every sheet of the project, its bus checks included, with fixes you apply — and the Copilot can propose them.
- **DRC**, measured against KiCad's own: solder mask bridges (**E10**) with the board's own mask settings; KiCad's silkscreen checks, on the silk the board really prints; fromTo lengths, starved thermals, copper necks and library checks; a footprint's copper drawings and differential pairs; the severities the board's designer set. A KiCad project's custom rules (`.kicad_dru`) are read as far as they are understood, and the rest are named under **W19**. See [DFM and DRC](pcb/dfm-and-drc.md).

### Fabrication

- **IPC-2581** and **ODB++** beside the Gerber set, with Gerber X2 component files — each read back and checked against the design.
- An **assembly drawing** (PDF) for each side, with the BOM, read back and checked.
- **Panelization**: copies, rails, fiducials, tooling holes, and tabs with mouse bites or V-score, checked copy by copy.
- KiCad's footprint flags come in with each placed footprint, and every fabrication output reads them as KiCad's own outputs do.
- A variant's package is built for that variant — see [Build a variant](pcb/design-variants.md#build-a-variant). The rest of the package is on [Fabrication and Export](pcb/fabrication-and-export.md).

### AI Copilot

- **The AI Copilot runs on WireFrame AI and your plan's AI credit.** WireFrame AI picks the model for each task; the Copilot panel shows **WireFrame AI** and the credit left, with no keys or model ids to set up. See [AI Credit and Your Data](ai/models-and-credits.md).
- The AI knows what you changed in what it made: a change that keeps the checks is your decision and is never reverted; a change that breaks a check is pointed out and asked about.
- **The agent sees what it draws**: a picture of the schematic it drew and of the board it lays out, each block in its own colour. See [How the agent understands a project](ai/how-the-agent-works.md).
- **Board layout by block**: the agent places the board by schematic block, routes with its pairs laid as pairs, and keeps what you changed. See [Placement and Routing Assistant](ai/auto-placer-router.md).
- **`/alternative`**: another part for a part's job — checked, then applied.
- **Datasheets read for the design**: the agent asks a part's datasheet what it says on a topic, page by page, from the PDF WireFrame downloaded (`read_datasheet`).
- **Research and draft a part**: the agent establishes what is known about one exact part number and drafts its symbol and land from the pin table it found; the engine checks the draft, and a person installs it.
- **Placement review (Penalty).** Blocks are placed with findings still open, each marked on the canvas with its number from `/issues`. Only a part the drawing would get wrong holds its block, and a minor part that cannot be drawn yet is left off its block and added later. Critical findings and unconfirmed parts are covered by you with **Place with issues** or `/place now`. See [Placement Review](ai/placement-review.md).
- **Your edits flow back.** Values, footprints, deletions, rewired pins and renamed nets you change on the sheet update the BOM plan and the netlist, and the repair agents are told never to undo them.
- **`/reference`** lifts a part's support circuit from a built KiCad or Altium design — a folder, a project or a GitHub repository — and adds it as a revision, with the source's licence named. See [Reference Designs](ai/reference-designs.md).
- **Numbered findings.** `fix 2`, `explain 3` and `accept 4 because …` act on the numbers `/issues` and the canvas share. A new instruction is no longer mistaken for the answer to a pending question.
- Revisions that name a part by what it does ("the RS-485 transceiver") reach that part.
- Wiring no longer waits for every confirmation: parts awaiting your look are wired, and their land problems are marked rather than parked.

Measured in early October on 20 designs driven end to end through the real Copilot panel (36–106 parts, up to 597 pins: MCUs, an FPGA, SDRAM and eMMC, Ethernet, CAN/RS-485, a BLDC driver, a Raspberry Pi CM4 carrier): a requirement became a checked BOM and netlist in 6–17 minutes, and no design was left with nothing it could draw (two runs cut short by a usage quota were repeated).

### Parts and libraries

- **System-on-module profiles**: a Raspberry Pi CM4 or an NVIDIA Jetson Nano is one part of the carrier designed around it.
- **DigiKey and Mouser, with your own keys** (**Preferences ▸ Part Sources**): datasheets, packages and lifecycle by part number. **Datasheets.com** is a third part source.
- **Fetch from LCSC**, in the online store of the Library panel and of the Library Manager: an exact part number or an LCSC code, fetched on your own machine with its 3D model where it fits.
- When WireFrame cannot download a datasheet itself, your browser can fetch it and hand it back.
- Pin names are held against the datasheet WireFrame downloaded.
- **Part generation**: BGA lands from the ball map; a pinout printed only as a drawing is read off the drawing; a part no package name builds is drawn from its datasheet's package drawing; and KiCad's package lands ship with the app.
- Better binding for RGB LEDs (`LED_RGBA`/`LED_RGBK`), D-sub connectors (`DB9-M-RA` → `DE9_Pins` + `DSUB-9`), RJ45 jacks (never a header of the same pin count), FFC/FPC connectors named by series (Hirose FH12…), JST SH/PH/XH including Qwiic and STEMMA QT, and two-row headers (`Conn_02xNN_Odd_Even`).
- A confirmation survives the part being copied into the project library.

### Account and plans

- **No trial.** A new account is Free — schematic, PCB layout, 3D, SPICE and fabrication output, with no time limit; the AI Copilot, MCP, the High-Speed Workbench and the Power Analyzer come with Pro or Max. See [Account, Plans and Devices](reference/accounts-and-plans.md#plans).
- A feature your plan does not include is not shown at all, rather than shown locked.
- **Account & usage**, in the account menu: your plan, AI credits, the last 30 days and your devices in one window.
- The account menu shows who is signed in and the plan, with **Account & usage**, **Plans & billing**, **Check for updates** and **Sign out of this device**.

### Interface

- A **Light** theme that reads: soft grey, legible colours, redone dialogs; the schematic canvas has Auto / Paper / Dark.
- The **Library Workspace** edits a library in place, with the Copilot in library mode (`/review`, `/check-physics`, `/contract`…). One land-pattern audit, calibrated on KiCad's 15,447 footprints, behind every footprint check.
- The agent is **Penalty** in the chat, and the chat panel is redrawn to look and behave like a professional tool's. A reply can be selected with the mouse and copied, and **Copy** takes the whole turn.
- **Help ▸ Documentation** opens this guide at wireframe.com.vn/docs.
- The sign-in, update-required and unavailable screens are drawn in WireFrame's own look.

### Speed and reliability

- **Auto-save never writes over your file.** It keeps a recovery copy beside it, and opening a file that has a newer one asks **Recover Unsaved Changes?**. Saves are atomic: a save that fails leaves the old file as it was.
- Undo puts back what you saw: a dragged pour's copper, **Properties** edits, **Update PCB**.
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
- Separate tiers for design work and quick questions.

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
