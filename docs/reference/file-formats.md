# Supported File Formats

This page separates formats that WireFrame opens directly, formats imported through a specific workflow, and release outputs. Support is determined by the command available in the current application—not by a converter script or an older roadmap.

## WireFrame project files

| Extension | Purpose |
|---|---|
| `.prjxml` | WireFrame project and its document references |
| `.schxml` | WireFrame schematic document |
| `.pcbxml` | WireFrame PCB document |

Keep the project and referenced files together when moving or archiving a design. Their internal schema may evolve, so edit them through WireFrame rather than by hand.

## Project import

Use **File → Import → KiCad Project** for:

| Extension | Source |
|---|---|
| `.kicad_pro` | Current KiCad project |
| `.pro` | Legacy KiCad project |

The importer reads the documents available from the selected KiCad project. Review imported symbols, footprints, nets, layers, and board outline before continuing.

!!! note "Removed legacy guidance"
    Altium `.PrjPcb` and Eagle project import are not exposed by the current File menu. Older claims that these projects could be imported directly have been removed.

## Library sources

Open **View → Local Library Manager** for supported library workflows:

| Format | Use |
|---|---|
| `.kicad_sym` | KiCad symbol library |
| `.kicad_mod` | KiCad footprint |
| `.SchLib` | Altium symbol library import |
| `.PcbLib` | Altium footprint library import |
| `.IntLib` | Altium integrated library import |
| `.LibPkg` | Altium library package import |

Imported library data must be reviewed against the source datasheet before use. Eagle `.lbr`, `.sch`, and `.brd` import are not part of the current library manager.

## PCB outline import

With a PCB active, use **File → Import → CAD Outline (.svg / .dxf)...**.

| Format | Read as |
|---|---|
| `.svg` | Board outline, or graphics on Edge.Cuts / Top Silk / Top Cu; size from the **Scale** field |
| `.dxf` (ASCII) | Board outline only (**Import as BOARD OUTLINE**); size from `$INSUNITS`. `LINE`, `LWPOLYLINE`, `POLYLINE`, `CIRCLE`, `ARC` are read; blocks, splines, and binary DXF are not, and are named in the verdict |

The board shape is saved in the `.pcbxml`. See [Board Shape and Outline](../pcb/board-outline.md).

| Assembly | Extension | Contains |
|---|---|---|
| Multi-board assembly | `.asmxml` | Which board projects make up a product, where each sits in the stack, and how they are wired to each other — see [Enclosure Fit and Multi-Board Products](../advanced/enclosure-and-assembly.md) |

## Fabrication and documentation outputs

Depending on the selected export workflow, WireFrame can produce:

| Format | Purpose |
|---|---|
| Gerber / Gerber X2 | Copper, mask, silkscreen, and board geometry |
| Excellon drill | Plated and non-plated drilling data |
| IPC-D-356A | Electrical connectivity reference |
| CSV | Bill of materials |
| PDF | Schematic documentation or supported plot output |
| Manifest / README | Fabrication-package inventory and generation context |

An exported file is not self-validating. Inspect the package, confirm the saved board revision, and follow the [Fabrication and Export](../pcb/fabrication-and-export.md) checklist.

### Image — Supported import commands

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the v1.5.47 **File → Import** submenu with KiCad Project and CAD Outline visible. Use a second inset of Local Library Manager showing the Altium library importer.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Related guidelines

- [Projects and Files](../projects.md)
- [Library Import and Management](../libraries/library-converter.md)
- [Fabrication and Export](../pcb/fabrication-and-export.md)
