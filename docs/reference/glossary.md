---
description: Plain-language definitions of the PCB design and EDA terms used in WireFrame — from ratsnest, net class and DRC to differential pair, return path, IR drop, Gerber and IPC-D-356 — each linked to where WireFrame uses it.
---

# Glossary

Short definitions of the terms used in this guide, each with the page where WireFrame works with it.

## Design and schematic

**BOM (bill of materials)**
: The list of parts a board needs, one row per part number, with quantities and designators. WireFrame writes it with the [fabrication outputs](../pcb/fabrication-and-export.md); the AI Copilot plans one from a requirement ([Design Agent](../ai/design-agent.md)).

**Designator (reference)**
: A part's name on the sheet and the board — R14, U1, J3. It links a symbol to its footprint and is how [cross-probing](../advanced/side-by-side-views.md) finds a part in every view.

**ERC (Electrical Rules Check)**
: Checks the schematic's connectivity: floating inputs, outputs driving each other, nets with one pin, duplicate designators. See [ERC](../schematic/erc.md).

**Footprint (land pattern)**
: The copper pads, silkscreen and courtyard a part is soldered to. See [Footprint Libraries](../libraries/footprints-library.md).

**Hierarchical sheet**
: A sheet placed inside another as a block, with labels as its ports. See [Wiring & Nets](../schematic/wiring-and-nets.md).

**Net, net label, power symbol**
: A net is everything electrically joined; a label names one and joins every wire with the same name; a power symbol (GND, +3V3) is a label that is a supply. See [Wiring & Nets](../schematic/wiring-and-nets.md).

**Netlist**
: The list of nets and the pins on each — what the schematic means electrically, and what the board is built from.

**Symbol**
: A part's drawing on the schematic, with its pins. See [Symbol Libraries](../libraries/symbols-library.md).

## Board

**Board outline (Edge.Cuts)**
: The board's shape, with its cutouts. See [Board Shape and Outline](../pcb/board-outline.md).

**Clearance**
: The minimum distance between copper of different nets (and to holes and the board edge). Set per net class in [Design Rules](../pcb/design-rules.md).

**Courtyard**
: The area a part occupies on the board, used to keep parts apart.

**Net class**
: A group of nets sharing rules — track width, clearance, via size, and for fast signals impedance, skew and length targets. See [Design Rules](../pcb/design-rules.md).

**Ratsnest**
: The thin lines showing connections not yet routed. They disappear as you route.

**Stack-up**
: The order and thickness of a board's copper and dielectric layers. Impedance, delay and plane capacitance are computed from it. See [High-Speed Workbench](../high-speed/index.md#stack-up).

**Via (through, blind/buried, micro)**
: A plated hole joining copper layers. A through via goes through the whole board; blind and buried vias span only some layers; a microvia joins neighbouring layers. See [Routing](../pcb/routing.md#vias-switching-layers).

**Zone (copper pour, plane)**
: A filled area of copper on a net — a ground plane, a power island. See [Zones & Planes](../pcb/zones-and-planes.md).

## Checks and manufacturing

**DRC (Design Rule Check)**
: Checks the board's copper against its rules: clearances, widths, unconnected nets. See [DFM & DRC](../pcb/dfm-and-drc.md).

**DFM (Design for Manufacturing)**
: Checks against what a board house can make: drill sizes, annular rings, copper to edge, mask slivers. See [DFM & DRC](../pcb/dfm-and-drc.md).

**Excellon (drill file)**
: The format drill files are written in — plated and non-plated holes separately.

**Gerber (RS-274X, Gerber X2)**
: The format board houses take: one file per layer (copper, mask, paste, silkscreen, outline). X2 adds attributes saying what each file is. See [Fabrication and Export](../pcb/fabrication-and-export.md).

**IPC-2221**
: The IPC standard WireFrame uses for a track's current capacity at a given temperature rise.

**IPC-D-356A**
: A netlist format the board house uses for bare-board electrical test.

**Pick-and-place (centroid) file**
: Each part's position, rotation and side, for the assembly machine.

## Signal and power integrity

**Characteristic impedance (Z0, Zdiff)**
: The impedance a signal sees along a track, set by its width, the dielectric and the plane under it. USB 2.0 wants 90 Ω differential; Ethernet 100 Ω. See [High-Speed Workbench](../high-speed/index.md).

**Common mode**
: The part of a differential signal that is the same on both halves. Skew creates it, and it is what radiates. See [Simulation](../high-speed/simulate-power-emi.md#simulate).

**Crosstalk (NEXT, FEXT)**
: Signal coupled from one track to its neighbour — near-end and far-end. See [Checks](../high-speed/checks-and-interfaces.md).

**Differential pair**
: Two tracks carrying a signal and its inverse, routed together. See [Length Tuning and Differential Pairs](../pcb/length-tuning.md).

**EMI / radiated emission**
: Energy a board radiates. Products must stay under limits such as CISPR 32 or FCC Part 15. See [EMI](../high-speed/simulate-power-emi.md#emi).

**Fly-by / tee topology**
: Ways to route one driver to several receivers — a chain past each (DDR3/DDR4 address and command) or a split into branches. See [Simulation](../high-speed/simulate-power-emi.md#simulate).

**IR drop**
: The voltage lost in copper between a regulator and the chip it feeds (current × resistance), on the supply and on the return. See [Power Analyzer](../power/power-analyzer.md).

**Length matching / time matching**
: Making the nets of a bus arrive together — by length, or by delay when they run on layers of different speed. See [Length Tuning](../pcb/length-tuning.md).

**Meander (accordion, trombone, sawtooth)**
: Bumps added to a track to make it longer. See [Length Tuning](../pcb/length-tuning.md#add-meanders).

**PDN (power distribution network)**
: Everything between a regulator and a chip's supply pins — copper, planes, capacitors. Its impedance across frequency must stay under a target. See [Power](../high-speed/simulate-power-emi.md#power-the-ac-side).

**Return path**
: The way a signal's current comes back — in the plane right under the track, when there is one. A gap in that plane forces it around and causes noise and emission. See [Checks](../high-speed/checks-and-interfaces.md).

**S-parameters (Touchstone)**
: A measured or simulated description of a channel's transmission and reflection across frequency, in `.sNp` files. See [Simulation](../high-speed/simulate-power-emi.md#simulate).

**Skew**
: The difference in arrival time between the two halves of a pair, or between nets of a bus.

**Termination**
: A resistor (or network) that matches a line's impedance so its signal does not reflect.

## Simulation

**SPICE (ngspice, Xyce, LTspice)**
: Circuit simulators. WireFrame has ngspice built in and can use Xyce or LTspice. See [Simulation](../simulation/index.md).

**Transient, AC, DC sweep, operating point**
: The analyses SPICE runs: over time, over frequency, over a swept value, and at rest. See [Running a Simulation](../simulation/running-simulation.md).

**Testbench**
: The sources, loads and measurements around a circuit under simulation, with pass/fail criteria. See [Testbenches & Measurements](../simulation/testbenches-and-measurements.md).

## Products of several boards

**Assembly (`.asmxml`)**
: The boards that make a product and the connections between them. See [Multi-Board Products](../advanced/multi-board.md).

**Board stack (tower)**
: Boards mounted above each other, each on a spacer. See [Enclosure Fit](../advanced/enclosure-and-assembly.md#stacks-of-boards).

**HAT, cape, shield**
: An add-on board for a Raspberry Pi, a BeagleBone, an Arduino. See [Multi-Board Products](../advanced/multi-board.md#bought-boards).
