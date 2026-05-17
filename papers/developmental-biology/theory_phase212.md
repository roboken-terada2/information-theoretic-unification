# Phase 212: Aging Deepening + Telomere + Senescence ― K_dev_aging ★ (#6 link)

Phase 211 で K_dev_stem の organoid + 再生を確立。Phase 212 では **老化生物学の深掘り** ― テロメア + cellular senescence + senolytics + 老化 hallmarks ― を扱い、**K_dev_aging** を ITU の "K-state 劣化フロー" として定式化します。Tier 1 #6 Aging (Phase 63-66) の continuation。

## Hallmarks of Aging (López-Otín 2013, 2023) ★

```
2013: López-Otín "The Hallmarks of Aging" (Cell, 6500+ citations)
2023: 改訂版 (12 hallmarks)
```

### 12 Hallmarks (2023 改訂)

| # | Hallmark | 概要 |
|---|---|---|
| 1 | Genomic instability | DNA 損傷蓄積 |
| 2 | **Telomere attrition** | テロメア短縮 |
| 3 | Epigenetic alterations | DNAm shift |
| 4 | Loss of proteostasis | タンパク質品質低下 |
| 5 | Disabled macroautophagy | autophagy 不全 |
| 6 | Deregulated nutrient sensing | mTOR/IGF1 |
| 7 | **Mitochondrial dysfunction** | ROS + ATP 低下 |
| 8 | **Cellular senescence** | 細胞老化 |
| 9 | **Stem cell exhaustion** | 幹細胞枯渇 (Phase 211 link) |
| 10 | Altered intercellular communication | 細胞間通信 |
| 11 | Chronic inflammation | "inflammaging" |
| 12 | Dysbiosis | マイクロバイオーム変化 (Phase 195 link) |

## Telomere shortening (Blackburn-Greider-Szostak Nobel 2009) ★

### テロメア構造

```
真核生物の染色体末端: TTAGGG 反復配列
ヒト出生時: 8-15 kb
50 cell division で 50-150 bp 短縮 / division
↓
Hayflick limit (1961): 体細胞は 50 cell divisions で複製停止
↓ "Mortal" cells
```

### テロメラーゼ (Telomerase)

```
Greider-Blackburn 1985: Tetrahymena で TERT 同定
↓ RNA template (TERC) + reverse transcriptase (TERT)
↓ テロメア伸長

発現:
  生殖細胞: 高発現 (immortal)
  幹細胞:   中等度
  体細胞:   低/ゼロ → 老化
  がん細胞: 80-90% で再活性化 → immortal
↓
2009 Nobel: Blackburn + Greider + Szostak
```

### テロメア関連疾患

```
Dyskeratosis congenita: TERC/TERT 変異
   早老症 + 骨髄不全 + 肺線維症
Idiopathic pulmonary fibrosis: テロメア短縮患者で 30%
```

## Cellular Senescence

### Hayflick limit (1961)

```
Leonard Hayflick: ヒト fibroblast in vitro
↓ 50 divisions で増殖停止
↓ "Senescent" 細胞は代謝活性維持するが分裂しない
↓ Originally controversial (1961-80s)
```

### SASP (Senescence-Associated Secretory Phenotype, Campisi 2008)

```
老化細胞 = 分裂停止 + SASP
↓ IL-6, TNF-α, MMP, growth factors を分泌
↓ 周辺組織に inflammaging 誘導
↓ がん細胞の浸潤促進 (paradox)
```

### Senolytics: 老化細胞除去療法 ★

```
2015: Mayo Clinic - Senolytics drug class 確立 (Zhu, Tchkonia, Kirkland)
↓
Dasatinib + Quercetin (D+Q): 第 1 世代 senolytic
↓ マウス実験で healthspan 30% 延長
↓
Phase II 試験 (2020-2024):
   - 高齢者 + chronic kidney disease
   - Alzheimer's (TauX therapy)
   - Pulmonary fibrosis (IPF)
↓
2024: 結果まだ mixed, 期待続く
```

