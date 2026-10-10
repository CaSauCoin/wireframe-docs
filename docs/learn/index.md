---
hide:
  - toc
---

# Learning paths

Not sure what to read first? Choose the path that matches you. Each one lists the pages **in order**, how long each takes, and what you will be able to do at the end. Tick the boxes as you go — they are just for you.

=== ":material-sprout: New to PCB design"

    ## New to PCB design

    You have never drawn a schematic or a board, or it has been a while. About **1 hour**.

    <div class="wf-path" markdown>

    - [ ] **[Install WireFrame](../installation.md)** <small>10 min</small> — download, install, first launch.
    - [ ] **[Getting started](../getting-started.md)** <small>10 min</small> — create a project, add a schematic and a PCB.
    - [ ] **[The user interface](../ui-overview.md)** <small>5 min</small> — what every panel is for.
    - [ ] **[Placing components](../schematic/placing-components.md)** and **[Wiring & nets](../schematic/wiring-and-nets.md)** <small>10 min</small>
    - [ ] **[Tutorial: A Simple LED Board](../tutorial/index.md)** <small>25 min</small> — the whole flow on one small board.
    - [ ] **[ERC](../schematic/erc.md)** and **[DFM & DRC](../pcb/dfm-and-drc.md)** <small>5 min</small> — read the checks before you trust a board.

    </div>

    !!! success "At the end you can"
        draw a small circuit, check it, turn it into a PCB, route it, and export files a manufacturer accepts.

=== ":material-swap-horizontal: Coming from KiCad or Altium"

    ## Coming from KiCad or Altium

    You know EDA; you want your work across and the differences. About **30 minutes**.

    <div class="wf-path" markdown>

    - [ ] **[Projects & files](../projects.md)** <small>5 min</small> — `.prjxml`, `.schxml`, `.pcbxml`, and importing a KiCad project.
    - [ ] **[Library import & management](../libraries/library-converter.md)** <small>10 min</small> — KiCad folders, Altium `.SchLib` / `.PcbLib` / `.IntLib`.
    - [ ] **[Keyboard shortcuts](../advanced/shortcuts.md)** <small>5 min</small> — the keys that differ from what your hands expect.
    - [ ] **[Selection, context menus & popups](../advanced/selection-and-editing.md)** <small>5 min</small>
    - [ ] **[Design rules & net classes](../pcb/design-rules.md)** <small>5 min</small>

    </div>

    !!! success "At the end you can"
        open an existing KiCad design in WireFrame, reuse your libraries, and work at your usual speed.

=== ":material-robot-outline: Design with AI"

    ## Design with AI

    You want the Copilot to draft a circuit and you want to know how to review it. About **45 minutes**.

    <div class="wf-path" markdown>

    - [ ] **[AI overview](../ai/index.md)** <small>10 min</small> — settings, sessions, what the Copilot can and cannot change.
    - [ ] **[Tutorial: AI-Assisted Design](../tutorial/ai-design.md)** <small>20 min</small> — an NE555 blinker from a one-line request.
    - [ ] **[AI Design Agent](../ai/design-agent.md)** <small>5 min</small> — the Component Review tabs, card by card.
    - [ ] **[Fix or Create a Component](../ai/component-generator.md)** <small>5 min</small> — when a part is not in your library.
    - [ ] **[Review & simulation guide](../ai-copilot.md)** <small>5 min</small> — what to verify before you apply.

    </div>

    !!! success "At the end you can"
        turn a written requirement into a reviewed BOM and schematic, and tell a sound proposal from a risky one.

=== ":material-factory: Ready for manufacturing"

    ## Ready for manufacturing

    The design is done; you need a clean, consistent release. About **30 minutes**.

    <div class="wf-path" markdown>

    - [ ] **[Design rules & net classes](../pcb/design-rules.md)** <small>5 min</small>
    - [ ] **[Zones & planes](../pcb/zones-and-planes.md)** <small>5 min</small>
    - [ ] **[DFM & DRC check](../pcb/dfm-and-drc.md)** <small>10 min</small> — resolve every blocking error, justify every warning.
    - [ ] **[Fabrication & export](../pcb/fabrication-and-export.md)** <small>10 min</small> — Gerber, drill, BOM and their inventory.

    </div>

    !!! success "At the end you can"
        hand a manufacturer a package where every file belongs to the same saved board revision.

=== ":material-sine-wave: Simulate a circuit"

    ## Simulate a circuit

    You want to know a circuit works before it is built. About **30 minutes**.

    <div class="wf-path" markdown>

    - [ ] **[Simulation workbench](../simulation/index.md)** <small>5 min</small>
    - [ ] **[Engines & SPICE models](../simulation/engines-and-models.md)** <small>10 min</small> — every part needs a model.
    - [ ] **[Running a simulation](../simulation/running-simulation.md)** <small>5 min</small> — blocks, preflight, run.
    - [ ] **[Testbenches & measurements](../simulation/testbenches-and-measurements.md)** <small>5 min</small>
    - [ ] **[Waveform viewer](../simulation/waveform-viewer.md)** <small>5 min</small> — signals and A/B cursors.

    </div>

    !!! success "At the end you can"
        run a simulation on a block of your schematic and measure the result instead of eyeballing it.

---

**Done with a path?** The [FAQ & Troubleshooting](../faq.md) page collects the questions people ask next.
