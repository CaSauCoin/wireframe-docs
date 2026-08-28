# Symbol Libraries (Schematic)

Symbol libraries define the electrical symbols used in schematic design. This page covers loading, structure, built-in symbols, and footprint linking.

---

## Loading Symbol Libraries

From the Library panel when a schematic is active:

1. Click **Load Symbols…**
2. Select one or more KiCad symbol files (`.kicad_sym`).
3. WireFrame parses the selected files immediately.
4. Once complete, results are merged into the symbol library map.
5. Available symbol names appear in a filterable list.

![Symbol Loading](../img/libraries/symbol-loading.png)


---

## Symbol Structure

Each parsed symbol data includes:

| Data | Description |
|---|---|
| **Pins** | Name, number, position, angle, length, electrical type (input/output/power), visibility |
| **Graphics** | Rectangles, polylines, circles, arcs that form the symbol outline |
| **Texts** | Reference ("R?"), Value, user-defined texts |
| **Properties** | Footprint (default footprint name), BOM inclusion flags, parent symbol |

### Pin types

| Electrical type | Description |
|---|---|
| Input | Signal input pin |
| Output | Signal output pin |
| Bidirectional | Can be input or output |
| Power | Power pin (VCC, GND) |
| Passive | Passive component pin (resistor, capacitor) |
| Open Collector | Output that can only sink current |

### Symbol inheritance

- Inheritance resolution merges properties from **parent symbols** before use.
- Child symbols inherit graphics and pins from their parent, then override or add to them.

---

## Virtual / Built-In Symbols

The built-in component library and the component manager provide simplified built-in components that don't require external library files:

| Symbol | Pins | Purpose |
|---|---|---|
| `NetLabel` | 1 pin at origin | Net naming label |
| `VCC` | 1 pin | Positive power rail symbol |
| `GND` | 1 pin | Ground reference symbol |
| `VDD` | 1 pin | Alternative positive power symbol |

These are used by the toolbar buttons for quick placement of power symbols and net labels.

---

## Linking Footprints to Symbols

the footprint linking feature associates a default footprint with a symbol in the library:

### How it works

1. Select a symbol in the Library panel.
2. Use the **Link Footprint** action (right-click menu or button).
3. Choose a footprint from the loaded footprint libraries.
4. The symbol's `Footprint` property is updated in the `.kicad_sym` file via an internal process.

### Result

- Future instances of that symbol automatically get the linked footprint in their properties.
- Existing placed components are **not retroactively updated** — edit them individually if needed.

<video controls width="100%">
  <source src="../img/libraries/symbol-footprint-link.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## Importing Libraries from Other EDA Tools

### Importing Altium symbol libraries

WireFrame can convert Altium schematic libraries for use in your projects:

1. Go to **File → Import → Altium Library…**
2. Select an Altium symbol library file (`.SchLib` or `.IntLib`).
3. WireFrame converts the symbols and adds them to your library panel.

| Altium format | Support |
|---|---|
| `.SchLib` | Full import — symbols, pins, graphics |
| `.IntLib` | Extracted and converted (integrated libraries) |

!!! info "Post-import review"
    After importing Altium symbols, verify pin assignments and footprint links. Some Altium-specific properties may not have a direct equivalent in WireFrame.

### Importing Eagle symbol libraries

Eagle library files (`.lbr`) contain both symbols and footprints. When importing:

1. Go to **File → Import → Eagle Library…**
2. Select an Eagle `.lbr` file.
3. WireFrame extracts both symbols and footprints from the file.
4. Symbols appear in the Library panel when a schematic is active.

!!! note "Eagle version"
    Only Eagle XML format (version 6+) is supported for library import.

---

## Creating Custom Symbols

Need a custom symbol not found in your libraries?

- Use the interactive [Symbol Creator](symbol-creator.md) to draw custom symbols or generate IC symbols with the wizard.
- Use the [Library Converter](library-converter.md) to bulk-convert Altium or KiCad libraries.
- Use the [AI Component Generator](../ai/component-generator.md) to generate symbols directly from datasheets.

---

## See Also

- [Symbol Creator](symbol-creator.md) — create custom symbols manually or with the wizard.
- [Library Converter](library-converter.md) — command-line converter for Altium/KiCad libraries.
- [AI Component Generator](../ai/component-generator.md) — datasheet-based automatic symbol creation.
- [Placing Components](../schematic/placing-components.md) — place symbols from loaded libraries.
- [Footprint Libraries](footprints-library.md) — the PCB-side library counterpart.
- [File Formats](../reference/file-formats.md) — KiCad `.kicad_sym` format details.
