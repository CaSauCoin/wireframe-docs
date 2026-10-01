# Tutorial: AI-Assisted Circuit Design

This tutorial uses AI Copilot to prepare a small NE555 LED blinker, review its proposed design, resolve missing library assets, and verify measurable behavior. AI output remains a proposal until you review and validate it.

### Image — Finished AI-assisted example

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the final schematic, routed PCB, and AI Copilot panel in one v1.5.47 workspace. Use a sample project and ensure no API key or private path is visible.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Before you start

You need a new project, an AI endpoint configured in **Preferences → AI Assistant** (an OpenRouter key, or the local agyserve preset), suitable component libraries, and at least one usable simulation engine. Save the project before starting the request.

## 1. State measurable requirements

Send a prompt such as:

> Design a 9 V NE555 astable LED blinker. Target 1 Hz, use a red LED, include current limiting and supply decoupling, and identify every assumption that needs my confirmation.

Include voltage, frequency, tolerances, package preferences, connector requirements, and board constraints when known. If Copilot asks a question, answer it before accepting a BOM; unanswered choices become risky assumptions.

### Image — Prompt and clarification

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the initial requirement and one clarification exchange in AI Copilot. The prompt must include supply voltage and target frequency.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 2. Review the proposed design

Use the **Component Review** tabs in order:

1. **BOM Components** — verify part identity, value, rating, package, and availability.
2. **Connections Netlist** — compare every NE555 pin and LED polarity with the datasheet.
3. **Blocks** — confirm that timing, output, power, and decoupling functions are present.
4. **Local Pool Settings** — decide which approved local assets may be reused.
5. **Simulate & Verify** — prepare measurable checks.
6. **Design Analysis** and **Netlist Check** — resolve warnings before applying changes.

Do not approve a component merely because its name matches. Package, pin numbering, ratings, and model pin order must also match.

### Image — Component Review tabs

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the complete review window with all seven tabs visible and one BOM item selected. Do not fabricate a separate schematic preview if the release UI does not show one.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 3. Generate a missing component when required

Select **AI Gen** for an unresolved item. Choose **From Template** for a clear standard part, or **From Datasheet** when an exact symbol and package must be derived from manufacturer material.

Before continuing, check pin count, pin names, electrical types, pad numbering, dimensions, pitch, orientation marker, and symbol-to-footprint mapping. Follow the [AI Component Generator guideline](../ai/component-generator.md) for the complete acceptance checklist.

### Short video — Resolve a missing component

!!! note "Video production brief"
    1. **Prepare:** Use a public eight-pin component, an approved public datasheet, and a card marked **Not in Pool**.
    2. **Opening shot (2–3 s):** Hold on the missing card and its **AI Gen** action.
    3. **Action shot (12–18 s):** Open the generator, attach or select the prepared source, start generation, show one real progress state, then cut across the wait.
    4. **Review shot (8–10 s):** Open the generated symbol and footprint, compare pin 1 and at least three readable pin-to-pad numbers, then return to the refreshed card.
    5. **Deliver:** Export a **25–35 second** 1080p MP4; hide the API key, local paths, and any proprietary datasheet content.

## 4. Add explicit simulation requirements

Open **Simulate & Verify** or the Simulation Workbench and define a transient run long enough to show several cycles. Add signals for the output and timing capacitor, then create assertions for the acceptable frequency range and output behavior.

A visual waveform that “looks right” is not a pass criterion. Use the A/B cursors or a measurement to confirm the period, and keep the engine, model revision, sources, loads, and assertion results with the review.

### Image — Measured transient result

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture output and timing-capacitor traces with A/B cursors spanning one period. Show the assertion result and engine used in the same release example where possible.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 5. Apply, place, and route

Apply only the reviewed proposal. Run ERC on the generated schematic, then update the PCB from the active schematic using the current project tool. Review footprint orientation and board constraints before using placement or routing assistance.

After any assisted placement or routing:

- Confirm connectors, controls, indicators, mounting holes, and keepouts are practical.
- Check that every ratsnest connection is resolved intentionally.
- Inspect vias, layer changes, clearances, and return paths.
- Run DFM/DRC and correct every release-blocking violation.

See [Placement and Routing Assistant](../ai/auto-placer-router.md).

### Short video — Review an assisted PCB result

!!! note "Video production brief"
    1. **Prepare:** Keep one assisted PCB proposal ready with a visible, safe manual adjustment still required.
    2. **Opening shot (2–3 s):** Show the proposal and current ratsnest count before approval.
    3. **Action shot (12–18 s):** Apply the proposal, move the chosen footprint or route segment manually, and inspect the remaining ratsnest connections.
    4. **Verification shot (6–9 s):** Run DFM/DRC and hold on the genuine clean summary or clearly explain any remaining issue in-frame.
    5. **Deliver:** Export a **25–35 second** 1080p MP4; the story must show review and correction, never a one-click “fully approved” claim.

## 6. Prepare release output

Save the verified revision, generate the fabrication package, and inspect representative Gerber and drill outputs. Check the BOM, IPC-D-356A, and manifest before archiving the package.

The tutorial is complete only when the schematic, generated library assets, simulation evidence, PCB checks, and fabrication archive all refer to the same saved revision.

## Related guidelines

- [AI Copilot](../ai/index.md)
- [AI Design Agent](../ai/design-agent.md)
- [Running a Simulation](../simulation/running-simulation.md)
- [DFM and DRC](../pcb/dfm-and-drc.md)
- [Fabrication and Export](../pcb/fabrication-and-export.md)
