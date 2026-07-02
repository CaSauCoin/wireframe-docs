---
hide:
  - navigation
  - toc
---

<div class="wf-hero" markdown>

<span class="wf-badge">v1.3.7 — Stable Release</span>

# WireFrame EDA

<p class="wf-subtitle">
A streamlined environment for schematic capture, PCB layout, 3D visualization,<br>
and manufacturing export — built for speed, precision, and KiCad compatibility.
</p>

<div class="wf-cta">
  <a href="getting-started/" class="primary">Get Started</a>
  <a href="tutorial/" class="secondary">Try the Tutorial →</a>
</div>

</div>

![Welcome Screen](img/home/welcome-screen.png)

---

## The WireFrame Workflow

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Create    │──▶│   Design    │──▶│   Convert   │──▶│   Route &   │──▶│   Export    │
│   Project   │   │  Schematic  │   │   to PCB    │   │   Verify    │   │   Gerbers   │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
```

1. **Create Project** — Centralize schematics, PCBs, and libraries in a single `.prjxml` file
2. **Design Schematic** — Place components, draw wires, assign net labels, configure properties
3. **Convert to PCB** — Automatically import netlist and footprints into the PCB editor
4. **Layout & Route** — Place footprints, route traces, fill copper zones, run DFM/DRC
5. **Export** — Generate Gerber, drill, BOM — ready for your manufacturer

---

## Core Capabilities

<div class="wf-grid" markdown>

<div class="wf-card" markdown>

### :material-chip: Schematic Editor

Draft robust circuits with an intuitive schematic engine. Place components from KiCad-compatible libraries, route nets with orthogonal wires, assign net labels (`SDA`, `GND`, `+3V3`), and manage a fully automatic netlist.

</div>

<div class="wf-card" markdown>

### :material-developer-board: PCB Layout

Translate schematics into physical boards with precision. WireFrame offers 45° routing guidance, multi-layer management, intelligent copper zone generation with priority sorting, and an advanced DFM clearance engine that correctly handles board-edge geometries and castellated holes.

</div>

<div class="wf-card" markdown>

### :material-library-shelves: Library Management

Load KiCad `.kicad_sym` and `.kicad_mod` libraries natively. Create new footprints with the Footprint Wizard. Assign STEP/OBJ 3D models and fine-tune alignment with the 3D Model Alignment dialog.

</div>

<div class="wf-card" markdown>

### :material-rotate-3d: 3D Visualization

Validate your design before fabrication. Render high-fidelity 3D previews with STEP and OBJ models. WYSIWYG accuracy is guaranteed by a precise Z-Y-X rotation pipeline with correct bottom-layer flip orientation.

</div>

<div class="wf-card" markdown>

### :material-keyboard: Keyboard-Driven Workflow

++w++ wire · ++x++ route · ++r++ rotate · ++f++ flip · ++v++ via · ++g++ GND. Every action is one keystroke away. The full keymap is customizable via **Tools → Keymap**.

</div>

<div class="wf-card" markdown>

### :material-export: Fabrication Export

Generate industry-standard Gerber (RS-274X) with WYSIWYG silkscreen accuracy, Excellon drill files, and BOM CSV. Includes a **Toner Transfer PDF Exporter** — multi-page, 1:1 scale, with automatic mirroring — designed for hobbyist manual PCB fabrication.

</div>

<div class="wf-card" markdown>

### :material-swap-horizontal: Seamless Import

Import KiCad 5.x legacy projects (`.sch`, `-cache.lib`, `.pro`) and modern KiCad 6+ formats (`.kicad_sch`, `.kicad_pcb`) natively. No manual conversion needed.

</div>

</div>

---

## Designed For

| Audience | Why WireFrame? |
|---|---|
| **Electronics Hobbyists** | Clean interface, Toner Transfer PDF for DIY board making, easy KiCad library import |
| **Students & Academia** | Lightweight installation, transparent workflow from schematic to Gerber |
| **Professional Engineers** | Keyboard-driven efficiency, full KiCad ecosystem compatibility, robust DFM/DRC engine |
| **Open-Source Developers** | Built on C++17 and ImGui — performant, extensible architecture |

---

## Documentation

| Section | Content |
|---|---|
| [Getting Started](getting-started.md) | Launch, main UI, create your first project |
| [Tutorial](tutorial/index.md) | Complete walkthrough: LED circuit from scratch to Gerber |
| [Schematic Editor](schematic/index.md) | Place components, draw wires, manage nets |
| [PCB Editor](pcb/index.md) | Footprints, routing, zones, DFM, Gerber export |
| [Libraries](libraries/symbols-library.md) | Create and manage symbol and footprint libraries |
| [Advanced Features](advanced/selection-and-editing.md) | Advanced selection, 3D viewer, keymap customization |
| [Reference](reference/file-formats.md) | File formats, configuration, FAQ, changelog |

---

!!! tip "New to WireFrame?"
    Start with [Getting Started](getting-started.md) to learn the interface, or jump straight into the [Tutorial](tutorial/index.md) to experience the full workflow hands-on.
