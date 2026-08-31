# グリッド操作

## 値プリセット / 入力 / 適用

### プリセットボタン

<img width="473" alt="Image" src="https://github.com/user-attachments/assets/061633e4-e2cf-471f-b9ad-c0c0ed909aaa" />

<img width="280" alt="Image" src="https://github.com/user-attachments/assets/463b655c-5b92-4641-89bd-a3abeff80b92" />

<p align="left">
  <img width="1188" alt="Image" src="https://github.com/user-attachments/assets/df656172-edbc-4420-9059-4b3932b18cf3" />
</p>

`0` `0.1` `0.25` `0.5` `0.75` `0.9` `1` をワンクリックで適用できます。`Add` / `Add%` モードでは `Shift + クリック` で負方向に適用します。プリセット値はアドオンプリファレンスで変更できます。

### 入力モード / スライダーと数値欄

<img width="431" alt="Image" src="https://github.com/user-attachments/assets/3ff92ec4-e965-47e9-a535-421889cac398" />

<img width="693" alt="Image" src="https://github.com/user-attachments/assets/56fd28a7-e82b-4c60-a4ee-034649542502" />

<p align="left">
  <img width="1188" alt="Image" src="https://github.com/user-attachments/assets/e0c3594f-f8f7-43d0-a298-a64aca7c210e" />
</p>

左端のボタンで入力モードを `ABS` → `ADD` → `ADD%` の順に切り替えます。

- `Abs` : 入力値で置き換え。
- `Add` : 現在値に加算（負の値で減算）。
- `Add%` : 現在値に対して割合で加算。

操作方法。

- スライダーのドラッグでリアルタイムに適用（**1 万頂点以上**では、離して確定した時点で適用）。
- 数値欄はクリックで直接入力、上でホイールすると少しずつ変更。
- `適用` : 数値欄の値を選択頂点の現在列に適用。
- `⟳` : 現在の選択頂点でグリッドを手動更新（特殊な選択コマンドの後などに）。
- `Ctrl + ホイール` で加減算、`Ctrl + Shift + ホイール` でより細かく加減算（増減量はプリファレンスで変更可）。

---

## 特殊グループ選択 / 骨取得

<img width="339" alt="Image" src="https://github.com/user-attachments/assets/a12b4d19-3c24-4d61-b7e5-18f19bf57710" />

<img width="109" alt="Image" src="https://github.com/user-attachments/assets/3257c432-2a43-482e-8eef-dddd109b300b" />

<p align="left">
  <img width="1218" alt="Image" src="https://github.com/user-attachments/assets/4324d885-a267-470a-b215-f4b7ef63ed39" />
</p>

`骨取得` を使うと、ビューポート上のボーンをクリックして、そのボーン名の頂点グループ列を選択できます。複数の Armature モディファイアがある場合は最も近い候補を取得します。

- 表示中は、デフォルトで `Alt + 右クリック` からも骨取得できます（`骨取得` ボタンの `Shift + クリック` で ON / OFF）。
- 右隣の `…` : 除外ワード（`IK` `FK` `twist` などを候補から外す）とショートカットを設定。
- `▣↖` が ON のとき : 選択頂点が変わるたびに、最もウェイト値が高い列を自動選択。頂点を切り替えながら主影響ボーンを確認する作業に向きます。

<p align="center">
  <img src="https://raw.githubusercontent.com/http4211/ToPu_weight_editor/main/README_images/bone_pick.gif" alt="骨取得の動作">
</p>

---

## 列状態 / 表示条件（ロック / 無視 / 強制表示）

<img width="156" alt="Image" src="https://github.com/user-attachments/assets/7d078ee1-5d84-48fb-b533-4b6c889e2c08" />
<img width="393" alt="image" src="https://github.com/user-attachments/assets/fccbf13f-6dc1-4dc8-97e1-cae4aaf6f785" />

<p align="left">
  <img width="1192" alt="Image" src="https://github.com/user-attachments/assets/5d1c7790-e614-45b6-8d47-9243c6fb875a" />
</p>

- `ロック` : 選択列を編集できない状態にする。
- `無視` : 対象列を合計・正規化・整理の対象外にする。
- `強制表示` : 0 ウェイトの列でもグリッドに表示する。
- `Shift + クリック` で選択列以外を対象に作用、`Alt + クリック` で状態をすべて解除。
- `Ctrl + 強制表示` : 文字フィルターを開き、カンマ区切りの複数ワードに部分一致する列をまとめて強制表示。

---

## グリッド操作 / 下部タブ

### 列ヘッダー

  <img width="425" alt="image" src="https://github.com/user-attachments/assets/6fb96f9a-399e-4b02-8338-2133fac54b9a" />

<p align="center">
  <img width="1346" alt="Image" src="https://github.com/user-attachments/assets/e5329a73-88bd-48c9-92db-512e42d478b0" />
