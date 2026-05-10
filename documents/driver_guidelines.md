# ZMK（Zephyr）用ドライバ開発方針  
**（Codex Agent 参照用）**

---

## 0. 本ドキュメントの目的

本ドキュメントは、ZMK（Zephyr）向けドライバ開発において  
**設計方針・依存関係・実装ルールを 明示する** ことを目的とする。

---

## 1. 前提条件

### 1.1 ZMK / Zephyr バージョン

- 対象 ZMK バージョン：**ZMK 3.0**
- 依存 Zephyr バージョン：**Zephyr 3.5.x**


## 2. 基本設計思想（最重要）

### 2.1 レイヤード設計

ドライバは以下の層構造を意識して実装する。

[ Hardware Driver (Zephyr) ]
↓
[ ZMK Adapter Layer ]
↓
[ ZMK Event / Input System ]

- Zephyr 依存部と ZMK 依存部を論理的に分離する
- ZMK 依存コードは最小限に抑える

---

## 3. Zephyr 側ドライバ設計方針

### 3.1 Driver Model

- `DEVICE_DT_DEFINE` / `DEVICE_DT_INST_DEFINE` を使用する
- `struct device` を前提とした設計とする
- 初期化優先度（init priority）は明示的に指定する

### 3.2 API 使用ルール

- GPIO / I2C / SPI は必ず **Zephyr API 経由**
- SoC HAL の直接呼び出しは禁止
- deprecated API を使用してはならない

### 3.3 実行コンテキスト

- IRQ ハンドラ内では最小限の処理のみ行う
- 実処理は `k_work` / `k_work_delayable` に委譲する
- IRQ コンテキストでのブロッキング処理は禁止

---

## 4. DeviceTree（DTS）依存設計

### 4.1 基本ルール

- 物理情報は **すべて DeviceTree から取得**
- GPIO 番号や IRQ 極性の直書きを禁止
- I2C / SPI 設定は DTS に集約する

### 4.2 DTS マクロ使用

- `DT_INST_*` マクロを使用する
- `compatible` 名を明確に定義する
- ボード固有差分は Config 側で上書き可能とする

---

## 5. ZMK 依存部分の設計方針

### 5.1 ZMK との接続方法

- ZMK とは **イベント送信のみ** で接続する
- ZMK 内部状態（レイヤー、モード等）を直接参照しない

### 5.2 使用可能 API（例）

- `input_report_key`
- `input_report_rel`
- ZMK Event Manager 経由のイベント送出

### 5.3 禁止事項

- ZMK 内部構造体の直接操作
- グローバル状態への直接依存
- 将来の ZMK 内部仕様に依存するハック

---

## 6. 設定値と Kconfig 方針

- バッファサイズ・周期・感度などは **Kconfig 化** する
- マジックナンバーをコード中に記述しない
- デフォルト値は保守的に設定する

---

## 7. ハードウェア依存の扱い

### 7.1 原則

- 特定 MCU / ボード前提の実装は禁止
- GPIO / I2C / SPI は必ず抽象化する

### 7.2 許容される依存

- DeviceTree によるボード差分
- Kconfig による条件分岐

---
