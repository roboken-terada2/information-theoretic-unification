# Phase 154: 磁性 — Heisenberg + Hubbard + Mott 絶縁体 + 反強磁性 + K_magnetic

> **Tier 1 #22 Condensed Matter Physics — Phase 4/8 (Block A paper 6/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 154 の目的

Phase 153 で超伝導を扱った (K_SC = Cooper pair 凝縮)。Phase 154 では **磁性** へ:

1. **Heisenberg model**: H = -J Σ S_i · S_j
2. **Curie-Weiss law**: χ = C / (T - T_c)
3. **強磁性 (Fe, Co, Ni)** + **反強磁性 (MnO, NiO)** + **フェリ磁性 (Fe₃O₄)**
4. **Spin waves (magnons)**: 連続対称性 Goldstone (Phase 145 接続)
5. **Hubbard model + Mott 絶縁体** (cuprate 親 → 高温 SC)
6. **Frustration + spin liquid**
7. **Stoner ferromagnetism** (itinerant)
8. **ITU 視点**: K_magnetic = K_stat + spin DOF + exchange coupling

中心テーゼ:

> **磁性 = K_spin の集団秩序 (broken symmetry)**。
> Mott 絶縁体 = K_correlation の U/t 大領域。
> Heisenberg AF = K_spin の SU(2) symmetry breaking。
> Stoner = K_FD の交換項 instability。

---

## 1. ★ Heisenberg Model ★

### 1.1 Hamiltonian

```
H = -J Σ_{⟨i,j⟩} S_i · S_j - g μ_B B Σ_i S_i^z

J > 0: 強磁性 (FM)
J < 0: 反強磁性 (AF)
```

### 1.2 ★ Heisenberg vs Ising ★

| Model | 自由度 | 連続対称性 | Goldstone |
|---|---|---|---|
| Ising | s = ±1 (1 軸) | Z_2 (離散) | なし |
| XY | (s_x, s_y) (2 軸) | O(2) ~ U(1) | あり |
| **Heisenberg** | **(s_x, s_y, s_z) (3 軸)** | **O(3)** | **magnon** |

Mermin-Wagner: 2D で連続対称性破れ ない (有限 T)。

### 1.3 強磁性体

| 物質 | T_C (Curie K) | μ/atom (μ_B) |
|---|---|---|
| Fe | 1043 | 2.22 |
| Co | 1394 | 1.72 |
| Ni | 631 | 0.61 |
| Gd | 293 | 7.55 |

### 1.4 反強磁性体

| 物質 | T_N (Néel K) |
|---|---|
| MnO | 116 |
| FeO | 198 |
| NiO | 525 |
| Cr | 311 |
| α-Fe₂O₃ | 953 |

### 1.5 ITU 視点

```
Heisenberg = K_spin の SU(2) invariant Hamiltonian
J = K_exchange coupling (Phase 152 hopping t の 4t²/U)
強磁性 = K_spin の 大域 SU(2) symmetry breaking
```

---

## 2. ★ Curie-Weiss Law (1907) ★

### 2.1 唯象式

```
χ(T) = C / (T - θ)

θ = T_C (FM) or -T_N (AF)
C = Curie constant
```

### 2.2 数値: Fe

```
θ ≈ 1043 K
C = N μ²_eff / (3 k_B)
μ_eff = √(g²μ_B² S(S+1)) ≈ 2.83 μ_B (Fe³⁺)
```

### 2.3 ITU 視点

```
Curie-Weiss = K_spin mean-field response の特異性
```

---

## 3. ★ Magnons (Spin Waves) ★

### 3.1 1D FM Heisenberg 分散

```
ε(k) = 2 J S (1 - cos(k a))
     ≈ J S a² k²   (small k)
```

= **ω ∝ k² 二次分散** (FM)。

### 3.2 1D AF Heisenberg 分散

```
ε(k) = 2 J S |sin(k a)|
     ≈ 2 J S a |k|  (small k)
```

= **ω ∝ |k| 線形分散** (AF)。

### 3.3 Bloch T^(3/2) 法則

3D FM 低温:

```
M(T) = M(0) [1 - (T/T_C)^{3/2} × const]
```

= magnon 励起による磁化減少 (Bloch 1930)。

### 3.4 ITU 視点

```
Magnon = K_spin Goldstone mode (連続 SU(2) 破れの帰結, Phase 145)
FM: quadratic (broken symmetry of non-conserved order param)
AF: linear (broken symmetry of conserved order param)
```

---

## 4. ★ Hubbard Model + Mott 絶縁体 ★

### 4.1 Hamiltonian

```
H = -t Σ_{⟨i,j⟩,σ} (c^†_{iσ} c_{jσ} + h.c.) + U Σ_i n_{i↑} n_{i↓}
```

- t: hopping (Phase 152 と同)
- U: on-site Coulomb repulsion

### 4.2 限界

- **U / t → 0**: free electron (Phase 151)
- **U / t → ∞**: Mott insulator (各 site 1 電子, 局在)

### 4.3 Mott 絶縁体

**band 半充填 + U > W で絶縁体**:

| 物質 | U (eV) | W (eV) | U/W | type |
|---|---|---|---|---|
| Cu metal | 7 | 9 | 0.78 | metal |
| NiO | 8 | 2 | 4 | Mott |
| **La₂CuO₄** | **10** | **2** | **5** | **Mott (cuprate 親)** |
| V₂O₃ | 2 | 1.5 | 1.3 | Mott |

### 4.4 ★ Cuprate ↔ HTS connection ★

```
親物質 (x=0): Mott 絶縁体 (反強磁性)
hole doping (x ~ 0.1-0.25): 高温 SC (Phase 153)
```

⇒ **HTS = Mott 絶縁体に hole 注入** → 強相関電子系 (Phase 156 で詳述)。

