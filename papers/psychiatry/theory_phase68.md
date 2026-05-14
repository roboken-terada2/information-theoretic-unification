# Phase 68: 統合失調症の ITU 解析 ― precision-weighting 失敗とドーパミン仮説

> **Tier 1 #7 (Psychiatry) — Phase 2/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 68 の目的

Phase 67 で 精神疾患 = K-component 破綻 と確立しました。Phase 68 では **統合失調症 (schizophrenia)** を詳細解析:

1. **Precision-weighting 失敗** = ITU の $K_{\rm precision}$ 故障
2. **3 つの症状群**: 陽性 / 陰性 / 認知の K 分類
3. **ドーパミン仮説の ITU 解釈** (mesolimbic 過剰 + mesocortical 不全)
4. **抗精神病薬 6 種**の作用機序と限界
5. **治療抵抗性統合失調症 (30%)** と Clozapine の特異性
6. Phase 69-70 への基盤

中心テーゼ:

> **統合失調症 = $K_{\rm precision}$ の壊れた優先順位付け**。
> 強すぎる事前確率 (top-down K) と弱すぎる感覚証拠 (bottom-up) のミスマッチ。
> ⇒ ノイズが信号と誤認 (幻覚)、内的予測が外的現実と誤認 (妄想)。

---

## 1. Precision-weighting 失敗 ― ITU 視点

### 1.1 Bayesian Brain と precision

階層的予測符号化:
- 上位層が事前 $p(\text{cause})$ を予測
- 下位層が感覚 $p(\text{obs}|\text{cause})$ を受信
- **precision** $\pi$ = 各層の信号信頼度の重み付け

健康脳:
- top-down precision: 中程度
- bottom-up precision: 中程度
- ⇒ バランスのとれた belief update

統合失調症:
- top-down 過剰 ⇒ **強すぎる予測**
- bottom-up 不全 ⇒ **弱すぎる感覚**
- ⇒ **内的予測が現実を支配** ⇒ 幻覚・妄想

### 1.2 ITU 解釈

$K_{\rm precision}$ は感覚と予測のミキシング比を制御:

$$K_{\rm precision} = \pi_{\rm bottom-up} / \pi_{\rm top-down}$$

健康時 $K_{\rm precision} \approx 1$、統合失調症で **<< 1**。

ITU 公理 $\delta S = \delta\langle K\rangle$ が破綻 ⇒ 内的状態 ($\rho_A$ の belief) と外的現実の不整合 ⇒ 病態。

### 1.3 数値モデル

Sterzer et al. (2018, Biol Psychiatry):
- 健康: precision ratio = 1.0
- 統合失調症 (陽性症状期): precision ratio = 0.3
- ⇒ false positive (幻覚) 確率増加

Phase 68 simulation で詳述 (図 a 参照)。

---

## 2. 3 症状群 と K-component

### 2.1 DSM-5 分類

| 症状群 | 例 | 主標的 K | 治療反応 |
|---|---|---|---|
| **陽性 (positive)** | 幻聴, 妄想, 思考障害 | K_precision (低下) | **70%+** (抗精神病薬) |
| **陰性 (negative)** | 意欲低下, 感情鈍麻, 無快感 | K_reward, K_motivation | **30%** (薬は弱い) |
| **認知 (cognitive)** | 実行機能, 作業記憶 | K_executive | **20%** (限定的) |

### 2.2 ITU 視点

陽性症状 = K_precision の壊れた誤った値 ⇒ **薬で K を強制 restore 可能**。
陰性・認知症状 = 構造的 K 欠失 (発達期の回路破綻) ⇒ **薬では補えない**。

これは **がん の細胞内 K 修復 (Phase 60-61) と同じ構造**:
- 急性破綻 (薬で逆転可能) vs 構造的破綻 (回復困難)

### 2.3 数値: 治療反応率

CATIE 試験 (2005, NEJM, N=1,460) の結果:

| 症状群 | 抗精神病薬での改善率 |
|---|---|
| 陽性 | **70-75%** |
| 陰性 | 25-35% |
| 認知 | 15-25% |

---

## 3. ドーパミン仮説と ITU

### 3.1 古典的ドーパミン仮説

Carlsson (1963) → Snyder (1976):
- **Mesolimbic 経路の D2 受容体過剰活性** = 陽性症状
- 抗精神病薬 = D2 拮抗薬 ⇒ 陽性症状を抑える

しかし...
- **Mesocortical 経路は不全 (低活性)** = 陰性・認知症状の起源
- 古典的 D2 拮抗薬は mesocortical も抑えてしまい、陰性症状を**悪化**

### 3.2 修正版仮説 (Howes & Kapur 2009)

**シナプス前ドーパミン合成過剰** が起源:
- 線条体 (mesolimbic 終末) で過剰 ⇒ 陽性
- 前頭前野 (mesocortical 終末) で不足 ⇒ 陰性

### 3.3 ITU 解釈

ドーパミン = K_precision の **生物学的実装の一部**:
- D1 ファミリー: top-down precision encoder
- D2 ファミリー: bottom-up gain modulator
- 統合失調症 = D2/D1 比の局所異常

ITU 視点では「**ドーパミン仮説は K_precision の生物物理的説明**」 として位置付け可能。

---

## 4. 抗精神病薬 (Antipsychotics)

