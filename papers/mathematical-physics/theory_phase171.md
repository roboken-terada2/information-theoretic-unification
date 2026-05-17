# Phase 171: 指数定理 — Atiyah-Singer + ABJ Anomaly + Witten Index + K_index

> **Tier 1 #24 Mathematical Physics — Phase 5/8 (Block A paper 8/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 171 の目的

Phase 167-170 で Lie + 可積分 + Yang-Mills + CFT。Phase 171 では **位相幾何と解析の橋渡し** = 指数定理:

1. **Atiyah-Singer 指数定理 (1963)** — 解析的指数 = 位相的指数
2. **Dirac 演算子の指数**
3. **★ ABJ (Adler-Bell-Jackiw) anomaly (1969) ★**
4. **Chiral anomaly + π⁰ → γγ**
5. **η-invariant (Atiyah-Patodi-Singer 1975)**
6. **Witten index (1982)** SUSY 拡張
7. **特性類** (Chern, Pontryagin, Euler)
8. **物理応用** (SM anomaly cancellation, Phase 135 接続)
9. **ITU 視点**: K_index = K_sym ↔ K_topo coupling

中心テーゼ:

> **指数定理 = K_sym (解析) と K_topo (幾何) の橋**。
> Anomaly = K_sym の局所保存と大域 topology の競合 (Phase 155 接続)。
> SM anomaly cancellation = 12 種 fermion の精緻 conspiracy。

---

## 1. ★ Atiyah-Singer 指数定理 (1963) ★

### 1.1 主張

楕円型微分演算子 D の **解析的指数** = **位相的指数**:

```
index(D) = dim ker(D) - dim coker(D)
        = ∫_M ch(D) td(M)   (Chern character × Todd class)
```

= **無限次元** な解析量が、**有限次元** トポロジー量に等しい。

### 1.2 受賞

Atiyah-Singer 1963; Atiyah & Singer Abel Prize 2004。

### 1.3 ITU 視点

```
Atiyah-Singer = K_sym (解析 ker/coker) ↔ K_topo (Chern/Todd) bridge
```

---

## 2. ★ Dirac 演算子の指数 ★

### 2.1 Dirac 演算子

```
i D̸ = i γ^μ D_μ
```

(gauge 場 D_μ = ∂_μ - i g A_μ)。

### 2.2 4D Dirac 指数

```
index(D̸) = (1/8π²) ∫ tr(F ∧ F)
         = (1/32π²) ∫ ε^μνρσ F_μν F_ρσ d⁴x
         = Pontryagin 数 n
```

(Phase 169 instanton + 接続)。

### 2.3 物理: zero mode

```
index(D̸) = #(正 chirality zero modes) - #(負 chirality zero modes)
```

= **chiral zero mode** の (net) 数。

### 2.4 ITU 視点

```
Dirac index = K_fermion zero mode topology
Pontryagin n = K_gauge topological invariant (Phase 169)
```

---

## 3. ★ ABJ Anomaly (1969) ★

### 3.1 古典 chiral 保存則

古典場 theory で:
```
∂_μ j^μ_5 = 0   (chiral current)
```

### 3.2 量子破れ

ABJ 1969: 量子効果で **保存が破れる**:
```
∂_μ j^μ_5 = (1/16π²) ε^μνρσ F_μν F_ρσ   (axial anomaly)
```

### 3.3 ★ π⁰ → γγ 崩壊 ★

QCD chiral anomaly で π⁰ → 2γ:
```
Γ(π⁰ → γγ) = (α² m_π³) / (64 π³ f_π²)
            ≈ 7.7 eV  (実験 7.82 eV ✓)
```

★ ABJ anomaly の **最直接的実験検証** (誤差 1%)。

### 3.4 ITU 視点

```
ABJ anomaly = K_sym (古典) と K_quantum (量子) の不両立
Triangle diagram = K_index 局所表現
π⁰ → γγ = K_chiral 破れの観測物理
```

---

## 4. ★ SM Anomaly Cancellation ★

### 4.1 必要条件

SM (Phase 135) が一貫するため、全 fermion を summed すると anomaly が **完全相殺**:

```
Σ_f Q_f³ = 0  (gauge anomaly cancellation)
Σ_f Q_f = 0  (mixed gauge-gravitational anomaly)
```

### 4.2 1 世代 fermion (15 fields)

```
左手 quark doublet (×3 color):  (u_L, d_L) × 3
右手 quark singlets (×3 color): u_R, d_R × 3
左手 lepton doublet: (ν_L, e_L)
右手 lepton singlet: e_R
合計: 6 + 6 + 2 + 1 = 15 fields per generation
```

### 4.3 数値検証 (Y hypercharge)

| field | Y/2 | x color | Σ Y³ |
|---|---|---|---|
| Q_L (u_L, d_L) | 1/6 | × 3 | 2 × 3 × (1/6)³ = 1/36 |
| u_R | 2/3 | × 3 | 3 × (2/3)³ = 8/9 |
| d_R | -1/3 | × 3 | 3 × (-1/3)³ = -1/9 |
| L_L (ν_L, e_L) | -1/2 | × 1 | 2 × (-1/2)³ = -1/4 |
| e_R | -1 | × 1 | 1 × (-1)³ = -1 |

```
Σ Y³ = 1/36 + 8/9 - 1/9 - 1/4 - 1 = 0   ★ 完全相殺
```

### 4.4 ITU 視点

```
SM anomaly 相殺 = K_field の global consistency constraint
12 + 1 species per generation = K_sym の精密 conspiracy
```

---

## 5. ★ Witten Index (1982) ★

### 5.1 定義

SUSY (Phase 140):
```
W = tr[(-1)^F e^{-βH}]
```

= bosonic - fermionic 状態の差。

