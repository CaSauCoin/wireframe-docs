# Tutorial: A Simple LED Board

This tutorial covers the complete user workflow with a small connector–resistor–LED circuit. The goal is to practice project organization, library use, schematic checks, PCB update, routing, DFM/DRC, and release output.

### Image — Finished tutorial project

!!! note "Image needed"
    Capture the final v1.5.47 schematic and PCB side by side, with the project tree visible. The previous tutorial image was a 1×1 placeholder.

## Before you start

Prepare an approved symbol and footprint for a resistor, LED, and two-pin connector. Open **View → Local Library Manager** and confirm all six assets in the active inventory.

Create a project from **File → New → New Project (.prjxml)** and keep it in a dedicated folder.

### Short video — Create the tutorial project

!!! note "Video needed"
    Record 10–15 seconds showing the current New Project command, folder choice, project name, and result in Project Structure. The older media files were empty placeholders.

## 1. Create the schematic

1. Add a new schematic to the project and save it.
2. Place the connector, resistor, and LED.
3. Arrange them so signal flow is easy to read.
4. Set unique designators, values, and footprint assignments.
5. Wire the supply path through the resistor and LED, then return to the connector.

Choose the resistor from the actual supply voltage, LED forward voltage, and target current. The example value is not a universal engineering recommendation.

### Image — Completed LED schematic

!!! note "Image needed"
    Capture the three placed symbols, readable values/designators, exact pin connections, and assigned footprint field in v1.5.47.

## 2. Check the schematic

Run **Electrical Rules Check**. Resolve incorrect pin connections, missing values, duplicate designators, and any blocking connectivity issue. Review LED polarity and connector pin numbering against their datasheets.

Do not continue merely because the drawing looks connected; the electrical check and footprint mapping are separate requirements.

### Short video — Fix one ERC issue

!!! note "Video needed"
    Record 15–20 seconds showing one selected ERC issue, its correction, and a clean rerun.

## 3. Update the PCB

With the schematic active, select **Tools → Update Schematic to PCB**. Choose the intended target board, review the imported footprints, and confirm that their designators and ratsnest connections match the schematic.

Draw a closed outline on **Edge.Cuts**, then place the connector near an accessible edge and leave practical space around the LED and resistor.

### Image — PCB after schematic update

!!! note "Image needed"
    Capture the board outline, three footprints, and unrouted ratsnest immediately after update. Show the active Edge.Cuts layer or Layers panel.

## 4. Route and inspect

Use the Route Trace tool to complete each connection. As each electrical path becomes complete, confirm that its ratsnest line clears. Keep copper away from the board edge and follow the active net-class width and clearance.

After routing, inspect LED and connector orientation, silkscreen readability, pad-to-track endpoints, and any layer changes.

### Short video — Route the LED board

!!! note "Video needed"
    Record 15–20 seconds showing one route started from a pad, completed at its target, and the corresponding ratsnest line disappearing.

## 5. Run DFM/DRC

Open **DFM & DRC Check**, run the full check, and resolve every release-blocking error. Review warnings one by one; record why a warning is acceptable rather than hiding it.

### Image — Clean DFM/DRC result

!!! note "Image needed"
    Capture the final routed sample board with the clean DFM/DRC summary visible. The previous tutorial result image was a 1×1 placeholder.

## 6. Generate release output

Open **File → Export → Fabrication Outputs (Gerber/Drill/BOM)** or **Tools → Fabrication Output**. Include the required Gerber, drill, BOM, connectivity, and manifest outputs for the selected manufacturer.

Inspect representative copper, mask, silkscreen, drill, and board-outline data in the available preview or a trusted viewer. Confirm that every output belongs to the same saved board revision.

### Short video — Verify the fabrication package

!!! note "Video needed"
    Record 20–30 seconds showing package generation, output inventory, and visual review of representative layers. The previous export video was an empty file.

## Completion checklist

- Project, schematic, and PCB are saved in the intended folder.
- Symbols, footprints, pin numbers, and polarity are verified.
- ERC and DFM/DRC have no unresolved blocking errors.
- No unintended ratsnest connection remains.
- Board outline, drills, masks, and BOM are present in the release package.
- The archived package identifies the correct board revision.

## Continue learning

- [Projects and Files](../projects.md)
- [Wiring and Nets](../schematic/wiring-and-nets.md)
- [Routing](../pcb/routing.md)
- [Fabrication and Export](../pcb/fabrication-and-export.md)
- [AI-Assisted Design](ai-design.md)
