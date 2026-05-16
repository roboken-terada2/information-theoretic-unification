# Phase 145: 相転移 + 臨界現象 + Universality + Renormalization Group

> **Tier 1 #21 Statistical Mechanics — Phase 3/8 (Block A paper 5/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 145 の目的

Phase 143-144 で平衡統計力学 (古典 MB + 量子 FD/BE) を扱った。Phase 145 では **相転移と臨界現象** に進む:

1. **Ising model (1925)**: 2D 厳密解 (Onsager 1944)
2. **Landau theory (1937)**: order parameter + 自由エネルギー展開
3. **臨界指数** (α, β, γ, δ, ν, η)
4. **Universality classes**: 細部によらず critical exponent が一致
5. **Renormalization Group (Wilson 1971, Nobel 1982)**
6. **ITU 視点**: 臨界現象 = K_stat の **scale invariance fixed point**

中心テーゼ:

> **臨界現象 = ITU K_stat の RG fixed point 構造**。
> Universality = K_stat の fixed point が microscopic details に依存しない。
> Wilson RG = K_stat 上の scale transformation 群。
> 第 2 種相転移 = K_stat の continuous symmetry breaking。

---

## 1. 相転移の分類

### 1.1 Ehrenfest 分類

- **第 1 種 (first-order)**: 自由エネルギー 1 階導関数が不連続
  - 例: 水 ↔ 氷 (融解熱あり)
- **第 2 種 (second-order, continuous)**: 1 階連続, 2 階発散
  - 例: 強磁性 → 常磁性 (Curie 温度), 超流動転移, BEC

### 1.2 Modern 分類

- **First-order**: latent heat あり、order parameter ジャンプ
- **Continuous (critical)**: order parameter 連続、相関長 発散

---

## 2. ★ Ising Model ★

### 2.1 Hamiltonian

```
H = -J Σ_⟨i,j⟩ s_i s_j - h Σ_i s_i

s_i ∈ {+1, -1} (spin)
J: exchange coupling
h: external field
```

### 2.2 1D Ising (Ising 1925)

厳密解:
- **相転移なし** at T > 0
- partition function:

```
Z = 2^N (cosh(βJ))^N (1 + tanh^N(βJ))
```

### 2.3 ★ 2D Ising (Onsager 1944) ★

★ 厳密解 (history-making) ★:

```
T_c = 2J / [k_B ln(1 + √2)] ≈ 2.269 J/k_B
```

- **連続相転移** (second-order)
- 自由エネルギー 解析的

### 2.4 3D Ising

厳密解 ない。Monte Carlo + conformal bootstrap で:

```
T_c ≈ 4.5115 J/k_B
β ≈ 0.3265
γ ≈ 1.2372
```

### 2.5 ITU 視点

```
K_Ising = K_stat with binary state variable + nearest-neighbor coupling
Phase transition = K_stat の symmetry breaking pattern
```

---

## 3. ★ Landau Theory (1937) ★

### 3.1 Order parameter 自由エネルギー

```
F(m, T) = a(T) m² + b m⁴ + ... - h m

a(T) = a_0 (T - T_c)
b > 0
```

### 3.2 T < T_c

```
∂F/∂m = 0 → m² = -a/(2b) > 0
m = ±√(|a|/(2b)) ∝ (T_c - T)^{1/2}
```

⇒ **β = 1/2** (mean-field critical exponent)。

### 3.3 T > T_c

m = 0 (disordered phase)。

### 3.4 Mean-field 臨界指数

```
α = 0     (specific heat)
β = 1/2   (order parameter)
γ = 1     (susceptibility)
δ = 3     (m ~ h^{1/δ})
ν = 1/2   (correlation length ξ ~ |T-T_c|^{-ν})
η = 0     (correlation function decay)
```

### 3.5 Mean-field の妥当性

```
Upper critical dimension d_c = 4
d > 4: mean-field exact
d < 4: fluctuations 重要、RG 必要
```

### 3.6 ITU 視点

```
Landau F = K_stat ⟨H_eff⟩ as function of order parameter
Mean-field = ITU saddle-point K-state
```

---

## 4. 臨界指数と Scaling Hypothesis

### 4.1 Widom scaling (1965)

自由エネルギー scaling form:

```
f(t, h) = b^{-d} f(b^{y_t} t, b^{y_h} h)

t = (T - T_c)/T_c
```

### 4.2 Scaling 関係式

```
α + 2β + γ = 2     (Rushbrooke)
β(δ - 1) = γ       (Widom)
α = 2 - νd         (hyperscaling)
γ = ν(2 - η)       (Fisher)
```

### 4.3 数値例 (3D Ising)

| 指数 | Mean-field | 3D Ising (実験 + bootstrap) |
|---|---|---|
| α | 0 | 0.110 |
| β | 0.5 | 0.3265 |
| γ | 1 | 1.2372 |
| δ | 3 | 4.789 |
| ν | 0.5 | 0.6300 |
| η | 0 | 0.0364 |

### 4.4 ITU 視点

Critical exponents = K_stat fixed point の **eigenvalue spectrum** (RG 流れ)。

---

## 5. ★ Universality Classes ★

### 5.1 同じクラスの系

Critical exponents が一致する系の集合:

| Class | dim | symmetry | 例 |
|---|---|---|---|
| **Ising** | 3D | Z_2 | 磁性体 (Fe, Ni), liquid-gas, 二元合金 |
| **XY** | 3D | O(2) = U(1) | superfluid He-4 (λ-transition) |
| **Heisenberg** | 3D | O(3) | 磁性体 (Ni 高温) |
| **Mean-field** | ≥4D | 任意 | mean-field 系全て |
| **2D Ising** | 2D | Z_2 | 薄膜磁性体 |

