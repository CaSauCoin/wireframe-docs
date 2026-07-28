# Schematic Templates & Title Block

WireFrame includes a template system for schematic sheets — customizable page borders, title blocks, revision fields, and company branding. Templates ensure professional, consistent documentation across all your schematic pages.

---

## Title Block

Every schematic sheet has a **title block** in the lower-right corner. It displays metadata from the page settings:

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│                                                               │
│                      (Schematic canvas)                       │
│                                                               │
│                                                               │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  Title: Power Supply Rev B    │ Drawn by: John Doe     │  │
│  │  Company: WireFrame Labs      │ Date: 2026-03-23       │  │
│  │  Revision: 1.2                │ Sheet: 1 / 3           │  │
│  └─────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────┘
```

### Editing the title block

1. Click on **empty canvas** (deselect everything).
2. The **Properties panel** shows page-level settings:

| Field | Description | Example |
|---|---|---|
| Paper size | A4, A3, A2, or custom dimensions | A4 |
| Title | Design title | "Power Supply Rev B" |
| Company | Organization name | "WireFrame Labs" |
| Revision | Version identifier | "1.2" |
| Date | Design date | "2026-03-23" |
| Drawn by | Author name | "John Doe" |
| Sheet number | Current / total sheets | "1 / 3" |
| Border color | Color of page border and title block | Cyan |

Changes are applied **immediately** — the title block updates in real time on the canvas.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Properties panel with page settings visible:
     - All fields listed above filled with sample data.
     - The schematic canvas in the background showing the title block rendered
       in the bottom-right corner with matching values.
     - The border color picker showing "Cyan" selected.
     SUGGESTED SIZE: 1280×720px (full window showing both panel and canvas)
-->
![Title Block Settings](../img/schematic/title-block-settings.png)

---

## Page Setup

### Paper size

WireFrame supports standard paper sizes and custom dimensions:

| Size | Dimensions |
|---|---|
| A4 | 297 × 210 mm |
| A3 | 420 × 297 mm |
| A2 | 594 × 420 mm |
| Custom | User-defined width × height |

Select the paper size from the **Paper size** dropdown in the Properties panel (when nothing is selected).

### Grid settings

The dot grid on the schematic canvas helps with alignment:

- Grid dots are spaced at regular intervals for clean component placement.
- Components and wires snap to the grid automatically.

---

## Template Builder

The Template Builder (`Sch_Template_Builder`) constructs the visual elements of the schematic page:

- **Page border** — drawn from the paper size dimensions with margins.
- **Title block frame** — structured table with labeled cells.
- **Revision history** — optional rows for tracking design changes.

The template is automatically rendered as part of the schematic canvas and included in **PDF exports**.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture a schematic with a clearly visible template:
     - A4 page with a thin border around the entire sheet.
     - A structured title block in the bottom-right showing all fields.
     - A few components placed on the sheet (for context).
     - The border color set to cyan (default) for contrast against the dark background.
     SUGGESTED SIZE: 900×600px
-->
![Template Example](../img/schematic/template-example.png)

---

## Tips

!!! tip "Consistent documentation"
    Fill in the title block fields for every schematic sheet in your project. This information appears in PDF exports and helps team members identify documents.

!!! info "Title block in exports"
    When you export a schematic to PDF (**File → Export → Schematic PDF**), the title block is included exactly as it appears on the canvas — including all text, borders, and colors (converted to print-friendly black/grey).

---

## See Also

- [Properties & Attributes](properties-and-attributes.md) — editing page settings in the Properties panel.
- [Fabrication & Export](../pcb/fabrication-and-export.md) — PDF export includes the title block.
