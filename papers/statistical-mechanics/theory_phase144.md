# Phase 144: 量子統計力学 — Fermi-Dirac + Bose-Einstein + BEC + 超流動

> **Tier 1 #21 Statistical Mechanics — Phase 2/8 (Block A paper 5/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 144 の目的

Phase 143 で古典統計力学を扱った。Phase 144 では **量子統計** に進む:

1. **Fermi-Dirac 統計 (1926)**: half-integer spin 粒子
2. **Bose-Einstein 統計 (1924)**: integer spin 粒子
3. **Bose-Einstein Condensation (BEC, 1925/1995, Nobel 2001)**
4. **Fermi 縮退**: electron gas, white dwarf, neutron star
5. **超流動 (He-4 superfluidity)**
6. **ITU 視点**: 量子統計 = K_stat の **identical particle constraint**

中心テーゼ:

> **量子統計 = ITU K_stat 内 identical particle exchange symmetry の帰結**。
> Fermi-Dirac: 反対称化 → Pauli exclusion → white dwarf 安定。
> Bose-Einstein: 対称化 → BEC → 超流動。
> Spin-statistics theorem (Pauli 1940) = ITU の **K_quantum + Lorentz 不変性の帰結**。

---

## 1. Fermi-Dirac 統計 (1926)

### 1.1 分布関数

```
n_FD(ε) = 1 / [exp((ε - μ) / k_B T) + 1]
```

- μ: chemical potential
- 0 ≤ n_FD ≤ 1 (**Pauli exclusion**)

### 1.2 T = 0 limit

```
n_FD(ε) = 1 if ε < ε_F (Fermi energy)
        = 0 if ε > ε_F
```

Step function (Fermi surface)。

### 1.3 Fermi 縮退

電子気体 in 金属:
- ε_F ≈ 5 eV (Cu, Ag)
- T_F = ε_F / k_B ≈ 80,000 K
- 室温では **完全に縮退** (T << T_F)

### 1.4 ITU 視点

```
K_FD = ITU K-state with anti-symmetrized N-body wavefunction
n_FD = K_stat thermal distribution under Pauli exclusion
```

---

## 2. Bose-Einstein 統計 (1924)

### 2.1 分布関数

```
n_BE(ε) = 1 / [exp((ε - μ) / k_B T) - 1]
```

- 0 ≤ n_BE < ∞ (**Pauli exclusion なし**)
- μ ≤ 0 (E_min から測定)

### 2.2 高温極限

n_BE → n_MB (Maxwell-Boltzmann) at T >> T_BEC。

### 2.3 ITU 視点

```
K_BE = ITU K-state with symmetrized N-body wavefunction
n_BE = K_stat thermal distribution allowing multiple occupation
```

---

## 3. ★ Bose-Einstein Condensation (BEC) ★

### 3.1 Einstein 1925 予言

T < T_BEC で **macroscopic number of bosons が ground state を占有**:

```
n_0 / N = 1 - (T / T_BEC)^{3/2}  (3D)
```

### 3.2 臨界温度

```
T_BEC = (h² / (2π m k_B)) × (n / ζ(3/2))^{2/3}
ζ(3/2) ≈ 2.612
```

### 3.3 観測 (1995, Cornell-Wieman-Ketterle, Nobel 2001)

- ⁸⁷Rb cloud (10⁴ atoms, T = 170 nK)
- T_BEC ≈ 170 nK
- Direct observation of momentum distribution narrowing

### 3.4 数値例 (Rb-87)

```
n = 10²⁰ /m³
m = 87 × 1.66e-27 kg = 1.44e-25 kg
T_BEC ≈ 1.7 × 10⁻⁷ K = 170 nK ✓
```

### 3.5 ITU 視点

BEC = **macroscopic quantum coherence**:
- K_BE が ground state K-mode に集中
- δS = δ⟨K⟩ の **macroscopic dominance**

---

## 4. Fermi 縮退と天体物理

### 4.1 White Dwarf (Chandrasekhar 1931, Nobel 1983)

電子 degeneracy pressure が gravity を支える:

```
P_deg ≈ (ℏ²/m_e) × n^{5/3}  (non-relativistic)
```

質量上限 (Chandrasekhar limit):
```
M_Ch ≈ 1.4 M_⊙
```

M > M_Ch では neutron star or BH へ崩壊。

### 4.2 Neutron Star

中性子 degeneracy pressure。

```
M_NS ~ 1.4-2.5 M_⊙
R_NS ~ 10 km
ρ_NS ~ 10¹⁷ kg/m³
```

Tolman-Oppenheimer-Volkoff (TOV) limit:
```
M_TOV ~ 2.0-2.5 M_⊙
```

M > M_TOV で BH (Phase 119 参照)。

### 4.3 ITU 視点

Degeneracy pressure = **K_FD の Pauli exclusion** に由来する macroscopic force。

---

## 5. 超流動 (Helium-4 Superfluidity)

### 5.1 観測 (Kapitza, Allen-Misener 1937-38, Nobel 1978)

He-4 (boson, ⁴He) は T < T_λ = 2.17 K で:
- 粘性 ゼロ
- thermal conductivity 無限大
- 容器壁を **登る** (Rollin film)

