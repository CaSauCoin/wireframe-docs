# Layers and Views

PCB layers control which drawing plane is active — copper, silkscreen, solder mask, or board outline. This page covers the layer stack, the Layer panel, rendering behavior, and canvas navigation.

---

## Default Layer Stack

| Layer | Color | Contains |
|---|---|---|
| **F.Cu** | Red | Front copper — traces and pads |
| **B.Cu** | Blue | Back copper |
| **F.SilkS** | Yellow | Front silkscreen — labels, outlines, logos |
| **B.SilkS** | Magenta | Back silkscreen |
| **F.Mask** | Purple | Front solder mask openings (around pads) |
| **B.Mask** | Green | Back solder mask openings |
| **F.Paste** | Light red | Front solder paste |
| **B.Paste** | Light blue | Back solder paste |
| **F.Fab** | Grey | Front fabrication layer |
| **B.Fab** | Grey | Back fabrication layer |
| **F.CrtYd** | Light grey | Front courtyard (keep-out area per component) |
| **B.CrtYd** | Light grey | Back courtyard |
| **Edge.Cuts** | Magenta | Board outline — physical board shape |
| **Dwgs.User** | Grey | User annotations and notes |

---

## The Layer Panel

Open **View → PCB Layers** or use the companion panel shown with an active PCB:

### Image — PCB Layers panel

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the Layers panel with F.Cu active, one hidden layer, and several visible copper and technical layers. Keep the eye icons, color swatches, and active highlight readable.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

| Column | Interaction |
|---|---|
| **👁 Eye icon** | Click to **show / hide** the layer |
| **Color swatch** | Click to **change the layer color** |
| **Layer name** | Click to set as the **active routing/drawing layer** |

The active layer has a **highlighted background**.

---

## The Active Layer

The active layer determines where traces and graphics are placed:

- Routing a trace → places it on the **active copper layer**
- Drawing text → places it on the **active layer** (set to F.SilkS for silkscreen labels)
- Change the active layer by **clicking its name** in the Layer panel

!!! tip "Always check your active layer before routing"
    F.Cu (red) and B.Cu (blue) are physically different sides of the board. Routing on the wrong layer will not connect the intended pads.

---

## Hiding and Showing Layers

Click the **eye icon** next to a layer name to toggle its visibility:

- Hidden layers — traces, pads, and graphics are **not drawn on the canvas**
- The data still exists — you can still select and edit hidden-layer items if you know they are there

**Practical examples:**

- Hide **B.Cu** while working on the front side to reduce visual clutter
- Hide **F.SilkS** to inspect trace routing without text overlay
- Re-enable all layers to review the full board

---

## Changing Layer Colors

Click the **color swatch** next to any layer name to open a color picker.

Default colors are chosen for easy visual distinction (red/blue for copper). You can adjust them to your preference — the setting is saved.

---

## How Colors Render on the Canvas

| Element | Color source |
|---|---|
| Trace | The layer the trace is on |
| Pad | Copper layer color |
| Footprint graphics | Layer of each individual graphic (SilkS, Fab, etc.) |
| Silkscreen | F.SilkS or B.SilkS layer color |
| Board outline | Edge.Cuts layer color |
| Copper zone | Layer color rendered semi-transparently |

---

## Canvas Navigation

| Action | Input |
|---|---|
| **Pan** | Hold middle mouse button and drag |
| **Zoom in / out** | Scroll wheel (centered on cursor position) |
| **Fit to board** | Use the configured Fit to Screen shortcut or canvas action |
| **Zoom to selection** | Press ++shift+f++ |
| **100% zoom** | Press ++1++ |

---

## See Also

- [PCB Editor Overview](index.md) — general PCB workspace
- [Routing](routing.md) — the active layer determines which copper layer is routed
- [Fabrication & Export](fabrication-and-export.md) — layer selection for Gerber export
