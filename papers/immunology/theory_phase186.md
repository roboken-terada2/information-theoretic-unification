# Phase 186: Affinity Maturation + Germinal Center + Kd 進化 ― K_affinity 深掘り ★

Phase 185 で MHC + ペプチド提示の K_MHC を確立。Phase 186 では **胚中心** で実装される **親和性成熟** (somatic hypermutation + clonal selection) の動力学を扱い、**K_affinity** = ITU 下降フローの生物学的最深実装 を提示します。

## 胚中心 (Germinal Center, GC) の解剖学

```
リンパ節 / 脾臓の B 細胞ゾーン
├── Dark zone (DZ)   : 増殖 + somatic hypermutation
│   └── Centroblasts (高度増殖, AID 高発現)
└── Light zone (LZ)  : 選択 + helper T cell 相互作用
    └── Centrocytes (T_fh helper / FDC pMHC で選別)
```

### Burnet clonal selection theory (1957, Nobel 1960)

```
1. 抗原と高親和性結合する BCR を持つクローン
2. 増殖 + 体細胞超変異 (10⁻³ /bp/division)
3. ↑ 高親和性変異体を選択
4. ↓ 低親和性 / autoreactive クローン apoptosis
5. ↑ メモリ B cell / 長寿命プラズマ細胞へ分化

⇒ 数週間で Kd 10⁻⁴ → 10⁻⁹ M (100,000× 改善)
```

## 主要分子機構

### AID (Activation-Induced cytidine Deaminase, Honjo 2000)

```
C → U 脱アミノ化 (BCR V 領域選択的)
↓ ミスマッチ修復 (UNG, MSH2/6) → 変異固定 or class switch
変異率: 10⁻³ /bp/division × 7 GC 周期 = ~10⁻²
```

= 体細胞変異率を生殖細胞変異 (10⁻⁹/bp/div) の **100 万倍** に局所増大

### Class Switch Recombination (CSR)

```
IgM/D → IgG/A/E への定常領域置換
S 領域 (switch region) でゲノム DNA 削除
AID + RAG-independent NHEJ で実装
```

## アフィニティ進化: 数式

### Eisen-Siskind kinetics (1964)

```
Kd(t) = Kd_0 · exp(-r·t)
   r ≈ 0.5 /week (germinal center activity)
   t ≈ 4-8 weeks ⇒ Kd 100-10,000× 改善
```

### Random mutation + selection (Fisher 1930 → 免疫学)

```
クローン適応度 f_clone = exp(-E_binding / kT)
                      ∝ 1/Kd

進化的Walk: BCR配列空間 → 局所最適 → 大域探索 (ε≈ε_GC)
```

= **Wrightian fitness landscape** の典型例

## ITU 視点: K_affinity の最小化フロー ★

```
K_affinity^(0) = -log P(clone i | antigen)
              = アフィニティに依存する情報的選択ポテンシャル

時刻 t における repertoire 分布: ρ(t)
S(ρ(t))         : Shannon entropy (多様性)
⟨K_affinity^(0)⟩: 平均アフィニティ親和性

⇒ GC内動力学: δS < 0, δ⟨K⟩ < 0 (ITU axiom 厳密成立)
⇒ ローカル ITU フロー = ρ(t) → δρ ∝ -∇K_affinity^(0)
```

### "Wrinkle in entropy" - GC dynamics の非単調性

```
Phase 1 (初期):    多クローン拡大 → S 増加, ⟨K⟩ 高位
Phase 2 (中期):    SHM導入 → S 増加, ⟨K⟩ 中位
Phase 3 (後期):    選択集中 → S 減少, ⟨K⟩ 低位 ★ ITU フロー収束
Phase 4 (出口):    プラズマ細胞 + memory B分化 → 持続性 K_state
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| Kd 初期 (germline) | 10⁻⁴ - 10⁻⁵ M |
| Kd 成熟 (post-GC) | 10⁻⁸ - 10⁻¹⁰ M |
| 改善倍率 | 10² - 10⁵ ★ |
| Affinity maturation 期間 | 2-8 週間 |
| SHM 変異密度 (V region) | 5-15% per V region |
| GC 周期 / 分裂回数 | 6-12 cycles |
| Memory B cell 半減期 | 10 年以上 (麻疹) |
| Plasma cell IgG 産生量 | 10⁴ molecules/cell/sec |
| **Kd 進化 ITU フロー検証** | δS/δ⟨K⟩ ≈ 1 |

## 重要実験データ

| 観察 | 値 | 出典 |
|---|---|---|
| 抗 HEL Kd germline → mature | 10⁻⁵ → 10⁻¹⁰ M (10⁵×) | Foote-Milstein 1991 |
| 抗 NP Kd germinal | 10⁻⁵ → 10⁻⁸ M | Berek-Milstein 1987 |
| 麻疹 vaccine 中和抗体半減期 | 200+ 年 | Amanna 2007 NEJM |
| COVID 中和抗体減衰 | 1-2 ヶ月で 4 倍減 | Wang 2021 Nature |
| AID -/- マウス CSR/SHM | 完全消失 | Muramatsu 2000 |

---

📄 **論文 (Tier 1 #26)**: 10.5281/zenodo.20256116

> Phase 187 で Tolerance + Autoimmunity (AIRE, Treg, SLE/RA) へ進みます。

#情報理論的統一理論 #ITU #免疫学 #親和性成熟 #胚中心 #体細胞超変異 #K_affinity #Phase186
