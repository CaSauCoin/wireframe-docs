# Fabrication and Export

WireFrame can export:

- Schematic PDFs.
- PCB Gerbers/drill files.
- BOM CSV.
- Gerber viewer previews.
- Optional 3D preview images.

---

## Schematic PDF export

`PdfExporter::exportSchematic` converts a `SchematicDocument` into a vector‑based PDF:

- Draws:
  - Components:
    - Outline, pins, designator and value text.
  - Wires and junctions.
  - Graphics (rectangles, circles, text).
  - Title block and border (from `PageSettings`).
- Applies color → black/grey conversions suitable for printing.

From the UI:

- **File → Export → Schematic PDF…** (when a schematic is active).
- Choose output filename.
- The PDF is written to disk.

> **Image placeholder**  
> `![Schematic PDF](img/fabrication/schematic-pdf.png)`  
> _Screenshot of a generated schematic PDF page opened in an external PDF viewer._

---

## PCB Gerber export

`GerberWriter` generates RS‑274X Gerber data:

- Handles:
  - Outline of traces (`Trace` objects):
    - Converts widths to mm.
    - Ensures minimum width, round‑capped strokes.
  - Pads (`Pad` in `PlacedFootprint`):
    - Circular pads as flashes.
    - Rectangular/oval pads as drawn shapes.
  - Polygons/zones (`ZoneManager` islands):
    - Filled polygons with optional holes.
  - Board outline (Edge.Cuts).

Workflow:

1. From PCB document, open **Fabrication** dialog.
2. Select which layers to export (e.g., F.Cu, B.Cu, F.SilkS, Edge.Cuts).
3. For each layer:
   - `GerberWriter::startFile` writes header and aperture setup.
   - Objects are written with coordinates in mm.
   - `GerberWriter::endFile` finalizes file.
4. Optionally compress outputs into a ZIP for manufacturer.

> **Image placeholder**  
> `![Gerber file list](img/fabrication/gerber-files.png)`  
> _Dialog showing generated `.gbr` and drill files for each relevant layer._

---

## Drill and NC files

While not fully detailed here, a similar process writes drill files from:

- Vias
- Holes
- Plated vs non‑plated holes.

Parameters:

- Diameters and coordinates converted to manufacturer units.

---

## BOM (Bill of Materials)

`PcbBomExporter::generateCSVString` produces a CSV:

Columns:

- `Designator`
- `Value`
- `Footprint`
- `Layer` (Top or Bottom)

Each placed footprint with a non‑empty value contributes one row.

User steps:

1. From PCB context menu or fabrication dialog, choose **Export BOM**.
2. Choose destination CSV file.
3. Open in spreadsheet software for ordering or documentation.

> **Image placeholder**  
> `![BOM in spreadsheet](img/fabrication/bom-spreadsheet.png)`  
> _Generated BOM CSV opened in a spreadsheet with columns for designator, value, footprint and layer._

---

## Gerber viewer

`GerberViewerDialog` is an internal viewer for inspecting Gerber layers:

- Parses a subset of Gerber commands from provided content.
- Displays:
  - Lines/traces with configured thickness.
  - Flashes (e.g., pads) as small circles.
- Provides pan and zoom within the preview canvas.

Use cases:

- Quick verification that exported data is sane.
- No need to launch external CAM software for minor checks.

> **Video placeholder**  
> _Short video where user opens a generated F.Cu Gerber file in the built‑in viewer, pans around and zooms into a BGA area to inspect pad and trace spacing._