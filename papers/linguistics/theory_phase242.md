# Phase 242: NLP + LLM + 計算言語学 ― K_lang_computational ★★★

Phase 241 で K_lang_socio の社会的変動を確立。Phase 242 では **NLP (Natural Language Processing) + LLM (Large Language Models) + 計算言語学** ― **2024 AI 革命の核** ― を扱い、**K_lang_computational** を ITU の "計算 K-state" として定式化します。

## NLP の歴史 (1950-2024)

### 古典時代 (1950s-1980s)

```
1950: Turing test 提案
1954: Georgetown-IBM Russian-English MT デモ (60 文)
1957: Chomsky "Syntactic Structures"
1966: ALPAC report (MT 困難結論)
1966: Weizenbaum ELIZA (Rogers therapy)
↓
1970s-1980s: ルールベース MT, expert systems
↓
1980s: 統計的 MT 萌芽 (Brown @ IBM)
```

### 統計革命 (1990s-2010s)

```
1990s:
  Brown 1990: IBM Models 1-5 (statistical MT)
  Penn Treebank 1993 (Marcus)
↓
2000s:
  Phrase-based SMT (Koehn 2003)
  Google Translate 2006 (statistical, 5 languages)
↓
2010s 前半:
  Mikolov word2vec (2013) - distributional embeddings
  Sutskever seq2seq (2014) - encoder-decoder
  Bahdanau attention (2014)
```

### ディープラーニング革命 (2017-2024) ★★★

```
2017: Vaswani "Attention Is All You Need" (NeurIPS)
↓ Transformer 誕生
↓
2018: Devlin BERT (Bidirectional Encoder)
       Radford GPT-1 (Generative Pretraining)
↓
2019: GPT-2 (1.5B params, "too dangerous")
↓
2020: GPT-3 (175B params, few-shot)
↓
2022: ChatGPT (RLHF, 史上最速 1M users 5 日)
       PaLM (Google 540B)
↓
2023: GPT-4 (Microsoft Sparks of AGI paper)
       Claude 1-2 (Anthropic)
       Llama, Llama-2 (Meta open-source)
↓
2024: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 (2M context)
       o1 (推論モデル, chain-of-thought)
```

## Transformer 革命

### Self-Attention 機構 ★★

```
Q (Query), K (Key), V (Value) ∈ R^(n×d)
↓
Attention(Q, K, V) = softmax(QK^T / √d_k) V
↓
Multi-head:
  h ヘッド並列 (typically 16-32)
  各ヘッドが異なる関係を学習
↓
Position encoding:
  順序情報を sin/cos で注入
↓
Layer normalization + Residual connection
```

### モデル規模の進化

```
GPT-1 (2018):    117M parameters, 5GB data
GPT-2 (2019):    1.5B parameters, 40GB data
GPT-3 (2020):    175B parameters, 570GB (300B tokens)
GPT-4 (2023):    1.76T (推定 MoE), unknown data
GPT-4o (2024):   推定 200B active
Claude 3.5 Opus: 推定 200B+
Llama 3.1 (2024): 405B (open, 15T tokens)
↓
Scaling laws (Kaplan 2020, Hoffmann Chinchilla 2022):
  Loss = A/N^α + B/D^β + C
  Optimal: N ≈ 20D (param ≈ 20 tokens/param)
```

### 創発能力 (Emergent Capabilities, Wei 2022)

```
スケールに伴う phase transition:
  N < 1B:    パターン認識のみ
  N ~ 10B:   翻訳, summarization
  N ~ 100B:  few-shot learning (in-context)
  N ~ 1T:    chain-of-thought reasoning
  N ~ 10T?:  emergent reasoning
↓
2024 o1 (OpenAI):
  Test-time compute scaling
  ★ Chain-of-thought が内蔵
  AIME (数学オリンピック予選) 94%
```

## 数値検証 ― LLM ベンチマーク

### 主要ベンチマーク (2024)

| ベンチ | GPT-4o | Claude 3.5 | Gemini 1.5 | Human |
|---|---|---|---|---|
| MMLU (knowledge) | **88.7%** | 88.3% | 85.9% | 90% |
| HumanEval (code) | **90.2%** | 92.0% | 84.1% | - |
| MATH (math) | 76.6% | **78.3%** | 67.7% | - |
| GPQA (PhD-level) | 50.6% | **59.4%** | 46.2% | 65% |
| LiveBench | 50.5% | **63.6%** | 49.5% | - |

