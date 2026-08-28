# Symbol Libraries

Symbol libraries provide the logical schematic representation of components. Use approved sources and verify every symbol against the exact manufacturer package before placing it in a release design.

## Add a symbol source

1. Open **View → Local Library Manager**.
2. Add the containing library folder or select the KiCad symbol file.
3. Confirm that the source is active and its symbols appear in the inventory.
4. Activate a schematic and search for the symbol in its Component Library.

For project portability, keep required custom libraries with the project or in a controlled team location.

### Image — KiCad symbol source and inventory

!!! note "Image needed"
    Capture Local Library Manager in v1.5.47 with a KiCad symbol source selected and part of its active inventory visible. Hide personal filesystem paths.

## Review a symbol

Before use, compare it with the exact datasheet:

- part and package variant;
- pin count, number, and signal name;
- electrical type used by ERC;
- visible power and ground pins;
- orientation, units, and readability;
- default value and reference prefix;
- footprint assignment and pin-to-pad mapping.

A readable drawing can still be electrically wrong. Treat pin number and footprint-pad mapping as release-critical data.

## Assign a footprint

Use the symbol's available footprint assignment or library action to select an approved physical package. Confirm package name, pad count, numbering, pitch, polarity marker, and orientation.

Existing placed instances may not inherit a later library change. Review them individually and update the PCB only after the schematic assignments are correct.

### Short video — Assign and verify a footprint

!!! note "Video review needed"
    Record 15–20 seconds showing the current footprint-assignment action, selection of a matching package, and verification of pin-to-pad numbering. Replace older media if the UI differs.

## Import an Altium symbol library

In **Local Library Manager**, choose the Altium importer and select a supported `.SchLib`, `.IntLib`, or `.LibPkg` file. After conversion, review the imported symbol and its footprint relationship before use.

Eagle library import is not exposed in the current release UI and is intentionally omitted.

## Create or generate a missing symbol

Use [Symbol Library Editor](symbol-creator.md) for manual creation or correction. When Component Review identifies a missing part, [AI Component Generator](../ai/component-generator.md) can prepare a symbol and footprint from a template or datasheet, but both assets still require the same datasheet review.

## Related guidelines

- [Placing Components](../schematic/placing-components.md)
- [Footprint Libraries](footprints-library.md)
- [Library Import and Management](library-converter.md)
- [ERC](../schematic/erc.md)
