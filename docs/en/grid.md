# Grid Controls

## Presets, Input & Apply

### Preset buttons

<img width="492" height="101" alt="image" src="https://github.com/user-attachments/assets/11f48284-8a22-4133-b3e9-a97db0e69445" />

<img width="280" height="28" alt="Image" src="https://github.com/user-attachments/assets/463b655c-5b92-4641-89bd-a3abeff80b92" />

<p align="left">
  <img width="1188" height="764" alt="Image" src="https://github.com/user-attachments/assets/df656172-edbc-4420-9059-4b3932b18cf3" />
</p>

Applies `0`, `0.1`, `0.25`, `0.5`, `0.75`, `0.9` or `1` in one click. In `Add` / `Add%` mode, `Shift + Click` applies the negative value. Preset values can be changed in the add-on preferences.

### Input mode, slider and value field

<img width="494" height="158" alt="image" src="https://github.com/user-attachments/assets/c3a9a157-9ab5-4a09-a081-183b39b28a99" />

<img width="693" height="37" alt="Image" src="https://github.com/user-attachments/assets/56fd28a7-e82b-4c60-a4ee-034649542502" />

<p align="left">
  <img width="1188" height="756" alt="Image" src="https://github.com/user-attachments/assets/e0c3594f-f8f7-43d0-a298-a64aca7c210e" />
</p>

The leftmost button cycles the input mode through `ABS` → `ADD` → `ADD%`.

- `Abs` — replaces the value with the entered one.
- `Add` — adds to the current value (negative values subtract).
- `Add%` — adds a percentage of the current value.

Usage.

- Dragging the slider applies in real time (with **10,000+ target vertices**, weights are committed on release).
- Click the value field to type; scroll the wheel over it to nudge the value.
- `Apply` — applies the value field to the current column of the selected vertices.
- `⟳` — rebuilds the grid from the current selection (useful after special selection commands).
- `Ctrl + Wheel` adds / subtracts, `Ctrl + Shift + Wheel` in finer steps (step sizes are set in preferences).

---

## Special Group Selection / Pick Bone

<img width="338" height="197" alt="image" src="https://github.com/user-attachments/assets/3f38bdb8-8fc5-48c9-ae62-89f9627bb8ee" />

<img width="109" height="24" alt="Image" src="https://github.com/user-attachments/assets/3257c432-2a43-482e-8eef-dddd109b300b" />

<p align="left">
  <img width="1218" height="758" alt="Image" src="https://github.com/user-attachments/assets/4324d885-a267-470a-b215-f4b7ef63ed39" />
</p>

`Pick Bone` lets you click a bone in the viewport to select the vertex-group column with that bone's name. With several Armature modifiers, the globally nearest visible bone is used.

- While the overlay is open, `Alt + Right Click` also starts bone picking by default (`Shift + Click` on `Pick Bone` toggles it).
- The `…` opens the excluded-word and shortcut settings (excluded words keep bones containing `IK`, `FK`, `twist` and similar out of the candidates).
- When `▣↖` is on, changing the selection automatically selects the highest-weight column. Suits switching vertices often to check the dominant influence bone.

<p align="center">
  <img src="README_images/bone_pick.gif" alt="Bone picking" width="720">
</p>

---

## Column State & Visibility (Lock / Ignore / Force Show)

<img width="157" height="28" alt="image" src="https://github.com/user-attachments/assets/1abf4eb8-5e6b-46e5-8fb4-13e5b1e48628" />

<img width="399" height="195" alt="image" src="https://github.com/user-attachments/assets/997d4dac-03f2-4866-a578-2b15df0007d8" />

<p align="left">
  <img width="1192" height="766" alt="Image" src="https://github.com/user-attachments/assets/5d1c7790-e614-45b6-8d47-9243c6fb875a" />
</p>

- `Lock` — makes the selected column non-editable.
- `Ignore` — excludes the column from totals, normalization and cleanup.
- `Force Show` — keeps a column in the grid even when its weights are zero.
- `Shift + Click` applies to every column except the selected one; `Alt + Click` clears the state everywhere.
- `Ctrl + Force Show` opens a text filter to force-show every group matching comma-separated fragments.

---

## Grid Controls & Bottom Tabs

### Column headers

