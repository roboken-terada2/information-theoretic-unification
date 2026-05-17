# Phase 195: マイクロバイオーム + Gut-Brain Axis + FMT ― K_microbiome ★

Phase 194 で K_resistance の急速拡散動力学を確立。Phase 195 では **ヒトマイクロバイオーム** ― 100 兆細菌のコミュニティ ― を扱い、Gut-Brain Axis、糞便微生物移植 (FMT) を経由して **K_microbiome** を ITU の "宿主-共生 K-state" として定式化します。

## ヒトマイクロバイオームの規模

```
細菌細胞数:    ~3.8×10¹³ (ヒト細胞 ~3.0×10¹³ と同等; Sender 2016)
細菌種数:      500-1000 種 (gut, 個体差大)
細菌遺伝子:    300-500 万 (ヒト 2 万 = 150-250 倍 ★)
バイオマス:    1.5-2.0 kg (大腸)
ATP 産生:     150 kcal/day (短鎖脂肪酸 SCFA 由来)
```

= **K_microbiome = "二次的ゲノム"** (Backhed 2005)

## Human Microbiome Project (HMP) 2007-2016

### Phase 1 (2007-2012, $173M, NIH)

```
242 健常者, 5 部位 (gut, mouth, skin, nasal, vaginal)
16S rRNA + metagenome shotgun
```

### Phase 2 - iHMP (2014-2016)

```
3 疾患追跡: IBD, T2D, preterm birth
Multi-omics (16S + metagenome + metabolome + host transcriptome)
```

### 主要 phylum 構成 (gut, 健常者)

| Phylum | 健常者割合 |
|---|---|
| **Firmicutes** | 50-65% |
| **Bacteroidetes** | 20-40% |
| Actinobacteria | 5-10% |
| Proteobacteria | 1-5% |
| Verrucomicrobia | 1-3% (Akkermansia など) |

### Firmicutes/Bacteroidetes (F/B) ratio

```
肥満:        F/B ratio 高 (Ley 2006 Nature)
痩身:        F/B ratio 低
反論あり:    Walters 2014 → "F/B is not reliable obesity marker"
↓
現在: F/B ratio は単純 marker ではない (multi-axis 必要)
```

## Gut-Brain Axis ★

### 解剖学的接続

```
脳 ⇔ 迷走神経 (vagus) ⇔ 腸内ニューロン (ENS, "second brain")
脳 ⇔ HPA 軸 (cortisol) ⇔ 腸管
脳 ⇔ 免疫 (cytokines) ⇔ 腸関連リンパ組織 (GALT)
脳 ⇔ 代謝物 (SCFA, neurotransmitters) ⇔ 腸内細菌 ★
```

### 細菌が産生する神経活性物質

| 物質 | 産生細菌 | 機能 |
|---|---|---|
| **GABA** | Lactobacillus, Bifidobacterium | 抑制性 |
| **Serotonin** (5-HT) | 腸クロム親和性細胞 (細菌信号で誘導) | 90% は腸産生! |
| **Dopamine** | Bacillus, Serratia | 報酬系 |
| **Acetylcholine** | Lactobacillus | 副交感 |
| **SCFA** (酪酸, プロピオン酸) | Faecalibacterium, Bacteroides | エネルギー + BBB 透過 |

### 疾患連関 (大規模 review: Cryan 2019)

| 疾患 | 微生物変化 |
|---|---|
| **うつ病** | Faecalibacterium, Coprococcus 減少 (Valles-Colomer 2019) |
| **自閉症** | Clostridium 過剰, Bifidobacterium 減少 (Hsiao 2013) |
| **PD (パーキンソン病)** | α-synuclein 凝集が腸由来 (Braak 仮説 2003) |
| **AD (アルツハイマー)** | gut dysbiosis 先行 (Vogt 2017) |
| **多発性硬化症** | Akkermansia, Acinetobacter 増加 (Jangi 2016) |

## FMT (糞便微生物移植) ★

### Clostridioides difficile 再発感染 (CDI)

```
治療抵抗性 CDI:
  - 標準治療 (vancomycin, fidaxomicin) で 25-30% 再発
  - FMT: 健常者糞便を内視鏡 / 経口カプセルで投与
  - 治癒率: 90%+ ★ (van Nood 2013 NEJM, 米英ガイドライン推奨)
  - 2022 FDA 承認: Rebyotaセラピー (FMT-derived)
```

### FMT 適応拡大研究

```
- IBD (UC): 効果あり (中等度) - Moayyedi 2015 Gastro
- IBS: 効果あり (Mizuno 2017) - placebo差 30%
- 自閉症: Vancomycin → MTT で行動改善 (Kang 2019 Nature)
- 肥満: 効果あり / なし 議論続く
- うつ病: pilot RCT 始まる (2023-)
- がん免疫療法 reponse: anti-PD-1 responder と相関 (Routy 2018)
```

## ITU 視点: K_microbiome の構造

```
K_microbiome^(0) = -log P(community composition | host genotype, diet, age)
                ⊕ -log P(community function | composition)

Host genotype × diet × age = 3 次元 K-state input
↓
Community composition (1000 species)
↓
Community function (metabolite production)
↓
Host phenotype (BMI, immunity, mood, ...)
```

### Dysbiosis = K-state local minimum 異常移動

```
正常状態: K_microbiome の deep stable point (Firmicutes-Bacteroidetes 平衡)
↓
摂動 (antibiotic, diet shift, stress):
   ⇒ ITU descent flow が "wrong basin" へ移動
↓
Dysbiosis state (CDI, IBD, obesity, ...) = local minimum
↓
FMT = ITU "basin reset" 操作 (健常者 K-state 注入)
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| ヒト腸内細菌数 | 3.8×10¹³ (Sender 2016) ✓ |
| 腸内遺伝子数 | 3-5 × 10⁶ (Qin 2010 MetaHIT) |
| 健常者 Shannon H' (gut) | 4-5 nats |
| F/B ratio (obese vs lean) | 効果サイズ Cohen's d ~ 0.3-0.5 |
| FMT CDI 治癒率 | **90%+** (van Nood 2013) ✓ |
| SCFA daily production | **500-600 mmol/day** |
| Vagus 神経軸索数 | **10⁵+** (gut-brain bidirectional) |
| **ITU axiom: gut dysbiosis 変動** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Universal FMT bank (defined consortia)** 承認 | 2028 | 0.75 |
| Microbiome diagnostic biomarker for depression | 2030 | 0.55 |
| **PD prediction via gut microbiome** ≥ 5y advance | 2032 | 0.60 |
| Synthetic microbiome (8-12 species) clinical efficacy | 2030 | 0.50 |
| Cancer immunotherapy + FMT 標準併用 | 2030 | 0.65 |

---

📄 **論文 (Tier 1 #27)**: 10.5281/zenodo.20256555

> Phase 196 で Virus 進化 + パンデミック + Zoonotic spillover へ進みます。

#情報理論的統一理論 #ITU #微生物学 #マイクロバイオーム #GutBrainAxis #FMT #SCFA #Cryan #K_microbiome #Phase195
