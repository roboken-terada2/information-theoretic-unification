# Phase 147: 揺動定理 — Jarzynski 等式 + Crooks 関係 + 非平衡仕事

> **Tier 1 #21 Statistical Mechanics — Phase 5/8 (Block A paper 5/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 147 の目的

Phase 146 で線形応答 + FDT を扱った。Phase 147 では **非線形領域** の揺動定理 (fluctuation theorems, FTs) に進む:

1. **Jarzynski 等式 (1997)**: ⟨e^{-βW}⟩ = e^{-βΔF}
2. **Crooks 揺動定理 (1999)**: P_F(W) / P_R(-W) = e^{β(W-ΔF)}
3. **Detailed fluctuation theorem (Gallavotti-Cohen 1995)**
4. **Integral fluctuation theorem**
5. **Stochastic thermodynamics** (Seifert 2005)
6. **ITU 視点**: 揺動定理 = K_stat の **path-space dual symmetry**

中心テーゼ:

> **Jarzynski 等式 = ITU K_stat の path integral 上の対数平均 = 自由エネルギー差**。
> Crooks = K_stat の前進/後退 trajectory 確率の **detailed balance** 拡張版。
> 第 2 法則の不等式 ⟨W⟩ ≥ ΔF は、Jarzynski 等式の Jensen 不等式 corollary。

---

## 1. 古典熱力学からの拡張

### 1.1 平衡熱力学第 2 法則

```
W ≥ ΔF   (isothermal process, T fixed)
```

= W は ΔF 以上の仕事を要する。

### 1.2 揺動の存在

**Microscopic** には W は確率分布 P(W)。
個別 trajectory では W < ΔF も可能 ⇒ **second-law violation locally**。

⇒ Fluctuation theorem は P(W) と P(-W) を結ぶ。

---

## 2. ★ Jarzynski 等式 (1997) ★

### 2.1 主張

任意の非平衡 protocol (初期 = 平衡 at λ_0) で:

```
⟨e^{-βW}⟩ = e^{-βΔF}
```

- W: 個別 trajectory の仕事
- ΔF = F(λ_f) - F(λ_0): 平衡自由エネルギー差
- ⟨...⟩: 全 trajectory についての平均

### 2.2 Jensen 不等式から第 2 法則

```
⟨e^{-βW}⟩ ≥ e^{-β⟨W⟩}   (Jensen, exp is convex)

⇒ e^{-βΔF} ≥ e^{-β⟨W⟩}
⇒ ⟨W⟩ ≥ ΔF   (第 2 法則回復)
```

### 2.3 含意

```
W < ΔF となる trajectory が存在 (微視的揺動)
だが ⟨e^{-βW}⟩ で平均すると ΔF と等しい
```

### 2.4 実験検証 (Liphardt et al. 2002, Collin et al. 2005)

- RNA hairpin unfolding by optical tweezer
- ⟨e^{-βW}⟩ 計算 → ΔF 抽出
- 平衡熱力学測定と一致 ✓

### 2.5 ITU 視点

```
Jarzynski = K_stat の path-space exponential moment generating function
⟨e^{-βW}⟩ = K_path → K_eq (boundary contraction)
```

---

## 3. ★ Crooks Fluctuation Theorem (1999) ★

### 3.1 主張

前進 protocol P_F(W) と時間反転 protocol P_R(-W) の比:

```
P_F(W) / P_R(-W) = e^{β(W - ΔF)}
```

### 3.2 Jarzynski 等式の導出

積分:
```
∫ P_F(W) e^{-βW} dW = ∫ P_R(-W) e^{-βΔF} dW = e^{-βΔF}
```

⇒ Jarzynski。

### 3.3 W = ΔF での交差

```
P_F(W = ΔF) = P_R(-W = -ΔF)
```

= 2 つの分布が ΔF で **交差**。実験的 ΔF 抽出に利用 (Collin et al. 2005)。

### 3.4 ITU 視点

```
Crooks = K_stat path 確率の time-reversal duality
= K_stat の 詳細釣り合い (detailed balance) の非平衡拡張
```

---

## 4. Detailed Fluctuation Theorem (Gallavotti-Cohen 1995)

### 4.1 主張

定常状態 (NESS) でエントロピー生成 σ:

```
P(σ) / P(-σ) = e^σ
```

### 4.2 平均からの含意

```
⟨σ⟩ ≥ 0  (第 2 法則)
```

### 4.3 ITU 視点

```
G-C = K_stat NESS path-space の time-reversal odd symmetry
```

---

## 5. Stochastic Thermodynamics (Seifert 2005-2012)

