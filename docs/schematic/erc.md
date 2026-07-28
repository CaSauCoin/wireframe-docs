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
2. Go to **Tools → ERC Check** (or click the ERC button in the toolbar area).
3. The **ERC Panel** opens and immediately runs all checks.
4. Results populate in the panel.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the ERC Panel after running checks on a schematic with 3–5 issues:
     - 🔴 Error: "Floating input pin: U1.Pin7 (RESET)" — no connection to the pin.
     - 🔴 Error: "Unconnected net: SDA (1 pin only)" — label placed but only one endpoint.
     - 🟡 Warning: "Duplicate designator: R1 appears 2 times."
     - Panel header showing "2 errors, 1 warning".
     - The schematic canvas visible behind the panel with highlighted problem areas.
     SUGGESTED SIZE: 800×500px
-->
![ERC Panel Results](../img/schematic/erc-panel-results.png)

---

## Check Types

### 🔴 Floating Input Pins

Detects input-type pins with **no electrical connection** (no wire, no net label, no power symbol).

- **Why it matters**: Floating inputs on digital ICs cause unpredictable behavior and excessive power draw.
- **How to fix**: Connect the pin to a signal, pull-up/pull-down resistor, or explicitly mark it as "no connect" if the pin is unused.

```
Example:
  U1 (STM32)
    Pin 7 (RESET) ← No wire attached → 🔴 Floating input pin
    
Fix: Connect to VCC through a 10kΩ pull-up resistor.
```

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

```
ERC Workflow:

  Run ERC
     ↓
  Any errors?
  ├─ Yes → Double-click error → Fix on canvas → Run ERC again
  └─ No  → Ready to convert to PCB ✅
```

<!-- TODO: Replace with actual video
     SCENARIO: Record a 20-second clip showing:
     1. Open ERC panel — shows 2 errors (floating pin, unconnected net).
     2. Double-click the floating pin error — canvas zooms to U1 pin 7.
     3. Draw a wire from pin 7 to VCC.
     4. Re-run ERC — the error disappears.
     5. Panel shows "0 errors, 0 warnings".
     RESOLUTION: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/schematic/erc-fix-workflow.webm" type="video/webm">
  <source src="../../img/schematic/erc-fix-workflow.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## ERC Before PCB Conversion

!!! important "Always run ERC before converting to PCB"
    Unresolved ERC errors can propagate into the PCB as missing connections, incorrect net mappings, or orphan footprints. Running ERC first ensures a clean netlist transfer.

---

## See Also

- [Wiring & Nets](wiring-and-nets.md) — fix connectivity issues found by ERC.
- [Properties & Attributes](properties-and-attributes.md) — fix missing values and designators.
- [DFM & DRC](../pcb/dfm-and-drc.md) — the PCB-side equivalent of ERC.
