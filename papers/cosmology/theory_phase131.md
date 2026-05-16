# Phase 131: Hubble Tension + S_8 Tension + 解決候補 + ITU K-flow 視点

> **Tier 1 #19 Cosmology — Phase 5/8 (Block A paper 3/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 131 の目的

Phase 127-130 で ΛCDM + DM + DE を扱った。Phase 131 では **ΛCDM の 2 大 tension** (Hubble, S_8) と解決候補を深く扱う。

確立する内容:

1. **Hubble tension 詳細**: distance ladder vs CMB の 5σ 不一致
2. **S_8 tension 詳細**: weak lensing vs CMB の 3σ 不一致
3. **解決候補**: Early Dark Energy (EDE), Strong DE, Decaying DM, 修正重力
4. **観測整合性チェック**: 各候補 vs Hubble vs S_8 vs CMB
5. **ITU 視点**: K-flow boundary condition の time evolution

中心テーゼ:

> **2 大 tension は ΛCDM の限界、ITU 拡張への明確な signal**。
> Hubble tension = 早期宇宙 K_inflaton と現在 K_Λ の不整合。
> S_8 tension = 構造形成期 K_DM の dynamical 修正の暗示。
> ITU は **time-varying K-state boundary conditions** で両 tension を同時解決可能。

---

## 1. Hubble Tension の構造

### 1.1 2 つの独立測定

**Late-time / distance ladder** (local Universe):
```
H_0 = 73.0 ± 1.0 km/s/Mpc  (SH0ES, Riess 2022)
H_0 = 76.5 ± 2.5 km/s/Mpc  (TRGB rev., Anand 2022)
H_0 = 73.9 ± 3.0 km/s/Mpc  (megamaser, Pesce 2020)
```

**Early-time / CMB+BAO** (global):
```
H_0 = 67.4 ± 0.5 km/s/Mpc  (Planck 2018)
H_0 = 68.1 ± 0.7 km/s/Mpc  (ACT DR4 + Planck)
H_0 = 67.7 ± 0.5 km/s/Mpc  (Planck + BAO)
```

### 1.2 Distance Ladder 構造

```
parallax (~kpc)
    ↓
Cepheids (~Mpc, P-L relation)
    ↓
Type Ia SNe (~Gpc, standardized candles)
    ↓
Hubble flow (H_0)
```

各 step に **systematic 不確実性** が累積。

### 1.3 CMB-based Approach

```
CMB power spectrum
    ↓ ΛCDM model 仮定
sound horizon r_s @ recombination
    ↓ BAO 比較
H_0 (model-dependent)
```

CMB は **早期宇宙**を測定し、ΛCDM model を経由して H_0 を **逆算**。

### 1.4 Tension 数値

```
ΔH_0 = 73.0 - 67.4 = 5.6 km/s/Mpc
σ_combined = √(1.0² + 0.5²) = 1.12
σ_tension = 5.6 / 1.12 ≈ 5.0σ
```

→ **>5σ で ΛCDM consistency に挑戦**。

---

## 2. S_8 Tension の構造

### 2.1 観測

```
S_8 ≡ σ_8 × √(Ω_m / 0.3)
```

**CMB-based**:
```
S_8 = 0.834 ± 0.016  (Planck 2018)
```

**Weak lensing**:
```
S_8 = 0.766 ± 0.020  (KiDS-1000, 2021)
S_8 = 0.776 ± 0.017  (DES Y3, 2022)
S_8 = 0.776 ± 0.024  (HSC Y3, 2023)
```

### 2.2 Tension 数値

```
S_8 (weak lensing avg) = 0.773 ± 0.012
ΔS_8 = 0.834 - 0.773 = 0.061
σ_tension ≈ 3.0σ
```

### 2.3 物理的意味

CMB は **線形 perturbation** を z ≈ 1100 で測定し、ΛCDM growth で現在まで evolution。
Weak lensing は z ≈ 0.3-0.7 の **non-linear structure** を直接測定。

→ **構造形成期に何か変化** している可能性 (DM 散逸 or 修正重力)。

---

## 3. 解決候補 1: Early Dark Energy (EDE)

### 3.1 提案 (Karwal-Kamionkowski 2016, Poulin 2019)

z ~ 3000-50000 で **transient DE 成分**:

```
ρ_EDE(z) = ρ_EDE^max × f(z)
f(z) = 0  (z >> z_c)
f(z) = peak  (z = z_c)
f(z) → 0  (z << z_c)
```

z_c ≈ recombination 直前 (z ≈ 3000)。

### 3.2 効果

EDE は recombination 前に **acoustic horizon を縮小** → r_s 減少 → CMB-inferred H_0 が **上昇**。

```
H_0^EDE ≈ 71-72 km/s/Mpc  (early DE 6-12% peak)
```

### 3.3 残る課題

- **σ_8 tension 悪化**: EDE で構造形成早期化 → σ_8 が増加 → S_8 tension 増悪
- **微調整問題**: z_c 自然性の説明困難
- ACT 観測でも完全 fit 不可

### 3.4 ITU 視点

EDE = **K-flow boundary condition の transient term**:

```
K_total(z) = K_Λ + K_matter + K_radiation + K_EDE(z)
```

ITU は **K-state superposition** を許容。

---

## 4. 解決候補 2: Modified Recombination History

### 4.1 提案

recombination 物理 (z ≈ 1100) を修正:

