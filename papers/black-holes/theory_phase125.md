# Phase 125: Primordial BH + 高次相関 + BH Merger 統計 (LIGO/Virgo)

> **Tier 1 #18 Black Holes — Phase 7/8 (Block A paper 2/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 125 の目的

Phase 119-124 で BH 物理 (古典 + 量子 + 情報) を扱った。Phase 125 では **天文学的観測**寄りの 3 テーマを扱う:

1. **Primordial BH (PBH)**: Hawking 1971, Carr-Hawking 1974、ダークマター候補
2. **BH 高次相関**: Hawking 放射の higher-point function
3. **BH merger 統計**: LIGO/Virgo GWTC-3 (2021), GWTC-4 (2024) のデータ
4. **BH 形成史**: 恒星進化、population synthesis
5. **ITU 視点**: 観測 BH = K_geom の **macroscopic 統計集団**

中心テーゼ:

> **観測される BH 集団 = ITU の K_geom 分布関数**。
> Primordial BH = inflation 期の K_geom 量子揺らぎから直接形成。
> LIGO/Virgo の BBH merger rate は K_geom 集団動力学の予言と整合。
> 高次相関 ⟨R_i R_j R_k⟩ は ITU 公理の **higher-order moments**。

---

## 1. Primordial Black Holes (PBH)

### 1.1 形成シナリオ

inflation 期の **巨大な curvature perturbation** が horizon 再入時に重力崩壊:

```
δ ρ / ρ ≳ 0.5  (collapse threshold)
M_PBH ~ M_horizon at formation
```

形成質量は inflation 終了後の **horizon scale** で決まる:

```
M_PBH ~ (c³ t / G_N) × 1 M_⊙
```

- t = 1s 時点: M ~ 10⁵ M_⊙ (super-massive PBH 候補)
- t = 10⁻³ s: M ~ 100 M_⊙ (LIGO BBH 候補)
- t = 10⁻²³ s (QCD epoch): M ~ 0.1 M_⊙ (sub-stellar)
- t = 10⁻⁴⁰ s (Planck): M ~ m_P

### 1.2 PBH と Dark Matter

仮説: dark matter の一部 (or 全部) が PBH:

```
Ω_PBH / Ω_DM = ?  (constraint dependent on M)
```

観測制約 (Carr et al. 2021):

| M_PBH | 制約 | 観測手段 |
|---|---|---|
| < 10¹⁵ g | excluded | Hawking radiation 蒸発 |
| 10¹⁵ - 10¹⁷ g | EGRET γ-ray | 制約 |
| 10¹⁷ - 10²² g | open window | --- |
| 10²² - 10²⁴ g | EROS / OGLE micro-lensing | <10% DM |
| 30-100 M_⊙ | LIGO BBH rate | <10% DM |

### 1.3 ITU 視点

PBH = ITU の **inflation 期 K_geom 自己組織化**:

- Inflation 期: K_inflaton dominant
- Reheating: K-flow が radiation に変換
- 局所的揺らぎが threshold 越え → BH 形成

---

## 2. BH 高次相関 (Hawking radiation の higher-point function)

### 2.1 2 点相関 (Phase 124)

```
⟨R_i R_j⟩ = thermal noise + post-Page entanglement
```

### 2.2 4 点相関

```
⟨R_i R_j R_k R_l⟩ = ⟨R_i R_j⟩⟨R_k R_l⟩ + permutations + connected piece
```

connected piece = **OTOC** (Out-of-Time-Order Correlator):

```
F(t) = ⟨W(t) V W(t) V⟩
```

scrambling 時間 t_scr ~ (β / 2π) log S_BH (Maldacena-Shenker-Stanford 2016 bound)。

### 2.3 ITU 視点

higher-order correlations = K-flow の **多体相関**:

```
⟨K_R_1 K_R_2 ... K_R_n⟩ ↔ ITU 公理の higher-order extension
```

⇒ 単一公理 δS = δ⟨K⟩ から全 n-point function が計算可能 (in principle)。

---

## 3. BH Merger 統計 (LIGO/Virgo)

### 3.1 GWTC-3 (2021) と GWTC-4 (2024)

| Catalog | 検出数 | 期間 |
|---|---|---|
| GWTC-1 (O1+O2) | 11 | 2015-17 |
| GWTC-2 (+O3a) | 50 | + 2019-20 |
| GWTC-3 (+O3b) | 90 | + 2020 |
| **GWTC-4 (O4 暫定)** | **180+** | + 2023-24 |

### 3.2 BBH 質量分布

- 最小: ~3 M_⊙ (NS の上限近傍)
- ピーク: **30-50 M_⊙** (pair-instability gap 下端)
- pair-instability mass gap: **45-130 M_⊙** (理論予言)
- 最大: 150+ M_⊙ (IMBH 候補)

### 3.3 BBH merger rate

```
R_BBH = 17-39 / Gpc³ / yr  (GWTC-3)
```

local rate 内で stellar evolution が説明 (PBH は <10%)。