</p>

  <img width="202" alt="image" src="https://github.com/user-attachments/assets/3d1f2be4-fb64-4ea1-a3c7-91dd255371d7" />

- クリック : その列が選択列になる。
- `Shift + 列クリック` : その頂点グループに値がある頂点をまとめて選択。
- `Ctrl + 列クリック` : 選択中の頂点のうち、その列に値がある頂点だけを残す。
- `Ctrl + Shift + 列クリック` : その列のセルをすべてセル選択する（全ページの表示行が対象）。
- 右クリック : **ウェイト転送メニュー**を開く。

### 固 / 頂点 / 合計

<img width="149" alt="Image" src="https://github.com/user-attachments/assets/20e5f137-204f-4693-84a6-e9f5455eb703" />

<p align="center">
  <img width="1192" alt="Image" src="https://github.com/user-attachments/assets/1f944500-6102-4533-915b-c1667d87732d" />
</p>

- `固` : 対象頂点をウェイトロック（`Alt + クリック` で解除）。各行の `固` セルでも切り替え可（ドラッグでまとめて）。
- `頂点` : 表示中の行をグリッド選択（`Alt + クリック` で解除）。各行の `頂点` セルで、その頂点をビュー上でハイライトし常に表示。
- `合計` : **違反のみ表示**を切り替え（`Shift + クリック` で表示中の頂点をメッシュ選択）。
- 影響数や合計値に問題がある頂点があると、`合計` ヘッダーが `合計 ⚠` に変わります。
- 違反のみ表示は、現在のページだけでなく全ページの違反行が対象です。

### セル

<p align="center">
  <img width="1184" alt="Image" src="https://github.com/user-attachments/assets/d40e61e9-ae42-4cf0-b916-46545d88c886" />
</p>

- クリック : 数値を直接入力（`Enter` で確定）。先頭に `+` `-` `*` `/` で現在値へ演算（例: `*0.5`、`+0.1`）。
- ドラッグ : 範囲選択（`Shift + ドラッグ` で追加、`Ctrl + ドラッグ` で解除）。
- 右クリック : セル選択を解除。
- `Ctrl + Shift + クリック` : そのセルの列をまとめてセル選択（列ヘッダーからも同じ）。
- 複数セル選択中は、入力値をまとめて適用。選択セルが残っている間は、スライダー / ホイール / プリセット / 適用など全ての値変更で実メッシュ選択より優先されます。

<p align="center">
  <img src="https://raw.githubusercontent.com/http4211/ToPu_weight_editor/main/README_images/cell_edit.gif" alt="セル編集">
</p>

### 表示タブ

<p align="left">
  <img width="724" alt="Image" src="https://github.com/user-attachments/assets/d9a3ea5b-4ce8-4942-994f-391fd78fc45b" />
</p>

<p align="left">
  <img width="1186" alt="Image" src="https://github.com/user-attachments/assets/153b50ac-3af7-404e-9795-18da04257bc9" />
</p>

グリッド下部のタブで、表示する列の種類を切り替えます。

- `すべて` : ボーン列と非ボーン列を表示。
- `変形` : ボーン名と一致する変形用の列だけを表示。
- `その他` : ボーン名と一致しない非ボーン列だけを表示。

タブごとのオプション。

- `非ボーン列を無視`（すべてタブ）: 非ボーン列を自動的に無視状態にする。
- `作成済み常時`（その他タブ）: 値が入っていなくても、作成済みの非ボーン列を常に表示。
- `不正規許可`（その他タブ）: ON のとき、その他列は合計が 1 以上でも違反にせず、正規化もしない。
- `非表示ワード` : 指定したワードをグループ名表示から隠して短く表示（実際の名前は変わらない）。

### 列右クリックのウェイト転送

<img width="517" alt="Image" src="https://github.com/user-attachments/assets/61f1ca69-668d-49d1-96f2-128bed527655" />

<img width="205" alt="Image" src="https://github.com/user-attachments/assets/4fb738b0-aad8-4714-93ca-a4320140b8db" />

<p align="left">
  <img width="571" alt="Image" src="https://github.com/user-attachments/assets/7d405982-882b-4299-a31f-460828fcdfae" />
</p>

列ヘッダーを右クリックすると、頂点グループ間の転送メニューを開けます。

- `転送元に指定` / `この列へ転送` : 右クリックした列を転送元にし、現在の列へ転送。
- `複数ウェイト転送` : 転送元・転送先・処理方法（`コピー` / `移行` / `置換`）・対象範囲（グループ全体 / 選択頂点）を指定して転送。複数ペアをまとめて処理できます。

---

## 複数オブジェクト編集

複数のメッシュを同時に編集モードにしていると、グリッドのフッターに現在列・選択頂点数・`複数編集: N obj` が表示され、複数オブジェクトの頂点をまとめて扱えます。

また `プロパティ > オブジェクトデータ > 頂点グループ` パネルに `選択を同期` ボタンが追加され、ON にするとオブジェクト間で頂点グループの選択を同期します。
