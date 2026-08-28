# Release Notes

## v1.5.47 — Release candidate

This documentation set is aligned to the v1.5.47 release candidate. Verify the final installer and screenshots against the tagged release before publication.

### Simulation and verification

- Added a six-tab Simulation Workbench: **Setup**, **Blocks**, **Testbench**, **Signals**, **Models**, and **AI**.
- Added selectable engines, configurable executable paths, analysis defaults, and preflight readiness checks.
- Added functional-block scope, sources and loads, reusable testbench assertions, signal selection, model-library handling, measurements, and explicit **Pass / Fail / Not measured** results.
- Added AI assistance for simulation setup, signal measurement, and result explanation.

### AI Copilot and component generation

- Added project-aware Copilot sessions and retained design context.
- Expanded Component Review to cover BOM, connections, blocks, local-pool settings, simulation, design analysis, and netlist checks.
- Added **AI Gen** for missing components with **From Template** and **From Datasheet** workflows.
- Added review requirements for generated symbol pins, footprint pads and geometry, and symbol-to-footprint mapping.

### Libraries and import

- Added Local Library Manager workflows for KiCad folders/files and supported Altium library packages.
- Added progress feedback for KiCad project import.
- Clarified that current project import covers KiCad `.kicad_pro` and `.pro`; direct Altium/Eagle project import is not documented as supported.
- Clarified that CAD outline import currently uses SVG.

### PCB and manufacturing

- Improved interactive routing, snapping, segment editing, alignment, cleanup, and multi-trace behavior.
- Expanded design rules, net-class assignment, DFM/DRC feedback, and board-edge/via checks.
- Expanded fabrication output with Gerber X2 metadata, separate plated/unplated drill data, IPC-D-356A, BOM, and package manifest.
- Improved copper-zone, mechanical-hole, annular-ring, and 3D board behavior.

### Interface and platform

- Consolidated appearance, workspace, grid/editing, simulation, AI, version, and account options in Preferences.
- Improved panel docking, multi-monitor behavior, notifications, platform packaging, and safe shutdown behavior.

## Documentation corrections for this release

The following older guidance was removed because it did not match the current release UI or user workflow:

- Direct Altium and Eagle project import.
- Eagle library conversion instructions.
- DXF as a selectable CAD-outline input.
- Developer-only library-converter CLI commands.
- Fabricated AI Component Generator actions such as a generic **Accept & Add** button.
- Internal implementation diagrams and raw configuration-schema examples.
- Duplicate or conflicting FAQ sections and obsolete menu names.

Historical release notes from earlier documentation were not carried forward when they could not be verified against a tagged release. Use the official release archive for authoritative older history.
