# Phase 152: Band Theory + Drude-Sommerfeld + 半導体物理

> **Tier 1 #22 Condensed Matter Physics — Phase 2/8 (Block A paper 6/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 152 の目的

Phase 151 で Bloch + 自由電子気体 + Phonon 基礎を据えた。Phase 152 では **band theory** + **半導体物理** へ進む:

1. **Tight-binding model** (1929 Bloch / 1954 Slater-Koster)
2. **Nearly free electron model** (NFE) — band gap 形成
3. **Density of states** (DOS) D(ε)
4. **半導体物理**: Si, GaAs, Ge — intrinsic + extrinsic carriers
5. **p-n junction** + Shockley diode 方程式
6. **ITU 視点**: K_band = K_solid の k-space 投影

中心テーゼ:

> **半導体 = K_band の Fermi level chemical potential 操作**。
> Doping = K_band の chemical-potential injection。
> p-n junction = K_band の境界 K-flow。

---

## 1. ★ Tight-Binding Model ★

### 1.1 1D 線形鎖 (s-band)

```
E(k) = ε_0 - 2 t cos(k a)
```

- ε_0: on-site energy
- t: hopping integral (transfer)
- a: lattice constant

帯幅: **W = 4 t**

### 1.2 2D 正方格子

```
E(k_x, k_y) = ε_0 - 2 t (cos k_x a + cos k_y a)
```

帯幅: W = 8 t。

### 1.3 3D 立方格子

```
E(k) = ε_0 - 2 t Σ_i cos(k_i a)
W = 12 t
```

### 1.4 数値例 (Si 価電子帯)

```
W_valence ≈ 12 eV → t_eff ≈ 1 eV
```

### 1.5 ITU 視点

```
TB = K_solid の effective lattice Hamiltonian
hopping t = K-state inter-site transfer amplitude
```

---

## 2. ★ Nearly Free Electron Model (NFE) ★

### 2.1 Schrödinger 方程式

```
[-ℏ²/2m ∇² + V(r)] ψ = E ψ
V(r) = Σ_G V_G e^{iG·r}   (Fourier expansion on reciprocal lattice)
```

### 2.2 Band gap 形成 (Bragg 条件)

```
k = G/2 (Brillouin zone boundary)
ΔE_gap = 2|V_G|
```

= 周期 ポテンシャル の **Fourier 成分** が gap を作る。

### 2.3 1D 数値例

```
V(x) = -V_0 cos(2π x / a)
1st band: E(k) ≈ ℏ²k²/(2m) - corrections
1st gap at k = π/a: ΔE = V_0
```

### 2.4 ITU 視点

```
NFE band gap = K_band の Bragg-reflection forbidden region
Periodic V = K-state forced 等価分解
```

---

## 3. ★ Density of States (DOS) ★

### 3.1 3D 自由電子

```
D(ε) = (1/2π²) (2m/ℏ²)^{3/2} √ε
```

(per volume, per spin)。

### 3.2 数値: Cu @ ε_F

```
D(ε_F) ≈ 1.5×10²⁸ /(m³·eV)
```

### 3.3 帯端の特異性

3D: D(ε) ∝ √ε (band edge)
2D: D(ε) = const (step)
1D: D(ε) ∝ 1/√ε (van Hove singularity)

### 3.4 ITU 視点

```
DOS = K_band 位相空間の volume measure
帯端 = K_band 境界の dimensional anomaly
```

---

## 4. ★ 半導体物理 ★

### 4.1 主要半導体

| 物質 | E_g (eV) | type | m_e*/m_e | m_h*/m_e |
|---|---|---|---|---|
| **Si** | 1.12 (300K) | indirect | 1.08 | 0.81 |
| **Ge** | 0.66 | indirect | 0.55 | 0.37 |
| **GaAs** | 1.42 | direct | 0.067 | 0.45 |
| **InP** | 1.34 | direct | 0.077 | 0.6 |
| **SiC (4H)** | 3.23 | indirect | 0.66 | 1.0 |
| **GaN** | 3.4 | direct | 0.20 | 0.8 |
| **Diamond** | 5.5 | indirect | 0.57 | 0.8 |

### 4.2 Intrinsic carrier 密度

```
n_i = √(N_c N_v) exp(-E_g / 2 k_B T)
N_c = 2 (2π m_e* k_B T / h²)^{3/2}
N_v = 2 (2π m_h* k_B T / h²)^{3/2}
```

### 4.3 数値: Si @ 300 K

```
N_c = 2.82×10¹⁹ /cm³
N_v = 1.83×10¹⁹ /cm³
n_i = 9.65×10⁹ /cm³  (実測 ~10¹⁰)
```

### 4.4 Doping (n型 vs p型)

