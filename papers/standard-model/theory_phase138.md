# Phase 138: QCD + Confinement + 量子色プラズマ + カイラル対称性破れ + Strong CP

> **Tier 1 #20 Standard Model — Phase 4/8 (Block A paper 4/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 138 の目的

Phase 135-137 で SM gauge 群 + fermion + Higgs を扱った。Phase 138 では **QCD の特殊性** に焦点を当てる:

1. **QCD Lagrangian** + asymptotic freedom 詳細
2. **Confinement**: quark/gluon は自由粒子として観測されない
3. **Quark-Gluon Plasma (QGP)**: 高温 deconfined phase
4. **Lattice QCD**: 非摂動的計算手法
5. **カイラル対称性破れ** (Chiral SSB): π, K のほぼ Goldstone
6. **ハドロン質量 spectrum**
7. **Strong CP problem** + axion
8. **ITU 視点**: K_QCD = strong K-flow

中心テーゼ:

> **QCD = ITU の K-flow non-perturbative regime の代表例**。
> Confinement = K_QCD の **IR strongly coupled phase**。
> Chiral SSB = K_QCD の自発的対称性破れ = ハドロン質量の主な起源。
> Strong CP problem (θ_QCD < 10⁻¹⁰) = ITU の **fine-tuning issue #2** (Higgs に次ぐ)。

---

## 1. QCD Lagrangian

```
L_QCD = -1/4 F^a_μν F^{aμν} + ψ̄_q (i γ^μ D_μ - m_q) ψ_q
```

- F^a_μν: SU(3) gauge field strength (a = 1, ..., 8)
- ψ_q: quark spinor (6 flavors)
- D_μ = ∂_μ - i g_s A^a_μ T^a (covariant derivative)
- m_q: bare quark mass

### 1.1 Gauge Self-Interaction

非可換 SU(3) → **gluon self-interaction**:

```
gluon-gluon-gluon vertex (3 gluon)
gluon-gluon-gluon-gluon vertex (4 gluon)
```

これが **QED と決定的に異なる** 特性 (photon は self-interact しない)。

---

## 2. Asymptotic Freedom 再訪

### 2.1 Beta 関数

```
β(α_s) = -α_s² / (2π) × (11 N_c/3 - 2 N_f/3)
```

N_c=3, N_f=6 で β < 0 → UV で α_s → 0。

### 2.2 Running

```
α_s(μ) = 4π / [b_0 × ln(μ²/Λ_QCD²)]
b_0 = (11 N_c - 2 N_f) / 3
```

Phase 135 で計算済み。Λ_QCD ≈ 200 MeV。

---

## 3. Confinement ★ 強相互作用の最大の謎の 1 つ

### 3.1 観測事実

- **Free quarks は観測されない**
- **Free gluons も観測されない**
- 全 hadron は **color-singlet** (color-neutral)

### 3.2 線形ポテンシャル

quark-quark 間 potential:

```
V(r) = -α_s × (4/3) / r + σ × r
```

- 短距離: クーロン-like (-1/r)
- 長距離: **線形上昇** (σ × r), σ ≈ 1 GeV/fm = string tension

### 3.3 String 描像

quark-antiquark 距離 r → flux tube (color string) が r に比例して伸びる:

```
E_string(r) = σ × r ≈ 1 GeV/fm × r
```

r が十分大きいと、**string が破断** → 新 quark-antiquark 対生成 (hadronization)。

### 3.4 ITU 視点

```
K_QCD(IR) >> K_QCD(UV)
```

= **K-flow の IR complexity** = confinement の幾何学的記述 (Wilson loop 期待値が area law)。

---

## 4. Quark-Gluon Plasma (QGP)

### 4.1 高温 deconfined phase

T > T_c ≈ 155 MeV で QCD は **deconfined**:

```
T < T_c: hadron phase
T > T_c: quark-gluon plasma (QGP)
```

### 4.2 観測

