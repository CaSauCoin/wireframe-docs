---
description: What WireFrame's AI agent works from — the design graph, part contracts and library checks, datasheets WireFrame downloads itself, project memory and the record of who edited what — what it does not see, and how your own agent reaches the same engines over MCP.
---

# How the Agent Understands a Project

WireFrame's AI Copilot — **Penalty**, in the chat — does not design from what a model remembers about parts, or from a guess at what your files say. It works from what WireFrame itself has read, measured and checked, and the model reasons over that. The model proposes; WireFrame's own code supplies the facts and checks the answer.

This page says what the agent works from, what it does not see, and how your own agent reaches the same engines over MCP. It links to the pages that cover each part in detail.

## What it works from

### The design graph

On a schematic, the agent answers from WireFrame's **design graph** — the parts, pins and nets read from your sheets, rebuilt whenever they change. On a board it reads the same graph plus the board itself. The findings in it come from WireFrame's own checks: `/findings` lists them with no model call, and `/rebuild` reads the graph again from the project files when an answer looks out of date. See [Copilot commands](commands.md#schematic).

Before there is a schematic, the agent holds a **draft** — the requirements, the BOM it chose and the netlist it is wiring — and reads it back with a tool (`get_draft`) rather than from its memory of the conversation. `/bom`, `/nets` and `/missing` show you the same draft. See [Planning a design in the chat](commands.md#planning-a-design-in-the-chat).

### Parts, and the checks a part must pass

Whether a part binds is decided by code, not by the model. The agent may propose a part; deterministic checks decide — the kind of part, its contact count, every symbol pin against a pad, the pads against the package drawing, copper that would short — and they give the same answer every time. Before it names a part in a BOM, the agent confirms the part is in the library on this machine (`search_library`, `check_pool`, `inspect_library_symbol`). See [How a Part Is Found](../libraries/how-parts-are-found.md).

### Part contracts

What a part needs electrically — supply range, decoupling, pull-ups, strapping pins — is worked out from its datasheet and kept as the part's **contract** (`/contract U1`). A contract belongs to the part, not to the project, so every board that uses the part is held to it: by later reviews and `/findings`, and by [Live Checks](../live-checks.md) as you draw. When no contract covers a requirement, the agent's tool (`get_contract`) says it is **unknown** rather than guessing. See [`/contract`](datasheets-and-memory.md#contract-what-a-part-needs-electrically).

### Datasheets WireFrame downloads itself

Pin functions and electrical limits come from a datasheet WireFrame has **actually downloaded**: the PDF you attach first, then the link in the library index, then the web — where the model may name a URL, but WireFrame downloads the file itself, keeps its hash and extracts the text. A link that does not download produces no claim, and a requirement with no downloaded page behind it is kept but capped, so it can never be reported as a fault. See [Where the datasheet comes from](datasheets-and-memory.md#where-the-datasheet-comes-from).

The agent can also ask that downloaded document what it says on a topic (`read_datasheet`), and establish what is known about one exact part number before it drafts the part (`research_part`).

### Measurements, and pictures of what it drew

On the High-Speed Workbench's pages, every number the agent quotes comes from an engine run — see [Fixes, Reports and the AI](../high-speed/fixes-and-report.md#what-the-ai-copilot-can-do-here). A trace's or a via's current comes from `ipc_calc`, computed to IPC and never quoted from memory, and `score_board` gives the number the panel would show.

It also looks at what it made: a picture of the sheet as it is drawn (`view_sheet`) and a top-down picture of the board's placement (`view_placement`), each block in its own colour.

### Project memory, and who edited what

The agent keeps durable facts per project — requirements, constraints, decisions, corrections and preferences. They survive closing the chat, a new session and reopening the project: `/memory` lists them, `/remember` pins one and `/forget` drops one. A newer decision about the same subject replaces the older one, and the history is kept. Long sessions are summarized. See [Project memory](datasheets-and-memory.md#project-memory).

Some decisions are written down for it: an applied `/fix` repair, so later runs do not undo it; the layout rules a layout used, once you apply it, so the next conversation starts from them; and a finding you accept with a reason (`accept 4 because …`), which is no longer counted or sent to a fix.

Every edit on the undo stack carries **who made it** — you or the AI. After each edit, WireFrame carries your changes into the BOM plan and the netlist, and the repair and wiring agents are told what you changed and never to undo it. A change of yours that keeps the checks is your decision and is never reverted; one that breaks a check is pointed out and asked about. See [Your edits flow back into the plan](placement-review.md#your-edits-flow-back-into-the-plan).

### The tools it may call, and the edits it may only propose

The agent works through tools. About 110 are defined. Which ones are offered follows what is open — the board tools need a board, the simulation tools a simulation — and with a board open there are 95. They are listed by task on [Use WireFrame from your own agent](mcp.md#the-design-tools): the same tools your own agent reaches over MCP.

Most of them read or measure. The ones that would change the design come in two kinds:

- **Proposals**, worked out on a copy and reported, changing nothing: a layout (`propose_layout`, `evaluate_layouts`), a placement (`propose_placement`), a high-speed patch (`propose_patch`, `preview_patch`), a power fix (`power_propose_fix`, `power_preview_fix`), a part repair from `/fix`.
- **Steps that apply**, each one undoable: `apply_layout` and `apply_placement` apply what was proposed; `apply_approved_patch` and `power_apply_approved_fix` apply only what a **person** approved in WireFrame's own window. The model can propose; it cannot approve, set a result's status or produce evidence.

Some answers are never the agent's to give: the number of copper layers, splitting a product into several boards, and which of several measured options to keep. It asks, and records your answer. Every gate is listed on [What waits for your approval](approvals.md).

## What it does not see

- **Not the whole project with every question.** A request carries your message and the part of the design it is about — a block, a net, the BOM rows in question, a datasheet page. Mention a reference designator (`U1`) or a net name (`VBUS`) and only that part of the design is sent with it. See [What is sent, and where](models-and-credits.md#what-is-sent-and-where).
- **Not your other projects.** A project's own library is data of that project: the matcher refuses its files for another project, and a part reaches another project only after a person confirms it. Over MCP, an agent cannot reach a project other than the one open.
- **Not a datasheet WireFrame did not download.** A paragraph the model *says* it read is never presented as evidence.
- **Not what nobody stated.** Load currents are yours to state — WireFrame does not guess a chip's consumption. A stack-up nobody confirmed caps every high-speed result at **WARNING**, and a missing input such as a rise time or a load step makes a result **UNKNOWN**, never PASS. See [High-Speed Workbench](../high-speed/index.md#two-rules-behind-every-page) and [Power Analyzer](../power/power-analyzer.md#what-it-does-not-do).
- **No copy in a cloud.** Your projects stay on your computer. WireFrame AI records which task was run and what it cost — not the contents of your messages or your design.

## Your own agent, over MCP

An agent you run yourself — Claude, Codex, Cursor or another MCP client — reaches the same engines through `wf-mcp-server`, the bridge installed beside WireFrame. The bridge talks to the WireFrame you have open over a local socket in your own user folder; there is no network port. See [Connect Claude, Codex, Cursor or another agent](mcp-connect.md).

It can work in two ways:

- **Hand the request to WireFrame's agent** with `chat` or `run_command`. WireFrame's agent then works from everything above — the design graph, the contracts, the datasheets, the project's memory — with its own sequencing, and spends your plan's AI credits exactly as it would if you had typed the request in the panel.
- **Call the design tools itself** with `call_tool`. The reasoning is your agent's, and WireFrame supplies the measurements, by the same code that answers the Copilot panel: `score_board` over MCP gets the number the panel would show. Such a call spends no AI credits.

Either way the same rules hold. Nothing runs until you press **Allow**; proposals work on a copy; a high-speed patch or a power fix waits for your approval in WireFrame's own window; and each step that applies is one undoable step, recorded against the client that made it. Your agent cannot reach another project or export Gerbers, and only one client is connected to a WireFrame at a time.

What your agent does with an answer is between you and your agent's provider. For MCP itself, WireFrame sends your account only how many calls were used and the name of the agent that used them. See [Your design stays on your machine](mcp.md#your-design-stays-on-your-machine) and the [MCP tool reference](mcp-tools.md).

## See also

- [AI Copilot overview](index.md)
- [Datasheets, Repairs and Project Memory](datasheets-and-memory.md)
- [How a Part Is Found](../libraries/how-parts-are-found.md)
- [What waits for your approval](approvals.md)
- [Use WireFrame from your own agent](mcp.md)
