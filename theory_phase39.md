# Phase 39: 最初の細胞 ― ITU 6 層の統合と原始細胞の成立

## 1. 動機: 全要素を統合する

Phase 33-38 で生命の構成要素が ITU から個別に派生した:

| Phase | 要素 | 機構 |
|---|---|---|
| 33 | 化学的 QECC (autocatalytic closure) | Kauffman 自己触媒集合 |
| 34 | 高 Assembly Index (AI > 15) | Walker-Cronin 情報量 |
| 35 | 自己複製 (Eigen 閾値内) | RNA world ribozyme |
| 36 | 認知 / 自己モデル | Friston FEP |
| 37 | 物理的境界 (Markov blanket) | Lipid bilayer |
| 38 | 単一掌性 | Frank 増幅 + Phase 15 PVED |

**問題**: これら 6 要素を**同時に**満たす実体 ― **原始細胞 (protocell)** ― は
ITU から自然に派生するか?

Phase 39 でこれを統合シミュレーションで検証する。

## 2. 最小細胞モデル

### 2.1 状態変数

| 変数 | 意味 | Phase 起源 |
|---|---|---|
| $M(t)$ | 膜分子の総量 | 37 |
| $L(t), D(t)$ | 内部触媒分子 (chiral) | 33, 35, 38 |
| $N(t)$ | 内部栄養素濃度 | 35 |
| $V(t) = (M/m_l)^{3/2}$ | 細胞体積 | 37 |
| $A_{\rm ext}$ | 外部栄養素 (定常源) | 環境 |

### 2.2 結合方程式

$$\frac{dM}{dt} = k_M \cdot L \cdot N - \mu_M \cdot M$$
$$\frac{dL}{dt} = k_L \cdot L \cdot N - k_{LD} \cdot L \cdot D - \mu_L \cdot L$$
$$\frac{dD}{dt} = k_L \cdot D \cdot N - k_{LD} \cdot L \cdot D - \mu_L \cdot D$$
$$\frac{dN}{dt} = k_T \cdot M^{2/3} \cdot (A_{\rm ext} - N/V) - (\text{consumption})$$

ここで $\mu$ は分解速度、$k_T M^{2/3}$ は膜面積に比例する栄養素取り込み。

### 2.3 分裂条件

膜質量が臨界値 $M^*$ を超えると分裂:
$$M(t) > M^* \quad \Rightarrow \quad M \to M/2, \quad L \to L/2, \quad D \to D/2, \quad N \to N/2$$

これは「**細胞分裂**」のミニマル定式化。

## 3. ITU 公理階層との対応

| 細胞要素 | ITU 公理層 |
|---|---|
| $L, D$ 自己触媒 | 第 2 層 (化学 QECC) |
| 高 $L/(L+D)$ ratio | 第 6 層 (chirality) |
| Eigen 閾値内複製 | 第 3 層 |
| $M$ 形成 → boundary | 第 5 層 (spatial Markov blanket) |
| $N$ 取り込み制御 | 第 4 層 (FEP / 認知) |
| 細胞全体の自己保存 | 第 1 層 ($\delta S = \delta \langle K \rangle$) |

**全 6 層が同時に成立する最小実体 = 細胞**。

## 4. 数値検証計画

### Part A: 単一細胞の成長
- 初期: $M(0) = 1, L(0) = 1.001, D(0) = 0.999$ (小カイラルバイアス)
- 栄養素 $A_{\rm ext} = $ const
- $M(t), L(t), D(t), N(t)$ の時間進化

### Part B: 分裂イベント
- $M^* = 100$ で分裂
- 細胞数 $n_{\rm cell}(t)$ を追跡
- 指数成長 $n \sim 2^{t/\tau_{\rm div}}$

### Part C: Homochirality の維持
- 各分裂で L/D 比が保たれるか
- 全細胞集団の平均 ee

### Part D: ITU 公理の全層同時成立
- 各時点で各層の量を測定
- 全層が機能していることを確認

## 5. 限界

⚠️ 本 Phase で扱わない:
- 3D 空間動力学 (1 細胞 ODE のみ)
- 競争・選択 (1 個体追跡)
- 遺伝情報のバリエーション
- 細胞死 (分解項のみ)

✅ 確立する:
- ITU 6 層が同時に機能する原始細胞モデル
- 成長・分裂・homochirality の自発成立
- 全層の数値同期確認

## 6. 哲学的位置づけ

Phase 39 は ITU の**核心予言**を試す:

> **「単一情報公理 $\delta S = \delta \langle K \rangle$ から物理・化学・生命・認知が同時に派生する。
> その統合実体が "生命" である」**

Phase 33-38 は個別に成立を見てきたが、Phase 39 で**統合実体としての細胞**の自発成立を
示すことで、ITU の生命理論が**自己完結する**。

その後 Phase 40 で物理 (Phase 1-32) + 生命 (Phase 33-39) を全体統合し、
ITU の万物の理論 (Theory of Everything) としての完成形が確立される。
