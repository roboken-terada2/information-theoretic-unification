# Phase 112: ER=EPR + 情報パラドックス + thermofield double

> **Tier 1 #17 Quantum Gravity — Phase 2/8 (Block A)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 112 の目的

Phase 111 で AdS/CFT と RT 公式により ITU 公理の幾何実現を確立。Phase 112 では、より深い等価性 **ER=EPR** (Maldacena-Susskind 2013) を扱う。

確立する内容:

1. **ER=EPR 予想**: エンタングルメント (EPR) ↔ Einstein-Rosen bridge (ER)
2. **Thermofield double (TFD) 状態**: 2 つの CFT の最大エンタングル状態 = AdS-Schwarzschild bulk
3. **情報パラドックス**: Hawking 1976 vs Susskind 1993 の対立、ITU での解決方針
4. **K-flow の non-local geometry encoding**

中心テーゼ:

> **エンタングルメント = 時空の縫合**。
> ITU 公理 δS = δ⟨K⟩ の K_A^(0) が、空間的に離れた領域間で **共通の幾何**を符号化する。
> TFD: |TFD⟩ = Σ_n e^{-βE_n/2} |n⟩_L ⊗ |n⟩_R = 2 つの CFT が「両側 AdS BH」を共有。
> Page curve (Phase 113) で具体的時間発展を扱う。

---

## 1. ER=EPR 予想 (Maldacena-Susskind 2013)

### 1.1 主張

> 任意の量子もつれ状態は、双対重力描像で **何らかの形の wormhole** (Einstein-Rosen bridge) に対応する。

具体例:
- 最大もつれ 2 粒子 = 1 本の microscopic ER bridge
- TFD 状態 = 巨大な eternal AdS-Schwarzschild wormhole

### 1.2 ITU 視点での再解釈

ITU 公理:

```
δS(ρ_AB) = δ Tr[K_AB^(0) ρ_AB]
```

A と B が空間的に分離していても、ρ_AB が entangled なら **K_AB^(0) が non-trivial な non-local 構造**を持つ。
この非局所構造が **bulk の wormhole 幾何**として実現される。

```
entanglement (boundary)  ⟺  geometry (bulk)
```

### 1.3 ER=EPR の「双対性」

| boundary 描像 | bulk 描像 |
|---|---|
| 2 CFT の entanglement | bulk wormhole |
| EPR 相関 | ER bridge |
| ρ_AB の Schmidt decomposition | bulk minimal surface |
| K_AB^(0) の non-local 構造 | bulk metric |

---

## 2. Thermofield Double (TFD) 状態

### 2.1 定義

2 つの CFT (L, R) のエンタングル状態:

```
|TFD(β)⟩ = (1/√Z) Σ_n e^{-βE_n/2} |n⟩_L ⊗ |n⟩_R
```

- β: 逆温度
- Z = Σ_n e^{-βE_n}: 分配関数
- ρ_L = Tr_R |TFD⟩⟨TFD| = e^{-βH_L}/Z = thermal state

### 2.2 TFD の双対 bulk = eternal AdS-Schwarzschild

```
ds² = -f(r) dt² + dr²/f(r) + r² dΩ²,    f(r) = 1 - r_h^{d-1}/r^{d-1}
```

2 つの境界 (L, R) を持ち、間に black hole horizon (面積 A_h、温度 T = 1/β)。

### 2.3 entanglement entropy

```
S(TFD) = S_BH = A_h / (4 G_N)
```

⇒ **TFD の絡み合い度 = black hole エントロピー**。

### 2.4 ITU 公理での確認

```
δ S(TFD) = δ A_h / (4 G_N) = δ ⟨K_geom⟩
```

K_geom は両側 CFT に対し対称な boost 生成元 (Bisognano-Wichmann)。

---

## 3. 情報パラドックス

### 3.1 Hawking 1976 の主張

ブラックホール蒸発後の状態は **混合状態** (thermal) → 純粋状態 → 混合状態の遷移を意味し、量子力学のユニタリ性を破る。

### 3.2 't Hooft 1985 / Susskind 1993 の応答

