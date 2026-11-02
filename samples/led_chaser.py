#!/usr/bin/env python3
"""LED Chaser — the tutorial board, written as a KiCad project WireFrame imports.

    python3 samples/led_chaser.py [OUT_DIR]

A fictional board made for this guide: an NE555 clock steps a 74HC4017 decade
counter, and its ten outputs light ten LEDs set in a ring, one at a time. 5 V
in on a 2-pin header, 0805 passives and LEDs, SOIC ICs, two layers, 50 x 60 mm.

What is written here is the DESIGN INPUT — schematic, part placement, the
LED cathode ring and the board outline — as a KiCad 8 project. WireFrame's own
importer turns it into a WireFrame project and WireFrame's router lays the
rest of the copper (see samples/README.md); nothing WireFrame writes is
written by this script.

Symbols and footprints are copied from the KiCad libraries (CC-BY-SA 4.0 with
the KiCad libraries' design exception). They are read from
$KICAD_LIBS (default: WireFrame's library cache), which must hold
kicad-symbols/ and kicad-footprints/ checkouts.
"""

from __future__ import annotations

import json
import math
import os
import re
import sys
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAME = "led_chaser"
LIBS = Path(os.environ.get("KICAD_LIBS", "~/.wireframe/library_cache/repos")).expanduser()
SYM_DIR = LIBS / "kicad-symbols"
FP_DIR = LIBS / "kicad-footprints"
DATE = "2026-11-02"

_NS = uuid.UUID("6f1c2d8e-3a57-4c1b-9d0e-5b7a2c4e8f10")


def uid(*key: object) -> str:
    """Stable UUIDs: the same input writes the same files."""
    return str(uuid.uuid5(_NS, "/".join(map(str, key))))


# ── s-expressions ───────────────────────────────────────────────────────────

class Q(str):
    """A quoted atom (kept escaped exactly as read)."""


_TOKEN = re.compile(r'\(|\)|"(?:[^"\\]|\\.)*"|[^\s()]+')


def parse(text: str) -> list:
    stack: list[list] = [[]]
    for m in _TOKEN.finditer(text):
        t = m.group(0)
        if t == "(":
            stack.append([])
        elif t == ")":
            done = stack.pop()
            stack[-1].append(done)
        elif t[0] == '"':
            stack[-1].append(Q(t[1:-1]))
        else:
            stack[-1].append(t)
    return stack[0][0]


def num(v: float) -> str:
    s = f"{v:.4f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def atom(a: object) -> str:
    if isinstance(a, Q):
        return f'"{a}"'
    if isinstance(a, float):
        return num(a)
    return str(a)


def dump(x: list, ind: int = 0) -> str:
    if all(not isinstance(e, list) for e in x):
        return "(" + " ".join(atom(e) for e in x) + ")"
    head = []
    rest = list(x)
    while rest and not isinstance(rest[0], list):
        head.append(atom(rest.pop(0)))
    tab = "\t" * (ind + 1)
    out = "(" + " ".join(head)
    for e in rest:
        out += "\n" + tab + (dump(e, ind + 1) if isinstance(e, list) else atom(e))
    return out + "\n" + "\t" * ind + ")"


def child(node: list, key: str) -> list | None:
    for e in node:
        if isinstance(e, list) and e and e[0] == key:
            return e
    return None


def font(size: float = 1.27, *extra: list) -> list:
    return ["effects", ["font", ["size", size, size], *extra]]


# ── the circuit ─────────────────────────────────────────────────────────────
#
# One table drives both sides: every symbol, its footprint, and which net each
# pin is on. The schematic draws these connections; check_schematic() proves
# the wires make exactly these nets before anything is written.

PARTS = {
    # ref: (lib_id, value, footprint, {pin: net})
    "J1": ("Connector:Conn_01x02_Pin", "5V IN", "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical",
           {"1": "+5V", "2": "GND"}),
    "C5": ("Device:C", "10u", "Capacitor_SMD:C_0805_2012Metric", {"1": "+5V", "2": "GND"}),
    "U1": ("Timer:NE555D", "NE555D", "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
           {"1": "GND", "2": "THR", "3": "CLK", "4": "+5V", "5": "CV", "6": "THR", "7": "DIS", "8": "+5V"}),
    "R1": ("Device:R", "1k", "Resistor_SMD:R_0805_2012Metric", {"1": "+5V", "2": "DIS"}),
    "R2": ("Device:R", "68k", "Resistor_SMD:R_0805_2012Metric", {"1": "DIS", "2": "THR"}),
    "C1": ("Device:C", "1u", "Capacitor_SMD:C_0805_2012Metric", {"1": "THR", "2": "GND"}),
    "C2": ("Device:C", "10n", "Capacitor_SMD:C_0805_2012Metric", {"1": "CV", "2": "GND"}),
    "C3": ("Device:C", "100n", "Capacitor_SMD:C_0805_2012Metric", {"1": "+5V", "2": "GND"}),
    "U2": ("4xxx:4017", "74HC4017", "Package_SO:SOIC-16_3.9x9.9mm_P1.27mm",
           {"1": "Q5", "2": "Q1", "3": "Q0", "4": "Q2", "5": "Q6", "6": "Q7", "7": "Q3", "8": "GND",
            "9": "Q8", "10": "Q4", "11": "Q9", "12": None, "13": "GND", "14": "CLK", "15": "GND", "16": "+5V"}),
    "C4": ("Device:C", "100n", "Capacitor_SMD:C_0805_2012Metric", {"1": "+5V", "2": "GND"}),
    "R3": ("Device:R", "330", "Resistor_SMD:R_0805_2012Metric", {"1": "LED_K", "2": "GND"}),
}
for _k in range(10):
    PARTS[f"D{_k + 1}"] = ("Device:LED", "RED", "LED_SMD:LED_0805_2012Metric", {"1": "LED_K", "2": f"Q{_k}"})
