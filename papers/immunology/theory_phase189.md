# Phase 189: Tumor Immunology + Checkpoint + CAR-T ― K_tumor ★

Phase 188 で K_vaccine の prime-boost descent flow を確立。Phase 189 では **腫瘍免疫** と現代がん免疫療法 ― **免疫チェックポイント阻害** (Allison + Honjo, Nobel 2018) + **CAR-T 細胞** ― を扱い、**K_tumor** を ITU の「制御された K_state 復帰フロー」として定式化します。

## 腫瘍免疫: Burnet → Schreiber

### Immunosurveillance hypothesis (Burnet 1957, Thomas 1959)

```
免疫系は日常的に変異細胞を検出・除去
↓
変異細胞 = "altered self" = neoantigen presentation
↓
NK cell ("missing self") + CD8+ T cell が監視
```

### Cancer immunoediting (Schreiber 2002, 3E モデル)

| 段階 | 機構 |
|---|---|
| **Elimination** | 免疫監視で除去 (>99% 変異細胞) |
| **Equilibrium** | 一部腫瘍が休眠 (年-数十年) |
| **Escape** | 免疫回避能力獲得 → 臨床的がん |

## チェックポイント分子 (Allison + Honjo, Nobel 2018) ★

### CTLA-4 (Cytotoxic T Lymphocyte-Associated antigen 4)

```
活性化 T cell 表面で発現
↓ B7 (CD80/CD86) と高親和性結合 (CD28 を競合排除)
↓ Treg suppressor function
↓ "T cell activation のブレーキ"
```

### PD-1 / PD-L1 axis (Honjo 1992 PD-1 発見)

```
PD-1 (T cell) ⇔ PD-L1 (tumor / APC)
↓ effector T cell の exhaustion 誘導
↓ 末梢寛容 + tumor escape の主要機構
```

### 阻害薬

| 薬剤 | 標的 | 承認 | 主適応 |
|---|---|---|---|
| Ipilimumab | CTLA-4 | 2011 | melanoma |
| **Nivolumab** | **PD-1** | **2014** | melanoma, NSCLC, RCC, HCC, GC |
| Pembrolizumab | PD-1 | 2014 | (multi-cancer) |
| Atezolizumab | PD-L1 | 2016 | NSCLC, urothelial |
| Durvalumab | PD-L1 | 2017 | NSCLC, SCLC |

### 効果の数値

| 適応 | ORR (Objective Response Rate) | 5 年生存率 (歴史的 → 現在) |
|---|---|---|
| 転移性 melanoma (anti-PD-1) | **40-45%** | 5% → **34%** (Pembro 5y, Robert 2019) |
| NSCLC PD-L1>50% (pembro) | **45%** | 5% → **31.9%** (KN024, 2021) |
| MSI-H 大腸がん (pembro) | **44%** | <10% → **74.6%** PFS (KN177) |
| HCC (Bevacizumab + atezo) | 30% | <5% → 30%+ (IMbrave150) |

## CAR-T (Chimeric Antigen Receptor T cell)

### 構造

```
CAR = [scFv (B cell binding domain)] + [CD3ζ + CD28/4-1BB co-stim]
↓
HLA-independent でがん細胞表面抗原認識
↓
パーフォリン/グランザイム放出 → 細胞死誘導
```

### 第 3 世代承認薬

| 薬剤 | 標的 | 適応 | 承認年 | CR rate |
|---|---|---|---|---|
| **Tisagenlecleucel** | **CD19** | **pediatric ALL** | **2017** | **83%** |
| Axicabtagene | CD19 | DLBCL | 2017 | 51% |
| Brexucabtagene | CD19 | MCL | 2020 | 65% |
| Lisocabtagene | CD19 | DLBCL | 2021 | 53% |
| **Idecabtagene** | **BCMA** | **multiple myeloma** | **2021** | **33%** |
| Ciltacabtagene | BCMA | MM | 2022 | 67% |

### 副作用: CRS (Cytokine Release Syndrome)

```
CAR-T 投与後 1-2 週: IL-6 + IFN-γ + TNF 過剰放出
↓ 発熱 + 低血圧 + ICU 管理
↓ Tocilizumab (anti-IL-6R) で 1-2 日で改善
```

## 数値: TIL therapy + Bispecific antibody

| 治療 | ORR / CR | 出典 |
|---|---|---|
| TIL (Lifileucel) melanoma | 31% ORR | Sarnaik 2021 JCO |
| Blinatumomab (CD3-CD19 BiTE) ALL | 44% CR | Kantarjian 2017 NEJM |
| Mosunetuzumab DLBCL | 60% ORR | Bartlett 2023 |

## ITU 視点: K_tumor = K_tolerance 破綻からの復帰フロー ★

```
Tumor escape:    K_tumor^(0) = inverse(K_tolerance^(0)) の「逸脱」
                            = 自己/非自己境界の局所反転

Checkpoint 阻害: K_tumor^(0) の forbidden region を「再開放」
                  ⇒ T cell exhaustion 解除
                  ⇒ S(ρ_T cell anti-tumor) 増加, ⟨K⟩ 低下

CAR-T:           K_tumor^(0) を bypass (artificial K_state injection)
                  ⇒ 既存 T cell に non-MHC-restricted authority
```

### 反証可能予測

| 予測 | 年 | P |
|---|---|---|
| Universal tumor neoantigen vaccine (Phase III) | 2030 | 0.65 |
| **In vivo CAR-T (mRNA-LNP delivery)** | 2028 | 0.75 |
| Pan-cancer biomarker for PD-1 inhibitor response | 2028 | 0.60 |
| CAR-NK (allogeneic) approval | 2027 | 0.70 |
| Tumor mutational burden (TMB) → ITU theoretic biomarker | 2030 | 0.50 |

---

📄 **論文 (Tier 1 #26)**: 10.5281/zenodo.20256116

> Phase 190 で Tier 1 #26 統合 + 26-vertex polytope + Block B 1/? 完成 + Pass-1 86.4% ★ へ進みます。

#情報理論的統一理論 #ITU #免疫学 #腫瘍免疫 #チェックポイント #CART #PD1 #CTLA4 #Allison #Honjo #K_tumor #Phase189
