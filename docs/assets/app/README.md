# Pictures drawn by the app's lab tools

These were rendered by WireFrame's own panels, headlessly, with `wf-panel-shot`
(a development build's `tests/cpp/wf-panel-shot`), on COPIES of the boards in
`boards.yaml`. Nothing here is drawn by hand. To make them again:

| File | Board | Command (run from a scratch folder with an `assets` symlink to the app's `assets/`) |
|---|---|---|
| `high-speed/*.png` | h730duino | `doc_builder/storyboards/guide/high-speed.yaml` (captured by doc_builder, copied from `doc_builder/assets/guide/high-speed/shots/`) |
| `power/setup.png`, `power/map-*.png`, `power/findings.png` | h730duino | `wf-panel-shot OUT.png --project h730duino.prjxml --pcb h730duino.pcbxml --size 1920x1080 --pdn setup --pdn-do use-proposed --pdn-do rail:+3V3 --pdn-do "amps:U1=0.45,U2=0.12,U10=0.08,J4=0.1,P2=0.25,P5=0.25" --pdn-do run --pdn-do page:map [--pdn-do layer:In2.Cu \| page:loads \| page:setup] --seconds 110` — the load currents are illustrative values typed for the picture |
| `views/probe-in-3d.png`, `views/probe-3d-properties.png` | h730duino | `wf-panel-shot OUT.png --project … --pcb … --size 1920x1080 --view3d-panel --probe U1 --seconds 60`, cropped (right half; the Properties panel) |
| `assembly/system-view.png` | hexapod cape on a BeagleBone AI | `wf-assembly-lab --new hexapod.asmxml --board Automative_Hexapod.prjxml --bought beaglebone-92 --bought hc-sr04 --bought gy-521 --bought servo --connect direct B2:P8_P9 B1:U2 --connect cable B1:J6 B3:J1 --length 150 --connect direct B1:J4 B4:J1 --connect cable B1:J7 B5:J1 --length 300 --place B2 5 --place B1 11 --place B4 11`, then `wf-panel-shot OUT.png --project Automative_Hexapod.prjxml --asmxml hexapod.asmxml --review-tab system --size 1920x1200 --seconds 20`, cropped to the top 890 px |

Credits: h730duino by Martin Ribelotta (MIT); the autonomous hexapod by its authors (GPL-2.0) — see `boards.yaml`.
