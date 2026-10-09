# Fabrication and Export

Once your design is complete and DFM passes cleanly, export manufacturing files to send to your PCB manufacturer — or to document your design.

---

## Export Types Overview

| File type | Format | Purpose |
|---|---|---|
| **Gerber** | RS-274X `.gbr` | PCB fabrication — copper, mask, silk, outline layers |
| **Drill** | Excellon `.drl` | Via and hole positions for CNC drilling |
| **BOM** | CSV `.csv` | Bill of Materials for component ordering |
| **Schematic PDF** | PDF `.pdf` | Printable schematic documentation |
| **Print PCB to PDF (1:1)** | PDF `.pdf` | **Hobbyist** — one 1:1 PDF per layer for toner transfer / UV film |

---

## Schematic PDF Export

Exports your schematic as a vector PDF for printing or sharing.

**Steps:**

1. Open the **Schematic** tab you want to export
2. Select **File → Export → Export Schematic to PDF**
3. Choose a filename and directory
4. Click **Export**

**PDF content:**

| Element | Rendering |
|---|---|
| Components | Symbol outlines, pins, designator and value text |
| Wires and junctions | Black/grey lines and dots |
| Graphics | Rectangles, circles, text annotations |
| Title block | Page border, title, company, revision, date |

> Colors are converted to **black and grey** for print-friendly output.

---

## PCB Gerber Export

Gerber is the **industry-standard format** sent to PCB manufacturers. Each layer produces a separate `.gbr` file.

**Steps:**

1. Open the **PCB** tab
2. Select **File → Export → Fabrication Outputs (Gerber/Drill/BOM)** or **Tools → Fabrication Output**
3. Select the layers to export:

| Layer | Example filename | Purpose |
|---|---|---|
| F.Cu | `MyBoard-F_Cu.gbr` | Front copper |
| B.Cu | `MyBoard-B_Cu.gbr` | Back copper |
| F.SilkS | `MyBoard-F_SilkS.gbr` | Front silkscreen |
| F.Mask | `MyBoard-F_Mask.gbr` | Front solder mask openings |
| B.Mask | `MyBoard-B_Mask.gbr` | Back solder mask openings |
| Edge.Cuts | `MyBoard-Edge_Cuts.gbr` | Board outline for cutting |

4. Choose the **output directory**
5. Click **Export** — one `.gbr` file is generated per selected layer
6. *(Optional)* Compress all files into a **ZIP** to send to the manufacturer

!!! tip "Which files to send?"
    Typically: `F_Cu`, `B_Cu`, `F_SilkS`, `F_Mask`, `B_Mask`, `Edge_Cuts`, and the drill `.drl` file. Always check your manufacturer's specific requirements.

---

## Drill File Export

The drill file contains all **hole locations and diameters** — vias and mechanical holes.

Format: **Excellon NC drill** (text-based coordinate format)

Data included:
- X, Y coordinates for each via and hole
- Drill diameter per tool
- Plated vs. non-plated hole separation

---

## BOM Export (Bill of Materials)

The BOM is a **parts list** used to order components for assembly.

**Steps:**

1. Open the fabrication output workflow.
2. Include the BOM CSV in the coordinated package.
3. Open in Excel, LibreOffice Calc, or Google Sheets

**BOM file columns:**

| Designator | Value | Footprint | Layer |
|---|---|---|---|
| R1 | 10kΩ | R_0603_1608Metric | Top |
| R2 | 330Ω | R_0603_1608Metric | Top |
| C1 | 100nF | C_0805_2012Metric | Top |
| U1 | STM32F103 | LQFP-48 | Top |

!!! info "Before exporting the BOM"
    Only footprints with a **non-empty Value** field are included. Verify that all components have values assigned.

---

## Print PCB to PDF (1:1) — toner transfer and UV film

For makers who produce boards by toner transfer or UV film, WireFrame prints PCB layers at **true 1:1 scale**.

1. Open the PCB.
2. Select **File → Export → Print PCB to PDF (1:1)...**.
3. Tick the layers to print — **each selected layer becomes its own PDF file**.
4. Set the options:
    - **Mirror X (Required for Bottom Layer Toner Transfer)** — tick it for layers that must be printed reversed;
    - **Print in Black & White (Best for UV)**;
    - **Draw Holes with Center Guide (Pad/Via/Mech)** — marks drill centres for hand drilling.
5. Select **Export PDFs...** and choose a folder. The files are written to `<project>_PDFs/<project>_<layer>.pdf`.
6. Print at **100% scale** — never fit-to-page — and measure a known dimension on the printout before transferring.

## Check the Gerbers before ordering

Always look at the exported Gerber and drill files in a Gerber viewer before sending them to a manufacturer — it is the last chance to catch a missing layer, a shifted drill file, or an outline that did not export.

1. Open the export folder in a full Gerber viewer: KiCad **GerbView**, **gerbv**, or the viewer on your manufacturer's order page.
2. Load every copper, mask, silkscreen, outline, and drill file together.
3. Check that:
    - every layer you expect is present and aligned with the others;
    - traces are continuous and pads sit on their copper;
    - drill hits land in the centre of pads and vias;
    - the board outline is closed and matches the mechanical drawing.

!!! warning "Built-in Gerber Viewer is a preview"
    **Tools → Gerber Viewer...** opens a `.gbr` (or `.gtl`, `.gbl`, `.gts`, `.gbs`, `.gto`, `.gbo`, `.gm1`) file in a WireFrame window. In the current release it shows the file name but does **not** yet draw the layer geometry, and it has no zoom or pan. Do not use it to approve a fabrication package — use one of the viewers above.

## Complete Export Workflow

1. Run DFM/DRC and resolve every release-blocking error.
2. Generate the coordinated fabrication package.
3. Review representative Gerber X2 layers and both drill outputs.
4. Check IPC-D-356A, BOM, and the package manifest.
5. Archive only the verified board revision and send that archive to the manufacturer.

### Image — Verified fabrication package

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the fabrication output dialog beside the generated package contents. Show the board revision and filenames, but no private customer path.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Fabrication package contents

The release workflow can generate a coordinated package rather than a set of unrelated exports:

| Output | Purpose |
|---|---|
| **Gerber X2** | Copper, mask, silkscreen, and board geometry with generation metadata |
| **PTH / NPTH drill files** | Separates plated electrical holes from unplated mechanical holes |
| **IPC-D-356A netlist** | Electrical connectivity reference for fabrication test and CAM review |
| **BOM CSV** | Designators, values, footprints, and placement layer |
| **Manifest / README** | WireFrame version, generation time, and package inventory |

!!! warning "Inspect the archive"
    A successful export does not prove manufacturability. Confirm that Edge.Cuts is closed, drill classifications are correct, every expected layer is present, and the package matches the board revision being released.

---

## See Also

- [DFM & DRC](dfm-and-drc.md) — run checks before exporting
- [Layers & Views](layers-and-views.md) — layer selection for export
- [File Formats](../reference/file-formats.md) — detailed file format specifications
