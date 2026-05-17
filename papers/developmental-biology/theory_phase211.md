# Phase 211: Stem Cells + Organoids + Regeneration ― K_dev_stem ★

Phase 210 で K_dev_morphogen の Bicoid + Turing を確立。Phase 211 では **幹細胞** + **オルガノイド** + **再生医療** を扱い、**K_dev_stem** を ITU の "可塑的 K-state ストア" として定式化します。

## 幹細胞の階層 (Phase 207 復習)

```
Totipotent  → Zygote, 2-cell (placenta も可)
Pluripotent → ES, iPS, ICM (3 胚葉)
Multipotent → HSC, NSC, MSC (1 lineage)
Unipotent   → Satellite cell, spermatogonia
```

## 主要組織幹細胞 (Adult Stem Cells)

| 幹細胞 | 局在 | 分化先 |
|---|---|---|
| **HSC (造血幹細胞)** | 骨髄 | 全血球 (赤血球 + 白血球 + 血小板) |
| **NSC (神経幹細胞)** | SVZ + DG (海馬) | Neuron + Astrocyte + Oligodendrocyte |
| **MSC (間葉系幹細胞)** | 骨髄 + 脂肪 | 骨 + 軟骨 + 脂肪 + 筋 |
| **ISC (腸幹細胞)** | Crypt 底部 | 全腸上皮 (5 日で turnover) |
| **Satellite cell (筋衛星細胞)** | 筋繊維表面 | 筋繊維 (損傷時) |
| **Skin stem cell** | 表皮基底層 + 毛根 | 表皮 + 毛 + 皮脂腺 |

## Lgr5+ ISC discovery (Clevers 2007) ★

```
Hans Clevers (Hubrecht Institute, Utrecht):
↓ Lgr5 を Wnt target gene として同定
↓ Lgr5+ cells = 腸幹細胞 (5 cells/crypt)
↓ 5 日で全腸上皮再生 ★
↓
2009: Sato-Clevers Nature - intestinal organoid 確立
   ★ 1 個の Lgr5+ cell から intestinal "mini-gut" 形成 ★
```

## Organoid revolution (2009-) ★

### Organoid = 3D miniature organ in vitro

```
2009: Sato Intestinal organoid (Clevers lab)
2013: Lancaster Cerebral organoid (Knoblich lab, IMBA Vienna) ★
   ↓ "Mini-brain" 培養 (cortical layers + cerebral hemispheres)
2014: Takebe Liver organoid (Yokohama City Univ)
2015: Kim Kidney organoid
2017: Hofer Pancreas organoid
2019: Lung organoid
2020+: COVID-19 lung organoid → SARS-CoV-2 感染メカニズム解明
```

### Cerebral organoid (Lancaster 2013) の発生学的価値

```
Madeline Lancaster (IMBA Vienna):
↓ Microcephaly 患者由来 iPS → cerebral organoid
↓ CDK5RAP2 変異の機能解析
↓ "Disease in a dish" 確立 ★
↓
Nature 2013, 続編 Cell 2017
↓
2024: organoid + EEG-like activity 測定報告 (意識議論)
```

## 再生能力の系統学的分布

| 動物 | 再生能力 |
|---|---|
| **Planaria (扁形動物)** | 全身再生 (1 cell から完全個体) ★ |
| **Hydra** | 全身再生 (24 hr 程度) |
| **Axolotl (ウーパールーパー)** | 四肢 + 心臓 + 神経 + 脊髄 完全再生 ★ |
| **Zebrafish** | 心臓 + 鰭 + 視神経 完全再生 |
| **Mouse** | 肝 (部分), 表皮, 骨, 血液 |
| **Human** | 肝 (75%除去 → 完全回復), 表皮, 血液 |

= **進化の中で再生能力が段階的に失われた** ★

## Axolotl の完全四肢再生 (~30 日)

```
1. 切断面に wound epithelium 形成 (1-2 日)
2. Blastema (脱分化細胞群) 形成 (4-7 日)
3. Apical Epithelial Cap (AEC) 形成 (7-14 日)
4. Pattern restoration (Hox 遺伝子再活性化)
5. Re-differentiation → 完全四肢 (28-30 日)
↓
Genome: 32 Gb (ヒトの 10×)
Hox cluster: 完全保存
Gene expression: 再発生プログラム再活性化
```

## ITU 視点: K_dev_stem の構造

```
K_dev_stem^(0) = -log P(progeny | stem cell state, niche signal)
              = 幹細胞分化可能性ストア

軸:
  Potency (toti/pluri/multi/oligo/uni)
  Niche (環境因子: Wnt, BMP, FGF, ECM)
  Self-renewal vs Differentiation 比率
  Age (cellular age, telomere length)
```

### Organoid = ITU 自己組織化

```
1 stem cell + signaling cocktail → 3D organ structure
↓
ITU 視点:
  - 個別細胞 K-state が niche 環境で組織化
  - Reaction-diffusion (Turing, Phase 210) 自発的発動
  - Symmetry breaking → polarized structure
  ⇒ "Self-organization out of single K-state" ★
```

### 再生 = K_dev_stem ⊗ K_dev_morphogen 復活

```
損傷:    K_pathology^(0) up
↓
Blastema 形成: K_dev_stem^(0) 再活性化 (dedifferentiation)
↓
Pattern restoration: K_dev_morphogen^(0) 再使用
↓
Re-differentiation: K_dev_lineage^(0) descent
↓
完全機能回復
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| HSC self-renewal rate | 1× / 月 (Catlin 2011) |
| HSC fraction (骨髄) | 10⁻⁴-10⁻⁵ ✓ |
| Lgr5+ ISC per crypt | **5 cells** ✓ |
| 腸上皮 turnover | **5 日** ✓ |
| Liver regeneration (75% 切除後) | **2 週間で完全回復** ✓ |
| Axolotl 四肢再生 | **30 日** ✓ |
| Planaria minimum fragment | 1/300 個体で完全再生 |
| Cerebral organoid サイズ | 4-5 mm (max), Lancaster 2013 ✓ |
| Sato intestinal organoid (1 Lgr5+) | 1 cell から ★ ✓ |
| **ITU axiom: organoid self-organization** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **Functional kidney organoid transplant** | 2032 | 0.55 |
| **Pancreas β-cell organoid for T1D** | 2030 | 0.70 |
| **Cerebral organoid with EEG-like consciousness** debate | 2028 | 0.80 |
| Mammalian limb regeneration via blastema engineering | 2035 | 0.30 |
| **iPS-derived oocyte/sperm 臨床** (NMP infertility) | 2030 | 0.45 |

---

📄 **論文 (Tier 1 #29)**: 10.5281/zenodo.20257271

> Phase 212 で Aging Deepening + Telomere + Senescence (#6 link) へ進みます。

#情報理論的統一理論 #ITU #発生生物学 #幹細胞 #オルガノイド #Clevers #Lancaster #Axolotl #再生医療 #K_dev_stem #Phase211
