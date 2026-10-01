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

!!! note "Video production brief"
    1. **Prepare:** Open a clean schematic block with space for one short constraint note and grouping rectangle.
    2. **Opening shot (2 s):** Hold on the unannotated block and relevant drawing tools.
    3. **Action shot (8–11 s):** Add the text note, draw the rectangle, then edit one property of each through **Properties**.
    4. **Result shot (3–4 s):** Select each object normally so current handles and selection styling are visible.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and replace older media if tools or handles differ.

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

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture one functional block with a clean grouping shape and a concise constraint note. Keep electrical wires visually distinct from annotations.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Related guidelines

- [Wiring and Nets](wiring-and-nets.md)
- [Properties and Attributes](properties-and-attributes.md)
- [Templates and Title Block](templates.md)
