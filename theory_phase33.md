# Phase 33: 情報理論的統一の延長 ― 生命の起源への橋渡し

## 1. 動機: ITU 完成の先に

Phase 1-32 で ITU は物理学の全領域 (重力, 量子論, 標準模型, ダークマター,
ダークエネルギー, 宇宙論) を単一公理
$$\delta S(\rho_A) = \delta\,\mathrm{Tr}[K_A^{(0)}\,\rho_A]$$
から導出することに成功した。

**しかし「物質」と「生命」の境界は未踏のままである。**

シュレディンガーは 1944 年の名著 *What is Life?* で:
> "Life feeds on negative entropy."

を主張した。エントロピー = 情報の概念は ITU の中心だ。本 Phase は ITU を
**生命の起源** へ拡張する第一歩を提案する。

## 2. 中心仮説

ITU の物理層と生命層の対応:

| 物理層 (Phase 1-32) | 生命層 (Phase 33+) |
|---|---|
| 量子状態 $|\psi\rangle$ | 化学組成 $\vec c = (c_1, ..., c_N)$ |
| エンタングルメント $S(\rho_A)$ | 化学的相関 (相関した濃度パターン) |
| モジュラーハミルトニアン $K_A$ | 化学的 "応答" 行列 ${\bf M}_{\rm chem}$ |
| QECC スタビライザ | 自己触媒サイクル |
| 凍結 QECC = DM | 自己保存代謝 = 生命 |
| 第1法則 $\delta S = \delta \langle K \rangle$ | **生命方程式** $\delta S_{\rm chem} = \delta \langle M_{\rm chem} \rangle$ |

**中心仮説**:

> **化学組成空間内で、情報パターン (= 触媒関係) を自己保存する閉じた部分系が「生命」である。**

これは「**生命 = 化学的 QECC**」とも言える。

## 3. 形式化

### 3.1 化学組成のヒルベルト空間

$N$ 種の化学種 $\{X_1, ..., X_N\}$ について、状態は濃度ベクトル
$\vec c \in \mathbb{R}_{\geq 0}^N$ で記述。これに対応する Hilbert 空間は
組合せ的に巨大だが、相互情報量解析には濃度ベクトル自体を coarse-grained
状態として扱う。

### 3.2 化学的モジュラーハミルトニアン

化学反応ネットワーク $\mathcal{R} = \{R_\alpha: A_\alpha + B_\alpha \to C_\alpha\}$
について、反応 rate 行列 ${\bf M}$ から:
$$M_{ij} = \frac{\partial \dot c_i}{\partial c_j}$$

これが "化学的 modular Hamiltonian"。エントロピー $S_{\rm chem}(\vec c)$
の変化と組合せて:
$$\delta S_{\rm chem} = \delta \langle M_{\rm chem} \cdot \vec c \rangle$$
が**生命系の第一法則**となる候補。

### 3.3 QECC 構造としての自己触媒集合

Kauffman 1986 の autocatalytic set: 化学種の部分集合 $\mathcal{A}$ が
- (1) **closed**: $\forall X \in \mathcal{A}$, ある $X' \in \mathcal{A}$ が $X$ の触媒
- (2) **self-sustaining**: $\forall X \in \mathcal{A}$, 反応で $X$ が生成

ITU 流の解釈:
- (1) は QECC スタビライザの commutator 構造 (各スタビライザが他のスタビライザの
  存在を「保証」)
- (2) は code の self-correction 性 (誤りを修復しながら code 状態を保つ)

**autocatalytic set = chemical QECC**

### 3.4 ITU 延長公理

物理層の axiom δS = δ⟨K⟩ を生命層へ:

$$\boxed{\delta S_{\rm chem}(\rho_{\mathcal{A}}) =
\delta\,\mathrm{Tr}[M_{\mathcal{A}}^{(0)}\,\rho_{\mathcal{A}}], \quad \forall \mathcal{A} \subset \text{chem.space}}$$

