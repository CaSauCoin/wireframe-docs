---
hide:
  - navigation
  - toc
---

<div class="wf-hero" markdown>

<span class="wf-badge">v1.3.7 — Stable Release</span>

# WireFrame EDA

<p class="wf-subtitle">
A streamlined environment for schematic capture, PCB layout, SPICE simulation,<br>
3D visualization, AI-assisted design, and manufacturing export — built for speed, precision, and KiCad compatibility.
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
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Create    │──▶│   Design    │──▶│  Simulate   │──▶│   Convert   │──▶│   Route &   │──▶│   Export    │
│   Project   │   │  Schematic  │   │   (SPICE)   │   │   to PCB    │   │   Verify    │   │   Gerbers   │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
```

1. **Create Project** — Centralize schematics, PCBs, and libraries in a single `.prjxml` file
2. **Design Schematic** — Place components, draw wires, assign net labels, configure properties
3. **Simulate** — Run SPICE simulation to verify circuit behavior before layout
4. **Convert to PCB** — Automatically import netlist and footprints into the PCB editor
5. **Layout & Route** — Place footprints, route traces, fill copper zones, run DFM/DRC
6. **Export** — Generate Gerber, drill, BOM — ready for your manufacturer

!!! tip "AI-assisted design"
    Skip steps 2–5 entirely! The [AI Copilot](ai/index.md) can design, simulate, place, and route a circuit from a single text prompt.

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

<div class="wf-card" markdown>

### :material-sine-wave: SPICE Simulation

Validate your design before manufacturing. Run **Transient**, **AC**, **DC Sweep**, and **Operating Point** analyses powered by NgSpice — then measure results in an interactive waveform viewer with cursors and delta measurements.

</div>

<div class="wf-card" markdown>

### :material-robot: AI Copilot

Describe a circuit in plain text and let the AI design it. The AI Copilot researches components, generates netlists, runs SPICE verification, and auto-places/routes the PCB — from prompt to Gerber in minutes.

</div>

<div class="wf-card" markdown>

### :material-puzzle-edit: Symbol & Footprint Creator

Create custom schematic symbols with the interactive editor or wizard. Generate footprints for any package type with the Footprint Wizard. AI can also generate components automatically from datasheets.

</div>

</div>

---

## Designed For

| Audience | Why WireFrame? |
|---|---|
| **Electronics Hobbyists** | Clean interface, Toner Transfer PDF for DIY board making, easy KiCad library import |
| **Students & Academia** | Lightweight installation, SPICE simulation, transparent workflow from schematic to Gerber |
| **Professional Engineers** | AI-assisted design, keyboard-driven efficiency, full KiCad ecosystem compatibility, robust DFM/DRC engine |
| **Open-Source Developers** | Built on C++17 and ImGui — performant, extensible architecture |

---

## Documentation

| Section | Content |
|---|---|
| [Getting Started](getting-started.md) | Launch, main UI, create your first project |
| [Tutorials](tutorial/index.md) | NE555 LED blinker walkthrough + AI-assisted design tutorial |
| [Schematic Editor](schematic/index.md) | Place components, draw wires, manage nets, run ERC |
| [PCB Editor](pcb/index.md) | Footprints, routing, zones, design rules, DFM, Gerber export |
| [Libraries](libraries/symbols-library.md) | Symbols, footprints, Symbol Creator, Library Converter |
| [Simulation](simulation/index.md) | SPICE simulation — transient, AC, DC, waveform viewer |
| [AI Copilot](ai/index.md) | AI-assisted design, auto-placer, auto-router, component generator |
| [Advanced Features](advanced/selection-and-editing.md) | Advanced selection, 3D viewer, keymap customization |
| [Reference](reference/file-formats.md) | File formats, configuration, FAQ, changelog |

---

!!! tip "New to WireFrame?"
    Start with [Getting Started](getting-started.md) to learn the interface, or jump straight into the [NE555 Tutorial](tutorial/index.md) to experience the full workflow hands-on. Want to see the AI in action? Try the [AI-Assisted Design Tutorial](tutorial/ai-design.md).
