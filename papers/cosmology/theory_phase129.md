# Phase 129: Dark Matter + 構造形成 + S_8 tension + K_DM 仮説

> **Tier 1 #19 Cosmology — Phase 3/8 (Block A paper 3/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 129 の目的

Phase 128 で inflation を扱い、CMB anisotropy を inflaton K-state の量子揺らぎとして解釈した。Phase 129 では **暗黒物質 (DM)** と **構造形成** を扱う。

確立する内容:

1. **DM 観測的証拠**: 銀河回転曲線、重力レンズ、CMB peaks
2. **DM 候補**: WIMP, axion, primordial BH (Phase 125), 修正重力
3. **構造形成**: matter power spectrum P(k), σ_8
4. **S_8 / σ_8 tension**: CMB vs weak lensing (KiDS, DES, HSC)
5. **MOND vs ΛCDM**: SPARC galactic rotation
6. **ITU 視点**: K_DM = ITU の暗黒 K-state hypothesis

中心テーゼ:

> **Dark Matter = ITU 公理の "見えない" K_DM が予言する密度寄与**。
> 観測的に Ω_DM = 0.265 (Planck 2018) で 5σ 確定。
> σ_8 tension は **K_DM の構造形成 dynamics** が ΛCDM から逸脱する兆候。
> ITU は WIMP / axion / PBH すべてを K_DM の異なる **physical realization** として包含。

---

## 1. Dark Matter 観測的証拠

### 1.1 銀河回転曲線 (Rubin-Ford 1970)

```
v_rot(r) ≈ const  (大半径)
```

可視物質のみなら v ∝ 1/√r 減少するはず → **halo of DM** 必要。

例: 銀河系
- 太陽位置 (8 kpc): v = 220 km/s
- 50 kpc: v ≈ 200 km/s (まだ平坦)
- 必要 DM 質量: ~ 10¹² M_⊙ (visible の ~10倍)

### 1.2 銀河団 重力 (Zwicky 1933)

Coma cluster 銀河の virial mass vs luminous mass:
- M_virial / M_lum ≈ **400×** 過剰

### 1.3 弾丸銀河団 (Bullet Cluster, Clowe 2006)

- X-ray (visible gas) と weak lensing (mass map) が **分離**
- → 暗黒物質は **collisionless** (or weakly interacting)
- MOND 単独では説明不可能 → DM が必須

### 1.4 CMB 第 3 peak

第 2 peak / 第 3 peak 比 ∝ Ω_b / Ω_DM。
Planck 2018: **Ω_DM/Ω_b ≈ 5.4** = DM は baryon の 5 倍。

---

## 2. Dark Matter 候補

### 2.1 候補の整理 (mass range)

| 候補 | 質量 | 状況 |
|---|---|---|
| **WIMP** | 10 GeV - 10 TeV | LUX-ZEPLIN, XENONnT 探索中 |
| **Axion** | 10⁻⁶ - 10⁻³ eV | ADMX, MADMAX 探索中 |
| **Sterile neutrino** | keV | X-ray line search |
| **Primordial BH** | 10¹⁷-10²² g | LISA microlensing (Phase 125) |
| **Self-interacting DM (SIDM)** | varies | dwarf galaxy 衝突断面積 |
| **Fuzzy DM (FDM)** | 10⁻²² eV | small-scale 構造 |

### 2.2 WIMP 仮説の現状

- **Direct detection** (LUX-ZEPLIN 2024): σ < 10⁻⁴⁷ cm² @ 30 GeV (no signal)
- **Indirect detection** (Fermi-LAT, IceCube): 上限のみ
- **Collider** (LHC): missing transverse momentum 探索、no excess

⇒ **WIMP は依然候補だがパラメータ空間縮小** (post-WIMP era?)。

### 2.3 Axion の現状

- ADMX (cavity haloscope): 1-10 μeV 帯探索
- IAXO (helioscope, 計画): 太陽 axion
- 検出されれば **QCD strong CP problem + DM** を同時解決

### 2.4 ITU 視点での候補統合

```
K_DM = generic "dark" K-state
     {
       K_WIMP    (heavy thermal relic),
       K_axion   (light pseudo-scalar),
       K_PBH     (primordial BH, Phase 125),
       K_SIDM    (self-interacting),
       ...
     }
```

ITU は **形而上的に neutral**: K_DM の **physical realization** を 観測が決定。

---

## 3. 構造形成 と Matter Power Spectrum

### 3.1 線形理論 (Jeans 1902, Lifshitz 1946)

```
δ(x,t) = ρ(x,t) - ρ̄(t)) / ρ̄(t)
```

線形成長:
```
δ̈ + 2 H δ̇ - 4π G ρ̄ δ = 0
```

matter-dominated:
```
δ(t) ∝ a(t)  (Einstein-de Sitter)
δ(t) ∝ a(t) × g(z)  (ΛCDM, g(0) ≈ 0.78)
```

### 3.2 Power Spectrum P(k)

```
P(k) = ⟨|δ_k|²⟩
```

Inflation 予言: P(k) ∝ k^{n_s-1} ≈ k^{-0.035} (近 scale-invariant)。

各 scale で:
- 大 scale (k → 0): P ∝ k (linear regime)
- BAO scale (k ~ 0.1 h/Mpc): acoustic peak
- 小 scale (k > 1 h/Mpc): non-linear

