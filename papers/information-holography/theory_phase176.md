# Phase 176: Holographic Entropy Bounds — Bekenstein + Bousso + RT + HRT + K_holo

> **Tier 1 #25 Information Geometry & Holography — Phase 2/8 (Block A paper 9/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 176 の目的

Phase 175 で情報幾何 (Fisher 計量) を扱った。Phase 176 では **エントロピー上限の系譜** に進む — 量子重力の核心:

1. **Bekenstein bound (1981)**: 体積 V 内 entropy ≤ A R E / (ℏc)
2. **'t Hooft holographic principle (1993)**: D-dim 物理 = (D-1)-dim 境界
3. **Susskind 拡張 (1995)**
4. **Bousso 共変 entropy bound (1999)**
5. **★ Ryu-Takayanagi (2006) ★**: S_A = Area(γ_A) / 4G
6. **HRT (Hubeny-Rangamani-Takayanagi 2007)**: 時間依存版
7. **Quantum extremal surface (Engelhardt-Wall 2014)**
8. **Page curve from island (2019-2020)**
9. **ITU 視点**: K_holo = K_info × K_geom hologram

中心テーゼ:

> **エントロピー = 境界面積 / 4G** (RT, ITU 公理 δS = δ⟨K_geom⟩ の幾何実現)。
> Bousso → RT → HRT → QES の階層 = K_holo の精緻化。
> Page curve from island = K_holo の量子重力 unitarity 保存。

---

## 1. ★ Bekenstein Bound (1981) ★

### 1.1 主張

体積 V (典型半径 R) 内に閉じ込められた quantum system のエントロピー:

```
S ≤ (2π R E) / (ℏ c)
```

E: 全エネルギー。

### 1.2 BH への応用

```
Schwarzschild: R = 2GM/c², E = Mc²
⇒ S_max = (2π × 2GM/c² × Mc²) / (ℏc)
        = 4πGM²/(ℏc) ★
```

= **Bekenstein-Hawking entropy** S_BH = A/(4Gℏc)。

### 1.3 ITU 視点

```
Bekenstein bound = K_info 上限 が K_geom (R, E) で決まる
```

---

## 2. ★ 't Hooft Holographic Principle (1993) ★

### 2.1 主張

D-dim 物理系のすべての情報は (D-1)-dim 境界に encoded:

```
S_max(volume) = S_max(boundary area) / (4 ℓ_P²)
```

### 2.2 Susskind 1995 拡張

弦理論で具体化 → AdS/CFT (Maldacena 1997, Phase 111) で完全実現。

### 2.3 ITU 視点

```
Holography = K_info volume ↔ K_geom boundary area (1:1 対応)
```

---

## 3. ★ Bousso Covariant Entropy Bound (1999) ★

### 3.1 主張

任意の **light-sheet** L からのエントロピー流束:

```
S(L) ≤ A(L) / (4 ℓ_P²)
```

A(L): light-sheet が囲む面積。

### 3.2 帰結

Bekenstein bound + holographic principle を **共変** に統一。

### 3.3 ITU 視点

```
Bousso bound = K_info covariant 上限
```

---

## 4. ★★ Ryu-Takayanagi (2006) ★★

### 4.1 主張

AdS/CFT で boundary region A の entanglement entropy:

```
S_A = Area(γ_A) / (4 G_N)
```

γ_A: A を boundary に持つ **bulk 最小面**。

### 4.2 検証

- 1+1D CFT で c log L → S_A = (c/3) log L ✓
- Holographic d-wave system での anomalous d 値 ✓
- AdS_3 で exact match with Cardy-Calabrese 1+1D CFT

### 4.3 数値: AdS_3 disk region

```
S_A = (c/3) log(L/a)
```

L: disk size, a: UV cutoff, c: central charge。

### 4.4 ITU 視点

```
RT formula = K_info (boundary entropy) = K_geom (bulk area / 4G)
            = ITU δS = δTr[K_geom ρ] (Phase 111 ITU 公理 geometric realisation)
```

---

## 5. ★ HRT — 共変版 (2007) ★

### 5.1 主張

時間依存 AdS/CFT で:

```
S_A(t) = Extr[Area(γ_A) / 4G]
```

= **extremal surface** 上の area (時間非対称含む)。

### 5.2 物理応用

- Black hole formation/evaporation
- Quench dynamics
- AdS-Schwarzschild 時間依存

### 5.3 ITU 視点

```
HRT = K_holo 動的版 (時間依存 K_geom area)
```

---

## 6. ★ Quantum Extremal Surface (Engelhardt-Wall 2014) ★

### 6.1 改良 RT

bulk 量子情報まで含めて:

```
S_A = min_γ [Area(γ)/4G + S_bulk(Σ)]
```

Σ: γ で囲まれた bulk region。

### 6.2 物理: Page curve

