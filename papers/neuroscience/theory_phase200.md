# Phase 200: LTP / LTD / Hebb 学習 / Memory ― K_synapse 深掘り ★★★ (200 大台)

Phase 199 で K_neuro 全体像と Hodgkin-Huxley を確立。Phase 200 ★ では **シナプス可塑性** ― 学習と記憶の分子基盤 ― を扱い、**K_synapse** を ITU の "情報蓄積 K-state" として定式化します。

## 🎉 Phase 200 大台到達 ★★★

Pass-1 220 phase のうち **200 phase 突破 = 90.9%** ★

## Hebb の学習則 (1949)

```
Donald Hebb "The Organization of Behavior" (1949):
"When an axon of cell A is near enough to excite cell B and repeatedly
or persistently takes part in firing it, some growth process or
metabolic change takes place in one or both cells such that A's
efficiency, as one of the cells firing B, is increased."

要約: "Neurons that fire together, wire together" (Carla Shatz)
```

### Hebb 学習則の数式化

```
Δw_ij = η · x_i · y_j        (基本 Hebb 則)

η: 学習率
x_i: pre-synaptic activity
y_j: post-synaptic activity

問題: w は単調増加 → 制限なし → 学習困難
修正: BCM, Oja, STDP などで時間/平均化要素を導入
```

## LTP (Long-Term Potentiation) 発見

### Bliss-Lømo (1973) ★

```
ウサギ海馬 perforant path → dentate gyrus
高頻度刺激 (100 Hz, 1 sec) 後:
   ↓ EPSP 振幅 2-3× 増大
   ↓ 数時間-数日持続
↓ "シナプス強度の長期増強" = LTP
↓ 学習と記憶の分子基盤候補
```

### NMDA 受容体仮説 (Collingridge 1983)

```
LTP は AP5 (NMDA antagonist) で阻害
↓ NMDA = "coincidence detector"
   Glu 結合 + Mg²⁺ block 解除 (depolarization)
   ⇒ Ca²⁺ 流入 → 細胞内シグナル → AMPA 受容体 増加
   ⇒ "more channels per synapse" = LTP
```

### LTD (Long-Term Depression)

```
低頻度刺激 (1 Hz, 15 min):
   ↓ シナプス強度減弱
   ↓ Ca²⁺ 低濃度 → phosphatase 活性化 → AMPA endocytosis
   ↓ 記憶の "消去" / "更新" メカニズム
```

## STDP (Spike-Timing-Dependent Plasticity, Markram 1997)

```
Pre が Post の前 (10-20 ms 以内): LTP (+30%)
Pre が Post の後 (10-20 ms 以内): LTD (-30%)
↓
"Causal Hebb" = 時間因果関係のみ強化
↓ 自然な時系列学習
```

### STDP 関数

```
Δw(Δt) = A+ · exp(-Δt/τ+)   if Δt > 0  (LTP)
       = -A- · exp(+Δt/τ-)  if Δt < 0  (LTD)

τ+ ~ 20 ms, τ- ~ 20 ms
A+ ~ A- ~ 0.05-0.10
```

## 記憶の分類

| タイプ | 持続 | 神経基盤 |
|---|---|---|
| **感覚記憶** | <1 秒 | 知覚野 |
| **短期記憶 / Working** | 秒-分 | Prefrontal cortex (Goldman-Rakic 1980s) |
| **長期記憶 (declarative)** | 永続 | 海馬 + 大脳皮質 |
| **手続き記憶** | 永続 | 小脳 + 基底核 |

### Declarative memory subtypes

```
Episodic    (個人的経験): "First kiss"
Semantic    (一般的知識): "Paris is the capital of France"
```

### Patient H.M. (Henry Molaison, 1953-2008) ★

```
1953: 重度てんかんで両側海馬切除
↓ 知能 + 短期記憶 = 保たれた
↓ 新しい declarative memory 形成 = 完全消失 (anterograde amnesia)
↓ 手続き記憶 (mirror drawing 学習) = 保たれた
↓ 「記憶と他の認知機能の分離」を証明 (Scoville-Milner 1957)
↓ 神経心理学最重要患者 (病歴 H.M. として 50 年研究)
```

## Engram (記憶痕跡) の発見

### Tonegawa Lab (2012-2014) ★

```
Liu et al. (2012 Nature):
↓ 光遺伝学で海馬 c-Fos 陽性ニューロン群を ChR2 発現
↓ 恐怖条件付け → 再活性化で恐怖反応再現
↓ "engram = 特定ニューロン集合の痕跡" 直接証明

Ramirez et al. (2013 Science):
↓ False memory implantation (false context fear)
```

= **記憶 = 物理的ニューロン回路パターン** ★

## ITU 視点: K_synapse + K_memory

```
K_synapse^(0) = -log p(w_ij | (pre, post) activity history)
              = シナプス強度分布の情報的状態

学習 = δw_ij が ITU axiom に従う:
   δS(synaptic distribution) = δ⟨K_synapse^(0)⟩
↓
   Hebb 則 / STDP / BCM = ITU descent flow 実装

K_memory^(0) = engram clone の identity 演算子
            = 特定 neural assembly の signature
```

## 学習アルゴリズムとの対応

| 神経実装 | 機械学習 |
|---|---|
| Hebb 則 | Hebbian learning, PCA |
| LTP/LTD | Gradient descent + back-prop (approximate) |
| STDP | Predictive coding |
| Dopamine RPE | TD-learning, Q-learning |
| Replay (海馬) | Experience replay (DQN) |

= **ITU 視点: 生物 + 人工学習 = 共通 ITU descent flow** ★

## Phase 200 数値検証目標

| 量 | 期待値 |
|---|---|
| LTP induction 周波数 | **100 Hz, 1 sec** (Bliss-Lømo 1973) ✓ |
| LTP 強度増大倍率 | **2-3×** ✓ |
| LTD induction 周波数 | 1 Hz, 15 min ✓ |
| STDP 時間窓 | ±20 ms ✓ |
| NMDA Mg²⁺ block 電位 | -65 mV → -40 mV で解除 ✓ |
| AMPA 単位電流 | 2-5 pA |
| 単一海馬ニューロン engram 数 | 数百 (sparse coding) |
| H.M. 海馬切除年 | 1953 ✓ |
| **ITU axiom: LTP induction** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Engram-based memory editing** 臨床応用 (PTSD) | 2032 | 0.55 |
| Single-cell engram identification 全脳 (mouse) | 2028 | 0.75 |
| Memory transfer (RNA-mediated, hypothesis) | 2035 | 0.20 |
| **Optogenetics 人類臨床応用** (RPE65 以外) | 2030 | 0.60 |
| Closed-loop neural prosthesis for memory (AD) | 2032 | 0.55 |

---

📄 **論文 (Tier 1 #28)**: 10.5281/zenodo.20256729

> Phase 201 で Visual Cortex + Hubel-Wiesel + Perception へ進みます。

#情報理論的統一理論 #ITU #神経科学 #LTP #LTD #Hebb #Engram #Tonegawa #H_M #K_synapse #Phase200
