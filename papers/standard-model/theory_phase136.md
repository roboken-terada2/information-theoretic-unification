# Phase 136: Fermion 3 世代 + Yukawa 結合 + CKM/PMNS 行列 + K_fermion

> **Tier 1 #20 Standard Model — Phase 2/8 (Block A paper 4/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 136 の目的

Phase 135 で SM の **gauge 構造** (12 boson) を扱った。Phase 136 では **fermion 内容**を扱う:

1. **3 世代の quark + lepton** (12 fermion fields)
2. **Left-handed doublet vs Right-handed singlet** 構造
3. **Yukawa 結合 → fermion 質量** (11 桁の階層)
4. **CKM 行列** (Cabibbo-Kobayashi-Maskawa 1973, Nobel 2008)
5. **PMNS 行列** (neutrino mixing)
6. **3 世代問題** (なぜ 3?)
7. **ITU 視点**: K_fermion structure

中心テーゼ:

> **3 世代 fermion = ITU K_fermion の 3-fold repetition**。
> Yukawa 質量階層 (11 桁) = K-flow の **scale separation** signature。
> CKM/PMNS mixing 行列 = K-state basis rotation の幾何的記述。
> 3 世代の起源は ITU の **K-state topological constraint** (anomaly cancellation) で部分説明。

---

## 1. 3 世代の Fermion

### 1.1 構造

各世代に 4 つの fermion (quark u-type, d-type + lepton charged, neutrino):

| 世代 | u-quark | d-quark | charged lepton | neutrino |
|---|---|---|---|---|
| 1 | u (2.16 MeV) | d (4.67 MeV) | e (0.511 MeV) | ν_e (< 1 eV) |
| 2 | c (1.27 GeV) | s (93 MeV) | μ (105.66 MeV) | ν_μ (< 1 eV) |
| 3 | t (172.5 GeV) | b (4.18 GeV) | τ (1776.86 MeV) | ν_τ (< 1 eV) |

**12 fermion fields × 各 3 colors (quark) + 1 (lepton)** = 全 fermion field 数 = 多数。

### 1.2 Left/Right Chirality

**Left-handed**: SU(2)_L doublet で参加

```
L_L = (ν_L, e_L)^T,  Q_L = (u_L, d_L)^T
```

**Right-handed**: SU(2) singlet

```
e_R, u_R, d_R  (ν_R は SM に含まれない)
```

### 1.3 Hypercharge 割り当て

電弱統一の整合性条件:

| Field | T_3 | Y | Q = T_3 + Y/2 |
|---|---|---|---|
| ν_L | +1/2 | -1 | 0 |
| e_L | -1/2 | -1 | -1 |
| u_L | +1/2 | +1/3 | +2/3 |
| d_L | -1/2 | +1/3 | -1/3 |
| e_R | 0 | -2 | -1 |
| u_R | 0 | +4/3 | +2/3 |
| d_R | 0 | -2/3 | -1/3 |

---

## 2. Yukawa Coupling

### 2.1 Lagrangian

```
L_Yukawa = -y_e (L_L H) e_R - y_d (Q_L H) d_R - y_u (Q_L H̃) u_R + h.c.
```

H = Higgs doublet, H̃ = i σ_2 H*。

### 2.2 EWSB 後の質量

```
m_f = y_f × v / √2
```

v = 246 GeV (Higgs VEV)。

### 2.3 Yukawa coupling 値

| Fermion | m_f (GeV) | y_f = m_f √2 / v |
|---|---|---|
| Electron | 5.11e-4 | 2.94e-6 |
| Up | 2.16e-3 | 1.24e-5 |
| Down | 4.67e-3 | 2.68e-5 |
| Strange | 9.3e-2 | 5.34e-4 |
| Charm | 1.27 | 7.30e-3 |
| Muon | 0.106 | 6.08e-4 |
| Bottom | 4.18 | 2.40e-2 |
| Tau | 1.777 | 1.02e-2 |
| **Top** | **172.5** | **0.991** ≈ 1 ★ |

⇒ **Top quark Yukawa ≈ 1** = O(1) coupling。他は遥かに小さい。

---

## 3. 質量階層 (Mass Hierarchy)

### 3.1 数値

```
m_t / m_e = 172.5 / 5.11e-4 ≈ 3.4 × 10⁵
m_t / m_u = 172.5 / 2.16e-3 ≈ 8 × 10⁴
```

⇒ Standard Model 内の **11 桁の質量階層** (t: 10² GeV → ν: 10⁻¹⁰ GeV)。

### 3.2 起源問題

なぜこの階層? Possible answers:
- **Anthropic principle**: 我々が存在可能な配置
- **Frogatt-Nielsen mechanism**: U(1) horizontal symmetry
- **String landscape**: 各 vacuum で異なる Yukawa
- **GUT relations**: SU(5)/SO(10) で部分予言

### 3.3 ITU 視点

```
y_f ∝ |⟨0|K_fermion|f⟩|²
```

Yukawa 結合の **指数的階層** = K-state scale separation:

```
y_t ~ O(1)
y_b ~ O(0.01)
y_τ ~ O(0.01)
y_u, y_d, y_e ~ O(10⁻⁵)
y_ν ~ O(10⁻¹²)
```

⇒ 6 オーダーの階層 = ITU の **K-flow scale separation signature**。

---

## 4. CKM 行列 (Cabibbo 1963, Kobayashi-Maskawa 1973, Nobel 2008)

### 4.1 構造

quark の weak interaction では **質量固有状態と弱固有状態が異なる**:

```
V_CKM = | V_ud  V_us  V_ub |
        | V_cd  V_cs  V_cb |
        | V_td  V_ts  V_tb |
```

