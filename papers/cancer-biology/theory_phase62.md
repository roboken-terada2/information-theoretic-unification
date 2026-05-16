# Phase 62: ITU-informed がん治療ロードマップ 2026-2040 ― 多 K 同時 restoration への道

> **Tier 1 #5 (Cancer Biology) — Phase 4/4 (最終回)**
> Tier 0 ITU: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 62 の目的

Phase 59-61 で「**がん = 細胞 + 組織レベルの $\delta S = \delta\langle K\rangle$ 破綻**」 を多角的に示しました。Phase 62 では:

1. **ITU が予測する治療戦略**: 多 K 同時 restoration
2. **2026-2040 年のがん治療ロードマップ**
3. **5 年生存率予測** (主要がん種別)
4. **新興療法**: ADC, bispecific, mRNA cancer vaccine, microbiome
5. **10 個の反証可能予測**
6. **Tier 1 #5 paper v1.0.0 完成** + engineering → medicine への展開記録

中心テーゼ:

> **がん克服 = 全 K-component の同時 restoration**。
> 単剤療法は K の代償経路で逃げられる。combo (代謝 + 免疫 + 標的) が ITU 必然。
> 2040 年に主要がんの 5 年生存率 50-90% を予測。

---

## 1. ITU 治療戦略: 多 K 同時 restoration

### 1.1 標的軸 (3 軸)

| 軸 | 標的 K-component | 既存薬例 |
|---|---|---|
| **#1 細胞内 K** (Phase 59) | Tumor suppressor, oncogene 経路 | imatinib, trastuzumab, BRAFi, KRAS G12C inhibitor |
| **#2 代謝 K** (Phase 60) | OXPHOS / glycolysis / aa metabolism | metformin, 2-DG, CB-839 (PhaseI/II) |
| **#3 免疫 K** (Phase 61) | T 細胞, NK, antigen presentation | Keytruda, Yervoy, CAR-T, TIL |

### 1.2 3 軸 combination = ITU 必然

| 治療軸数 | 期待反応率 | 例 |
|---|---|---|
| 1 軸 (単剤) | 20-30% | Keytruda 単独 |
| 2 軸 | 40-50% | Keytruda + chemo, ipi+nivo |
| **3 軸** | **60-75%** | **Keytruda + chemo + targeted** |
| 4 軸+ | 70-85% (理論値) | + metabolic / microbiome |

Phase 60-61 で示した combo の優位性は ITU 公理の物理的帰結。

### 1.3 主要難治がんへの 3 軸戦略

| がん種 | 細胞内 K | 代謝 K | 免疫 K |
|---|---|---|---|
| **膵がん** | KRAS G12C, MEK | 解糖系阻害 | TIL (MSI-H なら ICI) |
| **TNBC** | PARPi (BRCA変異) | metformin | PD-L1 (Tecentriq) |
| **GBM** | EGFRvIII CAR-T | 代謝介入未確立 | 効果限定 |
| **MSS 大腸** | KRAS G12C, NTRK | metformin | bispecific 必要 |

⇒ 単純な ICI で奏功しない難治がんでも、**3 軸 combo で 30-50% の反応率到達可能** (ITU 予測)。

---

## 2. 2026-2040 ロードマップ

### 2.1 主要マイルストーン

