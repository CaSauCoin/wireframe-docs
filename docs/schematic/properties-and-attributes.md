# Properties and Text Attributes

This page covers the schematic Properties panel — page settings, component attributes, wire/net properties, and text formatting controls.

---

## Sheet and Page Settings

When **nothing is selected**, the Properties panel shows page-level settings for the active `SchematicDocument`:

| Field | Description | Example |
|---|---|---|
| Paper size | A4, A3, A2, or Custom dimensions | A4 |
| Title | Design title shown in the title block | "Power Supply Rev B" |
| Company | Company or author name | "WireFrame Labs" |
| Revision | Revision identifier | "1.2" |
| Date | Design date | "2026-03-23" |
| Drawn by | Author name | "John Doe" |
| Sheet number | Current sheet number / total sheets | "1 / 3" |
| Filename | Document filename | "power.schxml" |
| Border color | Color of the page border and title block | Cyan / White |

These fields are editable directly in the Properties panel. Changes are reflected immediately on the schematic canvas (title block and page border).

![Page Properties](../img/schematic/page-properties.png)


---

## Component Attributes

When a **single component** is selected, the Properties panel shows its logical fields and text attributes:

### Logical fields

| Field | Command | Description |
|---|---|---|
| **Designator** (`id`) | an undoable command | Unique component ID (e.g., R1, U3) |
| **Value** | an undoable command | Electrical value (e.g., 10kΩ) |
| **Comment** | an undoable command | Free-text notes |
| **Type** | Read-only | Symbol type from library |
| **Footprint** | Direct edit | PCB footprint name |

### Text attributes

Each component carries visual text attributes that control how text appears on the canvas:

| Attribute | Properties | Description |
|---|---|---|
| `designatorAttribute` | position, rotation, fontSize, isVisible | Controls the "R1" text display |
| `valueAttribute` | position, rotation, fontSize, isVisible | Controls the "10kΩ" text display |
| Pin name attributes | per-pin text rendering | Pin name labels on each pin |
| Pin number attributes | per-pin text rendering | Pin number labels on each pin |

Each text attribute stores:

- `content` — the displayed string.
- `relativePosition` — offset from the component origin.
- `rotation` — angle in degrees.
- `fontSize` — text size.
- `isVisible` — whether the text is drawn.

Editing these uses an undoable command (for content/position/size) and an undoable command (for rotation).

<video controls width="100%">
  <source src="../img/schematic/component-attributes.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

## Aligning Attributes

For designs with many components, attribute alignment keeps the schematic clean:

- The selection system tracks attribute references for selected text attributes.
- Alignment functions arrange text uniformly:

| Alignment | Description |
|---|---|
| **Align horizontally** | All selected attribute texts aligned to the same Y coordinate |
| **Align vertically** | All selected attribute texts aligned to the same X coordinate |

From the UI:

- Use context menu commands like **"Align Text Horizontally"** / **"Align Text Vertically"**.
- Or use keyboard shortcuts if configured (see [Shortcuts](../advanced/shortcuts.md)).


![Aligned Attributes](../img/schematic/aligned-attributes.png)


---

## Wire and Net Properties

When a **wire or net label** is selected, the Properties panel shows:

| Field | Editable | Description |
|---|---|---|
| Net name | Yes | The net name for this wire/label (an undoable command) |
| Connected pins | Read-only | List of component pins on this net |
| Net classification | Future | Net class assignment for PCB design rules |

Renaming a net label updates:

- The component **value/text** for `NetLabel` components.
- The underlying **net name** in the schematic netlist.
- All other labels and wires on the same net are updated automatically.

---

## Selection-Dependent Content

The Properties panel dynamically switches its content based on what is selected:

| Selection state | Panel content |
|---|---|
| **No selection** | Page/sheet settings (paper size, title block) |
| **Single component** | Component fields + text attributes |
| **Multiple components** | Multi-edit fields (where applicable) or disabled fields |
| **Net label** | Net name editing, position |
| **Wire** | Net name, connected pins list |
| **Graphic object** | Position, size, color, line width, layer |

<video controls width="100%">
  <source src="../img/schematic/properties-switching.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

## See Also

- [Placing Components](placing-components.md) — place and edit components.
- [Wiring & Nets](wiring-and-nets.md) — manage wires and net names.
- [Graphics & Annotations](graphics-and-annotations.md) — drawing primitives and text.
