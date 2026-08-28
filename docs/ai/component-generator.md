# AI Component Generator

Use **AI Component Generator** when a design needs a physical component that is not ready in your project library. WireFrame can create a schematic symbol and a matching PCB footprint from a known template or from a manufacturer datasheet.

Generated library items are a starting point for review. Always compare the result with the exact manufacturer part number, pin table, package drawing, and recommended land pattern before using it in a board.

## Before you start

Prepare the following information:

- the exact manufacturer part number;
- the package variant, such as `SOIC-8`, `TQFP-48`, or `QFN-32`;
- the physical pin or pad count;
- the manufacturer datasheet for any uncommon or package-sensitive part;
- a writable project library location.

Avoid generating from a family name alone. For example, `STM32`, `USB-C connector`, or `5 V regulator` can refer to many incompatible pinouts and packages.

## Open the generator

1. Open the AI design's **Component Review**.
2. Find a component marked **Not in Pool**, **Symbol not in Pool**, or showing a pin-count mismatch.
3. Confirm its **Value** and **Footprint Package**.
4. Select **AI Gen** on that component card.

To create straightforward missing parts in one pass, select **AI Gen Missing** below the component list. Use this bulk action only when the component names, packages, and pin counts are already unambiguous. Review every generated result afterward.

### Image — Missing component card and AI Gen action

!!! note "Image needed"
    Capture **Component Review** with one component card marked **Not in Pool**. Include the component name, **Value**, **Footprint Package**, **AI Gen**, **Create**, and **Import** controls. Crop tightly enough that the warning and the action buttons remain readable. Suggested size: **1200 × 700 px**.

### Short video — Generate all missing components

!!! note "Short video needed"
    Record **8–12 seconds** showing two or more missing component cards, selecting **AI Gen Missing**, the generation status, and the cards changing to **Found in Pool**. Keep the pointer visible and avoid opening unrelated panels. Suggested format: **MP4 or WebM**, 16:9, 1080p.

## Choose a generation method

| Method | Best for | What you must verify |
|---|---|---|
| **From Template** | Common packages and familiar parts with a clear pin count | Selected schematic template, footprint template, package variant, and pin count |
| **From Datasheet** | ICs, connectors, uncommon packages, or any uncertain pinout | Datasheet revision, extracted pin table, dimensions, pitch, pad sizes, and orientation |

When WireFrame reports that it is not confident about the pinout, stop template generation and use the manufacturer's datasheet.

## Generate from a template

This is the faster option and should be the first choice for standard resistors, capacitors, headers, common IC packages, and other parts with an unambiguous physical form.

1. Open the **From Template** tab.
2. Add a short description when the component name does not fully identify its function or package.
3. Select **Research & Select Template**.
4. Read the AI recommendation.
5. Check **PCB Template**, **SCH Template**, and **Pin Count**.
6. Correct any field that does not match the exact part.
7. Select **Generate from Template**.
8. If the recommendation is wrong, update the description and select **Retry Research**.

WireFrame prefers a matching verified library footprint when one is available. Otherwise, it builds from the selected template.

### Image — Review the template recommendation

!!! note "Image needed"
    Capture the **AI Component Generator → From Template** tab after research has completed. Show the target component, recommendation summary, **PCB Template**, **SCH Template**, **Pin Count**, **Generate from Template**, and **Retry Research**. If possible, use an example with a confident recommendation. Suggested size: **1000 × 740 px**.

### Image — Low-confidence pinout warning

!!! note "Image needed"
    Capture the amber **AI not confident about the pinout** state with a generic symbol recommendation. The image must also show the guidance to use **From Datasheet** or retry research. Suggested size: **1000 × 500 px**.

## Generate from a datasheet

Use this method when pin numbers or mechanical dimensions cannot be safely inferred from the component name.

1. If possible, complete **Research & Select Template** first so WireFrame has an expected package and pin count.
2. Open the **From Datasheet** tab.
3. Select **Browse File**.
4. Attach the manufacturer's PDF datasheet or a clear image of the relevant pinout and mechanical drawing.
5. Confirm that the file shown in the dialog is the correct revision.
6. Select **Generate from Datasheet**.
7. Wait for extraction and generation to finish. You may select **Close (keeps running)** without cancelling the active request.

