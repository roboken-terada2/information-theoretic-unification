# Phase 128: Inflation + CMB Anisotropies + Inflaton K-state

> **Tier 1 #19 Cosmology — Phase 2/8 (Block A paper 3/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 128 の目的

Phase 127 で ΛCDM 全体像を扱った。Phase 128 では **インフレーション** に焦点を当て、**Inflaton K-state** = ITU 公理の最早期実現を解析する。

確立する内容:

1. **Inflation (Guth 1981, Linde 1982, Albrecht-Steinhardt 1982)**: 指数膨張で horizon/flatness 問題解決
2. **Slow-roll parameters ε, η**: スカラー場 inflaton の動力学
3. **CMB power spectrum (Sachs-Wolfe + acoustic peaks)**
4. **Tensor-to-scalar ratio r**: primordial gravitational waves
5. **観測史**: COBE 1992 → WMAP 2003 → Planck 2013-2018 → LiteBIRD 2030+
6. **ITU 視点**: inflaton = K_geom の最早期 stationary 点

中心テーゼ:

> **Inflation = ITU 公理 δS = δ⟨K⟩ の最早期 cosmic realization**。
> Inflaton scalar field φ の potential V(φ) = K-flow の **inflation potential**。
> CMB anisotropy power spectrum = inflaton 量子揺らぎの **K-state 痕跡**。
> Tensor-to-scalar ratio r が ITU の **inflation regime 判定パラメータ**。

---

## 1. Inflation の動機 (1981)

### 1.1 解決される 3 つの問題

**Horizon problem**: CMB は全方向で同温 (2.725 K) だが、Big Bang 時点で因果的接触不可能。
→ **指数膨張で全領域が因果的接触を持っていた** とすれば説明可能。

**Flatness problem**: Ω_total ≈ 1 (Planck 2018)。初期条件として極めて fine-tuned。
→ 指数膨張で曲率が事実上ゼロ化。

**Magnetic monopole problem**: GUT は magnetic monopole を予言するが未観測。
→ 指数膨張で密度が事実上ゼロ。

### 1.2 Inflation 実現条件

```
ä > 0  ⇔  p < -ρ c²/3  (Phase 127 の Friedmann 2)
```

→ **負圧** が必要。スカラー場 inflaton で実現:

```
ρ_φ = (1/2) φ̇² + V(φ)
p_φ = (1/2) φ̇² - V(φ)
```

φ̇² ≪ V(φ) で p ≈ -ρ → 指数膨張 (de Sitter-like)。

---

## 2. Slow-Roll Parameters

### 2.1 定義

```
ε = (M_Pl²/2) (V'/V)²
η = M_Pl² (V''/V)
```

- M_Pl = 1/√(8πG) = reduced Planck mass
- V'(φ) = dV/dφ
- ε, η ≪ 1 で slow-roll inflation 成立

### 2.2 inflation 持続時間 (e-folds)

```
N(t) = ln(a_end / a) = ∫ (V/V') dφ / M_Pl²
```

観測整合性: **N ≈ 50-60 e-folds** 必要。

### 2.3 観測予言

**Scalar spectral index**:

```
n_s = 1 - 6ε + 2η
```

Planck 2018: **n_s = 0.965 ± 0.004** (scale-invariant n_s=1 から逸脱)。

**Tensor-to-scalar ratio**:

```
r = 16 ε
```

現在の観測上限: r < 0.06 (Planck + BICEP/Keck 2021)。
LiteBIRD 2030+ で **r 〜 0.001 まで検出可能**。

---

## 3. CMB Anisotropies

### 3.1 観測

```
ΔT / T ~ 10⁻⁵  (全方向)
```

主要寄与:
- **Sachs-Wolfe 効果** (large angle, ℓ < 100): potential 揺らぎ
- **Acoustic peaks** (ℓ = 200-1000): baryon-photon plasma 音波振動
- **Damping tail** (ℓ > 1000): Silk damping

### 3.2 power spectrum C_ℓ

CMB 揺らぎを球面調和関数で展開:

```
ΔT(θ,φ) = Σ a_ℓm Y_ℓm(θ,φ)
C_ℓ = ⟨|a_ℓm|²⟩
```

- 第 1 peak (ℓ ≈ 220): acoustic horizon at recombination → curvature info
- 第 2-3 peaks: baryon density Ω_b
- 高 ℓ ratio: 暗黒物質 Ω_DM

### 3.3 数値: Planck 2018 result

| Peak | ℓ_peak | C_ℓ peak (μK²) |
|---|---|---|
| 1st | 220 | 5800 |
| 2nd | 540 | 2500 |
| 3rd | 810 | 2500 |
| 4th | 1140 | 1400 |
| 5th | 1450 | 800 |

---

## 4. Tensor-to-Scalar Ratio r と Primordial GW

### 4.1 物理的意味

