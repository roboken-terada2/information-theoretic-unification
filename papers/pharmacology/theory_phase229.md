# Phase 229: GPCR + Ion Channel + Structural Pharmacology ― K_pharma_target ★

Phase 228 で K_pharma 全体像を確立。Phase 229 では **GPCR + Ion channel + 構造薬理学** ― 創薬最大の標的群 ― を扱い、**K_pharma_target** を ITU の "受容体 K-state operator" として定式化します。

## GPCR (G-Protein Coupled Receptor)

### 7-transmembrane (7TM) 構造

```
N末 → TM1 → ICL1 → TM2 → ECL1 → ... → TM7 → C末
↓
細胞外: リガンド結合 (orthosteric site)
細胞内: G protein binding (helix 8)
```

### Class A/B/C/F (B2-AR は class A 代表)

| Class | 例 | リガンド |
|---|---|---|
| **A (rhodopsin-like, 80%)** | β-AR, dopamine, opioid | 小分子 / amine |
| B (secretin) | GLP-1R, glucagon, CGRP | peptide |
| C (glutamate) | mGluR, GABA-B, CaSR | 小分子 / amino acid |
| F (frizzled) | FZD, smoothened | lipid-modified protein |

### Lefkowitz-Kobilka Nobel 2012 詳細 ★

```
1979: Lefkowitz first GPCR cloning
1980s: β1/β2-AR sequence determined
2007: Kobilka crystallized β2-AR (Nature)
2011: β2-AR + Gs complex (Science) ★
   "Visualizing GPCR signaling"
2012: Nobel Chemistry
↓
2024: 200+ GPCR 結晶構造 (50% of human GPCRs covered)
   AlphaFold で全 800 GPCR 構造予測 (信頼度の差)
```

### Biased agonism (Lefkowitz 2007)

```
古典: agonist activates all downstream pathways equally
2007 発見: ある agonist は G protein 経由 OR β-arrestin 経由 を選択的
↓
"Biased agonist": side effect 減 + efficacy 維持
例:
  TRV130 (oliceridine): μ-opioid biased, less respiratory depression
  2020 FDA 承認 (痛み)
```

## GLP-1 receptor agonists (現代最大成功)

### Ozempic / Mounjaro / Wegovy (2024) ★

```
GLP-1: Glucagon-Like Peptide-1 (29 aa peptide)
GLP-1R: GPCR class B
↓
1993: Bayliss + Starling 概念
2005: Exenatide (Byetta) first GLP-1 agonist
2017: Semaglutide (Ozempic) - 1/week injection
2021: Wegovy (semaglutide 2.4 mg) - 肥満適応 ★
2022: Mounjaro (tirzepatide, dual GLP-1/GIP)
↓
2024 売上: Ozempic + Wegovy $30B+, Mounjaro $11.5B
体重減 15-20% (15-22 kg) - 史上最大効果
```

## Ion channel pharmacology

### 主要 channel + 代表薬

| Channel | 機能 | 代表薬 |
|---|---|---|
| **Nav (Na⁺)** | 活動電位 | Local anesthetic (lidocaine), Antiepileptic (carbamazepine) |
| **Kv (K⁺)** | 過分極 | Amiodarone (心房細動) |
| **Cav (Ca²⁺) L** | 心血管 | Amlodipine, Verapamil (CCB) |
| **Cav N/P/Q** | 神経終末 | Ziconotide (慢性痛, ω-conotoxin) |
| **GABA-A (Cl⁻)** | 抑制性 | Benzodiazepine (diazepam) |
| **nAChR (cation)** | 神経筋接合 | Varenicline (smoking cessation) |
| **TRP** | 感覚 | Capsaicin (TRPV1) |

### MacKinnon Nobel 2003 ★

```
Roderick MacKinnon (Rockefeller):
↓ 1998: KcsA K+ channel crystal structure (Science)
↓ "Selectivity filter" molecular basis
↓ Nobel Chemistry 2003
↓
解明: なぜ K+ が Na+ より 10⁴× 通りやすいか
   → carbonyl O が K+ サイズに最適化された配置
```

## Receptor Tyrosine Kinase (RTK)

### 主要 RTK + 治療薬

| RTK | がん | 薬 |
|---|---|---|
| **EGFR** | NSCLC | Gefitinib, Erlotinib, Osimertinib |
| **HER2** | 乳がん | Trastuzumab (Herceptin), T-DM1 |
| **VEGFR** | 多くのがん | Bevacizumab (Avastin), Sunitinib |
| **BCR-ABL** | CML | **Imatinib (Gleevec) ★** |
| **ALK** | NSCLC | Crizotinib, Alectinib |
| **BRAF** | 黒色腫 | Vemurafenib |

### Kinase inhibitor 化学構造原理

```
ATP 結合部位を競合阻害 (type I)
DFG-out conformation 安定化 (type II - 多くの近代薬)
↓
Drug-likeness:
   small mol (MW 300-600)
   Selectivity for target kinase ≥ 10× vs related
   Oral bioavailability
```

## Allosteric drug design (新世代)

### Allosteric site の利点

```
Orthosteric: リガンド結合部位 - 自然リガンド類似
Allosteric: 他の部位 - 機能 modulation
↓
利点:
  - 高い選択性 (orthosteric は GPCR family で似ている)
  - 飽和性 (内因性 ligand と協調)
  - 新しい薬理学的 profile
↓
例:
  Cinacalcet (CaSR allosteric, hyperparathyroidism)
  Maraviroc (CCR5 allosteric, HIV)
```

## ITU 視点: K_pharma_target の構造

```
K_pharma_target^(0) = -log P(downstream signaling | drug binding mode)

軸:
  Binding site (orthosteric vs allosteric)
  Affinity (Kd, nM to mM)
  Selectivity (>10× vs related targets)
  Conformational state (active/inactive/biased)
  Downstream (G_s/G_i/G_q/G_12 vs β-arrestin)

K_pharma_target = K_pharma の最深 sub-state
   ⊂ K_genome (target gene)
   ⊂ K_AI (AlphaFold で予測)
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **GPCR 数** | **800 ヒト** ✓ |
| GPCR 結晶構造 (2024) | 200+ ✓ |
| **Lefkowitz-Kobilka Nobel** | 2012 ✓ |
| **MacKinnon Nobel** | 2003 ✓ |
| K+/Na+ selectivity | **10⁴×** ✓ |
| **Semaglutide 体重減** | **15-20%** ✓ |
| **Tirzepatide 体重減** | **22%** ✓ |
| TRV130 oliceridine FDA | 2020 ✓ |
| GLP-1 + GIP dual | Mounjaro 2022 ✓ |
| **ITU axiom: receptor activation** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **All 800 GPCR cryo-EM structures** | 2028 | 0.80 |
| **GLP-1 agonist 5+ adapatations** (CV, Alzheimer, addiction) | 2030 | 0.85 |
| **Allosteric drug 10+ new FDA approvals** | 2030 | 0.75 |
| Biased agonist mainstream class | 2028 | 0.70 |
| AI-designed allosteric drugs | 2028 | 0.75 |

---

📄 **論文 (Tier 1 #32)**: 10.5281/zenodo.20258192

> Phase 230 で ADME + CYP450 + Pharmacogenomics へ進みます。

#情報理論的統一理論 #ITU #薬理学 #GPCR #Lefkowitz #Kobilka #MacKinnon #IonChannel #Imatinib #GLP1 #Ozempic #Mounjaro #BiasedAgonism #K_pharma_target #Phase229
