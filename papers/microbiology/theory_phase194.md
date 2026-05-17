# Phase 194: Antibiotic Resistance + Plasmid + AMR 分子機構 ― K_resistance ★

Phase 193 で K_phage + CRISPR の memory K-state 機構を確立。Phase 194 では **21 世紀最大の医療危機** = 抗生剤耐性 (AMR) の分子機構と集団動力学を扱い、**K_resistance** を ITU の "急速拡散 K-state" として定式化します。

## 抗生剤の歴史

```
1928: Fleming Penicillin 発見
1942: Florey-Chain 工業生産 (Nobel 1945)
1944: Streptomycin (Waksman, Nobel 1952)
1950s-1970s: "Antibiotic golden age" (cephalosporins, macrolides, tetracyclines, ...)
1980s-: 新規抗生剤承認激減 ★
2000s-: AMR 危機表面化
2019: WHO 10 大健康脅威に AMR
2022: Murray Lancet — AMR 死亡 127 万人/年 ★
```

## 抗生剤の作用機序 5 分類

| 標的 | 例 | 結果 |
|---|---|---|
| 細胞壁合成 | β-lactam (ペニシリン, セファロスポリン) | 殺菌 |
| タンパク合成 30S | アミノグリコシド (ストレプトマイシン) | 殺菌 |
| タンパク合成 50S | マクロライド, クリンダマイシン | 静菌 |
| DNA 複製 | フルオロキノロン (シプロフロキサシン) | 殺菌 |
| 葉酸合成 | サルファ剤, トリメトプリム | 静菌 |

## 耐性機構: 4 分類

| 機構 | 例 |
|---|---|
| **薬剤分解** | β-lactamase (TEM, SHV, **NDM-1**, KPC) |
| **薬剤改変** | アミノグリコシド-修飾酵素 (AAC, APH, ANT) |
| **標的改変** | PBP2a (MRSA), Vancomycin VanA (D-Ala-D-Lac) |
| **排出 / 透過低下** | efflux pump (AcrAB-TolC), porin loss |

## NDM-1: 21 世紀 AMR の象徴

```
2008: New Delhi で初検出 (Yong 2009 AAC)
分子: New Delhi Metallo-β-lactamase
↓ 全 β-lactam (carbapenem 含む) を分解
↓ Zn²⁺ 依存 (typeB carbapenemase)
↓ blaNDM-1 遺伝子は plasmid 上 → 急速拡散
2010-2024: 70+ 国, 細菌種 60+ 種で検出 ★
```

### blaNDM 拡散経路

```
原産: South Asia (India, Pakistan, Bangladesh)
↓ 国際移動者 (medical tourism, travelers)
↓ Enterobacteriaceae (大腸菌, K. pneumoniae) + Acinetobacter
↓ 病院内感染 → 市中感染
↓ 食糧連鎖 (poultry, swine)
↓ 環境 (河川水, 廃水)
↓ ★ "One Health" 連鎖 ★
```

## プラスミドと水平遺伝子伝播

### プラスミド分類

| Incompatibility group | 担う耐性 | 例 |
|---|---|---|
| **IncF** | ESBL (CTX-M-15) | epidemic global |
| **IncH** | NDM, KPC, OXA | epidemic carbapenem |
| **IncN** | KPC | hospital |
| **IncP** | broad-host (multi-species) | environmental |
| ColE1 | small, mobilizable | common |

### Conjugation: 細菌の "sex"

```
F+ (donor) cell:
  - F factor 上 tra operon → pilus 形成
  - Type IV secretion system (T4SS)
F- (recipient) cell:
  - pilus 接触 → DNA 一鎖伝達
  - Rolling circle replication
所要時間: 5-30 分で 100 kb プラスミド転送
転送頻度: 10⁻²-10⁻⁶ /細胞/世代
```

### Plasmid + transposon = 多剤耐性運搬車

