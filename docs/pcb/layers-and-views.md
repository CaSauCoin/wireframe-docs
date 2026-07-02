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

Open via **View → Toggle Layers** or from the sidebar when a PCB is active:

```
Layer Panel
────────────────────────────
👁  🟥  F.Cu        ← Active layer (highlighted background)
👁  🟦  B.Cu
👁  🟡  F.SilkS
    🟣  B.SilkS     ← Hidden (eye icon off)
👁  🟪  F.Mask
👁  🟢  B.Mask
👁  🟫  Edge.Cuts
```

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
| **Fit to board** | Press ++f++ or View → Fit to Screen |
| **Zoom to selection** | Press ++shift+f++ |
| **100% zoom** | Press ++1++ |

---

## See Also

- [PCB Editor Overview](index.md) — general PCB workspace
- [Routing](routing.md) — the active layer determines which copper layer is routed
- [Fabrication & Export](fabrication-and-export.md) — layer selection for Gerber export
