# Tutorial: AI-Assisted Circuit Design

This tutorial demonstrates the **AI Copilot workflow** — design a circuit entirely through conversation with the AI agent. We'll create a 555 Timer LED blinker, verify it with SPICE simulation, and export manufacturing files.

**What you will build:** A complete NE555 astable oscillator with an LED blinking at approximately 1 Hz — designed, verified, placed, and routed with AI assistance.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the finished design showing both the schematic (with NE555,
     resistors, capacitor, LED) and the PCB (routed board) side by side.
     The AI Copilot Panel visible on the side with the conversation history.
     SUGGESTED SIZE: 1280×720px
-->
![AI Design Final Result](../img/tutorial/ai-design-final.png)

---

## What You Will Learn

- [x] Configure the AI Copilot API key
- [x] Describe a circuit in plain text
- [x] Answer AI clarifying questions
- [x] Review AI-generated BOM and netlist
- [x] Verify the design with SPICE simulation
- [x] Auto-place components and auto-route traces
- [x] Export Gerber and BOM files

---

## Prerequisites

| Requirement | Details |
|---|---|
| **WireFrame** | Installed and activated |
| **API Key** | An [OpenRouter](https://openrouter.ai/) API key (free tier available) |
| **NgSpice** | Installed for simulation verification (see [Simulation — Prerequisites](../simulation/index.md#prerequisites)) |

---

## Step 1 — Configure AI and Create a Project

### Set up API key

1. Open WireFrame.
2. Go to **View → AI Copilot** to open the AI panel.
3. Click the **⚙ Settings** icon in the panel header.
4. Enter your OpenRouter API key.
5. Click **Save**.

### Create a project

1. Go to **File → New Project…**
2. Name it `NE555_Blinker.prjxml`.
3. Click **Create**.

---

## Step 2 — Describe Your Circuit to the AI

In the AI Copilot chat input, type:

```
Design a 555 timer LED blinker circuit.
The LED should blink at approximately 1 Hz.
Power supply: 9V battery.
Use a red LED with a current-limiting resistor.
```

Press **Enter** to send.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the AI Copilot Panel showing:
     - The user's message visible in the chat history.
     - The AI responding with "Researching your request..." and a thinking animation.
     - Thinking stages showing: "Analyzing requirements", "Researching NE555 datasheet".
     SUGGESTED SIZE: 400×500px (panel only)
-->
![AI Prompt Sent](../img/tutorial/ai-step2-prompt.png)

---

## Step 3 — Answer Clarifying Questions

The AI may ask clarifying questions:

```
┌─────────────────────────────────────────┐
│ AI: Before I design, a few questions:    │
│                                          │
│ 1. LED color preference?                 │
│    [● Red]  [○ Green]  [○ Blue]         │
│                                          │
│ 2. Duty cycle?                           │
│    [● 50%]  [○ 30%]  [○ 70%]           │
│                                          │
│ 3. Include on/off switch?                │
│    [● No]  [○ Yes]                      │
│                                          │
│ [Continue with selected options →]       │
└─────────────────────────────────────────┘
```

Select your preferences and click **Continue**.

---

## Step 4 — Review the Generated Design

The AI generates a BOM and netlist. The **Component Review** window opens:

### Expected BOM

| # | Designator | Part | Value | Purpose |
|---|---|---|---|---|
| 1 | U1 | NE555 | — | Timer IC |
| 2 | R1 | Resistor | 6.8kΩ | Timing resistor (charge path) |
| 3 | R2 | Resistor | 6.8kΩ | Timing resistor (charge + discharge) |
| 4 | R3 | Resistor | 330Ω | LED current limiter |
| 5 | C1 | Capacitor | 100µF | Timing capacitor |
| 6 | C2 | Capacitor | 10nF | Control voltage bypass |
| 7 | D1 | LED | Red | Visual indicator |
| 8 | J1 | Connector | 2-pin | Battery connection |

### Expected Netlist

```
Net "VCC":    J1.Pin1 → U1.VCC(8) → U1.RESET(4) → R1.Pad1
Net "GND":    J1.Pin2 → U1.GND(1) → C1.Pad2 → C2.Pad2 → D1.K
Net "DISCH":  U1.DISCH(7) → R1.Pad2 → R2.Pad1
Net "THRES":  U1.THRES(6) → U1.TRIG(2) → R2.Pad2 → C1.Pad1
Net "OUT":    U1.OUT(3) → R3.Pad1
Net "LED":    R3.Pad2 → D1.A
Net "CTRL":   U1.CTRL(5) → C2.Pad1
```

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Component Review window showing:
     - BOM tab with 8 components listed, all showing ✅ status.
     - Netlist tab visible with connection details.
     - The schematic preview showing the 555 timer circuit topology.
     SUGGESTED SIZE: 800×550px
-->
![AI BOM Review](../img/tutorial/ai-step4-review.png)

---

## Step 5 — Verify with Simulation

1. In the Component Review window, click **Verify with Simulation**.
2. The AI configures a transient analysis:
    - Stop time: 3 seconds (to see multiple blink cycles)
    - Step size: 1 ms
3. The simulation runs in the background.
4. Results appear in the Waveform Viewer:
    - **v(OUT)**: Square wave at ~1 Hz (the 555 output)
    - **v(THRES)**: Sawtooth charging/discharging of the timing capacitor

### Expected waveforms

```
v(OUT):   ┌──┐  ┌──┐  ┌──┐
          │  │  │  │  │  │
     ─────┘  └──┘  └──┘  └──  ← Square wave at ~1 Hz

v(THRES): /╲  /╲  /╲
         /  ╲/  ╲/  ╲         ← Charging/discharging between 1/3 and 2/3 VCC
```

!!! success "Simulation passes"
    If the output frequency is approximately 1 Hz and the waveform is a clean square wave, the design is verified. The AI confirms: *"Simulation passed — output frequency: 1.04 Hz"*.

<!-- TODO: Replace with actual screenshot
     SCENARIO: Capture the Waveform Viewer showing:
     - v(OUT) as a square wave (cyan trace).
     - v(THRES) as a sawtooth wave (yellow trace).
     - Time axis showing 0 to 3 seconds.
     - Cursors placed on two consecutive rising edges showing Δt ≈ 1s.
     SUGGESTED SIZE: 900×450px
-->
![Simulation Results](../img/tutorial/ai-step5-simulation.png)

---

## Step 6 — Place and Route

### Auto-Place

1. Click **Add to Project** in the Component Review window.
2. The AI auto-places components on the schematic:
    - U1 (NE555) in the center.
    - Timing components (R1, R2, C1) on the left.
    - Output components (R3, D1) on the right.
    - Power components (J1, C2) at the edges.

### Convert to PCB

1. Go to **Project → Convert to PCB**.
2. Footprints appear on the PCB with ratsnest lines.

### Auto-Route

1. Click **Auto-Route** (or use the AI panel's routing action).
2. The A* router processes all connections.
3. Traces appear on the board — ratsnest lines disappear.

<!-- TODO: Replace with actual video
     SCENARIO: Record a 20-second clip showing:
     1. Click "Add to Project" — schematic fills with placed components.
     2. Click "Convert to PCB" — PCB tab opens with footprints.
     3. Click "Auto-Route" — traces route automatically, progress bar visible.
     4. Final board shown fully routed.
     RESOLUTION: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/tutorial/ai-step6-place-route.webm" type="video/webm">
  <source src="../../img/tutorial/ai-step6-place-route.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Step 7 — DFM Check and Export

### Run DFM

1. Go to **Tools → DFM Check**.
2. Click **Run DFM** — verify 0 errors.

### Export

1. **Gerber**: File → Export → Gerber → select layers → Export.
2. **BOM**: File → Export → BOM → save as CSV.
3. **Verify**: Tools → Gerber Viewer → open F.Cu.gbr.

---

## Done! :material-check-decagram:{ style="color: #00E5FF" }

You've completed an AI-assisted design cycle:

```
Prompt → Research → Clarify → Design → Simulate → Place → Route → Export
```

| Deliverable | File |
|---|---|
| Project | `NE555_Blinker.prjxml` |
| Schematic | `NE555_Blinker.schxml` |
| PCB | `NE555_Blinker.pcbxml` |
| Gerber files | `F.Cu.gbr`, `F.SilkS.gbr`, `F.Mask.gbr`, `Edge.Cuts.gbr` |
| BOM | `NE555_Blinker_BOM.csv` |

---

## See Also

| Topic | Link |
|---|---|
| AI Copilot full guide | [AI Copilot Overview](../ai/index.md) |
| Manual simulation | [Simulation Guide](../simulation/index.md) |
| Manual routing | [PCB Routing](../pcb/routing.md) |
| NE555 manual tutorial | [NE555 LED Blinker Tutorial](index.md) |
