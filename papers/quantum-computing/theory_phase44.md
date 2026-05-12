# Phase 44: Surface code と ITU modular flow ― threshold の数値検証

## 1. 動機

Phase 43 で [[5,1,3]] 完全コードを fault-tolerant primitive として確立した。
しかし実用 量子計算は数百〜数百万 qubit の体系を要する。

**Surface code** (Kitaev 2003) は現代の主要 fault-tolerant 候補:
- 2D 格子, 近傍相互作用のみ
- threshold $p_c \approx 1\%$ (depolarizing)
- IBM, Google, Microsoft が採用中

本 Phase で:
1. Surface code の ITU modular-flow 解釈
2. 数値 threshold 測定
3. ITU 由来 decoder の可能性

を示す。

## 2. Toric code (surface code の最小形)

### 2.1 構造

- $L \times L$ 周期格子 (トーラス上)
- qubit はエッジ上に配置 ($2L^2$ qubits)
- 2 種類の stabilizer:
  - **Star** $A_v = \prod_{e \in v} X_e$ (vertex 周りの 4 X)
  - **Plaquette** $B_f = \prod_{e \in f} Z_e$ (face 周りの 4 Z)
- 論理 qubits: 2 (toroidal loops)
- Code distance: $L$

### 2.2 ITU との対応

Toric code の基底状態:
$$|\psi_0\rangle = \prod_v \frac{1 + A_v}{\sqrt{2}} |0\cdots 0\rangle$$

これは**長距離絡み合った状態** で:
- エンタングルメント entropy = $L \log 2 - \gamma_{\rm topo}$
- $\gamma_{\rm topo} = \log 2$ (topological entanglement)

ITU Phase 5 で示した: バルクの局所性 = QECC.
Toric code はこの**離散的実現**で、トーラス位相 → 2 論理 qubits 保護。

ITU 流の解釈:
> **Surface code の threshold は、modular Hamiltonian $K_A$ の固有値 gap が
> noise の典型エネルギー scale を上回る限界に対応する。**

## 3. Threshold 定理 (Aharonov-Ben-Or 1996)

Physical error rate $p < p_c$ ならば、$L$ を大きくすれば logical error rate
$\to 0$:
$$p_{\rm logical}(L) \sim (p/p_c)^{L/2}$$

つまり**指数抑制**。これは ITU 流に:
> noise が code structure (modular flow eigenspace) を破る確率が threshold 以下

なら、コード長を伸ばすと**情報が完全に保護される**。

## 4. 数値検証計画

### Part A: Toric code 実装
- $L = 3, 5$ の 2 サイズ
- qubits, stabilizers の構造を構築
- syndrome 計算

### Part B: ビット反転ノイズシミュレーション
- 各 qubit に確率 $p$ で X エラー
- syndrome 測定 (Z stabilizers)
- 簡易 decoder で訂正
- logical error 判定 (横断的 Z chain か?)

### Part C: Threshold 抽出
- $p$ を 0.01 〜 0.20 で scan
- $L = 3, 5$ で logical error rate 比較
- 交差点 = empirical $p_c$
- 理論値 ~11% (perfect MWPM) との比較

### Part D: ITU modular flow との対応
- Toric code stabilizers の commutation 構造
- これが modular Hamiltonian の固有空間構造と一致することを確認
- ITU 由来の decoder 重み付け案

## 5. 限界

⚠️ 本 Phase で扱わない:
- 完全 MWPM 実装 (naive decoder のみ)
- Z error / depolarizing noise (X-only)
- 測定エラー (qubit memory のみ)
- 巨大格子 ($L \geq 9$ は計算重い)

✅ 確立する:
- Surface code の数値 threshold (~10%)
- 距離 $L$ 拡大による error 抑制
- ITU との形式的対応

## 6. Phase 45-46 への展望

| Phase | テーマ |
|---|---|
| **44 (本論文)** | **Surface code threshold** |
| 45 | Magic state distillation (universality) |
| 46 | NISQ-era hardware 応用 |

Phase 43-46 完成で「ITU and Fault-Tolerant Quantum Computing」 が Tier 1 論文として完成形。
