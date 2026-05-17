# Phase 197: 細菌代謝 + 共生 + 極限環境 ― K_metabolism + K_extremophile ★

Phase 196 で K_pandemic の種間 jump を確立。Phase 197 では **細菌代謝の多様性** + **共生関係** + **極限環境微生物** を扱い、ITU を生命圏の代謝可能性空間として展開します。

## 細菌代謝: 6 主要型

| 型 | 炭素源 | エネルギー源 | 電子供与体 | 例 |
|---|---|---|---|---|
| **Photoautotroph** | CO₂ | 光 | H₂O / H₂S | Cyanobacteria, 紅色硫黄菌 |
| Photoheterotroph | 有機 | 光 | 有機物 | 紅色非硫黄菌 |
| **Chemolithoautotroph** | CO₂ | 化学 (NH₃, NO₂⁻, S, H₂, Fe²⁺) | 無機 | 硝化菌, 鉄酸化菌 |
| Chemoheterotroph | 有機 | 化学 | 有機物 | E. coli, ヒト病原菌 多数 |
| Mixotroph | 両方 | 両方 | 両方 | 多くの環境細菌 |
| **Diazotroph** (固定特化) | CO₂ / 有機 | 化学 / 光 | + **N₂ fixation** | Rhizobium, Azotobacter, Cyanobacteria |

## 生命の代謝経路階層

### 中心代謝

```
解糖 (Glycolysis, EMP): glucose → pyruvate + 2 ATP
TCA (Krebs): pyruvate → CO₂ + NADH + FADH₂
ETC + ATP synthase: NADH → 3 ATP (好気)
                    NADH → 1-2 ATP (嫌気, 発酵)
```

### 嫌気発酵 (酸素ゼロ)

| 産物 | 担体 |
|---|---|
| 乳酸 | Lactobacillus |
| エタノール + CO₂ | 酵母 (Saccharomyces) |
| 酢酸 | Acetobacter |
| 酪酸 | Clostridium butyricum |
| メタン | メタン生成古細菌 (Methanogen) |

### 嫌気呼吸: 多様な電子受容体

```
NO₃⁻ → N₂  (Denitrification)
SO₄²⁻ → H₂S (Sulfate reduction, Desulfovibrio)
Fe³⁺ → Fe²⁺ (Geobacter)
CO₂ → CH₄ (Methanogenesis)
```

## 共生 5 型 (de Bary 1879)

| 型 | 双方の影響 | 例 |
|---|---|---|
| **Mutualism** | + / + | 根粒菌-マメ科, 腸内細菌-ヒト |
| Commensalism | + / 0 | 皮膚菌叢 |
| Parasitism | + / - | 病原体-宿主 |
| Amensalism | 0 / - | Penicillium 抗生物質産生 |
| **Endosymbiosis** | 統合 | ミトコンドリア, 葉緑体 (Margulis 1970) |

### Endosymbiotic theory (Margulis 1970) ★

```
Mitochondria 起源: α-Proteobacteria (Rickettsia 系)
Chloroplast 起源: Cyanobacteria

証拠:
  - 二重膜 (内膜 = 細菌, 外膜 = 宿主由来)
  - 独自 DNA (環状, 細菌型)
  - 70S リボソーム (細菌型)
  - 細菌型抗生剤感受性
  - 二分裂で増殖
```

= **真核生物 = 細菌 + 古細菌の合体生物** ★

## 窒素固定 (Diazotrophy)

```
N₂ + 8 H⁺ + 8 e⁻ + 16 ATP → 2 NH₃ + H₂ + 16 ADP + 16 Pi
↓ ニトロゲナーゼ (Mo-Fe protein)
↓ 酸素に極めて感受性 (FeMoco クラスター壊れる)
```

### Diazotroph 分布

- 自由生活: Azotobacter (好気), Cyanobacteria (heterocyst で O₂ 隔離)
- 共生: Rhizobium (マメ科根粒), Frankia (Alnus)
- 海洋: Trichodesmium (10¹⁵ kg N/年 ★)
- 地球窒素サイクル: 人為 (Haber-Bosch, 1.2×10⁸ t/yr) + 生物 (1.5×10⁸ t/yr)

