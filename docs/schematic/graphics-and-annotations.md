# Graphics and Annotations

Beyond components and wires, the schematic editor supports drawing primitives and text.

---

## Drawing primitives

Available tools in **DrawingMode**:

- Line
- Rectangle
- Circle
- Arc
- Polygon
- Harness (special polyline style)
- Junction (graphic-only junction dots)

Each primitive is managed by `DrawingManager` and rendered by `DrawingRenderer`.

### Creating primitives

1. Select a tool from the toolbar.
2. Click and drag on the canvas:
   - Line: click start, drag to end, release.
   - Rectangle: click one corner, drag to opposite corner.
   - Circle: click center, drag to radius.
   - Polygon: multiple clicks to add vertices, ESC/right‑click to finish.
3. Resulting graphic is stored as:
   - `GraphicLine`, `GraphicRect`, `GraphicCircle`, `GraphicArc`, `GraphicPolygon`, etc.

Primitives have:

- `id` – unique per drawing object.
- `layerId` – for multi‑layer use (PCB also uses drawing layers).
- Colors and line thickness.
- Optional fill colors (for rectangles, circles, polygons).

---

## Text

`GraphicText` supports annotations:

- Position in world coordinates.
- Content string.
- Font size and color.

Creation:

1. Select **Text** tool.
2. Click at desired location.
3. Type the text into a popup or properties panel (depending on workflow implementation).

---

## Selection & editing

Graphics are part of the general selection system:

- Click to select a single object.
- Drag selection box to select multiple.
- Selected graphics show highlight/handles.

Editing modes:

- **Move**:
  - Drag selected graphic objects.
  - On release, `MoveGraphicsCommand` records before/after positions.

- **Resize**:
  - When hovering near handles (corners/midpoints) a resize cursor appears.
  - Dragging handles changes geometry (e.g. rectangle size).
  - On release, a resize command is recorded.

- **Delete**:
  - Delete key or context menu → `DeleteGraphicsCommand`.

> **Image placeholder**  
> `![Graphics handles](img/schematic/graphics-handles.png)`  
> _Rectangle graphic selected with resize handles visible, and a context menu offering delete and layer change options._

---

## Dimensions (experimental)

There is support for `GraphicDimension` objects:

- Represent measurement annotations (e.g. with arrows and labels).
- Created by a **Dimension** drawing mode when available.

A dimension includes:

- Start and end points.
- Offset for where the dimension line sits relative to the measured line.
- Text label (distance/annotation).

---

## Layers for graphics

While layers are most meaningful on PCB, schematic graphics also carry `layerId`:

- Colors derive from layer settings if a `LayerManager` is provided.
- You can use this in the future for:
  - Documentation overlays.
  - Printed vs non‑printed layers.

Currently, the main visible effect is per‑layer coloring in `DrawingRenderer::render`.