for _k in range(4):
    PARTS[f"H{_k + 1}"] = ("Mechanical:MountingHole", "MountingHole", "MountingHole:MountingHole_3.2mm_M3", {})

NETS = ["GND", "+5V", "CLK", "DIS", "THR", "CV", "LED_K"] + [f"Q{k}" for k in range(10)]


# ── symbols ─────────────────────────────────────────────────────────────────

_SYM_CACHE: dict[str, list] = {}


def lib_symbol(lib_id: str) -> list:
    if lib_id not in _SYM_CACHE:
        lib, name = lib_id.split(":")
        tree = parse((SYM_DIR / f"{lib}.kicad_symdir" / f"{name}.kicad_sym").read_text(encoding="utf-8"))
        sym = next(e for e in tree if isinstance(e, list) and e[0] == "symbol")
        sym = list(sym)
        sym[1] = Q(lib_id)
        _SYM_CACHE[lib_id] = sym
    return _SYM_CACHE[lib_id]


def symbol_pins(lib_id: str) -> dict[str, tuple[float, float]]:
    """pin number -> (x, y) in the library's frame (y up)."""
    out: dict[str, tuple[float, float]] = {}

    def walk(n: list) -> None:
        for e in n:
            if isinstance(e, list):
                if e and e[0] == "pin":
                    at = child(e, "at")
                    number = child(e, "number")
                    out[str(number[1])] = (float(at[1]), float(at[2]))
                else:
                    walk(e)
    walk(lib_symbol(lib_id))
    return out


def rot(dx: float, dy: float, deg: float) -> tuple[float, float]:
    """Screen offset (y down) rotated counter-clockwise as seen, KiCad's sense."""
    a = math.radians(deg)
    c, s = round(math.cos(a), 9), round(math.sin(a), 9)
    return dx * c + dy * s, -dx * s + dy * c


