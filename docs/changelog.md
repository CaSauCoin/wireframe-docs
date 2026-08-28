# Changelog

All notable changes to WireFrame EDA are documented here. Versions follow [Semantic Versioning](https://semver.org/).

---

## v1.5.47 — Upcoming release (2026-08-28)

This release candidate expands WireFrame from capture-and-layout into an integrated design verification workflow.

### Simulation and verification

- Added the **Simulation Workbench** with transient, AC sweep, DC operating point, and DC sweep analyses.
- Added the included ngspice simulator and optional support for ngspice CLI, Xyce, and LTspice.
- Added **Blocks** selection so users can simulate one circuit section or the complete sheet.
- Added DC, AC, Sine, Pulse, and PWL sources.
- Added model checking, missing-model guidance, and vendor SPICE model import.
- Added signal measurements, A/B measurement windows, waveform CSV export, simulation-log export, and schematic value overlays.
- Added per-block or whole-sheet testbenches with loads, settling windows, assertions, and explicit **Pass / Fail / Not measured** results.
- Added Copilot assistance for running simulations, measuring signals, and explaining failed checks.

### AI Copilot and libraries

- Added project-aware Copilot conversations that retain useful context between sessions.
- Added functional-block recognition, electrical value reading, and clearer design findings.
- Added reviewable pending schematic edits; proposed changes are shown before they are applied.
- Added local PDF datasheet attachment for component and library research.
- Expanded AI symbol and footprint creation with custom geometry, parametric connector/IC templates, previews, validation, and an interactive review step.
- Improved Vietnamese language detection, localized Copilot behavior, and native macOS Vietnamese IME input.
- Added a live progress window during KiCad project import.

### PCB, DFM, and manufacturing

- Improved interactive routing with obstacle avoidance, multi-trace routing, segment editing, alignment, snapping, and automatic cleanup.
- Expanded net classes with automatic rules, advanced width/clearance settings, and manual assignments.
- Added DFM progress reporting and improved clearance, via, and board-edge checks.
- Added Gerber X2 metadata, separated plated/unplated drill outputs, IPC-D-356A electrical netlists, BOM improvements, and fabrication package manifests.
- Added explicit unplated mechanical-pad support and improved annular-ring handling.
- Improved copper-zone updates, cancellation, layer support, and teardrop handling.

### Interface, platform, and 3D

- Added a unified Preferences dialog for hotkeys, simulation defaults/engines, AI, PCB defaults, and 3D materials.
- Added non-blocking notifications and more reliable panel layouts for each open document.
- Added native macOS menu/title-bar integration and safer application shutdown handling.
- Improved 3D board rendering with drilled holes, plated barrels, and configurable themes.
- Improved installers and application packaging across supported platforms.

### Release notes

- The application title bar, About dialog, and generated manufacturing files now show a consistent version number.
- Existing 1.3.x project files remain the baseline for compatibility testing; back up production projects before opening them in a release candidate.

---

## v1.3.7 — 2026-03-15

### Added
- **SPICE Simulation** — full NgSpice integration for Transient, AC, DC Sweep, and Operating Point analyses with an interactive Waveform Viewer (oscilloscope, cursors, delta measurements).
- **AI Copilot** — conversational AI design assistant that generates complete schematics, BOMs, and netlists from text descriptions with SPICE simulation verification.
- **AI Auto-Placer & Auto-Router** — physical component layout clustering and grid-based A* PCB trace routing.
- **AI Component Generator** — datasheet-based automatic symbol and footprint generation for missing components.
- **Electrical Rules Check (ERC)** — schematic validation for floating input pins, unconnected nets, driver contention, and duplicate designators.
- **Symbol Creator** — interactive symbol editor and wizard for designing custom schematic symbols.
- **Library Converter Pipeline** — CLI tool for converting Altium (`.IntLib`, `.SchLib`, `.PcbLib`) and KiCad libraries with fuzzy footprint matching and preview generation.
- **Design Rules & Net Classes** — configurable manufacturing constraints (clearance, trace width, via size) per net group.
- **Footprint Wizard** — built-in generator for common through-hole and SMD footprints with live preview.
- **Model Alignment Dialog** — interactive 3D model positioning for footprints with real-time preview.
- **Gerber Viewer** — built-in viewer for inspecting exported Gerber files without external software.
- **BOM export** — CSV export with Designator, Value, Footprint, and Layer columns.

### Improved
- 3D Viewer rendering performance — mesh caching reduces reload time by ~80%.
- Zone fill algorithm — better Clipper2 integration for complex polygon operations.
- Trace routing — improved 45° path calculation and mitering.
- DFM/DRC — added component overlap check and board-edge proximity check.

### Fixed
- Fixed crash when loading large KiCad symbol libraries (>500 symbols).
- Fixed wire endpoint detachment when moving components with rotated pins.
- Fixed incorrect net names when multiple NetLabels share the same wire cluster.
- Fixed Gerber export missing board outline when Edge.Cuts uses polygon instead of rectangle.

---

## v1.3.6 — 2026-01-20

### Added
- **Keyboard shortcut editor** (Edit → Keymap) — visual key binding configuration.
- **Schematic PDF export** — vector-based PDF with title block and border.
- **Session restoration** — automatically reopens projects and documents from last session.

### Improved
- Library panel search — now supports partial matching and case-insensitive filtering.
- Properties panel — dynamic content switching based on selection type.
- Undo/Redo — improved command history for multi-object move operations.

### Fixed
- Fixed via placement not inheriting the net from the active trace.
- Fixed copy/paste losing wire-to-pin attachments in schematic.
- Fixed layer color picker not saving custom colors.

---

## v1.3.5 — 2025-11-10

### Added
- **3D Viewer** — initial release with STEP and OBJ model support.
- **Copper zones** — zone fill with Clipper2, priority system, and cutouts.
- **DFM/DRC panel** — full check suite (outline, clearance, drill, orphans, missing components).

### Improved
- PCB routing — added collision detection during trace drawing.
- Footprint flipping — front/back toggle with automatic layer remapping.
- File I/O — faster `.pcbxml` save/load for large boards.

### Fixed
- Fixed schematic page settings not saving custom paper sizes.
- Fixed multi-select drag offset incorrect on first move.
- Fixed drawing primitives (circle, arc) not rendering on non-default layers.

---

## v1.3.0 — 2025-08-01

### Added
- **PCB editor** — initial release with footprint placement, trace routing, and via support.
- **KiCad footprint parser** — load `.kicad_mod` files.
- **Multi-document management** — tabbed editor with schematic and PCB documents.
- **Project management** — `.prjxml` project files linking schematics, PCBs, and libraries.

### Improved
- Schematic editor — added harness tool and junction auto-detection.
- Library manager — async loading with background parsing.

---

## v1.2.0 — 2025-04-15

### Added
- **Schematic editor** — component placement, wiring, net labels, power symbols.
- **KiCad symbol parser** — load `.kicad_sym` files.
- **Drawing tools** — line, rectangle, circle, arc, polygon, text.
- **Undo/Redo** — full command history for all schematic operations.
- **Copy/Cut/Paste** — structured clipboard with component ID remapping.

---

## v1.0.0 — 2025-01-01

### Initial Release
- Basic application framework with ImGui, GLFW, and OpenGL.
- Docking layout with configurable panels.
- File open/save infrastructure.
- Empty editor canvas with pan and zoom.
