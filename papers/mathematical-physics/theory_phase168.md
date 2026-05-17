# Phase 168: Soliton + Lax Pair + KdV + sine-Gordon + 厳密可解模型 + K_int

> **Tier 1 #24 Mathematical Physics — Phase 2/8 (Block A paper 8/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 168 の目的

Phase 167 で Lie 群論 (K_sym 静的) を扱った。Phase 168 では **動的** な可積分系へ:

1. **Soliton** (Russell 1834 観測, Korteweg-de Vries 1895)
2. **KdV 方程式** + **Inverse Scattering Transform** (Gardner-Greene-Kruskal-Miura 1967)
3. **Lax pair** (1968)
4. **sine-Gordon + NLS** 方程式
5. **Toda lattice** + 量子可積分 (Yang-Baxter, Bethe ansatz)
6. **ITU 視点**: K_int = K_sym + 無限保存量

中心テーゼ:

> **可積分系 = K_int = 無限保存量を持つ K_sym 拡張**。
> Lax pair = K_int spectral problem の対称性表現。
> Soliton = K_int の particle-like 非線形 wave。

---

## 1. ★ Soliton 歴史 ★

### 1.1 Russell 1834 観測

スコットランドの運河で **形を変えずに進む波** を発見:
- 速度: √(g h) × (1 + a/h)^{1/2}
- 形: sech² プロファイル
- 衝突後も保存

### 1.2 KdV 方程式 (1895)

```
∂u/∂t + 6 u ∂u/∂x + ∂³u/∂x³ = 0
```

= 浅水波の非線形分散方程式。

### 1.3 1-soliton 解

```
u(x, t) = (c/2) sech²[(√c/2)(x - ct - x_0)]
```

= 速度 c に比例した振幅 + 速度 c で進む単独波。

### 1.4 ITU 視点

```
Soliton = K_int particle-like non-linear wave
KdV = K_int の prototype 方程式
```

---

## 2. ★ Inverse Scattering Transform (Gardner-Greene-Kruskal-Miura 1967) ★

### 2.1 戦略

非線形 PDE を **線形** な散乱問題に翻訳:

```
KdV → Schrödinger 散乱問題 (potential u(x,t))
時間発展は spectral data の 線形 evolution
逆散乱で u(x,t) 復元
```

### 2.2 4-step 解法