class Sheet:
    def __init__(self) -> None:
        self.symbols: list[list] = []
        self.wires: list[tuple[tuple[float, float], tuple[float, float]]] = []
        self.junctions: list[tuple[float, float]] = []
        self.noconnects: list[tuple[float, float]] = []
        self.labels: list[tuple[str, tuple[float, float]]] = []
        self.pin_at: dict[tuple[str, str], tuple[float, float]] = {}
        self.power_at: list[tuple[str, tuple[float, float]]] = []
        self._pwr = 0
        self._flg = 0

    def place(self, ref: str, x: float, y: float, r: float = 0) -> dict[str, tuple[float, float]]:
        lib_id, value, footprint, _ = PARTS[ref]
        pins = {}
        for n, (px, py) in symbol_pins(lib_id).items():
            dx, dy = rot(px, -py, r)
            pins[n] = (round(x + dx, 3), round(y + dy, 3))
            self.pin_at[(ref, n)] = pins[n]
        # Where KiCad shows the texts; WireFrame's importer places its own.
        two_pin = lib_id in ("Device:R", "Device:C", "Device:LED")
        upright = (r % 180 == 0) != (lib_id == "Device:LED")
        bottom = max(p[1] for p in pins.values()) if pins else y
        if two_pin and upright:      # beside the body
            ref_at, val_at, just = (x + 2.54, y - 1.27), (x + 2.54, y + 1.27), [["justify", "left"]]
        elif two_pin:                # above and below the body
            ref_at, val_at, just = (x, y - 2.54), (x, y + 2.54), []
        elif lib_id.startswith(("Timer:", "4xxx:")):   # under the right-hand corner, clear of the pins
            ref_at, val_at, just = (x + 5.08, bottom + 1.27), (x + 5.08, bottom + 3.81), [["justify", "left"]]
        else:
            ref_at, val_at, just = (x, y - 3.81), (x, y + 5.08), []
        props = [
            ["property", Q("Reference"), Q(ref), ["at", ref_at[0], ref_at[1], 0], font(1.27) + just],
            ["property", Q("Value"), Q(value), ["at", val_at[0], val_at[1], 0], font(1.27) + just],
            ["property", Q("Footprint"), Q(footprint), ["at", x, y, 0], font(1.27) + [["hide", "yes"]]],
            ["property", Q("Datasheet"), Q("~"), ["at", x, y, 0], font(1.27) + [["hide", "yes"]]],
        ]
        self._emit(lib_id, ref, x, y, r, props, list(pins), in_bom=True)
        return pins

    def power(self, kind: str, x: float, y: float, r: float = 0) -> None:
        lib_id = f"power:{kind}"
        if kind == "PWR_FLAG":
            self._flg += 1
            ref = f"#FLG0{self._flg}"
        else:
            self._pwr += 1
            ref = f"#PWR0{self._pwr:02d}"
        tx, ty = rot(0, 3.81 if kind == "GND" else -3.81, r)
        props = [
            ["property", Q("Reference"), Q(ref), ["at", x, y, 0], font(1.27) + [["hide", "yes"]]],
            ["property", Q("Value"), Q(kind), ["at", x + tx, y + ty, 0], font(1.27)],
            ["property", Q("Footprint"), Q(""), ["at", x, y, 0], font(1.27) + [["hide", "yes"]]],
            ["property", Q("Datasheet"), Q(""), ["at", x, y, 0], font(1.27) + [["hide", "yes"]]],
        ]
        lib_symbol(lib_id)
        self._emit(lib_id, ref, x, y, r, props, ["1"], in_bom=False)
        if kind != "PWR_FLAG":
            self.power_at.append((kind, (x, y)))
        else:
            self.power_at.append(("FLAG", (x, y)))

    def _emit(self, lib_id: str, ref: str, x: float, y: float, r: float, props: list, pins: list,
              in_bom: bool) -> None:
        self.symbols.append(
            ["symbol", ["lib_id", Q(lib_id)], ["at", x, y, r], ["unit", 1],
             ["exclude_from_sim", "no"], ["in_bom", "yes" if in_bom else "no"], ["on_board", "yes"],
             ["dnp", "no"], ["uuid", Q(uid("sym", ref))], *props,
             *[["pin", Q(n), ["uuid", Q(uid("pin", ref, n))]] for n in pins],
             ["instances", ["project", Q(NAME), ["path", Q("/" + uid("sheet")), ["reference", Q(ref)], ["unit", 1]]]]])

    def label(self, name: str, x: float, y: float) -> None:
        """A net label, its anchor on a wire: the net's name on both sides."""
        self.labels.append((name, (round(x, 3), round(y, 3))))

    def wire(self, *pts: tuple[float, float]) -> None:
        pts = tuple((round(x, 3), round(y, 3)) for x, y in pts)
        for a, b in zip(pts, pts[1:]):
            assert a[0] == b[0] or a[1] == b[1], f"diagonal wire {a} {b}"
            self.wires.append((a, b))


