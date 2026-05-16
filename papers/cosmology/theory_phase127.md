# Phase 127: Tier 1 #19 Cosmology — Big Bang + ΛCDM + Friedmann + 宇宙年代

> **Tier 1 #19: Cosmology — Phase 1/8 (Block A paper 3/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> Tier 1 #17 (QG): [10.5281/zenodo.20230667](https://doi.org/10.5281/zenodo.20230667)
> Tier 1 #18 (BH): [10.5281/zenodo.20233070](https://doi.org/10.5281/zenodo.20233070)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 127 の目的

Tier 1 #17 (Quantum Gravity, K_geom) + Tier 1 #18 (Black Holes, K_horizon = horizon specialization) で Block A の物理を進めてきた。
Tier 1 #19 では **宇宙論** を扱い、**K_cosmic** (cosmic horizon specialization) を導入する。

Phase 127 (本) で確立する内容:

1. **Big Bang モデル**: ホットビッグバン、Planck 時代から現在まで
2. **Friedmann 方程式 (1922)**: scale factor a(t) の発展
3. **ΛCDM パラメータ (Planck 2018)**: H_0, Ω_m, Ω_Λ, σ_8, n_s 等
4. **宇宙年代タイムライン**: Planck → GUT → EW → BBN → CMB → 現在
5. **ITU 公理写像**: cosmic horizon = K_cosmic
6. **#18 BH との対称性**: BH horizon ↔ Cosmic horizon

中心テーゼ:

> **宇宙は ITU 公理 δS = δ⟨K_cosmic⟩ の最大規模実現**。
> Cosmic horizon (de Sitter horizon) = BH horizon の **dual**:
>   - BH: 内部に観測者、horizon は外向き
>   - Cosmic: 観測者が内部、horizon は外向き
> → **#18 BH と #19 Cosmology は対称的特殊化**。
> Friedmann eq. + Λ = K_cosmic の dynamical 方程式。

---

## 1. Big Bang モデル

### 1.1 主要証拠

| 観測 | 内容 |
|---|---|
| **赤方偏移** (Hubble 1929) | 銀河の距離 ∝ 後退速度 |
| **CMB** (Penzias-Wilson 1965) | 2.725 K 黒体放射、宇宙の "残光" |
| **BBN** (Gamow 1948) | ¹H, ²H, ³He, ⁴He, ⁷Li の存在比 |
| **大規模構造** | 銀河分布の階層性 |

### 1.2 宇宙年代の主要 epoch

