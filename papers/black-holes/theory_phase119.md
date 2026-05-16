# Phase 119: Tier 1 #18 Black Holes — Schwarzschild + Kerr + No-hair + ITU 公理

> **Tier 1 #18: Black Holes — Phase 1/8 (Block A paper 2/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> Tier 1 #17 (Quantum Gravity): [10.5281/zenodo.20230667](https://doi.org/10.5281/zenodo.20230667)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 119 の目的

Tier 1 #17 で量子重力の **全体像** (AdS/CFT, LQG, string, BMV) を扱った。
Tier 1 #18 では、量子重力の最重要対象 **ブラックホール** を **古典 GR から量子重力まで** 8 phases で深掘りする。

Phase 119 (本) で確立する内容:

1. **Schwarzschild 解 (1916)**: 球対称真空解
2. **Kerr 解 (1963)**: 回転 BH 解
3. **No-hair theorem**: BH は 3 パラメータ (M, J, Q) で完全記述
4. **Penrose process + ergosphere**: Kerr BH の回転エネルギー抽出
5. **Innermost Stable Circular Orbit (ISCO)**: 観測的に重要な軌道
6. **ITU 公理写像**: BH パラメータ ↔ K-state

中心テーゼ:

> **古典 BH 解 = ITU K_geom の安定 stationary 点**。
> Schwarzschild → Kerr → Kerr-Newman のパラメータ拡張は **K-state 次元の追加**。
> No-hair theorem = ITU の **K-flow stationary 条件の唯一性**。

---

## 1. Schwarzschild 解 (1916)

### 1.1 計量

```
ds² = -(1 - r_s/r) c² dt² + (1 - r_s/r)^{-1} dr² + r² (dθ² + sin²θ dφ²)
```

- **r_s = 2 G_N M / c²**: Schwarzschild 半径
- 静的、球対称、真空 (T_μν = 0)
- 質量 M のみで完全記述

### 1.2 イベント horizon

r = r_s で `g_tt = 0` → 古典的に光も脱出不可能。

### 1.3 観測量

| BH | M | r_s |
|---|---|---|
| Sun (toy) | 1 M_⊙ | 2.95 km |
| Stellar mass | 10 M_⊙ | 29.5 km |
| Cygnus X-1 | 21 M_⊙ | 62.0 km |
| M87* (super-massive) | 6.5 × 10⁹ M_⊙ | 1.92 × 10¹⁰ km = 128 AU |
| Sgr A* | 4.0 × 10⁶ M_⊙ | 1.18 × 10⁷ km |

---

## 2. Kerr 解 (1963) ★ 回転 BH

### 2.1 計量 (Boyer-Lindquist 座標)

```
ds² = -(1 - r_s r/Σ) c² dt² - (2 r_s r a sin²θ / Σ) c dt dφ
      + (Σ/Δ) dr² + Σ dθ²
      + (r² + a² + r_s r a² sin²θ / Σ) sin²θ dφ²
```

- a = J / (M c): 単位質量当たり角運動量 (m)
- Σ = r² + a² cos²θ
- Δ = r² - r_s r + a²

### 2.2 horizon 構造

**Inner horizon (r-)** と **outer horizon (r+)**:

```
r± = (r_s ± √(r_s² - 4 a²)) / 2
```

extremal limit: r_s = 2|a| → r+ = r- = r_s / 2。

### 2.3 ergosphere

g_tt = 0 となる面 (static limit surface) と event horizon の間。
ergosphere 内では、すべての物体が回転を強制される (frame dragging)。

### 2.4 Penrose process

ergosphere 内で粒子を 2 つに分裂させ、1 つを負エネルギー軌道に投入 → BH 回転エネルギーを抽出可能。

最大効率: **29% of M c²** (Christodoulou-Ruffini 1971)。

---

## 3. No-hair Theorem

### 3.1 主張

> **重力崩壊後の BH は (M, J, Q) の 3 パラメータで完全記述される。**

- M: mass
- J: angular momentum
- Q: electric charge
- (磁気電荷、higher multipole moments etc. は全て放散)

これは **classical no-hair** (Israel 1967, Carter 1971, Robinson 1975, Mazur 1982)。

### 3.2 物理的意味

BH 形成過程で、initial state の複雑な情報 (~ exp(S_BH) bits) はすべて **horizon に押し込まれる**。観測者は M, J, Q のみ "見える"。

### 3.3 量子情報パラドックスとの関係

No-hair theorem は古典的記述。量子的には **BH state は exp(S_BH) 個の microstate** を持つ (Strominger-Vafa 1996)。

