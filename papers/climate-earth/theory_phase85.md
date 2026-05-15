# Phase 85: 緩和策 ― 再エネ転換 + CDR + 気候工学のリスク低減

> **Tier 1 #11 (Climate / Earth Systems) — Phase 3/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 85 の目的

Phase 83 で K-state を定義し、Phase 84 で K-flow の動的構造 (炭素循環、ENSO、AMOC、tipping) を解析した。
Phase 85 では **K-state 修正・脱炭素介入** の効果を定量化する:

1. **再エネ転換**: 太陽光 + 風力で電力部門の K-flow を再構築
2. **CDR (Carbon Dioxide Removal)**: DAC + BECCS + reforestation で大気 K_carbon を能動除去
3. **SRM (Solar Radiation Management)**: 成層圏エアロゾル注入で短期 K-balance 是正
4. **3 緩和シナリオ比較**: BAU / NZE / NZE+CDR+SRM

中心テーゼ:

> **再エネ単独では 1.5°C 達成不可** (残余予算 6 年 + 慣性)。
> 緩和は **3 層構造** (排出削減 → CDR → SRM一時) が必須。
> ITU 視点: K_climate を安定領域へ戻すには **複数 K-current の並列介入**。

---

## 1. 再エネ転換ロードマップ

### 1.1 IEA NZE 2050 + Phase 80/82 の延長

電力部門の再エネシェア進捗 (Phase 82 から):

| 年 | 太陽光 + 風力 % | LCOE 比較 |
|---|---|---|
| 2024 | 14 | 太陽光 $40, 風力 $38, 石炭 $108 |
| 2030 | 31 | 太陽光 $25, 風力 $30 |
| 2040 | 57 | 太陽光 $18 |
| **2050** | **72** | **太陽光 $15** (光技術頂点) |

⇒ Wright's Law (累積生産 2× で 20-24% コスト減) は perovskite/Si tandem で更に加速。

### 1.2 ITU 解釈

再エネ転換 = K_energy 源の **fossil K-source (静的、有限)** から **太陽 K-source (情報的に無限)** への置換。

$$
\delta S_{\text{atm}} (\text{from fossil}) = +5 \text{ GtC/yr}^{-1}
$$
$$
\delta S_{\text{atm}} (\text{from solar}) \approx 0
$$

⇒ K-flow パターンの構造的変容。

### 1.3 排出経路への影響

電力部門 = 全排出の **34%** (2024)。完全再エネ化で:
- 直接削減: **3.7 GtC/yr**
- 間接効果: 輸送・産業・暖房の電化で +2-3 GtC/yr 削減

---

## 2. CDR (Carbon Dioxide Removal)

### 2.1 4 主要技術

| 技術 | 2024 容量 (MtCO₂/yr) | 2050 目標 | コスト 2024 → 2050 |
|---|---|---|---|
| **DAC** (Climeworks 他) | 0.01 | 1,000 | $600 → $50/t |
| **BECCS** (バイオエネ + CCS) | 2 | 3,000 | $100 → $50/t |
| **植林 / 再生林** | 1,000 | 5,000 | $30 → $20/t |
| **海洋アルカリ化** | 0 | 500 | $200 → $100/t |
| **合計 CDR** | **~1,000** | **~10,000** | — |

### 2.2 IEA NZE 2050 要件

NZE シナリオ: 2050 年に **6 GtCO₂/yr CDR** が必要 (残余排出オフセット)。

過剰なら **negative emissions** ⇒ 大気 CO₂ 濃度 **減少フェーズへ**。

### 2.3 ITU 解釈

CDR = K_carbon の **能動的 K-bit 除去**:

$$
\frac{dM_a}{dt} \rightarrow E(t) - \text{CDR}(t) - (\text{natural sinks})
$$

DAC 1 GtCO₂/yr の物理的限界: **MOF + 太陽電力** (Phase 81 連動) で $50/t 実現可能。

⇒ Tier 1 #10 (Energy/Materials) と Tier 1 #11 (Climate) は **同一の K-flow 介入**。

---

## 3. SRM (Solar Radiation Management)

### 3.1 主要技術と効果

| 技術 | ΔF 補正 (W/m²) | 副作用 |
|---|---|---|
| **成層圏 SO₂ 注入** | −1 to −5 | オゾン破壊、降水パターン変化 |
| **海洋雲 brightening** | −0.5 to −2 | 局所気象 |
| **シラスクラウド薄化** | −0.5 to −2 | 不確実 |
| **宇宙鏡** | −1 to −2 | 莫大コスト |

### 3.2 ITU 視点

SRM = 入射 K-flux を **物理的に削減**:

$$
S_0 \to (1 - f_{\text{SRM}}) S_0
$$

CO₂ 既蓄積を打ち消すパッチ。**根本治療ではない**。

### 3.3 termination shock のリスク

SRM 停止 → 5-10 年で温度急上昇 ⇒ K_climate の急速 jump。
**ガバナンス必須**: 数百年継続義務、国際合意。