| Epoch | t | scale | 物理 |
|---|---|---|---|
| Planck | 10⁻⁴³ s | T = E_P | 量子重力 (Tier 1 #17) |
| GUT | 10⁻³⁶ s | T ~ 10¹⁶ GeV | 統一相互作用破れ |
| Inflation 終了 | 10⁻³² s | T ~ 10¹⁵ GeV | reheating |
| EW symm breaking | 10⁻¹¹ s | T ~ 100 GeV | Higgs |
| QCD 転移 | 10⁻⁵ s | T ~ 150 MeV | hadron 化 |
| BBN | 1 s - 200 s | T ~ 1 MeV | 原子核合成 |
| Recombination | 380,000 yr | T ~ 0.3 eV | CMB 放射 |
| Reionization | 200 Myr | z ~ 6-20 | 最初の星 |
| 現在 | 13.8 Gyr | T_CMB = 2.725 K | --- |

---

## 2. Friedmann 方程式 (1922)

### 2.1 FLRW 計量

```
ds² = -c² dt² + a(t)² [ dr²/(1-k r²) + r² dΩ² ]
```

- a(t): scale factor (cosmic expansion)
- k: spatial curvature (-1, 0, +1)

### 2.2 Friedmann 第 1 式

```
H² ≡ (ȧ/a)² = (8πG/3) ρ - k c²/a² + Λ c²/3
```

- H: Hubble parameter
- ρ: 全エネルギー密度
- Λ: 宇宙定数

### 2.3 Friedmann 第 2 式

```
ä/a = -(4πG/3) (ρ + 3 p/c²) + Λ c²/3
```

加速膨張 (ä > 0) は **negative pressure (p < -ρc²/3)** が必要 → dark energy。

### 2.4 連続方程式

```
ρ̇ + 3 H (ρ + p/c²) = 0
```

各成分の発展:
- 物質 (p=0): ρ_m ∝ a⁻³
- 放射 (p=ρ/3): ρ_r ∝ a⁻⁴
- 暗黒エネルギー (p=-ρ): ρ_Λ = const

---

## 3. ΛCDM パラメータ (Planck 2018)

| パラメータ | 値 | 説明 |
|---|---|---|
| **H_0** | 67.4 ± 0.5 km/s/Mpc | Hubble 定数 (CMB から) |
| **Ω_m** | 0.315 ± 0.007 | 物質密度比 |
| **Ω_Λ** | 0.685 ± 0.007 | 暗黒エネルギー密度比 |
| Ω_b | 0.0490 ± 0.0007 | バリオン密度比 |
| Ω_DM | 0.265 ± 0.007 | dark matter 密度比 |
| Ω_r | 9.2 × 10⁻⁵ | 放射密度比 |
| **σ_8** | 0.811 ± 0.006 | 8 Mpc/h での密度ゆらぎ振幅 |
| **n_s** | 0.965 ± 0.004 | scalar spectral index |
| Age | 13.797 ± 0.023 Gyr | 宇宙年齢 |

### 3.1 critical density

```
ρ_c = 3 H_0² / (8πG) = 8.6 × 10⁻²⁷ kg/m³
```

H_0 = 67.4 km/s/Mpc で計算。

### 3.2 SH0ES vs Planck: Hubble tension

- Planck (CMB): H_0 = 67.4 km/s/Mpc
- SH0ES (Cepheids+SNe): H_0 = 73.0 ± 1.0 km/s/Mpc
- **5σ tension** ← Phase 131 で詳述

---

## 4. ITU 公理写像

### 4.1 K_cosmic = cosmic horizon modular Hamiltonian

de Sitter (Λ > 0 純真空) horizon は:

```
r_dS = √(3 c² / Λ) ≈ 16 Gpc (現在値)
```

その entropy (Gibbons-Hawking 1977):

```
S_dS = A_dS / (4 G_N ℏ) = π r_dS² / (G_N ℏ) ≈ 2.6 × 10¹²² nats
```

ITU 公理:

```
δS_dS = δ A_dS / (4 G_N ℏ) = δ⟨K_cosmic⟩
```

### 4.2 #18 BH ↔ #19 Cosmic 対称性

| 観点 | #18 BH | #19 Cosmic |
|---|---|---|
| Horizon | event horizon | de Sitter horizon |
| 観測者 | 外部 | 内部 |
| Hawking radiation | outward thermal | 不変 (de Sitter inflaton) |
| Temperature | T_H = ℏc³/(8πG M k_B) | T_dS = ℏ H/(2π k_B) ≈ 10⁻³⁰ K |
| K-state | K_horizon | **K_cosmic** |

両者は ITU 公理 δS = δ⟨K⟩ の **対称的特殊化**。

---

## 5. 数値検証項目

本 phase の simulation で確認:

1. **scale factor a(t) の数値積分** (matter-dominated → Λ-dominated)
2. **Friedmann 方程式の数値解**
3. **ΛCDM パラメータ vs 観測**
4. **宇宙年代 timeline 数値**
5. **critical density と de Sitter horizon**

---

## 6. Phase 127 主結論

1. **Big Bang model**: 13.8 Gyr の cosmic timeline
2. **Friedmann eq. (1922)**: H² = 8πG ρ/3 + Λc²/3 - kc²/a²
3. **ΛCDM (Planck 2018)**: H_0 = 67.4, Ω_m = 0.315, Ω_Λ = 0.685
4. **Hubble tension**: 5σ (Planck vs SH0ES)
5. **K_cosmic**: de Sitter horizon modular Hamiltonian
6. **#18 BH ↔ #19 Cosmic 対称性**: horizon の inside/outside 入れ替え
7. **次の Phase 128** で **Inflation + CMB anisotropies**

---

## 7. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Scale factor a(t) | K_cosmic dynamics |
| Friedmann eq. | δS = δ⟨K_cosmic⟩ の dynamic 形 |
| ΛCDM | K_cosmic の現代パラメータ |
| de Sitter horizon | K_cosmic specialization |
| #18 ↔ #19 対称性 | inside/outside K-flow dual |
| Hubble tension | ΛCDM の ITU 拡張可能性 |

---

## 引用

```
Terada, M. (2026). Phase 127: Big Bang cosmology, ΛCDM, Friedmann
equations, and cosmic timeline in ITU (Tier 1 #19 Cosmology, Block A
paper 3/9, phase 1/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Friedmann, A. (1922) "Über die Krümmung des Raumes" Z. Phys. 10, 377
- Hubble, E. (1929) "A relation between distance and radial velocity among extra-galactic nebulae" PNAS 15, 168
- Gamow, G. (1948) "The Origin of Elements and the Separation of Galaxies" PR 74, 505
- Penzias, A. A., Wilson, R. W. (1965) "A Measurement of Excess Antenna Temperature at 4080 Mc/s" ApJ 142, 419
- Gibbons, G. W., Hawking, S. W. (1977) "Cosmological event horizons, thermodynamics, and particle creation" PRD 15, 2738
- Planck Collaboration (2020) "Planck 2018 results. VI. Cosmological parameters" A&A 641, A6
- Riess, A. G. et al. (2022) "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team" ApJL 934, L7
- Dodelson, S., Schmidt, F. (2020) "Modern Cosmology" (2nd ed.) Academic Press