### 4.2 Wolfenstein parameterization

```
V_CKM ≈ | 1 - λ²/2    λ           A λ³ (ρ - iη) |
        | -λ          1 - λ²/2    A λ²          |
        | A λ³ (1-ρ-iη)  -A λ²    1             |
```

PDG 2024 値:
- λ ≈ **0.2253** (Cabibbo angle ≈ 13°)
- A ≈ 0.832
- ρ̄ ≈ 0.159
- η̄ ≈ 0.348

### 4.3 CP 違反

CKM 行列の **complex phase η** が CP 違反を生む。
KM 1973 が予言 → 1999 BaBar/Belle で確認 → **Nobel 2008**。

### 4.4 ITU 視点

CKM mixing = **K_quark basis rotation**。

---

## 5. PMNS 行列 (Neutrino Mixing)

### 5.1 提案 (Pontecorvo-Maki-Nakagawa-Sakata 1957, 1962)

```
V_PMNS = | U_e1  U_e2  U_e3 |
         | U_μ1  U_μ2  U_μ3 |
         | U_τ1  U_τ2  U_τ3 |
```

### 5.2 観測値 (NuFIT 2024)

```
θ_12 ≈ 33.4°  (solar)
θ_23 ≈ 49°    (atmospheric)
θ_13 ≈ 8.6°   (reactor, Daya Bay 2012)
```

CKM 比 **遥かに大きい mixing** (Cabibbo angle 13° vs solar 33°)。

### 5.3 Neutrino 質量

- m_ν < 0.8 eV (KATRIN 2022, β decay)
- Σ m_ν < 0.12 eV (Planck 2018 cosmology)
- Δm²_21 = 7.4 × 10⁻⁵ eV², |Δm²_31| = 2.5 × 10⁻³ eV²

順序 (normal vs inverted) は未確定。

### 5.4 ITU 視点

PMNS mixing 大 = **K_neutrino が他 K_fermion から大きく逸脱**。
neutrino mass の起源 (Dirac vs Majorana) は未解明 → Pass-2 priority。

---

## 6. 3 世代の起源問題

### 6.1 観測上の事実

LEP precision (1989-2000): **light neutrino flavor 数 = 3**:

```
N_ν = 2.9963 ± 0.0074
```

⇒ Standard Model fermion は **正確に 3 世代**。

### 6.2 理論候補

- **Anthropic**: 1-2 世代で複雑性発生せず
- **GUT**: SO(10) で 16-spinor が 1 世代を含む
- **String compactification**: CY 多様体の Euler characteristic
- **Generation number = topology**

### 6.3 ITU 視点

ITU の **K_fermion topological constraint**:

```
∑ Y³ = 0  (anomaly cancellation)
```

これは **3 世代で自然解決** (Quigg, Glashow 1990)。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **3 世代 fermion 質量**プロット (11 桁の階層)
2. **Yukawa 結合 y_f**: top で ~1, 他は << 1
3. **CKM 行列**の数値
4. **PMNS 角度**: θ_12, θ_23, θ_13
5. **Mass hierarchy ratio**: m_t/m_e ≈ 3.4×10⁵

---

## 8. Phase 136 主結論

1. **3 世代 fermion**: 6 quark + 6 lepton
2. **Left-handed doublet + Right-handed singlet** 構造
3. **Yukawa 階層**: top y ≈ 1, electron y ≈ 3e-6 (5 桁差)
4. **質量階層**: m_t/m_ν ≈ 10¹¹
5. **CKM 行列**: Cabibbo angle 13°, KM CP violation
6. **PMNS 行列**: solar 33°, atmospheric 49° (CKM より大)
7. **N_ν = 3** (LEP 観測)
8. **ITU**: K_fermion = 3-fold repetition, anomaly cancellation
9. **次の Phase 137** で **Higgs mechanism + 電弱対称性破れ**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| 3 世代 | K_fermion 3-fold repetition |
| Yukawa coupling | K_fermion-K_Higgs interaction |
| 質量階層 11 桁 | K-flow scale separation |
| CKM 行列 | K_quark basis rotation |
| PMNS 行列 | K_neutrino basis rotation |
| Anomaly cancellation | K-state topological constraint |

---

## 引用

```
Terada, M. (2026). Phase 136: SM fermion content, 3 generations, Yukawa
couplings, and CKM/PMNS in ITU (Tier 1 #20 phase 2/8). Zenodo. DOI:
[to be assigned].
```

主要参考文献:
- Cabibbo, N. (1963) "Unitary symmetry and leptonic decays" PRL 10, 531
- Kobayashi, M., Maskawa, T. (1973) "CP-violation in the renormalizable theory of weak interaction" Prog. Theor. Phys. 49, 652
- Pontecorvo, B. (1957) "Mesonium and antimesonium" Soviet Physics JETP 6, 429
- Maki, Z., Nakagawa, M., Sakata, S. (1962) "Remarks on the unified model of elementary particles" Prog. Theor. Phys. 28, 870
- ALEPH Collaboration et al. (2006) "Precision electroweak measurements on the Z resonance" Phys. Rept. 427, 257
- KATRIN Collaboration (2022) "Direct neutrino-mass measurement with sub-electronvolt sensitivity" Nature Phys. 18, 160
- Daya Bay Collaboration (2012) "Observation of electron-antineutrino disappearance at Daya Bay" PRL 108, 171803
- Quigg, C., Glashow, S. L. (1990) "Beyond the Standard Model" Springer
- Particle Data Group (2024) "Review of Particle Physics" PRD 110, 030001
- Esteban, I. et al. (2024) "NuFIT 5.3: three-flavour neutrino oscillation parameters"
