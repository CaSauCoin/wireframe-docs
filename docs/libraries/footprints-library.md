# Footprint Libraries

Footprints define the physical pads, drills, component outline, and optional 3D model used on the PCB. Select the exact manufacturer package and recommended land pattern, not only a similarly named footprint.

## Add a footprint source

1. Open **View → Local Library Manager**.
2. Add the containing folder or KiCad footprint source.
3. Confirm that the source is active and the footprint appears in inventory.
4. Activate a PCB and search its Component Library.

Keep custom footprints and their 3D models in a controlled project or team location so another machine can resolve them.

### Image — Footprint source and active inventory

!!! note "Image needed"
    Capture Local Library Manager in v1.5.47 with a KiCad footprint source and several active inventory items visible. Hide private paths.

## Review a footprint

Compare the footprint with the exact datasheet land pattern:

- package name and body dimensions;
- pad count, numbering, shape, size, and pitch;
- plated or non-plated drill geometry;
- pin-1 or polarity marker;
- solder-mask and paste behavior;
- courtyard, silkscreen, and fabrication outlines;
- component origin and board-side orientation;
- symbol-pin to footprint-pad mapping.

Print or measure at 1:1 scale when dimensions are safety-critical. A 3D model is useful for review but does not prove that the pads are correct.

## Create or edit a footprint

Open **Tools → PCB Footprint Editor**. Configure the package and pads, review the live result, then save it as a KiCad-compatible `.kicad_mod` in the intended local library.

### Image — PCB Footprint Editor

!!! note "Image review needed"
    Capture the current editor with package controls, pad numbering, dimensions, and preview visible. Replace older “Footprint Wizard” media if its window title or controls differ from v1.5.47.

Before release, place the footprint on a test board and inspect pad geometry, courtyard, silkscreen, origin, and orientation.

## Align a 3D model

Select the footprint and open the available 3D-model editing action. Choose the approved STEP or OBJ file, then adjust offset, scale, and rotation until pin 1, body position, and board side match the 2D footprint.

### Short video — Align a footprint model

!!! note "Video review needed"
    Record 15–20 seconds showing a public sample model aligned with the 2D pads and checked from top and underside views. Hide private paths.

## Import an Altium footprint library

In **Local Library Manager**, choose the Altium importer and select a supported `.PcbLib`, `.IntLib`, or `.LibPkg` file. Review all converted pads and dimensions; update external 3D model paths when needed.

Eagle footprint import is not exposed in the current release UI and is intentionally omitted.

## Related guidelines

- [Symbol Libraries](symbols-library.md)
- [Library Import and Management](library-converter.md)
- [AI Component Generator](../ai/component-generator.md)
- [Footprints and Placement](../pcb/footprints-and-placement.md)
- [3D Viewer](../advanced/3d-viewer.md)
