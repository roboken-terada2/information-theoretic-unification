# Phase 262: 教育課程 + Bloom + 教授法 ― K_edu_curriculum ★

Phase 261 で K_edu_developmental の認知発達を確立。Phase 262 では **教育課程 (Curriculum) + Bloom Taxonomy + 教授法 (Pedagogy)** を扱い、**K_edu_curriculum** を ITU の "知識伝達 K-state" として定式化します。

## Bloom Taxonomy (1956, 改訂 2001) ★★★

### オリジナル (Bloom 1956)

```
Benjamin Bloom et al.:
↓ "Taxonomy of Educational Objectives" (1956)
↓ 認知領域 6 階層 (低 → 高):

1. Knowledge (知識)
2. Comprehension (理解)
3. Application (応用)
4. Analysis (分析)
5. Synthesis (総合)
6. Evaluation (評価)
```

### Anderson-Krathwohl 改訂 (2001) ★

```
動詞化 + Synthesis ↔ Evaluation 位置交換:

1. Remember (記憶)
2. Understand (理解)
3. Apply (応用)
4. Analyze (分析)
5. Evaluate (評価)
6. Create (創造) ★ 最上位
↓
知識次元 (Anderson 2001 拡張):
  Factual (事実)
  Conceptual (概念)
  Procedural (手続)
  Metacognitive (メタ認知)
```

### Bloom 適用 (2024 標準)

```
カリキュラム設計:
  Lower-order (記憶+理解): K-12 基礎
  Higher-order (分析+評価+創造): 大学 + 大学院
↓
評価設計:
  Multiple choice: 主に Remember/Understand
  Essay: 主に Analyze/Evaluate
  Project: 主に Create
↓
AI 時代の修正提案:
  Create = AI tool 使用前提に再定義
  Critical evaluation 重要度上昇
```

## 教授法 (Pedagogy)

### Direct Instruction (Engelmann 1960s)

```
段階的, 体系的, scripted:
  I do (modeling) → We do (guided) → You do (independent)
↓
証拠ベース最強 (Hattie 2009 meta-analysis):
  effect size d=0.59
↓
批判:
  Creativity 抑制?
  低 SES 児に最適 (Project Follow Through 1970s)
```

### Inquiry-Based Learning (Schwab 1962, Dewey 1916)

```
学習者が問題発見 + 探究:
  Problem-Based Learning (PBL, McMaster 1969)
  Discovery learning
  Project-Based Learning (PBL, Buck Institute)
↓
医学部・工学部で標準:
  McMaster Medicine PBL 1969
  Harvard New Pathway 1985
↓
効果:
  Long-term retention 高い
  Initial knowledge low → high effort
```

### Flipped Classroom (Bergmann-Sams 2007)

```
家: video lecture
教室: 演習 + 議論 + 個別指導
↓
利点:
  個別ペース対応
  教室時間 = active learning
↓
普及:
  Khan Academy (2008-)
  K-12 + 大学一部標準
```

## カリキュラム理論

### Tyler's Rationale (1949)

```
Ralph Tyler "Basic Principles of Curriculum" (1949):
↓ 4 質問:
  1. 何を達成したいか? (objectives)
  2. どんな経験を提供するか? (experiences)
  3. どう組織するか? (organization)
  4. どう評価するか? (evaluation)
↓
最も影響力ある curriculum framework
```

### Spiral Curriculum (Bruner 1960)

```
Jerome Bruner "The Process of Education" (1960):
↓ "Any subject can be taught effectively in some
   intellectually honest form to any child at any
   stage of development"
↓
螺旋的反復: 同主題を発達段階に応じて深化
↓
Common Core (US 2010-): Spiral 採用
```

### Backward Design (Wiggins-McTighe 1998)

```
Understanding by Design (UbD):
  Stage 1: Identify desired results
  Stage 2: Determine acceptable evidence
  Stage 3: Plan learning experiences
↓
Outcome-first 設計
Essential questions 駆動
```

## 国際カリキュラム比較

### Finland モデル (2000s 注目)

```
Finland (PISA 2000-2009 連続トップ):
↓ Late start (7 歳入学)
↓ Standardized test 少ない
↓ 教師 master degree 必須
↓ Phenomenon-based learning (2016 改革)
↓ 信頼に基づく自治性
```

### Singapore モデル

```
Singapore (PISA 2015 1位):
↓ Teach Less, Learn More (2005)
↓ Heavy investment in teachers
↓ Math: Concrete-Pictorial-Abstract (CPA)
↓ "Singapore Math" 世界輸出
```

### Japan モデル

```
日本:
↓ Lesson Study (授業研究, 1960s-)
↓ 道徳教育 + 学級活動
↓ 平均的高水準, top 10% Finland 比劣る
↓ 2020 学習指導要領 改訂 (アクティブ・ラーニング)
↓ 2024 課題:
  - International rank 緩やかに低下
  - PISA reading 15位 (2022)
  - 教師長時間労働 OECD 最悪
```

### IB (International Baccalaureate)

```
1968 設立 (Geneva):
↓ PYP (Primary Years Programme, 3-12 歳)
↓ MYP (Middle Years, 11-16 歳)
↓ DP (Diploma, 16-19 歳) - 大学受験
↓ CP (Career-related, 16-19 歳)
↓
2024 5,800+ 学校 (世界 160 国)
日本: 200 校超 (2024)
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Bloom 1956** | **6 階層** ✓ |
| **Bloom 改訂 2001** | **Remember → Create** ✓ |
| **Tyler Rationale** | **1949** ✓ |
| **Bruner Spiral** | **1960** ✓ |
| **Hattie Direct Instruction d** | **0.59** ✓ |
| **PBL McMaster** | **1969** ✓ |
| **Flipped (Bergmann-Sams)** | **2007** ✓ |
| **IB 設立** | **1968 Geneva** ✓ |
| **Finland late start** | **7 歳入学** ✓ |
| **Singapore PISA 1位 (2015)** | ✓ |
| ITU axiom: 教育課程 K-state | δS/δ⟨K⟩ ≈ 1 |

## ITU 視点 ― K_edu_curriculum

```
K_edu_curriculum^(0) = -log P(competence | curriculum)

Bloom 6 階層 = K-state ascent:
  Remember (low K) → Create (high K)
↓
Backward Design = K-state goal-driven planning:
  K_target ← K_evidence ← K_experiences
↓
Spiral curriculum = K-state recursive deepening:
  同 K-state 反復 + 解像度向上
↓
Pedagogy 選択 = K-state navigation method:
  Direct = explicit transmission
  Inquiry = self-construction
  Flipped = hybrid attention allocation
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **AI 個別カリキュラム 標準化** | 2028 | 0.85 |
| **Bloom + AI 共生改訂版** | 2027 | 0.85 |
| Project-based 主流化 (G7) | 2030 | 0.65 |
| **PISA Singapore 連続 1位** | 2028 | 0.80 |
| **IB 普及 200+ 国** | 2030 | 0.65 |

---

📄 **論文 (Tier 1 #36, Block C 4/6)**: 10.5281/zenodo.20263371

> Phase 263 で評価 + PISA + 標準化試験 へ進みます。

#情報理論的統一理論 #ITU #教育課程 #Bloom #Tyler #Bruner #Finland #Singapore #IB #K_edu_curriculum #Phase262
