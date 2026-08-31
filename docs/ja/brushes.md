# ブラシ

<p align="left">
  <img width="192" alt="Image" src="https://github.com/user-attachments/assets/2e57f831-8509-4954-81cc-e75aed5e66c3" />
</p>

GPU オーバーレイから、ビューポート上で使う独自のウェイトブラシを開始できます。編集モード / ウェイトペイントモードの両方で使え、ブラシ中でも骨取得や骨トランスフォームを併用できます。

- `F` でサイズ変更、`Tab` / `Q` / `Esc` で元のツールへ戻る。
- ツールヘッダーで、サイズ・選択マスク・各ブラシ値などを調整。

### 通常ブラシ

<img width="436" alt="Image" src="https://github.com/user-attachments/assets/714c3d89-c99d-47ab-b348-2b36a4712cb2" />

<p align="left">
  <img width="898" alt="Image" src="https://github.com/user-attachments/assets/51d508d6-5c53-45cc-88a1-5d793de41f40" />
</p>

選択列のウェイトを加算 / 減算する基本ブラシです。

- 左ドラッグで加算、`Ctrl + 左ドラッグ` で減算。
- `Shift + 左ドラッグ` で一時的にスムーズ、`Ctrl + Shift + 左ドラッグ` で周辺の影響を広げる。
- `通常量` : 1 ストロークあたりの変化量。
- `一定塗` : 同じ頂点に重ねても塗りすぎないように塗る。
- `重ね塗` : 当たるたびに `通常量` を加減算し、なぞるほど強くなる。

### スムーズブラシ

<img width="719" alt="image" src="https://github.com/user-attachments/assets/753ab833-efb9-4ae2-b11c-810763683587" />

<p align="left">
  <img width="1268" alt="Image" src="https://github.com/user-attachments/assets/fe1cc575-10d5-49c8-884a-3b3351182f5a" />
</p>

選択列のウェイトを周囲になじませるブラシです。塗り跡の硬い部分やミラー後の境界を整えるのに向いています。

- 左ドラッグでなめらかにする。
- `Shift + 左ドラッグ` で指先でなぞるようにスミア、`Ctrl + 左ドラッグ` で選択列の強いウェイトを周囲へ広げる、`Alt + 左ドラッグ` で選択列の弱いウェイトを周囲へなじませながら広げる。
- `強さ` で寄せ具合、`回数` で反復回数を調整。
- 無視列を選択している場合は、その無視列だけを処理。

`稼働方式` で挙動を切り替えます。

- `高速` : カーソル下の接続辺の周辺だけを処理（最も軽い）。
- `表面` : 接続トポロジーをたどってスムーズ（裏面へ貫通しない）。
- `ボリューム` : 空間的に近い頂点も参照し、局所密度に合わせてスムーズ（`ボリューム範囲` で届く範囲を調整）。

### グラデーションブラシ

<img width="640" alt="Image" src="https://github.com/user-attachments/assets/a15031da-149f-49f5-84be-c73567c54603" />

<p align="left">
  <img width="1234" alt="Image" src="https://github.com/user-attachments/assets/df2d5bc8-1fbb-4c8d-90ff-31e5a5a0b02a" />
</p>

ドラッグ方向に沿って、選択列のウェイトにグラデーションを作るブラシです。

- `グラデ値` で最大値を調整（減衰カーブに沿ってこの値から 0 へ）。
- `Ctrl` で減算方向、`Shift` で加算方向。
- 種類 : `リニア`（直線）/ `放射`（開始点から外側へ）/ `線放射`（線から広がる）。
- `減衰` : `リニア` / `スムーズ` / `球状` / `ルート` / `シャープ`、または `カスタム`（`カスタム指数` `0.1〜8`）。

### 投げ縄ブラシ

<img width="384" alt="Image" src="https://github.com/user-attachments/assets/4756f60d-3580-463b-bf3a-96aeaafadef0" />

<p align="left">
  <img width="1154" alt="Image" src="https://github.com/user-attachments/assets/9c2046e0-adc7-49cd-98e2-7e854064ee5f" />
</p>

囲んだ範囲を指定値で塗るブラシです。広い範囲を一気に 0 / 0.5 / 1.0 などへそろえたいときに向いています。

- 左ドラッグで範囲を囲むと、内側へ `投げ縄値` を適用。
- `Ctrl` で減算方向、`Shift` で加算方向。
- ブラシサイズは、境界をなじませる幅として使われます。

### 選択マスク

<p align="left">
  <img width="1208" alt="Image" src="https://github.com/user-attachments/assets/4c9e47f7-afae-4fa9-9dfe-8d135c61ee2d" />
</p>

`マスク` を ON にすると、ブラシの影響先を選択中の頂点だけに制限します。近い別パーツや裏側の頂点へ意図せず塗るのを防げます。すべてのブラシで共通して使えます。

<p align="center">
  <img src="https://raw.githubusercontent.com/http4211/ToPu_weight_editor/main/README_images/brush_tools.gif" alt="ブラシ操作">
</p>