### 5.2 Landau (1941) 理論

```
v < v_c (critical velocity) で flow が dissipation なし
```

⇒ superfluid フェーズ確立。

### 5.3 ⁴He vs ³He

| 同位体 | spin | 性質 |
|---|---|---|
| **⁴He** (boson) | 0 | superfluid at T < 2.17 K |
| **³He** (fermion) | 1/2 | superfluid at T < 2.5 mK (Cooper pair 機構) |

### 5.4 ITU 視点

```
Superfluidity = K_BE macroscopic coherence
3-He: K_FD Cooper pairing (BCS-like)
```

---

## 6. Spin-Statistics Theorem (Pauli 1940)

### 6.1 主張

```
Half-integer spin → Fermi-Dirac
Integer spin → Bose-Einstein
```

### 6.2 Pauli の証明

Quantum field theory + relativistic causality → spin と statistics の必然的対応。

### 6.3 ITU 視点

```
K_quantum field theory + K_Lorentz invariance → 
   spin-statistics relation
```

= ITU 公理 + Lorentz symmetry の自然な帰結。

---

## 7. 量子 vs 古典 統計の遷移

### 7.1 De Broglie 波長

```
λ_dB = h / √(2π m k_B T)
```

### 7.2 量子化条件

```
n × λ_dB³ ≳ 1  (量子効果重要)
n × λ_dB³ << 1  (古典 MB OK)
```

### 7.3 数値例

| 系 | T | n (/m³) | λ_dB | n λ_dB³ | Statistics |
|---|---|---|---|---|---|
| Air (N₂) | 300 K | 2.5e25 | 2e-11 m | 2e-7 | classical MB |
| Cu electron | 300 K | 8.5e28 | 4e-9 m | 6 | **FD (degenerate)** |
| Rb cold | 170 nK | 10²⁰ | 1e-6 m | 100 | **BE (BEC)** |
| Sun core | 1.5e7 K | --- | --- | --- | classical MB |

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Fermi-Dirac vs Bose-Einstein vs Maxwell-Boltzmann** distributions
2. **Fermi energy ε_F** for Cu electron gas
3. **BEC critical temperature T_BEC** for Rb-87
4. **Chandrasekhar mass M_Ch ≈ 1.4 M_⊙**
5. **Degeneracy parameter n λ_dB³** for various systems

---

## 9. Phase 144 主結論

1. **Fermi-Dirac (1926)**: n_FD ≤ 1, Pauli exclusion
2. **Bose-Einstein (1924)**: n_BE unbounded, ground state condensation
3. **BEC (1925 predicted, 1995 observed, Nobel 2001)**: T_BEC ~ nK for Rb-87
4. **Fermi 縮退**: electron gas (5 eV), white dwarf (Chandrasekhar 1.4 M_⊙)
5. **超流動**: He-4 boson (2.17 K), He-3 fermion (Cooper, 2.5 mK)
6. **Spin-statistics theorem (Pauli 1940)**: 必然的対応
7. **ITU**: 量子統計 = K_stat + identical particle symmetry
8. **次の Phase 145** で **相転移 + 臨界現象 + universality**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Fermi-Dirac | K_FD anti-symmetric N-body |
| Bose-Einstein | K_BE symmetric N-body |
| BEC | K_BE macroscopic ground state |
| Fermi 縮退 | K_FD Pauli pressure |
| Chandrasekhar limit | K_FD gravitational saturation |
| 超流動 | K_quantum macroscopic coherence |
| Spin-statistics | ITU + Lorentz inv 帰結 |

---

## 引用

```
Terada, M. (2026). Phase 144: Quantum statistics — Fermi-Dirac, Bose-Einstein,
BEC, superfluidity in ITU (Tier 1 #21 phase 2/8). Zenodo. DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

主要参考文献:
- Bose, S. N. (1924) "Plancks Gesetz und Lichtquantenhypothese" Z. Phys. 26, 178
- Einstein, A. (1924, 1925) "Quantentheorie des einatomigen idealen Gases" Sitz. Preuß. Akad. Wiss.
- Fermi, E. (1926) "Sulla quantizzazione del gas perfetto monoatomico" Rend. Lincei 3, 145
- Dirac, P. A. M. (1926) "On the theory of quantum mechanics" Proc. Roy. Soc. A 112, 661
- Pauli, W. (1940) "The connection between spin and statistics" Phys. Rev. 58, 716
- Chandrasekhar, S. (1931) "The maximum mass of ideal white dwarfs" ApJ 74, 81
- Anderson, M. H., Ensher, J. R., Matthews, M. R., Wieman, C. E., Cornell, E. A. (1995) "Observation of Bose-Einstein condensation in a dilute atomic vapor" Science 269, 198
- Davis, K. B. et al. (1995) "Bose-Einstein condensation in a gas of sodium atoms" PRL 75, 3969
- Kapitza, P. (1938) "Viscosity of liquid helium below the λ-point" Nature 141, 74
- Allen, J. F., Misener, A. D. (1938) "Flow of liquid helium II" Nature 141, 75
- Landau, L. D. (1941) "The theory of superfluidity of helium II" J. Phys. USSR 5, 71
