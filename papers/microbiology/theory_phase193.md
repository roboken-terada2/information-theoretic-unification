# Phase 193: Bacteriophage + Phage Therapy + CRISPR 起源 ― K_phage ★

Phase 192 で K_phylogeny の系統樹構造を確立。Phase 193 では **生命圏最多実体** = バクテリオファージ (10³¹) を扱い、**K_phage** + ファージ療法 + CRISPR の起源を ITU 視点で統一します。

## ファージ: 地球で最多実体

```
海洋ファージ数:    10³⁰ (1 mL 海水に 10⁷ 個)
生物地球化学的役割:
  - 海洋細菌 1 日 20-40% 死亡 (viral shunt)
  - 炭素循環: 表層 → 深海 100 億トン/年
  - 遺伝子伝達: 海洋で 10²⁸ 移動/sec ★
```

= **K_phage = 地球の最大の K-state mixing 演算子**

## ファージ研究史

### 発見と命名

```
1915: Twort (英) 細菌溶解現象 (publication only)
1917: d'Herelle (仏-カナダ) "bacteriophage" 命名
1939: Schlesinger 電顕で形態観察
1952: Hershey-Chase Blender experiment (Nobel 1969):
      ファージ DNA が遺伝物質 ★
```

### Phage molecular biology の貢献

| 発見 | 年 | 出典 | 役割 |
|---|---|---|---|
| Hershey-Chase | 1952 | DNA = 遺伝物質 | Phage T2 |
| Meselson-Stahl | 1958 | 半保存複製 | Phage T7 |
| Genetic code | 1961 | Crick-Nirenberg | Phage T4 |
| Restriction enzymes | 1970 | Arber-Smith-Nathans (Nobel 1978) | Phage protection |
| **Phage display** | 1985 | Smith (Nobel 2018) | Antibody engineering |

## ファージ分類

### Caudovirales (Order, 全 phage の 95%)

| Family | Tail | 代表 |
|---|---|---|
| Myoviridae | 収縮性, 長い | T4, P1, P2 |
| Siphoviridae | 非収縮, 長い | T1, T5, λ |
| Podoviridae | 短い | T7, T3, ϕ29 |

### Lifecycle: Lytic vs Lysogenic

```
Lytic (溶菌):
  Adsorption → Injection → Replication → Assembly → Lysis
  20-40 分で 100-200 progeny

Lysogenic (溶原):
  Integration into host genome (prophage)
  λ phage 経典例 (Lwoff Nobel 1965)
  ↓
  Stress → SOS response → induction → lytic cycle
```

## CRISPR の起源 = ファージ防御 ★

### CRISPR 発見史

```
1987: Ishino (大阪大) 大腸菌で repeat 発見
2000: Mojica 多くの細菌で確認
2005: Mojica-Bolotin: ファージ + プラスミド由来配列
2007: Barrangou (Danisco) Yogurt 細菌で防御機能証明
2010: Doudna + Charpentier: tracrRNA + Cas9 機構解明
2012: 系統的 in vitro 切断 (Jinek)
2013: Zhang, Church: 真核細胞応用 ★
2020: Doudna + Charpentier Nobel ★
```

### CRISPR system 分類 (2 classes, 6 types)

```
Class 1: 多サブユニット effector (Cascade complex)
  Type I:  Cas3 helicase-nuclease (E. coli)
  Type III: Cas10 + multi-subunit (S. solfataricus)
  Type IV: rare
Class 2: 単一エフェクター (Cas9/Cas12/Cas13)
  Type II:  Cas9 (Streptococcus pyogenes) ★
  Type V:   Cas12 (DNA, blunt cut)
  Type VI:  Cas13 (RNA-targeting) ★ Phase 56 link
```

### CRISPR = ITU の "memory K-state"

```
Phage の K_state を spacer として「凍結」
↓ memory として保存
↓ 再侵入時に rapid detection + cleavage
⇒ 細菌の "adaptive immune-like memory" ★
⇒ K_phage^(0) を K_immune^(0) (microbial) に変換する演算子
```

