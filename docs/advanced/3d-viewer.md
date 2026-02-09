# 3D Viewer

The 3D viewer (`Pcb3D_Viewer`) renders a 3D representation of the PCB using `Pcb3D_Renderer` and `Pcb3D_Camera`.

---

## Opening the 3D viewer

From a PCB document:

1. Use **View → 3D Viewer…** or an equivalent toolbar button.
2. The 3D viewer opens as a separate ImGui window.
3. It renders:
   - The board (as a 3D extruded shape).
   - Footprints with 3D models (if available).
   - Simple colored boxes for footprints without models.

> **Image placeholder**  
> `![3D viewer](img/3d/3d-viewer.png)`  
> _3D view of a PCB rotated at an angle, with a semi‑transparent board and colored components._

---

## Camera controls

`Pcb3D_Camera` defines:

- `target` – look‑at point.
- `distance` – camera distance from target.
- `yaw`, `pitch` – rotation angles.

In the viewer:

- **Orbit**:
  - Drag with left or right mouse buttons to orbit around target.
- **Pan**:
  - Middle mouse drag to move target parallel to screen.
- **Zoom**:
  - Mouse wheel to change `distance`, focusing around the cursor.

The camera computes view matrices using `glm::lookAt` with Z‑up.

---

## Board and component rendering

`Pcb3D_Viewer::renderSceneContent`:

- Builds or updates a `DynamicMesh` representing the board, using:
  - Board outline geometry from zones or Edge.Cuts.
  - Board thickness parameter.
- For each placed footprint:
  - If `model3D` exists:
    - Try to resolve model path using project library path.
    - Load mesh via `ModelLoader`:
      - STEP files via `StepImporter` (Open CASCADE).
      - OBJ/STL etc. via Assimp.
    - Draw model with appropriate color based on designator prefix (R, C, U, etc.).
  - Else:
    - Draw a simple box approximating the footprint boundary.

The renderer supports:

- Simple Phong‑like shading with ambient + diffuse lighting.
- Alpha blending for translucent elements (e.g., board).

---

## Model caching

`Pcb3D_Renderer` caches uploaded meshes:

- `m_meshCache` maps model path to one or more `GLMesh` objects.
- Avoids reloading and re‑uploading the same model each frame.

`clearCache()` can be used (internally) to free memory if many different models are used.

---

## Use cases

- **Visual inspection**:
  - Check component orientations.
  - Verify placement density and mechanical clearances.
- **Presentation**:
  - Capture screenshots for documentation or manufacturing communication.
- **3D alignment**:
  - Combined with `ModelAlignmentDialog` to fine‑tune 3D model offsets.

> **Video placeholder**  
> _Short video demonstrating rotation, zoom and panning of the 3D view, with the user toggling component visibility and verifying the fit of a connector with the board edge._