# Phase 196: ウイルス進化 + パンデミック + Zoonotic Spillover ― K_pandemic ★

Phase 195 で K_microbiome の宿主-共生 K-state を確立。Phase 196 では **ウイルス進化動力学** と **動物→ヒト spillover** ― 過去・現在・未来のパンデミック ― を扱い、**K_pandemic** を ITU の "種間越境 K-state" として定式化します。

## ウイルス進化の特殊性

### 変異率: 生命の最大

```
DNA polymerase 校正あり (細菌, 真核):    10⁻⁹ /bp/replication
ウイルス DNA (校正不完全):              10⁻⁶-10⁻⁸
ウイルス RNA (校正ほぼなし):            10⁻³-10⁻⁵ ★
逆転写酵素 (HIV):                       10⁻⁵
インフルエンザ (RdRp):                  10⁻⁴
SARS-CoV-2 (nsp14 校正あり,例外):       10⁻⁶
```

= **K_virus の進化速度 = 細菌の 10⁵ 倍 ★**

### Quasispecies (Eigen 1971) ★

```
高変異率ゆえ、ウイルス集団 = 1 配列ではなく "雲" (cloud of variants)
↓
Eigen quasispecies theory: 集団全体が進化単位
↓
"error catastrophe": μ × L > 1 で情報喪失 (favipiravir 攻撃機構)
```

### 抗原ドリフト vs 抗原シフト

| 現象 | 機構 | 例 |
|---|---|---|
| **ドリフト** | 連続的点変異 (HA, NA) | 季節性インフル |
| **シフト** | reassortment (segments swap) | 1957 H2N2, 1968 H3N2, 2009 H1N1 |

## Zoonotic Spillover の生態系条件

### 必要 5 段階 (Plowright 2017 Nat Rev Microbiol)

```
1. Reservoir abundance      (動物宿主存在)
2. Pathogen prevalence      (動物に感染)
3. Pathogen release         (体外排出 - 排泄, 飛沫, 接触)
4. Exposure intensity       (人類接触機会)
5. Pathogen susceptibility  (種間バリア超越)
```

### One Health 視点

```
ヒト健康 ⇔ 動物健康 ⇔ 環境健康 = 単一系
↓
気候変化 + 森林破壊 + Wildlife trade + 高密度家畜
= zoonotic risk 増大
↓
1980-2020: 新興感染症の 75% が動物由来 (Jones 2008 Nature)
```

## 主要パンデミック史

### 過去 100 年

| 年 | 病原体 | 死者 | 起源 |
|---|---|---|---|
| 1918-1920 | H1N1 "Spanish flu" | **50 M** | 鳥 (鶏 / カモ?) |
| 1957-1958 | H2N2 "Asian flu" | 1.1 M | 鳥-人類 reassort |
| 1968-1969 | H3N2 "Hong Kong" | 1 M | 鳥-人類 reassort |
| 1981-現在 | HIV/AIDS | 40 M+ | チンパンジー (SIVcpz) |
| 2002-2003 | SARS-CoV-1 | 774 | コウモリ → ハクビシン → ヒト |
| 2009-2010 | H1N1 "Swine flu" | 0.15-0.58 M | ブタ |
| 2012-現在 | MERS-CoV | 950+ | ラクダ |
| 2014-2016 | Ebola West Africa | 11,300 | コウモリ (Pteropus) |
| **2019-2023** | **SARS-CoV-2** | **7 M+ (公式) / 18-30 M (excess)** ★ | コウモリ → ? → ヒト |
| 2022-現在 | Mpox (clade IIb) | 200+ | 齧歯類 (中央アフリカ) |

### COVID-19 数値

