# Graphics and Annotations

Use schematic graphics and text to explain circuit intent, group related sections, and record design constraints. They support documentation but do not create an electrical connection unless the selected tool is explicitly electrical.

## Choose the correct tool

| Tool | Use it for |
|---|---|
| Line, rectangle, circle, arc, polygon | Visual grouping or explanatory shapes |
| Text | Notes, limits, test points, and design intent |
| Harness | Supported grouped connection notation |
| Junction | Explicit electrical meeting point |

Do not use a graphic line as a wire. If two pins must be electrically connected, use the Wire tool and verify the result with net highlighting or ERC.

## Create and edit an annotation

1. Select the graphic or text tool.
2. Place its points or bounds on the sheet.
3. Press ++esc++ when the shape is complete.
4. Select it and use Properties to set content, color, line width, fill, position, or size when available.
5. Save and inspect the PDF result if the annotation is part of release documentation.

### Short video — Add a circuit note and grouping box

!!! note "Video review needed"
    Record 15–20 seconds in v1.5.47 showing a text note and rectangle added, edited through Properties, then selected as ordinary graphic objects. Replace older media if tools or handles differ.

## Annotation guidelines

- State measurable constraints, not vague comments.
- Keep notes outside symbol pins and wires.
- Use consistent font size and restrained color.
- Include voltage, current, tolerance, or test conditions when relevant.
- Avoid duplicating information that is already controlled by a component property.
- Confirm that release-critical notes remain readable in exported PDF.

## Dimensions

Do not rely on a schematic dimension tool unless it is visible and verified in the release build. Record required distances as clear text or in the relevant PCB/mechanical workflow instead of documenting experimental or programmatic features.

### Image — Documented schematic block

!!! note "Image needed"
    Capture one functional block with a clean grouping shape and a concise constraint note. Keep electrical wires visually distinct from annotations.

## Related guidelines

- [Wiring and Nets](wiring-and-nets.md)
- [Properties and Attributes](properties-and-attributes.md)
- [Templates and Title Block](templates.md)
