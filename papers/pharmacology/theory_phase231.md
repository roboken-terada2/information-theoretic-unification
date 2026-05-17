# Phase 231: 抗体医薬 + ADC + Bispecific Antibody ― K_pharma_biologic ★

Phase 230 で K_pharma_PK の ADME + PGx を確立。Phase 231 では **抗体医薬** + **ADC (抗体薬物複合体)** + **Bispecific Antibody** ― 21 世紀製薬産業の中核 ― を扱い、**K_pharma_biologic** を ITU の "高分子治療 K-state" として定式化します。

## 抗体医薬革命史

### Köhler-Milstein hybridoma (1975, Nobel 1984) ★

```
Georges Köhler + César Milstein (Cambridge MRC):
↓ 1975 Nature: B cell + myeloma fusion → 単一クローン Ab 生産
↓ "Hybridoma technology"
↓ 1984 Nobel Physiology/Medicine (Jerne と共同)
↓
2024: hybridoma → phage display → transgenic mouse → AI design
```

### 主要抗体世代

| 年 | 技術 | 抗原性問題 |
|---|---|---|
| 1986 | Murine (mouse) | HAMA 100% |
| 1988 | Chimeric (mouse/human) | HAHA 30% |
| 1990 | Humanized (CDR-grafted) | <10% |
| 1994 | Fully human (phage / transgenic) | 最小 |
| 2024 | AI-designed human | TBD |

### 主要 mAb FDA 承認 milestone

