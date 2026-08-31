# Preferences & Shortcuts

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
  <img width="600" alt="image" src="https://github.com/user-attachments/assets/f0ac612a-ab84-45df-a610-46dc28a2aa71" />
  <img width="590" alt="image" src="https://github.com/user-attachments/assets/97659a50-1ff6-46e6-affe-a22991584f30" />
</p>

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

> Shortcuts can be reviewed and changed in the add-on preferences (except the bone-transform right-drag).
