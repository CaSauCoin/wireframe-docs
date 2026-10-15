# Running a Simulation

Use the Simulation Workbench to prepare a simulation, configure the engine and analysis, add sources and loads, run preflight, and inspect results.

## Open the workbench

With a simulation (`.simxml`) in front, select **Simulation → SPICE Simulation Panel** or press **F5** — F5 also starts a run. With a sheet of the design in front, the workbench offers **New Simulation** and **Simulate a Block of This Sheet...** instead; see [Get a simulation](index.md#get-a-simulation).

The sidebar contains:

- **Setup**;
- **Blocks**;
- **Testbench**;
- **Signals**;
- **Models**;
- **AI**.

### Image — Current Simulation Workbench

!!! note "Image capture brief"
    1. **Prepare:** Copy the NE555 blinker's block into a simulation, add a 9 V supply, and run a 3 s transient.
    2. **Build the frame:** Capture the whole workbench with the toolbar, the sidebar on **Setup**, and the waveform.
    3. **Clean the frame:** Move the pointer away from key text.
    4. **Approve:** Check the image at 100% zoom for current labels and readable traces.

<!-- wf:shot id=current-simulation-workbench
caption: The Simulation Workbench on the NE555 blinker's simulation after a 3 s transient, with the 9
  V supply under Setup → Sources
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- ensure_schematic
- wait: 1
- keys:
  - F5
- wait: 2
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^.*Simulate a Block of This Sh.*$
    timeout: 3
- wait: 2
- click_match:
    window: Simulate a Block
    pattern: ^.*Copy to New Simulation$
    timeout: 3
- wait: 4
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^[^A-Za-z]* Add$
    timeout: 5
- wait: 1
- action:
    action: mouse_move_to
    x: 240
    y: 600
- scroll: -3
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/**/##DC
    text: '9'
- keys:
  - Tab
- click_at:
  - 350
  - 112
- wait: 0.5
- click: //##Combo_00/{fa:wave-square} Transient (.tran)
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/**/##StopTime
    text: '3000'
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
brief_sha256: a3f4fa3a36ced761
-->
<!-- wf:out id=current-simulation-workbench sha=2e743d936893 -->
![The Simulation Workbench on the NE555 blinker's simulation after a 3 s transient, with the 9 V supply under Setup → Sources](../assets/wf/docs/simulation/running-simulation/current-simulation-workbench.png)
<!-- /wf:out -->

## 1. Select an engine and analysis

In **Setup**:

1. Select an available simulation engine.
2. Choose the analysis type on the toolbar.
3. Set its values, such as transient stop time and step.
4. Add any required SPICE directives under **Testbench → SPICE directives**.

Configure external engine paths in **Preferences → Simulation**. A release build includes ngspice; alternative engines must be installed and selected explicitly.

## 2. Choose the circuits to run

A simulation can hold several independent circuits — a block copied from a sheet is usually one. Open **Blocks** to see them, each with its readiness, and tick the ones to simulate; the netlist is built from those parts alone.

Use **Select all**, **Only runnable** (blocks with enough models and connectivity to simulate), **None**, and **Re-scan** after editing the circuit. Read the reason shown for any block that is not runnable.

### Short video — Select runnable simulation blocks

!!! note "Video production brief"
    1. **Prepare:** Use a simulation that has been run, with **Blocks** open.
    2. **Opening shot (1–2 s):** Show the block list and the scope summary.
    3. **Action shot (4–6 s):** Click **None**, then **Only runnable**, then **Re-scan**.
    4. **Result shot (2–3 s):** Hold on the runnable block selected again.
    5. **Deliver:** Export a **10–15 second** 1080p MP4.

<!-- wf:video id=select-runnable-simulation-blocks
caption: Blocks lists the circuits of the simulation with their readiness; None, Only runnable and Re-scan
  set what runs
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- ensure_schematic
- wait: 1
- keys:
  - F5
- wait: 2
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^.*Simulate a Block of This Sh.*$
    timeout: 3
- wait: 2
- click_match:
    window: Simulate a Block
    pattern: ^.*Copy to New Simulation$
    timeout: 3
- wait: 4
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^[^A-Za-z]* Add$
    timeout: 5
- wait: 1
- action:
    action: mouse_move_to
    x: 240
    y: 600
- scroll: -3
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/**/##DC
    text: '9'
- keys:
  - Tab
- click_at:
  - 350
  - 112
- wait: 0.5
- click: //##Combo_00/{fa:wave-square} Transient (.tran)
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/**/##StopTime
    text: '3000'
- keys:
  - Tab
- wait: 0.5
- click_at:
  - 489
  - 112
- wait: 12
- &id001
  action:
    action: mouse_move_to
    x: 1000
    y: 12
- tab: Blocks
- wait: 1
steps:
- wait: 1.5
- click: //SPICE Circuit Simulation & Analysis/**/None
- wait: 1.5
- click: //SPICE Circuit Simulation & Analysis/**/Only runnable
- wait: 1.5
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^.*Re-scan$
    timeout: 3
- wait: 1.5
- *id001
- wait: 1.5
brief_sha256: e97d218f3c617120
-->
<!-- wf:out id=select-runnable-simulation-blocks sha=ed496d8fee0c -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/simulation/running-simulation/select-runnable-simulation-blocks.mp4" title="Blocks lists the circuits of the simulation with their readiness; None, Only runnable and Re-scan set what runs"></video>
<!-- /wf:out -->

## 3. Add sources and loads

In **Setup**, add sources to the intended nets. In **Testbench**, add loads and assertions.

Check source polarity, units, waveform parameters, and reference ground. A source added to the wrong net can produce a plausible but irrelevant waveform.

## 4. Run preflight

Click **Preflight** on the toolbar (or **Simulation → Pre-flight Validation Checklist...**). The **Simulation Models & Preflight** window lists every part with its mapped SPICE model and whether it is ready; **Run Simulation** in that window starts the run once nothing is missing.

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

Start the simulation and wait for the plot to update. Review:

- completion status;
- assertion results under **Testbench → Last run**;
- simulation log;
- selected waveform traces;
- cursor measurements when required.

If the run fails, open **AI** and use **Why did the last run fail?** or **Review the preflight blockers**, then verify the explanation against the log and circuit.

### Short video — Preflight, run, and inspect

!!! note "Video production brief"
    1. **Prepare:** Load a small runnable simulation with a validated engine, models, and a supply.
    2. **Opening shot (2 s):** Show the ready workbench before preflight.
    3. **Action shot (7–10 s):** Run preflight, hold on its result, and start the simulation from it. Cut only inactive compute time.
    4. **Result shot (4–5 s):** Hold on the waveform traces with **Signals** open.
    5. **Deliver:** Export a **15–20 second** 1080p MP4.

<!-- wf:video id=preflight-run-and-inspect
caption: 'Preflight on the NE555 blinker''s simulation: every part has a model, Run Simulation, then the
  waveforms under Signals'
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- ensure_schematic
- wait: 1
- keys:
  - F5
- wait: 2
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^.*Simulate a Block of This Sh.*$
    timeout: 3
- wait: 2
- click_match:
    window: Simulate a Block
    pattern: ^.*Copy to New Simulation$
    timeout: 3
- wait: 4
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^[^A-Za-z]* Add$
    timeout: 5
- wait: 1
- action:
    action: mouse_move_to
    x: 240
    y: 600
- scroll: -3
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/**/##DC
    text: '9'
- keys:
  - Tab
- click_at:
  - 350
  - 112
- wait: 0.5
- click: //##Combo_00/{fa:wave-square} Transient (.tran)
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/**/##StopTime
    text: '3000'
- keys:
  - Tab
- wait: 0.5
- &id001
  action:
    action: mouse_move_to
    x: 1000
    y: 12
steps:
- wait: 1.5
- click_at:
  - 580
  - 112
- wait: 3
- click_match:
    window: Simulation Models & Preflight
    pattern: ^.*Run Simulation$
    timeout: 3
- wait: 10
- tab: Signals
- wait: 1
- *id001
- wait: 3
brief_sha256: 434d6abc5a4a9a0b
-->
<!-- wf:out id=preflight-run-and-inspect sha=473b33c8e52c -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/simulation/running-simulation/preflight-run-and-inspect.mp4" title="Preflight on the NE555 blinker&#x27;s simulation: every part has a model, Run Simulation, then the waveforms under Signals"></video>
<!-- /wf:out -->

## Stop or repeat a run

Stop an active run only when required. After changing component values, source settings, models, scope, or analysis parameters, run preflight again before comparing results.

## Common failures

| Result | Check |
|---|---|
| Run is unavailable | A sheet is in front: open or create a simulation (`.simxml`) |
| Engine unavailable | **Preferences → Simulation** engine path and executable |
| No runnable blocks | Models, ground, connectivity, and block reasons |
| Empty waveform | Selected signals and completed analysis |
| Flat output | Source waveform, ground reference, operating point, and load — a copied block has no supply until you add one |
| Assertion not measured | Signal selection, analysis window, and assertion metric |
| Different engines disagree | Dialect, model version, sources, load, and analysis settings |

## See also

- [Simulation Workbench](index.md)
- [Testbenches and Measurements](testbenches-and-measurements.md)
- [Simulation Engines and Models](engines-and-models.md)
- [Waveform Viewer](waveform-viewer.md)
