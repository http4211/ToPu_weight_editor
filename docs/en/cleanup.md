# Cleanup

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

> Reference values come from **Edit Settings / Auto-cleanup reference values**. Run in Object Mode, these act on every vertex of the object. Editable center-axis L/R pairs that were already equal stay equal.

---

## Edit Settings / Auto-cleanup reference values

<p align="left">
  <img width="512" height="24" alt="image" src="https://github.com/user-attachments/assets/610329e6-337a-4cb1-aea2-13453394c95f" />
</p>

`Normalize`, `Decimals`, `Threshold` and `Influence Count` set the reference values used by the **Cleanup** buttons.

- Checked items are applied automatically whenever the add-on changes a value.
- Use the `−` / `+` buttons, or type into the value field, to change a value.
- The `…` on `Influence Count` opens `Influence Cleanup Settings`.

**Influence Cleanup Settings** (which bones to keep when a vertex exceeds the influence limit)

- `Consider Bone Hierarchy` (default) — keeps influences spread across the separate chains that branch off a shared parent bone (for example the left and right legs splitting from the hip), so a vertex driven by several chains (a skirt influenced by both legs) is less likely to lose one whole chain.
- `Prefer Weight Values` — the ordinary approach: keeps the highest-weighted bones first.
- `Similar Weight Range` — for `Consider Bone Hierarchy`, the weight difference within which bones in the same branch may be reordered. Groups without a hierarchy fall back to `Prefer Weight Values`.

> Automatic cleanup is not guaranteed to catch everything, so running `Fix Violations` as a final check is recommended.
