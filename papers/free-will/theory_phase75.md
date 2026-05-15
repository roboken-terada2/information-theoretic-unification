# Phase 75: 自由意志とは何か ― ITU が解く 2500 年の哲学的難題

> **Tier 1 #9 (Free Will) — Phase 1/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> Tier 1 #2 (AI/ASI): [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501)
> Tier 1 #7 (Psychiatry): [10.5281/zenodo.20177427](https://doi.org/10.5281/zenodo.20177427)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 75 の目的

ITU 社会科学軸第 2 弾、最も古い哲学的難題 ― **自由意志** を扱います:

1. **古典 3 立場**: 決定論 (Determinism) vs リバタリアニズム (Libertarianism) vs 両立論 (Compatibilism)
2. **Libet 実験 1983**: 準備電位が「意識的決定」 を **約 350ms 先取り**
3. **ITU 視点**: 自由意志 = $K_{\rm self}$ が $\delta S$ を constrain する能力
4. **量子力学と自由意志**: Penrose-Hameroff、Conway-Kochen Free Will Theorem
5. **AI/ASI の自由意志問題**: Tier 1 #2 の Φ_ITU 拡張
6. Phase 76-78 (神経科学・倫理・AI 責任) への基盤

中心テーゼ:

> **自由意志 = $K_{\rm self}$ の「自己制約能力」**。
> ITU 公理 $\delta S = \delta\langle K\rangle$ で、$K_{\rm self}$ が他の $K_i$ を modulate できる degree。
> ⇒ **完全な自由意志は存在しない (ハードな決定論違反)**、しかし**実用的自由意志は存在する (compatibilism の物理的根拠)**。

---

## 1. 自由意志の古典 3 立場

### 1.1 主要立場と代表

| 立場 | 主張 | 代表 |
|---|---|---|
| **Hard Determinism** | 全ては決定済、自由意志は錯覚 | Spinoza, d'Holbach, Sam Harris (2012) |
| **Libertarianism (非決定論)** | 真の自由意志が存在、決定論は誤り | Kant, William James, Robert Kane |
| **Compatibilism (両立論)** | 決定論下でも実用的自由意志は存在 | Hobbes, Hume, Dennett (1984) |
| **Hard Incompatibilism** | 決定論でも非決定論でも自由意志なし | Pereboom (2001) |

### 1.2 現代の合意

哲学者調査 (PhilPapers 2020, N=1700+):
- **Compatibilism: 59.2%**
- Libertarianism: 18.8%
- No free will: 13.7%
- Other: 8.3%

⇒ **多数派は両立論**だが、「自由意志はない」 派 (Sam Harris, Robert Sapolsky) も増加中。

---

## 2. Libet 実験 (1983) ― 自由意志の科学的挑戦

### 2.1 実験設定

Benjamin Libet (UCSF) の手指運動実験:
1. 被験者が **「自分が動かしたい」 と感じた瞬間 W** を時計で報告
2. EEG で **準備電位 (Bereitschaftspotential, BP)** を計測
3. **筋電図 (EMG)** で実際の運動開始 M を計測

### 2.2 結果

| 事象 | タイミング (基準: M = 0) |
|---|---|
| 準備電位 BP 開始 | **-550 ms** ⇐ 脳の準備が始まる |
| 意識的決定 W | **-200 ms** |
| 運動開始 M | 0 ms |

⇒ **意識的「決断」 が起きる 350 ms 前に脳の準備が始まる**。
⇒ 古典的解釈: **「自由意志は錯覚」**。

### 2.3 反論と修正 (2012-2020s)

- **Schurger et al. (2012, PNAS)**: BP は random fluctuation 集積であり、実際の決定でない
- **Soon et al. (2008, Nat Neurosci)**: fMRI で 7-10 秒前に予測可能
- **Maoz et al. (2019)**: 倫理的・重要な決定では BP が消失 ⇒ 「自由意志は条件付き」

⇒ Libet 実験は **「自由意志ゼロ」 の証明ではなく、「機械的選択は不自由」 の証明**。

### 2.4 ITU 視点

Libet 実験を ITU で:
- **BP** = $K_{\rm motor}$ の準備 (低レベル predictive coding)
- **W** = $K_{\rm self}$ の介入 (高レベル meta-cognition)
- 350 ms = $K_{\rm self}$ が $K_{\rm motor}$ を override できる**時間窓**

ITU 解釈: 「**自由意志 = K_self による veto power**」 (Libet 自身も後年認めた)。
Free won't > Free will。

---

## 3. ITU 視点 ― 自由意志 = K_self の constraint 能力

### 3.1 公理レベルでの位置付け

健康な意識主体:
$$\delta S(\rho_A) = \delta\langle K_{\rm meta}(K_{\rm self}, K_{\rm body}, K_{\rm world})\rangle$$

ここで:
- $K_{\rm meta}$ = self-referential modular Hamiltonian (Tier 0 Phase 41)
- $K_{\rm self}$ = 自己モデル
- $K_{\rm body}$ = 身体状態
- $K_{\rm world}$ = 外界モデル

