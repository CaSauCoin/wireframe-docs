# Running a Simulation

This page covers the complete simulation workflow — from preflight validation to configuring analysis parameters and executing the simulation.

---

## Step 1: Simulation Preflight

Before any simulation can run, WireFrame performs a **Preflight Check** — a strict gateway that catches fatal errors early:

| Check | Description | Severity |
|---|---|---|
| **Missing ground** | No GND symbol in the circuit — SPICE requires a reference node | 🔴 Fatal |
| **Floating nodes** | Nodes with no DC path to ground | 🔴 Fatal |
| **Missing component values** | Resistors, capacitors without numeric values (e.g., empty Value field) | 🔴 Fatal |
| **Missing SPICE models** | ICs or transistors without `.subckt` model definitions | 🟡 Warning |
| **Unconnected pins** | Component pins not wired to the circuit | 🟡 Warning |

If **fatal errors** are detected, the simulation is blocked and error messages appear in the Logger.

!!! warning "Fix all red errors before simulating"
    A circuit without a ground reference or with floating components will produce either no results or nonsensical data.

---

## Step 2: Netlist Generation

WireFrame automatically converts your schematic into a SPICE netlist using the **Netlist Builder**:

### What happens internally

1. The builder traverses all placed components and wires.
2. Each component is translated to its SPICE equivalent:

| Schematic Component | SPICE Element | Example |
|---|---|---|
| Resistor `R1 = 10kΩ` | `R1 net1 net2 10k` | Standard resistor |
| Capacitor `C1 = 100nF` | `C1 net1 net2 100n` | Standard capacitor |
| LED `D1` | `D1 net1 net2 LED_model` | Diode with model |
| Voltage source | `V1 net1 0 DC 5` | DC supply |
| Op-Amp | `.subckt` block | External model file |

3. The **Prefix Mapper** ensures SPICE naming conventions are followed:
    - Resistors → `R` prefix
    - Capacitors → `C` prefix
    - Voltage sources → `V` prefix
    - Inductors → `L` prefix

4. External SPICE model files (`.subckt` definitions) are injected automatically by the **Template Provider** for supported ICs (op-amps, timers, regulators).

### Viewing the netlist

The generated netlist is visible in the simulation log. Example:

```spice
* WireFrame EDA — Generated SPICE Netlist
V1 VCC 0 DC 5
R1 VCC out 1k
C1 out 0 100n
.tran 10u 10m
.end
```

---

## Step 3: Configure Analysis

Open the **Simulation Controls** panel from **Tools → Simulation**.

### Transient Analysis

| Parameter | Description | Default |
|---|---|---|
| **Stop Time** | Total simulation duration | 10 ms |
| **Step Size** | Time resolution (smaller = more detail, slower) | 10 µs |
| **Start Time** | When to begin recording results (skip initial transient) | 0 |

### AC Analysis

| Parameter | Description | Default |
|---|---|---|
| **Start Frequency** | Lower bound of frequency sweep | 1 Hz |
| **Stop Frequency** | Upper bound | 1 MHz |
| **Points per Decade** | Number of frequency points per decade | 100 |
| **Sweep Type** | Linear or logarithmic (decade) | Decade |

### DC Sweep

| Parameter | Description | Default |
|---|---|---|
| **Source** | Which voltage/current source to sweep | V1 |
| **Start Value** | Beginning of sweep range | 0 V |
| **Stop Value** | End of sweep range | 5 V |
| **Step** | Increment per point | 0.1 V |

### Operating Point

No parameters needed — calculates the single DC steady-state.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Simulation Controls panel showing:
     - A dropdown for "Analysis Type" with "Transient" selected.
     - Input fields: Stop Time = 10ms, Step Size = 10µs.
     - A "Run" button (green/cyan colored).
     - An "Abort" button (red, disabled since no sim is running).
     - A progress bar at 0%.
     SUGGESTED SIZE: 400×350px
-->
![Simulation Controls](../img/simulation/simulation-controls.png)

---

## Step 4: Run the Simulation

1. Click **Run** in the Simulation Controls panel.
2. The simulation starts on a **background thread** — the editor remains responsive.
3. A **progress bar** shows the simulation progress (percentage).
4. The **status line** shows the current simulation time (e.g., `tran: 5.2ms`).
5. When complete, results automatically populate the [Waveform Viewer](waveform-viewer.md).

### Aborting a simulation

If the simulation takes too long or you realize there's an error:

- Click the **Abort** button.
- The simulation halts immediately and partial results (if any) are discarded.

<!-- TODO: Replace with actual video
     SCENARIO: Record a 15-second clip showing:
     1. The Simulation Controls panel with Transient selected, Stop Time = 10ms.
     2. Click "Run" — the progress bar starts moving.
     3. Status shows "tran: 1.0ms", "tran: 5.0ms", "tran: 9.8ms".
     4. Progress reaches 100% — "Simulation complete" message.
     5. The Waveform Viewer tab opens with voltage traces.
     RESOLUTION: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/simulation/run-simulation.webm" type="video/webm">
  <source src="../../img/simulation/run-simulation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## SPICE Model Files

### Built-in models

WireFrame includes SPICE models for common components via the **Template Provider**:

| Component Type | Model Source |
|---|---|
| Standard diodes | Built-in `.model` definitions |
| LEDs | Built-in `.model` definitions |
| Common op-amps (LM741, LM358) | Built-in `.subckt` files |
| 555 Timer (NE555) | Built-in `.subckt` file |
| Standard transistors (2N2222, BC547) | Built-in `.model` definitions |

### External models

For components not in the built-in library:

1. Obtain the SPICE model file from the manufacturer's website.
2. Place the `.lib` or `.sub` model file in the `Simulate/models/` directory.
3. The Template Provider will find and include it during netlist generation.

---

## Simulation Log

During and after simulation, log messages are available:

| Log Level | Color | Example |
|---|---|---|
| **Info** | Blue | `"Netlist generated: 12 components, 8 nets"` |
| **Progress** | Grey | `"tran: 5.0ms of 10.0ms"` |
| **Warning** | Yellow | `"Model not found for Q3 — using default NPN"` |
| **Error** | Red | `"Simulation failed: singular matrix at time 2.1ms"` |

---

## Common Issues

??? question "Simulation fails with 'singular matrix'"
    This usually means there's an issue with the circuit topology:
    - A voltage source directly across another voltage source (short circuit).
    - An inductor loop without any resistance.
    - **Fix**: Add small series resistances (0.01Ω) or ensure proper circuit topology.

??? question "Simulation runs but produces flat lines"
    - Check that your source has the correct value and type (AC source for AC analysis, pulse for transient).
    - Verify the simulation time is long enough to see the expected behavior.
    - For oscillators: the simulation may need more time to reach steady state.

---

## See Also

- [Simulation Overview](index.md) — analysis types and prerequisites.
- [Waveform Viewer](waveform-viewer.md) — interpret and measure results.
- [ERC](../schematic/erc.md) — validate the schematic before simulating.
