# Library Converter Pipeline

WireFrame includes a powerful **command-line library converter** that transforms Altium and KiCad libraries into standardized WireFrame-compatible component packages. It automates symbol/footprint conversion, preview generation, and distribution packaging.

---

## What It Does

| Step | Description |
|---|---|
| **Parse** | Reads Altium (`.IntLib`, `.SchLib`, `.PcbLib`) and KiCad (`.kicad_sym`, `.kicad_mod`) files |
| **Convert** | Transforms components into standardized `.kicad_sym` + `.kicad_mod` format |
| **Match** | Fuzzy-matches footprints to symbols using pin analysis and naming heuristics |
| **Preview** | Generates PNG thumbnail images for each symbol and footprint (via Matplotlib) |
| **Package** | Compresses each component into a `.zip` archive for distribution |
| **Index** | Maintains a `lib_index.json` catalog of all converted components |

---

## Installation

```bash
cd WireFrame/Tools
pip install -r requirements.txt
```

### Dependencies

| Package | Purpose |
|---|---|
| `olefile` | Parsing Altium OLE compound formats |
| `sexpdata` | KiCad S-expression parsing |
| `matplotlib` | PNG preview generation |
| `gitpython` | Cloning GitHub repositories |
| `tqdm` | Progress visualization |

---

## Quick Start

### Convert from a GitHub URL

```bash
# Clone a GitHub repo and convert all libraries found
python3 run.py https://github.com/user/altium-library

# Specify KiCad target version
python3 run.py https://github.com/user/altium-library --kicad-version 7

# Custom output directory
python3 run.py https://github.com/user/altium-lib --output ~/my_kicad_libs
```

### Convert from local files

```bash
# Convert a local folder (auto-detects Altium/KiCad files)
python3 run.py --local /path/to/library

# Convert specific Altium integrated library
python3 run.py --local /path/to/MyLib.IntLib

# Convert Altium schematic library
python3 run.py --local /path/to/MyLib.SchLib
```

---

## Supported Input Formats

| Format | Extension | Description |
|---|---|---|
| **Altium IntLib** | `.IntLib` | Integrated Library (combined symbols + footprints) |
| **Altium SchLib** | `.SchLib` | Standalone schematic symbols |
| **Altium PcbLib** | `.PcbLib` | Standalone PCB footprints |
| **KiCad Symbol** | `.kicad_sym` | KiCad v6/v7/v8 symbols |
| **KiCad Footprint** | `.kicad_mod` | KiCad footprint files |
| **GitHub URL** | — | Any repo containing the above formats |

---

## Output Structure

Each component gets its own folder with all assets:

```
output/
├── STM32F103C8T6/
│   ├── STM32F103C8T6.kicad_sym    ← Schematic Symbol
│   ├── STM32F103C8T6.kicad_mod    ← PCB Footprint
│   ├── STM32F103C8T6.step         ← 3D Model (if available)
│   ├── STM32F103C8T6_sym.png      ← Symbol preview image
│   └── STM32F103C8T6_fp.png       ← Footprint preview image
│
├── RELAY_G6S-2/
│   ├── RELAY_G6S-2.kicad_sym
│   ├── RELAY_G6S-2.kicad_mod
│   └── RELAY_G6S-2.step
│
├── Dist_Repo/
│   ├── STM32F103C8T6.zip          ← Distribution package
│   ├── RELAY_G6S-2.zip
│   └── lib_index.json             ← Component catalog
```

---

## Command-Line Options

```
python3 run.py [GITHUB_URL] [options]

Positional:
  GITHUB_URL              GitHub repo URL containing libraries

Options:
  --local PATH            Convert local path instead of cloning
  --output, -o DIR        Output directory [default: ./output]
  --dist-dir DIR          Distribution directory for zips and index
  --format FMT            Input format: altium, kicad, auto [default: auto]
  --kicad-version, -k N   Target KiCad version: 6 or 7 [default: 6]
  --branch BRANCH         Git branch to clone [default: repo default]
  --keep-clone            Keep the cloned repository after conversion
  --no-preview            Skip PNG preview generation
  --no-package            Skip zip packaging and index update
  --action ACTION         'all', 'convert', or 'package'
```

---

## Smart Matching

The converter includes sophisticated matching logic:

### Symbol-to-Footprint Matching

1. **Direct match**: Component names in `.SchLib` and `.PcbLib` match exactly.
2. **Fuzzy match**: Uses string similarity to match variations (e.g., `STM32F103` vs `STM32F103C8T6`).
3. **Package-based match**: Standard packages (SOT-23, SOIC-8, etc.) are matched to symbols by pin count.
4. **Fallback generation**: If no symbol is found, a generic one is auto-generated from the footprint pin layout.

### KiCad Inheritance Resolution

For KiCad symbols using `extends` inheritance:

- The converter resolves the full inheritance chain across multiple library files.
- Child symbols inherit graphics and pins from parents, then apply their overrides.
- No manual resolution needed — it's fully automatic.

---

## Python API

You can integrate the converter into your Python scripts:

```python
from run import convert_library

result = convert_library(
    input_path='/path/to/altium-library',
    output_base='/path/to/output',
    kicad_version=6,
)

print(f"Components converted: {len(result['components'])}")
```

---

## Using Converted Libraries

After conversion:

1. Open WireFrame.
2. Load the converted `.kicad_sym` files via the Library panel (**Load Symbols…**).
3. Load the converted `.kicad_mod` files via the Library panel (**Load Footprints…**).
4. Components are ready to use in your designs.

!!! tip "Batch conversion"
    Use the `build_all_libs.sh` script to convert all libraries in a directory at once:
    ```bash
    bash build_all_libs.sh /path/to/libraries /path/to/output
    ```

---

## See Also

- [Symbol Libraries](symbols-library.md) — loading and using symbol libraries.
- [Footprint Libraries](footprints-library.md) — loading and using footprint libraries.
- [Projects & Files — Importing](../projects.md#importing-projects-from-other-eda-tools) — importing entire projects (not just libraries).
