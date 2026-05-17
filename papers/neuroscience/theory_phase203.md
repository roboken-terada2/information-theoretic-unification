# Phase 203: Prefrontal Cortex + Executive Function + Decision ― K_executive ★

Phase 202 で K_memory 海馬の時空間記憶を確立。Phase 203 では **前頭前野 (PFC)** ― 実行機能 / 意思決定 / ワーキングメモリ ― を扱い、**K_executive** を ITU の "上位制御 K-state" として定式化します。

## 前頭前野 (Prefrontal Cortex) の構造

```
PFC = 前頭葉の最前部 (中心溝より前)
↓ ヒト大脳皮質の ~30% (霊長類で最大進化)
↓ 主要部分:
   DLPFC (背外側): ワーキングメモリ, 計画
   VMPFC (腹内側): 価値評価, 感情調節
   OFC (眼窩前頭): 報酬予測, 社会認知
   ACC (前帯状回): 衝突モニタ, 注意
```

### 進化: ヒト PFC の特異性

| 種 | PFC 比率 | グリア-ニューロン比 |
|---|---|---|
| マウス | 5% | 0.3 |
| ネコ | 10% | 0.5 |
| マカク | 17% | 0.8 |
| **ヒト** | **29-30%** | **1.5** ★ |

= **ヒト = "前頭前野過剰発達" の霊長類** ★

## Working Memory: Goldman-Rakic (1980s) ★

```
Patricia Goldman-Rakic (Yale, 故人):
↓ マカク DLPFC 単一ニューロン記録
↓ "Delay period activity": 刺激消失後も発火継続
↓ → 内部表象の保持 = ワーキングメモリ
↓ Information retained even after cue offset
```

### Baddeley working memory model (1974)

```
Central Executive
├── Phonological Loop (音韻ループ)
├── Visuospatial Sketchpad (視空間スケッチパッド)
└── Episodic Buffer (Baddeley 2000 追加)
```

### Miller's 7±2 (1956) → 4±1 (Cowan 2001)

```
Miller 1956: "The magical number seven, plus or minus two"
↓ 短期記憶容量 = 7 chunks
↓ Cowan 2001 revision: 4 chunks ± 1 (chunking 除く)
↓ ヒト working memory の universal 限界
```

## 価値ベース意思決定

### Expected utility (von Neumann-Morgenstern 1944)

```
Utility maximizes: choose argmax_a E[U(R)]
↓
神経実装: VMPFC + OFC で価値表象
```

### Prospect theory (Kahneman-Tversky 1979, Nobel 2002) ★

```
損失回避 (loss aversion): λ ≈ 2.25
   損失の痛み = 利得の喜び × 2.25 ★

確率の歪み (probability weighting):
   小確率の過大評価 (10⁻⁴ の宝くじ過大評価)
   大確率の過小評価
↓
"Behavioral economics" の中核
```

### Reinforcement learning + Dopamine RPE (Schultz 1997)

```
Wolfram Schultz (Cambridge):
↓ マカク VTA dopamine ニューロン記録
↓ "Reward prediction error" (RPE) を符号化
↓ δ = R - V(s)  (Temporal Difference error)
↓ Sutton-Barto RL algorithm と神経実装の一致 ★

応用:
  - addiction (薬物乱用 = RPE hijack)
  - パーキンソン病 (DA 減 → 学習困難)
  - 統合失調症 (DA hypothesis)
```

## Iowa Gambling Task: Damasio (1994) ★

```
Bechara-Damasio (1994):
↓ VMPFC 損傷患者で risky choice 多用
↓ "Somatic marker hypothesis":
   感情シグナルが意思決定を導く
↓ 純粋理性 vs 感情の二分は誤り = 感情も合理性の一部
```

## ITU 視点: K_executive の構造

```
K_executive^(0) = -log P(action | state, goal, value)
                = 上位 K-state, K_perception を制御

軸:
  K_WM       (Working memory) - 短期保持
  K_attention (selective focus)
  K_value    (utility, dopamine RPE)
  K_planning (action sequencing)
  K_inhibition (response control)
  K_meta     (metacognition)

K_executive ⊃ K_perception ⊃ K_memory
   = ITU階層的構造 (top-down predictive)
```

### Free will (#9) との関連

```
Libet (1983): readiness potential 350 ms before conscious choice
↓
ITU 解釈: K_executive^(0) descent flow は意識より速い
↓ "free will" は K-state 最終 selection 段階のみ
↓ Phase 9 Free Will (Tier 1 #9) の神経実装基盤
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| PFC 全脳比率 (ヒト) | 30% ✓ |
| WM 容量 (Cowan) | 4 ± 1 chunks ✓ |
| Loss aversion λ | 2.25 ✓ |
| Iowa task VMPFC 損傷患者 | risky deck 多用 ✓ |
| Libet readiness potential | 350 ms ✓ |
| Schultz RPE 発火変化 | 報酬時 +50%, omission -30% ✓ |
| Dopamine ニューロン数 (ヒト VTA + SNc) | ~600,000 |
| **ITU axiom: decision making** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **WM BCI** 4 chunks → 8 chunks 拡張 | 2032 | 0.50 |
| Loss aversion λ の neurobiological mapping | 2028 | 0.65 |
| **Closed-loop dopamine modulation** (PD/addiction) | 2030 | 0.60 |
| AI decision agent = human Iowa task pattern 模倣 | 2028 | 0.75 |
| PFC digital twin (個人化) for decision support | 2032 | 0.45 |

---

📄 **論文 (Tier 1 #28)**: 10.5281/zenodo.20256729

> Phase 204 で Sleep + Consciousness Hard Problem へ進みます。

#情報理論的統一理論 #ITU #神経科学 #前頭前野 #ワーキングメモリ #意思決定 #Kahneman #Damasio #GoldmanRakic #Schultz #K_executive #Phase203