### 4.1 主要 6 種

| 薬剤 | 世代 | 主作用 | 適応 |
|---|---|---|---|
| **Haloperidol** | 第 1 (typical) | D2 強拮抗 | 急性精神病 |
| Chlorpromazine | 第 1 | D2 + α1 + H1 拮抗 | 古典 |
| **Risperidone** (Risperdal) | 第 2 (atypical) | D2 + 5-HT2A 拮抗 | 統合失調症, 双極 |
| Olanzapine (Zyprexa) | 第 2 | D2 + 5-HT2A + ヒスタミン拮抗 | 統合失調症 |
| **Aripiprazole** (Abilify) | 第 3 | **D2 partial agonist** | 統合失調症, うつ補助 |
| **Clozapine** | 第 2 (特殊) | D4 > D2, 5-HT2A, 他多数 | **治療抵抗性 (TRS) 第一選択** |

### 4.2 ITU 視点の作用機序

| 薬剤 | 効果 (K 視点) |
|---|---|
| D2 拮抗 (Haloperidol) | K_precision を強制 restore (rough) |
| D2 partial agonist (Abilify) | K_precision を中庸に調整 (sophisticated) |
| **Clozapine** | **多受容体作用** = 多 K の同時調整 |

⇒ Cancer/Aging と同じ「**多 K combination が最も効く**」 パターン。Clozapine が TRS で唯一効くのは多受容体作用故。

### 4.3 副作用

| 副作用 | 機序 | 影響 K |
|---|---|---|
| 錐体外路症状 (EPS) | nigrostriatal D2 阻害 | K_motor |
| 高プロラクチン血症 | tuberoinfundibular D2 | K_endocrine |
| 体重増加・糖尿病 | 5-HT2C, H1 | K_metab |
| 鎮静 | H1, α1 | K_arousal |
| **Clozapine 無顆粒症** | (不明) | 命に関わる ⇒ 週次血液検査 |

---

## 5. 治療抵抗性統合失調症 (TRS)

### 5.1 定義と頻度

**TRS = 2 種類以上の抗精神病薬で 6 週間以上の十分量投与でも改善しない**。
- 統合失調症患者の **30%** が TRS。
- TRS で **Clozapine が唯一効く** (40-60% 改善)。

### 5.2 ITU 解釈

TRS = K_precision に加えて **複数の構造的 K 破綻**を持つ:
- K_executive (DLPFC 回路)
- K_reward (mesolimbic)
- K_social (mentalizing network)

⇒ **多 K 同時破綻** ⇒ Clozapine の多受容体作用がないと届かない。

### 5.3 新興療法

- **TMS (経頭蓋磁気刺激)**: DLPFC 標的 ⇒ K_executive restore (一部 TRS で有効)
- **tDCS, DBS**: 深部脳刺激 ⇒ TRS 重症例
- **Pimavanserin (5-HT2A 逆作動薬)**: パーキンソン精神症で承認、統合失調症補助
- **KarXT (xanomeline + trospium)**: 2024 FDA 承認、ムスカリン作動薬 ⇒ **D2 を経由しない**初の薬

KarXT は ITU 観点で重要: **「K_precision を D2 以外の経路で restore できる**」 ことを示した世代交代の兆し。

---

## 6. Phase 68 数値検証

### 6.1 検証 1: Precision-weighting model
事前確率 vs 感覚証拠の bayesian update、precision ratio による幻覚誘発。

### 6.2 検証 2: 3 症状群への薬物反応率
CATIE データ整合性チェック。

### 6.3 検証 3: ドーパミン非対称性
mesolimbic 過剰 + mesocortical 不全のシミュレーション。

### 6.4 検証 4: 治療カスケード (1st → 2nd → Clozapine)
30% TRS の発生確率と Clozapine 救済率。

---

## 7. Phase 68 の結論

1. **統合失調症 = K_precision の破綻** (top-down と bottom-up のミスマッチ)
2. **陽性症状 = 薬で逆転可能、陰性・認知 = 構造的 K 欠失**
3. **ドーパミン仮説 = K_precision の生物物理的実装**
4. **抗精神病薬 = K_precision の薬理学的 restore** (粗 → 精緻 → 多受容体)
5. **TRS 30% = 多 K 破綻** ⇒ Clozapine の多受容体作用が必要
6. **KarXT (2024)** が D2 経路を経ない新世代薬として登場

Phase 69 では **大うつ病と不安障害** を扱い、**K_reward, K_threat** の破綻、SSRI、ketamine、psilocybin 等の作用を ITU で解析します。

---

## 引用

```
Terada, M. (2026). ITU and Psychiatry (Phase 67-70).
Tier 1 #7 application paper. In preparation.
```

参考:
- Sterzer et al. (2018) Biol Psychiatry 84, 634 (FEP and psychosis)
- Adams et al. (2013) Frontiers Psychiatry 4, 47 (precision and schizophrenia)
- Howes & Kapur (2009) Schizophr Bull 35, 549 (dopamine hypothesis revised)
- Lieberman et al. (2005) NEJM 353, 1209 (CATIE trial)
- Kane et al. (1988) Arch Gen Psychiatry 45, 789 (Clozapine in TRS)
- Brannan et al. (2021, 2024) NEJM (KarXT, xanomeline-trospium)
