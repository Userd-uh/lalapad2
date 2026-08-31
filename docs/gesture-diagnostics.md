# 2本指・3本指スクロールの診断ログ

## 診断版と通常版

診断版は `Build gesture diagnostics (left USB only)` ワークフローの
`gesture-diagnostics` 成果物にある `lalapadgen2_left-gesture-diagnostics.uf2`。
**左側にだけ**書き込む。右側は通常版のまま使う。settings_reset は使用しない。

左側では2本指・3本指の横方向がともに Scroll。右側の2本指横方向は Action のため、
今回は設定を変更せず左側で比較する。左右でセンサー挙動が違う可能性は残るため、
左側で再現しない場合は右側の別検証が必要。

通常の `build.yaml` は診断設定を読み込まない。診断コードは
`CONFIG_INPUT_IQS9151_GESTURE_DIAGNOSTICS=y` の場合だけコンパイルされる。
通常版のジェスチャーモード、ゲイン、キー割当、Studio設定は変更していない。
診断対象の左側では USB CDC をログ用に使用し、Studioを無効化する。
右側のStudioは通常どおりだが、比較中は設定を変えないこと。

## Windowsでの取得手順

1. 左側のリセットを素早く2回押してブートローダーを開き、診断UF2をコピーする。
2. **左側をデータ通信対応USBケーブルでPCへ接続**する。右側も電源を入れ、通常の左右接続を保つ。
   左側のログは右側のUSBには転送されない。右側のPC接続方法も比較中は変えない。
3. デバイスマネージャーの「ポート(COMとLPT)」で左側のCOM番号を確認する。
   抜き差しで増減するポートを特定する。ブートローダーではなく通常起動後の番号を使う。
4. そのポートを使うシリアルモニターなどを閉じる。PowerShellで以下を実行する。
   `COM7` は確認した番号に置き換える。保存先ファイルが既にある場合は別名にする。

```powershell
cd D:\project\keyboard\lalapad2\lalapad2
.\tools\capture-gesture-log.ps1 -Port COM7 -Seconds 30 -OutputPath .\gesture-2f.log
.\tools\capture-gesture-log.ps1 -Port COM7 -Seconds 30 -OutputPath .\gesture-3f.log
```

最初の30秒間に2本指、次の30秒間に3本指で、同じ左トラックパッドを左→右へ
同じ距離・速さで各5回程度動かす。毎回完全に指を離し、1秒程度間を空ける。
同じレイヤー・同じアプリで比較し、比較中はキーを押さない。
最後に2ファイルと「使ったレイヤー・アプリ・体感差」を共有する。
診断版でも差が再現するか確認すること。ログ有効時はタイミング・消費電力が変わり得る。

スクリプト実行がポリシーで禁止される場合は、既存のPuTTYのSerial接続
（同じCOM番号、115200、Flow control=None）で Session > Logging > All session output
を指定して保存してもよい。システムの実行ポリシーを変更する必要はない。

取得後は通常版の**左側UF2**に戻す。右側や settings_reset の書き込みは不要。

## ログの読み方・限界

同一 `seq` の4行で1フレーム。`t` はデバイスの起動後ミリ秒（32bit）。

- `GIN`: `fc`=finger_count、`f1v`=finger1_valid、`f1`=finger1_x,y、`f2v/f2`=2本目の有効性・座標。
- `GPRE`: 処理前の `a3`=three_active、`m3`=three_mode、`last3`=three_have_last、`sum3`=three_dx,dy。
- `GSTEP`: 処理後の上記状態と、実際に計算した `step2`（2本指重心差分）、`step3`（3本指のfinger1差分）。
- `GOUT`: resultの `started/active/scroll/ended` = scroll_started/scroll_active/scroll_x,y/scroll_ended。

`m3` は内部状態（0=未確定、1=横Scroll、2=縦Scroll、3=Action送信済み）であり、
エディターの保存モード値とは別物。

連続した無接触フレームは省略するが、指を離すフレームや3→2→3は記録する。
連番欠落・同じ連番の4行欠落・`messages dropped` はログ欠落を疑う。
連番はドライバー処理フレームの記録番号であり、センサー割り込みやI2C読取りの取りこぼしは証明できない。

まず `fc=3` の維持を確認し、次にstep3、最後にscrollを比較する。
無効座標や段階的な指離しではstepが0でも正常な場合がある。
このログは入力プロセッサーの縮小、軸処理、BLE転送、HIDレポート、Windows処理より**前**の値。
慣性ワーカーの出力も含まない。scrollが十分でも下流やWindowsを原因と断定せず、次の観測点を追加する。
3本指ゲインや重心化は今回変更しない。

公式参考: [ZMK v0.3 USB logging](https://github.com/zmkfirmware/zmk/blob/v0.3.0/docs/docs/development/usb-logging.mdx)
