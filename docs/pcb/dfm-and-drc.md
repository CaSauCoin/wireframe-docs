# DFM and DRC Checks

Before exporting Gerber files, run the **DFM & DRC Check** to find design-rule and manufacturability problems. DFM (Design For Manufacturability) checks that the board can be made; DRC (Design Rule Check) checks it against your net classes and constraints.

!!! warning "Fix errors before exporting"
    Do not export Gerber files while **errors** (red) remain. Manufacturers may reject the order, or the board may be defective.

---

## Running the Check

1. With a PCB active, open **Tools → DFM & DRC Check Panel...** (or **Run DRC** in the Design Rules Manager).
2. Optionally open **Check Settings** and choose which checks run (below).
3. Select **Run DFM Analysis**. A progress bar counts the finished checks, and **Rule stream** lists each step as it runs.
4. The result line reads **Found n Error(s) | n Warning(s)**, with errors listed first.

### Image — DFM and DRC results

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the v1.5.47 **DFM & DRC Check** panel with at least one error and one warning. Keep the selected violation and its highlighted canvas location visible.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

<!-- wf:shot id=dfm-and-drc-results
caption: DFM & DRC Check after a run — errors and warnings
setup:
- open_project
- ensure_pcb
- wait: 1
- menu:
  - Tools
  - DFM & DRC Check Panel...
- wait: 1
- click: '**/{fa:play} Run DFM Analysis'
- wait: 4
- action:
    action: mouse_move_to
    x: 1000
    y: 12
brief_sha256: 395b3d0325c9dbde
-->
<!-- wf:out id=dfm-and-drc-results sha=b8d75a542c22 -->
![DFM & DRC Check after a run — errors and warnings](../assets/wf/docs/pcb/dfm-and-drc/dfm-and-drc-results.png)
<!-- /wf:out -->

---

## Check Settings

The **Check Settings** header shows how many of the eight check groups are on (for example *8/8 enabled*).

| Check | Looks for |
|---|---|
| **Outline** | A closed board outline on Edge.Cuts; copper too close to the board edge |
| **Width** | Tracks narrower than the fab minimum, or outside their net class width |
| **Clearance** | Copper of different nets too close together |
| **Drill** | Drill and via sizes, annular rings, hole-to-hole spacing |
| **Nets** | Missing connections (ratsnest lines left) |
| **Orphans** | Traces with a wrong or missing net |
| **Placement** | Overlapping component bodies, parts too close to the edge, artwork over parts |
| **Missing** | Components of the schematic that are not on the board |

**Skip GND Conn** turns off **Nets** and **Orphans** — useful while the GND zone is not filled yet. **Enable All** turns every check back on. Run the full set before release.

---

## Reading the Results

Each row shows an icon, a code, and a message, for example `[E05] Clearance Error …`.

| Code | Severity | Meaning |
|---|---|---|
| **E00** | Error | Component in the schematic but not on the board |
| **E01** | Error | Board outline missing on Edge.Cuts, or a track narrower than the fab minimum |
| **E02** | Error | Unconnected net (ratsnest left), or a via drill below the fab minimum |
| **E03** | Error | Via diameter below the fab minimum |
| **E05** | Error | Clearance: copper of different nets too close |
| **E06** | Error | Component bodies overlap |
| **E07** | Error | Track too close to the board edge |
| **E08** | Error | Annular ring of a via or pad below the minimum |
| **E09** | Error | Two holes closer than the hole-to-hole minimum |
| **W01** | Warning | Track narrower than its net class |
| **W02** | Warning | Via smaller than its net class |
| **W05** | Warning | Orphaned track (wrong or missing net) |
| **W06** | Warning | Graphics or a logo over a part, or parts under a plug-in module |
| **W07** | Warning | Component pads too close to the board edge (ignore for edge connectors and castellations) |
| **W10** | Warning | Track wider than its net class maximum |
| **W11** | Warning | Net length outside its class target ± tolerance |
| **W12** | Warning | Differential pair skew over its budget |
| **W13** | Warning | Track width does not give the class impedance target on this stackup |
| **W14** | Warning | Length-matched group spread over its tolerance |
| **W15** | Warning | High-speed via leaves a long stub |
| **W16** | Warning | The two halves of a pair change layer a different number of times |
| **W17** | Warning | High-speed net without a reference plane on the next layer |

