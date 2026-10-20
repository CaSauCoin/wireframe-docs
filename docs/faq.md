# FAQ and Troubleshooting

Use this page to diagnose common release issues. Start with the check that matches the visible symptom, then record the exact message shown by WireFrame before changing project data.

## Installation and startup

??? question "WireFrame does not start or shows a blank workspace"
    1. Confirm that your operating system and graphics driver meet the requirements in [Installation](installation.md).
    2. Restart WireFrame once without reopening an existing project.
    3. If the application opens, load the project from **File → Open Project (.prjxml)** or **Open File** and note which document triggers the issue.
    4. If it still fails, attach the operating system, WireFrame version, and startup log to the issue report.

    Resetting configuration can help with a damaged workspace state, but it also removes saved session and layout preferences. Use it only after reviewing [Configuration and Session](reference/config-and-session.md#reset-wireframe-preferences).

??? question "macOS or Windows blocks the first launch"
    Use the operating system's **Open Anyway** or **More info → Run anyway** action only when the installer came from the official WireFrame release channel. Do not disable system security globally.

??? question "My previous project does not reopen automatically"
    Open it manually from **File → Open Project (.prjxml)** or **Open File**. If the files have moved or a removable drive is unavailable, WireFrame cannot restore the saved path. A normal close stores the current session for the next launch.

## Projects and libraries

??? question "Which external project formats can I import?"
    The project importer supports KiCad project files (`.kicad_pro` and legacy `.pro`). Altium and Eagle *project* import are not part of the current release workflow. Altium *library* files can be imported through **View → Local Library Manager**.

??? question "My KiCad symbols or footprints do not appear"
    Open **View → Local Library Manager**, select the source, and check that its parts are listed and ticked (a hidden part does not appear in the Library panel; **Hide power & logos** hides power symbols). Confirm that the source contains KiCad symbol or footprint files and has not been moved since it was added.

??? question "How do I import an Altium library?"
    Open **View → Local Library Manager**, select **Add library ▾ → Altium library (SchLib, PcbLib, IntLib)...**, and choose a `.SchLib`, `.PcbLib`, `.IntLib`, or `.LibPkg` file. Review the imported symbol and footprint before using it in a design. See [Library Import and Management](libraries/library-converter.md).

??? question "A component is missing from an AI-generated design"
    Confirm the exact part number, package, and pin count. On the card, **Create** searches WireFrame's published library first. Otherwise type `/fix <refdes> <what is wrong>` in the AI panel and attach the manufacturer datasheet with **Attach datasheet...**; to build every missing part at once, ask *"fix the parts that cannot be used yet"*. Review both generated assets using [Fix or Create a Component](ai/component-generator.md).

??? question "How do I link a footprint to a symbol?"
    For a placed component, select it and use **Properties → General → Linked Footprint → Link Footprint & Save to File**. For the library symbol, use the Library Manager's **Footprint** tab → **Link a footprint file...**. Confirm the package name, pad count, pad numbering, and orientation against the datasheet before **Update Schematic to PCB**. See [Symbol Libraries](libraries/symbols-library.md#assign-a-footprint).

## Schematic and PCB

??? question "A wire does not connect to a pin"
    Zoom in and place the wire endpoint on the pin connection point with grid snapping enabled. If a pin or imported symbol is off-grid, correct the symbol or its placement instead of drawing a nearly connected wire. Re-run ERC afterward.

??? question "Ratsnest lines remain after routing"
    Verify that each track endpoint reaches the intended pad or existing track, that all items share the same net, and that the route changes layer through a valid via. Re-run the PCB checks after correcting the connection.

??? question "DFM or DRC reports many clearance errors"
    Review the active design rules and net classes first. Open each violation, identify the two objects involved, and decide whether to reroute, move an item, or correct the applicable rule. Do not suppress a violation merely to obtain a clean report.

??? question "Copper zones show gaps or stale geometry"
    Open **View → Zone Manager**, confirm each zone's net, layer, clearance, and priority, then select **Refill** after routing or placement changes. A row at 0% has not been filled yet, or has no copper of its net to join. Clearances around objects on other nets are expected. A row marked `×2` usually means **GND plane** was pressed twice — delete the extra zone.

??? question "The canvas feels slow or stutters"
    Open **View → Performance HUD**. The overlay shows the frame rate on screen and the work per frame, then splits each frame into phases with mean and worst times:

    | Phase | If it dominates |
    |---|---|
    | **panels (CPU)** — with indented rows such as `pcb canvas`, `schematic canvas`, `AI copilot panel`, `review: BOM cards` | One panel is expensive to draw; the indented row names it. Closing or docking that panel is the quick test |
    | **upload + draw (GL)** | The graphics driver is the bottleneck — very large boards, or a weak or software GPU |
    | **platform windows (one swap each)** | Many panels are floating as separate windows; each costs a swap. Dock them back into the main window |
    | **swap (main window)** | Waiting on the display (vsync); usually not a problem in itself |

    The HUD also shows how many input events were queued and how far the pointer lagged behind the real cursor, and the size of the last frame's draw data. It measures only while it is open.

## Simulation

??? question "The Run button is disabled"
    Check the readiness information in **Simulation Workbench → Setup**. A run needs a usable engine, supported analysis, connected simulation scope, and no blocking model issue. Correct the reported item and run **Preflight** again.

??? question "WireFrame cannot find an installed simulation engine"
    Open **Preferences → Simulation**. Leave the executable path empty only when the engine is available on the system `PATH`; otherwise select the executable directly. Return to **Setup → Engine** and confirm that its status is usable.

??? question "Preflight reports a missing model"
    Open **Models**, identify the component and requested model, and import the correct vendor SPICE model. Verify its pin order against the datasheet before running Preflight again. You may also simulate an independent block that does not include the unresolved component.

??? question "An assertion is Not measured instead of Failed"
    The run did not produce the signal or metric needed for the comparison. Check the signal name, analysis type, circuit scope, measurement window, and engine log. **Not measured** is intentionally not treated as a pass.

??? question "Two engines produce different results"
    Compare the analysis, startup options, sources, loads, model revisions, and measurement windows. Keep both logs with the project when reporting the difference.

## AI Copilot

??? question "How do I configure AI Copilot?"
    Open **Preferences → AI Assistant** (or **AI settings...** in the Copilot menu) and choose who pays: **WireFrame credit** (your plan's credit, no key), or your own key at **OpenRouter**, **DeepSeek** or **Google AI**, then **Save & test**. If a model returns errors or empty answers, pick another one in **Models**. Never include a key in screenshots, shared projects, or support reports. See [Models, Credit and Your Data](ai/models-and-credits.md).

??? question "AI Copilot is not responding"
    Check the network connection, API-key validity, provider credit or rate limit, and the visible error message. Retry only after the current request has clearly stopped; repeated clicks can create duplicate provider charges.

??? question "Does Copilot edit the design automatically?"
    Treat every generated proposal as unverified design input. Review its component, connection, block, and analysis tabs before applying changes. Afterward, run the relevant ERC, DFM/DRC, and simulation checks.

??? question "Copilot says a signal passes without a requirement"
    A pass or fail requires an explicit criterion. Add a testbench assertion based on the product requirement or datasheet and rerun the simulation. A general AI assessment is not a replacement for a measurable limit.

## Export and release checks

??? question "Fabrication output is empty or incomplete"
    Confirm that the board outline is closed, the selected layers contain the intended data, and the current board revision was saved before export. Inspect representative Gerbers and drill files in a viewer before sending the package to a manufacturer.

??? question "What should I review before sharing a manufacturing package?"
    Check the board revision, Gerber layers, plated and non-plated drill outputs where applicable, IPC-D-356A, BOM, and package manifest. Keep the DFM/DRC result with the release evidence.

## Reporting an issue

The quickest way is **Help → Report a Bug...** (or **Help → Request a Feature...**) inside WireFrame. Write a **Summary** and **Details**, optionally **Attach image...** (PNG or JPG; files over 10 MB may be refused), keep **Include app version and OS** ticked, and select **Send**. If sending fails, your text is kept so you can **Try again** later.

Whichever channel you use, include:

- WireFrame version and operating system.
- A short sequence that reproduces the issue.
- The exact error message and relevant log excerpt.
- A screenshot with credentials and proprietary data removed.
- For slowness: a screenshot of **View → Performance HUD** taken while it happens. When the app cannot be clicked — or for a log over time — start WireFrame from a terminal with the environment variable `WF_PERF_LOG=1`; it prints a one-line timing summary every 2 seconds.
- A minimal project copy when it is safe to share.

Check the [Changelog](changelog.md) first. Never attach API keys, customer data, or private paths.