def draw_schematic() -> Sheet:
    s = Sheet()

    # Power input ─────────────────────────────────────────────────────────
    j1 = s.place("J1", 25.4, 81.28)
    assert j1["1"] == (30.48, 81.28) and j1["2"] == (30.48, 83.82), j1
    c5 = s.place("C5", 50.8, 86.36)
    s.wire(j1["1"], (40.64, 81.28), (50.8, 81.28), c5["1"])
    s.wire(j1["2"], (35.56, 83.82), (35.56, 93.98), (40.64, 93.98), (50.8, 93.98), c5["2"])
    s.power("+5V", 50.8, 81.28)
    s.power("GND", 50.8, 96.52)
    s.wire((50.8, 93.98), (50.8, 96.52))
    # KiCad's ERC wants the header named as what drives both rails
    s.power("PWR_FLAG", 40.64, 81.28)
    s.power("PWR_FLAG", 40.64, 93.98)

    # 555 astable ─────────────────────────────────────────────────────────
    u1 = s.place("U1", 99.06, 86.36)
    assert (u1["7"], u1["2"], u1["6"], u1["4"]) == ((88.9, 83.82), (88.9, 91.44), (88.9, 88.9), (88.9, 81.28)), u1
    assert (u1["8"], u1["5"], u1["1"], u1["3"]) == ((101.6, 76.2), (99.06, 76.2), (99.06, 96.52), (109.22, 86.36)), u1
    # R1: +5V → DIS, R2: DIS → THR, C1: THR → GND, one column on the left
    r1 = s.place("R1", 76.2, 74.93)
    r2 = s.place("R2", 76.2, 87.63)
    c1 = s.place("C1", 76.2, 99.06)
    s.power("+5V", 76.2, 68.58)
    s.wire((76.2, 68.58), r1["1"])
    s.wire(r1["2"], r2["1"], u1["7"])                 # DIS: R1, R2, DISCH
    s.label("DIS", 78.74, 83.82)
    s.wire(r2["2"], c1["1"])                          # THR: R2, C1 ...
    s.wire(r2["2"], (86.36, 91.44), u1["2"])          # ... TRIG ...
    s.label("THR", 78.74, 91.44)
    s.wire(u1["6"], (86.36, 88.9), (86.36, 91.44))    # ... and THRES
    s.power("GND", 76.2, 105.41)
    s.wire(c1["2"], (76.2, 105.41))
    s.wire(u1["4"], (83.82, 81.28), (83.82, 68.58), (76.2, 68.58))   # RESET high
    s.power("GND", 99.06, 99.06)
    s.wire(u1["1"], (99.06, 99.06))
    # VCC, decoupled by C3
    c3 = s.place("C3", 111.76, 74.93)
    s.wire(u1["8"], (101.6, 71.12), c3["1"])
    s.power("+5V", 101.6, 71.12)
    s.power("GND", 111.76, 78.74)
    # CONT to GND through C2, over the top of VCC
    c2 = s.place("C2", 121.92, 67.31)
    s.wire(u1["5"], (99.06, 63.5), c2["1"])
    s.label("CV", 106.68, 63.5)
    s.power("GND", 121.92, 71.12)
    # OUT → CLK of the counter
    s.wire(u1["3"], (127.0, 86.36), (127.0, 76.2))
    s.label("CLK", 113.03, 86.36)

    # 4017 and the LEDs ───────────────────────────────────────────────────
    u2 = s.place("U2", 152.4, 88.9)
    assert (u2["14"], u2["13"], u2["15"], u2["16"], u2["8"]) == \
        ((139.7, 76.2), (139.7, 78.74), (139.7, 83.82), (152.4, 68.58), (152.4, 111.76)), u2
    s.wire((127.0, 76.2), u2["14"])
    s.wire(u2["13"], (134.62, 78.74), (134.62, 83.82), (134.62, 86.36))   # CKEN and RESET low
    s.wire(u2["15"], (134.62, 83.82))
    s.power("GND", 134.62, 86.36)
    c4 = s.place("C4", 144.78, 64.77)
    s.wire(u2["16"], (152.4, 60.96), c4["1"])
    s.power("+5V", 152.4, 60.96)
    s.power("GND", 144.78, 68.58)
    s.power("GND", 152.4, 111.76)
    s.noconnects.append(u2["12"])
    # The staircase: Q0 (top row) to the leftmost LED, each next output one
    # column further right, so no two wires cross.
    led_y, bus_y, pitch = 50.8, 43.18, 7.62
    cols = [round(172.72 + pitch * k, 3) for k in range(10)]
    for k, x in enumerate(cols):
        d = s.place(f"D{k + 1}", x, led_y, 270)
        q = u2[{0: "3", 1: "2", 2: "4", 3: "7", 4: "10", 5: "1", 6: "5", 7: "6", 8: "9", 9: "11"}[k]]
        s.wire(q, (x, q[1]), d["2"])
        s.label(f"Q{k}", q[0] + 1.27, q[1])
        s.wire(d["1"], (x, bus_y))
    r3 = s.place("R3", 254.0, bus_y, 90)
    s.wire(*[(x, bus_y) for x in cols], r3["1"])
    s.label("LED_K", 242.57, bus_y)
    s.wire(r3["2"], (262.89, bus_y), (262.89, 48.26))
    s.power("GND", 262.89, 48.26)

    # Mounting holes ──────────────────────────────────────────────────────
    for k in range(4):
        s.place(f"H{k + 1}", 27.94 + 10.16 * k, 127.0)
    return s


def check_schematic(s: Sheet) -> None:
    """The wires must make exactly the nets of PARTS — nothing written otherwise."""
    pts: dict[tuple[float, float], int] = {}
    parent: list[int] = []

    def node(p: tuple[float, float]) -> int:
        p = (round(p[0], 3), round(p[1], 3))
        if p not in pts:
            pts[p] = len(parent)
            parent.append(len(parent))
        return pts[p]

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        parent[find(a)] = find(b)

    for a, b in s.wires:
        union(node(a), node(b))
    every = list(s.pin_at.values()) + [p for _, p in s.power_at] + [a for w in s.wires for a in w]
    for p in every:
        for a, b in s.wires:
            if min(a[0], b[0]) - 1e-6 <= p[0] <= max(a[0], b[0]) + 1e-6 and \
               min(a[1], b[1]) - 1e-6 <= p[1] <= max(a[1], b[1]) + 1e-6:
                union(node(p), node(a))
    named: dict[int, str] = {}
    for name, p in s.labels:
        if not any(p in w for w in s.wires):
            raise SystemExit(f"schematic: label {name} at {p} is not on a wire end")
    for kind, p in s.power_at + s.labels:
        if kind == "FLAG":
            continue
        r = find(node(p))
        if named.get(r, kind) != kind:
            raise SystemExit(f"schematic: {kind} and {named[r]} are shorted at {p}")
        named[r] = kind
    groups: dict[int, set] = {}
    for (ref, n), p in s.pin_at.items():
        groups.setdefault(find(node(p)), set()).add((ref, n))
    # +5V/GND symbols join every group they touch, by name
    by_name: dict[str, set] = {}
    for r, members in groups.items():
        key = named.get(r) or min(f"{a}.{b}" for a, b in members)
        by_name.setdefault(key, set()).update(members)
    want: dict[str, set] = {}
    for ref, (_, _, _, pins) in PARTS.items():
        for n, net in pins.items():
            if net:
                want.setdefault(net, set()).add((ref, n))
    for net, members in want.items():
        match = [k for k, v in by_name.items() if v == members]
        if match and match[0] != net and net in {n for n, _ in s.labels}:
            raise SystemExit(f"schematic: the label {net} names {match[0]}")
        if not match:
            close = [(k, sorted(v)) for k, v in by_name.items() if v & members]
            raise SystemExit(f"schematic: net {net} {sorted(members)} is drawn as {close}")
    for (ref, n), p in s.pin_at.items():
        net = PARTS[ref][3].get(n)
        if net is None and n in PARTS[ref][3] and p not in s.noconnects:
            raise SystemExit(f"schematic: {ref}.{n} must carry a no-connect flag")
    for f in [p for k, p in s.power_at if k == "FLAG"]:
        r = find(node(f))
        if r not in named:
            raise SystemExit(f"schematic: a PWR_FLAG at {f} is not on a supply")
    print(f"  schematic: {len(want)} nets drawn as intended, {len(s.wires)} wire segments")


