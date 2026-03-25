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

## Still Need Help?

If your issue is not listed here:

1. Check the [Changelog](changelog.md) for known issues in your version.
2. Search the [GitHub Issues](https://github.com/CaSauCoin/WireFrame_Product/issues) page.
3. Open a new issue with:
    - Your OS and WireFrame version.
    - Steps to reproduce the problem.
    - Any error messages from the Logger.
    - Screenshots if applicable.

