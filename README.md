# ToPu_weight_editor

<p align="center">
  <img width="663" height="601" alt="Image" src="https://github.com/user-attachments/assets/606d5cb3-e8ab-49b4-b5fd-49a571b353ac" />
</p>

ToPu_weight_editor は、Blender 上でスキンウェイトを確認・編集するためのアドオンです。  
Softimage 風のウェイト編集をベースに、3D ビュー上へ表示される **GPU オーバーレイ** から、ウェイトの数値編集、正規化、整理、スムーズ、ミラー、コピー&ペースト、転送、骨取得、表示補助までをまとめて操作できます。

## できること

- 編集モードとウェイトペイントモードの両方で、GPU オーバーレイからウェイトを確認・編集
- 選択頂点を軽量なセル表示で一覧化し、3D ビューを見ながら数値を直接調整
- セル、スライダー、プリセット、ブラシによる直感的なウェイト編集
- 正規化、小数点整理、影響数制限、閾値整理、違反整理
- スムーズ化、ミラー実行、コピー&ペースト、近接転送、頂点グループ間転送
- 骨取得、ボーンハイライト、骨トランスフォーム、表示補助の切り替え

## 動作環境

- Blender 4.0 以降

外部ウィンドウではなく Blender の 3D ビュー上に GPU オーバーレイを描画して動作します。
追加の UI ライブラリは不要です。

型番の古いCPU,GPUでの環境ではシステムのグラフィックス表示が`Vulkan`の場合パフォーマンスが落ちる現象を確認しています。
その場合は、システムのグラフィックス表示を`OpenGL`にしたら改善する可能性があります。

## インストール

### 1. ZIP をインストール

Blender の `編集 > プリファレンス > アドオン` を開き、`ディスクからインストール` で配布 ZIP を選択します。


### 2. アドオンを有効化

アドオン一覧で `ToPu_weight_editor` を有効化します。  
有効化すると、3D ビューのツールヘッダーにアイコンボタンとサイドバーに `TPWE` タブが追加されます。


## 起動方法

### ツールヘッダーから起動

3D ビューのツールヘッダーに表示される `GPUオーバーレイ` アイコンを押すと、GPU オーバーレイを表示できます。  
もう一度押すと閉じられます。

<p align="center">
  <img width="1248" height="792" alt="Image" src="https://github.com/user-attachments/assets/3948c27f-098b-4f10-9b65-1c2aa2b9dd14" />
</p>

### ショートカットで起動

デフォルトでは `W` キーで GPU オーバーレイの表示 / 非表示を切り替えられます。  
GPU オーバーレイを閉じるときは `W`、または `Esc` を使います。

### N パネルから起動

ツールヘッダーアイコンが非表示の場合は、`N` キーでサイドバーを開き、`TPWE` タブの `GPUオーバーレイ` からも起動できます。

## クイックスタート

1. メッシュを編集モード、またはウェイトペイントモードにします。
2. 編集したい頂点を選択します。
3. ツールヘッダーのアイコン、または `W` キーで GPU オーバーレイを表示します。
4. GPU オーバーレイの `グリッド表示` を ON にします。
5. 列ヘッダーをクリックして、編集したい頂点グループを選択します。
6. セル、スライダー、数値欄、プリセットボタン、ブラシ、スムーズ、でウェイトを調整します。
7. 最後に `正規化`、`小数点`、`影響数`、`閾値`、`違反整理` でウェイトを整えます。

## GPU オーバーレイ

### 全体レイアウト

<p align="center">
  <img width="960" height="742" alt="Image" src="https://github.com/user-attachments/assets/cfed90dc-1609-49cb-912e-18e6a7f3e460" />
</p>

- 上部の `ドラッグで移動` をドラッグすると、GPU オーバーレイの位置を動かせます。
- 右上のリサイズハンドルをドラッグすると、表示サイズを変更できます。
- `グリッド表示` で選択頂点のウェイト表を表示します。
- 歯車ボタンからアドオンプリファレンスを開けます。
- 行数・列数は スクロールバー、またはホイール操作で調整できます。

