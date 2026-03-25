# Graphics and Annotations

Beyond components and wires, the schematic editor supports drawing primitives, text, and dimension annotations. Use these to document your design, add visual grouping, or include notes.

---

## Drawing Primitives

Available tools from the schematic toolbar:

| Tool | Shortcut | How to draw | Result |
|---|---|---|---|
| **Line** | — | Click start → drag → release | Line object |
| **Rectangle** | — | Click corner → drag to opposite corner | Rectangle object |
| **Circle** | — | Click center → drag to set radius | Circle object |
| **Arc** | — | Click to define arc endpoints and midpoint | Arc object |
| **Polygon** | — | Click vertices → right-click to close | Polygon object |
| **Harness** | — | Click points → right-click to finish | Special polyline style |
| **Junction** | — | Click to place a dot | Manual junction marker |



### Primitive properties

All graphic objects share:

| Property | Description |
|---|---|
| `id` | Unique identifier per object |
| `layerId` | Drawing layer (for multi-layer use; mainly relevant on PCB) |
| Color | Stroke/outline color |
| Line thickness | Stroke width |
| Fill color | Optional fill (rectangles, circles, polygons) |

<!-- TODO: Replace with actual screenshot
     Capture a schematic area with several drawing primitives:
     - _A dashed **rectangle** used as a section border around a group of components, labeled "Power Section"._
     - _A **line** used as a separator between sections._
     - _A **circle** highlighting a test point._
     - _A **polygon** used as a custom shape or arrow._
     - _Different colors and line widths visible across the primitives._
     Suggested size: 700×450px.
-->
<video controls width="100%">
  <source src="../../img/schematic/drawing-primitives.webm" type="video/webm">
  <source src="../../img/schematic/drawing-primitives.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Text Annotations

Text annotation supports free-form text annotations on the schematic:

| Property | Description |
|---|---|
| Position | World coordinates on the canvas |
| Content | The displayed text string |
| Font size | Adjustable text size |
| Color | Text color |

### Creating text

1. Select the **Text** tool from the toolbar (or press ++t++ if configured).
2. Click at the desired location on the canvas.
3. Type the text into a popup field or the Properties panel.
4. The text object is placed and can be selected, moved, and edited later.

!!! tip "Use text for documentation"
    Add notes explaining circuit behavior, voltage levels, or design constraints directly on the schematic sheet. This keeps important information visible alongside the circuit.

---

## Selection and Editing

Graphics are part of the general selection system:

- **Click** to select a single graphic object.
- **Drag** a selection box to select multiple objects.
- Selected graphics show **highlight outlines** and **resize handles**.

### Editing operations

| Operation | How | Command |
|---|---|---|
| **Move** | Drag selected objects | Undo-supported command |
| **Resize** | Drag corner/edge handles | Resize command (geometry update) |
| **Delete** | ++delete++ or context menu | Undo-supported command |
| **Change color** | Properties panel | Direct property edit |
| **Change layer** | Properties panel or context menu | Layer assignment |

!!! info "Resize handles"
    When a graphic is selected, small squares appear at corners and midpoints. Hovering over them changes the cursor to a resize arrow. Drag to change the object's dimensions.

<!-- TODO: Replace with actual screenshot
     Capture a selected rectangle graphic with editing UI visible:
     - _The rectangle highlighted with a cyan selection outline._
     - _**Resize handles** (small squares) at all four corners and midpoints of each edge._
     - _A right-click **context menu** open next to the rectangle showing options: Delete, Change Color, Change Layer, Send to Back._
     - _The Properties panel on the right showing the rectangle's position, width, height, color, and line width._
     Suggested size: 600×400px.
-->

[//]: # (![Graphics Handles]&#40;../img/schematic/graphics-handles.png&#41;)


---

## Dimensions (Experimental)

WireFrame has preliminary support for Dimension annotation objects — measurement annotations:

| Property | Description |
|---|---|
| Start point | First measurement endpoint |
| End point | Second measurement endpoint |
| Offset | Distance of the dimension line from the measured line |
| Text label | Displayed measurement value or custom annotation |

A dimension draws:

- Two witness lines from the measurement points.
- A dimension line with arrows between them.
- A centered text label showing the distance.

!!! note "Experimental feature"
    Dimension tools may not be fully implemented in the current toolbar. They can be created programmatically or may appear in future releases.

---

## Layers for Graphics

While layers are most meaningful on PCB, schematic graphics also carry a `layerId`:

- Colors derive from layer settings if a the layer system is provided.
- Potential future uses:
    - **Documentation overlays** — separate annotations from the circuit.
    - **Printed vs. non-printed layers** — control what appears in PDF exports.

Currently, the main visible effect is **per-layer coloring** applied by the rendering engine.

---

## See Also

- [Placing Components](placing-components.md) — the main schematic elements.
- [Properties & Attributes](properties-and-attributes.md) — edit graphic properties in the Properties panel.
- [PCB Editor — Layers](../pcb/layers-and-views.md) — layers are more critical on the PCB side.
