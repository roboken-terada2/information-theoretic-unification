# Phase 254: 刑法 + 刑事手続 + 国際刑法 ― K_law_criminal ★

Phase 253 で K_law_constitutional の憲法・違憲審査を確立。Phase 254 では **刑法 (Criminal Law) + 刑事手続 (Criminal Procedure) + 国際刑法** を扱い、**K_law_criminal + K_law_procedural** を ITU の "規範違反 K-state" として定式化します。

## 刑法の基本原理

### 罪刑法定主義 (Nulla poena sine lege)

```
"罪なくして罰なし、法なくして罪なし"
↓
Roman law 起源
Cesare Beccaria "Dei delitti e delle pene" (1764):
  ★ 近代刑法理論の創始
  ★ 拷問廃止, 死刑反対, 比例原則
↓
影響:
  Napoleon Code Penal (1810)
  Bavarian Code (Feuerbach 1813)
  日本刑法 (1907)
```

### 主要刑法概念

```
構成要件 (Tatbestand):
  Actus reus + Mens rea (英米法)
  客観要件 + 主観要件 (大陸法)
↓
違法性阻却:
  正当防衛, 緊急避難, 自救行為, 同意
↓
責任阻却:
  心神喪失, 14 歳未満, 期待可能性なし
↓
処罰目的:
  - 報復 (retribution)
  - 抑止 (deterrence) ★ Beccaria
  - 改善 (rehabilitation)
  - 隔離 (incapacitation)
```

## 刑事手続 ― Due Process

### Adversarial vs Inquisitorial

```
Adversarial (英米法系):
  US, UK, Australia, Canada
  ↓ 検察 vs 弁護 (jury trial)
  ↓ Judge = 中立な審判
↓
Inquisitorial (大陸法系):
  France, Germany, Japan (混合)
  ↓ Judge actively investigates
  ↓ Juge d'instruction (France)
↓
Hybrid:
  Italy (1989 改正), Japan (2009 裁判員)
```

### Miranda Rights (1966) ★

```
Miranda v. Arizona (1966):
  "You have the right to remain silent..."
↓
4 警告:
  1. Right to remain silent
  2. Statements may be used against
  3. Right to attorney
  4. Right to appointed attorney
↓
全米標準, 多くの国が準用 (日本は限定的)
```

### Habeas Corpus (古代起源 - 1679)

```
Habeas Corpus Act (1679, England):
  違法拘禁からの保護
↓
US Constitution Art. I, Sec. 9:
  停止禁止 (戦時・反乱除く)
↓
2006 Hamdan v. Rumsfeld:
  Guantanamo 拘留者にも habeas corpus 適用
```

## 死刑制度 (Death Penalty)

### 世界の現状 (2024)

```
完全廃止: 112 国 (Amnesty 2023)
事実上廃止: 32 国
通常犯罪のみ廃止: 9 国
存続: 53 国
↓
2023 死刑執行国:
  China (推定 1,000+, 公式非公表)
  Iran (853 確認, Amnesty 2023)
  Saudi Arabia (170)
  Somalia (38)
  US (24)
↓
日本: 存続 (2023 執行 0, 2024 1)
  支持率 80%+ (世論)
```

### EU + 米国対立

```
EU: 1998 死刑廃止条約 (議定書 6, 13)
  → EU 加盟条件
↓
US: 27 州存続 (23 州廃止 or モラトリアム)
  2007 NJ廃止, 2019 NH廃止
  Texas (1976-2024 で 587 名執行, 最多)
↓
死刑反対論証拠:
  Death Penalty Information Center (2024):
  185 名 exonerated (DNA 等で無罪判明)
  ★ ~ 4% of death row 無罪疑い
```

## 国際刑法 ― ICC (International Criminal Court)

### ICC 設立 (1998 Rome Statute)

```
1998 Rome Statute:
  124 国批准 (2024)
  ★ USA, China, Russia, India 非批准
↓
管轄 4 罪:
  1. Genocide (集団殺害)
  2. Crimes against humanity (人道に対する罪)
  3. War crimes (戦争犯罪)
  4. Crime of aggression (侵略罪, 2017 発効)
↓
拠点: The Hague
最初の判決: Lubanga (2012, DRC 子兵)
```

### 主要 ICC 判決

```
Thomas Lubanga Dyilo (DRC, 2012): 14 年
Jean-Pierre Bemba (CAR, 2016 → 2018 無罪)
Bosco Ntaganda (DRC, 2019): 30 年
Ahmad al-Mahdi (Mali, 2016): 文化財破壊 9 年
↓
逮捕状発令 (2023-2024):
  2023.3 Vladimir Putin (ウクライナ子供拉致)
  2024.5 Israeli PM Netanyahu + Gallant (Gaza)
  2024.5 Hamas leaders Sinwar + Deif + Haniyeh
```

### ICJ (国際司法裁判所) との違い

```
ICJ (1945, The Hague):
  国家間紛争のみ
  UN 機関
↓
ICC (1998, The Hague):
  個人の刑事責任
  独立機関 (Rome Statute)
```

## Beccaria 抑止 ― 数学化された刑罰理論

```
Beccaria "On Crimes and Punishments" (1764):
↓
Deterrence (抑止) 3 条件:
  1. Certainty (確実性) ★ 最重要
  2. Celerity (迅速性)
  3. Severity (厳しさ)
↓
"100 人捕まる軽罰" > "1 人捕まる重罰"
↓
現代 econometric 検証:
  Becker 1968 → certainty effect 確認
  severity 限定的効果
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Beccaria** | **1764 Dei delitti e delle pene** ✓ |
| **Miranda v. Arizona** | **1966** ✓ |
| **Habeas Corpus Act** | **1679** ✓ |
| **死刑完全廃止国** | **112** (Amnesty 2023) ✓ |
| **ICC Rome Statute** | **1998, 124 批准** ✓ |
| ICC 最初判決 (Lubanga) | **2012, 14 年** ✓ |
| Putin 逮捕状 | **2023.3** ✓ |
| Netanyahu 逮捕状 | **2024.5** ✓ |
| Beccaria 3 条件 (certainty 最重) | Becker 1968 確認 ✓ |
| ITU axiom: 刑罰 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_law_criminal

```
K_law_criminal^(0) = -log P(behavior compliant | sanction)

抑止理論 = K-state 期待値修正:
  Expected_penalty = Certainty × Severity / Discount_rate
↓
Beccaria 最重要 = Certainty:
  ↓ K-state expectation の更新確実性
↓
ICC = 国際 K-state norm enforcement
  → 国家間 K-state non-uniform → uniform
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI 量刑支援 (主要国 50%)** | 2028 | 0.80 |
| **ICC 主要権力者 (Putin等) 法廷立つ** | 2032 | 0.30 |
| **DNA 冤罪 1,000+ 米国 exonerated** | 2030 | 0.85 |
| **日本死刑廃止** | 2040 | 0.30 |
| **AI 顔認証 + 犯罪予測規制法** | 2027 | 0.85 |

---

📄 **論文 (Tier 1 #35, Block C 3/6)**: 10.5281/zenodo.20263201

> Phase 255 で民法 + 契約 + 不法行為 へ進みます。

#情報理論的統一理論 #ITU #刑法 #Beccaria #Miranda #死刑 #ICC #Putin逮捕状 #Netanyahu逮捕状 #K_law_criminal #Phase254
