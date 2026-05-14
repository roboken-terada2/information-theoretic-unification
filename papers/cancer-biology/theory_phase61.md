# Phase 61: がん免疫学 ― K_immune の破綻と免疫療法の ITU 解釈

> **Tier 1 #5 (Cancer Biology) — Phase 3/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 61 の目的

Phase 59-60 で **がん細胞内の K 破綻** (regulatory + metabolic) を扱いました。Phase 61 では **organism レベルの K**:

1. **Cancer-Immunity Cycle** (Chen-Mellman 2013) を ITU で再構成
2. **免疫回避**: PD-L1, CTLA-4, MHC-I 抑制 = **K_immune の corruption**
3. **免疫チェックポイント阻害剤 (ICI)** = K の restoration
4. **Responder vs non-responder** ― なぜ 20-30% しか奏功しないか
5. **CAR-T 療法** = 人工的 K の augmentation
6. **TIL 療法** (2024 FDA 承認 lifileucel) = K の再教育

中心テーゼ:

> **正常免疫 = organism-level の QECC** (syndrome 検出 = T 細胞)
> **がん免疫回避 = K_immune の意図的劣化**
> **ICI = K_immune の restoration** (T 細胞の抑制解除)

---

## 1. 正常免疫の ITU 表記

### 1.1 免疫 = organism QECC

| QECC 概念 | 免疫対応 |
|---|---|
| 論理 qubit | 「自己 (self)」 状態 |
| Syndrome 検出 | T 細胞 / NK 細胞による異常抗原検出 |
| エラー訂正 | 異常細胞の排除 (cytotoxic T cell, NK) |
| 冗長性 | 多様な TCR レパートリー (~10⁷-10⁸) |
| 自己誤検出防止 | regulatory T cell + checkpoints |

ITU 公理: $\delta S_{\rm organism} = \delta\langle K_{\rm immune}\rangle$ ⇒ 異常細胞の出現 = δS_organism、それを免疫が抑える = δ⟨K_immune⟩。

### 1.2 Cancer-Immunity Cycle (Chen-Mellman 2013)

7 段階のサイクル:
```
1. 腫瘍抗原放出 (cancer cell death)
2. 抗原提示 (DC が tumor antigen を取込)
3. T 細胞プライミング (リンパ節)
4. T 細胞循環 (血液 → 腫瘍)
5. 腫瘍浸潤 (TIL になる)
6. 腫瘍細胞認識 (TCR-MHC 結合)
7. 腫瘍細胞殺害 (Granzyme B, IFN-γ)
```

ITU 視点: **各段階が K_immune の sub-component**。1 つでも壊れるとサイクル全体が止まる。

---

## 2. 免疫回避 = K_immune の corruption

### 2.1 各回避機構と K_immune の破綻

| 機構 | 標的サイクル段階 | ITU 解釈 |
|---|---|---|
| **PD-L1 発現** | 7 (殺害) | **K_self_inhibitor 過剰活性** |
| **CTLA-4** (Treg 上) | 3 (プライミング) | **K_priming 抑制** |
| **MHC-I 抑制** | 6 (認識) | **K_recognition 欠失** |
| **TGF-β 分泌** | 5-7 | **T 細胞 K の global 抑制** |
| **Treg recruitment** | 全段階 | regulatory K の hijack |
| **MDSC, TAM** | 5-7 | suppressive K の dominance |
| **Tryptophan 代謝 (IDO)** | 7 | T 細胞代謝 K の抑制 |

⇒ **がんは K_immune を 7 段階で同時に攻撃**する。

### 2.2 PD-L1/PD-1 軸の重要性

正常: T 細胞活性化後、PD-1 が PD-L1 (抗原提示細胞) と結合 → T 細胞鎮静化 (autoimmunity 防止)。

がん: 腫瘍細胞が **PD-L1 を過剰発現** → T 細胞を「自分は正常」 と誤認識させる。

ITU: K_self_inhibitor が cancer に hijack される。

---

## 3. 免疫チェックポイント阻害剤 (ICI)

### 3.1 主な承認薬

| 薬剤 | 標的 | 承認 | メーカー | 適応 |
|---|---|---|---|---|
| Ipilimumab (Yervoy) | CTLA-4 | 2011 | BMS | melanoma, 多種 |
| Pembrolizumab (Keytruda) | PD-1 | 2014 | Merck | melanoma, lung, head&neck, 30+ 種 |
| Nivolumab (Opdivo) | PD-1 | 2014 | BMS | melanoma, lung, kidney, 多種 |
| Atezolizumab (Tecentriq) | PD-L1 | 2016 | Roche | bladder, lung |
| Durvalumab (Imfinzi) | PD-L1 | 2017 | AstraZeneca | bladder, lung, biliary |
| Cemiplimab (Libtayo) | PD-1 | 2018 | Regeneron | skin |
| Dostarlimab (Jemperli) | PD-1 | 2021 | GSK | endometrial |

