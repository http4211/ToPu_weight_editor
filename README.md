# ToPu_weight_editor

<p align="center">
  <img src="README_images/Main.png" alt="ToPu_weight_editor GPU Overlay" width="720">
</p>

ToPu_weight_editor は、Blender 上でスキンウェイトを確認・編集するためのアドオンです。  
Softimage 風のウェイト編集をベースに、3D ビュー上へ表示される **GPU オーバーレイ** から、ウェイトの数値編集、正規化、整理、スムーズ、ミラー、コピー&ペースト、転送、骨取得、表示補助までをまとめて操作できます。

N パネルを何度も開き直さず、モデルを見ながらウェイトを直接調整したい場面を想定しています。

## できること

- 3D ビュー上の GPU オーバーレイで、選択頂点のウェイトを表形式で確認・編集
- セルクリック、横ドラッグ、スライダー、プリセットボタンによるウェイト編集
- `Abs` / `Add` / `Add%` の入力モード切り替え
- 頂点行・列・セル単位の選択、ロック、無視、0 ウェイト列の強制表示
- `All` / `Deform` / `Other` タブによる頂点グループ列の切り替え
- 正規化、小数点整理、影響数制限、閾値以下の削除、違反整理
- 通常 / スムーズ / グラデーション / 投げ縄ブラシによるビューポート上のウェイト編集
- 頂点ウェイトコピー、近接コピー、オブジェクト間ウェイトコピー
- GPU オーバーレイ上の列右クリックから、頂点グループ間のウェイト転送
- ミラー実行、スムーズ化、自動ウェイト
- 骨取得、選択列に対応するボーンのハイライト、ボーンの位置・回転・スケール調整
- アーマチュア表示、レスト表示、最前面表示、Vertex Group Weights 表示、マテリアル風ウェイト表示の切り替え

## 動作環境

- Blender 4.0 以降
- ToPu_weight_editor 1.4.1

外部ウィンドウではなく Blender の 3D ビュー上に GPU オーバーレイを描画して動作します。  
追加の UI ライブラリは不要です。

## インストール

### 1. ZIP をインストール

Blender の `編集 > プリファレンス > アドオン` を開き、`ディスクからインストール` で配布 ZIP を選択します。

<p align="left">
  <img src="README_images/install_addon.png" alt="アドオンのインストール" width="720">
</p>

### 2. アドオンを有効化

アドオン一覧で `ToPu_weight_editor` を有効化します。  
有効化すると、3D ビューのサイドバーに `TPWE` タブが追加されます。

<p align="left">
  <img src="README_images/enable_addon.png" alt="アドオンの有効化" width="720">
</p>

## 起動方法

1. 3D ビューでウェイトを編集したいメッシュを選択します。
2. `N` キーでサイドバーを開きます。
3. `TPWE` タブの `GPUオーバーレイ` を押します。
4. 3D ビュー上に GPU オーバーレイが表示されます。

<p align="center">
  <img src="README_images/open_gpu_overlay.png" alt="GPUオーバーレイの起動" width="720">
</p>

GPU オーバーレイは、デフォルトでは `W` キーでも表示 / 非表示を切り替えられます。  
閉じるときは `W` または `Esc` を使います。

## クイックスタート

1. メッシュを編集モード、またはウェイトペイントモードにします。
2. 編集したい頂点を選択します。
3. GPU オーバーレイの `グリッド表示` を ON にします。
4. 表示された列ヘッダーをクリックして、編集したい頂点グループを選択します。
5. セル、スライダー、数値欄、プリセットボタンでウェイトを調整します。
6. 必要に応じて `正規化`、`小数点`、`影響数`、`閾値`、`違反整理` でウェイトを整えます。

<p align="center">
  <img src="README_images/quick_start.gif" alt="GPUオーバーレイの基本操作" width="720">
</p>

## GPU オーバーレイ

### 全体レイアウト

<p align="center">
  <img src="README_images/gpu_overlay_layout.png" alt="GPUオーバーレイ全体" width="720">
</p>

- 上部の `ドラッグで移動` をドラッグすると、GPU オーバーレイの位置を動かせます。
- 右上のリサイズハンドルをドラッグすると、表示サイズを変更できます。
- `グリッド表示` で選択頂点のウェイト表を表示します。
- 歯車ボタンからアドオンプリファレンスを開けます。
- 行数・列数は GPU オーバーレイ上の表示数コントロール、またはホイール操作で調整できます。

### ウェイトグリッド

<p align="center">
  <img src="README_images/weight_grid.png" alt="ウェイトグリッド" width="720">
</p>

