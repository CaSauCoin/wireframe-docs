# Copilot Commands

Type `/` in the AI Copilot chat box to open the command list. The list filters as you type; use the arrow keys and **Enter** to pick a command, or keep typing its arguments. `/help` prints the same list inside the chat.

Anything that does not start with `/` is an ordinary question. Mention a reference designator (`U1`) or a net name (`VBUS`) and only that part of the design is sent with the question.

### Image — Copilot command list

!!! note "Image capture brief"
    1. **Prepare:** Open the sample project with a schematic and a PCB, and open **View → AI Copilot Chat**.
    2. **Build the frame:** Type `/` in the chat box so the command list opens under it, with the first rows and their descriptions readable. Suggested size: **900 × 620 px**.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Commands that read the design you are planning

These work on the BOM and netlist being planned in the current chat, before any schematic exists. They read the plan directly and make **no model call**, so they are instant and free.

| Command | What it does |
|---|---|
| `/bom` | The planned BOM and which rows are still unresolved |
| `/nets` | Every net in the planned design and the pins on it |
| `/missing` | Parts with no library symbol yet — these cannot be placed until resolved |
| `/specs` | The requirements the design was built from, and what was assumed on your behalf |
| `/arrange [BLOCK] [how]` | Lay one functional block out again as you describe it, for example `/arrange STM32 MCU crystal left of U1` |

### Resume a design run

If a long design run stops — the provider failed, a quota ran out, you changed the model — resume it instead of starting over:

| Command | Resumes from |
|---|---|
| `/retry-research` | The retained original request, after you fix the provider |
| `/retry-bom` | The retained research; only unresolved BOM rows are re-selected |
| `/retry-bom-all` | The retained research; every BOM row is regenerated, including verified parts |
| `/retry-netlist` | The current saved BOM; wiring is generated again |

## Commands that work on the open project and board

These need a project open. Board questions are answered from WireFrame's design graph, which is rebuilt from your schematic and PCB files.

| Command | What it does |
|---|---|
| `/review` | Review the open board: netlist, findings, and what is likely to break |
| `/report` | Write a full design report |
| `/findings` | List what WireFrame's own checks found — no model call, no token cost |
| `/focus <U1 \| NET \| U1:3>` | Pin every later question to that part, net, or pin |
| `/unfocus` | Clear the pinned focus |
| `/rebuild` | Rebuild the design graph from the project files; the errors and warnings are listed in the chat when it finishes |
| `/board <describe the board>` | Set the board's shape from a sentence — see [Board Shape and Outline](../pcb/board-outline.md) |
| `/topology [what you want]` | One board or a tower of boards, with the options measured side by side |
| `/layout [stages \| apply \| discard \| rules \| check \| request]` | Lay the PCB out and watch it live; nothing changes until you apply — see [Placement and Routing Assistant](auto-placer-router.md) |

## Commands for one component

| Command | What it does |
|---|---|
| `/contract <U1> [file.pdf]` | Work out what the part needs electrically — decoupling, pull-ups, strapping — from its datasheet, and store it for later checks |
| `/pins [U1]` | Name a bound symbol's blank pins from the datasheet, keeping the pin numbers; without a reference, every such part |
| `/fix <U1> <what is wrong> [file.pdf]` | Repair one part: describe the problem, optionally attach the datasheet; WireFrame proposes before changing anything |

See [Datasheets, Repairs and Project Memory](datasheets-and-memory.md) for how these use datasheets.

## Project memory

| Command | What it does |
|---|---|
| `/memory` | What this project has established across all conversations |
| `/remember <text>` | Pin something the assistant must not forget, for example `/remember no electrolytic capacitors` |
| `/forget <id>` | Drop one remembered fact; the id comes from `/memory` |
| `/help` | Show the command list in the chat |

Memory belongs to the project, not to one chat session, so it outlives every conversation about that project.

## Tips

- Use `/findings` before `/review`: it is free and often answers the question.
- `/fix` repairs **one** part. For the whole board's errors and warnings, use `/findings`.
- Commands answer in the language of the conversation — English or Vietnamese, detected from what you have written.

## See also

- [AI Copilot](index.md)
- [Placement and Routing Assistant](auto-placer-router.md)
- [Datasheets, Repairs and Project Memory](datasheets-and-memory.md)
