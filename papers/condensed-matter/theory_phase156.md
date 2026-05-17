# Phase 156: 強相関電子系 — 高温 SC 機構 + Kondo + スピン液体 + Fractionalization + K_correlation

> **Tier 1 #22 Condensed Matter Physics — Phase 6/8 (Block A paper 6/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 156 の目的

Phase 153 (BCS) + Phase 154 (Hubbard/Mott) + Phase 155 (topology) を統合する **強相関電子系** へ進む:

1. **Kondo 効果** + 重い電子系 (heavy fermion)
2. **高温超伝導 (HTS) 機構** — cuprate d-wave + 鉄系 s±
3. **擬ギャップ (pseudogap)** + Fermi 弧
4. **量子臨界点 + non-Fermi liquid**
5. **Anderson RVB + スピン液体**
6. **Fractionalization** — spinon, holon
7. **ITU 視点**: K_correlation = K_band + 相互作用 + 非自明 ground state

中心テーゼ:

> **強相関電子系 = K_band と K_correlation の競合**。
> 高温 SC = K_Mott にホール注入 → K_d-wave-SC。
> スピン液体 = K_spin の topological GS (Anderson RVB)。
> Fractionalization = K_electron が複数の elementary excitation に分解。

---

## 1. ★ Kondo 効果 + 重い電子系 ★

### 1.1 Kondo 問題 (1964)

希薄磁性不純物 (Fe in Cu, Ce in LaAl₂) の低温電気抵抗:

```
ρ(T) ∝ -log T   (T → 0)
```

= 磁性 unique 散乱 (Anderson 1961, Kondo 1964)。

### 1.2 Kondo 温度

```
T_K ≈ D exp(-1 / N(0) |J|)
```

D = bandwidth, J = exchange coupling。

### 1.3 数値例

| 物質 | T_K (K) |
|---|---|
| Fe in Cu | ~1 |
| Mn in Cu | ~0.01 |
| Ce in LaAl₂ | 0.5 |
| CeAl₃ (heavy fermion) | 5 |

### 1.4 ★ Heavy fermion (重い電子) ★

T < T_K で **電子有効質量 m* が大幅増大**:

```
m* / m_e = 10² - 10³
γ (Sommerfeld) ~ 10² - 10³ × normal
```

| 物質 | γ (mJ/mol K²) | m*/m_e |
|---|---|---|
| Cu (normal) | 0.69 | 1 |
| CeCu₂Si₂ | 1100 | ~800 |
| UPt₃ | 420 | ~300 |
| CeAl₃ | 1620 | ~1000 |

### 1.5 ITU 視点

```
Kondo = K_spin × K_FD hybridization
Heavy fermion = K_FD の renormalized quasi-particle
m*/m_e = K_correlation の renormalization 強度
```

---

## 2. ★ 高温超伝導 (HTS) 機構 ★

### 2.1 Cuprate phase diagram

```
La₂CuO₄ (x=0):        AF Mott insulator
hole doping x = 0.05: superconductor onset
x ≈ 0.16 (optimal):   max T_c ~ 100 K
x = 0.27:             overdoped Fermi liquid
```

### 2.2 ★ d-wave pairing ★

BCS gap が k-依存:

```
Δ(k) = Δ_0 [cos(k_x a) - cos(k_y a)]  /  2
```

- **node** at k_x = ±k_y (gap = 0)
- **anti-node** at k = (π, 0) (gap max)

実験検証: ARPES, phase-sensitive (Tsuei-Kirtley π-junction)。

### 2.3 鉄系 s± pairing

鉄系 SC (LaFeAsO, Ba(FeAs)₂):

```
Δ(k) on hole pocket > 0
Δ(k) on electron pocket < 0
(sign-changing s-wave)
```

### 2.4 機構候補

| 機構 | 候補物質 |
|---|---|
| Phonon | 通常 BCS, MgB₂, H₃S, LaH₁₀ |
| Spin fluctuation | cuprate d-wave, 鉄系 s± |
| Charge fluctuation | Bi-based |
| Loop currents | cuprate (Varma) |
| RVB | Anderson cuprate proposal |

