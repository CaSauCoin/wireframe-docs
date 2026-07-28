# Changelog

All notable changes to WireFrame EDA are documented here. Versions follow [Semantic Versioning](https://semver.org/).

---

## v1.3.7 — 2026-03-15 (Latest)

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

