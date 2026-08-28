# FAQ & Troubleshooting

Common questions and solutions for WireFrame EDA issues.

---

## Installation Issues

??? question "The application does not start / shows a blank window"
    **Possible causes and solutions:**

    1. **Missing OpenGL driver** — WireFrame requires OpenGL 3.3+. Check your GPU driver:
        - Linux: `glxinfo | grep "OpenGL version"` — should show 3.3 or higher.
        - Windows: Update your GPU drivers from the manufacturer (NVIDIA, AMD, Intel).
    2. **Wayland compatibility** — On Linux with Wayland, try forcing X11:
        ```bash
        GDK_BACKEND=x11 wireframe
        ```
    3. **Missing shared libraries** (Linux) — Install missing dependencies:
        ```bash
        sudo apt-get install -f
        ```
    4. **Corrupted config file** — Delete the config and restart:
        ```bash
        rm ~/.config/wireframe/user_config.json
        ```

??? question "macOS: 'WireFrame cannot be opened because it is from an unidentified developer'"
    This is a **Gatekeeper** restriction. Follow these steps:

    1. Open **Terminal** and run:
        ```bash
        sudo xattr -cr /Applications/WireFrame.app
        ```
    2. Then go to **System Settings → Privacy & Security** and click **Open Anyway**.
    3. Launch WireFrame again — it should open without the warning.

    See [Installation — macOS](installation.md#3-macos-installation) for full details.

??? question "Windows: SmartScreen blocks the installer"
    Windows SmartScreen may flag the installer because it has not yet accumulated enough reputation:

    1. Click **More info** on the SmartScreen dialog.
    2. Click **Run anyway**.
    3. The installer will proceed normally.

    This is expected for new or infrequently downloaded software.

??? question "Linux: `dpkg` fails with dependency errors"
    Run the following after the failed `dpkg` install:
    ```bash
    sudo apt-get install -f
    ```
    This will download and install any missing dependencies, then complete the WireFrame installation.

---

## Activation & Sign-In

??? question "I cannot activate — the server is not responding"
    - Check your **internet connection**.
    - Verify the activation server URL is correct (contact support if needed).
    - If you're behind a **corporate proxy**, ensure the proxy allows HTTPS connections to the activation server.
    - Try again after a few minutes — the server may be temporarily unavailable.

??? question "How do I reset my activation / log out?"
    Delete the configuration file:

    - **Linux**: `~/.config/wireframe/user_config.json`
    - **Windows**: `%APPDATA%\WireFrame\user_config.json`
    - **macOS**: `~/Library/Application Support/WireFrame/user_config.json`

    On next launch, the activation overlay will appear again.

??? question "Can I use WireFrame on multiple computers with one license?"
    Check your license terms. Typically, a single license allows activation on a limited number of devices. Contact support for clarification.

---

## Libraries

??? question "My KiCad symbols / footprints do not load"
    **Common causes:**

    1. **Wrong file format** — WireFrame supports KiCad v6/v7/v8 `.kicad_sym` and `.kicad_mod` files. Older `.lib` and `.mod` formats may have limited support.
    2. **File encoding** — Ensure files are UTF-8 encoded.
    3. **Corrupted files** — Open the library file in a text editor and check for syntax errors.
    4. **Parser errors** — Check the Logger overlay for error messages during loading. They may indicate which symbol/footprint failed to parse.

??? question "How do I create custom footprints?"
    Use the built-in **Footprint Wizard** (**Tools → Footprint Wizard**):

    1. Configure pin count, layout (single, dual, grid, quad), pad size, and pitch.
    2. Preview the generated footprint in real time.
    3. Export to `.kicad_mod` format.

    See [Footprint Libraries](libraries/footprints-library.md#footprint-generator-footprint-wizard) for details.

??? question "How do I link a footprint to a symbol?"
    1. Load both symbol and footprint libraries.
    2. In the Library panel (schematic mode), right-click a symbol.
    3. Choose **Link Footprint** and select the corresponding footprint.
    4. Future instances of that symbol will automatically have the footprint assigned.

    See [Symbol Libraries](libraries/symbols-library.md#linking-footprints-to-symbols).

---

## Schematic Editor

??? question "Wires don't connect to pins — I see no junction dots"
    - Ensure the wire endpoint **exactly touches the pin tip**. Zoom in to verify alignment.
    - Wire snapping is grid-based — if the pin is off-grid, you may need to zoom in and place the wire endpoint manually.
    - Junction dots appear automatically when **three or more** connections meet at one point.

??? question "My net names are wrong or duplicated"
    - Check that **Net Labels** are placed correctly and their values match.
    - The netlist is rebuilt from wires and labels. Use **Properties panel** to verify the net name of a selected wire.
    - Conflicting net names can occur if two different labels are connected by the same wire — review the schematic for overlapping labels.

??? question "Undo/Redo does not work as expected"
    - Some operations (like loading libraries) are not undoable — they are immediate.
    - If undo seems stuck, check the **Logger** for error messages.
    - As a workaround, reload the file from disk (**File → Open** the same file).

---

## PCB Editor

??? question "Ratsnest lines don't disappear after routing"
    - Ensure the trace **connects exactly to the pad center** at both ends.
    - The ratsnest is recomputed after each routing action. If lines persist, the trace may not be on the correct **layer** or **net**.
    - Check the net assignment in the Properties panel after selecting the trace.

??? question "DFM/DRC shows many clearance errors"
    - Review your **Design Rules** (Tools → Design Rules) — the default clearance may be too tight for your design.
    - Common fixes:
        - Increase minimum clearance.
        - Increase trace width for power nets.
        - Reroute traces that pass too close to pads or other traces.
    - Double-click each violation to zoom to the problem area.

??? question "Zones (copper pours) look incorrect or have gaps"
    - Run **zone fill rebuild** after making changes to traces or footprints.
    - Check zone **priority** — higher priority zones override lower ones.
    - Verify the zone's **net assignment** and **clearance** settings.
    - Gaps around pads are expected (clearance areas) unless the pad is on the same net (thermal connections).

---

## Export & Fabrication

??? question "Gerber export produces empty files"
    - Ensure there is content on the layers you selected for export.
    - Check that the board has a valid **board outline** (Edge.Cuts layer).
    - Verify in the **Gerber Viewer** (Tools → Gerber Viewer) that the generated files contain data.

??? question "BOM CSV is missing components"
    - Only components with a **non-empty Value** property are included in the BOM.
    - Ensure footprints are **placed** on the PCB (not in the "available" list).

??? question "PDF export has wrong colors or missing elements"
    - PDF export converts colors to black/grey for printing. This is by design.
    - If elements are missing, ensure they are on **visible layers** before exporting.

??? question "What should be in the manufacturing archive?"
    For the 1.5.47 release workflow, prefer the coordinated fabrication package. Check for Gerber X2 layers, separate plated and unplated drill files, IPC-D-356A, BOM, and the package manifest. Open representative Gerbers in the built-in viewer and confirm the board revision before sending the archive.

---

## Simulation

??? question "The Run button is disabled"
    Check the readiness card and hover the disabled analysis or engine. **Run** requires a usable selected engine, connected nets in the selected scope, no blocking model issues, a supported analysis, and no simulation already in progress. Run **Preflight** after correcting the circuit or model library.

??? question "An external engine is installed but WireFrame cannot find it"
    Open **Preferences → Simulation**. Leave its path empty only when the executable is available on your system `PATH`; otherwise click **Browse…** and select it directly. Return to **Setup → Engine** and confirm the status is usable.

??? question "Preflight reports a missing model"
    Open the workbench **Models** tab and note the requested model and component designator. Import the correct vendor SPICE model, confirm that its pin order matches the datasheet, then run Preflight again. You can also simulate an independent block that does not contain the unresolved component.

??? question "Why is an assertion Not measured instead of Failed?"
    The selected run did not produce the signal or metric required for comparison. Check the signal name, analysis type, circuit scope, cursor/settling window, and engine log. **Not measured** intentionally never counts as a pass.

??? question "Different simulators produce different results"
    Confirm that both runs use the same analysis, startup settings, sources, loads, model version, and measurement window. Export both simulation logs when you need to compare the runs or report the difference.

---

## AI Copilot

??? question "Does Copilot edit the schematic automatically?"
    Design changes are presented as pending edits for review. Inspect the affected components, nets, and rationale before approving. After applying a proposal, run ERC, DFM, or simulation as appropriate.

??? question "Copilot says a signal passes, but I did not define a requirement"
    A pass/fail claim needs an explicit criterion. Add a testbench assertion derived from your product requirement or datasheet, then rerun the simulation. Copilot should report that no criterion exists rather than inventing a typical threshold.

---

## Performance

??? question "The application is slow or laggy"
    **Tips to improve performance:**

    1. **Reduce loaded libraries** — unload libraries you don't need for the current project.
    2. **Simplify zone fills** — complex zones with many cutouts take longer to compute.
    3. **Close unused tabs** — each open document consumes memory.
    4. **Check GPU acceleration** — ensure your system uses hardware OpenGL, not software rendering.
    5. **Reduce window size** — on very high-DPI displays, a smaller window may help.

??? question "3D Viewer is very slow"
    - Loading **STEP files** requires significant computation (mesh tessellation). First load is slow, but subsequent renders use cached meshes.
    - Use simpler 3D models if possible (low polygon count).
    - Close the 3D viewer when not needed to free GPU resources.

---

## Simulation

??? question "Simulation menu is disabled / NgSpice not found"
    WireFrame loads `libngspice` dynamically at runtime. If it's not installed:

    - **Linux**: `sudo apt-get install libngspice0-dev`
    - **macOS**: `brew install ngspice`
    - **Windows**: NgSpice is bundled with the installer — reinstall WireFrame if missing.

    Check the Logger for the message: `"NgSpice: library not found"`.

??? question "Simulation fails with 'singular matrix'"
    This usually indicates a topology problem:

    - A voltage source directly across another voltage source.
    - An inductor loop without any resistance.
    - **Fix**: Add small series resistances (0.01Ω) or check your circuit connections.

??? question "Waveform shows flat lines or no data"
    - Verify component values are set (not empty) in the Properties panel.
    - Check that the analysis type matches your source type (use pulse/sine sources for transient analysis).
    - Ensure the simulation time is long enough to see the expected behavior.
    - For oscillators: increase the simulation time — they may need time to reach steady state.

??? question "How do I add custom SPICE models?"
    1. Obtain the `.lib` or `.sub` model file from the component manufacturer.
    2. Place it in the `Simulate/models/` directory.
    3. The Template Provider automatically includes it during netlist generation.

    See [Running a Simulation — SPICE Model Files](simulation/running-simulation.md#spice-model-files).

---

## AI Copilot

??? question "How do I set up the AI Copilot?"
    1. Open **View → AI Copilot** to show the panel.
    2. Click the **⚙ Settings** icon.
    3. Enter your [OpenRouter](https://openrouter.ai/) API key.
    4. Click **Save**.

    See [AI Copilot — Getting Started](ai/index.md#getting-started).

??? question "AI Copilot is not responding / API error"
    - Check your **internet connection** — the AI requires an active connection.
    - Verify your **API key** is valid and has remaining credits.
    - Check for rate limiting — wait a moment and try again.
    - Review the Logger for detailed error messages.

??? question "AI-generated design has incorrect pin assignments"
    The AI uses datasheet knowledge but may occasionally make errors:

    1. Review the **Netlist Validation** results in the Component Review window.
    2. Use **Refine** to ask the AI to fix specific issues (e.g., "Pin 7 should be RESET, not VCC").
    3. Click **Fix with AI** to have the AI automatically correct validation errors.

??? question "Missing components in AI-generated design"
    If the AI Library Reviewer shows ⚠ **Missing** components:

    1. Click **Generate** next to the missing component.
    2. The [AI Component Generator](ai/component-generator.md) creates the symbol and footprint.
    3. Review and accept the generated component.
    4. Alternatively, import the component manually from a KiCad library.

---

## Library Converter

??? question "How do I convert Altium libraries to KiCad format?"
    Use the Library Converter Pipeline:

    ```bash
    cd WireFrame/Tools
    python3 run.py --local /path/to/MyLib.IntLib
    ```

    See [Library Converter](libraries/library-converter.md) for full documentation.

??? question "Converted symbols are missing pin names"
    - This may happen with `.PcbLib` files (footprints only, no symbol data).
    - The converter uses **fallback generation** to create symbols from footprint geometry.
    - For better results, provide both `.SchLib` and `.PcbLib` files together.

---

## Still Need Help?

If your issue is not listed here:

1. Check the [Changelog](changelog.md) for known issues in your version.
2. Search the [GitHub Issues](https://github.com/CaSauCoin/WireFrame_Product/issues) page.
3. Open a new issue with:
    - Your OS and WireFrame version.
    - Steps to reproduce the problem.
    - Any error messages from the Logger.
    - Screenshots if applicable.
