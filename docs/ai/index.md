# AI Copilot

AI Copilot helps turn a circuit request into a reviewable design, inspect an existing schematic or PCB, organize functional blocks, generate missing library items, and explain simulation results. It assists the workflow; it does not replace datasheet review, ERC, DRC, DFM, or engineering approval.

## Configure AI access

Open **Preferences → AI Assistant**, or the **⋮** menu of the AI Copilot panel → **AI settings...**, and answer one question — **who pays for the AI**:

- **WireFrame credit** — your plan's AI credit; nothing else to set up. The card shows the credit left (1 credit = $0.01 of model use).
- **OpenRouter**, **DeepSeek** or **Google AI** — your own key at that provider, which bills you directly. Paste it, then **Save & test**.

Then choose the **Design model** (plans the BOM and netlist, repairs findings, reviews a board — the one that decides circuits) and the **Fast model** (routing your request, research, board questions). Open **View → AI Copilot Chat** (++ctrl+space++) and start.

Everything about the choices, the plans and what is sent where is on [Models, Credit and Your Data](models-and-credits.md).

## Start a focused session

Use the **+** button in the Copilot panel to start a session and the history button to reopen earlier sessions of the project. Describe one goal at a time and include measurable requirements where possible.

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

<!-- wf:video id=start-and-reopen-a-copilot-session
caption: Start a new session with +, then reopen the NE555 design session from History
project: none
setup:
- pick_folder: tutorials
- menu:
  - File
  - New
  - New Project (.prjxml)...
- wait: 1
- type:
    text: NE555 Blinker
- click_at:
  - 634
  - 485
- wait: 2
- menu:
  - File
  - New
  - New Schematic (.schxml)
- wait: 1
- save_file: tutorials/NE555 Blinker.schxml
- keys:
  - Ctrl
  - S
- wait: 2
- panel: ai
- wait: 1
- type:
    ref: //AI Copilot Panel/##ChatInput
    text: Design a 9 V NE555 astable LED blinker. Target 1 Hz, use a red LED, include current limiting
      and supply decoupling, and identify every assumption that needs my confirmation.
- keys:
  - Enter
- wait_for:
    ref: //AI Copilot Panel/Use all suggestions & continue
    timeout: 580
    scroll_in: //AI Copilot Panel
- action:
    action: mouse_move_to
    x: 1000
    y: 12
steps:
- wait: 1
- click: //AI Copilot Panel/{fa:plus}
- wait: 1.5
- click: //AI Copilot Panel/{fa:history}
- wait: 1.5
- click_at:
  - 140
  - 615
- wait: 3
brief_sha256: 78ff13376c9526fa
-->
<!-- wf:out id=start-and-reopen-a-copilot-session sha=63a468b7e772 -->
<video controls muted playsinline preload="metadata" src="../assets/wf/docs/ai/index/start-and-reopen-a-copilot-session.mp4" title="Start a new session with +, then reopen the NE555 design session from History"></video>
<!-- /wf:out -->

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
3. Answer the clarifying questions, or select **Use all suggestions & continue** only when the suggested answers are acceptable.
4. Review BOM components, connections, and functional blocks.
5. Resolve missing symbols, footprints, and pin-count mismatches.
6. Run **Netlist Check**, simulation, and design analysis.
7. Add approved blocks or create the AI project.
8. Inspect the schematic before updating a PCB.

## Component Review tabs

**Design Plan** in the AI Copilot panel opens the **AI Planned BOM & Schematic Review** window — called *Component Review* in this guide. Its status chips at the top summarise the design (parts bound, nets, enclosure, netlist issues, simulation, analysis); the tabs, in order:

| Tab | Use it for |
|---|---|
| **BOM Components** | Check part number, value, package, origin, and library status |
| **Connections Netlist** | Review named connections and pin references |
| **Blocks** | Generate and review functional circuit groups |
| **Board Fit** | Board shape, enclosure, stacks, and whether the BOM fits — see [Enclosure Fit and Multi-Board Products](../advanced/enclosure-and-assembly.md) |
| **System** | Products made of several boards (`.asmxml`): stacking and board-to-board wiring checks |
| **Netlist Check** | Find pin, connectivity, and consistency problems |
| **Simulate & Verify** | Readiness (components, library match, GND, power source, nets) and **Run Simulation** for the proposed design |
| **Design Analysis** | Review design-level findings |
| **Local Pool Settings** | Add library sources and review generated contracts |

### Image — Current Component Review tabs

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the full Component Review tab row from the current build, with **BOM Components** selected and at least one component card visible. This replaces older media showing only BOM, Netlist, and Placement Preview. Suggested size: **1400 × 820 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

<!-- wf:shot id=current-component-review-tabs
caption: 'The review window: status chips, the tabs, and BOM Components selected'
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- panel: ai
- wait: 2
- click: //AI Copilot Panel/{fa:tasks} Design Plan
- wait: 2
- action:
    action: mouse_move_to
    x: 1000
    y: 12
brief_sha256: cf3dd64d95d11c33
-->
<!-- wf:out id=current-component-review-tabs sha=3f474734b2b3 -->
![The review window: status chips, the tabs, and BOM Components selected](../assets/wf/docs/ai/index/current-component-review-tabs.png)
<!-- /wf:out -->

## Safety and privacy

- A request carries your message and the part of the design it is about (and an attached datasheet's content). It goes through WireFrame's AI service to the model provider you chose — see [what is sent, and where](models-and-credits.md#what-is-sent-and-where). Your projects stay on your computer.
- Review every proposed change before applying it.
- Treat generated symbols and footprints as unverified until checked against the datasheet.
- Limit each request to the relevant sheet, block, or signal.
- Re-run deterministic checks after every accepted change.
- Stop and review when part numbers, package variants, ratings, or pinouts are ambiguous.

## Continue learning

- [Copilot Commands](commands.md)
- [Models, Credit and Your Data](models-and-credits.md)
- [Datasheets, Repairs and Project Memory](datasheets-and-memory.md)
- [AI Design Agent](design-agent.md)
- [Fix or Create a Component](component-generator.md)
- [Placement and Routing Assistant](auto-placer-router.md)
- [Review and Simulation Guide](../ai-copilot.md)
- [AI-Assisted Design Tutorial](../tutorial/ai-design.md)
