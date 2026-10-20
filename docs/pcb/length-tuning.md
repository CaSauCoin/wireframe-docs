---
description: Route differential pairs as pairs, add GND return vias when they change layer, declare length groups, and tune length with accordion, trombone or sawtooth meanders in WireFrame — with a live length gauge and checks in length or in time.
---

# Length Tuning and Differential Pairs

Buses such as RMII, RGMII, SDMMC, QSPI or DDR need their traces to arrive together; a differential pair needs its two halves to stay together and equal. WireFrame keeps these as rules on the board — **pairs**, **length groups** and **class targets** — and gives you the tools to route and tune against them while you see the numbers.

## Declare pairs and groups

Three ways, all ending in the same rules (saved in the `.pcbxml`):

- **From net names.** **Design Rules ▸ High-Speed ▸ Detected from net names** (or **Properties ▸ Board Settings ▸ High-speed ▸ High-speed nets**) finds `USB_D+/D-`, `ETH_TX_P/N`, `DDR_DQ0…`, `QSPI_IO0…`, `*_CLK` and more, each with a target and a confidence. Accept the ones that are right. The [High-Speed Workbench](../high-speed/index.md) does the same on its **Start here** page and goes further: whole interfaces (USB, Ethernet, DDR byte lanes, RGMII, QSPI, SD/eMMC) with their published rules.
- **By hand, in Design Rules.** **Add pair** and **Add group** on the High-Speed page.
- **From the canvas.** Select tracks, right-click ▸ **High-speed ▸ Pairs & groups**: **Declare as differential pair**, **Remove from its pair**, **Add to length group ▸** an existing group, or **New group from selection**.

A pair's width and gap, its skew limit and a group's tolerance live on **net classes** — in length, or **in time** (picoseconds) when the nets change layer. See [Design Rules](design-rules.md) and the Workbench's [Rules](../high-speed/index.md#rules).

## Route a pair as a pair

With **Properties ▸ Board Settings ▸ High-speed ▸ Pairs: Both halves** on (the default), starting a route on a pad of a declared pair routes **both halves** together at the class's width and gap.

When the pair changes layer, **Return vias: Add GND vias** drops a ground via beside its two vias, so the return current changes reference plane at the same place as the signal. The High-Speed checks report a layer change without one.

## The length gauge

While you route a net that belongs to a pair, a length group or a class with a target length, the readout beside the cursor shows the routed length against its target — how long it is, how long it should be, and the difference — and the high-speed nets show markers in the layer list. In **Properties**, a selected track of such a net shows its measured length and its delta to the target.

## Add meanders

### With the Tune Length tool

1. Pick **Tune Length** on the PCB toolbar.
2. Hover a **straight segment** of a net that is short — short against its pair, its length group, or its class target.
3. The distance of the cursor from the segment sets the bump **height**; the side of the segment it is on sets the **side**.
4. Click to add. ++esc++ leaves the tool.

### From the right-click menu

Select a track, right-click ▸ **High-speed ▸ Tune length**:

| Field | Meaning |
|---|---|
| Target | **Match pair** (the partner's length), **Match group** (the group's longest), or **Class target** — each with the length it means |
| **Add (mil)** | How much length to add (filled from the target) |
| **Height (mil)** | How tall each bump is |
| **Pitch (mil)** | Centre to centre of the two legs of a bump. Keep legs at least 3 widths apart (pitch ≥ 4 × width) or they couple and the signal takes the short way |
| **Left / Right** | Which side of the track the bumps go |
| **Corners** | **Square**, **Chamfer 45°** or **Round** |

Press **Add meander**. The hint says how much was added in how many bumps — and how much is still missing if the segment was too short ("raise the height", or pick a longer straight segment).

The default corner style for every way of tuning is **Properties ▸ Board Settings ▸ High-speed ▸ Meanders**.

!!! tip "Where to tune a pair"
    Keep the gap constant and tune the short half **near where the mismatch starts** — usually right after the bend that made it. Skew that is corrected far from its cause still turns into common mode on the way, and common mode is what radiates.

## Check it

- **DRC** checks clearance around meanders like any other copper.
- **Design Rules ▸ High-Speed** shows each pair's skew and each group's length spread.
- The **High-Speed Workbench ▸ Checks** computes skew and matching **in time** as well as in length, impedance per layer, return path and crosstalk — see [Checks](../high-speed/checks-and-interfaces.md).

## See also

- [Routing traces](routing.md)
- [Design rules and net classes](design-rules.md)
- [High-Speed Workbench](../high-speed/index.md)
