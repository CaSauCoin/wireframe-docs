# Tutorial: A Simple LED Board

This tutorial takes one small circuit — a 5 V input, a resistor, and an LED — from an empty project to a fabrication package. It practises the whole workflow: project, libraries, schematic, ERC, PCB update, routing, DFM/DRC, and release output. Allow about 25 minutes.

### Image — Finished tutorial project

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the final v1.5.47 schematic and PCB side by side, with the project tree visible. The previous tutorial image was a 1×1 placeholder.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## The circuit

| Ref | Part | Value | Footprint (example) |
|---|---|---|---|
| J1 | 2-pin connector, 2.54 mm | `5V IN` | 1×02 pin header, 2.54 mm |
| R1 | Resistor | `330` | 0805 (2012 metric) |
| D1 | LED, red | `RED` | 0805 (2012 metric) |

J1 pin 1 is +5 V and pin 2 is GND. The current flows J1.1 → R1 → D1 anode → D1 cathode → J1.2.

**Choosing R1.** With a 5 V supply, a red LED dropping about 2.0 V, and a target of about 10 mA: R = (5 − 2.0) / 0.010 = 300 Ω. The next standard value up, 330 Ω, gives (5 − 2.0) / 330 ≈ 9 mA. Use your LED's datasheet forward voltage and current if they differ.

## Before you start

1. Create the project: **File → New → New Project (.prjxml)...**, choose an empty folder, name it `led_board`, and select **Create**.
2. Make the three parts available. Either add a KiCad library that has them with **View → Local Library Manager → Add library ▾**, or install them from WireFrame's catalog: in the **Library** panel open **Online Store**, search for each part, and select **Install**.

### Short video — Create the tutorial project

!!! note "Video production brief"
    1. **Prepare:** Create a neutral tutorial folder and choose the exact fictional project name used throughout this tutorial.
    2. **Opening shot (1–2 s):** Start on **File → New → New Project (.prjxml)**.
    3. **Action shot (5–8 s):** Choose the folder, enter the project name, and confirm creation.
    4. **Result shot (2–3 s):** Hold on the new tutorial project in **Project Structure**.
    5. **Deliver:** Export a **10–15 second** 1080p MP4 and replace the older empty media.

## 1. Create the schematic

1. Right-click `led_board` in **Project Structure** → **Add New Schematic**, then press ++ctrl+s++ and save it as `led_board.schxml`.
2. In the **Library** panel (**Local Library** tab), type the part name in **Filter...** and **drag** the connector, the resistor, and the LED onto the sheet. Leave space between them.
3. Rotate a part with ++space++ (or ++r++ while it is selected) so the circuit reads left to right.
4. Select each part and fill **Properties → General → Info**: **Designator** `J1`, `R1`, `D1`, and **Value** `5V IN`, `330`, `RED`. Check **Linked Footprint**; if it is empty, use **Link Footprint & Save to File** and pick the footprint from the table above.
5. Press ++w++ and draw the wires: click J1 pin 1, then R1 pin 1 to finish; R1 pin 2 to the LED **anode**; the LED **cathode** to J1 pin 2. ++esc++ leaves the Wire tool.
6. Press ++g++ and click near J1 pin 2 to place a **GND** symbol, then wire it to the pin. Optionally press ++p++ for a power symbol on J1 pin 1 and set its **Value** to `+5V`.
7. Save (++ctrl+s++).

Check the LED orientation against its datasheet: the anode goes towards R1, the cathode towards GND.

### Image — Completed LED schematic

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the three placed symbols, readable values/designators, exact pin connections, and assigned footprint field in v1.5.47.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 2. Check the schematic

Select **Tools → Electrical Rules Check (ERC)**, then **Run Project-Wide ERC Analysis**. The panel should show **0 Errors**. Typical first-time problems:

- **E302 Critical pin unconnected** — a wire stops just short of a pin. Redraw it so it ends on the pin.
- **E101 Duplicate designator** — two parts named the same; rename one.
- **W200 Net with only one connection** — a wire or label that goes nowhere.

Run the check again after each fix. A drawing that *looks* connected is not enough; ERC and the footprint links are separate requirements.

### Short video — Fix one ERC issue

!!! note "Video production brief"
    1. **Prepare:** Leave one deliberate ERC issue in the tutorial schematic and resolve every unrelated issue beforehand.
    2. **Opening shot (2 s):** Show the selected ERC row and highlighted schematic location.
    3. **Action shot (7–10 s):** Navigate to the issue, apply the documented correction, and run ERC again.
    4. **Result shot (3–4 s):** Hold on the clean rerun and corrected connection.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 with the error text readable before correction.

