# Phase 170: 共形場理論 (CFT) + Virasoro + BPZ + 2D 場理論 + K_CFT

> **Tier 1 #24 Mathematical Physics — Phase 4/8 (Block A paper 8/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 170 の目的

Phase 167-169 で Lie + 可積分 + Yang-Mills。Phase 170 では **共形対称性** に進む — Phase 145 critical phenomena の数学側 + Phase 122 AdS/CFT との接続:

1. **共形変換** (角度保存)
2. **2D 共形 = 無限次元 (Virasoro algebra)**
3. **BPZ (Belavin-Polyakov-Zamolodchikov 1984)** 公理
4. **Primary fields + conformal weight (h, h̄)**
5. **★ Minimal models** (Ising c=1/2, tricritical Ising c=7/10, ...)
6. **WZW models** + Kac-Moody algebra
7. **Modular invariance** (torus partition function)
8. **AdS/CFT** (Phase 111 接続)
9. **ITU 視点**: K_CFT = K_sym + scale invariance + 2D 無限拡張

中心テーゼ:

> **2D CFT = K_CFT の無限次元化** (Virasoro)。
> 中心電荷 c = K_CFT の universal invariant。
> Minimal models = K_CFT の有理 (rational) 系列。
> Phase 145 critical Ising = K_CFT c=1/2 の物理実現。

---

## 1. ★ 共形変換 ★

### 1.1 定義

```
g_{μν}(x) → Ω²(x) g_{μν}(x)
```

= **計量を局所 scale factor で変える** 変換。**角度保存**。

### 1.2 D 次元 共形 群

```
D ≥ 3: SO(D, 2) (D=4 → SO(4,2), 15 generators)
D = 2: 無限次元 (Virasoro)
D = 1: SL(2, ℝ) (3 generators)
```

### 1.3 4D の 15 generators

```
Translations: P_μ (4)
Lorentz: M_μν (6)
Dilatation: D (1)
Special conformal: K_μ (4)
合計: 15
```

### 1.4 ITU 視点

```
K_CFT = K_sym scale-invariant
D ≥ 3 vs D = 2 = K_CFT dimensional 違い
```

---

## 2. ★ 2D Virasoro 代数 ★

### 2.1 古典: Witt algebra

```
[L_m, L_n] = (m - n) L_{m+n}
```

= 円上の vector 場代数。

### 2.2 量子: Virasoro (central extension)

```
[L_m, L_n] = (m - n) L_{m+n} + (c/12) m (m² - 1) δ_{m+n, 0}
```

c: **central charge** (量子効果)。

### 2.3 物理: stress-tensor

```
T(z) = Σ L_n z^{-n-2}   (energy-momentum tensor)
```

### 2.4 ITU 視点

```
Virasoro = K_CFT 無限次元 algebra
c = K_CFT central charge (universal label, Cardy 接続)
```

---

## 3. ★ BPZ (Belavin-Polyakov-Zamolodchikov 1984) ★

### 3.1 主張

2D CFT を **公理的** に定式化:
- 共形対称性 (Virasoro)
- primary field + descendants
- operator product expansion (OPE)
- correlation function 計算

### 3.2 Primary field

```
T(z) φ(w) = h φ(w)/(z-w)² + ∂φ/(z-w) + ...
```

→ φ の **conformal weight** (h, h̄)。Scaling dimension Δ = h + h̄, spin s = h - h̄。

### 3.3 OPE

```
φ_i(z) φ_j(w) = Σ_k C_{ij}^k (z - w)^{h_k - h_i - h_j} φ_k(w) + ...
```

= primary field 同士の積を primary + descendants に展開。

### 3.4 ITU 視点

```
BPZ = K_CFT axiomatic system
Primary field = K_CFT eigenstate of L_0
OPE = K_CFT algebra of operators
```

---

## 4. ★ Minimal Models ★

### 4.1 Kac formula

c < 1 で **有理 (rational) CFT**:

```
c = 1 - 6(p - q)² / (pq)
p, q: coprime integers ≥ 2
```

### 4.2 例

