# Phase 164: 天体流体 — 降着円盤 + 相対論ジェット + 超新星衝撃波 + K_astro

> **Tier 1 #23 Fluid Dynamics — Phase 6/8 (Block A paper 7/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 164 の目的

Phase 163 で MHD を扱った。Phase 164 では **天体スケール流体** に進む — Block A 1-2 (#17 QG, #18 BH) との直接接続:

1. **Eddington luminosity** L_Edd
2. **Bondi 降着** (球対称)
3. **Shakura-Sunyaev α-disk (1973)** — 標準降着円盤
4. **★ M87 BH 降着 (EHT 2019, Phase 122 接続) ★**
5. **相対論ジェット** (AGN, GRB, microquasar)
6. **Lorentz 因子 + Doppler boosting**
7. **超新星衝撃波 + Sedov-Taylor**
8. **ITU 視点**: K_astro = K_MHD + K_gravity + K_relativistic

中心テーゼ:

> **天体流体 = K_MHD + 強重力 (K_geom) + 相対論 (K_field) の coupled K-state**。
> Eddington 限界 = K_radiation の重力 escape 閾値。
> 降着円盤 = K_flow の angular momentum transport problem。
> 相対論ジェット = K_MHD + K_geom の launching mechanism (Blandford-Znajek)。

---

## 1. ★ Eddington Luminosity (1916) ★

### 1.1 物理

輻射圧 = 重力 (平衡限界):

```
L_Edd = (4π G M m_p c) / σ_T
```

σ_T = Thomson cross section = 6.65×10⁻²⁹ m²。

### 1.2 数値公式

```
L_Edd = 1.26 × 10³¹ (M / M_sun) W
      = 3.28 × 10⁴ (M / M_sun) L_sun
```

### 1.3 例

| BH | M | L_Edd |
|---|---|---|
| Cyg X-1 | 21 M_sun | 6.9×10³² W |
| Sgr A* | 4.3×10⁶ M_sun | 1.4×10³⁸ W |
| M87* | 6.5×10⁹ M_sun | 2.1×10⁴¹ W |
| TON 618 (最重) | 6.6×10¹⁰ M_sun | 2.2×10⁴² W |

### 1.4 ITU 視点

```
Eddington = K_radiation × K_gravity の opacity-mediated balance
超 Eddington = K_flow super-critical (UFO, ULX)
```

---

## 2. ★ Bondi 球対称降着 (1952) ★

### 2.1 公式

```
Ṁ_Bondi = 4π λ_B (G M)² ρ_∞ / c_s,∞³
```

λ_B = constant ~ 0.25 (γ=5/3)。

### 2.2 Bondi radius

```
r_B = G M / c_s,∞²
```

### 2.3 数値 (Sgr A*)

```
M = 4.3×10⁶ M_sun
n_∞ ~ 10⁶ /m³, T ~ 10⁷ K → c_s ~ 4×10⁵ m/s
r_B ≈ 0.04 pc
Ṁ_Bondi ≈ 10⁻⁴ M_sun/yr (effective ~10⁻⁹ M_sun/yr 観測, 顕著に低い)
```

### 2.4 ITU 視点

```
Bondi = K_flow + K_gravity の球対称 stationary
低 Bondi 効率 = K_flow magnetic feedback による抑制
```

---

## 3. ★ Shakura-Sunyaev α-disk (1973) ★

### 3.1 設定

中心 BH の周りの薄い回転円盤。**乱流粘性** が angular momentum を外向き輸送 → 質量内向き降着。

### 3.2 α-prescription

```
ν_turb = α c_s H
α ~ 0.01 - 0.1
```

= 乱流粘性 = (sound speed) × (scale height) × α (Phase 160 K41 接続)。

### 3.3 降着率

```
Ṁ = 3 π ν Σ   (Σ: surface density)
```

### 3.4 放射効率

```
L = η Ṁ c²
η = 0.057 (Schwarzschild ISCO)
η = 0.42  (extreme Kerr a=1)
```

### 3.5 数値: M87*

```
M = 6.5×10⁹ M_sun
Ṁ ~ 10⁻³ M_sun/yr (low-luminosity AGN)
L ~ 10⁴² W (sub-Eddington)
```

### 3.6 ITU 視点

```
α-disk = K_flow turbulent angular momentum transport
ISCO (Kerr) = K_geom 内境界 (Phase 119 接続)
```

---

## 4. ★ M87 EHT (2019) + Sgr A* (2022) ★

### 4.1 M87* (Phase 122 接続)

```
M = (6.5 ± 0.7) × 10⁹ M_sun
D = 16.8 Mpc
Shadow radius θ_sh = 21 μas ≈ 5.2 r_g
EHT 観測 2019: ring 直径 42 μas
```

### 4.2 Sgr A* (EHT 2022)

```
M = 4.297 × 10⁶ M_sun
D = 8.277 kpc
θ_sh = 26 μas ≈ 5.2 r_g
EHT 観測 2022: ring 観測
```

### 4.3 ITU 視点

```
EHT image = K_MHD + K_geom の photon ring (Phase 122)
降着流 + ジェット launching = K_flow + K_field + K_gravity
```

---

## 5. ★ 相対論ジェット ★

### 5.1 分類

| 系 | Lorentz 因子 Γ | 例 |
|---|---|---|
| Microquasar | 2-10 | SS 433, GRS 1915 |
| AGN (BL Lac) | 10-30 | Mrk 421, BL Lac |
| AGN (Blazar) | 30-50 | 3C 279, 3C 273 |
| GRB long | 100-1000 | GRB 130427A |
| GRB short | 100-1000 | GW170817 + GRB170817A |

### 5.2 Lorentz 因子 Γ

```
Γ = 1 / √(1 - β²),  β = v/c
```

例 Γ=100: v ≈ 0.99995 c → Lorentz contraction 100×。

### 5.3 ★ Doppler boosting ★

観測 flux:

```
F_obs = F_emit × δ^{3+α}
δ = 1 / (Γ (1 - β cos θ))    (Doppler 因子)
```

ジェットが直接観測者方向に向く (θ ~ 0): δ ~ 2Γ → 強烈に boost。

### 5.4 Superluminal motion

横方向見かけ速度:

```
v_app = v sin θ / (1 - β cos θ)
v_app/c can exceed 1 for β ≈ 1, θ small  (visual illusion)
```

例: M87 jet HST-1 で v_app ~ 6c 観測。

### 5.5 Blandford-Znajek (1977)

回転 BH の磁束抽出による電磁ジェット launching:

```
L_BZ = c B² R_H²
```

R_H = horizon radius。a/M に依存。

### 5.6 ITU 視点

```
相対論 jet = K_MHD + K_geom (Kerr) + K_field の coupled launching
Doppler boosting = K_relativistic frame transformation
Blandford-Znajek = K_geom rotation → K_field flux extraction
```

---

## 6. ★ 超新星衝撃波 + Sedov-Taylor (1959) ★

### 6.1 設定

点状エネルギー注入 E_SN → 球対称衝撃波の自己相似展開:

```
r_sh(t) = ξ_0 (E t² / ρ_0)^{1/5}
```

ξ_0 = 1.15 (γ=5/3)。

### 6.2 数値: SN 1054 (Crab)

```
E_SN ~ 10⁴⁴ J
ρ_ISM ~ 10⁻²¹ kg/m³
At t = 1000 yr: r_sh ~ 5 pc (Crab Nebula 観測 ~ 5 pc ✓)
```

### 6.3 衝撃波後 v_sh

```
v_sh(t) = (2/5) ξ_0 (E / ρ_0)^{1/5} t^{-3/5}
```

= time-decreasing。

### 6.4 ★ Diffusive shock acceleration (DSA, Fermi 1949) ★

衝撃波で荷電粒子が 1 次 Fermi 加速 → **宇宙線 power-law spectrum E^{-2}**。

### 6.5 ITU 視点

```
SN 衝撃波 = K_flow + K_radiation injection
Sedov-Taylor = K_flow 自己相似 (Phase 145 universality 接続)
Fermi acceleration = K_flow から K_particle へエネルギー転送
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Eddington luminosity** for 4 BH masses
2. **Bondi accretion rate** for Sgr A*
3. **Shakura-Sunyaev α** standard values
4. **M87/Sgr A* shadow** θ_sh ≈ 5.2 r_g
5. **Doppler boost δ^{3+α}** Γ=10, 30, 100 で計算
6. **Sedov-Taylor** Crab 1000 yr → 5 pc

---

## 8. Phase 164 主結論

1. **Eddington L_Edd = 1.26×10³¹ (M/M_sun) W**
2. **Bondi spherical accretion** Ṁ ∝ M²
3. **Shakura-Sunyaev α-disk (1973)**: ν_turb = α c_s H
4. **Kerr η = 0.42** (extreme), Schwarzschild η = 0.057
5. **M87* EHT (2019)**: 42 μas ring at M = 6.5×10⁹ M_sun
6. **Doppler boost** δ^4 (continuum), δ^3 (line); Γ=10 で 10⁴× factor
7. **Superluminal v_app ~ 6c** for M87 jet (visual illusion)
8. **Blandford-Znajek (1977)**: 回転 BH 電磁 launching
9. **Sedov-Taylor (1959)**: r_sh ∝ t^{2/5}; Crab 5 pc ✓
10. **ITU**: K_astro = K_MHD + K_geom + K_relativistic
11. **次の Phase 165** で **Millennium Problem (Navier-Stokes)**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Eddington L_Edd | K_radiation × K_gravity balance |
| Bondi 降着 | K_flow + K_gravity 球対称 |
| α-disk | K_flow turbulent angular momentum transport |
| ISCO (Kerr) | K_geom 内境界 |
| M87 EHT | K_MHD + K_geom photon ring |
| Lorentz Γ | K_relativistic frame |
| Doppler boost | K_relativistic flux transformation |
| Blandford-Znajek | K_geom → K_field flux extraction |
| Sedov-Taylor | K_flow 自己相似衝撃波 (Phase 145 universality) |
| Fermi acceleration | K_flow → K_particle energy transfer |

---

## 引用

```
Terada, M. (2026). Phase 164: Astrophysical fluids — accretion, relativistic jets,
supernova shocks in ITU (Tier 1 #23 phase 6/8). Zenodo. DOI: [10.5281/zenodo.20249794](https://doi.org/10.5281/zenodo.20249794).
```

主要参考文献:
- Eddington, A. S. (1916) "On the radiative equilibrium of the stars" MNRAS 77, 16
- Bondi, H. (1952) "On spherically symmetrical accretion" MNRAS 112, 195
- Shakura, N. I., Sunyaev, R. A. (1973) "Black holes in binary systems: observational appearance" A&A 24, 337
- Novikov, I. D., Thorne, K. S. (1973) "Astrophysics of black holes" in Black Holes (Les Houches)
- Blandford, R. D., Znajek, R. L. (1977) "Electromagnetic extraction of energy from Kerr black holes" MNRAS 179, 433
- Blandford, R. D., Payne, D. G. (1982) "Hydromagnetic flows from accretion discs" MNRAS 199, 883
- Rees, M. J. (1966) "Appearance of relativistically expanding radio sources" Nature 211, 468 (superluminal)
- EHT Collaboration (2019) "First M87 Event Horizon Telescope results" ApJL 875, L1-L6
- EHT Collaboration (2022) "First Sgr A* Event Horizon Telescope results" ApJL 930, L12-L17
- Sedov, L. I. (1959) Similarity and Dimensional Methods in Mechanics. Academic Press
- Taylor, G. I. (1950) "The formation of a blast wave by a very intense explosion" Proc. R. Soc. A 201, 159
- Fermi, E. (1949) "On the origin of the cosmic radiation" Phys. Rev. 75, 1169
- Bell, A. R. (1978) "The acceleration of cosmic rays in shock fronts" MNRAS 182, 147
- Frank, J., King, A., Raine, D. (2002) Accretion Power in Astrophysics, 3rd ed. Cambridge UP
- Lyubarsky, Y. E. (2010) "A new mechanism for dissipation of alternating fields in Poynting-dominated outflows" ApJ 725, L234
