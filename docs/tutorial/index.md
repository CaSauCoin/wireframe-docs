# Tutorial: Design & Simulate an NE555 Circuit

This step-by-step tutorial walks you through the complete WireFrame workflow — from creating a project and drawing a schematic to **running a SPICE simulation**, layout, routing, and exporting Gerber files — using an **NE555 LED Blinker circuit**.

**What you will build:** A complete NE555 astable oscillator board with an LED blinking at 1 Hz — verified with SPICE simulation and fully routed for fabrication.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the finished NE555 LED Blinker PCB showing the components
     (NE555 IC, resistors R1/R2/R3, capacitors C1/C2, LED D1, terminal J1) routed
     with copper traces. Show both the 2D PCB view and the 3D Viewer side by side.
     SUGGESTED SIZE: 900×400px
-->
![Final Result](../img/tutorial/final-result.png)

---

## What You Will Learn

- [x] Create a project and load component libraries
- [x] Place components and wire an NE555 astable oscillator schematic
- [x] **Run a SPICE simulation** and measure waveforms in the Waveform Viewer
- [x] Run **ERC (Electrical Rules Check)** on the schematic
- [x] Convert schematic to PCB layout
- [x] Place footprints, define board outline, and route copper traces
- [x] Run DFM checks and export Gerber & BOM files

---

## Prerequisites

