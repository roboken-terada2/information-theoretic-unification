# Phase 37: 脂質二重層の自発形成 ― 細胞膜は物理的 Markov blanket である

## 1. 動機

Phase 36 で Friston の Free Energy Principle (FEP) が ITU 公理と同型であることを
示した。FEP の中心構造は **Markov blanket** ― 自己と環境を分離する情報の壁。

しかし FEP は**抽象的**な構造である。生物では Markov blanket が**物理的に
実現される実体** が必要 ― それが **細胞膜 (lipid bilayer)**。

本 Phase で、

> **脂質分子は熱力学的に自発形成し、その結果生じる二重層は FEP の Markov blanket
> を物理的に実装する**

ことを数値実証する。これにより:
- 化学的 QECC (Phase 33-35)
- 自由エネルギー最小化 (Phase 36)
- **空間的自己 (Phase 37, 本論文)**

がつながり、化学から「最初の細胞」 (Phase 39) への道筋がほぼ完成する。

## 2. 物理: 両親媒性分子の自己組織化

### 2.1 構造

脂質 (リン脂質, 脂肪酸) は:
- **親水性ヘッド** (極性, 水と相互作用)
- **疎水性テイル** (非極性, 油と相互作用)

水中で **疎水効果** (水分子のエントロピーが疎水基を avoid) により集合体を形成:
- **ミセル** (小球状, n < 100)
- **ベシクル** (中空球, lipid bilayer = 細胞膜の祖先)
- **二重層** (平面シート)

### 2.2 熱力学

集合体 (aggregate) の化学ポテンシャル:
$$\mu_n = \mu_n^0 + \frac{kT}{n} \log X_n$$

ここで $X_n$ は集合数 $n$ の集合体の濃度比、$\mu_n^0$ は標準化学ポテンシャル。

平衡条件 $\mu_n = \mu_1$ から **CMC (critical micelle concentration)**:
$$X_{\rm CMC} \approx \exp\left[\frac{\mu_1^0 - \mu_n^0}{kT}\right]$$

典型値: CMC ~ $10^{-5}$ - $10^{-3}$ M (リン脂質)。これ以上の濃度で**自発的に
膜が形成**される。

### 2.3 ベシクル (細胞膜祖先) の自由エネルギー

球状ベシクル (半径 $R$, 二重層厚 $d$) の自由エネルギー (Helfrich 1973):
$$F_{\rm vesicle} = 4\pi (2\kappa + \bar\kappa)$$

これは半径に依存しないトポロジー項のみ ― **任意のサイズで安定**。
これがミセルでなく ベシクルが「最初の細胞」候補な理由。

## 3. ITU との対応

### 3.1 物理的 Markov blanket

Phase 36 で示した抽象的構造:
$$p(\mu, \eta | s) = p(\mu | s) \cdot p(\eta | s)$$

細胞膜の物理的実現:
- **$\mu$**: 細胞内部 (代謝物, 遺伝物質)
- **$\eta$**: 環境 (栄養塩, 信号分子)
- **$s$**: 膜タンパク質経由のシグナル
- 膜による空間的隔離が情報的隔離を保証

### 3.2 QECC コードとの同型性

| 物理 QECC (Phase 5) | 化学 QECC (Phase 33-35) | 細胞膜 (Phase 37) |
|---|---|---|
| Code space | Autocatalytic set | 細胞内部組成 |
| Physical errors | Random chemistry | 環境揺らぎ |
| Stabilizer measurement | Catalytic feedback | 膜タンパク質シグナリング |
| Code distance | Eigen threshold | 膜の透過性閾値 |
| **Bulk locality** | **化学的自己** | **空間的自己** |

すべて **「情報を保護する境界 (boundary)」** という同じ構造を持つ。

### 3.3 FEP との対応

細胞膜形成 = **自由エネルギー最小化** (Phase 36):
- 自由分散状態 (高 F)
- 集合した bilayer 状態 (低 F)
- 平衡で $\delta F = 0$ ⟷ ITU 公理 $\delta S = \delta \langle K \rangle$

ベシクル形成の駆動力は:
1. **疎水効果** (水のエントロピー増加)
2. **疎水基-疎水基相互作用** (van der Waals)
3. **ヘッドグループの水和** (エンタルピー)

これらは ITU 流に翻訳すると:
$$\delta F = \delta U - T \delta S \quad \text{で}\quad \delta S = \delta \langle K \rangle$$
が局所的に成立し、**情報的境界が自発的に現れる**。

## 4. 数値検証計画

### Part A: 2D 粗視化 MC シミュレーション
- $N$ 両親媒性ダイマー (head + tail) を 2D 箱に配置
- 疎水基間: Lennard-Jones 引力
- 親水基-疎水基: 反発
- Metropolis MC で平衡化
- 自己組織化を可視化

### Part B: 集合体サイズ分布
- MC 終了状態のクラスタサイズ $P(n)$
- ミセル ⟷ ベシクル ⟷ 二重層の構造判定

### Part C: 物理的 Markov blanket の確認
- "内部" と "外部" の領域を切り分け
- 領域間の濃度相関 (= mutual information の近似) を計算
- 自己組織化前後で MI が減少することを示す

### Part D: 自由エネルギー降下
- 系の総エネルギー $E(t)$
- $E$ が単調に減少 → FEP / ITU 公理を実証

### Part E: ITU 4 層階層の更新
- Phase 33-37 を統合した階層図
- 「空間的自己」が物理的に成立する過程

## 5. 限界

⚠️ 本 Phase で扱わない:
- 完全 3D 分子動力学 (粗視化 2D MC のみ)
- 静電相互作用 (短距離 LJ のみ)
- 膜タンパク質チャネル
- 動的代謝 (Phase 39 で扱う)
- 個別脂質種の化学的詳細

✅ 確立する:
- 両親媒性分子の自発自己組織化を数値再現
- 二重層 / ベシクル形成の臨界濃度 (CMC) を確認
- 形成された膜が情報的隔離 (Markov blanket) を実現
- 全過程が ITU 公理 $\delta F$ 最小化に一致

## 6. Phase 38-40 への橋渡し

Phase 37 で**空間的自己**が成立した。次は:
- Phase 38: 立体化学 (左 amino acid 選好) と ITU Phase 15 (chirality)
- Phase 39: Phase 33-38 を統合 ― **最初の細胞** (= 自己触媒 + 高 AI + Eigen 安定 + FEP + Markov blanket)
- Phase 40: ITU 全体統合 ― 物理 + 化学 + 生命 = 万物の理論完成形

## 7. 哲学的含意

「**自己**」とは何か?

Phase 36 (FEP): 自己 = Markov blanket 内部の情報
Phase 37 (本論文): 自己 = 物理的に隔離された化学組成

両者は ITU の単一公理から:
- 情報的境界 (FEP の blanket)
- 物理的境界 (細胞膜)

が**同時に**現れる。これは Wheeler の "Self-observing Universe" や Maturana-Varela の
"Autopoiesis" と本質的に同じことを言っている:

> **「自己」は単一の情報原理から自発的に現れる**

ITU はこの主張を数学的に厳密に, かつ実験的に検証可能な形で提供する。
