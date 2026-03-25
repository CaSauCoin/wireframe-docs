# 3D Viewer

The 3D viewer renders a three-dimensional representation of your PCB board, showing component placement and board geometry. It is powered by the 3D viewer, the 3D renderer, and the 3D camera.

---

## Opening the 3D Viewer

From a PCB document:

1. Use **View → 3D Viewer…** or an equivalent toolbar button.
2. The 3D viewer opens as a **separate ImGui window**.
3. It renders:
    - The **board** as a 3D extruded shape (based on Edge.Cuts outline and board thickness).
    - **Footprints** with 3D models (STEP/OBJ) if available.
    - **Simple colored boxes** for footprints without 3D models.

<!-- TODO: Replace with actual screenshot
     Capture the 3D viewer showing a populated PCB:
     - _The board visible as a semi-transparent green slab (PCB substrate) with the correct outline shape._
     - _Several 3D component models visible: resistors as small rectangular blocks, an IC with visible pins, a connector standing upright._
     - _Components on both sides of the board (if any are flipped to the back)._
     - _The board rotated at an angle (~30° pitch, ~15° yaw) to show depth and perspective._
     - _A dark background with simple lighting (ambient + diffuse)._
     Suggested size: 800×600px.
-->
![3D Viewer](../img/3d/3d-viewer.png)


---

## Camera Controls

the 3D camera manages the 3D view:

| Control | Input | Description |
|---|---|---|
| **Orbit** | Left or right mouse button drag | Rotates the camera around the target point |
| **Pan** | Middle mouse button drag | Moves the target point parallel to the screen |
| **Zoom** | Mouse scroll wheel | Changes distance from the target |

Camera parameters:

| Parameter | Description |
|---|---|
| `target` | The point the camera looks at (center of orbit) |
| `distance` | Distance from camera to target |
| `yaw` | Horizontal rotation angle |
| `pitch` | Vertical rotation angle |

The camera computes view matrices using a standard look-at function with **Z-up** convention.

---

## Board and Component Rendering

The 3D viewer builds the 3D scene:

### Board

- Built from board outline geometry (Edge.Cuts or zones).
- Extruded to `boardThickness` to create a 3D slab.
- Rendered with semi-transparent material (green-ish PCB substrate).

### Components

For each placed footprint:

| Condition | Rendering |
|---|---|
| 3D model exists | Load mesh from STEP (via the STEP importer) or OBJ/STL (via Assimp), apply color based on component type |
| No 3D model | Draw a simple box approximating the footprint boundary, colored by designator prefix |

### Component color by type

| Prefix | Color | Component type |
|---|---|---|
| R | Beige/brown | Resistor |
| C | Yellow | Capacitor |
| U | Dark grey | IC |
| J, P | Light grey | Connector |
| D | Green | Diode |
| Q | Black | Transistor |

### Rendering features

- Simple **Phong-like shading** with ambient + diffuse lighting.
- **Alpha blending** for translucent elements (board substrate).
- **Mesh caching** (the mesh cache) — avoids reloading the same model each frame.

---

## Model Caching

the 3D renderer caches uploaded meshes:

| Feature | Description |
|---|---|
| Cache key | Model file path |
| Cache content | One or more GPU mesh objects (uploaded to GPU) |
| First load | Parse file → tessellate → upload to GPU (may be slow for STEP) |
| Subsequent frames | Reuse cached GPU data (fast) |

clearing the cache frees GPU memory if many different models are used.

!!! tip "Performance"
    First-time loading of STEP files can take several seconds due to mesh tessellation. Subsequent renders use the cached mesh and are fast.

---

## Use Cases

| Use case | How |
|---|---|
| **Visual inspection** | Check component orientations, verify placement density |
| **Mechanical clearance** | Verify that tall components don't interfere with enclosures |
| **Presentation** | Capture screenshots for documentation or client communication |
| **3D alignment** | Use with [Model Alignment Dialog](../libraries/footprints-library.md#3d-model-alignment) to fine-tune model positions |

<!-- TODO: Replace with actual video
     Record a 20-second clip:
     1. _Open the 3D viewer from a PCB document with 8–10 placed footprints._
     2. _The 3D board and components appear._
     3. _Orbit the view (left-click drag) — rotate around the board to show all sides._
     4. _Zoom in (mouse wheel) to a specific component (e.g., an IC) to show detail._
     5. _Pan (middle-click drag) to center a connector at the board edge._
     6. _Zoom out to show the full board._
     Resolution: 1280×720 at 30fps.
-->
<video controls width="100%">
  <source src="../../img/3d/3d-viewer-demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

## See Also

- [Footprint Libraries — 3D Model Alignment](../libraries/footprints-library.md#3d-model-alignment) — position 3D models on footprints.
- [PCB Editor](../pcb/index.md) — the 2D PCB workspace.
- [Fabrication & Export](../pcb/fabrication-and-export.md) — export the board design after 3D verification.
