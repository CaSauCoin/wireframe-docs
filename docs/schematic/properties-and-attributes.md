# Properties and Attributes

The Properties panel changes with the current selection. Use it to edit sheet metadata, component identity, text display, nets, and graphics without leaving the active document.

## Sheet properties

Click empty canvas to show page-level settings such as paper size, title, company, revision, date, author, sheet number, filename, and border styling.

Complete these fields before PDF release so every exported sheet can be identified independently.

### Image — Sheet properties and title block

!!! note "Image capture brief"
    1. **Prepare:** Compare the existing asset with the current release UI and list every changed label or control before recapturing.
    2. **Build the frame:** Capture the v1.5.47 Properties panel beside the title block it controls. Replace older media if fields, order, or styling have changed.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Component properties

When one component is selected, review:

| Property | Purpose |
|---|---|
| Designator | Unique circuit reference such as `R1` or `U3` |
| Value | Electrical value or part number used by design and BOM |
| Comment | Supporting note when needed |
| Symbol/type | Library identity |
| Footprint | Physical package used by PCB update |

Text controls may also set visibility, position, rotation, and size for the designator, value, and pin labels. Keep them readable without covering wires or pins.

### Short video — Edit and align component text

!!! note "Video production brief"
    1. **Prepare:** Select a component with a readable value and keep its Properties panel open.
    2. **Opening shot (2 s):** Hold on the original value and text position.
    3. **Action shot (7–10 s):** Edit the value, move or align its displayed attribute using the current controls, and pause on the changed result.
    4. **Result shot (3–4 s):** Press Undo and hold on the restored value and position.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and replace media using obsolete property labels.

## Wire and net properties

Selecting a wire or net label exposes its net name and available connectivity information. Use consistent names for rails and signals; renaming a shared net can affect multiple labels and connected items.

Net-class behavior for the PCB is managed in [Design Rules and Net Classes](../pcb/design-rules.md), not through a speculative “future” schematic field.

## Multi-selection and graphics

With multiple items selected, only common supported fields should be changed together. A selected graphic may expose position, size, color, line width, fill, or layer depending on its type.

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
