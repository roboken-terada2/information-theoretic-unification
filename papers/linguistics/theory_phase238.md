# Phase 238: 形態論 + 統語論 + Chomsky 生成文法 ― K_lang_syntax ★★

Phase 237 で K_lang_phonology の音韻離散化を確立。Phase 238 では **形態論 (Morphology) + 統語論 (Syntax)** ― **Chomsky 生成文法** の核 ― を扱い、**K_lang_syntax** を ITU の "句構造 K-state" として定式化します。

## 形態論 (Morphology)

### 形態素 (Morpheme) ― 最小有意味単位

```
形態素タイプ:
  自由形態素 (free): "cat", "run", "blue"
  拘束形態素 (bound):
    屈折 (inflection): -s, -ed, -ing
    派生 (derivation): un-, -ness, -tion, -ize
↓
例: unhappiness = un- + happy + -ness (3 morphemes)
   walked = walk + -ed (2 morphemes)
```

### 言語類型 (Morphological typology, Sapir 1921)

```
1. 孤立語 (Isolating, 1 morpheme/word):
   Mandarin: 我 看 书 (wǒ kàn shū) "I read book"
   ↓ morpheme:word ratio ≈ 1.00

2. 膠着語 (Agglutinative):
   Turkish: ev-ler-im-de "in my houses"
       house-PL-1SG.POSS-LOC
   日本語: 食べ-させ-られ-たく-な-い (6 morphemes)
   ↓ morpheme:word ratio ≈ 2-3

3. 屈折語 (Fusional):
   Latin: amō (1.SG.PRES.IND.ACT) "I love"
   ↓ 1 ending = multiple features

4. 抱合語 (Polysynthetic):
   Inuktitut: tusaatsiarunnanngittualuujunga
       "I cannot hear very well" (1 word = 1 sentence)
   ↓ morpheme:word ratio ≈ 10+
```

## 統語論 (Syntax) ― Chomsky 革命

### 句構造規則 (Phrase Structure Rules, Chomsky 1957)

```
S → NP VP
NP → Det N | Det Adj N
VP → V NP | V NP PP
PP → P NP

例: "The cat chased the mouse on the mat"
  S
  ├ NP (The cat)
  └ VP
    ├ V (chased)
    └ NP (the mouse)
    └ PP (on the mat)
```

### X-bar 理論 (Chomsky 1970, Jackendoff 1977)

```
普遍的階層構造:
  XP → Specifier X'
  X' → X' Adjunct
  X' → X Complement

⇒ NP, VP, PP, AP 全て同じ X-bar 構造
⇒ ヘッド (X) + 補部 + 修飾部 + 指定部
⇒ 言語間で順序のみ異なる (head-initial vs head-final)
```

### Principles and Parameters (Chomsky 1981) ★★

```
原理 (Universal):
  - X-bar 階層性
  - 投射原理 (Projection Principle)
  - 移動の局所性 (Subjacency)
  - 束縛原理 (Binding A, B, C)

パラメータ (Language-specific):
  - Head Parameter: head-initial (英) vs head-final (日)
  - Pro-drop Parameter: 主語省略可能か (Italian, Spanish, 日本語)
  - Wh-Parameter: 疑問詞移動 (英) vs 残留 (日本語)

⇒ ~20-30 パラメータで全言語生成
```

### Minimalist Program (Chomsky 1995) ★★★

```
Minimalism:
  唯一の操作 = "Merge"
  Merge (X, Y) → {X, Y}
↓
Merge を再帰的に適用:
  Merge (V, NP) = {V, NP} = VP
  Merge (NP, VP) = {NP, VP} = S
↓
"Faculty of Language Narrow (FLN)":
  = 再帰 (recursion) のみ ★
↓
2002 Hauser-Chomsky-Fitch (Science):
  人間言語のユニーク性 = 再帰
  動物 communication との明確な境界
```

### Universal Grammar の反証論争 ★