For a PDF, WireFrame looks for pinout and mechanical sections and uses the relevant text and drawing pages. A clean manufacturer PDF normally produces a more reliable result than a distributor screenshot or a scanned document.

!!! info "Datasheet privacy"
    Datasheet text and relevant images are sent to the configured AI provider for analysis. Do not attach confidential, licensed, or export-controlled documents unless your organization permits that use.

### Short video — Create a component from a datasheet

!!! note "Short video needed"
    Record **12–18 seconds** showing the **From Datasheet** tab, attaching a public manufacturer PDF, selecting **Generate from Datasheet**, and the visible progress states. End when generation completes and Component Review refreshes. Do not expose local usernames, private file paths, API keys, or confidential documents. Suggested format: **MP4 or WebM**, 16:9, 1080p.

## Review the generated component

After successful generation, WireFrame saves the symbol and footprint to the writable project library, refreshes the library pool, and updates the component card. Do not continue to placement until the symbol, footprint, and pin count agree.

Review these items against the datasheet:

### Symbol checklist

- every physical pin is present;
- pin numbers and names match the exact package variant;
- power, ground, input, output, and passive electrical types are appropriate;
- hidden or stacked power pins still represent real package pins;
- the reference prefix and component value are appropriate;
- no-connect and exposed-pad requirements are understood.

### Footprint checklist

- pad count matches the symbol's physical pin count;
- pad numbering and pin-1 orientation match the datasheet;
- surface-mount or through-hole technology is correct;
- pitch, row spacing, drill size, and pad dimensions match the recommended land pattern;
- thermal or exposed pads are present when required;
- silkscreen, courtyard, and body outline do not obscure pads or violate assembly clearance.

Select **Manage** on the component card to inspect or correct the generated symbol and footprint in the library editors. Save your changes, then let Component Review re-check the library assignment.

### Image — Inspect the generated symbol and footprint

!!! note "Image needed"
    Use a two-panel composite or two clearly labeled screenshots: **Generated symbol review** and **Generated footprint review**. Show matching pin/pad numbers, the pin-1 marker, package outline, and editor properties. Use a real example with at least eight pins. Suggested combined size: **1400 × 800 px**.

## Confirm generated library knowledge

WireFrame records an electrical description for a generated symbol as unverified library knowledge. In **Library Pool Settings**, confirm it only after you have checked the stated rules against the manufacturer datasheet.

Do not confirm a record merely because the symbol looks correct. Confirmation means you accept the pin behavior and electrical constraints for later design checks.

### Image — Confirm an AI-generated library contract

!!! note "Image needed"
    Capture **Library Pool Settings → Locally written contracts** with one unverified generated part expanded. Include the source/status text and the **Confirm**, **Revoke**, and **Forget** actions. Do not show private library paths. Suggested size: **1100 × 650 px**.

## Troubleshooting

| Message or result | What to do |
|---|---|
| **AI not confident about the pinout** | Attach the exact manufacturer datasheet instead of using a generic template |
| **No file attached** | Add a PDF, PNG, or JPG in **From Datasheet** |
| **No writable project library directory** | Save or open the project and configure a writable project library location |
| **Another AI generation request is already running** | Wait for the active component to finish before starting another |
| Wrong package or pad count | Correct the package and pin count, then retry; do not resize the result by eye |
| Generation request failed | Check the AI connection and account allowance, then retry with a smaller or clearer input |
| Generated part is found but still shows a mismatch | Open **Manage**, compare symbol pins with footprint pads, save corrections, and re-check the library pool |

## Release checklist

Before using an AI-generated component in a release design:

- record the exact manufacturer part number and datasheet revision;
- complete both symbol and footprint checklists;
- run ERC after placing the symbol;
- run DRC and DFM after placing the footprint;
- inspect pin 1 and package orientation in the 3D or assembly view;
- have another reviewer check safety-critical, high-voltage, RF, power, or fine-pitch parts.

## See also

- [AI Design Agent](design-agent.md) — review the generated BOM and missing library items.
- [Symbol Library Editor](../libraries/symbol-creator.md) — correct or create a symbol manually.
- [Footprint Libraries](../libraries/footprints-library.md) — inspect and edit footprint definitions.
- [DFM and DRC](../pcb/dfm-and-drc.md) — verify the board before release.
