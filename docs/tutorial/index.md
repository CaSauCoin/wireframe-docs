# Tutorial: A Simple LED Board

This tutorial covers the complete user workflow with a small connector–resistor–LED circuit. The goal is to practice project organization, library use, schematic checks, PCB update, routing, DFM/DRC, and release output.

### Image — Finished tutorial project

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the final v1.5.47 schematic and PCB side by side, with the project tree visible. The previous tutorial image was a 1×1 placeholder.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Before you start

Prepare an approved symbol and footprint for a resistor, LED, and two-pin connector. Open **View → Local Library Manager** and confirm all six assets in the active inventory.

Create a project from **File → New → New Project (.prjxml)** and keep it in a dedicated folder.

### Short video — Create the tutorial project

!!! note "Video production brief"
    1. **Prepare:** Create a neutral tutorial folder and choose the exact fictional project name used throughout this tutorial.
    2. **Opening shot (1–2 s):** Start on **File → New → New Project (.prjxml)**.
    3. **Action shot (5–8 s):** Choose the folder, enter the project name, and confirm creation.
    4. **Result shot (2–3 s):** Hold on the new tutorial project in **Project Structure**.
    5. **Deliver:** Export a **10–15 second** 1080p MP4 and replace the older empty media.

## 1. Create the schematic

1. Add a new schematic to the project and save it.
2. Place the connector, resistor, and LED.
3. Arrange them so signal flow is easy to read.
4. Set unique designators, values, and footprint assignments.
5. Wire the supply path through the resistor and LED, then return to the connector.

Choose the resistor from the actual supply voltage, LED forward voltage, and target current. The example value is not a universal engineering recommendation.

### Image — Completed LED schematic

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the three placed symbols, readable values/designators, exact pin connections, and assigned footprint field in v1.5.47.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 2. Check the schematic

Run **Electrical Rules Check**. Resolve incorrect pin connections, missing values, duplicate designators, and any blocking connectivity issue. Review LED polarity and connector pin numbering against their datasheets.

Do not continue merely because the drawing looks connected; the electrical check and footprint mapping are separate requirements.

### Short video — Fix one ERC issue

!!! note "Video production brief"
    1. **Prepare:** Leave one deliberate ERC issue in the tutorial schematic and resolve every unrelated issue beforehand.
    2. **Opening shot (2 s):** Show the selected ERC row and highlighted schematic location.
    3. **Action shot (7–10 s):** Navigate to the issue, apply the documented correction, and run ERC again.
    4. **Result shot (3–4 s):** Hold on the clean rerun and corrected connection.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 with the error text readable before correction.

## 3. Update the PCB

With the schematic active, select **Tools → Update Schematic to PCB**. Choose the intended target board, review the imported footprints, and confirm that their designators and ratsnest connections match the schematic.

Draw a closed outline on **Edge.Cuts**, then place the connector near an accessible edge and leave practical space around the LED and resistor.

### Image — PCB after schematic update

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the board outline, three footprints, and unrouted ratsnest immediately after update. Show the active Edge.Cuts layer or Layers panel.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 4. Route and inspect

Use the Route Trace tool to complete each connection. As each electrical path becomes complete, confirm that its ratsnest line clears. Keep copper away from the board edge and follow the active net-class width and clearance.

After routing, inspect LED and connector orientation, silkscreen readability, pad-to-track endpoints, and any layer changes.

### Short video — Route the LED board

!!! note "Video production brief"
    1. **Prepare:** Arrange the tutorial footprints so one short unrouted connection is centered and unobstructed.
    2. **Opening shot (2 s):** Hold on the source pad, destination pad, and ratsnest line.
    3. **Action shot (7–10 s):** Start routing at the source pad, place clean corners, and finish on the target pad.
    4. **Result shot (3–4 s):** Hold on the selected completed route with the corresponding ratsnest line gone.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and keep route geometry readable.

## 5. Run DFM/DRC

Open **DFM & DRC Check**, run the full check, and resolve every release-blocking error. Review warnings one by one; record why a warning is acceptable rather than hiding it.

### Image — Clean DFM/DRC result

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the final routed sample board with the clean DFM/DRC summary visible. The previous tutorial result image was a 1×1 placeholder.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 6. Generate release output

Open **File → Export → Fabrication Outputs (Gerber/Drill/BOM)** or **Tools → Fabrication Output**. Include the required Gerber, drill, BOM, connectivity, and manifest outputs for the selected manufacturer.

Inspect representative copper, mask, silkscreen, drill, and board-outline data in the available preview or a trusted viewer. Confirm that every output belongs to the same saved board revision.

### Short video — Verify the fabrication package

!!! note "Video production brief"
    1. **Prepare:** Use the finished tutorial PCB with revision metadata and a clean, neutral output folder.
    2. **Opening shot (2–3 s):** Show the fabrication output controls and board revision before generation.
    3. **Action shot (10–15 s):** Generate the package, open its inventory, then open representative copper, solder-mask, silkscreen, outline, and drill outputs in the viewer.
    4. **Result shot (4–6 s):** Hold on a readable layer view and the complete expected file inventory.
    5. **Deliver:** Export a **20–30 second** 1080p MP4 and replace the previous empty file.

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