### ウェイトグリッド

**列ヘッダー**

<p align="center">
  <img width="1346" height="790" alt="Image" src="https://github.com/user-attachments/assets/e5329a73-88bd-48c9-92db-512e42d478b0" />
</p>

- 列ヘッダーをクリックすると、その列が選択列になります。
- `Shift + 列クリック` で、その頂点グループに値が入っている頂点をまとめて選択します。
- `Ctrl + 列クリック` で、現在選択中の頂点の中から、その列に値が入っている頂点だけを残します。
- 列ヘッダーを右クリックすると、ウェイト転送メニューを開けます。

**個/ 頂点 / 合計**

<img width="149" height="30" alt="Image" src="https://github.com/user-attachments/assets/20e5f137-204f-4693-84a6-e9f5455eb703" />

<p align="center">
  <img width="1192" height="762" alt="Image" src="https://github.com/user-attachments/assets/f7cb13e9-7c26-41e1-940a-8ba1be68b235" />
</p>

- `個` ヘッダーをクリックすると、対象の行の値がロックされます。
- `頂点`ヘッダーをクリックすると、その頂点行がビュー上でハイライト表示され、グリッド上で常に表示状態になります。
- `Shift` / `Ctrl` を押しながらドラッグやクリックで、行選択を追加・解除できます。
- `個/頂点`ヘッダーをクリックすると、選択中の頂点すべてを対象にします。
- `個/頂点`を`alt+クリック`すると全ての対象の状態が解除されます。
- `合計`ヘッダーをクリックすると、影響数や合計値に問題がある頂点を優先して表示できます。



**セル**

<p align="center">
  <img width="1184" height="758" alt="Image" src="https://github.com/user-attachments/assets/d40e61e9-ae42-4cf0-b916-46545d88c886" />
</p>

- セルをクリックすると、そのセルの数値を直接入力できます。`Enter` で確定、セルを`右クリック`でキャンセル/セルの選択を解除。
- 複数セルを選択している場合は、入力値を選択セルへまとめて適用できます。
- セルをドラッグして範囲選択できます。`Shift` / `Ctrl` を押しながら操作すると、選択セルの追加・解除ができます。
- 選択セルがある状態でスライダーやプリセットを使うと、選択列全体ではなく選択セルを優先して編集します。


<p align="center">
  <img src="README_images/cell_edit.gif" alt="セル編集" width="720">
</p>

### ロック/無視/強制表示

<img width="156" height="26" alt="Image" src="https://github.com/user-attachments/assets/7d078ee1-5d84-48fb-b533-4b6c889e2c08" />

<p align="left">
  <img width="1192" height="766" alt="Image" src="https://github.com/user-attachments/assets/5d1c7790-e614-45b6-8d47-9243c6fb875a" />
</p>

- `ロック` は、選択列を編集できない状態にします。
- `無視` は、対象列を合計・正規化・整理の対象外として扱います。
- `強制表示` は、0 ウェイトの列でもグリッドに強制表示します。
- `Shift + Click` で選択列以外を対象に作用します。
- `Alt + Click` で対象の状態をすべて解除します。


### 入力モード/スライダーと数値欄

<img width="693" height="37" alt="Image" src="https://github.com/user-attachments/assets/56fd28a7-e82b-4c60-a4ee-034649542502" />

<p align="left">
  <img width="1188" height="756" alt="Image" src="https://github.com/user-attachments/assets/82048644-d3f9-4210-9808-25a44b92cd93" />
</p>

- `Abs` : 入力した値で置き換えます。
- `Add` : 現在値に加算します。負の値で減算できます。
- `Add%` : 現在値に対して割合で加算します。
- スライダーをドラッグすると、選択列へ値を即時適用します。
- 数値欄をクリックすると、キーボードから直接入力できます。
- 数値欄の上でホイールすると、値を少しずつ変更できます。
- `適用` ボタンで、数値欄の値を選択頂点の現在列に適用します。