evaporating BH に対し QES = **island** (entanglement wedge 中の disconnected region) を考慮 → **Page curve 自然に出現** (Penington 2019, Almheiri-Engelhardt-Marolf-Maxfield 2019)。

### 6.3 数値 (Phase 113, 122 接続)

```
Page time: S(BH) → S(BH after t_Page) = S_BH/2
```

⇒ unitarity 保存。

### 6.4 ITU 視点

```
QES = K_holo の量子補正 (bulk entropy 含む)
Island = K_holo の disconnected component
Page curve = K_holo unitarity 保存
```

---

## 7. ★ Lloyd Bound (1999-2000) ★

### 7.1 主張

unit volume での **computational rate** 上限:

```
Operations/s ≤ 2 E / (π ℏ)
```

E: 体積内エネルギー。

### 7.2 数値 (1 kg of 1 m³ 体積)

```
E = m c² = 9×10¹⁶ J
Ops/s ≤ 2 × 9×10¹⁶ / (π × 10⁻³⁴) ≈ 5.7×10⁵⁰
```

= 任意の物理系の **計算能力上限**。

### 7.3 ITU 視点

```
Lloyd bound = K_info × K_quantum 計算速度上限
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Bekenstein bound** for various R, E
2. **BH entropy** S_BH = A/(4ℓ_P²) for Sgr A*, M87
3. **RT formula** AdS_3 disk: S = (c/3) log(L/a)
4. **Lloyd bound** for 1 kg, sun, observable universe
5. **Holographic principle** entropy density per Planck area

---

## 9. Phase 176 主結論

1. **Bekenstein (1981)**: S ≤ 2π R E / (ℏc)
2. **'t Hooft holographic (1993)** + Susskind (1995)
3. **Bousso (1999)**: covariant entropy bound on light-sheets
4. **★ Ryu-Takayanagi (2006) ★**: S_A = Area(γ_A) / 4G
5. **HRT (2007)**: 共変 extremal
6. **QES (Engelhardt-Wall 2014)**: + bulk entropy
7. **Page curve from island (2019-2020)**: unitarity 保存
8. **Lloyd (1999-2000)**: Operations/s ≤ 2E/(πℏ)
9. **ITU**: K_holo = K_info × K_geom; RT = ITU 公理 geometric
10. **次の Phase 177** で **計算複雑性 = 体積** (Susskind)

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Bekenstein bound | K_info ≤ K_geom 制約 |
| Holographic principle | K_info volume ↔ K_geom boundary |
| Bousso covariant | K_info light-sheet 上限 |
| **RT formula** | **K_info = K_geom area / 4G ★** |
| HRT | K_holo 動的拡張 |
| QES | K_holo + bulk K_info |
| Island formula | K_holo disconnected component |
| Page curve | K_holo unitarity 保存 |
| Lloyd bound | K_info × K_quantum 計算速度 |

---

## 引用

```
Terada, M. (2026). Phase 176: Holographic entropy bounds — Bekenstein, Bousso,
Ryu-Takayanagi, HRT, quantum extremal surfaces in ITU
(Tier 1 #25 phase 2/8). Zenodo. DOI: 10.5281/zenodo.20253960.
```

主要参考文献:
- Bekenstein, J. D. (1981) "Universal upper bound on the entropy-to-energy ratio for bounded systems" PRD 23, 287
- 't Hooft, G. (1993) "Dimensional reduction in quantum gravity" arXiv:gr-qc/9310026
- Susskind, L. (1995) "The world as a hologram" J. Math. Phys. 36, 6377
- Bousso, R. (1999) "A covariant entropy conjecture" JHEP 07, 004
- Maldacena, J. M. (1998) "The large N limit of superconformal field theories and supergravity" Adv. Theor. Math. Phys. 2, 231
- Ryu, S., Takayanagi, T. (2006) "Holographic derivation of entanglement entropy from anti-de Sitter space/conformal field theory correspondence" PRL 96, 181602
- Hubeny, V., Rangamani, M., Takayanagi, T. (2007) "A covariant holographic entanglement entropy proposal" JHEP 07, 062
- Engelhardt, N., Wall, A. C. (2015) "Quantum extremal surfaces" JHEP 01, 073
- Faulkner, T., Lewkowycz, A., Maldacena, J. (2013) "Quantum corrections to holographic entanglement entropy" JHEP 11, 074
- Penington, G. (2020) "Entanglement wedge reconstruction and the information paradox" JHEP 09, 002
- Almheiri, A., Engelhardt, N., Marolf, D., Maxfield, H. (2019) "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole" JHEP 12, 063
- Penington, G., Shenker, S. H., Stanford, D., Yang, Z. (2022) "Replica wormholes and the black hole interior" JHEP 03, 205
- Lloyd, S. (2000) "Ultimate physical limits to computation" Nature 406, 1047
- Bekenstein, J. D. (1973) "Black holes and entropy" PRD 7, 2333 (S_BH original)
