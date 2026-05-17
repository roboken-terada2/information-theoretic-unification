# Phase 172: Knot 理論 + Jones Polynomial + Witten Chern-Simons + K_knot

> **Tier 1 #24 Mathematical Physics — Phase 6/8 (Block A paper 8/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 172 の目的

Phase 171 で指数定理 (anomaly + topology)。Phase 172 では **位相不変量** = 結び目理論 へ進む — 21 世紀の Fields Medal 級成果:

1. **Knot 理論基礎** (Reidemeister moves 1927)
2. **Alexander polynomial (1928)**
3. **★ Jones polynomial (1984, Fields 1990) ★**
4. **Witten Chern-Simons (1989, Fields 1990)**: Jones を QFT で導出
5. **Kauffman bracket** + skein relation
6. **HOMFLY polynomial** (1985)
7. **Khovanov homology** (1999)
8. **Volume conjecture** (Kashaev 1995)
9. **Topological quantum computation** (Phase 155 anyon 接続)
10. **ITU 視点**: K_knot = K_topo の 1D embedding invariant

中心テーゼ:

> **Jones polynomial = K_knot の universal 不変量** (Witten Chern-Simons より導出)。
> Chern-Simons gauge theory = K_knot を 3D QFT で生成。
> Topological 量子計算 = K_knot の anyon braiding (Phase 155 接続)。

---

## 1. ★ Knot 理論基礎 ★

### 1.1 結び目 + 鎖目

```
Knot: S¹ embedded in ℝ³ (or S³)
Link: 複数 S¹ disjoint embedding
Reidemeister moves I, II, III: equivalence
```

### 1.2 主要結び目

| 名前 | 表示 | crossing 数 |
|---|---|---|
| Unknot (○) | trivial | 0 |
| Trefoil (3_1) | 三葉 | 3 |
| Figure-eight (4_1) | 8字 | 4 |
| Cinquefoil (5_1) | 5葉 | 5 |
| ... | | |

### 1.3 chirality

- Trefoil: 左 / 右 = 異なる knot (mirror image 不変)
- Figure-eight: amphichiral (左右同一)

### 1.4 ITU 視点

```
K_knot = K_topo の 1D embedding invariant
Reidemeister moves = K_knot equivalence
```

---

## 2. Alexander Polynomial (1928)

### 2.1 定義

knot K の Alexander polynomial Δ_K(t):
- Δ_unknot = 1
- skein 関係式

### 2.2 例

| Knot | Δ(t) |
|---|---|
| Unknot | 1 |
| Trefoil | t² - t + 1 |
| Figure-eight | -t² + 3t - 1 |
| Cinquefoil 5_1 | t⁴ - t³ + t² - t + 1 |

### 2.3 制限

mirror image を区別しない (Trefoil 左右同 Δ)。

### 2.4 ITU 視点

```
Alexander Δ = K_knot の polynomial invariant (1928)
```

---

## 3. ★ Jones Polynomial (1984, Fields 1990) ★

### 3.1 定義

skein relation:
```
t^{-1} V(L_+) - t V(L_-) + (t^{1/2} - t^{-1/2}) V(L_0) = 0
```

L_+, L_-, L_0: 過交差, 下交差, 結合 (3 種の局所 crossing)。

### 3.2 例 (V_K(t))

| Knot | V(t) |
|---|---|
| Unknot | 1 |
| Trefoil (right) | -t⁴ + t³ + t |
| Trefoil (left) | -t^{-4} + t^{-3} + t^{-1} |
| Figure-eight | t² - t + 1 - t^{-1} + t^{-2} |
| Cinquefoil 5_1 | -t⁷ + t⁶ - t⁵ + t⁴ + t² |

### 3.3 ★ Chirality 検出 ★

Jones が **左 trefoil ≠ 右 trefoil** を区別 (Alexander は不能)。

### 3.4 Vaughan Jones (Fields Medal 1990)

operator algebra (subfactor) から出発 → 突然 knot 不変量を発見 (1984)。

