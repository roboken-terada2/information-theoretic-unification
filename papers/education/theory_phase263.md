# Phase 263: 評価 + PISA + 標準化試験 ― K_edu_assessment ★

Phase 262 で K_edu_curriculum の Bloom・教授法を確立。Phase 263 では **評価 (Assessment) + PISA + 標準化試験 + IRT** を扱い、**K_edu_assessment** を ITU の "K-state 測定" として定式化します。

## PISA (Programme for International Student Assessment) ★★

```
OECD 主催, 2000-:
↓ 15 歳の Reading + Math + Science 評価
↓ 3 年毎
↓ 81 国 + 経済圏参加 (2022)
↓
PISA 2022 結果 (Math top 10):
  1.  Singapore (575) ★
  2.  Macau (552)
  3.  Taiwan (547)
  4.  Hong Kong (540)
  5.  Japan (536) ★
  6.  S. Korea (527)
  7.  Estonia (510)
  8.  Switzerland (508)
  9.  Canada (497)
  10. Netherlands (493)
↓
日本 2022:
  Math 5位, Reading 3位, Science 2位 (前回比改善)
  ★ OECD トップクラス維持
↓
US 2022: Math 28位 (低下)
UK: Math 11位, Reading 13位
```

## TIMSS + PIRLS

```
TIMSS (Trends in Math + Science, IEA):
  4 + 8 学年, 4 年毎
  64 国 (2023 TIMSS)
↓
PIRLS (Reading Literacy, IEA):
  4 学年, 5 年毎
  57 国 (2021 PIRLS)
↓
日本 TIMSS 2023:
  G4 Math 4位 (591), Science 6位
  G8 Math 4位 (606), Science 3位
```

## 標準化試験 (Standardized Testing)

### US 大学入試

```
SAT (1926-):
  1600 点 (Reading 800 + Math 800)
  Critical Reading + Math + Writing (2005-2016)
  2024: Digital SAT (短縮版)
↓
ACT (1959-):
  36 点 (English/Math/Reading/Science 各)
  科目別アプローチ
↓
2020-2024 trend:
  Test-optional movement (COVID 加速)
  UC system 廃止 (2025-)
  Harvard 復活 (2025-)
↓
GRE / GMAT:
  大学院・MBA 入試
  GRE: 130-170 (各セクション)
```

### Japan 共通テスト (旧センター試験)

```
1979-1989: 共通一次試験
1990-2020: 大学入試センター試験
2021- 共通テスト (大学入学共通テスト):
↓
6 教科 30 科目
最大 1,000 点満点
↓
2024 受験者: 49.1 万人
2025 改革: 情報I 必須
```

## 評価理論

### Item Response Theory (IRT) ★

```
Rasch 1960, Lord-Novick 1968:
↓ 古典テスト理論 (CTT) を超える
↓
1-parameter (Rasch model):
  P(correct | θ) = 1 / (1 + exp(-(θ - b)))
  θ: 受験者能力
  b: 項目困難度
↓
3-parameter (3PL):
  + a (discrimination), c (guessing)
↓
適応型テスト (CAT):
  GRE 2011-, GMAT, TOEFL iBT
  ★ 効率 50% 向上
```

### Formative vs Summative Assessment

```
Formative (形成的):
  学習中 feedback
  目的: 学習改善
  例: クイズ, 練習問題
↓
Summative (総括的):
  学習後 評価
  目的: 成績判定
  例: 期末試験, PISA
↓
Black-Wiliam (1998):
  Formative の effect size d = 0.4-0.7
  → 教育介入で最高水準
```

### Bias + Validity

```
2024 評価論争:
↓
SAT 人種格差 (Asian > White > Latino > Black):
  ★ Schooling 不平等を反映? Bias?
↓
PISA 国際比較限界:
  Translation, cultural context
  Sampling (e.g., China 4 cities only)
↓
評価の妥当性 4 タイプ (Messick 1995):
  Construct, Content, Criterion, Consequential
```

## Adaptive Testing + AI

```
GRE Powerprep (2011-):
  Multi-stage adaptive
↓
Duolingo English Test (2014-):
  Computer adaptive, 1時間, $59
  300+ 大学受入 (2024)
↓
2024 AI 評価:
  Khan Academy Khanmigo (GPT-4 base)
  Quizlet AI tutoring
↓
2026 予測:
  AI 自動採点 essay 全米普及 (GMAT/GRE essays AI 採点)
```

## 信頼性 + 妥当性 ― 統計

### Reliability (Cronbach α)

```
Cronbach α (1951):
  α = (k/(k-1)) × (1 - Σσ_i² / σ_total²)
↓
標準:
  α > 0.9: Excellent
  0.7-0.9: Good
  < 0.7: Poor
↓
SAT: α ≈ 0.93 (high)
GRE: α ≈ 0.91
日本共通テスト: α ≈ 0.88
```

### Validity

```
Predictive validity:
  SAT - College GPA: r ≈ 0.3-0.5
  + HS GPA: r ≈ 0.5-0.6
↓
2020 SAT 廃止論証拠:
  HS GPA alone とほぼ同等予測力
↓
2024 College Board 反論:
  SAT は HS GPA の grade inflation を補正
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **PISA 開始** | **2000 (OECD)** ✓ |
| **PISA 2022 Math 1位** | **Singapore 575** ✓ |
| **PISA 2022 日本 Math** | **5位 (536)** ✓ |
| **TIMSS 日本 G4 Math** | **4位 (591)** ✓ |
| **SAT 満点** | **1600** ✓ |
| **共通テスト受験者 2024** | **49.1 万人** ✓ |
| **Rasch model** | **1 parameter** ✓ |
| **Black-Wiliam Formative d** | **0.4-0.7** ✓ |
| **SAT Cronbach α** | **≈ 0.93** ✓ |
| **SAT-GPA correlation** | **r ≈ 0.3-0.5** ✓ |
| ITU axiom: 評価 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_edu_assessment

```
K_edu_assessment^(0) = -log P(true_competence | test_score)

IRT model = K-state Bayesian inference:
  P(correct | θ) = logistic function
  ★ θ = K_competence の latent estimate
↓
Adaptive testing = K-state efficient sampling:
  各項目で K_estimate を update
  → 最少項目数で最大精度
↓
Formative assessment = K-state real-time update:
  Black-Wiliam d=0.4-0.7 = K-state gradient maximizing
↓
PISA = global K-state benchmark
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI 自動採点 essay 普及** | 2027 | 0.90 |
| **SAT digital + AI 完全移行** | 2027 | 0.85 |
| Test-optional 移行 (大学 50%+) | 2028 | 0.80 |
| **PISA 2028 日本 Math top 3** | 2028 | 0.65 |
| **IRT + AI 完全適応型** | 2028 | 0.85 |

---

📄 **論文 (Tier 1 #36, Block C 4/6)**: 10.5281/zenodo.20263371

> Phase 264 で高等教育 + 大学 + 研究 へ進みます。

#情報理論的統一理論 #ITU #評価 #PISA #SAT #IRT #Rasch #BlackWiliam #Cronbach #K_edu_assessment #Phase263
