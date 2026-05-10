# Phase 4: 時間の創発 — モジュラーフローと熱的時間仮説

## 1. 動機

Phase 1-3 では空間幾何・線形化Einstein方程式・双曲バルクが情報構造から創発した。
しかしどこにも**時間方向**は出てこない。すべて瞬間 (t=0 切片) の議論。

Connes-Rovelli (1994) "Von Neumann algebra automorphisms and time-thermodynamics relation in generally covariant quantum theories" の主張：
> 時間は古典的な背景ではなく、量子状態 (von Neumann 環+状態) からモジュラー自己準同型として導出される。

これは **熱的時間仮説 (thermal time hypothesis)** と呼ばれ、本Phase で数値検証する。

## 2. Tomita-Takesaki モジュラー理論の要点

von Neumann 環 $\mathcal{M}$ と (faithful, normal) 状態 $\omega$ から、一意の1-パラメータ自己準同型族
$$\sigma_t^\omega : \mathcal{M} \to \mathcal{M}, \quad t \in \mathbb{R}$$
が定義される (Tomita 1957, Takesaki 1970)。これを**モジュラーフロー**という。

具体形：$\rho_\omega = e^{-K}/Z$ と書けば
$$\sigma_t(O) = e^{i K t}\, O\, e^{-i K t}.$$

物理解釈 (Bisognano–Wichmann)：4次元 Minkowski 真空 $|\Omega\rangle$ で右 Rindler 楔を $\mathcal{M}$ にとると、$\sigma_t$ は $2\pi t$ ぶんの Lorentz 倍率変換 (boost) になる。
$$K_{\text{Rindler}} = 2\pi \int_0^\infty x\, T_{00}(x, 0)\, dx \quad \Rightarrow \quad \sigma_t = \text{Boost}(2\pi t).$$

つまり Rindler 観測者にとって**モジュラー時間 $t$ = Lorentz boost パラメータ × $1/2\pi$**。

## 3. CHM 一般化 (Casini-Huerta-Myers 2011)

球領域 $A = \{|\vec{x}| < R\}$ の真空モジュラーフローは
$$K_A = 2\pi \int_A \frac{R^2 - |\vec{x}|^2}{2R}\, T_{00}\, d^{d-1}x.$$

$\sigma_t$ で1点 $\vec{x}$ が描く軌跡は、ターゲット境界 $|\vec{x}|=R$ 付近では遅く、中心では速い。
これは**球内に閉じこもる時計** = 共形 Killing flow である。

## 4. 熱的時間仮説 (Connes-Rovelli)

$\mathcal{M}$ の自己準同型として、$\sigma_t^\omega$ は**状態 $\omega$ にしか依らない**。
時計は外部に置かれた絶対時間ではなく、**観測対象の状態が自分で決める**。

→ 別の状態 $\omega'$ は別の時間 $\sigma_t^{\omega'}$ を持つ。
これが「時間の起源は状態のエンタングルメント構造」と読み替えられる。

## 5. 自由フェルミオン 1次元鎖での実装

1点関数行列 $M_A = \log[(1-C_A)/C_A]$ から、単粒子部分のモジュラーフローは
$$\sigma_t(c_i) = \sum_j [e^{-iM_A t}]_{ij}\, c_j.$$

検証量：
1. **Bisognano–Wichmann 半直線**：$A = [0, \infty)$ では $M$ が boost generator。固有モードは Rindler モード。
2. **CHM 区間**：$A=[0, L)$ では $M$ の局所重み (= 対角) が $x(L-x)/L$ に従う (Phase 2 で確認済)。
3. **モジュラー速度の位置依存性**：単一サイト初期状態の即時拡散率
   $$v(x_0)^2 := \langle x_0 | M_A^2 | x_0 \rangle - \langle x_0 | M_A | x_0 \rangle^2$$
   が CHM Killing 核の平方 $\propto (R^2 - (x-x_0)^2)^2$ に従う。
4. **熱的時間の状態依存性**：基底状態と熱状態で $M_A^{\text{vac}}$ と $M_A^{\text{therm}}$ が異なる → 異なる時間流。

この4つを数値で示せば「時間 = 状態のモジュラーフロー」の最小実証になる。
