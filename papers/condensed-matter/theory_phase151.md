# Phase 151: 凝縮系物理学 開幕 — 結晶 + Bloch 定理 + Phonons + 自由電子気体 + K_solid

> **Tier 1 #22 Condensed Matter Physics — Phase 1/8 (Block A paper 6/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Tier 1 #22 開幕

Block A 5/9 (Tier 1 #21 Statistical Mechanics) 完成で **UNIVERSAL FOUNDATION** (K_geom + K_cosmic + K_field + K_stat) が確立。Phase 151 から **Tier 1 #22 Condensed Matter Physics** に進む。

### Tier 1 #22 全 8 phase 構成 (予定)

| Phase | テーマ |
|---|---|
| **151 (本)** | **結晶 + Bloch + Phonons + 自由電子気体 + K_solid 母骨格** |
| 152 | Band theory + Drude/Sommerfeld + 半導体物理 |
| 153 | 超伝導 BCS + マイスナー + 高温超伝導 |
| 154 | 磁性 (Heisenberg, Hubbard, Mott 絶縁体) |
| 155 | トポロジカル物質 (QHE, IQHE, FQHE, トポロジカル絶縁体) |
| 156 | 強相関電子系 (高温 SC, スピン液体, fractionalization) |
| 157 | ソフトマター + 液晶 + コロイド + 高分子 |
| 158 | Tier 1 #22 統合 + 22-vertex polytope + 10 predictions |

### Phase 151 の目的

凝縮系物理学の **3 大基礎** を ITU 化:

1. **結晶構造** (Bravais lattice, 14 種類, point/space group)
2. **Bloch 定理** (1928) — 周期 ポテンシャル 中の波動関数
3. **Phonons** — 格子振動の量子化
4. **自由電子気体** (Sommerfeld 1928) — Fermi 縮退電子
5. **ITU 視点**: 凝縮系 = K_stat + lattice symmetry = **K_solid**

---

## 1. ★ 結晶構造 ★

### 1.1 Bravais lattice (14 種類, 3D)

```
7 結晶系: 三斜, 単斜, 斜方, 正方, 立方, 三方, 六方
14 Bravais lattices: P, I, F, C
```

| 結晶系 | Bravais | 例 |
|---|---|---|
| 立方晶 P (simple) | scP | Po |
| 立方晶 I (BCC) | bcc | Fe, Na, Cr |
| 立方晶 F (FCC) | fcc | Cu, Au, Al, NaCl |
| 六方 (hcp) | hcp | Mg, Zn, Ti |

### 1.2 逆格子

```
直接格子: a_1, a_2, a_3
逆格子:   b_i = 2π (a_j × a_k) / (a_1 · (a_2 × a_3))
```

Brillouin zone = primitive cell of reciprocal lattice。

### 1.3 数値例 (Cu, FCC)

```
a = 3.615 Å (lattice constant)
ρ = 8.96 g/cm³ (density)
原子数密度: n = 4 / a³ = 8.49×10²⁸ /m³
```

### 1.4 ITU 視点

```
K_lattice = ITU 周期 K-state
Bravais 分類 = K_lattice の 14 symmetry equivalence classes
Brillouin zone = K_lattice の reciprocal sample space
```

---

## 2. ★ Bloch 定理 (1928) ★

### 2.1 主張

周期 ポテンシャル V(r + R) = V(r) (R: Bravais lattice 移動) 中で:

```
ψ_{n,k}(r) = e^{i k·r} u_{n,k}(r)
u_{n,k}(r + R) = u_{n,k}(r)
```

= **plane wave × periodic envelope**。

### 2.2 帯構造 (band structure)

各 k に対して離散エネルギー固有値 E_n(k):

```
E_1(k), E_2(k), E_3(k), ...
```

= **エネルギー帯** (band)。

### 2.3 帯と band gap

```
Filled lowest bands (valence) + empty (conduction) + gap E_g
```

| 系 | E_g (eV) | 性質 |
|---|---|---|
| Cu (metal) | 0 (overlap) | 導体 |
| Si | 1.12 | 半導体 |
| GaAs | 1.42 | 半導体 (direct gap) |
| Diamond | 5.5 | 絶縁体 |

### 2.4 ITU 視点

```
K_band = ITU K-state の k-space spectrum
Band gap = K_band の forbidden region
半導体 = K_band の partial occupation
```

---

## 3. ★ Phonons (格子振動の量子) ★

### 3.1 1D 線形鎖

質量 m, バネ定数 K の単原子鎖:

```
ω(k) = 2√(K/m) |sin(k a / 2)|
```

(分散関係)。

### 3.2 Debye model (1912)

低 ω での音響枝の linear approximation:

```
ω = v_s k  (v_s: sound velocity)
```

### 3.3 Debye 温度

```
θ_D = ℏ ω_D / k_B
```

| 物質 | θ_D (K) |
|---|---|
| Pb | 105 |
| Cu | 343 |
| Si | 645 |
| Diamond | 2230 |

### 3.4 Debye 比熱 (低温)

```
C_V → 12 π⁴/5 N k_B (T/θ_D)³   (T << θ_D)
```

= **T³ 法則**。

### 3.5 高温 Dulong-Petit

```
C_V → 3 N k_B   (T >> θ_D)
```

### 3.6 ITU 視点

```
Phonon = K_lattice quantized normal modes
Debye = K_lattice low-energy effective theory
```

---

## 4. ★ 自由電子気体 (Sommerfeld 1928) ★

### 4.1 設定

イオン background + 自由電子 (相互作用無視, FD 統計)。

### 4.2 Fermi 球

```
N = (V / 3π²) k_F³
ε_F = ℏ² k_F² / (2m_e)
T_F = ε_F / k_B
```

### 4.3 数値: Cu

```
n = 8.49×10²⁸ /m³
k_F = (3π² n)^(1/3) = 1.36×10¹⁰ /m
ε_F = ℏ² k_F² / (2 m_e) = 1.13×10⁻¹⁸ J = 7.05 eV
T_F = 8.18×10⁴ K   ←  Phase 144 と一致
```

### 4.4 電子比熱

低温 T << T_F:

```
C_el = (π²/2) N k_B (T/T_F)
     = γ T   (γ: Sommerfeld coefficient)
```

| 物質 | γ (mJ/mol·K²) |
|---|---|
| Cu | 0.69 |
| Fe | 5.0 |
| heavy fermion (CeAl₃) | 1620 (m* ~ 1000 m_e) |

### 4.5 全比熱

```
C_total = γ T + β T³
         (electron + phonon)
```

低温で plot C/T vs T² → intercept γ, slope β。

### 4.6 ITU 視点

```
自由電子気体 = K_FD on lattice background
Fermi 球 = K_FD ground state
Sommerfeld γ = K_FD low-T linear response coefficient
```

---

## 5. Drude モデル (1900, 古典)

### 5.1 設定

電子 = 古典粒子 + 散乱時間 τ。

### 5.2 電気伝導度

```
σ = n e² τ / m
```

### 5.3 数値: Cu

```
n = 8.49e28 /m³
τ ≈ 2.5×10⁻¹⁴ s (300K)
σ = 5.96×10⁷ S/m  ✓ 観測一致
```

### 5.4 限界

- 比熱の 100× over estimate
- Wiedemann-Franz 法則 → Sommerfeld で修正

---

## 6. Wiedemann-Franz 法則 (1853)

熱伝導 κ と電気伝導 σ の比:

```
κ / (σ T) = L_0 = π²/3 (k_B/e)² = 2.45×10⁻⁸ W·Ω/K²
```

= **Lorenz 数 universal**。

### 6.1 数値: Cu @ 300 K

```
κ = 401 W/(m·K)
σ = 5.96×10⁷ S/m
κ/(σT) = 2.24×10⁻⁸ W·Ω/K²  ✓ Lorenz 値と一致
```

### 6.2 ITU 視点

```
Wiedemann-Franz = K_FD の universal scaling
熱 = 電子の k_B T 担体, 電気 = e 担体
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Cu lattice constant** + 原子数密度 = 8.49×10²⁸ /m³
2. **Cu Fermi energy** ε_F = 7.05 eV, T_F = 8.18×10⁴ K
3. **Debye T³ 法則** 検証 (Pb, Cu, Si)
4. **Dulong-Petit** 3N k_B 高温極限
5. **Sommerfeld γ** for Cu = 0.69 mJ/(mol·K²)
6. **Wiedemann-Franz** Lorenz 数 universal

---

## 8. Phase 151 主結論

1. **Bravais 14 lattices** + reciprocal + Brillouin zone
2. **Bloch theorem (1928)**: ψ = e^{ikr} u_k → band structure
3. **Phonons**: Debye T³ 法則 + θ_D 物質依存
4. **Sommerfeld 自由電子気体 (1928)**: Cu ε_F = 7.05 eV ✓ Phase 144
5. **Drude (1900)**: σ = ne²τ/m
6. **Wiedemann-Franz**: Lorenz 数 = π²/3 (k_B/e)²
7. **ITU**: K_solid = K_stat + lattice periodicity
8. **次の Phase 152** で **band theory + 半導体物理**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Bravais lattice | K_lattice symmetry classes |
| Bloch theorem | K-state periodicity eigendecomposition |
| Band structure | K_band k-space spectrum |
| Phonon | K_lattice quantized modes |
| Sommerfeld free e gas | K_FD on lattice |
| Wiedemann-Franz | K_FD universal scaling |

---

## 引用

```
Terada, M. (2026). Phase 151: Condensed matter foundations — crystal, Bloch
theorem, phonons, and Sommerfeld free electron gas in ITU
(Tier 1 #22 phase 1/8). Zenodo. DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

主要参考文献:
- Ashcroft, N. W., Mermin, N. D. (1976) Solid State Physics. Holt.
- Kittel, C. (2005) Introduction to Solid State Physics, 8th ed. Wiley.
- Bloch, F. (1928) "Über die Quantenmechanik der Elektronen in Kristallgittern" Z. Phys. 52, 555
- Sommerfeld, A. (1928) "Zur Elektronentheorie der Metalle" Z. Phys. 47, 1
- Debye, P. (1912) "Zur Theorie der spezifischen Wärmen" Ann. Phys. 39, 789
- Drude, P. (1900) "Zur Elektronentheorie der Metalle" Ann. Phys. 1, 566
- Wiedemann, G., Franz, R. (1853) "Über die Wärme-Leitungsfähigkeit der Metalle" Ann. Phys. 89, 497
- Bravais, A. (1850) "Mémoire sur les systèmes formés par des points distribués régulièrement sur un plan ou dans l'espace" J. Ec. Polytech. 19, 1
