# Phase 185: MHC + Antigen Presentation + Peptide-MHC Binding ― K_MHC 深掘り

Phase 184 で TCR/BCR レパートリーの 10¹⁸ 多様性を確立。Phase 185 では **K_MHC** ― 主要組織適合複合体 (MHC) による **抗原ペプチド提示** と **TCR-pMHC 認識** の精密構造を扱います。

## MHC: 細胞内自己/非自己の窓

```
全有核細胞 → MHC class I → CD8+ T 細胞
プロフェッショナル抗原提示細胞 (APC) → MHC class II → CD4+ T 細胞
```

### Class I vs Class II 比較

| 性質 | Class I (HLA-A/B/C) | Class II (HLA-DR/DP/DQ) |
|---|---|---|
| 発現 | 全有核細胞 | DC, M φ, B 細胞 |
| 由来抗原 | 内在性 (細胞内タンパク) | 外来性 (エンドサイトーシス) |
| Peptide 長 | **8-10 aa** | **13-25 aa** |
| 結合 termini | 両端固定 (closed groove) | open groove (両端突出可) |
| プロセシング経路 | プロテアソーム + TAP | エンドソーム + cathepsin + HLA-DM |
| 認識 T 細胞 | CD8+ cytotoxic | CD4+ helper |

## HLA 遺伝子座 (Class I + II): 史上最多型ヒト遺伝子

| 遺伝子座 | アレル数 (IPD-IMGT/HLA 2024) |
|---|---|
| HLA-A | 8,500+ |
| HLA-B | 10,500+ |
| HLA-C | 8,000+ |
| HLA-DRB1 | 4,500+ |
| HLA-DQB1 | 2,800+ |
| **計** | **35,000+ アレル** ★ |

= ヒト集団の MHC ペプチド提示レパートリーが極端に異質 → ウイルス耐性のヘテロ性

## Peptide-MHC 結合親和性

```
Kd(strong binder)   < 50 nM       (immunodominant epitope)
Kd(weak binder)     500 nM - 5 μM (subdominant)
Kd(non-binder)      > 50 μM
```

### NetMHCpan / MHCflurry 予測 (Nielsen 2020, O'Donnell 2018)

- 8-10mer ペプチド × ~30,000 HLA アレル
- IC50 予測精度: AUC 0.92-0.95
- Anchor residue (P2, P9 for Class I): 結合の主決定因子

## TCR-pMHC 認識: 物理化学

```
TCR の特異性: pMHC 表面全体の認識
  - CDR1, CDR2 → MHC helix (germline-bias)
  - CDR3 α/β → peptide central residues (V(D)J-bias)

接触面積:        500-1500 Å²
KD(TCR-pMHC):    1-100 μM (低親和性が特徴)
親和性閾値:      < 50 μM → activation
"kinetic proofreading" (McKeithan 1995): 結合時間 > 5 sec → T cell signal
```

## Phase 185 数値検証目標

| 量 | 期待値 |
|---|---|
| HLA-A*02:01 9mer binding peptide 推定数 | ~10⁵ - 10⁶ in human proteome |
| 平均 anchor residue 寄与 (kcal/mol) | 2-4 |
| Class I peptide 切断 (chymotryptic specificity) | F/W/Y/L at C-terminus |
| Class II peptide central residue ratio | 9 aa core in 15 aa peptide |
| Peptide-MHC half-life t_1/2 | 30 sec (weak) → 24 hr (strong) |
| TCR KD typical | 1-100 μM |

## ITU 視点: K_MHC^(0) の構造

```
K_MHC^(0) = -log P(peptide | HLA-allele)
          = ペプチドエピトープ選択の情報的コスト

⇒ Negative selection (thymus) で自己ペプチド-MHC 認識 T 細胞を除去
   = K_MHC^(0) の自己分布を「禁制空間」として削除

⇒ Cancer neoantigens / viral peptides は自己空間外
   = K_MHC^(0) の応答可能領域 → 免疫攻撃

⇒ HLA heterozygosity = K_MHC^(0) の多次元化
   ⇒ COVID-19 重症化と HLA-B*46:01 相関 (Wang 2020) など
```

### "Holes in the repertoire" 概念

```
HLA-restricted MHC binding × thymic negative selection
⇒ 個体ごとに「免疫的死角」が必ず存在
= K_MHC^(0) の zero measure 集合
```

## 重要実験データ

| 観察 | 値 | 出典 |
|---|---|---|
| HLA-B*51 と HIV slow progression | OR ≈ 0.4 | Goulder 2008 |
| HLA-B*53 とマラリア重症化抑制 | OR ≈ 0.6 | Hill 1991 |
| HLA-DRB1*15:01 と多発性硬化症 | OR ≈ 3.0 | Sawcer 2011 |
| HLA-DR2 と SLE | OR ≈ 2.5 | Graham 2002 |

---

📄 **論文 (Tier 1 #26)**: 10.5281/zenodo.20256116

> Phase 186 で Affinity maturation + germinal center + Kd 10⁻⁴ → 10⁻⁹ evolution へ進みます。

#情報理論的統一理論 #ITU #免疫学 #MHC #抗原提示 #HLA #ペプチドMHC結合 #K_MHC #Phase185
