# Phase 123: AdS/CFT BH + Hawking-Page 相転移 + Bekenstein Bound + Holographic Complexity

> **Tier 1 #18 Black Holes — Phase 5/8 (Block A paper 2/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 123 の目的

Phase 119-122 で BH の古典・量子・情報パラドックスを扱った。Phase 123 では **AdS/CFT 文脈での BH** を深掘りし、**3 つの重要概念**を ITU 公理に統合する。

確立する内容:

1. **AdS-Schwarzschild BH の熱力学**: 自由エネルギー、温度、相転移
2. **Hawking-Page 相転移 (1983)**: 純 AdS ↔ AdS-BH の 1st order 転移
3. **Bekenstein bound**: S ≤ 2π R E / (ℏc) (1981)
4. **Holographic entanglement entropy 詳細** (Phase 111 の続き)
5. **Holographic complexity** (Susskind 2014 + Stanford-Susskind 2014)
6. **CV vs CA conjectures**

中心テーゼ:

> **AdS/CFT BH 物理 = ITU 公理 δS = δ⟨K⟩ の最高次対応**。
> Hawking-Page = K-state の **1st order 相転移**。
> Bekenstein bound = K-flow の **maximum entropy density**。
> Holographic complexity C = K-flow の **計算量距離** in モジュラー空間。

---

## 1. AdS-Schwarzschild BH

### 1.1 計量 (d+1 次元 AdS)

```
ds² = -f(r) dt² + dr²/f(r) + r² dΩ_{d-1}²
f(r) = 1 + r²/L_AdS² - r_s^{d-2}/r^{d-2}
```

- L_AdS: AdS curvature radius
- r_s: Schwarzschild parameter (mass ∝ r_s^{d-2})

### 1.2 horizon

f(r_h) = 0 → r_h は通常 2 つの解 (small/large BH)。**Large BH** が thermodynamically 安定。

### 1.3 温度

```
T = (1 / 4π) df/dr |_{r=r_h} = (d-2)/(4π r_h) + d r_h/(4π L_AdS²)
```

小 BH (r_h ≪ L_AdS): T ≈ (d-2)/(4π r_h) → **小さいほど熱い** (Schwarzschild と同じ)
大 BH (r_h ≫ L_AdS): T ≈ d r_h / (4π L_AdS²) → **大きいほど熱い** (新たな regime)

T が最小となる **r_h_min** = √((d-2)/d) × L_AdS、最小温度 T_min。

---

## 2. Hawking-Page 相転移 (1983)

### 2.1 自由エネルギー F = M - T S

```
F_BH(T) = ... (function of T)
F_pure_AdS = 0 (thermal AdS)
```

- 温度 T < T_HP: F_BH > 0 → thermal AdS dominant
- 温度 T > T_HP: F_BH < 0 → AdS-BH dominant

### 2.2 相転移温度 (4-dim AdS)

```
T_HP = (d-1) / (2π L_AdS)
```

4D AdS (d=4): T_HP = 3/(2π L_AdS)。

### 2.3 CFT 解釈 (Witten 1998)

AdS-BH 相 ↔ CFT confinement-deconfinement transition:

- 低温: confined phase (light hadrons)
- 高温: deconfined phase (BH thermal state)

### 2.4 ITU 視点

Hawking-Page = K-state の **1st order 相転移**:

- 低温 K-flow: K_AdS_thermal (small entropy density)
- 高温 K-flow: K_BH (high entropy density)
- 相転移 = K_AdS と K_BH の自由エネルギーが交差する点

---

## 3. Bekenstein Bound (1981)

### 3.1 公式

任意の物理系について:

```
S ≤ 2π k_B R E / (ℏ c)
```

- R: 系の特性長
- E: 系の総エネルギー

### 3.2 BH での saturation

Schwarzschild BH で:

```
R = r_s = 2 G M / c²
E = M c²
S = 2π k_B × (2 G M / c²) × M c² / (ℏ c) = 4π G M² k_B / (ℏ c)
  = A / (4 ℓ_P² k_B) (Bekenstein-Hawking)
```

⇒ **BH は Bekenstein bound を saturate**。

### 3.3 物理的意味

- BH = **maximum entropy density 物体**
- 同じ体積で BH より高 entropy の物体は存在不可能 (古典的)
- ITU 視点: K-flow の **最大密度上限**

### 3.4 量子情報的解釈

```
N_bits ≤ S / log 2 = 2π R E / (ℏ c log 2)
```

- 与えられた R, E で encode 可能な最大情報量
- BH = ユニバーサル "hard disk"

---

## 4. Holographic Entanglement Entropy 詳細

### 4.1 Ryu-Takayanagi (Phase 111 復習)

