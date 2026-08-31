# 2本指・3本指スクロールの診断ログ

## 慣性診断版（設定3専用、2026-08-31）

`Build inertia diagnostics (left split3 only)` を実行すると、
`inertia-diagnostics` 成果物に `lalapadgen2_left-split-3-inertia-diagnostics.uf2`
が生成される。**左側だけ**に適用する。右側、settings_reset、倍率、
センサー設定、指離しや慣性の判定ロジックは変更しない。

既存のGOUT（接触中の計算出力）に加えて、診断有効時のみ次を記録する。

- `GIREL version=1 seq/t/fc/history/enabled`: 実際のスクロール終了通知。
- `GIGATE kind=scroll t/reason/history/recent/gap/window/stale/min/speed`:
  慣性判定の実際の戻り箇所。reasonは `recent_samples` / `stale_gap` /
  `zero_total` / `direction_samples` / `slow` / `accepted`。
  gap=-1は履歴なし。speedは測定速度ではなく設定の最低速度。
- `GISTART seq/t/seed/active`: 開始関数呼出し後の慣性状態。
- `GIWORK seq/n/t/scroll/active/elapsed`: 慣性ワーカーの出力（クランプ前）。
  nはワーカー呼出しの連番。seqは最新接触フレームで、新しい接触連番ではない。
- `GIREPORT t/code/value/sync/rc`: 実際の入力報告APIの戻り値。
  code=6は横、8は縦。これは後段プロセッサーやHID/PC受信の成功証拠ではない。
- `GICANCEL reason=touch`: 通常の接触条件による実行中慣性の取消。
  すべての取消経路を網羅する記録ではない。

GIRELとGIGATEは同じデバイス時刻tで照合する。GIREPORTは実際の呼出し時刻。
PC側Raw Inputログとは時計が異なるため、厳密な1イベント対応を仮定しない。
Windows受信と同時取得し、2F/3Fを別々に、まず各1回の短いスワイプで比較する。
全指を離した後も数秒記録し、慣性の有無を確認する。

ログ追加による実時間への影響はあり得る。欠落やmessages droppedがある記録は
確定診断に使わない。GCFGの設定値は起動時読み戻しの再表示である。

## 診断版と通常版

診断版は `Build gesture diagnostics (left USB only)` ワークフローの
`gesture-diagnostics` 成果物にある `lalapadgen2_left-split-3-baseline.uf2`
（以前の診断版のファイル名は `lalapadgen2_left-gesture-diagnostics.uf2`）。
**左側にだけ**書き込む。右側は通常版のまま使う。settings_reset は使用しない。

指分離値の比較版（2/3/4）を使う場合は [自然な指配置での比較手順](gesture-split-comparison.md) を参照。

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

### 診断v2: 生データ・面積・強度・設定読み戻し

2026-08-31追加。センサー設定、感度、ジェスチャー処理は変更していない。
通常版のI2C読み取りは従来の28バイトのまま。診断版だけを72バイトに拡張し、
0x1014～0x105Bを1回のI2C読取りで取得する（7本分のスロット）。
別々の時点で指本数と面積を読む方式にはしていない。

各seqには従来の4行に加え、`GRAW` 1行と `GF` 7行が出る（合計12行）。

- `GRAW info`：0x1020の生フラグ。再校正、リセット等の調査用。
- `GRAW tp`：0x1022の生フラグ。下位4bit=指本数、bit5=認識数超過、bit6=ノイズによる周波数変更、
  bit7=飽和、bit8～14=各指の信頼度。後段の判定ではなくセンサーが返した値。
- `GF slot=1..7`：そのスロットの `xy`、`strength`（接触強度）、`area`（面積）、
  `confidence`（信頼度）。本数が減っても指が先頭へ詰め直されるとは限らないため、全7スロットを記録。
  65535の座標やconfidence=0も削除せず記録する。面積の単位は検出チャンネル数でmm²ではない。
- `GCFG version=2 source=boot rc=0`：起動時の設定読み戻し成功。
  起動時（初期設定・Kconfig上書き・ATIの後、イベントモード設定前）に実機の0x11E2～0x11F5を一度だけ読む。
  接触開始時に同じ保存値を再表示するため、途中からログ取得しても確認できる。
  常時の設定値を保証するものではない。`rc` が負の場合は取得失敗であり、設定値は表示しない。
- `GCFGV`：読戻しの `settings/rx/tx/max/split/confidence`。
  現行の書込み予定値は左側settings=0x28、rx=12、tx=13、max=3、split=3、confidence=20。
- `GCFGF`：解像度、座標フィルター、静止判定の移動しきい値、ジッターしきい値。

静止保持の再検証には、上記の取得コマンドを次のように変更する。

```powershell
.\tools\capture-gesture-log.ps1 -Port COM7 -Seconds 40 -OutputPath .\gesture-3f-sensor.log
```

開始直後の2秒は全ての指を離したまま待つ（古い受信ログを排出する）。
`Recording` と表示されたら、3本指を置いて3秒静止→2～3秒かけて横移動→全指を離して2秒待つ。
同じ左パッドで3回繰り返し、残り時間は触らず待つ。新しいログのGCFG version=2を確認し、
ファイル全体を共有する。実機での設定読み戻し成功とログ欠落の有無は、この取得結果で確認する。

ログ量と診断版のI2C転送時間は増えるため、通常版とはタイミングが異なり得る。
取得中にCOMポートを別アプリで開かないこと。先頭や末尾の途中行、欠けたseqは解析対象から除外する。

従来の4行の意味は以下のとおり。v2では上記の生データ8行も同じ `seq` に付く。
`t` はデバイスの起動後ミリ秒（32bit）。

- `GIN`: `fc`=finger_count、`f1v`=finger1_valid、`f1`=finger1_x,y、`f2v/f2`=2本目の有効性・座標。
- `GPRE`: 処理前の `a3`=three_active、`m3`=three_mode、`last3`=three_have_last、`sum3`=three_dx,dy。
- `GSTEP`: 処理後の上記状態と、実際に計算した `step2`（2本指重心差分）、`step3`（3本指のfinger1差分）。
- `GOUT`: resultの `started/active/scroll/ended` = scroll_started/scroll_active/scroll_x,y/scroll_ended。

`m3` は内部状態（0=未確定、1=横Scroll、2=縦Scroll、3=Action送信済み）であり、
エディターの保存モード値とは別物。

連続した無接触フレームは省略するが、指を離すフレームや3→2→3は記録する。
連番欠落・同じ連番の行欠落（v1は4行、v2は12行）・`messages dropped` はログ欠落を疑う。
連番はドライバー処理フレームの記録番号であり、センサー割り込みやI2C読取りの取りこぼしは証明できない。

まず `fc=3` の維持を確認し、次にstep3、最後にscrollを比較する。
無効座標や段階的な指離しではstepが0でも正常な場合がある。
このログは入力プロセッサーの縮小、軸処理、BLE転送、HIDレポート、Windows処理より**前**の値。
慣性ワーカーの出力も含まない。scrollが十分でも下流やWindowsを原因と断定せず、次の観測点を追加する。
3本指ゲインや重心化は今回変更しない。

公式参考: [ZMK v0.3 USB logging](https://github.com/zmkfirmware/zmk/blob/v0.3.0/docs/docs/development/usb-logging.mdx)
