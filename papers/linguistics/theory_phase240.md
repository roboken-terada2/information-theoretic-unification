# Phase 240: 言語獲得 + バイリンガリズム + 臨界期 ― K_lang_acquisition ★

Phase 239 で K_lang_semantics + K_lang_pragmatics の意味/語用を確立。Phase 240 では **言語獲得 (Language Acquisition) + バイリンガリズム + 臨界期** を扱い、**K_lang_acquisition** を ITU の "発達 K-state" として定式化します。

## 母語獲得 (L1 Acquisition)

### 段階 (Brown 1973, Clark 2003)

```
0-3 ヶ月:    cry, cooing
3-6 ヶ月:    babbling (反復音節, ba-ba-ba)
6-12 ヶ月:   ★ Werker-Tees 臨界期 - 母語音素鋭敏化
12 ヶ月:    最初の単語 (mama, dada)
12-18 ヶ月:  one-word stage (50 語平均)
18-24 ヶ月:  two-word stage (telegraphic speech)
2-3 歳:    語彙急増 ("vocabulary explosion") 1 日 9 語
            文法構造 (S-V-O)
3-5 歳:    複文, 過剰一般化 ("goed", "foots")
5-7 歳:    成人並文法 (大部分)
↓
3 歳児語彙: ~1,000 語
5 歳児語彙: ~5,000 語
成人語彙:   ~50,000-100,000 語
```

### 臨界期仮説 (Lenneberg 1967) ★★

```
Lenneberg "Biological Foundations of Language" (1967):
↓ 言語獲得は biological maturation に依存
↓ 0-13 歳が臨界期
↓ それ以降は完全な母語獲得困難
↓
証拠:
  Genie case (1970): 13 歳まで隔離
    → 単語獲得は可能だが文法獲得困難
  Victor of Aveyron (1799):
    野生児, 言語獲得失敗
↓
脳可塑性:
  シナプス密度 0-2 歳 peak
  2-10 歳 pruning
  ★ 10 歳以降 母語獲得困難
```

### 普遍文法 vs 経験主義論争

```
Chomsky 派 (Nativism):
  UG = 生得的
  "Poverty of Stimulus" 議論
  入力データ < 出力知識
↓
Tomasello 派 (Usage-based):
  汎用学習機構で十分
  社会的・認知的能力
  Construction Grammar
↓
2024 LLM の含意:
  GPT-4 は UG なしで文法獲得 → 経験主義側に有利
  但しデータ量が数万倍人間 → 単純比較不可
```

## バイリンガリズム (Bilingualism)

### 世界のバイリンガル人口

```
世界バイリンガル率 ≈ 60%+ (2024)
  ↓ モノリンガル国: 米国 (78% 英のみ), 日本 (98%)
  ↓ バイリンガル国: ベルギー, スイス, 印度
  ↓ 多言語国: パプアニューギニア (840 言語)
```

### バイリンガル獲得タイプ

```
Simultaneous bilingualism (同時):
  両親が異なる言語 (e.g., one-parent-one-language)
  0 歳から 2 言語並行
↓
Sequential bilingualism (継時):
  L1 確立後に L2 学習
  ★ L2 fluency は獲得開始年齢に依存
↓
2nd language critical period (Johnson-Newport 1989):
  3-7 歳開始: native-like
  8-15 歳: 良好だが non-native traces
  17+ 歳: significant accent/grammar gaps
```

### バイリンガル脳の利点 (Bialystok 2008-2024)

```
Executive function ベネフィット:
  ★ Stroop test improved (35-50ms faster)
  attentional control
  task switching
↓
認知症発症遅延:
  Bialystok 2007: 4 年遅延 (450 患者)
  ↓ "Cognitive reserve" 仮説
  Mendis 2020 meta-analysis: 4.7 年遅延
↓
Code-switching:
  脳内 2 言語同時活性化
  抑制機構が executive function 強化
```

