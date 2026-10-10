# Schematic Editor — Overview

The Schematic Editor is where you **design your circuit**: place components, draw wires, assign net labels, and prepare for PCB layout.

---

## What You Can Do Here

| Task | Tool |
|---|---|
| Place components from libraries | Drag a symbol from the **Library** panel onto the sheet |
| Draw wires connecting pins | Wire tool (++w++) |
| Assign net labels (SDA, SCL, +3V3…) | **Label** tool (++n++) |
| Place power symbols (GND, VCC) | **Place GND** (++g++) / **Place VCC** (++p++) |
| Draw annotations (boxes, text, lines) | Line, Rect, Text tools |
| Edit component properties | Properties panel |
| View net connectivity | Built automatically as you draw |

---

## Workspace

The schematic workspace consists of:

### Image — Schematic workspace

!!! note "Image capture brief"
    1. **Prepare:** Open the sample project's schematic.
    2. **Build the frame:** Capture the schematic editor with the canvas, the toolbar centred at the top, the Library panel (**Local Library** tab), and Properties.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

- **Canvas** — dot grid with an A4 page outline (configurable to A3, custom). Place all components and wires here.
- **Toolbar** — a strip of tool buttons centred at the top of the canvas; ++tab++ hides or shows it
- **Library panel** — symbol list for placing components
- **Properties panel** — edit properties of the selected item or page settings
- **ERC panel** — electrical rules check results ([details](erc.md))
- **Simulation panel** — configure and run SPICE simulations ([details](../simulation/index.md))

---

## Toolbar Modes

Each toolbar button activates a **drawing mode** that determines how mouse clicks are interpreted:

| Tool (tooltip) | Shortcut | Behavior |
|---|---|---|
| **Select** | ++esc++ | Click to select, drag to move, drag a box to multi-select |
| **Wire** | ++w++ | Click to start / add corners / end a wire |
| **Label** | ++n++ | Click to place a net label |
| **Probe Signal** | ++v++ | Click a wire, pin, net label, or power symbol to place a probe marker on its net for the simulation — see [Waveform Viewer](../simulation/waveform-viewer.md) |
| **Place GND** | ++g++ | Click to place a GND power symbol |
| **Place VCC** | ++p++ | Click to place a VCC power symbol |
| **Draw Line** | ++shift+l++ | Click start → drag → release |
| **Draw Rectangle** | ++r++ | Click one corner → drag to opposite |
| **Draw Circle** | ++e++ | Click center → drag to set radius |
| **Draw Arc** | ++a++ | Click to define arc points |
| **Draw Polygon** | ++o++ | Click vertices → right-click to close |
| **Junction** | ++j++ | Click to place junction dots manually |
| **Net Harness** | ++h++ | Drag to draw a harness line — a drawing that marks a bundle of signals; it does not connect nets |
| **Place Text** | ++t++ | Click to place a text annotation |
| **Import Image** | — | Place a PNG, JPG, or BMP picture at the centre of the view |

The active tool is **highlighted cyan**. Press ++esc++ to return to Select mode at any time.

---

## Basic Interactions

### Selecting objects

| Action | Input |
|---|---|
| Select a single component | Left-click on it |
| Select multiple objects | Drag a selection box on empty canvas |
| Open context menu | Right-click any object |
| Cancel current operation | ++esc++ |
| Delete selected | ++delete++ or ++backspace++ |
| Undo / Redo | ++ctrl+z++ / ++ctrl+y++ |

### Smart interactions

- **Dragging a component** — connected wires follow automatically, no broken connections
- **Rotating** (++space++, or ++r++ with a component selected) — the component rotates by the rotation step (90° by default), wires adjust to the new pin positions
- **Deleting a component** — connected wires are also removed (fully undoable)

---

## Section Pages

Continue to the detailed guides for each aspect of schematic design:

| Page | What you'll learn |
|---|---|
| [Placing Components](placing-components.md) | Load libraries, place symbols, edit designators |
| [Wiring & Nets](wiring-and-nets.md) | Draw wires, connect pins, net labels, GND/VCC |
| [Properties & Attributes](properties-and-attributes.md) | Edit page settings, component attributes, text |
| [Graphics & Annotations](graphics-and-annotations.md) | Draw boxes, lines, annotations |
| [ERC (Electrical Rules Check)](erc.md) | Validate connectivity before PCB conversion |
| [Templates & Title Block](templates.md) | Page setup, title block customization |

---

## Related Sections

| Section | What you'll learn |
|---|---|
| [Simulation](../simulation/index.md) | Run SPICE simulation on your schematic |
| [Symbol Library Editor](../libraries/symbol-creator.md) | Create or correct custom schematic symbols |
| [AI Copilot](../ai/index.md) | Generate schematics from text descriptions |
