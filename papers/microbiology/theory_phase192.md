# Phase 192: 系統発生 + 16S rRNA + LUCA + Tree of Life ― K_phylogeny ★

Phase 191 で K_microbe の全体像を提示。Phase 192 では **生命の系統樹** ― Darwin (1859) → Haeckel → Woese 3 ドメイン (1977) → LUCA → 現代 genome-based phylogenomics ― を扱い、**K_phylogeny** を ITU の "進化情報マップ" として定式化します。

## 系統発生学史

### Darwin "Tree of Life" (1859)

```
"The affinities of all the beings of the same class have sometimes been represented by a great tree."
  - Origin of Species, p. 129, only figure in the book
```

### Haeckel (1866) - 形態に基づく系統樹

```
Phylogeny (彼の造語) = 進化的歴史
Ontogeny vs Phylogeny: "Ontogeny recapitulates phylogeny" (議論あり)
```

### Woese (1977) - 16S rRNA で 3 ドメイン革命 ★

```
Carl Woese: rRNA 配列で系統樹を再構築
↓
発見: bacteria + archaea + eukarya = 3 ドメイン
↓
古細菌 (archaea) は bacteria より eukarya に近い
↓
真核細胞の起源論議 (asgardarchaea 2017)
```

## 16S rRNA = 系統学の "分子時計"

### なぜ 16S か?

- **ribosomeコア成分**: 全細菌で保存
- **遅い変化速度**: 進化的に長距離まで信号保持
- **可変領域 V1-V9**: 種レベル識別可能
- **長さ ~1500 bp**: PCR で増幅容易

### 環境シーケンシング革命

```
Pace 1985: 環境 DNA 直接シーケンス
↓
metagenomics: Venter 2004 (Sargasso Sea, 1800 種推定)
↓
EMP (Earth Microbiome Project) 2010-: 全世界 サンプル
↓
~10⁶-10⁷ "種" (OTU/ASV) 推定 ★
```

## LUCA (Last Universal Common Ancestor) ★

### LUCA の特徴 (Weiss et al. 2016 Nat. Microbiol.)

```
~4 Ga (40 億年前)
↓ 354 conserved genes 同定
↓
推定: thermophile, anaerobe, autotroph (CO2 fix)
↓ H2 + CO2 → 還元的アセチル CoA 経路
↓ N2 fixation 能力
```

### LUCA の住処: 深海熱水噴出孔 (alkaline serpentinization)

```
Lost City (Atlantic 2000): pH 9-11, 70-90°C, H2-rich
↓ ITU 視点: K_metabolism の最古 stable point
↓ "FeS chimney" 膜構造 → 初期 chemiosmosis
```

## 現代 phylogenomics

### マルチ遺伝子系統解析

| 手法 | 遺伝子セット | 出典 |
|---|---|---|
| 16S only | ribosomal | 古典 |
| **GTDB**  | 120 marker | Parks 2018 |
| Concatenated rProteins | 16 ribosomal | Hug 2016 |
| Whole-genome ANI | 全ゲノム比較 | Konstantinidis 2005 |
| **Pangenome** | core ⊕ accessory | Tettelin 2005 |

### Tree of Life の現代的姿 (Hug 2016 "Nat. Microbiol.")

```
3 ドメイン → 92 phyla (bacteria) + 26 phyla (archaea) + 真核生物
↓
"CPR" (Candidate Phyla Radiation, Brown 2015): 寄生 / 共生細菌の大集団
↓
ITU 視点: K_phylogeny の "暗黒物質" (uncultured majority)
```

## ITU 視点: K_phylogeny の構造

```
K_phylogeny^(0) = -log P(species | environmental + temporal coordinate)
                = 進化情報密度ポテンシャル

座標:
  τ : 進化的時間 (Ga)
  E : 環境ニッチ (T, pH, [O2], [CO2], etc.)
  G : ゲノム空間 (10^6-10^8 bp)

LUCA = K_phylogeny の origin (singularity)
系統樹 = K_phylogeny^(0) descent flow trajectory
```

### 主要 phylum 数値

| ドメイン | phylum 数 | 種多様性 |
|---|---|---|
| Bacteria | 92 (GTDB 2020) | 10⁶-10⁷ |
| Archaea | 26 | 10⁴-10⁵ |
| Eukarya | ~30 | 870 万 (Mora 2011) |

## 系統発生の数値検証

| 量 | 期待値 |
|---|---|
| 16S rRNA 変異率 | ~10⁻⁹ /位置/年 (Ochman 1999) |
| LUCA 年代 | 4.0-4.2 Ga (Battistuzzi 2004) |
| 真核生物分岐 | 1.5-2.0 Ga (Knoll 2014) |
| 動物分岐 | 0.6-0.7 Ga (Cambrian explosion) |
| HGT 寄与 (LUCA-era) | 70%+ of gene transfers (Doolittle 2000) |
| 海洋細菌 phylum (TARA Oceans) | 35,000 OTU (Sunagawa 2015) |

## ITU axiom と分子時計

```
分子時計: Δseq = μ × Δt × N (中立進化)
↓
K_phylogeny^(0)(t) - K_phylogeny^(0)(0) = -log p(seq_t | seq_0)
                                       = μ × Δt × N
↓
δS_evol = δ⟨K_phylogeny⟩  ★ ITU axiom の進化的版
```

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **LUCA genome 完全再構成 (in silico)** | 2030 | 0.55 |
| Asgardarchaea-eukaryote 直接祖先関係確定 | 2028 | 0.65 |
| Cryosphere microbial dark matter 主要 phyla 同定 | 2030 | 0.60 |
| **CPR cell culture 確立** | 2028 | 0.50 |
| 海洋 OTU 数 > 100 万 確定 | 2030 | 0.70 |

---

📄 **論文 (Tier 1 #27)**: 10.5281/zenodo.20256555

> Phase 193 で Bacteriophage + Phage Therapy + CRISPR 起源 へ進みます。

#情報理論的統一理論 #ITU #微生物学 #系統発生 #16SrRNA #LUCA #Woese #TreeOfLife #K_phylogeny #Phase192
