# Phase 120: Bekenstein-Hawking エントロピー + Hawking 放射 + BH 熱力学 4 法則

> **Tier 1 #18 Black Holes — Phase 2/8 (Block A paper 2/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 120 の目的

Phase 119 で古典 BH 解 (Schwarzschild, Kerr) を扱った。Phase 120 では **量子効果**を導入し、BH を **熱力学的対象**として扱う。

確立する内容:

1. **Bekenstein 1972, 1973**: BH は entropy を持つ → S_BH = A/(4 G_N ℏ)
2. **Hawking 1975**: BH は黒体放射する → T_H = ℏκ/(2π k_B c)
3. **BH 熱力学 4 法則** (Bardeen-Carter-Hawking 1973)
4. **Generalized Second Law (GSL)**
5. **Negative specific heat と蒸発時間**
6. **ITU 公理写像**: BH 熱力学全体が δS = δ⟨K_geom⟩ に帰着

中心テーゼ:

> **BH 熱力学 = ITU 公理 δS = δ⟨K_geom⟩ の最初の具体化**。
> Bekenstein S_BH = A/(4 ℓ_P²) は ITU 公理の特殊解。
> Hawking T_H = ℏκ/(2π k_B c) は K_geom の温度。
> 蒸発時間 t_evap ~ M³ × G²/(ℏ c⁴) で太陽質量 BH は 10⁶⁷ 年。

---

## 1. Bekenstein のエントロピー予想 (1972, 1973)

### 1.1 動機

熱力学第二法則:
- 物質を BH に投入 → 外部の S 減少
- BH 自体の S が増加せねば第二法則が破れる

⇒ **BH に entropy を割り当てる必要**。

### 1.2 公式

```
S_BH = k_B × A_horizon / (4 ℓ_P²) = k_B × c³ A / (4 ℏ G_N)
```

(SI 単位、自然単位では `S_BH = A / (4 ℓ_P²)` nats)

### 1.3 数値例

| BH | M | A (m²) | S_BH (nats) |
|---|---|---|---|
| Stellar | 10 M_⊙ | 1.10e+10 | 1.05e+79 |
| Sgr A* | 4×10⁶ M_⊙ | 1.76e+21 | 1.05e+89 |
| M87* | 6.5×10⁹ M_⊙ | 4.64e+27 | **4.43e+96** |

BH エントロピーは **巨大** (太陽の総 entropy ~ 10⁵⁸ nats を遥かに超える)。

---

## 2. Hawking Radiation (1975)

### 2.1 公式

BH の Hawking 温度:

```
T_H = ℏ κ / (2π k_B c) = ℏ c³ / (8π G_N M k_B)
```

- κ = c⁴ / (4 G_N M): surface gravity (Schwarzschild)
- T_H ∝ 1/M (質量が小さいほど熱い)

### 2.2 数値例

| BH | M | T_H (K) |
|---|---|---|
| Stellar | 10 M_⊙ | 6.17e-09 |
| Sgr A* | 4×10⁶ M_⊙ | 1.54e-14 |
| M87* | 6.5×10⁹ M_⊙ | **9.49e-18** |
| Planck-mass primordial | m_P | **5.3e+30** ≈ T_P |

CMB ~ 2.7 K より遥かに冷たい (すべての観測 BH)。

### 2.3 派生公式

- 放射出力: dM/dt = -ℏ c⁴ / (15360 π G_N² M²)
- 蒸発時間: t_evap = 5120 π G_N² M³ / (ℏ c⁴)

---

## 3. BH 熱力学 4 法則 (Bardeen-Carter-Hawking 1973)

| 法則 | 通常の熱力学 | BH 熱力学 |
|---|---|---|
| **0** | 平衡状態では T 一様 | κ は horizon 上一定 |
| **1** | dU = T dS + 仕事 | **dM = (κ/8π) dA + Ω dJ + Φ dQ** |
| **2** | dS ≥ 0 | dA ≥ 0 (面積非減少) |
| **3** | T → 0 で S → const | κ → 0 (extremal) に有限手段で到達不可 |

### 3.1 第一法則 (詳細)

```
dM c² = T_H dS_BH + Ω_H dJ + Φ_H dQ
```

- Ω_H: horizon 角速度
- Φ_H: horizon 電位
- T_H dS_BH = κ dA / (8π G_N)

### 3.2 ITU 視点

```
dS_BH = dA / (4 ℓ_P²) = d⟨K_geom⟩
```

第一法則は **ITU 公理の BH 版**。

---

## 4. Generalized Second Law (GSL)

### 4.1 主張 (Bekenstein 1973)

```
dS_total = dS_BH + dS_matter ≥ 0
```

物質を BH に投入しても、S_BH の増加が S_matter の減少を補う → 全 entropy は増加。

### 4.2 ITU 視点