```
1 つの conjugative plasmid (~100 kb) に複数 transposon が乗り
↓ 10-15 耐性遺伝子を 1 回の HGT で運搬可能
↓ ★ MDR / XDR / PDR 病原体出現の主機構 ★

ESKAPE pathogen の MDR plasmid 例:
  - K. pneumoniae IncFII pKpQIL: KPC + ESBL + aminoglycoside + tetracycline
```

## 耐性発生の速度: ITU 視点

```
δlog(R) / δt = k₁·(antibiotic conc) - k₂·(fitness cost)
            ⇒ S-shaped emergence + 拡散 sigmoid

Plasmid HGT による集団拡散時間: 数ヶ月-数年
Mutation-driven (chromosomal): 5-50 世代 (1-2 日)
```

### K_resistance^(0) の動力学

```
K_resistance^(0) = -log P(resistant phenotype | exposure)
                 = -log P(resistance gene | genomic context)

選択圧 (antibiotic exposure) ⇒ δ⟨K⟩ < 0 (R 株の頻度上昇)
HGT (plasmid spread) ⇒ K-state 集団間 jump
⇒ S(susceptible repertoire) 減少 = ITU descent
```

## ESKAPE 病原体: WHO Priority Pathogen List 1

| 病原体 | 耐性表現型 | WHO 2024 priority |
|---|---|---|
| **E. faecium** | VRE (Vancomycin-resistant) | Medium |
| **S. aureus** | MRSA, VRSA | High |
| **K. pneumoniae** | CRE (Carbapenem-resistant) | **Critical** ★ |
| **A. baumannii** | CRAB | **Critical** ★ |
| **P. aeruginosa** | CRPA | **Critical** ★ |
| **Enterobacter** | ESBL, CRE | Critical |

## 新規抗生剤承認: 30 年衰退

```
1980-1990: 大量承認 (~5/year)
1990-2000: 減少 (~2-3/year)
2000-2010: 激減 (~1-2/year)
2010-2024: 細々 (~1-2/year, 多くは派生品)
↓
"Antibiotic discovery void"
↓
原因:
  - 経済的に不採算 (短期治療 vs 開発費 $1B+)
  - 微生物源 (Streptomyces) からの新分子枯渇
  - 大手製薬撤退 (Pfizer, AstraZeneca 抗生剤部門解体)
```

### 治療オプション枯渇例

```
Carbapenem-resistant Acinetobacter baumannii (CRAB):
  Polymyxin B / colistin (1959, 腎毒性で除外されていた)
  Tigecycline (2005, off-label, bacteriostatic limit)
  Eravacycline (2018)
  Cefiderocol (2019, $$$$, 即耐性)
  → これ以上の選択肢なし!
```

## ITU 視点: K_resistance の予測 model

```
R(t) = R₀ + (1 - R₀) · sigmoid((t - t_emergence) / τ)

τ ∝ exp(K_resistance^(0) / kT_selection)
   selection 強度 ↑ ⇒ τ 短縮 ⇒ 急速拡散
```

### 数値予測

| 量 | 予測値 |
|---|---|
| 新規抗生剤 t_emergence (典型) | 5-10 年で 50% strain 耐性 |
| Cefiderocol → resistance | **1 年** ★ (Bonomo 2020) |
| HGT plasmid 1 ヶ月拡散 | 1 病院内, 50%+ K. pneumoniae 株 |
| 国際拡散 (global spread) | 5-10 年 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AMR 死亡 2030 突破 350 万/年** | 2030 | 0.65 |
| 新規 antibiotic クラス (last-resort) 承認 | 2028 | 0.45 |
| **AI-discovered antibiotic 臨床応用** (halicin 等) | 2030 | 0.70 |
| Plasmid-curing therapy (anti-plasmid) 承認 | 2032 | 0.40 |
| Global AMR surveillance system (WHO GLASS 拡張) | 2030 | 0.75 |

---

📄 **論文 (Tier 1 #27)**: 10.5281/zenodo.20256555

> Phase 195 で マイクロバイオーム + Gut-Brain Axis + FMT へ進みます。

#情報理論的統一理論 #ITU #微生物学 #抗生剤耐性 #AMR #NDM1 #ESKAPE #プラスミド #K_resistance #Phase194
