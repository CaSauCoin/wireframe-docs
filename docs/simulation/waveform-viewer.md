# Waveform Viewer

The waveform area displays results from the latest completed run of the simulation in front. Use it to compare selected signals, inspect timing and amplitude, and support testbench decisions.

## Select traces

Open **Signals** in the Simulation Workbench and select the nets to display. The plot updates from the available result data. **Filter signals** narrows a long list by name.

Use:

- **Named nets** for important labeled signals;
- **All** for broad debugging;
- **None** before building a focused comparison.

You can also mark a net directly on the simulation's canvas: choose **Probe Signal** on its toolbar (++v++) and click a wire, pin, net label, or power symbol. A probe marker is placed on that net. Probes belong to the simulation; sheets of the design have no probe tool.

Under the list, **Measurements** gives the maximum, minimum, and peak-to-peak of each plotted signal — over the whole record, or between the A/B cursors when **Measure between cursors** is ticked and the cursors are on.

### Image — Waveform Viewer with two signals

!!! note "Image capture brief"
    1. **Prepare:** Run a 3 s transient of the NE555 blinker's simulation.
    2. **Build the frame:** Filter **Signals** to two related nets and plot only those two, with their measurements visible.
    3. **Clean the frame:** Move the pointer away from key text.
    4. **Approve:** Check the image at 100% zoom for readable axes, legend, and values.

<!-- wf:shot id=waveform-viewer-with-two-signals
caption: 'Signals filtered to tim: timer_out and timing_node of the NE555 blinker plotted together, with
  their measurements'
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
- tab: Signals
- wait: 0.5
- type:
    ref: //SPICE Circuit Simulation & Analysis/**/##SignalFilter
    text: tim
- wait: 0.5
- click: //SPICE Circuit Simulation & Analysis/**/None
- wait: 0.5
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^timer_out$
    timeout: 3
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^timing_node$
    timeout: 3
- wait: 1
- *id001
brief_sha256: 799df41323b40420
-->
<!-- wf:out id=waveform-viewer-with-two-signals sha=b25e3cf9839d -->
![Signals filtered to tim: timer_out and timing_node of the NE555 blinker plotted together, with their measurements](../assets/wf/docs/simulation/waveform-viewer/waveform-viewer-with-two-signals.png)
<!-- /wf:out -->

## View controls

These are under **Setup → View**:

| Control | Purpose |
|---|---|
| **Auto-scale results** | Fit available traces to the current plot |
| **Grid** | Show measurement reference lines |
| **Legend** | Identify displayed traces |
| **A/B cursors** | Compare two points on a trace |

Disable auto-scale when you need a stable visual range across repeated runs. Re-enable it when new data falls outside the current view. **In**, **Out**, and **Fit** on the toolbar zoom the time axis.

## Use A/B cursors

1. Tick **A/B cursors** under **Setup → View**.
2. Drag cursor A to the first event.
3. Drag cursor B to the second event.
4. Read the time of each cursor, the interval (**dT**), and the matching frequency at the bottom of the plot.
5. Record the measurement or add an equivalent testbench assertion when it must be checked repeatedly.

### Short video — Measure a waveform with A/B cursors

!!! note "Video production brief"
    1. **Prepare:** Load a clean transient result with one stable periodic signal and readable axes.
    2. **Opening shot (1–2 s):** Hold on the waveform with cursors disabled.
    3. **Action shot (5–8 s):** Enable **A/B cursors**, drag A onto a rising edge, and drag B onto the next rising edge.
    4. **Result shot (2–3 s):** Hold on both cursors, the readable time delta, and the measurements between them.
    5. **Deliver:** Export a **10–15 second** 1080p MP4 with no unnecessary zoom animation.

<!-- wf:video id=measure-a-waveform-with-a-b-cursors
caption: A/B cursors on two rising edges of timer_out read 1011 ms, 0.99 Hz; Measurements follow the window
  between them
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
- action:
    action: mouse_move_to
    x: 240
    y: 600
- scroll: -10
- wait: 0.5
- *id001
steps:
- wait: 1.5
- click_match:
    window: SPICE Circuit Simulation
    pattern: ^A/B cursors$
    timeout: 3
- wait: 1.5
- drag_at:
    from:
    - 683
    - 500
    to:
    - 818
    - 500
    seconds: 1.5
- wait: 1
- drag_at:
    from:
    - 1032
    - 500
    to:
    - 1054
    - 500
    seconds: 1.2
- wait: 1.5
- *id001
- tab: Signals
- wait: 3
brief_sha256: a5b6b9b9dce5e1d2
-->
<!-- wf:out id=measure-a-waveform-with-a-b-cursors sha=e69b9702fd31 -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/simulation/waveform-viewer/measure-a-waveform-with-a-b-cursors.mp4" title="A/B cursors on two rising edges of timer_out read 1011 ms, 0.99 Hz; Measurements follow the window between them"></video>
<!-- /wf:out -->

## Interpret common analyses

### Transient

Check startup, delay, rise/fall time, overshoot, ripple, duty cycle, and settling behavior over time.

### AC

Check gain and phase across frequency. Confirm that the selected engine and model support the intended AC behavior.

### DC sweep

Check how an output or operating point changes with a swept source or parameter.

### Operating point

Check steady node voltages and branch currents without interpreting them as time-domain traces.

## Compare results safely

- keep source, load, model version, scope, and analysis settings identical;
- do not compare traces from different runs unless the settings are recorded;
- use assertions for release criteria instead of judging only by visual shape;
- exclude startup from steady-state measurements when appropriate;
- export data when another reviewer needs evidence.

## Ask Copilot

Use the robot action beside a signal or open the **AI** tab and select **Explain the waveform results**. State the expected behavior and the relevant time window. Verify the response against the plotted data and testbench limits.

## See also

- [Running a Simulation](running-simulation.md)
- [Testbenches and Measurements](testbenches-and-measurements.md)
- [Simulation Engines and Models](engines-and-models.md)
