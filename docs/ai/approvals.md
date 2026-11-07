---
description: Every point where the AI's work in WireFrame waits for a person before it changes the design — confirmed parts, /fix plans, /layout on a copy, approved high-speed and power fixes, findings accepted with a reason, MCP's Allow card — and how each one is undone.
---

# What Waits for Your Approval

The AI in WireFrame — the Copilot in the panel, or your own agent over MCP — proposes; a person decides. This page lists each point where its work waits for you before it changes the design, what you press there, and the page that documents it.

## Before a design is planned

- **Clarifying questions.** The Copilot asks before it plans a design, and each question has a **Suggested** answer and **Or your own answer**. **Use all suggestions & continue** keeps each suggestion listed as an explicit assumption; it is not an approval of production requirements. See [Research and clarification](design-agent.md#research-and-clarification).

## Parts

- **A repaired or automatically bound part is not trusted until a person confirms it.** Look at its **Schematic Symbol View** and **Physical Footprint View**, then press **Confirm this component**; one confirmation covers every row that shares the symbol and the footprint, and the button says how many. See [Confirm the part](component-generator.md#confirm-the-part).
- **Only what a person confirmed is reused.** A confirmed part goes to the store every project can use; an automatic acceptance is never carried forward. See [Confirmed parts are reused — but judged again](../libraries/how-parts-are-found.md#confirmed-parts-are-reused-but-judged-again).
- **`/fix` shows its plan before it writes.** The plan appears in the chat with **Apply**, **Attach datasheet...** and **Cancel**, and nothing changes until you press **Apply**. An applied repair is recorded as a decision in project memory, so later runs do not undo it. See [Repair a part with `/fix`](component-generator.md#repair-a-part-with-fix).
- **A footprint generated from a datasheet** waits for the **REQUIRED HUMAN CHECKS** — **Pin 1 and orientation match**, **Shell tabs, holes and omitted balls match**, **Critical pitch and pad sizes match dimensions** — and **Approve & Apply**. Until then the top bar reads *Confirm AI review to Save/Sync*. See [Generate a footprint from a datasheet](../libraries/footprints-library.md#generate-a-footprint-from-a-datasheet).
- **A part lifted with `/reference`** arrives as a revision you review, and a row bound to the reference's own part stays **unconfirmed** — marked by the placement review — until you confirm it in BOM Review. See [How it lands on your board](reference-designs.md#how-it-lands-on-your-board).

## Drawing the schematic

- **Critical findings and unconfirmed parts are yours to accept, not the Copilot's.** **Place with issues (N)**, or `/place now`, records your decision for exactly the parts it lists; a new critical on a part you have not covered asks again. See [Cover what is marked](placement-review.md#cover-what-is-marked).
- **A finding is accepted with a reason.** `accept 4 because the LED is decorative` records finding 4 as intentional; it is no longer counted or sent to a fix. `explain 3` says why finding 3 matters and what its fix would change, without changing anything. See [Fix it where you see it](placement-review.md#fix-it-where-you-see-it).
- **A request that does not fit the board stops first.** When the FPGA has no free I/O or a 2 A regulator sits behind a 750 mA fuse, the Copilot asks before it changes anything, with the options and the one it recommends. See [After a revision](placement-review.md#after-a-revision).

## Laying out the board

- **The copper layer count is your decision.** The Copilot asks for it before the first layout, records the answer for the project, and does not lay a board out until you have answered. See [Choose the copper layer count first](auto-placer-router.md#choose-the-copper-layer-count-first).
- **`/layout` works on a copy.** The card has **Stop** while it runs, then **Apply to the board** (or **Apply this option**) and **Discard**; nothing changes on the board until you apply. When it lays the board out several ways, it shows the comparison and asks which to apply. See [Lay the PCB out with `/layout`](auto-placer-router.md#lay-the-pcb-out-with-layout).
- **A net class changes only if you allowed rule changes** — never below the fabricator's minimum — and the Copilot says which classes it changed and asks you to accept them. See [Ways to use `/layout`](auto-placer-router.md#ways-to-use-layout).
- **One board or several is your choice.** `/topology` measures the options side by side; the option written to the project's board stack, and a split into boards, are the ones you chose. See [One board or a tower](auto-placer-router.md#one-board-or-a-tower-topology).

## High-speed and power fixes

- **High-Speed Workbench**: a fix moves through **Proposed → Previewed → Approved → Applied**. **Preview** runs the checks again on a copy; **Approve** is a person's alone, and records who approved it and on which revision of the board; **Apply to the board** writes it as one undoable step, and **Roll back** takes it back. A statement about the board — an interface, a rail's voltage or load step, the EMC limit — is a fix of its own, approved like any other. See [Fixes](../high-speed/fixes-and-report.md#fixes).
- **The Copilot can propose a high-speed fix; it cannot approve one**, set a result's status or produce evidence. Applying refuses any patch a person did not approve in the Workbench, on the same revision it was previewed on. See [What the AI Copilot can do here](../high-speed/fixes-and-report.md#what-the-ai-copilot-can-do-here).
- **Power Analyzer**: **Suggest fixes** proposes; **Preview** solves the changed board so you see the new voltages; a person chooses **Approve** or **Reject**; **Apply** makes it one undoable step. See [Fixes](../power/power-analyzer.md#fixes).

## Your own agent, over MCP

- **Allow or Decline.** The first time your agent calls a tool, WireFrame's AI panel shows a card — *"claude-ai wants to work on this design over MCP"* — with **Allow** and **Decline**. Nothing runs until you press **Allow**, and those calls are not counted. The permission lasts until the agent disconnects; the next connection asks again, and **Revoke** takes it back. See [Allow it in WireFrame](mcp-connect.md#allow-it-in-wireframe).
- **Copy first.** Every tool that would move a part, lay copper or rewrite a rule works on a copy and reports what it would do — `propose_layout`, `evaluate_layouts`, `preview_patch`, `power_preview_fix`. The change reaches the board only through a step that applies it, such as `apply_layout` or `apply_placement`. See [Nothing changes until it is applied](mcp.md#nothing-changes-until-it-is-applied).
- **Some changes wait for you, in WireFrame.** `apply_approved_patch` and `power_apply_approved_fix` apply only what a person approved in WireFrame's own window. The number of copper layers and a split into several boards are your answers: the agent records them, it does not choose for you.
- **What your agent can press for you.** `confirm_all` accepts every change offered on a card, and `place_schematic` places as **Place with issues** does. Both are marked as changing the design; `confirm_all` tells your agent to read the card first and to ask you when the change is yours to approve. See the [MCP tool reference](mcp-tools.md#confirm_all).

## Undo, and who made a change

- **Each applied step is one undo step.** An applied layout comes back one stage at a time with ++ctrl+z++; an applied high-speed or power fix is one undoable step; each change `confirm_all` accepts is one undo step, and each MCP step that applies is recorded against the client that made it.
- **Every edit on the undo stack carries who made it** — you or the AI. Your edits on the sheet are carried into the BOM plan and the netlist, and the repair and wiring agents are told never to undo them. See [Your edits flow back into the plan](placement-review.md#your-edits-flow-back-into-the-plan).

## See also

- [How the agent understands a project](how-the-agent-works.md)
- [Placement Review and Your Edits](placement-review.md)
- [Fixes, Reports and the AI](../high-speed/fixes-and-report.md)
- [Use WireFrame from your own agent](mcp.md)
