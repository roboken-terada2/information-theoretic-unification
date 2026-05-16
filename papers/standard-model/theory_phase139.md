# Phase 139: 電弱統一 + Weinberg angle + 精密電弱 + g-2 + LHC + ITU K_EW

> **Tier 1 #20 Standard Model — Phase 5/8 (Block A paper 4/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 139 の目的

Phase 135-138 で SM の各構成要素を扱った。Phase 139 では **電弱統一の精密検証** に焦点を当てる:

1. **Glashow-Weinberg-Salam (GWS) 統一** (Nobel 1979)
2. **Weinberg angle**: sin²θ_W ≈ 0.2312 の精密測定
3. **ρ parameter**: M_W²/(M_Z² cos²θ_W) ≈ 1.00
4. **LEP precision tests** (Z pole observables)
5. **W boson mass anomaly**: CDF 2022 (80.434 GeV) vs ATLAS 2024 (80.367 GeV)
6. **Muon g-2 anomaly**: Fermilab 2023 - 4.2σ deviation
7. **ITU 視点**: K_EW = electroweak unified K-state

中心テーゼ:

> **GWS 電弱統一 = ITU K_EW (K_weak + K_em → K_EW unified)**。
> Weinberg angle = K_EW の **mixing parameter**。
> ρ parameter ≈ 1 = **custodial symmetry** (ITU の K-state symmetry constraint)。
> W mass anomaly (CDF 2022) と muon g-2 (Fermilab 2023, 4.2σ) は **ITU BSM の暗示**。

---

## 1. Glashow-Weinberg-Salam (GWS) 統一

### 1.1 主張 (1961-1968, Nobel 1979)

弱い相互作用 (W^±) + 電磁気力 (γ) = **電弱統一 SU(2)_L × U(1)_Y**:

```
SU(2)_L × U(1)_Y --(EWSB Higgs)--> U(1)_EM
```

### 1.2 4 つの gauge boson

```
W^1, W^2, W^3 (SU(2)_L), B (U(1)_Y)
```

EWSB 後:

```
W^± = (W^1 ∓ i W^2) / √2  (charged, massive)
Z   = cos θ_W × W^3 - sin θ_W × B  (neutral, massive)
γ   = sin θ_W × W^3 + cos θ_W × B  (neutral, massless)
```

### 1.3 Weinberg Angle θ_W

```
tan θ_W = g' / g
sin²θ_W = g'² / (g² + g'²)
```

PDG 2024: **sin²θ_W = 0.23121 ± 0.00004** (on-shell scheme, Z pole)。

---

## 2. ρ Parameter

### 2.1 定義

```
ρ ≡ M_W² / (M_Z² cos²θ_W)
```

### 2.2 SM 予言 (Tree level)

```
ρ_tree = 1  (custodial SU(2) symmetry)
```

### 2.3 1 ループ補正

```
ρ = 1 + Δρ
Δρ ≈ (3 G_F m_t² / 8√2 π²) ≈ 0.009  (top quark dominant)
```

### 2.4 観測値

```
ρ_obs = 1.00038 ± 0.00020  (PDG 2024)
```

完全一致 → **custodial SU(2)** がほぼ完全に保護。

### 2.5 ITU 視点

```
ρ = 1 ⇒ K_EW の global SU(2) custodial symmetry
δρ ≈ 0.009 ⇒ K_top fermion による補正
```

= **K_EW の保存則**。

---

## 3. LEP Precision Electroweak Tests

### 3.1 Z Pole Observables (LEP 1989-2000)

LEP の高精度測定:

| 観測量 | 値 |
|---|---|
| **M_Z** | 91.1876 ± 0.0021 GeV |
| **Γ_Z (全幅)** | 2.4955 ± 0.0023 GeV |
| Γ(Z→e⁺e⁻) | 83.984 ± 0.086 MeV |
| Γ(Z→hadrons) | 1.7449 ± 0.0033 GeV |
| **N_ν (light neutrino flavors)** | **2.9963 ± 0.0074** (= 3) |
| sin²θ_W^eff | 0.23149 ± 0.00013 |
| A_FB^b (forward-backward asym) | 0.0996 ± 0.0016 |

### 3.2 W Mass: M_W

| Experiment | M_W (GeV) |
|---|---|
| LEP/Tevatron 2017 avg | 80.385 ± 0.015 |
| **CDF 2022** ★ | **80.4335 ± 0.0094** (anomaly!) |
| ATLAS 2024 | 80.3665 ± 0.016 |
| World avg (PDG 2024) | 80.3692 ± 0.0133 |

⇒ **CDF 2022 が SM 予言 (80.354 ± 0.007) より 7σ 高い** ← 異常。
他実験 (ATLAS 2024) は SM 一致 → CDF 系統誤差の可能性。

---

## 4. CDF 2022 W Mass Anomaly ★

### 4.1 観測 (Science 2022)

```
M_W^CDF = 80.4335 ± 0.0094 GeV
```

vs SM 予言 (electroweak fit) 80.354 ± 0.007 GeV → **7σ tension**!

### 4.2 解釈候補

