# Phase 140: BSM ― SUSY + GUT + ニュートリノ質量 + ITU K_BSM

> **Tier 1 #20 Standard Model — Phase 6/8 (Block A paper 4/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 140 の目的

Phase 135-139 で SM (gauge + fermion + Higgs + QCD + 電弱) を扱った。Phase 140 では **Beyond Standard Model (BSM)** を扱う:

1. **BSM 動機**: Hierarchy problem (Phase 137), Strong CP (Phase 138), 5σ Hubble (Phase 131), DM (Phase 129), neutrino mass, baryon asymmetry
2. **Supersymmetry (SUSY)**: hierarchy problem 解決 + DM 候補
3. **Grand Unified Theories (GUT)**: SU(5), SO(10) + coupling unification + proton decay
4. **Neutrino mass mechanisms**: Dirac vs Majorana + Seesaw
5. **ITU 視点**: K_BSM = SM の K-state 拡張

中心テーゼ:

> **BSM = ITU の K_BSM hypothesis 候補空間**。
> SUSY = K_fermion ↔ K_boson 対称性 (hierarchy 解決)。
> GUT = K_gauge の高次対称性 (SU(3)×SU(2)×U(1) → SU(5)/SO(10))。
> Neutrino Seesaw = K_neutrino の質量機構 (Pass-2 priority)。
> LHC 探索 (2024) で **natural SUSY 排除気味** → ITU が示す方向性?

---

## 1. BSM 動機の整理

### 1.1 SM 未解決問題

| 問題 | Phase 参照 |
|---|---|
| **Hierarchy problem** (m_H² fine-tuning) | 137 (10³² 桁) |
| **Strong CP problem** (θ_QCD < 10⁻¹⁰) | 138 (10¹⁰ 桁) |
| **Dark Matter** (Ω_DM = 0.265) | 129 (53 桁 mass) |
| **Dark Energy + Λ問題** | 130 (10¹²⁰ 桁) |
| **Hubble tension** (6.3σ) | 131 |
| **Neutrino mass** (m_ν < 0.8 eV) | 129 |
| **Baryon asymmetry** (η_B = 6×10⁻¹⁰) | --- |
| **3 generations** (Phase 136) | 136 |
| **Yukawa hierarchy** (11 桁) | 136 |
| **Cabibbo angle anomaly** | 139 (2-3σ) |
| **Muon g-2** (4.2σ HVPI) | 139 |

⇒ **少なくとも 11 個の未解決問題** が BSM への動機。

---

## 2. Supersymmetry (SUSY)

### 2.1 提案

Boson ↔ Fermion 対称性:

```
Q_α |boson⟩ = |fermion⟩
Q_α |fermion⟩ = |boson⟩
```

各 SM 粒子に **superpartner** が存在:

| SM particle | Superpartner | Spin |
|---|---|---|
| quark (1/2) | squark (0) | 1/2 → 0 |
| lepton (1/2) | slepton (0) | 1/2 → 0 |
| gluon (1) | gluino (1/2) | 1 → 1/2 |
| W, Z (1) | wino, zino (1/2) | 1 → 1/2 |
| Higgs (0) | Higgsino (1/2) | 0 → 1/2 |
| photon (1) | photino (1/2) | 1 → 1/2 |

### 2.2 Hierarchy Problem 解決

各 SM ループ補正 (positive δm²) を superpartner の補正 (negative) が **正確にキャンセル**:

```
δm_H²_SM + δm_H²_SUSY = 0  (exact SUSY)
δm_H²_SM + δm_H²_SUSY ≈ m_SUSY²  (broken SUSY)
```

⇒ Natural SUSY: m_SUSY ~ TeV scale が **m_H = 125 GeV を保護**。

### 2.3 Dark Matter 候補

R-parity 保存 SUSY:
- 最軽 supersymmetric particle (LSP) は安定
- 通常 neutralino (χ_1⁰) = WIMP candidate (Phase 129)
- M_DM ~ 100 GeV - few TeV

### 2.4 LHC 探索現状 (2024)

| 粒子 | 質量下限 (GeV) |
|---|---|
| Gluino (g̃) | > 2300 |
| Squark (q̃) | > 1900 |
| Stop (t̃) | > 1200 |
| Sbottom (b̃) | > 1300 |
| Chargino (χ̃⁺) | > 900 |
| Slepton (ℓ̃) | > 700 |

⇒ **Natural SUSY (m_SUSY ~ 100 GeV) は完全排除**。fine-tuning 復活。

