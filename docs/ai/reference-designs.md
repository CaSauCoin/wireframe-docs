---
description: Lift a part's support circuit from a design that was built — a KiCad or Altium project, a folder or a GitHub repository — and add it to your board as a revision you review, with the source and its licence named.
---

# Reference Designs

!!! info "In development"
    `/reference` is new in the development builds after 1.5.47. The public download is still v1.3.8.

Most parts on a board have been wired correctly before, by the part's vendor on an evaluation board or by an open-hardware project that was built and tested. `/reference` takes that circuit from the design itself instead of asking a model to recall it.

```text
/reference U2
/reference U2 ~/Downloads/tps62902evm
/reference U3 https://github.com/<owner>/<repo>
```

## Where the design comes from

In the order every outside lookup in WireFrame takes:

1. **What you name.** A folder, a `.kicad_pro`, an Altium `.PrjPcb` or a WireFrame `.prjxml`. In a folder, only the projects whose schematics name the part are used.
2. **A URL you give.** A GitHub repository (or a folder inside one) is downloaded as its archive; a `.zip` of project files is downloaded as it is.
3. **URLs the Copilot names.** With no source, the Copilot is asked where published design files for the part live. WireFrame downloads them itself. A link that does not download produces nothing, and the Copilot's description of a circuit is never used.

KiCad and Altium projects are imported once and kept in the library cache, so a second `/reference` to the same design is quick.

## What is taken

WireFrame reads the imported design's own connectivity and drawing:

- **The main part.** The reference's part that is your row, matched by part number. An order code such as `TPS62902RPJR` finds `TPS62902`.
- **Its support circuit.** Resistors, capacitors, inductors, ferrites, crystals, diodes and small transistors on the main part's sheet that sit on its signal pins (EN, FB, SW, XTAL…), plus the ones one step further on nets only that circuit uses, such as the output capacitor behind an inductor.
- **Capacitors on a shared rail** only when they are drawn beside the main part. Twenty capacitors on +3V3 are not all the regulator's.
- **Never another IC or a connector.** Those are where the block ends, and their nets become its interface.

## How it lands on your board

The lifted circuit becomes a revision, reviewed and applied like any other change:

- each support part is a new row with the next free designator, in the block of your part;
- a net on one of the main part's pins joins the net your part already has on that pin — matched by pin **name** first, so a different package still lands correctly;
- rails and ground join your nets of the same name (`+3V3` and `3V3` are one rail);
- everything else is a new net, renamed when the name is taken.

The chat lists what was lifted, which of your nets it joined, and the nets **still to wire**, the ones the reference connected to its own parts (an I²C bus, a status line). It also quotes the **licence** found beside the source. Designs under a share-alike licence (CC BY-SA, CERN-OHL-S) can oblige you to publish your board; vendor evaluation files often allow use only with the vendor's parts. Check before you build.

When the reference's own library carries the main part, your row is bound to it as an **unconfirmed** part. Placement review marks it until you confirm it in BOM Review.

## Example

On the open-hardware One-Air-Max board (KiCad, CC BY-SA 4.0) as the source, `/reference U2` for a TPS62902 buck lifted 13 parts: the 1 µH inductor, the feedback divider, the soft-start capacitor and the input and output capacitors. It joined the design's `+3V3` and `GND`, named `+5V` as still to wire, and bound the TPS62902 itself from the reference's library. The whole run — import, lift, binding, the datasheet-backed check of the new part — took about two minutes.

## Limits

- Only KiCad and Altium projects can be read; a PDF schematic, OrCAD or Allegro files cannot.
- A reference drawn on one large flat sheet can still lend a capacitor that served a neighbouring IC; review the list before you keep it.
- Footprints come from the reference's library or your own, and are checked like any other part. Confirm them before **Update PCB**.

## See also

- [Placement Review and Your Edits](placement-review.md)
- [Fix or Create a Component](component-generator.md)
- [Datasheets, Repairs and Project Memory](datasheets-and-memory.md)
