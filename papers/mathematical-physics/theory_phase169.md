# Phase 169: Yang-Mills + Gauge 理論 + Clay Millennium #5 質量ギャップ ★

> **Tier 1 #24 Mathematical Physics — Phase 3/8 (Block A paper 8/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 169 の目的

Phase 167 (Lie 群) + Phase 168 (可積分系) を物理に適用 — **非可換 gauge 理論** へ:

1. **Yang-Mills (1954)** 非可換 gauge 理論
2. **gauge 共変** 微分 D_μ + 場の強さ F_μν
3. **Asymptotic freedom** (GWP 1973, Phase 138)
4. **Confinement** + Wilson loop area law
5. **★ Clay Millennium #5: Yang-Mills mass gap ★**
6. **Lattice gauge theory** (Wilson 1974)
7. **Instanton** (BPST 1975)
8. **Witten SUSY argument** (1998)
9. **ITU 視点**: K_gauge = K_sym + 接続 (connection)

中心テーゼ:

> **Yang-Mills mass gap = K_gauge の non-perturbative 質量生成 (Clay $1M)**。
> Confinement = K_gauge の Wilson loop area law。
> Instanton = K_gauge の topologically non-trivial saddle (Pontryagin 数 整数)。

---

## 1. ★ Yang-Mills 理論 (1954) ★

### 1.1 動機

Yang-Mills 1954: SU(2) global symmetry (isospin) を **局所 gauge** に拡張。
当初は質量問題で物理応用困難 → 後年 Higgs 機構 (Phase 137) + QCD 漸近自由 (Phase 138) で復活。

### 1.2 gauge 場

```
A_μ = A_μ^a T^a   (Lie 代数値)
T^a: SU(N) generators
```

### 1.3 gauge 共変微分

```
D_μ = ∂_μ - i g A_μ
```

物質場 ψ の変換: ψ → U ψ, A_μ → U A_μ U^† - (i/g)(∂_μ U)U^†。

### 1.4 場の強さ

```
F_μν = ∂_μ A_ν - ∂_ν A_μ - i g [A_μ, A_ν]
```

= 非 Abelian 項 [A,A] が **自己相互作用** (3-gluon, 4-gluon vertex)。

### 1.5 Lagrangian

```
ℒ_YM = -(1/4) tr(F_μν F^μν)
```

### 1.6 ITU 視点

```
K_gauge = K_sym + connection A_μ
F_μν = K_gauge curvature (Bianchi 接続)
```

---

## 2. ★ Asymptotic Freedom (1973 Nobel 2004) ★

### 2.1 1-loop β 関数

```
β(g) = -b_0 g³ / (16π²) + ...

b_0 = (11/3) C_A - (4/3) T_F n_f
```

C_A = N (SU(N) adjoint), T_F = 1/2 (fundamental), n_f = flavors。

### 2.2 QCD (SU(3), n_f=6)

```
b_0 = 11 - 12 = -1   (wait check sign)
```

正確には QCD:
```
b_0^{QCD} = (33 - 2 n_f) / 3
b_0(n_f=6) = (33 - 12)/3 = 7 > 0
```

⇒ **β < 0**, **asymptotic freedom**: 高エネルギーで g → 0。

### 2.3 数値 (Phase 138)

```
α_s(M_Z) = 0.118
α_s(M_τ) ≈ 0.32 (低エネルギー)
α_s(M_Pl) ≈ 0.05 (Planck)
```

### 2.4 ITU 視点

```
Asymptotic freedom = K_gauge UV fixed point at g=0
```

---

## 3. ★ Confinement + Wilson loop ★

### 3.1 Wilson loop

```
W(C) = (1/N) tr[P exp(i g ∮_C A_μ dx^μ)]
```

closed loop C 上の **path-ordered exponential**。

### 3.2 ★ Area law (confinement) ★

```
⟨W(C)⟩ ∝ exp(-σ A_C)
```

A_C = loop の囲む面積, σ = string tension。

### 3.3 物理: 静的 quark pair potential

```
V(R) = σ R + (Cornell -α/R 項) + const
```

= **線形 confining potential**。Phase 138 の Cornell potential。

