---
description: The 29 tools WireFrame's MCP bridge offers your agent in 2.0.3 — what each one does, its parameters, whether it only reads or may change the design, and whether it counts as a call.
---

# MCP Tool Reference

When your agent connects to WireFrame, the bridge offers it **29 tools**. This page describes each one as WireFrame 2.0.3 reports it. The descriptions are the ones `wf-mcp-server --tools` of 2.0.3 prints, edited lightly for this guide; the parameters and the read-only marks are the ones each tool declares to your agent when it connects. WireFrame 2.0.1 and 2.0.2 offer fourteen of them, call `ask_penalty` `chat`, and count every call.

`wf-mcp-server --tools` prints the list as JSON and needs no WireFrame running, so it is a quick way to see what your copy has (where the bridge is: [Find the bridge](mcp-connect.md#find-the-bridge)). It prints all 29. A connected agent is offered them only while WireFrame is open and signed in to a plan that includes MCP — started without WireFrame, or with nobody signed in, the bridge offers none and says why.

None of them runs until you press **Allow** in WireFrame's AI panel — see [Allow it in WireFrame](mcp-connect.md#allow-it-in-wireframe). Only a call that changes the design, or puts Penalty, WireFrame's own agent, to work, counts as an MCP call; reading, checking and analysing are free. With `ask_penalty`, `run_command` and `build_blocks`, Penalty's job also spends AI credits, as it would if you had typed the request in the panel. See [How calls are counted](mcp.md#how-calls-are-counted).

## The design tools behind `call_tool`

One of the 29, `call_tool`, reaches the design tools WireFrame's own Copilot works with. Which ones are offered follows what is open — the board tools need a board, the simulation tools a simulation — and on a real project with its schematic and board open there are **117**. They are listed by task on [Use WireFrame from your own agent](mcp.md#the-design-tools). `list_design_tools` gives the list as it stands, and one tool's full description with `name`; the resource `wireframe://tools` gives every tool's parameters. Both are free.

A design tool that can run for minutes — `propose_layout`, `optimize_layout`, `evaluate_layouts`, `propose_placement`, `propose_floorplans`, `close_open_connections`, `analyze_current`, `analyze_thermal`, `run_simulation`, `research_layout`, `repeat_channel` — answers within `wait_s` seconds (20 unless your agent asks for up to 50) or carries on as a job, and `job_status` gives its answer when it is done.

## What reads, and what may change the design

Each tool carries MCP's hints — `readOnlyHint`, and for the tools that are not read-only, `destructiveHint` — so your agent's client can decide what to ask you before it calls one:

| Marked | Tools |
|---|---|
| **Read-only** | `read_design`, `read_guide`, `design_status`, `list_commands`, `read_transcript`, `is_busy`, `list_design_tools`, `job_status` |
| **Not read-only, not destructive** | `stop`, `attach`, `new_session` |
| **May change the design** (destructive) | `submit_bom`, `bind_part`, `install_part`, `confirm_parts`, `submit_netlist`, `revise_design`, `submit_blocks`, `edit_schematic`, `resolve_erc`, `save_design`, `ask_penalty`, `run_command`, `confirm_all`, `update_schematic`, `build_blocks`, `place_schematic`, `update_pcb`, `call_tool` |

`ask_penalty`, `run_command` and `call_tool` are marked as changing the design because they can: what they do depends on what is asked. `/bom`, or `call_tool` with `score_board`, only reads; `/layout apply`, or `call_tool` with `apply_layout`, writes. What counts as a call follows what really happens, not the mark: `call_tool` with `score_board` is free.

While Penalty is working on a job, a call that would change the design is refused — and not counted — until the job ends; so is a write, or a second long design tool, while a long design tool runs as a job. Tools that only read still answer. See [What changes the design, and what waits](mcp.md#what-changes-the-design-and-what-waits).

## Start here

Free, however often your agent calls them. An agent that reads `read_guide` before each stage and loops on `design_status` until it says done does better work for the same calls.

### `read_guide`

*Read-only. Free.*

How to design a board here: the way of working and what good looks like, by topic. Read start_here first and each stage's guide before that stage. With no topic it lists them.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `topic` | string | no | start_here, schematic, parts, board_and_floorplan, power_stage, decoupling, routing, signal_and_noise, thermal, manufacturing, review |

### `design_status`

*Read-only. Free.*

Is this design done? ERC, board checks, open connections, signal integrity and manufacturability in one answer, with `done` and what remains. Loop until done is true, or until what remains is the person's to decide.

No parameters.

### `read_design`

*Read-only. Free.*

The plan as it stands: every part with its binding and what blocks it, every net, the checkers' findings, the blocks and sheets. `pins` adds the real pin tables: read them before writing a netlist, because pin numbers come from the symbols, never from memory. A list of designators gives those parts' tables whole; `true` gives a long BOM's in part.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pins` | boolean or array | no | true, or a list of designators. Default none |

### `list_design_tools`

*Read-only. Free.*

The design tools call_tool can run on this project, one line each. Pass `name` for one tool's full description and arguments.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | no | A tool's name. Omit for the list |

### `job_status`

*Read-only. Free.*

The answer of a long tool that outlasted its call (optimize_layout, propose_layout, close_open_connections...). Says if it is still running, else gives its result. Omit `job` for the latest. `wait_s` waits up to 50 s first.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `job` | string | no | The id the call gave, e.g. "j3" |
| `wait_s` | integer | no | Seconds to wait first. Default 0 |

## Write the design yourself

Your agent's own work: the BOM, the bindings, the wiring, the blocks and sheets, and the push to the board. Each one counts as a call.

### `submit_bom`

*Changes the design. Counts as a call.*

Write the BOM yourself. Replaces the plan's parts and clears its wiring and blocks. Held to the same checks as any BOM, then every row is matched to the library; the answer says what bound and what blocks each row that did not. One physical part per row: a quantity above 1 is split. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `components` | array | yes | The parts |
| `requirement` | string | no | What the board must do, for the checks and later readers |
| `summary` | string | no | One line on the design |

### `bind_part`

*Changes the design. Counts as a call.*

Bind one BOM row to exactly the symbol and footprint you chose, overruling the matcher. `symbol` is a name in a loaded library, `symbol_file` an absolute path to a .kicad_sym to import. `footprint` is a footprint name, a standard land such as "0805 (SMD Passive)", or a wire pad in any size such as "SolderWirePad_1x01_SMD_3.5x4.5mm" ("SolderWirePad_1x01_THT_3.5x4.5mm_D1.7mm" with a plated hole for the wire); those two are made if they are not there yet. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `footprint` | string | no | Library footprint name |
| `id` | string | yes | The row's designator |
| `symbol` | string | no | Library symbol name |
| `symbol_file` | string | no | Absolute path to a .kicad_sym |

### `install_part`

*Changes the design. Counts as a call.*

Get a part the library does not hold yet, into this project's library. With `ids`: the part number those BOM rows name, as sold, from WireFrame's published library and then LCSC, bound to those rows. With `draft`: the id of a part draft_part drafted; bind it afterwards with bind_part. Calls no model. **This writes to the design and to disk.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `draft` | string | no | A draft's id from draft_part |
| `ids` | array | no | BOM rows to install for; rows naming one part share it |

### `confirm_parts`

*Changes the design. Counts as a call.*

Accept parts you have checked. Only a row that passes the checks can be confirmed. A confirmed row is protected from Penalty's work, and the record says you confirmed it, not a person. Rows sharing one symbol and footprint are confirmed together. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `ids` | array | yes | Designators |

### `submit_netlist`

*Changes the design. Counts as a call.*

Write the wiring yourself, against the parts now bound. A part you leave out of every net is left unwired rather than refused. The answer carries the checkers' findings. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `netlist` | array | yes | The nets |
| `summary` | string | no | One line on the design |

### `revise_design`

*Changes the design. Counts as a call.*

Change only what you name; every other row keeps its binding and confirmation and only the blocks you touch are redrawn. Use it instead of resubmitting. `set_components`: rows by `id` with only the fields that change (name, type, role, value, package, rationale, pin_count, quantity, block); a new id adds a part. `remove_components`: ids. `set_nets`: nets by `name` with all their `pins`. `remove_nets`: names. A part that loses its binding is reported, not fetched for you. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `remove_components` | array | no | Designators to remove |
| `remove_nets` | array | no | Net names to remove |
| `set_components` | array | no | Rows by `id` with only the fields that change: name, type, role, value, package, rationale, pin_count, quantity, block. A new id adds a part |
| `set_nets` | array | no | Nets by `name`, each with all its `pins` |
| `summary` | string | no | What this revision does |

### `submit_blocks`

*Changes the design. Counts as a call.*

Split the parts into blocks and pages yourself, and draw the sheets. Every physical part in exactly one block, every block on exactly one page. Leave out `sheets` for one page per block. **This writes to the design and to disk.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `blocks` | array | yes | The blocks; every physical part in exactly one |
| `build` | boolean | no | Draw the sheets now. Default true |
| `sheets` | array | no | The pages; every block on exactly one. Leave out for one page per block |

### `edit_schematic`

*Changes the design. Counts as a call.*

Change the drawn schematic directly, as one undo step. `edits` are the ops call_tool preview_edit takes: add_component, remove_component, connect, disconnect, set_value. Checked here against the design: a change that introduces an error is refused. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `edits` | array | yes | The changes — `add_component`, `remove_component`, `connect`, `disconnect`, `set_value`, the ops `preview_edit` takes |
| `reason` | string | yes | One sentence, kept in the chat for the person |
| `sheet` | string | no | Which sheet, by name. Default: the one that holds these parts |

### `update_schematic`

*Changes the design. Counts as a call.*

Draw the planned design onto the schematic sheets, or update them after a revision. Reports the blocker instead when something is in the way. **This writes to the design.**

No parameters.

### `place_schematic`

*Changes the design. Counts as a call — except with `review_only`, which changes nothing and is free.*

Place the parts on the sheets, marking anything still unresolved on the canvas rather than refusing. With `review_only` it reports what can be drawn and what waits, and changes nothing.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `review_only` | boolean | no | Report without placing. Default false |

### `resolve_erc`

*Changes the design. Counts as a call.*

Act on what call_tool run_erc found, by its #numbers. `fix`: WireFrame's own fixes (No-Connect on a pin meant to stay open, PWR_FLAG on a rail fed from a connector, a dangling wire). `exclude`: items the design means, kept with `why`. Answers the ERC totals after. **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `exclude` | array | no | ERC item numbers the design means, kept with `why` |
| `fix` | array | no | ERC item numbers for WireFrame's own fixes |
| `why` | string | no | Why these are right |

### `update_pcb`

*Changes the design. Counts as a call.*

Push the schematic's netlist onto the PCB and save it — footprints and nets are overwritten. Run this before any /layout, and again after the schematic changes. **This writes to the design and to disk.**

No parameters.

### `save_design`

*Changes the design. Counts as a call.*

Write every open sheet and board to disk. An applied layout and an edited sheet stay in the window until this runs. **This writes to disk.**

No parameters.

## Hand a job to Penalty

Penalty is WireFrame's own agent. `ask_penalty`, `run_command` and `build_blocks` wait for the job to finish — up to half an hour — before they answer. A job still running after that answers that it is still running, and nothing is lost: poll `is_busy`, then `read_transcript`.

### `ask_penalty`

*Changes the design. Counts as a call; the job also spends AI credits, as it would in the panel.*

Give Penalty, WireFrame's built-in co-pilot, one bounded job. You decide the design; Penalty does what you hand it: find candidates for a part, draft a symbol from a datasheet, review what you wrote, answer something it asked. The answer ends with what WireFrame measured it changing. Its report is a claim: check it against that. Spends the account's AI credits. Blocks until the job is done.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `task` | string | yes | The job, in plain language, naming what it may touch |

### `run_command`

*Changes the design. Counts as a call; the job also spends AI credits, as it would in the panel.*

Have Penalty run one of WireFrame's slash commands. The ones a design uses: `/layout [place,route|fresh reseed|fix|apply|discard|check]` lays the PCB out and nothing changes until `apply`; `/board <describe it>` sets the shape; `/fix <REF> <what is wrong>` repairs one part; `/missing` lists parts with no symbol; `/bom`, `/nets`, `/findings`, `/review` read the design; `/topology` weighs one board against a stack; `/erc review` sorts real faults from intended ones. Call list_commands for the rest. Blocks until the command is done.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `command` | string | yes | The whole command, e.g. "/layout fresh reseed" |

### `list_commands`

*Read-only. Free.*

Every slash command Penalty offers right now, with what it does. Cheap, no model call — read it before guessing a command.

No parameters.

### `build_blocks`

*Changes the design. Counts as a call; the job also spends AI credits, as it would in the panel.*

Have Penalty group the design into blocks and build the sheets from them. Spends AI credits; to decide the grouping yourself use submit_blocks. `stage` is "group" (propose the grouping) or "build" (draw the sheets). **This writes to the design.**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `stage` | string | yes | "group" or "build" |

### `confirm_all`

*Changes the design. Counts as a call.*

Accept everything Penalty is currently offering, unseen. Prefer confirm_parts, which names what you checked. **This writes to the design** — every change is one undo step, attributed to this client in the project's ledger.

No parameters.

## Follow and steer a job

None of these changes the design, and none counts.

### `read_transcript`

*Read-only. Free.*

The conversation so far, newest last. Use it after a job timed out, or to see what Penalty did and why.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `last` | integer | no | Only the last N messages. Omit for all |

### `is_busy`

*Read-only. Free.*

Whether Penalty or the library match is still working. Poll this instead of guessing when a call reported that it was still running.

No parameters.

### `stop`

*Changes nothing in the design. Free.*

Cancel what Penalty is doing, or the long tool running as a job. A layout that has not been applied changes nothing on the board.

No parameters.

### `attach`

*Changes nothing in the design. Free.*

Put files in front of Penalty for the NEXT job — a datasheet PDF, a pinout image, a reference project. Paths on this machine.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `paths` | array | yes | Absolute paths |

### `new_session`

*Changes nothing in the design. Free.*

Start a fresh conversation with Penalty, keeping the planned BOM. Use it when the chat has grown long and Penalty is repeating itself; the design is not lost.

No parameters.

## Call a design tool

### `call_tool`

*Counts as a call only when the design tool it names changes the design; a design tool that reads, checks, analyses or proposes is free.*

Call one of WireFrame's design tools by name, with JSON arguments: the board, library, datasheet, layout, simulation and power engines Penalty uses. You choose and sequence them. list_design_tools shows what this project offers. Writes under names like apply_, edit_ and set_ land on the design. Their descriptions were written for Penalty: where one says to ask the person first, the decision is yours.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `arguments` | object | no | Its arguments. Omit for none |
| `name` | string | yes | The tool's name, e.g. "score_board" |
| `wait_s` | integer | no | A long tool waits this long (up to 50 s, default 20), then continues as a job: see job_status |

A design tool opens what it reads: if no sheet or no board of the project is open, `call_tool` opens them before it runs. It reaches only the tools `list_design_tools` lists for the open project; a name that is not one of them is refused, nothing runs, and the call is given back — the answer ends "No call was counted."

## See also

- [Use WireFrame from your own agent](mcp.md) — the design tools by task, and how calls are counted
- [Connect Claude, Codex, Cursor or another agent](mcp-connect.md)
- [What waits for your approval](approvals.md)
- [Copilot commands](commands.md) — what `run_command` can run
