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

!!! note "Video needed"
    Record **10–15 seconds** showing one generated block card, adding it to a schematic, the proposed layout, and the placed result. Do not use the former ASCII block diagram. 1080p.

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

!!! note "Video needed"
    Record **12–18 seconds** showing a small routed PCB, unrouted/ratsnest count before and after, one layer transition, and the DRC/DFM re-check. Do not present progress animation alone as proof of a valid route. 1080p.

## Manual override is expected

Automatic placement and routing cannot decide product-specific mechanical, thermal, EMC, creepage, or signal-integrity requirements. Lock or manually position critical components and route critical nets deliberately.

## Removed legacy content

The previous page documented clustering algorithms, A* internals, route-order implementation, and experimental GNN training. Those details were removed because this site is a user guideline, not developer architecture documentation.

## See also

- [AI Design Agent](design-agent.md)
- [PCB Footprints and Placement](../pcb/footprints-and-placement.md)
- [Routing Traces](../pcb/routing.md)
- [DFM and DRC](../pcb/dfm-and-drc.md)
