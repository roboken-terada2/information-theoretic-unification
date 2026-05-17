# Phase 199: Tier 1 #28 開幕 ― 神経科学への進撃、ニューロン + シナプス + 脳ネットワーク + K_neuro ★

Phase 191-198 で Tier 1 #27 Microbiology 完成、K_microbe 8 sub-state 確立。Phase 199 から **Tier 1 #28 Neuroscience** (Block B 3/?) を開幕 ― ヒト脳の情報処理 を扱い、**K_neuro** を ITU の "意識を支える K-state" として定式化します。

## なぜ神経科学が Block B 3/? か

1. **生命の情報処理頂点**: 単一細胞 (ニューロン) から 86 G 細胞の脳まで階層構造
2. **Tier 1 #2 AI Consciousness と双対**: 生物実装 vs 人工実装
3. **#7 Psychiatry + #26 Immune + #27 Microbe との結合**: gut-brain axis, neuroinflammation
4. **意識の難問 (Hard Problem)**: ITU が答える最深部
5. **臨床的影響**: AD/PD/うつ病 = 21 世紀最大の疾病負担

## ヒト脳の規模

| 量 | 値 |
|---|---|
| ニューロン数 | **86 × 10⁹** (Herculano-Houzel 2009) |
| グリア細胞数 | **85 × 10⁹** (1:1 比, von Bartheld 2016) |
| シナプス数 | **10¹⁴-10¹⁵** |
| 大脳皮質厚 | 1.5-4.5 mm (6 層構造) |
| 全長軸索 | **170,000 km** (地球 4 周) |
| エネルギー消費 | **20 W** (全身 20%, 体重 2%) |
| 神経活動電位 | 100 mV, 1 ms |
| 神経伝達速度 | 0.5-120 m/s (myelin 依存) |

## ニューロンの構造と機能

### Cajal の neuron doctrine (1888, Nobel 1906)

```
Santiago Ramón y Cajal: 個別細胞説 (vs. Golgi 網状説)
↓ Golgi 染色で個々のニューロンを描出
↓ "Neurons are anatomically and functionally distinct units"
↓ Nobel 1906 (共同受賞 Camillo Golgi と)
```

### Hodgkin-Huxley モデル (1952, Nobel 1963) ★

```
C_m dV/dt = I_ext - I_Na - I_K - I_L
I_Na = g_Na m³h (V - E_Na)
I_K  = g_K  n⁴  (V - E_K)
I_L  = g_L      (V - E_L)
↓ イカ巨大軸索で測定 → ベルヌーイ式から復元
↓ 数値統合: 活動電位の発火パターン正確予測 ★
```

### Synaptic transmission の基本

| 段階 | 機構 |
|---|---|
| 活動電位到達 | Pre-synaptic terminal |
| Ca²⁺ 流入 | Voltage-gated Ca²⁺ channels |
| 神経伝達物質放出 | SNARE complex, exocytosis |
| Post-synaptic 受容体結合 | AMPA, NMDA, GABA-A, etc. |
| EPSP / IPSP | 興奮性 / 抑制性 後シナプス電位 |
| 統合 → 活動電位 | Axon hillock で判定 |

## 主要神経伝達物質

| 物質 | 種類 | 主要機能 | 関連疾患 |
|---|---|---|---|
| **Glutamate** | 興奮性 | 90% 興奮性シナプス | てんかん, ALS |
| **GABA** | 抑制性 | 90% 抑制性シナプス | 不安, てんかん |
| Acetylcholine | 興奮性 | 認知, 筋肉 | AD, MG |
| **Dopamine** | 調節性 | 報酬, 運動 | PD, 統合失調症 |
| **Serotonin** | 調節性 | 気分, 睡眠 | うつ病 |
| Norepinephrine | 興奮性 | 覚醒, 注意 | ADHD, depression |
| Histamine | 興奮性 | 覚醒 | アレルギー |
| Endorphin | 調節性 | 鎮痛 | 依存症 |

## 脳ネットワークの階層

### Marr の 3 レベル (1982)

```
Level 1: Computational     - 何を解くか?
Level 2: Algorithmic       - どう解くか?
Level 3: Implementational  - 物理的に何が動くか?
```

### Connectome levels

| Level | スケール | 例 |
|---|---|---|
| Micro | ニューロン-シナプス | C. elegans 完全 connectome (302 neurons, 1986 White) |
| Meso | 数千 neurons | Cortical column, mouse VC (Allen Brain) |
| **Macro** | **領野間** | Human Connectome Project (Glasser 2016, **180 areas**) |