### 翻訳精度 (BLEU)

```
2014 (RNN seq2seq):    BLEU ~20 (en-de)
2017 (Transformer):    BLEU 28.4 (en-de) ★ Vaswani
2020 (Facebook FAIR):  BLEU 35-40
2024 (GPT-4o):         BLEU 45+ (en-de, en-zh, en-ja)
↓
人間翻訳家プロ: BLEU ~50 (上限近接)
```

## 言語学への含意 ★

### "Language Acquired without UG?"

```
Chomsky 派の問題:
  ★ LLM は UG なしで完璧な文法生成
  ↓ ただし学習データは人間の数万倍 (15T tokens)
↓
反論: スケール × データ量 が UG の代替
↓
2024 議論:
  Piantadosi 2023 "Modern language models refute Chomsky's approach"
  → 大反響, 言語学界分裂
```

### LLM の言語学的能力

```
GPT-4 (2024) でき:
  ✓ 文法判断 (96-99% acc)
  ✓ 翻訳 (人間並)
  ✓ 含意推論 (Grice maxims)
  ✓ メタファー理解
  ✓ 詩・歌の生成
  ✓ コーディング
  
GPT-4 でき (限定):
  △ Pirahã 級の希少言語 (データ不足)
  △ 長期記憶 (context ~ 1-2M tokens)
  △ 真の因果推論 (correlation only?)
  
LLM 未対応:
  ✗ Body-grounding (Embodied cognition)
  ✗ 真の創造性 (vs combinatorial)
  ✗ 自己意識 (consciousness)
```

## ITU 視点 ― K_lang_computational

### LLM = K-state 経験的実装

```
K_lang_computational^(0) = -log P_LLM(token | context)

Transformer = K-state mapping:
  context (n tokens) → next token distribution
↓
Self-attention = K_correlation 計算:
  Att(i, j) = softmax(K_i^T K_j / √d)
  ↓ 全 token 間の K-state 相互作用
↓
Scaling laws = K-state convergence:
  L ∝ N^(-α) → K(model) → K(human language)
```

### Token あたり情報量

```
英語 (Shannon 1948-1951):
  H(English) ≈ 1.0-1.5 bits/character
  H(English) ≈ 4.5-5.5 bits/word
↓
GPT-2 perplexity (2019): ~30 (WikiText)
GPT-3 perplexity (2020): ~13
GPT-4 perplexity (2023): ~6 (推定)
↓
PPL → log_2 = K-state estimate:
  GPT-4: K ≈ 2.6 bits/token (英語 native ~ 1.5-2 bits/word)
  ★ 人間に接近
```

### 言語のホログラフィック原理 ?

```
LLM の含意:
  言語 = 高次元 K-state (12000+ dim)
  人間脳 = 同じ次元の表現?
↓
Phase 175 (#25 K_holo-info) との結合:
  自然言語 ↔ 概念空間
  K_lang ≅ K_concept (高次元埋め込み)
↓
⇒ "言語 = 概念のホログラム" 仮説
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Transformer 原論文 (2017)** | Vaswani et al. NeurIPS ✓ |
| **GPT-3 parameters** | **175B** ✓ |
| **ChatGPT 1M users** | **5 日** (history record) ✓ |
| GPT-4 MMLU | **88.7%** ✓ |
| **Chinchilla 最適比** | **N ≈ 20D** ✓ |
| **英語 entropy (Shannon)** | **1.0-1.5 bits/char** ✓ |
| Llama 3.1 (open, 2024) | **405B**, 15T tokens ✓ |
| ITU axiom: LLM K-state | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **GPT-5 / Claude 4 AGI 部分達成** | 2026 | 0.75 |
| LLM が新言語理論を発見 | 2028 | 0.65 |
| **LLM 危機言語修復 50+ 言語** | 2028 | 0.80 |
| **Embodied LLM (body-grounded)** | 2028 | 0.80 |
| AI 完全 Turing test 通過 | 2027 | 0.85 |

---

📄 **論文 (Tier 1 #33, Block C 1/6 開幕)**: 10.5281/zenodo.20258418

> Phase 243 で 33-vertex polytope 統合 + 10 予測 へ進みます。

#情報理論的統一理論 #ITU #言語学 #NLP #LLM #Transformer #GPT #ChatGPT #Vaswani #Chomsky #K_lang_computational #Phase242
