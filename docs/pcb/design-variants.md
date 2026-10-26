---
description: One design, several products — design variants in WireFrame. Parts fitted or not, values changed, parts kept out of the BOM or the position files, per variant; imported from and exported to KiCad 10 and Altium, and built by the fabrication outputs exactly as KiCad builds them.
---

# Design Variants

One board design often makes more than one product: a *Lite* build without the radio, a *HighGain* build with a different feedback resistor, a build for a customer who buys one part themselves. A **design variant** says what changes for that build — and only that.

For each part, a variant can say:

| | Meaning |
|---|---|
| **Fitted** off | Not fitted in this build (DNP). It stays in the BOM, marked DNP, and in the position file — as KiCad's outputs do. |
| **In BOM** off | Not bought for this build: left out of the BOM. |
| **Placed** off | Left out of the position (pick-and-place) files. |
| **Value** | The part's value in this build (`22k` instead of `10k`). |

A part a variant says nothing about is as drawn. The **default variant** is the design as drawn.

## Set up variants

**Tools ▸ Design Variants** opens the variant window.

- **Variants** lists the project's variants. Type a name and **Add**; edit the description in place; **Rename** or remove one (removing it removes what it did to every part). The **Active** column picks the variant the outputs build by default.
- **Parts in …** lists the parts of the open sheets (or of the board when no sheet is open) for the variant selected above: tick off *Fitted*, *In BOM* or *Placed*, or type the part's value in that variant. **Open the project's sheets** opens them when none are.

A change goes to every open sheet and board that holds the part, so the schematic and the board always agree. **Update PCB from schematic** also carries each part's variants to its footprint.

## Build a variant

In **File ▸ Export ▸ Fabrication Outputs**, the **Board** card has a **Variant** list when the design has variants. Pick one and generate: the pick-and-place file, the BOM (flat and grouped), the assembly drawing, IPC-2581, ODB++ and the X2 component files describe that build. The package's `README.txt` starts with the variant it is for, and switching variants marks a generated package out of date, so a package for one build is never saved as another.

The outputs agree with KiCad's: on a test design checked with `kicad-cli sch export bom --variant` and `kicad-cli pcb export pos --variant`, WireFrame's BOM and position files list the same parts with the same values for every variant.

## KiCad and Altium

| | KiCad 10 | Altium Designer |
|---|---|---|
| The list | `schematic.variants` in the `.kicad_pro`, `(variants …)` in the board | `[ProjectVariantN]` in the `.PrjPcb` (the description is the name) |
| Per part | `(variant …)` in each symbol instance and each footprint | `VariationN` — *Not Fitted* for a part left off |
| Read and written | all of it | *Not Fitted*, alternate-part values; the BOM, position-file and value changes Altium has no field for go under WireFrame's own keys |

Import a KiCad 10 or Altium project with variants and they are there; export and they go back out. Both directions are part of the [round-trip check](../import-export.md#a-round-trip-loses-nothing).

## See also

- [Fabrication and Export](fabrication-and-export.md)
- [Import and Export](../import-export.md)
