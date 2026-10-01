# Enclosure Fit and Multi-Board Products

Two tabs of the Component Review window deal with the physical product rather than the circuit:

| Tab | Answers |
|---|---|
| **Board Fit** | What shape is the board, does the BOM fit on it, and does it fit the case? |
| **System** | When the product is several boards, how are they stacked and wired to each other, and is anything wrong between them? |

Open them from AI Copilot's review window. Both are saved with the project. A design with no enclosure is not a design with a problem: nothing on these tabs is a fault until you give the board a case or a second board.

## Board Fit

**Board Fit** works from the BOM and the mechanics alone — before the schematic is drawn and long before placement — so a board that cannot hold its parts is found early.

### Give the board a shape

Pick one of these on the tab:

| Button | Use it for |
|---|---|
| **3D model(s)…** | A case, frame, tube, or a board you will stack on, as STEP, IGES, STL, 3MF, or OBJ — one file or several. The outline, holes, and heights are already in it |
| **Standard board…** | Raspberry Pi HAT / micro-HAT, Arduino UNO shield, or FPV stacks 30.5 / 25.5 / 20 / 16 mm, each from its published drawing |
| **Board outline (SVG / DXF)…** | The shape only; heights are typed afterwards. See [Board Shape and Outline](../pcb/board-outline.md) |

Or describe it in chat: `/board 100x80 mm, M3 holes 4 mm in from each corner`, or `/board two boards on the 30.5 stack, 6 mm apart`.

The board preview is drawn from above, +Y down as on the PCB: **green** the board, **white** holes and cutouts, **red** keepouts, **orange** openings in the lid, **purple** parts the case pins in place.

### 3D files

**Add 3D files…** copies each file into the project so it reopens with it. For each file you can set:

- **which way is up** in the file;
- the **unit** — STL and OBJ carry none and are read as millimetres; a board 25× too small or too large means the file was in inches or centimetres;
- what the file **is** — a case, a lid, a frame, a board. Mark the **lid** file: its openings decide where the display and the keys go, and those parts are pinned under them.

**Cut this board out of the model…** lists the model's upward-facing surfaces so you can use one as the board. When a model already contains boards — a flight stack, a Raspberry Pi — **Use the boards in the model** takes them as the stack, with their outlines, holes, thicknesses, and spacers.

For the screw holes, the hole a screw passes the board through is what counts. Leaving it at zero takes the bore under it, which in a plastic boss is usually the pilot hole the screw bites into (2.5 mm for M3) — too small for the board.

### Stacks of boards

**Board above…** adds another board on top: a HAT, the flight controller over the ESC, the next board in a tube. A HAT or shield is moved so its holes land on the holes of the board below. Each board has a spacer below it — a standoff's length or a stacking header's mated height, which only you can state. What caps the tower (the lid's underside, a top plate) is set from the base; leave it at 0 and the top board's headroom is not checked.

Each board in the stack can be bound to a PCB file. **Update PCB** then gives that file the board's outline, holes, and heights.

`/topology` in the chat compares one board against a tower, and which parts go on which board, side by side.

### Does the BOM fit?

**What it has to hold** measures the area each part really needs against the board, with the height of each part against the case. The area factor is a multiple of the courtyard for clearance, routing channels, and fanout — a judgement, not a measurement: a hand-assembled two-layer board needs more room than a dense four-layer module. **both sides** is off by default, because a design that only fits by using both faces is a decision to make on purpose.

With several boards, **BOM across the boards** proposes which block goes on which board: blocks are kept whole, parts the case pins and parts already assigned stay where they are, and each remaining block — largest first — goes where most of its signals already are, on a board with room. The proposal is shown with the reason for each block; nothing moves until you accept it.

### Put the board on the schematic

The board can be added to the schematic as a part: a **BOARD CUT** box on the root sheet, with a footprint that carries the outline and cutouts on Edge.Cuts, the holes as NPTH pads, and courtyards around them. **Update PCB** then carries it like any other part, and it follows any later change to the board shape.

### Image — Board Fit with a case and lid

!!! note "Image capture brief"
    1. **Prepare:** Open a sample project with a BOM, and load a case STEP and its lid STEP on the **Board Fit** tab.
    2. **Build the frame:** Capture the **Board Fit** tab with the board preview (board, holes, keepouts, lid openings, and pinned parts in their colours) and the **What it has to hold** fit summary readable. Suggested size: **1400 × 820 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## System: products made of several boards

One project is one board. A product made of several — a flight stack, a HAT on a Pi, a display cabled to the main board — is an **assembly** (`.asmxml`): which boards, where each sits in the tower, and how they are wired to each other. Problems that no single project can see — a pinout that disagrees across a cable, two different rails joined, signals crossing without a ground — are checked here.

### Build an assembly

1. On the **System** tab, select **New assembly…** (or **Open assembly…**).
2. **Add a board (project)…** for each board you design in WireFrame.
3. **Add a board not designed here…** for bought boards — a Raspberry Pi, an ESC, a SoM — declared by what it is and the connector it offers. Its pins start with no nets, so nothing crossing to it is checked pin by pin until you declare them.
4. **Place…** each board in the tower and state its spacer.
5. **Connect two boards…** for each cable or header. Name what the connection is (for example *"JST-SH 1.0 mm"* or *"FFC 0.5 mm, contacts on opposite sides"*), then choose **Pin for pin** or **Reversed (1 meets N)** — what an FFC with contacts on opposite sides does between two connectors facing the same way.

Use **Open the boards** to load every board's project so its drawn schematic can be read; the project you are working on stays active. **Read the boards again** refreshes after you edit a board.

### Read the result

The summary line reads *N board(s), N connection(s) — N blocker(s), N warning(s)*. In the connection view, line thickness shows the kind of link (thick: plugged together, medium: a cable, thin: loose wires) and colour shows the worst finding on it. Each connection can be expanded pin by pin.

The **Assembly 3D** view shows the boards where the tower's spacers put them: left or right drag to turn, middle drag to move, wheel to zoom. Lifting the boards apart in that view is for looking only — the checks use the real spacers.

A board's own pinout is edited in its own project; open it from the System tab.

### Short video — Connect two boards in an assembly

!!! note "Video production brief"
    1. **Prepare:** Create a sample assembly with two WireFrame board projects that share a 4-pin connector.
    2. **Opening shot (1–2 s):** Show the **System** tab with both boards listed and no connection yet.
    3. **Action shot (6–10 s):** Select **Connect two boards…**, name the connection, choose **Pin for pin**, and confirm.
    4. **Result shot (3–4 s):** Hold on the connection with its pin-by-pin view and the blocker/warning summary readable.
    5. **Deliver:** Export a **12–18 second** 1080p MP4.

## See also

- [Board Shape and Outline](../pcb/board-outline.md)
- [3D Viewer](3d-viewer.md)
- [Placement and Routing Assistant](../ai/auto-placer-router.md)
