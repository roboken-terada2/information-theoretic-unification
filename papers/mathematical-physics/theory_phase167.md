# Phase 167: Lie 群 + Lie 代数 + Cartan 分類 + 表現論 + K_sym 母骨格

> **Tier 1 #24 Mathematical Physics — Phase 1/8 (Block A paper 8/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Tier 1 #24 開幕

Block A 7/9 (Tier 1 #23 流体力学) 完成で **EXTENDED MATTER BLOCK** (K_geom + K_cosmic + K_field + K_stat + K_solid + K_flow) 確立。Phase 167 から **Tier 1 #24 Mathematical Physics** に進む — 数学的基盤層。

### Tier 1 #24 全 8 phase 構成 (予定)

| Phase | テーマ |
|---|---|
| **167 (本)** | **Lie 群 + Lie 代数 + Cartan 分類 + 表現論 + K_sym 母骨格** |
| 168 | Soliton + Lax pair + KdV + sine-Gordon + 厳密可解 |
| 169 | Yang-Mills + gauge 理論 + Clay Millennium #5 mass gap |
| 170 | CFT + Virasoro + BPZ + 2D field theory |
| 171 | Index 定理 + Atiyah-Singer + anomaly |
| 172 | Knot 理論 + Jones polynomial + Witten CS |
| 173 | Random matrix theory + Riemann Hypothesis |
| 174 | Tier 1 #24 統合 + 24-vertex polytope + 10 predictions |

### Phase 167 の目的

数理物理の **基礎言語** Lie 群論を ITU 化:

1. **連続対称性** (Lie 1873-)
2. **Lie 代数** (commutators, Jacobi)
3. **Cartan 分類** (1894): A_n, B_n, C_n, D_n + 5 例外 (E_6, E_7, E_8, F_4, G_2)
4. **表現論** (Cartan weights, Dynkin diagrams)
5. **物理応用** (SU(2) spin, SU(3) flavor/color, SO(10) GUT, E_8 string)
6. **ITU 視点**: K_sym = ITU の対称性 backbone

---

## 1. ★ Lie 群 ★

### 1.1 定義

連続パラメータを持つ群 (微分多様体 + 群構造):

```
G : smooth manifold + group operation
dim G = 連続パラメータ数
```

### 1.2 主要 Lie 群

| 群 | dim | 物理 |
|---|---|---|
| U(1) | 1 | 電磁気 (Phase 135) |
| **SU(2)** | 3 | spin, 弱相互作用 |
| **SU(3)** | 8 | QCD (8 グルーオン) |
| SO(3) | 3 | 3D 回転 |
| SO(3,1) | 6 | Lorentz |
| SL(2,ℝ) | 3 | AdS₃ 等 |
| **Poincaré** | 10 | 特殊相対論 |
| **E_8** | 248 | string/M (Heterotic) |

### 1.3 連続パラメータ

例 SU(2) 元:
```
U = exp(i θ_a σ_a / 2)
σ_a: Pauli matrices, θ_a: 3 連続パラメータ
```

### 1.4 ITU 視点

```
K_sym = ITU symmetry K-state
Lie 群 = K_sym connected (連続)
```

---

## 2. ★ Lie 代数 ★

### 2.1 定義

Lie 群の **接空間 at identity**:

```
g = T_e G
```

### 2.2 commutator (Lie bracket)

```
[X, Y] = XY - YX
```

= bilinear + antisymmetric + Jacobi identity。

### 2.3 構造定数

```
[T^a, T^b] = i f^{abc} T^c
```

| 代数 | f^{abc} |
|---|---|
| SU(2) | ε^{abc} (Levi-Civita) |
| SU(3) | Gell-Mann 8 generators |
| SO(n) | so(n) antisymmetric |

### 2.4 Killing form

```
g_{ab} = f_{acd} f_{bdc}
```

**Cartan-Killing**: simple iff non-degenerate negative-definite。

### 2.5 ITU 視点

```
Lie 代数 = K_sym infinitesimal generator
構造定数 f^{abc} = K_sym 結合則
```

---

## 3. ★ Cartan 分類 (1894) ★

### 3.1 主張

任意の **complex simple Lie 代数** は 4 + 5 = 9 種に分類:

```
A_n  (n ≥ 1): SU(n+1)
B_n  (n ≥ 2): SO(2n+1)
C_n  (n ≥ 3): Sp(2n)
D_n  (n ≥ 4): SO(2n)
+ E_6, E_7, E_8, F_4, G_2 (例外型)
```

### 3.2 例外 Lie 代数

| 名 | dim | rank | 物理 |
|---|---|---|---|
| G_2 | 14 | 2 | M 理論 G_2-holonomy |
| F_4 | 52 | 4 | Octonionic |
| E_6 | 78 | 6 | GUT 候補 |
| E_7 | 133 | 7 | string |
| **E_8** | **248** | **8** | **Heterotic E_8 × E_8** |

### 3.3 Dynkin diagrams

各 Lie 代数を **graph** で表す:
- A_n: linear chain n nodes
- D_n: chain + branch
- E_8: 7+1 nodes, 1 branch

### 3.4 ITU 視点

```
Cartan 分類 = K_sym の universal taxonomy
9 種 = K_sym irreducible bases
```

---

## 4. ★ 表現論 ★

### 4.1 highest weight 理論

Cartan subalgebra (極大可換) + 重み (weights) + roots。

### 4.2 例: SU(2)

```
表現: spin j = 0, 1/2, 1, 3/2, ...
dim = 2j + 1
```

### 4.3 例: SU(3)

| 表現 | dim | 物理 |
|---|---|---|
| 1 | 1 | singlet |
| 3 | 3 | quark |
| 3̄ | 3 | antiquark |
| **8** | 8 | gluon, meson octet |
| 10 | 10 | baryon decuplet |

### 4.4 Casimir 演算子

```
C_2 = T^a T^a
```

= 表現を label。例 SU(2): C_2 |j⟩ = j(j+1) |j⟩。

### 4.5 ITU 視点

```
表現論 = K_sym の eigendecomposition
Casimir = K_sym universal label
```

---

## 5. 物理応用

### 5.1 Standard Model (Phase 135)

```
G_SM = SU(3)_C × SU(2)_L × U(1)_Y
12 generators
```

### 5.2 GUT 候補

| 群 | dim | 物理 |
|---|---|---|
| SU(5) (Georgi-Glashow 1974) | 24 | minimal GUT |
| **SO(10)** | 45 | viable GUT (Phase 140) |
| **E_6** | 78 | string-derived |
| E_8 × E_8 | 496 | Heterotic |

### 5.3 Lorentz + Poincaré

```
SO(3,1) (Lorentz, 6 generators) ⊂ Poincaré (Lorentz + translation, 10)
```

= 特殊相対論の対称性。

### 5.4 ITU 視点

```
SM gauge group G_SM = K_sym × K_field
GUT = K_sym unified
```

---

## 6. SUSY (Phase 140 + 174)

### 6.1 Graded Lie 代数

```
{Q_α, Q_β^†} = 2 σ^μ_{αβ} P_μ
```

= **anticommutator** で fermion-boson 統一。

### 6.2 Coleman-Mandula no-go (1967) + Haag-Łopuszański-Sohnius (1975)

bosonic Lie 代数 × Poincaré では non-trivial 拡張不能 → **graded** (super) Lie 代数のみ可能。

### 6.3 ITU 視点

```
SUSY = K_sym 拡張 (Z_2-graded)
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Pauli matrices** σ_a で SU(2) [σ_a, σ_b] = 2i ε_abc σ_c
2. **Gell-Mann matrices** SU(3) 8 generators + commutators
3. **Casimir SU(2)** j(j+1) for j = 0, 1/2, 1, 3/2
4. **Lie 代数 dim** classical groups: A_n, B_n, C_n, D_n
5. **Dynkin diagrams** A_n, E_8 visualization

---

## 8. Phase 167 主結論

1. **Lie 群** = 連続対称性の数学的基盤
2. **Lie 代数** = 接空間 + commutator
3. **Cartan 分類 (1894)**: A_n, B_n, C_n, D_n + 5 例外 (E_6, E_7, E_8, F_4, G_2)
4. **表現論**: weights, Casimir, Dynkin diagrams
5. **SM**: SU(3) × SU(2) × U(1) (12 generators, Phase 135)
6. **GUT**: SO(10), E_6, E_8 × E_8 Heterotic
7. **SUSY**: graded (Z_2) Lie 代数 (Coleman-Mandula no-go 拡張)
8. **ITU**: K_sym = symmetry K-state
9. **次の Phase 168** で **Soliton + Lax pair + 厳密可解模型**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Lie 群 | K_sym connected continuous |
| Lie 代数 | K_sym infinitesimal generator |
| 構造定数 f^{abc} | K_sym 結合則 |
| Cartan 分類 | K_sym universal taxonomy |
| 表現論 | K_sym eigendecomposition |
| Casimir | K_sym universal label |
| Dynkin diagram | K_sym topological signature |
| SUSY | K_sym graded extension |

---

## 引用

```
Terada, M. (2026). Phase 167: Lie groups, Lie algebras, Cartan classification,
and representation theory in ITU (Tier 1 #24 phase 1/8). Zenodo.
DOI: [10.5281/zenodo.20251178](https://doi.org/10.5281/zenodo.20251178).
```

主要参考文献:
- Lie, S. (1873-1888) Theorie der Transformationsgruppen
- Cartan, É. (1894) Sur la structure des groupes de transformations finis et continus
- Killing, W. (1888-1890) "Die Zusammensetzung der stetigen endlichen Transformationsgruppen" Math. Ann.
- Weyl, H. (1925-1926) Classical Groups (later book 1939)
- Dynkin, E. B. (1947) "Structure of semisimple algebras" Russ. Math. Surveys 2, 59
- Coleman, S., Mandula, J. (1967) "All possible symmetries of the S matrix" Phys. Rev. 159, 1251
- Haag, R., Łopuszański, J. T., Sohnius, M. (1975) "All possible generators of supersymmetries of the S matrix" Nucl. Phys. B 88, 257
- Gell-Mann, M. (1962) "Symmetries of baryons and mesons" Phys. Rev. 125, 1067
- Georgi, H., Glashow, S. L. (1974) "Unity of all elementary particle forces" PRL 32, 438
- Humphreys, J. E. (1972) Introduction to Lie Algebras and Representation Theory. Springer
- Fulton, W., Harris, J. (1991) Representation Theory: A First Course. Springer
- Hall, B. C. (2015) Lie Groups, Lie Algebras, and Representations, 2nd ed. Springer
