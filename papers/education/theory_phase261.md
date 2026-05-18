# Phase 261: 発達心理学 + Piaget + Vygotsky ― K_edu_developmental ★★

Phase 260 で K_edu の枠組みを確立。Phase 261 では **発達心理学 (Developmental Psychology) + Piaget + Vygotsky + 学習理論** を扱い、**K_edu_developmental** を ITU の "発達 K-state" として定式化します。

## Piaget 認知発達段階 (1923-1980) ★★★

```
Jean Piaget (1896-1980, Switzerland):
↓ 子供の認知発達 4 段階
↓ "Le langage et la pensée chez l'enfant" (1923)
```

### 4 段階

```
Sensorimotor (0-2 歳):
  感覚 + 運動
  Object permanence (8-12 ヶ月) ★

Preoperational (2-7 歳):
  記号 + 言語 + 自己中心性
  Conservation 未獲得
  ★ "I think, therefore concrete operations needed"

Concrete Operational (7-11 歳):
  論理 + Conservation 獲得
  Number/Volume/Mass 保存

Formal Operational (11+ 歳):
  抽象 + 仮説思考
  Counterfactual reasoning
```

### 検証 + 修正 (1980-2024)

```
Piaget 古典版:
  Object permanence 8-12 ヶ月
↓
Baillargeon (1985) 改訂:
  ★ 3.5 ヶ月で existence violation 検出
  → Object permanence は更に早い
↓
Spelke "Core knowledge" (1994):
  乳児に物理・心理 prior 内蔵
```

## Vygotsky ZPD (Zone of Proximal Development) ★★

```
Lev Vygotsky (1896-1934, USSR):
↓ "Thought and Language" (1934, 死後出版)
↓ "Mind in Society" (1978, 英訳)
```

### ZPD 概念

```
独力で can do (実際的発達)
  ↓
ZPD (Zone of Proximal Development) ★
  援助で can do
  ↓
できない (まだ)
```

```
教育の最適点 = ZPD 内
↓
Scaffolding (足場かけ):
  熟達者 (教師・親) が一時的支援
  徐々に支援を減らす
  → 自立的 task 達成
```

### Vygotsky vs Piaget

```
Piaget: 認知発達 ← 個人内構築 (構成主義)
Vygotsky: 認知発達 ← 社会・言語介在 (社会構成主義)
↓
両者の統合:
  Bruner (1960s): Spiral curriculum
  Bandura (1970s): Social learning theory
```

## 学習理論 ― Behaviorism → Cognitivism → Constructivism

### Behaviorism (1900s-1950s)

```
Pavlov (1904 Nobel): 古典的条件付け
Watson (1913): "Psychology as Behaviorist Views It"
Skinner (1938): Operant conditioning
↓
教育応用:
  Programmed instruction (Skinner 1958)
  CAI (Computer-Assisted Instruction, 1960s)
```

### Cognitivism (1950s-1970s)

```
Bruner (1960): "The Process of Education"
Ausubel (1968): "Meaningful learning"
↓
スキーマ理論:
  既存知識構造に新情報を統合
↓
情報処理モデル:
  Encoding → Storage → Retrieval
```

### Constructivism (1970s-現在)

```
Piaget + Vygotsky 基盤:
  知識 = 学習者が構築
  教師 = facilitator
↓
Cognitive Apprenticeship (Collins-Brown 1989)
Situated Learning (Lave-Wenger 1991):
  Communities of practice
  Legitimate peripheral participation
↓
2024 主流: Constructivism + Cognitivism hybrid
```

## メタ認知 (Metacognition) ★

```
Flavell (1979):
  "Knowing about knowing"
↓
2 軸:
  Metacognitive knowledge (自己の認知についての知識)
  Metacognitive regulation (planning + monitoring + evaluation)
↓
教育応用:
  Self-regulated learning (Zimmerman 1990s)
  Metacognitive scaffolds in MOOC + Khan Academy
↓
2024 LLM 時代:
  AI tutor がメタ認知をモデル化
  Anthropic Claude が思考過程を提示
```

## 多元知能 (Multiple Intelligences, Gardner 1983)

```
Howard Gardner "Frames of Mind" (1983):
↓ 7 → 9 知能:
  Linguistic
  Logical-Mathematical
  Spatial
  Bodily-Kinesthetic
  Musical
  Interpersonal
  Intrapersonal
  Naturalistic (1995 追加)
  Existential (2000s 提案)
↓
批判:
  経験的根拠不足 (Visser 2006)
  IQ 因子分析 = g 単一因子
  ★ 2024 学術界 = mixed evidence
```

## Brain-based Learning (2000s-)

```
脳神経科学 + 教育:
↓
Critical periods (Phase 240 言語学参照):
  L1: 0-7 歳
  L2: 3-7 歳 native-like
  Mathematics: 連続的に可塑性高い
↓
Brain-based myths (debunked, Howard-Jones 2014):
  "Left/right brain dominance" — 神話
  "Learning styles" (VAK) — 経験的根拠なし
  "10% brain use" — 神話
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Piaget 4 段階** | **Sensorimotor/Preop/Concrete/Formal** ✓ |
| **Object permanence** | **8-12 ヶ月 (Piaget) / 3.5 ヶ月 (Baillargeon)** ✓ |
| **Vygotsky ZPD** | **Mind in Society 1978** ✓ |
| **Gardner Multiple Intelligences** | **9 (1983 + 拡張)** ✓ |
| **Pavlov Nobel** | **1904** ✓ |
| **Flavell Metacognition** | **1979** ✓ |
| **Lave-Wenger Communities of Practice** | **1991** ✓ |
| **Howard-Jones Neuromyths** | **2014 Nature Rev. Neurosci.** ✓ |
| ITU axiom: 発達 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_edu_developmental

```
K_edu_developmental^(0) = -log P(competence | developmental_stage)

Piaget 4 段階 = K-state phase transitions:
  Sensorimotor → Preop: K_object_permanence emerges
  Preop → Concrete: K_conservation emerges
  Concrete → Formal: K_abstract emerges
↓
Vygotsky ZPD = K-state gradient:
  ∇K_competence × scaffolding = learning rate
↓
Metacognition = K-state self-monitoring:
  ★ K-state on K-state (higher-order)
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI tutor がメタ認知主導** | 2028 | 0.85 |
| **発達障害 (ADHD等) 神経画像診断** | 2030 | 0.75 |
| Critical period 拡張 (薬理介入) | 2032 | 0.55 |
| **ZPD 自動測定 (AI)** | 2027 | 0.85 |
| Learning styles 完全廃止 (教科書) | 2028 | 0.65 |

---

📄 **論文 (Tier 1 #36, Block C 4/6)**: 10.5281/zenodo.20263371

> Phase 262 で教育課程 + Bloom + 教授法 へ進みます。

#情報理論的統一理論 #ITU #発達心理 #Piaget #Vygotsky #ZPD #Gardner #Flavell #メタ認知 #K_edu_developmental #Phase261
