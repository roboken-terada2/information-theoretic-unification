# Phase 130: Dark Energy + 宇宙加速膨張 + Λ 問題 + DESI 2024

> **Tier 1 #19 Cosmology — Phase 4/8 (Block A paper 3/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 130 の目的

Phase 129 で Dark Matter を扱った。Phase 130 では **Dark Energy (DE)** と **宇宙加速膨張**を扱う。

確立する内容:

1. **加速膨張発見 (Riess 1998, Perlmutter 1999)** = Nobel 2011
2. **Type Ia 超新星 = standard candle**: 30 Mpc-10 Gpc 距離測定
3. **宇宙定数 Λ**: Einstein 1917, Friedmann eq に再導入
4. **Λ 問題**: 観測 vs 理論で **120 桁の差**
5. **状態方程式 w = -1**: vs evolving w (quintessence)
6. **DESI 2024**: 進化する DE の暗示?
7. **ITU 視点**: K_Λ = 真空の K-flow stationary value

中心テーゼ:

> **Dark Energy = ITU 公理 δS = δ⟨K_Λ⟩ の宇宙真空 K-flow**。
> Λ-problem (10¹²⁰ 桁の差) は **ITU の最大の挑戦** であると同時に **最大の検証窓**。
> DESI 2024 が w(z) ≠ -1 を示唆 → ITU **K_Λ の時間発展**で説明可能性。

---

## 1. 加速膨張の発見 (1998)

### 1.1 観測

Type Ia supernova を **standard candle** として使用:

```
m - M = 5 log_10(d_L / 10 pc) + K
```

- m: apparent magnitude
- M: absolute magnitude (Type Ia で標準化, M = -19.3)
- d_L: luminosity distance
- K: K-correction

### 1.2 結果

z = 0.3-1.0 の SNe Ia が **想定より暗い**:

→ 宇宙が **加速膨張** している証拠。

```
ä > 0  ⇒  ρ + 3p/c² < 0  ⇒  p < -ρc²/3
```

### 1.3 Nobel 賞

- **2011 Nobel 物理学賞**:
  - Saul Perlmutter (LBL, SCP)
  - Brian P. Schmidt (ANU, HZT)
  - Adam G. Riess (JHU, HZT)

---

## 2. Type Ia Supernova の物理

### 2.1 起源

白色矮星 (M ≈ 1.4 M_⊙ = Chandrasekhar limit) の thermonuclear runaway:

- single degenerate: WD + main-sequence/red-giant companion
- double degenerate: WD + WD merger

### 2.2 光度曲線の標準化

- Phillips relation (1993): peak luminosity ∝ rise time
- MLCS, SALT2 method で M を 0.1 mag 精度に
- ⇒ d_L 精度 ~5%

### 2.3 現代の SN Ia samples

- **SDSS-II / SNLS** (~500 SNe)
- **Pantheon+ (2021)**: 1701 SNe (z = 0.001-2.3)
- **DES-SN (2024)**: ~2000 SNe high-z
- **LSST / Rubin Observatory** (2025-): ~10⁶ SNe 期待

---

## 3. 宇宙定数 Λ

### 3.1 Einstein 1917 ← 「最大の間違い」

Einstein は静的宇宙のため Λ を導入:

```
G_μν + Λ g_μν = 8π G T_μν / c⁴
```

Hubble 膨張発見後撤回。1998 加速膨張発見で **復活**。

### 3.2 Λ の物理的意味

```
ρ_Λ = Λ c² / (8π G) = const
p_Λ = -ρ_Λ c²
```

w_Λ = -1 (状態方程式)。

### 3.3 観測値

```
Λ ≈ 1.1 × 10⁻⁵² m⁻²
ρ_Λ ≈ 6.0 × 10⁻¹⁰ J/m³ ≈ 5.4 GeV/m³ (proton mass density)
Ω_Λ = 0.685  (Planck 2018)
```

---

## 4. Λ 問題 ★ 最大のミステリー

### 4.1 量子場理論の予言

zero-point energy:

```
ρ_vac (theoretical) = ∫ d³k (2π)⁻³ × (ℏω/2)
```

UV cutoff Λ_QFT に依存:

| Cutoff Λ_QFT | ρ_vac (J/m³) | 観測との差 |
|---|---|---|
| **Planck (E_P)** | **10¹¹³** | **10¹²² 倍** |
| GUT (10¹⁶ GeV) | 10¹⁰⁰ | 10¹¹⁰ 倍 |
| EW (TeV) | 10⁴³ | 10⁵³ 倍 |
| QCD (GeV) | 10³⁷ | 10⁴⁷ 倍 |

⇒ **120 orders of magnitude の不整合** (Weinberg 1989 review)。

### 4.2 解決候補

- **Anthropic principle**: 観測者が存在する宇宙では Λ が小さい (Weinberg 1987)
- **String landscape**: 10⁵⁰⁰ vacua の中で Λ ~ 0 を選択
- **Sequestering** (Kaloper-Padilla 2014): geometric average で Λ cancel
- **修正重力** (f(R), DGP, etc.)
- **Dynamical relaxation** (Λ が時間発展)

### 4.3 ITU 視点

```
K_Λ = vacuum modular Hamiltonian
ρ_Λ = δ⟨K_Λ⟩ / δV  (vacuum K-state energy density)
```