| 年 | 主要進展 |
|---|---|
| 2024-26 | bispecific 抗体 (tarlatamab, BCMA bispecific) 普及 |
| 2026 | mRNA cancer vaccine 第 III 相 (Moderna+Merck, melanoma) |
| **2027** | **KRAS G12C 全体生存改善 (sotorasib+immunotherapy)** |
| 2028 | TIL 療法 適応拡大 (cervical, lung) |
| 2029 | 多 K 同時 monitoring 標準化 (リキッドバイオプシー) |
| **2030** | **主要がんの 50% で 5 年生存 ≥ 70%** |
| 2032 | microbiome-cancer 介入が補助療法へ |
| 2034 | 量子計算による創薬時間 1/10 (Tier 1 #1 の応用) |
| 2036 | AI 主導の患者層別化 (Tier 1 #2 の応用) |
| **2040** | **「がんは治療可能な慢性疾患」** が標準認識 |

### 2.2 5 年生存率予測 (主要がん)

| がん種 | 2024 | 2030 | 2040 (ITU 予測) |
|---|---|---|---|
| Melanoma (advanced) | 50% | 65% | 80% |
| Lung (NSCLC) | 25% | 40% | 60% |
| Breast | 90% | 92% | 95% |
| Colorectal | 65% | 73% | 85% |
| **Pancreatic** | **10%** | **25%** | **50%** ★ |
| **Glioblastoma** | **5%** | **10%** | **30%** ★ |
| Liver | 20% | 35% | 55% |
| Multiple myeloma | 60% | 75% | 90% |
| Hematologic (overall) | 70% | 85% | 95% |

⇒ **2040 年に難治がん 2 種 (膵, GBM) でも 30-50% 生存率**到達 (ITU 予測)。

### 2.3 治療費・社会的コスト

| 年 | 米がん治療市場 ($B) | 患者あたり平均年費用 |
|---|---|---|
| 2024 | 240 | $50K |
| 2030 | 350 | $80K (combo 価格) |
| 2040 | 500 | **$150K** (多 K combo) ⚠️ |

⇒ **アクセス格差** が新たな倫理問題に。低中所得国向けの biosimilars 戦略必須。

---

## 3. 新興療法のスナップショット

### 3.1 ADC (Antibody-Drug Conjugate)

- **Enhertu** (HER2 ADC, AstraZeneca): HER2-low TNBC で奏功
- **Trodelvy** (Trop-2 ADC, Gilead): TNBC
- ITU 解釈: **抗体 = K 認識、payload = K restoration の物理化**

### 3.2 Bispecific antibody

- **Blincyto** (CD19/CD3, BiTE): ALL で標準化
- **Tecvayli** (BCMA/CD3): myeloma
- **Tarlatamab** (DLL3/CD3): SCLC (2024 承認)

ITU 解釈: **2 つの K (認識 + 攻撃) を 1 分子で実装**。

### 3.3 mRNA cancer vaccine

- **Moderna mRNA-4157 + Keytruda**: melanoma 第 III 相 (2024-26)
- 患者個別ネオアンチゲン に対する mRNA ワクチン

ITU 解釈: **K_immune を「教える」** = 認識すべき syndrome を直接ロード。

### 3.4 Microbiome

- 腸内細菌叢が ICI 反応性を制御 (Akkermansia muciniphila)
- FMT (糞便微生物移植) で ICI non-responder を responder 化

ITU 解釈: **K_immune は身体内の細菌生態系にも依存** ― 真の ITU は organism + microbiome 全体。

---

## 4. 10 個の反証可能予測

ITU 視点 + 現状トレンドから 2026-2040 年に検証可能:

1. **3 軸 combo (代謝+免疫+標的) で MSS 大腸がん反応率 ≥ 30%** ← 2028 年
2. **mRNA cancer vaccine が melanoma 5 年生存率 ≥ 80%** ← 2030 年
3. **KRAS G12D inhibitor (sotorasib 後継) が 2027 年承認**
4. **量子計算が新規 oncology 標的を 1 つ以上特定** ← 2030 年
5. **TIL 療法が固形腫瘍 5 種以上で標準化** ← 2032 年
6. **多 K 同時 liquid biopsy が ASCO 標準** ← 2029 年
7. **膵がん 5 年生存率 30% 到達** ← 2032 年
8. **GBM 5 年生存率 20% 到達** ← 2034 年
9. **microbiome-modulating cancer drug が 2030 年に承認**
10. **ITU 多 K 治療指数 (TKI) が NCCN ガイドラインに導入** ← 2033 年

⇒ 1 個でも反証されれば ITU の精緻化を要求。

---

## 5. 政策提言

### 国家
- 量子計算 + AI 投資を**oncology drug discovery** に集中 (Tier 1 #1, #2 と統合)
- リキッドバイオプシー保険償還の標準化
- 国境を超えた **TMB/MSI 等バイオマーカー国際標準**

### 製薬
- 単剤よりも **combination trial** を優先 (regulatory も後押し)
- 患者個別 mRNA vaccine の製造プラットフォーム投資

### 個人・社会
- **early detection** (50 才以上の年次 liquid biopsy) の普及
- 健康寿命 = ITU 視点では **K_immune と K_metab の長期維持**
- 喫煙・肥満・運動不足 = 全 K の慢性劣化要因

---

## 6. Tier 1 #5 全体まとめ

### 6.1 4 phase 統合

| Phase | テーマ | 主要発見 |
|---|---|---|
| 59 | ITU 基礎 | がん = δS = δ⟨K⟩ 破綻、10 hallmarks = 10 K-components、Two-hit = redundant QECC |
| 60 | Warburg 代謝 | K_metab の意図的劣化で δS 暴走を支える、3 軸 combo が ITU 必然 |
| 61 | 免疫学 | K_immune 7-step corruption、ICI で 20-50% restore、CAR-T/TIL は K augmentation/amplification |
| **62** | **ロードマップ** | **3 軸 combo で 2040 年に主要難治がん 30-50% 生存、10 予測** |

### 6.2 ITU 構造拡張: rectangle → pentagon

```
   AI/ASI #2 ──── 暗号 #3
       ↑              ↑
       │              │
   量子計算 #1 ── 半導体 #4
       │              │
       └─── がん #5 ──┘ ← NEW (engineering → medicine)
```

Tier 1 #5 から **medicine ベクトル**が始まる。次の Tier 1 #6 (老化) で **medicine triangle (がん + 老化 + 精神医学)** が形成される予定。

### 6.3 ITU 全体での位置付け

- engineering: substrate (#4) → computation (#1) → intelligence (#2) → communication (#3)
- medicine: cancer (#5) → aging (#6) → psychiatry (#7) [予定]

両系列が **dS = d⟨K⟩** で接続される ― これが ITU の真の野心。

---

## 引用

```
Terada, M. (2026). ITU and Cancer Biology: A Single-Axiom View of Cellular
Breakdown, Metabolism, Immunology, and the 2026-2040 Treatment Roadmap (v1.0.0).
Zenodo. DOI: [to be assigned]
```

参考:
- Hanahan & Weinberg (2000, 2011, 2022) Hallmarks of Cancer series
- Chen & Mellman (2013) Immunity (cancer-immunity cycle)
- Vander Heiden, Cantley, Thompson (2009) Science (Warburg re-interpretation)
- AACR, ASCO, ESMO 2024 guidelines and abstracts
- Moderna-Merck mRNA cancer vaccine trial reports
