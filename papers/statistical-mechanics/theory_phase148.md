# Phase 148: 情報理論 — Shannon + Jaynes 最大エントロピー + K_info ↔ K_stat

> **Tier 1 #21 Statistical Mechanics — Phase 6/8 (Block A paper 5/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 148 の目的

Phase 143-147 で熱統計力学 (古典 + 量子 + 相転移 + 非平衡 + 揺動定理) を扱った。Phase 148 では **情報理論との統合** に進む:

1. **Shannon 情報量 (1948)**: H = -Σ p log p
2. **Jaynes 最大エントロピー原理 (1957)**
3. **Boltzmann S = k_B ln Ω と Shannon H の関係**
4. **相互情報量 (mutual information) と Kullback-Leibler 距離**
5. **量子情報理論 (von Neumann S = -Tr ρ log ρ)**
6. **ITU 視点**: K_stat ↔ K_info の **isomorphism**

中心テーゼ:

> **熱力学エントロピー S_thermo = k_B × 情報エントロピー H_Shannon** (適切な確率分布で)。
> Jaynes 最大エントロピー = ITU K-state を constraint だけから選ぶ universal 原理。
> **ITU = K_stat と K_info の統合**: 物理は情報の動力学。

---

## 1. ★ Shannon 情報量 (1948) ★

### 1.1 定義

```
H[p] = -Σ_i p_i log p_i

(bits if log_2, nats if ln)
```

### 1.2 性質

- **非負**: H ≥ 0
- **最大**: uniform 分布で H_max = log N
- **加法性**: H[X, Y] = H[X] + H[Y | X]
- **凹性** in p

### 1.3 例

| 分布 | H (nats) | H (bits) |
|---|---|---|
| Coin (fair) | ln 2 = 0.693 | 1 |
| Coin (biased p=0.9) | 0.325 | 0.469 |
| 6-面 die (fair) | ln 6 = 1.792 | 2.585 |

### 1.4 ITU 視点

```
Shannon H[p] = ITU K_info の log-occupation measure
S_thermo = k_B H_Shannon (Boltzmann constant が unit conversion)
```

---

## 2. ★ Jaynes 最大エントロピー (1957) ★

### 2.1 主張

確率分布 p を **既知の制約のみ** から推定する場合、**H[p] を最大化する分布** を選ぶ。

### 2.2 古典統計力学の導出

Microcanonical (E fixed):
```
max H subject to Σ p_i = 1, ⟨E⟩ = E_0
→ p_i = 1/Ω = uniform on shell  (Boltzmann)
```

Canonical (T fixed):
```
max H subject to Σ p_i = 1, ⟨E⟩ = U
→ p_i = e^(-βE_i) / Z  (Gibbs)
```

Grand canonical:
```
max H subject to Σ p_i = 1, ⟨E⟩ = U, ⟨N⟩ = N̄
→ p_i = e^(-β(E_i - μN_i)) / Ξ
```

### 2.3 Lagrange multiplier

```
L = -Σ p_i log p_i - α(Σ p_i - 1) - β(Σ p_i E_i - U)

∂L/∂p_i = 0  →  p_i = exp(-1 - α - β E_i)
```

⇒ β = 1/(k_B T), α = log Z - 1。

### 2.4 ITU 視点

```
Jaynes Max-Ent = ITU K-state を 与えられた制約 のみから 一意 に決定
constraint = ⟨K_obs⟩ (observable mean)
```

---

## 3. ★ Boltzmann ↔ Shannon の対応 ★

### 3.1 関係式

```
S_Boltz = k_B ln Ω      (microcanonical, equally probable)
        = k_B × (-Σ p_i ln p_i)
        = k_B × H_Shannon
```

(uniform p_i = 1/Ω なら Σ p_i ln p_i = -ln Ω)。

### 3.2 一般化 Gibbs

```
S_Gibbs = -k_B Σ p_i ln p_i = k_B H_Shannon
```

### 3.3 単位変換

```
1 bit = k_B ln 2 ≈ 1.38e-23 × 0.693 ≈ 9.57e-24 J/K
1 nat = k_B ≈ 1.38e-23 J/K
```

### 3.4 ITU 視点

```
ITU 公理: δS = δ⟨K⟩  (Tier 0)
古典統計力学: S = k_B H[p]
⇒ K_stat = K_info × k_B (単位変換)
```

⇒ **K_stat と K_info は同一概念の物理単位/情報単位 表現**。

---

## 4. 相互情報量と Kullback-Leibler

### 4.1 KL 発散

```
D_KL[p || q] = Σ p_i log(p_i / q_i)

D_KL ≥ 0, = 0 iff p = q  (Gibbs inequality)
```

### 4.2 相互情報量

```
I[X; Y] = D_KL[p(x, y) || p(x) p(y)]
       = H[X] + H[Y] - H[X, Y]
```

**統計的依存性の尺度**。

### 4.3 例: 熱浴と系

```
I[系 ; 浴] ∝ 相関の強さ
熱平衡接触: 局所 I 増大
```

### 4.4 ITU 視点

