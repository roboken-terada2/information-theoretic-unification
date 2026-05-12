# Phase 36: Free Energy Principle と ITU ― 生命の単一原理

## 1. 動機

Phase 33-35 で「生命 = 自己安定化情報パターン」を構造的に確立した。
しかし**生命システムの「行動 (behaviour) と認知 (cognition)」** ―
脳・知覚・予測 ― はまだ扱っていない。

Karl Friston は 2005 年から **Free Energy Principle (FEP)** を提唱:

> **全ての生命システムは変分自由エネルギー (variational free energy) を
> 最小化する。**

これは脳科学・神経生物学・行動学を統一する候補原理であり、本 Phase で
ITU の単一公理 $\delta S = \delta \langle K \rangle$ との**形式的同値性**を示す。

## 2. Free Energy Principle の核心

### 2.1 変分自由エネルギー

観測 $o$ と隠れ状態 $z$ を持つ生命システム。生成モデル $p(o, z) = p(o|z) p(z)$、
認識密度 (内部表現) $q(z)$。

**変分自由エネルギー**:
$$F[q, o] = \mathbb{E}_q[\log q(z)] - \mathbb{E}_q[\log p(o, z)]$$

これは**負の対数尤度 (surprise) の上限**:
$$F[q, o] = D_{\rm KL}[q(z) \| p(z|o)] - \log p(o) \geq -\log p(o)$$

### 2.2 最小化原理

生命システムは:
1. **知覚** (perception): $F$ を $q$ について最小化 → $q(z) \to p(z|o)$
2. **行動** (action): $F$ を $o$ について最小化 → 期待外れの観測を回避

両者で **$F$ が下がる方向に進む** ことが「**生きている**」ということ。

これは熱力学的自由エネルギー $F = U - TS$ の情報理論版:
- 物理: 熱平衡で $F$ 最小
- 生命: 認識平衡で $F$ 最小

### 2.3 Markov blanket 構造

FEP の核心構造は **Markov blanket**:
- 内部状態 $\mu$ (= 認知)
- 外部状態 $\eta$ (= 環境)
- 感覚状態 $s$ + 行動状態 $a$ = blanket

$$p(\mu, \eta | s, a) = p(\mu | s, a) \cdot p(\eta | s, a)$$

内部と外部が blanket で条件付き独立 → 「自己」が形式的に定義される。

## 3. ITU との対応

### 3.1 変分自由エネルギー ⟷ ITU 公理

ITU 単一公理:
$$\delta S(\rho_A) = \delta\,\mathrm{Tr}[K_A^{(0)} \rho_A]$$

これは**相対エントロピーの 1 次変分が消える**ことと等価:
$$\delta D_{\rm KL}(\rho_A \| \rho_A^{(0)}) = 0 \quad \Leftrightarrow \quad
\delta S = \delta \langle K \rangle$$

FEP の変分自由エネルギー:
$$F = D_{\rm KL}[q \| p(\cdot | o)] - \log p(o)$$

$F$ 最小化は $\delta D_{\rm KL} = 0$ と同値 ― **ITU 公理と完全に同じ形**。

| ITU (物理層) | FEP (生命層) |
|---|---|
| $\rho_A$ | $q(z)$ (認識密度) |
| $\rho_A^{(0)}$ | $p(z\|o)$ (事後分布) |
| Modular Hamiltonian $K$ | $-\log p(z\|o)$ |
| $\delta S = \delta \langle K \rangle$ | $\delta F = 0$ |
| 部分系 $A$ | 内部状態 $\mu$ |
| 補集合 $A^c$ | 外部状態 $\eta$ |
| Entanglement | Markov blanket |

### 3.2 Markov blanket = QECC

Phase 5 で示した「**バルクの局所性 = QECC**」(Almheiri-Dong-Harlow 2015):
- 符号空間内で論理量子ビットが物理エラーから保護される
- 内部 (logical) と外部 (errors) が stabilizer 測定で分離

FEP の Markov blanket:
- 内部 (cognition) と外部 (environment) が感覚-行動 boundary で分離

**両者は同型な情報分離構造**。生命システムは「**QECC を実装する物理過程**」と
解釈できる。

### 3.3 ITU 公理階層の完成

