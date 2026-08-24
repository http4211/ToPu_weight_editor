# ToPu_weight_editor

<p align="center">
  <img width="611" height="807" alt="image" src="https://github.com/user-attachments/assets/e69834b9-3d6d-47b2-b239-baccc06b948f" />
</p>

<p align="center">
  <a href="README.md">日本語</a> | <b>English</b>
</p>

ToPu:Weight Editor is a Blender add-on for reviewing and editing skin weights.
From a **GPU overlay** drawn in the 3D View, it puts numeric editing, cleanup, smoothing, mirroring, copy / transfer, bone picking, bone creation and display helpers into one place. No external framework or extra Python package is required.

> **This document describes version 1.5.179.**
> The N-panel and Pie Menu from the 1.4 series have been removed; all operations now live in the GPU overlay. The overlay shortcut also changed from `W` to `Ctrl + W`.

## Table of contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Opening the editor](#opening-the-editor)
- [Quick start](#quick-start)
- [GPU overlay / Header row](#gpu-overlay--header-row)
- [Weight snapshots](#weight-snapshots)
- [Bone transform](#bone-transform)
- [Edit](#edit) ([Smooth Weights](#smooth-weights) / [Mirror](#mirror) / [Bone Creation](#bone-creation) / [Apply Rest Pose](#apply-rest-pose))
- [Weight Copy](#weight-copy) ([Auto Weight](#auto-weight) / [Object transfer](#object-transfer))
- [Brushes](#brushes)
- [Cleanup](#cleanup)
- [Display helpers](#display-helpers)
- [Edit Settings / Auto-cleanup reference values](#edit-settings--auto-cleanup-reference-values)
- [Presets, Input & Apply](#presets-input--apply)
- [Special Group Selection / Pick Bone](#special-group-selection--pick-bone)
- [Column State & Visibility](#column-state--visibility-lock--ignore--force-show)
- [Grid Controls & Bottom Tabs](#grid-controls--bottom-tabs)
- [Multi-object editing](#multi-object-editing)
- [Add-on preferences](#add-on-preferences)
- [Shortcuts](#shortcuts)
- [Changes made to the blend file](#changes-made-to-the-blend-file)
- [License and third-party attribution](#license-and-third-party-attribution)

## Features

<p align="center">
  <img width="7600" height="5200" alt="Image" src="https://github.com/user-attachments/assets/d79350fc-493b-4ed0-adac-0435dc3ce42c" />
</p>

- Review and edit weights from the GPU overlay in both Edit Mode and Weight Paint Mode
- Save and restore named weight snapshots
- Pick bones, edit bone transforms, Smooth Weights, Mirror and Apply Rest Pose
- Create bones from selected edges, auto-weight with the generated bones, and split existing bones and weights
- Vertex copy / nearest transfer / object-to-object transfer / vertex-group transfer
- Two automatic weighting methods (Blender built-in / Voxel Heat Skinning)
- Four weight brushes (Normal / Smoothing / Gradient / Lasso)
- Cleanup commands (Normalize, Clean Decimals, Limit Influences, Threshold Cleanup, Fix Violations, Unused, Stepped)
- Display helpers such as bone highlighting and weight-color preview
- Intuitive numeric editing through cells, the slider and presets
- Simultaneous editing of several meshes, with vertex-group selection sync
- A dedicated ToPu Weight Editor area available as a Blender editor type, plus a separate dedicated window
- Japanese / English UI (follows Blender's language setting, or can be forced)

## Requirements

- **Blender 4.2 LTS or newer**
- No additional Python packages (NumPy is used when available, otherwise a scalar fallback)

> On some older CPU / GPU setups, performance can drop when the graphics backend is set to `Vulkan`. Switching to `OpenGL` may improve it.

## Installation

1. Download the distribution ZIP from `Assets` of the latest [release](https://github.com/http4211/ToPu_weight_editor/releases).
2. Drag & drop the ZIP onto the Blender window (or choose `Edit > Preferences > Add-ons > Install from Disk` and select the ZIP).
3. Enable `ToPu:Weight Editor` in the add-on list.

Two icon buttons are then added to the 3D View tool header.

## Opening the editor

<p align="center">
  <img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/15f610fb-c21a-4d02-bc4e-715a7f0f310b" />
</p>
<p align="center">
  <img width="230" height="28" alt="image" src="https://github.com/user-attachments/assets/4303fa20-bf9e-4f50-bdae-3d7d5c8e28ea" />
</p>

- **Tool-header buttons** — the armature icon shows / hides the GPU overlay; the window icon opens / closes the dedicated window.
- **Shortcut** — `Ctrl + W` toggles the overlay; `Ctrl + W` or `Esc` closes it.
- **Editor Type** — choose `ToPu Weight Editor` from the Editor Type selector at the upper-left of any area.

> The tool-header buttons can be hidden with `Show GPU Overlay Button in Tool Header` in the add-on preferences.

### Dedicated area / window

Choosing `ToPu Weight Editor` from the Editor Type selector turns that area into a dedicated weight-editing area. It is stored with its screen / workspace in the `.blend`, and its HUD is restored when the file is opened. The window icon in the tool header can open the same dedicated area in a separate window.

- Operations are the same as the 3D View version. `Clean View` hides the header, toolbar, sidebar and other chrome; click it again to restore.
- Only one HUD is interactive at a time. Another `ToPu Weight Editor` area shows `Make This the Main Area` to adopt the HUD.
- Blender and the OS manage the window size and placement; adjust the HUD size separately with the scale button.
- The viewport display toggles (`Modifier`, `Rest`, `In Front`, `Overlay`, and so on) target the 3D View that opened the dedicated window.

## Quick start

https://github.com/user-attachments/assets/39c5e757-1003-4f13-8ad1-2b021f5474c6

1. Select a mesh that is bound to an armature.
2. Enter Edit Mode or Weight Paint Mode.
3. Select the vertices you want to edit.
4. Open the GPU overlay from the tool-header icon or with `Ctrl + W`.
5. Turn on `Grid Display`.
6. Click a column header to choose the vertex group.
7. Adjust weights with cells, the slider, the value field, presets or brushes.
8. Finish with `Normalize`, `Clean Decimals`, `Threshold Cleanup`, `Limit Influences` and `Fix Violations`.

## GPU overlay / Header row

- `Drag to Move` — moves the overlay.
- `Grid Display` — toggles grid display and realtime update.
- `▣` `↶` `🗑` — save / restore / delete a [weight snapshot](#weight-snapshots).
- `⚙` — opens the add-on preferences.
- `AUTO ×1` — click to cycle `Auto` → `×1` → `×1.5` → `×2`. `Shift + Click` to enter `0.50`–`4.00`.
- `×` — closes the overlay.

> The HUD scale is stored separately for the 3D View and for the dedicated area / window. `Auto` follows Blender's UI scale and the available drawing area.

## Weight snapshots

`▣` `↶` `🗑` in the header row provide temporary weight storage and restoration.

- `▣` — save all weights of the target object under a name.
- `↶` — restore from the list. Object Mode restores the whole target; Edit / Weight Paint Mode restores selected vertices.
- `🗑` — delete a saved snapshot (single or bulk).

The same object with the same vertex count is restored directly by vertex index; a different object or topology uses the saved positions and normals for spatial transfer (interpolation and so on follow the `Object Weight Copy` detail settings).

> Snapshots are compressed and stored inside the `.blend`. Large snapshots increase the file size.

## Bone transform

<img width="532" height="28" alt="Image" src="https://github.com/user-attachments/assets/18661bf8-2ccc-4e3c-9481-de04e75502ae" />

<p align="left">
  <img width="1314" height="756" alt="Image" src="https://github.com/user-attachments/assets/0b5ab8d2-1abd-4378-9fcc-268317d0ef22" />
</p>

When the selected column matches a bone, its `Location`, `Rotation` and `Scale` can be reviewed and edited. Useful for nudging the pose while watching how the weights behave.

- `L` `R` `S` — edit Location / Rotation / Scale. Click a value field to type directly, or horizontal-drag to change (`Shift` for fine steps, `Ctrl` for large steps).
- `↱` — toggles right-drag editing in the viewport. While on, right-dragging changes the current value along the screen direction.
- `↺` — restore the current bone to its original values. `Alt + ↺` restores every changed bone.

## Edit

<p align="left">
  <img width="107" height="114" alt="image" src="https://github.com/user-attachments/assets/c63dd83d-edeb-476b-8a78-c8a682264b16" />
</p>

The `Edit` section holds `x-` / `x+`, plus `Smooth Weights`, `Mirror`, `Bone Creation` and `Apply Rest Pose`.

### Selecting vertices by X side

<img width="53" height="25" alt="Image" src="https://github.com/user-attachments/assets/b50216db-62f4-4d14-b880-35172f970311" />

<p align="left">
  <img width="1304" height="758" alt="Image" src="https://github.com/user-attachments/assets/e224cfe8-1ec2-4d8d-92ce-7dbead312eb4" />
</p>

Selects vertices on the `x-` or `x+` side, using the armature origin (or each object's origin when there is no armature) as the reference.

- Plain click — does not select vertices on the center line.
- `Shift + Click` — also selects the center-line vertices.

### Smooth Weights

<img width="299" height="230" alt="image" src="https://github.com/user-attachments/assets/df0b567d-c156-4139-9d88-2e4b572a6dcd" />

<p align="left">
  <img width="1236" height="764" alt="Image" src="https://github.com/user-attachments/assets/ba09f7df-ebff-4b3c-886e-9c563eec4936" />
</p>

Blends the weights of the selected vertices into their surroundings.

- Plain click — smooths the selected vertices.
- `Shift + Click` — smooths the full weight range of the selected column plus one outer ring.
- `Ctrl + Click` — repairs abnormal weights using the surroundings as the reference.
- `…` — detail settings: range, method (`Fast` / `Surface` / `Volume`), iterations, and the cleanup applied afterwards.

### Mirror

<img width="478" height="454" alt="image" src="https://github.com/user-attachments/assets/ab59df15-6f02-46ab-9c79-0ed322987407" />

<img width="339" height="288" alt="image" src="https://github.com/user-attachments/assets/ba82830e-3339-474e-87a3-989f86abf288" />

<p align="left">
  <img width="1354" height="762" alt="Image" src="https://github.com/user-attachments/assets/f45e4116-7cf0-4867-9eca-9b5b7fdc8ead" />
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
  <img width="458" height="508" alt="image" src="https://github.com/user-attachments/assets/e8583f09-280f-4af6-a9bc-19f993d039c6" />
  <img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/752b69ab-1cc3-4801-9613-42bcd4463eb1" />
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
  <img width="439" height="311" alt="image" src="https://github.com/user-attachments/assets/d02ef477-5d14-4015-a27f-b6a44dc5cc26" />
</p>

`Shift + Click` on `Bone Creation` splits existing bones into connected chains and redistributes each matching vertex-group weight among the resulting bones.

- Target — the selected bones (Pose / Object / Armature Edit Mode), or the bone matching the TPWE active column (Mesh Edit Mode).
- `Split Count` (2–64) and `Smooth` (transition width between split bones, default `0`).
- `Mirror` (on by default) — splits the opposite side with the same settings using the left/right word sets.
- After execution, `F9` can readjust `Split Count`, `Smooth` and `Mirror`.

### Apply Rest Pose

<p align="left">
  <img width="1302" height="768" alt="Image" src="https://github.com/user-attachments/assets/9f61975e-ab08-4fa3-a47d-47aefd04bfdf" />
</p>

Applies the current visual pose as the new rest pose. Action and shape-key retargeting are supported.

> It can modify armature rest data, mesh / shape-key coordinates, Actions and NLA-referenced animation. **Save a backup before running it.**

## Weight Copy

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

## Brushes

<p align="left">
  <img width="187" height="111" alt="image" src="https://github.com/user-attachments/assets/64ef486e-415f-48ef-8e13-97b9cac42136" />
</p>

The overlay can start the add-on's own weight brushes, used directly in the viewport. They work in both Edit Mode and Weight Paint Mode, and bone picking / bone transform stay available while brushing.

- `F` changes the size; `Tab` / `Q` / `Esc` return to the previous tool.
- The tool header exposes size, selection mask and each brush's value.

### Normal brush

<img width="539" height="29" alt="image" src="https://github.com/user-attachments/assets/9d3ade5f-ecc5-4456-babc-703c9596b5ec" />

<p align="left">
  <img width="898" height="764" alt="Image" src="https://github.com/user-attachments/assets/51d508d6-5c53-45cc-88a1-5d793de41f40" />
</p>

The basic brush that adds to or subtracts from the selected column.

- Left-drag adds; `Ctrl + Left-drag` subtracts.
- `Shift + Left-drag` temporarily smooths; `Ctrl + Shift + Left-drag` spreads surrounding influences.
- `Normal Amount` — how much one stroke changes.
- `Constant Paint` — avoids over-layering when the same vertex is hit repeatedly.
- `Stack Paint` — adds/subtracts `Normal Amount` on every touch, building up gradually.

### Smoothing brush

<img width="787" height="29" alt="image" src="https://github.com/user-attachments/assets/47dadabd-d050-464c-95d4-e702ca28b778" />

<p align="left">
  <img width="1268" height="762" alt="Image" src="https://github.com/user-attachments/assets/fe1cc575-10d5-49c8-884a-3b3351182f5a" />
</p>

Blends the selected column with the surrounding vertices. Good for hard paint edges and seams left after mirroring.

- Left-drag smooths the weights around the cursor.
- `Shift + Left-drag` smears like a fingertip; `Ctrl + Left-drag` spreads surrounding influences.
- `Strength` — how far values move toward their neighbours; `Iterations` — how many passes run.
- When an ignored column is selected, only that ignored column is processed.

`Work Mode` switches the behavior.

- `Fast` — processes only the connected edges under the cursor (lightest).
- `Surface` — walks connected topology (does not bleed to the back side).
- `Volume` — also references spatially-near vertices to match local density (`Volume Range` tunes the reach).

### Gradient brush

<img width="707" height="26" alt="image" src="https://github.com/user-attachments/assets/ea890ba2-f618-4a65-98df-af87c8946b0c" />

<p align="left">
  <img width="1234" height="756" alt="Image" src="https://github.com/user-attachments/assets/df2d5bc8-1fbb-4c8d-90ff-31e5a5a0b02a" />
</p>

Builds a weight gradient along the drag direction.

- `Gradient Value` — the maximum weight (the falloff curve runs from this value down to 0).
- Hold `Ctrl` for the subtract direction, `Shift` for the add direction.
- Type — `Linear` (straight) / `Radial` (outward from the start point) / `Line Radial` (spreads from the dragged line).
- `Falloff` — `Linear` / `Smooth` / `Sphere` / `Root` / `Sharp`, or `Custom` (`Custom Exponent` `0.1`–`8`).

### Lasso brush

<img width="407" height="28" alt="image" src="https://github.com/user-attachments/assets/a9f066a5-c5c9-4e4d-9bf8-93cdc9dc093d" />

<p align="left">
  <img width="1154" height="796" alt="Image" src="https://github.com/user-attachments/assets/9c2046e0-adc7-49cd-98e2-7e854064ee5f" />
</p>

Fills an enclosed area with a set value. Good for flattening a wide area to 0 / 0.5 / 1.0 in one action.

- Left-drag to enclose an area; `Lasso Value` is applied inside it.
- Hold `Ctrl` for the subtract direction, `Shift` for the add direction.
- The brush size is used as the width that blends the boundary.

### Selection mask

<p align="left">
  <img width="1208" height="772" alt="Image" src="https://github.com/user-attachments/assets/4c9e47f7-afae-4fa9-9dfe-8d135c61ee2d" />
</p>

Turning `Mask` on restricts the brush to the currently selected vertices. Helps avoid painting nearby parts or back-side vertices by accident. Shared by all brushes.

<p align="center">
  <img src="README_images/brush_tools.gif" alt="Brush tools" width="720">
</p>

## Cleanup

<p align="left">
  <img width="188" height="112" alt="image" src="https://github.com/user-attachments/assets/946e636f-8162-4b77-9f79-58ce49000510" />
</p>

- `Normalize` — normalizes the weight total of the selected vertices to 1.0.
- `Clean Decimals` — rounds weight values to the configured digits.
- `Threshold Cleanup` — zeroes weights at or below the threshold.
- `Limit Influences` — brings each vertex within the maximum influence count.
- `Fix Violations` — applies normalize, decimals, threshold and influence-count settings together.
- `Unused` — deletes unused vertex groups.
- `Stepped` — quantizes weights to a fixed step while keeping each vertex total (`…` sets the step size).

> Reference values come from [Edit Settings / Auto-cleanup reference values](#edit-settings--auto-cleanup-reference-values). Run in Object Mode, these act on every vertex of the object. Editable center-axis L/R pairs that were already equal stay equal.

## Display helpers

<img width="524" height="24" alt="image" src="https://github.com/user-attachments/assets/0b801af1-7993-4ce6-b328-5d2e16eb6020" />

<p align="left">
  <img width="1380" height="980" alt="Image" src="https://github.com/user-attachments/assets/e0581f1f-0fc1-4dc9-8fab-e7d581c1d296" />
</p>

- `Modifier` — toggles the Armature modifier display (pose deformation).
- `Rest` — switches the armature between Pose and Rest Position.
- `In Front` — toggles In Front display for the armatures.
- `Overlay` — toggles Blender's Vertex Group Weights display.
- `Bone Hi` — highlights the bone matching the active vertex group (or the selected column), in Edit / Weight Paint Mode only. Its enabled state is restored on reload.
- `Material` — toggles the weight-color preview. The `…` next to it configures color (hue / saturation / value) and material replacement.

<p align="center">
  <img src="README_images/display_tools.gif" alt="Display helpers" width="720">
</p>

### Weight-color preview

`Material` toggles a preview that shows weights as colors.

- Creates a uniquely named, add-on-owned color attribute (it never overwrites or deletes a same-named user attribute).
- `Replace Materials` (off by default) — only when on does it temporarily replace material slots, restoring them when the preview is disabled. Skipped on shared mesh data.

> The `Material` preview is heavy; constant use is not recommended.

## Edit Settings / Auto-cleanup reference values

<p align="left">
  <img width="512" height="24" alt="image" src="https://github.com/user-attachments/assets/610329e6-337a-4cb1-aea2-13453394c95f" />
</p>

`Normalize`, `Decimals`, `Threshold` and `Influence Count` set the reference values used by the [Cleanup](#cleanup) buttons.

- Checked items are applied automatically whenever the add-on changes a value.
- Use the `−` / `+` buttons, or type into the value field, to change a value.
- The `…` on `Influence Count` opens `Influence Cleanup Settings`.

**Influence Cleanup Settings** (which bones to keep when a vertex exceeds the influence limit)

- `Consider Bone Hierarchy` (default) — keeps influences spread across the separate chains that branch off a shared parent bone (for example the left and right legs splitting from the hip), so a vertex driven by several chains (a skirt influenced by both legs) is less likely to lose one whole chain.
- `Prefer Weight Values` — the ordinary approach: keeps the highest-weighted bones first.
- `Similar Weight Range` — for `Consider Bone Hierarchy`, the weight difference within which bones in the same branch may be reordered. Groups without a hierarchy fall back to `Prefer Weight Values`.

> Automatic cleanup is not guaranteed to catch everything, so running `Fix Violations` as a final check is recommended.

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

## Grid Controls & Bottom Tabs

### Column headers

<p align="center">
  <img width="1346" height="790" alt="Image" src="https://github.com/user-attachments/assets/e5329a73-88bd-48c9-92db-512e42d478b0" />
</p>

- Click — makes it the selected column.
- `Shift + Click` — selects every vertex that has a value in that group.
- `Ctrl + Click` — keeps only the current-selection vertices that have a value in that column.
- Right-click — opens the [weight transfer menu](#column-right-click-weight-transfer).

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

## Multi-object editing

When several meshes are in Edit Mode at once, the grid footer shows the current column, selected-vertex count and a multi-edit indicator (`N obj`), and the vertices of all objects are handled together.

A `Sync Selection` button is also added to `Properties > Object Data > Vertex Groups`; turning it on synchronizes the vertex-group selection across the objects.

## Add-on preferences

Open them with the `⚙` button in the overlay, or from `Edit > Preferences > Add-ons`.

- `Display Language` — `Auto` / `Japanese` / `English` (Auto follows Blender's language setting).
- `Display Settings` — whether the GPU overlay button is shown in the tool header.
- `GPU Overlay UI Scale` — separate scales for the `3D View HUD` and the `Dedicated Area / Window HUD`.
- `GPU Overlay UI Style` — `Slightly Round UI Corners`.
- `GPU Overlay Color Theme` — built-in palettes (20) and user sets; import / export of presets.
- `GPU Overlay Preset Values` — changes the preset button values.
- `Scroll Step` — step sizes for `Ctrl + Wheel` and `Ctrl + Shift + Wheel`.
- `Default Influence Cleanup Method` — `Consider Bone Hierarchy` (default) or `Prefer Weight Values`.
- Left/right word sets — word pairs used to infer left/right names during mirroring.
- `Additional Shortcuts` — Smooth Weights and Pick Influence are off by default; HUD-only bone picking is on.
- `Shortcut Settings` — review and change the registered keymap.
- `Bulk Weight and Mirror Debug` — prints timing and mirror source/destination details to the console.

> `Auto` scale can be turned off to enter a manual value from `0.50` to `4.00`, kept in sync with the HUD scale buttons.

<p align="left">
  <img width="600" height="1113" alt="image" src="https://github.com/user-attachments/assets/f0ac612a-ab84-45df-a610-46dc28a2aa71" />
  <img width="590" height="359" alt="image" src="https://github.com/user-attachments/assets/97659a50-1ff6-46e6-affe-a22991584f30" />
</p>

## Shortcuts

| Action | Default | Initial state |
| --- | --- | --- |
| Show / hide the GPU overlay | `Ctrl + W` | Enabled |
| Close the GPU overlay | `Ctrl + W` / `Esc` | Enabled |
| Add to / subtract from the selected column | `Ctrl + Wheel` | Enabled |
| Fine adjustment of the selected column | `Ctrl + Shift + Wheel` | Enabled |
| Pick a bone while the overlay is open | `Alt + Right Click` | Enabled |
| Smooth Weights | `Ctrl + Alt + S` | Disabled |
| Pick an influence from a bone | `Ctrl + Alt + B` | Disabled |

> Shortcuts can be reviewed and changed in the add-on preferences (except the bone-transform right-drag).

## Changes made to the blend file

The add-on does not access the network, run external programs, or install Python packages. It reads or writes an external file only when you choose `Import Color Preset` or `Export Color Preset`.

Some features intentionally modify the current blend file.

- **Dedicated area / window** — stores the marker and editor type in Screen / Workspace data (no OS window position).
- **Weight snapshots** — compressed and stored in Text datablocks (large ones increase file size).
- **Bone transform** — creates undo data as Text datablocks; obsolete anchors are removed automatically.
- **Bone Creation / Split Bone and Weights** — add bones to an armature and redistribute vertex-group weights.
- **Weight-color preview** — creates an add-on-owned color attribute (materials are only replaced when `Replace Materials` is on).
- **Apply Rest Pose** — may modify rest data, coordinates, Actions and NLA-referenced animation. Back up before applying.
- **Auto Weight** — creates temporary data during calculation and removes it when finished.
- **Object transfer** — can add an Armature modifier to a destination that has none (on by default).

> Bug reports and reproducible test files can be submitted to the [issue tracker](https://github.com/http4211/ToPu_weight_editor/issues).

## License and third-party attribution

The add-on itself is licensed under GPL-3.0-or-later.

- **Robust Weight Inpainting** — based on [RobustSkinWeightsTransferCode](https://github.com/rin-23/RobustSkinWeightsTransferCode) by Rinat Abdrashitov (MIT License), adapted for Blender. It does not bundle or require libigl or Polyscope. The original notice is in `LICENSES/RobustSkinWeightsTransferCode-MIT.txt`.
- **GPU overlay color palettes** — twenty built-in palettes were adapted from user-provided Blender theme extensions. `Blender Dark` / `Blender Light` are based on Blender's standard theme settings. Details are recorded in `LICENSES/BlenderThemePalette-Attributions.txt`.
