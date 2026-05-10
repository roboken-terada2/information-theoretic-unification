# Phase 5: ホログラフィック量子誤り訂正と創発バルク

## 1. 動機

Phase 1-4 で空間・時間・重力・双曲バルクが情報構造から創発した。
最後のピースは「**バルクのテンソルネットワーク表現が、境界 CFT における量子誤り訂正符号 (QECC) として機能する**」という発見 (Almheiri-Dong-Harlow 2014)。
これは AdS/CFT 対応の最も深い量子情報理論的解釈であり：

> 時空 ≅ 量子状態の冗長な符号化 ≅ 誤り訂正符号

## 2. ADH の定理 (略式)

AdS/CFT のバルク場 $\phi(x)$ は、エンタングルメント wedge $\mathcal{E}_A$ ($A$ は境界領域) 内に位置するなら**境界 $A$ の作用素**として再構成できる：
$$\phi_{\text{bulk}}(x) \cong \mathcal{O}_A \in \text{Algebra}(A) \quad \text{if } x \in \mathcal{E}_A.$$

異なる境界領域から同じバルク作用素が再構成できる**冗長性**は QECC の論理作用素の特徴。

**Petz 回復写像**：誤り後の境界状態 $\rho_A$ から元のバルク状態を確率1で復元する具体的な量子操作。

## 3. 完全テンソル符号 [[5,1,3]]

ホログラフィー対応の最小モデルとして、5量子ビット完全符号を使う。
- 物理量子ビット 5 = 境界の各点
- 論理量子ビット 1 = バルクの1点
- 距離 3 = 任意の 1 量子ビット誤りを訂正

スタビライザ生成元：
$$g_1 = X Z Z X I,\quad g_2 = I X Z Z X,\quad g_3 = X I X Z Z,\quad g_4 = Z X I X Z.$$
論理作用素：$\bar X = X^{\otimes 5},\quad \bar Z = Z^{\otimes 5}$。

**完全テンソル性 (perfect tensor)**：5脚テンソル $T_{ijklm}$ をどの方法で 2-3 分割しても同型 (isometry)。
$\Rightarrow$ 任意の 2量子ビットの reduced state は最大混合 $I/4$ 。

## 4. 創発 RT 相転移

論理量子ビットを参照系 $R$ と Bell ペアにし、論理側を [[5,1,3]] で符号化:
$$|\Phi\rangle_{LR} = \frac{1}{\sqrt 2}(|0\rangle_L|0\rangle_R + |1\rangle_L|1\rangle_R) \xrightarrow{\text{encode}} |\tilde\Phi\rangle = \frac{1}{\sqrt 2}(|\bar 0\rangle|0\rangle_R + |\bar 1\rangle|1\rangle_R).$$

任意の境界部分集合 $A \subset \{1,...,5\}$ に対し、相互情報量を計算：
$$I(A : R) = S(A) + S(R) - S(AR).$$

**主張 (= ADH の数値版)**：
$$I(A:R) = \begin{cases} 0 & \text{if } |A| \leq 2 \\ 2\log 2 & \text{if } |A| \geq 3. \end{cases}$$

これは Ryu-Takayanagi の**離散版相転移**：バルク量子ビットは「境界の大きい方の半分」のエンタングルメント wedge に属する。
- $|A| \geq 3$ → バルクは $A$ の wedge → $A$ から復号可能、$R$ と相関
- $|A| \leq 2$ → バルクは $A^c$ の wedge → $A$ には情報なし、$I(A:R)=0$

## 5. Petz 回復写像の存在

距離 3 の符号なので、任意の 2量子ビット誤りは syndrome から検出 (or 1量子ビット誤りは訂正) できる。
3 量子ビットだけ持っていれば、Petz 写像で論理量子ビットを完全復元できる：
$$\mathcal{R}_A^{\sigma} \circ \mathcal{N}_{A^c}(\rho_L) = \rho_L \quad (|A| \geq 3).$$

これは「**バルク作用素 $\bar X, \bar Z$ は3量子ビット部分集合上の作用素として表現できる**」と同値。

## 6. 大きな描像 (情報理論的統一理論との繋がり)

| Phase | 創発する物 | 符号化原理 |
|---|---|---|
| 1 | 空間 (S¹) | 相互情報量 = 距離 |
| 2 | 線形化Einstein | エンタングルメント第1法則 |
| 3 | 双曲バルク (AdS₃) | MERA 階層 = 双曲タイル |
| 4 | 時間 | モジュラーフロー σ_t^ω |
| 5 | **バルクの局所性** | **境界 QECC の冗長性** |

最終的に、Phase 5 は:
> 「時空の各点は、境界量子状態の論理作用素として実装される」

を主張する。これは **It from Qubit** プログラムが目指す究極の同一視であり、Phase 1-4 で個別に見てきた創発現象を**統一する原理**。

## 7. 本シミュレーションの計画

1. [[5,1,3]] の codeword $|\bar 0\rangle, |\bar 1\rangle$ を構築 (32 次元 Hilbert)
2. 論理-参照 Bell ペア $|\tilde\Phi\rangle$ を 6 量子ビット系で構成
3. 全 $2^5 = 32$ 通りの境界部分集合 $A$ について $I(A:R)$, $S(A)$ を計算
4. **完全な階段関数**：$|A| \leq 2$ で $I=0$、$|A| \geq 3$ で $I=2$ ビットの確認
5. 完全テンソル性確認 ($S(A) = \min(|A|, 5-|A|) \log 2$ の純粋部分)
6. ペンタゴン上の幾何的可視化 (バルク中央、境界5点、エンタングルメント wedge)