- **RHIC** (Brookhaven, 2000-): Au+Au collisions → QGP
- **ALICE** (CERN LHC, 2010-): Pb+Pb collisions → "perfect fluid" QGP
- 観測: η/s ≈ 1/(4π) (KSS bound from AdS/CFT, Phase 116)

### 4.3 早期宇宙

QCD transition at t ≈ 10⁻⁵ s, T ≈ 150 MeV (Phase 127 cosmic timeline)。
**Big Bang 直後** 〜 QCD transition で全宇宙が QGP phase。

### 4.4 ITU 視点

QGP = **K_QCD の deconfined K-state**:

```
T < T_c: K_QCD confined (hadron, K-flow localized)
T > T_c: K_QCD deconfined (free quarks/gluons, K-flow delocalized)
```

= **K-flow phase transition** (1st order? crossover?)。Lattice QCD で確認。

---

## 5. Lattice QCD

### 5.1 提案 (Wilson 1974)

時空を格子 (lattice) で離散化、non-perturbative 計算可能:

```
∫ Dψ DA e^{-S_E[ψ,A]}  →  Σ_{lattice} e^{-S_E^lattice}
```

### 5.2 主要成果

- **Hadron 質量 spectrum** (BMW collaboration 2008, etc.) — proton mass with sub-1% accuracy
- **string tension** σ ≈ 1 GeV/fm
- **QGP transition** T_c ≈ 155 MeV
- **位相幾何的真空** (instantons, monopoles)

### 5.3 数値リソース

- Modern lattice: 96⁴ lattice, peta-flop years
- Open-source codes: MILC, USQCD, Chroma, HotQCD

---

## 6. Chiral Symmetry Breaking

### 6.1 Chiral 対称性

m_u, m_d ≈ 0 limit で:

```
SU(2)_L × SU(2)_R × U(1)_V × U(1)_A
```

(left-right separable quark currents)。

### 6.2 自発的破れ

quark condensate `⟨ūu⟩ + ⟨d̄d⟩ ≠ 0`:

```
SU(2)_L × SU(2)_R → SU(2)_V  (vector, diagonal)
```

→ **3 (pseudo-) Goldstone bosons** = π⁰, π⁺, π⁻ (ほぼ massless)。

### 6.3 ハドロン質量の起源

```
m_proton ≈ 938 MeV
3 × (m_u + m_d) ≈ 20 MeV  (bare quark masses)
```

⇒ **proton 質量の ~ 98% は QCD chiral SSB 由来** (gluon energy, condensate)。

これが **宇宙の baryonic mass の主源**。

### 6.4 ITU 視点

```
K_QCD vacuum = ⟨0|K_QCD|0⟩ ≠ 0 (chiral condensate)
m_hadron = δ⟨K_QCD⟩ at composite K-state
```

= **K_QCD spontaneous symmetry breaking** が proton 質量を生む。

---

## 7. Strong CP Problem ★ Fine-tuning #2

### 7.1 問題

QCD Lagrangian には CP-violating term が許される:

```
L_θ = θ × (g_s² / 32π²) × G^a_μν G̃^{aμν}
```

- θ = QCD vacuum angle
- 自然な値: θ ~ O(1)

### 7.2 観測上限

中性子の電気双極子モーメント (EDM):
```
|d_n| < 1.8 × 10⁻²⁶ e·cm  (PSI 2020)
→ θ_QCD < 10⁻¹⁰
```

⇒ θ が **10¹⁰ 桁 fine-tuned**!

### 7.3 解決候補

- **Peccei-Quinn mechanism** (1977): θ を dynamical field (axion) にして dynamical 0 へ
- **Axion = dark matter 候補** (Phase 129)
- 質量 m_a ~ 10⁻⁶ - 10⁻³ eV, ADMX, IAXO で探索中

### 7.4 ITU 視点

Strong CP problem = K_QCD の **CP-violating boundary condition** の anomalously small value。
Peccei-Quinn = K_axion field でこの value を dynamically driven to 0。

---

## 8. ハドロン質量 Spectrum

### 8.1 メゾン (q̄q)

