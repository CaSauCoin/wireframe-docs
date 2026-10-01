# Library Import and Management

Use **Local Library Manager** to add KiCad libraries, import Altium libraries, inspect active inventory, and remove sources you no longer need. This page replaces the old command-line converter documentation, which described developer tooling rather than the released user interface.

## Open Local Library Manager

Select **View → Local Library Manager**.

The window has two main areas:

- **Add & Import Options** for adding a folder, KiCad symbol files, or an Altium library;
- **Loaded Library Inventory** for inspecting and managing active sources.

### Image — Local Library Manager overview

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the complete **Local Library Manager** window. Include both column headers, the three source cards, and part of the active inventory. Use a clean project and hide personal filesystem paths. Suggested size: **1400 × 900 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

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

!!! note "Video production brief"
    1. **Prepare:** Place a public `.IntLib` or supported paired library in a neutral demo folder.
    2. **Opening shot (1–2 s):** Start on **View → Local Library Manager** with **Altium Library Importer** visible.
    3. **Action shot (6–9 s):** Select **Select Altium File**, choose the source, show the genuine **Converting Altium** state, and cut only the inactive wait.
    4. **Result shot (3–4 s):** Expand the new entry under **Imported / Converted Libraries** and hold on its symbol/footprint counts.
    5. **Deliver:** Export a **12–18 second** 1080p MP4 with all private paths hidden.

!!! warning "Review converted content"
    Library conversion is not manufacturing approval. Check the exact part variant, pin mapping, pad dimensions, footprint orientation, and model paths before using an imported component.

## Inspect or remove a source

The **Loaded Library Inventory** separates sources into **Loaded Folders**, **Imported / Converted Libraries**, and **Individual Library Files**. Select a source to populate its component list. Use **Select All** or **Deselect All** when reviewing a large source, then select a component to open its CAD preview.

A folder can be expanded with its arrow or by double-clicking it. Hover a folder, file, or converted entry to inspect its full source path. Use the trash action beside an inventory entry only when no active project depends on it.

Removing a source from the manager does not repair placed components whose definitions can no longer be resolved. Archive required project libraries with the project before moving it to another machine.

## Review and edit an imported component

The preview area follows the selected component and provides three tabs:

| Preview tab | Review | Available action |
|---|---|---|
| **Symbol** | Shape, pin numbers, pin names, electrical types, reference prefix, and default footprint | **Edit Symbol Properties & Pins**, **Add Pin**, **Edit Geometry in full Canvas Editor**, **Save**, or **Save As** |
| **Footprint** | Pad numbers, pad geometry, body outline, and linked footprint | **Edit Geometry in full Canvas Editor** or **Link Footprint & Save to File** |
| **3D Model** | Package model, orientation, offset, and scale | **Edit 3D Model & Alignment** |

When editing symbol properties, use **Cancel** to discard the pending form edits. Saving a renamed symbol or linking a footprint can affect how the item is resolved later, so confirm the symbol-to-footprint mapping before closing the manager.

### Image — Inventory selection and CAD preview tabs

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture one imported library selected under **Imported / Converted Libraries**, several components in the selection list, and the **Symbol**, **Footprint**, and **3D Model** tabs in the preview area. Show **Select All**, **Deselect All**, and one edit action without exposing a personal path. Suggested size: **1500 × 950 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

### Short video — Inspect and correct an imported component

!!! note "Video production brief"
    1. **Prepare:** Import a public sample containing a symbol, linked footprint, and 3D model.
    2. **Opening shot (2 s):** Show the collapsed converted-library entry and empty or previous preview.
    3. **Action shot (8–11 s):** Expand the entry, select a component, pause on **Symbol**, **Footprint**, and **3D Model** in order, then open **Edit Symbol Properties & Pins**.
    4. **Result shot (3–4 s):** Select **Cancel** and hold on the unchanged preview to demonstrate that no edit was saved.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 using a visible pointer and no private path.

## Component Library panel context actions

The docked **Component Library** is separate from Local Library Manager. In its **Local Library** tab:

- right-click a converted library and select **Remove Library**;
- right-click a loaded folder and select **Remove Folder**;
- right-click a symbol and select **Remove Symbol**;
- select multiple symbols with ++ctrl++ or ++shift++, then use **Remove Selected** or right-click for **Remove _n_ Selected**;
- drag an approved symbol onto the schematic canvas to place it.

Use the manager for source-level import and detailed preview. Use the docked panel for search, selection, placement, and its limited removal actions.

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
