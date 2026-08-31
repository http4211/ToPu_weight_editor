# Brushes

<p align="left">
  <img width="187" alt="image" src="https://github.com/user-attachments/assets/64ef486e-415f-48ef-8e13-97b9cac42136" />
</p>

The overlay can start the add-on's own weight brushes, used directly in the viewport. They work in both Edit Mode and Weight Paint Mode, and bone picking / bone transform stay available while brushing.

- `F` changes the size; `Tab` / `Q` / `Esc` return to the previous tool.
- The tool header exposes size, selection mask and each brush's value.

### Normal brush

<img width="539" alt="image" src="https://github.com/user-attachments/assets/9d3ade5f-ecc5-4456-babc-703c9596b5ec" />

<p align="left">
  <img width="898" alt="Image" src="https://github.com/user-attachments/assets/51d508d6-5c53-45cc-88a1-5d793de41f40" />
</p>

The basic brush that adds to or subtracts from the selected column.

- Left-drag adds; `Ctrl + Left-drag` subtracts.
- `Shift + Left-drag` temporarily smooths; `Ctrl + Shift + Left-drag` spreads surrounding influences.
- `Normal Amount` — how much one stroke changes.
- `Constant Paint` — avoids over-layering when the same vertex is hit repeatedly.
- `Stack Paint` — adds/subtracts `Normal Amount` on every touch, building up gradually.

### Smoothing brush

<img width="787" alt="image" src="https://github.com/user-attachments/assets/47dadabd-d050-464c-95d4-e702ca28b778" />

<p align="left">
  <img width="1268" alt="Image" src="https://github.com/user-attachments/assets/fe1cc575-10d5-49c8-884a-3b3351182f5a" />
</p>

Blends the selected column with the surrounding vertices. Good for hard paint edges and seams left after mirroring.

- Left-drag smooths the weights around the cursor.
- `Shift + Left-drag` smears like a fingertip; `Ctrl + Left-drag` spreads the selected column's stronger weights outward; `Alt + Left-drag` feathers its weaker weights outward, blending them into the surroundings.
- `Strength` — how far values move toward their neighbours; `Iterations` — how many passes run.
- When an ignored column is selected, only that ignored column is processed.

`Work Mode` switches the behavior.

- `Fast` — processes only the connected edges under the cursor (lightest).
- `Surface` — walks connected topology (does not bleed to the back side).
- `Volume` — also references spatially-near vertices to match local density (`Volume Range` tunes the reach).

### Gradient brush

<img width="707" alt="image" src="https://github.com/user-attachments/assets/ea890ba2-f618-4a65-98df-af87c8946b0c" />

<p align="left">
  <img width="1234" alt="Image" src="https://github.com/user-attachments/assets/df2d5bc8-1fbb-4c8d-90ff-31e5a5a0b02a" />
</p>

Builds a weight gradient along the drag direction.

- `Gradient Value` — the maximum weight (the falloff curve runs from this value down to 0).
- Hold `Ctrl` for the subtract direction, `Shift` for the add direction.
- Type — `Linear` (straight) / `Radial` (outward from the start point) / `Line Radial` (spreads from the dragged line).
- `Falloff` — `Linear` / `Smooth` / `Sphere` / `Root` / `Sharp`, or `Custom` (`Custom Exponent` `0.1`–`8`).

### Lasso brush

<img width="407" alt="image" src="https://github.com/user-attachments/assets/a9f066a5-c5c9-4e4d-9bf8-93cdc9dc093d" />

<p align="left">
  <img width="1154" alt="Image" src="https://github.com/user-attachments/assets/9c2046e0-adc7-49cd-98e2-7e854064ee5f" />
</p>

Fills an enclosed area with a set value. Good for flattening a wide area to 0 / 0.5 / 1.0 in one action.

- Left-drag to enclose an area; `Lasso Value` is applied inside it.
- Hold `Ctrl` for the subtract direction, `Shift` for the add direction.
- The brush size is used as the width that blends the boundary.

### Selection mask

<p align="left">
  <img width="1208" alt="Image" src="https://github.com/user-attachments/assets/4c9e47f7-afae-4fa9-9dfe-8d135c61ee2d" />
</p>

Turning `Mask` on restricts the brush to the currently selected vertices. Helps avoid painting nearby parts or back-side vertices by accident. Shared by all brushes.

<p align="center">
  <img src="https://raw.githubusercontent.com/http4211/ToPu_weight_editor/main/README_images/brush_tools.gif" alt="Brush tools">
</p>