ブラックホールは **量子情報を保持**しているはず:
- Bekenstein-Hawking エントロピー S_BH = A/(4G_N) = ブラックホールの状態数 log
- 蒸発過程は **ユニタリ**であるべき

### 3.3 ITU 視点

ITU 公理 δS = δ⟨K⟩ は **ユニタリ進化のもとで成立**。
ブラックホール蒸発も ITU 公理に従うなら、Hawking 放射と内部状態の relative entropy が時間とともに減少 → 情報は放射に符号化される。

### 3.4 Page curve (次回 Phase 113 で詳細)

ブラックホール内部 (S_BH) と Hawking 放射 (S_R) の関係:

```
t < t_Page: S_R(t) ↑ (放射は熱的に見える)
t = t_Page = t_evap / 2: S_R は最大値 = S_BH(0)/2 に到達
t > t_Page: S_R(t) ↓ (情報が放射に戻る)
```

---

## 4. K-flow の non-local geometry encoding

### 4.1 通常領域での K_A^(0)

連結領域 A について、Bisognano-Wichmann:

```
K_A^(0) = 2π × ∫_A x^⊥ T_{00}(x) d^{d-1}x
```

これは local な boost 生成元。

### 4.2 非連結 A∪B (entangled の場合)

A と B が空間的に分離していても entangled なら:

```
K_{A∪B}^(0) ≠ K_A^(0) + K_B^(0)
```

非局所項が現れ、これが **bulk wormhole 幾何**として実現される (ER=EPR)。

### 4.3 ITU の予言

ITU は **modular Hamiltonian の非局所成分**を直接予言する。これは:
- bulk: wormhole geometry
- boundary: cross-region modular flow

として観測可能。

---

## 5. Phase 112 の数値検証項目

本 phase の simulation で確認:

1. **TFD 状態の構築**: 2 量子ビット系で |TFD(β)⟩ を作り、ρ_L が thermal であることを確認
2. **TFD entropy と BH エントロピーの対応**: S_TFD = (β/2) ⟨H⟩ - (1/2) log Z の数値計算
3. **ER=EPR エネルギー対応**: entanglement 量 vs 想定 ER bridge 質量
4. **情報パラドックス示唆**: Hawking thermal vs unitary 解像

---

## 6. Phase 112 主結論

1. **ER=EPR (Maldacena-Susskind 2013)**: entanglement ↔ wormhole
2. **TFD 状態**: |TFD(β)⟩ = Σ e^{-βE_n/2} |n⟩_L⊗|n⟩_R = eternal AdS-Schwarzschild bulk
3. **TFD entropy = BH entropy**: S(TFD) = A_h/(4G_N) = ⟨K_geom⟩
4. **情報パラドックス**: Hawking 1976 vs ユニタリ性 → ITU 解像方針
5. **ITU 公理**: 非局所 K_A^(0) が bulk wormhole 幾何を符号化
6. **次の Phase 113** で **Page curve + Island formula** に進む

---

## 7. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| ER=EPR | K_A^(0) の非局所成分 = bulk 幾何 |
| TFD | 最大エンタングル ↔ eternal BH |
| 情報パラドックス | ITU ユニタリ進化での再評価 |
| Page curve | K_BH(t) の二段階発展 |
| Island formula | bulk-boundary K-flow 縫合 (Phase 113-115) |

---

## 引用

```
Terada, M. (2026). Phase 112: ER=EPR, thermofield double, and the
information paradox in ITU. Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Maldacena, J., Susskind, L. (2013) "Cool horizons for entangled black holes" Fortsch. Phys. 61, 781 (arXiv:1306.0533)
- Israel, W. (1976) "Thermo-field dynamics of black holes" Phys. Lett. A 57, 107
- Maldacena, J. (2001) "Eternal black holes in anti-de Sitter" JHEP 04, 021 (arXiv:hep-th/0106112)
- Hawking, S. W. (1976) "Breakdown of predictability in gravitational collapse" PRD 14, 2460
- 't Hooft, G. (1985) "On the quantum structure of a black hole" Nucl. Phys. B 256, 727
- Susskind, L., Thorlacius, L., Uglum, J. (1993) "The stretched horizon and black hole complementarity" PRD 48, 3743