```
Pirahã 言語論争 (Everett 2005 Current Anthropology):
  ブラジル先住民 Pirahã 語: 数詞なし, 色彩語なし
  ★ 再帰なし? (Everett の主張)
↓
Chomsky 派反論:
  Pirahã にも埋め込みあり
  または文化的制約による表面構造
↓
2024: 未解決, 言語普遍性論争の核
```

### 依存文法 (Dependency Grammar, Tesnière 1959)

```
依存関係:
  動詞中心
  各語が "支配 (govern)" / "依存 (depend)" 関係を持つ

例: "The cat chased the mouse"
  chased (root)
  ├ cat (subject) [the]
  └ mouse (object) [the]
↓
Universal Dependencies (UD) project (2014-):
  170+ 言語の依存ツリーバンク
  ★ LLM 訓練の標準
```

## 統語論の数値検証

### Greenberg 普遍規則 (1963)

```
Universal 1: SOV, SVO, VSO が支配的 (96%)
Universal 3: VSO 言語は前置詞を持つ
Universal 4: SOV 言語の大多数は後置詞
Universal 18: 形容詞は名詞の前 or 後
↓
WALS 2024 確認:
  Universal 1: ✓ (SOV 41% + SVO 35% + VSO 7% = 83%)
  ↓
  少数派 VSO/VOS/OVS/OSV = 4% のみ
```

### 文の埋め込み深さ (Karlsson 2007)

```
書き言葉:
  英語: 平均 1.4 埋め込み, max 5
  ドイツ語: 平均 1.5, max 5
  ↓
話し言葉:
  平均 1.0-1.2, max 2-3
↓
Miller 1956 magical number 7±2:
  working memory が 5 以上の埋め込みを許さない
```

## ITU 視点 ― K_lang_syntax

### 統語 = 再帰的 K-state 合成

```
K_lang_syntax^(0) = -log P(structure | sentence)

Merge as ITU operation:
  S_merge = S(X) + S(Y) + S_correlation
↓
Recursion creates infinite K-state space:
  N(possible sentences) = ∞ (in principle)
  N(actual sentences ≤ length L) ≈ B^L (B = branching factor)
↓
⇒ 統語 = 有限手段で無限表出 (Humboldt 1836, Chomsky 1965)
```

### Chomsky 階層 (Formal language)

```
Type 0: 無制限 (Turing machine equivalent)
Type 1: 文脈依存 (Linear bounded automaton)
Type 2: 文脈自由 (Pushdown automaton) ← 自然言語のコア
Type 3: 正規 (Finite automaton)
↓
自然言語 ≈ Mildly Context-Sensitive (Joshi 1985):
  英・日のほとんどは Type 2
  スイスドイツ語の交叉依存 = Type 1
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Greenberg SOV+SVO** | **76%** (WALS 2024) ✓ |
| **Pirahã 再帰なし論争** | Everett 2005 ✓ |
| **Universal Dependencies (2024)** | **170+ 言語** ✓ |
| Merge as sole syntactic operation | Chomsky 1995 ✓ |
| **Miller 7±2 埋め込み上限** | ~5-7 levels ✓ |
| 抱合語 morpheme:word | **10+** (Inuktitut) ✓ |
| 孤立語 morpheme:word | **1.0** (Mandarin) ✓ |
| ITU axiom: 統語再帰 | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **LLM 普遍文法 (UG) emergent** | 2027 | 0.75 |
| Pirahã 再帰論争解決 | 2030 | 0.40 |
| **構文解析精度 99%+ (全主要言語)** | 2027 | 0.85 |
| 言語進化シミュレーション統合理論 | 2030 | 0.65 |
| **AI が新文法体系を発見** | 2032 | 0.55 |

---

📄 **論文 (Tier 1 #33, Block C 1/6 開幕)**: 10.5281/zenodo.20258418

> Phase 239 で Semantics + Pragmatics + Discourse へ進みます。

#情報理論的統一理論 #ITU #言語学 #統語論 #Chomsky #Merge #UG #Greenberg #Pirahã #K_lang_syntax #Phase238
