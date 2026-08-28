# Tutorial: Design a Simple LED Circuit

This step-by-step tutorial walks you through the complete WireFrame workflow — from creating a project to exporting Gerber files — using a **simple LED circuit** with a resistor and a connector.

**What you will build:** A basic single-layer PCB with one LED, one current-limiting resistor, and a 2-pin connector — fully routed and ready for fabrication.

![Final Result](../img/tutorial/final-result.png)


---

## What You Will Learn

- [x] Create a project and load libraries
- [x] Place components and wire them in the schematic editor
- [x] Convert the schematic to a PCB
- [x] Place footprints and define the board outline
- [x] Route traces and add a ground plane
- [x] Run DFM checks
- [x] Export Gerber and BOM files

---

## Prerequisites

| Requirement | Details |
|---|---|
| **WireFrame** | Installed and activated ([Installation guide](../installation.md)) |
| **Libraries** | At least one KiCad symbol (`.kicad_sym`) and footprint (`.kicad_mod`) library containing R, LED, and Conn_01x02 |

!!! tip "Don't have libraries?"
    You can download free KiCad libraries from [https://www.kicad.org/libraries/](https://www.kicad.org/libraries/) — WireFrame loads them natively.

---

## Step 1 — Create a Project

1. Launch WireFrame.
2. Go to **File → New Project…**
3. Choose a folder and name it `LED_Board.prjxml`.
4. Click **Create**.

The **Project Structure** panel now shows your empty project.

![Step1 New Project](../img/tutorial/step1-new-project.png)


!!! tip "Importing from other EDA tools"
    Already have a design in KiCad, Altium, or Eagle? Use **File → Import** instead. See [Projects & Files — Importing](../projects.md#importing-projects-from-other-eda-tools) for details.

---

## Step 2 — Load Libraries

### Load symbol libraries

1. Go to **File → New Schematic** to create a schematic document.
2. In the **Library** panel (right side), click **Load Symbols…**
3. Select your `.kicad_sym` file(s) containing `R`, `LED`, and `Conn_01x02`.
4. Wait for parsing — symbol names appear in the list.

### Load footprint libraries

1. Go to **File → New PCB** to create a PCB document.
2. In the **Library** panel, click **Load Footprints…**
3. Select your `.kicad_mod` file(s) containing `R_0805`, `LED_0805`, and `PinHeader_1x02`.
4. Footprint names appear in the list.

![Step2 Libraries](../img/tutorial/step2-libraries.png)


---

## Step 3 — Draw the Schematic

Switch to the schematic tab (click the schematic tab at the top of the editor).

### 3.1 Place the components

| Component | How to find it | Designator |
|---|---|---|
| **Resistor** | Search `R` in Library panel → double-click | R1 |
| **LED** | Search `LED` → double-click | D1 |
| **Connector** | Search `Conn_01x02` → double-click | J1 |

For each component:

1. Double-click its name in the Library panel.
2. Move the mouse to position it on the schematic.
3. Press ++r++ to rotate if needed.
4. **Left-click** to place.

Arrange the symbols from left to right as **J1 → R1 → D1**, leaving enough space for orthogonal wires. The placement clip below shows the intended result.

<video controls width="100%">
  <source src="../img/tutorial/step3-place-components.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


### 3.2 Edit component properties

Click each component and set its properties in the **Properties** panel:

| Component | Designator | Value | Footprint |
|---|---|---|---|
| Resistor | `R1` | `330Ω` | `R_0805_2012Metric` |
| LED | `D1` | `Red` | `LED_0805_2012Metric` |
| Connector | `J1` | `Power` | `PinHeader_1x02_P2.54mm_Vertical` |

![Step3 Properties](../img/tutorial/step3-properties.png)


### 3.3 Wire the circuit

1. Press ++w++ to activate the **Wire** tool.
2. **Wire 1**: Click on **J1 pin 1** → click on **R1 pin 1**. The wire connects them.
3. **Wire 2**: Click on **R1 pin 2** → click on **D1 anode (A)**.
4. **Wire 3**: Click on **D1 cathode (K)** → click on **J1 pin 2**. This closes the loop.
5. Press ++esc++ to exit wire mode.

<video controls width="100%">
  <source src="../img/tutorial/step3-wiring.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


### 3.4 Save the schematic

Press ++ctrl+s++ and save as `LED_Board.schxml`.

![Step3 Complete](../img/tutorial/step3-complete.png)


---

## Step 4 — Convert Schematic to PCB

1. With the schematic active, go to **Project → Convert to PCB**.
2. A new PCB document opens automatically with:
    - All three footprints loaded (clustered together).
    - Ratsnest lines showing the connections to route.

![Step4 Converted](../img/tutorial/step4-converted.png)


!!! warning "Check footprint assignments"
    If a component shows as "missing footprint", go back to the schematic and verify the Footprint field is set correctly in the Properties panel.

---

## Step 5 — Place Footprints

Spread the footprints out on the board:

1. Select the **Select** tool (default, or press ++esc++).
2. **Click and drag** each footprint to a good position.
3. Press ++r++ to rotate if needed.

Suggested layout: keep **J1** near the board edge, with **R1** between the connector and **D1**, while preserving room for routing and silkscreen. Use the placement media below as the visual reference.

| Shortcut | Action |
|---|---|
| Click + drag | Move footprint |
| ++r++ | Rotate 90° |
| ++f++ | Flip to back side |

<video controls width="100%">
  <source src="../img/tutorial/step5-placement.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

## Step 6 — Define the Board Outline

1. In the **Layer** panel, click **Edge.Cuts** to set it as the active layer.
2. Select the **Draw Rectangle** tool from the toolbar.
3. Click and drag to draw a rectangle around all three footprints.
4. Leave some margin (~50 mil) between footprints and the edge.

![Step6 Outline](../img/tutorial/step6-outline.png)


---

## Step 7 — Route Traces

1. Press ++x++ to activate the **Route Trace** tool.
2. Click on **J1 pad 1** to start a trace → route to **R1 pad 1** → click to finish.
3. Click on **R1 pad 2** → route to **D1 anode pad** → click to finish.
4. Click on **D1 cathode pad** → route to **J1 pad 2** → click to finish.

As you complete each trace, the corresponding ratsnest line disappears.

| Action | Input |
|---|---|
| Start / add vertex | Left-click |
| Finish on pad | Left-click on target pad |
| Cancel | Right-click or ++esc++ |

<video controls width="100%">
  <source src="../img/tutorial/step7-routing.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

## Step 8 — Run DFM Check

1. Go to **Tools → DFM Check**.
2. Click **Run DFM**.
3. Review the results:
    - **0 errors** = ready to export :material-check-circle:{ style="color: green" }
    - If errors appear, double-click each one to zoom to the issue and fix it.

![Step8 Dfm](../img/tutorial/step8-dfm.png)


---

## Step 9 — Export Fabrication Files

### Gerber export

1. Go to **File → Export → Gerber…**
2. Select layers: **F.Cu**, **F.SilkS**, **F.Mask**, **Edge.Cuts**.
3. Choose an output folder.
4. Click **Export**.

### BOM export

1. Go to **File → Export → BOM…**
2. Save as `LED_Board_BOM.csv`.

The BOM contains:

| Designator | Value | Footprint | Layer |
|---|---|---|---|
| R1 | 330Ω | R_0805_2012Metric | Top |
| D1 | Red | LED_0805_2012Metric | Top |
| J1 | Power | PinHeader_1x02_P2.54mm_Vertical | Top |

### Verify with Gerber Viewer

1. Go to **Tools → Gerber Viewer**.
2. Open the generated `F.Cu.gbr` file.
3. Verify traces and pads look correct.

<video controls width="100%">
  <source src="../img/tutorial/step9-export.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

## Done! :material-check-decagram:{ style="color: #00E5FF" }

You have completed a full design cycle:

```
Project → Schematic → PCB → Route → DFM → Export
```

| Deliverable | File |
|---|---|
| Project | `LED_Board.prjxml` |
| Schematic | `LED_Board.schxml` |
| PCB | `LED_Board.pcbxml` |
| Gerber files | `F.Cu.gbr`, `F.SilkS.gbr`, `F.Mask.gbr`, `Edge.Cuts.gbr` |
| BOM | `LED_Board_BOM.csv` |

---

## Quick Reference — Shortcuts Used

| Action | Shortcut |
|---|---|
| Save | ++ctrl+s++ |
| Undo | ++ctrl+z++ |
| Place wire | ++w++ |
| Route trace | ++x++ |
| Rotate | ++r++ |
| Flip | ++f++ |
| Cancel / Select | ++esc++ |
| Delete | ++delete++ |

---

## Next Steps

Now that you know the basic workflow, explore more:

| Topic | Link |
|---|---|
| Add net labels and power symbols | [Wiring & Nets](../schematic/wiring-and-nets.md) |
| Multi-layer routing with vias | [Routing](../pcb/routing.md) |
| Add a ground plane | [Zones & Planes](../pcb/zones-and-planes.md) |
| Preview in 3D | [3D Viewer](../advanced/3d-viewer.md) |
| Import KiCad / Altium projects | [Projects & Files](../projects.md#importing-projects-from-other-eda-tools) |
| All keyboard shortcuts | [Shortcuts](../advanced/shortcuts.md) |
