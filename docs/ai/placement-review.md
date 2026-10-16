---
description: How the WireFrame AI Copilot decides what can be drawn while findings are still open, marks them on the schematic, and carries your edits on the sheet back into the BOM plan and netlist.
---

# Placement Review and Your Edits

!!! info "In the next release"
    The placement review and edit sync described here are in WireFrame 1.5.47, which is in beta testing. The public download is still v1.3.8.

A design the Copilot drafts is rarely free of findings: a pull-up it is unsure of, a pin left floating, a part the library does not carry yet. Earlier builds refused to draw anything while a single critical finding was open, so a 300-part board could wait on one floating pin with nothing on the canvas to fix it on. Now the Copilot's reviewer, **Penalty**, separates two questions:

- *Is the design right?* — answered by the checks, as before;
- *Would the drawing be right?* — the only question that can keep a block off the sheet.

## What can wait, and what is drawn

Penalty reads the library and the netlist, never a model's opinion, and sorts every part into one of three outcomes.

| Outcome | When | What you see |
|---|---|---|
| **Drawn and marked** | Any finding the drawing shows honestly: a missing pull-up, a floating pin, an LED the wrong way round, a footprint that does not match its package, a part nobody has confirmed | The part is drawn as planned, with a red wash and **!** badge for a critical finding (its number from `/issues`) or an amber dot for a warning. Hover for the finding and its suggested fix; click to open it |
| **Left off its block** | A part that cannot be drawn yet (no symbol, a symbol that is another part) but is *not* what its block is built around — a status LED, a spare header | The block is drawn without it. When the part is fixed, **Update Schematic** draws the block again with it |
| **Held with its block** | The part the block is built around cannot be drawn — the MCU of an MCU block, an unbound regulator of its power block — or the drawing would be wrong: the netlist wires a pin the symbol does not have, one pin sits on two nets (it would short them), or a BOM row still stands for several parts | The block waits. The card names the part, the reason and the command that clears it, usually `/fix REF` |

Which part a block is built around is decided by weight: its connections, or the pins it should have when it is not wired yet. An unbound ESP32 module therefore still holds its own block, even though it is on no net.

## Cover what is marked

Critical findings and unconfirmed parts are yours to accept, not the Copilot's. The Penalty card in **BOM Review** shows a verdict — **READY TO PLACE**, **PLACE WITH ISSUES**, **PARTLY PLACEABLE** or **BLOCKED** — with what waits and why.

1. Read the card, or say `/place` in the chat for the full account.
2. Press **Place with issues (N)**, or say `/place now`. This records your decision for exactly the parts it lists.
3. Build the sheets as usual. Held blocks stay queued for **Update Schematic**.

A new critical on a part you already covered does not ask again. A critical on a part you have not covered does. Parts already on the sheet are never asked about twice.

## Fix it where you see it

Every mark carries the number the finding has in `/issues`, so the chat and the canvas speak about the same thing:

| You type | What happens |
|---|---|
| `/issues` | The numbered list: what is wrong, why it matters, what its fix would do |
| `fix 2` | Runs the fix for finding 2: a computed pin swap, the wiring agent, a repair agent, or `/fix` on the part |
| `explain 3` | Why finding 3 matters and what its fix would change, without changing anything |
| `accept 4 because the LED is decorative` | Records the finding as intentional; it is no longer counted or sent to a fix |

A repair agent that cannot tell what you meant asks you instead of guessing. Answer in the chat. If you write a new instruction about something else instead, it is treated as a new request, not as the answer.

## Your edits flow back into the plan

Once the sheets are drawn you will edit them by hand: change a value, swap a footprint, delete a part, rewire a pin, rename a net. Every edit on the undo stack carries who made it, you or the AI. After each edit WireFrame compares the drawing with the drawing the plan last matched and carries **your** changes into the BOM plan and netlist:

- value, footprint and symbol changes;
- parts you added or deleted (a part disappears from the plan only when you deleted it);
- pins moved between nets, pins disconnected, nets renamed or merged.

The chat reports each one, for example *R1 value 5.1k → 22k*, *C2 removed from the design*, *U1:1 disconnected (was on +3V3)*. Netlist Check runs again and the marks on the canvas follow. A value-only change keeps the part's confirmation.

The repair and wiring agents are told what you changed and are instructed never to undo it. In testing, a `fix 1` on a net you had disconnected on purpose made the agent ask *should U1:4 be reconnected?* rather than wire it back.

## After a revision

A revision such as *add an SPI TFT with touch* changes only the blocks it touches. **Update Schematic** redraws those in place and draws new blocks on the sheet of the block they connect to most. A block that is already on the sheet without a held part is not redrawn until it changes or the part is fixed. The update card then reads *nothing more to draw until …* and names the parts.

When a request does not fit the board — the FPGA has no free I/O, a 2 A regulator behind a 750 mA fuse — the Copilot stops and asks before it changes anything, with the options and the one it recommends.

## See also

- [AI Design Agent](design-agent.md)
- [Copilot Commands](commands.md)
- [Reference Designs](reference-designs.md)
- [Fix or Create a Component](component-generator.md)
