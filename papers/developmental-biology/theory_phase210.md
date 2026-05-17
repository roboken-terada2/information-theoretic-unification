# Phase 210: Morphogen Gradients + Turing Pattern + Organogenesis ― K_dev_morphogen ★

Phase 209 で K_dev_spatial の体軸 + Hox を確立。Phase 210 では **モルフォゲン勾配** + **Turing パターン形成** + **器官形成** を扱い、**K_dev_morphogen** を ITU の "化学パターン → 細胞運命" 変換 K-state として定式化します。

## モルフォゲン (Morphogen) 概念

### Wolpert "French flag model" (1969) ★

```
Lewis Wolpert (UCL):
↓ "Positional information" 概念
↓ Morphogen の濃度勾配
↓ Threshold-based 細胞応答 → French flag pattern (青/白/赤)
↓ "How does a cell know where it is?"
```

### 主要 morphogen (5 シグナリング pathway)

| Morphogen | Pathway | 機能 |
|---|---|---|
| **Sonic Hedgehog (Shh)** | Hedgehog | Neural tube ventral, limb anterior-posterior |
| **BMP** | TGF-β | DV axis, bone formation |
| **Wnt** | Wnt/β-catenin | AP axis, gastrulation |
| **FGF** | RTK | Limb outgrowth, lung branching |
| **Retinoic acid (RA)** | Nuclear receptor | Hindbrain, limb |

### Bicoid in Drosophila (1988) ★

```
Driever-Nüsslein-Volhard 1988 Cell:
↓ Bicoid mRNA は卵の前端に局在
↓ 翻訳後タンパクが exponential gradient 形成 (拡散)
↓ "Anterior morphogen" 最初の同定

数式: c(x, t) = c_0 · exp(-x/λ),  λ = √(D/k_deg)
     λ ≈ 100 μm (Drosophila egg 500 μm の 20%)
```

## Turing pattern (1952) ★

### Turing "The Chemical Basis of Morphogenesis" (1952)

```
Alan Turing (1952 Phil. Trans. R. Soc. B):
↓ 数学的に "自発的パターン形成" を予測
↓ 2 つの拡散物質 (activator + inhibitor)
↓ Reaction-diffusion equation:
   ∂u/∂t = D_u ∇²u + f(u, v)
   ∂v/∂t = D_v ∇²v + g(u, v)
↓ Diffusion-driven instability:
   D_v >> D_u + reaction kinetics → stripes/spots/labyrinths
```

### Turing pattern の生物実例

| パターン | 生物 | Activator/Inhibitor |
|---|---|---|
| Zebrafish stripes | Kondo-Asai 1995 | Mela-Iri Notch |
| Cheetah spots | (predicted) | (RDE simulation match) |
| Hair follicle distribution | mouse | WNT/DKK |
| **Fingerprints** | human | BMP/EDAR/WNT |
| Limb digit pattern | mouse | Sox9/BMP (Sheth 2012 Science) |

### Kondo-Asai (1995 Nature) ★

```
角の魚 (Pomacanthus) で stripes 動的形成を観察
↓ 成長中に stripes が動的に rearrange
↓ Turing prediction と完全一致 ★
↓ "Turing pattern" の最初の動物例
```

## Organogenesis: 主要器官形成

### 心臓 (Heart)

```
Day 17-18: Cardiac progenitor (mesoderm)
Day 22: 拍動開始 (Heart beat) ★
Day 28: 心臓形成完了 (4 房 + 大血管)
↓
先天性心疾患 (CHD): 出生児の 1%
↓ Tetralogy of Fallot, VSD, ASD, など
```

### 神経管 (Neural tube)

```
Day 18: 神経板 (neural plate) 形成
Day 22: 神経管閉鎖 (anterior + posterior neuropore)
↓
Neural tube defect (NTD): 1-2/1000 出生
↓ Anencephaly, Spina bifida
↓ Folate 葉酸補充で 70% 予防 (MRC trial 1991)
```

### 肺 (Lung)

```
Branching morphogenesis: 23 世代の二分岐
   気管 → 主気管支 → 細気管支 → 終末細気管支 → 肺胞
↓ ~5 億 alveoli per lung
↓ FGF10 + Shh feedback で fractal-like 分岐
```

## ITU 視点: K_dev_morphogen の構造

```
K_dev_morphogen^(0) = -log P(cell fate | morphogen concentration c(x))

軸:
  c (concentration): morphogen 局所値
  T (threshold): 細胞応答閾値
  τ (time): exposure duration

⇒ 細胞は c が threshold を超えた時間で運命決定
   ("temporal integration", Briscoe 2007)
```

### Reaction-diffusion = ITU 動的展開

```
∂ρ/∂t = D ∇²ρ + f(ρ, K^(0))

⇒ K^(0) が空間勾配を駆動
⇒ Turing instability = K-state symmetry breaking
⇒ ITU descent flow が "パターン" を生成
```

### French flag model の ITU 解釈

```
1 morphogen + 2 thresholds → 3 細胞集団 (3 fates)
S(initial) = log 3 ≈ 1.10 nats  (3 fates 均等候補)
S(after morphogen) = 0 (各細胞が確定運命)
δ⟨K⟩ < 0 (threshold-based 確定)
ratio = 1 (ITU axiom 厳密)
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| **Bicoid gradient λ (Drosophila)** | **~100 μm** ✓ |
| Bicoid 拡散係数 D | 0.3 μm²/s |
| Bicoid 半減期 | 50 分 |
| **Turing 1952 提唱** | morphogenesis 化学基盤 ✓ |
| **Kondo-Asai 1995 zebrafish** | Turing 動物初例 ✓ |
| 心拍開始日 | **D22** ✓ |
| 肺 branching 世代数 | **23** ✓ |
| 肺胞総数 (1 肺) | 3-5 億 |
| 葉酸 NTD 予防効果 | **70%** (MRC 1991) ✓ |
| **ITU axiom: morphogen patterning** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| **3D 器官 organoid (kidney/heart/lung) 機能完全** | 2030 | 0.70 |
| **Synthetic morphogen system** in iPS culture | 2028 | 0.65 |
| Limb regeneration in mammals via Turing patch | 2035 | 0.30 |
| **Fingerprint mathematical prediction** validated | 2028 | 0.75 |
| Synthetic embryo → bilaterian gastruloid | 2030 | 0.65 |

---

📄 **論文 (Tier 1 #29)**: 10.5281/zenodo.20257271

> Phase 211 で Stem Cells + Organoids + Regeneration へ進みます。

#情報理論的統一理論 #ITU #発生生物学 #Morphogen #Wolpert #Turing #Bicoid #KondoAsai #Organogenesis #K_dev_morphogen #Phase210
