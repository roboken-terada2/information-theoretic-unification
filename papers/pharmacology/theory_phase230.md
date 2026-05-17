# Phase 230: ADME + CYP450 + Pharmacogenomics ― K_pharma_PK ★

Phase 229 で K_pharma_target の受容体構造を確立。Phase 230 では **薬物動態 (PK)** + **CYP450 代謝** + **薬理ゲノミクス** を扱い、**K_pharma_PK** を ITU の "体内動態 K-state" として定式化します。

## ADME: 薬の体内 4 過程

| Phase | 機構 | 速度定数 |
|---|---|---|
| **A**bsorption (吸収) | 経口 → 腸 → 門脈 → 肝臓 → 全身循環 | k_a |
| **D**istribution (分布) | 血液 → 組織 (Vd) | t_distribution |
| **M**etabolism (代謝) | Phase I (CYP) + Phase II (conjugation) | k_metab |
| **E**xcretion (排泄) | 腎 (尿) + 胆汁 + 呼気 | k_excret |

### 主要 PK パラメータ

```
Bioavailability F: 経口投与から循環血中到達比 (0.0-1.0)
Volume of distribution Vd (L/kg): 0.1 (細胞外) - 50+ (脂溶性蓄積)
Clearance Cl (mL/min/kg): 体外除去速度
Half-life t₁/₂ = 0.693 × Vd / Cl: 1-100 hr
Cmax: 最大血中濃度
AUC: Area Under Curve (曝露量)
```

### 一区画 vs 二区画モデル

```
1-compartment: dC/dt = -k_e × C
   C(t) = C₀ × exp(-k_e × t)

2-compartment: distribution + elimination
   C(t) = A × exp(-α × t) + B × exp(-β × t)
   ↓ より realistic for most drugs
```

## Cytochrome P450 (CYP) 系

### Phase I 主要 CYP enzyme + 担当薬

| CYP | 担当 % | 代表薬 |
|---|---|---|
| **CYP3A4** | **50%** | Statins (atorvastatin), Calcineurin inhibitors |
| CYP2D6 | 25% | β-blockers, SSRIs, codeine |
| CYP2C9 | 15% | Warfarin, NSAIDs |
| CYP2C19 | 10% | Clopidogrel, PPIs |
| CYP1A2 | 5% | Caffeine, theophylline |
| CYP2E1 | <5% | Ethanol, acetaminophen |
| CYP2B6 | <5% | Efavirenz, bupropion |

### 主要 CYP3A4 阻害剤 / 誘導剤

```
強阻害剤:
  Grapefruit juice (furanocoumarins)
  Itraconazole (antifungal)
  Ritonavir (HIV protease inhibitor)
↓ 併用薬の血中濃度上昇 → 副作用
↓
強誘導剤:
  Rifampin (TB), Carbamazepine
↓ 併用薬濃度低下 → 治療失敗
```

### Phase II 代謝 (conjugation)

```
UGT (glucuronidation): UGT1A1 - bilirubin, irinotecan
SULT (sulfation): SULT1A1 - estradiol
NAT (acetylation): NAT2 - isoniazid
GST (glutathione): GSTP1 - oxidative stress
```

## Pharmacogenomics (PGx) ★

### 主要 CYP 多型 + 表現型

| 遺伝子 | 表現型 | 頻度 | 影響 |
|---|---|---|---|
| **CYP2D6** | PM/IM/EM/UM | PM 7-10% Caucasian, UM 1-2% | β-blockers, SSRIs |
| **CYP2C19** | PM | 15-20% Asian (>3%) | Clopidogrel, PPIs |
| **CYP3A5*3** | non-expressor | 80% Caucasian | Tacrolimus dosing |
| **TPMT** | Low/Intermediate/Normal | PM 0.3% | 6-MP, azathioprine |
| **HLA-B*5701** | + | 5-8% Caucasian | Abacavir (FDA preemptive) |
| **HLA-B*1502** | + | 10% Asian | Carbamazepine |
| **DPYD** | variant | 7-9% (Caucasian) | 5-FU dosing |

### CPIC Guidelines (Clinical Pharmacogenetics Implementation Consortium)

```
2009-: CPIC consortium 設立
↓ 100+ gene-drug pairs 推奨済み
↓ 米 PGRN (Pharmacogenomics Research Network)
2024: 主要病院で PGx routine testing 開始
   Mayo Clinic, Vanderbilt, Stanford
↓
Top 10 PGx tests:
  CYP2C19 (clopidogrel)
  CYP2D6 (tamoxifen)
  HLA-B*5701 (abacavir)
  HLA-B*1502 (carbamazepine)
  DPYD (5-FU)
  TPMT (6-MP)
  CYP3A5 (tacrolimus)
  VKORC1 (warfarin)
  UGT1A1 (irinotecan)
  CYP2C9 (warfarin)
```

### 経済学的影響

```
2024 推定: PGx testing で adverse drug reactions 30% 減
   米国年間 100,000 deaths from ADRs → 30,000 prevented
   コスト: $2,500 / patient (1-time genotyping)
   節約: $50,000 / prevented severe ADR
```

## ITU 視点: K_pharma_PK の構造

```
K_pharma_PK^(0) = -log P(drug concentration | patient genome, dose, time)

軸:
  Absorption (Ka, F)
  Distribution (Vd, tissue affinity)
  Metabolism (Vmax, Km, CYP genotype)
  Excretion (Cl, kidney/liver function)
  Genome (PGx variants)
  Comedications (DDI)

K_pharma_PK = K_pharma ⊗ K_genome (#30) ⊗ K_microbe (#27)
                       ⊗ K_age (Phase 6 link)
```

## Personalized Medicine 進化

| 年 | 出来事 |
|---|---|
| 1957 | Motulsky "Drug reactions, enzymes and biochemical genetics" |
| 1995 | TPMT deficiency 同定 |
| 2003 | Human Genome Project 完了 |
| 2007 | HLA-B*5701 + abacavir FDA preemptive testing |
| 2009 | CPIC consortium |
| 2018 | All of Us cohort (1M people, genome + EHR) |
| 2024 | 100K Genomes Project UK 完了 |

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **CYP3A4 担当** | **50%** of drugs ✓ |
| **CYP2D6 担当** | 25% ✓ |
| Grapefruit + statin t₁/₂ | 2-3× 増加 ✓ |
| CYP2C19 PM (Asian) | **15-20%** ✓ |
| HLA-B*5701 + abacavir | 5-8% Caucasian ✓ |
| **CPIC gene-drug pairs** | **100+** ✓ |
| **TPMT PM 頻度** | 0.3% ✓ |
| Annual US ADR deaths | 100,000 ✓ |
| **ITU axiom: drug PK** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **All hospitals PGx routine testing** | 2030 | 0.70 |
| Annual ADR deaths 50% reduction | 2032 | 0.65 |
| **All 1B humans genotyped** | 2035 | 0.55 |
| PGx-guided dosing algorithms for 50+ drugs | 2028 | 0.80 |
| Universal newborn PGx panel | 2030 | 0.75 |

---

📄 **論文 (Tier 1 #32)**: 10.5281/zenodo.20258192

> Phase 231 で 抗体医薬 + ADC + Bispecific へ進みます。

#情報理論的統一理論 #ITU #薬理学 #ADME #CYP450 #Pharmacogenomics #PGx #CPIC #TPMT #HLAB5701 #K_pharma_PK #Phase230
