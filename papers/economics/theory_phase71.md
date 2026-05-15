# Phase 71: 経済とは何か ― ITU が見る市場 = 集合的推論エンジン

> **Tier 1 #8 (Economics) — Phase 1/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> Tier 1 #1-#7 (engineering rectangle + medicine triangle): completed
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 71 の目的

engineering rectangle (#1-#4) + medicine triangle (#5-#7) 完成後、ITU は **社会人文科学** へ展開します。第一弾は **経済 / 情報市場**:

1. **市場 = 集合的 Bayesian 推論エンジン**
2. **価格 = 多数のエージェントの K_value の集約**
3. **情報非対称性** (Akerlof 1970) を ITU で再解釈
4. **効率的市場仮説 (EMH)** vs ITU 視点
5. **行動経済学** (Kahneman-Tversky) と K_decision の偏り
6. **予測市場** (Polymarket, Kalshi) = K の最高解像度実装
7. Phase 72-74 への基盤 (バブル, 不平等, AI 自動市場)

中心テーゼ:

> **市場は集合的 ITU 装置**:
> 個々のエージェントが $K_i$ (価値モデル) を持ち、取引で **$K_{\rm market} = \sum w_i K_i$ を集約**。
> 価格 = $\langle K_{\rm market}\rangle$、価格変動 = $\delta S = \delta\langle K_{\rm market}\rangle$。

---

## 1. ITU 経済学 ― 基礎概念の対応

### 1.1 価格・価値・情報

| 経済学概念 | ITU 解釈 |
|---|---|
| 市場価格 $P$ | 集合的 K_value の期待値 $\langle K_{\rm market}\rangle$ |
| ボラティリティ $\sigma$ | K_precision の逆数 |
| 出来高 | K_market 更新の頻度 |
| 情報非対称性 | エージェント間 $K_i \neq K_j$ |
| バブル | $\langle K_{\rm market}\rangle$ が fundamental から乖離 |
| クラッシュ | 急速な $K_{\rm market}$ reset (公理破綻からの復元) |

### 1.2 ITU 公理の市場版

$$\delta S_{\rm market}(\rho_{\rm price}) = \delta\langle K_{\rm market}\rangle$$

- $\rho_{\rm price}$: 価格分布 (時系列)
- $K_{\rm market}$: 集合的 valuation model
- 両者の等号が成立 = **市場が「健全」 に機能**

不成立時:
- $\delta S > \delta\langle K\rangle$: 価格が情報を上回って変動 ⇒ **過剰ボラティリティ**
- $\delta S < \delta\langle K\rangle$: 情報があるのに価格が動かない ⇒ **流動性危機**

---

## 2. Efficient Market Hypothesis (EMH) と ITU

### 2.1 Fama (1970) の EMH

3 形態:
- **Weak**: 過去価格に情報含まれる
- **Semi-strong**: 公開情報全てに含まれる
- **Strong**: インサイダー情報も含まれる

### 2.2 ITU 解釈

EMH = **市場が ITU 公理を完璧に satisfy する** 状態 (理想化)。
現実: 公理破綻が常に存在 ⇒ アービトラージ機会、超過リターン。

### 2.3 数値モデル

ランダムウォーク (EMH) vs 実市場:

| 指標 | EMH 予測 | 実観測 (S&P 500) |
|---|---|---|
| 1 日 returns 分布 | Gaussian | **fat-tailed** (Mandelbrot) |
| autocorrelation | 0 | 弱い負相関 |
| 大きな下落の頻度 | 極小 | **数年に 1 回** (LTCM, リーマン, COVID) |

⇒ ITU 視点: 実市場は **EMH からの逸脱頻発** ⇒ K-component の構造的破綻が起きる。

---

## 3. Akerlof Lemons モデル (1970)

### 3.1 古典的 setup

中古車市場:
- 売り手は車の品質を知る (information asymmetry)
- 買い手は知らない ⇒ 平均品質を仮定して価格付け
- 良質車の売り手は引っ込める ⇒ 平均品質が下がる
- ⇒ **悪循環で市場崩壊** (adverse selection)

### 3.2 ITU 解釈

エージェント K_i の不一致が **市場全体の K_market を破綻**させる:
- 高 K_i (情報あり) と低 K_i (情報なし) の混在
- 取引コストが ITU 公理違反を増幅
- ⇒ 市場流動性消失

### 3.3 解決策と ITU

| 解決策 | ITU 視点 |
|---|---|
| 保証 (warranty) | K_seller の情報を K_buyer に転送 |
| 認証 (certification) | 中立的 K_third party の導入 |
| ブランド | K_reputation を K_market に追加 |
| 規制 (lemon laws) | K_market の構造的修正 |

⇒ Phase 73 で詳述: AI が情報非対称性をどう変えるか。

---

## 4. 行動経済学 ― K_decision の偏り

### 4.1 主要バイアス (Kahneman-Tversky)

| バイアス | ITU 解釈 |
|---|---|
| 損失回避 (loss aversion) | K_threat > K_reward (uneven weighting) |
| アンカリング | K_prior が事後を支配 (Bayesian 過剰固定) |
| 利用可能性ヒューリスティック | K_memory の偏り |
| 確証バイアス | K_belief の自己強化 |
| 過信 | K_self_model の精度過大評価 |
| プロスペクト理論 | K_utility の S 曲線歪み |

### 4.2 数値モデル

期待効用理論 vs プロスペクト理論の予測差を確認 (図 c)。
ITU 視点: 行動経済学 = **「人間の K_decision は実際にどう壊れているか」 の実証**。

### 4.3 ノーベル経済学賞 (経済+心理融合)

- 2002: Kahneman (プロスペクト理論)
- 2017: Thaler (ナッジ)
- 2019: Banerjee-Duflo-Kremer (RCT in 経済学)

⇒ 行動経済学が**主流化**した 20 年。ITU 視点で「**K_decision の偏りを定量化**」 とまとめられる。

---

## 5. 予測市場 (Prediction Markets) ― ITU の最高解像度実装

### 5.1 主要プラットフォーム (2024)

| 市場 | 規模 | 特徴 |
|---|---|---|
| **Polymarket** | $9B 取引 (2024) | 仮想通貨ベース、政治・経済予測 |
| **Kalshi** | $1B (2024 CFTC 規制下) | 米法的に承認 |
| Manifold Markets | コミュニティ駆動 | 小規模だが密度高 |
| PredictIt | 大学運営 | 政治予測 |
| Augur, Gnosis | 完全分散 | 流動性課題 |

### 5.2 予測精度

2024 米大統領選:
- **Polymarket**: トランプ勝利確率 60% (10月末) ⇒ 的中
- **世論調査平均**: 50-50 (foa virtual tie)
- **専門家パネル**: ハリス優位

⇒ **予測市場が世論調査・専門家を一貫して上回る** (FiveThirtyEight 等の解析)。

### 5.3 ITU 解釈

予測市場 = **数千〜数百万エージェントの K を金銭インセンティブで集約**:
- 良い情報を持つエージェントは儲かる ⇒ 参加促進
- 集合 K_market = **「最高解像度の世界モデル」**
- ITU 公理が比較的厳密に成立

「**predictive K の集合知**」 が ITU 視点で最も「健全な市場」。

---

## 6. Phase 71 数値検証

### 6.1 検証 1: EMH vs 実市場の returns 分布

### 6.2 検証 2: Akerlof lemons モデル ― 市場崩壊シミュレーション

### 6.3 検証 3: プロスペクト理論 vs 期待効用 (損失回避)

### 6.4 検証 4: 予測市場精度 vs 世論調査 (2024 米大統領選)

---

## 7. Phase 71 の結論

1. **市場 = 集合的 ITU 装置**, 価格 = $\langle K_{\rm market}\rangle$
2. **EMH = ITU 公理が完璧に成立する理想状態**, 実市場は逸脱頻発
3. **Akerlof Lemons = K_i 不一致が市場全体を破綻**
4. **行動経済学 = K_decision の偏りの定量化**
5. **予測市場 = ITU 最高解像度実装** (世論調査を上回る精度)
6. **AI 時代 (Phase 73-74)**: agentic AI が market K にどう影響するか

Phase 72 では **バブルと金融危機**を ITU で解析: dot-com、住宅、暗号通貨バブルの構造的破綻パターン。

---

## 引用

```
Terada, M. (2026). ITU and Economics (Phase 71-74).
Tier 1 #8 application paper. In preparation.
```

参考:
- Akerlof (1970) Q J Econ 84, 488 (lemons market)
- Fama (1970) J Finance 25, 383 (EMH)
- Kahneman & Tversky (1979) Econometrica 47, 263 (prospect theory)
- Hayek (1945) Am Econ Rev 35, 519 (use of knowledge in society)
- Wolfers & Zitzewitz (2004) J Econ Perspectives 18, 107 (prediction markets)
- Hanson (1995) Foundations of Prediction Markets
- Mandelbrot (1963) J Bus 36, 394 (fat tails)
