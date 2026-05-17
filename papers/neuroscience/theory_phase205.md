# Phase 205: 神経変性疾患 + AD / PD / うつ / 統合失調症 ― K_pathology ★

Phase 204 で K_consciousness の Hard Problem を確立。Phase 205 では **神経疾患 4 大** ― AD / PD / うつ / 統合失調症 ― を扱い、**K_pathology** を ITU の "病的 K-state 偏位" として定式化します。

## アルツハイマー病 (AD)

### 神経病理学的特徴 (Alzheimer 1906)

```
1906: Alois Alzheimer (Frankfurt):
↓ Auguste Deter 51 歳症例
↓ Amyloid plaques (Aβ) + Neurofibrillary tangles (NFT, tau)
↓ 海馬萎縮 → 大脳皮質 → 死亡
```

### Amyloid hypothesis (Hardy-Selkoe 1992)

```
APP → β-secretase → γ-secretase → Aβ40, Aβ42
↓ Aβ42 oligomer (toxic 種, < fibril)
↓ NFT → 神経死 → 認知障害
↓
家族性 AD: APP, PSEN1, PSEN2 変異 → Aβ42 増加
APOE4 alleleキャリア: AD リスク 3-15×
```

### 治療: Lecanemab (Leqembi, 2023 FDA ★)

```
Anti-Aβ抗体 (humanized IgG1)
Phase III CLARITY AD (van Dyck 2023 NEJM):
   18 ヶ月で 認知低下 27% 抑制
   Aβ PET clearance 著明
↓
副作用: ARIA-E (脳浮腫) ~12%, 死亡 3 例 報告
↓
40 年来の amyloid hypothesis 初の臨床確証
```

## パーキンソン病 (PD)

### 病理 (Parkinson 1817)

```
James Parkinson "Shaking Palsy" (1817):
↓ Substantia nigra 黒質細胞死
↓ Dopamine 減少 → 運動症状 (tremor, rigidity, bradykinesia)
↓ Lewy body (α-synuclein 凝集) ★
↓
"Braak 仮説 2003": 病変が腸 → 迷走神経 → 脳幹 → 中脳 へ progress
                  Phase 195 Gut-Brain 接続 ★
```

### 治療

| 治療 | 概要 |
|---|---|
| **L-DOPA (1967)** | dopamine 前駆体, 古典的標準 |
| DBS (Deep brain stimulation, 1987) | STN/GPi 高頻度刺激 (Benabid) |
| GDNF / Neurotrophic factor | 補修療法 (試験段階) |
| α-synuclein vaccine | PRX002, 試験中 |
| **AAV gene therapy** | NRTN, GAD - 臨床 |

## うつ病 (Major Depression)

### モノアミン仮説 (1965)

```
Schildkraut: NE/5-HT 低下 → うつ
↓ TCA, MAOI, SSRI が効果
↓ しかし 30% 治療抵抗
```

### Ketamine = NMDA antagonist (Zarate 2006) ★

```
従来 SSRI: 効果まで 2-4 週
↓ ↓
Ketamine: 2 時間で効果 ★
↓ Spravato (esketamine, 2019 FDA 承認)
↓ Glutamate hypothesis 確立
↓ "脳内 plasticity rapid restoration"
```

### Psychedelic renaissance

```
Psilocybin (Compass Pathways):
  Phase III for treatment-resistant depression
  2024 expected approval

MDMA-assisted therapy for PTSD:
  Phase III complete; FDA expected 2024-25 (delayed)

DMT, LSD: research phase
```

## 統合失調症 (Schizophrenia)

### 病理 (Kraepelin 1893, Bleuler 1911)

```
Bleuler 1911: "schizophrenia" 命名 (mind splitting)
↓ Positive symptoms: 幻覚, 妄想
↓ Negative symptoms: 無感情, 引きこもり
↓ Cognitive: WM 障害, 実行機能低下
```

### Dopamine hypothesis (Carlsson 1963, Nobel 2000)

```
Mesolimbic DA 過剰: positive symptoms
Mesocortical DA 不足: negative + cognitive

D2 antagonist (haloperidol, risperidone):
  positive 症状有効; negative には限定
```

### Genetic basis (GWAS)

```
PGC schizophrenia GWAS 2022:
↓ 287 risk loci 同定
↓ MHC region, DRD2, GRIN2A
↓ heritability ~ 80%
```

## 疾病負担: 世界レベル

| 疾患 | 罹患者 | DALYs (M/yr) |
|---|---|---|
| Depression | 280 M | 50.0 |
| AD/Dementia | 55 M | 28.5 |
| PD | 8.5 M | 5.8 |
| Schizophrenia | 24 M | 15.0 |
| Stroke | 13 M | 143.0 |
| **計 神経精神** | **~400 M** | **~250 M** |

= **世界疾病負担の最大カテゴリ** (Lancet 2024)

## ITU 視点: K_pathology の構造

```
K_pathology^(0) = 健常 K-state からの偏位
              = K_neuro^(0) の局所 minimum trap

AD:    K_memory 退化 + K_neuron 死 (海馬 → 皮質)
PD:    K_motor (黒質-線条体路) 偏位
うつ:  K_emotion + K_reward の global descent (anhedonia)
統失:  K_perception (positive) + K_executive (negative) の dual 偏位
```

### Bouncing back: 治療 = K-state restoration

```
Lecanemab (AD):  K_memory の Aβ-trap 解除
L-DOPA (PD):     K_motor の DA depletion 補填
Ketamine (うつ): K_neuro の rapid plasticity restoration
Risperidone (統失): K_DA の rebalancing
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| AD prevalence 65 歳以上 | 10% ✓ |
| AD 65 → 85 歳 | 累積 50% (Brookmeyer 2007) |
| APOE4 ホモ AD risk | 12-15× ✓ |
| **Lecanemab 認知低下抑制** | **27%** (CLARITY AD) ✓ |
| PD 黒質細胞死率 | 5%/年 (発症前 10 年で 80% 死亡時) |
| L-DOPA "honeymoon" | 5-10 年 |
| **Ketamine 抑うつ効果** | 2 時間 → 1 週間 ✓ |
| Schizophrenia 男女罹患率 | 1.4:1 (男性やや多い) |
| 統失 GWAS 287 loci | PGC 2022 ✓ |
| **ITU axiom: pathology** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Lecanemab follow-on 多剤併用 (anti-tau)** | 2028 | 0.75 |
| Psilocybin FDA 承認 (TRD) | 2028 | 0.70 |
| MDMA-assisted therapy 承認 | 2027 | 0.55 |
| **α-synuclein vaccine 効果** | 2030 | 0.50 |
| Schizophrenia molecular 診断 biomarker | 2032 | 0.45 |

---

📄 **論文 (Tier 1 #28)**: 10.5281/zenodo.20256729

> Phase 206 で 統合 + 28-vertex polytope + Tier 1 #28 完成 + Pass-1 93.6% へ進みます。

#情報理論的統一理論 #ITU #神経科学 #AD #PD #うつ病 #統合失調症 #Lecanemab #Ketamine #K_pathology #Phase205