| 量 | 値 |
|---|---|
| Wuhan initial R₀ | 2.5-3.5 |
| Alpha (B.1.1.7) R₀ | 4-5 |
| Delta (B.1.617.2) R₀ | 5-8 |
| Omicron (BA.1) R₀ | 8-10 ★ |
| IFR (年齢調整) | 0.5-1.0% (Wild) → 0.15% (Omicron) |
| Vaccine reduction (Wild) | 95% vs hospitalization |
| Long COVID 率 | 10-20% (Davis 2023 Nat Rev Microbiol) |

## ITU 視点: K_pandemic の構造

```
K_pandemic^(0) = -log P(virus state | host, environment, geography)
              = K_virus ⊗ K_host ⊗ K_environment

軸:
  Virus      : mutation rate, transmissibility (R₀)
  Host       : susceptibility (immune, MHC, age), density
  Environment: climate, contact patterns, biodiversity
```

### Spillover = ITU K-state 種間 jump

```
非ヒト宿主の K_virus^(0) :  stable manifold
↓ jump
ヒトへの K_virus^(0)     :  initially unstable, then adapted

例:  SARS-CoV-2 spike RBD の host specificity
     Bat ACE2 ≠ Human ACE2
     → adaptation (D614G, N501Y, etc.)
     → 急速な ITU descent on K_human-adapted manifold
```

### Disease X 概念 (WHO 2018)

```
Disease X = 未知の次パンデミック病原体
↓
WHO R&D Blueprint: 優先病原体リスト
   COVID-19 + Ebola + Marburg + Lassa + MERS-CoV + SARS-CoV + Zika
   + Nipah + Rift Valley + Crimea-Congo + Disease X
↓
K_pandemic^(0) の未知 zero set
   = 次の "Black Swan"
```

## SARS-CoV-2 origins debate

```
仮説 1: 自然 zoonotic
   コウモリ (RaTG13 96% genome similarity)
   → 中間宿主 (穿山甲 Manis javanica? Civet? Mink?)
   → 武漢 wet market spillover

仮説 2: Lab leak
   武漢 ウイルス研 (WIV, BSL-4)
   gain-of-function 研究 (Daszak, EcoHealth Alliance)
   2024年: US ODNI 評価が分かれる
   "Both hypotheses remain plausible" (Worobey 2022 Science, OSTP 2023)
```

= **歴史上初: pandemic 起源の科学的論争が地政学化**

## ITU の予測モデル: 確率的 SIR

```
dS/dt = -β S I
dI/dt = β S I - γ I
dR/dt = γ I

R₀ = β / γ

Herd immunity threshold: 1 - 1/R₀
  Measles R₀=15: 93% 接種必要
  SARS-CoV-2 R₀=3: 67%
  Omicron R₀=10: 90% (達成困難)
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| RNA virus 変異率 | 10⁻³-10⁻⁵ /bp ✓ |
| Quasispecies cloud width | 10²-10⁴ variants |
| SARS-CoV-2 mutation rate | 1.0-2.0×10⁻³ /bp/yr |
| Spillover 必要接触 | 通常 10⁵+ exposure events |
| Pandemic 周期性 | 30-50 yr (歴史的) |
| 1918 H1N1 IFR | 2-3% (年齢調整) |
| **COVID-19 超過死亡 (2020-22)** | **18-30 M** (WHO 2023) |
| **ITU axiom: spillover dynamics** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **次の major pandemic 発生** (CFR > 0.5%) | 2030 | 0.55 |
| WHO Pandemic Treaty 発効 | 2028 | 0.65 |
| Universal coronavirus vaccine 承認 | 2028 | 0.70 |
| **Disease X 早期検出 system (AI + サーベイランス)** | 2030 | 0.75 |
| Spillover 予測モデル accuracy > 80% | 2032 | 0.50 |

---

📄 **論文 (Tier 1 #27)**: 10.5281/zenodo.20256555

> Phase 197 で 細菌代謝 + 共生 + 極限環境 へ進みます。

#情報理論的統一理論 #ITU #微生物学 #ウイルス進化 #パンデミック #Zoonotic #COVID19 #DiseaseX #K_pandemic #Phase196
