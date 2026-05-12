# Phase 45: Magic state distillation の ITU 解釈

## 1. 動機

Phase 43 ([[5,1,3]] code) と Phase 44 (surface code) で fault-tolerant な
**Clifford gate** の実装を確立した。しかし**完全な universal QC** には
non-Clifford gate (例: $T = \mathrm{diag}(1, e^{i\pi/4})$) が必要。

問題: **stabilizer code は Clifford gate しか transversal に実装できない**
(Eastin-Knill theorem 2009)。

解: **magic state distillation** (Bravyi-Kitaev 2005)
- "noisy" magic state $|T\rangle = (|0\rangle + e^{i\pi/4}|1\rangle)/\sqrt 2$ を準備
- 蒸留 (distillation) でエラー率を**指数抑制**
- 純粋 magic state → T gate teleportation で universal QC 達成

本 Phase で:
1. Magic state distillation の数値実証
2. ITU 流の解釈
3. 「**magic = non-stabilizer 情報量**」 を ITU 枠組みで定式化

## 2. Magic state とは

### 2.1 Stabilizer 部分理論

Stabilizer formalism (Gottesman 1997):
- Clifford gate (H, S, CNOT) + Pauli 測定で表現可能な subset of QC
- 古典的に効率的シミュレート可能 (Gottesman-Knill 定理)
- **計算的に強くない** (BPP より強くない)

→ **Universal QC には non-stabilizer 操作が必要**。

### 2.2 Magic state

$T$ gate を「外部」から供給する状態:
$$|T\rangle = T|+\rangle = (|0\rangle + e^{i\pi/4}|1\rangle)/\sqrt 2$$

これを teleportation で消費すれば T gate が実装される。

### 2.3 Bravyi-Kitaev 5-to-1 蒸留

5 つの noisy magic state (error rate $\epsilon_{\rm in}$) を
[[5,1,3]] 符号 (Phase 43!) で**蒸留**:
- Stabilizer 測定で post-selection
- 出力: 1 つの清浄な magic state
- 誤差: $\epsilon_{\rm out} \approx 5 \epsilon_{\rm in}^2$ (二次抑制)

**Threshold**: $\epsilon_{\rm in} < \epsilon_{\rm th} = 1/5 = 0.20$ なら iteration で $\epsilon \to 0$.

15-to-1 (Reed-Muller code) なら:
- $\epsilon_{\rm out} \approx 35 \epsilon_{\rm in}^3$ (三次抑制)
- Threshold $\epsilon_{\rm th} \approx 0.14$

## 3. ITU との対応

### 3.1 「Magic = non-stabilizer 情報量」

ITU Phase 5 は QECC = stabilizer 構造を扱う。
**Magic** は **stabilizer 部分理論から逸脱する情報量** ― すなわち:

| ITU 概念 | Stabilizer 部分理論 | Magic |
|---|---|---|
| 情報 | 古典シミュレート可能 | 真に量子 |
| エンタングルメント | 計算 entanglement | "magic entanglement" |
| QECC | code subspace 保護 | non-stabilizer 拡張 |
| ITU 公理 $\delta S = \delta\langle K\rangle$ | 直接適用可 | 別解釈必要 |

### 3.2 Magic resource の情報理論

Robustness of magic (Howard-Campbell 2017):
$$\mathcal{R}(\rho) = \min_{\rho = \sum c_i \sigma_i} \sum |c_i|, \quad \sigma_i \in \text{stab}$$

これは「**stabilizer 凸結合からの距離**」を測る情報量。

ITU 流に解釈:
> **Magic = ITU の K_A 固有空間外の情報量**

つまり QECC が保護する情報 (stabilizer subspace) **以外**の自由度が
magic として現れる。これは ITU が**完全に量子計算を覆う**ためには
必要な追加構造。

### 3.3 蒸留 = 非自明 QECC

Magic state distillation は通常の QECC とは異なる:
- 入力: 同種の状態を多数 ($N$ copies)
- 出力: より清浄な 1 つ
- 「**符号化 → 復号化**」 ではなく「**フィルタリング**」

ITU 流の見方:
> **蒸留 = stabilizer code (QECC) の non-stabilizer 拡張**
> [[5,1,3]] symmetry を利用して magic 資源を精製。

## 4. 数値検証計画

### Part A: 5-to-1 蒸留シミュレーション
- 5 つの noisy magic state (各 error rate $\epsilon$)
- [[5,1,3]] stabilizer 測定 + post-selection
- 出力 magic state の error rate を測定

### Part B: 二次抑制の確認
- $\epsilon_{\rm in}$ vs $\epsilon_{\rm out}$ のスケーリング
- 予想: $\epsilon_{\rm out} \sim c\, \epsilon_{\rm in}^2$
- 係数 $c \sim 5$ を確認

### Part C: 反復蒸留での指数収束
- 初期 $\epsilon_0$ から複数ラウンド
- $\epsilon_n \to 0$ if $\epsilon_0 < \epsilon_{\rm th}$
- Threshold $\epsilon_{\rm th} = 1/c \approx 0.2$

### Part D: ITU と Tier 0 の繋がり
- [[5,1,3]] が Phase 43 で使った同じ code
- ITU 単一公理から code が出る (Phase 5)
- その code が distillation にも使える
- ITU の「単一原理」 が QC の Clifford + non-Clifford 両方を統合

## 5. 限界

⚠️ 本 Phase で扱わない:
- 完全量子状態シミュレーション (確率モデルのみ)
- 測定エラー (perfect measurement 仮定)
- T gate teleportation の詳細回路
- Universal gate set の完全構築
- Reed-Muller 15-to-1 (5-to-1 のみ)

✅ 確立する:
- 5-to-1 distillation の二次抑制
- 反復による指数収束
- ITU 流の magic = non-stabilizer 解釈
- Phase 43 の [[5,1,3]] が non-Clifford 領域にも応用可能

## 6. Phase 46 への展望

| Phase | テーマ |
|---|---|
| 43 ✅ | [[5,1,3]] 完全コード |
| 44 ✅ | Surface code threshold |
| **45 (本論文)** | **Magic state distillation** |
| 46 | NISQ-era hardware 応用 |

Phase 45 完成で **universal fault-tolerant QC** の理論的枠組みが ITU から派生。
Phase 46 で実装現実性を議論し、Tier 1 論文「ITU and Quantum Computing」 が完成形。
