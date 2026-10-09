# Running a Simulation

Use the Simulation Workbench to select a supported circuit scope, configure the engine and analysis, prepare sources and loads, run preflight, and inspect results.

## Open the workbench

With a schematic active, select **Simulation → SPICE Simulation Panel** or press **F5**.

The current sidebar contains:

- **Setup**;
- **Blocks**;
- **Testbench**;
- **Signals**;
- **Models**;
- **AI**.

Older documentation referring to a separate Analysis tab or a different sidebar layout has been removed.

### Image — Current Simulation Workbench

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the complete workbench with the current six sidebar tabs, the waveform area, and run controls visible. Use a small circuit with at least one selectable block and signal. Suggested size: **1600 × 900 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

<!-- wf:shot id=current-simulation-workbench
caption: The Simulation Workbench after a transient run of the NE555 blinker
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- ensure_schematic
- wait: 1
- keys:
  - F5
- wait: 2
- click_at:
  - 385
  - 760
- wait: 1
- action:
    action: mouse_move_to
    x: 240
    y: 600
- scroll: -3
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/##DC
    text: '9'
- keys:
  - Tab
- click_at:
  - 430
  - 112
- wait: 0.5
- click: //##Combo_00/{fa:wave-square} Transient (.tran)
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/##StopTime
    text: '3000'
- keys:
  - Tab
- type:
    ref: //SPICE Circuit Simulation & Analysis/##TimeStep
    text: '1'
- keys:
  - Tab
- wait: 0.5
- click_at:
  - 489
  - 112
- wait: 12
- action:
    action: mouse_move_to
    x: 1000
    y: 12
brief_sha256: 4df8cf3781bdb558
-->
<!-- wf:out id=current-simulation-workbench sha=0812c6f13f55 -->
![The Simulation Workbench after a transient run of the NE555 blinker](../assets/wf/docs/simulation/running-simulation/current-simulation-workbench.png)
<!-- /wf:out -->

## 1. Select an engine and analysis

In **Setup**:

1. Select an available simulation engine.
2. Choose the analysis type.
3. Set its values, such as transient stop time and step.
4. Add any required SPICE directives.

Configure external engine paths in **Preferences → Simulation**. A release build normally includes or locates Ngspice; alternative engines must be installed and selected explicitly.

## 2. Choose the circuit scope

Open **Blocks** and select:

- **Entire schematic**; or
- one or more recognized functional blocks.

Use **Only runnable** to select blocks with enough models and connectivity for simulation. Read the reason shown for any block that is not runnable.

### Short video — Select runnable simulation blocks

!!! note "Video production brief"
    1. **Prepare:** Use a schematic with at least two runnable blocks and one unsupported block with a readable reason.
    2. **Opening shot (1–2 s):** Show the initial block list and scope summary.
    3. **Action shot (5–8 s):** Click **Re-scan**, enable **Only runnable**, select two blocks, then briefly reveal the unsupported reason before filtering if needed.
    4. **Result shot (2–3 s):** Hold on the updated two-block scope summary.
    5. **Deliver:** Export a **10–15 second** 1080p MP4; do not remove the unsupported block merely to make the demo pass.

<!-- wf:video id=select-runnable-simulation-blocks
caption: 'Blocks tab: Re-scan, keep only runnable blocks, select them'
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- ensure_schematic
- wait: 1
- keys:
  - F5
- wait: 2
- click_at:
  - 385
  - 760
- wait: 1
- action:
    action: mouse_move_to
    x: 240
    y: 600
- scroll: -3
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/##DC
    text: '9'
- keys:
  - Tab
- click_at:
  - 430
  - 112
- wait: 0.5
- click: //##Combo_00/{fa:wave-square} Transient (.tran)
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/##StopTime
    text: '3000'
- keys:
  - Tab
- type:
    ref: //SPICE Circuit Simulation & Analysis/##TimeStep
    text: '1'
- keys:
  - Tab
- wait: 0.5
- tab: Blocks
- wait: 1
- action:
    action: mouse_move_to
    x: 1000
    y: 12
