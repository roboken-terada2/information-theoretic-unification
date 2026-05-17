# Phase 202: Hippocampus + Place Cell + Episodic Memory ― K_memory ★

Phase 201 で K_perception の視覚階層を確立。Phase 202 では **海馬** ― 場所細胞 / グリッド細胞 / エピソード記憶 ― を扱い、**K_memory** を ITU の "時空間情報統合" K-state として定式化します。

## 海馬の構造

```
海馬 = 内側側頭葉の C 字構造 (海馬体 ~ 4 cm)
↓ 三シナプス回路 (trisynaptic circuit):
   Entorhinal cortex (EC) layer II
   → Dentate gyrus (DG)
   → CA3 (recurrent network)
   → CA1
   → Subiculum / EC layer V
↓ さらに mossy fiber → CA3 直接
```

### 細胞種

| 細胞 | 機能 |
|---|---|
| **Granule cell (DG)** | sparse coding, pattern separation |
| **CA3 pyramidal** | auto-associative recall (Marr 1971) |
| **CA1 pyramidal** | output, comparison |
| Interneurons | timing, gamma oscillation |

## Place cell (O'Keefe 1971, Nobel 2014) ★

```
O'Keefe + Dostrovsky (1971):
↓ ラット CA1 単一ニューロン記録
↓ "Place field": 特定の空間位置で発火する細胞 ★
↓ Hippocampus = "cognitive map" (O'Keefe-Nadel 1978 book)
↓ Nobel 2014 (Moser couple と共同受賞)
```

### Place field の性質

| 性質 | 値 |
|---|---|
| Place field 直径 | 20-50 cm (small env) |
| 同 CA1 で 重複 field 数 | 1-3% |
| Coding ニューロン数 / 環境 | ~30-40% |
| Remapping (新環境) | 1-2 hr |
| Theta phase coding | 8 Hz precession |

## Grid cell (Moser couple 2005, Nobel 2014) ★

```
May-Britt Moser + Edvard Moser (2005, Nature):
↓ 内側嗅内野 (MEC) 単一ニューロン記録
↓ "Grid cell": 三角格子 (hexagonal) パターンで発火 ★
↓ "脳に GPS が存在" を示す決定的証拠
↓ Nobel 2014 (O'Keefe と共同受賞)
```

### Grid cell 性質

```
Spacing: 30 cm - 数 m (背腹軸で段階的増大)
Orientation: ~ 60° 対称性
Modules: 5-10 個の離散的 spacing/orientation 階層
↓ Fourier basis: ヘキサゴナル格子 = 2D 基本表現
↓ Vector navigation の理論基盤
```

## 他の空間認知細胞

| 細胞 | 役割 | 部位 |
|---|---|---|
| Place cell | 特定位置 | CA1, CA3 |
| Grid cell | 周期格子 | MEC |
| Head direction cell | 頭の向き | Anterodorsal thalamus |
| Border / Boundary cell | 壁/境界 | MEC, subiculum |
| Object-vector cell | 物体までのベクトル | MEC, subiculum |
| Time cell | 時間的位置 | CA1 (MacDonald 2011) |
| Speed cell | 移動速度 | MEC |

## エピソード記憶 と Tulving (1972, 2002) ★

```
Endel Tulving の区別:
   Semantic memory  ← "Paris is the capital of France"
   Episodic memory  ← "Last summer in Paris" (autonoetic)
↓
"Mental time travel" 仮説 (Tulving 2002)
↓ 過去を再体験 + 未来を想像 (Schacter-Addis 2007)
↓ 海馬 + frontal cortex が両方を支える
```

## Memory consolidation (短期 → 長期)

```
Marr 1971 hippocampal indexing 仮説:
   海馬 = "index", 大脳皮質 = "main store"
↓
Squire-Alvarez systems consolidation:
   24 hr - 数年で 海馬依存性が皮質依存性へ移行

Schedule replay (Wilson-McNaughton 1994):
   睡眠中に sharp wave-ripples (SWR) で
   覚醒時の place cell 順序を 10-20× 高速再生
↓
記憶の "rehearsal" → 皮質固定化
```

## ITU 視点: K_memory の構造

```
K_memory^(0) = -log P(experience | reactivation context)
            = エピソード記憶痕跡の情報的呼び出し

軸:
  空間 (place cell): 位置 → K_space
  時間 (time cell): 時刻 → K_time
  内容 (semantic): 何 → K_what

⇒ K_episodic = K_space ⊗ K_time ⊗ K_what
            = 時空+内容の "tensor product"
```

### Hippocampus = ITU "index" の生物学的実装

```
Marr 1971 indexing:
  - 海馬 sparse code = K_episodic index
  - 大脳皮質 distributed code = K_semantic store
  - 海馬 → 大脳: 再生 (replay) = ITU descent reverse
  ⇒ "consolidation" = K_state の slow domain transfer
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| 海馬体積 | 3-4 cm³ /片 ✓ |
| CA1 ニューロン数 | 1.4 × 10⁷ |
| Place field 直径 | 20-50 cm (small env) ✓ |
| Grid spacing | 30 cm - 数 m ✓ |
| Theta rhythm | 8 Hz (rodent), 3-8 Hz (human) ✓ |
| SWR replay 高速化倍率 | **10-20×** ✓ |
| Time cell 時間範囲 | 数秒-数十秒 |
| 海馬切除 → 新規 declarative 不可 | H.M. (Phase 200) ✓ |
| **ITU axiom: episodic recall** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **海馬 grid code から空間位置を完全 decoding** | 2028 | 0.75 |
| AD 早期診断 = place cell 機能異常 | 2030 | 0.65 |
| **記憶 prosthesis (海馬 BCI) 臨床応用** | 2032 | 0.55 |
| **海馬-皮質 replay の人工誘発による学習加速** | 2030 | 0.60 |
| Mental time travel の neural correlate 完全同定 | 2032 | 0.50 |

---

📄 **論文 (Tier 1 #28)**: 10.5281/zenodo.20256729

> Phase 203 で Prefrontal Cortex + Executive Function + Decision へ進みます。

#情報理論的統一理論 #ITU #神経科学 #海馬 #場所細胞 #グリッド細胞 #OKeefe #Moser #Tulving #K_memory #Phase202