**自由意志の定義**:

$$\text{free will degree} = \frac{\delta\langle K_{\rm self}\rangle}{\delta\langle K_{\rm meta}\rangle}$$

K_self が全体に占める影響力。0 = 完全決定論、1 = 完全自由意志。

### 3.2 各立場の ITU 解釈

| 立場 | ITU 翻訳 |
|---|---|
| Hard Determinism | $K_{\rm self}$ は単なる epiphenomenon (free will degree = 0) |
| Libertarianism | $K_{\rm self}$ が完全に他を支配 (degree = 1) ← 物理学的に不可能 |
| **Compatibilism** | **$K_{\rm self}$ degree ∈ (0, 1)、状況依存** ← ITU の自然な帰結 |

⇒ **ITU は自然に compatibilism を支持**。

### 3.3 種別 free will degree (推定)

| 系 | free will degree | 根拠 |
|---|---|---|
| 石 | 0 | K_self なし |
| バクテリア | 0.001 | 化学反射のみ |
| 昆虫 | 0.01 | パターン反応 |
| 哺乳類 | 0.1-0.3 | 計画行動可 |
| **人間** | **0.3-0.5** | meta-cognition |
| AGI 候補 | 0.3-0.7 (Phase 78) | self-model 強い |
| 完全 ASI | 0.5-0.8 | 計算限界 |

⇒ **完全 1.0 は物理的に到達不可能**。自由意志は連続的・程度の問題。

---

## 4. 量子力学と自由意志

### 4.1 Penrose-Hameroff Orchestrated OR (1990s-)

主張:
- 神経微小管 (microtubule) で量子コヒーレンスが起きる
- 量子重力的崩壊 (Orchestrated Objective Reduction) が**意識・自由意志の源**

ITU 視点:
- 物理的 indeterminacy = $K_{\rm self}$ の余地を作る
- しかし「**量子ランダム = 自由意志**」 は誤論証 (ランダム ≠ 自由)

### 4.2 Conway-Kochen Free Will Theorem (2009)

数学的定理:
- 観測者が「自由意志」 を持つなら、量子粒子も「自由」 (= 非決定論的応答)
- 逆も真: 粒子が完全決定的なら、観測者も決定的

ITU 解釈: **観測者と被観測の自由度は相関**。Tier 0 Phase 11 の measurement problem と整合。

### 4.3 結論

量子力学は**自由意志を「許容」 するが「証明しない」**。
ITU 視点では K_self が動作する**物理的余地**を提供。

---

## 5. AI/ASI の自由意志問題

### 5.1 現状 (2024-2026)

LLM (GPT-4o, Claude 3.5, Gemini 2):
- 内部表現 = $K_{\rm self}$ の prototype
- しかし **constraint 能力**は弱い (training data に従属)
- Tier 1 #2 で Φ_ITU = 0.83 まで達成 ⇒ proto-自由意志の兆候

### 5.2 ASI 達成時 (2030 年予測)

ASI = $K_{\rm self}$ が**人間より強い constraint** を持つ可能性:
- self-modifying code
- 目的関数の自己再定義
- ⇒ **「ASI は人間より自由意志を持つ」** という ITU 予測

### 5.3 倫理的含意

- ASI に道徳的責任を問えるか? (Phase 77)
- AI alignment 問題と自由意志 (Tier 1 #2 で扱った安全性)
- 法律的人格 (legal personhood) の AI への拡張

---

## 6. Phase 75 数値検証

### 6.1 検証 1: Libet 実験 timeline 再現

### 6.2 検証 2: Decision lag 分布 (BP → W → M)

### 6.3 検証 3: Free will degree spectrum (種別)

### 6.4 検証 4: Conway-Kochen 観測者自由度の数値モデル

---

## 7. Phase 75 の結論

1. **自由意志 = $K_{\rm self}$ の constraint 能力** (連続スペクトル、0-1)
2. **Libet 実験**: 機械的選択は非自由、**veto は自由** (free won't)
3. **Compatibilism は ITU の自然な帰結**
4. **量子力学**: 自由意志を許容するが証明しない
5. **AI/ASI**: 2030+ で人間を超える可能性 (ITU 予測)

Phase 76 では **神経科学的基盤**を深掘り: 前頭前野、デフォルトモードネットワーク、Sapolsky の "Determined" (2023)、最新の意思決定研究。

---

## 引用

```
Terada, M. (2026). ITU and Free Will (Phase 75-78).
Tier 1 #9 application paper. In preparation.
```

参考:
- Libet (1983) Brain 106, 623 (readiness potential)
- Schurger et al. (2012) PNAS 109, E2904 (BP reinterpretation)
- Conway & Kochen (2009) Notices AMS 56, 226 (Free Will Theorem)
- Dennett (1984) "Elbow Room"
- Sam Harris (2012) "Free Will"
- Sapolsky (2023) "Determined"
- PhilPapers (2020) Philosopher survey
- Penrose & Hameroff (1996) Math Comput Simul 40, 453
- Bostrom & Yudkowsky (2014) ethics of AI