steps:
- wait: 1
- click: //SPICE Circuit Simulation & Analysis/{fa:sync} Re-scan
- wait: 1.5
- click: //SPICE Circuit Simulation & Analysis/Only runnable
- wait: 1.5
- click: //SPICE Circuit Simulation & Analysis/Select all
- wait: 2
brief_sha256: c43a8bf5e8ebb61f
-->
<!-- wf:out id=select-runnable-simulation-blocks sha=60c12550bd79 -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/simulation/running-simulation/select-runnable-simulation-blocks.mp4" title="Blocks tab: Re-scan, keep only runnable blocks, select them"></video>
<!-- /wf:out -->

## 3. Add sources and loads

In **Setup**, add sources to the intended nets. In **Testbench**, add loads and assertions.

Check source polarity, units, waveform parameters, and reference ground. A source added to the wrong net can produce a plausible but irrelevant waveform.

## 4. Run preflight

Select **Simulation → Pre-flight Validation Checklist** before running.

Resolve blockers such as:

- missing ground;
- missing or incompatible SPICE models;
- invalid source or analysis values;
- disconnected required pins;
- unsupported selected blocks;
- engine not found.

Warnings require review even when the Run action remains available.

## 5. Select signals

Open **Signals** and select the nets to plot. Use **Named nets** for a concise view or **All** when investigating an unknown issue. Too many traces can make the plot difficult to read.

## 6. Run and inspect

Start the simulation and wait for **Last run** to update. Review:

- completion status;
- assertion results;
- simulation log;
- selected waveform traces;
- cursor measurements when required.

If the run fails, open **AI** and use **Why did the last run fail?** or **Review preflight blockers**, then verify the explanation against the log and circuit.

### Short video — Preflight, run, and inspect

!!! note "Video production brief"
    1. **Prepare:** Load a small runnable circuit with a validated engine, models, and two useful signals.
    2. **Opening shot (2 s):** Show the ready scope and run controls before preflight.
    3. **Action shot (7–10 s):** Run preflight, hold on its success, select both signals, and start the simulation. Cut only inactive compute time.
    4. **Result shot (4–5 s):** Hold on both waveform traces and the **Last run** result in the same final view.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and replace clips containing obsolete controls.

<!-- wf:video id=preflight-run-and-inspect
caption: Preflight checks every part's SPICE model, then Run Simulation draws the waveforms
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- ensure_schematic
- wait: 1
- keys:
  - F5
- wait: 2
- click_at:
  - 385
  - 760
- wait: 1
- action:
    action: mouse_move_to
    x: 240
    y: 600
- scroll: -3
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/##DC
    text: '9'
- keys:
  - Tab
- click_at:
  - 430
  - 112
- wait: 0.5
- click: //##Combo_00/{fa:wave-square} Transient (.tran)
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/##StopTime
    text: '3000'
- keys:
  - Tab
- type:
    ref: //SPICE Circuit Simulation & Analysis/##TimeStep
    text: '1'
- keys:
  - Tab
- wait: 0.5
steps:
- wait: 1
- click_at:
  - 580
  - 112
- wait: 3
- click: //Simulation Models & Preflight/{fa:play} Run Simulation
- wait: 8
brief_sha256: 103b64d4f5cf5014
-->
<!-- wf:out id=preflight-run-and-inspect sha=a38233eb8d2c -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/simulation/running-simulation/preflight-run-and-inspect.mp4" title="Preflight checks every part&#x27;s SPICE model, then Run Simulation draws the waveforms"></video>
<!-- /wf:out -->

## Stop or repeat a run

Stop an active run only when required. After changing component values, source settings, models, scope, or analysis parameters, run preflight again before comparing results.

## Common failures

| Result | Check |
|---|---|
| Engine unavailable | **Preferences → Simulation** engine path and executable |
| No runnable blocks | Models, ground, connectivity, and block reasons |
| Empty waveform | Selected signals and completed analysis |
| Flat output | Source waveform, ground reference, operating point, and load |
| Assertion not measured | Signal selection, analysis window, and assertion metric |
| Different engines disagree | Dialect, model version, sources, load, and analysis settings |

## See also

- [Simulation Workbench](index.md)
- [Testbenches and Measurements](testbenches-and-measurements.md)
- [Simulation Engines and Models](engines-and-models.md)
- [Waveform Viewer](waveform-viewer.md)
