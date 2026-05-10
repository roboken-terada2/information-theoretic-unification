# Phase 10: 物質場の創発 — 標準模型ゲージ対称性 SU(3)×SU(2)×U(1)_Y

## 1. 動機

Phase 1-9 で時空・重力・時間・宇宙論的進化を量子情報構造から導いた。残された大課題は **物質場 (素粒子) の創発** — 標準模型のゲージ群 SU(3)_c × SU(2)_L × U(1)_Y がどこから来るか。

中心アイディア (Maldacena-Witten 1998 [hep-th/9803131]):
> **境界 CFT の任意の大域対称性 G は、バルク重力理論のゲージ群 G と双対**

ここで境界の保存カレント $J^\mu_a$ ($a$ は群指標) はバルクのゲージ場 $A^\mu_a$ と1対1対応する。

したがって本 Phase の目標は：**標準模型のゲージ群を大域対称性として持つ境界 CFT を量子情報の枠組み内で構成する**こと。

## 2. 6フレーバー自由フェルミオン = 左手クォーク二重項 QL

標準模型における左手クォーク二重項 QL は表現 $(3, 2, 1/6)$:
- SU(3)_c で **3 重項** (3 色: r, g, b)
- SU(2)_L で **2 重項** (アップ型 u, ダウン型 d)
- U(1)_Y で**ハイパーチャージ** $Y = 1/6$

合計内部自由度 $3 \times 2 = 6$。これを **6 フレーバー自由フェルミオン**

$$H = -\sum_{i,\alpha} (c_{i,\alpha}^\dagger c_{i+1,\alpha} + \mathrm{h.c.}), \quad \alpha = (\text{color}, \text{isospin}) \in \{1,...,6\}$$

として実装する。

## 3. ゲージ生成子の構成

6 次元フレーバー空間 = 3 色 ⊗ 2 同位スピン に対し、標準模型生成子は以下：

### 3.1 SU(3)_c (8 個)

Gell-Mann 行列 $\lambda^A$ ($A = 1,...,8$, $\mathrm{Tr}\,\lambda^A \lambda^B = 2\delta^{AB}$) を用い:
$$T^A_{\rm color} = \frac{\lambda^A}{2} \otimes \mathbb{1}_2, \quad A = 1,...,8.$$

### 3.2 SU(2)_L (3 個)

Pauli 行列 $\sigma^a$ ($a=1,2,3$) を用い:
$$T^a_{\rm weak} = \mathbb{1}_3 \otimes \frac{\sigma^a}{2}, \quad a = 1,2,3.$$

### 3.3 U(1)_Y (1 個)

ハイパーチャージ:
$$T^Y = \frac{1}{6} \mathbb{1}_6.$$

合計 $8 + 3 + 1 = 12$ 個の生成子。これは $\mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1)$ の 12 次元 Lie 代数を張る。

### 3.4 Tr 正規化

正規化: $\mathrm{Tr}(T^A T^B) = \delta_{AB}$ (各群内で)、群間は 0:

| | SU(3) | SU(2) | U(1)_Y |
|---|---|---|---|
| SU(3) | $\delta_{AB}$ | 0 | 0 |
| SU(2) | 0 | $\delta_{ab}$ | 0 |
| U(1)_Y | 0 | 0 | $1/6$ |

これは**標準模型のゲージ群がブロック対角に分解されている**ことの行列実装。

## 4. 保存カレントと 2 点関数

格子上の SU(N) 電流密度:
$$J^A(i) = \sum_{\alpha,\beta} (T^A)_{\alpha\beta}\, c_{i,\alpha}^\dagger c_{i,\beta}$$

これは$\mathrm{Tr}\,T^A = 0$ の SU 群生成子に対し $\langle J^A(i)\rangle = 0$ (真空でカレント期待値 0)。

連結 2 点関数を Wick の定理で計算:
$$\langle J^A(x) J^B(0)\rangle_c = -\mathrm{Tr}(T^A T^B) \cdot |c_{x0}|^2$$

ここで $c_{x0} = \langle c_x^\dagger c_0\rangle$ は単フレーバー 2 点関数 (フレーバー対称性により全フレーバーで等しい)。