def tidy(s: Sheet) -> None:
    """Every connection at a segment END (an importer need not join a pin to
    the middle of a wire), and a junction dot wherever three or more meet."""
    stops = {p for w in s.wires for p in w} | set(s.pin_at.values()) | {p for _, p in s.power_at} | \
        {p for _, p in s.labels}
    out = []
    for a, b in s.wires:
        if a == b:
            continue
        inner = [p for p in stops if p not in (a, b) and
                 min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]) and
                 (a[0] == b[0] == p[0] or a[1] == b[1] == p[1])]
        inner.sort(key=lambda p: abs(p[0] - a[0]) + abs(p[1] - a[1]))
        chain = [a, *inner, b]
        out += list(zip(chain, chain[1:]))
    s.wires = out
    ends: dict[tuple[float, float], int] = {}
    for w in out:
        for p in w:
            ends[p] = ends.get(p, 0) + 1
    for p in list(s.pin_at.values()) + [q for _, q in s.power_at]:
        if p in ends:
            ends[p] += 1
    s.junctions = sorted(p for p, n in ends.items() if n >= 3)


def write_schematic(s: Sheet, path: Path) -> None:
    libs = []
    seen = set()
    for sym in s.symbols:
        lib_id = str(sym[1][1])
        if lib_id not in seen:
            seen.add(lib_id)
            libs.append(lib_symbol(lib_id))
    root = ["kicad_sch", ["version", 20231120], ["generator", Q("eeschema")], ["generator_version", Q("8.0")],
            ["uuid", Q(uid("sheet"))], ["paper", Q("A4")],
            ["title_block", ["title", Q("LED Chaser")], ["date", Q(DATE)], ["rev", Q("A")],
             ["company", Q("WireFrame tutorial")], ["comment", 1, Q("NE555 clock, 74HC4017 counter, 10 LEDs")]],
            ["lib_symbols", *libs]]
    for p in s.junctions:
        root.append(["junction", ["at", p[0], p[1]], ["diameter", 0], ["color", 0, 0, 0, 0],
                     ["uuid", Q(uid("junction", *p))]])
    for name, p in s.labels:
        root.append(["label", Q(name), ["at", p[0], p[1], 0], ["fields_autoplaced", "yes"],
                     ["effects", ["font", ["size", 1.27, 1.27]], ["justify", "left", "bottom"]],
                     ["uuid", Q(uid("label", name))]])
    for p in s.noconnects:
        root.append(["no_connect", ["at", p[0], p[1]], ["uuid", Q(uid("nc", *p))]])
    for i, (a, b) in enumerate(s.wires):
        if a == b:
            continue
        root.append(["wire", ["pts", ["xy", a[0], a[1]], ["xy", b[0], b[1]]],
                     ["stroke", ["width", 0], ["type", "default"]], ["uuid", Q(uid("wire", i))]])
    root += s.symbols
    root.append(["sheet_instances", ["path", Q("/"), ["page", Q("1")]]])
    path.write_text(dump(root) + "\n", encoding="utf-8")


# ── the board ───────────────────────────────────────────────────────────────

BX, BY, BW, BH, BR = 100.0, 100.0, 50.0, 60.0, 3.0      # outline, mm
CX, CY = 125.0, 125.0                                   # centre of the LED ring
RING = 18.0                                             # LED centres
HOLES = [(104.0, 104.0), (146.0, 104.0), (104.0, 156.0), (146.0, 156.0)]


def led_angle(k: int) -> float:
    """D(k+1) sits at this angle (degrees, screen, y down): a gap at the top and at the bottom."""
    return -72.0 + 36.0 * k


PLACEMENT = {
    # ref: (x, y, rotation)
    "U2": (125.0, 120.5, 0.0),
    "C4": (130.6, 116.0, 0.0),
    "U1": (125.0, 132.0, 0.0),
    "C3": (120.2, 128.4, 0.0),
    "R1": (131.4, 130.2, 90.0),
    "R2": (131.4, 133.9, 90.0),
    "C1": (118.6, 131.7, 90.0),
    "C2": (127.6, 137.6, 0.0),
    "J1": (123.73, 153.5, 90.0),
    "C5": (117.5, 153.5, 90.0),
    "R3": (134.5, 147.5, 0.0),
}
for _k in range(10):
    _a = math.radians(led_angle(_k))
    # pad 2 (anode, local +x) points at the centre
    PLACEMENT[f"D{_k + 1}"] = (CX + RING * math.cos(_a), CY + RING * math.sin(_a),
                               (-(led_angle(_k) + 180.0)) % 360.0)
