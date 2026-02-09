# Symbol Libraries (Schematic)

Symbol libraries are managed by `LibraryManager` and used by `ComponentManager`.

---

## Loading symbol libraries

From the Library panel in schematic context:

1. Click **Load Symbols…**.
2. Choose one or more KiCad symbol files.
3. `LibraryManager::queueLoadSymbolsFromFiles`:
   - Launches background parsing via `KicadSymbolParser`.
   - Once complete, `loadSymbols` merges results into the symbol library map.

The available symbol names are shown in a list; they can be filtered with a search string.

---

## Symbol structure

Parsed `SymbolData` includes:

- Pins:
  - Name, number, position, angle, length.
  - Electrical type (input, output, power, etc.).
  - Visibility (hidden/visible).
- Graphics:
  - Rectangles, polylines, circles, arcs.
- Texts:
  - Reference, value, user texts.
- Properties:
  - Footprint property (mapping symbol to default footprint).
  - DefaultFootprintName.
  - Parent symbol (for inheritance).
  - Flags for BOM and board presence.

Inheritance:

- `resolveInheritance` merges properties from parent symbols before use.

---

## Virtual / built‑in symbols

`Component_Library` and `ComponentManager` add some built‑in component definitions:

- `NetLabel`
- `VCC`
- `GND`
- `VDD`

These are simplified components with:

- Single pin at origin.
- Component type used by toolbar for power symbols and net labels.

---

## Linking footprints to symbols

`LibraryManager::linkFootprintToSymbol`:

- Modifies symbol library files to include/update a `Footprint` property.
- Uses `injectFootprintProperty` to insert the property into symbol S‑expressions.

From the user perspective:

- You can pair a symbol with a default footprint in the library panel.
- Future component instances automatically get this footprint assigned in their properties.

> **Image placeholder**  
> `![Symbol-footprint link](img/libraries/symbol-footprint-link.png)`  
> _UI showing a symbol selected with a button to attach a default footprint from the loaded footprint libraries._