# Design Rules and Net Classes

Design rules express the manufacturing limits and electrical routing constraints for the active board. Configure them before routing, then use the same rules for DFM/DRC and release review.

## Open Design Rules Manager

With a PCB active, select **View → Design Rules**. Confirm the board and unit system before changing a value.

### Image — Design Rules Manager

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the v1.5.47 manager with global limits and at least two net classes visible. Use clearly fictional example values and show the active unit.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Set global limits

Enter values that your chosen manufacturer can reliably produce:

| Rule | What it controls |
|---|---|
| Minimum clearance | Allowed gap between copper objects on different nets |
| Minimum trace width | Narrowest permitted routed track |
| Via diameter and drill | Smallest allowed plated via geometry |
| Minimum drill | Smallest mechanical or plated drill |
| Annular ring | Copper remaining around a drilled hole |
| Board-edge clearance | Copper distance from the finished outline |

Do not copy “typical” internet values into a production board. Use the current fabricator's published capability and apply a margin appropriate to the design.

## Create net classes

Use net classes when groups need different widths, clearances, or via sizes. Common examples are low-current signals, supply rails, high-current paths, sensitive analog nets, or controlled routing groups.

1. Add a class with a descriptive name.
2. Set its width, clearance, and via requirements.
3. Assign nets by explicit name or a supported automatic rule.
4. Review the resolved class for each critical net.

A manual assignment takes precedence when both automatic and manual classification apply. Avoid overlapping patterns whose result is difficult to predict.

## Verify the effect

During routing, confirm that a new track uses the expected class width. After changes, rerun DFM/DRC and review violations involving existing geometry; changing a rule does not automatically reroute old tracks.

### Short video — Assign and verify a net class

!!! note "Video production brief"
    1. **Prepare:** Create a fictional supply net and a clearly wider demo power net class with valid rule values.
    2. **Opening shot (2–3 s):** Show the unassigned supply net and both net classes in Design Rules Manager.
    3. **Action shot (10–15 s):** Assign the supply net, apply the rules, route a short connection, and show the route adopting the class width.
    4. **Verification shot (5–7 s):** Run DFM/DRC and hold on the result plus the selected wide route.
    5. **Deliver:** Export a **20–30 second** 1080p MP4 with the active unit and width readable.

## Release checklist

- Rules match the selected manufacturer's current capabilities.
- Critical nets resolve to the intended class.
- Manual overrides are intentional and documented.
- Existing tracks and vias comply after every rule change.
- DFM/DRC has been rerun on the saved release revision.

## Related guidelines

- [Routing](routing.md)
- [Zones and Planes](zones-and-planes.md)
- [DFM and DRC](dfm-and-drc.md)
- [Fabrication and Export](fabrication-and-export.md)
