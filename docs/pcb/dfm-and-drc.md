# DFM and DRC Checks

Before exporting Gerber files, run **DFM/DRC** to detect and fix design errors. DFM (Design For Manufacturability) verifies that your board can actually be manufactured correctly.

!!! warning "Run DRC before exporting"
    Do not export Gerber files while **critical errors (red)** remain. Manufacturers may reject the order or the produced board may be defective.

---

## Running DFM Checks

1. Open **DFM & DRC Check** for the active PCB
2. Click **Run DFM**
3. WireFrame executes all check routines
4. Results populate in the DFM panel

### Image — DFM and DRC results

!!! note "Image needed"
    Capture the v1.5.47 **DFM & DRC Check** panel with at least one error and one warning. Keep the selected violation and its highlighted canvas location visible.

---

## Understanding the Results

| Icon | Type | Meaning |
|---|---|---|
| 🔴 **Error** | Critical | **Must be fixed** before export — board will fail if ignored |
| 🟡 **Warning** | Non-critical | Should be reviewed — may be acceptable in some situations |

---

## Check Types Explained

### 🔴 Unconnected Nets

Detects nets that still have **ratsnest lines** (pads not connected by a trace or zone).

- Example: `"Unconnected net: GND (pin U1.3, J1.2)"`
- **Fix:** Route a trace or add a copper zone to complete the connection

### 🔴 Clearance Violations

Two copper elements from different nets are too close together.

- Checks: trace ↔ trace, trace ↔ pad, pad ↔ pad, copper ↔ board edge
- **Fix:** Re-route the trace to a different path, or reduce trace width to create more clearance

### 🔴 Trace Width

A trace is too narrow for its assigned net class:

| Net class | Minimum width | Used for |
|---|---|---|
| Default (Signal) | 6 mil | Standard signal traces |
| Power | 12 mil | VCC, GND power rails |

- **Fix:** Increase the trace width in the Properties panel

### 🔴 Drill Sizes

A via or hole diameter is too small for the manufacturer to drill.

- **Fix:** Increase the drill diameter in the Via or Hole Properties panel

### 🟡 Component Near Board Edge

A footprint is too close to Edge.Cuts and may be clipped during manufacturing.

- **Fix:** Move the footprint further inward, or increase the board size
- *Note:* This is a warning (not an error) to accommodate castellated holes and edge connectors

### 🔴 Missing Components

Components exist in the schematic netlist but have no corresponding placed footprint on the PCB.

- **Fix:** Return to the schematic, verify the Footprint field is set correctly, then run Convert to PCB again

### 🔴 Orphan Traces / Vias

Copper that is not connected to any net or pad.

- **Fix:** Select and delete the orphan traces/vias

### 🔴 Board Outline

No board outline found (Edge.Cuts is empty), or the outline is malformed (self-intersecting, not closed).

- **Fix:** Draw a valid board outline using the Rectangle or Polygon tool on the Edge.Cuts layer

---

## Viewing and Fixing Violations

### Step 1: Double-click a violation

- The canvas **automatically pans and zooms** to the violation location
- The problematic area is centered on screen

### Step 2: Fix the issue

- Route the missing trace
- Move a trace to increase clearance
- Delete an orphan trace
- Place the missing footprint

### Step 3: Re-run DFM

Click **Run DFM** again to confirm the issue is resolved.

Repeat the check–locate–fix cycle until there are no release-blocking errors. Review every remaining warning and document why it is acceptable before fabrication export.

### Short video — Resolve and recheck a violation

!!! note "Video needed"
    Record a 20–30 second clip showing one violation selected, corrected on the PCB, and cleared by the next DFM/DRC run.

---

## See Also

- [Routing](routing.md) — fix trace-related violations by re-routing
- [Zones & Planes](zones-and-planes.md) — zone connectivity affects unconnected net checks
- [Fabrication & Export](fabrication-and-export.md) — export only after DRC passes cleanly
