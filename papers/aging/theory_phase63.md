# Phase 63: 老化とは何か ― K_organism の経時劣化と Sinclair の情報理論

> **Tier 1 #6 (Aging) — Phase 1/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> Tier 1 #5 (Cancer Biology): [10.5281/zenodo.20174318](https://doi.org/10.5281/zenodo.20174318)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 63 の目的

Tier 1 #5 (Cancer) では「**急性 K 破綻**」 を扱いました。Tier 1 #6 (Aging) では「**慢性 K 劣化**」:

1. **老化 = K_organism の経時的劣化** (decades scale)
2. **12 Hallmarks of Aging** (López-Otín 2023) を ITU で K-component に対応付け
3. **Gompertz 死亡則** ($e^{\alpha t}$ 法則) を ITU で導出
4. **Horvath 表観遺伝時計 (2013)** = K-fidelity meter
5. **Sinclair 情報理論的老化説** (2019) と ITU の関係
6. **がん vs 老化**: 急性 vs 慢性 K 破綻の対比

中心テーゼ:

> **老化 = $\delta\langle K_{\rm organism}\rangle$ の単調減少**
> がんは局所的・急性、老化は全身的・慢性。両者とも ITU 公理破綻だが時間スケールが異なる。

---

## 1. 老化の物理: 時間と共に K が劣化する

### 1.1 ITU 公理の時間依存版

健康若年体:
$$\delta S(\rho_A) = \delta\langle K_A^{(0)}(t)\rangle$$

加齢:
$$K_A^{(0)}(t_{\rm old}) < K_A^{(0)}(t_{\rm young})$$

⇒ K-fidelity が経時的に低下。臨界点で $\delta S > \delta\langle K\rangle$ ⇒ 死亡。

### 1.2 がんとの対比