The limits come from **Design Rules → Constraints** and the net classes — see [Design Rules](design-rules.md).

### Changing a severity

Right-click a row to **Change to Warning** (or **Change to Error**) for this result, or **Reset Severity to Default**. Record why a downgraded item is acceptable; do not hide real problems to get a clean report.

### AI Explain Violations

**AI Explain Violations** sends the current list to the configured AI and shows an explanation and an impact score (*Impact n/5*) under each row. It needs an AI endpoint (see [AI Copilot](../ai/index.md)); the explanation is advice, not a fix.

---

## Viewing and Fixing Violations

1. **Click** a row — the canvas pans and zooms to the location (the tooltip shows its X / Y).
2. Fix the issue: reroute, move the part, change the net class, or correct the outline.
3. Select **Run DFM Analysis** again and repeat until no error remains.

With the panel open, markers on the canvas show where violations are. They hide while you edit and come back when the board has been still for a moment, so a marker never points at a part that has moved.

### Short video — Resolve and recheck a violation

!!! note "Video production brief"
    1. **Prepare:** Use a public demo PCB with one deliberate clearance or width violation and no distracting critical issues.
    2. **Opening shot (2–3 s):** Select the violation in **DFM & DRC Check** and show its highlighted board location.
    3. **Action shot (10–15 s):** Navigate to the object, correct its geometry or rule-compliant value, then run the check again.
    4. **Result shot (4–6 s):** Hold on the refreshed summary with that violation cleared and the corrected object visible.
    5. **Deliver:** Export a **20–30 second** 1080p MP4; do not hide remaining violations outside the stated example.

<!-- wf:video id=resolve-and-recheck-a-violation
caption: Default clearance set to 7 mil flags 13 places on a board laid out at 5 mil; focus one, set the
  rule back to the fab value, run the check again
project: none
setup:
- wait: 1
- open_file: board:buck-converter:kicad
- menu:
  - File
  - Import
  - KiCad Project (.kicad_pro, .pro)...
- wait: 12
- click_at:
    at:
    - 150
    - 109
    double: true
- wait: 4
- menu:
  - View
  - Design Rules
- wait: 2
- click_at:
  - 1175
  - 453
- keys:
  - End
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- type:
    text: '7'
- keys:
  - Enter
- wait: 1
- click: //Design Rules Manager/Close
- wait: 1
- menu:
  - Tools
  - DFM & DRC Check Panel...
- wait: 1
- click: '**/{fa:play} Run DFM Analysis'
- wait: 4
- action:
    action: mouse_move_to
    x: 1000
    y: 12
steps:
- wait: 2
- click_at:
  - 1470
  - 245
- wait: 3
- menu:
  - View
  - Design Rules
- wait: 2
- click_at:
  - 1175
  - 453
- keys:
  - End
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- keys:
  - Backspace
- type:
    text: '5'
- keys:
  - Enter
- wait: 2
- click: //Design Rules Manager/Close
- wait: 1
- click: '**/{fa:play} Run DFM Analysis'
- wait: 2
- action:
    action: mouse_move_to
    x: 1000
    y: 12
- wait: 4
brief_sha256: 0c438ae461c4de56
-->
<!-- wf:out id=resolve-and-recheck-a-violation sha=aabd644b729f -->
<video controls muted playsinline preload="metadata" src="../../assets/wf/docs/pcb/dfm-and-drc/resolve-and-recheck-a-violation.mp4" title="Default clearance set to 7 mil flags 13 places on a board laid out at 5 mil; focus one, set the rule back to the fab value, run the check again"></video>
<!-- /wf:out -->

---

---

## See Also

- [Routing](routing.md) — fix clearance and width violations
- [Design Rules & Net Classes](design-rules.md) — the limits the checks use
- [Zones & Planes](zones-and-planes.md) — fill zones before checking connectivity
- [Fabrication & Export](fabrication-and-export.md) — export after a clean check
- [ERC](../schematic/erc.md) — the schematic-side equivalent