⇒ classical 3 parameters と quantum exp(S_BH) microstates の整合性が Phase 121 の Page curve で取り扱う中心テーマ。

---

## 4. ISCO: Innermost Stable Circular Orbit

### 4.1 Schwarzschild の場合

```
r_ISCO = 3 r_s = 6 G_N M / c²
```

ISCO 内側では円軌道が不安定 → BH へ落下。

### 4.2 Kerr (extremal) の場合

| 軌道方向 | r_ISCO |
|---|---|
| Co-rotating (prograde) | r_s / 2 (extremal) |
| Counter-rotating (retrograde) | 9 r_s / 2 (extremal) |

co-rotating ISCO は extremal Kerr で horizon と一致 → 最大効率 accretion (Thorne-Novikov 1973)。

### 4.3 観測 (LIGO/LISA/EHT)

- LIGO BBH inspiral: ISCO で plunge 移行
- EHT M87* shadow: ISCO 周りの photon ring が決定要因
- LISA EMRI: ISCO で多波サイクル

---

## 5. ITU 公理写像: BH パラメータ ↔ K-state

### 5.1 K_geom の BH での具体化

```
K_geom(M, J, Q) = 2π × (boost generator around horizon)
```

- Schwarzschild: K_geom = 2π × κ (surface gravity)
- Kerr: K_geom + K_angular (frame dragging contribution)
- Kerr-Newman: + K_charge (electromagnetic contribution)

### 5.2 ITU 公理の確認

```
δS = δ A_horizon / (4 G_N ℏ) = δ⟨K_geom⟩
```

- Schwarzschild: S = π r_s² / (G_N ℏ)
- Kerr: S = π (r_+² + a²) / (G_N ℏ) (area-based)

### 5.3 No-hair = K-flow stationary 条件

ITU 視点: classical BH は **K_geom の最小作用 stationary 点**。
- 3 parameters (M, J, Q) = K-state の **3 つの保存量** (Killing 場対応)
- 他のすべての成分は K-flow で消散 → no-hair

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **Schwarzschild r_s の質量別計算** (5 つの BH スケール)
2. **Kerr horizon r± vs spin a の数値プロット**
3. **ISCO 計算** (Schwarzschild + Kerr prograde/retrograde)
4. **Penrose process 最大効率** (29% bound)
5. **K_geom の数値**: 各 BH での surface gravity κ + K_angular 量

---

## 7. Phase 119 主結論

1. **Schwarzschild 解 (1916)**: 静的球対称、r_s = 2GM/c²
2. **Kerr 解 (1963)**: 回転、a = J/(Mc)、ergosphere、Penrose process (29% 最大)
3. **No-hair theorem**: classical BH は (M, J, Q) で完全記述
4. **ISCO**: Schwarzschild r=3 r_s, Kerr extremal prograde r=r_s/2
5. **ITU 解釈**: BH 解 = K_geom 安定 stationary 点
6. **次の Phase 120** で **Bekenstein-Hawking エントロピー詳細 + 量子効果**

---

## 8. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Schwarzschild | K_geom 最も対称な解 |
| Kerr | K_geom + K_angular |
| No-hair | K-flow stationary 唯一性 |
| Ergosphere | K-flow 強制回転領域 |
| Penrose process | K_angular 取り出し可能 |
| ISCO | K_geom 安定軌道下限 |

---

## 引用

```
Terada, M. (2026). Phase 119: Schwarzschild, Kerr, and no-hair theorem
in ITU (Tier 1 #18 Black Holes, Block A paper 2/9, phase 1/8). Zenodo.
DOI: [to be assigned].
```

主要参考文献:
- Schwarzschild, K. (1916) "Über das Gravitationsfeld eines Massenpunktes" Berlin Math. Phys. 189
- Kerr, R. P. (1963) "Gravitational field of a spinning mass" PRL 11, 237
- Israel, W. (1967) "Event horizons in static vacuum space-times" Phys. Rev. 164, 1776
- Carter, B. (1971) "Axisymmetric black hole has only two degrees of freedom" PRL 26, 331
- Penrose, R. (1969) "Gravitational collapse: the role of general relativity" Riv. Nuovo Cim. 1, 252
- Christodoulou, D., Ruffini, R. (1971) "Reversible transformations of a charged black hole" PRD 4, 3552
- Thorne, K., Novikov, I. (1973) "Black Holes" Gordon & Breach
- Mazur, P. (1982) "Proof of uniqueness of the Kerr-Newman black hole solution" J. Phys. A 15, 3173
- Robinson, D. (1975) "Uniqueness of the Kerr black hole" PRL 34, 905
