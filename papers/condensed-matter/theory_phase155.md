# Phase 155: トポロジカル物質 — 量子 Hall + トポロジカル絶縁体 + K_topo

> **Tier 1 #22 Condensed Matter Physics — Phase 5/8 (Block A paper 6/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 155 の目的

Phase 154 で磁性 (K_magnetic) を扱った。Phase 155 では **トポロジカル物質** へ進む — 21 世紀の凝縮系物理の **革命** とされる:

1. **整数量子 Hall 効果 (IQHE)** — von Klitzing 1980 (Nobel 1985)
2. **分数量子 Hall 効果 (FQHE)** — Tsui-Stormer-Gossard 1982 (Nobel 1998)
3. **Berry phase + Berry curvature**
4. **トポロジカル絶縁体 (TI)** — Kane-Mele 2005, BHZ 2006 (Nobel 2016)
5. **Weyl/Dirac semimetal**
6. **ITU 視点**: K_topo = K_band の topological invariant 分類

中心テーゼ:

> **トポロジカル物質 = K_band の topological invariant による分類**。
> Chern number = K_band の 1st 整数不変量 (IQHE).
> Z₂ index = K_band の time-reversal-protected 不変量 (TI).
> Bulk-boundary 対応 = K_topo の境界での conducting state 強制。

---

## 1. ★ 整数量子 Hall 効果 (IQHE) — von Klitzing 1980 ★

### 1.1 観測

2DEG (GaAs/AlGaAs 界面) に強磁場 → Hall conductance:

```
σ_xy = ν e² / h   (ν = 1, 2, 3, ...)
```

精度: **10⁻⁹** (= 抵抗標準, von Klitzing constant)。

### 1.2 von Klitzing constant

```
R_K = h / e² = 25,812.807... Ω  ★ 普遍定数
```

2019 SI 改訂で **抵抗の primary standard**。

### 1.3 Landau level

磁場 B 中の電子のエネルギー:

```
ε_n = ℏ ω_c (n + 1/2)
ω_c = eB / m
```

= **量子化された Landau 準位**, 縮退度 N_Φ = eBA/h = Φ/Φ_0。

### 1.4 数値例 (B = 10 T, GaAs m*=0.067)

```
ω_c = e × 10 / (0.067 × 9.11e-31) = 2.63×10¹³ rad/s
ℏω_c = 17.3 meV
n = 2DEG density / N_Φ
```

### 1.5 TKNN formula (1982)

```
σ_xy = (e²/h) × C_n   (C_n = Chern number)
```

= **topological 量子数** が σ_xy を厳密に量子化。

### 1.6 ITU 視点

```
IQHE = K_band の 1st Chern number 表現
量子化 σ_xy = K_topo の universal Hall conductance
```

---

## 2. ★ 分数量子 Hall 効果 (FQHE) — Tsui-Stormer-Gossard 1982 ★

### 2.1 観測

**より清浄な** 2DEG + 強磁場 → 分数 ν:

```
σ_xy = ν e²/h   (ν = 1/3, 2/5, 3/7, 5/2, ...)
```

### 2.2 Laughlin 波動関数 (1983, Nobel 1998)

ν = 1/m (m = 3, 5, ...):

```
Ψ_L = Π_{i<j} (z_i - z_j)^m × exp(-Σ |z_i|² / (4 l_B²))
```

z_i = x_i + i y_i (複素 2D 座標)。

### 2.3 fractional 励起

```
Quasi-particle 電荷 e* = e/m   (m=3 で e/3)
Anyon 統計 (Bose/Fermi の中間)
```

### 2.4 ν = 5/2 状態

```
Moore-Read 1991: non-abelian anyon (Pfaffian state)
→ topological 量子コンピュータ候補 (Phase 156 接続)
```

### 2.5 ITU 視点

```
FQHE = K_correlation × K_topo の 強相関 topological state
Anyon = K_topo の fractional statistics
e/3 = K_charge fractionalization
```

---

## 3. ★ Berry Phase + Berry Curvature ★

### 3.1 Berry phase (1984)

断熱 cycle 後の波動関数:

```
γ = i ∮ ⟨ψ(R) | ∇_R | ψ(R)⟩ · dR
```

### 3.2 Berry curvature

```
Ω_n(k) = ∇_k × A_n(k)
A_n(k) = i ⟨u_n,k | ∇_k | u_n,k⟩
```

### 3.3 Chern number

```
C_n = (1/2π) ∫_BZ Ω_n(k) d²k   ∈ ℤ
```

= **第 1 Chern class 整数** (topological invariant)。

### 3.4 ITU 視点

```
Berry phase = K_band の internal connection
Chern number = K_band の topological integer invariant
```

---

## 4. ★ トポロジカル絶縁体 (TI) ★

### 4.1 Quantum Spin Hall (QSH, 2005-2007)

2D TI: Kane-Mele 2005, BHZ 2006 提案。
König et al. 2007: **HgTe/CdTe 量子井戸** で観測。

特徴:
- Bulk: gap あり (絶縁体)
- Edge: gapless helical edge state (Z₂-protected)

### 4.2 Z₂ invariant

時間反転対称性下:
```
ν ∈ {0, 1}  (Z₂)
ν = 0: trivial
ν = 1: TI (non-trivial)
```

### 4.3 3D TI

| 物質 | E_g (meV) | 表面状態 |
|---|---|---|
| Bi₂Se₃ | 300 | single Dirac cone |
| Bi₂Te₃ | 150 | single Dirac cone |
| Sb₂Te₃ | 280 | single Dirac cone |
| Bi₁Sb₁ | 30 | 5 Dirac cones |

### 4.4 数値: Bi₂Se₃

