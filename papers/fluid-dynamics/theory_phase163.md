# Phase 163: 磁気流体力学 (MHD) + プラズマ流体 + Alfvén 波 + K_MHD

> **Tier 1 #23 Fluid Dynamics — Phase 5/8 (Block A paper 7/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 163 の目的

Phase 159-162 で中性流体 NS / 乱流 / 境界層 / 渦を扱った。Phase 163 では **荷電流体 (磁気流体力学 = MHD)** へ進む — プラズマ物理 (Tier 1 #2) との接続:

1. **MHD 基礎方程式** (Maxwell + NS 結合)
2. **Magnetic Reynolds 数** R_m
3. **★ Alfvén 波 (1942 Nobel 1970) ★**
4. **磁気張力 + 磁気圧**
5. **Alfvén 凍結 (Frozen-in 定理)**
6. **太陽風 + 磁気圏 + 磁気再結合**
7. **トカマク核融合プラズマ閉じ込め**
8. **ITU 視点**: K_MHD = K_flow + K_field (B-coupled), 量子渦 (Phase 162) との類縁

中心テーゼ:

> **MHD = K_flow + K_Maxwell の coupled K-state**。
> Alfvén 波 = K_MHD の transverse wave mode。
> 凍結磁束 = K_flow + K_field の topological coupling (高 R_m 極限)。
> 太陽風 = K_MHD の天体スケール例。

---

## 1. ★ MHD 基礎方程式 ★

### 1.1 4 つの基礎方程式

```
質量保存:   ∂ρ/∂t + ∇·(ρu) = 0
運動量:    ρ Du/Dt = -∇p + J×B + μ∇²u + ρg
電場:      E + u×B = J/σ       (Ohm's law)
磁場:      ∂B/∂t = -∇×E,  ∇·B = 0,  ∇×B = μ_0 J  (Maxwell)
```

### 1.2 Induction 方程式

Ohm's law + Maxwell → :

```
∂B/∂t = ∇×(u×B) + η ∇²B
```

η = 1/(μ_0 σ): magnetic diffusivity。

### 1.3 ★ Magnetic Reynolds 数 ★

```
R_m = U L / η = μ_0 σ U L
```

- **R_m ≪ 1**: 拡散支配 (laboratory plasma 一部)
- **R_m ≫ 1**: 移流支配 (astrophysical plasma)

### 1.4 数値例

| 系 | U (m/s) | L (m) | σ (S/m) | R_m |
|---|---|---|---|---|
| Mercury lab | 0.1 | 0.1 | 10⁶ | **1.3** |
| Earth liquid core | 1e-3 | 10⁶ | 10⁵ | **130** |
| Sun convection cell | 200 | 10⁸ | 10⁶ | **2×10¹⁹** |
| Solar wind | 4e5 | 10¹¹ | 10⁻⁴ | **5×10¹³** |
| Tokamak plasma | 10³ | 1 | 10⁸ | **10¹³** |

### 1.5 ITU 視点

```
MHD = K_flow + K_Maxwell の coupled K-state
R_m = K_field advection / diffusion 比
```

---

## 2. ★ Alfvén 波 (Alfvén 1942, Nobel 1970) ★

### 2.1 物理

均一磁場 B₀ に沿った **横波**:
- 流体運動 u ⊥ B₀
- 磁力線が "弦のように" 振動

### 2.2 Alfvén 速度

```
v_A = B₀ / √(μ_0 ρ)
```

= 磁場張力 / 流体慣性 比。

### 2.3 数値例

| 系 | B (T) | ρ (kg/m³) | v_A (m/s) |
|---|---|---|---|
| Sun corona | 0.01 | 10⁻¹² | **8.9×10⁶** (8.9 Mm/s) |
| Sun photosphere | 0.1 | 10⁻⁴ | 8.9×10⁴ |
| Solar wind | 5e-9 | 5e-21 | 6.3×10⁴ |
| Earth磁気圏尾 | 2e-8 | 1e-23 | 1.4×10⁶ |
| Tokamak | 5 | 1e-6 | **4.5×10⁶** |

### 2.4 ITU 視点

```
Alfvén 波 = K_MHD transverse mode
v_A = K_MHD 磁気弾性 propagation speed
```

---

## 3. ★ 磁気張力 + 磁気圧 ★

### 3.1 J × B 力分解

```
J × B = (B·∇)B/μ_0 - ∇(B²/(2μ_0))
       = 磁気張力      + 磁気圧
```

### 3.2 磁気圧

```
p_mag = B² / (2 μ_0)
```

太陽光球 B=0.1T: p_mag = 0.1²/(2×4π×1e-7) ≈ 4000 Pa。

### 3.3 プラズマ β

```
β = p_gas / p_mag = (n k_B T) × 2μ_0 / B²
```

- β ≪ 1: 磁場支配 (太陽 corona, tokamak)
- β ≫ 1: 流体支配 (太陽内部)

### 3.4 ITU 視点

```
磁気圧 = K_field の equivalent pressure
プラズマ β = K_gas / K_field 比
```

---

## 4. ★ 凍結磁束 定理 (Alfvén 1942) ★

### 4.1 主張

R_m → ∞ (理想 MHD) で **磁束 が流体粒子と共に運ばれる**:

```
∂B/∂t = ∇×(u×B)   (η = 0)
⇒ DΦ/Dt = 0 (磁束 Φ = ∫ B·dA on co-moving surface)
```

= **磁場線が流体に "凍結"**。Kelvin 循環定理 (Phase 162) の磁場版。

### 4.2 帰結

- **磁束の topological 連結性が保存**
- 磁気エネルギー の蓄積 → magnetic reconnection で解放 (太陽フレア)

### 4.3 Magnetic reconnection

η ≠ 0 の薄い拡散層で磁束が切れる:
- 太陽フレア (10²⁵ J/event)
- 磁気圏オーロラ
- Tokamak disruption

### 4.4 ITU 視点

```
凍結磁束 = K_flow + K_field の topological coupling
Reconnection = K_field topology change → energy release
```

---

## 5. 太陽風 + 磁気圏 + 太陽磁気活動

### 5.1 Parker 太陽風モデル (1958)

太陽 corona の超音速膨張:

```
v_solar wind ≈ 400-700 km/s
n ≈ 5 /cm³ at 1 AU
T ≈ 10⁵-10⁶ K
B (Parker spiral) ≈ 5 nT at 1 AU
```

### 5.2 磁気圏

地球磁場が太陽風を偏向:
```
Magnetopause (day-side): R ≈ 10 R_E ≈ 64,000 km
Bow shock (Mach 8): R ≈ 12 R_E
Magnetotail: 100-1000 R_E
```

### 5.3 太陽サイクル 11 年

- 黒点数 (Schwabe 1843)
- ダイナモ理論 (Parker 1955)
- 偏光磁場反転

### 5.4 ITU 視点

```
太陽風 = K_MHD 天体スケール K-state
ダイナモ = K_field self-sustained generation
```

---

## 6. ★ 核融合 + Tokamak (1968-) ★

### 6.1 ITER (2025-)

```
R = 6.2 m (主半径)
a = 2.0 m (小半径)
B_t = 5.3 T
I_p = 15 MA
β ≈ 0.025
Q = P_fusion/P_heat ≈ 10 (target)
T_ion = 15 keV ≈ 1.7×10⁸ K
```

### 6.2 ローソン基準

```
n τ_E T > 3×10²¹ keV·s/m³
```

= 自己加熱条件。

### 6.3 Tokamak vs Stellarator

| 機 | 磁場形態 | 状態 |
|---|---|---|
| Tokamak (ITER) | toroidal + plasma current | 主流 |
| Stellarator (Wendelstein 7-X) | external coils only | プラズマ電流不要 |
| Spherical Tokamak (NSTX-U) | small aspect ratio | コンパクト |

### 6.4 ITU 視点

```
Tokamak = K_MHD 制御核融合プラズマ閉じ込め
Lawson criterion = K_MHD energetic threshold
```

---

## 7. MHD instabilities

### 7.1 主要モード

- **Kink instability** (m=1): プラズマ柱 ねじれ
- **Sausage** (m=0): 軸対称収縮
- **Rayleigh-Taylor in MHD**: 浮力 + 磁場
- **Kelvin-Helmholtz in MHD**: 剪断 + 磁場安定化

### 7.2 安定化条件

```
Suydam: B_z' / (k r) < threshold
Mercier criterion
```

### 7.3 ITU 視点

```
MHD instability = K_MHD の不安定 K-channel
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Magnetic Reynolds 数** R_m 各種系
2. **Alfvén 速度** v_A for Sun, tokamak
3. **Plasma β** for 各種環境
4. **太陽風 1 AU** 数値
5. **ITER パラメータ** 一覧
6. **Magnetic pressure** B²/(2μ_0)

---

## 9. Phase 163 主結論

1. **MHD = NS + Maxwell 結合** (Faraday-Ohm + induction)
2. **R_m = μ_0 σ U L** で diffusion vs advection 分類
3. **Alfvén 波 (1942 Nobel 1970)**: v_A = B/√(μ_0 ρ)
4. **磁気圧** = B²/(2μ_0); プラズマ β = p_gas/p_mag
5. **凍結磁束 (Alfvén)**: 理想 MHD で磁場線が流体凍結 (Kelvin 類縁)
6. **Magnetic reconnection**: η ≠ 0 で磁束 topology 変化 → 太陽フレア 10²⁵ J
7. **Parker 太陽風 (1958)**: 400-700 km/s, B ≈ 5 nT @ 1 AU
8. **ITER (2025-)**: B=5.3T, T=15 keV, Q=10 target
9. **ITU**: K_MHD = K_flow + K_Maxwell coupled, 凍結 = topological
10. **次の Phase 164** で **天体流体 (降着円盤 + 相対論ジェット)**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| MHD 方程式 | K_flow + K_Maxwell coupling |
| R_m | K_field advection/diffusion 比 |
| Alfvén 波 | K_MHD transverse mode |
| v_A | K_MHD 磁気弾性速度 |
| 磁気圧 B²/(2μ_0) | K_field equivalent pressure |
| プラズマ β | K_gas/K_field 比 |
| 凍結磁束 | K_flow + K_field topological coupling |
| Magnetic reconnection | K_field topology change |
| Tokamak | K_MHD 制御核融合 |
| Lawson criterion | K_MHD 自己加熱閾値 |

---

## 引用

```
Terada, M. (2026). Phase 163: Magnetohydrodynamics + plasma fluids + Alfvén waves
in ITU (Tier 1 #23 phase 5/8). Zenodo. DOI: [10.5281/zenodo.20249794](https://doi.org/10.5281/zenodo.20249794).
```

主要参考文献:
- Alfvén, H. (1942) "Existence of electromagnetic-hydrodynamic waves" Nature 150, 405 (Nobel 1970)
- Parker, E. N. (1955) "Hydromagnetic dynamo models" ApJ 122, 293
- Parker, E. N. (1958) "Dynamics of the interplanetary gas and magnetic fields" ApJ 128, 664
- Cowling, T. G. (1957) Magnetohydrodynamics. Interscience
- Biskamp, D. (2000) Magnetic Reconnection in Plasmas. Cambridge UP
- Priest, E. R. (2014) Magnetohydrodynamics of the Sun. Cambridge UP
- Wesson, J. (2011) Tokamaks, 4th ed. Oxford UP
- Goedbloed, J. P., Poedts, S. (2004) Principles of Magnetohydrodynamics. Cambridge UP
- Sweet, P. A. (1958), Parker, E. N. (1957) Sweet-Parker reconnection
- Petschek, H. E. (1964) "Magnetic field annihilation" NASA SP-50, 425
- ITER organization (2025+) ITER Tokamak Reference Design
- Lawson, J. D. (1957) "Some criteria for a power producing thermonuclear reactor" Proc. Phys. Soc. B 70, 6