<p align="center">
  <img width="1346" height="790" alt="Image" src="https://github.com/user-attachments/assets/e5329a73-88bd-48c9-92db-512e42d478b0" />
</p>

- Click — makes it the selected column.
- `Shift + Click` — selects every vertex that has a value in that group.
- `Ctrl + Click` — keeps only the current-selection vertices that have a value in that column.
- `Ctrl + Shift + Click` — cell-selects every cell in that column (all displayed rows, across pages).
- Right-click — opens the **weight transfer menu**.

### L / Vertex / Sum

<img width="111" height="33" alt="image" src="https://github.com/user-attachments/assets/7af6fa19-7275-46ae-972a-25e2ab45ceb2" />

<p align="center">
  <img width="1192" height="762" alt="Image" src="https://github.com/user-attachments/assets/1f944500-6102-4533-915b-c1667d87732d" />
</p>

- `L` — weight-lock the target vertices (`Alt + Click` unlocks). Each row's `L` cell also toggles the lock (drag for several).
- `Vertex` — grid-select the displayed rows (`Alt + Click` clears). Each row's `Vertex` cell highlights that vertex in the viewport and keeps it visible.
- `Sum` — toggle **violation-only view** (`Shift + Click` selects the vertices shown in the grid).
- When some vertices have a total-value or influence-count problem, the `Sum` header changes to `Sum ⚠`.
- Violation-only view covers violations across every page, not just the current one.

### Cells

<p align="center">
  <img width="1184" height="758" alt="Image" src="https://github.com/user-attachments/assets/d40e61e9-ae42-4cf0-b916-46545d88c886" />
</p>

- Click — type the value directly (`Enter` confirms). Start with `+` `-` `*` `/` for a relative operation (for example `*0.5` or `+0.1`).
- Drag — select a range (`Shift + Drag` adds, `Ctrl + Drag` removes).
- Right-click — clear the cell selection.
- `Ctrl + Shift + Click` — cell-selects the whole column of that cell (same as from the column header).
- With several cells selected, the entered value applies to all at once. While a cell selection remains, every value-changing operation (slider / wheel / presets / Apply) prioritizes the selected cells over the live mesh selection.

<p align="center">
  <img src="README_images/cell_edit.gif" alt="Cell editing" width="720">
</p>

### Column tabs

<p align="left">
  <img width="562" height="31" alt="image" src="https://github.com/user-attachments/assets/9a6f941e-05c7-4855-812e-7f618001c662" />
  <img width="1186" height="764" alt="Image" src="https://github.com/user-attachments/assets/153b50ac-3af7-404e-9795-18da04257bc9" />
</p>

The tabs below the grid choose which columns are shown.

- `All` — bone columns and non-bone columns.
- `Deform` — only deform vertex groups whose names match a bone.
- `Other` — only non-bone vertex groups that do not match a bone name.

Per-tab options.

- `Ignore Non-Bone Columns` (All tab) — marks non-bone groups as ignored.
- `Always Show` (Other tab) — always shows existing non-bone columns even when the selection has no values for them.
- `Allow >1` (Other tab) — when on, Other columns are not treated as violations at a total of 1 or more, and are not normalized.
- `Hidden Words` — hides specified words from the group-name display (actual names are unchanged).

### Column right-click weight transfer

<p align="left">
  <img width="515" height="246" alt="image" src="https://github.com/user-attachments/assets/08b1ca77-55aa-438a-bb2d-dab1ee1afd59" />
  <img width="577" height="835" alt="image" src="https://github.com/user-attachments/assets/a38e5d23-7c4a-4102-971a-b54873d67845" />
</p>

Right-clicking a column header opens the vertex-group transfer menu.

- `Set as Transfer Source` / `Transfer to This Column` — make the right-clicked column the source and transfer into the current column.
- `Multi Weight Transfer` — transfer with explicit source, destination, method (`Copy` / `Move` / `Replace`) and scope (whole group / selected vertices). Several pairs can be processed together.

---

## Multi-object editing

When several meshes are in Edit Mode at once, the grid footer shows the current column, selected-vertex count and a multi-edit indicator (`N obj`), and the vertices of all objects are handled together.

A `Sync Selection` button is also added to `Properties > Object Data > Vertex Groups`; turning it on synchronizes the vertex-group selection across the objects.