### 4.1 検証可能な構造

(a) **群ブロック対角性**: 
$$\langle J^A_{\rm color}(x) J^a_{\rm weak}(0)\rangle_c = 0$$
SU(3) 生成子と SU(2) 生成子のクロス項は厳密に 0。これは 2 つの群が独立に作用することの数値証拠。

(b) **CFT スケーリング** (Calabrese-Cardy):
1+1D 自由フェルミオンで $|c_{x0}|^2 \sim 1/(\pi^2 x^2)$ at large $|x|$.
よって
$$\langle J^A(x) J^A(0)\rangle_c \sim -\frac{1}{\pi^2 x^2}$$

これは **Kac-Moody 代数レベル $k=1$** の SU(N) 電流の CFT 予言 (Knizhnik-Zamolodchikov 1984; Affleck 1989)。

(c) **電流保存**: $\partial_\mu J^\mu_a = 0$ は対称性から自動。Heisenberg 方程式
$$\partial_t \rho_a + \nabla \cdot \vec j_a = 0$$
から確認可能。

## 5. AdS/CFT バルク双対との接続

Maldacena-Witten 1998 の結果を本 Phase の文脈で:

> 境界 CFT₂ (= 1+1D, 我々の鎖) が大域対称性 SU(3)×SU(2)×U(1)_Y を持つ ⇔ バルク AdS₃ には対応するゲージ場 $A^{\mu(c)}_A, A^{\mu(w)}_a, A^{\mu(Y)}$ が存在する

物質場とゲージ場の幾何的描像:
- 境界の電流 $J^A$ → バルク内に伝播するゲージ場 $A^A$
- 電流 2 点関数 → バルク両端ゲージ場の Witten 図 (propagator)
- カイラル異常 → バルクの Chern-Simons 項

これによって、**標準模型のゲージ場 (光子・W/Z・グルーオン) がバルクの幾何構造として現れる**。

## 6. シミュレーション計画

### Part A: 生成子の構成
- 6×6 行列で $T^A_{\rm color}, T^a_{\rm weak}, T^Y$
- $\mathrm{Tr}(T^A T^B)$ 行列計算
- ブロック対角性の数値検証

### Part B: 単フレーバー 2 点関数
- $N = 64$ サイト 1D 鎖、半占有
- $c_{ij}$ 計算 (= 単フレーバー XX 模型基底状態)

### Part C: 全 12 電流の 2 点関数
- 全 144 個の組み合わせ $\langle J^A(x) J^B(0)\rangle$
- 行列形式で $-\mathrm{Tr}(T^A T^B) \times |c_{x0}|^2$

### Part D: CFT スケーリング検証
- 距離 $x$ に対し $\log|\langle J^A J^B\rangle|$ vs $\log x$
- 傾き $\approx -2$ (CFT 予言) 確認
- Kac-Moody レベル $k$ の数値抽出

### Part E: ブロック対角性可視化
- $\mathrm{Tr}(T^A T^B)$ の 12×12 ヒートマップ
- 実距離での $\langle J^A J^B\rangle$ の 12×12 ヒートマップ
- 両者の構造が一致することを確認

## 7. この Phase が示すこと

- 標準模型のゲージ群構造 SU(3)×SU(2)×U(1) は**境界 CFT のフレーバー対称性として自然に出現**
- 各群の電流が独立に保存し、互いに無相関 (= 群論的ブロック対角)
- バルク双対は 12 個のゲージ場 — 光子 + W/Z + グルーオン (に類似する 4 次元的な内部構造)
- なぜ我々の宇宙が SU(3)×SU(2)×U(1) であるかは**未解明** (フレーバー次元 N=6 の起源は別の問題) だが、**フレームワークは標準模型を自然に収容する**

## 8. 限界と今後の課題

⚠️ 本 Phase が**示さない**こと:
- なぜ「3 世代」のクォーク・レプトンか (これは別の物理)
- 質量階層 ($m_e \ll m_t$) の起源
- ヒッグス機構 (= SU(2) 自発破れ) の動的描像
- カイラル性 (左手のみが弱相互作用)

これらは **Phase 11+: 物質階層の創発** で取り組むべき次のフェーズ。
