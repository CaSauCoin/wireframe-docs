# Footprint Libraries

Footprints define the physical pads, drills, component outline, and optional 3D model used on the PCB. Select the exact manufacturer package and recommended land pattern, not only a similarly named footprint.

## Add a footprint source

1. Open **View → Local Library Manager**.
2. Add the containing folder or KiCad footprint source.
3. Confirm that the source is active and the footprint appears in inventory.
4. Activate a PCB and search its Component Library.

Keep custom footprints and their 3D models in a controlled project or team location so another machine can resolve them.

### Image — Footprint source and active inventory

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture Local Library Manager in v1.5.47 with a KiCad footprint source and several active inventory items visible. Hide private paths.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

<!-- wf:shot id=footprint-source-and-active-inventory
caption: Local Library Manager with the project's KiCad library folders loaded
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
brief_sha256: 18e2a7efa4ab9d2e
-->
<!-- wf:out id=footprint-source-and-active-inventory sha=fb46fca0158a -->
![Local Library Manager with the project's KiCad library folders loaded](../assets/wf/docs/libraries/footprints-library/footprint-source-and-active-inventory.png)
<!-- /wf:out -->

## Review a footprint

Compare the footprint with the exact datasheet land pattern:

- package name and body dimensions;
- pad count, numbering, shape, size, and pitch;
- plated or non-plated drill geometry;
- pin-1 or polarity marker;
- solder-mask and paste behavior;
- courtyard, silkscreen, and fabrication outlines;
- component origin and board-side orientation;
- symbol-pin to footprint-pad mapping.

Print or measure at 1:1 scale when dimensions are safety-critical. A 3D model is useful for review but does not prove that the pads are correct.

## Create or edit a footprint

Open **Tools → PCB Footprint Editor**. Configure the package and pads, review the live result, then save it as a KiCad-compatible `.kicad_mod` in the intended local library.

### Image — PCB Footprint Editor

!!! note "Image capture brief"
    1. **Prepare:** Compare the existing asset with the current release UI and list every changed label or control before recapturing.
    2. **Build the frame:** Capture the current editor with package controls, pad numbering, dimensions, and preview visible. Replace older “Footprint Wizard” media if its window title or controls differ from v1.5.47.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

<!-- wf:shot id=pcb-footprint-editor
caption: Footprint Library Editor with an 8-pin dual-row package
setup:
- open_project
- wait: 1
- menu:
  - Tools
  - PCB Footprint Editor
- wait: 2
- action:
    action: mouse_move_to
    x: 1000
    y: 12
brief_sha256: a8d5ea63c48a9392
-->
<!-- wf:out id=pcb-footprint-editor sha=7f96fb2ac0ce -->
![Footprint Library Editor with an 8-pin dual-row package](../assets/wf/docs/libraries/footprints-library/pcb-footprint-editor.png)
<!-- /wf:out -->

Before release, place the footprint on a test board and inspect pad geometry, courtyard, silkscreen, origin, and orientation.

## Align a 3D model

Select the footprint and open the available 3D-model editing action. Choose the approved STEP or OBJ file, then adjust offset, scale, and rotation until pin 1, body position, and board side match the 2D footprint.

### Short video — Align a footprint model

!!! note "Video production brief"
    1. **Prepare:** Load a public footprint and matching 3D model with a small intentional alignment offset.
    2. **Opening shot (2 s):** Show the offset model over the 2D pads in the alignment editor.
    3. **Action shot (7–10 s):** Correct the offset and rotation, then switch between top and underside views.
    4. **Result shot (3–4 s):** Hold on the aligned model with pin 1 and pad centers visibly consistent.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and hide every private model path.

## Import an Altium footprint library

In **Local Library Manager**, choose the Altium importer and select a supported `.PcbLib`, `.IntLib`, or `.LibPkg` file. Review all converted pads and dimensions; update external 3D model paths when needed.

Eagle footprint import is not exposed in the current release UI and is intentionally omitted.

## Related guidelines

- [Symbol Libraries](symbols-library.md)
- [Library Import and Management](library-converter.md)
- [AI Component Generator](../ai/component-generator.md)
- [Footprints and Placement](../pcb/footprints-and-placement.md)
- [3D Viewer](../advanced/3d-viewer.md)