| ハドロン | 質量 (MeV) | 構成 |
|---|---|---|
| π⁰ | 134.98 | (uū - dd̄)/√2 |
| π⁺ | 139.57 | ud̄ |
| K⁺ | 493.68 | us̄ |
| K⁰ | 497.61 | ds̄ |
| η | 547.86 | (uū + dd̄ - 2ss̄)/√6 |
| η' | 957.78 | (uū + dd̄ + ss̄)/√3 |
| ρ | 775.26 | (uū - dd̄)/√2 vector |

### 8.2 バリオン (qqq)

| ハドロン | 質量 (MeV) | 構成 |
|---|---|---|
| p | 938.27 | uud |
| n | 939.57 | udd |
| Λ | 1115.68 | uds |
| Σ⁺ | 1189.37 | uus |
| Ξ⁰ | 1314.86 | uss |
| Ω⁻ | 1672.45 | sss |

### 8.3 観測 vs Lattice QCD

BMW collaboration 2008: lattice prediction agrees with experiment within ~1%.

---

## 9. 数値検証項目

本 phase の simulation で確認:

1. **QCD running α_s(μ)** (Phase 135 再訪 + Λ_QCD)
2. **Confinement potential** V(r) plot
3. **QGP T_c ≈ 155 MeV** (lattice)
4. **Chiral SSB**: proton mass vs 3 × m_u,d
5. **Hadron spectrum** vs experiment
6. **Strong CP**: θ < 10⁻¹⁰ from neutron EDM

---

## 10. Phase 138 主結論

1. **QCD = SU(3)_C gauge** with asymptotic freedom (Phase 135) + confinement
2. **Confinement**: linear potential V(r) ≈ σ × r, σ ≈ 1 GeV/fm
3. **QGP**: T > T_c ≈ 155 MeV, perfect fluid (η/s ≈ 1/4π)
4. **Lattice QCD**: hadron masses agree with experiment ~1%
5. **Chiral SSB**: π = pseudo-Goldstone; proton mass 98% from QCD
6. **Strong CP problem**: θ < 10⁻¹⁰, fine-tuning 10¹⁰
7. **Peccei-Quinn axion**: DM candidate + Strong CP solution
8. **ITU**: K_QCD = strong K-flow with IR complexity + chiral SSB
9. **次の Phase 139** で **電弱統一 + Weinberg angle + W boson 詳細**

---

## 11. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| QCD Lagrangian | K_QCD strong K-flow |
| Asymptotic freedom | K-flow UV simplification |
| Confinement | K-flow IR complexity |
| QGP | K_QCD deconfined phase |
| Chiral SSB | K_QCD spontaneous symmetry breaking |
| Proton mass 938 MeV | δ⟨K_QCD⟩ (98%) + bare quark (2%) |
| Strong CP problem | K_QCD fine-tuning |
| Axion | K_axion field |

---

## 引用

```
Terada, M. (2026). Phase 138: QCD, confinement, QGP, chiral SSB, and
Strong CP problem in ITU (Tier 1 #20 phase 4/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Wilson, K. G. (1974) "Confinement of quarks" PRD 10, 2445
- Gell-Mann, M. (1962) "Symmetries of baryons and mesons" PR 125, 1067
- Politzer, H. D. (1973), Gross-Wilczek (1973) — Asymptotic freedom
- Peccei, R. D., Quinn, H. R. (1977) "CP conservation in the presence of pseudoparticles" PRL 38, 1440
- BMW Collaboration (2008) "Ab Initio Determination of Light Hadron Masses" Science 322, 1224
- 't Hooft, G. (1976) "Computation of the quantum effects due to a four-dimensional pseudoparticle" PRD 14, 3432
- ALICE Collaboration (2010) "Elliptic flow of charged particles in Pb-Pb collisions at √s_NN = 2.76 TeV" PRL 105, 252302
- PSI nEDM Collaboration (2020) "Measurement of the permanent electric dipole moment of the neutron" PRL 124, 081803
- Particle Data Group (2024) "Review of Particle Physics" PRD 110, 030001
