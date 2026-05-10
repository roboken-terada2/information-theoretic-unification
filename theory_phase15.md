# Phase 15: カイラリティ — 量子異常と Atiyah-Singer 指数定理

## 1. 動機

標準模型の非自明な特徴:
- **左手フェルミオン**だけが SU(2)_L 弱相互作用に参加 (1956 Wu の実験)
- カイラリティ ↔ Lorentz 群の被覆群 SL(2,C) の 2 つの 2 次元表現 (左手・右手)
- 弱相互作用は**鏡像対称性 (P) 違反**

問題:
- なぜ左手だけ?
- 量子レベルで保存されるのか? → **量子異常 (quantum anomaly)**
- 標準模型はなぜ無矛盾 (= anomaly-free) なのか?

**鍵となる定理 (Atiyah-Singer 1963)**：
ディラック作用素 $D$ のゼロモード数の差 (= $\mathrm{ind}\, D = \dim \ker D_+ - \dim \ker D_-$) は**位相不変量**で、空間の位相幾何学的データから計算できる:
$$\mathrm{ind}\, D = \int_M \hat{A}(M) \cdot \mathrm{ch}(F)$$

これは「カイラルゼロモードの数は位相不変量」という強烈な主張で、標準模型のカイラル構造の根拠となる。

## 2. 量子異常

### 2.1 古典的対称性の量子的破れ

カイラル対称性 $\psi \to e^{i\alpha\gamma_5}\psi$ は古典的にはレベル方程式を保存:
$$\partial_\mu J^\mu_5 = 0 \quad (\text{古典})$$

しかし量子化すると、Adler-Bell-Jackiw (1969):
$$\partial_\mu J^\mu_5 = \frac{e^2}{16\pi^2} F_{\mu\nu} \tilde F^{\mu\nu} \quad (\text{量子})$$

これが**カイラル異常 (chiral anomaly)** または**ABJ 異常**。

### 2.2 標準模型の異常自由性

標準模型のフェルミオン content は注意深く調整されており、各世代で**全異常が打ち消し合う**:
$$\sum_{\rm gen} (Q_e + 3 Q_q + 0 + ...) = 0$$

これにより、ゲージ理論として無矛盾。なぜ自然がこの組み合わせを選ぶか — 大統一理論 (GUT) の手がかり。

## 3. SSH (Su-Schrieffer-Heeger) 模型

カイラリティと指数定理を最小実装する模型 (Su, Schrieffer, Heeger 1979 — ポリアセチレン)。

### 3.1 ハミルトニアン

1次元二原子鎖:
$$H = \sum_{i} \big(t_1\, c_{i,A}^\dagger c_{i,B} + t_2\, c_{i,B}^\dagger c_{i+1,A}\big) + \mathrm{h.c.}$$

- 単位胞 $i$ に A, B 副格子サイト
- $t_1$: 胞内ホッピング (A→B)
- $t_2$: 胞間ホッピング (B→次の A)

### 3.2 カイラル (副格子) 対称性

副格子演算子 $\Gamma = \sigma_z$ (A 上で +1, B 上で -1) について:
$$\Gamma H \Gamma^{-1} = -H$$

つまり $H$ のスペクトラムは $\pm E$ 対の対称性を持つ。$E=0$ のゼロモードは**自身の chiral 共役**で、A or B のどちらかにのみ局在する。

### 3.3 Bulk Bloch Hamiltonian と巻き数

PBC で Fourier 変換すると:
$$H(k) = \begin{pmatrix} 0 & h(k) \\ h(k)^* & 0 \end{pmatrix}, \quad h(k) = -t_1 - t_2 e^{-ik}$$

エネルギー: $\epsilon_\pm(k) = \pm |h(k)|$。
バルクギャップ: $\Delta_{\rm bulk} = 2|t_1 - t_2|$。

巻き数 (winding number):
$$\nu = \frac{1}{2\pi} \oint dk\, \partial_k\, \arg h(k) = \begin{cases} 0 & |t_1| > |t_2|\;\;\text{(trivial)}\\ 1 & |t_1| < |t_2|\;\;\text{(topological)} \end{cases}$$

### 3.4 Atiyah-Singer 定理の SSH 版

