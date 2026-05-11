# IQS9151 `work_cb` ZTESTケース一覧（実装同期版）

この文書は `tests/iqs9151_work_cb/src/main.c` の現行ケースを
レビューしやすい一覧にしたものです。

## 前提

- 実行環境: `native_sim_64`（`native_sim` でも実行可能）
- テストフック: `CONFIG_INPUT_IQS9151_TEST=y`
- 観測対象:
  - 出力イベント (`KEY` / `REL`)
  - 内部状態 (`prev_finger_count`, inertia active, hold_button)

## 閾値（テスト前提）

- 共通:
  - `IQS9151_TAP_REENTRY_WINDOW_MS = 30`
- 1F:
  - `ONE_FINGER_TAP_MAX_MS = 120`
  - `ONE_FINGER_TAP_MOVE = 25`
  - `ONE_FINGER_TAPDRAG_GAP_MAX_MS = 230`
- 2F:
  - `TWO_FINGER_TAP_MAX_MS = 130`
  - `TWO_FINGER_TAP_MOVE = 30`
  - `TWO_FINGER_TAPDRAG_GAP_MAX_MS = 200`
  - `TWO_FINGER_SCROLL_START_MOVE = 50`
  - `TWO_FINGER_PINCH_START_DISTANCE = 80`
  - `TWO_FINGER_PINCH_WHEEL_DIV = 12`
- 3F:
  - `THREE_FINGER_TAP_MAX_MS = 180`
  - `THREE_FINGER_TAP_MOVE = 30`
  - `THREE_FINGER_TAPDRAG_GAP_MAX_MS = 230`
  - `THREE_FINGER_*_LEAD_MAX_MS = 120`
  - `THREE_FINGER_RELEASE_PENDING_MAX_MS = 150`

## ケース一覧（42件）