| Year | Drug | Target | Disease |
|---|---|---|---|
| 1986 | Muromonab-CD3 (OKT3) | CD3 | 移植拒絶 (初) |
| 1997 | **Rituximab (Rituxan)** | CD20 | B cell lymphoma ★ |
| 1998 | **Trastuzumab (Herceptin)** | HER2 | Breast cancer ★ |
| 2002 | Adalimumab (Humira) | TNF-α | RA/Crohn |
| 2014 | **Pembrolizumab (Keytruda)** | PD-1 | Melanoma → 全がん ★ |
| 2014 | Nivolumab (Opdivo) | PD-1 | Melanoma |
| 2018 | Dupilumab (Dupixent) | IL-4Rα | Atopic dermatitis |
| 2023 | Lecanemab (Leqembi) | Aβ | Alzheimer (#29 link) |

## ADC (Antibody-Drug Conjugate) ★

### 構造

```
Antibody (HER2, CD22, ...) - Linker - Payload (toxin)
↓
受容体結合 → 内在化 → リソソーム分解 → toxin 放出
↓ "Magic bullet" (Ehrlich 1900) の現代実装
```

### 主要 ADC FDA 承認

| 薬剤 | 標的 | Payload | 適応 | 承認 |
|---|---|---|---|---|
| **Mylotarg** | CD33 | Calicheamicin | AML | 2000 (initially withdrawn, re-approved 2017) |
| **Kadcyla (T-DM1)** | HER2 | DM1 | HER2+ breast | 2013 |
| **Adcetris** | CD30 | MMAE | HL | 2011 |
| **Enhertu (T-DXd)** | HER2 | DXd (topo I inh) | HER2-low breast ★ | 2019 → expanded 2022 |
| **Trodelvy** | TROP2 | SN-38 | TNBC | 2020 |
| **Padcev** | Nectin-4 | MMAE | Urothelial | 2019 |
| **Blenrep** | BCMA | MMAF | MM | 2020 (withdrawn 2022) |

### Enhertu (T-DXd) 革命 (2022) ★

```
従来 HER2 standard: HER2+ (3+ IHC or FISH+) only
Enhertu DESTINY-Breast04 (2022 NEJM):
↓ HER2-LOW (1+ or 2+ FISH-) → previously incurable
↓ HR for death 0.64 (NEJM 2022)
↓ 6 month median PFS improvement
↓ "Reshape the HER2 landscape"
```

## Bispecific Antibody (BsAb) ★

### 構造

```
2 different antigen binding sites (Fab × 2)
↓ 1 arm: T cell (CD3) recruit
↓ Other arm: tumor antigen
↓ "T cell engager" (BiTE)
```

### 承認薬

| 薬剤 | 標的 | 適応 | 承認 |
|---|---|---|---|
| **Blincyto** | CD3 × CD19 | ALL | 2014 (BiTE 初) |
| **Hemlibra** | F.IX × F.X (mimic FVIII) | Hemophilia A | 2017 |
| **Rybrevant** | EGFR × MET | NSCLC | 2021 |
| **Faricimab** | VEGF-A × Ang-2 | nAMD/DME | 2022 |
| **Tecvayli** | BCMA × CD3 | Multiple myeloma | 2022 |
| **Elrexfio** | BCMA × CD3 | MM | 2023 |
| **Talquetamab** | GPRC5D × CD3 | MM | 2023 |
| **Epkinly** | CD20 × CD3 | DLBCL | 2023 |

### Hemlibra (emicizumab) - 病態 mimicry ★

```
Hemophilia A: F.VIII 欠損
従来: F.VIII 補充 (週 3 回 IV)
Hemlibra: F.IX + F.X を架橋して F.VIII の機能を模倣
↓ 月 1 回 皮下注射
↓ 出血 87% 減 (HAVEN-3 NEJM 2018)
↓ "Functional replacement" 新概念
```

## ADC + Bispecific の市場 (2024)

```
ADC market 2024: $13 B
ADC market 2030 予測: $50 B
Bispecific 2024: $7 B
Bispecific 2030: $30 B
↓
Combined oncology biologic: $80 B (top growth segment)
```

## ITU 視点: K_pharma_biologic の構造

```
K_pharma_biologic^(0) = -log P(targeted cell kill | Ab × payload/recruit × patient)

軸:
  Antibody specificity (target × isoform)
  Linker chemistry (cleavable vs non-cleavable)
  Payload mechanism (MT inh, topo, DNA cross-link, radio)
  Internalization rate
  Bystander effect (cell-cell killing)
  Immune cell recruitment

K_pharma_biologic = K_pharma ⊗ K_immune (#26) ⊗ K_genome (#30)
```

### Antibody = ITU specific operator ★

```
Trastuzumab (Herceptin) operator:
   HER2 (+: 20% breast cancer)
   → ADCC + apoptosis
   → 患者群選択 + 効果 specific
   
Pembrolizumab (Keytruda) operator:
   PD-1 (T cell)
   → "Release the brake"
   → 25+ cancer types (universal)

Enhertu (T-DXd) operator:
   HER2 (1+ も含む)
   → DXd payload で bystander 効果
   → "HER2-low" 新 category
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Köhler-Milstein Nobel** | **1984** ✓ |
| Trastuzumab 承認 | 1998 ✓ |
| Keytruda 2024 sales | $25 B ✓ |
| **Kadcyla (T-DM1) 承認** | 2013 ✓ |
| **Enhertu HER2-low** | DESTINY-Breast04 2022 ✓ |
| **Blincyto BiTE 初承認** | 2014 ✓ |
| **Hemlibra HAVEN-3** | 出血 87% 減 ✓ |
| ADC market 2030 予測 | **$50 B** ✓ |
| Bispecific 2024 sales | $7 B ✓ |
| **ITU axiom: targeted biologic** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **ADC market $50 B** | 2030 | 0.85 |
| **Trispecific antibody 承認** | 2028 | 0.70 |
| **AI-designed first-in-class Ab** | 2028 | 0.75 |
| ADC for solid tumor (multiple) | 2028 | 0.80 |
| ADC + IO 標準併用 (NSCLC) | 2030 | 0.75 |

---

📄 **論文 (Tier 1 #32)**: 10.5281/zenodo.20258192

> Phase 232 で Vaccines + Immunotherapy deep (#26 link) へ進みます。

#情報理論的統一理論 #ITU #薬理学 #抗体 #ADC #Bispecific #KohlerMilstein #Nobel1984 #Herceptin #Keytruda #Enhertu #Blincyto #Hemlibra #K_pharma_biologic #Phase231
