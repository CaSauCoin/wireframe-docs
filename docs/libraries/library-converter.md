# Library Import and Management

Use **Local Library Manager** to add KiCad libraries, import Altium libraries, inspect active inventory, and remove sources you no longer need. This page replaces the old command-line converter documentation, which described developer tooling rather than the released user interface.

## Open Local Library Manager

Select **View → Local Library Manager**.

The window has two main areas:

- **Add & Import Options** for adding a folder, KiCad symbol files, or an Altium library;
- **Loaded Library Inventory** for inspecting and managing active sources.

### Image — Local Library Manager overview

!!! note "Image needed"
    Capture the complete **Local Library Manager** window. Include both column headers, the three source cards, and part of the active inventory. Use a clean project and hide personal filesystem paths. Suggested size: **1400 × 900 px**.

## Add a KiCad library folder

1. Open **Local Library Manager**.
2. Under **Library Folder**, select **Select Folder**.
3. Choose a directory containing `.kicad_sym`, `.kicad_mod`, or `.pretty` footprint content.
4. Wait for the folder to appear under **Loaded Folders**.
5. Open a schematic or PCB and confirm that the expected items appear in the Component Library.

Use a folder when a library contains multiple related symbol and footprint files. Keep the folder available at the same path after loading it.

## Add KiCad symbol files

1. Under **KiCad Symbol File**, select **Select File(s)**.
2. Choose one or more `.kicad_sym` files.
3. Confirm the files appear in the inventory.
4. Search for a known symbol in the Component Library.

For individual footprints, use the footprint-loading action in the PCB library panel or add the containing folder.

## Import an Altium library

The current importer accepts:

- `.SchLib`;
- `.PcbLib`;
- `.IntLib`;
- `.LibPkg`.

To import:

1. Under **Altium Library Importer**, select **Select Altium File**.
2. Choose the source library.
3. Wait for **Converting Altium** to finish.
4. Find the result under **Imported / Converted Libraries**.
5. Inspect representative symbols, footprints, pad numbering, and 3D model references.

### Short video — Import an Altium library

!!! note "Video needed"
    Record **12–18 seconds** showing **View → Local Library Manager**, selection of a public `.IntLib` or paired library, conversion status, and the new entry under **Imported / Converted Libraries**. Do not expose private paths. 1080p.

!!! warning "Review converted content"
    Library conversion is not manufacturing approval. Check the exact part variant, pin mapping, pad dimensions, footprint orientation, and model paths before using an imported component.

## Inspect or remove a source

Select a loaded folder or imported library in the inventory to review its symbols and footprints. Remove a source only when no active project depends on it.

Removing a source from the manager does not repair placed components whose definitions can no longer be resolved. Archive required project libraries with the project before moving it to another machine.

## What is not currently supported in the UI

The released interface does not expose:

- importing an entire Altium project;
- importing Eagle `.lbr`, `.sch`, or `.brd` files;
- cloning and converting arbitrary GitHub repositories;
- the old `python3 run.py` converter workflow.

Those items have been removed from the user guideline. Do not add them back until they are available and verified in the application UI.

## After any import

- confirm symbols appear in a schematic;
- confirm footprints appear in a PCB;
- link the intended footprint to each symbol;
- check pin and pad counts;
- inspect 3D model paths;
- run ERC, DRC, and DFM on a test project before production use.

## See also

- [Symbol Libraries](symbols-library.md)
- [Footprint Libraries](footprints-library.md)
- [AI Component Generator](../ai/component-generator.md)
- [Projects and Files](../projects.md)
