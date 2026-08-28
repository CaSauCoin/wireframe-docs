# Placing Components

Place schematic symbols from approved local libraries and assign the exact value and PCB footprint required by the selected physical part.

## Prepare the library

1. Open **View → Local Library Manager**.
2. Add the KiCad symbol file or containing library folder.
3. Confirm the source and symbol in the active inventory.
4. Activate the target schematic and search its Component Library.

If the exact part is missing, import an approved library, create it in Symbol Library Editor, or use the [AI Component Generator](../ai/component-generator.md) with full datasheet review.

## Place a symbol

1. Search by exact part family or symbol name.
2. Select or double-click the intended symbol to enter placement mode.
3. Move the preview to a clear grid location.
4. Rotate if needed and click to place.
5. Press ++esc++ to return to selection.

### Short video — Find and place a symbol

!!! note "Video review needed"
    Capture 10–15 seconds showing an approved library source, symbol search, grid-snapped placement, and exit from placement mode. Replace older media if the library UI differs.

## Complete component properties

Select the component and verify:

| Field | Review |
|---|---|
| Designator | Unique and appropriate prefix |
| Value | Electrical value or exact orderable part number |
| Footprint | Exact package variant and pad count |
| Comment | Useful design or sourcing note, when required |

Changing a designator can affect connected references. Review the updated item and run ERC before PCB update.

## Move, rotate, copy, or delete

Use drag to move, ++r++ to rotate, standard clipboard shortcuts to duplicate, and ++delete++ to remove. After moving or rotating a connected component, inspect each wire endpoint at the pin tip.

Pasted components receive new identities to avoid duplicates, but you must still review their values, footprint assignments, and connections.

## Pre-ERC checklist

- Exact device and package variant are known.
- Designator is unique.
- Value and rating are correct.
- Footprint pad numbering matches symbol pins.
- Polarity and orientation are clear.
- Every used pin is connected intentionally; unused pins are handled explicitly.

## Related guidelines

- [Symbol Libraries](../libraries/symbols-library.md)
- [Wiring and Nets](wiring-and-nets.md)
- [Properties and Attributes](properties-and-attributes.md)
- [ERC](erc.md)
