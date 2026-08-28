# Testbenches and Measurements

A waveform tells you what happened. A testbench lets you record what the circuit should do and asks WireFrame to check it after every run.

## A simple verification workflow

Add the expected load, choose a signal, define an acceptable limit, and run the simulation. Treat **Pass** as evidence for that requirement, **Fail** as a circuit or setup issue to investigate, and **Not measured** as an incomplete check.

### Image — Testbench with load and assertion

!!! note "Image needed"
    Capture the current **Testbench** tab with one load and one assertion, plus a visible Last run result. Do not use a generated flowchart in place of the real UI. Suggested size: **1100 × 760 px**.

Open the Simulation Workbench and select the **Testbench** tab. The heading shows whether you are editing the whole-sheet testbench or one selected circuit block.

## Add a load

Real circuits must power something. An output with no load can look better than it will in the final product.

1. Under **Loads**, choose the output net.
2. Click **Add**.
3. Enter the load required by your design.
4. Run the simulation again.

Use values taken from the product requirement, connected device, or component datasheet.

## Add an acceptance check

1. Under **Assertions**, click **Add**.
2. Choose the signal to check.
3. Choose a measurement.
4. Select **Within**, **At most**, or **At least**.
5. Enter the required value and tolerance.
6. Run the simulation.

### Common measurements

| Measurement | Example use |
|---|---|
| Minimum / Maximum | Make sure a rail never leaves its safe range |
| Peak-to-peak | Check total ripple or signal swing |
| Mean | Check the average DC output |
| RMS / AC RMS | Check signal level or ripple without the DC component |
| Frequency / Period | Verify an oscillator or clock |
| Duty cycle | Verify a PWM output |
| Rise / Fall time | Check switching speed |
| Overshoot | Check startup or edge quality |

## Exclude startup from a steady-state check

If the requirement applies only after startup, set a settled measurement window. You can also enable A/B cursors in **Signals** and measure only the interval between them.

For example, check the average `VOUT` after the regulator has settled instead of including its initial rise from 0 V.

## Understand the result

| Result | Meaning | What to do next |
|---|---|---|
| **Pass** | The measured value meets your limit | Keep the check and continue |
| **Fail** | The measured value is outside your limit | Inspect the waveform, source, load, and circuit |
| **Not measured** | WireFrame could not calculate the requested value | Check the selected signal, analysis, and measurement window |

!!! important
    **Not measured** is not a pass. Also, WireFrame does not assume what a “good” value should be—you must enter the requirement you want to verify.

## Ask Copilot for help

When Copilot is connected, select **Ask why** beside a failed or unmeasured result. Copilot receives the current signal, testbench, and result so it can help you investigate.

Review the explanation against the waveform and datasheet before changing the circuit.

## Before moving to PCB

- Use the same supply voltage and load expected in the final product.
- Add checks for every important output.
- Separate startup requirements from steady-state requirements.
- Resolve every **Fail** and **Not measured** result.
- Save a CSV when you need to share verification evidence.