### 3.4 ITU 視点

BBH merger = K_geom の **macroscopic dynamics**:

- GW チャネル: K_geom が radiation (Phase 117)
- post-merger ringdown: K_geom quasi-normal modes
- Page curve に類似の post-merger evolution (Tier 1 #18 全体)

---

## 4. BH 形成史

### 4.1 Stellar evolution

```
Main sequence → Red giant → Supernova → NS or BH
```

質量に応じて:
- M_progenitor < 8 M_⊙: white dwarf
- 8-20 M_⊙: NS
- 20-40 M_⊙: stellar BH
- 40-130 M_⊙: pair-instability supernova (no BH, completely destroyed)
- 130-260 M_⊙: pulsational pair-instability, partial BH
- > 260 M_⊙: direct collapse BH (Mass gap "Q" candidates)

### 4.2 SMBH 起源 (super-massive BH)

| theory | mechanism |
|---|---|
| Direct collapse | 10⁴-10⁶ M_⊙ seed at z~20 |
| Stellar BH seeds | 多重合体で成長 (slow) |
| Primordial BH seeds | inflation 期から (Phase 125.1) |

M87* (6.5×10⁹ M_⊙) の起源は **未解明** = 大 SMBH パラドックス。

### 4.3 ITU 視点

BH 形成史 = K_geom の **cosmic timeline**:

- Big Bang (PBH 候補)
- 恒星進化 (stellar BH)
- 銀河中心 (SMBH)
- ⇒ K_geom が 14 Gyr で多様な分布を形成

---

## 5. ITU 観測予言

### 5.1 高次相関スパイク

Page time 後の Hawking radiation 3-point, 4-point correlation でスパイク:

```
⟨R_i R_j R_k⟩_connected ≠ 0 for t > t_Page
```

### 5.2 BBH merger rate と PBH constraint

LIGO O4-O5 で merger rate 高精度測定:

```
R_obs = R_stellar + R_PBH
R_PBH < 10% R_DM (current)
```

### 5.3 IMBH (Intermediate Mass BH) 検出

LISA + ngEHT で 10²-10⁵ M_⊙ BH 検出 → ITU の K_geom 質量分布予言の検証。

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **PBH 形成質量 vs 形成時刻**: M_PBH ~ c³ t / G の数値
2. **PBH constraint plot**: M_PBH vs Ω_PBH/Ω_DM
3. **Scrambling time t_scr** vs M_BH: (β/2π) log S_BH
4. **BBH mass distribution** (GWTC-3 + GWTC-4 暫定)
5. **Stellar evolution → BH mass funnel**

---

## 7. Phase 125 主結論

1. **PBH (Hawking 1971)**: inflation 期から形成、形成質量 ~ c³t/G
2. **PBH DM 候補**: 10¹⁷-10²² g window が open
3. **高次相関**: OTOC scrambling time t_scr ~ (β/2π) log S_BH
4. **GWTC-4 (2024)**: 180+ BBH 検出、ピーク 30-50 M_⊙
5. **BBH merger rate**: 17-39 / Gpc³ / yr、PBH < 10% DM
6. **SMBH 起源パラドックス**: 大 SMBH は未解明
7. **ITU 観測予言**: 高次相関スパイク、IMBH 検出、PBH constraint
8. **次の Phase 126** で **Tier 1 #18 統合 + 10 predictions**

---

## 8. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| PBH 形成 | inflation 期 K_inflaton → K_geom |
| Hawking 高次相関 | K-flow n-point functions |
| BBH merger 統計 | K_geom macroscopic dynamics |
| Scrambling t_scr | K-flow chaos time |
| 恒星進化 | K_star → K_geom funnel |
| SMBH 起源 | cosmic K-state history |

---

## 引用

```
Terada, M. (2026). Phase 125: Primordial BH, higher-order correlations,
and BH merger statistics (Tier 1 #18 phase 7/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Hawking, S. W. (1971) "Gravitationally collapsed objects of very low mass" MNRAS 152, 75
- Carr, B. J., Hawking, S. W. (1974) "Black holes in the early Universe" MNRAS 168, 399
- Carr, B., Kuhnel, F. (2020) "Primordial Black Holes as Dark Matter" Annu. Rev. Nucl. Part. Sci. 70, 355
- Carr, B. et al. (2021) "Constraints on primordial black holes" Rept. Prog. Phys. 84, 116902
- Maldacena, J., Shenker, S., Stanford, D. (2016) "A bound on chaos" JHEP 08, 106
- Hayden, P., Preskill, J. (2007) "Black holes as mirrors" JHEP 09, 120
- LIGO/Virgo/KAGRA (2021) "GWTC-3: Compact Binary Coalescences..." (arXiv:2111.03606)
- Belczynski, K. et al. (2016) "The first gravitational-wave source from isolated binary evolution" Nature 534, 512
- Begelman, M. C., Rees, M. J. (2018) "Gravity's Fatal Attraction" Cambridge