### プリセットボタン

<img width="280" height="28" alt="Image" src="https://github.com/user-attachments/assets/463b655c-5b92-4641-89bd-a3abeff80b92" />

<img width="473" height="101" alt="Image" src="https://github.com/user-attachments/assets/061633e4-e2cf-471f-b9ad-c0c0ed909aaa" />

<p align="left">
  <img width="1188" height="764" alt="Image" src="https://github.com/user-attachments/assets/df656172-edbc-4420-9059-4b3932b18cf3" />
</p>

`0`、`0.1`、`0.25`、`0.5`、`0.75`、`0.9`、`1` のプリセットをワンクリックで適用できます。  
`Add` / `Add%` モードでは、`Shift + クリック` で負方向の値として適用できます。

プリセット値はアドオンプリファレンスで変更できます。

## 骨取得 / 骨トランスフォーム/最大ウェイト列を追従

### 骨取得/最大ウェイト列を追従

<img width="339" height="195" alt="Image" src="https://github.com/user-attachments/assets/a12b4d19-3c24-4d61-b7e5-18f19bf57710" />

<img width="109" height="24" alt="Image" src="https://github.com/user-attachments/assets/3257c432-2a43-482e-8eef-dddd109b300b" />



<p align="left">
  <img width="1218" height="758" alt="Image" src="https://github.com/user-attachments/assets/4324d885-a267-470a-b215-f4b7ef63ed39" />
</p>

`骨取得` を使うと、ビューポート上のボーンをクリックして、そのボーン名の頂点グループ列を選択できます。  
GPU オーバーレイ表示中は、デフォルトで `Alt + 右クリック` からも骨取得を開始できます。

除外ワードを設定すると、`IK`、`FK`、`twist` などを含むボーンを骨取得の候補から外せます。

 
 `▣↖`がオンの場合選択頂点が変化した時、選択範囲で最もウェイト値が高い頂点グループ列を自動選択します。  
 頻繁に頂点を切り替えながら主影響ボーンを確認する作業に向きます。






<p align="center">
  <img src="README_images/bone_pick.gif" alt="骨取得の動作" width="720">
</p>

### 骨トランスフォーム

<img width="532" height="28" alt="Image" src="https://github.com/user-attachments/assets/18661bf8-2ccc-4e3c-9481-de04e75502ae" />

<p align="left">
  <img width="1314" height="756" alt="Image" src="https://github.com/user-attachments/assets/0b5ab8d2-1abd-4378-9fcc-268317d0ef22" />
</p>

選択列に対応する骨がある場合、GPU オーバーレイ上で骨の `位置`、`回転`、`スケール` を確認・編集できます。

- 左端の `↱` ボタンで、ビューポート上の右ドラッグ編集を ON / OFF できます。
- `↱` が ON のとき、ビューポート上で右ドラッグすると、現在選択している骨トランスフォーム値を画面方向に合わせて変更できます。
- 右ドラッグ中に `Shift` を押すと微調整、`Ctrl` を押すと大きめの変更になります。
- 右ドラッグを OFF にしたい場合は、もう一度 `↱` をクリックします。
- 右ドラッグは、モデルを見ながらポーズを少し動かしてウェイトの効き方を確認したいときに使います。
- `位` : Location を編集します。
- `回` : Rotation を編集します。
- `ス` : Scale を編集します。
- 数値欄をクリックすると直接入力できます。
- 数値欄を横ドラッグすると値を変更できます。
- `Shift + ドラッグ` で微調整、`Ctrl + ドラッグ` で大きく変更できます。
- `↺` で現在の骨を元の値へ戻します。
- `Alt + ↺` で変更した全ボーンを元の値へ戻します。



## 表示タブ

<img width="724" height="25" alt="Image" src="https://github.com/user-attachments/assets/d9a3ea5b-4ce8-4942-994f-391fd78fc45b" />

