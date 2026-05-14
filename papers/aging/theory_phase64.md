# Phase 64: 老化の三本柱 ― テロメア・ミトコンドリア・プロテオスタシス

> **Tier 1 #6 (Aging) — Phase 2/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 64 の目的

Phase 63 で「**老化 = K_organism の経時劣化**」 と「**12 Hallmarks**」 を確立しました。
Phase 64 では 12 hallmark のうち **3 つの中核機構**を分子レベルで深堀りします:

1. **Telomere attrition** (Hayflick limit, telomerase): K_replication の燃料計
2. **Mitochondrial dysfunction**: K_energy の劣化、heteroplasmy
3. **Loss of proteostasis**: タンパク質凝集 (Alzheimer's, Parkinson's の根源)

中心テーゼ:

> **3 hallmark は ITU の 3 つの根本 K-component に対応**:
> K_replication, K_energy, K_information_integrity。
> いずれかが**閾値以下**になると、他の hallmark も連鎖的に崩壊する (downstream cascade)。

---

## 1. Telomere Attrition: 複製カウンタの枯渇

### 1.1 物理機構

哺乳類の染色体末端には **テロメア** (TTAGGG 反復配列、初期 10-15 kb)。
DNA 複製の **end-replication problem** で、各細胞分裂で **50-100 bp 短縮**。
**~50 分裂 (Hayflick limit)** で限界 ⇒ 細胞老化 or apoptosis。

### 1.2 ITU 解釈

テロメア = **K_replication の整合性カウンタ**:
$$\rm telomere\_length(n) = L_0 - \delta_n \cdot n$$

n = 分裂数、$\delta_n$ = 1 分裂あたり短縮 ~70 bp。

短縮 ⇒ K_replication が低下 ⇒ 細胞は安全な複製を実施できない ⇒ ITU 公理を維持できないため senescence / apoptosis 選択。

### 1.3 例外と治療

| 系 | テロメラーゼ活性 | 動態 |
|---|---|---|
| 幹細胞・胚 | **強** | テロメア維持 |
| 体細胞 | ほぼ無 | 経時短縮 |
| **がん細胞** | **再活性化 (90%)** | 複製不死化 |
| マウス | 体細胞でも活性 | 種寿命は短い別要因 |

⇒ **テロメラーゼは諸刃の剣**: 老化抑制 vs がん促進。Phase 65 でテロメラーゼ補充療法の限界を議論。

---

## 2. Mitochondrial Dysfunction: エネルギー K の劣化

### 2.1 Free Radical Theory (Harman 1956)

ミトコンドリアの electron transport chain で **ROS (reactive oxygen species)** 生成。
ROS が mtDNA を傷つけ、修復不全で蓄積。

### 2.2 mtDNA 変異の蓄積

1 細胞あたり **100-10,000 個** のミトコンドリアが存在 ⇒ **heteroplasmy** (野生型 + 変異型の混在)。

ITU 視点:
- 各 mtDNA = K_energy の sub-instance
- 変異 mtDNA が **閾値 (60-80%) を超える** と細胞機能が崩れる ⇒ **threshold effect**

### 2.3 数値モデル

確率的シミュレーション (random walk):
- 1 細胞 = 1000 mtDNA
- 各分裂で各 mtDNA が ε = 10⁻⁴ の確率で変異
- 多数のヘテロプラスミー細胞 + ボトルネック効果 (oogenesis 等)
- 80 歳で平均 30% 変異 mtDNA、しかし**分布の長尾**で一部細胞は 80%+

### 2.4 ITU 解釈

K_energy = mtDNA aggregate fidelity。閾値超過細胞は **「ITU 破綻したエネルギー基盤」** で δS = δ⟨K⟩ を維持できない。

---

## 3. Loss of Proteostasis: 情報整合性の崩壊

### 3.1 機構

タンパク質品質管理系:
- **シャペロン** (HSP70, HSP90): 折りたたみ補助
- **UPS** (ubiquitin-proteasome system): 不良タンパク質分解
- **Autophagy**: 大規模 recycling

加齢で全 3 系が**低下** ⇒ misfold タンパク質が蓄積 ⇒ 凝集体形成。

### 3.2 神経変性疾患との関係

