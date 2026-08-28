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

### Image — Clarifying questions

!!! note "Image needed"
    Capture the actual clarification UI with two or three questions and the current **Proceed to Design** and **Skip (Use Defaults)** buttons. Remove the former ASCII mockup. Suggested size: **1000 × 700 px**.

## Review BOM components

For each physical component:

1. Confirm the exact part name and value.
2. Confirm the package.
3. Read the role and origin indicator.
4. Resolve **Not in Pool**, partial matches, and pin-count mismatches.
5. Use **AI Gen**, **Create**, **Import**, or **Manage** as appropriate.

An item marked **auto** was added by WireFrame support rules. Keep it only when the design actually needs it.

### Image — BOM component review

!!! note "Image needed"
    Capture several current component cards, including one **Found in Pool**, one missing item, and one support-rule item marked **auto**. Show Value, Footprint Package, and contextual actions. Suggested size: **1400 × 900 px**.

## Review connections and netlist checks

Open **Connections Netlist** to inspect named nets and referenced pins. Then open **Netlist Check** and resolve critical findings before placement or simulation.

Pay particular attention to:

- missing or nonexistent pins;
- symbol pin count versus footprint pad count;
- power and ground connectivity;
- single-ended nets that should have more than one connection;
- inconsistent net names.

Use **Fix with AI** only after reading the proposed correction. Re-run the check afterward.

## Generate functional blocks

Open **Blocks** and select **Generate Blocks**. Review the membership and purpose of each power, protection, control, interface, oscillator, or load block. Use **Send Blocks to Chat** when you want Copilot to discuss or refine them.

### Short video — Generate and review functional blocks

!!! note "Video needed"
    Record **12–18 seconds** showing **Blocks**, **Generate Blocks**, the resulting block cards, and **Send Blocks to Chat**. Use a medium-size circuit so at least three blocks appear. 1080p.

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
