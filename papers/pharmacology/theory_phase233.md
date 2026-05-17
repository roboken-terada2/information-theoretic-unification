# Phase 233: AI 創薬 Deep ― Insilico + Recursion + Atomwise + K_pharma_AI ★

Phase 232 で K_pharma_immune の免疫療法を確立。Phase 233 では **AI 創薬産業** の深掘り ― Phase 217 AlphaFold extension + 主要 AI 創薬企業 + 実臨床応用 ― を扱い、**K_pharma_AI** を ITU の "AI 駆動 K-state 設計" として定式化します。

## AI 創薬: 主要企業 catalogue (2024)

### Insilico Medicine (中国-香港) ★

```
創業: 2014 (Alex Zhavoronkov)
拠点: Hong Kong + New York + Suzhou
主軸:
  - Generative AI (Pharma.AI platform)
  - PandaOmics: target discovery
  - Chemistry42: molecular design
  - InClinico: clinical outcome prediction

ステップ製品: INS018_055 ★ (TNIK inhibitor for IPF)
  2020: 21 日で AI 設計
  2021: Phase I 開始
  2023: Phase II 開始
  2024: Phase II 進行中

時価総額: 2024 IPO 計画 ($7-10B 推定)
```

### Recursion Pharmaceuticals (米国)

```
創業: 2013 (Chris Gibson, U of Utah)
拠点: Salt Lake City
主軸:
  - High-throughput cell imaging (millions of cells/week)
  - Map of biology (relationships between genes/compounds)
  - Multi-modal AI (vision + omics)

主要パートナー:
  - Bayer (multiple targets)
  - Roche/Genentech (neuroscience, oncology)
  - Tempus (acquired 2024)

製品 candidate:
  REC-994: Cerebral Cavernous Malformation (Phase II/III)
  REC-2282: NF2-mutated meningioma (Phase II/III)

2021 IPO at $1.8B; 2024 market cap ~$2.5B
```

### Atomwise (米国)

```
創業: 2012 (Abe Heifets)
拠点: San Francisco
主軸:
  - AtomNet: CNN for ligand-protein binding
  - 数十億 化合物 virtual screening
  - 700+ academic partners

主要 partnerships:
  - Eli Lilly ($1B 2019)
  - X-Chem
  - Bayer ($1B 2020)
  - Bridge Biotherapeutics
```

### BenevolentAI (英国)

```
創業: 2013 (Ken Mulvany)
拠点: London + New York
主軸:
  - Knowledge graph + literature mining
  - "Benevolent Platform" (relationship discovery)

主要成功例:
  - Baricitinib for COVID-19 (Eli Lilly partnership, 2020) ★
    EUA FDA 11/2020
  - BEN-2293 (atopic dermatitis, Phase II)
```

### Exscientia (英国)

```
創業: 2012 (Andrew Hopkins)
拠点: Oxford
主軸:
  - "Centaur" model (human + AI 協調)
  - 多目的 multi-objective optimization

主要薬剤:
  - EXS-21546 (immuno-oncology, Phase I)
  - EXS-21504 (psychiatry)
  
2023: Recursion と $700M 合併発表 → 2024 完了
```

### Verge Genomics, Healx, Schrödinger, Relay 等

```
Verge Genomics (米): ALS, Parkinson AI 創薬
Healx (英): rare disease repositioning
Schrödinger (米): physics-based + ML
Relay Therapeutics (米): "motion-aware" drug design
```

## 主要 AI 創薬の段階別影響

### Target Identification

```
Verge Genomics ALS analysis:
   12M public datasets
   ↓ Disease-specific gene networks
   ↓ VRG50635 (PIKfyve inhibitor)
   ↓ Phase II clinical 2024
   
Recursion + Bayer: 11 cardiovascular targets in 12 months
   vs 古典 1-2 years/target
```

### Hit Discovery

```
Atomwise AtomNet:
   72 million compounds virtual screened
   ↓ Top 50 candidates → biochemistry
   ↓ 10-20× success rate vs random
   
AI-discovered candidate molecules pipeline (2024):
   pre-clinical: 70+
   Phase I-III: 25+
```

