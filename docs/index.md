---
hide:
  - navigation
  - toc
---

<div class="wf-hero wf-reveal" markdown>

<svg xmlns="http://www.w3.org/2000/svg" class="wf-mark wf-hero-mark" viewBox="12 -18 326 236" aria-hidden="true" focusable="false"><defs><linearGradient id="wf-mark-hero" x1="0%" y1="0%" x2="100%" y2="100%"><stop class="wf-mark-a" offset="0%" stop-color="#00f2ff"/><stop class="wf-mark-b" offset="100%" stop-color="#00ff9d"/></linearGradient></defs><path d="M30 0 L80 200 L130 50 L180 200 L230 50 L230 0 L320 0" fill="none" stroke="url(#wf-mark-hero)" stroke-width="32" stroke-linecap="round" stroke-linejoin="round"/><circle class="wf-mark-via wf-mark-via-a" cx="80" cy="200" r="10" stroke="#00f2ff" stroke-width="6"/><circle class="wf-mark-via wf-mark-via-b" cx="180" cy="200" r="10" stroke="#00ff9d" stroke-width="6"/><circle class="wf-mark-node" cx="30" cy="0" r="14"/><circle class="wf-mark-node" cx="320" cy="0" r="14"/><circle class="wf-mark-node" cx="290" cy="100" r="14"/></svg>

<p class="wf-eyebrow">WireFrame EDA · v1.5.47 guide</p>

# <span class="wf-gradient-text">From idea to a board you can order.</span>

<p class="wf-subtitle">Draw the schematic, check it, simulate it, lay out the PCB and export fabrication files — with an AI Copilot that proposes and never applies on its own.</p>