```
Surface state: linear dispersion E(k) = ℏ v_F |k|
v_F ≈ 5×10⁵ m/s
Spin-momentum locking
```

### 4.5 ITU 視点

```
TI = K_band の Z₂-protected topological insulator
表面状態 = K_topo bulk-boundary correspondence
Spin-momentum locking = K_topo の helical 結合
```

---

## 5. ★ Weyl / Dirac Semimetal ★

### 5.1 Weyl 点

3D で band 縮退点 (Weyl point) が pair で出現:

```
H = ± ℏ v_F σ · k   (±: chirality)
```

= 3D Weyl fermion 実現 (素粒子物理で発見されなかった粒子)。

### 5.2 物質例

| 物質 | type |
|---|---|
| TaAs, TaP, NbAs, NbP | Weyl Type I |
| MoTe₂, WTe₂ | Weyl Type II |
| Cd₃As₂, Na₃Bi | Dirac semimetal |

### 5.3 Fermi arc

Weyl 点を結ぶ **境界 Fermi arc** (open Fermi line) — 通常金属にはない構造。

### 5.4 ITU 視点

```
Weyl semimetal = K_band の chirality-pair topological state
Fermi arc = K_topo bulk Weyl points を結ぶ表面構造
```

---

## 6. Higher-order TI + Crystalline TI

### 6.1 Higher-order TI (HOTI)

```
3D HOTI: gapped bulk + gapped surfaces + gapless hinges
```

### 6.2 Topological crystalline insulator (TCI)

非対称結晶 symmetry が protect する topology。例: SnTe (mirror Chern)。

### 6.3 ITU 視点

```
HOTI / TCI = K_topo の階層的 protection
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Landau level** ε_n = ℏω_c(n+1/2)
2. **σ_xy 量子化** ν e²/h plateaus
3. **von Klitzing constant** R_K = h/e² = 25,812.8 Ω
4. **Berry phase** simple two-band model
5. **Chern number** numerical integration
6. **Bi₂Se₃ surface state** linear dispersion
7. **Laughlin ν = 1/3** quasi-particle charge e/3

---

## 8. Phase 155 主結論

1. **IQHE (von Klitzing 1980, Nobel 1985)**: σ_xy = ν e²/h, R_K = 25,812.8 Ω
2. **TKNN (1982)**: σ_xy = (e²/h) × Chern number
3. **FQHE (Tsui-Stormer-Gossard 1982, Nobel 1998)**: ν = 1/3, anyon e/3
4. **Laughlin wavefunction (1983)**: Π(z_i - z_j)^m × Gaussian
5. **Berry phase (1984)** + Chern number ∈ ℤ
6. **TI (Kane-Mele 2005, BHZ 2006)**: Z₂ invariant, HgTe edge state (König 2007)
7. **3D TI (Bi₂Se₃, Bi₂Te₃)**: single Dirac cone surface
8. **Weyl/Dirac semimetal**: TaAs, Cd₃As₂
9. **Topological 2016 Nobel**: Thouless-Haldane-Kosterlitz
10. **ITU**: K_topo = K_band topological invariants
11. **次の Phase 156** で **強相関電子系 + 高温 SC 機構 + スピン液体**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Landau level | K_band magnetic 量子化 |
| σ_xy 量子化 | K_topo Chern number 表現 |
| von Klitzing R_K | K_topo 普遍抵抗 |
| Laughlin | K_correlation × K_topo |
| Anyon | K_topo fractional statistics |
| Berry phase | K_band internal connection |
| Chern number | K_band topological invariant |
| TI | K_band Z₂-protected |
| Surface state | K_topo bulk-boundary correspondence |
| Weyl semimetal | K_band chirality-pair |

---

## 引用

```
Terada, M. (2026). Phase 155: Topological matter — quantum Hall effect,
topological insulators, and Weyl semimetals in ITU
(Tier 1 #22 phase 5/8). Zenodo. DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

主要参考文献:
- von Klitzing, K., Dorda, G., Pepper, M. (1980) "New method for high-accuracy determination of the fine-structure constant based on quantized Hall resistance" PRL 45, 494
- Tsui, D. C., Stormer, H. L., Gossard, A. C. (1982) "Two-dimensional magnetotransport in the extreme quantum limit" PRL 48, 1559
- Laughlin, R. B. (1983) "Anomalous quantum Hall effect: An incompressible quantum fluid with fractionally charged excitations" PRL 50, 1395
- Thouless, D. J., Kohmoto, M., Nightingale, M. P., den Nijs, M. (TKNN, 1982) "Quantized Hall conductance in a two-dimensional periodic potential" PRL 49, 405
- Berry, M. V. (1984) "Quantal phase factors accompanying adiabatic changes" Proc. R. Soc. A 392, 45
- Haldane, F. D. M. (1988) "Model for a quantum Hall effect without Landau levels" PRL 61, 2015
- Kane, C. L., Mele, E. J. (2005) "Quantum spin Hall effect in graphene" PRL 95, 226801
- Bernevig, B. A., Hughes, T. L., Zhang, S. C. (2006) "Quantum spin Hall effect and topological phase transition in HgTe quantum wells" Science 314, 1757
- König, M. et al. (2007) "Quantum spin Hall insulator state in HgTe quantum wells" Science 318, 766
- Fu, L., Kane, C. L. (2007) "Topological insulators with inversion symmetry" Phys. Rev. B 76, 045302
- Hsieh, D. et al. (2008) "A topological Dirac insulator in a quantum spin Hall phase" Nature 452, 970
- Moore, G., Read, N. (1991) "Nonabelions in the fractional quantum Hall effect" Nucl. Phys. B 360, 362
- Wan, X. et al. (2011) "Topological semimetal and Fermi-arc surface states in pyrochlore iridates" PRB 83, 205101
