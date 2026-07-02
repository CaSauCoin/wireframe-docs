# Zones and Copper Planes

Copper zones (fills / pours) cover a board area with copper — typically used for **ground planes** or **power planes**. This is a standard practice in professional PCB design.

---

## Why Use Zones?

- **Ground plane** — reduces EMI noise and improves RF signal integrity
- **Power plane** — reduces voltage drop on power rails
- **Larger copper area** → lower impedance → better heat dissipation

---

## What Is a Zone?

```
Board with GND zone (top view):

┌─────────────────────────────────────────┐
│ ░░░░░░░[R1]░░░░░░░░░░░░░░░░░░░░░░░░░░░ │  ← GND copper fill (░)
│ ░░░░░   ┊  ░░░░░░░   ┊  ░░░░░░░░░░░░░ │
│ ░░░░░  [U1] ░░░░░  [C1] ░░░░░░░░░░░░░ │
│ ░░░░░   ┊  ░░░░░░░   ┊  ░░░░░░░░░░░░░ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
└─────────────────────────────────────────┘

Legend:
  ░ = GND copper fill
  ┊ = clearance gap around pads on other nets
  [R1] = footprint (GND pads connect directly to the fill)
```

Each zone has:

| Property | Description |
|---|---|
| **Net** | The net name (e.g. `GND`, `VCC`) |
| **Layer** | Copper layer (e.g. F.Cu, B.Cu) |
| **Priority** | Higher-priority zones override lower ones where they overlap |
| **Clearance** | Minimum gap from pads and traces on other nets |
| **Outline** | The polygon you draw to define the zone boundary |

---

## Quick Ground Plane

The fastest way — use **Fill GND Plane**:

1. Go to **Tools → Fill GND Plane**
2. WireFrame automatically:
    - Reads the board outline from Edge.Cuts
    - Creates a GND zone covering the entire board interior
    - Computes clearance gaps around all pads and traces not on GND
    - Connects GND pads directly into the fill

```
Before Fill GND:              After Fill GND:
  ┌────────────┐                ┌──░░░░░░░░░░░┐
  │  [R1] [C1] │                │░░[R1]░[C1]░░│
  │            │                │░░░░░░░░░░░░░│
  └────────────┘                └──░░░░░░░░░░░┘
```

---

## Creating a Zone Manually

1. Select a copper layer (e.g. **F.Cu**) in the Layer panel
2. Use the **Draw Polygon** tool to draw a closed polygon boundary
3. Assign zone properties:
    - **Net name** (e.g. `GND`)
    - **Clearance** (e.g. 0.2 mm)
    - **Priority** (default: 0)
4. WireFrame computes and renders the copper fill

---

## Zone Priority

When two zones overlap, the zone with the **higher priority** wins:

```
Example — VCC island inside a GND plane:

┌────────────────────────────────────────────┐
│ ░░░░░░░░░░ GND (priority 0) ░░░░░░░░░░░░ │
│ ░░░░ ┌──────────────────┐ ░░░░░░░░░░░░░░ │
│ ░░░░ │ ▓▓▓ VCC (p=1) ▓▓│ ░░░░░░░░░░░░░░ │
│ ░░░░ │   ▓▓▓▓▓▓▓▓▓▓▓   │ ░░░░░░░░░░░░░░ │
│ ░░░░ └──────────────────┘ ░░░░░░░░░░░░░░ │
└────────────────────────────────────────────┘
```

!!! tip "Priority guidelines"
    - Ground plane → priority **0** (lowest)
    - VCC island inside the GND plane → priority **1**
    - Zone nested inside VCC → priority **2**, and so on

---

## How Zones Interact with Nets

| Situation | Result |
|---|---|
| Pad on the **same net** as the zone | Pad connects directly to the fill (no ratsnest) |
| Trace on the **same net** passing through | Trace connects to the zone |
| Pad on a **different net** inside the zone | Clearance gap is maintained around the pad |
| Trace on a **different net** inside the zone | Clearance gap is maintained around the trace |

---

## Editing Zones

| Property | Editable |
|---|---|
| Net name | ✅ — in Properties panel |
| Layer | ✅ |
| Priority | ✅ |
| Clearance | ✅ |
| Outline (vertices) | ✅ — drag vertices to reshape the boundary |
| Cutouts | ✅ — add excluded shapes inside the zone |

---

## See Also

- [Routing](routing.md) — traces interact with zone clearances
- [DFM & DRC](dfm-and-drc.md) — zone connectivity is validated during DRC
- [Layers & Views](layers-and-views.md) — zone visibility follows layer settings
