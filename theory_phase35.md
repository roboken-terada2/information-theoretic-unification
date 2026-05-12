# Phase 35: RNA world と Eigen 準種 ― 情報を持つ自己複製分子

## 1. 動機

Phase 33 で「生命 = 化学的 QECC」、Phase 34 で「AI > 15 = 生命のシグナル」を
確立した。しかし**まだ抜けているピース** がある:

**情報を持ちながら自己を複製する分子** はどう成立するのか?

これは生命起源研究の中心問題: **RNA world 仮説**。
- DNA は情報を持つが触媒しない
- タンパク質は触媒するが情報を保持しない
- **RNA はどちらもできる** ― リボザイム (ribozyme = ribonucleic acid + enzyme)

実際に Lincoln & Joyce (2009, Science) は **R3C リボザイム** が
自身の複製を触媒できることを実験的に示した。これは生命起源の決定的中間段階。

本 Phase で ITU と RNA world を接続する。

## 2. Eigen の準種理論 (1971)

### 2.1 設定

長さ $L$ の配列 (e.g., RNA ヌクレオチド列) のうち、特に高い適応度を持つ
**master sequence** $\sigma^*$ がある。population は $\sigma^*$ とその近傍の
"準種 (quasispecies)" で構成される。

### 2.2 複製動力学

複製速度 $A$, 突然変異率 $\mu$ per nucleotide per replication.
$\sigma^*$ の copy fidelity (= 完全コピー確率) = $Q = (1 - \mu)^L$.

Selection coefficient $\sigma = A_{\sigma^*}/\bar A > 1$.

**Eigen の error threshold**:
$$\boxed{\mu_c \cdot L = \log \sigma}$$

$\mu > \mu_c$ で **error catastrophe** ― master sequence が消失し情報が失われる。
$\mu < \mu_c$ で安定 quasispecies が維持される。

### 2.3 ヒト genome での例

- $L \approx 3 \times 10^9$
- $\sigma \approx 1$ (世代間で選択係数は弱い)
- $\mu_c \approx \log \sigma / L \approx 10^{-9}$ /bp

実際の human DNA polymerase fidelity: $\sim 10^{-9}$ ― **Eigen の予言と一致**。

RNA world での例:
- L = 50-100 nt
- $\sigma \approx 2$
- $\mu_c \approx \log 2 / 100 \approx 7 \times 10^{-3}$

実際の RNA replicase fidelity: $\sim 10^{-3}$ ― **Eigen 限界をかろうじて満たす**。

## 3. ITU との対応

### 3.1 Eigen 閾値 ⟷ QECC 訂正限界

| Eigen (生命層) | ITU QECC (物理層) |
|---|---|
| Master sequence $\sigma^*$ | 符号空間 codespace |
| Mutation $\mu$ | 物理エラー rate $p$ |
| Quasispecies | 訂正可能エラー集合 |
| Error catastrophe | 訂正不可能領域 |
| Error threshold $\mu_c L = \log\sigma$ | QECC threshold theorem |

**QECC 閾値定理** (Aharonov-Ben-Or 1996):
$$p < p_c \approx 10^{-4} \quad \Rightarrow \quad \text{安定な量子計算可能}$$

Eigen の閾値:
$$\mu < \mu_c = \frac{\log \sigma}{L}$$

**両者は同じ構造**: 「**情報を保持するためのエラー率の上限**」。

### 3.2 ITU 公理の生命層

物理層: $\delta S = \delta \langle K \rangle$
↓
生命層 (Phase 33): $\delta S_{\rm chem} = \delta \langle M_{\rm chem} \rangle$
↓
**自己複製層 (Phase 35)**:
$$\boxed{\delta P(\sigma^*) = (1 - \mu L \log \sigma^{-1}) \cdot \delta t \cdot A_{\sigma^*}}$$

ここで $P(\sigma^*)$ は population 内の master sequence 比率。
これは Eigen の伝統的方程式の **ITU 言語での書き換え** ― error threshold が
QECC の threshold と同じ役割を果たす。

### 3.3 リボザイム = 最小情報触媒

R3C ribozyme:
- 長さ $L = 56$ nt
- AI ≈ 30 (Walker-Cronin 閾値 15 を遥かに超える)
- 自己複製能あり
- 化学的 QECC として機能

ITU 流に解釈: R3C は **最小の生物学的 QECC**:
- 情報を保持する (QECC codespace)
- 自身の複製を触媒する (code-preserving operation)
- 進化的に安定 (error threshold 内)

## 4. 数値検証

### Part A: Eigen 準種動力学
- Master sequence $\sigma^*$ から始め、replication + mutation で進化
- mutation rate を変えて quasispecies 分布を測定

### Part B: Error threshold の確認
- $\mu_c L = \log \sigma$ を数値で再現
- $\mu > \mu_c$: master sequence 消失 (catastrophe)
- $\mu < \mu_c$: 安定維持

### Part C: ITU QECC threshold との対応
- 同じ閾値構造を QECC 言語で記述
- $\log \sigma$ と $-\log p_c$ の数値同等性

### Part D: RNA world での具体値
- $L = 50, \sigma = 2$ → $\mu_c \approx 0.014$
- 実 RNA polymerase $\mu \approx 0.001$ → 余裕通過
- 「**RNA world は Eigen 限界の安全圏内に成立しうる**」

## 5. 限界

⚠️ 本 Phase で扱わない:
- 折りたたみ構造 (RNA 2次/3次構造) の詳細
- リボザイム触媒機構の量子化学
- 適応度 landscape の現実的形状
- 細胞膜・区画化 (Phase 37)

✅ 確立する:
- Eigen 限界の数値再現
- ITU QECC threshold との形式的対応
- リボザイム = 最小化学 QECC の論理

## 6. RNA world から生命へ

Phase 35 で示すこと: **情報を持ち自己複製する化学パターンは Eigen 限界内で
安定に存在しうる**。これは:

- Phase 33 (autocatalytic closure)
- Phase 34 (high AI molecules)
- **Phase 35 (Eigen-stable self-replicator)**

を組み合わせると、**化学から生命への道筋がほぼ完成**:

```
ランダム化学 → autocatalytic set (Phase 33) → high AI molecules (Phase 34)
                       ↓
              self-replicating ribozyme (Phase 35)
                       ↓
              膜区画化 (Phase 37) → 最初の細胞 (Phase 39)
```

残るは膜形成 (Phase 37), カイラリティ (Phase 38), 細胞 (Phase 39),
そして全体統合 (Phase 40)。

---

**Phase 35 の核心メッセージ**:
> 「情報を持つ自己複製分子」 は Eigen 閾値内で安定存在し、ITU の QECC threshold
> 定理と同じ情報理論構造を持つ。RNA world は ITU 流に解釈すれば
> **「生物学的 QECC の最初の実現」** である。