1. 初期 u(x,0) → 散乱 data S(0) = {κ_n, c_n, R(k)}
2. spectral data の線形時間発展: S(t)
3. 逆散乱: GLM (Gel'fand-Levitan-Marchenko) 積分方程式
4. u(x, t) 復元

### 2.3 ITU 視点

```
IST = K_int の linearization 戦略
spectral data = K_int conserved invariants
```

---

## 3. ★ Lax pair (1968) ★

### 3.1 形式

```
∂L/∂t = [M, L] = ML - LM
```

L, M: 演算子。

### 3.2 帰結

L の固有値 (spectrum) は時間不変 → **無限保存量**:

```
I_n = tr(L^n) = const
```

### 3.3 KdV の Lax pair

```
L = -∂²_x + u(x,t)   (Schrödinger)
M = -4 ∂³_x + 6 u ∂_x + 3 ∂_x u
```

[M, L] = -u_t + 6 u u_x + u_xxx = 0 ⇒ KdV。

### 3.4 ITU 視点

```
Lax pair = K_int spectral representation
無限保存量 I_n = K_int の Cartan 拡張
```

---

## 4. ★ sine-Gordon 方程式 ★

### 4.1 式

```
∂²φ/∂t² - ∂²φ/∂x² + sin φ = 0
```

### 4.2 ★ ソリトン (kink) 解 ★

```
φ_kink(x, t) = 4 arctan[exp(γ(x - vt))]
γ = 1/√(1 - v²)
```

= **topological** soliton (位相数 ±1)。

### 4.3 場の理論 + 双対性

```
sine-Gordon ↔ Thirring model (Coleman 1975)
boson ↔ fermion 双対性 (= bosonization)
```

### 4.4 物理応用

- Josephson junction (Phase 153 接続)
- pendulum chain
- DNA torsion
- crystal dislocation

### 4.5 ITU 視点

```
sine-Gordon kink = K_int topological soliton
S-G ↔ Thirring 双対 = K_int bosonization
```

---

## 5. ★ NLS (Non-linear Schrödinger) ★

### 5.1 式

```
i ∂ψ/∂t + ∂²ψ/∂x² + 2|ψ|² ψ = 0
```

= focusing NLS。逆符号で defocusing。

### 5.2 1-soliton 解

```
ψ(x,t) = η sech[η(x - 2ξt)] exp[i(ξ(x - 2ξt) + (η² + ξ²)t)]
```

### 5.3 物理応用

- 光ファイバ通信 (光ソリトン Hasegawa-Tappert 1973)
- 水波 (Stokes wave instability)
- BEC (Phase 144 接続)
- プラズマ Langmuir wave

### 5.4 ITU 視点

```
NLS = K_int focusing soliton
Optical soliton = K_int 工学応用 (Tier 1 #14 Comm)
```

---

## 6. Toda Lattice (1967)

### 6.1 ハミルトニアン

```
H = Σ p_n²/2 + Σ exp(q_n - q_{n+1})
```

= 指数ポテンシャル連結粒子鎖。

### 6.2 Flaschka 変換

```
a_n = (1/2) exp((q_n - q_{n+1})/2)
b_n = -p_n/2
```

→ Lax pair で完全可積分が証明 (Flaschka 1974)。

### 6.3 ITU 視点

```
Toda = K_int 離散可積分系
```

---

## 7. ★ 量子可積分系 ★

### 7.1 Yang-Baxter 方程式

```
R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)
```

= 3-粒子散乱の **factorize** 条件。

### 7.2 Bethe ansatz (1931)

Heisenberg XXX spin chain の厳密解:
```
|ψ⟩ = Σ A(k_1, ..., k_N) |k_1, ..., k_N⟩
```

ki が **Bethe 根** (連立方程式の解)。

### 7.3 例: Heisenberg XXX (Phase 154 接続)

```
H = -J Σ S_i · S_{i+1}
```

(Phase 154 で magnon 分散を扱った)。

Bethe ansatz で完全に解ける (1D XXX チェイン)。

### 7.4 ITU 視点

```
Yang-Baxter = K_int の braiding consistency
Bethe ansatz = K_int の exact eigenstate construction
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **KdV 1-soliton** 数値発展 (固有形保存)
2. **KdV 2-soliton 衝突** (形保存 + phase shift)
3. **sine-Gordon kink** topological 数 ±1
4. **NLS bright soliton** focusing
5. **Toda lattice** 数粒子 energy 保存
6. **Yang-Baxter R-matrix** 6-vertex (Heisenberg XXX)

---

## 9. Phase 168 主結論

1. **Russell 1834**: 運河 soliton 発見
2. **KdV 1895**: 浅水波 非線形分散方程式
3. **IST 1967 (GGKM)**: KdV を **線形** 散乱問題に
4. **Lax pair 1968**: ∂L/∂t = [M, L] → 無限保存量
5. **sine-Gordon kink**: topological soliton (Coleman 双対 Thirring)
6. **NLS**: 光ファイバ + BEC ソリトン
7. **Toda lattice**: 離散可積分 (Flaschka 1974)
8. **Yang-Baxter + Bethe ansatz**: 量子可積分
9. **ITU**: K_int = K_sym + 無限保存量 (Cartan 拡張)
10. **次の Phase 169** で **Yang-Mills + Clay Millennium mass gap**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Soliton | K_int particle-like non-linear wave |
| KdV | K_int prototype 方程式 |
| IST | K_int linearization 戦略 |
| Lax pair | K_int spectral representation |
| 無限保存量 I_n | K_int Cartan 拡張 |
| sine-Gordon kink | K_int topological soliton |
| Thirring 双対 | K_int bosonization |
| NLS | K_int focusing wave packet |
| Toda lattice | K_int 離散可積分 |
| Yang-Baxter | K_int braiding consistency |
| Bethe ansatz | K_int exact eigenstate |

---

## 引用

```
Terada, M. (2026). Phase 168: Solitons, Lax pair, KdV, sine-Gordon, and exactly
solvable models in ITU (Tier 1 #24 phase 2/8). Zenodo. DOI: [10.5281/zenodo.20251178](https://doi.org/10.5281/zenodo.20251178).
```

主要参考文献:
- Russell, J. S. (1844) "Report on waves" Brit. Assoc. Adv. Sci. 14, 311
- Korteweg, D. J., de Vries, G. (1895) "On the change of form of long waves..." Phil. Mag. 39, 422
- Zabusky, N. J., Kruskal, M. D. (1965) "Interaction of solitons in a collisionless plasma" PRL 15, 240
- Gardner, C. S., Greene, J. M., Kruskal, M. D., Miura, R. M. (1967) "Method for solving the Korteweg-deVries equation" PRL 19, 1095
- Lax, P. D. (1968) "Integrals of nonlinear equations of evolution and solitary waves" CPAM 21, 467
- Coleman, S. (1975) "Quantum sine-Gordon equation as the massive Thirring model" PRD 11, 2088
- Hasegawa, A., Tappert, F. (1973) "Transmission of stationary nonlinear optical pulses in dispersive dielectric fibers I" Appl. Phys. Lett. 23, 142
- Toda, M. (1967) "Vibration of a chain with nonlinear interaction" J. Phys. Soc. Jpn. 22, 431
- Flaschka, H. (1974) "The Toda lattice II. Existence of integrals" PRB 9, 1924
- Yang, C. N. (1967) "Some exact results for the many-body problem in one dimension..." PRL 19, 1312
- Baxter, R. J. (1972) "Partition function of the eight-vertex lattice model" Ann. Phys. 70, 193
- Bethe, H. (1931) "Zur Theorie der Metalle. I. Eigenwerte und Eigenfunktionen der linearen Atomkette" Z. Phys. 71, 205
- Faddeev, L. D., Sklyanin, E. K., Takhtajan, L. A. (1979) "Quantum inverse problem method I" TMP 40, 688
- Drinfeld, V. G. (1986) "Quantum groups" Proc. ICM Berkeley, 798
- Ablowitz, M. J., Segur, H. (1981) Solitons and the Inverse Scattering Transform. SIAM