### 5.2 主張

```
W は β に依存しない
W ≠ 0 ⇒ SUSY 不破れ
W = 0 ⇒ SUSY 破れの可能性 (確定ではない)
```

### 5.3 例: 1D SUSY QM

```
H = (p² + W'²)/2 + (1/2)[ψ̄, ψ] W''
W: superpotential
```

Witten 1982 計算: W_index = sgn(W(+∞)) - sgn(W(-∞))。

### 5.4 ITU 視点

```
Witten index = K_SUSY × K_index topology
SUSY 破れ条件 = K_SUSY 不安定性
```

---

## 6. 特性類 (Characteristic Classes)

### 6.1 Chern class (complex bundle)

```
c_1 = (1/2π) tr(F)     (1st Chern)
c_2 = (1/8π²) tr(F ∧ F)  (2nd Chern, = instanton)
```

### 6.2 Pontryagin class (real bundle)

```
p_1 = -(1/8π²) tr(F ∧ F)
```

### 6.3 Euler class

```
e = Pfaffian(F) / (2π)^n
```

### 6.4 物理応用

| 量 | 特性類 |
|---|---|
| QHE Chern number (Phase 155) | c_1 |
| Instanton (Phase 169) | c_2 |
| Z₂ TI (Phase 155) | refined |
| TI surface state | bulk-boundary correspondence |

### 6.5 ITU 視点

```
特性類 = K_topo の integer invariant family
```

---

## 7. η-Invariant (Atiyah-Patodi-Singer 1975)

### 7.1 定義

Dirac 演算子の **正/負 spectrum** の差:
```
η(s) = Σ_λ sgn(λ) |λ|^{-s}
η(0) = regularized 差
```

### 7.2 物理応用

- Boundary index theorem
- Chern-Simons theory
- Phase 155 topological insulator

### 7.3 ITU 視点

```
η-invariant = K_index boundary refinement
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **2D 球面 Atiyah-Singer**: Dirac index from Pontryagin
2. **ABJ anomaly**: π⁰ → γγ 崩壊率
3. **SM anomaly cancellation** Σ Y³ = 0 計算
4. **Witten index** 1D SUSY QM 例
5. **Chern number** (Phase 155 接続)

---

## 9. Phase 171 主結論

1. **Atiyah-Singer (1963, Abel 2004)**: 解析 index = 位相 index
2. **Dirac index = Pontryagin n** (Phase 169 instanton 接続)
3. **ABJ (1969)**: ∂_μ j^μ_5 = (1/16π²) F F̃
4. **π⁰ → γγ**: Γ ≈ 7.7 eV (実験 7.82 ±0.14 eV ✓)
5. **SM anomaly cancellation**: Σ Y³ = 0 with 15 fermions per gen
6. **Witten index (1982)**: W = tr[(-1)^F e^{-βH}] = SUSY indicator
7. **特性類** (Chern, Pontryagin, Euler) = K_topo invariants
8. **η-invariant (APS 1975)**: boundary refinement
9. **ITU**: K_index = K_sym (解析) ↔ K_topo (幾何) bridge
10. **次の Phase 172** で **Knot 理論 + Jones polynomial + Witten CS**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Atiyah-Singer | K_sym ↔ K_topo bridge |
| Dirac index | K_fermion zero mode topology |
| ABJ anomaly | K_sym 局所 vs 大域 不両立 |
| π⁰ → γγ | K_chiral 破れの観測 |
| SM anomaly cancellation | K_field global consistency |
| Witten index | K_SUSY × K_index |
| Chern number | K_topo ∈ ℤ invariant |
| η-invariant | K_index boundary refinement |

---

## 引用

```
Terada, M. (2026). Phase 171: Index theorems — Atiyah-Singer, ABJ anomaly,
Witten index, and characteristic classes in ITU (Tier 1 #24 phase 5/8).
Zenodo. DOI: [10.5281/zenodo.20251178](https://doi.org/10.5281/zenodo.20251178).
```

主要参考文献:
- Atiyah, M. F., Singer, I. M. (1963) "The index of elliptic operators on compact manifolds" Bull. Amer. Math. Soc. 69, 422
- Atiyah, M. F., Singer, I. M. (1968, 1971) papers I-V on index theorem, Ann. Math.
- Adler, S. L. (1969) "Axial-vector vertex in spinor electrodynamics" Phys. Rev. 177, 2426
- Bell, J. S., Jackiw, R. (1969) "A PCAC puzzle: π⁰ → γγ in the σ-model" Nuovo Cim. A 60, 47
- Witten, E. (1982) "Constraints on supersymmetry breaking" Nucl. Phys. B 202, 253
- Atiyah, M. F., Patodi, V. K., Singer, I. M. (1975) "Spectral asymmetry and Riemannian geometry I" Math. Proc. Camb. Phil. Soc. 77, 43
- Chern, S. S., Simons, J. (1974) "Characteristic forms and geometric invariants" Ann. Math. 99, 48
- Alvarez-Gaumé, L., Witten, E. (1984) "Gravitational anomalies" Nucl. Phys. B 234, 269
- Bouchiat, C., Iliopoulos, J., Meyer, P. (1972) "An anomaly-free version of Weinberg's model" Phys. Lett. B 38, 519 (SM anomaly cancellation)
- Stora, R. (1984) "Algebraic structure and topological origin of anomalies" Cargese Summer School
- Zumino, B., Wu, Y. S., Zee, A. (1984) "Chiral anomalies, higher dimensions, and differential geometry" Nucl. Phys. B 239, 477
- Nakahara, M. (2003) Geometry, Topology and Physics, 2nd ed. CRC Press
- Bertlmann, R. A. (1996) Anomalies in Quantum Field Theory. Oxford UP