for _k, (_x, _y) in enumerate(HOLES):
    PLACEMENT[f"H{_k + 1}"] = (_x, _y, 0.0)


def fp_rotate(x: float, y: float, deg: float) -> tuple[float, float]:
    """A footprint-local point rotated as KiCad rotates footprints (CCW as seen, y down)."""
    return rot(x, y, deg)


_FP_CACHE: dict[str, list] = {}


def footprint_tree(fp: str) -> list:
    if fp not in _FP_CACHE:
        lib, name = fp.split(":")
        _FP_CACHE[fp] = parse((FP_DIR / f"{lib}.pretty" / f"{name}.kicad_mod").read_text(encoding="utf-8"))
    return _FP_CACHE[fp]


def pad_positions(ref: str) -> dict[str, tuple[float, float]]:
    fp = PARTS[ref][2]
    x, y, r = PLACEMENT[ref]
    out = {}
    for e in footprint_tree(fp):
        if isinstance(e, list) and e and e[0] == "pad" and str(e[1]):
            at = child(e, "at")
            dx, dy = fp_rotate(float(at[1]), float(at[2]), r)
            out[str(e[1])] = (x + dx, y + dy)
    return out


def board_footprint(ref: str, net_ids: dict[str, int], ref_hidden: bool = False) -> list:
    lib_id, value, fp, pins = PARTS[ref]
    x, y, r = PLACEMENT[ref]
    src = footprint_tree(fp)
    out = ["footprint", Q(fp), ["layer", Q("F.Cu")], ["uuid", Q(uid("fp", ref))], ["at", x, y, r] if r else ["at", x, y]]
    for e in src[2:]:
        if not isinstance(e, list):
            continue
        key = e[0]
        if key in ("version", "generator", "generator_version", "layer"):
            continue
        e = [list(c) if isinstance(c, list) else c for c in e]
        if key == "property":
            name = str(e[1])
            if name == "Reference":
                e[2] = Q(ref)
                if ref_hidden and not child(e, "hide"):
                    e.insert(4, ["hide", "yes"])
            elif name == "Value":
                e[2] = Q(value)
                if ref[0] in "DH" and not child(e, "hide"):   # "RED" ten times round the ring says nothing
                    e.insert(4, ["hide", "yes"])
            e.append(["uuid", Q(uid("fp-prop", ref, name))])
            at = child(e, "at")
            if at is not None:
                at[1:] = [at[1], at[2], (float(at[3] if len(at) > 3 else 0) + r) % 360.0]
                e.insert(e.index(at) + 1, ["unlocked", "yes"])
        elif key == "pad":
            at = child(e, "at")
            ang = float(at[3]) if len(at) > 3 else 0.0
            at[1:] = [at[1], at[2], (ang + r) % 360.0] if (ang + r) % 360.0 else [at[1], at[2]]
            net = pins.get(str(e[1]))
            if net:
                e.append(["net", net_ids[net], Q(net)])
            e.append(["uuid", Q(uid("pad", ref, str(e[1]), len(out)))])
        elif key == "fp_text":
            at = child(e, "at")
            if at is not None:
                at[1:] = [at[1], at[2], (float(at[3] if len(at) > 3 else 0) + r) % 360.0]
                e.insert(e.index(at) + 1, ["unlocked", "yes"])
        out.append(e)
    return out


def edge_cuts() -> list[list]:
    x0, y0, x1, y1, r = BX, BY, BX + BW, BY + BH, BR
    st = ["stroke", ["width", 0.1], ["type", "default"]]
    lyr = ["layer", Q("Edge.Cuts")]
    items = [
        ["gr_line", ["start", x0 + r, y0], ["end", x1 - r, y0], st, lyr],
        ["gr_line", ["start", x1, y0 + r], ["end", x1, y1 - r], st, lyr],
        ["gr_line", ["start", x1 - r, y1], ["end", x0 + r, y1], st, lyr],
        ["gr_line", ["start", x0, y1 - r], ["end", x0, y0 + r], st, lyr],
    ]
    k = r * (1 - math.sqrt(0.5))
    items += [
        ["gr_arc", ["start", x0, y0 + r], ["mid", x0 + k, y0 + k], ["end", x0 + r, y0], st, lyr],
        ["gr_arc", ["start", x1 - r, y0], ["mid", x1 - k, y0 + k], ["end", x1, y0 + r], st, lyr],
        ["gr_arc", ["start", x1, y1 - r], ["mid", x1 - k, y1 - k], ["end", x1 - r, y1], st, lyr],
        ["gr_arc", ["start", x0 + r, y1], ["mid", x0 + k, y1 - k], ["end", x0, y1 - r], st, lyr],
    ]
    for i, it in enumerate(items):
        it.append(["uuid", Q(uid("edge", i))])
    return items


