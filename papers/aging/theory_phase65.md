# Phase 65: 老化介入療法 ― ITU が評価する rapamycin, metformin, senolytics, NAD+

> **Tier 1 #6 (Aging) — Phase 3/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 65 の目的

Phase 63-64 で 老化を ITU の K_organism 劣化として捉えました。Phase 65 では:

1. **既知の介入候補 6 種**を ITU で評価
2. 各介入が標的とする **K-component** を明示
3. 単剤 vs combination の効果比較
4. **TAME (Targeting Aging with Metformin) 試験**等の臨床現状
5. **OSKM 部分リプログラミング** (Sinclair) と Yamanaka 因子
6. Phase 66 (ロードマップ) への基盤

中心テーゼ:

> **老化介入も「**多 K 同時 restoration**」 が ITU 必然**。
> 単剤 (rapamycin only など) は K の代償経路で効果限定。Cancer (Phase 60-61) と同じ構造。

---

## 1. 6 つの主要介入候補

### 1.1 Rapamycin (mTOR 阻害剤)

- **発見**: イースター島 (Rapa Nui) の土壌細菌 (1972)
- **機序**: mTORC1 阻害 ⇒ オートファジー促進 + タンパク合成抑制
- **動物データ**: マウス寿命 **+9-14%** (Harrison et al. 2009, Nature) ⇒ NIA ITP の最大ヒット
- **副作用**: 免疫抑制 (臓器移植薬として使用)、口内炎
- **ヒト臨床**: Mannick et al. PEARL 試験 進行中

**ITU 解釈**: $K_{\rm proteostasis}$ + $K_{\rm metab}$ の同時 restore (autophagy = リソース recycling、mTOR↓ = 同化抑制)。

### 1.2 Metformin (AMPK 活性化剤)

- **歴史**: 1957 年承認の糖尿病薬、推定 1.5 億人使用中
- **機序**: AMPK 活性化 ⇒ ミトコンドリア Complex I 阻害 + 解糖系誘導
- **動物データ**: マウス寿命 **+5-6%** (modest だが robust)
- **疫学**: 糖尿病患者の Metformin 使用は心血管死・認知症・がん死減少と関連
- **TAME 試験**: 2022 年開始、3000 人、6 年間 follow-up ⇒ 2028 年結果予定

**ITU 解釈**: $K_{\rm metab}$ restore (PI3K/AKT/mTOR の対抗 K)。Phase 60 (がん代謝) でも同薬が活躍。

### 1.3 Senolytics (Dasatinib + Quercetin, Fisetin, UBX1325)

- **概念**: senescent cells を選択的に除去 (Kirkland 2015, Nature Medicine)
- **薬剤**:
  - **Dasatinib + Quercetin (D+Q)**: 経口、月 1-2 回投与
  - **Fisetin**: 植物由来 flavonoid (イチゴ等)、安全性高
  - **UBX1325** (Unity Biotechnology): 眼内注射、糖尿病性網膜症
- **動物データ**: マウス寿命 **+36% (1 回投与でも)** (Xu et al. 2018, Nat Med)
- **ヒト臨床**: Phase II 進行中 (Idiopathic Pulmonary Fibrosis、骨粗鬆症)

**ITU 解釈**: senescent cells = ITU 破綻 partial mode + SASP で K 劣化伝播 ⇒ それを除去 ⇒ **K_organism の地域的 restore**。

### 1.4 NAD+ Boosters (NMN, NR, Niagen)

- **NAD+ の役割**: redox, sirtuin substrate, DNA 修復 (PARP1)
- **加齢で**: NAD+ 量が **半減** (40 歳までに)
- **介入**: NMN (Nicotinamide Mononucleotide) または NR (Nicotinamide Riboside) を経口
- **動物データ**: マウス mitochondrial 機能、運動能力、insulin 感受性改善
- **ヒト臨床**: 小規模 RCT で safety + biomarker 改善あり、寿命延長は未証明

**ITU 解釈**: $K_{\rm energy}$ + $K_{\rm DNA\_repair}$ の補強。NAD+ = 複数 K の cofactor。

### 1.5 Caloric Restriction (CR)

- **歴史**: McCay (1935) でラットで初観察、最も古い longevity 介入
- **動物データ**: マウス・霊長類で **+30-50% 寿命延長** (Mattison 2017, Nat Comm)
- **ヒト**: CALERIE 試験 (2017) で生物学的年齢↓、代謝改善
- **限界**: 25% 以上の継続的 CR はヒトで困難 (compliance)、骨密度低下リスク

**ITU 解釈**: 食事量↓ ⇒ mTOR↓, AMPK↑, autophagy↑ ⇒ **全 K-component の system-wide reset**。介入として最も理に適うが**実装困難**。

### 1.6 OSKM Partial Reprogramming (Yamanaka factors)