### 2.5 ITU 視点

```
K_SUSY = K_fermion ↔ K_boson symmetry
```

SUSY が高 scale (TeV〜PeV) なら ITU の **K-flow protection partial** = 階層問題部分解。

---

## 3. Grand Unified Theories (GUT)

### 3.1 動機

SM の 3 つの結合 (g_s, g, g') の **GUT scale (10¹⁶ GeV) での統一**:

```
α_1(μ) = (5/3) × α'(μ)  (GUT normalization)
α_2(μ) = α(μ)
α_3(μ) = α_s(μ)
```

3 つが ~ 1 つの scale で **収束**?

### 3.2 SU(5) (Georgi-Glashow 1974)

```
SU(3)_C × SU(2)_L × U(1)_Y ⊂ SU(5)
```

各世代の fermion を **5̄ + 10** に統合:

```
5̄: (d_R, e_L, ν_L, e_R)
10: (u_L, d_L, u_R, e_R^charge-conjugate)
```

### 3.3 Proton Decay (SU(5) 予言)

X, Y gauge bosons (M ~ 10¹⁶ GeV) が **proton decay** を媒介:

```
p → e⁺ + π⁰
τ_p (SU(5) predicted) ~ 10²⁹-10³² years
```

観測上限 (Super-Kamiokande 2020):
```
τ_p > 2.4 × 10³⁴ years (p → e⁺ π⁰)
```

⇒ **Minimal SU(5) は除外**。SUSY-SU(5) (τ_p ~ 10³⁶) または **SO(10)** が必要。

### 3.4 SO(10) (Fritzsch-Minkowski 1975)

```
SO(10): 16-spinor が **1 世代を含む** (16 = 15 SM fermions + 1 right-handed neutrino)
```

ν_R を含むため **neutrino mass 自然**。

### 3.5 ITU 視点

GUT = K_gauge の **高次対称性回復** at μ ~ 10¹⁶ GeV:

```
K_SM(low E) ⊂ K_GUT(high E)
```

= ITU の **K-flow UV unification**。

### 3.6 Coupling Unification 数値

1-loop running:
```
α_i^{-1}(μ) = α_i^{-1}(M_Z) + (b_i / 2π) × ln(μ/M_Z)
```

GUT scale: μ_GUT ≈ 10¹⁶ GeV で `α_i^{-1}` が ~ 同一値に近づく (precise には SUSY 必要)。

---

## 4. Neutrino Mass Mechanisms

### 4.1 Dirac Mass (SM extension)

ν_R を SM に追加:

```
L = -y_ν (L̄_L H̃) ν_R + h.c.
m_ν = y_ν × v / √2
```

m_ν ~ 0.1 eV なら y_ν ~ 10⁻¹² ← **超小** Yukawa。
electron Yukawa y_e ~ 10⁻⁶ と比較しても **6 桁小**。

⇒ Yukawa hierarchy 悪化。

### 4.2 Majorana Mass (See-saw)

ν_R の Majorana 質量を導入:

```
L_Maj = -(1/2) M_R ν̄_R^c ν_R
```

See-saw mechanism (Yanagida 1979, Gell-Mann-Ramond-Slansky 1979):

```
m_ν ≈ m_D² / M_R = (y_ν v)² / M_R
```

- m_D ~ Yukawa × v ~ 100 GeV
- M_R ~ 10¹⁴ GeV (GUT scale)
- m_ν ~ (100 GeV)² / (10¹⁴ GeV) = **0.1 eV** ✓

⇒ **Natural** neutrino mass from large M_R = right-handed Majorana mass。

### 4.3 観測

KATRIN 2022: m_ν < **0.8 eV** (direct β decay)
Planck 2018: Σ m_ν < **0.12 eV** (cosmology)
Oscillation: Δm²_21 = 7.4e-5 eV², |Δm²_31| = 2.5e-3 eV² (Phase 136)

順序 (normal hierarchy vs inverted) 未確定。

### 4.4 Lepton Number Violation

Majorana mass は L (lepton number) を 2 単位破る。
**Neutrinoless double beta decay (0νββ)** 探索:

```
(A, Z) → (A, Z+2) + 2 e⁻
```

KamLAND-Zen (2024): τ_{1/2}(0νββ) > 2 × 10²⁶ yr → m_ν^{Maj} < 36-156 meV。

未検出だが、検出されれば **Majorana 確定**。

### 4.5 ITU 視点

```
K_neutrino = K_Dirac + K_Majorana mass terms
m_ν small ↔ See-saw via heavy M_R
```

= ITU の **K-flow scale hierarchy** での自然解決。

---

## 5. Baryon Asymmetry (Bonus)

### 5.1 観測

```
η_B = (n_B - n_B̄) / n_γ ≈ 6 × 10⁻¹⁰
```

宇宙が baryon dominant (反 baryon は ほぼ消失)。

### 5.2 Sakharov Conditions (1967)

Baryon asymmetry 生成に必要:
1. **Baryon number violation** (B violating process)
2. **C and CP violation**
3. **Out of thermal equilibrium**

### 5.3 候補

- **Electroweak Baryogenesis**: SM + extra Higgs / SUSY 必要
- **Leptogenesis**: neutrino Majorana + see-saw (Phase 140 と整合)
- **GUT baryogenesis**: SU(5)/SO(10) で proton decay 逆反応

⇒ neutrino mass + GUT が同時に説明する自然な scenario。

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **SUSY mass limit** (LHC 2024): gluino > 2.3 TeV など
2. **Proton decay lifetime**: τ_p > 2.4×10³⁴ yr (Super-K)
3. **Neutrino mass**: m_ν < 0.8 eV (KATRIN)
4. **See-saw mechanism**: m_ν = m_D² / M_R
5. **Baryon asymmetry**: η_B = 6×10⁻¹⁰

---

## 7. Phase 140 主結論

1. **BSM 動機**: 11 個の SM 未解決問題
2. **SUSY**: hierarchy 解決 + DM 候補 (neutralino) — **LHC 2024 で natural SUSY 排除気味**
3. **GUT SU(5)** (1974): 結合定数統一、proton decay 予言
4. **Super-K 2020**: τ_p > 2.4×10³⁴ yr → minimal SU(5) 排除
5. **SO(10) + SUSY**: 16-spinor + ν_R + τ_p ~ 10³⁶ yr
6. **Neutrino See-saw**: m_ν = m_D²/M_R, M_R ~ 10¹⁴ GeV
7. **KATRIN m_ν < 0.8 eV** (direct), Planck < 0.12 eV (cosmology)
8. **Leptogenesis** = baryon asymmetry + neutrino mass 同時説明
9. **ITU**: K_BSM = SM の K-state 拡張仮説候補空間
10. **次の Phase 141** で **LHC 実験 + 将来 collider + Particle Cosmology**

---

## 8. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| SUSY | K_fermion ↔ K_boson symmetry |
| Natural SUSY | K-flow protection partial |
| GUT (SU(5)/SO(10)) | K_gauge UV unification |
| Proton decay | K_baryon non-conservation |
| Dirac neutrino mass | K_neutrino tiny Yukawa |
| Majorana + See-saw | K_neutrino scale hierarchy |
| 0νββ | Lepton number violation = K_lepton non-conservation |
| Leptogenesis | K_baryon asymmetry mechanism |

---

## 引用

```
Terada, M. (2026). Phase 140: BSM physics — SUSY, GUT, neutrino mass,
and K_BSM in ITU (Tier 1 #20 phase 6/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Wess, J., Zumino, B. (1974) "Supergauge transformations in four dimensions" Nucl. Phys. B 70, 39
- Nilles, H. P. (1984) "Supersymmetry, supergravity, and particle physics" Phys. Rept. 110, 1
- Georgi, H., Glashow, S. L. (1974) "Unity of all elementary-particle forces" PRL 32, 438
- Fritzsch, H., Minkowski, P. (1975) "Unified interactions of leptons and hadrons" Ann. Phys. 93, 193
- Yanagida, T. (1979) "Horizontal gauge symmetry and masses of neutrinos" KEK Workshop Proc.
- Gell-Mann, M., Ramond, P., Slansky, R. (1979) "Complex spinors and unified theories" Supergravity ed. North-Holland
- Sakharov, A. D. (1967) "Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe" JETP Lett. 5, 24
- Super-Kamiokande Collaboration (2020) "Search for proton decay via p → e⁺ π⁰" PRD 102, 112011
- KATRIN Collaboration (2022) "Direct neutrino-mass measurement with sub-electronvolt sensitivity" Nature Phys. 18, 160
- KamLAND-Zen Collaboration (2024) "Search for Majorana Neutrinos with the Complete KamLAND-Zen Dataset" arXiv:2406.11438
- ATLAS Collaboration (2024) "SUSY summary plots" (CDS preliminary)
- Particle Data Group (2024) "Review of Particle Physics" PRD 110, 030001
