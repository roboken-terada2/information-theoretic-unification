# Phase 204: Sleep + Consciousness Hard Problem ― K_consciousness ★★

Phase 203 で K_executive の意思決定を確立。Phase 204 では **睡眠** + **意識のハード問題** ― Chalmers (1995), Tononi IIT, Dehaene GNWT ― を扱い、**K_consciousness** を ITU の最深 K-state として定式化します。

## 睡眠の構造

### 睡眠ステージ (Aserinsky-Kleitman 1953)

```
NREM Stage 1 (N1):  入眠期, 数分
NREM Stage 2 (N2):  軽い睡眠, K-complex + sleep spindle (50%)
NREM Stage 3 (N3):  深い睡眠 / Slow-wave sleep (SWS), δ波
REM:                Rapid Eye Movement, 夢の主舞台
```

### 90 分周期 (Kleitman BRAC)

```
4-5 cycle / 一晩
N1 → N2 → N3 → N2 → REM (繰返し)
SWS dominant: 前半
REM dominant: 後半
```

### 睡眠の機能 (Walker 2017 "Why We Sleep")

```
SWS:    declarative memory consolidation (Born 2010)
REM:    procedural memory + emotional regulation
Glymphatic system (Iliff 2012): 老廃物クリアランス (Aβ 含む)
↓
AD と睡眠不足の関連 (Mander 2016)
```

## 意識のハード問題 (Chalmers 1995) ★

```
David Chalmers (1995):
"Why does physical processing give rise to subjective experience at all?"
↓
Easy problems: 注意, 報告, 学習, 行動 (機能説明可)
Hard problem:  Qualia - "red の赤さ" の主観的経験

= 物理主義の限界?
```

### 4 主要意識理論

| 理論 | 提唱 | 核心 |
|---|---|---|
| **GWT** (Global Workspace) | Baars 1988 / Dehaene 2014 | Global broadcast = consciousness |
| **IIT** (Integrated Information) | Tononi 2004-2014 | Φ (Phi) = consciousness の量 |
| **HOT** (Higher-Order Thought) | Rosenthal 1990 | meta-representation |
| **Recurrent processing** | Lamme 2006 | 再帰活動 in sensory cortex |

## IIT (Integrated Information Theory) ★

### Tononi の axioms (2014, 2022)

```
1. Intrinsic existence (内在的存在)
2. Composition (複合)
3. Information (情報)
4. Integration (統合)
5. Exclusion (排他)
↓
Φ = 部分の和を超えた統合情報量
↓ Φ 最大化サブシステム = "consciousness"
```

### Φ 計算の問題

```
Computational complexity: O(2^N) for N elements
↓ 14 ニューロンでスパコン困難
↓ proxy 提案: PCI (Casali 2013 perturbational complexity index)
↓ 臨床応用: VS/MCS 患者の意識判定
```

## GWT (Global Workspace, Dehaene-Baars) ★

```
Bernard Baars 1988 + Stanislas Dehaene 2014:
↓ 大脳皮質は集中 "global workspace" を持つ
↓ broadcast されたコンテンツ = "意識的"
↓ 大量 PFC + parietal で表象される

実験証拠:
  - Sub/supra-threshold visual stimulus
  - All-or-none cortical activation (Dehaene 2001)
  - "Ignition" event
```

### 機械意識 (Dehaene 2017)

```
"What is consciousness, and could machines have it?" (Science)
↓ GWT framework で AI 意識評価可能
↓ Phase 47-50 (Tier 1 #2 AI Consciousness) との直接接続
```

## ITU 視点: K_consciousness の構造 ★★

```
K_consciousness^(0) = -log P(unified experience | neural state)
                  = 統合された主観経験の情報的密度

ITU 解釈:
  GWT broadcast = K-state global integration
  Φ (Tononi)     = K-state irreducibility
  HOT            = K_meta^(0) appended

↓
K_consciousness ≈ K_neuro の "global integration phase"
↓ 自由意志 (#9), AI意識 (#2), 記憶 (#26), 知覚 (#28) のすべてを統合
```

### Hard Problem ⇔ ITU axiom

```
Chalmers: なぜ物理から主観経験が生じるか?
↓
ITU 答え (provisional):
   δS = δ⟨K^(0)⟩ が情報処理 (= 物理) を 主観 (= 経験) と同一視
   ⇒ K^(0) = -log ρ = 経験そのもの (Tomita-Takesaki modular)
   ⇒ 物理-情報-経験は ITU の異なる "side"
```

= **Wheeler "It from Bit" (Phase 180) の意識的版** ★

## Anesthesia と意識 喪失

```
Propofol, sevoflurane:
  α7-nicotinic, GABA-A 作動
  ↓ thalamo-cortical decoupling
  ↓ Φ 低下 (Casali 2013, PCI で 0.31 未満)
  ↓ 意識喪失

LOC 持続時間 vs 用量応答 曲線あり (clinical use)
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| 睡眠周期 | **90 分** (Kleitman) ✓ |
| REM 全睡眠比 | **20-25%** ✓ |
| SWS δ 波 | 0.5-4 Hz |
| Glymphatic flow 増加 (sleep) | 60% (Xie 2013) |
| PCI 健常覚醒 | 0.50-0.70 |
| PCI VS 患者 | < 0.31 (Casali 2013) ✓ |
| Φ 14 element 計算 | O(2¹⁴) = 16,384 sub |
| **ITU axiom: sleep transitions** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Φ proxy 全脳測定法確立** | 2030 | 0.65 |
| **意識 BCI (機械意識検出)** | 2032 | 0.55 |
| Anesthesia awareness 検出 100% | 2028 | 0.70 |
| **AI Φ > human で意識的判定** | 2035 | 0.30 |
| AD 早期診断 = sleep architecture 異常 | 2030 | 0.75 |

---

📄 **論文 (Tier 1 #28)**: 10.5281/zenodo.20256729

> Phase 205 で 神経変性疾患 + AD/PD/うつ/統合失調症 へ進みます。

#情報理論的統一理論 #ITU #神経科学 #意識 #ハード問題 #Chalmers #Tononi #Dehaene #Φ #IIT #GWT #K_consciousness #Phase204