- **CDF 系統誤差**: 後続 ATLAS 2024 が SM 一致 (80.367 GeV) → CDF が outlier 可能性
- **BSM physics**:
  - Two-Higgs-doublet model (2HDM)
  - Inert doublet model
  - Extra SU(2) gauge boson (W')
  - Stop, slepton, neutralino in SUSY

### 4.3 ITU 視点

CDF anomaly が確認されれば:
```
K_EW(beyond SM) = K_EW^SM + δK_BSM
δK ↔ extra Higgs / extra gauge / SUSY contribution
```

Pass-2 (Phase 224) で ITU-specific BSM scenarios を提案予定。

---

## 5. Muon g-2 Anomaly ★

### 5.1 物理

電子・muon の **異常磁気モーメント** (Schwinger 1948):

```
a_ℓ = (g_ℓ - 2) / 2
```

g = 2 (Dirac point), a > 0 = ループ補正。

### 5.2 SM 予言

```
a_μ^SM = 116591810(43) × 10⁻¹¹  (Hadronic Vacuum Polarization Initiative 2020)
```

主寄与:
- QED: 116584719 × 10⁻¹¹ (5 loop, Aoyama-Hayakawa-Kinoshita-Nio 2012)
- Electroweak: 154 × 10⁻¹¹
- Hadronic VP: 6845 × 10⁻¹¹ (data-driven) or 7090 × 10⁻¹¹ (lattice BMW 2020)
- Hadronic LbL: 92 × 10⁻¹¹

### 5.3 観測 (Fermilab 2023)

```
a_μ^exp = 116592061(41) × 10⁻¹¹  (Run 1 + Run 2/3 combined)
```

### 5.4 偏差

```
Δa_μ = a_μ^exp - a_μ^SM = 251 (59) × 10⁻¹¹  → 4.2σ ★
```

(BMW lattice 採用なら ~1σ に縮小、まだ議論中)。

### 5.5 BSM 解釈

```
Δa_μ ∝ (m_μ / Λ_BSM)² × C
```

Λ_BSM ~ 1-10 TeV で C ~ O(1)。SUSY, leptoquarks, Z', dark photon, etc.

### 5.6 ITU 視点

Muon g-2 anomaly = K_muon の **量子補正に未知 K-state 寄与**:

```
δK_μ^anomaly ↔ δa_μ = 251 × 10⁻¹¹
```

Pass-2 (Phase 224) で ITU 候補 K-state を 4.2σ 偏差から absorb 提案。

---

## 6. CKM Unitarity Tests

### 6.1 First Row Unitarity

```
|V_ud|² + |V_us|² + |V_ub|² = 1  (SM)
```

PDG 2024:
```
|V_ud|² + |V_us|² + |V_ub|² = 0.9989 ± 0.0007
```

→ **約 3σ deficit** = "Cabibbo angle anomaly" (CAA)。

### 6.2 解釈

- nuclear-physics 系統誤差?
- BSM (right-handed currents)?
- 同様 ITU 視点で K_quark の修正可能性。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Weinberg angle**: sin²θ_W = 0.2312, M_W = M_Z cos θ_W
2. **ρ parameter** ≈ 1.00038
3. **W mass: CDF 2022 vs ATLAS 2024 vs SM**
4. **Muon g-2 偏差**: 251 ± 59 × 10⁻¹¹ ≈ 4.2σ
5. **N_ν = 3** (LEP)
6. **CKM first row unitarity**: 3σ deficit

---

## 8. Phase 139 主結論

1. **GWS 電弱統一 (1961-1968, Nobel 1979)**: SU(2)_L × U(1)_Y → U(1)_EM
2. **Weinberg angle sin²θ_W = 0.23121** (PDG 2024)
3. **ρ parameter = 1.00038**: custodial SU(2) protected
4. **LEP**: M_Z, Γ_Z, N_ν = 3 sub-‰ precision
5. **CDF 2022 W anomaly**: 80.4335 GeV (7σ above SM) → ATLAS 2024 解消?
6. **Muon g-2 (Fermilab 2023)**: 4.2σ tension ★ BSM 暗示
7. **CKM first row**: 3σ deficit (Cabibbo angle anomaly)
8. **ITU**: K_EW = electroweak unified K-state with custodial symmetry
9. **次の Phase 140** で **BSM (SUSY, GUT, neutrino mass) + 階層問題**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| GWS 統一 | K_weak + K_em → K_EW |
| Weinberg angle | K_EW mixing parameter |
| ρ ≈ 1 | K_EW custodial symmetry |
| LEP Z pole | K_EW precision K-flow |
| CDF W anomaly | δK_EW BSM correction (還元中) |
| Muon g-2 4.2σ | K_μ BSM contribution (4.2σ) |
| CKM CAA | K_quark BSM modification |

---

## 引用

```
Terada, M. (2026). Phase 139: Electroweak unification, precision tests,
g-2 and W-mass anomalies in ITU (Tier 1 #20 phase 5/8). Zenodo. DOI:
[to be assigned].
```

主要参考文献:
- Glashow, S. L. (1961) Nucl. Phys. 22, 579
- Weinberg, S. (1967) PRL 19, 1264
- Salam, A. (1968) "Elementary particle theory", ed. Svartholm
- Schwinger, J. (1948) PR 73, 416
- ALEPH-DELPHI-L3-OPAL-SLD (2006) Phys. Rept. 427, 257  (Z pole precision)
- CDF Collaboration (2022) "High-precision measurement of the W boson mass with the CDF II detector" Science 376, 170
- ATLAS Collaboration (2024) "Measurement of the W boson mass and width with the ATLAS detector at √s = 7 TeV" (CDS preliminary)
- Muon g-2 Collaboration (2023) "Measurement of the Positive Muon Anomalous Magnetic Moment to 0.20 ppm" PRL 131, 161802
- BMW Collaboration (2020) "Leading hadronic contribution to the muon magnetic moment from lattice QCD" Nature 593, 51
- Cirigliano, V. et al. (2022) "Quark-lepton unification, anomalies in V_us extractions" Annu. Rev. Nucl. Part. Sci. 72, 69
- Particle Data Group (2024) "Review of Particle Physics" PRD 110, 030001
