# Properties and Attributes

The Properties panel changes with the current selection. Use it to edit sheet metadata, component identity, text display, nets, and graphics without leaving the active document.

## Sheet properties

Click empty canvas to show page-level settings such as paper size, title, company, revision, date, author, sheet number, filename, and border styling.

Complete these fields before PDF release so every exported sheet can be identified independently.

### Image — Sheet properties and title block

!!! note "Image review needed"
    Capture the v1.5.47 Properties panel beside the title block it controls. Replace older media if fields, order, or styling have changed.

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

!!! note "Video review needed"
    Record 15–20 seconds showing a value edited, its display moved or aligned, and Undo restoring the previous state. Replace old media if property labels differ.

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
