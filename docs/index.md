# WireFrame EDA User Guide

WireFrame EDA is a lightweight EDA environment combining:

- **Schematic editor** for circuit design.
- **PCB editor** for layout, routing and manufacturing data.
- **Symbol & footprint wizards** for quickly generating libraries.
- **3D viewer** for PCB visualization.
- **Project management** with multi‑sheet schematics and multiple PCBs.

This documentation is organized by workflow and area of the UI:

- [Getting Started](getting-started.md)
- [User Interface Overview](ui-overview.md)
- [Projects and Files](projects.md)
- [Schematic Editor](schematic/index.md)
- [PCB Editor](pcb/index.md)
- [Libraries (Symbols & Footprints)](libraries/symbols-library.md)
- [Advanced Editing & Shortcuts](advanced/selection-and-editing.md)
- [Reference](reference/file-formats.md)

> **Image placeholder**  
> `![Welcome screen](img/home/welcome-screen.png)`  
> _Shows WireFrame main window just after launch, with menu bar, project structure panel on the left and empty editor area._

---

## Typical Workflow

1. **Create or open a project**
   - Use the main menu to create a `.prjxml` project.
   - Add or open schematic (`.schxml`) and PCB (`.pcbxml`) documents.

2. **Design the schematic**
   - Place components from symbol libraries.
   - Wire nets, add labels, power symbols and graphic annotations.
   - Use the properties panel to edit component attributes and page settings.

3. **Generate / sync PCB**
   - Convert the schematic into a PCB document.
   - Place footprints, assign footprints to symbols if needed.

4. **Route the PCB**
   - Route traces with 45° paths, place vias and mechanical holes.
   - Manage layers, copper pours/zones and DRC/DFM checks.

5. **Finalize & export**
   - Run DFM checks.
   - Generate Gerber, drill files and BOM.
   - Optionally inspect the board in 3D.

---

## Who is this for?

- Users who are familiar with basic EDA concepts (nets, footprints, layers) and want a focused, script‑free tool.
- Hobbyists and professionals who prefer an ImGui‑style, keyboard‑friendly desktop UI.

If you are just starting, continue to [Getting Started](getting-started.md).