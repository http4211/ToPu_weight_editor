# Weight Copy

<img width="189" height="113" alt="image" src="https://github.com/user-attachments/assets/7dffb678-b146-43cb-9fb5-e6b892af89b1" />

<p align="left">
  <img width="1042" height="770" alt="Image" src="https://github.com/user-attachments/assets/b8453e66-c226-46db-b887-b2e01a3a3042" />
</p>

- `Vtx Copy` / `Vtx Paste` — copy the active vertex's weights and paste onto the selected vertices.
- `Near Copy` / `Near Paste` — store the selected vertices' positions and weights, then paste the closest stored weights.
- `Auto Weight` — bind the selected meshes to an armature and assign automatic weights.
- `Obj Xfer` — transfer weights from the active mesh to the other selected meshes.

The `…` next to `Auto Weight` and `Obj Xfer` opens their detail settings.

### S / T buttons (column transfer)

`S` / `T` on the right of the section title are transfer shortcuts for the current column.

- `S` — register the current column as the transfer source.
- `T` — transfer from the registered source into the current column.
- `Shift + T` — open the `Multi Weight Transfer` dialog, pre-filled with the source and current column.

### Object transfer

Transfers weights from the object selected last (the active one) to the other selected objects. Because it transfers per face, results stay relatively clean even on low-poly meshes (at the cost of a heavier computation).

- `Robust Weight Inpainting` — fills in unmatched areas during the transfer.
- `Clothing Inner-Side Mode` — uses source normals and distance to prioritize inner-shell candidates.
- If a destination has no Armature modifier, one can be added automatically (on by default).

### Auto Weight

<img width="576" height="310" alt="image" src="https://github.com/user-attachments/assets/08be9571-5c7e-44ce-b7a9-0c6531d67393" />

<img width="433" height="326" alt="image" src="https://github.com/user-attachments/assets/7634218e-d086-4b3c-a080-26a5ac5cfca1" />

Binds the selected meshes to an armature and assigns automatic weights. It can keep parent relationships and weight only the part covered by the current selection. The detail settings switch between Blender's built-in automatic weights and Voxel Heat Skinning.

**Main Voxel Heat Skinning settings**

- `Voxel Heat Resolution` — voxels along the longest axis. Higher preserves more detail but increases time and memory.
- `Diffuse Loops` — diffusion passes (resolution × loops). Higher propagates more smoothly but takes longer.
- `Occupied Cell Dilation` — expands surface voxels to prevent broken propagation on thin outfits. Set `0` if weights leak across touching parts.
- `Diffuse Falloff` — higher reduces distant-bone contribution, producing tighter local weights.
- `Distance Falloff` — higher favors nearby bones more strongly.
- `Detect Solidify` — gives thin outfits and shells volume (occupied-cell dilation is at least 1 when on).
- `Solid Votes` — axis-inside tests required to classify an interior cell. `2` majority, `1` broader, `3` stricter.
- `Maximum Influences` — max bones per vertex (default `4`).
- `Smoothing` / `Smoothing Passes` — smooths boundaries after weighting (default ON, `5` passes).
- `Range Proxy (Object)` — uses visible meshes only to correct the calculation range. Weights are written only to selected meshes (default OFF).
- `Range Proxy (Edit)` — for partial weighting, uses unselected vertices and meshes sharing the armature as proxies. Weights are written only to selected vertices (default OFF).

> Processing time depends heavily on resolution, `Diffuse Loops` and target vertex count, and Blender may remain unavailable until it finishes.

**Use Specified Bones Only**

When on, automatic weighting is restricted to the saved bone list (both methods, Object and Edit Mode).

- `Get Selected Bones` — captures the bone selection from Edit / Pose / Object Mode.
- `All` / `None` and the checklist adjust the list.
- `Enabled First` (on by default) — groups enabled bones at the top.