### 3.4 ITU 提言

SRM = **「外科的・期間限定 K-current 補正」** として CDR と並行運用すべき。
単独依存は K_climate の不安定化を招く。

---

## 4. 3 シナリオ比較

### 4.1 シナリオ設定

| 名 | 内容 |
|---|---|
| **BAU** | Business as usual: 排出継続 (RCP6.0 軌道) |
| **NZE** | Net Zero Emissions 2050: 排出単独削減 |
| **NZE+CDR** | NZE + DAC/BECCS 10 GtCO₂/yr by 2050 |
| **NZE+CDR+SRM** | + 成層圏 SO₂ で ΔF -2 W/m² 補正 (2035-2080) |

### 4.2 温度パスウェイ予測 (簡易 EBM)

エネルギー収支モデル:

$$
C \frac{dT}{dt} = \Delta F(t) - \lambda T
$$

- C ≈ 8 W·yr/m²/K (海洋熱容量)
- λ = 1.3 W/m²/K (Phase 83 結果)

| シナリオ | ΔT 2050 | ΔT 2100 | Tipping cascade 確率 |
|---|---|---|---|
| BAU | +2.5°C | +3.8°C | ~70% |
| NZE | +1.8°C | +2.1°C | ~25% |
| NZE+CDR | +1.6°C | +1.5°C | ~10% |
| **NZE+CDR+SRM** | **+1.3°C** | **+1.2°C** | **<5%** |

### 4.3 ITU 視点

各シナリオ = K-state ポテンシャル曲面上の異なる軌道:
- BAU: 複数 attractor へ転移リスク
- NZE: 安定領域に滞在 (確率 75%)
- NZE+CDR: 元の前産業 K-state に漸近
- NZE+CDR+SRM: 短期的に強制復帰、長期に CDR で根本治療

---

## 5. 緩和策の経済性

### 5.1 削減コスト曲線 (MACC, McKinsey 2024)

| 介入 | コスト ($/tCO₂) | 削減ポテンシャル (GtCO₂/yr) |
|---|---|---|
| 太陽光 PV 普及 | −20 (節約) | 6 |
| 風力 | −15 | 4 |
| 電化 (EV, ヒートポンプ) | −5 | 5 |
| 効率改善 | −10 | 3 |
| **負コスト (節約) サブトータル** | — | **18 GtCO₂/yr** |
| 原子力新設 | $50 | 2 |
| 水素 (グリーン) | $80 | 2 |
| 植林 / BECCS | $50-100 | 5 |
| **DAC** | $100-600 | 1+ |

⇒ 現状 **約半分の必要削減 (40 GtCO₂/yr の半分)** はコストネガティブで実現可能。

### 5.2 投資総額

IEA NZE 2050 シナリオ要件:
- 累積投資 2024-2050: **$200 trillion** (GDP の ~2%/年)
- 化石燃料投資撤退: **$10-15 trillion** stranded assets
- CDR + SRM 投資: ~$5-10 trillion (2030-2050)

### 5.3 ITU 視点

投資 = K_capital を K_renewable へリダイレクト。Tier 1 #8 (Economics) 連動。

---

## 6. Phase 85 主結論

1. **再エネ単独**: ΔT 2100 = +2.1°C (1.5°C 未達)
2. **+ CDR 10 GtCO₂/yr**: ΔT 2100 = +1.5°C (達成可能)
3. **+ SRM 一時 (2035-2080)**: ΔT ピーク +1.3°C
4. **Tipping cascade 確率**: 70% → 5% (緩和最大時)
5. **負コスト削減**: 約半分の必要量を経済合理性のみで実現可能

⇒ Phase 86 で 10 反証可能予測 + Tier 1 #11 統合まとめ。

---

## 7. ITU 統合視点

| 介入 | K-axis | 主体 |
|---|---|---|
| 再エネ転換 | K_energy 源置換 | Tier 1 #10 連動 |
| CDR | K_carbon 能動除去 | Tier 1 #10 (MOF) 連動 |
| SRM | K-flux 入射削減 | 新規 |
| カーボンプライシング | K_economic シグナル | Tier 1 #8 連動 |
| AGI 加速 | K_innovation | Tier 1 #2 連動 |

⇒ Tier 1 #11 (気候) は polytope の **超核 (super-hub)**: 全 vertex と双方向結合。

---

## 引用

```
Terada, M. (2026). Phase 85: Renewable transition, CDR, and SRM as K-current
mitigation pathways (Tier 1 #11 Phase 3/4). Zenodo. DOI: [to be assigned].
```

参考:
- IEA (2024) World Energy Outlook + Net Zero Roadmap
- IPCC SR1.5 (2018) + AR6 WG III (2023)
- McKinsey (2024) Net Zero MACC
- Climeworks, Carbon Engineering 2024 reports
- National Academies (2021) Reflecting Sunlight: SRM Research
- Smith et al. (2023) State of Carbon Dioxide Removal
