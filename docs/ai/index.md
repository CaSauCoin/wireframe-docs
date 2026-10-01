# AI Copilot

AI Copilot helps turn a circuit request into a reviewable design, inspect an existing schematic or PCB, organize functional blocks, generate missing library items, and explain simulation results. It assists the workflow; it does not replace datasheet review, ERC, DRC, DFM, or engineering approval.

## Configure AI access

Open **Preferences → AI Assistant**, or open the Copilot menu and select **AI settings...**. WireFrame speaks one protocol to every provider (an OpenAI-style `/chat/completions` endpoint), so the setup is an endpoint, the model ids it serves, and a key when the endpoint bills per token.

1. Under **API Endpoint**, pick a preset or type an endpoint URL.
2. If the endpoint is a hosted provider, paste its key under **API Key**. Local endpoints have no key field.
3. Fill **Design model** and **Fast model**. Use **List** beside each field to ask the endpoint which ids it serves.
4. Select **Test** (hosted) or **Check server** (local) and wait for the status line.
5. Open **View → AI Copilot Chat**.

| Preset | What it configures | Key |
|---|---|---|
| **OpenRouter** | `https://openrouter.ai/api/v1` with `google/gemini-2.5-pro` (design) and `google/gemini-2.5-flash` (fast) | Required |
| **agyserve** | A local bridge to the Antigravity CLI on port 8799, so calls are covered by that subscription instead of per token | None |

A preset sets the endpoint **and** its model ids together. Model ids are not portable between providers: `google/gemini-2.5-flash` on OpenRouter is not a valid id on a local server. If you switch endpoints by hand, press **List** and pick ids from the new endpoint; WireFrame warns when a hosted-provider id (one containing `/`) is paired with a local endpoint.

### Two model tiers

| Field | Used for |
|---|---|
| **Design model** | Planning the BOM and netlist, repairing findings, generating library parts, reviewing a board — the model that decides circuits |
| **Fast model** | Request routing, project naming, requirement research, board questions — classification and summaries. Leave it empty to use the design model |

The fast tier can also use its own endpoint (**Fast tier endpoint**). A common split is the design tier on one provider and the fast tier on another, for example routine calls on **agyserve** while design calls stay on a hosted model.

### Local endpoints and agyserve

The line **Requests go to …** under the fields shows where requests are sent and whether they are billed per token or stay on this machine.

For **agyserve**, WireFrame starts the bridge in the background on the first request when port 8799 is offline. If **Check server** still fails, start it yourself from a WireFrame source checkout with `python3 Tools/agyserve/server.py`, then check again. Expect 20–30 seconds per request — slower than a hosted provider.

Keys are stored in the local WireFrame configuration. Do not place a key in screenshots, project files, bug reports, or shared configuration examples.

### Image — AI settings

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture **Preferences → AI Assistant** with the key value hidden. Show the endpoint presets, the **Design model** and **Fast model** fields, and the **Requests go to** status line. Do not use the older screenshot placeholder that shows a different header or input text. Suggested size: **900 × 620 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Start a focused session

Use the **+** control to create a session and the history control to reopen earlier project sessions. Describe one goal at a time and include measurable requirements where possible.

Good starting requests include:

- “Design a 12 V to 5 V buck supply for a 1 A load.”
- “Review the USB-C power input and protection block on this schematic.”
- “Explain the failed `VOUT` ripple assertion from the latest simulation.”
- “Group this sheet into power, control, and interface blocks.”

Long sessions are summarized and relevant project facts can be recalled later. Still restate safety-critical values before asking Copilot to modify or verify a design.

### Short video — Start and reopen a Copilot session

!!! note "Video production brief"
    1. **Prepare:** Open a fictional sample project and prewrite a short non-sensitive prompt for pasting.
    2. **Opening shot (1–2 s):** Start on the workspace with the **View** menu closed.
    3. **Action shot (6–9 s):** Open **View → AI Copilot Chat**, create a session, paste and submit the request, then open **History** and select the same session.
    4. **Result shot (2–3 s):** Hold on the reopened conversation with its session identity and request visible.
    5. **Deliver:** Export a **10–15 second** 1080p MP4; remove waiting time and reveal no API key or private project data.

## Design workflow

### Diagram — AI design review workflow

!!! note "Diagram production brief"
    1. **Prepare:** Copy the exact workflow stages and review gates from this page into a vector design file.
    2. **Build the content:** Create a polished release diagram showing: requirement and constraints → clarification → component and connection review → missing-item generation when needed → deterministic verification → user-approved apply. The older four-step image omitted review and simulation gates and must not be reused.
    3. **Compose:** Arrange the stages left to right, use one consistent shape system, and make review or correction loops visually distinct.
    4. **Finish:** Verify every label manually; do not use ASCII art, a Mermaid screenshot, or AI-generated text inside the graphic.
    5. **Deliver and approve:** Export SVG plus a 2× PNG fallback, then confirm readability at the documentation embed width.

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
| **Board Fit** | Board shape, enclosure, stacks, and whether the BOM fits — see [Enclosure Fit and Multi-Board Products](../advanced/enclosure-and-assembly.md) |
| **System** | Products made of several boards (`.asmxml`): stacking and board-to-board wiring checks |

### Image — Current Component Review tabs

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the full Component Review tab row from the current build, with **BOM Components** selected and at least one component card visible. This replaces older media showing only BOM, Netlist, and Placement Preview. Suggested size: **1400 × 820 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Safety and privacy

- AI requests and attached datasheet content are sent to the configured endpoint. With a hosted provider that means a third-party service; with a local endpoint such as agyserve, to the service that endpoint forwards to.
- Review every proposed change before applying it.
- Treat generated symbols and footprints as unverified until checked against the datasheet.
- Limit each request to the relevant sheet, block, or signal.
- Re-run deterministic checks after every accepted change.
- Stop and review when part numbers, package variants, ratings, or pinouts are ambiguous.

## Continue learning

- [Copilot Commands](commands.md)
- [Datasheets, Repairs and Project Memory](datasheets-and-memory.md)
- [AI Design Agent](design-agent.md)
- [AI Component Generator](component-generator.md)
- [Placement and Routing Assistant](auto-placer-router.md)
- [Review and Simulation Guide](../ai-copilot.md)
- [AI-Assisted Design Tutorial](../tutorial/ai-design.md)
