# Getting Started

## Features

<p align="center">
  <img width="7600" alt="Image" src="https://github.com/user-attachments/assets/d79350fc-493b-4ed0-adac-0435dc3ce42c" />
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

---

## Requirements

- **Blender 4.2 LTS or newer**
- No additional Python packages (NumPy is used when available, otherwise a scalar fallback)

> On some older CPU / GPU setups, performance can drop when the graphics backend is set to `Vulkan`. Switching to `OpenGL` may improve it.

---

## Installation

1. Download the distribution ZIP from `Assets` of the latest [release](https://github.com/http4211/ToPu_weight_editor/releases).
2. Drag & drop the ZIP onto the Blender window (or choose `Edit > Preferences > Add-ons > Install from Disk` and select the ZIP).
3. Enable `ToPu:Weight Editor` in the add-on list.

Two icon buttons are then added to the 3D View tool header.

---

## Opening the editor

<p align="center">
  <img width="1280" alt="Image" src="https://github.com/user-attachments/assets/15f610fb-c21a-4d02-bc4e-715a7f0f310b" />
</p>
<p align="center">
  <img width="230" alt="image" src="https://github.com/user-attachments/assets/4303fa20-bf9e-4f50-bdae-3d7d5c8e28ea" />
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

---

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
