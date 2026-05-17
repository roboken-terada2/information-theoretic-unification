# Phase 239: 意味論 + 語用論 + 談話 ― K_lang_semantics ★

Phase 238 で K_lang_syntax の Merge を確立。Phase 239 では **意味論 (Semantics) + 語用論 (Pragmatics) + 談話 (Discourse)** を扱い、**K_lang_semantics** + **K_lang_pragmatics** を ITU の "意味 K-state" として定式化します。

## 意味論 (Semantics)

### Frege-Russell-Tarski 伝統 (1879-1933) ★

```
Frege "Über Sinn und Bedeutung" (1892):
  Sinn (意義, sense) vs Bedeutung (意味, reference)
  ↓
  "明けの明星" Sinn ≠ "宵の明星" Sinn
  だが Bedeutung = 金星 (同一)
↓
Russell "On Denoting" (1905):
  記述の理論
  "The present King of France is bald" の論理形式
↓
Tarski (1933):
  真理の意味論的定義
  "snow is white" is true iff snow is white
```

### Montague 文法 (1970) ★

```
Montague "Universal Grammar" (1970):
↓ 形式意味論 + λ計算
↓ 統語 ↔ 意味の同型対応 (Rule-to-Rule)
↓
λ-term:
  walk = λx. walk(x)
  John walks = walk(John) = TRUE if John walks
  Every man walks = ∀x. man(x) → walk(x)
```

### 語彙意味論 (Lexical Semantics)

```
意味場 (Semantic field):
  色彩語 (Berlin-Kay 1969 階層):
    Stage 1: black, white (2 色)
    Stage 2: + red (3 色)
    Stage 3: + green/yellow (4-5 色)
    ...
    Stage 7: + 11 基本色 (English, Russian +blue/light blue)
↓
WordNet (Princeton 1985-):
  英語 117,000+ synsets
  上位-下位関係 (hyponym), 同義 (synonym), 部分 (meronym)
↓
FrameNet (Berkeley 1997-):
  ~1,200 semantic frames
  Commercial_transaction = {Buyer, Seller, Goods, Money}
```

### 認知意味論 (Cognitive Semantics) ★

```
Lakoff "Women, Fire, and Dangerous Things" (1987):
  カテゴリーの prototype 構造
  "鳥" カテゴリー: 雀 > ペンギン > ダチョウ
↓
概念メタファー (Conceptual Metaphor):
  "TIME IS MONEY":
    "spend time", "waste time", "invest time"
  "ARGUMENT IS WAR":
    "attack position", "defend claim", "win argument"
↓
Image schemas:
  CONTAINER, PATH, FORCE, SOURCE-PATH-GOAL
```

## 語用論 (Pragmatics)

### Grice 協調原理 (Cooperative Principle, 1975) ★

```
Grice "Logic and Conversation" (1975):
↓ 会話の協調原理
↓ 4 つの公準 (Maxims):
  Quantity: 必要十分な情報
  Quality:  真実を述べる
  Relation: 関連性を保つ
  Manner:   明瞭・簡潔
↓
含意 (Implicature):
  Q: "John is a good student?"
  A: "He has nice handwriting."
  → 暗黙: John は学業優秀ではない
```

### 発話行為 (Speech Acts, Austin 1962, Searle 1969) ★

```
Austin "How to Do Things with Words" (1962):
↓ Constative (描写) vs Performative (遂行)
↓ "I promise..." 発話 = 約束行為
↓
Searle 5 分類 (1969):
  Assertive:    "It is raining" (主張)
  Directive:    "Open the door" (指示)
  Commissive:   "I'll come" (約束)
  Expressive:   "Thank you" (感謝)
  Declarative:  "I name this ship..." (宣言)
↓
Locutionary (発話) → Illocutionary (発話内行為)
  → Perlocutionary (発話媒介行為)
```

### Relevance Theory (Sperber-Wilson 1986)

```
関連性理論:
  認知効果 / 処理コスト = 関連性
↓
Maximize relevance:
  最大の認知効果 × 最小の処理コスト
↓
含意計算は推論 (Grice 規範) ではなく
認知的にデフォルト
```

## 談話 (Discourse)

### 結束性 (Cohesion, Halliday-Hasan 1976)

```
結束装置:
  指示 (Reference): "he", "it", "this"
  代用 (Substitution): "do so", "one"
  省略 (Ellipsis): "Yes [I will go]"
  接続 (Conjunction): "however", "therefore"
  語彙 (Lexical): 反復, 同義, 上位語
```

### Rhetorical Structure Theory (Mann-Thompson 1988)

```
RST: 談話 = 修辞関係の木構造
↓
~30 関係:
  Elaboration (詳述)
  Contrast (対照)
  Cause (因果)
  Sequence (順序)
  Background (背景)
  ...
↓
Discourse parsing in NLP:
  Penn Discourse Treebank (PDTB 2008-2024)
```

## ITU 視点 ― K_lang_semantics + K_lang_pragmatics

### 意味 = K-state mapping

```
K_lang_semantics^(0) = -log P(meaning | utterance)

語彙意味:
  word embedding ∈ R^d (d ~ 300-12,000)
  例: word2vec, GloVe, BERT, GPT-4
↓
合成意味:
  Frege原理 = 部分の意味 + 統語規則 で全体意味
  λ-calculus が形式的実装
↓
⇒ 意味の合成性 = K-state の加法性
```

### 語用 = 文脈による K-state 補正

```
K_lang_pragmatics^(0) = -log P(intent | utterance, context)

Grice maxims = K-state minimization principles:
  Quantity:  H(message) = optimal
  Quality:   P(true | message) → 1
  Relation:  KL(context || message) → min
  Manner:    L(message) → min (Kolmogorov)
↓
⇒ 語用論 = 文脈条件付き ITU 推論
```

### 意味のベクトル空間 (Distributional Semantics)

```
分布仮説 (Harris 1954, Firth 1957):
  "You shall know a word by the company it keeps"
↓
word2vec (Mikolov 2013):
  king - man + woman ≈ queen
  Paris - France + Japan ≈ Tokyo
↓
BERT/GPT contextual embeddings:
  bank (river) ≠ bank (financial)
  ↓ 文脈依存ベクトル
↓
LLM 2024: 12,000+ 次元埋め込み
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Berlin-Kay 基本色語階層** | **7 stages, 2-11 colors** ✓ |
| **WordNet synsets (英語, 2024)** | **117,000+** ✓ |
| **FrameNet semantic frames** | **~1,200** ✓ |
| Searle 発話行為分類 | **5 types** ✓ |
| **Grice maxims** | **4 quantitative axioms** ✓ |
| word2vec king-man+woman ≈ queen | cosine sim 0.7+ ✓ |
| GPT-4 context length (2024) | 128K+ tokens ✓ |
| ITU axiom: 意味合成 | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **LLM 完全意味理解 (人間並)** | 2028 | 0.70 |
| FrameNet 全言語版完成 (50+) | 2030 | 0.65 |
| **LLM が Grice 含意推論完全達成** | 2027 | 0.85 |
| 意味論 + 神経科学統合理論 | 2032 | 0.55 |
| **新概念メタファー AI 発見** | 2028 | 0.80 |

---

📄 **論文 (Tier 1 #33, Block C 1/6 開幕)**: 10.5281/zenodo.20258418

> Phase 240 で言語獲得 + バイリンガリズム へ進みます。

#情報理論的統一理論 #ITU #言語学 #意味論 #語用論 #Frege #Montague #Grice #Searle #Lakoff #K_lang_semantics #Phase239
