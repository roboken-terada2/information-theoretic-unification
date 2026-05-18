# Phase 246: 音楽知覚 + 認知音楽学 + 神経音楽学 ― K_music_perception ★

Phase 245 で K_music_theory の音律・和声・形式を確立。Phase 246 では **音楽知覚 + 認知音楽学 (Cognitive Musicology) + 神経音楽学 (Neuromusicology)** を扱い、**K_music_perception** を ITU の "聴覚 K-state" として定式化します。

## 聴覚生理学

### 蝸牛 (Cochlea) の周波数分析 ★

```
蝸牛 = 進化的に最も精密な周波数分析器:
↓
Békésy 1928 trauma-wave 理論 (Nobel 1961):
↓ 基底膜 (basilar membrane) の場所による周波数選択
↓ 高周波: 蝸牛入口
↓ 低周波: 蝸牛頂部
↓
~16,000 internal hair cells (Corti器官)
~3,500 inner + 12,500 outer hair cells
↓
周波数分解能: 1-3 Hz @ 1 kHz
時間分解能: 10 μs (interaural time difference)
```

### 絶対音感 vs 相対音感

```
絶対音感 (Perfect pitch, AP):
  音名を聴くだけで識別可能
  発生率: 0.01-1% (アジア人 > 西洋人)
  ↓ 早期 (3-6歳) 音楽教育で増加
  ↓ Levitin 1994 7セミトーン以内で識別可能
↓
相対音感 (Relative pitch):
  ほぼ全人類が獲得可能
  音程関係の把握
```

### Cochlear Implant (人工内耳)

```
1957: Djourno-Eyriès 最初の電気刺激試験
1972: Clark 多チャネル (3 ch)
1990s: 22 ch 標準
2024: 22 ch 50万人以上が使用
↓
言語理解: 高機能患者 80%+
音楽: 限定的 (倍音情報損失)
```

## 認知音楽学

### Gestalt 原理 (Wertheimer 1923 → Bregman 1990)

```
Auditory Scene Analysis (Bregman 1990):
↓ "Streaming" - 周波数+時間で音源分離
↓ Pitch proximity, Temporal proximity, Common fate

音楽特有:
  Voice leading: 旋律線が分離して聞こえる
  Polyphony: バッハフーガ多声 → 個別追跡可能
```

### Krumhansl 確率モデル (Krumhansl 1990)

```
"Cognitive Foundations of Musical Pitch" (1990):
↓ Tonal hierarchy: I > V > IV > vi > ... 
↓ 各音度の "確率分布" を実験的に測定
↓
予測:
  リスナーが next note を予測
  予測誤差 = K-state surprise → 美的感覚
```

### 期待理論 (Huron 2006 "Sweet Anticipation")

```
David Huron (2006):
↓ ITPRA model (Imagine, Tension, Prediction, Reaction, Appraisal)
↓ 予測 ↔ 違反のバランスが快感を生む
↓
音楽 = 期待生成 + 適度な violation
↓
ITU: 期待 = K_predicted, 違反 = K_surprise
情動 = Δ K ≈ optimal
```

## 神経音楽学

### 音楽処理脳マップ

```
聴覚皮質: A1 (一次), A2 (二次)
位置: Heschl's gyrus (横側頭回)
↓
音楽特化:
  右側聴覚皮質 = 音程・和声
  左側 = リズム
  右前頭 = 音楽理解
  運動野 = リズム同期
↓
fMRI: 音楽聴取で 30+ 領域活性化
```

### 音楽 + 感情

```
辺縁系 + 報酬系:
  扁桃体 (Amygdala): 感情応答
  腹側線条体 (NAc): "musical chills" (ドーパミン放出)
↓
Salimpoor 2011 (Nat Neurosci):
  "musical chills" 中ドーパミン放出 PET 確認
  cocaine と同じ報酬経路
↓
治療応用:
  音楽療法 (depression, autism, Alzheimer)
```

### Musical training の脳可塑性

```
プロ音楽家 vs アマチュア vs 非音楽家:
↓
脳灰白質増大:
  Schlaug 1995: corpus callosum +10-15% (両手協調)
  Gaser-Schlaug 2003: motor cortex, sensory cortex
↓
小児期 7 歳前開始:
  ★ Critical period for advanced training
  ↓ 言語と同じ臨界期
```

### Amusia (失音楽症)

```
先天性 amusia: 4% 人口
↓ congenital pitch deficit
↓ Peretz 2002, Hyde 2007 fMRI

後天性 amusia:
  右半球障害 (Broca homolog) → pitch
  左半球障害 → rhythm 障害
```

## ITU 視点 ― K_music_perception

### 聴覚 = 周波数 K-state mapping

```
K_music_perception^(0) = -log P(percept | stimulus)

蝸牛 → 周波数 → 旋律 → 和声 → 音楽
↓
階層的 K-state:
  K_pitch (Hz level)
  K_interval (relations)
  K_chord (vertical structure)
  K_phrase (horizontal structure)
  K_form (macroscopic)
```

### 予測 = K-state minimization

```
Huron model = ITU 期待:
  P_listener(next note | history)
↓ K_predicted = -log P
↓ K_surprise = -log P_observed
↓ "美的感動" ∝ Δ(K_predicted, K_surprise)
↓ optimal = 中程度の predictability
```

### Musical chills = K-state phase transition

```
NAc dopamine release ★:
  Salimpoor 2011 - chills 経験中
↓
ITU: 大きな K-state transition (予測 → 違反 → 解決)
↓ 報酬系発火
↓ "脳の K-state 大域再配置"
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **可聴域** | **20 Hz - 20 kHz** ✓ |
| Critical bands | **24** (Bark) ✓ |
| Frequency resolution | **1-3 Hz @ 1 kHz** ✓ |
| Inner hair cells | **~3,500** ✓ |
| **AP (絶対音感) 発生率** | **0.01-1%** ✓ |
| **Cochlear implant 数 (2024)** | **500K+ patients** ✓ |
| Congenital amusia 発生率 | **4%** (Peretz 2002) ✓ |
| **Musical chills + dopamine** | Salimpoor 2011 Nat Neurosci ✓ |
| ITU axiom: 音楽期待 | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **fMRI による情動音楽予測** | 2028 | 0.80 |
| **AI 音楽 emotional response 完全予測** | 2030 | 0.70 |
| BCI 音楽再生 (脳直接) | 2032 | 0.60 |
| **音楽療法 + AI 個別化** | 2027 | 0.85 |
| Amusia 遺伝子治療 | 2032 | 0.50 |

---

📄 **論文 (Tier 1 #34, Block C 2/6)**: 10.5281/zenodo.20262862

> Phase 247 で作曲 + 即興演奏 + アルゴリズム作曲 へ進みます。

#情報理論的統一理論 #ITU #音楽 #音楽知覚 #認知音楽学 #神経音楽学 #Krumhansl #Huron #Salimpoor #K_music_perception #Phase246