- 行は頂点、列は頂点グループです。
- 列ヘッダーをクリックすると、その列が選択列になります。
- 同じ列をもう一度クリックすると選択を解除できます。
- `Shift + 列クリック` で、その頂点グループに値が入っている頂点を選択します。
- `Ctrl + 列クリック` で、現在の選択頂点の中からその列に値が入っている頂点を選択します。
- 列ヘッダーを右クリックすると、ウェイト転送メニューを開けます。
- 頂点番号の行をクリックすると、GPU オーバーレイ上の行選択ができます。
- `Shift` / `Ctrl` を押しながら行クリックで追加・解除、ドラッグで範囲選択できます。
- セルをクリックすると数値入力、横ドラッグで加算調整できます。
- `Shift + ドラッグ` で細かく調整できます。

<p align="center">
  <img src="README_images/cell_edit.gif" alt="セル編集" width="720">
</p>

### 行・列・セルのロック

<p align="left">
  <img src="README_images/locks_and_ignore.png" alt="ロックと無視" width="720">
</p>

- 列の `ロック` は、選択列を編集できない状態にします。
- `Shift + ロック` で選択列以外をロックします。
- `Alt + ロック` でロックをすべて解除します。
- `無視` は、対象列を合計・正規化・整理の対象外として扱います。
- `0` 表示は、0 ウェイトの列をグリッドに強制表示します。
- 行ロックは、頂点単位でウェイト編集を保護します。ドラッグで複数行をまとめて切り替えられます。

## 数値編集

<p align="left">
  <img src="README_images/value_editing.png" alt="GPUオーバーレイの数値編集" width="720">
</p>

### 入力モード

- `Abs` : 入力した値で置き換えます。
- `Add` : 現在値に加算します。負の値で減算できます。
- `Add%` : 現在値に対して割合で加算します。

### スライダーと数値欄

- スライダーをドラッグすると、選択列へ値を即時適用します。
- 数値欄をクリックすると、キーボードから直接入力できます。
- 数値欄の上でホイールすると、値を少しずつ変更できます。
- `適用` ボタンで、数値欄の値を選択頂点の現在列に適用します。

### プリセットボタン

<p align="left">
  <img src="README_images/presets.png" alt="プリセットボタン" width="720">
</p>

`0`、`0.1`、`0.25`、`0.5`、`0.75`、`0.9`、`1` のプリセットをワンクリックで適用できます。  
`Add` / `Add%` モードでは、`Shift + クリック` で負方向の値として適用できます。

プリセット値はアドオンプリファレンスで変更できます。

## 表示タブ

<p align="left">
  <img src="README_images/grid_tabs.png" alt="All Deform Other タブ" width="720">
</p>

- `All` : ボーン列と非ボーン頂点グループ列を表示します。
- `Deform` : ボーン名と一致する変形用の頂点グループ列だけを表示します。
- `Other` : ボーン名と一致しない非ボーン頂点グループ列だけを表示します。
- `非ボーン列を無視` を使うと、非ボーン頂点グループを合計・正規化・整理から外して扱えます。
- `非作成グループの表示` を使うと、対象メッシュにまだ存在しない頂点グループも一覧に表示できます。
- `非表示ワード` では、列名の表示だけを短くできます。実際の頂点グループ名は変更されません。

## 表示補助

<p align="left">
  <img src="README_images/display_tools.png" alt="表示補助ボタン" width="720">
</p>

- `モディ` : 対象メッシュの Armature モディファイア表示を切り替えます。
- `レスト` : 対象アーマチュアをポーズ位置 / レスト位置で切り替えます。
- `最前面` : アーマチュアの最前面表示を切り替えます。
- `オーバーレイ` : Blender の `Vertex Group Weights` 表示を切り替えます。
- `骨ハイ` : 選択列に対応するボーンを GPU オーバーレイ独自の表示でハイライトします。
- `マテリ` : ウェイトをマテリアルカラー風に表示する補助機能を切り替えます。

<p align="center">
  <img src="README_images/display_tools.gif" alt="表示補助の動作" width="720">
</p>

## 整理 / 検証

<p align="left">
  <img src="README_images/cleanup_tools.png" alt="整理と検証" width="720">
</p>

- `正規化` : 選択頂点のウェイト合計を 1.0 に整えます。
- `小数点` : ウェイト値を指定桁で整理します。
- `影響数` : 頂点あたりの最大影響数を上限に収めます。
- `閾値` : 指定値以下の弱いウェイトを 0 にします。
- `違反整理` : 正規化、小数点、閾値、影響数の設定を使ってまとめて整理します。
- `グループ削除` : 未使用の頂点グループを削除します。

