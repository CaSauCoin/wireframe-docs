# AI Design Agent

The AI Design Agent is the core intelligence behind WireFrame's AI Copilot. It takes a plain-text circuit description and produces a complete **Bill of Materials (BOM)** and **topological netlist** — selecting real components with correct pin assignments based on datasheet analysis.

---

## Design Phases

The Design Agent operates in two distinct phases:

### Phase 1: Research

When you type a prompt (e.g., *"Design a 5V 1A buck converter with LM2596"*), the AI:

1. **Analyzes** the request — extracts specifications, voltage levels, current requirements.
2. **Researches** — queries component databases and datasheets for suitable parts.
3. **Asks clarifying questions** — if requirements are ambiguous, the AI presents interactive questions:

```
┌─────────────────────────────────────────────────────┐
│  AI: I have a few questions before I start:          │
│                                                      │
│  1. Input voltage range?                             │
│     [○ 7-12V]  [○ 12-24V]  [○ Custom: ___]         │
│                                                      │
│  2. Output current requirement?                      │
│     [○ 500mA]  [○ 1A]  [○ 2A]                      │
│                                                      │
│  3. Board form factor?                               │
│     [○ Custom]  [○ Arduino UNO shield]              │
│                                                      │
│  [Proceed with selected options →]                   │
└─────────────────────────────────────────────────────┘
```

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the AI Copilot Panel showing clarifying questions:
     - 3-4 questions displayed with radio button / dropdown options.
     - A "Proceed" button at the bottom.
     - The original user prompt visible in the chat history above.
     - Dark theme, clean modern UI.
     SUGGESTED SIZE: 400×500px (panel only)
-->
![Clarifying Questions](../img/ai/clarifying-questions.png)

### Phase 2: Design Generation

After receiving your answers (or if no questions were needed), the AI generates:

1. **BOM (Bill of Materials)** — a list of components with:
    - Part name and description
    - Package/footprint
    - Key specifications (voltage rating, value, tolerance)
    - Pin count and pin names

2. **Netlist** — complete wiring connections:
    - Pin-to-pin connections between components
    - Net names for each connection group
    - Support circuitry (decoupling capacitors, pull-up resistors, bypass components)

---

## Component Review Window

After the Design Agent generates a design, a **Component Review** window opens with multiple tabs:

### BOM Tab

Lists all generated components:

| # | Designator | Part | Value | Footprint | Status |
|---|---|---|---|---|---|
| 1 | U1 | LM2596 | — | TO-263-5 | ✅ In library |
| 2 | L1 | Inductor | 33µH | 10x10mm | ⚠ Not in library |
| 3 | D1 | SS34 | — | SMA | ✅ In library |
| 4 | C1 | Capacitor | 680µF | 10mm radial | ✅ In library |
| 5 | C2 | Capacitor | 220µF | 8mm radial | ✅ In library |
| 6 | R1 | Resistor | 1.2kΩ | 0603 | ✅ In library |
| 7 | R2 | Resistor | 3.9kΩ | 0603 | ✅ In library |

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Component Review window's BOM tab:
     - A table with 6-8 components listed.
     - Status column showing green checkmarks for found components
       and yellow warnings for missing ones.
     - Column headers: #, Designator, Part, Value, Footprint, Status.
     SUGGESTED SIZE: 700×400px
-->
![Component Review BOM](../img/ai/component-review-bom.png)

### Netlist Tab

Shows the generated connections in a readable format:

```
Net "VIN":     U1.Pin1 ── C1.Pad1 ── J1.Pin1
Net "VOUT":    U1.Pin2 ── L1.Pad2 ── C2.Pad1 ── R1.Pad1
Net "GND":     U1.Pin3 ── C1.Pad2 ── C2.Pad2 ── D1.K ── R2.Pad2 ── J1.Pin2
Net "FB":      U1.Pin4 ── R1.Pad2 ── R2.Pad1
Net "SW":      U1.Pin5 ── L1.Pad1 ── D1.A
```

### Placement Preview Tab

An interactive preview canvas showing the planned component layout:

- **Block view**: Components grouped by function (Power, MCU, Interface, etc.)
- **Whole circuit view**: Complete schematic topology
- Zoom and pan controls (same as the schematic canvas)

---

## Library Pool Check

The **AI Library Reviewer** automatically scans each generated component against your **local library pool**:

| Status | Icon | Meaning |
|---|---|---|
| **Found** | ✅ | Symbol and footprint exist in loaded libraries |
| **Missing** | ⚠ | Component not found — needs to be created or imported |
| **Partial** | 🟡 | Symbol found but footprint missing, or vice versa |

### Configuring the library pool

1. In the Component Review window, click **Library Pool Settings**.
2. Add paths to your library directories.
3. Click **Re-check** to rescan all components.

For missing components, use the [AI Component Generator](component-generator.md) to create them automatically.

---

## Netlist Validation

WireFrame includes a **deterministic Netlist Validator** (`AI_Netlist_Validator`) that runs independently of the AI:

| Check | Description |
|---|---|
| **Pin existence** | Every pin referenced in the netlist actually exists on the component |
| **Pin count match** | Component pin count matches the datasheet/library |
| **Floating pins** | Critical pins (power, ground) are connected |
| **Net consistency** | No net has only a single connection |

Results are displayed in a **Netlist Validation** section with pass/fail indicators.

---

## Simulation Verification

The AI can automatically verify the design using SPICE simulation:

1. Click **Verify with Simulation** in the Component Review window.
2. The **AI Simulation Verifier**:
    - Generates a SPICE netlist from the design.
    - Runs a transient or DC analysis.
    - Compares results against the design requirements.
3. If verification **fails**, the AI feeds error logs back to the LLM for automatic correction.

<!-- TODO: Replace with actual video
     SCENARIO: Record a 30-second clip showing:
     1. User types "Design a 555 Timer LED blinker at 1Hz" in the AI Copilot.
     2. AI research phase — thinking stages appear with progress.
     3. Clarifying questions pop up — user selects "5V supply" and "red LED".
     4. AI generates BOM — Component Review window opens with 6-7 components.
     5. Netlist tab shows connections.
     6. User clicks "Verify with Simulation" — simulation runs and passes.
     RESOLUTION: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/ai/ai-design-workflow.webm" type="video/webm">
  <source src="../../img/ai/ai-design-workflow.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Refining the Design

After the initial generation, you can refine the design through conversation:

- *"Change R1 to 4.7kΩ"* — AI updates the specific component.
- *"Add an LED indicator on the output"* — AI adds components and connections.
- *"Use a different voltage regulator"* — AI swaps the IC and adjusts the support circuitry.

The AI preserves your manual edits (coordinate locking) — only the requested changes are applied.

---

## Circuit Design Analysis

The **AI Circuit Analyzer** provides an AI-powered review of the design:

- Analyzes the circuit topology for best practices.
- Checks for common design issues (missing decoupling, incorrect biasing).
- Provides recommendations for improvement.

Click **Analyze Design** in the Component Review window to run this analysis.

---

## See Also

- [AI Copilot Overview](index.md) — setup and architecture.
- [Auto-Placer & Auto-Router](auto-placer-router.md) — physical implementation after design.
- [AI Component Generator](component-generator.md) — create missing components.
- [Simulation](../simulation/index.md) — manual simulation workflow.
