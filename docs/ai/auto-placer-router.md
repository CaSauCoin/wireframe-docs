# Placement and Routing Assistant

Use WireFrame's placement and routing assistance after component identities, footprints, pin counts, and connections have been reviewed. Automatic output is a proposed starting point, not a finished board.

## Before placement

- resolve every missing physical component;
- confirm symbol pins match footprint pads;
- review functional blocks;
- run Netlist Check and ERC;
- confirm the target schematic or PCB is active;
- save the project.

## Place functional blocks on a schematic

When Copilot presents a block card that can be placed:

1. Review its components and connections.
2. Add or drag the block to the schematic.
3. Inspect the placement and wire proposal.
4. Apply it only when it targets the intended sheet.
5. Move crowded items and re-run ERC.

### Short video — Place a Copilot block

!!! note "Video production brief"
    1. **Prepare:** Generate one small approved functional block and leave its card visible beside an empty schematic area.
    2. **Opening shot (1–2 s):** Hold on the block card with its title and component list readable.
    3. **Action shot (5–8 s):** Drag the card to the schematic, pause on the proposed layout, then confirm placement.
    4. **Result shot (2–3 s):** Hold on the placed block with symbols and interface nets visible.
    5. **Deliver:** Export a **10–15 second** 1080p MP4; use real UI only and no ASCII substitute.

## Run schematic auto-routing

From **Simulate & Verify**, use **Run Schematic Auto-Router** only after library and netlist checks pass. Inspect:

- whether wires terminate on the correct pins;
- whether labels and junctions remain readable;
- whether power and ground nets are clear;
- whether generated paths cross symbols or hide annotations.

Use Undo or **Revise Design** when the result is not acceptable.

## Update the schematic to a PCB

After the schematic is approved, use **Tools → Update Schematic to PCB**. Then give the board its shape — **File → Import → CAD Outline**, `/board`, or the **Board Fit** tab (see [Board Shape and Outline](../pcb/board-outline.md)). The layout refuses a board with no outline.

## Lay the PCB out with `/layout`

With the PCB open, type `/layout` in AI Copilot. The layout runs on a **copy** of the board in five stages, shown on a live card in the chat as they happen:

| Stage | What it does |
|---|---|
| **Place** | Puts parts on the board: connectors to the edge facing out, each functional block around its busiest part, decoupling capacitors against the pins they serve |
| **Planes** | Adds the copper pours the design rules ask for; a split plane gives each rail the region over its own loads |
| **Vias** | A fanout via for every surface pad of a plane net, into its own rail's region; thermal via arrays in exposed pads |
| **Route** | Tracks for every net no plane or pour carries. Nothing is forced: a net that cannot be routed cleanly is named, never shipped with a violation |
| **Stitch** | Ground stitching and the edge via fence, after the tracks |

**Nothing changes on the board until you apply.** The card has **Stop** while it runs, then **Apply to the board** (or **Apply this option**) and **Discard**. After applying, **Ctrl+Z** takes it back one stage at a time.

### Choose the copper layer count first

The number of copper layers sets the board's price and what the layout can do — 2 layers is cheapest (rails routed, ground poured), 4 layers adds inner ground and power planes. It is **your** decision: Copilot asks for it before the first layout and records the answer for the project; it does not lay a board out until you have answered.

### Ways to use `/layout`

| You type | What happens |
|---|---|
| `/layout` | All stages, no model call |
| `/layout place,route` | Only the stages you list (`place`, `planes`, `vias`, `route`, `stitch`) — no model call |
| `/layout apply` | Commits the proposed layout; `/layout apply option <name>` commits one compared option |
| `/layout discard` | Throws the proposal away; the board stays as it was |
| `/layout rules` | Prints the layout rules in force (net classes, widths, clearances) |
| `/layout check` | Checks the board as it stands; `/layout check full` lists every item |
| `/layout <what you want>` | Copilot plans the layout from your request — for example *"keep the keypad together and route on two layers"* |

With a free-text request, Copilot can lay the board out **several ways and compare them** (parts placed, connections routed, vias, copper, overlaps, parts off the board, decoupling distance, blockers), show the table, say which the numbers favour, and **ask which to apply**. When you ask for the board to be finished rather than for options, it can keep improving a layout round by round — each round listed with its reason — until everything is placed and routed or no change helps.

Copilot changes a net class (a narrower track or a smaller clearance) only if you allowed rule changes, never below the fabricator's minimum, and never below **0.10 mm** track/space on 1- and 2-layer boards. It tells you which classes it changed and asks you to accept them.

### Short video — Lay out a board with /layout

!!! note "Video production brief"
    1. **Prepare:** Open the sample project's PCB with a board outline, the copper layer count already chosen, and parts not yet placed.
    2. **Opening shot (1–2 s):** Show the unplaced board and the AI Copilot chat side by side.
    3. **Action shot (8–12 s):** Type `/layout` and let the live card run through Place, Planes, Vias, Route, and Stitch; cut only waiting time.
    4. **Result shot (3–4 s):** Hold on the finished card with its routed count and the **Apply to the board** and **Discard** buttons visible, then press **Apply to the board**.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and keep the stage labels readable.

### Review an applied layout

1. Inspect every via, layer transition, clearance, and connection the router named as unrouted.
2. Manually repair critical power, high-speed, RF, differential, and sensitive analog paths.
3. Run **DFM & DRC Check**.

### Short video — Review an automatic route

!!! note "Video production brief"
    1. **Prepare:** Use a small demo PCB with a known ratsnest count and a reviewed automatic-route proposal containing one via.
    2. **Opening shot (2 s):** Show the unrouted count and the relevant board area before applying the proposal.
    3. **Action shot (6–10 s):** Apply the route, show the F.Cu-to-B.Cu transition at the via, then open and run **DFM & DRC Check**. Cut only inactive processing time.
    4. **Result shot (3–4 s):** Hold on the reduced ratsnest count and the actual check summary; do not stop on a progress animation.
    5. **Deliver:** Export a **12–18 second** 1080p MP4 and retain enough resolution to inspect both layer colors.

## One board or a tower: `/topology`

`/topology` asks whether the product should be one board or a stack of boards, and if a stack, which part goes on which board. The options are measured side by side from the design and any 3D files on the **Board Fit** tab; without a design, only the available room is measured. See [Enclosure Fit and Multi-Board Products](../advanced/enclosure-and-assembly.md).

## Manual override is expected

Automatic placement and routing cannot decide product-specific mechanical, thermal, EMC, creepage, or signal-integrity requirements. Lock or manually position critical components and route critical nets deliberately.

## Removed legacy content

The previous page documented clustering algorithms, A* internals, route-order implementation, and experimental GNN training. Those details were removed because this site is a user guideline, not developer architecture documentation.

## See also

- [Copilot Commands](commands.md)
- [Board Shape and Outline](../pcb/board-outline.md)
- [AI Design Agent](design-agent.md)
- [PCB Footprints and Placement](../pcb/footprints-and-placement.md)
- [Routing Traces](../pcb/routing.md)
- [DFM and DRC](../pcb/dfm-and-drc.md)