GSL = **ITU 公理 δS = δ⟨K⟩ の保存則**:

- S_matter → 物質の modular Hamiltonian エネルギー期待値
- S_BH → K_geom の boundary contribution
- Total: K-flow 保存により dS_total ≥ 0

### 4.3 反例?

理論的には GSL 違反シナリオが提案されたが (Bekenstein-Mayo information bound)、 **Bekenstein-Hawking エントロピー上限を遵守**すれば GSL は破れない (Wall 2009)。

---

## 5. Negative Specific Heat + 蒸発時間

### 5.1 Schwarzschild BH の熱容量

```
C = dM c² / dT_H = -M c² / T_H = -8π G_N M² k_B / (ℏ c)
```

**負の熱容量**! エネルギーを失うほど温度が上昇 → **不安定平衡** (Hawking 1976)。

### 5.2 蒸発過程

dM/dt = -ℏc⁴/(15360π G_N² M²) を積分:

```
t_evap = 5120 π G_N² M³ / (ℏ c⁴)
       ≈ 2.1 × 10⁶⁷ (M/M_⊙)³ years
```

### 5.3 数値例

| M | t_evap |
|---|---|
| m_P (Planck mass) | 10⁻³⁹ s |
| 10¹¹ kg (primordial) | 13.8 Gyr ≈ 宇宙年齢 |
| 1 M_⊙ | **2.1×10⁶⁷ 年** |
| 10 M_⊙ | 2.1×10⁷⁰ 年 |
| Sgr A* | 2.1×10⁸⁵ 年 |

⇒ **観測 BH は実質的に蒸発しない**。

---

## 6. ITU 公理写像のまとめ

| BH 熱力学 | ITU |
|---|---|
| S_BH = A / (4 ℓ_P²) | 公理 δS = δ⟨K_geom⟩ の特殊解 |
| T_H = ℏ κ / (2π k_B c) | K_geom modular flow の温度 |
| dM c² = T_H dS + Ω dJ + Φ dQ | ITU 公理 + 保存量 (K_geom, K_angular, K_charge) |
| GSL: dS_total ≥ 0 | K-flow 保存則 |
| Negative C | K_geom の非安定 stationary 点 |
| t_evap ∝ M³ | K_geom dynamics |

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **S_BH 公式 vs 質量** (8 BH スケール)
2. **T_H vs 質量** (CMB との比較)
3. **熱容量 C = dM/dT_H** の負値
4. **蒸発時間 t_evap = 5120 π G² M³ / (ℏ c⁴)** の数値
5. **4 法則の数値検証** (1 法則: dM = T dS + Ω dJ)

---

## 8. Phase 120 主結論

1. **Bekenstein-Hawking**: S_BH = A/(4 ℓ_P²), 巨大エントロピー (10⁷⁷ ~ 10⁹⁶ nats)
2. **Hawking radiation**: T_H ∝ 1/M, CMB より遥かに冷たい
3. **BH 熱力学 4 法則**: 通常の熱力学と完全対応
4. **GSL**: dS_total ≥ 0 (ITU K-flow 保存)
5. **Negative C**: BH は不安定 (蒸発で加熱)
6. **t_evap ∝ M³**: 太陽質量 BH は 10⁶⁷ 年で蒸発
7. **ITU 統一**: BH 熱力学全体が δS = δ⟨K_geom⟩
8. **次の Phase 121** で **Page curve 厳密版 + 蒸発過程の量子情報**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| S_BH | K_geom eigenvalue area |
| T_H | K_geom modular temperature |
| 4 法則 | ITU 公理 + 保存量 |
| GSL | K-flow 保存則 |
| Negative C | K-stationary 不安定性 |
| t_evap ∝ M³ | K_geom dynamics |

---

## 引用

```
Terada, M. (2026). Phase 120: Bekenstein-Hawking entropy, Hawking
radiation, and BH thermodynamics in ITU (Tier 1 #18 phase 2/8).
Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Bekenstein, J. D. (1972) "Black holes and the second law" Lett. Nuovo Cimento 4, 737
- Bekenstein, J. D. (1973) "Black holes and entropy" PRD 7, 2333
- Hawking, S. W. (1974) "Black hole explosions?" Nature 248, 30
- Hawking, S. W. (1975) "Particle creation by black holes" Commun. Math. Phys. 43, 199
- Bardeen, J., Carter, B., Hawking, S. (1973) "The four laws of black hole mechanics" Commun. Math. Phys. 31, 161
- Bekenstein, J. D. (1981) "Universal upper bound on the entropy-to-energy ratio" PRD 23, 287
- Wall, A. C. (2009) "A proof of the generalized second law for rapidly-evolving Rindler horizons" PRD 82, 124019
- Page, D. N. (1976) "Particle emission rates from a black hole" PRD 13, 198