```
D_KL = K_info の非対称距離 (発散)
I[X;Y] = ITU 二部 K-state 間の相関情報
```

---

## 5. ★ 量子情報理論 (von Neumann) ★

### 5.1 von Neumann エントロピー

```
S[ρ] = -Tr (ρ log ρ)

ρ: density matrix
```

### 5.2 古典極限

```
ρ = Σ p_i |i⟩⟨i|  (diagonal)
S = -Σ p_i log p_i  = Shannon H
```

### 5.3 純粋状態

```
ρ = |ψ⟩⟨ψ|  → S = 0
```

(完全に決定された量子状態は info 0)。

### 5.4 量子相互情報量

```
I(A : B) = S(ρ_A) + S(ρ_B) - S(ρ_AB)
```

絡み合い量子状態で I は古典 bound を超える。

### 5.5 ITU 視点

```
S[ρ] = ITU K_quantum の von Neumann measure
絡み合い = ITU 二部 K-state 間の non-separable 構造
```

---

## 6. データ圧縮と Channel capacity

### 6.1 Source coding theorem (Shannon)

最小平均符号長:
```
L_min = H[X] / log 2  (bits/symbol)
```

### 6.2 Channel coding theorem

Noisy channel での最大送信レート (capacity):
```
C = max I[X; Y]
```

### 6.3 Holevo bound (量子)

量子チャネルでの古典 info 送信:
```
χ ≤ S(ρ̄) - Σ p_i S(ρ_i)
```

### 6.4 ITU 視点

```
Channel capacity = K_info の transmission limit
Holevo bound = K_quantum の classical info extraction limit
```

---

## 7. Black hole 情報 paradox との接続

### 7.1 Bekenstein-Hawking entropy

```
S_BH = A / (4 ℓ_P²)  (in nats)
```

**情報量** として再解釈:
```
S_BH = k_B A / (4 ℓ_P²)  (J/K)
```

### 7.2 情報 paradox (Hawking 1976)

BH 蒸発で純粋状態 → mixed (S 増大?) ⇒ unitarity 違反?

### 7.3 解決 (Page curve, 2019-2020)

```
S_radiation(t) follows Page curve
→ unitary, info 保存
```

(Phase 122-124 参照)。

### 7.4 ITU 視点

```
S_BH = K_horizon の log-degeneracy
Page curve = K_horizon ↔ K_radiation entanglement
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Shannon H** 計算 (binary, ternary, ...)
2. **Jaynes Max-Ent** derivation: canonical e^{-βE}/Z
3. **KL 発散** の非対称性
4. **相互情報量** in correlated bivariate Gaussian
5. **von Neumann S** for entangled qubits
6. **Landauer limit** ↔ Shannon bit (Phase 147 と整合)

---

## 9. Phase 148 主結論

1. **Shannon (1948)**: H = -Σ p log p、加法性 + 凹性
2. **Jaynes (1957)**: Max-Ent から canonical 分布が自然導出
3. **Boltzmann S = k_B H**: 単位変換のみ
4. **KL 発散** D_KL[p || q]: 確率分布の非対称距離
5. **von Neumann S = -Tr ρ log ρ**: 量子情報の基本量
6. **Holevo bound**: 量子 channel capacity
7. **ITU**: K_stat ↔ K_info isomorphism (k_B が unit converter)
8. **次の Phase 149** で **複雑系 + active matter + 生命系**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Shannon H | K_info log-occupation measure |
| Jaynes Max-Ent | K-state を 制約 のみから一意決定 |
| Boltzmann S | k_B × K_info |
| KL 発散 | K_info 非対称距離 |
| von Neumann S | K_quantum log-density measure |
| Holevo bound | K_quantum → K_classical extraction limit |
| S_BH | K_horizon log-degeneracy |

---

## 引用

```
Terada, M. (2026). Phase 148: Information theory — Shannon, Jaynes, and the
K_info ↔ K_stat isomorphism in ITU (Tier 1 #21 phase 6/8). Zenodo. DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

主要参考文献:
- Shannon, C. E. (1948) "A mathematical theory of communication" Bell Syst. Tech. J. 27, 379 & 623
- Jaynes, E. T. (1957) "Information theory and statistical mechanics" Phys. Rev. 106, 620; 108, 171
- Boltzmann, L. (1877) "Über die Beziehung zwischen dem zweiten Hauptsatze..." Wien. Ber. 76, 373
- Kullback, S., Leibler, R. A. (1951) "On information and sufficiency" Ann. Math. Statist. 22, 79
- von Neumann, J. (1932) "Mathematische Grundlagen der Quantenmechanik" Springer
- Holevo, A. S. (1973) "Bounds for the quantity of information transmitted by a quantum communication channel" Probl. Inf. Transm. 9, 177
- Bekenstein, J. D. (1973) "Black holes and entropy" Phys. Rev. D 7, 2333
- Bennett, C. H., Shor, P. W. (1998) "Quantum information theory" IEEE Trans. Inf. Theor. 44, 2724
- Landauer, R. (1991) "Information is physical" Physics Today 44(5), 23
- Wheeler, J. A. (1990) "It from bit" Proc. Santa Fe 1989, 309