- **2006 年**: Yamanaka & Takahashi、4 因子 (OCT4, SOX2, KLF4, c-Myc) で体細胞 → iPSC
- **2020 年**: Sinclair lab、**部分的 OSKM 発現で網膜神経細胞を若返り** (Lu et al. Nature 2020)
- **2023 年**: Altos Labs ($3B funding, Bezos), Retro Biosciences (Sam Altman) が in vivo reprogramming に投資
- **動物データ**: 視神経再生、心臓再生 ⇒ 「**生物学的時計巻き戻し**」

**ITU 解釈**: epigenome reset = **$K_{\rm information}$ の全面再書込み**。Sinclair の情報理論 ITU 版 の物理的実装。最大の野心、最大のリスク (がん化)。

---

## 2. 介入 × K-component マトリクス

| 介入 | K_replication | K_energy | K_proteostasis | K_immune | K_info |
|---|---|---|---|---|---|
| Rapamycin | — | + | **++** | -* | + |
| Metformin | — | **++** | + | + | + |
| Senolytics | + | + | + | **++** | + |
| NAD+ | — | **++** | + | + | + |
| **CR** | + | **++** | **++** | + | + |
| **OSKM** | **++** | + | + | + | **+++** |

(- = 影響なし、+ = 軽度、++ = 中等度、+++ = 強い restore、-* = 抑制)

⇒ **どの介入も 1-2 K-component に偏る**。複数 K の同時 restore には combination が必要。

---

## 3. Combination Longevity 戦略

### 3.1 既知の combination

| 組合せ | 動物データ | ITU 評価 |
|---|---|---|
| Rapamycin + Metformin | マウスで +13% (vs 単剤 +9% / +5%) | ★ 2 軸 restore |
| Rapamycin + Acarbose | マウスで +20% (Strong 2016) | ★★ Robust |
| D+Q + NMN | 試験中 | ★★ 3 軸 restore |
| **CR + OSKM** | 理論段階 | ★★★ ITU 理想 |

### 3.2 ITU 予測の数値モデル

各介入の K 補強効果 (0-1 スケール) を加算 (上限 1.0 で clipping):

$$K_{\rm restored}(intervention) = \min(1, K_{\rm baseline} + \sum_i \alpha_i \cdot \text{effect}_i)$$

⇒ Phase 65 simulation で詳細計算 (図 d 参照)。

---

## 4. 臨床試験の現状

### 4.1 進行中の主要試験

| 試験名 | 介入 | 規模 | 期間 | 主要評価項目 |
|---|---|---|---|---|
| **TAME** | Metformin | 3,000 人 | 6 年 | aging-related multi-morbidity |
| **PEARL** | Rapamycin (intermittent) | 200 人 | 1 年 | safety + frailty |
| **UNITY 311** | UBX1325 (senolytics) | 100 人 | 2 年 | 糖尿病性網膜症 |
| **CALERIE** | 25% CR | 200 人 | 2 年 (完了) | biological aging |

### 4.2 規制上の課題

FDA は「**老化を疾患として認めていない**」 ⇒ 「longevity drug」 として申請不可。
TAME 試験は **「multi-morbidity 予防」** として申請する戦略。
**2030 年までに「老化」 が FDA 認可 indication になる**ことが ITU 予測 (Phase 66 で詳述)。

---

## 5. Phase 65 数値検証

### 5.1 検証 1: 介入別 lifespan 延長率 (マウスデータ)

### 5.2 検証 2: K-component restoration マトリクス (heatmap)

### 5.3 検証 3: Combination 相加効果と相乗効果

### 5.4 検証 4: ITU prediction: K_overall(age) with vs without intervention

---

## 6. Phase 65 の結論

1. **6 主要介入**それぞれが特定 K-component を restore
2. **どの介入も単剤では 1-2 軸のみ** ⇒ Phase 60-61 と同じパターン
3. **Combination が ITU 必然**: Rapa+Met = +13%, Rapa+Acarbose = +20%
4. **CR は全 K 介入だが実装困難**
5. **OSKM partial reprogramming = 最大の野心**、Altos Labs/Retro Bio が投資中
6. **TAME 試験 2028 結果**が「老化を疾患として FDA 認知」 の規制突破口

Phase 66 (最終回) では **2026-2050 longevity ロードマップ**、平均寿命予測、10 個の反証可能予測を提示し、Tier 1 #6 を完成させます。

---

## 引用

```
Terada, M. (2026). ITU and Aging (Phase 63-66).
Tier 1 #6 application paper. In preparation.
```

参考:
- Harrison et al. (2009) Nature 460, 392 (rapamycin & mouse lifespan)
- Barzilai et al. (2016) Cell Metab 23, 1060 (TAME trial design)
- Kirkland & Tchkonia (2015) Cell Metab 22, 922 (senolytics concept)
- Xu et al. (2018) Nat Med 24, 1246 (senolytics longevity)
- Mattison et al. (2017) Nat Comm 8, 14063 (CR in primates)
- Lu et al. (2020) Nature 588, 124 (OSKM in vivo reprogramming)
- Mannick et al. (2018, 2022) PEARL trial (rapamycin)
