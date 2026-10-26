---
description: Live Checks in WireFrame — the design's own electrical, power, high-speed, DC drop and part lifecycle checks run as you draw, and what an edit breaks is said at once.
---

# Live Checks

The checks WireFrame has — the parts' electrical contracts, the power tree, the high-speed rules, the DC drop of the rails you set up and the parts' lifecycle — do not wait for the end. They run each time an edit settles, and **what an edit breaks is said at once**: an error appears as a notification, and **View ▸ Live Checks** shows it under *What the last edit changed*.

| Source | Runs after | Says |
|---|---|---|
| **Electrical** | a sheet edit | What a part's contract forbids: an output tied to a rail, a missing pull-up, flyback diode or decoupling capacitor |
| **Power tree** | a sheet edit | A pin whose rail is over (or under) what the part is rated for — *U1 pin 1 on +12V: 12 V is over its 3.6 V maximum* — with where the rail's voltage comes from |
| **High-speed** | a board edit | The high-speed rules on the nets whose copper moved (only on a board with high-speed nets) |
| **DC drop** | a board edit | The rails set up in the [Power Analyzer](power/power-analyzer.md) are solved again when their copper moves: a load cut off from its source, one whose ground return is open, one short of its minimum voltage |
| **Part lifecycle** | a sheet edit | Parts named by a part number that the part catalogue lists as obsolete (an error) or not recommended for new designs (a warning) — from the catalogue's cache, without a request — with `/alternative` to find a replacement |

Each finding says why and the step that fixes it; **Show** points at the part on every view (or the net on the board). What an edit clears is said too.

The checks run in the background and wait until you stop editing for a moment — longer on a design whose last read was slow. **Check now** reads again at once; each source can be turned off, and **Check while I edit** pauses them all. A source that says nothing tells you why (no rail set up, no high-speed nets, no part contracts installed).

What the checks found when the project opened is the starting point, not news: only what changes after that is announced.

Pins left unconnected and other structural problems are the [ERC](schematic/erc.md)'s; Live Checks leave them to it.
