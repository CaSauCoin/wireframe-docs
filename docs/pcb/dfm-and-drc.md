# DFM and DRC Checks

The `PcbDFMManager` runs Design For Manufacturability (DFM) checks on a `PcbDocument` and produces a list of `DFMViolation` entries.

---

## Running checks

From a PCB document:

1. Open **Design Rules / DFM** panel or a **Fabrication** dialog.
2. Click “Run DFM” or similar.
3. `PcbDFMManager::runFullCheck` is called, which executes:
   - `checkBoardOutline`
   - `checkUnconnectedNets`
   - `checkTraceWidths`
   - `checkClearance`
   - `checkDrillSizes`
   - `checkComponents`
   - `checkOrphans`
   - `checkMissingComponents`

Each check populates a vector of `DFMViolation`:

- `code` – short code like `E01`, `W02`.
- `message` – human‑readable description.
- `location` – approximate board position of the issue.
- `isCritical` – whether it is an error or warning.

> **Image placeholder**  
> `![DFM panel](img/pcb/dfm-panel.png)`  
> _Panel listing errors and warnings with codes, messages and a "Zoom to" button._

---

## Types of checks

### Board outline

- Ensures the board boundary is well‑formed.
- Warns if:
  - No outline is defined.
  - Outline is self‑intersecting or degenerate.
  - Footprints lie outside the board area.

### Unconnected nets

- Uses `PcbNetlistManager` connectivity to find nets where:
  - Ratsnest lines remain.
  - Pins w/ same net are not connected by traces/zones.

### Trace widths

- Verifies trace widths against `DesignSettings`:
  - Each net has a net class (e.g., Default, Power).
  - Checks that trace width ≥ class minimum.

### Clearances

- Computes distances between:
  - Trace segments.
  - Traces and pads or vias.
  - Pads and other pads.
- Flags violations where distance < required clearance.

### Drill sizes

- Checks via and hole diameters vs minimum allowed sizes.
- Flags too small drills.

### Components

- Checks:
  - If footprints have overlapping bounding boxes (possible collisions).
  - If components extend beyond board edge.

### Orphans & missing components

- Orphan traces or vias:
  - Unconnected to any pad or within a net.
- Missing footprints:
  - Components in schematic/netlist without corresponding footprints on PCB.

---

## Viewing violations

The DFM/DRC panel:

- Lists violations with severity.
- Allows double‑click / button to:
  - Pan and zoom to `location`.
- Colors or icons:
  - Red for critical errors.
  - Yellow for warnings.

> **Video placeholder**  
> _Short clip where user runs "Run DFM", then clicks each error to center the view on the problematic area._