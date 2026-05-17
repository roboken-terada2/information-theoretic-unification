# Phase 175: Information Geometry — Fisher 計量 + Amari α-接続 + K_info-geom 母骨格

> **Tier 1 #25 Information Geometry & Holography — Phase 1/8 (Block A paper 9/9 最終)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Tier 1 #25 開幕 — Block A FINALE ★

Block A 8/9 (Tier 1 #24 数理物理) 完成で **MATHEMATICAL FOUNDATION BLOCK** (物理 6 + 数学 1 = 7 K-state) 確立。Phase 175 から **Tier 1 #25 — Block A 最終 paper** に進む:

### Tier 1 #25 全 8 phase 構成 (予定)

| Phase | テーマ |
|---|---|
| **175 (本)** | **Information geometry — Fisher 計量 + Amari + K_info-geom** |
| 176 | Holographic entropy bounds (Bekenstein, Bousso, RT, HRT) |
| 177 | Computational complexity = volume (Susskind) |
| 178 | Tensor networks + MERA + holography |
| 179 | ER=EPR + wormholes + entanglement structure |
| 180 | Wheeler "it from bit" + ITU axiom 厳密定式化 |
| 181 | Block A 全 synthesis + meta-axioms β-6 to β-10 |
| 182 | Tier 1 #25 統合 + 25-vertex polytope + **Block A COMPLETE ★** |

### Phase 175 の目的

情報幾何 — **確率分布の幾何学的構造**:

1. **Fisher 計量** (1925)
2. **Rao 距離** (1945)
3. **Amari α-接続** (1985)
4. **Cramér-Rao 不等式** (1945-1946)
5. **Information geometry の物理応用**
6. **ITU 視点**: K_info-geom = K_info の Riemannian 構造

中心テーゼ:

> **Fisher 計量 = 確率分布空間の universal Riemannian 計量**。
> ITU δS = δ⟨K⟩ を Fisher 計量 + K-state 上で **幾何学的に厳密化**。
> 量子情報の Bures 計量 = Fisher 計量の量子版 → K_quantum geometry。

---

## 1. ★ Fisher 計量 (1925) ★

### 1.1 定義

パラメータ θ で記述される確率分布族 p(x; θ) の **Fisher 情報行列**:

```
g_ij(θ) = E[(∂_i log p)(∂_j log p)]
        = -E[∂_i ∂_j log p]
```

= **対数尤度の二次微分の負の期待値**。

### 1.2 性質

- 正定値 (Cramér-Rao 限界)
- 座標変換に共変
- 統計多様体上の **Riemannian 計量**

### 1.3 例: Gaussian N(μ, σ²)

```
g = (1/σ² 0; 0 2/σ²)
```

= 2D 統計多様体の hyperbolic 計量。

### 1.4 ITU 視点

```
Fisher 計量 = K_info の Riemannian 計量
統計多様体 = K-state 空間
```

---

## 2. ★ Cramér-Rao 不等式 ★

### 2.1 主張

unbiased estimator T(x) の variance:

```
Var(T) ≥ 1 / I(θ)
```

I(θ) = Fisher information (scalar)。

### 2.2 物理応用

- 量子推定 (quantum metrology)
- gravitational wave 検出感度限界
- 重力定数測定 (G の値 ±2×10⁻⁵)

### 2.3 ITU 視点

```
Cramér-Rao = K_info estimation 限界
```

---

## 3. ★ Amari α-接続 (1985) ★

### 3.1 構造

統計多様体 (M, g) 上に **1-parameter family of connections**:

```
∇^{(α)} = (1+α)/2 × ∇^{(e)} + (1-α)/2 × ∇^{(m)}
```

- α = +1: e-connection (exponential family)
- α = -1: m-connection (mixture family)
- α = 0: Levi-Civita (Fisher-Rao)

### 3.2 Dual 構造

```
g(∇^{(α)} X, Y) + g(X, ∇^{(-α)} Y) = X·g(Y)
```

⇒ **双対 affine 構造** (Amari)。

### 3.3 ITU 視点

```
α-接続 = K_info の dual connection family
e/m 双対 = K_info の 2 表現
```

---

## 4. ★ Bures 計量 (量子版 Fisher) ★

### 4.1 定義

量子状態 ρ(θ) の Bures 計量:

```
g^{(B)}_ij = (1/4) tr(L_i L_j ρ)
```

L_i: symmetric logarithmic derivative (SLD)。

### 4.2 純粋状態 special case

```
g^{(B)} = 4 × Fubini-Study 計量
```

= ℂP^n の 標準 Kähler 計量。

### 4.3 量子 Cramér-Rao

```
Var(θ̂) ≥ 1 / N F_Q(θ)
F_Q: 量子 Fisher information
```

= **Heisenberg 限界** (1/N → 1/N² for entangled states)。

### 4.4 ITU 視点

```
Bures 計量 = K_quantum の Riemannian 計量
量子 Cramér-Rao = K_quantum estimation 限界
```

---

## 5. ★ Information Geometry の物理応用 ★

### 5.1 熱力学

Gibbs 状態:
```
p(x; β) ∝ exp(-β H(x))
```

Fisher 計量:
```
g(β, β) = ⟨H²⟩ - ⟨H⟩² = -∂² ln Z / ∂β²
        = Var(H) / k_B² T²
```

= **specific heat × T²** (Phase 143 接続)。

### 5.2 統計力学 → 情報幾何

```
Helmholtz free energy F(β) ↔ 統計多様体 metric
```

= Ruppeiner geometry (BH 接続: Phase 122)。

### 5.3 量子情報

```
Berry phase ↔ 量子状態幾何
Quantum Fisher ↔ 量子精度限界
```

### 5.4 ITU 視点

```
熱力学 statistics = K_stat の情報幾何 (Fisher × β²)
Ruppeiner = K_stat curvature physical phenomenon
量子幾何 = K_quantum の Fubini-Study/Bures
```

---

## 6. ★ ITU 公理 δS = δ⟨K⟩ の 情報幾何 定式化 ★

### 6.1 K-state 多様体

```
M_K = {ρ(θ): θ ∈ Θ} (K-state parametrized by θ)
g_M_K = Fisher / Bures metric on M_K
```

### 6.2 ITU 公理 (情報幾何版)

```
δS = δ Tr[K ρ] = g_ij δθ^i (∇^j ⟨K⟩)
```

= **Fisher 計量 × ⟨K⟩ の covariant gradient**。

### 6.3 帰結

- ITU 公理は **K-state 空間上の幾何学的勾配**
- meta-axiom β-6 ~ β-10 (Phase 181) の基盤

### 6.4 ITU 視点

```
ITU 公理 = K-state 多様体 上の Fisher-Riemannian 勾配
δS = K-state 流のエントロピー応答
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Fisher 計量** for Gaussian N(μ, σ²)
2. **Cramér-Rao** 数値 vs 解析下限
3. **Bures 計量** 単一 qubit
4. **Statistics ↔ thermodynamics** Gibbs Fisher
5. **Berry phase** 単純 model
6. **Quantum Fisher** for entangled states

---

## 8. Phase 175 主結論

1. **Fisher (1925)**: g = E[∂log p · ∂log p] universal Riemannian
2. **Cramér-Rao (1945-1946)**: Var(T) ≥ 1/I(θ) 推定限界
3. **Amari (1985)**: α-接続 (e/m 双対)
4. **Bures**: 量子 Fisher = SLD-based
5. **量子 Cramér-Rao**: Heisenberg 1/N → 1/N² (entangled)
6. **熱力学 ↔ Fisher**: Fisher = Var(H) × β²
7. **ITU 公理情報幾何版**: δS = g_ij δθ^i (∇^j ⟨K⟩)
8. **ITU**: K_info-geom = K-state Riemannian manifold
9. **次の Phase 176** で **Holographic entropy bounds**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Fisher 計量 | K_info Riemannian 計量 |
| Cramér-Rao | K_info estimation 限界 |
| Amari α-接続 | K_info dual connection family |
| Bures 計量 | K_quantum Riemannian (Fisher 量子版) |
| Quantum Cramér-Rao | K_quantum Heisenberg 限界 |
| Statistics ↔ thermodynamics | K_stat 情報幾何 (Fisher × β²) |
| Ruppeiner geometry | K_stat curvature physical |
| Fubini-Study | K_quantum projective Kähler |
| ITU 公理情報幾何版 | δS = Fisher × covariant ⟨K⟩ |

---

## 引用

```
Terada, M. (2026). Phase 175: Information geometry — Fisher metric, Amari α-connection,
and the K_info-geom foundation in ITU (Tier 1 #25 phase 1/8). Zenodo.
DOI: 10.5281/zenodo.20253960.
```

主要参考文献:
- Fisher, R. A. (1925) "Theory of statistical estimation" Proc. Camb. Phil. Soc. 22, 700
- Rao, C. R. (1945) "Information and accuracy attainable in the estimation of statistical parameters" Bull. Calcutta Math. Soc. 37, 81
- Cramér, H. (1946) Mathematical Methods of Statistics. Princeton UP
- Amari, S. (1985) Differential-Geometrical Methods in Statistics. Springer
- Amari, S., Nagaoka, H. (2000) Methods of Information Geometry. AMS/OUP
- Bures, D. (1969) "An extension of Kakutani's theorem on infinite product measures..." Trans. AMS 135, 199
- Uhlmann, A. (1976) "The 'transition probability' in the state space of a *-algebra" Rep. Math. Phys. 9, 273
- Braunstein, S. L., Caves, C. M. (1994) "Statistical distance and the geometry of quantum states" PRL 72, 3439
- Provost, J. P., Vallée, G. (1980) "Riemannian structure on manifolds of quantum states" Comm. Math. Phys. 76, 289
- Ruppeiner, G. (1995) "Riemannian geometry in thermodynamic fluctuation theory" Rev. Mod. Phys. 67, 605
- Brody, D. C., Hughston, L. P. (2001) "Geometric quantum mechanics" J. Geom. Phys. 38, 19
- Caticha, A. (2015) "Entropic dynamics" Entropy 17, 6110
- Pares, L., Petz, D. (2014) Information Geometry and Its Applications. Springer