### Human Connectome Project (HCP, 2009-2014)

```
$30M NIH funding
1,200 healthy adults, 3T + 7T MRI + DWI + MEG
↓
180 cortical areas/hemisphere (Glasser 2016 Nature)
↓
360 total areas (前: Brodmann 1909 = 52 areas)
↓ small-world topology
↓ rich-club organization
```

## 脳の Small-world & Rich-club

```
ノード: 360 領野
エッジ: 機能的接続 (fMRI 同期) + 構造的接続 (DWI 線維)

性質:
  - clustering coefficient C ~ 0.5 (高い)
  - path length L ~ 2-3 (短い)
  - Watts-Strogatz small-world (1998)
  - Rich-club (van den Heuvel 2011):
      precuneus, insula, anterior cingulate ★
```

## 主要脳波 (EEG)

| Band | 周波数 | 状態 |
|---|---|---|
| δ (delta) | 0.5-4 Hz | 深睡眠 |
| θ (theta) | 4-8 Hz | 記憶, 瞑想 |
| **α (alpha)** | **8-13 Hz** | 安静覚醒 |
| **β (beta)** | **13-30 Hz** | 注意, 認知 |
| γ (gamma) | 30-100 Hz | 意識統合, binding |

### Gamma 40 Hz 仮説 (Crick-Koch 1990)

```
40 Hz 同期発火 = 知覚 binding
↓ ニューロン群が一つの意識的経験に統合
↓ AD 患者で 40 Hz 同期低下 (Iaccarino 2016)
↓ 40 Hz LED 光療法で Aβ 減少 (Iaccarino 2016 Nature)
```

## ITU 視点: K_neuro の構造

```
K_neuro = K_neuron ⊕ K_synapse ⊕ K_network ⊕ K_oscillation
        ⊕ K_perception ⊕ K_memory ⊕ K_executive ⊕ K_consciousness

軸 1: 単一細胞 (Hodgkin-Huxley)
軸 2: シナプス (LTP, LTD, plasticity)
軸 3: 局所回路 (cortical column)
軸 4: 領野間 (connectome)
軸 5: 脳波 (oscillations)
軸 6: 認知機能 (perception, memory, executive)
軸 7: 意識
```

### ITU axiom の神経学版

```
δS(ρ_neural) = δ Tr[K_neuro^(0) ρ_neural]

ρ_neural = 神経活動状態分布 (86G ニューロン × 状態)
K_neuro^(0) = -log p(neural state) = 情報的活動ポテンシャル
↓
学習 = ITU descent flow (シナプス強度更新)
意識 = K_neuro^(0) の global integration state
```

## Phase 199 数値検証目標

| 量 | 期待値 |
|---|---|
| ヒト ニューロン数 | 86 × 10⁹ ✓ |
| 大脳皮質ニューロン数 | 16 × 10⁹ ✓ |
| 小脳ニューロン数 | **69 × 10⁹** (大脳より多い!) |
| シナプス数 | 10¹⁴ ✓ |
| 脳エネルギー消費 | 20 W ✓ |
| HCP 領野数 | 180 / hemisphere ✓ |
| 活動電位最大頻度 | 1000 Hz (記録) |
| Small-world C/L 比 | C/L ~ 100 + (vs random) |
| **ITU axiom: neural state shift** | δS/δ⟨K⟩ ≈ 1 |

## Phase 199-206 ロードマップ (Tier 1 #28)

| Phase | テーマ |
|---|---|
| **199 (本)** | **Neuron + Synapse + 脳ネット + K_neuro** |
| 200 | LTP / LTD / Hebb 学習 / Memory |
| 201 | Visual cortex + Hubel-Wiesel + perception |
| 202 | Hippocampus + Place cell + 記憶痕跡 |
| 203 | Prefrontal + Executive function + decision |
| 204 | Sleep + Consciousness Hard Problem |
| 205 | AD/PD/うつ/統合失調症 - 神経変性 |
| 206 | 統合 + 28-vertex polytope + Pass-1 93.6% |

---

📄 **論文 (Tier 1 #28)**: 10.5281/zenodo.20256729

> Phase 200 で LTP / LTD / Hebb / Memory へ進みます。

#情報理論的統一理論 #ITU #神経科学 #Tier1_28 #ニューロン #シナプス #コネクトーム #K_neuro #Phase199