## Yamanaka factors と若返り (rejuvenation)

### Partial reprogramming (Ocampo 2016, Salk) ★

```
Ocampo, Belmonte (Salk Institute) 2016 Cell:
↓ 4 因子 OSKM を一過性発現 (full iPS 化させず)
↓ マウス老化マーカー (DNAm age, senescence) 改善
↓ Progeria マウス寿命 30% 延長 ★
↓
"Yamanaka 部分リプログラミング" は老化を逆転可能?
```

### Altos Labs (2022-) - 100 億ドル創業 ★

```
2022 1月: Altos Labs 発表 (Jeff Bezos + Yuri Milner 投資 $3.0B)
   - CEO: Hal Barron (前 GSK)
   - Chief Scientist: Rick Klausner
   - Yamanaka, Ocampo, López-Otín, Belmonte 招聘
↓
Mission: "Restore cell health and resilience"
↓
2024: Phase I trial 開始予定
```

### Calico Labs (Google 2013-)

```
$1B+ 投資, Hal Barron(前) + Cynthia Kenyon (前)
2024: Naked mole rat (32 yr 寿命) ゲノミクス
       AbbVie 共同で drug pipeline
       実用化はまだ
```

## ITU 視点: K_dev_aging の構造

```
K_dev_aging^(0) = -log P(cell state | chronological age, cumulative damage)

軸:
  Damage accumulation (DNA + protein + lipid)
  Telomere length (DNA template integrity)
  Epigenetic age (DNAm, Horvath clock)
  Senescent cell fraction (SASP burden)
  Stem cell pool (regenerative capacity)
```

### Aging = K_dev "reversal" (Phase 207 双対)

```
Phase 207 (発生): zygote → 200 cell types  (S↓, ⟨K⟩↓: 専門化)
Phase 212 (老化): cell types → senescent / death (S↓, ⟨K⟩↑: 劣化)
↓
両者とも δS < 0 だが:
  発生: ⟨K_dev_lineage⟩ ↓ (情報的選択)
  老化: ⟨K_dev_aging⟩  ↑ (情報的損失)
⇒ 異なる sub-K_state での descent
⇒ Yamanaka rejuvenation = K_dev_aging を reverse
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Hayflick limit (1961)** | **~50 divisions** ✓ |
| ヒト出生時テロメア | 8-15 kb ✓ |
| 1 cell division 短縮 | 50-150 bp ✓ |
| **Blackburn-Greider-Szostak Nobel** | **2009** ✓ |
| Horvath clock 精度 | ±3-5 年 ✓ (Horvath 2013) |
| **D+Q senolytic マウス healthspan** | **30% 延長** ✓ |
| **Ocampo partial reprogramming** | progeria 30% 延長 ✓ |
| Altos Labs 投資額 | **$3.0 B** (2022) ✓ |
| ヒト最大寿命 (Calment) | 122 年 (1997) |
| Naked mole rat 寿命 | 32 年 (ラット 10× 同サイズ) ✓ |
| **ITU axiom: aging** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Senolytics FDA 承認 (1 適応)** | 2028 | 0.65 |
| **Partial reprogramming 臨床試験 (Altos)** | 2030 | 0.70 |
| Healthspan extension 5+ years (population trial) | 2035 | 0.45 |
| **Horvath clock 標準化 (clinical)** | 2028 | 0.75 |
| Human max lifespan > 130 years | 2050 | 0.30 |

---

📄 **論文 (Tier 1 #29)**: 10.5281/zenodo.20257271

> Phase 213 で Birth Defects + Teratology + Epigenetics へ進みます。

#情報理論的統一理論 #ITU #発生生物学 #老化 #テロメア #Senescence #LopezOtin #BlackburnGreiderSzostak #Yamanaka #AltosLabs #K_dev_aging #Phase212
