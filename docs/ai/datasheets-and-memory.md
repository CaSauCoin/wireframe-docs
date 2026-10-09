# Datasheets, Repairs and Project Memory

Three Copilot commands work on **one component** at a time and lean on its datasheet: `/contract`, `/pins`, and `/fix`. A fourth group, `/memory`, `/remember`, and `/forget`, keeps decisions that must outlive a single conversation.

## Where the datasheet comes from

WireFrame looks for a datasheet in this order and stops at the first that works:

1. **The PDF you attach** — add its path at the end of the command, for example `/contract U1 ~/Downloads/tps62902.pdf`. This is the most reliable source: it is the document you chose, not one matched by name.
2. **The published component index** — free and instant, but many proprietary, renamed, and obsolete ICs have no datasheet link there.
3. **The web** — the model is asked for the URL of the datasheet; **WireFrame downloads the file itself**, records its hash, and extracts the text.

The third step is deliberate: a URL the model made up simply fails to download, and a failed download produces no conclusion. Copilot never presents a paragraph the model *says* it read as evidence. Requirements backed by a downloaded page can be cited; requirements without one are kept, but capped so they can never be reported as a fault.

AI requests and attached datasheet content are sent to the configured AI endpoint.

## `/contract` — what a part needs electrically

```text
/contract U1
/contract U1 /path/to/datasheet.pdf
```

Copilot works out what the part needs around it — decoupling, pull-ups, strapping pins, and similar requirements — from the datasheet, and stores the result as the part's **contract**. Later reviews, `/findings`, and answers use it.

Contracts belong to the **component**, not the project, so a contract written once is reused on every board that uses the same part.

When no datasheet can be found, Copilot says so and asks for the PDF. Without one it can still write a draft, but every line of that draft is capped so it cannot report a fault.

## `/pins` — name blank pins

Some symbols arrive with pin numbers but no meaningful pin names. Design checks then flag the part.

```text
/pins
/pins U4
```

`/pins` with no argument names the pins of **every** part whose symbol has blank pin names; `/pins U4` does only that part (if U4 is not one of them, the reply lists the ones that are). Copilot asks the datasheet what each pin is called and adds **only the names**, on a copy of the symbol in the project library. Pin numbers, wiring, and the footprint stay as they are.

## `/fix` — repair one part

Describe what is wrong with one part, optionally with its datasheet:

```text
/fix U4 the symbol's pins have no names, take them from the datasheet
/fix SW1 its symbol points at a footprint we do not have
/fix U1 connect pin 2 to SW and pin 3 to GND
/fix U2 wrong part — install the real one from the published library
/fix U4 name the pins ~/Downloads/pc817.pdf
```

Copilot answers with what it **would** change and changes nothing until you press **Apply**. An applied repair is recorded as a decision in project memory, so later runs do not undo it.

`/fix` repairs **one** part. To see every error and warning on the board, use `/findings` — it costs no tokens. When several checks disagree about the same part, `/fix` asks you to say which problem you mean, or to start from the **Netlist Check** tab.

### Short video — Repair a part with /fix

!!! note "Video production brief"
    1. **Prepare:** Open a sample project where one symbol has blank pin names, and have its public datasheet PDF available locally.
    2. **Opening shot (1–2 s):** Show `/findings` output naming the part with blank pins.
    3. **Action shot (6–10 s):** Type `/fix U4 name the pins` followed by the datasheet path, and let Copilot propose the change.
    4. **Result shot (3–4 s):** Hold on the proposal with **Apply** visible, press it, and show the named pins.
    5. **Deliver:** Export a **12–18 second** 1080p MP4; reveal no private paths or API keys.

## Project memory

Copilot keeps durable facts per project — requirements, constraints, decisions, corrections, and preferences. They survive closing the chat, starting a new session, and reopening the project.

| Command | Use it to |
|---|---|
| `/memory` | List what the project has established, with an id for each fact |
| `/remember <text>` | Pin a fact Copilot must not forget, for example `/remember no electrolytic capacitors` |
| `/forget <id>` | Drop one fact by its id from `/memory` |

A newer decision about the same subject replaces the older one, but the history is kept.

## See also

- [Copilot Commands](commands.md)
- [AI Component Generator](component-generator.md)
- [AI Copilot](index.md)
