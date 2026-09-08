# Edit

<p align="left">
  <img width="107" alt="image" src="../images/en/edit-01.png" />
</p>

The `Edit` section holds `x-` / `x+`, plus `Smooth Weights`, `Mirror`, `Bone Creation` and `Apply Rest Pose`.

### Selecting vertices by X side

<img width="53" alt="Image" src="../images/shared/selecting-vertices-by-x-side-01.png" />

<p align="left">
  <img width="1304" alt="Image" src="../images/shared/selecting-vertices-by-x-side-02.gif" />
</p>

Selects vertices on the `x-` or `x+` side, using the armature origin (or each object's origin when there is no armature) as the reference.

- Plain click — does not select vertices on the center line.
- `Shift + Click` — selects only the center-line vertices.

### Smooth Weights

<img width="299" alt="image" src="../images/en/smooth-weights-01.png" />

<p align="left">
  <img width="1236" alt="Image" src="../images/shared/smooth-weights-01.gif" />
</p>

Blends the weights of the selected vertices into their surroundings.

- Plain click — smooths the selected vertices.
- `Shift + Click` — smooths the selected column’s weighted region plus one outer ring. In multi-object Edit Mode, this includes meshes with no selected vertices.
- `Ctrl + Click` — repairs abnormal weights using the surroundings as the reference.
- `…` — detail settings: range, method (`Fast` / `Surface` / `Volume`), iterations, and the cleanup applied afterwards.
- Shift-click settings: `Border Spread Value` (default `0.01`; `0` disables outward expansion) and `Selected Vertices Only` (off by default). Enable the latter to restrict the whole range, including the outer ring, to selected vertices.

### Mirror

<img width="478" alt="image" src="../images/en/mirror-01.png" />

<img width="339" alt="image" src="../images/en/mirror-02.png" />

<p align="left">
  <img width="1354" alt="Image" src="../images/shared/mirror-01.gif" />
</p>

Brings weights over from the mirrored position on the opposite side. Left/right names such as `_L` / `_R` are swapped as well.

- Plain click — mirrors selected vertices in Edit / Weight Paint Mode. In Object Mode, opens a direction dialog and mirrors the whole selected meshes.
- `Ctrl + Click` — choose a direction and mirror the whole target object (or selected vertices only).
- `…` — detail settings: mirror direction, reference space, search distance, center correction, center tolerance and the left/right word sets.

Notes.

- Supports multiple meshes. Selected-vertex mirroring uses each mesh’s own selection; whole-mesh mirroring also includes edited meshes with no selected vertices.
- Asymmetric geometry is supported (the reflected position is projected onto the source surface and interpolated; can be disabled in the details).
- If the opposite vertex group is missing but the corresponding opposite bone exists, it is created automatically (otherwise a dialog lets you create or skip).
- **Center L/R Balancing** (on by default) balances the L/R weights of center-axis vertices. Turn off `Balance Center L/R Weights` in Mirror Details to skip only this step.

### Bone Creation

<p align="left">
  <img width="458" alt="image" src="../images/en/bone-creation-01.png" />
  <img width="1280" alt="Image" src="../images/shared/bone-creation-01.gif" />
</p>

Creates a bone chain or branched bone tree from edges selected in Mesh Edit Mode.

- Plain click — chooses a suitable method from the selected edges and opens the confirmation dialog (closed loops / open paths / edge rings / branching edges).
- `Ctrl + Click` — opens `Bone Creation Settings` (defaults).
- Bone direction is based on the last-selected active edge, which becomes the tip.
- `Bone Count` and `Reverse Direction` (and `Branch Count` for branches) can be adjusted in the confirmation dialog and via `F9`. The dialog also controls Auto Weights, target, naming, connection, roll reference and post-creation mode.
- Multiple open paths — `Center Axis` off creates an independent chain on each path; on averages them into one center chain.

`Auto Weights` (in the dialog) weights the target region using only the newly created bones (`Blender Built-in` / `Voxel Heat Skinning`). With `Replace Existing Weights`, existing bone weights belonging to the destination armature are cleared from the target vertices first. Unrelated vertex groups are preserved.

> The target is normally the selected vertices. When multiple open edge paths enclose the same connected mesh strip, unselected vertices between them are included. Disconnected meshes are unaffected. `Center Axis` uses the same region.

`Bone Roll Reference` aligns the bone axes while keeping each bone along its chain.

- `Automatic Axis` — chooses a suitable reference axis automatically.
- `Selected Edge Surface` — follows the faces connected to the selected edges.
- `Mesh Local Z` — uses the mesh’s local Z axis.
- `Mesh Local Y` — uses the mesh’s local Y axis.
- `World Z` — uses the world Z axis.
- `World Y` — uses the world Y axis.

#### Split Bone and Weights

<p align="left">
  <img width="439" alt="image" src="../images/en/split-bone-and-weights-01.png" />
</p>

`Shift + Click` on `Bone Creation` splits existing bones into connected chains and redistributes each matching vertex-group weight among the resulting bones.

- Target — the selected bones (Pose / Object / Armature Edit Mode), or the bone matching the TPWE active column (Mesh Edit Mode).
- `Split Count` (2–64) and `Smooth` (transition width between split bones, default `0`).
- `Mirror` (on by default) — splits the opposite side with the same settings using the left/right word sets.
- After execution, `F9` can readjust `Split Count`, `Smooth` and `Mirror`.

### Apply Rest Pose

<p align="left">
  <img width="1302" alt="Image" src="../images/shared/apply-rest-pose-01.gif" />
</p>

Applies the current visual pose as the new rest pose. Action and shape-key retargeting are supported.

> It can modify armature rest data, mesh / shape-key coordinates, Actions and NLA-referenced animation. **Save a backup before running it.**
