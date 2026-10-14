# Content plan — guide, blog and videos (2026-10)

Every picture and clip on the guide, the blog and the website is drawn by the
WireFrame app itself (`doc_builder`), on real open-hardware boards listed in
[`boards.yaml`](boards.yaml). Nothing is mocked up, nothing is a hand-taken
screenshot, and the 7805 test project is no longer used for media.

## 1. Boards and what each is for

| Board | Layers / parts | Licence | Used for |
|---|---|---|---|
| Jetson AGX Thor baseboard (Antmicro, KiCad demo) | 10 L · 1125 | Apache-2.0 | **showcase** — hero video, sponsor deck, ads |
| Jetson Nano baseboard (Antmicro) | 8 L · 391 | Apache-2.0 | **showcase**, blog |
| CM5 Minima (Raspberry Pi CM5 carrier, KiCad demo) | 6 L · 112 | CERN-OHL-S-2.0 | **showcase**, blog |
| One-Air-Max (ESP32-C6 sensor, KiCad demo) | 4 L · 210 | CC-BY-SA-4.0 | **showcase**, blog |
| H730duino (STM32H730) | 4 L · 111 | MIT | showcase, **guide**, blog |
| Autonomous hexapod main board | 2 L · 160, 8 sheets | GPL-2.0 | showcase, **guide**, blog |
| Automotive buck converter | 2 L · 36 | MIT | **guide** (PCB, routing, zones, DFM, fab) |
| KLP4e MCU datalogger | 2 L · 2 sheets | MIT | **guide** (schematic, ERC, libraries) |
| NE555 blinker, LED board (made by the Copilot) | — | made in WireFrame | **guide** (AI tutorial, simulation) |

Rule of thumb: **big boards sell, small boards teach.** A guide picture has to
be readable at 100 % and show one feature; a showcase clip has to look like a
real product being engineered.

## 2. The user guide (this repo, MkDocs)

Feature by feature, each page:

1. *What it is for* — one paragraph, with the picture.
2. *Do it* — numbered steps, the real menu labels.
3. *In depth* — every option, what each check means, what the numbers are.
4. *Pitfalls* — the mistakes the app catches and the ones it does not.

Which board illustrates which section:

| Section | Board |
|---|---|
| Getting started, UI, projects | buck converter (schematic + PCB fit one screen) |
| Schematic, ERC, properties, templates | KLP4e datalogger, hexapod (multi-sheet) |
| Libraries, symbol/footprint editors | KLP4e, H730duino parts |
| PCB: layers, zones, routing, rules, DFM, fab | buck converter (2 L), H730duino (4 L stackup, planes, meanders) |
| 3D, enclosure | H730duino, One-Air-Max |
| Simulation | NE555 blinker |
| AI Copilot, tutorials | NE555 / LED boards made by the Copilot, then H730duino for /layout and review |

Captures run with `WF_DOCS_RUNS_DIR=/tmp/wf-docs` and the guide's slots say
`project: board:<id>`.

## 3. Blog (wireframe-auth/content/blog) — the range of circuits

One post per board, written around what is hard about *that* circuit, with
numbers WireFrame measured (`boards <docs> --fetch` records them):

- 10-layer Jetson AGX Thor: camera pairs, PCIe, a 1125-part board opened in seconds.
- 8-layer Jetson Nano baseboard: SO-DIMM module, M.2, stackup and impedance classes.
- 6-layer Raspberry Pi CM5 carrier.
- 4-layer ESP32-C6 air sensor: antenna keepout, solar charging, power tree.
- H730duino and the hexapod (posts exist; refresh their media).
- Small boards: an automotive buck converter and a datalogger, start to finish.

## 4. Videos

Recorded in real time (AI turns take minutes on agy), then cut by
`doc_builder/video_edit.py`: fast-forward with a visible `8×` badge, slow
motion, zoom into the panel that matters, chapter labels. The master and the
edit recipe are kept beside every clip (`<id>.master.mp4`, `<id>.edit.json`).

| Clip | Board | Length |
|---|---|---|
| Hero: open a 10-layer board, walk the layers, 3D, DFM | Jetson AGX Thor | 45–60 s |
| From one sentence to a reviewed schematic (Copilot) | new design | 60–90 s |
| Copilot lays out and routes a board (`/layout`) | H730duino copy | 60 s |
| KiCad project in, Gerbers out | One-Air-Max | 40 s |
| Short feature clips (guide) | small boards | 10–20 s each |

## 5. Credits

Each page or post that shows a board links its source and licence
(`python3 -m doc_builder boards ../wireframe-docs --credits`).