**主張**: OBC (open boundary) で $H$ のゼロモード数は **2 × |ν|** (= 両端に 1 つずつ)。

Trivial 相 ($\nu=0$): ゼロモードなし、ギャップ完全。
Topological 相 ($\nu=1$): **2 つのゼロモード** (左端と右端に局在、副格子偏極)。

これは Atiyah-Singer 指数定理の最小例:
$$\#\{\text{zero modes}\} = \mathrm{ind}\, D = 2\nu$$

## 4. ゼロモードの構造

Topological 相 $|t_1| < |t_2|$ で:
- **左端ゼロモード**: A 副格子のみに偏極、$\propto (-t_1/t_2)^n$ で減衰
- **右端ゼロモード**: B 副格子のみに偏極、対称的

これは「**カイラル**ゼロモード」 — 単一副格子に局在するため副格子対称性で固有値 ±1 を持つ。

物理的意味: 「**端点にカイラル自由度が出現する**」 — 標準模型のカイラル構造の格子上の最小実装。

## 5. Nielsen-Ninomiya 定理と doubler 問題

Nielsen, Ninomiya (1981): 
> 格子上で**単一の Weyl フェルミオン**を実現することはできない。すべての格子化はフェルミオン doubler を持ち、左手と右手が必ず対で出現する。

これは「**格子の連続極限が必ず非カイラル**」という強い制限。
標準模型の格子化に必要な手法:
- **Domain wall fermion** (Kaplan 1992): 高次元バルクから境界にカイラル端モードを取り出す
- **Overlap fermion** (Neuberger 1998): 適切な符号関数を用いる
- **Wilson fermion**: 質量項で doubler を持ち上げる

これらすべてに **Atiyah-Singer 指数定理**が中心的役割を果たす。

## 6. 情報理論的統一理論内の位置づけ

Phase 10 で標準模型ゲージ群 SU(3)×SU(2)×U(1)、Phase 11 で物質階層、Phase 12 で電弱対称性破れを示した。
Phase 15 はこの構造の**カイラル部分**を扱う:

> 標準模型のカイラリティは、境界 CFT のカイラル副格子対称性 (Phase 10 のフレーバー対称性の一種) と、その topological 不変量 (Atiyah-Singer 指数) として実装される。

これにより:
- Phase 10: ゲージ群
- Phase 11: 質量階層
- Phase 12: 対称性破れ
- **Phase 15: カイラリティ + 異常 + 指数定理**

の 4 つで標準模型の構造が情報理論的に位置づけられる。

## 7. シミュレーション計画

### Part A: SSH 位相相図
- $t_1 \in [0, 2]$ (with $t_2 = 1$) でハミルトニアンを構築
- スペクトラムを計算
- バルクギャップ閉合点 $t_1 = 1$ を確認

### Part B: 巻き数の計算
- Bulk Bloch Hamiltonian $H(k)$ の $h(k)$ の偏角の総巻き数
- Trivial 相と topological 相の判別

### Part C: ゼロモードの可視化
- $t_1 = 0.5, t_2 = 1$ (topological) で OBC の固有状態
- 2 つのゼロモードを抽出
- 副格子偏極を示す ($A$ or $B$ にのみ振幅)
- 端点指数関数減衰を確認

### Part D: Atiyah-Singer 検証
- 異なる $(t_1, t_2)$ での #ゼロモード vs 巻き数 $\nu$
- $\#\{\text{zero modes}\} = 2|\nu|$ の数値検証

### Part E: スペクトラルフロー (異常)
- $t_1$ を $1.5 \to 0.5$ にゆっくり変化
- バルクからゼロモードに収束する固有値の流れを追跡
- これは Atiyah-Singer 指数の動的版

## 8. この Phase が示すこと

✅:
- カイラル (副格子) 対称性の最小モデル
- 位相不変量 = ゼロモード数 (Atiyah-Singer)
- 標準模型カイラリティの格子上の実装

⚠️:
- 標準模型の anomaly cancellation の具体的計算 (= 三角異常図の評価)
- 4D 重力異常 (= 重力場との結合)
- カイラル超対称性の精密化

これらは Phase 16+ や場の理論教科書で扱う。