<p align="left">
  <img width="1186" height="764" alt="Image" src="https://github.com/user-attachments/assets/5a7eba2d-79fc-47c2-8886-716c0944f700" />
</p>

- `すべて` : ボーン列と非ボーン頂点グループ列を表示します。
- `変形` : ボーン名と一致する変形用の頂点グループ列だけを表示します。
- `その他` : ボーン名と一致しない非ボーン頂点グループ列だけを表示します。
- `非ボーン列を無視` : 「すべて」タブのオプション、非ボーン頂点グループを自動的に無視状態にして合計・正規化・整理から外して扱えます。
- `作成済み常時` : 「その他」タブのオプション。作成済みの非ボーン頂点グループ列を常に表示します。
- `不正規許可` : 「その他」タブのオプション。合計が1異様でも違反扱いにせず、正規化ONでも正規化しません。
- `非表示ワード` : では、列名の表示だけを短くできます。実際の頂点グループ名は変更されません。

## 表示補助

<img width="510" height="24" alt="Image" src="https://github.com/user-attachments/assets/fb306577-a3d4-467f-8ba0-261e4183ef3d" />

<p align="left">
  <img width="1380" height="980" alt="Image" src="https://github.com/user-attachments/assets/e0581f1f-0fc1-4dc9-8fab-e7d581c1d296" />
</p>

- `モディ` : 対象メッシュの Armature モディファイア表示を切り替えます。
- `レスト` : 対象アーマチュアをポーズ位置 / レスト位置で切り替えます。
- `最前面` : アーマチュアの最前面表示を切り替えます。
- `オーバーレイ` : Blender の `Vertex Group Weights` 表示を切り替えます。
- `骨ハイ` : 選択列に対応するボーンを GPU オーバーレイ独自の表示でハイライトします。
- `マテリ` : ウェイトをマテリアルカラー風に表示する補助機能を切り替えます。
- `マテリ`の横の`…` で色相/彩度/輝度/マテリアルモード用のマテリアル変更のオンオフが設定できます。
- ※`マテリ`表示は動作が重くなるため推奨していません。

<p align="center">
  <img src="README_images/display_tools.gif" alt="表示補助の動作" width="720">
</p>

## 整理 /自動整理(基準)

<p align="left">
  <img width="192" height="117" alt="Image" src="https://github.com/user-attachments/assets/13d54963-ecdb-4838-b3fe-1aef5015a16b" />
</p>

- `正規化` : 選択頂点のウェイト合計を 1.0 に整えます。
- `小数点` : ウェイト値を指定桁で整理します。
- `影響数` : 頂点あたりの最大影響数を上限に収めます。
- `閾値` : 指定値以下の弱いウェイトを 0 にします。
- `違反整理` : 正規化、小数点、閾値、影響数をまとめて整理します。
- `グループ削除` : 未使用の頂点グループを削除します。
- オブジェクトモードで実行した場合、そのオブジェクトの頂点全てに実行します。


<p align="left">
<img width="519" height="26" alt="Image" src="https://github.com/user-attachments/assets/416d1946-2607-42b6-a038-2b816687af63" />
</p>
↑ここで決めた値が整理実行での基準になります。

チェックを入れた項目はアドオンで値を変更する際に自動で整理されるようになります。

※自動整理は確実ではないため最後に確認をして違反整理などの実行を推奨します。


## ブラシ

<p align="left">
  <img width="192" height="111" alt="Image" src="https://github.com/user-attachments/assets/2e57f831-8509-4954-81cc-e75aed5e66c3" />
</p>

GPU オーバーレイから、ビューポート上で使う TPWE 独自のウェイトブラシを開始できます。  
ブラシは編集モードとウェイトペイントモードの両方で使用できます。
併用して、骨取得や骨トランスフォームも実行できるため、ウェイト作業がが迅速にできます。


ブラシ中は `F` でサイズ変更、`Tab` / `Q` / `Esc` で元のツールへ戻れます。  
ツールヘッダーでは、サイズ、選択マスク、通常量、スムーズの強さ、グラデ値、投げ縄値などを調整できます。

