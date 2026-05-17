# Phase 187: Tolerance + Autoimmunity ― AIRE + Tregs + SLE/RA + K_tolerance ★

Phase 186 で胚中心の ITU descent flow (affinity maturation) を確立。Phase 187 では **自己/非自己境界の維持機構** ― 中枢/末梢寛容 (central/peripheral tolerance) + 自己免疫疾患を扱い、**K_tolerance** を ITU forbidden subset として定式化します。

## 中枢寛容 (Central Tolerance, 胸腺)

### 胸腺 negative selection

```
未熟 T 細胞 → 胸腺 medulla
↓
mTEC (medullary thymic epithelial cell) が自己抗原提示
↓
強く反応する thymocyte → apoptosis (clonal deletion)
弱く反応する → Treg 分化 or 末梢へ
```

### AIRE (Auto-Immune REgulator, 1997)

```
AIRE 遺伝子 (21q22.3)
↓ 転写因子として mTEC で発現
↓ 末梢組織特異的抗原 (insulin, thyroid peroxidase, etc.) を異所性発現
↓ 自己反応 T 細胞を thymic deletion で除去
```

### AIRE 機能喪失 → APECED (自己免疫多腺性内分泌障害症候群)

```
APECED = Autoimmune Polyendocrinopathy-Candidiasis-Ectodermal Dystrophy
発症: 副甲状腺機能低下 + Addison 病 + 慢性カンジダ症
遺伝子: AIRE 常染色体劣性
頻度: 1/9,000 (フィンランド), 1/14,000 (サルディーニャ)
```

## 末梢寛容 (Peripheral Tolerance)

### Treg (Regulatory T cell, Sakaguchi 1995)

```
CD4+ CD25+ FoxP3+ T 細胞
末梢で active immunosuppression を実行
- IL-10, TGF-β 分泌
- CTLA-4 経由で APC 抑制
- IL-2 capture で effector T 抑制
```

### FoxP3 機能喪失 → IPEX 症候群

```
IPEX = Immune dysregulation, Polyendocrinopathy, Enteropathy, X-linked
発症: 重症腸炎 + 1 型糖尿病 + 湿疹
治療: HSCT 必須 (untreated lethal in 2 yr)
頻度: 極めて稀 (1/100,000 male births)
```

### 寛容の 5 機構

| # | 機構 | 部位 | キー分子 |
|---|---|---|---|
| 1 | Clonal deletion | 胸腺 | AIRE, MHC, TCR |
| 2 | Clonal anergy | 末梢 | TCR signal without CD28 |
| 3 | Treg suppression | 末梢 | FoxP3, IL-10, TGF-β |
| 4 | Activation-induced death | 末梢 | Fas/FasL |
| 5 | Privileged sites | 眼, 脳, 精巣 | barrier + TGF-β |

## 自己免疫疾患: 自己/非自己境界の破綻

### 代表的疾患

| 疾患 | 自己抗原 | 主な機構 | 罹患率 |
|---|---|---|---|
| **SLE** (全身性エリテマトーデス) | dsDNA, snRNP, histone | type III hypersensitivity (immune complex) | 0.05% |
| **RA** (関節リウマチ) | citrullinated peptide (anti-CCP) | type IV (T cell + B cell) | 0.5-1% |
| **1 型糖尿病** | insulin, GAD-65, IA-2 | type IV (CD8+ killing β cell) | 0.4% |
| **多発性硬化症** | MOG, MBP (myelin) | type IV (Th1/Th17) | 0.1% |
| **橋本病** | thyroglobulin, TPO | type IV + type II | 1-2% |
| **Graves 病** | TSHR (TSH 受容体) | type II 刺激抗体 | 0.5% |
| **Sjögren 症候群** | Ro/SSA, La/SSB | type IV 唾液腺破壊 | 0.5% |

### 数値: 自己免疫疾患の集合的負担

```
推定総罹患率 (米欧): 5-10%
F:M 比: 2-9:1 (女性優位)
遺伝率: HLA + 多遺伝子 + 環境
```

## ITU 視点: K_tolerance を ITU forbidden subset として ★

```
K_tolerance^(0) : ITU 公理の "禁止領域" 演算子
  = -log P(allowed clone | self-MHC + self-peptide universe)

中枢寛容 = K_tolerance^(0) の global zero-set 削除
  ⇒ ρ_repertoire を制約多様体に拘束

末梢寛容 = K_tolerance^(0) の local damping
  ⇒ dynamics の reactive region を抑制
```

### 自己免疫疾患 = K_tolerance 破綻

```
SLE:       K_tolerance^(0) の dsDNA + snRNP 領域 leakage
RA:        K_tolerance^(0) の citrullinated antigen 認識ホールが侵食
T1D:       K_tolerance^(0) の insulin + β-cell 領域消失
```

## 重要数値

| 量 | 値 |
|---|---|
| 胸腺 thymocyte 産生/日 (若年) | 10⁹ |
| Negative selection 除去率 | **95-99%** (1-5% のみ生存) |
| 末梢 Treg fraction (CD4+ T 中) | **5-10%** |
| FoxP3+ Treg 半減期 | 数週間 |
| AIRE-/- マウス autoimmune phenotype | 95% (Anderson 2002) |
| **FoxP3-/- マウス (scurfy)** | **lethal 3-4 週で多臓器不全** |

## 実験データ

| 観察 | 値 | 出典 |
|---|---|---|
| dsDNA 抗体陽性率 (SLE) | **95%+ (specific)** | ACR criteria |
| Anti-CCP RA 特異度 | **95%+** | Schellekens 1998 |
| HLA-DRB1*04 shared epitope (RA) | OR 3-5 | Gregersen 1987 |
| HLA-DQ2/8 1 型糖尿病 | OR 5-10 | Pugliese 2017 |
| Treg adoptive transfer (T1D NOD マウス) | 発症遅延 50% | Tang 2004 |

---

📄 **論文 (Tier 1 #26)**: 10.5281/zenodo.20256116

> Phase 188 で Vaccines + mRNA + Prime-Boost dynamics へ進みます。

#情報理論的統一理論 #ITU #免疫学 #自己免疫 #寛容 #AIRE #Treg #SLE #RA #K_tolerance #Phase187