|No.|テスト名|主な確認点|
| - | - | - |
|1|`test_show_reset_releases_pinch_and_clears_state`|`SHOW_RESET` で BTN7 release と内部状態クリア|
|2|`test_one_finger_release_starts_cursor_inertia`|1Fリリースで cursor inertia 開始|
|3|`test_one_finger_release_after_stale_gap_does_not_start_cursor_inertia`|1F release が stale gap 超過なら cursor inertia 不発|
|4|`test_one_finger_release_after_slowdown_does_not_start_cursor_inertia`|release 直前に減速した 1F では cursor inertia 不発|
|5|`test_two_finger_scroll_reports_and_starts_scroll_inertia`|2Fスクロール出力 (`INPUT_REL_HWHEEL=-60`) と scroll inertia|
|6|`test_two_finger_scroll_release_after_stale_gap_does_not_start_inertia`|2F scroll release が stale gap 超過なら scroll inertia 不発|
|7|`test_new_one_finger_touch_cancels_scroll_inertia`|scroll inertia 動作中に新規 1F 接触 (`0->1`) で inertia 停止|
|8|`test_two_finger_scroll_tail_two_to_one_to_zero_suppresses_cursor_path`|2F Scroll終端の `2->1->0` では cursor `REL_X/Y` / inertia を抑止し、scroll inertia のみ開始|
|9|`test_two_finger_pinch_reports_btn7_and_wheel`|2Fピンチで BTN7 press/wheel/release (`wheel=6`)|
|10|`test_two_finger_pinch_tail_two_to_one_to_zero_suppresses_cursor_path`|2F Pinch終端の `2->1->0` では cursor `REL_X/Y` / inertia を抑止し、BTN7 release のみ行う|
|11|`test_two_finger_pinch_to_three_finger_releases_btn7`|2F pinch中 `2->3` 遷移で BTN7 release|
|12|`test_two_finger_tap_click_emits_btn1`|2Fタップで BTN1 click|
|13|`test_two_finger_tap_staggered_release_emits_btn1`|`2->1->0` 段階リリースで BTN1 click|
|14|`test_two_finger_tap_one_lead_finger_emits_btn1`|`1->2` one-lead で BTN1 click|
|15|`test_two_finger_tap_moved_one_lead_does_not_click`|移動済み one-lead は2Fタップ不成立|
|16|`test_two_finger_tap_jitter_no_pinch_emits_btn1`|軽微ジッターで2Fタップ成立（Pinch誤判定なし）|
|17|`test_two_finger_tap_releases_latched_hold`|2Fタップ時に既存 hold を解放|
|18|`test_one_finger_tap_defers_release_until_timeout`|1F TapでBTN0をpress保持し、timeoutでrelease|
|19|`test_one_finger_double_tap_emits_release_then_click`|1Fダブルタップで「1回目release + 2回目click」を出力|
|20|`test_one_finger_second_touch_drag_releases_on_finger_up`|2回目タッチ継続時はBTN0を保持し、UPでrelease|
|21|`test_one_finger_long_press_without_tapdrag_arm_does_not_emit_hold`|1回目タップ不成立の長押しはBTN0イベントなし|
|22|`test_one_finger_tap_releases_latched_hold`|1Fタップ時に既存 hold を解放|
|23|`test_two_finger_double_tap_emits_release_then_click`|2Fダブルタップで「1回目release + 2回目click」を出力|
|24|`test_two_finger_double_tap_one_lead_second_touch_emits_release_then_click`|2Fダブルタップの2回目 `0->1->2` one-lead でも「1回目release + 2回目click」|
|25|`test_two_finger_second_touch_drag_releases_on_finger_up`|2Fの2回目タッチ継続時はBTN1を保持し、全指UPでrelease|
|26|`test_two_finger_second_touch_drag_one_lead_keeps_hold_until_finger_up`|2F TapDragの2回目 `0->1->2` one-lead でも保持継続し、全指UPでrelease|
|27|`test_two_finger_second_touch_drag_two_to_one_reports_cursor_motion`|2F TapDragの `2->1` 遷移中も BTN1保持しつつ `REL_X/Y` を出力|
|28|`test_three_finger_tap_releases_latched_hold`|3Fタップ時に既存 hold を解放|
|29|`test_three_finger_double_tap_emits_release_then_click`|3Fダブルタップで「1回目release + 2回目click」を出力|
|30|`test_three_finger_second_touch_drag_releases_on_finger_up`|3Fの2回目タッチ継続時はBTN2を保持し、全指UPでrelease|
|31|`test_three_finger_second_touch_drag_staged_entry_keeps_hold_until_finger_up`|3F TapDragの2回目 `0->2->3` two-lead でも保持継続し、全指UPでrelease|
|32|`test_three_finger_second_touch_drag_three_to_one_reports_cursor_motion`|3F TapDragの `3->1` 遷移中も BTN2保持しつつ `REL_X/Y` を出力|
|33|`test_three_finger_tap_click_emits_btn2`|3Fタップで deferred press後にtimeout release|
|34|`test_three_finger_tap_staggered_release_emits_btn2`|`3->2->1->0` の3Fタップでも deferred press後にtimeout release|
|35|`test_three_finger_tap_one_lead_finger_emits_btn2`|`1->3` one-lead で deferred press後にtimeout release|
|36|`test_three_finger_tap_moved_one_lead_does_not_click`|移動済み one-lead は3Fタップ不成立|
|37|`test_three_finger_tap_two_lead_fingers_emits_btn2`|`2->3` two-lead で deferred press後にtimeout release|
|38|`test_three_finger_tap_moved_two_lead_does_not_click`|移動済み two-lead は3Fタップ不成立|
|39|`test_three_finger_tap_step_to_two_then_zero_avoids_btn1`|`3->2->0` で BTN2成立し BTN1誤発火なし|
|40|`test_three_finger_swipe_right_emits_btn3_click`|3F右スワイプで BTN3 click|
|41|`test_three_finger_swipe_continuous_touch_emits_once`|3F連続接触中のスワイプが1ショットのみ|
|42|`test_three_finger_swipe_left_continuous_touch_emits_once`|3F左スワイプでも連続接触中は1ショットのみ|

注: テスト総数は `42` 件です（2026-04-09 時点）。

## 補足

- 2F/3F Tap は `release_pending` により段階リリース (`2->1->0`, `3->2->1->0`, `3->2->0`) を許容。
- 3F Tap は `1->3` / `2->3` の lead 遷移を許容。
- 3F Swipe は `three_swipe_sent` ラッチで1ショット化し、
  3本指接触が続く間は再送しない。
- 各ケース開始前に `iqs9151_test_cancel_pending_work()` を呼び、
  前ケース由来の `k_work_delayable` をキャンセルして順序依存を防止する。
- 1Fは deferred-click 方式: 1回目TapでBTN0 press保持、2回目Touch判定またはtimeoutでrelease。
- 2F/3Fも deferred-click 方式: 1回目TapでBTN1/BTN2 press保持、2回目Touch判定またはtimeoutでrelease。

## 実行コマンド

```bash
cd zmk
west build -p -b native_sim_64 ../ShiniNet/zmk-driver-iqs9151/tests/iqs9151_work_cb -d ../artifacts/iqs9151_work_cb_test
west build -d ../artifacts/iqs9151_work_cb_test -t run
```