ここで $\rho_{\mathcal{A}}$ は化学組成の確率分布 (経験的 ensemble)、
$M_{\mathcal{A}}^{(0)}$ は静止状態での化学応答行列。

**この公理を満たす最大の部分集合 $\mathcal{A}^* \subset$ chem.space が "生命体" である**。

## 4. 観測との接続

| 観測 | ITU 延長予言 |
|---|---|
| 自己触媒集合の臨界出現密度 | $N_{\rm crit} \sim e^{S_{\rm chem}/k_B \log 2}$ |
| 生命の最小システムサイズ | $N_{\rm min} \sim 200$ (Mycoplasma genitalium 480 遺伝子) |
| 遺伝子コードの冗長性 | QECC distance $d \geq 3$ (3 重 codon → 単一 base swap 訂正) |
| ribosome の error rate | $\sim 10^{-4}$ (QECC 訂正効率の上限) |
| 細胞の自己複製時間 | $\tau_{\rm cycle} \sim \log_2(\text{cell info content}) / S_{\rm chem}$ |

## 5. Phase 33-40 のロードマップ

| Phase | テーマ |
|---|---|
| **33** | **橋渡し: 化学的 QECC = 生命** (本 Phase) |
| 34 | Kauffman autocatalytic set の数値シミュレーション |
| 35 | RNA world: 自己複製 ribozyme の情報構造 |
| 36 | Assembly Theory (Walker-Cronin) との接続 |
| 37 | Free Energy Principle (Friston) との対応 |
| 38 | 細胞膜の自発形成 + lipid bilayer の QECC 構造 |
| 39 | 遺伝コードのカイラリティ (左 amino acid 選好) と ITU Phase 15 |
| 40 | 生命の起源 — 化学から最初の細胞への遷移を数値再現 |

## 6. 本 Phase の数値実験計画

簡略 Kauffman 模型で「自己触媒集合 = chemical QECC」仮説を最初の数値証拠
として確立:

### Part A: ランダム化学ネットワーク
- $N$ 化学種、$N_R$ 反応 (ランダム)
- 各反応に触媒 (ランダムにある化学種)
- 連結成分を抽出

### Part B: closure & self-sustaining 判定
- 最大連結成分 $\mathcal{A}$ について chemical-QECC 条件をチェック
- 結果は (closed, self-sustaining, 両方) のフラグ

### Part C: 相転移の確認
- 反応密度 $\rho = N_R/N$ をスキャン
- $\rho$ 関数として QECC-閉じた集合のサイズ
- Kauffman 1986 の **臨界 $\rho_c \approx 1$** の再現

### Part D: ITU 延長公理の数値検証
- 化学エントロピー $S_{\rm chem}$ と $\langle M \cdot c \rangle$ の対応
- $\delta S = \delta \langle M c \rangle$ の係数を測定

## 7. 限界

⚠️ 本 Phase で扱わない:
- 完全な熱力学的非平衡定式化 (Friston Phase 37 で扱う)
- 立体化学・カイラリティ (Phase 39)
- 膜 (lipid bilayer) の役割 (Phase 38)
- 遺伝子コードの具体的構造 (Phase 35)

✅ 確立する:
- 化学的 QECC = 生命 仮説の数値的妥当性
- Kauffman 臨界 $\rho_c \approx 1$ の再現
- ITU 延長公理が形式的に成立する

## 8. 哲学的含意

ITU の真価は、**「情報→物理→生命→意識」** の単一公理階層を示せるかにある。
Phase 33 はその第二階層 (物理→生命) の最初の一段。

物理的時空が情報パターンから創発するなら、生命も情報パターンから創発する
はずだ — ITU はその統一を提供する候補となる。

Schrödinger の "生命は負のエントロピーを食べる" は、ITU 流に翻訳すると:

> **生命は局所的に $\delta S = \delta \langle K \rangle$ を破らない**

物理学的時空のように、生命も自己保存する情報構造である。
