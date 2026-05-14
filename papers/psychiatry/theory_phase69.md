# Phase 69: うつ病・不安障害の ITU 解析 ― K_reward と K_threat の破綻

> **Tier 1 #7 (Psychiatry) — Phase 3/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 69 の目的

Phase 68 で **統合失調症 = K_precision 失敗** を扱いました。Phase 69 では精神医学の最大負担:

1. **大うつ病 (MDD) = K_reward 破綻** (世界 DALYs #1, 47.5M)
2. **不安障害 = K_threat 過活性** (世界 DALYs #2, 26.4M)
3. **SSRI/SNRI** の作用機序 ― なぜ 30-50% しか効かないか
4. **Ketamine (2019 FDA)** ― 数時間で効く rapid-acting antidepressant
5. **Psilocybin (FDA breakthrough)** ― 2024-25 で第 III 相進行
6. **治療抵抗性うつ病 (TRD ~30%)** の階層治療

中心テーゼ:

> **うつ病 = 内的予測モデル ($K_{\rm reward}$) が「報酬は起きない」 と確信した状態**。
> **不安 = $K_{\rm threat}$ が「危険が常にある」 と過剰確信した状態**。
> ⇒ 両者とも ITU 公理破綻、しかし「破綻の方向」 が逆。

---

## 1. 大うつ病 = K_reward の破綻

### 1.1 症状と Bayesian Brain

| 症状 | 標準解釈 | ITU 解釈 |
|---|---|---|
| Anhedonia (無快感) | 報酬感受性低下 | **正の prediction error が起きない** |
| 絶望感 | 認知バイアス | K_reward の事前確率 → 0 |
| 自責感 | 自己評価低下 | K_self_model が低下値で固定 |
| 食欲・性欲低下 | 動機付け不足 | K_motivation 全般低下 |
| 不眠/過眠 | 概日リズム異常 | K_circadian の破綻 |

### 1.2 ITU 数式

健康な脳:
- 報酬予測: $\hat{R}_t$ (中庸の期待値)
- 実報酬: $R_t$
- prediction error: $\delta_t = R_t - \hat{R}_t$ (正負あり)
- K_reward 更新: $\hat{R}_{t+1} = \hat{R}_t + \alpha \delta_t$

うつ病:
- $\hat{R}_t \to 0$ (絶望)
- 正の $\delta_t$ も拾わない (K_reward の precision が低下)
- 結果: いくら良い出来事があっても感じない (anhedonia)

### 1.3 神経生物学

主要回路:
- **mPFC (内側前頭前野)**: K_self_model
- **NAc (側坐核)**: K_reward, ドーパミン報酬
- **Amygdala**: K_threat (Phase 69-2 で詳述)
- **DLPFC**: K_executive
- **デフォルトモードネットワーク**: K_self の自己参照

うつ病: mPFC ↔ Amygdala 結合過剰、NAc 反応低下、DLPFC 機能低下。
⇒ 「ネガティブ K の優位、ポジティブ K の不全」。

---

## 2. 不安障害 = K_threat の過活性

### 2.1 種類

| 障害 | 主な threat 内容 | K_threat の偏り |
|---|---|---|
| 全般性不安 (GAD) | 将来の漠然とした脅威 | 広範な K_threat 過活性 |
| パニック障害 | 身体感覚の解釈 | 内受容 K の暴走 |
| 社交不安 (SAD) | 他者評価 | K_social_threat 過剰 |
| 特定恐怖症 | 特定対象 (蛇, 高所等) | K_threat の局所過剰 |
| PTSD | trauma 想起 | K_threat の trauma-locking |

### 2.2 ITU 解釈

健康時:
- threat 予測の precision は中庸
- 偽陽性 (false alarm) と偽陰性のバランス

不安障害:
- K_threat の precision 過剰
- **偽陽性激増** ⇒ 何でも危険に感じる
- 過剰 prediction error ⇒ 自律神経興奮、回避行動

### 2.3 不安 vs うつ の共通点

両者とも **負の感情の K が支配的**、しかし:
- うつ = **過去/絶望** に focus
- 不安 = **未来/脅威** に focus
- ⇒ 50-60% が併発 (comorbidity)

---

## 3. 薬物療法

### 3.1 SSRI / SNRI

| 薬剤 | クラス | 効果開始 | 反応率 |
|---|---|---|---|
| **Fluoxetine** (Prozac) | SSRI | **4-6 週** | 50% |
| Sertraline (Zoloft) | SSRI | 4-6 週 | 50% |
| Escitalopram (Lexapro) | SSRI | 4-6 週 | 55% |
| **Venlafaxine** (Effexor) | SNRI | 4-6 週 | 55% |
| Duloxetine (Cymbalta) | SNRI | 4-6 週 | 55% |
| Bupropion (Wellbutrin) | NDRI | 4-6 週 | 50% |

ITU 解釈:
- セロトニン上昇 ⇒ K_reward + K_threat の **両方を緩衝**
- だから不安にもうつにも効くが、特異性は弱い
- 効果発現に **数週間** ⇒ K の再構築には時間が必要 (神経新生説)

### 3.2 Ketamine (2019 FDA esketamine = Spravato)

| 特徴 | 値 |
|---|---|
| 作用機序 | **NMDA glutamate 受容体拮抗** |
| 効果開始 | **数時間〜24h** ← SSRI の 100 倍速い |
| 持続 | 1-2 週間 (反復投与必要) |
| TRD 反応率 | 60-70% |
| 副作用 | 解離、血圧上昇、依存リスク |

ITU 解釈:
- NMDA = シナプス可塑性の主要回路
- ketamine ⇒ **K_reward の急速 reset**
- 「神経新生では遅すぎる」 ⇒ 既存回路の直接調整

### 3.3 Psilocybin (Compass Pathways Phase III)

| 特徴 | 値 |
|---|---|
| 作用機序 | **5-HT2A 強作動** + 神経可塑性 |
| 効果開始 | **1 セッション (数時間)** で持続 |
| 持続 | 数週間〜数ヶ月 |
| TRD 反応率 | **70-80%** (Carhart-Harris 2018) |
| 副作用 | 「bad trip」, 心血管リスク |

ITU 解釈:
- 5-HT2A 作動 ⇒ デフォルトモードネットワーク (K_self) の **「reset」**
- 患者は治療中に「自己の K_model が再構築」 を主観体験
- 心理療法と組合せて initial K の置き換え

⇒ ITU 観点で **新世代抗うつ薬 = K_reward + K_self を急速再構築**。

### 3.4 TMS, ECT, DBS

| 介入 | 作用 | 適応 |
|---|---|---|
| TMS | DLPFC 磁気刺激 | TRD 第 1 選択 (薬剤抵抗) |
| **ECT** (電気けいれん療法) | 全脳発作 | **重症 TRD で最も効果的** (75-85% 反応) |
| DBS | 帯状回 (Brodmann 25) 刺激 | 末期 TRD |
| Vagus nerve stim | 迷走神経刺激 | 補助的 |

ITU 解釈: 全脳 K のリセット (ECT) > 局所 K (TMS, DBS)。

---

## 4. 治療抵抗性うつ病 (TRD)

### 4.1 定義

STAR*D 試験 (2006):
- 4 段階治療しても remission しない場合
- **約 30% が TRD**

### 4.2 階層治療カスケード

| Step | 治療 | Cumulative response | Cumulative remission |
|---|---|---|---|
| 1 | SSRI (Citalopram) | 50% | **37%** |
| 2 | SSRI 変更 or augmentation | 60% | 50% |
| 3 | TCA / MAOI / lithium augm. | 65% | 60% |
| 4 | Combination | 68% | 65% |
| **5 (TRD)** | **Ketamine / Psilocybin / ECT** | **80%** | **70%** |

⇒ ITU 視点: 各 step は **異なる K-component を targeting**。多軸 combination が必然。

---

## 5. ネットワーク理論 ― K 回路としての mood

### 5.1 主要回路

```
[mPFC (K_self)] ←──── [DLPFC (K_executive)]
       ↑                       ↑
       │                       │
   [Amygdala (K_threat)] ←─→ [NAc (K_reward)]
                                       │
                                  [VTA (dopamine)]
```

健康時: 各 K がバランス、双方向制御。
うつ: mPFC↔Amygdala 過剰、NAc 不活性。
不安: Amygdala 全般過活性。

### 5.2 ITU 視点

mood = **K-network の動的均衡**。
治療 = ネットワーク全体の **新均衡点への遷移**。
⇒ 単剤では局所介入のみ、combination + 心理療法で安定状態を変えられる。

---

## 6. Phase 69 数値検証

### 6.1 検証 1: K_reward dynamics (healthy vs depressed)

### 6.2 検証 2: K_threat over-activation (anxiety vs PTSD)

### 6.3 検証 3: 薬剤 vs 効果発現時間 (SSRI 数週 → ketamine 数時間 → psilocybin 1 セッション)

### 6.4 検証 4: STAR*D 階層治療カスケード

---

## 7. Phase 69 の結論

1. **大うつ病 = K_reward 破綻** (正の prediction error 不全)
2. **不安障害 = K_threat 過活性** (偽陽性激増)
3. **SSRI = K の slow 再構築** (4-6 週), **Ketamine = K の急速 reset** (数時間)
4. **Psilocybin = K_self の体験的再構築** (1 セッション)
5. **TRD 30% = 多 K 破綻** ⇒ 多軸 combination + ECT が必要
6. **mood = K-network の動的均衡** ⇒ ネットワーク介入が次世代

Phase 70 (最終回) では **ASD/ADHD + 全 K 治療戦略 + 10 予測**を提示し、**Tier 1 #7 を完成、ITU medicine triangle を閉じます**。

---

## 引用

```
Terada, M. (2026). ITU and Psychiatry (Phase 67-70).
Tier 1 #7 application paper. In preparation.
```

参考:
- Rush et al. (2006) Am J Psychiatry 163, 1905 (STAR*D)
- Berman et al. (2000) Biol Psychiatry 47, 351 (ketamine antidepressant)
- Carhart-Harris et al. (2018) Lancet Psychiatry 5, 793 (psilocybin TRD)
- Sahay & Hen (2007) Nat Neurosci 10, 1110 (neurogenesis hypothesis)
- Drevets et al. (1997) Nature 386, 824 (subgenual ACC in depression)
- Disner et al. (2011) Nat Rev Neurosci 12, 467 (cognitive depression)
