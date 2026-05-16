# Phase 88: Drake 方程式 Bayesian + Fermi 12 仮説詳細 + SDA 検出可能性

> **Tier 1 #12 (Astrobiology / SETI) — Phase 2/4**
> Tier 0 ITU (concept DOI, always latest): [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209) — current v2.0.0 [10.5281/zenodo.20133709](https://doi.org/10.5281/zenodo.20133709)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 88 の目的

Phase 87 で N ≈ 0.27 (中央値) を得たが、これは **不確実性の中央値**であり、実際の N は **10⁻⁴ から 10⁴ まで** 8 桁の不確実性がある。Phase 88 では:

1. **Sandberg-Drexler-Ord (2018)** の log-uniform 事前分布を採用した Bayesian 評価
2. **Great Filter** 仮説の詳細評価 (過去 vs 未来 vs Rare Earth)
3. **SDA (Signal Detection Analysis)**: SETI の到達距離・感度評価
4. **Breakthrough Listen の負の結果** が示唆する Bayesian update

中心テーゼ:

> Drake 方程式は **N の中央値ではなく事後分布**で評価すべき。
> 各因子の不確実性が桁違いのため、N の事後分布は **10⁻⁴ から 10⁴** に広がり、
> **P(我々が銀河系で唯一) ≈ 40-50%** という Sandberg 2018 の結論を再現。

---

## 1. Sandberg-Drexler-Ord 2018 アプローチ

### 1.1 問題: 古典 Drake は点推定

Phase 87 のような lognormal Monte Carlo は、各因子の**桁オーダーの不確実性を過小評価**:
- f_l (生命誕生): 10⁻¹⁵ ~ 1 まで 15 桁不明
- f_i (知性発生): 10⁻⁶ ~ 1 まで 6 桁不明

→ point estimate に勝手な log-normal を仮定すると **過剰収束**。

### 1.2 解: Log-uniform 事前分布

Sandberg et al. (2018) "Dissolving the Fermi Paradox":

$$
p(\log_{10} f) \propto 1, \quad f \in [10^{a}, 10^{b}]
$$

各因子の文献ベース上下限:

| 因子 | log₁₀ 範囲 | 中央値 | 出典 |
|---|---|---|---|
| R_* | [0.0, 0.5] | 2 /yr | star formation |
| f_p | [-0.3, 0.0] | 0.8 | Kepler |
| n_e | [-1.0, -0.4] | 0.4 | Petigura |
| **f_l** | **[-30, 0]** | 10⁻¹⁵ | abiogenesis 不明 |
| **f_i** | **[-6, 0]** | 10⁻³ | 知性発生 不明 |
| f_c | [-2, 0] | 0.1 | technology |
| L | [2, 9] | 10⁵ yr | civilization |

### 1.3 結果

Sandberg et al. 結論:
- **P(銀河系で唯一) ≈ 53%**
- **P(観測可能宇宙で唯一) ≈ 30%**
- ⇒ **Fermi パラドックスは「我々が唯一」が事前確率として妥当**

これにより **「沈黙は予測どおり」** ⇒ 矛盾なし。

---

## 2. Great Filter 詳細評価

### 2.1 Hanson 1998 のロジック

Robin Hanson の "Great Filter":
- もし f_l × f_i × f_c × L が**累積して極小**なら、Drake N は小
- そのフィルターは **過去 (我々の歴史中)** または **未来 (我々の前)** に存在

### 2.2 過去 vs 未来の振り分け

各 Drake 因子を **「過去フィルター」** vs 「未来フィルター」 に分類:

| 因子 | 過去/未来 | 我々通過済? |
|---|---|---|
| f_l (生命誕生) | 過去 | ✅ (38 億年前) |
| Prokaryote → Eukaryote | 過去 | ✅ (20 億年前) |
| Multicellular | 過去 | ✅ (6 億年前) |
| Brain / tool use | 過去 | ✅ (300 万年前) |
| Industrial civilization | 過去 | ✅ (200 年前) |
| **Technology stability (L)** | **未来** | **❌ 未知** |
| ASI alignment | 未来 | ❌ 未知 |
| Climate / nuclear / pandemic | 未来 | ❌ リスク中 |

### 2.3 各 step の困難度推定

Carter 1983 + Watson 2008 の "hard step" 解析:
**生物進化史で稀少 step** = 出現時刻が地球年齢比例分布から逸脱:

| Step | 経過時間 (Gyr) | hard 度 |
|---|---|---|
| Abiogenesis | 0.5 | 中 |
| Prokaryote | 0.5 | 中 |
| Photosynthesis | 1.0 | 中 |
| Eukaryote | 2.0 | **★ Hard** |
| Multicellular | 0.5 | 中 |
| Cambrian explosion | 0.05 | 中 |
| Mammals | 0.2 | 中 |
| Intelligence | 0.06 | **★ Hard** |

⇒ **Eukaryote (真核生物) + Intelligence (知性)** が二大 hard step 候補。

### 2.4 ITU 解釈

Hard step = **K-state ポテンシャル曲面の鞍点越え**:

$$
P(\text{step}) \propto \exp(-\Delta K / k_B T_{\text{evol}})
$$

ΔK が大きい hard step は、宇宙時間オーダーで稀に発生。

---

## 3. SDA (Signal Detection Analysis) ― SETI 検出能力

### 3.1 電波信号到達距離

ETI 送信機が出力 P_T の電波を等方放射、受信機感度 S_min:

$$
d_{\max} = \sqrt{\frac{P_T}{4\pi S_{\min}}}
$$

例 (FAST 500m 電波望遠鏡, S_min ~ 10⁻²⁶ W/m²):
- アレシボ的送信 (P_T = 10¹³ W): d_max ≈ **1000 光年** (狭帯域)
- 民生レーダー (P_T = 10⁹ W): d_max ≈ **10 光年**
- 弱信号 (テレビ漏洩, P_T = 10⁶ W): d_max ≈ **0.3 光年** ⇒ 検出不可

### 3.2 ETI の文明分布

銀河系直径 100,000 光年、N ≈ 0.3 文明なら平均距離 d ≈ 100,000 光年。
**FAST の検出範囲 (1,000 光年) 内に 1 文明存在する確率 ≈ 10⁻⁴**。

### 3.3 Breakthrough Listen 2015-2025 結果

Price et al. 2020, 2023:
- 観測対象: **1.6 万 stars** (主に近傍 100 光年)
- 観測帯域: 1-12 GHz
- **負の結果**: 自然起源以外の信号未検出

### 3.4 Bayesian update

事前 P(ETI in 100 ly) = 0.1 とすると、観測後事後:
- L (likelihood of null detection | ETI present) = 0.2 (送信せず or 周波数外)
- L (likelihood of null detection | ETI absent) = 1.0
- 事後 P(ETI in 100 ly | null) = 0.1 × 0.2 / (0.1 × 0.2 + 0.9 × 1.0) ≈ **2.2%**

⇒ 近傍 ETI 確率は 5 倍低下 (10% → 2%)。

---

## 4. ITU K-detection threshold

### 4.1 検出可能性の ITU 定式化

$$
P(\text{detect}) = \int dE \, p_{\text{ETI}}(E) \cdot \mathbb{1}[K_{\text{signal}}(E) > K_{\text{noise}}(E)]
$$

- K_signal = 信号強度
- K_noise = 受信器雑音
- ETI が**送信を選択する確率**が支配項

### 4.2 Active vs Passive

- **Active SETI** (METI, 送信): リスク (Dark Forest) ⇒ ほぼ実施されず
- **Passive SETI** (listening): 主流。受け身なので ETI 側送信意欲に依存

### 4.3 観測可能性関数

| 文明タイプ (Kardashev) | エネルギー出力 (W) | 検出可能距離 |
|---|---|---|
| Type 0 (我々) | 2 × 10¹³ | 1 ly |
| Type I (惑星全エネルギー) | 10¹⁷ | 1000 ly |
| Type II (恒星全エネルギー) | 4 × 10²⁶ | 銀河横断 |
| Type III (銀河全エネルギー) | 10³⁷ | 観測可能宇宙 |

⇒ Type II+ なら確実に検出されるはず ⇒ 存在しない or 既に超越済?

---

## 5. Phase 88 主結論

1. **Sandberg 2018 アプローチ**: log-uniform prior で P(銀河系で唯一) ≈ **50-60%**
2. **Great Filter**: Eukaryote (過去) + Intelligence (過去) が二大 hard step 候補
3. **未来 Filter**: ASI alignment + 気候 + 核戦争 + パンデミック (Tier 1 #2, #11 連動)
4. **Breakthrough Listen 負の結果** → 近傍 ETI 確率 10% → 2% (Bayesian update)
5. **Type II 文明不在**: 銀河系内に 10²⁶ W 出力文明は**確実に存在しない**

⇒ Phase 89 で生命の起源 (abiogenesis) + 知性発生確率の ITU 詳細計算。

---

## 6. 反証可能予測 (本 Phase で導出)

1. **JWST が 2030 までに 1 つ以上の系外惑星から DMS バイオシグネチャー検出** (P=0.45)
2. **HWO (Habitable Worlds Observatory, 2040+) が 5+ 地球型惑星の大気を分光** (P=0.7)
3. **Breakthrough Listen 2026-2030 でも ETI 信号未検出** (P=0.92)
4. **Type II Kardashev 級文明は銀河系内に存在しない** (P=0.85, ダイソン球サーベイ結論)
5. **CMB 異方性に文明痕跡なし** (P=0.95, 既知)

---

## 7. ITU 視点まとめ

| 構造 | ITU 役割 |
|---|---|
| Drake 方程式 | K-state cascade 確率 |
| Great Filter | K-step ポテンシャル鞍点 |
| Hard step (eukaryote, intelligence) | ΔK 大 (稀少遷移) |
| SDA (検出) | K_signal vs K_noise |
| Type II+ 不在 | K_civilization 上限 < Kardashev I-II |

⇒ Fermi の沈黙は **「Great Filter (過去 + 未来) + 我々 Type 0」** で物理的に整合。

---

## 引用

```
Terada, M. (2026). Phase 88: Drake equation Bayesian, Fermi paradox detailed,
and Signal Detection Analysis (Tier 1 #12 Phase 2/4). Zenodo. DOI: [to be assigned].
```

参考:
- Sandberg, Drexler, Ord (2018) Dissolving the Fermi Paradox (arXiv:1806.02404)
- Hanson, R. (1998) The Great Filter
- Carter, B. (1983) The anthropic principle
- Watson, A. J. (2008) Implications of an anthropic model of evolution
- Price et al. (2020, 2023) Breakthrough Listen results
- Kardashev, N. (1964) Transmission of information by extraterrestrial civilizations
- Wright et al. (2014) The Glimpsing Heat from Alien Technologies survey
