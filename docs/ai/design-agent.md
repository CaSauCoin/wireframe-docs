# AI Design Agent

Use AI Design Agent to research a circuit request, clarify requirements, and prepare a BOM, connection plan, and functional blocks for review.

## Prepare the request

Include:

- input and output voltage;
- maximum current or load;
- interfaces and connector requirements;
- size, package, or assembly constraints;
- environmental or safety constraints;
- preferred or prohibited parts;
- the result you expect from simulation.

Avoid requests such as “make a power supply” without ratings. Copilot can ask questions, but it cannot infer product requirements that have not been decided.

## Research and clarification

After receiving the request, review the research summary and answer the displayed clarification questions. Select **Proceed to Design** when the answers are correct. Use **Skip (Use Defaults)** only for exploratory work.

Each question offers one or more choices plus a **Custom** answer field. Selecting **Proceed to Design** submits the visible choices. **Skip (Use Defaults)** replaces the unanswered decisions with WireFrame's defaults; it is not an approval of production requirements.

### Image — Clarifying questions

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the actual clarification UI with two or three questions and the current **Proceed to Design** and **Skip (Use Defaults)** buttons. Remove the former ASCII mockup. Suggested size: **1000 × 700 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Review BOM components

For each physical component:

1. Confirm the exact part name and value.
2. Confirm the package.
3. Read the role and origin indicator.
4. Resolve **Not in Pool**, partial matches, and pin-count mismatches.
5. Use **AI Gen**, **Create**, **Import**, or **Manage** as appropriate.

Left-click a component card, its type tag, or one of its actions to make that item the active preview. The action row changes with library state:

| Component state | Actions | Result |
|---|---|---|
| Found in Pool | **AI Gen**, **Manage**, **Import** | Regenerate, open the matched library editors, or replace the assignment from a KiCad symbol file |
| Not in Pool | **AI Gen**, **Create**, **Import** | Generate with AI, start a new symbol in Symbol Library Editor, or load a `.kicad_sym` file |

Editing **Value** or **Footprint Package** invalidates derived validation, simulation, and placement results. Let the pool re-check finish, then repeat the relevant review tabs.

An item marked **auto** was added by WireFrame support rules. Keep it only when the design actually needs it.

### Image — BOM component review

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture several current component cards, including one **Found in Pool**, one missing item, and one support-rule item marked **auto**. Show Value, Footprint Package, and contextual actions. Suggested size: **1400 × 900 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Review connections and netlist checks

Open **Connections Netlist** to inspect named nets and referenced pins. Then open **Netlist Check** and resolve critical findings before placement or simulation.

Pay particular attention to:

- missing or nonexistent pins;
- symbol pin count versus footprint pad count;
- power and ground connectivity;
- single-ended nets that should have more than one connection;
- inconsistent net names.

Use **Fix with AI** only after reading the proposed correction. Re-run the check afterward.

**Fix with AI** appears when critical deterministic findings remain and is limited to three attempts for that review cycle. It sends the listed critical issues back for regeneration; it does not replace ERC.

## Generate functional blocks

Open **Blocks** and select **Generate Blocks**. Review the membership and purpose of each power, protection, control, interface, oscillator, or load block. Use **Send Blocks to Chat** when you want Copilot to discuss or refine them.

### Short video — Generate and review functional blocks

!!! note "Video production brief"
    1. **Prepare:** Load a reviewed medium-size design that can produce at least three functional blocks.
    2. **Opening shot (1–2 s):** Open **Blocks** and hold on the empty or previous-result state with **Generate Blocks** visible.
    3. **Action shot (6–9 s):** Click **Generate Blocks**, keep one genuine running state, then cut to the completed cards and scan their titles and memberships.
    4. **Result shot (3–4 s):** Click **Send Blocks to Chat** and hold on the confirmation plus the resulting chat cards.
    5. **Deliver:** Export a **12–18 second** 1080p MP4; never hide an unresolved-library warning to make the send action appear successful.

## Verify before applying

1. Resolve library issues.
2. Run **Netlist Check**.
3. Run **Simulate & Verify** when the circuit is supported.
4. Review **Design Analysis**.
5. Add the approved design or block to the active project.
6. Run schematic ERC after placement.

## Revise the design

Ask for one bounded change at a time, such as:

- “Replace the regulator with a 1 A part in SOIC-8.”
- “Add reverse-polarity protection before the input filter.”
- “Correct U2 pin 5 to `EN` and regenerate the affected connection.”

After revision, previous validation, simulation, and placement results may be stale. Re-run them.

## See also

- [AI Component Generator](component-generator.md)
- [Placement and Routing Assistant](auto-placer-router.md)
- [Simulation Workbench](../simulation/index.md)
- [ERC](../schematic/erc.md)