### 通常ブラシ

<img width="436" height="27" alt="Image" src="https://github.com/user-attachments/assets/714c3d89-c99d-47ab-b348-2b36a4712cb2" />

<p align="left">
  <img width="898" height="764" alt="Image" src="https://github.com/user-attachments/assets/51d508d6-5c53-45cc-88a1-5d793de41f40" />
</p>

`通常` は、選択列のウェイトをブラシで加算 / 減算する基本ブラシです。

- 左ドラッグで選択列へ加算します。
- `Ctrl + 左ドラッグ` で減算します。
- `Shift + 左ドラッグ` で一時的にスムーズ処理になります。
- `通常量` で 1 ストロークあたりの変化量を調整できます。
- `一定塗` : 1 回のドラッグ中に同じ頂点へ何度も当たっても、重ね塗りされすぎないように塗ります。狙った量だけ安定して足したいときに向いています。
- `重ね塗` : ブラシが当たるたびに現在値へ `通常量` を加算 / 減算します。何度もなぞって徐々に強くしたいときに向いています。


### スムーズブラシ

<img width="625" height="29" alt="Image" src="https://github.com/user-attachments/assets/52c425a0-aeec-4080-9798-5170c5fdb615" />

<p align="left">
  <img width="1268" height="762" alt="Image" src="https://github.com/user-attachments/assets/fe1cc575-10d5-49c8-884a-3b3351182f5a" />
</p>

`スムーズ` は、選択列のウェイトを周囲の頂点になじませるブラシです。

- 左ドラッグした周辺のウェイトをなめらかにします。
- `強さ` でどれだけ周囲へ寄せるかを調整できます。
- `回数` でスムーズ処理の反復回数を調整できます。
- 塗り跡が硬い部分、段差が出た部分、ミラー後の境界を整える用途に向いています。

### グラデーションブラシ

<img width="640" height="24" alt="Image" src="https://github.com/user-attachments/assets/a15031da-149f-49f5-84be-c73567c54603" />

<p align="left">
  <img width="1234" height="756" alt="Image" src="https://github.com/user-attachments/assets/df2d5bc8-1fbb-4c8d-90ff-31e5a5a0b02a" />
</p>

`グラデ` は、ドラッグ方向に沿ってウェイトのグラデーションを作るブラシです。

- ドラッグ開始位置から終了位置に向かって、選択列のウェイトを変化させます。
- `グラデ値` で最大ウェイト値を調整できます。減衰カーブに沿って、この値から 0 へ変化します。
- `Ctrl` を押しながら実行すると減算方向、`Shift` を押しながら実行すると加算方向として使えます。
- `リニア` : ドラッグ方向へ 1 から 0 の直線的なグラデーションを作ります。
- `放射` : ドラッグ開始点を中心に、外側へ向かって弱くなる放射状のグラデーションを作ります。
- `線放射` : ドラッグした線を基準に、線方向と反対方向へ広がるグラデーションを作ります。
- `減衰` では値の落ち方を切り替えられます。`リニア` は均等、`スムーズ` は自然なS字、`球状` は柔らかめ、`ルート` は開始側を広め、`シャープ` は開始側から強めに落ちます。
- `カスタム` 減衰では `カスタム指数` で`0.1~8`の間で落ち方を調整できます。`1` がリニア、`2` 以上で急減衰、`1` 未満で緩やかになります。

### 投げ縄ブラシ

<img width="384" height="27" alt="Image" src="https://github.com/user-attachments/assets/4756f60d-3580-463b-bf3a-96aeaafadef0" />

<p align="left">
  <img width="1154" height="796" alt="Image" src="https://github.com/user-attachments/assets/9c2046e0-adc7-49cd-98e2-7e854064ee5f" />
</p>

`投げ縄` は、囲んだ範囲を指定値で塗るブラシです。

