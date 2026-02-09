# Properties and Text Attributes

This page covers the schematic properties panel and text attributes.

---

## Sheet and page settings

For a `SchematicDocument`, `PageSettings` includes:

- **Paper size**: A4, A3, A2 or Custom.
- Title block:
  - Title
  - Company
  - Revision
  - Date
  - Drawn by
  - Sheet number / total
  - Filename
- Border color.

The properties panel allows:

- Editing these fields.
- Potentially previewing the title block on the sheet border.

> **Image placeholder**  
> `![Page properties](img/schematic/page-properties.png)`  
> _Panel with fields for title, company, revision, sheet numbers and paper size dropdown._

---

## Component attributes

`PlacedComponent` has:

- **Logical fields**:
  - `id` (designator)
  - `value`
  - `comment`
  - `type`
  - `m_footprintName`
- **Text attributes** (for positioning and formatting text on screen):
  - `designatorAttribute`
  - `valueAttribute`
  - Pin name and number attributes per pin.

Each `TextAttribute` contains:

- `content` – the displayed string.
- `relativePosition` – offset from component origin.
- `rotation` – angle in degrees.
- `fontSize`.
- `isVisible`.

Editing these from the properties panel uses commands:

- `ModifyAttributeCommand` – for designator, value, pin name/number.
- `RotateAttributeCommand` – for rotating labels.

---

## Aligning attributes

For multi‑component designs, attribute alignment is useful:

- The selection system stores `AttributeRef` for selected text attributes.
- Functions like `alignSelectedAttributes` can arrange:
  - All selected names along a horizontal line.
  - All values aligned to one side (left/right) of components.

From the user side:

- Expect commands like “Align text horizontally/vertically” in context menus or hotkeys.

> **Image placeholder**  
> `![Aligned attributes](img/schematic/aligned-attributes.png)`  
> _Several resistors with perfectly aligned designators and values, demonstrating alignment tools._

---

## Wire and net properties

For selected wires or nets, the properties panel may show:

- Net name.
- Connected pins.
- Option to rename the net (via `ChangeNetNameCommand`).
- Net classification (later used for PCB net classes).

Renaming a net label updates:

- Component value/text for `NetLabel` components.
- Underlying net name within schematic netlist.

---

## Selection‑dependent content

The schematic properties panel dynamically switches content based on selection:

- **Single component selected**:
  - Component fields and its text attributes.
- **Multiple components selected**:
  - Multi‑edit possibilities or disabled fields.
- **Net label selected**:
  - Net name editing.
- **No selection**:
  - Document/page properties (sheet settings).

> **Video placeholder**  
> _Short video where user clicks different elements (component, net label, background) and the properties panel updates to show the corresponding controls._