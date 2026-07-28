# Waveform Viewer

The Waveform Viewer is an **interactive oscilloscope** built into WireFrame. After a simulation completes, it displays voltage, current, and phase waveforms with zoom, pan, cursors, and measurement capabilities.

---

## Opening the Waveform Viewer

The Waveform Viewer opens **automatically** after a successful simulation. It appears as a panel or tab within the editor workspace.

---

## Viewer Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  ⚙ Auto Scale  │  📐 Grid  │  📋 Legend  │  ✂ Cursors          │  ← Controls
├─────────────────────────────────────────────────────────────────┤
│  V (volts)                                                      │
│  5.0 ┤                     ┌──────────────┐                     │
│      │                    ╱│              │╲                     │
│  2.5 ┤                   ╱ │              │ ╲                    │
│      │                  ╱  │              │  ╲                   │
│  0.0 ┤─────────────────╱───┤──────────────┤───╲──────────       │
│      │                C1   │              │   C2                 │
│      └────────┼────────┼───┼──────────┼───┼──────────── t (ms) │
│               0        2   │          6   │       10             │
│                            │  Δt = 4ms    │                     │
│                            │  ΔV = 2.5V   │                     │
│                            │  f = 250 Hz  │                     │
├─────────────────────────────────────────────────────────────────┤
│  Legend: ── v(out)  ── v(in)  ── i(R1)                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Waveform Display

### Traces

Each simulation output vector is plotted as a colored trace:

| Trace type | Description | Example |
|---|---|---|
| **Voltage** | Node voltage (referenced to GND) | `v(out)`, `v(VCC)` |
| **Current** | Branch current through a component | `i(R1)`, `i(V1)` |
| **Phase** | Phase angle (AC analysis only) | Phase of `v(out)` |

Multiple traces can be displayed simultaneously with different colors.

### Transient results

- X-axis: **Time** (seconds, ms, µs)
- Y-axis: **Voltage** (V) or **Current** (A)

### AC results

- X-axis: **Frequency** (Hz, kHz, MHz) — logarithmic scale
- Y-axis: **Magnitude** (dB) and/or **Phase** (degrees)

### Operating Point results

Displayed as a **table** rather than a waveform:

| Node / Branch | Value |
|---|---|
| `v(out)` | 2.483 V |
| `v(VCC)` | 5.000 V |
| `i(R1)` | 0.248 mA |
| `i(V1)` | -1.25 mA |

---

## Controls

### Auto Scale

- **Auto Scale ON** (default): Y-axis range automatically fits all visible data.
- **Auto Scale OFF**: Manually set Y-axis min/max for precise comparison.

| Control | Description |
|---|---|
| Auto Scale toggle | Automatically fit Y-axis range to data |
| Min Y / Max Y | Manual Y-axis range (when auto scale is off) |
| Min X / Max X | Manual X-axis range |

### Grid

Toggle a reference grid overlay on the plot:

- Grid lines help estimate values visually.
- Click **Grid** to show/hide.

### Legend

Toggle the legend display showing trace names and colors:

- Each trace is listed with its color and name.
- Click **Legend** to show/hide.

---

## Cursor Measurements

The waveform viewer supports **two measurement cursors** (C1 and C2) for precise readings:

### Placing cursors

1. Click the **Cursors** toggle to enable cursors.
2. Click on the plot area to place **Cursor 1** (C1).
3. Click again to place **Cursor 2** (C2).
4. Drag cursors left/right to reposition them.

### Reading measurements

When both cursors are placed, the viewer displays:

| Measurement | Description | Example |
|---|---|---|
| **Δt** (Delta time) | Time difference between C1 and C2 | 4.0 ms |
| **ΔV** (Delta voltage) | Voltage difference at C1 and C2 | 2.5 V |
| **Frequency** | 1 / Δt — the frequency if measuring one period | 250 Hz |

```
Cursor Measurement Example:

  C1 at t = 2.0 ms, v = 0.0 V
  C2 at t = 6.0 ms, v = 2.5 V

  Δt = 4.0 ms
  ΔV = 2.5 V
  f  = 1 / 4.0ms = 250 Hz
```

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Waveform Viewer showing:
     - A transient simulation result with 2 traces: v(out) in cyan and v(in) in yellow.
     - v(out) showing a square wave or RC charging curve.
     - Two vertical cursor lines (C1 and C2) positioned on the waveform.
     - Measurement readout showing Δt, ΔV, and frequency values.
     - Grid visible, legend showing trace names.
     - Dark background consistent with the ImGui theme.
     SUGGESTED SIZE: 900×500px
-->
[//]: # (![Waveform Viewer Cursors](../img/simulation/waveform-viewer-cursors.png))

---

## Interacting with the Plot

| Action | Input | Effect |
|---|---|---|
| **Zoom in/out** | Scroll wheel | Zoom the time axis (X) |
| **Pan** | Click and drag | Move the view left/right and up/down |
| **Reset view** | Double-click | Reset to auto-scale view |
| **Move cursor** | Drag cursor line | Reposition C1 or C2 |

---

## Auto-Run Timer

The simulation viewer supports an **auto-run timer** for iterative testing:

- Useful when tweaking component values — the simulation re-runs automatically after changes.
- The timer countdown is visible in the controls area.

---

## Practical Examples

### Example 1: RC Time Constant

Simulate an RC circuit (R = 10kΩ, C = 100nF) with a 5V step input:

- **Expected**: Exponential charging curve with τ = R×C = 1ms.
- **Verify**: Place C1 at t=0, C2 at t=1ms → v(out) should be ~3.16V (63% of 5V).

### Example 2: 555 Timer Oscillator

Simulate a 555 timer in astable mode:

- **Expected**: Square wave output.
- **Verify**: Place cursors on consecutive rising edges → Δt gives the period, 1/Δt gives frequency.

### Example 3: Filter Frequency Response

Run AC analysis on an RC low-pass filter:

- **Expected**: Flat response below cutoff, -20dB/decade rolloff above.
- **Verify**: Find the -3dB point on the magnitude plot.

<!-- TODO: Replace with actual video
     SCENARIO: Record a 20-second clip showing:
     1. A completed RC circuit simulation result in the Waveform Viewer.
     2. Enable cursors — place C1 at t=0, C2 at the 63% voltage point.
     3. The measurement readout shows Δt ≈ 1ms (matching RC time constant).
     4. Zoom in to verify the exact voltage at C2.
     RESOLUTION: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/simulation/waveform-measurement.webm" type="video/webm">
  <source src="../../img/simulation/waveform-measurement.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## See Also

- [Running a Simulation](running-simulation.md) — configure and execute simulations.
- [Simulation Overview](index.md) — supported analysis types.
- [Tutorial: NE555 LED Blinker](../tutorial/index.md) — includes hands-on simulation.
