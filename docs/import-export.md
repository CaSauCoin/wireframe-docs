---
description: Open KiCad and Altium Designer projects in WireFrame, and export a WireFrame project to KiCad, Altium Designer or EasyEDA — with every net checked against WireFrame's own netlist — plus PDF, 1:1 PCB print, fabrication outputs, CAD outlines and STEP.
---

# Import and Export

WireFrame reads the designs you already have and writes designs other tools can open. Every exchange is checked against WireFrame's own netlist, and the notification after an import or an export says what came across and what could not.

## Import

| Menu | Reads |
|---|---|
| **File ▸ Import ▸ KiCad Project (.kicad_pro, .pro)…** | A KiCad project — KiCad 5 legacy `.pro` up to current `.kicad_pro` |
| **File ▸ Import ▸ Altium Project (.PrjPcb, .SchDoc, .PcbDoc, .zip)…** | An Altium Designer project, a single SchDoc or PcbDoc, or a zip of them (SchLib, PcbLib and IntLib inside are read too) |
| **File ▸ Import ▸ CAD Outline (.svg / .dxf)…** | A board outline, cutouts and holes, with a size check first — see [Board Shape and Outline](pcb/board-outline.md) |
| **View ▸ Local Library Manager** | KiCad symbol and footprint libraries; Altium `.SchLib`, `.PcbLib`, `.IntLib`, `.LibPkg` — see [Library Import](libraries/library-converter.md) |

Imports run in the background with progress; the result opens as an ordinary WireFrame project (`.prjxml` with its sheets, board and project library) that you can edit, simulate, check and export.

### KiCad projects

Sheets (hierarchical and flat), the board, the project's own libraries and 3D model paths, net classes and the board's design and fabrication constraints from the project's setup (the fab preset becomes *Custom* with KiCad's values), the stack-up, zones, arcs (kept as arcs), and vias with KiCad's *remove unused layers*. Schematic pages keep their real size, including custom ones.

On the KiCad demo projects WireFrame was measured against, the imported connectivity is identical to `kicad-cli`'s own netlist — 15 of 15 projects. See [Projects & Files](projects.md#import-a-kicad-project) for the step-by-step.

### Altium Designer projects

Schematics (parts, wires, net labels, ports, power ports, sheet symbols), and the board: the layer stack, components with their pads, vias, tracks, arcs, polygons and their poured copper, keep-outs and cut-outs, teardrops, plane split lines (as pour keep-outs), rules and embedded STEP models.

On an RFSoC mezzanine board, WireFrame's netlist of the imported board joins exactly the pads the Altium board joins — 245 nets, 1346 pads, nothing missing, split or merged. The hero board on the WireFrame home page, Sinara's 8-layer **Kasli 2.0** (791 parts), was opened from its Altium files.

!!! note "Eagle"
    Eagle projects are not imported. Open them in KiCad first (KiCad imports Eagle), then import the KiCad project.

## Export to another EDA tool

| Menu | Writes |
|---|---|
| **File ▸ Export ▸ KiCad Project…** | A KiCad project folder: `.kicad_pro`, `.kicad_sch` sheets, `.kicad_pcb`, and the libraries it uses |
| **File ▸ Export ▸ Altium Designer Project…** | `.PrjPcb`, `.SchDoc` sheets, `.SchLib`, `.PcbDoc` (with embedded STEP models) |
| **File ▸ Export ▸ EasyEDA Project (Standard)…** | `<name>_Schematic.json` (one page per sheet instance) and `<name>_PCB.json` |

Pick a folder; the export reads the open project — including edits you have not saved yet — and writes in the background. The notification says where the files went, **whether every net came out as it is in WireFrame**, and what could not be carried.

How the nets are kept: WireFrame computes the connections the written schematic means by the target tool's own rules and compares them pin by pin with its own. Anything that came apart is joined with labels; anything joined that WireFrame keeps apart is reported. Measured with `kicad-cli`'s netlist on boards of 90, 1395 and 3050 pins: no split, no merge.

Things worth knowing:

- **Custom pads** (trapezoids, odd chamfers, polygons) go to Altium the way Altium users draw them: a small anchor pad with the number, net and hole, plus a copper region of the same net with its mask and paste openings. KiCad reads that back as a custom pad.
- **A sheet placed twice** keeps its per-placement designators in Altium.
- **EasyEDA** text on the board carries its stroke-font paths, because EasyEDA draws text from them. KiCad 10 imports the exported EasyEDA board with every placement, pad, via, track and arc in place.

## Documents and manufacturing

| Menu | Writes |
|---|---|
| **File ▸ Export ▸ Export Schematic to PDF…** | The sheets as a printable PDF |
| **File ▸ Export ▸ Print PCB to PDF (1:1)…** | Board layers at true scale, one per page — for checking footprints against real parts on paper |
| **File ▸ Export ▸ Fabrication Outputs (Gerber/Drill/BOM)…** | One `.zip` for the board house: Gerber X2, plated and non-plated Excellon drill, IPC-D-356A netlist, BOM, pick-and-place, job file and README — audited against the board before you send it. See [Fabrication and Export](pcb/fabrication-and-export.md) |
| **Tools ▸ Gerber Viewer…** | Opens any Gerber set to inspect it |
| Board Fit ▸ **Export for the case (STEP)…** | The board and its parts as boxes of their real height, for the mechanical CAD — see [Enclosure Fit](advanced/enclosure-and-assembly.md#export-the-board-for-the-case-maker) |

## See also

- [Projects & Files](projects.md)
- [Library Import and Management](libraries/library-converter.md)
- [File Formats](reference/file-formats.md)
