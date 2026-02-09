# Projects and Files

WireFrame uses a project‑oriented structure to keep schematics, PCBs and libraries organized.

---

## Project files (`.prjxml`)

A project file (`*.prjxml`) stores:

- A list of schematic files.
- A list of PCB files.
- The project library folder name.
- Libraries used by the project.

### Creating a project

1. **File → New Project…**
2. Choose a `.prjxml` path.
3. WireFrame:
   - Creates the project file.
   - Sets project root directory.
   - Sets a default library folder (e.g. `lib/`).

### Opening a project

1. **File → Open Project…**
2. Select a `.prjxml`.
3. The **ProjectStructure panel** parses the XML and lists:
   - `<Schematics>` → schematic file entries.
   - `<PCBs>` → PCB file entries.
   - `<Libraries>` → symbol and footprint library references.

---

## Schematics (`.schxml`)

Each schematic document includes:

- Placed components with IDs and attributes.
- Wires, wire vertices and pin attachments.
- Net labels, text and graphics (lines, rectangles, circles, etc.).
- Page settings (paper size, title block data).

Important aspects:

- The schematic **netlist** is rebuilt from wires and labels using `SchNetlistManager`.
- Components are tied to symbol definitions from loaded libraries (via `LibraryManager`).
- Cross‑document mapping: schematic component IDs can be linked to PCB footprints by ID.

Saving a schematic:

- **File → Save** updates the `.schxml` via `FileManager::saveSchematic`.
- **File → Save As…** writes to a new file and updates the document path.

---

## PCBs (`.pcbxml`)

Each PCB document records:

- Placed footprints and their parameters.
- Traces, vias and mechanical holes.
- Drawing graphics (board outline, dimensions, etc.).
- Netlist data and zone definitions.
- Design rules (net classes, clearances, via sizes).

Saving a PCB:

- **File → Save** calls `FileManager::savePcb` with:
  - Footprints
  - Traces
  - Layers
  - Netlist
  - Drawings
  - Zones
  - Design settings

---

## Linking schematics and PCBs

While the code supports full netlist propagation, from the user’s perspective the typical flow is:

1. Design a schematic and assign footprints (via symbol properties).
2. Use a **Convert to PCB** or similar action from the document manager (when implemented) to:
   - Create a new PCB document.
   - Populate footprints matching schematic IDs.
   - Transfer netlist to the PCB.

Later, changes in the schematic can be re‑applied to PCB by updating netlists and marking nets dirty to recompute ratsnests.

> **Video placeholder**  
> _Short clip showing: user edits a schematic, runs "Update PCB from Schematic", then PCB netnames and ratsnest update accordingly._

---

## Session restoration

The application stores session data (open projects/documents) in a user config file. On startup:

- It restores:
  - Previously open projects.
  - Previously open documents.
- It then re‑populates the ProjectStructure and Editor tabs.

Details are in [Config & Session](reference/config-and-session.md).