## 極限環境微生物 (Extremophiles)

### 6 主要極限環境

| 環境 | 上限 / 下限 | 代表生物 |
|---|---|---|
| **高温** | **122°C** | *Methanopyrus kandleri* (深海熱水) |
| 低温 | -25°C | Cryptoendolith (南極岩) |
| **高酸** | **pH 0** | *Picrophilus oshimae* (温泉) |
| 高アルカリ | pH 12 | *Natranaerobius* |
| **高塩** | **30% NaCl** | *Halobacterium salinarum* (Dead Sea) |
| 高圧 | 110 MPa | *Pyrococcus yayanosii* (海溝) |
| 高放射線 | 5 kGy | *Deinococcus radiodurans* (= 人類致死量 1000×) |
| 高乾燥 | 数百万年 | Spore forming bacteria |

### Deinococcus radiodurans ★ — 自然界の "Conan the Bacterium"

```
γ線 5 kGy 耐性 (ヒト致死量 5 Gy = 1000× 耐性)
↓ 機構: DNA 多重修復 + Mn²⁺ クラスター抗酸化 + 環状ゲノム複数 copy
↓ 用途: 放射性廃棄物バイオレメディエーション候補
```

### 122°C 生命の上限? (現時点)

```
Methanopyrus kandleri Strain 116 (Takai 2008 PNAS):
  in vitro 増殖: 80-122°C
  Volcanic vent (Atlantic Ocean)
  代謝: CO₂ + H₂ → CH₄ + H₂O
↓
さらに高温の生命体は理論的に存在しうる?
プロテインの熱安定性限界が制約 (~150°C?)
```

## ITU 視点: K_metabolism + K_extremophile

```
K_metabolism^(0) = -log P(metabolic pathway | environment, organism)
                = 代謝可能性の情報的距離

K_extremophile^(0) = -log P(viable | extreme condition)
                  = "禁制空間" の境界

K_endosymbiotic = K_state 合体演算子 (Margulis)
   → 真核細胞 = 2 K-state の "tensor product"
```

### Metabolic landscape の ITU 描像

```
1 細胞 = 数百-数千 反応のネットワーク
↓
flux balance = K_metabolism^(0) の制約多様体
↓ optimization
↓
細菌種ごとに固有 K-state attractor

E. coli K-12: 約 1,800 反応
Genome-scale model (GEM): iJO1366 (1366 遺伝子, Orth 2011)
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| 窒素固定 ATP cost | 16 ATP / N₂ ✓ |
| Trichodesmium 海洋 N 固定 | 1.5×10¹⁵ kg N/yr (Capone 2005) |
| D. radiodurans LD50 (γ線) | **5,000 Gy** (ヒト 5 Gy) ✓ |
| 生命温度上限 (現在記録) | **122°C** (Takai 2008) ✓ |
| 生命 pH 範囲 | 0-12 ✓ |
| 真核ミトコンドリア DNA | 16,569 bp (ヒト) ✓ |
| 葉緑体 DNA | 120-180 kb ✓ |
| **ITU axiom: metabolic shift** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| 生命温度上限 130°C+ 検出 | 2030 | 0.45 |
| **D. radiodurans 工業応用 (核廃棄物)** | 2032 | 0.55 |
| **Haber-Bosch alternative (生物的 N 固定 industrial)** | 2030 | 0.50 |
| Synthetic minimum genome 100 遺伝子以下 | 2030 | 0.40 |
| Astrobiology extremophile = アナログ確立 | 2028 | 0.65 |

---

📄 **論文 (Tier 1 #27)**: 10.5281/zenodo.20256555

> Phase 198 で 統合 + 27-vertex polytope + Tier 1 #27 完成 + Pass-1 90% へ進みます。

#情報理論的統一理論 #ITU #微生物学 #細菌代謝 #共生 #極限環境 #Endosymbiosis #Margulis #K_metabolism #Phase197