```
S(A) = Area(γ_A) / (4 G_N)
```

### 4.2 HRT 動的拡張 (Hubeny-Rangamani-Takayanagi 2007)

時間依存:

```
S(A) = ext_X Area(X) / (4 G_N)
```

X = extremal surface (codim-2, time-dependent OK)。

### 4.3 QES (Engelhardt-Wall 2014)

量子補正:

```
S(A) = min ext [Area(X)/(4G_N) + S_bulk(Σ_X)]
```

(Phase 113 と一致)

### 4.4 Mutual Information

```
I(A:B) = S(A) + S(B) - S(A∪B)
```

両 boundary 領域間。bulk minimal surface の組み合わせで計算。

### 4.5 Phase transition

I(A:B) には **mutual information phase transition** あり:
- 近距離: I > 0 (entanglement あり)
- 遠距離: I = 0 (disconnected RT surfaces)

---

## 5. Holographic Complexity

### 5.1 動機 (Susskind 2014)

エンタングルメントエントロピーは Page time 後に飽和するが、bulk **wormhole 長**は伸び続ける → 飽和しない新しい不変量が必要。

⇒ **Computational complexity** が候補。

### 5.2 CV Conjecture (Complexity = Volume)

```
C_V(t) = Vol(Σ_t) / (G_N L_AdS)
```

- Σ_t = bulk codim-1 maximal volume slice at boundary time t

### 5.3 CA Conjecture (Complexity = Action)

```
C_A(t) = I_WDW / (π ℏ)
```

- I_WDW = on-shell action of Wheeler-DeWitt patch

### 5.4 線形成長

両 conjecture とも、TFD 状態で:

```
dC/dt = (2 M) / (π ℏ) (large t)
```

→ Lloyd's bound (computational speed) と一致。

### 5.5 ITU 視点

Holographic complexity = **K-flow modular space での distance**:

- C(t) = ∫ ||δK_t|| dt
- 飽和しない量 = K-state の **dynamical irreversibility**

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **AdS-Schwarzschild の T vs r_h プロット**: T_min を確認
2. **Hawking-Page 相転移**: F_BH(T) の zero crossing
3. **Bekenstein bound vs BH actual entropy**: saturation 検証
4. **Holographic complexity 線形成長**: dC/dt ~ 2M
5. **Lloyd's bound 比較**: dC/dt ≤ 2E/πℏ

---

## 7. Phase 123 主結論

1. **AdS-Schwarzschild**: 温度 T(r_h) = (d-2)/(4π r_h) + d r_h/(4π L²)、T_min で最小化
2. **Hawking-Page 相転移**: T_HP = (d-1)/(2π L_AdS)、CFT confinement-deconfinement
3. **Bekenstein bound**: S ≤ 2π k_B R E / (ℏ c)、BH で saturation
4. **Holographic complexity**: C_V or C_A、Lloyd's bound と整合
5. **ITU 統合**: AdS/CFT BH = K-flow の最高次対応
6. **次の Phase 124** で **BH information observable + Maxwell daemon + 量子計算 BH**

---

## 8. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| AdS-Schwarzschild T_min | K-flow 温度極値 |
| Hawking-Page transition | K-state 1st order 相転移 |
| Bekenstein bound | K-flow max density |
| RT/HRT/QES | K_geom 階層的精緻化 |
| Holographic complexity | K-modular space distance |
| Lloyd's bound | K-flow computational speed |

---

## 引用

```
Terada, M. (2026). Phase 123: AdS/CFT BH, Hawking-Page transition,
Bekenstein bound, and holographic complexity in ITU (Tier 1 #18
phase 5/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Hawking, S. W., Page, D. N. (1983) "Thermodynamics of black holes in anti-de Sitter space" Commun. Math. Phys. 87, 577
- Bekenstein, J. D. (1981) "Universal upper bound on the entropy-to-energy ratio for bounded systems" PRD 23, 287
- Hubeny, V., Rangamani, M., Takayanagi, T. (2007) "A covariant holographic entanglement entropy proposal" JHEP 07, 062
- Susskind, L. (2014) "Computational complexity and black hole horizons" Fortsch. Phys. 64, 24 (arXiv:1402.5674)
- Stanford, D., Susskind, L. (2014) "Complexity and shock wave geometries" PRD 90, 126007 (arXiv:1406.2678)
- Brown, A., Roberts, D., Susskind, L., Swingle, B., Zhao, Y. (2016) "Holographic Complexity Equals Bulk Action?" PRL 116, 191301
- Lloyd, S. (2000) "Ultimate physical limits to computation" Nature 406, 1047
- Witten, E. (1998) "Anti-de Sitter space, thermal phase transition, and confinement in gauge theories" Adv. Theor. Math. Phys. 2, 505
