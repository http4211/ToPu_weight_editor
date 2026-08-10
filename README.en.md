# ToPu_weight_editor

<p align="center">
  <img width="591" height="651" alt="image" src="https://github.com/user-attachments/assets/6e99de70-2fb1-4dcf-acc1-f8b4eafee4ce" />
</p>

<p align="center">
  <a href="README.md">日本語</a> | <b>English</b>
</p>

ToPu_weight_editor (extension name: **ToPu:Weight Editor**) is a Blender add-on for reviewing and editing skin weights.
Based on Softimage-style weight editing, it puts numeric weight editing, normalization, cleanup, smoothing, mirroring, copy & paste, transfer, bone picking, and display helpers into a single **GPU overlay** drawn directly in the 3D View.

No external UI framework or extra Python package is used. The add-on runs with Blender's built-in GPU drawing and Blender-native areas/windows.

> **This document describes version 1.5.112.**
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
  - [Overall layout](#overall-layout)
  - [Header row](#header-row)
  - [Weight grid](#weight-grid)
  - [Column tabs](#column-tabs)
  - [Lock / Ignore / Force Show](#lock--ignore--force-show)
  - [Input mode, slider and value field](#input-mode-slider-and-value-field)
  - [Preset buttons](#preset-buttons)
  - [Auto-cleanup reference values](#auto-cleanup-reference-values)
- [Pick Bone / follow the peak column](#pick-bone--follow-the-peak-column)
- [Bone transform](#bone-transform)
- [Display helpers](#display-helpers)
- [Cleanup](#cleanup)
- [Brushes](#brushes)
- [Edit](#edit)
- [Weight Copy](#weight-copy)
- [Column right-click weight transfer](#column-right-click-weight-transfer)
- [Weight snapshots](#weight-snapshots)
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
  <img width="7600" height="5200" alt="Image" src="https://github.com/user-attachments/assets/a2a0c44a-340a-4d4b-856b-fca37bce31dd" />
</p>


- Review and edit weights from the GPU overlay in both Edit Mode and Weight Paint Mode
- List selected vertices in a lightweight cell grid and adjust values while watching the 3D View
- Intuitive editing through cells, slider, presets and brushes
- Four dedicated weight brushes: Normal, Smoothing, Gradient and Lasso
- Normalize, Clean Decimals, Limit Influences, Threshold Cleanup, Fix Violations, Unused cleanup and Stepped
- Smooth Weights, Mirror and Apply Rest Pose
- Vertex copy/paste, nearest transfer, object-to-object transfer and vertex-group transfer
- Bone picking, bone-transform editing, bone highlighting and display-helper toggles
- Two automatic weighting methods: Blender's built-in automatic weights and a dedicated voxel diffusion method (Voxel Heat Skinning)
- Weight snapshots saved by name inside the blend file
- Weight-color preview
- A **ToPu Weight Editor area** available as a Blender editor type, plus a **dedicated Weight Editor window** separate from the 3D View
- Simultaneous editing of several meshes, with vertex-group selection sync
- Japanese / English UI (follows Blender's language setting, or can be forced)

### Center L/R balancing in mirror and cleanup

With the default settings, selected-vertex and whole-object mirroring automatically balance the L/R weights of vertices on the center axis. Turn off `Balance Center L/R Weights` in Mirror Details to skip only that balancing step.
`Normalize`, `Clean Decimals`, `Threshold Cleanup`, `Limit Influences` and `Fix Violations` preserve an editable center-axis L/R pair when it was equal before the operation. Intentionally asymmetric pairs remain asymmetric. Decimal rounding and influence-limit selection treat an equal L/R pair as one symmetric unit.

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
  <img width="257" height="55" alt="image" src="https://github.com/user-attachments/assets/06b31e51-68da-4cf4-a228-10104cc5a101" />
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

### Overall layout

<p align="center">
  <img width="591" height="651" alt="image" src="https://github.com/user-attachments/assets/6e99de70-2fb1-4dcf-acc1-f8b4eafee4ce" />
</p>

From top to bottom:

1. **Header row** — move handle, Grid Display toggle, weight snapshots, preferences, UI scale, close button
2. **Bone transform row** — shown only when the selected column matches a bone
3. **Four sections** — `Edit` / `Weight Copy` / `Brush` / `Cleanup`
4. **Display helper row** — `Modifier` `Rest` `In Front` `Overlay` `Bone Hi` `Material`
5. **Auto-cleanup reference row** — `Normalize` `Decimals` `Threshold` `Influence Count`
6. **Preset row** — preset values, `▣↖`, `Pick Bone`, `Lock`, `Ignore`, `Force Show`
7. **Input row** — input mode, slider, value field, `Apply`, `⟳`
8. **Weight grid** — including the column tabs and `Hidden Words`

- Drag `Drag to Move` at the top to move the overlay.
- Drag any of the four corners to resize it.
- The visible row and column capacity follows the actual drawable size of the HUD or dedicated area. Use the scrollbars or mouse wheel to move through the remaining rows and columns.

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

<img width="149" height="30" alt="Image" src="https://github.com/user-attachments/assets/20e5f137-204f-4693-84a6-e9f5455eb703" />

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

<img width="724" height="25" alt="Image" src="https://github.com/user-attachments/assets/d9a3ea5b-4ce8-4942-994f-391fd78fc45b" />

<p align="left">
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

### Lock / Ignore / Force Show

<img width="156" height="26" alt="Image" src="https://github.com/user-attachments/assets/7d078ee1-5d84-48fb-b533-4b6c889e2c08" />

<p align="left">
  <img width="1192" height="766" alt="Image" src="https://github.com/user-attachments/assets/5d1c7790-e614-45b6-8d47-9243c6fb875a" />
</p>

- `Lock` — makes the selected column non-editable.
- `Ignore` — excludes the column from totals, normalization and cleanup. On the `Other` tab this is handled as an Other-specific ignore state.
- `Force Show` — keeps a column in the grid even when its weights are zero.
- `Shift + Click` applies the action to every column except the selected one.
- `Ctrl + Force Show` opens a text filter. Comma-separated fragments force-show every partially matching group, while columns force-shown manually stay enabled.
- `Alt + Click` clears the state everywhere.

### Input mode, slider and value field

<img width="431" height="156" alt="Image" src="https://github.com/user-attachments/assets/3ff92ec4-e965-47e9-a535-421889cac398" />

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

### Preset buttons

<img width="473" height="101" alt="Image" src="https://github.com/user-attachments/assets/061633e4-e2cf-471f-b9ad-c0c0ed909aaa" />

<img width="280" height="28" alt="Image" src="https://github.com/user-attachments/assets/463b655c-5b92-4641-89bd-a3abeff80b92" />

<p align="left">
  <img width="1188" height="764" alt="Image" src="https://github.com/user-attachments/assets/df656172-edbc-4420-9059-4b3932b18cf3" />
</p>

Applies `0`, `0.1`, `0.25`, `0.5`, `0.75`, `0.9` or `1` in one click.
In `Add` / `Add%` mode, `Shift + Click` applies the negative value.

Preset values can be changed in the add-on preferences.

### Auto-cleanup reference values

<p align="left">
<img width="519" height="26" alt="Image" src="https://github.com/user-attachments/assets/416d1946-2607-42b6-a038-2b816687af63" />
</p>

`Normalize`, `Decimals`, `Threshold` and `Influence Count`. The values set here are the reference used by the [Cleanup](#cleanup) buttons.

- Checked items are applied automatically whenever the add-on changes a value.
- Use the `−` / `+` buttons, or type into the value field, to change the reference value.

> Automatic cleanup is not guaranteed to catch everything, so running `Fix Violations` as a final check is recommended.

---

## Pick Bone / follow the peak column

<img width="339" height="195" alt="Image" src="https://github.com/user-attachments/assets/a12b4d19-3c24-4d61-b7e5-18f19bf57710" />

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

## Display helpers

<img width="510" height="24" alt="Image" src="https://github.com/user-attachments/assets/fb306577-a3d4-467f-8ba0-261e4183ef3d" />

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

## Brushes

<p align="left">
  <img width="192" height="111" alt="Image" src="https://github.com/user-attachments/assets/2e57f831-8509-4954-81cc-e75aed5e66c3" />
</p>

The overlay can start the add-on's own weight brushes, used directly in the viewport.
They work in both Edit Mode and Weight Paint Mode.
Bone picking and bone transform stay available while brushing, which keeps weighting work fast.

While a brush is active, `F` changes the size and `Tab` / `Q` / `Esc` return to the previous tool.
The tool header exposes size, selection mask, normal amount, smoothing strength, gradient value, lasso value and more.

### Normal brush

<img width="436" height="27" alt="Image" src="https://github.com/user-attachments/assets/714c3d89-c99d-47ab-b348-2b36a4712cb2" />

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

<img width="625" height="29" alt="Image" src="https://github.com/user-attachments/assets/52c425a0-aeec-4080-9798-5170c5fdb615" />

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

<img width="640" height="24" alt="Image" src="https://github.com/user-attachments/assets/a15031da-149f-49f5-84be-c73567c54603" />

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

<img width="384" height="27" alt="Image" src="https://github.com/user-attachments/assets/4756f60d-3580-463b-bf3a-96aeaafadef0" />

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

## Edit

<p align="left">
  <img width="98" height="109" alt="Image" src="https://github.com/user-attachments/assets/b5a71567-3cdc-4ca8-b371-c59428e4c4a8" />
</p>

The `Edit` section holds `x-` / `x+` on its title row, plus `Smooth Weights`, `Mirror` and `Apply Rest Pose`.

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

<img width="296" height="163" alt="Image" src="https://github.com/user-attachments/assets/9b1fc7b0-366f-4646-b56b-dacad2702608" />

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

<img width="484" height="459" alt="Image" src="https://github.com/user-attachments/assets/b6c7b993-1e28-4ab3-925b-db2b697cd7b8" />

<img width="340" height="232" alt="Image" src="https://github.com/user-attachments/assets/b0c1e84f-6dbd-4a73-9186-fa0eee9e6912" />

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

<img width="165" height="108" alt="Image" src="https://github.com/user-attachments/assets/ef71a5b2-b587-4898-bbdc-6eb6a670ac43" />

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

<p align="left">
  <img width="1406" height="958" alt="Image" src="https://github.com/user-attachments/assets/ecde6c2a-a6d8-4069-81aa-55582c799c53" />
</p>

`Auto Weight` binds the selected meshes to an armature and assigns automatic weights.
It can keep existing parent relationships, and linked objects can be localized automatically.
It can also weight only the part covered by the current vertex selection.

The detail settings switch between Blender's built-in automatic weights and the dedicated voxel diffusion method (Voxel Heat Skinning).

**Main Voxel Heat Skinning settings**

| Item | Description |
| --- | --- |
| `Voxel Resolution` | Voxels along the longest axis. Controls quality, speed and memory. |
| `Diffuse Loops` | Total diffusion passes are resolution × loops. Higher is smoother but heavier. |
| `Diffuse Falloff` | Higher values reduce distant bone influence and create tighter, more local weights. |
| `Smoothing Passes` | Post-process smoothing passes. Higher values spread the blend farther. |
| `Sample Rays` | Ray samples used for solidification. More samples are more robust on non-watertight meshes. |
| `Detect Solidify` | Solidifies thin outfits and shells. When on, all bones must be inside the character volume. |
| `Use Half CPU Cores` | Compatibility setting that keeps CPU usage lower. |

The method is heavy, but because it voxelizes the space regardless of mesh front/back faces, it tends to produce clean weights even on complex models.

**Use Specified Bones Only**

When `Use Specified Bones Only` is on, automatic weighting is restricted to the saved bone list.

- The same list applies to both Blender's built-in automatic weights and Voxel Heat Skinning, in Object Mode and Edit Mode.
- `Get Selected Bones` captures the bone selection from Edit, Pose or Object Mode.
- `All` / `None` buttons and a compact bone checklist let you adjust the list.
- Explicitly selected bones override deform-bone and excluded-keyword filtering.

---

## Column right-click weight transfer

<img width="517" height="246" alt="Image" src="https://github.com/user-attachments/assets/61f1ca69-668d-49d1-96f2-128bed527655" />

<img width="205" height="125" alt="Image" src="https://github.com/user-attachments/assets/4fb738b0-aad8-4714-93ca-a4320140b8db" />

<p align="left">
  <img width="571" height="1024" alt="Image" src="https://github.com/user-attachments/assets/7d405982-882b-4299-a31f-460828fcdfae" />
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
  <img width="432" height="1047" alt="Image" src="https://github.com/user-attachments/assets/5bac5b98-8968-4f9c-9abd-93796713896f" />
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