### 2.5 ITU 視点

```
HTS d-wave = K_correlation × K_topo (node 構造)
HTS = K_band × K_AF spin fluctuation 結合
```

---

## 3. ★ 擬ギャップ (Pseudogap) ★

### 3.1 観測

Cuprate underdoped 領域 (T_c < T < T*):
- Spectroscopy で **gap-like feature** at anti-node
- Node 付近は arc (Fermi arc) として gapless

### 3.2 T* (擬ギャップ温度)

```
T* ~ 200-300 K (underdoped)
```

T_c (90 K) より高温で発現。

### 3.3 解釈候補

- preformed Cooper pair (BEC-BCS crossover)
- competing order (CDW, SDW, nematicity)
- Anderson RVB short-range singlet

### 3.4 ITU 視点

```
Pseudogap = K_SC の K_AF-correlation precursor
Fermi arc = K_band の partial Fermi surface
```

---

## 4. ★ 量子臨界点 + non-Fermi liquid ★

### 4.1 Quantum critical point (QCP)

T = 0 で連続相転移 (quantum phase transition):

```
g_c: tuning parameter (pressure, doping, magnetic field)
QCP at (T=0, g=g_c)
```

### 4.2 Non-Fermi liquid (NFL)

QCP 近傍で異常な低 T 挙動:

```
ρ(T) ∝ T^α   (α ≠ 2)  ← 標準 Fermi liquid は α = 2
C/T ∝ -log T
χ(T) ∝ T^{-γ}
```

### 4.3 物質例

| 系 | ρ(T) | comment |
|---|---|---|
| Standard Fermi liquid | T² | normal metal |
| Cuprate optimally doped | **T** (linear) | strange metal |
| Iron pnictide near QCP | T | NFL |
| YbRh₂Si₂ | T | heavy fermion QCP |

### 4.4 ITU 視点

```
QCP = K_stat の T=0 critical point (Phase 145 拡張)
NFL = K_correlation の non-trivial RG fixed point
strange metal = K_FD universality 破れ
```

---

## 5. ★ Spin Liquid + Anderson RVB ★

### 5.1 Anderson RVB (1973)

Triangular AF Heisenberg ground state:
```
|RVB⟩ = Σ valence-bond covering
```
= 非磁性, 量子 superposition of singlet pairs。

### 5.2 RVB → HTS 提案 (Anderson 1987)

```
親物質 (Mott AF) = RVB-like
doping → spinon-holon
Cooper pair = spinon-spinon pairing
→ HTS
```

### 5.3 候補 spin liquid 物質

| 物質 | type | T_low (K) |
|---|---|---|
| Herbertsmithite ZnCu₃(OH)₆Cl₂ | kagome | < 0.05 |
| κ-(BEDT-TTF)₂Cu₂(CN)₃ | triangular organic | spin liquid |
| YbMgGaO₄ | triangular | mK |
| α-RuCl₃ | Kitaev (perturbed) | ~7 |

### 5.4 ITU 視点

```
RVB = K_spin の topologically-ordered ground state
Anderson 提案 = K_Mott × K_doping → K_HTS via K_RVB
```

---

## 6. ★ Fractionalization ★

### 6.1 概念

通常: electron = (charge -e, spin 1/2)
強相関で:
```
electron → spinon (charge 0, spin 1/2) + holon (charge -e, spin 0)
```

= **電子の準粒子的分解**。

### 6.2 観測例

| 系 | fractional excitation |
|---|---|
| FQHE ν=1/3 | quasi-particle charge e/3 (Laughlin) |
| 1D spin chain | spinon (Bethe ansatz) |
| Kitaev 模型 | Majorana fermion |
| ν=5/2 FQHE | non-abelian anyon (候補) |

### 6.3 ITU 視点

```
Fractionalization = K_electron が複数の K_emergent に分解
spinon, holon = K_correlation の elementary excitation
```

---

## 7. Twisted Bilayer Graphene (Magic Angle, 2018)

### 7.1 観測 (Cao et al. Nature 2018)