## ファージ療法 (Phage therapy)

### 歴史

```
1920s-1940s: ソ連 + 東欧で広く臨床利用 (Eliava Institute, Tbilisi 1923-)
1940s-1970s: 西側で衰退 (抗生剤普及)
2010s-2020s: AMR 危機で復活
2017: Strathdee case (UCSD) ★
2023-: FDA Phase II 多発
```

### Strathdee case (2017) - 西側ファージ療法復活点 ★

```
Tom Patterson 教授 (心理学者, 70 才)
  → 多剤耐性 Acinetobacter baumannii 感染
  → 抗生剤すべて無効
  → 妻 Steffanie (UCSD 疫学者) が phage 探索を要請
  → 米軍 + UCSD + Texas A&M + Belgium 協力
  → 個別 phage cocktail 4 種類
  → 静注で 完全回復
  → IND 取得し論文化
  → "The Perfect Predator" (2019, ベストセラー)
```

### 現在の Phase 試験 (2024)

| Sponsor | 適応 | Phase |
|---|---|---|
| Adaptive Phage (米) | UTI, prosthetic joint | II |
| BiomX (米) | Acne vulgaris, CF | II |
| Locus Biosciences (米) | CRISPR-Cas3 + phage | II |
| **Eliava Institute** | Multiple (1923-) | 認可済 (旧ソ連圏) |

## ITU 視点: K_phage の構造 ★

```
K_phage^(0) = -log P(prophage | host genome) ⊕ P(phage state | environment)

軸:
  - Phage型 (T4, λ, etc., 10⁹ identified)
  - Host range (specificity)
  - Lifecycle (lytic vs lysogenic)
  - Prophage integration site
  - CRISPR spacer memory

K_phage ⊗ K_microbe = co-evolutionary K-state
  ⇒ Red Queen dynamics (Van Valen 1973): 永続的 arms race
```

### Phage-host arms race の ITU 表現

```
細菌:    K_resistance^(0) up
↓
ファージ: K_anti-resistance^(0) up
↓
細菌:    K_CRISPR^(0) up
↓
ファージ: Anti-CRISPR (Acr) gene
↓
... 無限螺旋
⇒ 双方とも S(repertoire) 維持 + ⟨K⟩ 増加方向 = "co-descent flow"
```

## 数値検証目標

| 量 | 期待値 |
|---|---|
| ファージ burst size (T4) | **100-300 progeny/cell** |
| Lytic cycle 時間 (T4) | **25-30 分** |
| CRISPR spacer 長 | 28-44 bp (typically 32) |
| CRISPR memory 数 (single E. coli) | 数千 spacer max |
| Phage display library size | 10⁹-10¹⁰ peptide variants |
| Strathdee case phage cocktail efficacy | **完全回復 < 3 months** ✓ |
| **ITU axiom: phage-host coevolution** | δS/δ⟨K⟩ ≈ 1 |

## 反証可能予測 (Tier 1 #27 内)

| 予測 | 年 | P |
|---|---|---|
| **Phage therapy FDA 承認** | 2028 | 0.75 |
| Universal phage cocktail platform | 2030 | 0.55 |
| CRISPR Type VI (RNA-targeting) 臨床応用 | 2030 | 0.60 |
| **Anti-CRISPR 系統的 catalog 完成** | 2028 | 0.70 |
| Phage-resistant strain × FDA approved phage 共進化 model | 2030 | 0.50 |

---

📄 **論文 (Tier 1 #27)**: 10.5281/zenodo.20256555

> Phase 194 で 抗生剤耐性 + プラスミド + AMR 分子機構 へ進みます。

#情報理論的統一理論 #ITU #微生物学 #ファージ #バクテリオファージ #CRISPR #Doudna #Charpentier #PhageTherapy #K_phage #Phase193
