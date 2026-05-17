# Phase 177: 計算複雑性 = 体積 / 作用 — Susskind Complexity Conjectures + K_complexity

> **Tier 1 #25 Information Geometry & Holography — Phase 3/8 (Block A paper 9/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 177 の目的

Phase 176 で holographic entropy bounds。Phase 177 では **計算複雑性 (computational complexity)** = 体積 / 作用:

1. **Susskind (2014)**: BH 内部 = computational growth
2. **Complexity = Volume (CV) conjecture** (Stanford-Susskind 2014)
3. **Complexity = Action (CA) conjecture** (Brown-Roberts-Susskind-Swingle-Zhao 2016)
4. **Lloyd bound** (Phase 176 接続)
5. **Scrambling time** t_scr = log S
6. **Switchback effect**
7. **Complexity = Anything** (Belin-Myers-Ruan-Sárosi-Speranza 2022)
8. **ITU 視点**: K_complexity = K_holo の dynamical depth

中心テーゼ:

> **Computational complexity = bulk geometric quantity (volume/action)**。
> Susskind: BH 内部の growth = 量子計算の "深さ"。
> Lloyd bound + Holography → universal computational speed limit。

---

## 1. ★ Computational Complexity 基本 ★

### 1.1 定義

quantum state |ψ⟩ を初期状態 |0⟩^⊗N から準備する **最小 gate 数**:

```
𝒞(|ψ⟩) = min # gates to construct |ψ⟩ from |0⟩^⊗N
```

universal gate set (Toffoli + Hadamard 等)。

### 1.2 主要 BH 系での値

| 系 | Complexity |
|---|---|
| Polynomial-time prepare | 𝒞 ~ poly(N) |
| Maximally complex | 𝒞 ~ 2^N (exponential) |
| **Random TFD state** | 𝒞 ~ exp(S) at t = O(S) |

### 1.3 ITU 視点

```
𝒞 = K_complexity の量
量子状態の preparation difficulty = K_info の dynamical depth
```

---

## 2. ★ Susskind (2014) ★

### 2.1 動機

AdS-Schwarzschild BH の **interior** は時間と共に growth 続ける:
- horizon area = const
- bulk **Einstein-Rosen bridge volume** ∝ t

⇒ boundary CFT 側で何が成長?
**Answer**: Complexity (Susskind 2014)。

### 2.2 主張

```
𝒞_CFT(t) ≈ V_ERB(t) / (G_N ℓ_AdS)
```

= **bulk volume と boundary complexity の比例**。

### 2.3 ITU 視点

```
Susskind = K_complexity ↔ K_geom volume duality
```

---

## 3. ★ Complexity = Volume (CV, 2014) ★

### 3.1 公式

```
𝒞_V = max V(Σ) / (G_N ℓ_AdS)
```

Σ: anchored maximal volume slice in bulk。

### 3.2 BH での挙動

```
ΔV/Δt = const (linear growth, late time)
⇒ d𝒞/dt = 2 M / π  (Lloyd-saturating rate!)
```

### 3.3 数値: Schwarzschild AdS

```
M = 1.4 × 10⁹ M_sun (M87 BH 想定)
d𝒞/dt ≈ 2Mc²/(πℏ) ≈ 5 × 10⁹³ ops/s
```

### 3.4 ITU 視点

```
CV = K_complexity の体積 representation
Late-time linear growth = K_holo の universal scrambling rate
```

---

## 4. ★ Complexity = Action (CA, 2016) ★

### 4.1 公式 (Brown-Roberts-Susskind-Swingle-Zhao)

```
𝒞_A = (S_WdW) / (π ℏ)
```

S_WdW = Wheeler-DeWitt patch (light-cone wedge in bulk) action。

### 4.2 BH での挙動

```
d𝒞_A/dt = 2M / (πℏ) at late time
```

**↑ ★ Lloyd bound 飽和** (Phase 176 接続)。

### 4.3 CV vs CA

| 性質 | CV | CA |
|---|---|---|
| 公式 | max volume | WdW action |
| Lloyd bound saturation | 2× だけ違い | exact |
| Switchback effect | OK | OK |
| 計算複雑性 | 一致 | 一致 |

### 4.4 ITU 視点

```
CA = K_complexity の action representation
Lloyd saturation = K_complexity universal rate
```

---

## 5. ★ Scrambling Time ★

### 5.1 主張 (Sekino-Susskind 2008)

BH は **fastest scrambler** in nature:

```
t_scr = (β / 2π) log S_BH
```

= **logarithmic in entropy**。

### 5.2 数値 (Phase 125 接続)

```
Sgr A*: S_BH ≈ 10^91 nats
t_scr ≈ (β / 2π) × 91 × ln 10 ≈ 0.3 ms × log scale
(actual: ~10⁻⁴ s for Sgr A*)
```

