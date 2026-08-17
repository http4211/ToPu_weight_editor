# ToPu_weight_editor

<p align="center">
  <img width="611" height="807" alt="image" src="https://github.com/user-attachments/assets/e69834b9-3d6d-47b2-b239-baccc06b948f" />

</p>

<p align="center">
  <a href="README.md">日本語</a> | <b>English</b>
</p>

ToPu_weight_editor (extension name: **ToPu:Weight Editor**) is a Blender add-on for reviewing and editing skin weights.
Based on Softimage-style weight editing, it puts numeric weight editing, normalization, cleanup, smoothing, mirroring, copy & paste, transfer, bone picking, bone creation, and display helpers into a single **GPU overlay** drawn directly in the 3D View.

No external UI framework or extra Python package is used. The add-on runs with Blender's built-in GPU drawing and Blender-native areas/windows.

> **This document describes version 1.5.121.**
> The legacy N-panel (sidebar) and the quick Pie Menu that existed up to the 1.4 series have been removed; all operations now live in the GPU overlay.
> The overlay shortcut also changed from `W` to `Ctrl + W`.

---

## Table of contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Opening the editor](#opening-the-editor)
- [Quick start](#quick-start)
- [GPU overlay](#gpu-overlay)
  - [Header row](#header-row)
- [Weight snapshots](#weight-snapshots)
- [Bone transform](#bone-transform)
- [Edit](#edit)
  - [Bone Creation](#bone-creation)
- [Weight Copy](#weight-copy)
- [Brushes](#brushes)
- [Cleanup](#cleanup)
- [Display helpers](#display-helpers)
- [Edit Settings](#edit-settings)
- [Presets, Input & Apply](#presets-input--apply)
- [Special Group Selection](#special-group-selection)
- [Column State & Visibility](#column-state--visibility)
- [Grid Controls & Bottom Tabs](#grid-controls--bottom-tabs)
- [Weight-color preview](#weight-color-preview)
- [Multi-object editing](#multi-object-editing)
- [Dedicated area / Weight Editor window](#dedicated-area--weight-editor-window)
- [Add-on preferences](#add-on-preferences)
- [Shortcuts](#shortcuts)
- [Changes made to the blend file](#changes-made-to-the-blend-file)
- [License and third-party attribution](#license-and-third-party-attribution)

---

## Features

<p align="center">
  <img width="7600" height="5200" alt="Image" src="https://github.com/user-attachments/assets/dff69772-33ea-47ba-b2e9-2990c6e058fb" />
</p>


- Review and edit weights from the GPU overlay in both Edit Mode and Weight Paint Mode
- Save and restore named weight snapshots inside the blend file
- Pick bones and edit bone transforms
- Smooth Weights, Mirror, Bone Creation and Apply Rest Pose
- Create a bone chain from selected edge loops or an edge ring, then readjust its count and direction with `F9`
- Vertex copy/paste, nearest transfer, object-to-object transfer and vertex-group transfer
- Two automatic weighting methods: Blender's built-in automatic weights and a dedicated voxel diffusion method (Voxel Heat Skinning)
- Four dedicated weight brushes: Normal, Smoothing, Gradient and Lasso
- Normalize, Clean Decimals, Limit Influences, Threshold Cleanup, Fix Violations, Unused cleanup and Stepped
- Bone highlighting, weight-color preview and display-helper toggles
- Intuitive numeric editing through cells, the slider and presets
- List selected vertices in a lightweight cell grid and adjust values while watching the 3D View
- Simultaneous editing of several meshes, with vertex-group selection sync
- A **ToPu Weight Editor area** available as a Blender editor type, plus a **dedicated Weight Editor window** separate from the 3D View
- Japanese / English UI (follows Blender's language setting, or can be forced)

---
## Requirements

- **Blender 4.2 LTS or newer**

No additional Python packages need to be installed. The add-on only uses modules bundled with Blender.
NumPy is used when Blender provides it; otherwise a main-thread scalar fallback is used. Voxel Heat's dense NumPy path has an estimated 384 MiB working-memory limit and switches to the lower-memory scalar path if the limit or an allocation is exceeded.

On some older CPU/GPU setups, performance can drop when Blender's graphics backend is set to `Vulkan`.
Switching the backend to `OpenGL` may improve it.

---
## Installation

### 1. Download

[**⬇ Download ToPu Weight Editor (GitHub Releases)**](https://github.com/http4211/ToPu_weight_editor/releases)

Open the Releases page and download the distribution ZIP from `Assets` under the latest version.

### 2. Install the ZIP

Open `Edit > Preferences > Add-ons`, choose `Install from Disk`, and select the distributed ZIP.

### 3. Enable the add-on

Enable `ToPu:Weight Editor` in the add-on list.
Two icon buttons are then added to the 3D View tool header.

---
## Opening the editor
<p align="center">
  <img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/15f610fb-c21a-4d02-bc4e-715a7f0f310b" />
</p>
<p align="center">
  <img width="230" height="28" alt="image" src="https://github.com/user-attachments/assets/4303fa20-bf9e-4f50-bdae-3d7d5c8e28ea" />
</p>

### From the tool header

| Button | Action |
| --- | --- |
| Armature icon | Show / hide the GPU overlay in the 3D View |
| Window icon | Open / close the dedicated Weight Editor window |


The tool-header buttons can be hidden with `Show GPU Overlay Button in Tool Header` in the add-on preferences.

### By switching an area

You can also start the editor by changing any Blender area to the dedicated `ToPu Weight Editor` editor type.

1. Open the **Editor Type** selector at the upper-left of any area.
2. Choose `ToPu Weight Editor` from the editor list.
3. If the HUD is already active somewhere else, click `Make This the Main Area` in the new area.

The converted area is stored with its screen/workspace in the `.blend`. To restore the previous editor, use the same Editor Type selector and choose the 3D View or another editor.

### With the shortcut

`Ctrl + W` toggles the GPU overlay by default.
Use `Ctrl + W` or `Esc` to close it.

---
## Quick start

https://github.com/user-attachments/assets/39c5e757-1003-4f13-8ad1-2b021f5474c6

1. Select a mesh that is bound to an armature.
2. Enter Edit Mode or Weight Paint Mode.
3. Select the vertices you want to edit.
4. Open the GPU overlay from the tool-header icon, with `Ctrl + W`, or by switching an area to `ToPu Weight Editor`.
5. Turn on `Grid Display` in the overlay.
6. Click a column header to choose the vertex group to edit.
7. Adjust weights with cells, the slider, the value field, preset buttons or brushes.
8. Finish with `Normalize`, `Clean Decimals`, `Threshold Cleanup`, `Limit Influences` or `Fix Violations`.

---
## GPU overlay

### Header row

| Control | Action |
| --- | --- |
| `Drag to Move` | Drag to move the GPU overlay. |
| `Grid Display` | Toggles grid display and realtime update together. |
| `▣` | Save all weights of the target object under a name. |
| `↶` | Restore all weights of the target object from a saved snapshot. |
| `🗑` | Delete an unnecessary saved snapshot from the list. |
| `⚙` | Open this add-on's preferences. |
| `AUTO ×1` | Cycles `Auto` → `×1` → `×1.5` → `×2`. `Shift + Click` lets you enter a custom scale from `0.50` to `4.00`. |
| `×` | Close the GPU overlay. |

The 3D View HUD scale and the dedicated area/window HUD scale are stored separately and reused the next time each HUD opens. `Auto` follows Blender's UI scale and the available drawing area.

<!-- Screenshot: header row (move handle through close button) -->
## Weight snapshots

`▣`, `↶` and `🗑` in the header row provide temporary weight storage and restoration.

- `▣` — save all weights of the current target object under a name.
- `↶` — restore all weights of the target object from a saved snapshot.
- `🗑` — delete an unnecessary saved snapshot; single and bulk deletion are both supported.

Snapshots are compressed and stored in Blender Text datablocks inside the blend file.
Large snapshots increase the `.blend` file size.
Restoring requires the vertex count to match the count at save time.

<!-- Screenshot: snapshot save / restore dialogs -->

---
## Bone transform

<img width="532" height="28" alt="Image" src="https://github.com/user-attachments/assets/18661bf8-2ccc-4e3c-9481-de04e75502ae" />

<p align="left">
  <img width="1314" height="756" alt="Image" src="https://github.com/user-attachments/assets/0b5ab8d2-1abd-4378-9fcc-268317d0ef22" />
</p>

When the selected column matches a bone, its `Location`, `Rotation` and `Scale` can be reviewed and edited from the overlay.

- `↱` — toggles right-drag editing in the viewport. While it is on, right-dragging in the viewport changes the current bone transform value along the screen direction.
  - Hold `Shift` while dragging for fine adjustment, `Ctrl` for larger steps.
  - Useful for nudging the pose while watching how the weights behave.
- `L` — edit Location.
- `R` — edit Rotation.
- `S` — edit Scale.
- Click a value field to type directly. Horizontal drag also changes the value; `Shift + Drag` for fine steps, `Ctrl + Drag` for large steps.
- `↺` — restore the current bone to its original values. `Alt + ↺` restores every bone that was changed.

---
## Edit

<p align="left">
  <img width="107" height="114" alt="image" src="https://github.com/user-attachments/assets/c63dd83d-edeb-476b-8a78-c8a682264b16" />
</p>

The `Edit` section holds `x-` / `x+` on its title row, plus `Smooth Weights`, `Mirror`, `Bone Creation` and `Apply Rest Pose`.

### Selecting vertices by X side

<img width="53" height="25" alt="Image" src="https://github.com/user-attachments/assets/b50216db-62f4-4d14-b880-35172f970311" />

<p align="left">
  <img width="1304" height="758" alt="Image" src="https://github.com/user-attachments/assets/e224cfe8-1ec2-4d8d-92ce-7dbead312eb4" />
</p>

Selects vertices on the `x-` or `x+` side, using the armature origin as the reference.
Without an armature, each object's own origin is used.

- A plain click does not select vertices on the center line.
- `Shift + Click` selects the vertices on the center line.

### Smooth Weights

<img width="299" height="230" alt="image" src="https://github.com/user-attachments/assets/df0b567d-c156-4139-9d88-2e4b572a6dcd" />

<p align="left">
  <img width="1236" height="764" alt="Image" src="https://github.com/user-attachments/assets/ba09f7df-ebff-4b3c-886e-9c563eec4936" />
</p>

Blends the weights of the selected vertices into their surroundings.

- Plain click — smooths the selected vertices.
- `Shift + Click` — automatically smooths the full weight range of the selected column plus one outer ring. The detail settings can limit this to selected vertices only.
- `Ctrl + Click` — repairs abnormal weights using the unselected surroundings as the reference. `Ctrl` takes priority.
- The `…` next to it opens the detail settings: range, method, iterations, and the cleanup applied afterwards.
- The method can be `Fast`, `Surface` or `Volume`.

### Mirror

<img width="478" height="454" alt="image" src="https://github.com/user-attachments/assets/ab59df15-6f02-46ab-9c79-0ed322987407" />

<img width="339" height="288" alt="image" src="https://github.com/user-attachments/assets/ba82830e-3339-474e-87a3-989f86abf288" />

<p align="left">
  <img width="1354" height="762" alt="Image" src="https://github.com/user-attachments/assets/f45e4116-7cf0-4867-9eca-9b5b7fdc8ead" />
</p>

Looks up the mirrored position of the selected vertices and brings the weights over from the opposite side.
Left/right names such as `_L` / `_R` are swapped as well, and the L/R weights of center vertices are balanced.

- `Ctrl + Click` — opens the direction and whole-object mirror settings.
- The `…` next to it opens the detail settings: mirror direction, reference space, search distance, center tolerance and the left/right word sets.
- With direction set to `Auto`, Edit Mode uses the side of the actual mesh selection. If both sides are selected or the side cannot be determined, it does not use the active vertex or selection counts; it uses the direction in Mirror Details.
- If the direction in Mirror Details is itself `Auto`, a mixed-side selection keeps the established per-destination-vertex Auto behavior.
- On asymmetric geometry, adaptive matching can project the reflected position onto the source surface and interpolate the nearby triangle's weights. Exact symmetric points keep the fast nearest-vertex path, and adaptive matching can be disabled in the details.
- `Balance Center L/R Weights` is on by default. Turning it off skips only center-vertex averaging.
- Left/right word sets can also be configured in the add-on preferences.
- Whole-object mirroring has a selected-only option.

#### Center L/R Balancing

With the default settings, selected-vertex and whole-object mirroring automatically balance the L/R weights of vertices on the center axis. Turn off `Balance Center L/R Weights` in Mirror Details to skip only that balancing step.

`Normalize`, `Clean Decimals`, `Threshold Cleanup`, `Limit Influences` and `Fix Violations` preserve an editable center-axis L/R pair when it was equal before the operation. Intentionally asymmetric pairs remain asymmetric. Decimal rounding and influence-limit selection treat an equal L/R pair as one symmetric unit.

### Bone Creation

<p align="left">
  <img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/752b69ab-1cc3-4801-9613-42bcd4463eb1" />
</p>

`Bone Creation` creates a bone chain from edge loops or an edge ring selected in Mesh Edit Mode.

- A regular click analyzes the selected edges and opens a confirmation dialog before creating anything.
- The confirmation dialog lets you review or change the bone count, target, bone name, connection, deform use, roll reference, post-creation mode and `Reverse Direction`.
- `Shift + Click` opens `Bone Creation Settings`, where you can set the generation method, automatic or fixed bone count, and a new or existing target armature.
- It supports multiple closed loops, open edge paths, a single loop's normal direction and chains through edge-ring centers.
- After creation, use the `F9` panel to readjust the bone count and `Reverse Direction`.

### Apply Rest Pose

<p align="left">
  <img width="1302" height="768" alt="Image" src="https://github.com/user-attachments/assets/9f61975e-ab08-4fa3-a47d-47aefd04bfdf" />
</p>

`Apply Rest Pose` applies the current visual pose as the new rest pose.

- Use it after adjusting bone placement, when that state should become the new rest pose.
- Action and shape-key retargeting are supported.
- It can modify armature rest data, mesh and shape-key coordinates, Actions and NLA-referenced animation.
- **Save a backup before running it,** and review the confirmation dialog.

---
## Weight Copy

<img width="189" height="113" alt="image" src="https://github.com/user-attachments/assets/7dffb678-b146-43cb-9fb5-e6b892af89b1" />


<p align="left">
  <img width="1042" height="770" alt="Image" src="https://github.com/user-attachments/assets/b8453e66-c226-46db-b887-b2e01a3a3042" />
</p>

| Button | Action |
| --- | --- |
| `Vtx Copy` | Copies the weights of the single active vertex. |
| `Vtx Paste` | Pastes the copied vertex weights onto the selected vertices. |
| `Near Copy` | Stores the positions and weights of the selected vertices as the nearest-paste source. |
| `Near Paste` | Pastes, for each selected vertex, the weights of the closest stored vertex. |
| `Auto Weight` | Binds the selected meshes to an armature and assigns automatic weights. |
| `Obj Xfer` | Transfers weights from the active mesh to the other selected meshes using the saved settings. |

The `…` next to `Auto Weight` and `Obj Xfer` opens their respective detail settings.

### S / T buttons (column transfer)

`S` and `T` on the right of the section title are transfer shortcuts for the current column.

- `S` — registers the current column as the transfer source. Its color changes while a source is registered.
- `T` — transfers from the registered source into the current column.
- `Shift + T` — opens the `Multi Weight Transfer` dialog, pre-filled with the registered source and the current column.

### Object transfer

Transfers weights from the object selected last (the active one) to the other selected objects.
Because it transfers per face rather than per vertex, results stay relatively clean even on low-poly meshes — at the cost of a heavier computation.

The detail settings cover method, interpolation, Robust inpainting and finishing options.
`Robust Weight Inpainting` fills in unmatched areas during the transfer.
`Clothing Inner-Side Mode` uses source normals and a bounded distance to prioritize inner-shell candidates, then fills unmatched areas from destination topology. `Near Paste` also uses the saved Object Weight Copy interpolation, distance and clothing-inner settings.

If a destination has no Armature modifier, one can be added automatically (on by default; it can be disabled in the Object Weight Copy settings).

### Auto Weight

<img width="576" height="310" alt="image" src="https://github.com/user-attachments/assets/08be9571-5c7e-44ce-b7a9-0c6531d67393" />

<img width="433" height="326" alt="image" src="https://github.com/user-attachments/assets/7634218e-d086-4b3c-a080-26a5ac5cfca1" />

`Auto Weight` binds the selected meshes to an armature and assigns automatic weights.
It can keep existing parent relationships, and linked objects can be localized automatically.
It can also weight only the part covered by the current vertex selection.

The detail settings switch between Blender's built-in automatic weights and the dedicated voxel diffusion method (Voxel Heat Skinning).

**Main Voxel Heat Skinning settings**

| Item | Description |
| --- | --- |
| `Voxel Heat Resolution` | Number of voxels along the longest axis. Higher values preserve more detail but increase processing time and memory use. |
| `Diffuse Loops` | Total diffusion passes are resolution × loops. Higher values propagate heat more smoothly but take longer. |
| `Occupied Cell Dilation` | Expands surface voxels to prevent broken propagation on thin outfits and non-watertight meshes. Set it to `0` if weights leak across touching parts. |
| `Diffuse Falloff` | Higher values reduce distant-bone contribution more strongly, producing tighter and more local weights. |
| `Distance Falloff` | Controls how sharply voxel distance is converted into initial heat. Higher values favor nearby bones more strongly. |
| `Detect Solidify` | Gives thin outfits and shells volume. When enabled, occupied-cell dilation is at least 1 and all bones must be inside the character volume. |
| `Solid Votes` | Number of axis-inside tests required to classify an interior cell. `2` is majority voting, `1` is broader and `3` is stricter. |
| `Maximum Influences` | Maximum number of bones assigned to one vertex. The default is `4`. |
| `Smoothing` / `Smoothing Passes` | Smooths boundaries along real mesh edges after automatic weighting. The defaults are ON and `5` passes; higher values spread the blend farther. |
| `Range Proxy (Object)` | Uses visible meshes only to correct occupied cells, radii and calculation range. Weights are still written only to selected meshes. The default is OFF. |
| `Range Proxy (Edit)` | For partial weighting, uses unselected vertices and meshes sharing the armature as calculation proxies. Weights are still written only to selected vertices. The default is ON. |

Voxel Heat Skinning generates weights from a volumetric voxel distance field and heat diffusion, with guards that suppress leakage into nearby parts. Processing time depends especially on resolution, `Diffuse Loops`, occupied-cell dilation and target vertex count, and Blender may remain unavailable until the operation finishes.

**Use Specified Bones Only**

When `Use Specified Bones Only` is on, automatic weighting is restricted to the saved bone list.

- The same list applies to both Blender's built-in automatic weights and Voxel Heat Skinning, in Object Mode and Edit Mode.
- `Get Selected Bones` captures the bone selection from Edit, Pose or Object Mode.
- `All` / `None` buttons and a compact bone checklist let you adjust the list.
- Explicitly selected bones override deform-bone and excluded-keyword filtering.

---
## Brushes

<p align="left">
  <img width="187" height="111" alt="image" src="https://github.com/user-attachments/assets/64ef486e-415f-48ef-8e13-97b9cac42136" />
</p>

The overlay can start the add-on's own weight brushes, used directly in the viewport.
They work in both Edit Mode and Weight Paint Mode.
Bone picking and bone transform stay available while brushing, which keeps weighting work fast.

While a brush is active, `F` changes the size and `Tab` / `Q` / `Esc` return to the previous tool.
The tool header exposes size, selection mask, normal amount, smoothing strength, gradient value, lasso value and more.

### Normal brush

<img width="539" height="29" alt="image" src="https://github.com/user-attachments/assets/9d3ade5f-ecc5-4456-babc-703c9596b5ec" />

<p align="left">
  <img width="898" height="764" alt="Image" src="https://github.com/user-attachments/assets/51d508d6-5c53-45cc-88a1-5d793de41f40" />
</p>

`Normal` is the basic brush that adds to or subtracts from the selected column.

- Left-drag adds to the selected column.
- `Ctrl + Left-drag` subtracts.
- `Shift + Left-drag` temporarily smooths instead.
- `Ctrl + Shift + Left-drag` spreads surrounding influences.
- `Normal Amount` sets how much one stroke changes.
- `Constant Paint` — avoids over-layering when the same vertex is hit repeatedly during one drag. Good for adding a precise amount.
- `Stack Paint` — adds/subtracts `Normal Amount` every time the brush touches a vertex. Good for building up gradually.

### Smoothing brush

<img width="787" height="29" alt="image" src="https://github.com/user-attachments/assets/47dadabd-d050-464c-95d4-e702ca28b778" />

<p align="left">
  <img width="1268" height="762" alt="Image" src="https://github.com/user-attachments/assets/fe1cc575-10d5-49c8-884a-3b3351182f5a" />
</p>

`Smoothing` blends the selected column with the surrounding vertices.

- Left-drag smooths the weights around the cursor.
- `Shift + Left-drag` smears the weights like a fingertip tool.
- `Ctrl + Left-drag` spreads surrounding influences. `Ctrl` takes priority.
- `Strength` controls how far values move toward their neighbours.
- `Iterations` controls how many smoothing passes run.
- When an ignored column is selected, only that ignored column is processed.
- Good for hard paint edges, steps, and seams left after mirroring.

### Gradient brush

<img width="707" height="26" alt="image" src="https://github.com/user-attachments/assets/ea890ba2-f618-4a65-98df-af87c8946b0c" />

<p align="left">
  <img width="1234" height="756" alt="Image" src="https://github.com/user-attachments/assets/df2d5bc8-1fbb-4c8d-90ff-31e5a5a0b02a" />
</p>

`Gradient` builds a weight gradient along the drag direction.

- Weights in the selected column change from the drag start point toward the end point.
- `Gradient Value` sets the maximum weight; the falloff curve runs from this value down to 0.
- Hold `Ctrl` to work in the subtract direction, `Shift` in the add direction.
- `Linear` — a straight 1-to-0 gradient along the drag direction.
- `Radial` — radiates outward from the drag start point, getting weaker with distance.
- `Line Radial` — spreads out from the dragged line, perpendicular to it.
- `Falloff` switches how the value drops: `Linear` is even, `Smooth` is a natural S-curve, `Sphere` is softer, `Root` widens the start side, `Sharp` drops steeply from the start.
- With `Custom` falloff, `Custom Exponent` tunes the curve between `0.1` and `8`. `1` is linear, `2` and above fall off sharply, below `1` is gentler.

### Lasso brush

<img width="407" height="28" alt="image" src="https://github.com/user-attachments/assets/a9f066a5-c5c9-4e4d-9bf8-93cdc9dc093d" />

<p align="left">
  <img width="1154" height="796" alt="Image" src="https://github.com/user-attachments/assets/9c2046e0-adc7-49cd-98e2-7e854064ee5f" />
</p>

`Lasso` fills an enclosed area with a set value.

- Left-drag to enclose an area; `Lasso Value` is applied inside it.
- Hold `Ctrl` for the subtract direction, `Shift` for the add direction.
- The brush size is used as the width that blends the boundary of the area.
- Good for flattening a wide area to 0, 0.5 or 1.0 in one action.

### Selection mask

<p align="left">
  <img width="1208" height="772" alt="Image" src="https://github.com/user-attachments/assets/4c9e47f7-afae-4fa9-9dfe-8d135c61ee2d" />
</p>

Turning `Mask` on restricts the brush to the currently selected vertices.

- Helps avoid painting nearby parts or vertices on the back side by accident.
- Selecting only the vertices you want to edit before turning it on keeps the working area stable.
- Shared by the Normal, Smoothing, Gradient and Lasso brushes.

<p align="center">
  <img src="README_images/brush_tools.gif" alt="Brush tools" width="720">
</p>

---
## Cleanup

<p align="left">
  <img width="188" height="112" alt="image" src="https://github.com/user-attachments/assets/946e636f-8162-4b77-9f79-58ce49000510" />
</p>

| Button | Action |
| --- | --- |
| `Normalize` | Normalizes the weight total of the selected vertices to 1.0. |
| `Clean Decimals` | Rounds weight values to the configured number of digits. |
| `Threshold Cleanup` | Zeroes weights at or below the threshold. |
| `Limit Influences` | Brings each vertex within the maximum influence count. |
| `Fix Violations` | Applies normalize, decimals, threshold and influence-count settings together. |
| `Unused` | Deletes unused vertex groups. |
| `Stepped` | Quantizes weights to a fixed step while keeping each vertex total. Remainders that do not fit the step are left on editable influences. |

- The `…` next to `Stepped` sets the step size.
- Run in Object Mode, these act on every vertex of the object.
- They preserve editable center-axis L/R pairs that were already equal; intentionally asymmetric pairs remain asymmetric.

The reference values come from [Auto-cleanup reference values](#auto-cleanup-reference-values).

---
## Display helpers

<img width="524" height="24" alt="image" src="https://github.com/user-attachments/assets/0b801af1-7993-4ce6-b328-5d2e16eb6020" />

<p align="left">
  <img width="1380" height="980" alt="Image" src="https://github.com/user-attachments/assets/e0581f1f-0fc1-4dc9-8fab-e7d581c1d296" />
</p>

- `Modifier` — toggles the Armature modifier display (pose deformation) of the target mesh.
- `Rest` — switches the target armature between Pose Position and Rest Position.
- `In Front` — toggles In Front display for the armatures related to the target mesh.
- `Overlay` — toggles Blender's Vertex Group Weights display.
- `Bone Hi` — highlights the bone matching the selected column with the add-on's own overlay, in Edit and Weight Paint Mode only.
- `Material` — toggles the [weight-color preview](#weight-color-preview).
- The `…` next to `Material` opens the preview's color and material-replacement settings.

<p align="center">
  <img src="README_images/display_tools.gif" alt="Display helpers" width="720">
</p>

---
## Edit Settings

### Auto-cleanup reference values

<p align="left">
  <img width="512" height="24" alt="image" src="https://github.com/user-attachments/assets/610329e6-337a-4cb1-aea2-13453394c95f" />
</p>

`Normalize`, `Decimals`, `Threshold` and `Influence Count`. The values set here are the reference used by the [Cleanup](#cleanup) buttons.

- Checked items are applied automatically whenever the add-on changes a value.
- Use the `−` / `+` buttons, or type into the value field, to change the reference value.

> Automatic cleanup is not guaranteed to catch everything, so running `Fix Violations` as a final check is recommended.

---
## Presets, Input & Apply

### Preset buttons

<img width="492" height="101" alt="image" src="https://github.com/user-attachments/assets/11f48284-8a22-4133-b3e9-a97db0e69445" />

<img width="280" height="28" alt="Image" src="https://github.com/user-attachments/assets/463b655c-5b92-4641-89bd-a3abeff80b92" />

<p align="left">
  <img width="1188" height="764" alt="Image" src="https://github.com/user-attachments/assets/df656172-edbc-4420-9059-4b3932b18cf3" />
</p>

Applies `0`, `0.1`, `0.25`, `0.5`, `0.75`, `0.9` or `1` in one click.
In `Add` / `Add%` mode, `Shift + Click` applies the negative value.

Preset values can be changed in the add-on preferences.
### Input mode, slider and value field

<img width="494" height="158" alt="image" src="https://github.com/user-attachments/assets/c3a9a157-9ab5-4a09-a081-183b39b28a99" />

<img width="693" height="37" alt="Image" src="https://github.com/user-attachments/assets/56fd28a7-e82b-4c60-a4ee-034649542502" />

<p align="left">
  <img width="1188" height="756" alt="Image" src="https://github.com/user-attachments/assets/e0c3594f-f8f7-43d0-a298-a64aca7c210e" />
</p>

The leftmost button cycles the input mode through `ABS` → `ADD` → `ADD%`.

- `Abs` — replaces the value with the entered one.
- `Add` — adds to the current value. Negative values subtract.
- `Add%` — adds a percentage of the current value.

Usage:

- Dragging the slider normally applies values to the target in real time. With **10,000 or more target vertices**, only the displayed value and handle update during the drag; the weights are committed when the slider is released and confirmed.
- Click the value field to type a value from the keyboard.
- Scroll the wheel over the value field to nudge the value.
- `Apply` applies the value field to the current column of the selected vertices.
- `⟳` rebuilds the grid manually from the current selection and weights — useful after special selection commands.
- `Ctrl + Wheel` adds to / subtracts from the selected column on the selected vertices (independent of the slider mode).
- `Ctrl + Shift + Wheel` does the same in finer steps.
- The wheel step sizes can be changed in the add-on preferences.
## Special Group Selection

### Pick Bone / follow the peak column

<img width="338" height="197" alt="image" src="https://github.com/user-attachments/assets/3f38bdb8-8fc5-48c9-ae62-89f9627bb8ee" />

<img width="109" height="24" alt="Image" src="https://github.com/user-attachments/assets/3257c432-2a43-482e-8eef-dddd109b300b" />

<p align="left">
  <img width="1218" height="758" alt="Image" src="https://github.com/user-attachments/assets/4324d885-a267-470a-b215-f4b7ef63ed39" />
</p>

`Pick Bone` lets you click a bone in the viewport to select the vertex-group column with that bone's name.

- While the GPU overlay is open, `Alt + Right Click` also starts bone picking by default.
- `Shift + Click` on the `Pick Bone` button toggles that `Alt + Right Click` shortcut on and off.
- The `…` button next to it opens the excluded-word and shortcut settings. Excluded words keep bones containing `IK`, `FK`, `twist` and similar out of the pick candidates.
- Bones hidden through Bone Collections are also excluded. Bones matching the excluded words are temporarily hidden only while the picker is active, then restored exactly after confirm or cancel.

When `▣↖` is on, changing the vertex selection automatically selects the vertex-group column with the highest weight in that selection.
This suits workflows where you switch vertices often to check the dominant influence bone.

<p align="center">
  <img src="README_images/bone_pick.gif" alt="Bone picking" width="720">
</p>

---
## Column State & Visibility

### Lock / Ignore / Force Show

<img width="157" height="28" alt="image" src="https://github.com/user-attachments/assets/1abf4eb8-5e6b-46e5-8fb4-13e5b1e48628" />

<img width="399" height="195" alt="image" src="https://github.com/user-attachments/assets/997d4dac-03f2-4866-a578-2b15df0007d8" />


<p align="left">
  <img width="1192" height="766" alt="Image" src="https://github.com/user-attachments/assets/5d1c7790-e614-45b6-8d47-9243c6fb875a" />
</p>

- `Lock` — makes the selected column non-editable.
- `Ignore` — excludes the column from totals, normalization and cleanup. On the `Other` tab this is handled as an Other-specific ignore state.
- `Force Show` — keeps a column in the grid even when its weights are zero.
- `Shift + Click` applies the action to every column except the selected one.
- `Ctrl + Force Show` opens a text filter. Comma-separated fragments force-show every partially matching group, while columns force-shown manually stay enabled.
- `Alt + Click` clears the state everywhere.
## Grid Controls & Bottom Tabs

### Weight grid

**Column headers**

<p align="center">
  <img width="1346" height="790" alt="Image" src="https://github.com/user-attachments/assets/e5329a73-88bd-48c9-92db-512e42d478b0" />
</p>

- Click a column header to make it the selected column.
- `Shift + Click` selects every vertex that has a value in that vertex group.
- `Ctrl + Click` keeps only the vertices that have a value in that column, out of the current selection.
- Right-click a column header to open the [weight transfer menu](#column-right-click-weight-transfer).

**L / Vertex / Sum**

<img width="111" height="33" alt="image" src="https://github.com/user-attachments/assets/7af6fa19-7275-46ae-972a-25e2ab45ceb2" />

<p align="center">
  <img width="1192" height="762" alt="Image" src="https://github.com/user-attachments/assets/1f944500-6102-4533-915b-c1667d87732d" />
</p>

| Header | Click | Modifier |
| --- | --- | --- |
| `L` | Weight-lock the target vertices. | `Alt + Click` unlocks |
| `Vertex` | Grid-select the displayed rows. | `Alt + Click` clears |
| `Sum` | Toggle **violation-only view**. | `Shift + Click` selects the vertices currently shown in the grid |

- Clicking a row's `L` cell toggles the weight lock for that vertex. Drag to toggle several vertices at once.
- Clicking a row's `Vertex` cell highlights that vertex row in the viewport and keeps it visible in the grid.
- Hold `Shift` / `Ctrl` while clicking or dragging to add to or remove from the row selection.
- When some vertices have a total-value or influence-count problem, the `Sum` header changes to `Sum ⚠`. While violation-only view is active it reads `Viol. Only`.
- Violation-only view covers violations across every page, not just the current one.
- In violation-only view, the `Vertex` and `L` header actions also target only the displayed violation vertices.

**Cells**

<p align="center">
  <img width="1184" height="758" alt="Image" src="https://github.com/user-attachments/assets/d40e61e9-ae42-4cf0-b916-46545d88c886" />
</p>

- Click a cell to type its value directly. `Enter` confirms; `Right-click` cancels and clears the cell selection.
- Starting the input with `+` `-` `*` `/` makes it a relative operation on the current value (for example `*0.5` or `+0.1`).
- With several cells selected, the entered value is applied to all of them at once.
- Drag across cells to select a range. `Shift + Drag` adds to the selection, `Ctrl + Drag` removes from it.
- While a cell selection remains, every value-changing operation—including the slider, wheel adjustment, presets and `Apply`—prioritizes the selected cells over the live mesh selection.
- Cell selections survive paging, scrolling, visible row/column-count changes and selected-column changes. They become invalid when the actual mesh vertex-selection scope changes.
- Right-clicking an empty part of the grid clears the remaining cell selection. A left click is consumed as a grid-background action and does not pass through to the 3D View.

<p align="center">
  <img src="README_images/cell_edit.gif" alt="Cell editing" width="720">
</p>

### Column tabs

<p align="left">

  <img width="562" height="31" alt="image" src="https://github.com/user-attachments/assets/9a6f941e-05c7-4855-812e-7f618001c662" />
  
  <img width="1186" height="764" alt="Image" src="https://github.com/user-attachments/assets/153b50ac-3af7-404e-9795-18da04257bc9" />
</p>

The tabs below the grid choose which columns are shown.

- `All` — bone columns and non-bone vertex-group columns.
- `Deform` — only deform vertex groups whose names match a bone.
- `Other` — only non-bone vertex groups that do not match a bone name.

Per-tab options:

- `Ignore Non-Bone Columns` — an `All` tab option. Automatically marks non-bone vertex groups as ignored so they stay out of totals, normalization and cleanup.
- `Always Show` — an `Other` tab option. Always shows existing non-bone vertex-group columns even when the selected vertices contain no values for them.
- `Allow >1` — an `Other` tab option. When on, Other columns are not treated as violations when their total is 1 or more, and they are not normalized even when Normalize is on.
- `Hidden Words` — hides specified words from the group-name display in the grid to make names shorter. Actual vertex group names are not changed.
### Column right-click weight transfer

<p align="left">
  
  <img width="515" height="246" alt="image" src="https://github.com/user-attachments/assets/08b1ca77-55aa-438a-bb2d-dab1ee1afd59" />

  <img width="577" height="835" alt="image" src="https://github.com/user-attachments/assets/a38e5d23-7c4a-4102-971a-b54873d67845" />

</p>


Right-clicking a column header in the GPU overlay opens the vertex-group transfer menu.

- `Set as Transfer Source` — makes the right-clicked column the transfer source.
- `Transfer to This Column` — transfers from the registered source into the current column.
- `Multi Weight Transfer` — transfer with explicit source, destination, method and scope.
- Methods include `Copy`, `Move` and `Replace`.
- The scope can be the whole group or only the selected vertices.
- Several pairs can be registered and transferred together with the same method.

When opened from the dedicated Weight Editor window, the menu belongs to that window.

---
## Weight-color preview

`Material` in the display helper row toggles a preview that shows weights as colors.
The `…` next to it configures hue / saturation / value and whether materials are replaced.

- The preview creates a uniquely named, add-on-owned color attribute. It never overwrites or deletes a same-named user attribute.
- `Replace Materials` is off by default. When explicitly enabled, it may temporarily replace material slots, and it restores the slot order, DATA/OBJECT links, per-object overrides, the active slot and per-face material assignments when the preview is disabled.
- On a mesh datablock shared by several objects, material replacement is skipped and viewport color display is used instead, so the other objects are not changed.

> The `Material` preview is heavy; it is not recommended for constant use.

<!-- Screenshot: weight-color preview and its detail settings -->

---
## Multi-object editing

When several meshes are in Edit Mode at once, the grid footer shows the current column, selected-vertex count and a multi-edit indicator (`N obj`), and the vertices of all objects are handled together.

A `Sync Selection` button is also added to `Properties > Object Data > Vertex Groups`.
When it is on, the vertex-group selection is synchronized across the objects being multi-edited.

<!-- Screenshot: multi-edit display and the Sync Selection button -->

---
## Dedicated area / Weight Editor window

Choose `ToPu Weight Editor` from Blender's normal editor-type selector to turn any area into a dedicated weight-editing area. The area is stored with its screen/workspace in the `.blend`, and its HUD display is restored when the file is opened.

- The GPU HUD provides the same operations as the 3D View version. `Clean View` hides the header, toolbar, sidebar and other editor chrome together; click it again to restore the previous layout.
- Only one HUD is interactive at a time. Another `ToPu Weight Editor` area shows `Make This the Main Area`, allowing it to adopt the HUD. If no HUD is active, use `Open ToPu Weight Editor`.
- The window icon in the tool header can also open/close the same dedicated area in a separate Blender window.
- Blender and the operating system manage the window size and placement; adjust the GPU UI separately with the HUD scale button.
- Its viewport display toggles (`Modifier`, `Rest`, `In Front`, `Overlay`, and so on) target the 3D View that opened the dedicated window.
- In the dedicated window, the `×` in the header closes the window.

<!-- Screenshot: dedicated Weight Editor window -->

---
## Add-on preferences

Open them with the `⚙` button in the GPU overlay, or from `Edit > Preferences > Add-ons`.

| Section | Contents |
| --- | --- |
| `Display Language` | `Auto` / `Japanese` / `English`. Auto follows Blender's language setting. |
| `Display Settings` | Whether the GPU overlay button is shown in the tool header. |
| `GPU Overlay UI Scale` | Separate automatic and manual scales for the `3D View HUD` and the `Dedicated Area / Window HUD`. |
| `GPU Overlay UI Style` | `Slightly Round UI Corners` — draws HUD elements with subtle rounded corners closer to Blender UI. |
| `GPU Overlay Color Theme` | `Built-in Set` (20 palettes) and `User Sets`. Import / export of color presets. |
| `GPU Overlay Preset Values` | Changes the values of the preset buttons. |
| `Scroll Step` | Step sizes for `Ctrl + Wheel` and `Ctrl + Shift + Wheel`. |
| Left/right word sets | Word pairs used to infer left/right names during mirroring. |
| `Additional Shortcuts` | Smooth Weights and Pick Influence are off by default; HUD-only bone picking is on by default. |
| `Shortcut Settings` | Review and change the registered keymap items. |
| `Bulk Weight and Mirror Debug` | Prints timing for Scroll, Slider, Preset and Apply, plus mirror source/destination details, to the console. Direct cell entry is not measured. |

`Auto` scale follows Blender's UI scale and the available drawing area. Turn Auto off to enter a manual value from `0.50` to `4.00`; it is stored in sync with the HUD scale buttons. In the 3D View, automatic corner resizing can shrink the HUD as far as `0.25` when necessary.

<p align="left">
  
  <img width="600" height="1113" alt="image" src="https://github.com/user-attachments/assets/f0ac612a-ab84-45df-a610-46dc28a2aa71" />

  <img width="590" height="359" alt="image" src="https://github.com/user-attachments/assets/97659a50-1ff6-46e6-affe-a22991584f30" />


</p>

<!-- Screenshot: color theme settings and UI scale settings -->

---
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

- Shortcuts can be reviewed and changed in the add-on preferences.
- Every shortcut is editable except the bone-transform right-drag.
- The `Alt + Right Click` bone pick can also be toggled with `Shift + Click` on the overlay's `Pick Bone` button, or from its `…` settings. If the binding is lost, `Reset (Alt + Right Click)` restores it.

---
## Changes made to the blend file

The add-on does not access the network, run external programs, or install Python packages.
It reads or writes an external file only when the user explicitly chooses `Import Color Preset` or `Export Color Preset`.

Some features intentionally modify the current blend file:

- **ToPu Weight Editor areas/windows** store the dedicated-window marker and editor type in Blender Screen/Workspace data. No operating-system window position or runtime pointer is stored.
- **Weight snapshots** are compressed and stored in Blender Text datablocks. Large snapshots increase the `.blend` file size.
- **Bone-transform undo data** also creates internal Text datablocks, and obsolete anchors are removed automatically.
- **Bone Creation** adds bones to the specified new or existing armature.
- **Weight-color preview** creates a uniquely named, add-on-owned color attribute. Material slots are only replaced when `Replace Materials` is explicitly enabled.
- **Apply Rest Pose** can modify armature rest data, mesh and shape-key coordinates, Actions and NLA-referenced animation. Save a backup before applying it.
- **Auto Weight** can create temporary mesh/object datablocks during calculation; they are removed when processing finishes.
- **Object transfer** can add an Armature modifier to a destination that does not already have one (on by default).

Bug reports and reproducible test files can be submitted to the [issue tracker](https://github.com/http4211/ToPu_weight_editor/issues).

---
## License and third-party attribution

The add-on itself is licensed under GPL-3.0-or-later.

**Robust Weight Inpainting**

The implementation is based on [RobustSkinWeightsTransferCode](https://github.com/rin-23/RobustSkinWeightsTransferCode) by Rinat Abdrashitov.

Copyright (c) 2024 Rinat Abdrashitov. Licensed under the MIT License.
The original copyright and permission notice is included in `LICENSES/RobustSkinWeightsTransferCode-MIT.txt`.
The implementation here was adapted for Blender and does not bundle or require libigl or Polyscope.

**GPU overlay color palettes**

Twenty built-in palettes were adapted from user-provided Blender theme extensions.
The `Blender Dark` and `Blender Light` palettes are based on Blender's standard theme settings. Their XML files are not bundled.
Package versions, maintainers, licenses, and available source links are recorded in `LICENSES/BlenderThemePalette-Attributions.txt`.