⇒ **2024 年時点で年売上 $50B+ 市場**。Keytruda 単独で年 $25B (世界 #1 医薬品)。

### 3.2 ITU 解釈: K の restoration

ICI は cancer の阻害シグナルをブロック ⇒ **K_immune を「強制的に restore」**:
- Anti-CTLA-4: priming K を回復
- Anti-PD-1/PD-L1: cytotoxic K を回復
- 両者 combo: 2 つの K 同時 restore (Phase 60 と同じ「多 K 同時 restore」 戦略)

---

## 4. Responder vs Non-responder

### 4.1 反応率の現実

| がん種 | ICI 単独反応率 | 5 年生存 |
|---|---|---|
| Melanoma | **40-50%** | ~50% (anti-PD-1+CTLA-4) |
| NSCLC | 20-30% | ~25% |
| Renal | 25-35% | ~30% |
| Head & Neck | 15-20% | ~15% |
| Triple-neg breast | 20% | ~15% |
| **Pancreatic, prostate, colorectal MSS** | **<5%** | ほぼ 0 |

⇒ **多くのがんで 70-95% は奏功しない**。

### 4.2 ITU による説明

ICI が効くには:
1. **TMB (Tumor Mutational Burden) ≥ 10 mut/Mb**: ネオアンチゲン豊富 = T 細胞 K が認識可能
2. **MHC-I 機能保持**: 抗原提示 K が動く
3. **CD8+ T 細胞浸潤**: K が物理的にアクセス可能
4. **PD-L1 発現** ≥ 1-50%: ICI の標的が存在
5. **IFN-γ 経路 intact**: cytotoxic K が機能

⇒ **5 つの K-component が全て生きている** 患者のみ反応。実は ICI は「健康な K_immune の蘇生」 であって、**完全に破綻した K は restore できない**。

### 4.3 数値例: TMB vs 反応率

NSCLC のデータ (Rizvi et al. 2015):

| TMB レンジ | ICI 反応率 |
|---|---|
| <100 mut/exome | ~5% |
| 100-200 | ~15% |
| 200-300 | ~30% |
| **>300** | **~60%** |

⇒ ITU 視点: TMB = K_immune が認識できる「**syndrome density**」。

---

## 5. CAR-T 細胞療法

### 5.1 概要

患者の T 細胞を取り出し、**人工 chimeric antigen receptor (CAR)** を遺伝子導入 ⇒ 標的抗原 (CD19 等) を持つ細胞を強制的に攻撃。

| 製品 | 標的 | 承認 | 適応 |
|---|---|---|---|
| Kymriah | CD19 | 2017 | ALL, DLBCL |
| Yescarta | CD19 | 2017 | DLBCL, FL |
| Tecartus | CD19 | 2020 | MCL, ALL |
| Breyanzi | CD19 | 2021 | DLBCL |
| Abecma | BCMA | 2021 | multiple myeloma |
| Carvykti | BCMA | 2022 | multiple myeloma |

### 5.2 ITU 解釈

CAR-T = **人工 K の augmentation**:
- 自然 T 細胞が K_immune の sub-component なら
- CAR-T は **特定の K を強制的に追加** したエンジニアリング細胞

⇒ ITU 観点で「**外部から K を補強する**」 工学的 immunotherapy。

### 5.3 限界

固形腫瘍では成功率低い:
- 腫瘍ホーミング (cycle step 4-5) が弱い
- TME の免疫抑制 (cycle step 6-7)
- CRS (cytokine release syndrome) 副作用

⇒ **K augmentation だけでは TME-level の K 破綻に勝てない**。

---

## 6. TIL 療法 (2024 FDA 承認の最新)

**Lifileucel (Amtagvi)** — 2024 年 2 月 FDA 承認:
- 患者腫瘍から **TIL (tumor-infiltrating lymphocytes) を抽出**
- 体外で IL-2 で増殖
- 患者に大量返戻 ⇒ tumor 攻撃

melanoma で 30-50% 反応率。Carvykti より高い場合も。

ITU 解釈: TIL = **既に K_immune が部分的に動いている細胞を増幅** ⇒ 「健康な K の amplification」 戦略。

---

## 7. Phase 61 数値検証

### 7.1 検証 1: Cancer-immunity cycle 7-step kinetic
各段階のレート定数で T cell 流入をシミュレーション。

### 7.2 検証 2: TMB vs ICI 反応率
Rizvi 2015 のデータと整合する logistic フィット。

### 7.3 検証 3: 単剤 vs combination ICI
Anti-PD-1 単独 vs Anti-CTLA-4+PD-1 combo の反応率比較。

### 7.4 検証 4: 治療戦略のヒート: PD-L1 × TMB
2 次元グリッドで「どの患者が ICI 適応か」 を可視化。

---

## 8. Phase 61 の結論

1. **正常免疫 = organism-level QECC** (7-step cycle = K_immune の 7 sub-components)
2. **がん免疫回避 = K_immune の 7 段階同時攻撃**
3. **ICI = K の restoration** (cancer の阻害解除)
4. **70-95% が non-responder**: K の複数 component が同時に必要
5. **CAR-T = 人工 K の augmentation** (固形腫瘍は不十分)
6. **TIL = 健康 K の amplification** (新承認)
7. **将来**: 多 K 同時 restoration (combo + cell therapy + metabolic) が標準化

Phase 62 (最終回) では **ITU-informed cancer treatment roadmap** を作成し、10 個の反証可能予測を提示して Tier 1 #5 を完成させます。

---

## 引用

```
Terada, M. (2026). ITU and Cancer Biology (Phase 59-62).
Tier 1 #5 application paper. In preparation.
```

参考:
- Chen & Mellman (2013) Immunity 39, 1 (cancer-immunity cycle)
- Hodi et al. (2010) NEJM 363, 711 (ipilimumab in melanoma)
- Topalian et al. (2012) NEJM 366, 2443 (nivolumab)
- Rizvi et al. (2015) Science 348, 124 (TMB and ICI)
- Maude et al. (2018) NEJM 378, 439 (CAR-T in ALL)
- Sarnaik et al. (2021) JCO 39, 2656 (lifileucel TIL)
