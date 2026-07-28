# SPICE Simulation — Overview

WireFrame integrates industry-standard **SPICE simulation** directly into the editor. Design your circuit in the schematic editor, then simulate it without leaving the application — view voltages, currents, and frequency responses in an interactive waveform viewer.

---

## What You Can Do

| Capability | Description |
|---|---|
| **Transient Analysis** (.TRAN) | Time-domain simulation — see how signals change over time |
| **AC Analysis** (.AC) | Frequency-domain sweep — plot gain and phase (Bode plots) |
| **DC Sweep** (.DC) | Sweep a voltage/current source and plot the response |
| **Operating Point** (.OP) | Calculate DC bias voltages and currents at steady state |
| **Waveform Viewer** | Interactive oscilloscope with cursors for measurement |

---

## How It Works

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Schematic   │────▶│  Preflight   │────▶│  Netlist      │────▶│   NgSpice    │────▶│  Waveform    │
│  Design      │     │  Checks      │     │  Builder      │     │   Engine     │     │  Viewer      │
└─────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
     Draw your           Validate            Convert              Run the             View results
     circuit             components          to SPICE             simulation           interactively
```

1. **Design** your circuit in the schematic editor with components and wires.
2. **Preflight** checks scan for errors that would prevent simulation (missing values, floating ground, etc.).
3. The **Netlist Builder** converts the schematic into a SPICE-compatible text netlist.
4. The **NgSpice Engine** runs the simulation in a background thread.
5. Results are displayed in the **Waveform Viewer** — an interactive oscilloscope.

---

## Prerequisites

### NgSpice Runtime

WireFrame loads `libngspice` **dynamically at runtime**. If NgSpice is not installed on your system, the simulation feature is gracefully disabled — the rest of the application works normally.

=== "Linux"

    ```bash
    # Ubuntu / Debian
    sudo apt-get install libngspice0-dev

    # Fedora
    sudo dnf install ngspice-devel
    ```

=== "Windows"

    NgSpice is bundled with the WireFrame Windows installer — no additional installation needed.

=== "macOS"

    ```bash
    brew install ngspice
    ```

!!! info "Checking if NgSpice is available"
    When WireFrame starts, it attempts to load `libngspice`. If successful, the simulation menu items are enabled. If not, a message appears in the Logger: `"NgSpice: library not found — simulation disabled."`

---

## Supported Analysis Types

### Transient Analysis (.TRAN)

Simulates circuit behavior **over time**. Best for:

- Oscillator circuits (555 timer, RC oscillators)
- Power supply startup behavior
- Digital signal timing

| Parameter | Description | Example |
|---|---|---|
| Stop time | Total simulation duration | 10 ms |
| Step size | Time resolution | 10 µs |

### AC Analysis (.AC)

Sweeps frequency and plots **gain and phase**. Best for:

- Filter frequency response
- Amplifier bandwidth analysis
- Impedance vs. frequency

| Parameter | Description | Example |
|---|---|---|
| Start frequency | Sweep start | 1 Hz |
| Stop frequency | Sweep end | 1 MHz |
| Points per decade | Resolution | 100 |

### DC Sweep (.DC)

Sweeps a **source voltage or current** and plots the DC response. Best for:

- Diode I-V curves
- Transfer characteristics
- Bias point analysis

| Parameter | Description | Example |
|---|---|---|
| Source name | Which source to sweep | V1 |
| Start value | Sweep start | 0 V |
| Stop value | Sweep end | 5 V |
| Step size | Increment | 0.1 V |

### Operating Point (.OP)

Calculates the **DC steady-state** of the circuit — all node voltages and branch currents at a single point.

- Results displayed in a **table format** rather than waveforms.
- Useful for verifying bias conditions before running transient or AC analysis.

---

## Quick Start

1. Complete your schematic (components, wires, values assigned).
2. Go to **Tools → Simulation** or the Simulation panel.
3. Select analysis type (e.g., Transient).
4. Configure parameters (stop time, step size).
5. Click **Run**.
6. View results in the Waveform Viewer.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the simulation workflow — a schematic of a simple RC circuit
     (resistor + capacitor + voltage source) with the Simulation Controls panel open,
     showing "Transient Analysis" selected, stop time = 10ms, step = 10µs.
     The Run button is visible and highlighted.
     SUGGESTED SIZE: 1280×720px (full window)
-->
[//]: # (![Simulation Quickstart](img/simulation/simulation-quickstart.png))

---

## Section Pages

| Page | What you'll learn |
|---|---|
| [Running a Simulation](running-simulation.md) | Preflight checks, configuration, running, SPICE models |
| [Waveform Viewer](waveform-viewer.md) | Interactive plotting, cursors, measurements |

---

## See Also

- [Tutorial: NE555 LED Blinker](../tutorial/index.md) — includes a complete simulation walkthrough.
- [Schematic Editor](../schematic/index.md) — design the circuit to simulate.
