# Properties and Attributes

The Properties panel changes with the current selection. Use it to edit sheet metadata, component identity, text display, nets, and graphics without leaving the active document.

## Sheet properties

Click empty canvas to show **Document Settings**. Under **Title Block Info** set the **Width** and **Height** of the title block, **Title**, **Company**, **Revision**, **Drawn By**, **Date**, **Sheet No.**, and **Total**. **Size** shows the current paper size; **Page Setup...** opens the full **Page Settings** dialog with paper size, border, and logo — see [Templates and Title Block](templates.md).

Complete these fields before PDF release so every exported sheet can be identified independently.

### Image — Sheet properties and title block

!!! note "Image capture brief"
    1. **Prepare:** Compare the existing asset with the current release UI and list every changed label or control before recapturing.
    2. **Build the frame:** Capture the v1.5.47 Properties panel beside the title block it controls. Replace older media if fields, order, or styling have changed.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

<!-- wf:shot id=sheet-properties-and-title-block
caption: 'Document Settings beside the KLP4e title block: the Title field holds ${project_name}, and the
  block shows the project name in its place'
setup:
- open_project
- ensure_schematic
- wait: 1
- canvas_fit:
    box:
    - 1150
    - 1450
    - 3000
    - 2110
- wait: 0.5
- action:
    action: mouse_move_to
    x: 1000
    y: 12
brief_sha256: b1fad8de01dc06c6
-->
<!-- wf:out id=sheet-properties-and-title-block sha=e5f7e768b196 -->
![Document Settings beside the KLP4e title block: the Title field holds ${project_name}, and the block shows the project name in its place](../assets/wf/docs/schematic/properties-and-attributes/sheet-properties-and-title-block.png)
<!-- /wf:out -->

## Component properties

When one component is selected, review:

| Tab / section | Property | Purpose |
|---|---|---|
| **General → Info** | **Designator** | Unique circuit reference such as `R1` or `U3` |
| | **Value** | Electrical value or part number used by design and BOM |
| | **Comment** | Supporting note when needed |
| | **Exclude from PCB** | Leaves the part out of **Update Schematic to PCB** |
| **General → Location** | **Position**, **Rotation** | Placement on the sheet |
| **General → Linked Footprint** | Footprint, **Link Footprint & Save to File** | Physical package used by PCB update |
| **3D Model** | — | Preview of the footprint's 3D model |
| **Pins** | **No**, **Name**, **Show Num**, **Show Name** | Pin numbering and which pin texts are shown |

The eye button beside **Designator**, **Value**, and **Comment** shows or hides that text on the sheet.

### Moving and aligning component text

1. Right-click the component and choose **Edit Attributes (Lock Body)**. The body stays put while you work on its texts.
2. Drag the designator, value, or pin texts; rotate a selected text with ++space++ (or ++r++); align several with ++shift+y++ / ++shift+x++.
3. Right-click again and choose **Finish Editing**.

**Sync Attributes to Similar Components** (right-click) copies the position, rotation, size, and visibility of this component's designator, value, and pin texts to every component with the same value (or name) and the same footprint.

### Short video — Edit and align component text

!!! note "Video production brief"
    1. **Prepare:** Select a component with a readable value and keep its Properties panel open.
    2. **Opening shot (2 s):** Hold on the original value and text position.
    3. **Action shot (7–10 s):** Edit the value, move or align its displayed attribute using the current controls, and pause on the changed result.
    4. **Result shot (3–4 s):** Press Undo and hold on the restored value and position.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and replace media using obsolete property labels.

<!-- wf:video id=edit-and-align-component-text
caption: Select R5, change its value from 330 Ω to 470 Ω in Properties, then undo
setup:
- open_project
- ensure_schematic
- wait: 1
- canvas_fit:
    refs:
    - R5
    - D1
    margin: 0.6
- wait: 0.5
- canvas_click: R5
- action:
    action: mouse_move_to
    x: 1000
    y: 12
steps:
- wait: 1.5
- type:
    ref: '**/##Value'
    text: 470 Ω
- wait: 2
- keys:
  - Ctrl
  - Z
- wait: 2
brief_sha256: 7085671e0ff8e91c
-->
<!-- wf:out id=edit-and-align-component-text sha=a59b46582932 -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/schematic/properties-and-attributes/edit-and-align-component-text.mp4" title="Select R5, change its value from 330 Ω to 470 Ω in Properties, then undo"></video>
<!-- /wf:out -->

## Wire and net properties

Selecting a wire or net label exposes its net name and available connectivity information. Use consistent names for rails and signals; renaming a shared net can affect multiple labels and connected items.

Net classes for the PCB are set in [Design Rules and Net Classes](../pcb/design-rules.md).

## Multi-selection and graphics

A selected graphic shows **Graphic Object**: **Content** for text, **Size**, **Color**, and **Thickness**, depending on its type.

After a bulk change, zoom in and inspect each affected item before saving.

## Review checklist

- Sheet revision and title match the release.
- Designators are unique.
- Values include necessary units and tolerances.
- Footprints match the exact package.
- Text is visible and does not obscure connectivity.
- Net names are consistent across the sheet.
- Structural changes are followed by ERC and PCB update review.

## Related guidelines

- [Placing Components](placing-components.md)
- [Wiring and Nets](wiring-and-nets.md)
- [Graphics and Annotations](graphics-and-annotations.md)
- [Templates and Title Block](templates.md)
