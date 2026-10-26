---
description: Design blocks and channel reuse in WireFrame — keep a piece of circuit and place it again, in KiCad 9/10's own .kicad_block format, with its PCB layout; and lay out one channel of a multi-channel design, then repeat it on the others.
---

# Design Blocks and Channel Reuse

## Design blocks

A **design block** is a piece of circuit kept to be placed again: a regulator with its capacitors, an input filter, a connector with its protection. WireFrame keeps blocks in **KiCad's own format** (KiCad 9 and 10), so a block made in WireFrame opens in KiCad and a block from KiCad places in WireFrame:

```
MyBlocks.kicad_blocks/            a library is a folder
  ldo_3v3.kicad_block/            a block is a folder in it
    ldo_3v3.kicad_sch             its circuit, symbols included
    ldo_3v3.json                  description, keywords, fields
    ldo_3v3.kicad_pcb             its layout (KiCad 10), when saved with one
```

**Tools ▸ Design Blocks** opens the block window: the libraries on the left, the block picked on the right with a preview of its circuit.

### Libraries

| Library | Where |
|---|---|
| **WireFrame** | Your own blocks, in `~/.wireframe/design_blocks/`. Always there, always writable |
| The project's | Every library in the project's `design-block-lib-table` (`${KIPRJMOD}` is the project folder) |
| KiCad's | Every library in KiCad's own `design-block-lib-table`, when KiCad is installed |

### Save a block

1. Select what the block holds on a sheet — parts, wires, labels, power symbols, notes. Wires between two selected parts come with them.
2. **Tools ▸ Save Selection as Design Block…** (or the **Save selection as a block** card in the window).
3. Pick the library, give it a name, a description and keywords, and **Save block**.

A part keeps the footprint it names (`Resistor_SMD:R_0603_1608Metric`). When the project's board is open and the selected parts are placed on it, the block also keeps **their layout**: the footprints and the tracks and vias between them.

### Place a block

Pick it and **Place on sheet**. The block lands in the middle of the view — or, when that would cover what is already drawn, in the free space to the right — and stays **selected**, so you drag it where it goes. It is one undo step.

- Its parts take the **next free designators of the whole project** (`R1`, `R2` of the block become `R14`, `R15`), units of one part keep one designator, unnumbered `R?` are numbered. Tick **Keep the block's designators** to keep the ones that are free.
- Labels and power symbols come as they are: a label named `VIN` joins the `VIN` already in the design.
- The block moves by whole 50 mil (1.27 mm) steps, so its pins stay on the grid.

### Apply a block's layout

For a block saved with its layout: after **Update PCB from schematic**, make the board the active view and press **Apply its layout to the board**. WireFrame finds every place the block was placed on the project's sheets (its parts still drawn as placed), keeps the largest part of each where you put it on the board, places the others around it as in the block — turned with it — and lays the block's tracks and vias on that placement's nets. The routing of nets that only that placement uses is replaced; ++ctrl+z++ undoes the copper, then the placement.

## Repeat a channel's layout

A design with several identical channels (an 8-channel ADC front end, a multi-output driver) usually draws each channel as a copy of one sheet. **Tools ▸ Repeat Channel Layout** finds them: sheets with the same parts at the same places are **channels**.

1. Lay out one channel on the board — placement and routing.
2. Open **Tools ▸ Repeat Channel Layout**, pick that channel as the **Reference**, and tick the channels to lay out like it.
3. **Repeat layout**.

Each channel keeps its own copy of the reference's largest part where you placed it; the other parts are placed around it as the reference's are, turned with it. With **Copy routing** on, the reference's tracks and vias are laid on each channel's own nets; a net channels share (ground, a supply) is copied only where it runs among the channel's parts, and never twice. With **Replace routing** on, a channel's own earlier routing is taken up first — shared nets never are.

Parts are matched by where they are on the sheet and what they are, not by designator, so channels numbered `R101…` and `R201…` match. A part moved on one sheet makes that sheet a different circuit: it is no longer a channel.

## See also

- [Placing components](placing-components.md)
- [Footprints and placement](../pcb/footprints-and-placement.md)
- [Import & export](../import-export.md) — KiCad round trips
