# Phase 208: Cell Differentiation + Waddington + Yamanaka iPSC ― K_dev_lineage ★

Phase 207 で K_dev 全体像と 45 doublings 細胞数増殖を確立。Phase 208 では **細胞分化** の中核 ― Waddington 風景 + Yamanaka iPSC (Nobel 2012) ― を扱い、**K_dev_lineage** を ITU の "分化軌跡 K-state" として定式化します。

## Waddington epigenetic landscape (1957) ★

```
Conrad Waddington "The Strategy of the Genes" (1957):
↓ 細胞分化 = "ボール" が傾斜地形を転がる過程
↓ 谷 = 細胞型 attractor
↓ 山 = 遷移エネルギー障壁
↓ 分岐点 = canalization 分かれ目
```

### Waddington landscape の現代化

```
古典 Waddington (1957): 隠喩的
↓
Kauffman boolean network (1969): 遺伝子調節ネットワーク
↓
Wang potential landscape (2008): Hopfield-like energy
↓
Single-cell RNA seq + RNA velocity (La Manno 2018):
   ★ 個別細胞の動的経路を実測可能 ★
↓
Pseudotime ordering (Trapnell Monocle 2014, Diffusion map)
```

## Yamanaka iPSC (2006, Nobel 2012) ★

```
Shinya Yamanaka 山中伸弥 (Kyoto):
↓ "Could differentiated cells be reprogrammed to pluripotent state?"
↓ 24 candidate genes をスクリーニング
↓ ↓
4 因子で十分: Oct3/4, Sox2, Klf4, c-Myc
↓ "Yamanaka factors" (OSKM) ★
↓
体細胞 (fibroblast) → iPS cell (induced pluripotent stem cell)
↓ Nobel 2012 (Gurdon と共同, 体細胞核移植 + iPS)
```

### Yamanaka factor 4 つの役割

| 因子 | 機能 |
|---|---|
| **Oct3/4 (POU5F1)** | Master pluripotency regulator |
| **Sox2** | Pluripotency 維持 |
| **Klf4** | Self-renewal + tumor suppressor |
| c-Myc | Proliferation (発がん性, 後に省略可能) |

### Yamanaka 以降の応用 (2007-2024)

```
2007: ヒト fibroblast → iPS 確立
2013: 高橋政代 黄斑変性 iPS-RPE 移植 (世界初臨床) ★
2018: Parkinson disease iPS-dopamine 細胞 治験 (京都大)
2024: 心臓再生 iPS-cardiomyocyte sheet 治験
↓
将来: 心筋, 神経, β細胞, 軟骨, 等の再生医療
```

## 細胞リプログラミング技術 (Yamanaka 後)

| 方法 | 担い手 | 効率 |
|---|---|---|
| **iPS (OSKM)** | 4 transcription factor | 0.01-0.1% (低) |
| **mRNA delivery** | non-integrating, 安全 | 1-2% |
| Sendai virus | non-integrating, RNA virus | 0.1-1% |
| Episomal plasmid | 一過性 DNA | 0.01% |
| Small molecules (CiPS) | 化学物質のみ (Deng 2013) | 0.001% |
| **Direct conversion** | Lineage 直接変換 | 1-5% |

### Direct conversion 例 (Wernig 2010)

```
Fibroblast → Neuron (iN cells, 3 TF)
Fibroblast → Cardiomyocyte (3 TF + cocktail)
Astrocyte → Neuron (in situ, AD治療候補)
↓
Waddington landscape の "横移動" (山越え)
```

## ITU 視点: K_dev_lineage の構造

```
K_dev_lineage^(0) = -log P(cell type t+1 | cell type t, signal)
                  = 分化軌跡の情報的選択

Waddington 風景:
  低い谷 (low ⟨K⟩) → 細胞型 attractor
  高い山 (high ⟨K⟩) → 遷移バリア
↓
ITU 視点:
  分化 = ⟨K⟩ 局所最小化方向への自然降下
  iPS リプログラミング = 強制的 ⟨K⟩ 上昇 (人工 lifting)
                       → 山頂 (Pluripotent) へ戻す ★
```

### Yamanaka 因子 = ITU "lifting operators"

```
分化進行: K_dev_lineage^(0) descent (自然)
iPS:    K_dev_lineage^(0) anti-descent (人工 OSKM 入力)

⇒ 細胞運命可逆性の証明 (Yamanaka 2006)
⇒ ITU 視点では energy injection by external operators
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Yamanaka 4 因子** | OSKM ✓ (Nobel 2012) |
| iPS reprogramming 効率 | **0.01-0.1%** (OSKM virus) ✓ |
| mRNA-based iPS 効率 | 1-2% (Warren 2010) |
| iPS 確立期間 | **3-4 週間** |
| iPS の分化能 | All 3 germ layers ✓ |
| 高橋政代 RPE 移植 | **2013 世界初** ✓ |
| ヒト ES cells (Thomson 1998) | 7 日で iPS と同等 |
| ヒト体細胞 → 神経 (iN) 効率 | 5-20% (Wernig 2010) |
| **ITU axiom: differentiation vs reprogramming** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **iPS-derived β細胞 1型糖尿病治療承認** | 2030 | 0.70 |
| **iPS 心筋シート 心不全治療承認** | 2030 | 0.65 |
| **In vivo direct reprogramming 臨床** | 2032 | 0.55 |
| Universal iPS bank (HLA-matched, 50 lines) | 2028 | 0.75 |
| **AI-designed reprogramming factor (Yamanaka 5.0)** | 2030 | 0.50 |

---

📄 **論文 (Tier 1 #29)**: 10.5281/zenodo.20257271

> Phase 209 で Body Axis + Hox + Segmentation へ進みます。

#情報理論的統一理論 #ITU #発生生物学 #Waddington #Yamanaka #iPSC #Nobel2012 #高橋政代 #K_dev_lineage #Phase208
