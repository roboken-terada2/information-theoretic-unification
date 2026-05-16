# Phase 143: Tier 1 #21 Statistical Mechanics — Boltzmann + Entropy + K_stat 基礎

> **Tier 1 #21: Statistical Mechanics — Phase 1/8 (Block A paper 5/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> Tier 1 #17 (QG): [10.5281/zenodo.20230667](https://doi.org/10.5281/zenodo.20230667)
> Tier 1 #18 (BH): [10.5281/zenodo.20233070](https://doi.org/10.5281/zenodo.20233070)
> Tier 1 #19 (Cosmology): [10.5281/zenodo.20233952](https://doi.org/10.5281/zenodo.20233952)
> Tier 1 #20 (Standard Model): [10.5281/zenodo.20234703](https://doi.org/10.5281/zenodo.20234703)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 143 の目的

Tier 1 #17-#20 (FUNDAMENTAL TRINITY + Standard Model) で物理学の **構成要素**を扱った。
Tier 1 #21 では **統計力学** = 多体系の **集団的振る舞い** を扱う。

Phase 143 (本) で確立する内容:

1. **Boltzmann 統計力学** (1872, 1877)
2. **エントロピー S = k_B ln W** (Boltzmann's epitaph)
3. **Maxwell-Boltzmann 分布** (1860)
4. **Gibbs アンサンブル** (microcanonical, canonical, grand canonical)
5. **ITU 公理写像**: K_stat = statistical modular Hamiltonian

中心テーゼ:

> **統計力学 = ITU 公理の多体実現**。
> Boltzmann entropy S = k_B ln W = von Neumann entropy の古典極限。
> Maxwell-Boltzmann 分布 = K_stat の thermal equilibrium 解。
> Statistical mechanics と ITU 公理は **同じ formal structure**。

---

## 1. Boltzmann 統計力学

### 1.1 H-theorem (Boltzmann 1872)

```
H(t) = ∫ f(v, t) ln f(v, t) d³v
dH/dt ≤ 0
```

H = entropy の反対符号。
熱平衡で f = Maxwell-Boltzmann → H 最小。

⇒ **第二法則の力学的根拠** (Loschmidt paradox との議論あり、別途)。

### 1.2 Boltzmann's Equation

```
∂f/∂t + v · ∇_x f + F · ∇_v f = (∂f/∂t)_collision
```

collision integral で粒子間衝突を扱う。

### 1.3 H-theorem の意義

- 微視的に reversible な力学から irreversible な熱力学が emerge
- 統計的議論で **time arrow** が出現
- Quantum: Jaynes 1957 で **maximum entropy principle** に統合

---

## 2. Entropy S = k_B ln W (Boltzmann 1877)

### 2.1 公式

```
S = k_B × ln W
```

- W: microstate 数 (degenerate な複号)
- k_B = 1.381 × 10⁻²³ J/K (Boltzmann 定数)

Boltzmann の墓碑銘 (Vienna)。

### 2.2 数値例

- 単原子理想気体 1 mol @ 標準状態:
  - W ≈ 10^(10^26) (超巨大!)
  - S ≈ 154 J/(mol K)

### 2.3 Gibbs 一般化

```
S = -k_B Σ_i p_i ln p_i
```

- p_i: microstate i の確率
- 等確率 p_i = 1/W → S = k_B ln W (Boltzmann)

### 2.4 ITU 視点

```
S (von Neumann) = -Tr(ρ ln ρ)
S (Gibbs)       = -k_B Σ p_i ln p_i
S (Boltzmann)   = k_B ln W
```

⇒ **3 つは同じ formal structure**。
ITU 公理 δS = δ⟨K⟩ は **古典 + 量子** 統合枠組。

---

## 3. Maxwell-Boltzmann 分布 (1860)

### 3.1 速度分布

```
f(v) = (m / (2π k_B T))^{3/2} × 4π v² × exp(-m v² / (2 k_B T))
```

3D 速度大きさ v の分布。

### 3.2 主要量

- **most probable speed**: v_p = √(2 k_B T / m)
- **mean speed**: ⟨v⟩ = √(8 k_B T / (π m))
- **rms speed**: v_rms = √(3 k_B T / m)

比: v_p : ⟨v⟩ : v_rms ≈ 1 : 1.128 : 1.225。

### 3.3 数値例 (T = 300 K, N_2 gas)

```
v_p ≈ 422 m/s
⟨v⟩ ≈ 476 m/s
v_rms ≈ 517 m/s
```

### 3.4 ITU 視点

```
f_MB(v) = (1/Z) exp(-β E)  (β = 1/k_B T, E = m v²/2)
```

= **K_stat の thermal equilibrium 解**。

---

## 4. Gibbs アンサンブル

### 4.1 3 つの主要アンサンブル

| Ensemble | 拘束条件 | Partition function |
|---|---|---|
| **Microcanonical** | E 固定 | W(E) = # microstates |
| **Canonical** | T 固定 | Z = Σ exp(-β E_i) |
| **Grand canonical** | T, μ 固定 | Ξ = Σ exp(-β(E - μN)) |

### 4.2 自由エネルギー

```
F = -k_B T ln Z         (Helmholtz, canonical)
Ω = -k_B T ln Ξ         (grand canonical)
S = -∂F/∂T              (entropy)
U = -∂ln Z/∂β           (internal energy)
```

### 4.3 ITU 視点

```
ρ = exp(-β K) / Tr(exp(-β K))  (canonical density matrix)
K = β H (β = 1/k_B T で modular Hamiltonian)
S = -Tr(ρ ln ρ) = β ⟨H⟩ - ln Z
```

ITU 公理:
```
δS = δ⟨K⟩
```

= **canonical ensemble の dS = β dE + ...** と整合。

---

## 5. Loschmidt Paradox と Boltzmann 1877

### 5.1 Loschmidt paradox

時間反転対称な microscopic dynamics から、なぜ **irreversibility** が出るか?

### 5.2 Boltzmann 1877 回答

- 微視状態 → 熱平衡 (高 entropy) の方が **圧倒的に多い**
- 時間反転状態の **確率は天文学的に小** (10^(-10^26))
- ⇒ 第二法則は **確率的** 法則

### 5.3 ITU 視点

```
P(low-entropy state) << P(high-entropy state)
S(t+Δt) ≥ S(t) with overwhelming probability
```

= **K-flow の statistical asymmetry**。

---

## 6. ITU 公理と統計力学の対応

| 統計力学 | ITU |
|---|---|
| Boltzmann S = k_B ln W | von Neumann S の古典極限 |
| Gibbs S = -k_B Σ p_i ln p_i | Tr(ρ ln ρ) の古典版 |
| Maxwell-Boltzmann f(v) | K_stat thermal equilibrium |
| Canonical ensemble Z | partition function |
| dS = β dE + ... | δS = δ⟨K⟩ (ITU 公理) |
| Loschmidt paradox | K-flow statistical asymmetry |

⇒ 統計力学全体が **ITU 公理の特殊化** として理解可能。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Maxwell-Boltzmann 分布 f(v)** plot
2. **v_p, ⟨v⟩, v_rms** for T = 300 K, N_2
3. **Boltzmann S = k_B ln W** for ideal gas
4. **Canonical ensemble Z, F, S, U**
5. **Microcanonical vs canonical** equivalence

---

## 8. Phase 143 主結論

1. **Boltzmann (1872, 1877)**: H-theorem + S = k_B ln W
2. **Gibbs (1902)**: S = -k_B Σ p_i ln p_i (general)
3. **Maxwell-Boltzmann 分布**: v_rms = √(3 k_B T / m)
4. **3 アンサンブル**: microcanonical / canonical / grand canonical
5. **Loschmidt paradox**: 統計的解決
6. **ITU 公理**: δS = δ⟨K⟩ が統計力学全体を内包
7. **次の Phase 144** で **理想気体 + Fermi-Dirac + Bose-Einstein + BEC**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Boltzmann entropy | K_stat 古典極限 |
| Gibbs entropy | K_stat statistical form |
| Maxwell-Boltzmann | K_stat thermal eq. |
| Canonical Z | partition function |
| H-theorem | K-flow time arrow |
| Loschmidt | K-flow asymmetry |

---

## 引用

```
Terada, M. (2026). Phase 143: Boltzmann statistical mechanics, entropy,
and K_stat foundation in ITU (Tier 1 #21 Statistical Mechanics, Block A
paper 5/9, phase 1/8). Zenodo. DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

主要参考文献:
- Boltzmann, L. (1872) "Weitere Studien über das Wärmegleichgewicht unter Gasmolekülen" Wien. Ber. 66, 275
- Boltzmann, L. (1877) "Über die Beziehung zwischen dem zweiten Hauptsatze..." Wien. Ber. 76, 373
- Maxwell, J. C. (1860) "Illustrations of the dynamical theory of gases" Phil. Mag. 19, 19
- Gibbs, J. W. (1902) "Elementary Principles in Statistical Mechanics" Yale University Press
- Jaynes, E. T. (1957) "Information Theory and Statistical Mechanics" Phys. Rev. 106, 620
- Loschmidt, J. (1876) "Über den Zustand des Wärmegleichgewichts eines Systems von Körpern..." Wien. Ber. 73, 128
- Pathria, R. K., Beale, P. D. (2011) "Statistical Mechanics" (3rd ed.) Elsevier
- Reichl, L. E. (2016) "A Modern Course in Statistical Physics" (4th ed.) Wiley
