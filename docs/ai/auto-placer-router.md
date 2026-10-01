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

## Update and place the PCB

After the schematic is approved, use **Tools → Update Schematic to PCB**. Arrange footprints by function, then verify:

- connectors and controls are reachable;
- decoupling parts are close to the intended pins;
- power paths are short and wide enough;
- noisy and sensitive blocks are separated;
- board-edge and mechanical clearances are respected.

## Run PCB auto-routing

If using an automatic PCB route:

1. Finalize board outline and placement first.
2. Confirm net classes and design rules.
3. Run the router.
4. Inspect every via, layer transition, clearance, and unrouted net.
5. Manually repair critical power, high-speed, RF, differential, and sensitive analog paths.
6. Run DRC and DFM.

### Short video — Review an automatic route

!!! note "Video production brief"
    1. **Prepare:** Use a small demo PCB with a known ratsnest count and a reviewed automatic-route proposal containing one via.
    2. **Opening shot (2 s):** Show the unrouted count and the relevant board area before applying the proposal.
    3. **Action shot (6–10 s):** Apply the route, show the F.Cu-to-B.Cu transition at the via, then open and run **DFM & DRC Check**. Cut only inactive processing time.
    4. **Result shot (3–4 s):** Hold on the reduced ratsnest count and the actual check summary; do not stop on a progress animation.
    5. **Deliver:** Export a **12–18 second** 1080p MP4 and retain enough resolution to inspect both layer colors.

## Manual override is expected

Automatic placement and routing cannot decide product-specific mechanical, thermal, EMC, creepage, or signal-integrity requirements. Lock or manually position critical components and route critical nets deliberately.

## Removed legacy content

The previous page documented clustering algorithms, A* internals, route-order implementation, and experimental GNN training. Those details were removed because this site is a user guideline, not developer architecture documentation.

## See also

- [AI Design Agent](design-agent.md)
- [PCB Footprints and Placement](../pcb/footprints-and-placement.md)
- [Routing Traces](../pcb/routing.md)
- [DFM and DRC](../pcb/dfm-and-drc.md)
