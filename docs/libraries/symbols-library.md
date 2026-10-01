# Symbol Libraries

Symbol libraries provide the logical schematic representation of components. Use approved sources and verify every symbol against the exact manufacturer package before placing it in a release design.

## Add a symbol source

1. Open **View → Local Library Manager**.
2. Add the containing library folder or select the KiCad symbol file.
3. Confirm that the source is active and its symbols appear in the inventory.
4. Activate a schematic and search for the symbol in its Component Library.

For project portability, keep required custom libraries with the project or in a controlled team location.

### Image — KiCad symbol source and inventory

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture Local Library Manager in v1.5.47 with a KiCad symbol source selected and part of its active inventory visible. Hide personal filesystem paths.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

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

!!! note "Video production brief"
    1. **Prepare:** Select a public symbol with a known matching footprint and readable pin/pad numbering.
    2. **Opening shot (2 s):** Show the symbol and its current empty or incorrect footprint assignment.
    3. **Action shot (7–10 s):** Open the current assignment control, choose the correct package, save or apply, and open its footprint preview.
    4. **Result shot (3–4 s):** Compare at least three readable symbol pins with corresponding footprint pads.
    5. **Deliver:** Export a **15–20 second** 1080p MP4; replace older media whenever labels or controls differ.

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
