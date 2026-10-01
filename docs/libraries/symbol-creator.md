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

## Generate pins from images with AI OCR

Use **AI OCR Manager** when the datasheet exposes a clear pin table as an image and manual entry would be error-prone.

1. Open the OCR action from Symbol Library Editor.
2. Select **Add Images** to choose one or more PNG or JPEG pin-table captures, or **Paste from Clipboard** when the image is already copied.
3. Inspect every thumbnail and use **Remove** on package drawings, timing charts, or unrelated tables.
4. Select **Generate Pins**.
5. Compare the generated number, name, and electrical type for every pin with the exact datasheet before saving.

**Generate Pins** requires at least one image. **Cancel** closes the modal without running generation. OCR can confuse characters such as `0`/`O`, `1`/`I`, overbars, slashes, and active-low markers, so it must never be treated as an approved pin table by itself.

### Image — AI OCR Manager with a clean pin table

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture **AI OCR Manager** with two public datasheet pin-table images loaded. Show **Add Images**, **Paste from Clipboard**, one **Remove** action, **Generate Pins**, and **Cancel**. Crop or blur local paths while keeping the thumbnails readable. Suggested size: **1200 × 780 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

### Short video — OCR pins and verify one correction

!!! note "Video production brief"
    1. **Prepare:** Have one clear public pin-table image and one irrelevant public datasheet image ready in a neutral folder.
    2. **Opening shot (1–2 s):** Hold on the empty **AI OCR Manager**.
    3. **Action shot (6–9 s):** Add both images, remove the irrelevant one, select **Generate Pins**, and cut across processing after showing one real status.
    4. **Result shot (3–5 s):** In Symbol Library Editor, highlight and correct one OCR mismatch against the visible public reference.
    5. **Deliver:** Export a **12–18 second** 1080p MP4; do not imply that unreviewed OCR output is approved.

### Image — Symbol Library Editor

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the v1.5.47 Symbol Library Editor with an eight-pin example selected. Show the body, pin numbers/names, and the properties used for one pin.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

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

!!! note "Video production brief"
    1. **Prepare:** Open a public demo symbol with one known pin issue and a writable test library.
    2. **Opening shot (2–3 s):** Show the incorrect pin and the corresponding public datasheet row.
    3. **Action shot (12–17 s):** Add or correct the pin, save to the local library, then place the updated symbol in a test schematic.
    4. **Verification shot (7–10 s):** Connect the representative nets, run ERC, and hold on the resulting clean or expected summary.
    5. **Deliver:** Export a **25–35 second** 1080p MP4 with the corrected number and name readable.

## When to use AI generation

For a supported workflow based on an exact datasheet, **AI Gen → From Datasheet** may prepare both symbol and footprint. It does not remove the same pin, pad, dimension, and mapping review. See [AI Component Generator](../ai/component-generator.md).

## Related guidelines

- [Symbol Libraries](symbols-library.md)
- [Footprint Libraries](footprints-library.md)
- [Library Import and Management](library-converter.md)
- [ERC](../schematic/erc.md)