- 左ドラッグで範囲を囲むと、その内側へ `投げ縄値` を適用します。
- ブラシサイズは、範囲の境界をなじませる幅として使われます。
- 広い範囲を一気に 0、0.5、1.0 などへそろえたい場面に向いています。

### 選択マスク

<p align="left">
  <img width="1208" height="772" alt="Image" src="https://github.com/user-attachments/assets/4c9e47f7-afae-4fa9-9dfe-8d135c61ee2d" />
</p>

`マスク` を ON にすると、ブラシの影響先を現在選択中の頂点だけに制限します。

- 近い別パーツや裏側の頂点へ意図せず塗るのを防ぎやすくなります。
- 先に編集したい頂点だけを選択してから ON にすると、ブラシ作業の範囲を安定させられます。
- 通常、スムーズ、グラデ、投げ縄の各ブラシで共通して使えます。

<p align="center">
  <img src="README_images/brush_tools.gif" alt="ブラシ操作" width="720">
</p>




## 編集

<p align="left">
  <img width="98" height="109" alt="Image" src="https://github.com/user-attachments/assets/b5a71567-3cdc-4ca8-b371-c59428e4c4a8" />
</p>


### X 方向の頂点選択

<img width="53" height="25" alt="Image" src="https://github.com/user-attachments/assets/b50216db-62f4-4d14-b880-35172f970311" />

<p align="left">
  <img width="1304" height="758" alt="Image" src="https://github.com/user-attachments/assets/e224cfe8-1ec2-4d8d-92ce-7dbead312eb4" />
</p>

GPU オーバーレイから、アーマチュア原点を基準に `x-側` または `x+側` の頂点を選択できます。  
アーマチュアがない場合は、各オブジェクト原点を基準にします。中心線上の頂点は選択しません。


### スムーズ化


<img width="296" height="163" alt="Image" src="https://github.com/user-attachments/assets/9b1fc7b0-366f-4646-b56b-dacad2702608" />

<p align="left">
  <img width="1236" height="764" alt="Image" src="https://github.com/user-attachments/assets/ba09f7df-ebff-4b3c-886e-9c563eec4936" />
</p>

選択頂点のウェイトを周囲へなじませます。  
詳細設定では、稼働方式、スムーズの強さ、回数、実行後の整理方法を調整できます。  
稼働方式は 高速/表面/ボリューム　の三つから選択できます。


### ミラー実行


<img width="484" height="459" alt="Image" src="https://github.com/user-attachments/assets/b6c7b993-1e28-4ab3-925b-db2b697cd7b8" />

<img width="340" height="232" alt="Image" src="https://github.com/user-attachments/assets/b0c1e84f-6dbd-4a73-9186-fa0eee9e6912" />

<p align="left">
  <img width="1354" height="762" alt="Image" src="https://github.com/user-attachments/assets/f45e4116-7cf0-4867-9eca-9b5b7fdc8ead" />
</p>

選択頂点の反転位置を参照し、反対側の頂点からウェイトを持ってきます。  
`_L` / `_R` などの左右名も入れ替えて適用できます。

詳細設定では、ミラー方向、基準空間、検索距離、左右ワードセットを調整できます。  
左右ワードセットはアドオンプリファレンスからでも設定できます。  



### レスト位置変更

<p align="left">
  <img width="1302" height="768" alt="Image" src="https://github.com/user-attachments/assets/9f61975e-ab08-4fa3-a47d-47aefd04bfdf" />
</p>

`レスト位置変更` は、現在のポーズを新しいレストポーズとして適用する機能です。

- 現在のポーズを基準姿勢として保存できます。
- ボーン配置を調整した後、その状態を新しいレスト姿勢にしたい場合に使用します。
- 実行前にバックアップを取ることをおすすめします。

## ウェイトコピー

<img width="165" height="108" alt="Image" src="https://github.com/user-attachments/assets/ef71a5b2-b587-4898-bbdc-6eb6a670ac43" />

