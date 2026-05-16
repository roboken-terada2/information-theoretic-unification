# Phase 113: Page Curve + Island Formula + Quantum Extremal Surface

> **Tier 1 #17 Quantum Gravity — Phase 3/8 (Block A)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 113 の目的

Phase 112 で情報パラドックスの概要と Page curve のスケッチを示した。Phase 113 で **Page curve を厳密に解析**し、その背後にある **Island formula** (Penington 2019, Almheiri-Engelhardt-Marolf-Maxfield 2019) を ITU 公理で再構築する。

確立する内容:

1. **Page curve の数学的構造**: Page (1993) average entropy of subsystems
2. **Quantum Extremal Surface (QES)**: Engelhardt-Wall 2014 の RT 一般化
3. **Island formula**: S(R) = min ext [Area(∂I)/(4G_N) + S_matter(R ∪ I)]
4. **Replica wormhole**: Penington-Shenker-Stanford-Yang 2019 によるユニタリ性回復
5. **ITU 視点**: K_BH(t) の二段階発展 と replica K-flow

中心テーゼ:

> **Page curve = ITU 公理 δS = δ⟨K⟩ の時間発展**。
> t < t_Page: K_geom 支配 (S_R = K_R growth)。
> t > t_Page: K_island 支配 (S_R = K_island shrinkage)。
> ⇒ **min ext 原理 = 2 つの K-channel の競合**。

---

## 1. Page Curve の数学的構造 (Page 1993)

### 1.1 設定

Hilbert 空間 H = H_A ⊗ H_B、次元 d_A × d_B、|ψ⟩ ∈ H ランダム状態 (Haar measure)。

A の reduced state ρ_A = Tr_B |ψ⟩⟨ψ| のエントロピーの平均:

```
⟨S_A⟩ ≈ log min(d_A, d_B) - (1/2) (min/max),    for d_A << d_B
```

(Page 1993 公式)

### 1.2 ブラックホール蒸発への適用

- d_B = e^{S_BH(t)}: black hole の Hilbert dim
- d_A = e^{S_R(t)}: radiation の Hilbert dim
- 蒸発時間 t_evap 内で d_A : d_B が反転

```
t < t_Page = t_evap / 2:   S_R(t) = (s_rate) t  (linear growth, "Hawking-like")
t = t_Page:                 S_R = S_BH(0)/2 = S_R^max
t > t_Page:                 S_R(t) = (s_rate) (t_evap - t)  (linear decrease)
```

### 1.3 ITU 公理の役割

S_R(t) の振る舞いは、**ITU 公理が ユニタリ進化下で課す制約**:

```
δS_R(t) = δ⟨K_R(t)⟩
```

K_R(t) の支配項が time-dependent:
- 早期: K_R が radiation 自身の熱的成分支配 → 増加
- 後期: K_R に black hole 内部 island 寄与 → 減少

---

## 2. Quantum Extremal Surface (QES)

### 2.1 RT → HRT → QES の階層

| 公式 | 提案 | 内容 |
|---|---|---|
| RT (2006) | Ryu-Takayanagi | 静的、classical, S = A/(4G_N) |
| HRT (2007) | Hubeny-Rangamani-Takayanagi | 時間依存、classical |
| **QES (2014)** | Engelhardt-Wall | 量子補正含む |

### 2.2 QES の公式

```
S(A) = min ext_X [ Area(X) / (4G_N) + S_bulk(Σ_X) ]
```

- X: bulk codim-2 面
- Σ_X: X と boundary A で囲まれる bulk 領域
- S_bulk: bulk 量子場のエンタングルメントエントロピー
- min ext: extremize して minimum を選ぶ

### 2.3 ITU 解釈

QES = **2 つの K-channel の競合**:

```
S = min ( Area-dominated K_geom,  bulk-quantum K_matter )
```

「extremize」は K-flow の **stationary point** に対応。

---

## 3. Island Formula (Penington 2019, Almheiri et al. 2019)

### 3.1 公式

Radiation R のエントロピー:

```
S(R) = min ext_I [ Area(∂I) / (4G_N) + S_bulk(R ∪ I) ]
```