合計ヘッダーの警告をクリックすると、影響数や合計値に問題がある頂点を優先して表示できます。

<p align="center">
  <img src="README_images/cleanup_tools.gif" alt="違反整理の動作" width="720">
</p>

## ブラシ

<p align="left">
  <img src="README_images/brush_tools.png" alt="GPUオーバーレイのブラシ" width="720">
</p>

GPU オーバーレイから、ビューポート上で使うウェイトブラシを開始できます。

- `通常` : 選択列へ加算 / 減算します。`Ctrl` で減算、`Shift` で一時スムーズになります。
- `スムーズ` : 選択列を周囲頂点になじませます。
- `グラデ` : ドラッグ方向に沿ってグラデーションを作成します。
- `投げ縄` : 囲んだ範囲を指定値で塗り、境界をブラシ幅でなじませます。
- `マスク` : ブラシの影響先を現在選択中の頂点だけに制限します。

<p align="center">
  <img src="README_images/brush_tools.gif" alt="ブラシ操作" width="720">
</p>

## スムーズ化 / ミラー

<p align="left">
  <img src="README_images/smooth_mirror.png" alt="スムーズ化とミラー" width="720">
</p>

### スムーズ化

選択頂点のウェイトを周囲へなじませます。  
詳細設定では、スムーズの強さ、回数、実行後の整理方法を調整できます。

<p align="left">
  <img src="README_images/smooth_settings.png" alt="スムーズ化設定" width="720">
</p>

### ミラー実行

選択頂点の反転位置を参照し、反対側の頂点からウェイトを持ってきます。  
`_L` / `_R` などの左右名も入れ替えて適用できます。

詳細設定では、ミラー方向、基準空間、検索距離、左右ワードセットを調整できます。

<p align="left">
  <img src="README_images/mirror_settings.png" alt="ミラー実行設定" width="720">
</p>

## コピー / 貼り付け / 転送

<p align="left">
  <img src="README_images/copy_paste_transfer.png" alt="コピー 貼り付け 転送" width="720">
</p>

- `頂点コピー` : 現在の頂点ウェイトをコピーします。
- `頂点貼付` : コピーした頂点ウェイトを選択頂点へ貼り付けます。
- `近接コピー` : 選択頂点の位置とウェイトを保存します。
- `近接貼付` : 近接コピー元から、貼り付け先に近いウェイトを転送します。
- `オブジェクト転送` : 選択順の最後に選択したアクティブオブジェクトから、他の選択オブジェクトへ最近傍でウェイトを転送します。

<p align="center">
  <img src="README_images/copy_paste_transfer.gif" alt="コピーと転送の動作" width="720">
</p>

### 列右クリックのウェイト転送

GPU オーバーレイの列ヘッダーを右クリックすると、頂点グループ間の転送メニューを開けます。

<p align="left">
  <img src="README_images/column_transfer_menu.png" alt="列右クリックのウェイト転送" width="720">
</p>

- `転送元に指定` : 右クリックした列を転送元にします。
- `この列へ転送` : 指定済みの転送元から、現在の列へ転送します。
- `複数ウェイト転送` : 転送元・転送先・処理方法・対象範囲を指定して転送します。
- `コピー` / `移行` / `置換` などの処理方法を選べます。
- 対象範囲は、グループ全体または選択頂点から選べます。
- 複数ペアを登録して、同じ処理方法でまとめて転送できます。

<p align="left">
  <img src="README_images/column_transfer_dialog.png" alt="複数ウェイト転送ダイアログ" width="720">
</p>

## 自動ウェイト

<p align="left">
  <img src="README_images/auto_weight.png" alt="自動ウェイト" width="720">
</p>

`自動ウェイト` は、選択メッシュをアーマチュアへ紐づけ、自動ウェイトを割り当てます。  
詳細設定では、Blender 公式の自動ウェイトと、独自ボクセル拡散方式を切り替えられます。

独自方式では、解像度、最大影響数、スムーズ、範囲補正プロキシなどを調整できます。

## 骨取得 / 骨トランスフォーム

<p align="left">
  <img src="README_images/bone_pick_transform.png" alt="骨取得と骨トランスフォーム" width="720">
</p>

### 骨取得

`骨取得` を使うと、ビューポート上のボーンをクリックして、そのボーン名の頂点グループ列を選択できます。  
GPU オーバーレイ表示中は、デフォルトで `Alt + 右クリック` からも骨取得を開始できます。

除外ワードを設定すると、`IK`、`FK`、`twist` などを含むボーンを骨取得の候補から外せます。

