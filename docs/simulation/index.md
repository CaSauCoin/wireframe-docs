# Simulation Workbench

Use the Simulation Workbench to check how a circuit behaves before you move on to PCB layout. You can view voltage waveforms, measure signals, and verify that important outputs stay within your chosen limits.

A simulation is a file of its own (`.simxml`). It holds one circuit, drawn in the schematic editor from parts that have a SPICE model, and it is listed in the project under its own name. The sheets of your design are not simulated: nothing you add to a simulation — supplies, probes, test loads — ever reaches the sheets, the PCB, the BOM or the ERC.

!!! note "Simulator included"
    WireFrame ships ngspice, which runs inside the application — nothing else to install. Xyce, LTspice, and a separately installed ngspice are optional; see [Engines & SPICE Models](engines-and-models.md).

## Get a simulation

There are two ways to start one:

- **Copy a block of a sheet.** With a sheet in front, select **Simulation → Simulate a Block of This Sheet...**. The dialog lists the blocks of the sheet; each shows **Ready** or **Needs input** with the reason (for example, no source drives it). Select one and click **Copy to New Simulation**. Its parts, the wires between them, and the labels and ports on those wires are copied into a new simulation, which opens in its own tab. Parts without a SPICE model on those wires, such as connectors, are named rather than copied.
- **Start an empty one.** Select **File → New → New Simulation (.simxml)** or **Simulation → New Simulation (.simxml)** and draw the circuit. While a simulation is in front, the **Library** panel lists only parts that have a SPICE model.

The copy is made once. After that the sheet and the simulation do not know each other: change the sheet, and copy the block again when you want to simulate the new version.

Pressing ++f5++ with a sheet in front opens the workbench on a page offering both buttons. With a simulation in front, ++f5++ opens the workbench **and runs** the current setup.

### Short video — Copy a block into a simulation

!!! note "Video production brief"
    1. **Prepare:** Open the NE555 blinker sample with its schematic sheet in front.
    2. **Opening shot (1–2 s):** Press F5 and hold on the workbench page that says simulations have a file of their own.
    3. **Action shot (4–6 s):** Click **Simulate a Block of This Sheet...**, hold on the block list with its readiness, then click **Copy to New Simulation**.
    4. **Result shot (2–3 s):** Hold on the new simulation tab and the workbench ready to run.
    5. **Deliver:** Export a **10–15 second** 1080p MP4.

<!-- wf:video id=copy-a-block-into-a-simulation
caption: 'The NE555 blinker''s sheet: Simulation → Simulate a Block of This Sheet, then Copy to New Simulation
  — the block opens as a simulation of its own'
project: samples/ne555-blinker/NE555 Blinker.prjxml
setup:
- open_project
- ensure_schematic
- wait: 1
- &id001
  action:
    action: mouse_move_to
    x: 1000
    y: 12
steps:
- wait: 1
- keys:
  - F5
- wait: 2.5
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^.*Simulate a Block of This Sh.*$
    timeout: 3
- wait: 3
- click_match:
    window: Simulate a Block
    pattern: ^.*Copy to New Simulation$
    timeout: 3
- wait: 3
- *id001
- wait: 2
brief_sha256: 30fae378f417ac88
-->
<!-- wf:out id=copy-a-block-into-a-simulation sha=1524371c661f -->
<video controls muted playsinline preload="metadata" src="../assets/wf/docs/simulation/index/copy-a-block-into-a-simulation.mp4" title="The NE555 blinker&#x27;s sheet: Simulation → Simulate a Block of This Sheet, then Copy to New Simulation — the block opens as a simulation of its own"></video>
<!-- /wf:out -->

## Quick start

1. Copy a block into a simulation, or open one.
2. Open **Setup → Sources**, add a supply on the circuit's rail, and set its value.
3. Choose the type of analysis you need and its values.
4. Click **Preflight** and resolve any item marked as blocking.
5. Click **Run** (or press ++f5++).
6. Open **Signals** and enable the nets you want to view.

## Workbench tabs

| Tab | What you do there |
|---|---|
| **Setup** | Check readiness, choose a simulator, add sources, and adjust the graph display |
| **Blocks** | Choose which circuits of the simulation to run, when it holds more than one |
| **Testbench** | Add loads and define the results that count as acceptable |
| **Signals** | Show, hide, and measure voltage waveforms |
| **Models** | Find components that need a simulation model |
| **AI** | Ask Copilot to explain a signal or failed check |

## Choose an analysis

| Analysis | Choose it when you want to check |
|---|---|
| **Transient** | Startup, switching, timing, oscillation, or ripple over time |
| **AC Sweep** | Gain and phase across a frequency range |
| **DC Bias Op** | Steady DC voltage at each node (operating point) |
| **DC Sweep** | How an output changes while an input voltage is varied |

The controls below the toolbar change with the selected analysis. Hover a disabled option to see why it is unavailable for the current circuit.

## Add power and input signals

A block copied from a sheet usually has no supply of its own: on the sheet, its rail came from another part of the design. Open **Setup**, choose a named net, and click **Add** under **Sources**. Select the source type that matches your circuit:

- **DC** for a fixed supply or input;
- **AC** for small-signal frequency analysis;
- **Sine** for a repeating analog input;
- **Pulse** for clocks and switching inputs;
- **PWL** for a custom sequence of time and voltage points.

!!! tip
    Give important nets clear names such as `VIN`, `VOUT`, `SDA`, or `CLK`. Named nets are easier to select and understand in the results.

## Run Preflight

Preflight checks whether the simulation is ready to run. Common issues include:

- the circuit has no GND reference;
- components are not connected;
- a resistor, capacitor, or source has no usable value;
- a component needs a simulation model;
- the selected simulator is unavailable.

Double-check the indicated component, correct the issue, then run **Preflight** again.

If an unrelated circuit in the simulation is not ready, open **Blocks** and select only the circuit you want to test.

## Read the waveform

In **Signals**, enable the nets you want to plot. To mark a net on the simulation's canvas instead, choose **Probe Signal** on its toolbar (++v++) and click a wire, pin, net label, or power symbol. Use the graph controls to:

- zoom and pan;
- fit all active signals automatically;
- show or hide the grid and legend;
- enable A/B cursors for interval measurements;
- show the latest simulated voltages on the simulation's canvas (**Voltage heatmap**).

Use **More → Export waveform CSV** to save the plotted data. If a run fails, use **More → Export simulation log** when reporting the problem.

## Continue learning

- [Running a Simulation](running-simulation.md)
- [Waveform Viewer](waveform-viewer.md)
- [Testbenches & Measurements](testbenches-and-measurements.md)
- [Simulation Engines & Models](engines-and-models.md)
- [AI Copilot](../ai-copilot.md)