| Requirement | Details |
|---|---|
| **WireFrame** | Installed and activated ([Installation guide](../installation.md)) |
| **NgSpice** | Installed for SPICE simulation ([Simulation setup](../simulation/index.md#prerequisites)) |
| **Libraries** | KiCad symbol (`.kicad_sym`) and footprint (`.kicad_mod`) libraries |

---

## Step 1 — Create a Project

1. Launch WireFrame.
2. Go to **File → New Project…**
3. Name your project `NE555_Blinker.prjxml`.
4. Click **Create**.

The **Project Structure** panel now displays your project root node.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Project Structure panel showing "NE555_Blinker.prjxml" expanded.
     SUGGESTED SIZE: 300×200px
-->
![Step1 New Project](../img/tutorial/step1-new-project.png)

---

## Step 2 — Draw the NE555 Schematic

1. Go to **File → New Schematic**.
2. Save it as `NE555_Blinker.schxml` (++ctrl+s++).

### 2.1 Place components

Search and place the following components from the Library panel:

| Component | Library Symbol | Designator | Value | Footprint |
|---|---|---|---|---|
| **Timer IC** | `NE555` | `U1` | — | `DIP-8_W7.62mm` |
| **Resistor 1** | `R` | `R1` | `6.8kΩ` | `R_0805_2012Metric` |
| **Resistor 2** | `R` | `R2` | `6.8kΩ` | `R_0805_2012Metric` |
| **Resistor 3** | `R` | `R3` | `330Ω` | `R_0805_2012Metric` |
| **Capacitor 1** | `C_Polarized` | `C1` | `100µF` | `CP_Radial_D5.0mm_P2.00mm` |
| **Capacitor 2** | `C` | `C2` | `10nF` | `C_0805_2012Metric` |
| **LED** | `LED` | `D1` | `Red` | `LED_0805_2012Metric` |
| **Connector** | `Conn_01x02` | `J1` | `9V Power` | `PinHeader_1x02_P2.54mm_Vertical` |
| **Ground** | `GND` | — | — | — |

<!-- TODO: Replace with actual video
     SCENARIO: Record a 20-second clip showing:
     1. Search "NE555" in Library → place U1 on canvas.
     2. Search "R" → place R1, R2, R3.
     3. Search "C" → place C1, C2.
     4. Place D1 and J1. Place GND power symbols.
     RESOLUTION: 1280×720 at 30fps
-->
<video controls width="100%">
  <source src="../../img/tutorial/step3-place-components.webm" type="video/webm">
  <source src="../../img/tutorial/step3-place-components.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### 2.2 Wire the circuit

Press ++w++ to activate the Wire tool and make the following connections:

1. **Power & Ground**: Connect `J1 pin 1` to `U1 pin 8 (VCC)` and `U1 pin 4 (RESET)`. Connect `J1 pin 2` to `GND`. Connect `U1 pin 1 (GND)` to `GND`.
2. **Timing Branch**: Connect `VCC` → `R1 pin 1`. Connect `R1 pin 2` → `R2 pin 1` → `U1 pin 7 (DISCH)`.
3. **Threshold & Trigger**: Connect `R2 pin 2` → `U1 pin 6 (THRES)` → `U1 pin 2 (TRIG)` → `C1 positive (+)` → `C1 negative (-)` to `GND`.
4. **Control Voltage**: Connect `U1 pin 5 (CTRL)` → `C2 pin 1` → `C2 pin 2` to `GND`.
5. **Output**: Connect `U1 pin 3 (OUT)` → `R3 pin 1` → `R3 pin 2` → `D1 Anode (A)` → `D1 Cathode (K)` to `GND`.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the completed NE555 schematic with all wires connected,
     designators R1, R2, R3, C1, C2, D1, U1, J1 visible, and GND symbols attached.
     SUGGESTED SIZE: 800×500px
-->
![NE555 Schematic Complete](../img/tutorial/step3-complete.png)

---

## Step 3 — Run SPICE Simulation

Before building the PCB, verify that the circuit oscillates at 1 Hz using the built-in SPICE simulator.

### 3.1 Open Simulation Controls

Go to **Tools → Simulation** (or open the Simulation Controls panel).

### 3.2 Configure Transient Analysis

1. Set **Analysis Type**: `Transient (.TRAN)`.
2. Set **Stop Time**: `3 s` (to capture 3 full 1-second cycles).
3. Set **Step Size**: `1 ms`.
4. Click **Run**.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Simulation Controls panel with Transient selected,
     Stop Time = 3s, Step Size = 1ms, and progress bar showing 100%.
     SUGGESTED SIZE: 400×350px
-->
[//]: # (![Step 3 Sim Setup](../img/tutorial/step3-sim-setup.png))

### 3.3 Analyze Waveforms

The **Waveform Viewer** opens automatically:

- **Output Signal `v(OUT)`**: A clear square wave switching between 0V and ~8.2V at ~1 Hz.
- **Timing Capacitor Voltage `v(THRES)`**: Sawtooth wave charging between 1/3 VCC (3V) and 2/3 VCC (6V).
- **Measure Frequency**: Turn on **Cursors** (++c++) → place Cursor 1 on first rising edge, Cursor 2 on second rising edge → read Δt ≈ 1.0 s (Frequency = 1.0 Hz).

<!-- TODO: Replace with actual video
     SCENARIO: Record a 20-second clip showing:
     1. Click "Run" in Simulation Controls.
     2. Progress bar moves to 100% — Waveform Viewer opens.
     3. Toggle Cursors — drag C1 and C2 onto consecutive output pulses.
     4. Delta readout shows Δt = 1.02s (f = 0.98 Hz).
     RESOLUTION: 1280×720 at 30fps
-->
<video controls width="100%">
  <source src="../../img/tutorial/step3-sim-waveforms.webm" type="video/webm">
  <source src="../../img/tutorial/step3-sim-waveforms.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Step 4 — Run Electrical Rules Check (ERC)

1. Go to **Tools → ERC Check**.
2. The ERC panel runs checks:
    - Verifies no floating pins remain.
    - Confirms all nets connect to valid endpoints.
    - Verifies duplicate designators don't exist.
3. Ensure **0 Errors, 0 Warnings**.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the ERC Panel showing "0 errors, 0 warnings" clean result.
     SUGGESTED SIZE: 500×300px
-->
[//]: # (![Step 4 ERC](../img/tutorial/step4-erc.png))

---

## Step 5 — Convert to PCB & Arrange Footprints

1. Go to **Project → Convert to PCB**.
2. A new PCB document `NE555_Blinker.pcbxml` opens with footprints clustered together.
3. Arrange footprints logically:
    - `J1` near the left board edge.
    - `U1 (NE555)` in the center.
    - `R1`, `R2`, `C1` grouped on the left of U1.
    - `R3`, `D1` placed to the right of U1 output.
    - `C2` placed close to U1 pin 5.
4. Set **Edge.Cuts** layer → draw a rectangular board outline (approx 50 × 40 mm).

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the PCB layout with footprints arranged, yellow ratsnest lines
     connecting pads, and a magenta board outline on Edge.Cuts.
     SUGGESTED SIZE: 700×450px
-->
[//]: # (![Step 5 Placement](../img/tutorial/step5-placement.png))

---

## Step 6 — Route Traces & Add Ground Plane

### 6.1 Route Copper Traces

1. Press ++x++ to activate the **Route Trace** tool.
2. Route signal traces on **F.Cu** (Red):
    - Connect `U1 pin 3` → `R3` → `D1 Anode`.
    - Connect `R1` → `R2` → `U1 pin 7`.
    - Connect `R2` → `U1 pin 6` → `U1 pin 2` → `C1`.
3. Press ++v++ to place vias when switching to **B.Cu** (Blue) for power paths.

### 6.2 Add Ground Plane (Copper Zone)

1. Select **Zone** tool → set layer to **B.Cu** → Net `GND`.
2. Draw a polygon around the entire board outline.
3. Click **Fill Zone** — a solid ground fill generates automatically with thermal reliefs around GND pads.

<!-- TODO: Replace with actual video
     SCENARIO: Record a 20-second clip showing:
     1. Routing signal traces with Route Trace tool (X).
     2. Selecting Zone tool → drawing GND plane polygon on B.Cu.
     3. Click Fill Zone — copper flood fills the bottom layer.
     4. All ratsnest lines disappear.
     RESOLUTION: 1280×720 at 30fps
-->
<video controls width="100%">
  <source src="../../img/tutorial/step7-routing.webm" type="video/webm">
  <source src="../../img/tutorial/step7-routing.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Step 7 — Run DFM Check & Export

### 7.1 DFM Verification

Go to **Tools → DFM Check** → click **Run DFM**. Verify 0 clearance errors and 0 trace width violations.

### 7.2 Fabrication Export

1. **Gerber Files**: **File → Export → Gerber…** → select `F.Cu`, `B.Cu`, `F.SilkS`, `F.Mask`, `Edge.Cuts` → **Export**.
2. **BOM Export**: **File → Export → BOM…** → save `NE555_Blinker_BOM.csv`.
3. **Verify**: Open **Tools → Gerber Viewer** → load `F.Cu.gbr` to verify trace shapes.

---

## Summary Deliverables :material-check-decagram:{ style="color: #00E5FF" }

| Output | File | Purpose |
|---|---|---|
| Project File | `NE555_Blinker.prjxml` | Central project workspace |
| Schematic | `NE555_Blinker.schxml` | Schematic diagram with SPICE properties |
| PCB Layout | `NE555_Blinker.pcbxml` | Fully routed 2-layer PCB |
| Simulation | Waveform logs | Transient simulation output |
| Gerbers | `*.gbr` files | Manufacturing files for PCB fabricator |
| BOM | `NE555_Blinker_BOM.csv` | Component list for purchasing |

---

## See Also

- [SPICE Simulation Guide](../simulation/index.md) — advanced simulation modes (AC, DC sweep).
- [AI-Assisted Design Tutorial](ai-design.md) — design this same circuit automatically using AI.
- [Design Rules & Net Classes](../pcb/design-rules.md) — PCB constraint management.