### 3.3 σ_8 (normalisation)

```
σ_8² = (1/2π²) ∫ k² P(k) W²(k R_8) dk
R_8 = 8 h⁻¹ Mpc
```

Planck 2018: **σ_8 = 0.811 ± 0.006** (CMB から ΛCDM model 経由)。

---

## 4. S_8 Tension (Weak Lensing vs CMB)

### 4.1 観測値

| Survey | S_8 = σ_8 √(Ω_m / 0.3) |
|---|---|
| **Planck 2018 (CMB)** | 0.834 ± 0.016 |
| KiDS-1000 (2021) | 0.766 ± 0.020 |
| DES Y3 (2022) | 0.776 ± 0.017 |
| HSC Y3 (2023) | 0.776 ± 0.024 |

### 4.2 Tension

```
ΔS_8 = 0.834 - 0.770 = 0.064
σ_combined ≈ 0.025
S_8 tension ≈ 2.5-3σ
```

Hubble tension (5σ) ほど深刻ではないが、**ΛCDM の限界**を示唆。

### 4.3 解決候補

- **Decaying DM**: DM の一部が崩壊 → σ_8 抑制
- **Self-interacting DM**: small-scale 構造を抑える
- **Early dark energy** (Phase 130 で詳述)
- **修正重力 f(R) etc.**

### 4.4 ITU 視点

```
S_8 deficit ∝ K_DM の dynamical correction
```

→ ITU は **K_DM が ΛCDM standard DM から逸脱**する余地を持つ。
Pass-2 (Phase 222) で ITU-specific DM dynamics を提案予定。

---

## 5. MOND vs ΛCDM

### 5.1 MOND (Milgrom 1983)

「Modified Newtonian Dynamics」: 重力法則を低加速度で修正:

```
a → a_M = √(a × a_0)  for a ≪ a_0
a_0 = 1.2 × 10⁻¹⁰ m/s²
```

DM なしで銀河回転曲線を説明。

### 5.2 SPARC データ (Lelli et al. 2016)

- 175 銀河の回転曲線解析
- MOND は **個別銀河を非常によく fit**
- 銀河団 scale では失敗 → ΛCDM が必要

### 5.3 ITU 視点

両者は **K-flow の異なる scale 領域**:

- 銀河 scale: K_DM が局所的に MOND-like 振る舞い
- 銀河団 scale: K_DM が collisionless DM (Bullet cluster)

⇒ ITU は両者を矛盾なく統合。

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **銀河回転曲線**: visible only vs +DM halo
2. **DM 候補質量範囲**: WIMP, axion, PBH, FDM
3. **Matter power spectrum P(k)** ΛCDM model
4. **S_8 tension の数値** (Planck vs KiDS/DES/HSC)
5. **σ_8 の linear growth** vs scale factor

---

## 7. Phase 129 主結論

1. **DM 証拠**: 銀河回転曲線、Coma virial, Bullet cluster, CMB
2. **Ω_DM = 0.265** (Planck 2018, 5σ 確定)
3. **候補**: WIMP, axion, PBH, sterile neutrino, SIDM, fuzzy DM
4. **S_8 tension**: 2.5-3σ (CMB vs weak lensing)
5. **MOND**: 個別銀河 OK、銀河団 NG
6. **ITU K_DM**: 全候補を包含、観測で確定
7. **次の Phase 130** で **Dark Energy + cosmic acceleration**

---

## 8. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Dark matter | K_DM (generic dark K-state) |
| WIMP / axion / PBH | K_DM の physical realization 候補 |
| Power spectrum P(k) | K_DM linear growth |
| σ_8 / S_8 | K_DM の 8 Mpc/h スケール amplitude |
| S_8 tension | K_DM dynamical 逸脱の signature |
| MOND | K_DM の銀河スケール effective theory |

---

## 引用

```
Terada, M. (2026). Phase 129: Dark matter, structure formation, S_8
tension, and K_DM hypothesis in ITU (Tier 1 #19 phase 3/8). Zenodo.
DOI: [to be assigned].
```

主要参考文献:
- Rubin, V. C., Ford, W. K. (1970) "Rotation of the Andromeda Nebula from a Spectroscopic Survey of Emission Regions" ApJ 159, 379
- Zwicky, F. (1933) "Die Rotverschiebung von extragalaktischen Nebeln" Helv. Phys. Acta 6, 110
- Clowe, D. et al. (2006) "A Direct Empirical Proof of the Existence of Dark Matter" ApJL 648, L109
- Milgrom, M. (1983) "A modification of the Newtonian dynamics" ApJ 270, 365
- Lelli, F., McGaugh, S. S., Schombert, J. M. (2016) "SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves" AJ 152, 157
- LUX-ZEPLIN Collaboration (2024) "First Dark Matter Search Results from the LUX-ZEPLIN (LZ) Experiment" PRL 131, 041002
- ADMX Collaboration (2020) "A Search for Invisible Axion Dark Matter with the ADMX Experiment" PRL 124, 101303
- KiDS Collaboration (2021) "KiDS-1000 Cosmology: Multi-probe weak gravitational lensing and spectroscopic galaxy clustering constraints" A&A 646, A140
- DES Collaboration (2022) "Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing" PRD 105, 023520
- HSC Collaboration (2023) "Hyper Suprime-Cam Year 3 results: Cosmology from cosmic shear two-point correlation functions" PRD 108, 123517