- I: island = bulk 内の disconnected region
- ∂I: island の境界面
- 「I が空」または「I が non-empty」の 2 つの状況を比較

### 3.2 Hawking saddle vs Island saddle

| t | dominant saddle | S(R) |
|---|---|---|
| t < t_Page | I = ∅ (empty island) | S_bulk(R) ≈ S_R^thermal |
| t > t_Page | I = non-empty island | Area(∂I)/(4G_N) + S_bulk(R∪I) |

⇒ **Page curve は 2 saddle の swap で自動発生**。

### 3.3 ITU 視点

Hawking saddle: K_R が **thermal** で熱増加。
Island saddle: K_R が **bulk 領域を含む** ように再定義され、entropy が **bulk area** で制限される。

```
S(R) = min ( S^thermal_R(t),  Area(∂I)/(4G_N) + S^entangled_{R∪I}(t) )
```

⇒ ITU 公理は **min ext を natural に内包**。

---

## 4. Replica Wormhole (Penington-Shenker-Stanford-Yang 2019)

### 4.1 Replica trick

```
S(R) = - lim_{n→1} ∂_n log Tr(ρ_R^n)
```

n コピーを準備し、Tr(ρ_R^n) を gravitational path integral で評価。

### 4.2 Wormhole saddle の出現

- n=2: ρ_R^2 = sum of all wormhole connections between replicas
- Hawking 計算: planar saddle のみ (disconnected)
- Penington et al.: **connected wormhole saddle** が後期支配
- ⇒ replica wormhole で **Page curve が gravitational path integral から自動導出**

### 4.3 ITU 視点

Replica wormhole = **K-flow の non-local topology**。
ITU 公理は modular Hamiltonian の structure を時間とともに変化させる:
- 早期: local K_R (disconnected saddle)
- 後期: global K_{R∪I} (connected saddle)

---

## 5. 数値検証項目

本 phase の simulation で確認:

1. **Page curve (random state)**: H = H_A ⊗ H_B でランダム状態のエントロピー Page 公式と比較
2. **Page time の特定**: d_A = d_B となる時刻
3. **Island saddle vs Hawking saddle の swap**: 2 つの直線の min
4. **K-flow stationary point**: 簡易模型で extremize の数値検証

---

## 6. Phase 113 主結論

1. **Page curve (Page 1993)**: ランダム状態のエントロピー期待値による導出
2. **QES (Engelhardt-Wall 2014)**: 量子補正含む extremal surface
3. **Island formula (Penington 2019)**: S(R) = min ext [Area/(4G_N) + S_bulk]
4. **Replica wormhole (Penington et al. 2019)**: ユニタリ性をパス積分で回復
5. **ITU 解釈**: min ext = 2 つの K-channel の競合
6. **次の Phase 114** で **firewall paradox + 量子重力スケール** に進む

---

## 7. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Page curve | δS = δ⟨K⟩ の時間発展 |
| QES | 2 K-channel の stationary point |
| Island formula | K_geom + K_bulk の min ext |
| Replica wormhole | non-local K-flow topology |
| Hawking saddle | local K_R (early) |
| Island saddle | global K_{R∪I} (late) |

---

## 引用

```
Terada, M. (2026). Phase 113: Page curve, island formula, and quantum
extremal surfaces in ITU. Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Page, D. (1993) "Average entropy of a subsystem" PRL 71, 1291
- Engelhardt, N., Wall, A. (2014) "Quantum extremal surfaces" JHEP 01, 073 (arXiv:1408.3203)
- Penington, G. (2019) "Entanglement Wedge Reconstruction and the Information Paradox" arXiv:1905.08255
- Almheiri, A., Engelhardt, N., Marolf, D., Maxfield, H. (2019) "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole" JHEP 12, 063 (arXiv:1905.08762)
- Penington, G., Shenker, S., Stanford, D., Yang, Z. (2019) "Replica wormholes and the black hole interior" arXiv:1911.11977
- Almheiri, A., Hartman, T., Maldacena, J., Shaghoulian, E., Tajdini, A. (2021) "The entropy of Hawking radiation" Rev. Mod. Phys. 93, 035002
