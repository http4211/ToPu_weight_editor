# Display Helpers

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