def cathode_ring(net_ids: dict[str, int]) -> list[list]:
    """LED_K: chords from cathode to cathode, D6 round to D5 (open at the bottom
    so +5V and GND come in from the header), then on to R3."""
    order = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]               # D6 … D10, D1 … D5
    pts = [pad_positions(f"D{k + 1}")["1"] for k in order]
    r3 = pad_positions("R3")["1"]
    pts.append((r3[0], pts[-1][1]))
    pts.append(r3)
    segs = []
    for i, (a, b) in enumerate(zip(pts, pts[1:])):
        segs.append(["segment", ["start", round(a[0], 4), round(a[1], 4)], ["end", round(b[0], 4), round(b[1], 4)],
                     ["width", 0.3], ["layer", Q("F.Cu")], ["net", net_ids["LED_K"]],
                     ["uuid", Q(uid("ring", i))]])
    return segs


def zone(net_ids: dict[str, int], layer: str) -> list:
    x0, y0, x1, y1, c = BX + 0.5, BY + 0.5, BX + BW - 0.5, BY + BH - 0.5, 2.0
    pts = [(x0 + c, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1 - c), (x1 - c, y1), (x0 + c, y1), (x0, y1 - c), (x0, y0 + c)]
    return ["zone", ["net", net_ids["GND"]], ["net_name", Q("GND")], ["layer", Q(layer)],
            ["uuid", Q(uid("zone", layer))], ["hatch", "edge", 0.5],
            ["connect_pads", ["clearance", 0.3]], ["min_thickness", 0.25], ["filled_areas_thickness", "no"],
            ["fill", ["thermal_gap", 0.5], ["thermal_bridge_width", 0.5]],
            ["polygon", ["pts", *[["xy", x, y] for x, y in pts]]]]


def write_board(path: Path) -> None:
    net_ids = {n: i + 1 for i, n in enumerate(NETS)}
    layers = [[0, Q("F.Cu"), "signal"], [31, Q("B.Cu"), "signal"],
              [32, Q("B.Adhes"), "user", Q("B.Adhesive")], [33, Q("F.Adhes"), "user", Q("F.Adhesive")],
              [34, Q("B.Paste"), "user"], [35, Q("F.Paste"), "user"],
              [36, Q("B.SilkS"), "user", Q("B.Silkscreen")], [37, Q("F.SilkS"), "user", Q("F.Silkscreen")],
              [38, Q("B.Mask"), "user"], [39, Q("F.Mask"), "user"],
              [40, Q("Dwgs.User"), "user", Q("User.Drawings")], [41, Q("Cmts.User"), "user", Q("User.Comments")],
              [44, Q("Edge.Cuts"), "user"], [45, Q("Margin"), "user"],
              [46, Q("B.CrtYd"), "user", Q("B.Courtyard")], [47, Q("F.CrtYd"), "user", Q("F.Courtyard")],
              [48, Q("B.Fab"), "user"], [49, Q("F.Fab"), "user"]]
    root = ["kicad_pcb", ["version", 20240108], ["generator", Q("pcbnew")], ["generator_version", Q("8.0")],
            ["general", ["thickness", 1.6], ["legacy_teardrops", "no"]], ["paper", Q("A4")],
            ["title_block", ["title", Q("LED Chaser")], ["date", Q(DATE)], ["rev", Q("A")],
             ["company", Q("WireFrame tutorial")]],
            ["layers", *layers],
            ["setup", ["pad_to_mask_clearance", 0], ["allow_soldermask_bridges_in_footprints", "no"]],
            ["net", 0, Q("")], *[["net", i, Q(n)] for n, i in net_ids.items()]]
    for ref in PARTS:
        root.append(board_footprint(ref, net_ids, ref_hidden=ref[0] in "HD"))
    for k in range(10):
        a = math.radians(led_angle(k))
        root.append(["gr_text", Q(f"D{k + 1}"), ["at", round(CX + 22.0 * math.cos(a), 3), round(CY + 22.0 * math.sin(a), 3), 0],
                     ["layer", Q("F.SilkS")], ["uuid", Q(uid("text", "led", k))],
                     ["effects", ["font", ["size", 1.0, 1.0], ["thickness", 0.15]]]])
    root += edge_cuts()
    root += cathode_ring(net_ids)
    root.append(["gr_text", Q("LED CHASER"), ["at", 125.0, 157.6, 0], ["layer", Q("F.SilkS")],
                 ["uuid", Q(uid("text", "title"))],
                 ["effects", ["font", ["size", 1.6, 1.6], ["thickness", 0.3], ["bold", "yes"]]]])
    root.append(["gr_text", Q("rev A"), ["at", 139.0, 157.6, 0], ["layer", Q("F.SilkS")],
                 ["uuid", Q(uid("text", "rev"))],
                 ["effects", ["font", ["size", 1.0, 1.0], ["thickness", 0.15]]]])
    root.append(zone(net_ids, "F.Cu"))
    root.append(zone(net_ids, "B.Cu"))
    path.write_text(dump(root) + "\n", encoding="utf-8")


