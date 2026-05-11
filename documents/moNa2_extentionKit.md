# moNa2拡張キットの使い方

- 本ドキュメントでは、トラックパッドをmoNa2に組み込む手順を解説します。
- ここでは、moNa2の右手側にあるトラックボールはそのまま残し、左手側のロータリーエンコーダーをトラックパッドへ換装する方法を例として紹介します。
- ZMKのビルド手順など、基本的な説明は省略しています。

- トラックパッドモジュール本体は[Boothで入手可能](https://shininet.booth.pm/)です。（準備中）
- アダプターモジュール（3DP製）は[MakerWorldでデータ公開中](https://makerworld.com/ja/@ShiniNet/upload)です。（準備中）

![IMG_20260328_142403](https://github.com/user-attachments/assets/b126c955-8b99-423a-8c96-8f6632046878)

<BR/><BR/>

## moNa2のロータリーエンコーダーを取り外す

<img width="1024" height="656" alt="2026-03-28_12h59_17" src="https://github.com/user-attachments/assets/dfb5ea6e-5524-4737-b1b7-7d198c763d27" />

<BR/><BR/>

## マイコンとブレークアウトボードを配線図に従って接続する

<img width="400" alt="2026-03-28_13h04_34" src="https://github.com/user-attachments/assets/cf80116f-213e-45b1-8a8f-b9e2cc02021b" />

<img width="1364" height="768" alt="2026-03-28_13h05_04" src="https://github.com/user-attachments/assets/4325f1ed-6ac9-4a4c-bd48-980a10305c29" />

<BR/><BR/>

## ブレークアウトボードを適当な両面テープなどでマイコンに固定する

<img width="1546" height="612" alt="2026-03-28_13h06_03" src="https://github.com/user-attachments/assets/5b2d5b46-96d8-4b8f-9ca0-415f64dc7259" />

<BR/><BR/>

## アダプターパーツ（3DP製）を使ってトラックパッドをmoNa2に固定する

<img width="2760" height="1005" alt="2026-03-28_13h09_22" src="https://github.com/user-attachments/assets/169c2c7a-a760-433d-b83a-7343e776ee6d" />

<img width="1547" height="789" alt="2026-03-28_13h09_55" src="https://github.com/user-attachments/assets/4253c42e-0e73-4162-aba6-892b91022766" />

<BR/><BR/>

## ファームウェアをセットアップする

- ShiniNetが作成した[moNa2ファームウェアのフォーク](https://github.com/ShiniNet/zmk-config-moNa2-v2_TP/actions/runs/23678787056)から、最新のUF2ファイルを取得します。
- moNa2にファームウェアを書き込みます。

> [!TIP]
> - 自分のmoNa2フォークに組み込みたい場合は、[コミットログ](https://github.com/ShiniNet/zmk-config-moNa2-v2_TP/commit/7e83a23ea202d5694ea33503b81cd67133515d6f)を参考に変更を取り込んでください。
<BR/><BR/>

## 動作確認（デフォルト機能のみ）

- ビルドと書き込みの後、1～2本指スワイプによるポインタ移動とスクロールを確認します。
- 1～3本指タップによる左クリック・右クリック・中クリック、およびタップドラッグを確認します。
- 3本指の左右スワイプで、マウスボタン4/5（戻る/進む）が出力されることを確認します。

> [!TIP]
> - トラックパッドの使い方や全機能の詳細については[LaLaPad Gen2の解説](https://github.com/ShiniNet/LaLaPadGen2/blob/main/guide/HowtoUse.md#%E3%83%88%E3%83%A9%E3%83%83%E3%82%AF%E3%83%91%E3%83%83%E3%83%89%E3%81%AE%E6%A9%9F%E8%83%BD)を参考にしてください。

> [!WARNING]
> - 本ガイドはあくまでクイックスタートであり、トラックパッドの全機能を利用するにはDTSやコンフィグの拡張が必要です。