<p align="left">
  <img width="1042" height="770" alt="Image" src="https://github.com/user-attachments/assets/b8453e66-c226-46db-b887-b2e01a3a3042" />
</p>

- `頂点コピー` : 現在アクティブに選択している一つの頂点ウェイトをコピーします。
- `頂点貼付` : コピーした頂点ウェイトを選択頂点へ貼り付けます。
- `近接コピー` : 選択頂点の位置とウェイトを保存します。
- `近接貼付` : 近接コピー元から、貼り付け先に近いウェイトを転送します。
- `オブジェクト転送` : 選択順の最後に選択したアクティブオブジェクトから、他の選択オブジェクトへ最近傍でウェイトを転送します。
                      （少し重いですが、通常の転送に比べ面ベースで転送するためローポリでも比較的きれいに転送されます。）

## 自動ウェイト


<img width="552" height="381" alt="Image" src="https://github.com/user-attachments/assets/6f5d9511-81a5-4bed-84a8-b8a937823c8e" />

<img width="340" height="260" alt="Image" src="https://github.com/user-attachments/assets/fedcfce4-9335-4db3-9a95-fba6fbe8c92f" />

<p align="left">
  <img width="1406" height="958" alt="Image" src="https://github.com/user-attachments/assets/ecde6c2a-a6d8-4069-81aa-55582c799c53" />
</p>

`自動ウェイト` は、選択メッシュをアーマチュアへ紐づけ、自動ウェイトを割り当てます。  
親子関係を維持しながら実行でき、またリンクオブジェクトがある場合、自動でローカル化できます。  
選択頂点の部位だけを部分的に自動ウェイトでウェイト付けすることなどが可能です。  

詳細設定では、Blender 公式の自動ウェイトと、独自ボクセル拡散方式を切り替えられます。

独自方式では、解像度、最大影響数、スムーズ、範囲補正プロキシなどを調整できます。  
非常に重いのですが、メッシュの表裏など関係なく、空間をボックス上にしてウェイト付けを行っているため複雑なモデルでも綺麗にウェイトが付きやすいです。


## 列右クリックのウェイト転送


<img width="517" height="246" alt="Image" src="https://github.com/user-attachments/assets/61f1ca69-668d-49d1-96f2-128bed527655" />

<img width="205" height="125" alt="Image" src="https://github.com/user-attachments/assets/4fb738b0-aad8-4714-93ca-a4320140b8db" />

<p align="left">
  <img width="571" height="1024" alt="Image" src="https://github.com/user-attachments/assets/7d405982-882b-4299-a31f-460828fcdfae" />
</p>


GPU オーバーレイの列ヘッダーを右クリックすると、頂点グループ間の転送メニューを開けます。



- `転送元に指定` : 右クリックした列を転送元にします。
- `この列へ転送` : 指定済みの転送元から、現在の列へ転送します。
- `複数ウェイト転送` : 転送元・転送先・処理方法・対象範囲を指定して転送します。
- `コピー` / `移行` / `置換` などの処理方法を選べます。
- 対象範囲は、グループ全体または選択頂点から選べます。
- 複数ペアを登録して、同じ処理方法でまとめて転送できます。


## N パネル

<p align="left">
  <img width="274" height="1141" alt="Image" src="https://github.com/user-attachments/assets/610a168d-f1e8-44fa-a1be-e26c0a79dce3" />
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
  <img width="1119" height="528" alt="Image" src="https://github.com/user-attachments/assets/84eed356-69b6-45c2-beee-6696df63a906" />
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
brush_normal.png
brush_smooth.png
brush_gradient.png
brush_lasso.png
brush_mask.png
smooth_mirror.png
smooth_settings.png
mirror_settings.png
copy_paste_transfer.png
copy_paste_transfer.gif
column_transfer_menu.png
column_transfer_dialog.png
auto_weight.png
bone_pick.png
bone_pick.gif
bone_transform_panel.png
bone_transform.gif
x_side_select.png
n_panel.png
pie_menu.png
shortcut_preferences.png
-->
