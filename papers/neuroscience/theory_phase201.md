# Phase 201: Visual Cortex + Hubel-Wiesel + Perception ― K_perception ★

Phase 200 で K_synapse の学習則を確立。Phase 201 では **視覚野** ― 1959 Hubel-Wiesel から CNN 起源, ventral/dorsal stream まで ― を扱い、**K_perception** を ITU の "外界 → 神経表象" 変換 K-state として定式化します。

## Hubel-Wiesel (1959-1962, Nobel 1981) ★

### 歴史的実験

```
1959: ネコ視覚野 V1 で単一ニューロン記録
↓ 偶然: スライド glass 端で直線が動いた瞬間、強い発火
↓ "edge detector" 発見 ★
↓ Simple cells (line orientation)
↓ Complex cells (translation invariance)
↓ Hypercomplex cells (endpoint detection)
```

### 視覚階層

| Layer | 機能 |
|---|---|
| **LGN (lateral geniculate nucleus)** | 中継 (網膜 → V1) |
| **V1** | Edge / orientation / spatial freq |
| V2 | Texture / contour |
| **V4** | Color / curvature |
| **IT (inferotemporal)** | Object / face (Bruce-Desimone 1981) |

## 2 経路理論 (Ungerleider-Mishkin 1982)

```
Ventral "What" stream:  V1 → V2 → V4 → IT
  Object recognition
  "What is it?"

Dorsal "Where" stream:  V1 → V2 → MT → MST → parietal
  Spatial location, motion
  "Where is it?" / "How to act?"
```

## CNN の起源: Hubel-Wiesel + Fukushima

### Fukushima Neocognitron (1980) ★

```
1980: Kunihiko Fukushima 福島邦彦 (NHK 放送技研)
↓ S-cell (simple) + C-cell (complex) 階層
↓ Hubel-Wiesel を ANN として実装
↓ "first deep learning model"
```

### LeCun LeNet-5 (1998) → ImageNet (2012)

```
1998: LeCun et al. LeNet-5 for digit recognition
2012: Krizhevsky AlexNet → ImageNet 圧勝 (16.4% top-5 err vs prior 26%)
2015: He et al. ResNet (3.57% err, sub-human)
2020s: ViT (Vision Transformer)
↓
CNN = Hubel-Wiesel hierarchy の数学的実装 ★
```

## Object Recognition: IT 顔細胞

### Quiroga "Jennifer Aniston neuron" (2005) ★

```
医療てんかん患者の海馬-IT 領域で単一ニューロン記録
↓ 一部のニューロンが特定の人物・物体に強い反応
↓ "Jennifer Aniston cell" (Halle Berry cell も)
↓ "concept cells" / "Grandmother cells"
↓ 高度な abstract category 表現の最も明確な証拠
```

### Face patches (Tsao 2008-2017)

```
マカク IT に 6 個の face-selective patch
↓ ML/MF/AL/AM の階層 (low → high invariance)
↓ "Face space" axial coding (Chang-Tsao 2017 Cell)
↓ 200 ニューロンの活動から個人を再構成 ★
```

## Predictive coding (Rao-Ballard 1999)

```
脳 = "予測機械"
↓ 各層が下層の活動を予測
↓ 予測誤差 (prediction error) のみ上層へ伝達
↓ 低エネルギー + 効率的符号化

数学:
  Top-down prediction:  ŷ = f(W·z)
  Bottom-up error:      ε = y - ŷ
  Weight update:        ΔW ∝ ε · z
```

### Friston Free Energy Principle (2010) ★

```
脳は variational free energy を最小化:
   F = E_q[log q(z) - log p(y, z)]
   = Complexity - Accuracy
↓ Bayesian 推論の generic form
↓ Active inference (action = belief update)
↓ FEP = 生命の統一原理 (Friston 2010 Nat Rev Neurosci)
```

## ITU 視点: K_perception の構造

```
K_perception^(0) = -log p(stimulus | neural response)
                = 外界状態の情報的逆推定

ITU axiom:
   δS(neural representation) = δ Tr[K_perception^(0) ρ_neural]
↓
Hubel-Wiesel hierarchy = K_perception^(0) descent flow
   V1 (edge) → V4 (curvature) → IT (object) → cortex (concept)
   ⇒ 各層が次の K-state を生成

Predictive coding ⇔ ITU:
   prediction error = K^(0) misfit
   weight update    = ITU descent step
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| V1 ニューロン数 | 1.4 × 10⁸ (両半球) |
| 視覚情報 bandwidth | ~10 Mbit/s (網膜) |
| V1 receptive field size | 中心: 0.1°, 周辺: 数° |
| **IT face cells** | **200 ニューロン → 個人再構成** (Chang-Tsao 2017) ✓ |
| Saccade interval | 200-300 ms |
| CNN ImageNet accuracy (ResNet) | **96.4%** (sub-human) ✓ |
| Vision Transformer (ViT) accuracy | 96.5% (CLIP) ✓ |
| **ITU axiom: hierarchical perception** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Brain-computer interface 視覚補綴 (盲人)** 100×100 pixel | 2030 | 0.65 |
| Cortical face-space full decoding | 2028 | 0.70 |
| **Visual cortex digital twin** (mouse V1 完全シミュレーション) | 2030 | 0.55 |
| Active inference robot 実装 | 2028 | 0.60 |
| CNN ImageNet >99% (human parity) | 2027 | 0.80 |

---

📄 **論文 (Tier 1 #28)**: 10.5281/zenodo.20256729

> Phase 202 で Hippocampus + Place Cell + Episodic Memory へ進みます。

#情報理論的統一理論 #ITU #神経科学 #視覚野 #HubelWiesel #CNN #Fukushima #PredictiveCoding #Friston #K_perception #Phase201