| 疾患 | 凝集タンパク | 部位 |
|---|---|---|
| Alzheimer's | **Aβ (amyloid-β) + tau** | 脳全体 |
| Parkinson's | **α-synuclein** | 黒質 |
| Huntington's | polyQ huntingtin | 線条体 |
| ALS | TDP-43, SOD1 | 運動ニューロン |
| プリオン病 | PrP^Sc | 全身/脳 |

### 3.3 Prion-like 伝播

最新理解: **凝集体は「種」 となって周辺の正常タンパク質を misfold させる** (prion-like)。

ITU 視点:
- 各タンパク質 = K_information_integrity の sub-instance
- 凝集体 = **「ITU 破綻の伝染源**」 ⇒ 慢性的 K 劣化を加速
- Phase 63 の senescent cells と同様、**老化破綻の局所的増幅機構**

### 3.4 閾値モデル

凝集タンパク濃度 $C$ が臨界 $C_c$ を超えると **核形成爆発**:
$$\frac{dC}{dt} = k_{\rm prod} - k_{\rm clear} C - \text{prion-like} \cdot C^n$$

加齢で $k_{\rm clear}$ 低下 ⇒ $C$ が $C_c$ 超 ⇒ **発症**。

---

## 4. 3 機構の相互作用 ― ITU の連鎖

### 4.1 Downstream cascade

```
mtDNA mutation (K_energy↓)
       ↓
ATP不足 → autophagy 不全 (K_information↓)
       ↓
proteotoxic stress
       ↓
シャペロン枯渇 → 凝集体形成
       ↓
細胞 senescence (Hayflick + 凝集ストレス)
       ↓
SASP → 周辺細胞の K_immune, K_metab を劣化
       ↓
組織レベルの inflammaging (Hallmark 11)
```

⇒ ITU 観点: **3 機構の劣化は独立ではなく、互いの K を引き下げる正のフィードバック**。だから老化は加速度的。

### 4.2 介入の階層

| 介入レベル | 標的 K | 例 |
|---|---|---|
| **テロメア** | K_replication | テロメラーゼ補充 (TA-65 等) |
| **ミトコンドリア** | K_energy | MitoQ, NAD+ booster |
| **プロテオスタシス** | K_information | autophagy inducer (rapamycin), HSP inducer |

Phase 65 で各介入の現状と ITU 視点での評価を行います。

---

## 5. Phase 64 数値検証

### 5.1 検証 1: Telomere kinetics + Hayflick
分裂数 vs テロメア長 + 細胞老化転換点。

### 5.2 検証 2: mtDNA heteroplasmy random walk
1000 細胞 × 1000 mtDNA、80 年シミュレーション、80% threshold 超過率。

### 5.3 検証 3: Protein aggregation threshold
$C(t)$ の時間発展、加齢に伴う発症年齢分布。

### 5.4 検証 4: 3-axis K-fidelity composite
Telomere × Mito × Proteo の積分 K_overall。

---

## 6. Phase 64 の結論

1. **Telomere = K_replication の燃料計**, Hayflick = ITU 維持限界
2. **mtDNA heteroplasmy = K_energy の閾値現象**, 高変異率細胞が老化を加速
3. **Proteostasis = K_information_integrity**, 凝集体が prion-like に伝播 ⇒ 慢性 ITU 破綻源
4. **3 機構は相互に強化し合う正のフィードバック**
5. **介入は 3 軸独立では不十分** ⇒ Phase 65 で combination longevity 戦略

Phase 65 では **rapamycin, metformin, senolytics, NAD+** 等の介入を ITU で評価し、**実臨床への翻訳**を議論します。

---

## 引用

```
Terada, M. (2026). ITU and Aging (Phase 63-66).
Tier 1 #6 application paper. In preparation.
```

参考:
- Hayflick & Moorhead (1961) Exp Cell Res 25, 585 (Hayflick limit)
- Harman (1956) J Gerontol 11, 298 (free radical theory)
- Wallace (2010) Mitochondrion 10, 12 (heteroplasmy)
- Selkoe (2003) Nat Med 9, 1024 (proteostasis in neurodeg)
- Sinclair (2019) Lifespan
- Soto & Pritzkow (2018) Nat Neurosci 21, 1332 (prion-like propagation)