<p align="center">
  <img src="README_images/bone_pick.gif" alt="骨取得の動作" width="720">
</p>

### 骨トランスフォーム

選択列に対応する骨がある場合、GPU オーバーレイ上で骨の `位置`、`回転`、`スケール` を確認・編集できます。

- `位` : Location を編集します。
- `回` : Rotation を編集します。
- `ス` : Scale を編集します。
- 数値欄をクリックすると直接入力できます。
- 数値欄を横ドラッグすると値を変更できます。
- `Shift + ドラッグ` で微調整、`Ctrl + ドラッグ` で大きく変更できます。
- `↺` で現在の骨を元の値へ戻します。
- `Alt + ↺` で変更した全ボーンを元の値へ戻します。
- `右ドラッグ` で骨トランスフォームを変えるモードも切り替えられます。

<p align="center">
  <img src="README_images/bone_transform.gif" alt="骨トランスフォームの動作" width="720">
</p>

## X 方向の頂点選択

<p align="left">
  <img src="README_images/x_side_select.png" alt="X方向の頂点選択" width="720">
</p>

GPU オーバーレイから、アーマチュア原点を基準に `x-側` または `x+側` の頂点を選択できます。  
アーマチュアがない場合は、各オブジェクト原点を基準にします。中心線上の頂点は選択しません。

## N パネル

<p align="left">
  <img src="README_images/n_panel.png" alt="Nパネル" width="720">
</p>

基本操作は GPU オーバーレイから行えますが、N パネルにも同じ処理へアクセスするためのボタンがあります。

- `GPUオーバーレイ` の起動
- インフルエンス一覧、検索、除外ワード
- ロック / 無視 / 非作成グループ表示
- 編集設定、数値設定
- 正規化、整理、スムーズ化、ミラー実行
- コピー / 貼り付け / 自動ウェイト / ウェイト転送

## クイックパイメニュー

<p align="left">
  <img src="README_images/pie_menu.png" alt="クイックパイメニュー" width="720">
</p>

デフォルトでは `6` キーで従来のクイックパイメニューを開けます。  
GPU オーバーレイを閉じている状態でも、表示 / 更新、インフルエンス、スムーズ、ミラー、コピー、整理などへすばやくアクセスできます。

## ショートカット

| 操作 | デフォルト |
| --- | --- |
| GPU オーバーレイ表示 / 非表示 | `W` |
| GPU オーバーレイを閉じる | `W` / `Esc` |
| クイックパイメニュー | `6` |
| 選択列のウェイト加算 / 減算 | `Ctrl + ホイール` |
| 選択列のウェイト微調整 | `Ctrl + Shift + ホイール` |
| GPU オーバーレイ中の骨取得 | `Alt + 右クリック` |
| スムーズ化（任意ショートカット） | `Ctrl + Alt + S`（初期 OFF） |
| 骨からインフルエンス選択（任意ショートカット） | `Ctrl + Alt + B`（初期 OFF） |

ショートカットはアドオンプリファレンスから確認・変更できます。  
一部のショートカットはプリファレンスで ON / OFF を切り替えられます。

<p align="left">
  <img src="README_images/shortcut_preferences.png" alt="ショートカット設定" width="720">
</p>

## 補足

- GPU オーバーレイのグリッドは、基本的に選択頂点を対象に表示します。
- 重いメッシュでは、必要な頂点だけを選択してから `グリッド表示` を使うと軽く扱えます。
- ロック列、無視列、行ロックは、編集・正規化・整理の結果に影響します。
- マテリアル風ウェイト表示と Blender 標準の Vertex Group Weights 表示は、表示状態に応じて切り替えて使えます。
- 画像や GIF は `README_images/` フォルダに配置してください。

<!--
README_images に後から配置する想定の画像一覧:

Main.png
install_addon.png
enable_addon.png
open_gpu_overlay.png
quick_start.gif
gpu_overlay_layout.png
weight_grid.png
cell_edit.gif
locks_and_ignore.png
value_editing.png
presets.png
grid_tabs.png
display_tools.png
display_tools.gif
cleanup_tools.png
cleanup_tools.gif
brush_tools.png
brush_tools.gif
smooth_mirror.png
smooth_settings.png
mirror_settings.png
copy_paste_transfer.png
copy_paste_transfer.gif
column_transfer_menu.png
column_transfer_dialog.png
auto_weight.png
bone_pick_transform.png
bone_pick.gif
bone_transform.gif
x_side_select.png
n_panel.png
pie_menu.png
shortcut_preferences.png
-->
