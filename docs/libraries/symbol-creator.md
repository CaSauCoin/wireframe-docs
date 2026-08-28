# Symbol Library Editor

Use the Symbol Library Editor to create or correct schematic symbols that are not available from an approved library or the AI Component Generator. A symbol is acceptable only when its logical pins match the physical component and its footprint mapping.

## Open the editor

Choose **Tools → Symbol Library Editor**. When editing an existing library item, start from the selected symbol and save to the intended local library rather than overwriting an unrelated source.

## Information to prepare

Before drawing, obtain the manufacturer datasheet and record:

- Exact part number and package variant.
- Pin numbers, names, and electrical roles.
- Hidden, power, no-connect, and duplicated unit pins.
- Default reference prefix and displayed value.
- Intended footprint and its pad numbering.

## Create the symbol

1. Set a unique symbol name, reference prefix, and default value.
2. Draw a simple body that remains readable at normal schematic zoom.
3. Add every physical pin with the datasheet number and signal name.
4. Assign the correct electrical type to support meaningful ERC results.
5. Arrange inputs, outputs, power, and control pins consistently.
6. Save the symbol into the intended local library.

Do not encode package geometry into the schematic symbol. Physical dimensions, pad shape, and courtyard belong to the footprint.

### Image — Symbol Library Editor

!!! note "Image needed"
    Capture the v1.5.47 Symbol Library Editor with an eight-pin example selected. Show the body, pin numbers/names, and the properties used for one pin.

## Validate before use

Compare the saved symbol with the datasheet line by line:

- Every physical pin is represented exactly once unless the device specification requires otherwise.
- Pin numbers and names match the selected package variant.
- Power and ground pins are not hidden accidentally.
- Input/output/passive types support correct ERC behavior.
- Symbol pins map one-to-one to footprint pads.
- The symbol remains readable when placed and wired on a normal sheet.

Place the symbol in a temporary schematic, connect representative nets, and run ERC. Correct the library source rather than patching each placed instance.

### Short video — Create and validate a symbol

!!! note "Video needed"
    Record a 25–35 second clip showing a pin added or corrected, the symbol saved to a local library, placed in a test schematic, and checked with ERC.

## When to use AI generation

For a supported workflow based on an exact datasheet, **AI Gen → From Datasheet** may prepare both symbol and footprint. It does not remove the same pin, pad, dimension, and mapping review. See [AI Component Generator](../ai/component-generator.md).

## Related guidelines

- [Symbol Libraries](symbols-library.md)
- [Footprint Libraries](footprints-library.md)
- [Library Import and Management](library-converter.md)
- [ERC](../schematic/erc.md)
