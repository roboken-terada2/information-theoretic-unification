# Phase 132: CMB Polarization (E/B-modes) + LiteBIRD + Primordial GW

> **Tier 1 #19 Cosmology — Phase 6/8 (Block A paper 3/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 132 の目的

Phase 128 で inflation 期の量子揺らぎを扱った。Phase 132 では **CMB 偏光** に焦点を当て、**B-mode (primordial gravitational waves)** の検出戦略を解析する。

確立する内容:

1. **CMB 偏光の物理**: Thomson scattering at recombination
2. **E-mode vs B-mode decomposition** (Kamionkowski-Kosowsky-Stebbins 1997, Seljak-Zaldarriaga 1997)
3. **E-mode 起源**: scalar density perturbations
4. **B-mode 起源**: primordial GW (tensor) + lensing (secondary)
5. **観測史**: WMAP → Planck → BICEP/Keck → SPTpol/ACT → LiteBIRD 2032+
6. **ITU 視点**: K_tensor の直接検証 platform

中心テーゼ:

> **CMB B-mode = inflation 期 K_tensor の直接観測信号**。
> r (tensor-to-scalar ratio) ↔ inflation energy scale ↔ ITU K_geom amplitude at horizon exit。
> **LiteBIRD (2032 launch, JAXA)** が r ~ 0.001 で **K_tensor の存在を確定可能**。
> CMB-S4 (2030s, ground) で r ~ 0.0005、Starobinsky R² inflation 確定圏。

---

## 1. CMB 偏光の物理

### 1.1 Thomson Scattering at Recombination

CMB photons (z ≈ 1100) は最後の散乱面で **anisotropic quadrupole** を持つ電子と Thomson scattering:

```
σ_T = 6.65 × 10⁻²⁹ m²
```

quadrupole が偏光を作る (Rees 1968)。

### 1.2 Polarization Pattern

CMB 偏光は **Stokes parameters Q, U** で記述:

```
Q = ⟨E_x²⟩ - ⟨E_y²⟩
U = 2 ⟨E_x E_y⟩
```

球面上で **spin-2 tensor field** = (Q ± i U) ψ。

### 1.3 強度

```
P / T ≈ 5-10% (typical)
B-mode / T ≈ 0.01-0.1%  (primordial GW)
```

---

## 2. E-mode vs B-mode Decomposition

### 2.1 定義 (Kamionkowski-Kosowsky-Stebbins 1997)

偏光 tensor を **gradient (E)** と **curl (B)** に分解:

```
∇² P^E (scalar)
∇ × P^B (pseudoscalar)
```

- **E-mode**: parity even, radial/tangential pattern
- **B-mode**: parity odd, curl pattern

### 2.2 球面調和展開

```
P = E_ℓm × Y_ℓm^E + B_ℓm × Y_ℓm^B
```

power spectra:
```
C_ℓ^EE = ⟨|E_ℓm|²⟩
C_ℓ^BB = ⟨|B_ℓm|²⟩
C_ℓ^TE = ⟨a_ℓm^T × E_ℓm⟩  (T-E correlation)
```

### 2.3 起源

| Mode | 起源 |
|---|---|
| E | scalar density perturbations (acoustic) |
| B | tensor (GW) + lensing (secondary) |
| TE | scalar acoustic phase relation |

---

## 3. E-mode Power Spectrum

### 3.1 観測 (Planck 2018)

E-mode acoustic peaks:
- 第 1 peak: ℓ ≈ 140 (T peak の半分の位置)
- amplitude: ~ T amplitude × 0.1

E-mode は **scalar perturbation** から派生 → ΛCDM で完全予言。

### 3.2 重要性

- 再電離時期 (z ≈ 6-20) の τ (optical depth) を制約
- T-E correlation で **acoustic phase** を独立確認

### 3.3 数値

Planck 2018:
- τ = 0.054 ± 0.007 (再電離 optical depth)
- C_ℓ^EE_max ≈ 40 μK² @ ℓ ≈ 140

---

## 4. B-mode Power Spectrum ★ 究極の目標

### 4.1 起源 1: Primordial GW (Tensor)

Inflation 中の量子揺らぎが tensor mode (重力波) を生成:

```
δh ∝ H_inflation / M_Pl
```

CMB last scattering で偏光に encode → **primordial B-mode**。

### 4.2 起源 2: Gravitational Lensing (Secondary)

E-mode が大規模構造による weak lensing で B-mode に **散乱**:

```
B_lens(ℓ) ∝ ∫ d²ℓ' E(ℓ') × C_φφ(|ℓ-ℓ'|) × sin(2(φ - φ'))
```

- Lensing B-mode peak: ℓ ~ 1000
- Primordial B-mode peak: ℓ ~ 80-100 (reionization), ℓ ~ 300 (recombination)

⇒ ℓ ~ 100 が **primordial signature 検出の最適範囲**。

### 4.3 Tensor-to-Scalar Ratio r

```
r = C_ℓ^BB,prim / C_ℓ^EE,scalar  (at ℓ ~ 80-100)
```

```
V^{1/4} = (r / 0.01)^{1/4} × 10¹⁶ GeV
```

- r = 0.06: V^{1/4} ~ 1.8 × 10¹⁶ GeV (GUT scale)
- r = 0.001: V^{1/4} ~ 6 × 10¹⁵ GeV

---

## 5. 観測史 + LiteBIRD / CMB-S4