inflation 中の量子揺らぎ:
- **Scalar**: 物質密度揺らぎ → CMB temperature anisotropy
- **Tensor**: time-varying metric (重力波) → CMB B-mode polarization

両者の比 r が **inflation エネルギースケール**を決める:

```
V^{1/4} = (r / 0.01)^{1/4} × 10¹⁶ GeV
```

### 4.2 現在の制約

| Experiment | r upper limit |
|---|---|
| WMAP (2009) | < 0.20 |
| Planck (2018) | < 0.10 |
| Planck + BICEP/Keck (2021) | < 0.06 |
| **LiteBIRD (2030+) target** | **0.001** |

r ≳ 0.01 なら GUT scale inflation 確認。

### 4.3 ITU 視点

```
r = 16 ε = δ K_tensor / δ K_scalar
```

⇒ inflation potential V(φ) の **形状情報**が r に encode。

---

## 5. 観測史と将来計画

| Mission | 期間 | 主要結果 |
|---|---|---|
| COBE | 1989-1993 | CMB anisotropy 初検出 (Smoot-Mather 2006 Nobel) |
| WMAP | 2001-2010 | n_s = 0.96, ΛCDM 確立 |
| Planck | 2009-2013 | 高精度 ΛCDM パラメータ |
| BICEP/Keck | 2014- | B-mode 探索 |
| **LiteBIRD** (JAXA) | **2032 打ち上げ予定** | r ~ 0.001 検出 |
| CMB-S4 (ground) | 2030s | 大規模ground array |

---

## 6. ITU 公理写像

### 6.1 Inflaton K-state

inflation 期の K-state:

```
K_inflaton = (1/2) ∫ d³x [π_φ² + (∇φ)² + 2 V(φ)]
```

- π_φ = ∂L/∂(φ̇): 共役運動量
- V(φ): inflation potential

ITU 公理 δS = δ⟨K_inflaton⟩ が量子揺らぎを発生。

### 6.2 K_inflaton → K_cosmic への遷移

inflation 終了 (reheating) で:

```
K_inflaton → K_radiation + K_matter
```

= ITU の **phase transition**。

### 6.3 CMB power spectrum = K-state 痕跡

```
C_ℓ ∝ |T_ℓ|² × P_scalar(k)
```

P_scalar(k) = inflaton 量子揺らぎ → CMB に **K-fingerprint**。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **slow-roll parameters ε, η** vs n_s 一致
2. **N e-folds** vs r prediction
3. **CMB power spectrum C_ℓ** (toy 5 peak)
4. **LiteBIRD detection prospect** (r ~ 0.001)
5. **Inflaton potential 例** (V(φ) = (1/2) m² φ² etc.)

---

## 8. Phase 128 主結論

1. **Inflation (Guth 1981)**: horizon + flatness + monopole 問題解決
2. **Slow-roll**: ε, η ≪ 1、N ≈ 50-60 e-folds
3. **Observation**: n_s = 0.965 (Planck), r < 0.06 (BICEP/Keck)
4. **CMB**: 5+ acoustic peaks, 1st at ℓ ≈ 220
5. **LiteBIRD (2032+)**: r ~ 0.001 で primordial GW 検出
6. **ITU**: inflaton = K-state の最早期 stationary 点
7. **次の Phase 129** で **Dark Matter + 構造形成**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Inflation | K-state 指数膨張 phase |
| Inflaton φ | K_inflaton scalar |
| Slow-roll ε, η | K-flow stationary 条件 |
| CMB anisotropy | K-state 量子揺らぎ痕跡 |
| Tensor-scalar ratio r | inflation regime 判定 |
| LiteBIRD | K_tensor 直接検証 |

---

## 引用

```
Terada, M. (2026). Phase 128: Inflation, CMB anisotropies, and inflaton
K-state in ITU (Tier 1 #19 phase 2/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Guth, A. H. (1981) "Inflationary universe: A possible solution to the horizon and flatness problems" PRD 23, 347
- Linde, A. D. (1982) "A new inflationary universe scenario" PLB 108, 389
- Albrecht, A., Steinhardt, P. J. (1982) "Cosmology for grand unified theories" PRL 48, 1220
- Mukhanov, V. F., Chibisov, G. V. (1981) "Quantum fluctuations and a nonsingular universe" JETP Lett. 33, 532
- Smoot, G. F. et al. (1992) "Structure in the COBE differential microwave radiometer first-year maps" ApJL 396, L1
- Sachs, R. K., Wolfe, A. M. (1967) "Perturbations of a cosmological model and angular variations of the microwave background" ApJ 147, 73
- Planck Collaboration (2020) "Planck 2018 results. X. Constraints on inflation" A&A 641, A10
- BICEP/Keck Collaboration (2021) "Improved Constraints on Primordial Gravitational Waves" PRL 127, 151301
- LiteBIRD Collaboration (2023) "LiteBIRD: JAXA's New Strategic L-class Mission" PTEP 2023, 042F01
