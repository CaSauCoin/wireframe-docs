# ERC — Electrical Rules Check

The Electrical Rules Check (ERC) scans your schematic for common connectivity and electrical errors **before** you convert to PCB. Catching problems early saves time and prevents hard-to-trace issues downstream.

---

## Why Run ERC?

| Benefit | Example |
|---|---|
| **Detect floating pins** | An MCU input pin left unconnected picks up noise |
| **Find missing connections** | A power pin never wired to VCC |
| **Catch driver conflicts** | Two output pins shorted together |
| **Prevent duplicate IDs** | Two components both named `R1` — causes BOM and netlist confusion |

---

## Running the ERC

1. Open the schematic you want to check.
2. Select **Tools → Electrical Rules Check (ERC)**.
3. The **ERC Panel** opens and immediately runs all checks.
4. Results populate in the panel.

### Image — ERC results and highlighted issue

!!! note "Image needed"
    Capture the v1.5.47 ERC panel with a small mix of errors and warnings. Keep one result selected and its affected pin or net visible on the canvas.

---

## Check Types

### 🔴 Floating Input Pins

Detects input-type pins with **no electrical connection** (no wire, no net label, no power symbol).

- **Why it matters**: Floating inputs on digital ICs cause unpredictable behavior and excessive power draw.
- **How to fix**: Connect the pin to a signal, pull-up/pull-down resistor, or explicitly mark it as "no connect" if the pin is unused.

For example, an MCU reset input with no connection may need the pull-up or control circuit specified by its datasheet. Do not apply a generic resistor value without checking the device requirements.

### 🔴 Unconnected Nets

A net label is placed but connects to **only one pin** — meaning the connection goes nowhere.

- **Why it matters**: The intended signal path is broken.
- **How to fix**: Add the matching net label on the destination, or draw a wire to complete the connection.

### 🔴 Output Driver Contention

Two or more **output pins** are connected to the same net, creating a potential short circuit.

- **Why it matters**: Conflicting output drivers can damage ICs and cause undefined logic states.
- **How to fix**: Review the design — use open-collector outputs, add buffers, or separate the conflicting outputs.

### 🟡 Duplicate Designators

Two components share the same designator (e.g., both named `R1`).

- **Why it matters**: The BOM will merge them incorrectly, and PCB netlist mapping fails.
- **How to fix**: Rename one of the components in the Properties panel.

### 🟡 Missing Component Values

A component has no **Value** property set (empty field).

- **Why it matters**: The BOM will have an empty entry, and simulation cannot determine the component's behavior.
- **How to fix**: Select the component → set the Value in the Properties panel (e.g., `10kΩ`, `100nF`).

---

## Navigating ERC Results

### Zoom to issue

**Double-click** any ERC result row:

1. The canvas **automatically pans and zooms** to center the problematic area.
2. The affected component or pin is highlighted.
3. Fix the issue directly on the canvas.

### Re-run after fixing

After making corrections, click **Run ERC** again (or close and reopen the ERC panel) to verify the issue is resolved.

Repeat **Run ERC → locate issue → correct design → Run ERC** until no blocking error remains. Review warnings individually before PCB conversion.

### Short video — Fix and re-run ERC

!!! note "Video needed"
    Record a 20-second clip showing an ERC issue selected, corrected on the schematic, and removed by the next ERC run. Use a non-proprietary example project.

---

## ERC Before PCB Conversion

!!! important "Always run ERC before converting to PCB"
    Unresolved ERC errors can propagate into the PCB as missing connections, incorrect net mappings, or orphan footprints. Running ERC first ensures a clean netlist transfer.

---

## See Also

- [Wiring & Nets](wiring-and-nets.md) — fix connectivity issues found by ERC.
- [Properties & Attributes](properties-and-attributes.md) — fix missing values and designators.
- [DFM & DRC](../pcb/dfm-and-drc.md) — the PCB-side equivalent of ERC.