### 3.5 ITU 視点

```
Jones polynomial = K_knot universal invariant (chirality 検出)
```

---

## 4. ★ Kauffman Bracket + skein ★

### 4.1 Kauffman 1987

normalized bracket ⟨K⟩:
- ⟨○⟩ = 1
- ⟨K ⊔ ○⟩ = (-A² - A^{-2}) ⟨K⟩
- ⟨crossing⟩ = A ⟨smoothing_0⟩ + A^{-1} ⟨smoothing_∞⟩

### 4.2 Jones との関係

```
V_K(t) = (-A)^{-3w(K)} ⟨K⟩, A = t^{-1/4}
```

w(K) = writhe (signed crossings)。

### 4.3 ITU 視点

```
Kauffman bracket = K_knot の State sum
```

---

## 5. ★ Witten Chern-Simons (1989) ★

### 5.1 主張

3D Chern-Simons gauge theory が **Jones polynomial を path integral** で生成:

```
S_CS = (k/4π) ∫ tr(A ∧ dA + (2/3) A ∧ A ∧ A)
```

k = level (integer)。

### 5.2 Wilson loop 期待値

```
W_K = ⟨tr_R P exp(∮_K A)⟩ = V_K(q)
```

q = e^{2πi/(k+2)}, R = SU(2) 2 (fundamental)。

### 5.3 Witten 1989 (Fields 1990)

```
Fields Medal: V. Jones (1990), E. Witten (1990)
```

= 同年。Jones (operator algebra) ↔ Witten (QFT) 双対。

### 5.4 ITU 視点

```
Chern-Simons = K_knot 生成 3D QFT
Wilson loop = K_knot expectation value
```

---

## 6. HOMFLY (1985) + Khovanov (1999)

### 6.1 HOMFLY (2 変数 generalization)

```
P(a, z) skein:
a P(L_+) - a^{-1} P(L_-) = z P(L_0)
```

Jones は HOMFLY の specialization。

### 6.2 Khovanov homology (1999)

各 knot に **homology 群** H^{i,j}(K) を割り当てる:

```
χ(H_K) = Jones polynomial
```

= categorification (より洗練された invariant)。

### 6.3 主要結果

- Khovanov + Ozsváth-Szabó knot Floer → **slice genus** など解析的不変量
- Rasmussen invariant s(K) → exotic ℝ⁴ structures (Mike Freedman, Fields 1986)

### 6.4 ITU 視点

```
HOMFLY = K_knot 2-変数 polynomial
Khovanov = K_knot categorified homology
```

---

## 7. Volume Conjecture (Kashaev 1995, Murakami 2001)

### 7.1 主張

```
lim_{N→∞} (1/N) log |V_N(K, e^{2πi/N})| = (1/2π) Vol(S³ \ K)
```

= colored Jones polynomial の large N 漸近 が **双曲体積** を与える。

### 7.2 未解決

部分的に証明 (8字結び目等), 一般 knot は未解決。

### 7.3 ITU 視点

```
Volume conjecture = K_knot ↔ K_hyperbolic 双対 (未解決)
```

---

## 8. ★ Topological 量子計算 ★

### 8.1 Anyon braiding

Phase 155 で FQHE ν=5/2 の non-abelian anyon を扱った。anyon の braiding = **knot 操作** に対応:

```
Braiding = K_knot generation
Anyon statistics → universal quantum computation 候補
```

### 8.2 Kitaev model (2003)

2D spin lattice で **toric code** + **honeycomb model** → topological qubit 候補。

### 8.3 Majorana fermion (Phase 156 接続)

```
Majorana 0-mode at TI/SC boundary → non-abelian anyon
quantum computing platform
```

### 8.4 ITU 視点

```
Topological 量子計算 = K_knot operations physical realization
```

---

## 9. 数値検証項目

本 phase の simulation で確認:

1. **Jones polynomial** for unknot, trefoil L/R, figure-eight, 5_1
2. **Jones 値 at t=1**: Jones(1) = 1 (規格化)
3. **Chirality 検出**: V(trefoil L) ≠ V(trefoil R)
4. **Kauffman bracket** ⟨trefoil⟩ 計算
5. **Skein relation** 検証
6. **Anyon braiding matrix** for ν=1/3 FQHE

---

## 10. Phase 172 主結論

1. **Knot 理論基礎**: Reidemeister moves I, II, III
2. **Alexander (1928)**: polynomial invariant (chirality blind)
3. **Jones (1984, Fields 1990)**: chirality 検出 polynomial
4. **Kauffman bracket (1987)**: state sum
5. **Witten Chern-Simons (1989, Fields 1990)**: Jones を QFT 化
6. **HOMFLY (1985)**: 2 変数 generalization
7. **Khovanov (1999)**: categorified homology
8. **Volume conjecture**: V_N → hyperbolic Vol (未解決)
9. **Topological 量子計算**: anyon braiding (Phase 155, 156)
10. **ITU**: K_knot = K_topo 1D embedding invariant
11. **次の Phase 173** で **Random matrix theory + Riemann Hypothesis**

---

## 11. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Knot | K_topo 1D embedding |
| Reidemeister moves | K_knot equivalence |
| Alexander Δ | K_knot 1928 polynomial |
| Jones V | K_knot chirality-sensitive |
| Kauffman bracket | K_knot state sum |
| Witten CS | K_knot 3D QFT origin |
| HOMFLY | K_knot 2-変数 generalization |
| Khovanov | K_knot categorified homology |
| Volume conjecture | K_knot ↔ K_hyperbolic |
| Anyon braiding | K_knot physical realization |

---

## 引用

```
Terada, M. (2026). Phase 172: Knot theory — Jones polynomial, Witten Chern-Simons,
and topological quantum computation in ITU (Tier 1 #24 phase 6/8). Zenodo.
DOI: [10.5281/zenodo.20251178](https://doi.org/10.5281/zenodo.20251178).
```

主要参考文献:
- Alexander, J. W. (1928) "Topological invariants of knots and links" Trans. Amer. Math. Soc. 30, 275
- Reidemeister, K. (1927) "Knoten und Gruppen" Abh. Math. Sem. Univ. Hamburg 5, 7
- Jones, V. F. R. (1985) "A polynomial invariant for knots via von Neumann algebras" Bull. Amer. Math. Soc. 12, 103 (Fields 1990)
- Kauffman, L. H. (1987) "State models and the Jones polynomial" Topology 26, 395
- Freyd, P., Yetter, D., Hoste, J., Lickorish, W. B. R., Millett, K. C., Ocneanu, A. (1985) "A new polynomial invariant of knots and links" Bull. Amer. Math. Soc. 12, 239 (HOMFLY)
- Witten, E. (1989) "Quantum field theory and the Jones polynomial" Comm. Math. Phys. 121, 351 (Fields 1990)
- Khovanov, M. (2000) "A categorification of the Jones polynomial" Duke Math. J. 101, 359
- Ozsváth, P., Szabó, Z. (2004) "Holomorphic disks and topological invariants for closed three-manifolds" Ann. Math. 159, 1027
- Rasmussen, J. (2010) "Khovanov homology and the slice genus" Invent. Math. 182, 419
- Kashaev, R. M. (1997) "The hyperbolic volume of knots from quantum dilogarithm" Lett. Math. Phys. 39, 269
- Murakami, H., Murakami, J. (2001) "The colored Jones polynomials and the simplicial volume of a knot" Acta Math. 186, 85
- Drinfeld, V. G. (1986) "Quantum groups" Proc. ICM Berkeley, 798
- Kitaev, A. (2003) "Fault-tolerant quantum computation by anyons" Ann. Phys. 303, 2
- Nayak, C., Simon, S. H., Stern, A., Freedman, M., Das Sarma, S. (2008) "Non-Abelian anyons and topological quantum computation" Rev. Mod. Phys. 80, 1083
