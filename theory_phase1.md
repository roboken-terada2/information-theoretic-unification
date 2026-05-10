# 情報理論的統一理論：時空の創発 (Emergent Spacetime from Information)

## 1. 問題設定

一般相対性理論 (GR) は連続的な時空多様体 $(\mathcal{M}, g_{\mu\nu})$ を**前提**にする。
量子力学はヒルベルト空間 $\mathcal{H}$ 上のユニタリ進化を**前提**にする。
両者を統一するには、どちらかを他方から導出する必要がある。

**情報理論的統一仮説**：時空・計量・次元はヒルベルト空間上の量子状態の **エンタングルメント構造** から創発する。

## 2. 既存研究の系譜

| 年 | 著者 | 主張 |
|---|---|---|
| 1995 | Jacobson | $T dS = \delta Q$ から Einstein 方程式が導かれる (熱力学的 GR) |
| 2006 | Ryu–Takayanagi | $S_A = \frac{\text{Area}(\gamma_A)}{4 G_N}$ (AdS/CFT における面積=エントロピー) |
| 2010 | Van Raamsdonk | "Building up spacetime with quantum entanglement" — エンタングルメントを切ると時空が分離する |
| 2011 | Verlinde | エントロピー的重力 |
| 2012 | Swingle | MERA テンソルネットワーク=離散 AdS |
| 2013 | Maldacena–Susskind | ER = EPR (ワームホール=エンタングルメント) |
| 2017 | Cao–Carroll–Michalakis | "Space from Hilbert Space" — 相互情報量から距離・次元を抽出 |
| 2020s | It from Qubit collaboration | 量子誤り訂正符号としてのホログラフィー |

## 3. 中心的アイディア (本シミュレーションが実装するもの)

### 3.1 公理
- **公理 I**：宇宙は純粋状態 $|\Psi\rangle \in \mathcal{H}$ で記述される。
- **公理 II**：$\mathcal{H} = \bigotimes_{i=1}^{N} \mathcal{H}_i$ という**因子分解**が選ばれている。各 $i$ が「原始情報セル (qubit/qudit/フェルミオンモード)」。
- **公理 III**：時空構造 (近接関係・距離・次元) は、状態 $|\Psi\rangle$ から induced されるエンタングルメント分布のみで決まる。

### 3.2 距離の構成 (情報計量)
任意の2サブシステム $A, B$ に対し相互情報量を定義：
$$I(A:B) = S(A) + S(B) - S(A \cup B), \quad S(X) = -\mathrm{Tr}\,\rho_X \log \rho_X.$$
$I \geq 0$ かつ $I=0 \Leftrightarrow \rho_{AB} = \rho_A \otimes \rho_B$ (積状態)。

**相関の上限定理 (Wolf-Verstraete-Hastings-Cirac 2008)**：任意の演算子 $\mathcal{O}_A, \mathcal{O}_B$ に対し
$$\frac{|\langle \mathcal{O}_A \mathcal{O}_B\rangle - \langle \mathcal{O}_A\rangle\langle \mathcal{O}_B\rangle|^2}{2\|\mathcal{O}_A\|^2 \|\mathcal{O}_B\|^2} \leq I(A:B).$$

つまり $I(A:B)$ は**全ての物理相関を支配する**普遍的尺度である。これを「物理的近さ」の唯一の候補にする：
$$d(A,B) := -\log\!\left(\frac{I(A:B)}{I_{\max}}\right), \quad I_{\max} = 2\min(S(A), S(B)).$$

### 3.3 創発幾何 (MDS による埋め込み)
距離行列 $D_{ij} = d(i,j)^2$ の二重中心化 $B = -\tfrac{1}{2} J D J$ ($J = I - \tfrac{1}{N}\mathbf{1}\mathbf{1}^\top$) を対角化すると、固有値 $\{\lambda_k\}$ の階段構造が**創発次元**を与える：
- 上位 $d$ 個の固有値が支配的 → $d$ 次元多様体として表現可能
- 固有値が均等 → 幾何的に解釈不可能 (高次元/フラクタル状態)

## 4. 検証可能な予言 (本シミュレーションが示すこと)

### 予言 A (CFT スケーリング)
1次元臨界系 (中心電荷 $c$) では Calabrese-Cardy より
$$S_A(\ell) = \frac{c}{3} \log\!\left[\frac{N}{\pi}\sin\frac{\pi\ell}{N}\right] + \text{const}.$$
XX モデル (自由フェルミオン半占有) で $c = 1$。

### 予言 B (1次元時空の復元)
XX 鎖の基底状態に対し、$d_{ij}$ から MDS で 1〜2 個の固有値が支配的になり、座標が**円周上**に並ぶ (PBC ではトポロジーまで再現)。

### 予言 C (非幾何状態との対比)
ランダム Gaussian 状態では MDS 固有値スペクトルが平坦化し、低次元埋め込みが破綻する。「情報構造が地理的でない状態は時空を持たない」。

### 予言 D (相互情報量の冪則)
臨界鎖では $I(i:j) \sim |i-j|^{-2K}$ ($K=1$ for free fermion at half filling)。
これは相対論における「光円錐の relics」の離散版に相当し、$g_{\mu\nu}$ の連続極限を作る出発点になる。

## 5. 本研究で示せる範囲と限界

✅ 示せる：
- 量子状態のエンタングルメント分布だけから 1 次元計量・次元・連続極限の片鱗が**数値的に**復元される。
- 「時空がない量子状態」と「時空がある量子状態」の明確な対比。

⚠️ 示せない (今後の課題)：
- Einstein 方程式 $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ の動的部分 (Jacobson 1995 の議論を融合する必要)。
- 4次元ローレンツ多様体への一般化 (時間方向は modular flow / Tomita-Takesaki から導出する必要)。
- 動的時空の進化方程式 (Lloyd の計算的時間概念 / page curve)。

つまり本シミュレーションは「**情報 → 空間** (静的計量)」の片道のみを最小モデルで証明する。重力場方程式までの完全統一には modular Hamiltonian の幾何化が必要であり、別ステップ。
