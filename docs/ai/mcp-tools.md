---
description: The fourteen tools WireFrame's MCP bridge offers your agent in 2.0.1 — what each one does, its parameters, and whether it only reads or may change the design — as wf-mcp-server --tools reports them.
---

# MCP Tool Reference

When your agent connects to WireFrame, the bridge offers it **fourteen tools**. This page describes each one as WireFrame 2.0.1 reports it. The names and descriptions are taken from `wf-mcp-server --tools` of 2.0.1, edited lightly for this guide; the parameters and the read-only marks are the ones each tool declares to your agent when it connects.

`wf-mcp-server --tools` prints the list as JSON and needs no WireFrame running, so it is a quick way to see what your copy has (where the bridge is: [Find the bridge](mcp-connect.md#find-the-bridge)). It prints all fourteen. A connected agent is offered the ones WireFrame can serve at that moment — started without WireFrame, the bridge offers none and says why.

None of them runs until you press **Allow** in WireFrame's AI panel — see [Allow it in WireFrame](mcp-connect.md#allow-it-in-wireframe). Each call is one MCP call, a read such as `is_busy` included; with `chat` and `run_command`, the turn WireFrame's agent takes also spends AI credits, as it would if you had typed the request in the panel. See [How calls are counted](mcp.md#how-calls-are-counted).

## The design tools behind `call_tool`

One of the fourteen, `call_tool`, reaches the design tools WireFrame's own Copilot works with. About 110 are defined. Which ones are offered follows what is open — the board tools need a board, the simulation tools a simulation — and with a board open there are **95**. They are listed by task on [Use WireFrame from your own agent](mcp.md#the-design-tools). Your agent can read the list as it stands, with every tool's parameters, from the resource `wireframe://tools`, without spending a call.

## What reads, and what may change the design

Each tool carries MCP's hints — `readOnlyHint`, and for the tools that are not read-only, `destructiveHint` — so your agent's client can decide what to ask you before it calls one:

| Marked | Tools |
|---|---|
| **Read-only** | `list_commands`, `read_transcript`, `is_busy` |
| **Not read-only, not destructive** | `stop`, `attach`, `new_session` |
| **May change the design** (destructive) | `chat`, `run_command`, `confirm_all`, `update_schematic`, `build_blocks`, `place_schematic`, `update_pcb`, `call_tool` |

`chat`, `run_command` and `call_tool` are marked as changing the design because they can: what they do depends on what is asked. A question in `chat`, `/bom`, or `call_tool` with `score_board` only reads; `/layout apply` or `call_tool` with `apply_layout` writes.

While WireFrame's agent is working on a turn, a call that would change the design is refused — and not counted — until the turn ends; tools that only read still answer. See [Nothing changes until it is applied](mcp.md#nothing-changes-until-it-is-applied).

## Talk to WireFrame's agent

`chat` and `run_command` wait for the turn to finish — up to half an hour — before they answer. A turn still running after that answers that it is still running, and nothing is lost: poll `is_busy`, then `read_transcript`. When a turn leaves a card waiting for a decision, its answer says so.

### `chat`

*May change the design. The turn spends AI credits as it would in the panel.*

Say something to WireFrame's design agent and get its answer, in plain language: what to build, a question about the open board, or an answer to something it asked. This is the main way to design — WireFrame's agent holds the board, the library, the part contracts and this project's memory, and picks its own tools. The call returns when the turn is done.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `message` | string | yes | What to say, in plain language |

### `run_command`

*May change the design. The turn spends AI credits as it would in the panel.*

Run one of WireFrame's slash commands. The ones a design uses most:

- `/layout [place,route|fresh reseed|fix|apply|discard|check]` lays the PCB out, and nothing changes until `apply`;
- `/board <describe it>` sets the board's shape;
- `/fix <REF> <what is wrong>` repairs one part;
- `/missing` lists the parts with no symbol;
- `/bom`, `/nets`, `/findings` and `/review` read the design;
- `/topology` weighs one board against a stack;
- `/erc review` sorts real faults from intended ones.

`list_commands` gives the rest. The call returns when the command is done. A command sent without its leading `/` is run as the command it names. What each command does is on [Copilot commands](commands.md).

| Parameter | Type | Required | Description |
|---|---|---|---|
| `command` | string | yes | The whole command, for example `/layout fresh reseed` |

### `list_commands`

*Read-only.*

Every slash command offered right now, with what it does. It makes no model call — read it before guessing a command. Like the `/` list in the chat, it offers what can run where you are; see [How the list is chosen](commands.md#how-the-list-is-chosen).

No parameters.

## Follow and answer a turn

### `read_transcript`

*Read-only.*

The conversation so far, newest last. Use it after a turn timed out, or to see what the agent decided and why.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `last` | integer | no | Only the last N messages. Omit for all |

### `is_busy`

*Read-only.*

Whether WireFrame's agent is still working: it answers `working` or `idle`. Poll it, rather than guess, when a turn reported that it was still running.

No parameters.

### `stop`

*Not read-only, not destructive.*

Cancel what the agent is doing. A layout that has not been applied changes nothing on the board.

No parameters.

### `confirm_all`

*May change the design.*

Accept every change WireFrame's agent is offering on a card right now; the answer lists what was accepted, and when nothing is offered, nothing is confirmed. **This writes to the design**: each change is one undo step, recorded against your agent in the project's ledger. The tool tells your agent to read the card first with `read_transcript`, and to ask you when the change is yours to approve.

No parameters.

## Prepare the next message

### `attach`

*Not read-only, not destructive.*

Put files in front of WireFrame's agent for the **next** `chat` message — a datasheet PDF, a pinout image, a reference project. The paths are on this machine. Files are given one by one, not folders, and nothing hidden: no file under a folder whose name starts with a dot. When some files are refused, the answer names them and says why, and the others are still attached.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `paths` | array of strings | yes | Absolute paths |

### `new_session`

*Not read-only, not destructive.*

Start a fresh conversation, keeping the planned BOM. Use it when the chat has grown long and the agent is repeating itself; the design is not lost.

No parameters.

## Build the design

These four turn a design planned in the chat into sheets and a board. In the panel, the same steps are the review's **Blocks** tab, **Update Schematic** and **Place with issues** — see [AI Design Agent](design-agent.md) and [Placement Review](placement-review.md).

### `update_schematic`

*May change the design.*

Draw the planned design onto the schematic sheets, or update them after a revision. When something is in the way, it reports the blocker instead. **This writes to the design.**

No parameters.

### `build_blocks`

*May change the design.*

Group the design into blocks and build the sheets from them — the step between a planned BOM and a drawn schematic. With `stage` set to `"group"` it proposes the grouping; with `"build"` it draws the sheets. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `stage` | string | yes | `"group"` or `"build"` |

### `place_schematic`

*May change the design — except with `review_only`.*

Place the parts on the sheets, marking anything still unresolved on the canvas rather than refusing. Without `review_only` it does what **Place with issues** does in the review: it covers the marked findings and places the parts — see [Placement Review](placement-review.md#cover-what-is-marked). With `review_only` it reports what can be drawn and what waits, and changes nothing.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `review_only` | boolean | no | Report without placing. Default `false` |

### `update_pcb`

*May change the design.*

Push the schematic's netlist onto the PCB and save it — footprints and nets are overwritten. Run it before any `/layout`, and again after the schematic changes. **This writes to the design and to disk.**

No parameters.

## Call a design tool

### `call_tool`

*May change the design, depending on the tool it calls.*

Call one of WireFrame's design tools directly by name, with JSON arguments. The catalogue is the resource `wireframe://tools`. `chat` and `run_command` are usually the better way: WireFrame's own agent sequences these tools better than a remote caller can. Reach for `call_tool` to read something specific — `get_board`, `score_board`, `check_board`, `read_layout`, `ipc_calc`, `calculate_impedance` — or to repeat an exact call.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | The tool's name, for example `score_board` |
| `arguments` | object | no | Its arguments. Omit for none |

A design tool opens what it reads: if no sheet or no board of the project is open, `call_tool` opens them before it runs. It reaches only the tools `wireframe://tools` lists for the open project; a name that is not one of them is refused, and still counts as a call — so let your agent read the list first, which is free.

## See also

- [Use WireFrame from your own agent](mcp.md) — the design tools by task, and how calls are counted
- [Connect Claude, Codex, Cursor or another agent](mcp-connect.md)
- [What waits for your approval](approvals.md)
- [Copilot commands](commands.md) — what `run_command` can run