二層 graphene を ~1.1° 捻る → flat band → superconductivity (T_c = 1.7 K) + Mott-like 絶縁体。

### 7.2 ITU 視点

```
Moiré superlattice = K_band の effective bandwidth 制御
Flat band = K_correlation U/W → ∞ 模擬可能
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Kondo log T** 抵抗
2. **Heavy fermion γ** 比較 (Cu vs CeCu₂Si₂ vs UPt₃)
3. **d-wave gap** Δ(k) = Δ_0 (cos k_x - cos k_y)/2
4. **Cuprate phase diagram** (x vs T)
5. **Linear-T resistivity** (strange metal)
6. **Anderson RVB** singlet superposition simple example
7. **ν=1/3 fractional charge** (Phase 155 再掲)

---

## 9. Phase 156 主結論

1. **Kondo (1964)**: ρ ∝ -log T, T_K で局所モーメント screening
2. **Heavy fermion**: m*/m_e ~ 10²-10³ (CeCu₂Si₂, UPt₃)
3. **HTS d-wave (cuprate)**: Δ(k) = Δ_0(cos k_x - cos k_y)/2, node あり
4. **HTS s± (鉄系)**: sign-changing pocket structure
5. **Pseudogap**: T* > T_c, Fermi arc
6. **Strange metal**: linear-T resistivity (quantum critical)
7. **RVB (Anderson 1973, 1987)**: spinon-holon HTS proposal
8. **Spin liquid**: Herbertsmithite, organics, YbMgGaO₄
9. **Fractionalization**: spinon, holon, FQHE e/3, Majorana
10. **Magic-angle graphene (2018)**: moiré flat band → SC
11. **ITU**: K_correlation = K_band + 強相互作用 + 非自明 GS
12. **次の Phase 157** で **ソフトマター + 液晶 + コロイド + 高分子**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Kondo | K_spin × K_FD hybridization |
| Heavy fermion | K_FD renormalized quasi-particle |
| d-wave SC | K_SC × K_topo (node 構造) |
| Pseudogap | K_SC precursor + K_AF |
| Strange metal | K_FD universality 破れ |
| RVB | K_spin topological GS |
| Spinon/holon | K_electron fractionalization |
| Magic-angle graphene | K_moiré flat band |

---

## 引用

```
Terada, M. (2026). Phase 156: Strongly correlated electrons — Kondo, high-Tc
mechanisms, spin liquids, and fractionalization in ITU
(Tier 1 #22 phase 6/8). Zenodo. DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

主要参考文献:
- Kondo, J. (1964) "Resistance minimum in dilute magnetic alloys" Prog. Theor. Phys. 32, 37
- Anderson, P. W. (1961) "Localized magnetic states in metals" Phys. Rev. 124, 41
- Stewart, G. R. (1984) "Heavy-fermion systems" Rev. Mod. Phys. 56, 755
- Anderson, P. W. (1987) "The resonating valence bond state in La2CuO4 and superconductivity" Science 235, 1196
- Tsuei, C. C., Kirtley, J. R. (2000) "Pairing symmetry in cuprate superconductors" Rev. Mod. Phys. 72, 969
- Mazin, I. I., Singh, D. J., Johannes, M. D., Du, M. H. (2008) "Unconventional superconductivity with a sign reversal in the order parameter of LaFeAsO1-xFx" PRL 101, 057003
- Norman, M. R. et al. (1998) "Destruction of the Fermi surface in underdoped high-Tc superconductors" Nature 392, 157 (pseudogap)
- Lohneysen, H. v. et al. (2007) "Fermi-liquid instabilities at magnetic quantum phase transitions" Rev. Mod. Phys. 79, 1015
- Sachdev, S. (2011) Quantum Phase Transitions, 2nd ed. Cambridge UP
- Cao, Y. et al. (2018) "Unconventional superconductivity in magic-angle graphene superlattices" Nature 556, 43
- Han, T. H. et al. (2012) "Fractionalized excitations in the spin-liquid state of a kagome-lattice antiferromagnet" Nature 492, 406
- Mendels, P. et al. (2007) "Quantum magnetism in the paratacamite family" PRL 98, 077204
