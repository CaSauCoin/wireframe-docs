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
| `led-chaser/` | The [tutorial](../docs/tutorial/index.md) board — see below |

## The tutorial board: `led-chaser/`

An NE555 clock steps a 74HC4017 decade counter; its ten outputs light ten red
LEDs set in a ring, one at a time. 25 parts (0805 passives and LEDs, two SOIC
ICs, a 2-pin header, four M3 holes) on a 50 × 60 mm two-layer board. Fictional,
made for the tutorial, like everything else here.

| Folder | What it is | Made by |
|---|---|---|
| `kicad/` | The design input: schematic, part placement, the LED cathode ring and the outline, as a KiCad 8 project with its footprints beside it (`fp-lib-table`) | `python3 samples/led_chaser.py` |
| `1-schematic/` | WireFrame project, schematic only — where the tutorial's PCB section starts | WireFrame's KiCad importer, on `kicad/` without the `.kicad_pcb` |
| `2-placed/` | + the board: parts placed, cathode ring drawn, everything else ratsnest | WireFrame's KiCad importer, on `kicad/` |
| `3-routed/` | The finished board: `2-placed` after **Auto-route** in WireFrame, saved | WireFrame (Route Assist) |

`led_chaser.py` checks that the drawn wires make exactly the netlist in its
`PARTS` table before it writes anything. The symbols and footprints are copied
from the KiCad libraries (CC-BY-SA 4.0 with the libraries' design exception);
it reads them from `$KICAD_LIBS` (default `~/.wireframe/library_cache/repos`).

Rebuilding the WireFrame projects after a change to `led_chaser.py` or to the
importer, from the WireFrame repository:

```bash
python3 ../wireframe-docs/samples/led_chaser.py
S=../wireframe-docs/samples/led-chaser; T=$(mktemp -d)
mkdir -p $T/sch-in && cp -r $S/kicad/led_chaser.kicad_pro $S/kicad/led_chaser.kicad_sch $S/kicad/fp-lib-table $S/kicad/footprints $T/sch-in/
cmake-build-debug/tests/cpp/wf-import-kicad $T/sch-in/led_chaser.kicad_pro $T/sch
cmake-build-debug/tests/cpp/wf-import-kicad $S/kicad/led_chaser.kicad_pro $T/full
rm -rf $S/1-schematic $S/2-placed
cp -r $T/sch/led_chaser_WireFrame $S/1-schematic
cp -r $T/full/led_chaser_WireFrame $S/2-placed
```

Then open `2-placed/led_chaser.prjxml` in WireFrame, box-select the whole
board, press Ctrl+Shift+W (**Auto-route selection**), wait for the
notification, save, and copy the project's `.prjxml`, `.schxml`, `.pcbxml` and
`led_chaser_lib/` into `3-routed/` (not `ai_memory.db`). Check the result with
`cmake-build-debug/tests/cpp/wf-pcb-lab ../wireframe-docs/samples/led-chaser/3-routed --dfm`:
no ratsnest, **DFM & DRC 0 error(s), 0 warning(s)** (48 tracks and 25 vias with
the importer and router of 2026-11-02).

Some scenes generate their data at capture time with WireFrame's own labs
(`wf-enclosure-lab --make-demo`, `wf-assembly-lab --make-demo`) instead of
storing it here — see `prepare:` in `.wf-docs.yaml`.
