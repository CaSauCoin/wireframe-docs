# Design Rules & Net Classes

Design rules define the **manufacturing constraints** for your PCB — minimum clearances, trace widths, via sizes, and drill diameters. Net classes let you assign different rules to different signal groups (e.g., wider traces for power nets).

---

## Accessing Design Rules

Go to **Tools → Design Rules** to open the Design Rules dialog.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Design Rules dialog showing:
     - A "Global Rules" section with fields for: Minimum Clearance (0.15mm),
       Minimum Trace Width (0.15mm), Minimum Via Diameter (0.6mm),
       Minimum Drill Size (0.3mm).
     - A "Net Classes" table below with 2-3 entries.
     - Input fields with numeric values and unit labels (mm).
     SUGGESTED SIZE: 600×500px
-->
[//]: # (![Design Rules Dialog](../img/pcb/design-rules-dialog.png))

---

## Global Rules

Global rules apply to **all nets** unless overridden by a net class:

| Rule | Description | Typical value |
|---|---|---|
| **Minimum Clearance** | Minimum gap between copper features on different nets | 0.15 mm (6 mil) |
| **Minimum Trace Width** | Narrowest allowed trace | 0.15 mm (6 mil) |
| **Minimum Via Diameter** | Smallest via annular ring outer diameter | 0.6 mm |
| **Minimum Drill Size** | Smallest drill hole diameter | 0.3 mm |
| **Minimum Annular Ring** | Copper ring width around a drill hole | 0.13 mm |
| **Board Edge Clearance** | Minimum distance from copper to Edge.Cuts | 0.25 mm |

!!! tip "Check your manufacturer's capabilities"
    Different PCB manufacturers have different minimum capabilities. A common budget PCB service supports 6 mil (0.15 mm) minimum trace/clearance. High-end services can go down to 3 mil (0.075 mm). Set your rules to match your manufacturer's specs.

---

## Net Classes

Net classes allow you to define **different rules for different groups of nets**. This is essential for mixed-signal designs where power traces need to be wider than signal traces.

### Default net classes

| Net class | Trace width | Clearance | Typical use |
|---|---|---|---|
| **Default** | 0.15 mm | 0.15 mm | Standard signal traces |
| **Power** | 0.30 mm | 0.20 mm | VCC, GND, high-current paths |

### Creating a net class

1. Open **Tools → Design Rules**.
2. In the **Net Classes** section, click **Add Class**.
3. Set the class name (e.g., `Power`, `HighSpeed`, `Analog`).
4. Configure the rules for that class:
    - Trace width
    - Clearance
    - Via diameter
    - Drill size

### Assigning nets to a class

1. In the **Net Classes** section, select a class.
2. Choose which nets belong to that class:
    - Type net names manually (e.g., `GND`, `VCC`, `+5V`).
    - Or select from the netlist dropdown.

```
Example net class configuration:

  Default class (signals):
    Trace width: 0.15 mm    Clearance: 0.15 mm

  Power class:
    Trace width: 0.30 mm    Clearance: 0.20 mm
    Nets: GND, VCC, +5V, +3V3

  HighSpeed class:
    Trace width: 0.12 mm    Clearance: 0.20 mm
    Nets: USB_D+, USB_D-
```

---

## How Rules Affect Your Workflow

### During routing

- The **Route Trace** tool uses the **net class trace width** as the default width for each net.
- If you route a GND trace and GND is in the Power class, the trace defaults to 0.30 mm width.
- You can override the width manually in the Properties panel for individual traces.

### During DFM/DRC

The DFM checker validates your design against the configured rules:

- Traces narrower than the net class minimum → **Error**
- Clearance violations between copper on different nets → **Error**
- Via drill smaller than minimum → **Error**
- Copper too close to board edge → **Warning**

See [DFM & DRC](dfm-and-drc.md) for the full check suite.

---

## PCB Template Builder

WireFrame includes a PCB Template Builder (`Pcb_Template_Builder`) for setting up standard board configurations:

- **Board outline** presets (standard sizes, Arduino form factors)
- **Mounting hole** placement patterns
- **Grid and origin** configuration

Access via **Tools → Board Template** or when creating a new PCB.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the PCB Template Builder dialog showing:
     - Board size presets (dropdown with "Custom", "Arduino UNO", "50x50mm").
     - Mounting hole pattern options.
     - Preview of the board outline with mounting holes marked.
     SUGGESTED SIZE: 600×450px
-->
[//]: # (![PCB Template Builder](../img/pcb/pcb-template-builder.png))

---

## See Also

- [Routing](routing.md) — trace width follows net class rules.
- [DFM & DRC](dfm-and-drc.md) — validates against these rules.
- [Zones & Planes](zones-and-planes.md) — zone clearance settings.
