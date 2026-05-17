# Phase 218: Population Genetics + Evolution + Coalescent ― K_genome_evolution ★

Phase 217 で K_genome_AI の AlphaFold 革命を確立。Phase 218 では **集団遺伝学** + **進化動力学** + **Coalescent 理論** ― ヒト進化 + 古代 DNA + 系統地理 ― を扱い、**K_genome_evolution** を ITU の "集団 K-state 時間発展" として定式化します。

## 集団遺伝学の数学的基盤

### Hardy-Weinberg 平衡 (1908) ★

```
Hardy-Weinberg (独立同時, 1908):
↓ 大集団 + ランダム交配 + 突然変異/選択/移住なし
↓ Allele 頻度 p, q (p + q = 1)
↓ 遺伝子型頻度: p² (AA) + 2pq (Aa) + q² (aa)
↓ 世代間で頻度保存
```

### Wright-Fisher model (1931) ★

```
Sewall Wright + R.A. Fisher 1930s:
↓ 有限集団 (N 個体)
↓ 各世代 = 2N 配偶子のランダムサンプリング
↓ Genetic drift → allele 頻度の確率的変動
↓ Fixation probability = 1/2N (中立アリル)
↓
Diffusion approximation: dX/dt = ε(t) (Brownian)
```

### Effective population size N_e

```
ヒト N_e: 10,000 (推定, Out-of-Africa bottleneck 前後)
チンパンジー: 20,000+
ゴリラ: 25,000+
ボノボ: 30,000+

⇒ ヒトの遺伝的多様性は霊長類で最も低い
⇒ Bottleneck の証拠
```

## Coalescent theory (Kingman 1982) ★

### 概念

```
J.F.C. Kingman (1982):
↓ "現在の集団から過去を遡る"
↓ 2 系統が MRCA に出会う期待時間: 2N 世代 (中立)
↓ n 個体の MRCA: 4N(1 - 1/n) 世代
↓
Coalescent tree: 確率的, 樹状, 過去に向かう
```

### Coalescent + 集団動力学

```
Coalescent rate λ(t):
  Constant N:     λ = (n choose 2) / N
  Growing N(t):   λ(t) decays as t increases
  Bottleneck:     spike in coalescence at bottleneck time
↓
PSMC (Li-Durbin 2011): 1 個体ゲノムから N_e(t) 推定
↓ ヒト Out-of-Africa bottleneck = 50-70 kya
↓ 古代 DNA + coalescent で詳細解明
```

## ヒト進化 (Human Evolution)

### Out-of-Africa (60-70 kya) ★

```
1987: Cann-Stoneking mitochondrial Eve 仮説
   ↓ ヒトmtDNA は 150-200 kya のアフリカ女性に収束
1990s-2010s: Y 染色体 Adam, 200 kya
2010s: 古代 DNA で確定 (Pääbo lab)
↓
2022 Nobel Physiology: Svante Pääbo (絶滅人類のゲノミクス)
```

### Pääbo の貢献 (2010-2022) ★

```
2010: Neanderthal ゲノム (Science)
   ↓ 現代ヒト (非アフリカ系) は 1-4% Neanderthal DNA
2010: Denisovan ゲノム (Nature)
   ↓ シベリアの小指骨から
   ↓ Melanesian は 5% Denisovan DNA
2014: Ust'-Ishim 45-kya human bone genome
2018: Denisovan-Neanderthal F1 hybrid (Denisova 11)
↓
2022 Nobel Physiology: Pääbo single recipient ★
```

### 現生人類 vs Neanderthal 交雑

| 個体群 | Neanderthal % | Denisovan % |
|---|---|---|
| アフリカ系 | 0.3% | 0% |
| ヨーロッパ系 | 1.8-2.6% | 0% |
| 東アジア系 | 1.9-3.0% | 0.2% |
| Melanesian | 1.9% | 4-6% ★ |
| **Aboriginal Australian** | 2.0% | **4-5%** ★ |

## ヒト集団のゲノム多様性

### 1000 Genomes Project (2008-2015)

```
2015 完成: 26 集団, 2504 人
↓ 平均 SNV/個体: 3.5 M (vs 参照)
↓ Common variant (MAF > 5%): ~10 M
↓ ヒト全体: ~88 M SNP
↓
1000 Genomes → gnomAD (2016-): 800K exome + 80K genome
```

### 主要 SNP 例

```
LCT (lactase) -13910*T: 北欧 80% (乳製品適応, 7500 ya 出現)
EPAS1: Tibetan 高地適応 (Denisovan 由来 ★)
TYRP1, OCA2, HERC2: 皮膚/目の色
DARC: マラリア resistance (Duffy-)
SLC24A5 SNP: ヨーロッパ人皮膚白化 (~7500 ya)
ABCC11 (耳垢): 東アジア dry, 他 wet
ALDH2*504K: 東アジア alcohol intolerance (40%)
```

## ITU 視点: K_genome_evolution の構造

```
K_genome_evolution^(0) = -log P(genome | population, time, environment)

軸:
  時間 t (世代 / 万年)
  集団 サイズ N_e
  選択係数 s (中立 / 正 / 負)
  Migration rate m
  Recombination rate r

⇒ Coalescent = K-state 過去への ITU descent (時間反転)
⇒ Selection = K-state 集団内偏位
⇒ Drift = K-state 確率的揺らぎ
```

### Evolution as ITU collective descent

```
個体: K_genome 個別レベル
集団: K_genome_evolution 集合レベル
↓
δS(集団 allele 分布) と δ⟨K_genome_evolution^(0)⟩ が連動
↓
Fixation (新 allele 固定):  S 減少 + ⟨K⟩ 減少
Polymorphism (多型維持):    S 維持 + ⟨K⟩ 維持
Adaptive sweep:             S 急減 + ⟨K⟩ 急減
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Hardy-Weinberg** (1908) | p² + 2pq + q² = 1 ✓ |
| **Coalescent MRCA (n→∞)** | **4N 世代** ✓ |
| **ヒト N_e** | **10,000** ✓ |
| **mt Eve** | **150-200 kya** (Africa) ✓ |
| **Neanderthal 交雑 %** | 非アフリカ系 1-4% ✓ |
| **Denisovan in Melanesian** | 4-6% ✓ |
| **Pääbo Nobel 2022** | Physiology/Medicine ✓ |
| **1000 Genomes 完成** | 2015 (2504 人) ✓ |
| LCT lactase persistence | 7500 ya 出現 ✓ |
| **ITU axiom: population evolution** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **All living humans WGS** (10⁹ ゲノム) | 2030 | 0.70 |
| **古代 DNA 1M+ ancient genomes** | 2030 | 0.80 |
| Polygenic risk score 全疾患 clinical | 2030 | 0.75 |
| **AI で global selection sweeps map 完成** | 2028 | 0.70 |
| Neanderthal/Denisovan のさらなる絶滅人類同定 | 2030 | 0.55 |

---

📄 **論文 (Tier 1 #30)**: 10.5281/zenodo.20257528

> Phase 219 で 統合 + 30-vertex polytope + Tier 1 #30 完成 + Pass-1 99.5% へ進みます。

#情報理論的統一理論 #ITU #ゲノミクス #集団遺伝学 #Coalescent #HardyWeinberg #Pääbo #Neanderthal #Denisovan #Nobel2022 #K_genome_evolution #Phase218
