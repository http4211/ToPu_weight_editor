# 編集

<p align="left">
  <img width="97" height="110" alt="image" src="https://github.com/user-attachments/assets/6ed02355-6c1f-4a9a-8922-f1d12c5de4de" />
</p>

`編集` セクションには、`x-` / `x+` と、`スムーズ化` / `ミラー実行` / `骨作成` / `レストポーズ適用` があります。

### X 方向の頂点選択

<img width="53" height="25" alt="Image" src="https://github.com/user-attachments/assets/b50216db-62f4-4d14-b880-35172f970311" />

<p align="left">
  <img width="1304" height="758" alt="Image" src="https://github.com/user-attachments/assets/e224cfe8-1ec2-4d8d-92ce-7dbead312eb4" />
</p>

アーマチュア原点（無い場合はオブジェクト原点）を基準に、`x-` 側または `x+` 側の頂点を選択します。

- 通常クリック : 中心線上の頂点は選択しません。
- `Shift + クリック` : 中心線上の頂点も選択します。

### スムーズ化

<img width="296" height="163" alt="Image" src="https://github.com/user-attachments/assets/9b1fc7b0-366f-4646-b56b-dacad2702608" />

<p align="left">
  <img width="1236" height="764" alt="Image" src="https://github.com/user-attachments/assets/ba09f7df-ebff-4b3c-886e-9c563eec4936" />
</p>

選択頂点のウェイトを周囲へなじませます。

- 通常クリック : 選択頂点をスムーズ化。
- `Shift + クリック` : 選択列のウェイト範囲全体と外側 1 リングを自動スムーズ。
- `Ctrl + クリック` : 周囲を基準に異常なウェイトを修正。
- 右隣の `…` : 対象範囲・方式（`高速` / `表面` / `ボリューム`）・回数・実行後の整理方法を調整。

### ミラー実行

<img width="484" height="459" alt="Image" src="https://github.com/user-attachments/assets/b6c7b993-1e28-4ab3-925b-db2b697cd7b8" />

<img width="340" height="232" alt="Image" src="https://github.com/user-attachments/assets/b0c1e84f-6dbd-4a73-9186-fa0eee9e6912" />

<p align="left">
  <img width="1354" height="762" alt="Image" src="https://github.com/user-attachments/assets/f45e4116-7cf0-4867-9eca-9b5b7fdc8ead" />
</p>

反転位置の反対側からウェイトを持ってきます。`_L` / `_R` などの左右名も入れ替えて適用されます。

- 通常クリック : 選択頂点をミラー。
- `Ctrl + クリック` : 方向を選んで、対象オブジェクト全体（または選択頂点のみ）をミラー。
- 右隣の `…` : 詳細設定（方向・基準空間・検索距離・中央補正・中央許容・左右ワードセット）を開く。

補足。

- 左右非対称の形状にも対応します（近傍サーフェスへ投影して補間。詳細設定で無効化可）。
- 反対側の頂点グループが無くても、対応する反対側ボーンがあれば自動作成します（対応ボーンが無い場合は作成 / スキップを確認）。
- **中央 L/R 均等化**（デフォルト ON）: 中心軸上の頂点の L/R ウェイトを自動で均等化します。ミラー詳細の `中央頂点L/R補正` を OFF にするとこの均等化だけを省略できます。

### 骨作成

<p align="left">
  <img width="459" height="508" alt="image" src="https://github.com/user-attachments/assets/53b3d388-e046-4716-915d-9f0663bf8ec5" />
  <img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/752b69ab-1cc3-4801-9613-42bcd4463eb1" />
</p>

編集モードで選択した辺から、骨列または分岐した骨ツリーを作成します。

- 通常クリック : 選択辺に合う作成方法を自動判断し、確認ダイアログを開く（閉じた辺ループ / 開いた辺列 / 辺リング / 分岐辺に対応）。
- `Ctrl + クリック` : `骨作成設定`（初期設定）を開く。
- 骨の向きは、最後に選択したアクティブ辺が先端になります。
- `骨数` `方向を反転`（分岐時は `分岐数` も）は、確認ダイアログと `F9` から調整できます。確認ダイアログでは、自動ウェイト・作成先・名前・接続・ロール基準・作成後のモードも変更できます。
- 複数の開いた辺列 : `中心軸` OFF で各辺列に独立した骨列、ON で中央に 1 本の骨列を作成します。

`自動ウェイト`（確認ダイアログ内）: 作成した骨だけで対象範囲にウェイトを割り当てます（`Blender 公式` / `Voxel Heat Skinning`）。`既存ウェイトを置き換え` を有効にすると、選択頂点の既存ボーンウェイトを消してから割り当てます（骨以外のグループは残る）。

> 対象範囲は、基本的に選択した頂点です。ただし複数の辺ループでメッシュを挟むように選択した場合は、ループの間に挟まれた頂点もまとめてウェイト付けされます。選択とつながっていない別メッシュには影響しません。

`ボーンロール基準` : `自動軸` / `選択辺の面方向` / `メッシュのローカルZ` / `メッシュのローカルY` / `ワールドZ` / `ワールドY`。

#### 骨とウェイトの分割

<p align="left">
  <img width="440" height="311" alt="image" src="https://github.com/user-attachments/assets/f674e8d4-612d-4ff7-bc64-723289b3a73b" />
</p>

`骨作成` ボタンを `Shift + クリック` すると、既存の骨を連続した骨列へ分割し、対応する頂点グループのウェイトを再分配します。

- 対象 : 選択ボーン（ポーズ / オブジェクト / アーマチュア編集モード）、または TPWE のアクティブ列と同名の骨（メッシュ編集モード）。
- `分割数`（2〜64）と `スムーズ`（分割骨間の遷移幅、デフォルト `0`）を指定。
- `ミラー`（デフォルト ON）: 左右ワードセットを使って反対側も同じ設定で分割。
- 実行後は `F9` から `分割数` `スムーズ` `ミラー` を再調整できます。

### レストポーズ適用

<p align="left">
  <img width="1302" height="768" alt="Image" src="https://github.com/user-attachments/assets/9f61975e-ab08-4fa3-a47d-47aefd04bfdf" />
</p>

現在の見た目のポーズを、新しいレストポーズとして適用します。アクションとシェイプキーのリターゲットに対応しています。

> ※ アーマチュアのレストデータ、メッシュ / シェイプキーの座標、アクション、NLA 参照のアニメーションを変更する可能性があります。**実行前に必ずバックアップを取ってください。**
