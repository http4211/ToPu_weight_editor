# About

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

---

## License and third-party attribution

The add-on itself is licensed under GPL-3.0-or-later.

- **Robust Weight Inpainting** — based on [RobustSkinWeightsTransferCode](https://github.com/rin-23/RobustSkinWeightsTransferCode) by Rinat Abdrashitov (MIT License), adapted for Blender. It does not bundle or require libigl or Polyscope. The original notice is in `LICENSES/RobustSkinWeightsTransferCode-MIT.txt`.
- **GPU overlay color palettes** — twenty built-in palettes were adapted from user-provided Blender theme extensions. `Blender Dark` / `Blender Light` are based on Blender's standard theme settings. Details are recorded in `LICENSES/BlenderThemePalette-Attributions.txt`.
