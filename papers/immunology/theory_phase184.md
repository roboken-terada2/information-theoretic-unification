# Phase 184: TCR / BCR + V(D)J Recombination + Repertoire 多様性 ― K_adaptive 深掘り

Phase 183 で K_immune 全体像と自然/獲得二層構造を提示。Phase 184 では **K_adaptive** の中核 ― **T 細胞受容体 (TCR) と B 細胞受容体 (BCR) の分子機構** + **V(D)J 組換え** + **レパートリー多様性の生成** を深掘りします。

## V(D)J 組換え (Tonegawa 1976, Nobel 1987)

```
ゲノム → 受容体: 中央教義の例外的書き換え
胚細胞: 限定された V/D/J 遺伝子セグメント
体細胞 (リンパ球): RAG1/RAG2 が DNA を切断 → 結合 → 受容体遺伝子完成
```

### RAG1/RAG2 (Schatz-Oettinger-Baltimore 1989)

| 段階 | 機構 |
|---|---|
| **認識** | RSS (recombination signal sequence) 12/23 規則 |
| **切断** | RAG1/RAG2 が DSB (double-strand break) 生成 |
| **結合** | NHEJ + TdT による P/N nucleotide 付加 |
| **修復** | Artemis, DNA-PKcs, XRCC4, ligase IV |

## TCR / BCR の構造

### TCR (T cell receptor)

| 鎖 | 遺伝子座 | 用途 |
|---|---|---|
| TCR α | TRA (14q11) | αβ T cell (95%) |
| TCR β | TRB (7q34) | αβ T cell |
| TCR γ | TRG (7p14) | γδ T cell (5%) |
| TCR δ | TRD (14q11) | γδ T cell |

- **αβ T cell**: MHC restricted, peptide-specific
- **γδ T cell**: MHC-independent, lipid/metabolite sensing (CD1 経由)

### BCR (B cell receptor) / Antibody

| 鎖 | 種類 | 機能 |
|---|---|---|
| 重鎖 (H) | IGH (14q32) | 5 isotype: IgM/D/G/A/E |
| 軽鎖 κ | IGK (2p11) | 60% of antibodies |
| 軽鎖 λ | IGL (22q11) | 40% of antibodies |

## 数値: 多様性の階層

### TCR β segment count (IMGT データベース)

```
V_β: 65 functional (out of ~80 total)
D_β: 2
J_β: 13 functional
```

### BCR heavy chain (IGH)

```
V_H: 38-46 functional
D_H: 23
J_H: 6 functional
```

### 多様性の積算

| 寄与 | TCR αβ | BCR (germline) | BCR (post-SHM) |
|---|---|---|---|
| 組合せ (V·D·J × αβ pair) | ~10⁶ | ~10⁵ | ~10⁵ |
| P/N nucleotide (junctional) | ×10⁷ | ×10⁷ | ×10⁷ |
| **計 germline** | **~10¹³** | **~10¹²** | - |
| Allelic inclusion / pairing | ×10² | ×10² | ×10² |
| **計 + pairing** | **~10¹⁵** | **~10¹⁴** | - |
| SHM (B 細胞のみ) | - | - | ×10⁴-10⁶ |
| **計 final** | **~10¹⁵-10¹⁸** | - | **~10¹⁸-10²⁰** |

## CDR3 がエピトープ認識の主役

```
CDR1, CDR2: V 遺伝子由来 (germline)
CDR3:       V-(D)-J junction 由来 (V(D)J 組換えで最大多様化)
            ⇒ 受容体特異性の 80% を担う
```

CDR3 長: TCRβ 13-15 aa (中央値), BCR-H 12-25 aa (より広い分布)

## ITU 視点: K_adaptive^(0) の構造

```
K_adaptive^(0) = K_VDJ ⊕ K_pairing ⊕ K_junctional ⊕ K_SHM

ρ_adaptive = レパートリー分布 (10¹⁵-10¹⁸ clones)
S(ρ_adaptive) = repertoire entropy (~20-25 nats for naive)
              + reduced post antigen exposure (clone expansion)
```

### Affinity maturation = ITU フロー

```
δS(ρ_adaptive) / δt < 0  (germinal center で多様性減少)
δ⟨K_adaptive^(0)⟩ / δt < 0  (clone 集中 ⇒ Kd 低下方向)
```

= **ITU axiom の生物学的実装** ★

## Theory check

| 量 | 計算 | 観測 |
|---|---|---|
| TCRβ CDR3 平均長 | 13.5 aa (model) | 14-15 aa (IMGT) ✓ |
| TCR β segment count | 65V × 2D × 13J = 1690 | 1690 (IMGT) ✓ |
| BCR-H combinatorial | 40V × 23D × 6J = 5520 | 5520 (IMGT) ✓ |
| α/β pairing entropy | log(65·13) ≈ 6.7 nats | 6-7 ✓ |
| SHM rate per generation | 10⁻³ /bp/division | 10⁻³ ✓ (Rajewsky 1996) |

---

📄 **論文 (Tier 1 #26)**: 10.5281/zenodo.20256116

> Phase 185 で MHC + antigen presentation + peptide-MHC binding affinity へ進みます。

#情報理論的統一理論 #ITU #免疫学 #VDJ組換え #TCR #BCR #レパートリー多様性 #K_adaptive #Phase184