| (p, q) | c | 名前 | 物理 |
|---|---|---|---|
| (3, 4) | **1/2** | **Ising** | Phase 145 ferromagnet |
| (4, 5) | 7/10 | tricritical Ising | |
| (5, 6) | 4/5 | tetracritical | |
| (6, 7) | 6/7 | hexacritical | |
| p = q+1, q→∞ | → 1 | XXZ chain | |

### 4.3 Ising CFT (c = 1/2)

3 primary fields:
```
1 (h=0)         identity
σ (h=1/16)      spin (order parameter)
ε (h=1/2)       energy (disorder)
```

### 4.4 数値 (Phase 145 接続)

| Critical exponent | Ising CFT | Phase 145 |
|---|---|---|
| β | 1/8 | 0.125 (2D ✓) |
| ν | 1 | 1.0 (2D ✓) |
| η | 1/4 | 1/4 ★ from σ |
| γ | 7/4 | 1.75 ✓ |

⇒ **CFT c = 1/2 が 2D Ising の正確な解** (Onsager 1944 の現代版)。

### 4.5 ITU 視点

```
Minimal models = K_CFT 有理 (rational) series
c = 1/2 Ising = K_CFT critical Phase 145 物理実現
```

---

## 5. WZW Models + Kac-Moody Algebra

### 5.1 Wess-Zumino-Witten

```
G_k WZW: G compact simple Lie group, k integer (level)
```

### 5.2 Kac-Moody algebra

```
[J_m^a, J_n^b] = i f^{abc} J_{m+n}^c + k m δ^{ab} δ_{m+n, 0}
```

= Virasoro の **Lie 代数版** (affine extension)。

### 5.3 Sugawara construction

```
T(z) = (1/(2(k + h^∨))) Σ_a : J^a J^a : (z)
```

→ Virasoro central charge:
```
c = k dim(G) / (k + h^∨)
```

h^∨: dual Coxeter number。

### 5.4 ITU 視点

```
WZW = K_CFT + K_sym 非可換 fiber
Kac-Moody = K_sym infinite-dim affine extension
```

---

## 6. Modular Invariance

### 6.1 Torus partition function

CFT を torus 上で計算 → 振動子 (q = e^{2πiτ}, τ = modular parameter):

```
Z(τ, τ̄) = tr(q^{L_0 - c/24} q̄^{L̄_0 - c/24})
```

### 6.2 SL(2, ℤ) invariance

```
τ → (aτ + b)/(cτ + d), ad - bc = 1
```

⇒ Z は **modular invariant**。

### 6.3 帰結

ADE 分類 (Cappelli-Itzykson-Zuber 1987):
```
SU(2)_k 分類: A_k, D_2n, E_6, E_7, E_8
```

= ADE Dynkin と一致 (Phase 167 接続)。

### 6.4 ITU 視点

```
Modular invariance = K_CFT torus consistency
ADE 分類 = K_sym と K_CFT の double role
```

---

## 7. AdS/CFT (Maldacena 1997, Phase 111 接続)

### 7.1 主張

```
N=4 SYM (4D CFT, conformal) ↔ Type IIB string on AdS_5 × S⁵
```

= ホログラフィック 双対性 (Phase 111-114, 122-124)。

### 7.2 RT formula (Phase 111)

```
S_A = Area(γ_A) / (4 G_N)
```

= boundary entropy ↔ bulk minimal surface area。

### 7.3 ITU 視点