### Lead Optimization

```
Insilico Chemistry42:
   Genetic algorithm + reinforcement learning
   ↓ 1 cycle: 5-15 day for molecular library
   ↓ Properties optimization: 12 parameters simultaneous

vs 古典: 1-2 year for lead opt
```

### Clinical Trial Design

```
Insilico InClinico:
   AI predicts Phase II → III success
   2024: 上場主張 79% accuracy
   ↓
   2030 予測: AI-managed adaptive trials standard
```

## 主要 AI 創薬パイプライン (2024 Phase I+)

| 薬剤 | 会社 | 段階 | 標的 |
|---|---|---|---|
| **INS018_055** | Insilico | **Phase II** | IPF (TNIK) |
| EXS-21546 | Exscientia | Phase I | Immuno-onc (A2aR) |
| REC-994 | Recursion | Phase II/III | CCM |
| REC-2282 | Recursion | Phase II/III | NF2 meningioma |
| BEN-2293 | BenevolentAI | Phase II | Atopic |
| VRG50635 | Verge Genomics | Phase II | ALS |
| **Baricitinib (COVID)** | BenevolentAI + Lilly | **FDA EUA 2020** | COVID-19 ★ |
| Halicin | MIT (Stokes lab) | Pre-clinical | Antibiotic ★ |

## Halicin (MIT 2020) - 古典 AI 創薬例 ★

```
2020 Stokes et al. (Cell):
↓ Deep learning on 2,335 compounds
↓ 107 million molecule screening
↓ Halicin (新規抗生剤) 発見
↓ E. coli + C. difficile + A. baumannii 効果
↓ Mechanism: proton motive force disruption
↓ Pre-clinical
```

## ITU 視点: K_pharma_AI の構造

```
K_pharma_AI^(0) = -log P(drug × target × patient | AI prior + data)

軸:
  Target prediction (Verge, Recursion)
  Molecule generation (Insilico, Schrödinger)
  Binding affinity prediction (Atomwise, Boltz-1)
  Trial design (InClinico)
  Multimodal data (Recursion)
  AI-AI synergy (multi-agent)

K_pharma_AI = K_pharma ⊗ K_AI (#2) ⊗ K_genome (#30, AlphaFold)
            ⊗ K_compute (#1, #4, #226 photonic)
```

### AI 創薬時短効果 (cumulative)

```
古典 創薬: 11-15 年, $2.6B
AI 創薬: 6-10 年, $1-1.5B (時短 30-50%)

成功率: 
   古典 Phase I → market: 10%
   AI-discovered Phase I → ?: too early (2024)
   InClinico 主張: 79% Phase II → III prediction accuracy
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Insilico INS018_055 design** | **21 日** (AI 駆動) ✓ |
| Insilico Phase II 開始 | 2023 ✓ |
| **Halicin AI 発見** | Stokes 2020 Cell ✓ |
| **Baricitinib COVID** | BenevolentAI + Lilly 2020 ✓ |
| **AI 創薬 pre-clinical pipeline** | 70+ candidates ✓ |
| **AI 創薬 clinical pipeline** | 25+ Phase I-III ✓ |
| AI 創薬時短 | **30-50%** ✓ |
| Recursion Bayer CV deal | 11 targets in 12 mo ✓ |
| **ITU axiom: AI drug discovery** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **First AI-discovered drug FDA approval** | 2028 | 0.75 |
| **AI 創薬 cum 5 FDA approvals** | 2030 | 0.80 |
| **AI clinical trial design standard** | 2028 | 0.70 |
| **In silico trial regulatory acceptance** | 2030 | 0.65 |
| **AI 創薬 industry M&A consolidation** | 2028 | 0.85 |

---

📄 **論文 (Tier 1 #32)**: 10.5281/zenodo.20258192

> Phase 234 で FDA + 臨床試験 + 規制 へ進みます。

#情報理論的統一理論 #ITU #薬理学 #AI創薬 #Insilico #Recursion #Atomwise #BenevolentAI #Exscientia #Halicin #Baricitinib #K_pharma_AI #Phase233