[:material-rocket-launch: Start learning](learn/index.md){ .md-button .md-button--primary }
[:material-download: Download WireFrame](https://wireframe.com.vn/download){ .md-button }

</div>

## Where do you want to start? { .wf-section-title }

Pick the line that sounds most like you. Each one opens a short path with the pages in order and how long they take.

<div class="grid cards wf-paths" markdown>

-   :material-sprout:{ .lg .middle } **I'm new to PCB design**

    ---

    Learn the screen, then build a small LED board from schematic to Gerber files.

    [:octicons-arrow-right-24: The beginner path](learn/index.md#new-to-pcb-design) · about 1 hour

-   :material-swap-horizontal:{ .lg .middle } **I already use KiCad or Altium**

    ---

    Bring your projects and libraries across and learn what is different here.

    [:octicons-arrow-right-24: The switcher path](learn/index.md#coming-from-kicad-or-altium) · about 30 min

-   :material-robot-outline:{ .lg .middle } **I want AI to help me design**

    ---

    Describe a circuit, review the BOM and connections the Copilot proposes, fix missing parts.

    [:octicons-arrow-right-24: The AI path](learn/index.md#design-with-ai) · about 45 min

-   :material-factory:{ .lg .middle } **I need to send a board to the fab**

    ---

    Design rules, DFM and DRC checks, and a fabrication package that matches one revision.

    [:octicons-arrow-right-24: The release path](learn/index.md#ready-for-manufacturing) · about 30 min

</div>

## Your first hour, step by step { .wf-section-title }

<div class="wf-steps" markdown>

<div class="wf-step wf-reveal" markdown>
<span class="wf-step-num">1</span>

### Install and open WireFrame <small>10 min</small>

Download the build for your system and check that it starts — no account is needed. → [Installation](installation.md)
</div>

<div class="wf-step wf-reveal" markdown>
<span class="wf-step-num">2</span>

### Find your way around <small>10 min</small>

Project tree on the left, editor in the middle, Library and Properties on the right, AI Copilot below. → [User Interface](ui-overview.md)
</div>

<div class="wf-step wf-reveal" markdown>
<span class="wf-step-num">3</span>

### Build your first board <small>30 min</small>

Connector, resistor and LED: schematic, ERC, PCB, routing, DFM. → [Tutorial: A Simple LED Board](tutorial/index.md)
</div>

<div class="wf-step wf-reveal" markdown>
<span class="wf-step-num">4</span>

### Let the Copilot help <small>10 min</small>

Ask for a circuit, then review what it proposes before anything is applied. → [Tutorial: AI-Assisted Design](tutorial/ai-design.md)
</div>

</div>

## What you can do in WireFrame { .wf-section-title }

Eight areas, each with its own guide. The links under each card go straight to the task.

<div class="grid cards wf-tour" markdown>

-   [![Schematic page with its title block](assets/wf/docs/schematic/templates/completed-schematic-title-block.png)](schematic/index.md)

    **Schematic editor**

    Multi-sheet schematics with live connectivity.
    { .wf-tour-lead }

    - [Place parts](schematic/placing-components.md) and fill in their properties
    - [Wires, net labels and power symbols](schematic/wiring-and-nets.md), with net highlighting and Auto Wire
    - [An ERC that names the pin](schematic/erc.md), run before the PCB
    - [Title blocks and sheet templates](schematic/templates.md)

    [Open the guide :octicons-arrow-right-24:](schematic/index.md){ .wf-tour-more }

-   [![A routed board in the PCB editor](assets/wf/docs/pcb/routing/completed-pad-to-pad-route.png)](pcb/index.md)

    **PCB layout**

    From the ratsnest to a routed, poured board.
    { .wf-tour-lead }

    - [Board shape from SVG or DXF](pcb/board-outline.md), or described in chat
    - [Footprints and placement](pcb/footprints-and-placement.md)
    - [Tracks, vias, length tuning and differential pairs](pcb/routing.md)
    - [Zones and planes](pcb/zones-and-planes.md), [design rules and net classes](pcb/design-rules.md)

    [Open the guide :octicons-arrow-right-24:](pcb/index.md){ .wf-tour-more }

-   [![The SPICE Simulation Workbench](assets/wf/docs/simulation/running-simulation/current-simulation-workbench.png)](simulation/index.md)

    **Simulation**

    SPICE in a simulation file of its own.
    { .wf-tour-lead }

    - [Copy a block of a sheet](simulation/index.md#get-a-simulation) into a `.simxml`
    - [Transient, AC, DC sweep and operating point](simulation/running-simulation.md) on ngspice, Xyce or LTspice
    - [Waveforms measured with A/B cursors](simulation/waveform-viewer.md)
    - [Testbench checks](simulation/testbenches-and-measurements.md): Pass, Fail or Not measured

    [Open the guide :octicons-arrow-right-24:](simulation/index.md){ .wf-tour-more }

-   [![AI Component Review of a planned BOM](assets/wf/docs/ai/design-agent/bom-component-review.png)](ai/index.md)

    **AI Copilot**

    Describe a circuit, then review what it proposes.
    { .wf-tour-lead }

    - [Plan a design](ai/design-agent.md): BOM, connections and blocks, card by card
    - [Fix or create a part](ai/component-generator.md) with `/fix` and its datasheet
    - [Commands for every panel](ai/commands.md) — type ++slash++ in the chat
    - [Datasheets, repairs and project memory](ai/datasheets-and-memory.md)

    [Open the guide :octicons-arrow-right-24:](ai/index.md){ .wf-tour-more }

-   [![Local Library Manager](assets/wf/docs/libraries/library-converter/local-library-manager-overview.png)](libraries/library-converter.md)

    **Libraries**

    KiCad and Altium libraries, and your own.
    { .wf-tour-lead }

    - [Add KiCad folders or files, convert Altium](libraries/library-converter.md) in place
    - [Library Workspace](libraries/library-workspace.md): edit and audit parts with the Copilot
    - [Symbol editor](libraries/symbol-creator.md) and the [footprint library](libraries/footprints-library.md)
    - [How a part is found](libraries/how-parts-are-found.md) for every BOM row

    [Open the guide :octicons-arrow-right-24:](libraries/library-converter.md){ .wf-tour-more }

-   [![DFM and DRC results](assets/wf/docs/pcb/dfm-and-drc/dfm-and-drc-results.png)](pcb/dfm-and-drc.md)

    **Checks and fabrication**

    Check the board, then send it to be made.
    { .wf-tour-lead }

    - [DFM and DRC](pcb/dfm-and-drc.md), each violation located on the board
    - [One fabrication package](pcb/fabrication-and-export.md#the-fabrication-package): Gerber X2, drill, BOM, pick-and-place
    - [Check the Gerbers before ordering](pcb/fabrication-and-export.md#check-the-gerbers-before-ordering)
    - Schematic PDF and a 1:1 PCB print

    [Open the guide :octicons-arrow-right-24:](pcb/fabrication-and-export.md){ .wf-tour-more }

-   [![The 3D viewer](assets/wf/docs/advanced/3d-viewer/3d-viewer.png)](advanced/3d-viewer.md)

    **3D viewer**

    See the board before you order it.
    { .wf-tour-lead }

    - [Orbit, pan and zoom](advanced/3d-viewer.md#camera-controls) around the board
    - Parts drawn from their STEP or OBJ models; [assign a missing model](advanced/3d-viewer.md#assigning-3d-models-to-footprints)
    - [Bottom-side parts](advanced/3d-viewer.md#bottom-side-components) on the other face
    - Heights, clearances and connector positions at a glance

    [Open the guide :octicons-arrow-right-24:](advanced/3d-viewer.md){ .wf-tour-more }

-   [![A board fitted to its case and lid](assets/wf/docs/advanced/enclosure-and-assembly/board-fit-with-a-case-and-lid.png)](advanced/enclosure-and-assembly.md)

    **Enclosure and multi-board**

    Fit the board to its case; build products of several boards.
    { .wf-tour-lead }

    - [Board Fit](advanced/enclosure-and-assembly.md#board-fit): a board cut out of a case, frame or standard outline
    - Holes, keepouts and the parts the lid pins in place
    - [Stacks of boards](advanced/enclosure-and-assembly.md#stacks-of-boards) on their spacers
    - [System](advanced/enclosure-and-assembly.md#system-products-made-of-several-boards): boards connected pin by pin, checked across

    [Open the guide :octicons-arrow-right-24:](advanced/enclosure-and-assembly.md){ .wf-tour-more }

</div>

!!! warning "One rule for everything automatic"
    AI proposals, imported libraries, automatic placement and routing, and simulation results are all **proposals**. Check part numbers, pin mapping, package geometry, model assumptions and design rules before you release a board.

<div class="wf-help" markdown>
**Stuck?** Search this guide with ++slash++ or ++s++, read the [FAQ & Troubleshooting](faq.md), or see the [keyboard shortcuts](advanced/shortcuts.md).
</div>