- **Free electron fraction X_e(z)** の変更
- **CMB last scattering surface** の位置移動
- → r_s 修正

### 4.2 効果

```
H_0^modified ≈ 70-71 km/s/Mpc
```

σ_8 tension への影響は小さい (中性のため)。

### 4.3 ITU 視点

K_recomb modification = **electron-photon 相互作用の K-flow correction**。

---

## 5. 解決候補 3: Modified Gravity

### 5.1 候補

- **f(R) gravity**: R + αR² (Starobinsky)
- **DGP gravity**: 5D Dvali-Gabadadze-Porrati
- **Massive gravity**: graviton mass
- **Galileons**: scalar field with second-derivative kinetic term

### 5.2 効果

修正重力は **growth rate** を変更:

```
f(z) = d ln δ/d ln a  (linear growth rate)
```

ΛCDM: f ≈ Ω_m(z)^0.55
修正重力: f が逸脱

→ S_8 tension 改善可能。

### 5.3 課題

- 多くの修正重力モデルが LIGO の GW170817 で **排除** (速度 c に等しい)
- f(R) は OK だが quintessence-like

### 5.4 ITU 視点

修正重力 = **K_geom (Tier 1 #17) の large-scale 修正**。

---

## 6. 解決候補 4: Decaying / Interacting Dark Matter

### 6.1 提案

DM が時間とともに decay:

```
ρ_DM(z) = ρ_DM^0 × (1+z)^3 × e^{-Γ t}
```

Γ ~ Hubble time^{-1} で σ_8 抑制。

### 6.2 効果

- σ_8 tension 改善 (DM 質量減少で structure 抑制)
- Hubble tension への影響は限定的

### 6.3 ITU 視点

K_DM dynamical decay = **K-flow non-stationary correction**。

---

## 7. 観測整合性チェック

複数 tension を **同時解決** する候補は限られている:

| 候補 | Hubble | S_8 | CMB fit |
|---|---|---|---|
| EDE | 改善 | **悪化** | OK |
| Modified recomb | 改善 | 中立 | OK |
| f(R) gravity | 中立 | 改善 | OK |
| Decaying DM | 中立 | 改善 | OK |
| **EDE + interacting DM** | **改善** | **改善** | OK |

⇒ **複合解** が必要。ITU の **K-state superposition** が自然な枠組み。

---

## 8. ITU K-flow 視点

### 8.1 統一 framework

```
K_total(t) = K_radiation(t) + K_DM(t) + K_baryon(t) + K_Λ(t) + K_EDE(t) + ...
```

各 K-state は **boundary condition + dynamical evolution** を持つ。

### 8.2 Tension = K-flow inconsistency

両 tension は **K-state cross-correlations** の評価不足:

```
ΔH_0 ∝ ⟨K_Λ(now) - K_radiation(early)⟩
ΔS_8 ∝ ⟨K_DM(structure) - K_DM(linear)⟩
```

### 8.3 Pass-2 priority

Phase 222 で ITU-specific evolving K_Λ + interacting K_DM hypothesis を提案予定。

---

## 9. 数値検証項目

本 phase の simulation で確認:

1. **H_0 measurements bar chart** (late vs early)
2. **S_8 measurements bar chart** (CMB vs lensing)
3. **EDE 効果** (H_0 vs σ_8 trade-off)
4. **修正重力 growth rate**
5. **複合候補 (EDE + interacting DM) の同時 fit**

---

## 10. Phase 131 主結論

1. **Hubble tension 5σ**: SH0ES 73.0 vs Planck 67.4 km/s/Mpc
2. **S_8 tension 3σ**: lensing 0.773 vs CMB 0.834
3. **EDE**: Hubble 改善、S_8 悪化
4. **Modified gravity / decaying DM**: S_8 改善 selected
5. **複合解 (EDE + interacting DM)** が同時解決候補
6. **ITU**: K-state superposition で自然な統合
7. **次の Phase 132** で **CMB polarization (E/B mode) + LiteBIRD**

---

## 11. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Hubble tension | K_inflaton vs K_Λ inconsistency |
| S_8 tension | K_DM 構造形成 dynamics 逸脱 |
| EDE | K-flow transient component |
| 修正重力 | K_geom large-scale modification |
| Decaying DM | K_DM non-stationary correction |
| 複合解 | K-state superposition (ITU 自然) |

---

## 引用

```
Terada, M. (2026). Phase 131: Hubble tension, S_8 tension, and ITU
K-flow resolutions (Tier 1 #19 phase 5/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Riess, A. G. et al. (2022) "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team" ApJL 934, L7
- Anand, G. S. et al. (2022) "Comparing tip of the red giant branch distance scales: an independent reduction" ApJ 932, 15
- Karwal, T., Kamionkowski, M. (2016) "Dark energy at early times, the Hubble parameter, and the string axiverse" PRD 94, 103523
- Poulin, V. et al. (2019) "Early Dark Energy can resolve the Hubble Tension" PRL 122, 221301
- KiDS Collaboration (2021) "KiDS-1000 Cosmology" A&A 646, A140
- Hu, B., Liguori, M., Bartolo, N., Matarrese, S. (2014) "Parametrized post-Friedmann framework for interacting dark energy theories" PRD 88, 123514
- Banerjee, A. et al. (2021) "Hubble Sinks In the Low-Redshift Swampland" PRD 103, L081305
- Schöneberg, N. et al. (2022) "The H_0 Olympics: A fair ranking of proposed models" Phys. Rept. 984, 1