### 4.5 ITU 視点

```
Hubbard = K_band + K_correlation
Mott = K_correlation の U → ∞ 極限 (kinetic 失活)
Cuprate HTS = K_correlation × K_doping → K_SC
```

---

## 5. Anderson Superexchange (1959)

### 5.1 機構

Mott 絶縁体で 2 spin 間の **virtual hopping** が exchange を生成:

```
J_ex ≈ -4 t² / U  (反強磁性)
```

### 5.2 数値: La₂CuO₄

```
t ≈ 0.4 eV, U ≈ 10 eV
J_ex = -4 × 0.16 / 10 ≈ -0.064 eV ≈ -740 K
```

実測 J ≈ -1500 K と整合 (再正規化込み)。

### 5.3 ITU 視点

```
Superexchange = K_correlation 二次摂動 → K_exchange
```

---

## 6. ★ Stoner Ferromagnetism (1938, itinerant) ★

### 6.1 Stoner 判定条件

free electron + exchange I:

```
I D(ε_F) > 1   →   ferromagnetic
```

### 6.2 数値: Fe, Co, Ni

| 物質 | D(ε_F) (states/eV/atom) | I (eV) | I × D | FM? |
|---|---|---|---|---|
| Fe | 2.0 | 0.93 | 1.86 | ✓ |
| Co | 1.8 | 0.99 | 1.78 | ✓ |
| Ni | 2.8 | 0.99 | 2.77 | ✓ |
| Cu | 0.3 | 0.73 | 0.22 | ✗ |
| Pd | 1.8 | 0.50 | 0.90 | nearly ✓ |

### 6.3 ITU 視点

```
Stoner = K_FD の交換項 instability → K_spin 分極
```

---

## 7. ★ Frustration + Spin Liquid ★

### 7.1 Geometric frustration

三角格子 AF: 3 spin が全て anti-parallel **不可能**:

```
↑ ↓
 \ /
  ?   (frustrated)
```

⇒ ground state 退化 → spin liquid 候補。

### 7.2 例

- Triangular: Cs₂CuCl₄
- Kagome: ZnCu₃(OH)₆Cl₂ (Herbertsmithite)
- Pyrochlore: spin ice Dy₂Ti₂O₇, Ho₂Ti₂O₇

### 7.3 Spin liquid signatures

- No magnetic order down to T → 0
- Fractional excitations (spinons)
- Topological order

### 7.4 ITU 視点

```
Frustration = K_spin の geometric constraint
Spin liquid = K_spin の topological K-state (Anderson RVB 1973)
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **2D Ising AF Monte Carlo** (Phase 145 拡張)
2. **Heisenberg dispersion** FM (k²) vs AF (k)
3. **Curie-Weiss χ(T)** Fe, Co, Ni
4. **Stoner 判定** Fe/Co/Ni/Cu/Pd
5. **Superexchange J = 4t²/U** for cuprate
6. **Bloch T^{3/2} law** for magnetization

---

## 9. Phase 154 主結論

1. **Heisenberg (1928)**: H = -J Σ S·S, SU(2) symmetry
2. **Curie-Weiss (1907)**: χ = C/(T-θ)
3. **Magnon**: FM k², AF |k| (Goldstone Phase 145)
4. **Hubbard**: t/U 競合, Mott 絶縁体 (cuprate 親)
5. **Anderson superexchange (1959)**: J = -4t²/U
6. **Stoner (1938)**: I·D(ε_F) > 1 → FM
7. **Frustration → spin liquid (Anderson RVB 1973)**
8. **ITU**: K_magnetic = K_stat + K_spin (SU(2))
9. **次の Phase 155** で **トポロジカル物質 + QHE + IQHE/FQHE**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Heisenberg | K_spin SU(2) Hamiltonian |
| Curie-Weiss | K_spin mean-field response |
| Magnon | K_spin Goldstone (Phase 145 接続) |
| Hubbard | K_band + K_correlation |
| Mott | K_correlation U/t → ∞ |
| Superexchange | K_correlation perturbative |
| Stoner | K_FD exchange instability |
| Frustration | K_spin geometric constraint |
| Spin liquid | K_spin topological order |

---

## 引用

```
Terada, M. (2026). Phase 154: Magnetism — Heisenberg, Hubbard, Mott insulator,
and antiferromagnetism in ITU (Tier 1 #22 phase 4/8). Zenodo. DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

主要参考文献:
- Heisenberg, W. (1928) "Zur Theorie des Ferromagnetismus" Z. Phys. 49, 619
- Weiss, P. (1907) "L'hypothèse du champ moléculaire" J. Phys. Radium 6, 661
- Néel, L. (1948) "Propriétés magnétiques des ferrites" Ann. Phys. 3, 137 (Nobel 1970)
- Bloch, F. (1930) "Zur Theorie des Ferromagnetismus" Z. Phys. 61, 206
- Hubbard, J. (1963) "Electron correlations in narrow energy bands" Proc. R. Soc. A 276, 238
- Mott, N. F. (1968) "Metal-insulator transition" Rev. Mod. Phys. 40, 677 (Nobel 1977)
- Anderson, P. W. (1959) "New approach to the theory of superexchange interactions" Phys. Rev. 115, 2
- Anderson, P. W. (1973) "Resonating valence bonds: A new kind of insulator?" Mater. Res. Bull. 8, 153
- Stoner, E. C. (1938) "Collective electron ferromagnetism" Proc. R. Soc. A 165, 372
- Mermin, N. D., Wagner, H. (1966) PRL 17, 1133
- Goldstone, J. (1961) Nuovo Cim. 19, 154
- Bednorz, J. G., Müller, K. A. (1986) Z. Phys. B 64, 189