### 5.1 単一 trajectory のエントロピー

```
s_tot[x(t)] = s_sys[x(t)] + s_env[x(t)]

s_sys = -log P(x, t)
s_env = ∫ q(t) / T dt   (heat / T)
```

### 5.2 Integral fluctuation theorem

```
⟨e^{-s_tot}⟩ = 1
```

(Jarzynski の一般化)。

### 5.3 ITU 視点

```
Stochastic thermodynamics = K_stat trajectory-level エントロピー会計
```

---

## 6. Maxwell の魔 と Landauer の限界

### 6.1 Maxwell の魔 (1867)

エネルギーなしで分子を選別 → 第 2 法則違反?

### 6.2 Szilard engine (1929)

1 bit 情報 → k_B T ln 2 の仕事。

### 6.3 Landauer の限界 (1961)

```
W_erase ≥ k_B T ln 2  per bit
```

(Bennett 1982 が解決: 情報消去にコスト)。

### 6.4 数値例 (300 K)

```
W_min = k_B × 300 × ln 2 ≈ 2.87e-21 J/bit ≈ 17.9 meV/bit
```

### 6.5 実験検証 (Bérut et al. 2012)

Colloidal particle double-well で Landauer 限界の直接観測。

### 6.6 ITU 視点

```
Maxwell demon = ITU 情報-熱統合
Landauer = K_info ↔ K_thermo の最小 conversion cost
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Jarzynski 等式**: ⟨e^{-βW}⟩ = e^{-βΔF} (調和振動子 spring shift)
2. **Crooks 関係**: P_F(W) / P_R(-W) = e^{β(W-ΔF)}
3. **W < ΔF trajectories の存在** (確率分布裾)
4. **Landauer limit**: k_B T ln 2 / bit
5. **Integral FT**: ⟨e^{-s_tot}⟩ = 1

---

## 8. Phase 147 主結論

1. **Jarzynski 1997**: ⟨e^{-βW}⟩ = e^{-βΔF}
2. **Crooks 1999**: P_F(W) / P_R(-W) = e^{β(W-ΔF)}
3. **Gallavotti-Cohen 1995**: P(σ)/P(-σ) = e^σ
4. **Seifert 2005-2012**: stochastic thermodynamics
5. **Landauer 1961**: W_erase ≥ k_B T ln 2 (Bérut 2012 実験)
6. **第 2 法則**: 平均量の不等式 (Jensen) であり、microscopic には violations 可能
7. **ITU**: 揺動定理 = K_stat path-space dual symmetry
8. **次の Phase 148** で **情報理論 + Shannon + Jaynes max entropy**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Jarzynski equality | K_stat path-space exp moment |
| Crooks FT | K_stat time-reversal path duality |
| Gallavotti-Cohen | K_stat NESS odd parity |
| Stochastic thermo | K_stat trajectory-level accounting |
| Landauer limit | K_info ↔ K_thermo minimal conversion |

---

## 引用

```
Terada, M. (2026). Phase 147: Fluctuation theorems (Jarzynski + Crooks) and
stochastic thermodynamics in ITU (Tier 1 #21 phase 5/8). Zenodo. DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

主要参考文献:
- Jarzynski, C. (1997) "Nonequilibrium equality for free energy differences" PRL 78, 2690
- Crooks, G. E. (1999) "Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences" Phys. Rev. E 60, 2721
- Gallavotti, G., Cohen, E. G. D. (1995) "Dynamical ensembles in nonequilibrium statistical mechanics" PRL 74, 2694
- Evans, D. J., Cohen, E. G. D., Morriss, G. P. (1993) "Probability of second-law violations in shearing steady states" PRL 71, 2401
- Seifert, U. (2005) "Entropy production along a stochastic trajectory and an integral fluctuation theorem" PRL 95, 040602
- Seifert, U. (2012) "Stochastic thermodynamics, fluctuation theorems and molecular machines" Rep. Prog. Phys. 75, 126001
- Landauer, R. (1961) "Irreversibility and heat generation in the computing process" IBM J. Res. Dev. 5, 183
- Bennett, C. H. (1982) "The thermodynamics of computation — a review" Int. J. Theor. Phys. 21, 905
- Liphardt, J. et al. (2002) "Equilibrium information from nonequilibrium measurements in an experimental test of Jarzynski's equality" Science 296, 1832
- Collin, D. et al. (2005) "Verification of the Crooks fluctuation theorem and recovery of RNA folding free energies" Nature 437, 231
- Bérut, A. et al. (2012) "Experimental verification of Landauer's principle linking information and thermodynamics" Nature 483, 187
