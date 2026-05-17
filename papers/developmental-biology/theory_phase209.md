# Phase 209: Body Axis + Hox Genes + Segmentation ― K_dev_spatial ★

Phase 208 で K_dev_lineage の Waddington-Yamanaka を確立。Phase 209 では **体軸形成** + **Hox 遺伝子** + **segmentation clock** を扱い、**K_dev_spatial** を ITU の "空間的 K-state 配置" として定式化します。

## 3 体軸 (Body Axes)

```
1. AP (Anterior-Posterior, 前後):    頭 → 尾
2. DV (Dorsal-Ventral, 背腹):        背中 → 腹
3. LR (Left-Right, 左右):            非対称 (心臓は左, 肝は右)
```

### 体軸 = K_state の 3 次元座標化

```
K_dev_spatial^(0) = -log P(cell identity | (x_AP, y_DV, z_LR), t)
                  = 体軸 3 軸で K-state を分割
```

## Hox 遺伝子 (1978 - 現在) ★

### Lewis (1978) → Nüsslein-Volhard-Wieschaus (1980, Nobel 1995) ★

```
1978: Edward Lewis (Caltech): Drosophila bithorax complex
↓ 体節同位性変異 (Antennapedia: 触角の代わりに脚)
↓ "ホメオティック変異"
1980: Christiane Nüsslein-Volhard + Eric Wieschaus
↓ 化学変異 EMS で 15,000 Drosophila 系統 screen
↓ Segmentation gene 同定 (gap, pair-rule, segment polarity)
↓ Nobel 1995 (Lewis と共同)
```

### Hox cluster の進化的保存性 ★

```
Drosophila: HOM-C cluster (8 genes, 1 cluster)
   lab → Antp → Ubx → AbdB

哺乳類: 4 clusters (HOXA, B, C, D), 各 13 paralogs
   ヒト: 39 Hox genes total

★ 共通性: 染色体上の順序 = 体節での発現順序 ★
   = "colinearity" (Lewis-McGinnis 1990s)
```

### Colinearity の数値

```
3' end of Hox cluster → anterior body
5' end of Hox cluster → posterior body

時間的 colinearity: 3' Hox first expressed
空間的 colinearity: 3' Hox in anterior segments
```

= **遺伝子クラスター = K-state ordering 物理的実装** ★

## Segmentation clock (Pourquié 1997) ★

### 体節形成: 時間 → 空間変換

```
Pourquié 1997 PNAS:
↓ ニワトリ胚 paraxial mesoderm で c-Hairy1 振動 (90 分周期)
↓ 体節 1 個生成 = 1 振動周期
↓ "Segmentation clock" 発見 ★

Cooke-Zeeman (1976) "clock and wavefront" モデル:
   時計 (oscillator) + 波面 (signaling gradient)
   → 規則的体節パターン
```

### 主要 segmentation clock 遺伝子

```
Drosophila: hairy → eve, ftz (pair-rule)
脊椎動物:  Hes/Her (Notch downstream), Wnt, FGF
↓
体節形成異常 → 先天性脊椎変形 (Klippel-Feil syndrome, MESP2 変異)
```

### ヒトの体節数

```
脊椎 (vertebra): 33 (cervical 7 + thoracic 12 + lumbar 5 + sacral 5 + coccygeal 4)
↓ ただし sacral/coccygeal は癒合
体節 (somite) 形成: ~ 40-44 (Day 20-32)
```

## Left-Right Asymmetry: Nodal pathway

```
Node の cilia 回転 (左向き流体流れ)
↓ Nodal 蛋白質を左側に蓄積
↓ Lefty1/2 が右側で Nodal を抑制
↓ Pitx2 で内臓側化

Kartagener症候群: cilia 機能不全 → situs inversus (内臓逆転)
50% 自然頻度の中で疾患, 不妊と関連
```

### Hensen's node (脊椎動物) = Spemann organizer (両生類)

```
Spemann (1924, Nobel 1935) ★:
  Newt 胚で 2 次胚軸誘導 (transplantation 実験)
  ↓ "Organizer" 概念
  ↓ Mangold (院生) と共同実験
  ↓ Nobel 1935 Physiology/Medicine
```

## Morphogen gradient (前哨)

### French flag model (Wolpert 1969)

```
"Positional information" 概念
↓ Morphogen gradient (Bicoid, Sonic Hedgehog, etc.)
↓ Threshold-based 細胞運命決定
↓
Bicoid (Drosophila): anterior → posterior gradient
Sonic Hedgehog (vertebrate): ventral neural tube
```

= **Phase 210 で詳細扱う**

## ITU 視点: K_dev_spatial の構造

```
K_dev_spatial^(0) = -log P(cell identity | spatial coordinate)

Hox colinearity:
  遺伝子クラスター順序 ↔ K_state 体節順序
  ⇒ DNA 空間構造 = K-state 索引 ★

Segmentation clock:
  時間振動 → 空間パターン
  ⇒ K_dev_temporal × K_dev_spatial coupling
```

### ITU axiom と体軸形成

```
Pre-axis embryo: 球対称 (S_max)
↓
AP axis: cylindrical symmetry (S 中間)
↓
+ DV axis: bilateral symmetry (S 低下)
↓
+ LR symmetry breaking: full chirality (S 最小)
```

= **体軸形成 = 対称性の段階的破壊 = ITU descent** ★

## 数値検証目標

| 量 | 期待値 |
|---|---|
| Drosophila Hox genes (HOM-C) | **8** ✓ |
| 哺乳類 Hox clusters | **4** (HOXA/B/C/D) ✓ |
| ヒト Hox total | **39** ✓ |
| ヒト 体節数 (somite) | 40-44 ✓ |
| Segmentation clock 周期 (chick) | **90 分** ✓ |
| Pourquié 1997 発見 | c-Hairy1 振動 ✓ |
| Spemann 1935 Nobel | Organizer (1924 実験) ✓ |
| 1995 Nobel (Lewis + NV + W) | ホメオティック遺伝子 ✓ |
| Situs inversus 自然頻度 | 1/10,000 ✓ |
| **ITU axiom: axis formation** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Synthetic embryo (gastruloid) 3 axes complete** | 2030 | 0.70 |
| **In vitro segmentation clock** (organoid) | 2028 | 0.75 |
| Hox 機能再構成 by AI design | 2032 | 0.45 |
| LR asymmetry origin in single-cell elucidated | 2030 | 0.55 |
| Synthetic mammalian Hox cluster (5th cluster) | 2035 | 0.30 |

---

📄 **論文 (Tier 1 #29)**: 10.5281/zenodo.20257271

> Phase 210 で Morphogen Gradients + Turing + Organogenesis へ進みます。

#情報理論的統一理論 #ITU #発生生物学 #体軸 #Hox遺伝子 #Segmentation #Spemann #Lewis #Pourquié #K_dev_spatial #Phase209