| | がん (Tier 1 #5) | 老化 (Tier 1 #6) |
|---|---|---|
| 時間スケール | 月〜年 | decades |
| 範囲 | 局所 (細胞・組織) | 全身 (organism) |
| K の破綻 | 急性 (driver mutation) | 慢性 (緩やかな drift) |
| 主因 | 数 hits の lethal failure | 多 K-component の同時劣化 |
| 結末 | 制御不能増殖 | 機能不全死亡 |

⇒ **両者は ITU 公理破綻の 2 つのモード**: catastrophic vs cumulative。

---

## 2. 12 Hallmarks of Aging (López-Otín 2023)

最新版 (Cell 2023) では 12 hallmark:

| # | Hallmark | ITU 解釈 (どの K-component) |
|---|---|---|
| 1 | Genomic instability | DNA 修復 K の劣化 |
| 2 | **Telomere attrition** | **K_replication の指標** (Hayflick limit) |
| 3 | Epigenetic alterations | **DNA メチル化 K の drift** ★ |
| 4 | Loss of proteostasis | タンパク質品質管理 K |
| 5 | Disabled macroautophagy | リソース recycling K |
| 6 | Deregulated nutrient sensing | mTOR/AMPK K の hijack |
| 7 | Mitochondrial dysfunction | エネルギー K の劣化 |
| 8 | Cellular senescence | 細胞周期 K の異常 |
| 9 | Stem cell exhaustion | 再生 K の枯渇 |
| 10 | Altered intercellular communication | サイトカイン K の drift |
| 11 | **Chronic inflammation** (inflammaging) | **免疫 K の慢性活性化** |
| 12 | **Dysbiosis** | **微生物叢 K の崩壊** ★ NEW |

⇒ **老化は 12 種類の K-component が並行劣化**する複合現象。

---

## 3. Gompertz 死亡則 ― ITU 公理の経時帰結

### 3.1 経験則 (1825 年!)

死亡率 $\mu(t)$ は年齢と共に指数的に増加:

$$\mu(t) = A e^{\alpha t}$$

ヒトの $\alpha \approx 0.085$ /yr ⇒ **死亡率が 8 年ごとに倍増**。

### 3.2 ITU 導出

K-fidelity の時間発展を一次劣化:

$$\frac{d\langle K\rangle}{dt} = -\beta\langle K\rangle$$

⇒ $\langle K(t)\rangle = K_0 e^{-\beta t}$

死亡確率 $\propto 1/\langle K\rangle = e^{\beta t}/K_0$

⇒ **Gompertz 則 (exp(αt)) は K の指数劣化の自然帰結**。 $\alpha = \beta$。

### 3.3 種差

| 種 | 最大寿命 (yr) | $\alpha$ (/yr) | $K_0$ |
|---|---|---|---|
| マウス | 4 | 0.7 | 中 |
| イヌ | 20 | 0.15 | 中 |
| ヒト | **122 (Calment)** | **0.085** | 高 |
| クジラ (bowhead) | 200+ | 0.04 | 高 |
| ロブスター | (?) negligible senescence | ~0 | — |
| Hydra | immortal | 0 | — |

ITU 解釈: 種ごとに **初期 K-fidelity $K_0$** と **劣化率 $\beta$** が遺伝的に決まる。

---

## 4. Horvath 表観遺伝時計 (2013) = K-fidelity meter

Steve Horvath (UCLA, 2013, Genome Biology): **DNA メチル化 353 サイト**から「**生物学的年齢**」 を予測。
- 暦年齢との相関 r > 0.95
- 異なる組織でも同じ時計が動く
- 健康ライフスタイルで時計が**遅く**、ストレスで**速く**進む

ITU 解釈:
> DNA メチル化パターン = K_epigenetic の状態空間。
> 時計の進行 = $\langle K_{\rm epi}(t)\rangle$ の単調減少。

これは Sinclair の「**情報理論的老化説**」 (2019) と直接整合。

---

## 5. Sinclair 情報理論的老化説

David Sinclair (Harvard, 2019, Cell): **老化 = epigenetic 情報の損失**。

- 細胞が「自分は若い肝細胞」 という epigenetic identity を持つ
- DNA 損傷修復時に **エピゲノムが噪音化** ⇒ 細胞がアイデンティティ喪失
- **Yamanaka factors (OSKM)** で部分的 reprogramming ⇒ epigenetic 若返り

ITU 解釈: Sinclair の仮説は **ITU 公理の老化版**:
- 情報損失 = δS 増加 (organism スケール)
- それを補償する K 機構 (修復・autophagy) も同時に劣化
- ⇒ $\delta S > \delta\langle K\rangle$ で死亡に到達

**ITU は Sinclair の数学的基盤を提供**。

---

## 6. 細胞老化 (Cellular Senescence) と SASP

### 6.1 メカニズム

複製限界 (Hayflick) に達した細胞は **senescent state** に入る:
- 分裂停止 (cell cycle arrest)
- 抗 apoptosis (BCL-2 高発現) ⇒ 死なずに残る
- **SASP** (Senescence-Associated Secretory Phenotype): 炎症性サイトカイン分泌

### 6.2 ITU 視点

Senescent cell = **K_replication が破綻したが K_apoptosis も破綻**した cell。
- ITU 破綻が partial mode で固定
- SASP = 周辺細胞の K を劣化させる「**ITU 破綻の伝播**」

⇒ **老化は senescent cells によって伝染する**。Phase 65 の **senolytics** (senescent cell を殺す薬) が原理上 K_organism を restore できる。

---

## 7. Phase 63 数値検証

### 7.1 検証 1: Gompertz fit
ヒト・マウス・イヌの死亡率カーブを Gompertz でフィット、α 推定。

### 7.2 検証 2: 12 Hallmarks K プロファイル
若年 (年齢 25) vs 老年 (年齢 80) の K-component スパイダーチャート。

### 7.3 検証 3: Horvath methylation clock vs chronological age
シミュレーションで生物学的年齢と暦年齢の相関を確認。

### 7.4 検証 4: 種別 最大寿命と $\alpha$ の関係
8 種比較プロット (マウス〜クジラ〜ヒト)。

---

## 8. Phase 63 の結論

1. **老化 = K_organism の経時的指数劣化** ($\langle K(t)\rangle = K_0 e^{-\beta t}$)
2. **Gompertz 死亡則は ITU 公理の自然帰結**
3. **12 Hallmarks = 12 K-component の並行劣化**
4. **Horvath 時計 = K_epigenetic-fidelity meter**
5. **Sinclair 情報理論 = ITU の老化版**, OSKM = K 部分復元
6. **Cellular senescence = ITU 破綻の partial mode + 伝播**
7. **がん (急性) と老化 (慢性) は同じ公理破綻の 2 時間スケール**

Phase 64 では **telomere, mitochondria, proteostasis** の 3 つの hallmark を深堀りし、それぞれの分子機構と ITU の関係を詳述します。

---

## 引用

```
Terada, M. (2026). ITU and Aging (Phase 63-66).
Tier 1 #6 application paper. In preparation.
```

参考:
- López-Otín et al. (2013, 2023) Cell 153, 1194 / 186, 243 (Hallmarks of Aging)
- Gompertz (1825) Phil Trans R Soc 115, 513 (mortality law)
- Hayflick & Moorhead (1961) Exp Cell Res 25, 585 (Hayflick limit)
- Horvath (2013) Genome Biol 14, R115 (DNA methylation clock)
- Sinclair & LaPlante (2019) "Lifespan: Why We Age—and Why We Don't Have To"
- Yamanaka & Takahashi (2006) Cell 126, 663 (OSKM reprogramming)
- Tchkonia et al. (2013) JCI 123, 966 (cellular senescence)