## 3. Update the PCB

1. Right-click the project → **Add New PCB**, and save it as `led_board.pcbxml`.
2. Make the schematic tab active and select **Tools → Update Schematic to PCB**. J1, R1, and D1 arrive on the board in a grid, joined by ratsnest lines.
3. Draw the board outline: in the **Layers** panel click **Edge.Cuts**, choose **Draw Rectangle** (++r++), and drag a rectangle about **30 × 20 mm** around the parts. (You can also type `/board 30x20 mm` in AI Copilot, or import a drawing with **File → Import → CAD Outline**.)
4. Drag J1 to an edge so the connector is reachable, and place R1 and D1 nearby. Rotate with ++space++.

### Image — PCB after schematic update

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the board outline, three footprints, and unrouted ratsnest immediately after update. Show the active Edge.Cuts layer or Layers panel.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 4. Route and inspect

1. Click **F.Cu** in the **Layers** panel.
2. Press ++x++, click a pad, click to add corners, and click the destination pad. Route the three connections. ++esc++ ends a route; ++backspace++ takes back the last corner.
3. Each finished connection clears its ratsnest line. Nets named `GND` or starting with `+` (such as `+5V`) use the **Power** class — 20 mil tracks, 15 mil clearance; the R1–D1 net uses **Default** — 10 mil tracks, 6 mil clearance. Both are plenty for 9 mA (see [Design Rules](../pcb/design-rules.md)).
4. Optional: open **View → Zone Manager**, choose **GND plane ▾ → B.Cu**, then **Refill**, to pour ground on the back.

After routing, check LED and connector orientation, silkscreen readability, and that every track ends on its pad.

### Short video — Route the LED board

!!! note "Video production brief"
    1. **Prepare:** Arrange the tutorial footprints so one short unrouted connection is centered and unobstructed.
    2. **Opening shot (2 s):** Hold on the source pad, destination pad, and ratsnest line.
    3. **Action shot (7–10 s):** Start routing at the source pad, place clean corners, and finish on the target pad.
    4. **Result shot (3–4 s):** Hold on the selected completed route with the corresponding ratsnest line gone.
    5. **Deliver:** Export a **15–20 second** 1080p MP4 and keep route geometry readable.

## 5. Run DFM/DRC

Open **Tools → DFM & DRC Check Panel...** and select **Run DFM Analysis**. Click each error to jump to it, fix it, and run again until the result reads **Found 0 Error(s)**. Review each warning; record why an accepted warning is fine rather than hiding it.

### Image — Clean DFM/DRC result

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the final routed sample board with the clean DFM/DRC summary visible. The previous tutorial result image was a 1×1 placeholder.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## 6. Generate release output

1. Save the board.
2. Select **File → Export → Fabrication Outputs (Gerber/Drill/BOM)...**.
3. Open **Options**, set **Revision** to `A`, and leave the other options at their defaults.
4. Select **Generate Files to Memory**, read the file list and any warnings, then **Save Package (.zip)...**.
5. Unzip the package and open the Gerber and drill files in a full Gerber viewer (KiCad GerbView, gerbv, or your manufacturer's viewer) before ordering.

### Short video — Verify the fabrication package

!!! note "Video production brief"
    1. **Prepare:** Use the finished tutorial PCB with revision metadata and a clean, neutral output folder.
    2. **Opening shot (2–3 s):** Show the fabrication output controls and board revision before generation.
    3. **Action shot (10–15 s):** Generate the package, open its inventory, then open representative copper, solder-mask, silkscreen, outline, and drill outputs in the viewer.
    4. **Result shot (4–6 s):** Hold on a readable layer view and the complete expected file inventory.
    5. **Deliver:** Export a **20–30 second** 1080p MP4 and replace the previous empty file.

## Completion checklist

- Project, schematic, and PCB are saved in the project folder.
- R1 = 330 Ω and the LED polarity are correct; every symbol has its footprint.
- ERC shows no errors; DFM/DRC shows no errors.
- No ratsnest line remains.
- The package contains copper, mask, silkscreen, outline, drill files, and the BOM, all from revision `A`.

## Continue learning

- [Projects and Files](../projects.md)
- [Wiring and Nets](../schematic/wiring-and-nets.md)
- [Routing](../pcb/routing.md)
- [Fabrication and Export](../pcb/fabrication-and-export.md)
- [AI-Assisted Design](ai-design.md)
