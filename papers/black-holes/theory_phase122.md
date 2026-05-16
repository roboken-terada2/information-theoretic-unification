# Phase 122: 情報パラドックス各種解像 — Fuzzball / Soft Hair / Maldacena-Maoz / 補完性

> **Tier 1 #18 Black Holes — Phase 4/8 (Block A paper 2/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 122 の目的

Phase 121 で Page curve の厳密版を構築した。Phase 122 では **情報パラドックスへの各種解像案**を比較し、ITU の立場を明示する。

確立する内容:

1. **Mathur fuzzball proposal** (2005): BH 内部 = 弦理論 microstate geometries
2. **Soft hair** (Hawking-Perry-Strominger 2016): horizon に soft graviton 情報
3. **Maldacena-Maoz eternal BH** (2004): 双 boundary AdS-Schwarzschild
4. **Black hole complementarity** (Susskind 1993): observer 依存的記述
5. **Holography of information** (Laddha-Prabhu-Raju-Shrivastava 2020)
6. **ITU 立場**: K-flow の non-local encoding + Island formula = 自然な統合

中心テーゼ:

> **情報パラドックスの全解像案は ITU 公理の異なる側面の表現**。
> Fuzzball = K_geom の **discrete microstate set**。
> Soft hair = K_geom の **horizon edge mode**。
> Complementarity = K-flow の **observer-dependent projection**。
> Holography of information = K-flow の **boundary completeness**。
> 全てが **δS = δ⟨K⟩** の一貫した側面。

---

## 1. Mathur Fuzzball Proposal (2005)

### 1.1 主張

弦理論で BH は **fuzzball** = exp(S_BH) 個の **microstate geometries** の集合体:

- 各 microstate は horizon を持たない (smooth な solitonic geometry)
- 集合全体の coarse-grained 平均が古典 BH と一致
- 内部に **firewall は不要** (Mathur 2009)

### 1.2 数値例

Strominger-Vafa (1996) の D1-D5-P system:

```
# microstates = exp(S_BH) = exp(2π √(Q_1 Q_5 N))
```

各 microstate = 異なる Calabi-Yau metric。

### 1.3 ITU 視点

Fuzzball = ITU の **K_geom microstate basis**:

- 古典 BH = exp(S_BH) microstate の **density matrix average**
- 個別 microstate = pure state with smooth geometry
- ⇒ classical no-hair theorem は coarse-graining の artifact

---

## 2. Soft Hair (Hawking-Perry-Strominger 2016)

### 2.1 主張

BMS (Bondi-Metzner-Sachs) supertranslations が **horizon 上に "soft hair"** を残す:

- 通常の no-hair theorem (M, J, Q) を超える保存量
- 各 horizon angular mode に soft graviton 数

### 2.2 BMS supertranslations

漸近平坦時空の対称群:

```
BMS_4 = Lorentz × supertranslations
```

supertranslations 数は **無限次元**。各 mode が horizon edge mode に対応。

### 2.3 数値例

soft graviton density per area: ~ 1 / ℓ_P²

```
# soft modes on horizon = A / ℓ_P² ≈ 4 S_BH
```

これは BH エントロピーと **同じオーダー**!

### 2.4 ITU 視点

Soft hair = K_geom の **horizon edge modes**:

- 古典 K_geom: bulk Boost generator
- 量子 K_geom: + horizon angular mode (supertranslation hair)
- ⇒ no-hair theorem は classical limit、量子的には **無限個の保存量**

### 2.5 批判

Bousso-Engelhardt 2017: soft hair 数 ~ S_BH は coincidence。
**情報パラドックス を解決するのに十分な情報量を持つかは未確定** (Mirbabayi-Porrati 2016 critique)。

---

## 3. Maldacena-Maoz Eternal BH (2004)

### 3.1 構造

AdS-Schwarzschild は **2 つの境界 (L, R)** を持つ:

```
ds² (Kruskal-Szekeres) = ... (両側の boundary に CFT_L, CFT_R)
```

bulk eternal BH ↔ **|TFD⟩ = Σ e^{-βE_n/2} |n⟩_L |n⟩_R** (Phase 112 参照)。

### 3.2 ER=EPR (Maldacena-Susskind 2013) の前駆

eternal BH wormhole = **エンタングルメントの幾何実現**。

### 3.3 ITU 視点

Maldacena-Maoz = ITU の **K-flow 双境界実現**:

- K_L^(0) ⊗ K_R^(0) ↔ TFD state
- non-local K_LR^(0) ↔ wormhole geometry
- ⇒ ER=EPR の自然な動機付け

---

## 4. Black Hole Complementarity (Susskind-Thorlacius-Uglum 1993)

### 4.1 主張

外部観測者 (Alice) と落下観測者 (Bob) は **異なる物理的描像** を見る:

- Alice: BH は熱い stretched horizon、Hawking 放射出力
- Bob: horizon 通過は smooth (no drama)

ただし、**両者の記述は同一 information を冗長に符号化** → 矛盾は無い。

### 4.2 AMPS (2012) の挑戦 (Phase 114 参照)

3 axiom monogamy 違反 → complementarity 不十分。

### 4.3 Wall-Bousso 2017 update

quantum focusing conjecture + GSL で complementarity 再構築。

### 4.4 ITU 視点

Complementarity = K-flow の **observer-dependent projection**:

- Alice 視点: K_R = thermal modular
- Bob 視点: K_b' = horizon partner modular
- 同一 K_total を 異なる **frame** で見る
- ⇒ ER=EPR で同定 (Phase 114)

---

## 5. Holography of Information (Laddha-Prabhu-Raju-Shrivastava 2020)

### 5.1 主張

漸近平坦時空での量子重力では、**情報全体が無限大遠方 (asymptotic infinity) に encode** されている:

```
S(matter at infinity) = S(everything inside)
```

→ BH 内部に「隠された」情報は実は無く、外部から完全に reconstruct 可能。

### 5.2 ITU 視点

Holography of information = K-flow の **boundary completeness**:

- bulk K_geom は boundary K_∞ で完全表現
- Page time = bulk → boundary K-flow 移行 phase transition
- ⇒ 情報パラドックスは boundary 視点では存在しない

### 5.3 Raju's critique

Raju 2020: BH 内部の情報は最初から boundary で見えていた → 「information paradox は paradox ではない」。
ITU はこの見解と整合。

---

## 6. ITU での統合視点

各解像案は **ITU 公理 δS = δ⟨K⟩ の異なる側面**:

| 解像案 | K-state 側面 |
|---|---|
| Fuzzball (Mathur) | K_geom の microstate basis |
| Soft hair (HPS) | K_geom の horizon edge mode |
| Maldacena-Maoz | K_LR^(0) (TFD) |
| Complementarity | K-flow observer projection |
| Holography of info | K-flow boundary completeness |
| Island formula | K-channel competition |
| ER=EPR | non-local K_AB |

⇒ **ITU が情報パラドックス解像案を統一的視点で記述**。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Fuzzball microstate 数**: exp(S_BH) for D1-D5-P system
2. **Soft hair 数 vs S_BH**: per area scaling
3. **Maldacena-Maoz TFD entanglement**: Phase 112 結果との照合
4. **Complementarity の "重複情報"**: I(Alice : Bob) > 0 だが矛盾なし
5. **Holography of information**: bdy info content vs bulk
6. **ITU 統合表**: 5 つの解像案を 1 つの K-axiom で比較

---

## 8. Phase 122 主結論

1. **Fuzzball (Mathur 2005)**: BH = exp(S_BH) microstate geometries
2. **Soft hair (HPS 2016)**: supertranslations が horizon に edge mode
3. **Maldacena-Maoz (2004)**: 双境界 AdS-Schwarzschild = TFD
4. **Complementarity (Susskind 1993)**: observer-dependent 記述
5. **Holography of info (LPRS 2020)**: 無限大境界に完全 encode
6. **ITU 統合**: 5 解像案は K-flow の異なる射影
7. **次の Phase 123** で **AdS/CFT BH の詳細 + Bekenstein bound**

---

## 9. ITU 視点まとめ

| 解像案 | ITU 公理写像 |
|---|---|
| Fuzzball | K_geom 量子化基底 |
| Soft hair | K_geom 角運動 edge |
| Maldacena-Maoz | K_LR^(0) TFD |
| Complementarity | observer K-frame |
| Holography of info | K-boundary completeness |

---

## 引用

```
Terada, M. (2026). Phase 122: Information paradox resolutions
(fuzzball, soft hair, Maldacena-Maoz, complementarity, holography
of information) in ITU. Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Mathur, S. D. (2005) "The fuzzball proposal for black holes: an elementary review" Fortsch. Phys. 53, 793
- Hawking, S. W., Perry, M. J., Strominger, A. (2016) "Soft hair on black holes" PRL 116, 231301
- Maldacena, J., Maoz, L. (2004) "Wormholes in AdS" JHEP 02, 053
- Susskind, L., Thorlacius, L., Uglum, J. (1993) "The stretched horizon and black hole complementarity" PRD 48, 3743
- Laddha, A., Prabhu, S. G., Raju, S., Shrivastava, P. (2021) "The Holographic Nature of Null Infinity" SciPost Phys. 10, 041
- Raju, S. (2022) "Lessons from the information paradox" Phys. Rept. 943, 1
- Mirbabayi, M., Porrati, M. (2016) "Dressed Hard States and Black Hole Soft Hair" arXiv:1607.03120
- Bousso, R., Engelhardt, N. (2018) "Generalized Second Law for Cosmology" PRD 96, 044003