## 第二言語獲得 (SLA, Second Language Acquisition)

### 主要モデル

```
Krashen Input Hypothesis (1985):
  i+1 input が必要
  Comprehensible input が unique 駆動
↓
Swain Output Hypothesis (1985):
  Comprehensible output も必要
↓
Long Interaction Hypothesis (1996):
  Negotiation of meaning が獲得促進
↓
DeKeyser Skill Acquisition (2007):
  Declarative → Procedural knowledge
  Power law of practice
```

### Common European Framework (CEFR 2001)

```
A1: Beginner
A2: Elementary
B1: Intermediate
B2: Upper Intermediate
C1: Advanced
C2: Mastery
↓
Native-like = C2+ (typically ~10,000 hrs immersion)
```

## 言語と思考 (Sapir-Whorf 仮説)

### 強い仮説 vs 弱い仮説

```
Strong Whorf (linguistic determinism):
  言語 → 思考を決定
  ★ 反証多数, 現代では支持されず

Weak Whorf (linguistic relativity):
  言語 ↔ 思考を影響
  ★ 部分的に支持
↓
証拠:
  色彩語 (Berlin-Kay) - 弱い影響
  空間語 (Levinson 2003) - "north of tree" Tzeltal
  数詞 (Pirahã 1, 2, many) - 計算能力影響
  時制 (Boroditsky 2001) - 時間概念影響
```

## ITU 視点 ― K_lang_acquisition

### 言語獲得 = K-state 発達

```
K_lang_acquisition^(0)(t) = -log P(grammar(t))

t = 0 (新生児): K^(0) = log(All possible languages)
t = 6 mo:      K^(0) drop 50% (音韻 narrowing)
t = 12 mo:    K^(0) drop 80% (母語音素確定)
t = 2 yr:     K^(0) drop 95% (文法 emergence)
t = 7 yr:     K^(0) → mature K_native
↓
⇒ 発達 = entropy reduction
⇒ 母語獲得 = K-state crystallization
⇒ 臨界期 = K-state plasticity window
```

### バイリンガル K-state

```
K_bilingual = K_L1 ⊕ K_L2 + K_interface

simultaneous: K_L1 ≈ K_L2 (両方 native)
sequential:   K_L1 native, K_L2 partial
↓
脳内2言語活性化 → executive K-state 強化
⇒ Bialystok 効果 = K-state efficiency
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **臨界期 (Lenneberg 1967)** | **0-13 歳** ✓ |
| **Werker-Tees 音韻 narrowing** | **6-12 ヶ月** ✓ |
| 2 歳語彙急増 | **~9 語/日** ✓ |
| 成人語彙 | **50,000-100,000 語** ✓ |
| **世界バイリンガル率** | **60%+** ✓ |
| Bialystok 認知症遅延 | **4.7 年** (Mendis 2020) ✓ |
| **Johnson-Newport L2 critical age** | **~7 歳** ✓ |
| CEFR レベル | **A1-C2 (6 levels)** ✓ |
| ITU axiom: 言語獲得 | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI による L2 指導 (CEFR C2 達成 50% 加速)** | 2028 | 0.85 |
| **臨界期の神経機構 fMRI で完全特定** | 2030 | 0.65 |
| バイリンガル認知症遅延 大規模確認 | 2028 | 0.80 |
| Sapir-Whorf 仮説 LLM で検証 | 2027 | 0.75 |
| **AI で先天言語障害 (SLI) 治療法** | 2032 | 0.55 |

---

📄 **論文 (Tier 1 #33, Block C 1/6 開幕)**: 10.5281/zenodo.20258418

> Phase 241 で Sociolinguistics + 言語変化 + 危機言語 へ進みます。

#情報理論的統一理論 #ITU #言語学 #言語獲得 #臨界期 #Lenneberg #Werker #Bialystok #バイリンガル #SapirWhorf #K_lang_acquisition #Phase240