物理層 (Phase 1-32):
$$\delta S(\rho_A) = \delta \langle K_A \rangle$$
↓ 化学翻訳 (Phase 33)
$$\delta S_{\rm chem}(\rho_{\mathcal{A}}) = \delta \langle M_{\rm chem} \rangle$$
↓ 自己複製翻訳 (Phase 35)
$$\delta P(\sigma^*) = (1 - \mu L \log \sigma^{-1}) A_{\sigma^*} \delta t$$
↓ **認知翻訳 (Phase 36)**
$$\boxed{\delta F[q, o] = 0 \quad \Leftrightarrow \quad
\delta D_{\rm KL}[q \| p(\cdot|o)] = 0}$$

全 4 階層が**同一の情報理論的構造**を持つ:
- **時空・重力**: 量子もつれの第一法則
- **生命の成立**: 化学的 QECC
- **自己複製**: Eigen 準種閾値
- **認知**: 変分自由エネルギー最小化

これが「**ITU は物理から認知まで貫通する**」という主張の本体。

## 4. Friston の予言 vs 観測

| 予言 | 観測 | 整合性 |
|---|---|---|
| 知覚 = Bayesian 推論 | fMRI: 予測符号化シグナル | ✅ Rao-Ballard 1999 |
| 行動 = active inference | 強化学習との橋渡し | ✅ Friston 2010 |
| 病気 = 異常な precision | 統合失調症の予測誤差 | ✅ Adams et al. 2013 |
| 老化 = 自由エネルギー増加 | 加齢で予測精度低下 | ✅ Friston 2018 |

FEP は神経科学で実験的支持を得ている。本 Phase はこれを ITU 公理の特殊例
として位置づける。

## 5. 数値検証計画

### Part A: 単純ベイズ推定での $F$ 最小化
- ガウス生成モデル $p(o|z)$, $p(z)$
- $q(z; \theta)$ の variational 最適化
- $F$ が単調減少することを確認

### Part B: $\delta F = 0 \Leftrightarrow \delta D_{\rm KL} = 0$
- $F$ 最小点で $q = p(\cdot|o)$
- 相対エントロピーがゼロ

### Part C: ITU 公理との同型対応
- $K = -\log p(z|o)$, $\rho = q$, $\rho^{(0)} = p(z|o)$ の代入
- $\delta S = \delta \langle K \rangle$ が成立することを確認

### Part D: Markov blanket 構造の数値構築
- 2 領域の確率モデル
- 条件付き独立性 (blanket 性) を確認

## 6. 限界

⚠️ 本 Phase で扱わない:
- 連続時間 active inference (Hamiltonian flow 形式)
- 非平衡熱力学との接続 (Friston 2019 で扱われる)
- 意識のハードプロブレム (Phase 40 で示唆程度)
- 具体的神経生理学のシミュレーション

✅ 確立する:
- FEP と ITU 公理の数値的同型性
- Markov blanket = QECC の同型構造
- 4 階層 (物理-化学-自己複製-認知) の単一原理化

## 7. 哲学的含意

ITU が示すのは:

> **「単一公理 $\delta S = \delta \langle K \rangle$ が物理から認知まで一貫する」**

これは:
- 物理的時空 (Phase 1-17) も
- ダークマター・ダークエネルギー (Phase 22-32) も
- 化学的生命 (Phase 33-35) も
- 認知・行動 (Phase 36, 本 Phase) も

**全て同じ情報理論的原理に従う**ことを意味する。

これは Tegmark の「数学的宇宙仮説」、Wheeler の "It from Bit"、
Friston の FEP、ITU の単一公理 ― 全てが**同じ情報統一を目指している**
ことを示唆する。

ITU はその情報統一の**具体的な数学的実装**を提供する候補である。

## 8. Phase 37 への橋渡し

次の Phase 37 では **lipid bilayer の自発形成** に進む。
これは Markov blanket の**物理的実装** ― 細胞膜が「自己」と「環境」を分離する
boundary を作る。FEP の認知的 blanket と細胞膜の物理的 blanket は同じ情報構造
を持つ。

その後 Phase 38 (chirality), 39 (first cell), 40 (synthesis) と続く。

---

**Phase 36 の核心メッセージ**:
> Friston の Free Energy Principle は ITU 単一公理の**生命層・認知層**での
> 顕在化である。$\delta F = 0$ と $\delta S = \delta \langle K \rangle$ は
> **同じ情報理論的原理の異なる表現**。生命と意識も時空と同じ axiom から派生する。