### 5.3 物理機構

OTOC (out-of-time-order correlator) ∝ e^{λ_L t}:
```
λ_L ≤ 2π / β (Maldacena-Shenker-Stanford 2016 bound)
BH saturates ⇒ chaotic systems の上限
```

= **Maximally chaotic** quantum systems。

### 5.4 ITU 視点

```
Scrambling = K_quantum information の diffusion rate
t_scr = K_holo の universal scrambling clock
```

---

## 6. ★ Switchback Effect ★

### 6.1 主張

complexity が **後戻り** (switchback) する場合:

```
𝒞(W₁ U(t) W₂ U(t)^†) = 𝒞 − 2 × |W| × t_scr  (approx)
```

W: 局所 perturbation。

### 6.2 物理意味

```
Black hole interior remembers
時間反転で complexity が "uncomputed"
```

### 6.3 ITU 視点

```
Switchback = K_complexity の reversibility 性質
```

---

## 7. ★ Complexity = Anything (2022) ★

### 7.1 主張 (Belin-Myers-Ruan-Sárosi-Speranza)

CV と CA だけでなく **無限族の bulk 観測量** が複雑性と同じ性質:

```
{F_n(geometry)} all satisfy complexity-like properties
```

⇒ "Complexity" = robust holographic 概念だが、precise 定義は **CV/CA の universality 後** に来る。

### 7.2 ITU 視点

```
Complexity = Anything = K_complexity の universality class
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **CV growth rate** d𝒞/dt = 2M/π for various BHs
2. **CA growth rate** = Lloyd bound saturation
3. **Scrambling time** t_scr = (β/2π) log S
4. **Maximally chaotic** λ_L = 2π/β saturation
5. **Complexity exponential growth** 𝒞 ~ exp(S) at late times

---

## 9. Phase 177 主結論

1. **Susskind (2014)**: BH 内部 = computational growth = boundary 複雑性
2. **CV = max V/(G_N ℓ_AdS)** (Stanford-Susskind 2014)
3. **CA = S_WdW/(πℏ)** (Brown-Roberts-Susskind-Swingle-Zhao 2016)
4. **Lloyd bound saturation**: d𝒞/dt = 2M/(πℏ) (CA)
5. **Scrambling time**: t_scr = (β/2π) log S_BH (Sekino-Susskind 2008)
6. **Maximally chaotic** bound: λ_L ≤ 2π/β (MSS 2016)
7. **Switchback effect**: 局所 perturb. + time-reverse → complexity decrease
8. **Complexity = Anything (2022)**: universal robust 概念
9. **ITU**: K_complexity = K_holo dynamical depth
10. **次の Phase 178** で **Tensor networks + MERA**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Computational complexity | K_complexity のメインターン |
| CV conjecture | K_complexity = K_geom volume |
| CA conjecture | K_complexity = K_geom action |
| Lloyd saturation | K_complexity universal rate |
| Scrambling time | K_holo time scale |
| Maximally chaotic | K_quantum chaos upper bound |
| Switchback | K_complexity reversibility |
| Complexity = Anything | K_complexity universality class |

---

## 引用

```
Terada, M. (2026). Phase 177: Computational complexity as holographic volume/action
— Susskind conjectures and Lloyd bound saturation in ITU
(Tier 1 #25 phase 3/8). Zenodo. DOI: 10.5281/zenodo.20253960.
```

主要参考文献:
- Susskind, L. (2016) "Computational complexity and black hole horizons" Fortsch. Phys. 64, 24 (originally 2014)
- Stanford, D., Susskind, L. (2014) "Complexity and shock wave geometries" PRD 90, 126007
- Brown, A. R., Roberts, D. A., Susskind, L., Swingle, B., Zhao, Y. (2016) "Holographic complexity equals bulk action?" PRL 116, 191301
- Maldacena, J., Shenker, S., Stanford, D. (2016) "A bound on chaos" JHEP 08, 106
- Sekino, Y., Susskind, L. (2008) "Fast scramblers" JHEP 10, 065
- Susskind, L. (2018) "Why do things fall?" arXiv:1802.01198
- Belin, A., Myers, R. C., Ruan, S. M., Sárosi, G., Speranza, A. J. (2022) "Does complexity equal anything?" PRL 128, 081602
- Susskind, L., Zhao, Y. (2018) "Switchbacks and the bridge to nowhere" JHEP 09, 130
- Carmi, D., Chapman, S., Marrochio, H., Myers, R. C., Sugishita, S. (2017) "On the time dependence of holographic complexity" JHEP 11, 188
- Lloyd, S. (2000) Nature 406, 1047
- Maldacena, J. (2013) "A simple quantum system that can be solved exactly" arXiv:1312.0533
- Penington, G., Shenker, S. H., Stanford, D., Yang, Z. (2022) JHEP 03, 205 (replica wormholes)
