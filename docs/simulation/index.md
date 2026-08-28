# Simulation Workbench

Use the Simulation Workbench to check how a schematic behaves before you move on to PCB layout. You can view voltage waveforms, measure signals, and verify that important outputs stay within your chosen limits.

Open a schematic, then select **Simulation → SPICE Simulation Panel** or press ++f5++.

!!! note "Available in the upcoming release"
    This guide describes WireFrame 1.5.47. The simulator included with WireFrame is ready to use after installation.

## Quick start

### Diagram — Multi-engine simulation workflow

!!! note "Diagram replacement needed"
    Create a polished release diagram showing: schematic/block scope → preflight → selected simulation engine → analysis run → signals and measurements → assertions and review. The previous ngspice-only pipeline does not represent the current multi-engine workbench.

1. Open a schematic that contains a GND connection and named signal nets.
2. Click **Preflight**.
3. Resolve any item marked as blocking.
4. Choose the type of analysis you need.
5. Click **Run**.
6. Open **Signals** and enable the nets you want to view.

## Workbench tabs

| Tab | What you do there |
|---|---|
| **Setup** | Check readiness, choose a simulator, add sources, and adjust the graph display |
| **Blocks** | Run the whole schematic or only the circuit section you are working on |
| **Testbench** | Add loads and define the results that count as acceptable |
| **Signals** | Show, hide, and measure voltage waveforms |
| **Models** | Find components that need a simulation model |
| **AI** | Ask Copilot to explain a signal or failed check |

## Choose an analysis

| Analysis | Choose it when you want to check |
|---|---|
| **Transient** | Startup, switching, timing, oscillation, or ripple over time |
| **AC Sweep** | Gain and phase across a frequency range |
| **DC Bias** | Steady DC voltage at each node |
| **DC Sweep** | How an output changes while an input voltage is varied |

The controls below the toolbar change with the selected analysis. Hover a disabled option to see why it is unavailable for the current circuit.

## Add power and input signals

Open **Setup**, choose a named net, and click **Add** under **Sources**. Select the source type that matches your circuit:

- **DC** for a fixed supply or input;
- **AC** for small-signal frequency analysis;
- **Sine** for a repeating analog input;
- **Pulse** for clocks and switching inputs;
- **PWL** for a custom sequence of time and voltage points.

!!! tip
    Give important nets clear names such as `VIN`, `VOUT`, `SDA`, or `CLK`. Named nets are easier to select and understand in the results.

## Run Preflight

Preflight checks whether the selected circuit is ready to simulate. Common issues include:

- the circuit has no GND reference;
- components are not connected;
- a resistor, capacitor, or source has no usable value;
- a component needs a simulation model;
- the selected simulator is unavailable.

Double-check the indicated component, correct the issue, then run **Preflight** again.

If an unrelated section is not ready, open **Blocks** and select only the section you want to test.

## Read the waveform

In **Signals**, enable the nets you want to plot. Use the graph controls to:

- zoom and pan;
- fit all active signals automatically;
- show or hide the grid and legend;
- enable A/B cursors for interval measurements;
- display the latest simulated values on the schematic.

Use **More → Export waveform CSV** to save the plotted data. If a run fails, use **More → Export simulation log** when reporting the problem.

## Continue learning

- [Running a Simulation](running-simulation.md)
- [Waveform Viewer](waveform-viewer.md)
- [Testbenches & Measurements](testbenches-and-measurements.md)
- [Simulation Engines & Models](engines-and-models.md)
- [AI Copilot](../ai-copilot.md)
