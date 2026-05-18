# Phase 255: 民法 + 契約 + 不法行為 + 物権 ― K_law_civil ★

Phase 254 で K_law_criminal の刑罰・抑止を確立。Phase 255 では **民法 (Civil Law) + 契約法 + 不法行為法 + 物権法** を扱い、**K_law_civil** を ITU の "私的合意 K-state" として定式化します。

## 民法体系の系譜

### Roman 法 (BC 450 - AD 533) ★★

```
BC 450 12 表法:
  最古 Roman 成文法
↓
Gaius "Institutiones" (AD 161):
  Persons, Things, Actions の三分
↓
AD 533 Justinian Corpus Iuris Civilis:
  - Institutiones (教科書)
  - Pandectae/Digesta (法学者著作集 50 巻)
  - Codex (皇帝勅令集)
  - Novellae (新法)
↓
中世大学 (Bologna 1088): 復活研究
近世自然法学派 (Grotius, Pufendorf)
```

### Napoleon Code Civil (1804) ★★★

```
1804 Code civil des Français:
  Napoleon 個人主導, 4 起草者
  ↓ 2,281 条
  ↓ "Personnes, biens, modes d'acquisition"
↓
特徴:
  - 自由意志 + 所有権神聖
  - 個人主義
  - 平易な仏語 (法学者言語ではなく)
↓
影響:
  Belgium, Spain, Italy, Latin America (Code Napoleon)
  Quebec, Louisiana, 日本 (1898)
  → 30+ 国家
```

### 日本民法 (1898) + ドイツ BGB (1900)

```
1898 日本民法 (Boissonade + 梅謙次郎):
  仏 + 独折衷
  1,044 条 → 1,050 条 (2024 改正後)
↓
1896 ドイツ Bürgerliches Gesetzbuch (BGB):
  施行 1900.1.1
  2,385 条
  最も体系的成文法
↓
両者: 現代 Civil law の双璧
```

## 契約法 (Contract Law)

### 契約の要件 (4 原則)

```
1. 申込 + 承諾 (Offer + Acceptance)
2. 約因 (Consideration, 英米法のみ)
3. 当事者能力 (Capacity)
4. 適法性 (Legality)
↓
無効事由:
  錯誤 (Mistake), 詐欺 (Fraud), 強迫 (Duress)
  通謀虚偽表示, 公序良俗違反
```

### Pacta sunt servanda (合意は守られねばならぬ)

```
Roman 法 → Vienna 条約法 (1969) Art. 26:
  "Every treaty in force is binding and must
   be performed in good faith"
↓
契約自由 vs 修正:
  消費者保護, 労働法, 反トラスト
  Force majeure (不可抗力) ← COVID 2020 大量訴訟
```

### CISG (1980 ウィーン売買条約)

```
United Nations Convention on Contracts for the
International Sale of Goods (CISG, 1980):
  ★ 国際商取引の統一私法
  ★ 96 国批准 (2024)
↓
主要規定:
  申込 + 承諾 mirror rule
  品質適合義務
  Fundamental breach 解除権
```

## 不法行為法 (Tort Law)

### 要件 (4 elements)

```
Duty of care: 注意義務
Breach: 義務違反
Causation: 因果関係 (cause-in-fact + proximate)
Damages: 損害
↓
過失責任 vs 厳格責任 vs 無過失責任
```

### 著名訴訟

```
Donoghue v. Stevenson (1932, UK):
  "Neighbour principle" - duty of care 拡大
  ★ ginger beer + snail 事件
↓
Liebeck v. McDonald's (1994, US):
  Hot coffee burns
  ★ $2.9M (削減後 $640K) - punitive damages 論争
↓
Roundup (glyphosate) litigation (2018-):
  Bayer/Monsanto $11B+ settlement
  ★ 多発的 product liability
```

### 製造物責任 (Product Liability)

```
US: 1965 Restatement (Second) §402A:
  Strict liability (defective product)
↓
EU: 1985 Product Liability Directive:
  Producer's strict liability
↓
Japan: 製造物責任法 (PL 法, 1995)
↓
AI 時代の課題:
  Tesla Autopilot 事故 - 製造者責任?
  Driver-AI joint liability emerging
```

## 物権法 (Property Law)

### 所有権の 5 つの権能

```
Use (使用)
Enjoyment (収益)
Disposal (処分)
Possession (占有)
Inheritance (相続)
↓
"Bundle of rights" (Hohfeld 1913, US)
```

### 知的財産権 (詳しくは Phase 258)

```
Patent (特許): 20 年
Copyright (著作権): 著者生涯 + 70 年 (Berne 1886)
Trademark (商標): 無期限 (10 年更新)
Trade Secret (営業秘密): 無期限 (秘密保持必要)
```

### Coase 定理 (1960) ★

```
Coase "Problem of Social Cost" (1960):
  取引コスト 0 + 初期権利配分 → 最終効率配分は同じ
↓ Nobel Economics 1991
↓
Application:
  公害 + 産業 → 排出権取引 (Cap & Trade)
  電波周波数 → オークション (1994 US FCC, $7B)
  土地利用 zoning
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Napoleon Code Civil** | **1804, 2,281 条** ✓ |
| **日本民法** | **1898, ~ 1,050 条** ✓ |
| **ドイツ BGB** | **1900, 2,385 条** ✓ |
| **Roman 12 表法** | **BC 450** ✓ |
| **Justinian Corpus Iuris** | **AD 533** ✓ |
| **CISG** | **1980, 96 国** ✓ |
| **Donoghue v. Stevenson** | **1932 UK** ✓ |
| **Roundup settlement** | **$11B+ (Bayer)** ✓ |
| **Berne Convention** | **1886, 生涯 + 70 年** ✓ |
| **Coase 定理 + Nobel** | **1960 / 1991** ✓ |
| ITU axiom: 民法 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_law_civil

```
K_law_civil^(0) = -log P(transaction | private_norm)

契約 = 当事者間 K-state coupling:
  Pacta sunt servanda = K-state stability
  Breach = K-state perturbation
↓
不法行為 = K-state externality (Coase):
  Tort liability = K-state cost internalization
↓
Coase 定理 = K-state efficient allocation:
  取引コスト 0 → K-state attractor 一意
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI 契約自動審査 (50% 標準)** | 2028 | 0.85 |
| **Smart contract 国際法的承認** | 2027 | 0.80 |
| **Coase 定理 +AI 適用拡大** | 2027 | 0.80 |
| Roundup 系訴訟 $20B+ | 2027 | 0.80 |
| AI 製造物責任 EU 整備 | 2026 | 0.85 |

---

📄 **論文 (Tier 1 #35, Block C 3/6)**: 10.5281/zenodo.20263201

> Phase 256 で国際法 + UN + ICC へ進みます。

#情報理論的統一理論 #ITU #民法 #契約 #不法行為 #Napoleon #Roman #Donoghue #Coase #Roundup #K_law_civil #Phase255
