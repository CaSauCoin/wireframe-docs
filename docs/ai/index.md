# AI Copilot

AI Copilot helps turn a circuit request into a reviewable design, inspect an existing schematic or PCB, organize functional blocks, generate missing library items, and explain simulation results. It assists the workflow; it does not replace datasheet review, ERC, DRC, DFM, or engineering approval.

## Configure AI access

1. Open **Preferences → AI**, or open the Copilot menu and select **AI settings**.
2. Enter your OpenRouter API key.
3. Select an allowed model.
4. Save the settings.
5. Open **View → AI Copilot Chat**.

The current release uses a locally configured, user-provided OpenRouter key. Do not place that key in screenshots, project files, bug reports, or shared configuration examples.

### Image — AI settings

!!! note "Image needed"
    Capture the current AI provider settings with the key value hidden. Show the provider/model controls and save action. Do not use the older screenshot placeholder that shows a different header or input text. Suggested size: **900 × 620 px**.

## Start a focused session

Use the **+** control to create a session and the history control to reopen earlier project sessions. Describe one goal at a time and include measurable requirements where possible.

Good starting requests include:

- “Design a 12 V to 5 V buck supply for a 1 A load.”
- “Review the USB-C power input and protection block on this schematic.”
- “Explain the failed `VOUT` ripple assertion from the latest simulation.”
- “Group this sheet into power, control, and interface blocks.”

Long sessions are summarized and relevant project facts can be recalled later. Still restate safety-critical values before asking Copilot to modify or verify a design.

### Short video — Start and reopen a Copilot session

!!! note "Video needed"
    Record **10–15 seconds** showing **View → AI Copilot Chat**, creation of a new session, one short request, opening History, and returning to the session. Do not expose an API key or private project data. 1080p.

## Design workflow

### Diagram — AI design review workflow

!!! note "Diagram replacement needed"
    Create a polished release diagram showing: requirement and constraints → clarification → component and connection review → missing-item generation when needed → deterministic verification → user-approved apply. The older four-step image omitted review and simulation gates and must not be reused.

1. Describe the circuit and constraints.
2. Review the research summary.
3. Answer clarifying questions or select **Skip (Use Defaults)** only when the defaults are acceptable.
4. Review BOM components, connections, and functional blocks.
5. Resolve missing symbols, footprints, and pin-count mismatches.
6. Run **Netlist Check**, simulation, and design analysis.
7. Add approved blocks or create the AI project.
8. Inspect the schematic before updating a PCB.

## Component Review tabs

| Tab | Use it for |
|---|---|
| **BOM Components** | Check part number, value, package, origin, and library status |
| **Connections Netlist** | Review named connections and pin references |
| **Blocks** | Generate and review functional circuit groups |
| **Local Pool Settings** | Add library sources and review generated contracts |
| **Simulate & Verify** | Run simulation checks for the proposed design |
| **Design Analysis** | Review design-level findings |
| **Netlist Check** | Find pin, connectivity, and consistency problems |

### Image — Current Component Review tabs

!!! note "Image needed"
    Capture the full Component Review tab row from the current build, with **BOM Components** selected and at least one component card visible. This replaces older media showing only BOM, Netlist, and Placement Preview. Suggested size: **1400 × 820 px**.

## Safety and privacy

- AI requests and attached datasheet content are sent to the configured provider.
- Review every proposed change before applying it.
- Treat generated symbols and footprints as unverified until checked against the datasheet.
- Limit each request to the relevant sheet, block, or signal.
- Re-run deterministic checks after every accepted change.
- Stop and review when part numbers, package variants, ratings, or pinouts are ambiguous.

## Continue learning

- [AI Design Agent](design-agent.md)
- [AI Component Generator](component-generator.md)
- [Placement and Routing Assistant](auto-placer-router.md)
- [Review and Simulation Guide](../ai-copilot.md)
- [AI-Assisted Design Tutorial](../tutorial/ai-design.md)
