# Phase 141: LHC + 将来 Collider + Particle Cosmology + ITU 検証 Platform

> **Tier 1 #20 Standard Model — Phase 7/8 (Block A paper 4/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 141 の目的

Phase 135-140 で SM + BSM の理論を扱った。Phase 141 では **実験的検証 platform** を整理する:

1. **LHC** (CERN): Run 1-3 と HL-LHC
2. **将来 collider**: FCC, CEPC, ILC, Muon Collider
3. **Particle Cosmology**: Tier 1 #19 Cosmology との連携
4. **Cosmic ray + Neutrino astronomy**: IceCube, Pierre Auger
5. **ITU 検証 priority**: 量子重力 (#17) + BH (#18) + Cosmology (#19) + SM (#20)

中心テーゼ:

> **LHC + 将来 collider = ITU の K_field 実験検証 platform**。
> HL-LHC (2030+) で Higgs self-coupling λ_3 直接測定 → K_Higgs 構造確認。
> FCC-hh 100 TeV → 10⁴ Higgs / Z'/leptoquark 探索 = K_BSM 範囲確定。
> IceCube + Pierre Auger = K_cosmic + K_field 高エネルギー検証。

---

## 1. LHC History

### 1.1 Runs

| Run | 期間 | √s (TeV) | 統合 luminosity |
|---|---|---|---|
| Run 1 | 2010-2013 | 7-8 | 30 fb⁻¹ |
| Run 2 | 2015-2018 | 13 | 140 fb⁻¹ |
| Run 3 | 2022-2025 (進行中) | 13.6 | 300 fb⁻¹ (目標) |
| **HL-LHC** | **2030-2041** | **14** | **3000 fb⁻¹** (目標) |

### 1.2 Run 1-2 主要成果

- **Higgs boson 発見** (2012, Nobel 2013) — Phase 137
- W mass 精密測定 — Phase 139
- top quark 精密測定
- BSM 探索: SUSY, Z', WIMP DM
- B physics: LHCb で flavor violations

### 1.3 Run 3 (2024 中現状)

- ATLAS + CMS: 140 fb⁻¹ + 100 fb⁻¹ accumulated
- 統合解析中、新物理 hint 暗示 (W mass, g-2 と整合する候補)
- 2025 終了予定 → HL-LHC 工事 (2026-2029)

### 1.4 HL-LHC (High-Luminosity LHC)

- 2030 から稼働
- 統合 luminosity 3000 fb⁻¹ (Run 2 の **20 倍**)
- Higgs precision (κ → < 5% measure)
- Higgs self-coupling λ_3 (di-Higgs production) **初測定**
- BSM 探索範囲拡大

---

## 2. Higgs Self-coupling λ_3

### 2.1 物理的重要性

Higgs potential 形状:

```
V(H) = -μ²|H|² + λ|H|⁴
     = (1/2) m_H² h² + λ_3 v h³ + (1/4) λ_4 h⁴
```

- SM: **λ_3^SM = m_H² / (2 v) ≈ 32 GeV** (or κ_λ = 1 in dimensionless)
- λ_3 = 0: Mexican hat 平坦 (異常)
- λ_3 ≠ λ_3^SM: BSM Higgs sector

### 2.2 di-Higgs Production

```
g g → H H (via top loop)
σ(HH) ≈ 31 fb at 14 TeV
```

decay: HH → bb̄γγ, bb̄ττ, bb̄WW

### 2.3 観測

- Current (Run 2): **κ_λ ∈ [-0.4, 6.3]** (95% CL, ATLAS+CMS combined)
- HL-LHC target: **κ_λ = 1 ± 0.5** (50%)
- FCC-hh target: **κ_λ = 1 ± 0.05** (5%)

⇒ **Higgs potential 形状を直接観測**できる。

---

## 3. 将来 Collider

### 3.1 候補 (2025 現在 R&D 中)

| Collider | 場所 | エネルギー | 期間 | 目的 |
|---|---|---|---|---|
| **FCC-ee** | CERN | 90-365 GeV (e⁺e⁻) | 2045-2065 | Higgs + Z + top precision |
| **FCC-hh** | CERN | 100 TeV (pp) | 2070-2100 | 直接 BSM 探索 |
| **CEPC + SppC** | China | 240 GeV / 100 TeV | 2030s+ | Higgs factory + pp |
| **ILC** | Japan (planned) | 250-500 GeV (e⁺e⁻) | TBD | Higgs precision |
| **Muon Collider** | TBD | 3-10 TeV (μ⁺μ⁻) | 2040+ | Higgs + BSM |

### 3.2 FCC-hh (Future Circular Collider, hadron mode)

- CERN 計画 (2070s+)
- 100 km circumference, 100 TeV pp
- 直接 BSM: 50-100 TeV gluino/squark, **5 TeV 範囲 leptoquark**
- Higgs self-coupling λ_3 to 5%
- Higgs total cross section 1% accuracy

### 3.3 Muon Collider (新提案)

- μ⁺μ⁻ collisions: low synchrotron radiation (small ring)
- 3-10 TeV center-of-mass at 10 km ring
- **Higgs precision** + BSM搜索同時
- Technical challenges: muon cooling, neutrino radiation

---

## 4. Particle Cosmology Connection

### 4.1 Tier 1 #19 ↔ #20 Bridge

| 観点 | #19 Cosmology | #20 Standard Model |
|---|---|---|
| Inflation | K_inflaton scalar | K_Higgs-like? |
| Dark matter | K_DM Ω_DM = 0.265 | Neutralino candidate? |
| Baryon asymmetry | η_B = 6×10⁻¹⁰ | Leptogenesis (Phase 140) |
| Hubble tension | K_inflaton vs K_Λ | EW phase transition? |
| Neutrino mass | Σ m_ν < 0.12 eV | See-saw + Majorana (140) |

### 4.2 Particle-Cosmology 連携実験

| 実験 | 検証対象 |
|---|---|
| LHC (#20) | Higgs, SUSY, top |
| LiteBIRD (#19) | Inflation r ~ 10⁻³ (K_tensor) |
| DESI (#19) | DE w(z), structure |
| IceCube (#20) | Cosmic neutrinos, BSM |
| KATRIN (#20) | Neutrino mass direct |
| XENONnT, LZ (#20) | WIMP DM direct |
| Fermi-LAT (#20) | DM indirect (γ-ray) |
| CMS+ATLAS HL (#20) | BSM precision |

### 4.3 ITU 視点

SM + Cosmology = **K_field + K_cosmic の coupled K-flow**:

```
K_total = K_field (SM) + K_cosmic (universe) + K_BSM (extension)
```

ITU は両者の **共通 K-flow** を仮定。

---

## 5. Cosmic Ray + Neutrino Astronomy

### 5.1 Pierre Auger Observatory (Argentina)

- 3000 km² array
- 観測: UHE cosmic rays (E > 10¹⁸ eV)
- GZK cutoff (E > 5×10¹⁹ eV) 観測
- Source: 高エネルギー AGN, neutron stars

### 5.2 IceCube Neutrino Observatory (Antarctic)

- 1 km³ ice array
- 観測: PeV-EeV cosmic neutrinos
- 2013: 初の astrophysical ν 発見
- 2017: TXS 0506+056 blazar との同時観測 (multi-messenger)
- 2022: NGC 1068 (Seyfert 2) からの ν 観測

### 5.3 ITU 視点

```
K_neutrino_astro = high-energy K_neutrino reaching Earth
```

- 高エネルギー ν 源: AGN, Seyfert galaxies, GRBs
- DM annihilation 探索 (Sun center, galactic center)
- Lorentz invariance test (Phase 117)

---

## 6. ITU 実験検証 Priority Map

Block A (#17-#19) + #20 SM の検証 priority:

| 実験 | 検証対象 | 期限 | P |
|---|---|---|---|
| **BMV (Bose 2017)** | #17 K_geom (quantum gravity) | 2032 | 0.65 |
| **LiteBIRD r ~ 0.001** | #19 K_tensor inflation | 2034 | 0.85 |
| **EHT M87* 5 μas** | #18 K_horizon (BH) | 2030 | 0.90 |
| **DESI Y3 evolving DE** | #19 K_Λ(t) | 2027 | 0.75 |
| **HL-LHC Higgs λ_3** | #20 K_Higgs structure | 2035 | 0.85 |
| **FCC-hh** | #20 K_BSM (5 TeV) | 2070+ | 0.30 |
| **Muon g-2 Fermilab** | #20 K_μ BSM (4.2σ) | 進行中 | 0.55 |
| **KamLAND-Zen 0νββ** | #20 K_lepton Majorana | 2030 | 0.40 |
| **IceCube cosmic ν** | #20 K_neutrino_astro | 進行中 | 0.85 |

⇒ Block A 全体で **9 つの並行検証 platform** が稼働中。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **LHC integrated luminosity timeline**
2. **HL-LHC vs FCC-hh vs Muon Collider 比較**
3. **Higgs λ_3 precision evolution**
4. **将来 collider energy reach vs SUSY mass limits**
5. **ITU 検証 priority map (9 experiments)**

---

## 8. Phase 141 主結論

1. **LHC Run 3**: 13.6 TeV, 300 fb⁻¹ target by 2025
2. **HL-LHC (2030-2041)**: 3000 fb⁻¹, Higgs self-coupling **initial measurement** ★
3. **FCC-hh (2070+)**: 100 TeV pp, λ_3 to 5%, gluino to 50 TeV
4. **Muon Collider**: 3-10 TeV μ⁺μ⁻, 2040+ feasibility study
5. **Particle-Cosmology bridge**: SM ↔ Cosmology (#19 と #20)
6. **IceCube + Pierre Auger**: high-E ν / cosmic ray detection
7. **ITU 検証 priority**: 9 experiments across Block A (#17-#20)
8. **次の Phase 142** で **Tier 1 #20 統合 + 20-vertex polytope + 10 predictions**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| LHC Run 1-3 | K_field 中エネルギー検証 |
| HL-LHC | K_Higgs 自己結合 λ_3 |
| FCC-hh | K_BSM 100 TeV 探索 |
| Muon Collider | K_lepton 高 E precision |
| LiteBIRD | K_tensor inflation |
| IceCube | K_neutrino_astro |
| 9 検証 platforms | Block A K-state 多面検証 |

---

## 引用

```
Terada, M. (2026). Phase 141: LHC + future colliders + particle cosmology
in ITU (Tier 1 #20 phase 7/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- ATLAS Collaboration (2024) "ATLAS physics results database" CERN-EP-2024-XXX
- CMS Collaboration (2024) "CMS physics results database" CMS-PAS-XXX
- HL-LHC Project (2020) "High-Luminosity Large Hadron Collider — Technical Design Report" CERN Yellow Report 10/2020
- FCC Collaboration (2025) "FCC Conceptual Design Report — Future Circular Collider" Eur. Phys. J. C
- CEPC Steering Committee (2024) "CEPC Technical Design Report"
- ILC Collaboration (2013) "The International Linear Collider Technical Design Report"
- Muon Collider Collaboration (2022) "Muon Collider — A Path to Tomorrow's Discoveries" arXiv:2209.01318
- Pierre Auger Collaboration (2017) "Observation of a large-scale anisotropy in the arrival directions of cosmic rays above 8×10¹⁸ eV" Science 357, 1266
- IceCube Collaboration (2013) "Evidence for High-Energy Extraterrestrial Neutrinos at the IceCube Detector" Science 342, 1242856
- IceCube Collaboration (2022) "Evidence for neutrino emission from the nearby active galaxy NGC 1068" Science 378, 538
- Bose, S. et al. (2017) "Spin entanglement witness for quantum gravity" PRL 119, 240401
- LiteBIRD Collaboration (2023) "LiteBIRD" PTEP 2023, 042F01
