# GPU Overlay

## GPU overlay / Header row

- `Drag to Move` — moves the overlay.
- `Grid Display` — toggles grid display and realtime update.
- `▣` `↶` `🗑` — save / restore / delete a **weight snapshot**.
- `⚙` — opens the add-on preferences.
- `AUTO ×1` — click to cycle `Auto` → `×1` → `×1.5` → `×2`. `Shift + Click` to enter `0.50`–`4.00`.
- `×` — closes the overlay.

> The HUD scale is stored separately for the 3D View and for the dedicated area / window. `Auto` follows Blender's UI scale and the available drawing area.

---

## Weight snapshots

`▣` `↶` `🗑` in the header row provide temporary weight storage and restoration.

- `▣` — save all weights of the target object under a name.
- `↶` — restore from the list. Object Mode restores the whole target; Edit / Weight Paint Mode restores selected vertices.
- `🗑` — delete a saved snapshot (single or bulk).

The same object with the same vertex count is restored directly by vertex index; a different object or topology uses the saved positions and normals for spatial transfer (interpolation and so on follow the `Object Weight Copy` detail settings).

> Snapshots are compressed and stored inside the `.blend`. Large snapshots increase the file size.

---

## Bone transform

<img width="532" height="28" alt="Image" src="https://github.com/user-attachments/assets/18661bf8-2ccc-4e3c-9481-de04e75502ae" />

<p align="left">
  <img width="1314" height="756" alt="Image" src="https://github.com/user-attachments/assets/0b5ab8d2-1abd-4378-9fcc-268317d0ef22" />
</p>

When the selected column matches a bone, its `Location`, `Rotation` and `Scale` can be reviewed and edited. Useful for nudging the pose while watching how the weights behave.

- `L` `R` `S` — edit Location / Rotation / Scale. Click a value field to type directly, or horizontal-drag to change (`Shift` for fine steps, `Ctrl` for large steps).
- `↱` — toggles right-drag editing in the viewport. While on, right-dragging changes the current value along the screen direction.
- `↺` — restore the current bone to its original values. `Alt + ↺` restores every changed bone.
