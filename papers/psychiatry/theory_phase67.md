# Phase 67: 精神医学とは何か ― ITU が見る Free Energy Principle と K_brain の破綻

> **Tier 1 #7 (Psychiatry) — Phase 1/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> Tier 1 #5 (Cancer): [10.5281/zenodo.20174318](https://doi.org/10.5281/zenodo.20174318)
> Tier 1 #6 (Aging): [10.5281/zenodo.20175663](https://doi.org/10.5281/zenodo.20175663)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 67 の目的

ITU **medicine triangle** の第 3 頂点 ― 精神医学 ― を扱います:

1. **Karl Friston の Free Energy Principle (FEP)** を ITU 公理と直接対応付け
2. **Bayesian Brain** = $K_{\rm prediction}$ の物理的実装
3. **主要精神疾患 8 種**を K-component 失敗パターンに分類
4. **疾病負担 (DALY, 経済損失)** の世界的規模
5. Phase 68-70 (統合失調症, うつ, 自閉/ADHD/治療) への基盤

中心テーゼ:

> **精神疾患 = 脳における $\delta S = \delta\langle K\rangle$ の破綻**。
> がん (#5) = 細胞・組織レベル、老化 (#6) = 経時劣化、**精神 (#7) = 予測モデルの構造的破綻**。
> Friston FEP は ITU 公理の **脳特化版**。

---

## 1. Friston FEP と ITU の同型性

### 1.1 FEP のコア (再掲)

Karl Friston (UCL) 2010年代以降:
**脳は外界の generative model を持ち、surprise (free energy F) を最小化する**。

$$F = -\ln p(o|m) \quad \text{(変分自由エネルギー)}$$

ここで $o$ = 観測, $m$ = モデル。FEP: $F$ を最小化する制御 (active inference) と感覚 (perceptual inference)。

### 1.2 ITU 公理との対応

ITU 公理: $\delta S(\rho_A) = \delta\langle K_A\rangle$。

脳の場合:
- $\rho_A$ = 内部状態の信念分布 (Bayesian posterior over hidden causes)
- $K_A$ = generative model (= predictive K)
- $\delta S$ = 不確実性の変化 (= belief 更新)
- $\delta\langle K\rangle$ = 予測モデルが実行する「仕事」 (推論コスト)

**両者は数式として等価**:
$$F = -\langle \ln p(o|m)\rangle = D_{KL}(q\|p) + H(q) \Longleftrightarrow \delta S = \delta\langle K\rangle$$

Phase 36 (Tier 0) で既に示した結果を、Tier 1 #7 で**臨床応用**します。

### 1.3 Bayesian Brain

脳の各階層は **「予測 → 誤差 → 更新」** を繰り返す:
- 上位層 (前頭前野) が予測 → 下位層 (感覚野) へ
- 下位層が誤差を生成 → 上位層が予測を修正
- ⇒ **K_prediction が hierarchical** に組織化

精神疾患 = この階層的 K の特定箇所での破綻。

---

## 2. 主要精神疾患 = K-component の破綻パターン

### 2.1 8 大精神疾患の ITU 分類

| 疾患 | 主標的 K-component | 標準解釈 | ITU 解釈 |
|---|---|---|---|
| **統合失調症** | K_precision (感覚) | アベラントサリエンス | **precision-weighting 失敗** ⇒ ノイズを信号と誤認 |
| **大うつ病** | K_reward | 報酬学習低下 | **正の prediction error 不全** ⇒ anhedonia |
| **不安障害** | K_threat | 過剰警戒 | **K_threat 過活性** ⇒ false-positive 予測 |
| **PTSD** | K_threat (trauma 由来) | フラッシュバック | **trauma により K_threat 過固定** |
| **自閉スペクトラム** | K_social | TOM 困難 | **K_social の過剰 precision** ⇒ 柔軟性喪失 |
| **ADHD** | K_attention | 注意散漫 | **K_attention の precision 失敗** ⇒ 信号選択不能 |
| **OCD** | K_action | 強迫行動 | **K_action の precision 過剰** ⇒ 確信不能ループ |
| **双極性障害** | K_mood (cyclic) | 感情変動 | **K_mood が unstable oscillation** |

⇒ **各疾患 = 特定の K-component の破綻**。

### 2.2 共通点と相違点

| 概念 | がん (#5) | 老化 (#6) | 精神 (#7) |
|---|---|---|---|
| 時間スケール | 月-年 | decades | 急性-慢性混在 |
| K 破綻範囲 | 細胞局所 | 全身緩慢 | 脳構造的 (回路レベル) |
| 主因 | 変異・代謝 | 経時劣化 | **発達 + 環境 + 遺伝** |
| 治療 | 多軸 combo | 多 K longevity | **薬物 + 心理療法 + neuromodulation** |

⇒ 精神疾患の独自性 = **発達**と**経験**が K-component の形成に大きく寄与。

---

## 3. 疾病負担 (世界的規模)

### 3.1 DALYs (Disability-Adjusted Life Years)

WHO/IHME GBD 2021:

| 疾患 | 世界 DALYs (百万) | 罹患率 (世界) |
|---|---|---|
| **大うつ病** | **47.5** | 3.8% |
| 不安障害 | 26.4 | 4.0% |
| 双極性障害 | 7.5 | 0.6% |
| 統合失調症 | 13.9 | 0.3% |
| ADHD | 16.5 | 5% (児童) |
| 自閉スペクトラム | 11.5 | 1% |
| OCD | 5.1 | 1.2% |
| PTSD | 8.4 | 2.6% (戦争・災害地域) |
| **合計 精神疾患** | **~150** (全疾患の 7%) | ~25% (生涯有病率) |

### 3.2 経済負担

| 領域 | 年間コスト (米) |
|---|---|
| 直接医療費 | $200B |
| 生産性低下 | $150B |
| 介護・社会保障 | $80B |
| **合計 (米)** | **$430B** |

世界では $5T 規模 (2023, Mental Health Foundation 報告)。

⇒ **精神医学は人類最大の医療経済課題**。

---

## 4. なぜ精神医学は他の医学より難しいか

### 4.1 K の物理的アクセスの難しさ

- がん: 生検で組織を直接見る
- 老化: 血液 biomarker (Horvath clock)
- **精神疾患: 「K_brain は心 (内部状態)」 ⇒ 直接観察不能**

EEG, fMRI, MEG 等の間接測定のみ ⇒ 診断は症状ベース (DSM-5) に頼る。

### 4.2 治療の試行錯誤性

| 疾患 | 第一選択 | 反応率 |
|---|---|---|
| 大うつ病 | SSRI | **30-50%** |
| 統合失調症 | 第二世代抗精神病薬 | 60-70% (陽性症状), 陰性は弱い |
| ADHD | メチルフェニデート | 70% |
| 自閉 | (薬物治療なし、行動療法のみ) | — |

⇒ **試行錯誤** が標準 (try-and-see)。ITU 視点でこれは **「どの K が壊れているか分からないまま K-restore を試す」** ためと解釈可能。

### 4.3 ITU 視点での突破口

- **脳の K-component を測定する技術** (Phase 70 で詳述: EEG/MEG biomarker, K-mapping)
- **発達初期の K 構築介入** (青年期前の予防)
- **digital phenotyping** (スマホ・wearable で K_attention/mood を継続測定)

---

## 5. Phase 67 数値検証

### 5.1 検証 1: FEP と ITU 公理の同値性 (数式比較)

### 5.2 検証 2: 8 疾患の K-component スパイダープロファイル

### 5.3 検証 3: 世界疾病負担 (DALYs) の可視化

### 5.4 検証 4: 治療反応率 vs 「K 特定の難しさ」 の相関

---

## 6. Phase 67 の結論

1. **FEP (Friston) = ITU 公理の脳特化版** (Phase 36 の臨床応用)
2. **8 大精神疾患 = 8 種の K-component 破綻**
3. **精神医学 = 世界医療経済の最大課題** ($5T/年規模)
4. **試行錯誤治療** ⇒ K 直接測定技術が次世代突破口
5. **発達・経験**が K 形成に大きく寄与 (がん・老化と異なる)

Phase 68 では **統合失調症**を ITU で深堀り解析 ―
- precision-weighting 失敗の数値モデル
- ドーパミン仮説の ITU 解釈
- 抗精神病薬 (Risperdal, Abilify, Clozapine) の作用機序

---

## 引用

```
Terada, M. (2026). ITU and Psychiatry (Phase 67-70).
Tier 1 #7 application paper. In preparation.
```

参考:
- Friston (2010) Nat Rev Neurosci 11, 127 (FEP)
- Sterzer et al. (2018) Biol Psychiatry 84, 634 (FEP and psychosis)
- Adams et al. (2013) Frontiers Psychiatry 4, 47 (computational psychiatry review)
- Pellet & Friston (2018) Cell 174, 1029 (active inference)
- GBD 2021 mental health collaborators (Lancet Psychiatry 2022)
- DSM-5-TR (APA 2022)
