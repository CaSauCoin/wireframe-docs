# Schematic Templates & Title Block

WireFrame includes a template system for schematic sheets — customizable page borders, title blocks, revision fields, and company branding. Templates ensure professional, consistent documentation across all your schematic pages.

---

## Title Block

Every schematic sheet has a **title block** in the lower-right corner. It displays metadata from the page settings:

### Image — Completed schematic title block

!!! note "Image needed"
    Capture an entire schematic page with its lower-right title block readable. Use sample project metadata rather than a customer or unreleased product name.

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

### Image — Title-block properties

!!! note "Image needed"
    Capture the page-level Properties panel beside the title block it updates. Make the title, revision, date, author, and sheet number readable.

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

## Sheet template behavior

WireFrame constructs the visual elements of the schematic page from its settings:

- **Page border** — drawn from the paper size dimensions with margins.
- **Title block frame** — structured table with labeled cells.
- **Revision history** — optional rows for tracking design changes.

The template is automatically rendered as part of the schematic canvas and included in **PDF exports**.


---

## Tips

!!! tip "Consistent documentation"
    Fill in the title block fields for every schematic sheet in your project. This information appears in PDF exports and helps team members identify documents.

!!! info "Title block in exports"
    When you select **File → Export → Export Schematic to PDF**, the title block is included with the sheet. Review the exported PDF for readable text, borders, and revision data.

---

## See Also

- [Properties & Attributes](properties-and-attributes.md) — editing page settings in the Properties panel.
- [Fabrication & Export](../pcb/fabrication-and-export.md) — PDF export includes the title block.
