# Sample data for documentation captures

Input files used when WireFrame's `doc_builder` lab captures the screenshots
and short videos in this guide (`python3 -m doc_builder docs-fill ../wireframe-docs`
from the WireFrame repository; see `.wf-docs.yaml`).

Everything here is **fictional** and made for this documentation — no
third-party data, no customer data. Regenerate with:

```bash
python3 samples/generate.py      # needs pdftoppm (poppler-utils) for the PNG
```

| File | What it is |
|---|---|
| `outlines/demo-board.dxf` | 80 × 60 mm board, R3 corners, four M3 holes 4 mm from each corner, a 20 × 12 mm battery pocket. ASCII DXF in millimetres |
| `outlines/demo-board.svg` | The same board as SVG (mm) |
| `datasheets/wf-demo8.pdf` | Two-page datasheet of **WF-DEMO8**, a fictional 8-pin SOIC-8 buck converter: pinout, operating conditions, application notes, package data |
| `datasheets/wf-demo8-pinout.png` | The pin table as an image, for the pin-OCR scene |

Some scenes generate their data at capture time with WireFrame's own labs
(`wf-enclosure-lab --make-demo`, `wf-assembly-lab --make-demo`) instead of
storing it here — see `prepare:` in `.wf-docs.yaml`.
