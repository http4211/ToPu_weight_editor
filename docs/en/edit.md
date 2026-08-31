# Edit

<p align="left">
  <img width="107" alt="image" src="https://github.com/user-attachments/assets/c63dd83d-edeb-476b-8a78-c8a682264b16" />
</p>

The `Edit` section holds `x-` / `x+`, plus `Smooth Weights`, `Mirror`, `Bone Creation` and `Apply Rest Pose`.

### Selecting vertices by X side

<img width="53" alt="Image" src="https://github.com/user-attachments/assets/b50216db-62f4-4d14-b880-35172f970311" />

<p align="left">
  <img width="1304" alt="Image" src="https://github.com/user-attachments/assets/e224cfe8-1ec2-4d8d-92ce-7dbead312eb4" />
</p>

Selects vertices on the `x-` or `x+` side, using the armature origin (or each object's origin when there is no armature) as the reference.

- Plain click — does not select vertices on the center line.
- `Shift + Click` — also selects the center-line vertices.

### Smooth Weights

<img width="299" alt="image" src="https://github.com/user-attachments/assets/df0b567d-c156-4139-9d88-2e4b572a6dcd" />

<p align="left">
  <img width="1236" alt="Image" src="https://github.com/user-attachments/assets/ba09f7df-ebff-4b3c-886e-9c563eec4936" />
</p>

Blends the weights of the selected vertices into their surroundings.

- Plain click — smooths the selected vertices.
- `Shift + Click` — smooths the full weight range of the selected column plus one outer ring.
- `Ctrl + Click` — repairs abnormal weights using the surroundings as the reference.
- `…` — detail settings: range, method (`Fast` / `Surface` / `Volume`), iterations, and the cleanup applied afterwards.

### Mirror

<img width="478" alt="image" src="https://github.com/user-attachments/assets/ab59df15-6f02-46ab-9c79-0ed322987407" />

<img width="339" alt="image" src="https://github.com/user-attachments/assets/ba82830e-3339-474e-87a3-989f86abf288" />

<p align="left">
  <img width="1354" alt="Image" src="https://github.com/user-attachments/assets/f45e4116-7cf0-4867-9eca-9b5b7fdc8ead" />
</p>

Brings weights over from the mirrored position on the opposite side. Left/right names such as `_L` / `_R` are swapped as well.

- Plain click — mirrors the selected vertices.
- `Ctrl + Click` — choose a direction and mirror the whole target object (or selected vertices only).
- `…` — detail settings: mirror direction, reference space, search distance, center correction, center tolerance and the left/right word sets.

Notes.

- Asymmetric geometry is supported (the reflected position is projected onto the source surface and interpolated; can be disabled in the details).
- If the opposite vertex group is missing but the corresponding opposite bone exists, it is created automatically (otherwise a dialog lets you create or skip).
- **Center L/R Balancing** (on by default) balances the L/R weights of center-axis vertices. Turn off `Balance Center L/R Weights` in Mirror Details to skip only this step.

### Bone Creation

<p align="left">
  <img width="458" alt="image" src="https://github.com/user-attachments/assets/e8583f09-280f-4af6-a9bc-19f993d039c6" />
  <img width="1280" alt="Image" src="https://github.com/user-attachments/assets/752b69ab-1cc3-4801-9613-42bcd4463eb1" />
</p>

Creates a bone chain or branched bone tree from edges selected in Mesh Edit Mode.

- Plain click — chooses a suitable method from the selected edges and opens the confirmation dialog (closed loops / open paths / edge rings / branching edges).
- `Ctrl + Click` — opens `Bone Creation Settings` (defaults).
- Bone direction is based on the last-selected active edge, which becomes the tip.
- `Bone Count` and `Reverse Direction` (and `Branch Count` for branches) can be adjusted in the confirmation dialog and via `F9`. The dialog also controls Auto Weights, target, naming, connection, roll reference and post-creation mode.
- Multiple open paths — `Center Axis` off creates an independent chain on each path; on averages them into one center chain.

`Auto Weights` (in the dialog) weights the target region using only the newly created bones (`Blender Built-in` / `Voxel Heat Skinning`). With `Replace Existing Weights`, existing bone weights on the selected vertices are cleared first (non-bone groups are preserved).

> The target is normally the selected vertices. But if you select two or more edge loops that sandwich a section of the mesh, the vertices between those loops are weighted as well. A separate mesh that is not connected to the selection is never affected.

`Bone Roll Reference` : `Automatic Axis` / `Selected Edge Surface` / `Mesh Local Z` / `Mesh Local Y` / `World Z` / `World Y`.

#### Split Bone and Weights

<p align="left">
  <img width="439" alt="image" src="https://github.com/user-attachments/assets/d02ef477-5d14-4015-a27f-b6a44dc5cc26" />
</p>

`Shift + Click` on `Bone Creation` splits existing bones into connected chains and redistributes each matching vertex-group weight among the resulting bones.

- Target — the selected bones (Pose / Object / Armature Edit Mode), or the bone matching the TPWE active column (Mesh Edit Mode).
- `Split Count` (2–64) and `Smooth` (transition width between split bones, default `0`).
- `Mirror` (on by default) — splits the opposite side with the same settings using the left/right word sets.
- After execution, `F9` can readjust `Split Count`, `Smooth` and `Mirror`.

### Apply Rest Pose

<p align="left">
  <img width="1302" alt="Image" src="https://github.com/user-attachments/assets/9f61975e-ab08-4fa3-a47d-47aefd04bfdf" />
</p>

Applies the current visual pose as the new rest pose. Action and shape-key retargeting are supported.

> It can modify armature rest data, mesh / shape-key coordinates, Actions and NLA-referenced animation. **Save a backup before running it.**