### 5.2 Universality の意味

**Microscopic details (lattice 形状, coupling 値, ...) が critical exponent に影響しない**:
- ⇒ scale-invariant fixed point の存在
- ⇒ RG 流れの attractor

### 5.3 ITU 視点

```
Universality = K_stat fixed point の 普遍 attractor
詳細 = irrelevant operators (RG flow で消える)
```

---

## 6. ★ Renormalization Group (Wilson 1971, Nobel 1982) ★

### 6.1 基本構想

格子 a → b a に拡大、blocking で coarse-grain:

```
H[s] → H'[s']   (block spin transformation)
```

Coupling constants が flow:

```
K' = R(K)
```

### 6.2 Fixed point

```
K* = R(K*)
```

- **Stable fixed point**: 通常相
- **Unstable fixed point**: critical point
- **Trivial fixed point**: T=0, T=∞

### 6.3 Linearization

```
δK' = M δK  near fixed point

Eigenvalues λ_i = b^{y_i}
y > 0: relevant
y < 0: irrelevant
y = 0: marginal
```

### 6.4 Wilson-Fisher fixed point (1972)

```
ε-expansion: d = 4 - ε
β = 1/2 - ε/6 + O(ε²)
ν = 1/2 + ε/12 + O(ε²)
```

3D (ε=1) で 3D Ising の値に良い近似。

### 6.5 数値例 (Ising 2D Migdal-Kadanoff)

```
T_c^{exact} = 2.2692 J/k_B
T_c^{RG} ≈ 2.55 J/k_B  (近似)
```

### 6.6 ITU 視点

```
RG = K_stat 上の scale group action
Fixed point = K_stat の scale-invariant 配置
Critical exponents = K_stat fixed point の representation theory
```

---

## 7. 連続相転移と Symmetry Breaking

### 7.1 Goldstone theorem (1961)

連続対称性が自発的に破れる ⇒ **massless mode (Goldstone boson)**:
- magnon (Heisenberg ferromagnet)
- phonon (crystal)
- pion (chiral symmetry)

### 7.2 Mermin-Wagner theorem (1966)

**2D で連続対称性は破れない** (有限 T)。

```
d ≤ 2 + (correlation function divergence)
```

### 7.3 Kosterlitz-Thouless (1973, Nobel 2016)

2D XY model: 通常の相転移 ない が、**vortex unbinding transition**:
- T < T_KT: bound vortex pairs (power-law correlations)
- T > T_KT: free vortices (exponential decay)

### 7.4 ITU 視点

```
Goldstone = K_stat broken symmetry の massless mode
Mermin-Wagner = K_stat の dimension-dependent symmetry constraint
KT = K_stat の topological phase transition
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **2D Ising T_c ≈ 2.269 J/k_B** (Onsager exact)
2. **Order parameter m vs T** (mean-field β = 0.5)
3. **Susceptibility χ peak at T_c** (γ = 1)
4. **Specific heat C peak at T_c**
5. **Correlation length ξ → ∞** at T_c
6. **Universality demonstration**: 異なる lattice で同じ exponents

---

## 9. Phase 145 主結論

1. **Ising model**: 1D no transition, 2D Onsager exact, 3D MC
2. **Landau theory (1937)**: mean-field exponents (β=1/2, γ=1, δ=3)
3. **臨界指数**: scaling 関係式 (Rushbrooke, Widom, Fisher, hyperscaling)
4. **Universality**: microscopic details に依存しない fixed point
5. **Wilson RG (1971, Nobel 1982)**: block spin + ε-expansion
6. **Mermin-Wagner**: 2D で continuous symmetry broken なし
7. **Kosterlitz-Thouless (Nobel 2016)**: 2D XY topological transition
8. **ITU**: 臨界現象 = K_stat の RG fixed point
9. **次の Phase 146** で **非平衡熱力学 + Onsager + linear response**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Phase transition | K_stat symmetry breaking |
| Order parameter | K_stat broken-symmetry observable |
| Critical exponent | K_stat fixed point eigenvalue |
| Universality | K_stat fixed point attractor |
| RG flow | K_stat scale transformation orbit |
| Goldstone | K_stat massless mode |
| KT transition | K_stat topological transition |

---

## 引用

```
Terada, M. (2026). Phase 145: Phase transitions, critical phenomena, universality,
and renormalization group in ITU (Tier 1 #21 phase 3/8). Zenodo. DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

主要参考文献:
- Ising, E. (1925) "Beitrag zur Theorie des Ferromagnetismus" Z. Phys. 31, 253
- Onsager, L. (1944) "Crystal statistics I. A two-dimensional model with order-disorder transition" Phys. Rev. 65, 117
- Landau, L. D. (1937) "On the theory of phase transitions" Zh. Eksp. Teor. Fiz. 7, 19
- Widom, B. (1965) "Equation of state in the neighborhood of the critical point" J. Chem. Phys. 43, 3898
- Kadanoff, L. P. (1966) "Scaling laws for Ising models near T_c" Physics 2, 263
- Wilson, K. G. (1971) "Renormalization group and critical phenomena" Phys. Rev. B 4, 3174
- Wilson, K. G., Fisher, M. E. (1972) "Critical exponents in 3.99 dimensions" Phys. Rev. Lett. 28, 240
- Goldstone, J. (1961) "Field theories with superconductor solutions" Nuovo Cim. 19, 154
- Mermin, N. D., Wagner, H. (1966) "Absence of ferromagnetism or antiferromagnetism in one- or two-dimensional Heisenberg models" PRL 17, 1133
- Kosterlitz, J. M., Thouless, D. J. (1973) "Ordering, metastability and phase transitions in two-dimensional systems" J. Phys. C 6, 1181