### 3.4 数値: QCD

```
σ ≈ 1 GeV/fm ≈ 0.18 GeV²
```

(lattice QCD 計算)。

### 3.5 ITU 視点

```
Confinement = K_gauge Wilson loop area law
σ = K_gauge string tension
```

---

## 4. ★★ Clay Millennium #5: Yang-Mills Mass Gap ★★

### 4.1 公式 Statement (Jaffe-Witten 2000)

**任意の compact simple gauge 群 G (例: SU(3)) に対し、4 次元 Minkowski 時空での Yang-Mills 量子場理論が non-perturbatively 存在し、ある質量ギャップ Δ > 0 を持つことを証明**。

```
質量ギャップ: 最低励起状態 (lightest glueball) の質量 m > 0
```

### 4.2 物理的予想

```
SU(3) glueball mass (lattice): m_{0++} ≈ 1.7 GeV
                                m_{2++} ≈ 2.4 GeV
```

### 4.3 困難

- non-perturbative: 摂動展開 (asymptotic) のみでは到達不能
- 4D Minkowski の axiomatic 構築 (Wightman, Osterwalder-Schrader)
- 質量ギャップの厳密証明

### 4.4 部分結果

| 年 | 結果 |
|---|---|
| 1980s | 1+1D, 2+1D で部分構築 |
| 1998 | Witten SUSY argument (heuristic) |
| 2000s | 格子 QCD で数値強い証拠 |
| 2015 | constructive YM in 2D toy |
| 2020s+ | **未解決** (Clay $1M 待機) |

### 4.5 ITU 視点

```
Mass gap = K_gauge non-perturbative excitation gap
ITU 答えがどちらでも整合
```

---

## 5. ★ Lattice Gauge Theory (Wilson 1974) ★

### 5.1 設定

時空を格子化, gauge 場 = link variables U_l ∈ SU(N):
```
U_l = exp(i a A_μ T^a)
```

### 5.2 Wilson action

```
S_W = β Σ_p (1 - (1/N) Re tr U_p)
U_p = plaquette (4 link 周回)
β = 2N / g²
```

### 5.3 強結合極限

```
g → ∞: ⟨W(C)⟩ ∝ exp(-σ A)
⇒ confinement 確立 ✓
```

### 5.4 数値 lattice QCD (2020s)

| 量 | 値 |
|---|---|
| Glueball 0++ | 1.7 GeV |
| Static potential slope σ | 0.18 GeV² |
| α_s(M_Z) lattice | 0.118 ✓ |

### 5.5 ITU 視点

```
Lattice gauge = K_gauge UV regularization
Strong coupling expansion = K_gauge confinement direct
```

---

## 6. ★ Instanton (BPST 1975) ★

### 6.1 Euclidean self-dual 解

```
F_μν = ± *F_μν   (self-dual)
```

(Belavin-Polyakov-Schwarz-Tyupkin 1975)。

### 6.2 Topological charge

```
n = (1/32π²) ∫ d⁴x tr(F μν *F^μν) ∈ ℤ
```

= **Pontryagin 数** (integer)。

### 6.3 BPST 解

```
A_μ^a = 2 η_{aμν} x_ν / (x² + ρ²)
```

ρ = instanton size。Action S = 8π²/g²。

### 6.4 物理応用

- **θ-vacuum** + **strong CP problem** (Phase 138)
- Axion (Peccei-Quinn) 解決候補
- baryon number 違反 (electroweak instanton)
- ABJ anomaly (Phase 171 で扱う)

### 6.5 ITU 視点

```
Instanton = K_gauge topologically non-trivial saddle
Pontryagin n = K_gauge topological invariant ∈ ℤ
θ-vacuum = K_gauge instanton sum
```

---

## 7. Witten SUSY Argument (1998)

### 7.1 主張

N=1 SUSY YM では **gluino condensate** ⟨λλ⟩ ≠ 0 が厳密に証明可能 (Seiberg-Witten 1994 拡張)。

```
⟨λλ⟩ = e^{2πik/N} Λ³,  k = 0, 1, ..., N-1
```

= mass gap の **間接** 証拠 (SUSY breaking 補正後)。