### 5.1 観測史

| Mission | Year | r limit |
|---|---|---|
| WMAP | 2003-2010 | < 0.20 |
| Planck | 2013-2018 | < 0.10 |
| BICEP1 / BICEP2 | 2009-2015 | < 0.07 (initial false claim 2014) |
| **BICEP/Keck + Planck** | **2021** | **< 0.06** ← current best |
| SPT-3G | 2017- | < 0.10 |
| POLARBEAR / Simons Array | 2014- | < 0.13 |
| ACTPol | 2014- | --- |

### 5.2 LiteBIRD (Lite (Light) satellite for the studies of B-mode polarization and Inflation from cosmic background Radiation Detection)

- **打ち上げ予定: 2032** (JAXA strategic L-class mission)
- 軌道: Sun-Earth L2 (Lagrange point)
- 観測周波数: 40-402 GHz, 15 bands
- 感度: r ~ 0.001 (1σ)
- 主要目的: **inflation energy scale 直接測定**

### 5.3 CMB-S4 (2030s)

- 地上 (South Pole + Atacama)
- 大規模 detector array (500,000+ TES)
- 感度: r ~ 0.0005

### 5.4 Combined: LiteBIRD + CMB-S4

- r ~ 0.001 を **5σ 検出**可能
- Starobinsky R² inflation (r ≈ 0.003) を確定範囲

---

## 6. ITU 視点

### 6.1 K_tensor の直接検証

inflation 中の K-flow:

```
K_inflaton (scalar K-state)
+ K_tensor (gravitational waves K-state)
```

B-mode 検出 ⇔ K_tensor の量子揺らぎ存在確認。

### 6.2 r ↔ inflation energy scale

```
r ∝ ε ∝ (V'/V)²
V^{1/4} = (r/0.01)^{1/4} × 10¹⁶ GeV
```

ITU は **inflation potential V(φ) の形**を直接読み出す。

### 6.3 LiteBIRD priority

ITU 検証 priority list (Phase 117 + 118 + 126 から):
1. BMV (gravitational entanglement, 2032)
2. **LiteBIRD (r ~ 0.001, 2034)** ★
3. EHT 5 μas (BH shadow, 2030)
4. GWTC-5 (LIGO O5, 2030)
5. Q-computer BH simulation (2032)

LiteBIRD は **inflation epoch K_tensor の唯一直接観測**。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **E-mode + B-mode power spectra** (toy model)
2. **Primordial vs lensing B-mode comparison**
3. **r upper limit history** (Phase 128 と整合)
4. **LiteBIRD sensitivity vs r** prediction
5. **Inflaton potential predictions** (r vs V^{1/4})

---

## 8. Phase 132 主結論

1. **CMB 偏光**: Thomson scattering で生成、Stokes Q, U で記述
2. **E/B 分解** (KKS 1997): scalar vs tensor 起源
3. **E-mode**: τ = 0.054 (Planck 2018)、ΛCDM で完全予言
4. **B-mode primordial**: inflation 期 K_tensor の signature
5. **B-mode lensing**: ℓ ~ 1000 peak、secondary
6. **LiteBIRD 2032+** (JAXA): r ~ 0.001 で 5σ 検出可能
7. **CMB-S4 2030s**: r ~ 0.0005、Starobinsky R² 確定圏
8. **ITU**: K_tensor の直接 cosmological 検証 platform
9. **次の Phase 133** で **Cosmic horizons + multiverse + anthropic**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Thomson scattering | photon-electron K-flow coupling |
| E-mode | K_scalar (density) signature |
| B-mode (primordial) | **K_tensor inflation signature ★** |
| B-mode (lensing) | K_geom × K_scalar correlation |
| r = C_BB^prim / C_EE | tensor K-amplitude ratio |
| LiteBIRD | K_tensor 直接検証 |

---

## 引用

```
Terada, M. (2026). Phase 132: CMB polarization E/B-modes, LiteBIRD,
and primordial gravitational waves in ITU (Tier 1 #19 phase 6/8).
Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Rees, M. J. (1968) "Polarization and Spectrum of the Primeval Radiation in an Anisotropic Universe" ApJL 153, L1
- Kamionkowski, M., Kosowsky, A., Stebbins, A. (1997) "Statistics of cosmic microwave background polarization" PRD 55, 7368
- Seljak, U., Zaldarriaga, M. (1997) "Signature of Gravity Waves in Polarization of the Microwave Background" PRL 78, 2054
- Hu, W., White, M. (1997) "A CMB Polarization Primer" New Astron. 2, 323
- Page, L. et al. (2007) "Three-Year Wilkinson Microwave Anisotropy Probe (WMAP) Observations: Polarization Analysis" ApJS 170, 335
- Planck Collaboration (2020) "Planck 2018 results. V. CMB power spectra and likelihoods" A&A 641, A5
- BICEP/Keck Collaboration (2021) "Improved Constraints on Primordial Gravitational Waves using Planck, WMAP, and BICEP/Keck Observations through the 2018 Observing Season" PRL 127, 151301
- LiteBIRD Collaboration (2023) "LiteBIRD: JAXA's New Strategic L-class Mission for All-Sky Surveys of Cosmic Microwave Background Polarization" PTEP 2023, 042F01
- CMB-S4 Collaboration (2019) "CMB-S4 Science Case, Reference Design, and Project Plan" arXiv:1907.04473