**問題の本質**: K_Λ の boundary condition が現在の宇宙 horizon scale で **何故 small** か。

ITU は holographic principle 経由で:

```
ρ_Λ ~ S_horizon / (A_horizon × c²) ~ (4 G ℏ) / (A_horizon c²)
```

これは **観測値とオーダー一致** (Cohen-Kaplan-Nelson 1999 holographic bound)。

⇒ **Λ 問題は ITU で半解決** (Pass-2 で詳述予定)。

---

## 5. 状態方程式 w(z)

### 5.1 w = -1 (Λ): ΛCDM

```
ρ_Λ(z) = const
```

### 5.2 w ≠ -1: Quintessence

Slowly rolling scalar field φ_DE:

```
ρ_φ = (1/2) φ̇² + V(φ)
p_φ = (1/2) φ̇² - V(φ)
w = (φ̇² - 2V) / (φ̇² + 2V)
```

slow-roll で w → -1+δ。

### 5.3 CPL parameterization (Chevallier-Polarski-Linder)

```
w(z) = w_0 + w_a × z / (1+z)
```

- ΛCDM: w_0 = -1, w_a = 0
- 観測で w_0 + 0.5 w_a を制約

---

## 6. DESI 2024 衝撃結果 ★

### 6.1 観測

**DESI Year 1** (Dark Energy Spectroscopic Instrument, 2024 April):

- BAO measurements 100,000+ luminous red galaxies
- combined with CMB + SNe Ia

### 6.2 結果

```
w_0 = -0.95 ± 0.09
w_a = -0.39 ± 0.34
```

**ΛCDM (w_0=-1, w_a=0) からの逸脱**: 2-4σ レベル (combination 依存)。

w(z=0.5) = w_0 + 0.5 w_a / 1.5 ≈ -1.08 (w(z) が time-evolving)。

### 6.3 解釈

- **証拠が確定的ではない** (2-4σ)
- DESI Year 2-3 (2025-26) で 5σ レベル期待
- 確認されれば **ΛCDM は破綻**、ITU 拡張への扉開く

### 6.4 ITU 視点

DESI 2024 が示唆する evolving DE:

```
K_Λ(t) ≠ const
dK_Λ/dt = (vacuum K-flow drift)
```

ITU は **vacuum K-state の時間発展**を自然に許容 (Pass-2 priority)。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Type Ia SN Hubble diagram** (m - M vs z)
2. **Λ 問題の 120 桁差** 数値比較
3. **w(z) plot** (ΛCDM vs DESI 2024 + quintessence)
4. **w_0-w_a 制約平面**
5. **加速膨張 ä(t) > 0** 確認

---

## 8. Phase 130 主結論

1. **加速膨張発見 (1998)**: Type Ia SNe → Nobel 2011
2. **Λ ≈ 1.1×10⁻⁵² m⁻²**: 観測 Ω_Λ = 0.685
3. **Λ 問題**: 理論 ρ_vac (Planck) は観測の **10¹²² 倍**
4. **DESI 2024**: w_0 = -0.95, w_a = -0.39 (2-4σ ΛCDM 逸脱)
5. **ITU K_Λ**: vacuum K-state, holographic で半解決
6. **Pass-2 priority**: evolving K_Λ(t) hypothesis
7. **次の Phase 131** で **Hubble tension + early DE + 解決候補**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Dark Energy | K_Λ vacuum modular Hamiltonian |
| Λ = 1.1e-52 m^-2 | K_Λ 観測値 |
| Λ 問題 (120 桁) | K_Λ boundary condition の謎 |
| Holographic bound | ITU の半解決 |
| w(z) evolving | K_Λ(t) drift |
| DESI 2024 | evolving K_Λ の暗示 |

---

## 引用

```
Terada, M. (2026). Phase 130: Dark energy, cosmic acceleration, Λ
problem, and DESI 2024 in ITU (Tier 1 #19 phase 4/8). Zenodo. DOI:
[to be assigned].
```

主要参考文献:
- Riess, A. G. et al. (1998) "Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant" AJ 116, 1009
- Perlmutter, S. et al. (1999) "Measurements of Ω and Λ from 42 High-Redshift Supernovae" ApJ 517, 565
- Einstein, A. (1917) "Kosmologische Betrachtungen zur allgemeinen Relativitätstheorie" Sitz. Preuß. Akad. Wiss.
- Weinberg, S. (1989) "The cosmological constant problem" Rev. Mod. Phys. 61, 1
- Weinberg, S. (1987) "Anthropic bound on the cosmological constant" PRL 59, 2607
- Chevallier, M., Polarski, D. (2001) "Accelerating universes with scaling dark matter" Int. J. Mod. Phys. D 10, 213
- Linder, E. V. (2003) "Exploring the expansion history of the universe" PRL 90, 091301
- Cohen, A. G., Kaplan, D. B., Nelson, A. E. (1999) "Effective Field Theory, Black Holes, and the Cosmological Constant" PRL 82, 4971
- DESI Collaboration (2024) "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations" arXiv:2404.03002
- Pantheon+ Collaboration (2022) "The Pantheon+ Analysis: Cosmological Constraints" ApJ 938, 110
