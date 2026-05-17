# Phase 216: CRISPR + 遺伝子編集 + Gene Therapy ― K_genome_edit ★

Phase 215 で K_genome の central dogma + 構造を確立。Phase 216 では **CRISPR-Cas9 + 遺伝子編集 + 遺伝子治療** ― 2023 Casgevy FDA 承認 を中心に扱い、**K_genome_edit** を ITU の "ゲノム書き換え K-state" として定式化します。

## CRISPR 革命 (2012-2024)

### CRISPR 発見史 (Phase 193 復習 + 拡張)

```
1987: Ishino (大阪大) 大腸菌で repeat 配列発見
2000: Mojica 多細菌で確認
2005: Mojica-Bolotin: ファージ + プラスミド由来
2007: Barrangou (Danisco) 機能証明 (乳酸菌)
2010: Doudna + Charpentier 機構解明
2012: Jinek-Doudna in vitro 切断 (Science) ★
2013: Zhang, Church 真核細胞応用 (3 papers Science) ★
2020: Doudna + Charpentier Nobel Chemistry ★
2023: Casgevy 鎌状赤血球症 FDA 初承認 ★
```

## CRISPR-Cas9 機構

```
構成要素:
  - sgRNA (single guide RNA): 標的 20 bp に相補的
  - Cas9 (Streptococcus pyogenes): DNA 切断酵素
  - PAM 配列 (NGG, 3 bp): Cas9 が認識
↓
ガイドRNA設計 → DNA 標的部位 → 二本鎖切断 (DSB) → 修復
↓
DSB 修復経路:
  - NHEJ (Non-Homologous End Joining): 不正確, indel 形成 → KO
  - HDR (Homology-Directed Repair): 正確修復, テンプレート要 → knock-in
```

## CRISPR 派生技術

| 技術 | 機能 | 開発者 / 年 |
|---|---|---|
| **Cas9** | DSB induction | Doudna-Charpentier 2012 |
| **dCas9** | catalytically dead, gene reg | Qi 2013 (CRISPRi/a) |
| **Cas12 (Cpf1)** | DSB blunt cut | Zetsche 2015 |
| **Cas13** | RNA-targeting | Abudayyeh 2016 |
| **Base Editor (Liu 2016)** | C→T, A→G **no DSB** ★ | Komor-Liu 2016/2017 |
| **Prime Editor (Liu 2019)** | search-replace **no DSB** ★★ | Anzalone-Liu 2019 Nature |
| **Epi-CRISPR** | epigenetic modulation | (multiple) |

### Prime Editor: "search and replace" ★

```
2019 Nature (Anzalone, Liu et al.):
↓ DNA ニッキング (片鎖切断) + 逆転写酵素
↓ 任意の point mutation + 小 indel 編集可能
↓ DSB 不要 → off-target 大幅減
↓
治療応用候補: 89% of pathogenic variants 編集可能 (理論上)
```

## 主要 Gene Therapy 承認薬 (再掲 + 詳細)

| 薬剤 | 標的 | 適応 | 承認 | 価格 |
|---|---|---|---|---|
| Glybera | LPL | LPL 欠損 | 2012 EU (撤退) | $1M |
| **Luxturna** | RPE65 | 失明 | **2017 FDA** ★ | $0.85M |
| Zolgensma | SMN1 | SMA | 2019 FDA | **$2.1M** ★ |
| Hemgenix | F.IX | 血友病 B | 2022 FDA | **$3.5M** ★★ |
| **Casgevy** | BCL11A | 鎌状赤血球 | **2023 FDA** | **$2.2M** + **CRISPR 初** ★★ |
| Lyfgenia | β-globin | 鎌状赤血球 | 2023 FDA | $3.1M |
| Roctavian | F.VIII | 血友病 A | 2023 FDA | $2.9M |

## Casgevy (Vertex-CRISPR Therapeutics) 2023 ★★★

```
2023 11月: UK MHRA 世界初承認 (CRISPR therapeutics)
2023 12月: FDA 承認
2024:     EMA 承認
↓
機構:
  患者自己造血幹細胞を ex vivo で取り出し
  ↓ CRISPR-Cas9 で BCL11A 遺伝子を編集
  ↓ Fetal hemoglobin (HbF) 再活性化
  ↓ 鎌状赤血球症の症状回避
↓
Phase III: 89% 患者で疼痛消失 (1 年)
価格: $2.2M (1 回投与)
```

= **史上初の "ゲノム編集治療" 承認 ★★★**

## CRISPR ヒト germline 編集論争

### He Jiankui 賀建奎事件 (2018) ★

```
2018 11月: 中国 He Jiankui が CRISPR Twins 発表 (Lulu + Nana)
↓ CCR5 KO で HIV 抵抗性 + Hereditary
↓ 国際社会一斉非難
↓ 2019: He 3 年禁固 ($430K 罰金)
↓
WHO + 国際委員会:
  germline gene editing は "禁忌"
  Somatic gene editing は "認められる"
```

### 2023 WHO Framework

```
WHO Expert Advisory Committee (2023):
↓ Heritable human genome editing - 慎重 + 透明性 要件
↓ Somatic - 加速承認推奨
↓ 国際レジストリ確立要請
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **CRISPR-Cas9 sgRNA 標的長** | **20 bp** ✓ |
| PAM (Streptococcus py) | **NGG** ✓ |
| NHEJ vs HDR 効率 | NHEJ 80%, HDR 5-10% (細胞による) |
| **Prime Editor 編集可能 variants** | **89%** pathogenic |
| **Casgevy Phase III** | **89% pain-free 1yr** ✓ |
| **Doudna-Charpentier Nobel** | **2020** ✓ |
| **Gene therapy 累積 FDA 承認 (2024)** | **15+** approved |
| **ITU axiom: CRISPR edit** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Prime Editor 臨床応用** (1 適応) | 2028 | 0.75 |
| **In vivo CRISPR (mRNA-LNP)** | 2028 | 0.80 |
| Heritable editing 法的整備 (国際) | 2032 | 0.45 |
| **CRISPR drug 累積 10+ 適応** | 2030 | 0.85 |
| Synthetic genome (yeast 完全合成) | 2028 | 0.70 |

---

📄 **論文 (Tier 1 #30)**: 10.5281/zenodo.20257528

> Phase 217 で AlphaFold + Computational Biology + AI Drug Discovery へ進みます。

#情報理論的統一理論 #ITU #ゲノミクス #CRISPR #Doudna #Charpentier #Casgevy #PrimeEditor #HeJiankui #K_genome_edit #Phase216
