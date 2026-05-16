# Phase 59: がんとは何か ― ITU が見る dS = d⟨K⟩ の細胞レベル破綻

> **Tier 1 #5 (Cancer Biology) — Phase 1/4**
> Tier 0 ITU: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 1 #1-#4 (engineering rectangle): completed
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 59 の目的

engineering 4 部作 (Tier 1 #1-#4) を完成し、ITU は **engineering → medicine** に展開します。最初のテーマは **がん**:

1. **健康細胞**: ITU 公理 $\delta S = \delta\langle K\rangle$ が厳密に成立
2. **がん細胞**: 公理が破綻 ($\delta S \gg \delta\langle K\rangle$ もしくは $\delta\langle K\rangle$ が腐敗)
3. **The Hallmarks of Cancer** (Hanahan-Weinberg 2000/2011/2022) を ITU 言語で再分類
4. **Two-hit 仮説** (Knudson 1971) を redundant K-control で説明
5. Phase 60-62 (代謝, 免疫, 治療) への基盤

中心テーゼ:

> **がんは細胞・組織レベルでの $\delta S = \delta\langle K\rangle$ 破綻である。**
> 健康細胞は QECC のように regulatory K が S を抑える ⇒ がんは syndrome detection と error correction の両方が破綻した状態。

---

## 1. 細胞は ITU で見ると何か

### 1.1 健康細胞の ITU 表記

部分系 A = 単一細胞、$\rho_A$ = 細胞状態 (遺伝子発現プロファイル + 代謝状態)、$K_A$ = 細胞内 regulatory ネットワーク (転写因子, シグナル伝達, DNA repair, apoptosis 機構)。

ITU 公理:

$$\delta S(\rho_A) = \delta\mathrm{Tr}[K_A^{(0)} \rho_A]$$

- 左辺 $\delta S$: 細胞状態の不確実性変化 (= 増殖, 分化, 死)
- 右辺 $\delta\langle K\rangle$: regulatory ネットワークの仕事 (= シグナル受信, 遺伝子発現, 修復)

両者が等しい ⇒ **細胞は環境シグナルに応じて適切に増殖・分化・死を選択**。

### 1.2 健康細胞は QECC

Tier 1 #1 で「QECC = $\delta S = \delta\langle K\rangle$ の工学的実装」 と示しました。健康細胞も同じ:
- **Syndrome 検出** = DNA 損傷検出 (ATM/ATR), 細胞周期チェックポイント (p53, RB1)
- **エラー訂正** = DNA 修復, apoptosis (= 致命的損傷を持つ細胞の除去)
- **論理状態** = 「正常な細胞アイデンティティ + 組織内位置」

⇒ 細胞は **生物学的 QECC**。

---

## 2. がん細胞は ITU 公理の破綻

### 2.1 破綻の 2 パターン

| パターン | 状態 | 例 |
|---|---|---|
| **A: $\delta S \gg \delta\langle K\rangle$** | エントロピー暴走 | regulatory が追いつかない異常増殖 |
| **B: $\delta\langle K\rangle$ 自体の腐敗** | regulatory K が改ざん | driver mutation で恒常活性化 |

実際のがんは **A + B** の組合せ。例:
- KRAS G12D 変異 (B): K が常時 ON → 細胞は常に増殖シグナル受信状態
- 結果として S 暴走 (A): 制御不能な複製、ゲノム不安定

### 2.2 ITU 数式

健康細胞:
$$\frac{dS}{dt} = \frac{d\langle K\rangle}{dt} \quad (\text{均衡})$$

がん細胞:
$$\frac{dS}{dt} \neq \frac{d\langle K\rangle}{dt} \quad (\text{破綻})$$

差 $\Delta = dS/dt - d\langle K\rangle/dt$ が **がん severity** の指標。$\Delta > 0$ で増殖性、$\Delta < 0$ で apoptosis 回避型。

---

## 3. The Hallmarks of Cancer を ITU で再分類

Hanahan-Weinberg (2000/2011/2022) の **10 hallmarks** を ITU 視点で:

| Hallmark | 標準解釈 | ITU 視点 (どの K 成分が失敗) |
|---|---|---|
| 1. Sustained proliferative signaling | RAS/EGFR 恒常活性 | **K_proliferation 常時 ON** ⇒ S 増加 |
| 2. Evading growth suppressors | p53/RB1 損失 | **K_suppress が S を抑制できない** |
| 3. Resisting cell death | BCL2 過剰, BAX 損失 | **K_apoptosis 不全** ⇒ S 高位状態維持 |
| 4. Replicative immortality | テロメラーゼ活性化 | **K_aging (Hayflick limit) bypass** |
| 5. Inducing angiogenesis | VEGF 分泌 | **K_organism level が局所要求に従属** |
| 6. Activating invasion | EMT, MMPs | **K_tissue_cohesion 喪失** |
| 7. Genome instability | DNA 修復不全 (BRCA1/2) | **K_repair 不全** ⇒ S 不可逆増加 |
| 8. Tumor-promoting inflammation | 慢性炎症 | **K_immune 機能変質** |
| 9. Deregulating cellular energetics | Warburg 効果 | **K_metabolism shift** (Phase 60) |
| 10. Avoiding immune destruction | PD-L1 発現 | **K_immune_recognition 回避** (Phase 61) |

⇒ **10 hallmark は 10 種の K-component の破綻パターン**。ITU は hallmarks を**統一的な「K の故障」 として記述**。

---

## 4. Two-Hit 仮説の ITU 解釈

### 4.1 Knudson 1971

retinoblastoma の家族性 vs 散発性発症パターンから、**TSG (tumor suppressor gene) は 2 つの alleles 両方が失われないと機能停止しない** ことを発見。

### 4.2 ITU 解釈: redundant QECC

ITU 観点では:
- **TSG = K_suppress に冗長性を持たせる QECC**
- 2 alleles = 2 物理 qubit による論理 qubit 符号化
- 1 hit (heterozygous loss) では K_suppress まだ機能
- **2 hits 必要** = QECC の syndrome 訂正能力を超える

これは **Tier 1 #1 の [[5,1,3]] code** が「2 つまでのエラーを訂正」 する原理と**同型**。

### 4.3 数値例: BRCA1 と乳がん

- 一般人口 BRCA1 変異率: ~0.25%
- 家族性 (1 hit 既に保有): 生涯リスク 65-80%
- 散発性 (2 hits 体細胞変異要): 生涯リスク 12%

⇒ **両 alleles の同時変異確率** = $(p_{\rm mutation})^2$ で 5 倍以上の差を説明。

---

## 5. Mutation accumulation: いつ「がん化」 するか

### 5.1 Multi-hit Armitage-Doll model (1954)

がん発症年齢分布は **t^5 〜 t^7** の累乗則 ⇒ **5-7 個の独立な変異** が必要。

### 5.2 ITU 解釈: K-component の階層的破綻

| 変異数 | 状態 | ITU |
|---|---|---|
| 0-2 | 健康 | δS = δ⟨K⟩ 維持 |
| 3-4 | 前がん (dysplasia) | K のいくつかが弱まる、組織レベルで補償 |
| 5-6 | 悪性形質獲得 | **K のクリティカルマス崩壊** ⇒ δS ≠ δ⟨K⟩ |
| 7+ | 転移能獲得 | K_tissue, K_immune も破綻 |

5-7 hits = **K-component が 10 種類あるうち 5-7 種** が同時失敗。Hallmarks の数と一致。

---

## 6. Phase 59 数値検証

### 6.1 検証 1: 健康 vs がん 増殖曲線
ロジスティック (健康) vs 指数 (がん) の細胞数増加を比較。
ITU 公理破綻 ⇒ carrying capacity を無視した暴走。

### 6.2 検証 2: Multi-hit cancer onset
変異率 $\mu$、必要 hits $n$ から発症年齢分布を計算 (Armitage-Doll)。

### 6.3 検証 3: 10 Hallmarks ↔ 10 K-components 対応図
Spider chart で正常細胞 vs がん細胞の K プロファイル可視化。

### 6.4 検証 4: Two-hit fit (BRCA1 example)
1 hit保有者 vs 2 hits 必要パターンの生涯リスク曲線。

---

## 7. Phase 59 の結論

1. **がん = $\delta S = \delta\langle K\rangle$ の細胞レベル破綻**
2. **健康細胞 = 生物学的 QECC** (syndrome 検出 + 訂正)
3. **10 Hallmarks of Cancer = 10 種の K-component 故障**
4. **Two-hit 仮説 = redundant QECC**
5. **Multi-hit 仮説 (5-7) = critical mass of K failures**

Phase 60 では **がん代謝 (Warburg 効果, Otto Warburg 1924)** を ITU で再解釈し、**代謝シフトが δS 暴走を支える物理基盤** として位置付けます。

---

## 引用

```
Terada, M. (2026). ITU and Cancer Biology (Phase 59-62).
Tier 1 #5 application paper. In preparation.
```

参考:
- Hanahan & Weinberg (2000, 2011, 2022) "Hallmarks of Cancer" series
- Knudson (1971) PNAS 68, 820 (Two-hit hypothesis)
- Armitage & Doll (1954) Br J Cancer 8, 1 (Multi-hit model)
- Stratton, Campbell, Futreal (2009) Nature 458, 719 (cancer genome landscape)
- Vogelstein, Kinzler (1993) Trends Genet 9, 138 (genetic basis of cancer)
