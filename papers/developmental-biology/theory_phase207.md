# Phase 207: Tier 1 #29 開幕 ― 発生生物学への進撃、Zygote → Embryo + K_dev (Block B 4/?)

Phase 199-206 で Tier 1 #28 Neuroscience 完成、K_neuro 8 sub-state を確立。Phase 207 から **Tier 1 #29 Developmental Biology** (Block B 4/?) を開幕 ― 1 細胞 (zygote) から 37 兆細胞のヒトへ ― を扱い、**K_dev** を ITU の "時空間情報展開" K-state として定式化します。

## なぜ発生生物学が Block B 4/? か

1. **生命の情報展開最深部**: 1 細胞 → 37 兆細胞 (10¹³ × 増殖)
2. **時空間 K-state の動的構築**: 時間 (胚日) × 空間 (体軸) × 細胞種 (200+)
3. **#26 Immune + #27 Microbe + #28 Neuro との連携**: 免疫細胞分化, 微生物コロニー化, 神経発生
4. **遺伝学 (#30) との橋渡し**: 遺伝子発現プログラム
5. **#6 Aging と双対**: 発生 (構築) ↔ 老化 (劣化)
6. **臨床応用**: 再生医療, organoid, 先天異常

## 受精から胚盤胞へ (ヒト)

```
受精 (Day 0):           精子 + 卵子 → 1 細胞 zygote
分割 (cleavage):        Day 1-3, 2 → 4 → 8 cells (totipotent)
桑実胚 (morula):        Day 3-4, 16-32 cells
胚盤胞 (blastocyst):    Day 5-6, 128 cells
   ├── 内細胞塊 (ICM) → 胚体 + ES cells 起源
   └── 栄養外胚葉 (trophoblast) → 胎盤
着床 (implantation):    Day 6-10
原腸形成 (gastrulation): Day 14-18, 3 胚葉確立 ★
```

### 3 胚葉 (Germ Layers)

| 胚葉 | 由来組織 |
|---|---|
| **Ectoderm** (外胚葉) | 神経系, 表皮, 感覚器 |
| **Mesoderm** (中胚葉) | 筋, 骨, 心血管, 腎, 性腺 |
| **Endoderm** (内胚葉) | 消化管, 肺, 肝, 膵 |

= **ITU 視点: K_state 3 主軸への初期分岐** ★

## 細胞数の指数増加 (ヒト)

```
Day 0:    1 cell
Day 6:    128 cells (blastocyst)
Day 14:   ~10⁴ cells (gastrulation 開始)
Week 8:   ~10⁹ cells (organogenesis 完了)
Week 38:  ~10¹² cells (出生)
成人:     ~3.7×10¹³ cells
```

= **約 45 cell division** (1 zygote → 成人, double 約 45 回)

## ITU 視点: K_dev の構造

```
K_dev^(0) = -log P(cell type | spatiotemporal coordinate, genotype)
          = 発生情報展開ポテンシャル

軸:
  t : 発生時間 (受精後日数, fertilization day)
  x : 空間座標 (体軸, anterior-posterior + dorsal-ventral + left-right)
  s : 細胞状態 (遺伝子発現プロファイル)
  g : ゲノム (遺伝子 - 不変)

K_dev = K_dev_temporal ⊕ K_dev_spatial ⊕ K_dev_lineage
      ⊕ K_dev_morphogen ⊕ K_dev_stem ⊕ K_dev_organoid
      ⊕ K_dev_aging ⊕ K_dev_teratology (8 sub-states)
```

### Cell potency 階層

| 段階 | 能力 | 細胞例 |
|---|---|---|
| **Totipotent** | 全能 (胎盤含む全細胞へ) | Zygote, 2-cell embryo |
| **Pluripotent** | 多能 (3 胚葉全て) | ICM, ES cells, iPS cells |
| **Multipotent** | 多分化 (1 lineage 内) | HSC (造血), NSC (神経) |
| **Oligopotent** | 数細胞種 | Myeloid progenitor |
| **Unipotent** | 単一分化 | Satellite cell, spermatogonia |

= **K_dev^(0) descent flow = 細胞分化 = 情報損失の連鎖** ★

## ITU axiom と細胞分化

```
受精卵: 最大 S (全細胞種潜在)
↓ 分化進行
↓
最終分化細胞: 最小 S (1 細胞種 fix)

δS_lineage(t) < 0  (時間の単方向情報損失)
δ⟨K_dev⟩(t) < 0  (専門化進行)
ratio = 1 (ITU axiom 厳密)
```

## Phase 207 数値検証目標

| 量 | 期待値 |
|---|---|
| 受精〜出生 cell division 数 | **~45 doublings** ✓ |
| ヒト成人 細胞数 | **3.7×10¹³** (Bianconi 2013) |
| 胚盤胞細胞数 | 128 (Day 5-6) |
| 細胞種数 (ヒト) | ~200-400 (broad), ~700 (細分) |
| Cleavage 周期 | 約 24 hr |
| 妊娠期間 | 38 週 (266 日) |
| **ITU axiom: cell potency descent** | δS/δ⟨K⟩ ≈ 1 |

## Phase 207-214 ロードマップ (Tier 1 #29)

| Phase | テーマ |
|---|---|
| **207 (本)** | **Zygote → Embryo + K_dev 導入 + 3 胚葉** |
| 208 | Cell differentiation + Waddington + Yamanaka iPSC |
| 209 | Body axis + Hox genes + segmentation |
| 210 | Morphogen gradients + Turing + organogenesis |
| 211 | Stem cells + Organoids + Regeneration |
| 212 | Aging deepening + telomere + senescence (#6 link) |
| 213 | Birth defects + teratology + epigenetics |
| 214 | 統合 + 29-vertex polytope + Pass-1 97.3% |

---

📄 **論文 (Tier 1 #29)**: 10.5281/zenodo.20257271

> Phase 208 で Cell differentiation + Waddington + Yamanaka iPSC へ進みます。

#情報理論的統一理論 #ITU #発生生物学 #Tier1_29 #Zygote #Gastrulation #3胚葉 #K_dev #Phase207