def write_project(path: Path) -> None:
    def cls(name: str, track: float, clearance: float) -> dict:
        return {"name": name, "clearance": clearance, "track_width": track, "via_diameter": 0.7,
                "via_drill": 0.3, "microvia_diameter": 0.3, "microvia_drill": 0.1,
                "diff_pair_gap": 0.25, "diff_pair_via_gap": 0.25, "diff_pair_width": 0.2,
                "bus_width": 12, "wire_width": 6, "line_style": 0,
                "pcb_color": "rgba(0, 0, 0, 0.000)", "schematic_color": "rgba(0, 0, 0, 0.000)"}
    pro = {
        "board": {"design_settings": {"rules": {
            "min_clearance": 0.15, "min_copper_edge_clearance": 0.3, "min_hole_clearance": 0.25,
            "min_hole_to_hole": 0.25, "min_track_width": 0.15, "min_via_annular_width": 0.15,
            "min_via_diameter": 0.6, "min_through_hole_diameter": 0.3}}},
        "meta": {"filename": f"{NAME}.kicad_pro", "version": 1},
        "net_settings": {
            "classes": [cls("Default", 0.254, 0.1524), cls("Power", 0.508, 0.381)],
            "meta": {"version": 3},
            "netclass_patterns": [{"netclass": "Power", "pattern": "+5V"},
                                  {"netclass": "Power", "pattern": "GND"}]},
        "sheets": [[uid("sheet"), "Root"]],
        "text_variables": {},
    }
    path.write_text(json.dumps(pro, indent=2) + "\n", encoding="utf-8")


def write_outline_dxf(path: Path) -> None:
    """The board's outline alone, for the tutorial's File > Import > CAD Outline:
    50 x 60 mm, R3 corners, centred on the origin, millimetres. No holes — H1-H4
    are parts of the design and bring their own."""
    w, h, r = BW / 2, BH / 2, BR
    q = math.tan(math.radians(90) / 4)  # the bulge of a quarter circle
    pts = [(-w + r, -h, 0), (w - r, -h, q), (w, -h + r, 0), (w, h - r, q),
           (w - r, h, 0), (-w + r, h, q), (-w, h - r, 0), (-w, -h + r, q)]
    lines = ["0", "SECTION", "2", "HEADER", "9", "$INSUNITS", "70", "4", "0", "ENDSEC",
             "0", "SECTION", "2", "ENTITIES",
             "0", "LWPOLYLINE", "8", "Edge.Cuts", "90", str(len(pts)), "70", "1"]
    for x, y, b in pts:
        lines += ["10", f"{x:.4f}", "20", f"{y:.4f}"] + (["42", f"{b:.6f}"] if b else [])
    lines += ["0", "ENDSEC", "0", "EOF"]
    path.write_text("\n".join(lines) + "\n", encoding="ascii")


def write_footprint_libs(out: Path) -> None:
    """The footprints the board uses, beside the project with an fp-lib-table,
    so the schematic alone finds them (Update Schematic to PCB on a machine with
    no KiCad library) — as a KiCad project kept with its own parts would."""
    libs: dict[str, set[str]] = {}
    for _, _, fp, _ in PARTS.values():
        lib, name = fp.split(":")
        libs.setdefault(lib, set()).add(name)
    rows = []
    for lib in sorted(libs):
        d = out / "footprints" / f"{lib}.pretty"
        d.mkdir(parents=True, exist_ok=True)
        for name in sorted(libs[lib]):
            (d / f"{name}.kicad_mod").write_bytes((FP_DIR / f"{lib}.pretty" / f"{name}.kicad_mod").read_bytes())
        rows.append(f'  (lib (name "{lib}")(type "KiCad")(uri "${{KIPRJMOD}}/footprints/{lib}.pretty")(options "")(descr ""))')
    (out / "fp-lib-table").write_text("(fp_lib_table\n  (version 7)\n" + "\n".join(rows) + "\n)\n", encoding="utf-8")


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "led-chaser" / "kicad"
    if not SYM_DIR.is_dir() or not FP_DIR.is_dir():
        raise SystemExit(f"needs kicad-symbols/ and kicad-footprints/ under {LIBS} (set KICAD_LIBS)")
    out.mkdir(parents=True, exist_ok=True)
    sheet = draw_schematic()
    tidy(sheet)
    check_schematic(sheet)
    write_schematic(sheet, out / f"{NAME}.kicad_sch")
    write_board(out / f"{NAME}.kicad_pcb")
    write_project(out / f"{NAME}.kicad_pro")
    write_footprint_libs(out)
    write_outline_dxf(out.parent / f"{NAME}_outline.dxf")
    print(f"  wrote {out}/{NAME}.kicad_pro, .kicad_sch, .kicad_pcb ({len(PARTS)} parts)"
          f" and {out.parent}/{NAME}_outline.dxf")


if __name__ == "__main__":
    main()