### 7.2 ITU 視点

```
Witten SUSY → mass gap evidence
Pure YM 厳密証明には別アプローチが必要
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **β 関数** QCD α_s(μ) running (Phase 138 再掲)
2. **Wilson loop area law** simple lattice 2D illustration
3. **Cornell potential** V(R) = σR - α/R
4. **Instanton action** S = 8π²/g²
5. **Pontryagin n** integer 検証
6. **Glueball mass** lattice predictions

---

## 9. Phase 169 主結論

1. **Yang-Mills (1954)**: 非可換 gauge 理論
2. **F_μν = ∂A - ∂A - ig[A,A]** with self-interaction
3. **Asymptotic freedom (1973, Nobel 2004)**: β<0 → UV fixed point
4. **Confinement**: Wilson loop area law, σ ≈ 0.18 GeV²
5. **Clay Millennium #5 (2000)**: Mass gap proof 未解決 ($1M)
6. **Lattice (Wilson 1974)**: glueball ≈ 1.7 GeV 数値強証拠
7. **Instanton (BPST 1975)**: Pontryagin n ∈ ℤ, S = 8π²/g²
8. **Witten SUSY (1998)**: gluino condensate 間接証拠
9. **ITU**: K_gauge = K_sym + connection + curvature F_μν
10. **次の Phase 170** で **CFT + Virasoro + BPZ**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Yang-Mills | K_gauge non-Abelian extension |
| gauge 場 A_μ | K_gauge connection |
| 場の強さ F_μν | K_gauge curvature |
| Asymptotic freedom | K_gauge UV fixed point at g=0 |
| Wilson loop | K_gauge holonomy |
| Confinement (area law) | K_gauge non-perturbative |
| Mass gap | K_gauge excitation threshold (Clay) |
| Lattice | K_gauge UV regularization |
| Instanton | K_gauge topological saddle |
| Pontryagin n | K_gauge ∈ ℤ topological invariant |
| θ-vacuum | K_gauge instanton sum |

---

## 引用

```
Terada, M. (2026). Phase 169: Yang-Mills gauge theory and the Clay Millennium
mass gap problem in ITU (Tier 1 #24 phase 3/8). Zenodo. DOI: [10.5281/zenodo.20251178](https://doi.org/10.5281/zenodo.20251178).
```

主要参考文献:
- Yang, C. N., Mills, R. L. (1954) "Conservation of isotopic spin and isotopic gauge invariance" Phys. Rev. 96, 191
- 't Hooft, G. (1972) unpublished. Gross, D., Wilczek, F. (1973) "Ultraviolet behavior of non-abelian gauge theories" PRL 30, 1343. Politzer, H. D. (1973) "Reliable perturbative results for strong interactions" PRL 30, 1346 [Nobel 2004]
- Wilson, K. G. (1974) "Confinement of quarks" PRD 10, 2445
- Belavin, A. A., Polyakov, A. M., Schwarz, A. S., Tyupkin, Yu. S. (1975) "Pseudoparticle solutions of the Yang-Mills equations" Phys. Lett. B 59, 85
- Jaffe, A., Witten, E. (2000) "Quantum Yang-Mills theory" Clay Math. Inst. Millennium Prize
- Seiberg, N., Witten, E. (1994) "Electric-magnetic duality, monopole condensation, and confinement in N=2 supersymmetric Yang-Mills theory" Nucl. Phys. B 426, 19; 431, 484
- 't Hooft, G. (1976) "Symmetry breaking through Bell-Jackiw anomalies" PRL 37, 8
- Witten, E. (1998) "Anti-de Sitter space, thermal phase transition, and confinement in gauge theories" Adv. Theor. Math. Phys. 2, 505
- Peccei, R. D., Quinn, H. R. (1977) "CP conservation in the presence of pseudoparticles" PRL 38, 1440
- Polyakov, A. M. (1977) "Quark confinement and topology of gauge theories" Nucl. Phys. B 120, 429
- Greensite, J. (2011) An Introduction to the Confinement Problem. Springer
- Bali, G. S. (2000) "QCD forces and heavy quark bound states" Phys. Rep. 343, 1
