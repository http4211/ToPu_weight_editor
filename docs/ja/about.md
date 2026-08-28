# その他

## blend ファイルへの変更について

このアドオンはネットワークにアクセスせず、外部プログラムの実行や Python パッケージのインストールも行いません。外部ファイルの読み書きは、`カラープリセットのインポート` / `エクスポート` を選んだときだけです。

一部の機能は、意図的に現在の blend ファイルを変更します。

- **専用エリア / ウィンドウ** : 識別情報とエリアタイプを Screen / Workspace に保存（OS ウィンドウ位置は保存しない）。
- **ウェイトスナップショット** : 圧縮してテキストデータブロックに保存（大きいとファイルサイズが増える）。
- **骨トランスフォーム** : 取り消し用データをテキストデータブロックとして作成し、不要なものは自動削除。
- **骨作成 / 骨とウェイトの分割** : アーマチュアへ骨を追加し、頂点グループのウェイトを再分配。
- **ウェイトカラープレビュー** : 専用のカラー属性を作成（`マテリアル置換` ON 時のみマテリアルを一時置換）。
- **レストポーズ適用** : レストデータ・座標・アクション・NLA 参照アニメーションを変更する可能性あり。実行前にバックアップを推奨。
- **自動ウェイト** : 計算中に一時データを作成し、終了時に削除。
- **オブジェクト転送** : 転送先に Armature モディファイアが無ければ追加できる（デフォルト ON）。

> 不具合の報告や再現用ファイルは [Issue トラッカー](https://github.com/http4211/ToPu_weight_editor/issues) へお願いします。

---

## ライセンス / サードパーティ表記

本体は GPL-3.0-or-later です。

- **Robust Weight Inpainting** : [RobustSkinWeightsTransferCode](https://github.com/rin-23/RobustSkinWeightsTransferCode)（Rinat Abdrashitov 氏、MIT ライセンス）をもとに Blender 向けに改変。libigl / Polyscope の同梱・要求はありません。原文表示は `LICENSES/RobustSkinWeightsTransferCode-MIT.txt`。
- **GPU オーバーレイのカラーパレット** : 20 種のビルトインパレットはユーザー提供の Blender テーマ拡張から取り込み。`Blender Dark` / `Blender Light` は Blender 標準のテーマ設定に基づきます。詳細は `LICENSES/BlenderThemePalette-Attributions.txt`。
