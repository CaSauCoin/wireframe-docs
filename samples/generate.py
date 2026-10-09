#!/usr/bin/env python3
"""Sinh lại các file mẫu dùng khi chụp ảnh/quay video tài liệu.

    python3 samples/generate.py

Mọi thứ ở đây là HƯ CẤU, làm riêng cho tài liệu — không có bản quyền của ai
khác, không có dữ liệu khách hàng. Kích thước được chọn để dễ kiểm trên ảnh:

  outlines/demo-board.dxf   board 80 x 60 mm, góc bo R3, 4 lỗ M3 (Ø3.2) cách
                            mỗi góc 4 mm, một hốc pin 20 x 12 mm. ASCII DXF,
                            $INSUNITS = 4 (mm) — đúng tập entity WireFrame đọc.
  outlines/demo-board.svg   cùng hình, đơn vị mm.
  datasheets/wf-demo8.pdf   datasheet 2 trang của "WF-DEMO8", một IC 8 chân
                            SOIC-8 hư cấu: bảng chân, điều kiện làm việc, kích
                            thước package, mạch ứng dụng.
  datasheets/wf-demo8-pinout.png   bảng chân dạng ảnh (cho cảnh OCR), cắt
                            từ trang 1 của PDF — cần pdftoppm.

Chỉ dùng thư viện chuẩn của Python (+ pdftoppm cho ảnh bảng chân).
"""

from __future__ import annotations

import math
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ── board ───────────────────────────────────────────────────────────────────
W, H, R = 80.0, 60.0, 3.0
HOLE_D, HOLE_IN = 3.2, 4.0
POCKET = (50.0, 38.0, 70.0, 50.0)   # x0, y0, x1, y1 (mm, gốc ở góc dưới-trái, +Y lên)


def _dxf_header() -> list[str]:
    return ["0", "SECTION", "2", "HEADER", "9", "$INSUNITS", "70", "4", "0", "ENDSEC",
            "0", "SECTION", "2", "ENTITIES"]


def _lwpolyline(points: list[tuple[float, float, float]], layer: str) -> list[str]:
    """points: (x, y, bulge) — bulge của đoạn TỪ điểm đó tới điểm kế."""
    out = ["0", "LWPOLYLINE", "8", layer, "90", str(len(points)), "70", "1"]
    for x, y, b in points:
        out += ["10", f"{x:.4f}", "20", f"{y:.4f}"]
        if b:
            out += ["42", f"{b:.6f}"]
    return out


def write_dxf(path: Path) -> None:
    q = math.tan(math.radians(90) / 4)  # bulge của cung 90°
    outline = [  # ngược chiều kim đồng hồ, mỗi góc là một cung 90°
        (R, 0, 0), (W - R, 0, q), (W, R, 0), (W, H - R, q),
        (W - R, H, 0), (R, H, q), (0, H - R, 0), (0, R, q),
    ]
    x0, y0, x1, y1 = POCKET
    pocket = [(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0)]
    lines = _dxf_header() + _lwpolyline(outline, "Edge.Cuts") + _lwpolyline(pocket, "Edge.Cuts")
    for cx in (HOLE_IN, W - HOLE_IN):
        for cy in (HOLE_IN, H - HOLE_IN):
            lines += ["0", "CIRCLE", "8", "Edge.Cuts", "10", f"{cx:.4f}", "20", f"{cy:.4f}",
                      "40", f"{HOLE_D / 2:.4f}"]
    lines += ["0", "ENDSEC", "0", "EOF"]
    path.write_text("\n".join(lines) + "\n", encoding="ascii")


def write_svg_outline(path: Path) -> None:
    # SVG là +Y xuống: lật y để cùng một board như DXF.
    def fy(y: float) -> float:
        return H - y
    x0, y0, x1, y1 = POCKET
    holes = "".join(
        f'<circle cx="{cx}" cy="{fy(cy)}" r="{HOLE_D / 2}" fill="none" stroke="black" stroke-width="0.1"/>'
        for cx in (HOLE_IN, W - HOLE_IN) for cy in (HOLE_IN, H - HOLE_IN))
    path.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">\n'
        f'  <!-- WireFrame documentation sample: fictional 80 x 60 mm board -->\n'
        f'  <rect x="0" y="0" width="{W}" height="{H}" rx="{R}" ry="{R}" fill="none" stroke="black" stroke-width="0.1"/>\n'
        f'  <rect x="{x0}" y="{fy(y1)}" width="{x1 - x0}" height="{y1 - y0}" fill="none" stroke="black" stroke-width="0.1"/>\n'
        f'  {holes}\n</svg>\n', encoding="utf-8")


# ── datasheet ───────────────────────────────────────────────────────────────
PINS = [
    (1, "VIN", "Power", "Supply input, 2.7 V to 5.5 V"),
    (2, "GND", "Ground", "Ground return"),
    (3, "EN", "Input", "Enable, active high; 100 kOhm internal pull-down"),
    (4, "PG", "Output", "Power good, open drain; needs a 10 kOhm pull-up"),
    (5, "FB", "Input", "Feedback, 0.6 V reference"),
    (6, "SW", "Power", "Switch node to the inductor"),
    (7, "BST", "Power", "Bootstrap; 100 nF from BST to SW"),
    (8, "PGND", "Ground", "Power ground; connect to GND under the part"),
]


