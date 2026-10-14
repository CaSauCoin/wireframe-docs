# Symbol Libraries

Symbol libraries provide the logical schematic representation of components. Use approved sources and verify every symbol against the exact manufacturer package before placing it in a release design.

## Add a symbol source

1. Open **View → Local Library Manager**.
2. Select **Add library ▾ → Folder of KiCad libraries...** or **KiCad symbol file (.kicad_sym)...**.
3. Select the new source and confirm its symbols are listed and ticked (shown in the Library panel).
4. Activate a schematic and search for the symbol with **Filter...** in the Library panel.

For project portability, keep required custom libraries with the project or in a controlled team location.

### Image — KiCad symbol source and inventory

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture Local Library Manager in v1.5.47 with a KiCad symbol source selected and part of its active inventory visible. Hide personal filesystem paths.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

<!-- wf:shot id=kicad-symbol-source-and-inventory
caption: Local Library Manager — KiCad symbol sources and the active inventory
setup:
- open_project
- ensure_schematic
- wait: 1
- menu:
  - View
  - Local Library Manager
- wait: 2
- action:
    action: mouse_move_to
    x: 1000
    y: 12
brief_sha256: b68c58cfdbecfa22
-->
<!-- wf:out id=kicad-symbol-source-and-inventory sha=5a290a10d330 -->
![Local Library Manager — KiCad symbol sources and the active inventory](../assets/wf/docs/libraries/symbols-library/kicad-symbol-source-and-inventory.png)
<!-- /wf:out -->

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

Link an approved physical package in one of these places:

- for a placed component: **Properties → General → Linked Footprint → Link Footprint & Save to File**;
- for the library symbol: Library Manager → **Footprint** tab → **Link a footprint file...**, or **Edit properties & pins → Default footprint**;
- in the Library panel preview (**Properties → Footprint** tab): **Manual Load .kicad_mod**, then **Link Footprint & Save to File**.

Confirm package name, pad count, numbering, pitch, polarity marker, and orientation.

Existing placed instances may not inherit a later library change. Review them individually and update the PCB only after the schematic assignments are correct.

### Short video — Assign and verify a footprint

!!! note "Video production brief"
    1. **Prepare:** Select a public symbol with a known matching footprint and readable pin/pad numbering.
    2. **Opening shot (2 s):** Show the symbol and its current empty or incorrect footprint assignment.
    3. **Action shot (7–10 s):** Open the current assignment control, choose the correct package, save or apply, and open its footprint preview.
    4. **Result shot (3–4 s):** Compare at least three readable symbol pins with corresponding footprint pads.
    5. **Deliver:** Export a **15–20 second** 1080p MP4; replace older media whenever labels or controls differ.

<!-- wf:video id=assign-and-verify-a-footprint
caption: R1 (10 kΩ) shows its linked R_0805_2012Metric footprint in Properties; Link Footprint & Save
  to File links the .kicad_mod you pick and saves it with the part
setup:
- open_project
- ensure_schematic
- wait: 2
- canvas_fit:
    refs:
    - R1
    margin: 2.5
- wait: 1
- canvas_click: R1
- wait: 1
- action:
    action: mouse_move_to
    x: 1450
    y: 600
- scroll: -10
- action:
    action: mouse_move_to
    x: 1000
    y: 12
- wait: 1
steps:
- wait: 2.5
- open_file: wireframe:tests/data/mcu_datalogger/wireframe/MCU Datalogger_lib/R_0805_2012Metric.kicad_mod
- hover: '**/{fa:link} Link Footprint & Save to File'
- wait: 1
- click: '**/{fa:link} Link Footprint & Save to File'
- wait: 2
- action:
    action: mouse_move_to
    x: 1450
    y: 600
- scroll: -10
- action:
    action: mouse_move_to
    x: 1470
    y: 705
- wait: 4
brief_sha256: 6f00fe6429c0a032
-->
<!-- wf:out id=assign-and-verify-a-footprint sha=c4f9ec3b55c8 -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/libraries/symbols-library/assign-and-verify-a-footprint.mp4" title="R1 (10 kΩ) shows its linked R_0805_2012Metric footprint in Properties; Link Footprint &amp; Save to File links the .kicad_mod you pick and saves it with the part"></video>
<!-- /wf:out -->

## Import an Altium symbol library

In the Library Manager, select **Add library ▾ → Altium library (SchLib, PcbLib, IntLib)...** and choose a `.SchLib`, `.IntLib`, or `.LibPkg` file. After conversion, review the imported symbol and its footprint relationship before use.

Eagle library import is not exposed in the current release UI and is intentionally omitted.

## Create or generate a missing symbol

Use [Symbol Library Editor](symbol-creator.md) for manual creation or correction. When Component Review identifies a missing part, `/fix` in the AI panel ([Fix or Create a Component](../ai/component-generator.md)) can prepare a symbol and footprint from the datasheet, but both assets still require the same datasheet review.

## Related guidelines

- [Placing Components](../schematic/placing-components.md)
- [Footprint Libraries](footprints-library.md)
- [Library Import and Management](library-converter.md)
- [ERC](../schematic/erc.md)
