# Layers and Views

PCB layers are managed by `LayerManager` and influence visibility, color and type of drawing/rendering.

---

## Layer definitions

`LayerManager` defines:

- `PcbLayer`:
  - `id` (e.g., `PcbLayerId::F_Cu`).
  - `name` (e.g., `F.Cu`, `B.Cu`, `Edge.Cuts`).
  - `type` (`Signal`, `Silk`, `Mask`, `Paste`, `Fab`, `Edge`, `User`).
  - `color`.
  - `isVisible`.

Default layers include:

- **Signal**: F.Cu (0), B.Cu (31)
- **Silk**: F.SilkS, B.SilkS
- **Mask**: F.Mask, B.Mask
- **Paste**: F.Paste, B.Paste
- **Fab**: F.Fab, B.Fab
- **Courtyard**: F.CrtYd, B.CrtYd
- **Edge**: Edge.Cuts
- **User drawing**: Dwgs.User

---

## Layer panel (UI)

Open via View menu or main menu:

- Shows a table:
  - Column for **visibility**:
    - Eye icon toggles `isVisible`.
  - Column for **color**:
    - Color patch opens a color picker.
  - Column for **name**:
    - Clicking a layer selects it as the current PCB routing/drawing layer.

> **Image placeholder**  
> `![Layer panel detail](img/pcb/layer-panel-detail.png)`  
> _Layer panel with 'F.Cu' highlighted as active routing layer, B.Cu visible but not active, several mask/silk layers greyed out._

---

## Layer colors and rendering

Rendering functions (`FootprintRenderer`, `DrawingRenderer`, trace rendering) use layer colors:

- Traces:
  - Drawn in the color of their layer.
- Footprint graphics:
  - Lines, arcs, circles and polygons use per‑graphic `layerId` and color from `LayerManager`.
- Silkscreen:
  - Typically yellow or cyan depending on side.
- Edge.Cuts:
  - Magenta or another distinct color.

Layer visibility:

- Hidden layers:
  - Their traces and graphics are not drawn.
  - However, underlying data still exist and can be operated on via selection/hotkeys (depending on future design decisions).

---

## View controls

Navigation:

- Pan:
  - Middle mouse drag on the PCB canvas.
- Zoom:
  - Mouse wheel, centered on mouse cursor.
- Fit:
  - A "fit to board" or "fit to selection" command can be triggered (e.g., via keyboard).
  - Uses controller functions similar to schematic's `fitAll`/`zoomToSelection`.

> **Video placeholder**  
> _Short video: user toggles visibility of B.Cu and silkscreen, then uses mouse wheel to zoom in on a small portion of the board._