def _pdf_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _page_stream(lines: list[tuple[float, float, int, str]]) -> bytes:
    """lines: (x, y, size, text) — font chuẩn PDF, không cần nhúng. Cỡ 10 là
    bảng: Courier để cột thẳng hàng như trong datasheet thật."""
    parts = []
    for x, y, size, text in lines:
        font = "/F2" if size >= 12 else ("/F3" if size == 10 and text[:1].isdigit() or text.startswith("PIN") else "/F1")
        parts.append(f"BT {font} {size} Tf {x:.1f} {y:.1f} Td ({_pdf_escape(text)}) Tj ET")
    return "\n".join(parts).encode("latin-1")


def write_pdf(path: Path) -> None:
    p1 = [(56, 790, 18, "WF-DEMO8  -  2 A synchronous buck converter"),
          (56, 770, 9, "FICTIONAL PART - documentation sample for WireFrame EDA. Not a real product."),
          (56, 735, 13, "1  Pin Configuration and Functions"),
          (56, 715, 9, "Package: SOIC-8 (top view).   Pin 1 is marked by a dot."),
          (56, 695, 10, "PIN    NAME    TYPE      DESCRIPTION")]
    y = 678
    for num, name, kind, desc in PINS:
        p1.append((56, y, 10, f"{num:<6} {name:<7} {kind:<9} {desc}"))
        y -= 16
    p1 += [(56, y - 20, 13, "2  Recommended Operating Conditions"),
           (56, y - 40, 10, "VIN supply voltage ............ 2.7 V to 5.5 V"),
           (56, y - 56, 10, "Output current ................ 0 A to 2 A"),
           (56, y - 72, 10, "Junction temperature .......... -40 C to 125 C")]
    p2 = [(56, 790, 13, "3  Application Information"),
          (56, 770, 10, "Place a 10 uF input capacitor from VIN to PGND within 2 mm of the device."),
          (56, 754, 10, "Place a 100 nF bypass capacitor from VIN to GND within 3 mm of the device."),
          (56, 738, 10, "Connect a 100 nF bootstrap capacitor between BST (pin 7) and SW (pin 6)."),
          (56, 722, 10, "PG (pin 4) is open drain: pull it up to the logic rail with 10 kOhm."),
          (56, 690, 13, "4  Mechanical Data - SOIC-8"),
          (56, 670, 10, "Body 4.90 x 3.90 mm, pitch 1.27 mm, lead span 6.00 mm, height 1.75 mm max."),
          (56, 654, 10, "Recommended land pattern: 8 pads 1.55 x 0.60 mm, row spacing 5.40 mm.")]
    streams = [_page_stream(p1), _page_stream(p2)]

    objs: list[bytes] = []
    objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{6 + 2 * i} 0 R" for i in range(len(streams)))
    objs.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(streams)} >>".encode())
    objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
    objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>")
    for i, s in enumerate(streams):
        content_id = 7 + 2 * i
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
                    f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> /Contents {content_id} 0 R >>".encode())
        objs.append(b"<< /Length " + str(len(s)).encode() + b" >>\nstream\n" + s + b"\nendstream")

    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = []
    for n, body in enumerate(objs, 1):
        offsets.append(len(out))
        out += f"{n} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
    out += b"".join(f"{o:010d} 00000 n \n".encode() for o in offsets)
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    path.write_bytes(bytes(out))


def write_pinout_png(pdf: Path, png: Path) -> bool:
    """Bảng chân dạng ẢNH (cho cảnh OCR), cắt từ chính trang 1 của PDF."""
    import shutil
    import subprocess
    tool = shutil.which("pdftoppm")
    if not tool:
        print("bỏ qua wf-demo8-pinout.png: cần pdftoppm (poppler-utils)")
        return False
    subprocess.run([tool, "-png", "-r", "150", "-f", "1", "-l", "1", "-x", "100", "-y", "270",
                    "-W", "1000", "-H", "330", "-singlefile", str(pdf), str(png.with_suffix(""))], check=True)
    return True


def main() -> None:
    (HERE / "outlines").mkdir(exist_ok=True)
    (HERE / "datasheets").mkdir(exist_ok=True)
    write_dxf(HERE / "outlines" / "demo-board.dxf")
    write_svg_outline(HERE / "outlines" / "demo-board.svg")
    write_pdf(HERE / "datasheets" / "wf-demo8.pdf")
    write_pinout_png(HERE / "datasheets" / "wf-demo8.pdf", HERE / "datasheets" / "wf-demo8-pinout.png")
    print("ok:", ", ".join(str(p.relative_to(HERE)) for p in sorted(HERE.rglob("*.*")) if p.suffix != ".py"))


if __name__ == "__main__":
    main()