```
n型: donor (P in Si) → 余剰電子
p型: acceptor (B in Si) → 余剰 hole
電気中性: n = p + N_D⁺ - N_A⁻
```

### 4.5 ITU 視点

```
半導体 = K_band の partial occupation (Fermi level in gap)
Doping = K_chemical-potential injection
Direct/indirect gap = K_band の k-momentum 一致/不一致
```

---

## 5. ★ p-n 接合 + Shockley diode 方程式 ★

### 5.1 平衡 built-in potential

```
V_bi = (k_B T / e) ln(N_A N_D / n_i²)
```

### 5.2 数値: Si p-n junction @ 300 K

```
N_A = N_D = 10¹⁷ /cm³, n_i = 10¹⁰ /cm³
V_bi = 0.0259 × ln(10³⁴ / 10²⁰) = 0.0259 × 32.2 = 0.83 V  ✓
```

### 5.3 Shockley diode 方程式 (1949)

```
I = I_s (e^{eV / k_B T} - 1)
```

- I_s: saturation current (typ. 10⁻¹² - 10⁻⁹ A)
- V: applied bias
- 0.0259 V = k_B T / e @ 300 K = **thermal voltage** V_T

### 5.4 ITU 視点

```
p-n junction = K_band の境界 K-flow
Shockley = K_chemical-potential gradient → K_current
Forward bias = K_chemical-potential injection
```

---

## 6. Hall effect (古典)

### 6.1 Hall coefficient

```
R_H = 1 / (n e)   (for electrons; sign + for holes)
```

### 6.2 数値: Cu @ 300 K

```
n = 8.5e28 /m³
R_H = -7.35×10⁻¹¹ m³/C  (negative → electron carrier ✓)
```

### 6.3 数値: Si (n-doped, N_D=10²² /m³)

```
R_H = -6.25×10⁻⁴ m³/C (1万倍大きい — low carrier density)
```

### 6.4 ITU 視点

```
Hall = K_band carrier 同定 (sign + density)
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **1D tight-binding** E(k) = ε_0 - 2t cos(ka) 帯構造
2. **NFE band gap** at BZ boundary
3. **DOS** 3D 自由電子 D(ε) ∝ √ε
4. **Si n_i** @ 300 K = 9.65×10⁹ /cm³
5. **Si p-n V_bi** = 0.83 V
6. **Shockley diode** I-V 曲線
7. **Hall coefficient** Cu vs Si

---

## 8. Phase 152 主結論

1. **Tight-binding (1929)**: E = ε_0 - 2t cos(ka), 帯幅 W = 2z·t
2. **NFE**: band gap = 2|V_G| at BZ boundary (Bragg)
3. **DOS** 3D 自由電子: D(ε) ∝ √ε
4. **Si E_g = 1.12 eV (indirect)**, GaAs 1.42 eV (direct)
5. **Si n_i @ 300K** = 10¹⁰ /cm³
6. **Shockley diode** I = I_s (e^{eV/k_BT} - 1)
7. **ITU**: K_band = K_solid k-space spectrum, doping = K_μ injection
8. **次の Phase 153** で **超伝導 BCS + Meissner + 高温 SC**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Tight-binding | K_solid effective lattice Hamiltonian |
| NFE | K_band Bragg-gap structure |
| DOS | K_band volume measure |
| 半導体 | K_band partial Fermi level |
| Doping | K_μ chemical-potential injection |
| p-n junction | K_band boundary K-flow |
| Shockley | K_chemical-current relation |
| Hall | K_band carrier identification |

---

## 引用

```
Terada, M. (2026). Phase 152: Band theory, Drude-Sommerfeld synthesis, and
semiconductor physics in ITU (Tier 1 #22 phase 2/8). Zenodo. DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

主要参考文献:
- Bloch, F. (1929) "Über die Quantenmechanik der Elektronen in Kristallgittern" Z. Phys. 52, 555
- Slater, J. C., Koster, G. F. (1954) "Simplified LCAO method for the periodic potential problem" Phys. Rev. 94, 1498
- Shockley, W. (1949) "The theory of p-n junctions in semiconductors" Bell Syst. Tech. J. 28, 435
- Bardeen, J., Brattain, W. H. (1948) "The transistor, a semi-conductor triode" Phys. Rev. 74, 230
- Shockley, W. (1950) Electrons and Holes in Semiconductors. Van Nostrand.
- Sze, S. M., Ng, K. K. (2007) Physics of Semiconductor Devices, 3rd ed. Wiley.
- Madelung, O. (2004) Semiconductors: Data Handbook, 3rd ed. Springer.
- Hall, E. H. (1879) "On a new action of the magnet on electric currents" Am. J. Math. 2, 287