```
AdS/CFT = K_CFT (boundary) ↔ K_geom (bulk) holographic duality
RT formula = K_CFT entropy = K_geom area (Phase 111 ITU axiom 一致)
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Virasoro commutator** [L_m, L_n] の数値
2. **Minimal model central charges** (3,4), (4,5), (5,6) → c
3. **Ising CFT exponents** β=1/8, ν=1, γ=7/4
4. **Cardy formula** S = 2π √(c L_0 / 6) (Phase 122 BH 接続)
5. **WZW Sugawara c** for SU(2)_k

---

## 9. Phase 170 主結論

1. **共形変換** = 角度保存 + 計量 scale
2. **2D CFT** = 無限次元 (Virasoro)
3. **Virasoro [L_m, L_n] = (m-n)L_{m+n} + (c/12)m(m²-1)δ_{m+n,0}**
4. **BPZ (1984)** axiomatic 2D CFT
5. **Kac minimal models**: c = 1 - 6(p-q)²/(pq), p,q coprime
6. **Ising c = 1/2**: 2D Ising universality class (Phase 145 ✓)
7. **WZW + Kac-Moody**: infinite affine extension
8. **Modular invariance**: SL(2,ℤ) torus → ADE 分類
9. **AdS/CFT**: K_CFT (boundary) ↔ K_geom (bulk) hologram
10. **Cardy** S = 2π √(c L_0/6): BH entropy 微視的起源
11. **ITU**: K_CFT = K_sym + scale + 2D infinite extension
12. **次の Phase 171** で **Index 定理 + Atiyah-Singer + anomaly**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| 共形変換 | K_sym scale-invariant 拡張 |
| Virasoro | K_CFT infinite-dim algebra |
| Central charge c | K_CFT universal label |
| BPZ | K_CFT axiomatic |
| Primary field | K_CFT L_0 eigenstate |
| OPE | K_CFT operator algebra |
| Minimal models | K_CFT rational series |
| Ising c=1/2 | K_CFT critical 2D realisation |
| WZW | K_CFT + K_sym non-abelian |
| Kac-Moody | K_sym affine extension |
| Modular invariance | K_CFT torus consistency |
| ADE 分類 | K_sym ↔ K_CFT double role |
| AdS/CFT | K_CFT ↔ K_geom hologram |
| Cardy formula | K_CFT entropy = K_geom area |

---

## 引用

```
Terada, M. (2026). Phase 170: Conformal field theory — Virasoro algebra, BPZ
formalism, minimal models, WZW, modular invariance in ITU
(Tier 1 #24 phase 4/8). Zenodo. DOI: [10.5281/zenodo.20251178](https://doi.org/10.5281/zenodo.20251178).
```

主要参考文献:
- Belavin, A. A., Polyakov, A. M., Zamolodchikov, A. B. (1984) "Infinite conformal symmetry in two-dimensional quantum field theory" Nucl. Phys. B 241, 333
- Cardy, J. L. (1986) "Operator content of two-dimensional conformally invariant theories" Nucl. Phys. B 270, 186
- Kac, V. G. (1979) "Contravariant form for infinite-dimensional Lie algebras and superalgebras" Lect. Notes Phys. 94, 441
- Friedan, D., Qiu, Z., Shenker, S. (1984) "Conformal invariance, unitarity, and critical exponents in two dimensions" PRL 52, 1575
- Wess, J., Zumino, B. (1971) "Consequences of anomalous Ward identities" Phys. Lett. B 37, 95
- Witten, E. (1984) "Non-abelian bosonization in two dimensions" Comm. Math. Phys. 92, 455
- Knizhnik, V. G., Zamolodchikov, A. B. (1984) "Current algebra and Wess-Zumino model in two dimensions" Nucl. Phys. B 247, 83
- Cappelli, A., Itzykson, C., Zuber, J.-B. (1987) "The A-D-E classification of minimal and A_1^(1) conformal invariant theories" Comm. Math. Phys. 113, 1
- Goddard, P., Olive, D. (1986) "Kac-Moody and Virasoro algebras in relation to quantum physics" Int. J. Mod. Phys. A 1, 303
- Maldacena, J. M. (1998) "The large N limit of superconformal field theories and supergravity" Adv. Theor. Math. Phys. 2, 231
- Cardy, J. L. (1989) "Operator content and modular properties of higher dimensional conformal field theories" Nucl. Phys. B 270, 186
- Strominger, A., Vafa, C. (1996) "Microscopic origin of the Bekenstein-Hawking entropy" Phys. Lett. B 379, 99 (BH = Cardy)
- Di Francesco, P., Mathieu, P., Sénéchal, D. (1997) Conformal Field Theory. Springer
- Ginsparg, P. (1988) "Applied conformal field theory" arXiv:hep-th/9108028
