# 表示補助

<img width="510" alt="Image" src="https://github.com/user-attachments/assets/fb306577-a3d4-467f-8ba0-261e4183ef3d" />

<p align="left">
  <img width="1380" alt="Image" src="https://github.com/user-attachments/assets/e0581f1f-0fc1-4dc9-8fab-e7d581c1d296" />
</p>

- `モディ` : Armature モディファイア表示（ポーズ変形）を切り替え。
- `レスト` : アーマチュアをポーズ位置 / レスト位置で切り替え。
- `最前面` : アーマチュアの最前面表示を切り替え。
- `オーバーレイ` : Blender の頂点グループウェイト表示を切り替え。
- `骨ハイ` : アクティブ頂点グループ（無い場合は選択列）に対応するボーンを、編集 / ウェイトペイント時だけハイライト。ON 状態は保存されます。
- `マテリ` : ウェイトカラープレビューを切り替え。横の `…` で色（色相 / 彩度 / 輝度）とマテリアル置換を設定。

<p align="center">
  <img src="https://raw.githubusercontent.com/http4211/ToPu_weight_editor/main/README_images/display_tools.gif" alt="表示補助の動作">
</p>

### ウェイトカラープレビュー

<p align="center">
  <img width="332" alt="image" src="https://github.com/user-attachments/assets/c92a022d-92b4-486b-990c-a56aa7ea6098" />
</p>

`マテリ` で、ウェイトをカラー表示するプレビューを切り替えます。

- 専用の一意な名前のカラー属性を作成します（同名のユーザー属性は上書き・削除しません）。
- `マテリアル置換`（デフォルト OFF）: ON のときだけマテリアルスロットを一時的に置き換え、解除時に元へ復元。共有メッシュでは置換をスキップ。

> ※ `マテリ` 表示は動作が重くなるため、常用は推奨しません。
