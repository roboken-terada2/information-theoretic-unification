# Phase 2: エンタングルメント第1法則と線形化Einstein方程式

## 1. モジュラーハミルトニアン

$\rho_A = e^{-K_A}/Z_A$ と書いたとき $K_A = -\log\rho_A$ をモジュラーハミルトニアンと呼ぶ。
これは「サブシステム $A$ から見た熱力学的エネルギー」の役割を果たす。

**重要事実 1 (Bisognano-Wichmann)**：1+1D CFT の真空で半直線 $A=(0,\infty)$ をとると、
$$K_A = 2\pi \int_0^\infty x\, T_{00}(x)\, dx.$$
$K_A$ は**局所**で、Rindler 観測者のハミルトニアン $\times 2\pi$ に等しい。

**重要事実 2 (Casini-Huerta-Myers 2011)**：$d$ 次元 CFT 真空で球領域 $A$ (半径 $R$, 中心 $\vec{x}_0$):
$$K_A = 2\pi \int_A \frac{R^2 - |\vec{x} - \vec{x}_0|^2}{2R}\, T_{00}(\vec{x})\, d^{d-1}x.$$
これも局所で、共形 Killing ベクトルで重みづけられている。

**重要事実 3 (Peschel 2003)**：自由フェルミオン (Gaussian) 状態では、
$$K_A = \sum_{i,j \in A} M_{ij}\, c_i^\dagger c_j, \qquad M_A = \log\!\left(\frac{1 - C_A}{C_A}\right),$$
ここで $C_A$ は $A$ 内の2点関数の行列。$K_A$ は2次形式に閉じる。

## 2. エンタングルメント第1法則 (entanglement first law)

任意の1パラメータ族 $\rho(\lambda) = \rho^{(0)} + \lambda\, \delta\rho + O(\lambda^2)$ ($\mathrm{Tr}\,\delta\rho = 0$) に対し、von Neumann エントロピーの1次変分は
$$\delta S(A) = -\mathrm{Tr}[\delta\rho_A \log\rho_A^{(0)}] = \mathrm{Tr}[\delta\rho_A K_A^{(0)}] = \delta\langle K_A^{(0)} \rangle.$$

これは**熱力学第1法則のエンタングルメント版**：
$$\boxed{\delta S_A = \delta \langle K_A \rangle}$$
$K_A$ が逆温度 $1/2\pi$ の Rindler 観測者の Hamiltonian なら、これは Clausius $\delta Q = T\, \delta S$ に他ならない。

## 3. 線形化 Einstein 方程式の導出 (FGHMR 2014)

ホログラフィー (AdS/CFT) では Ryu–Takayanagi により
$$S_A = \frac{\text{Area}(\gamma_A)}{4 G_N}.$$

両辺の摂動：
$$\underbrace{\delta S_A}_{\text{量子情報}} = \underbrace{\frac{\delta \text{Area}(\gamma_A)}{4 G_N}}_{\text{幾何}}.$$

第1法則 $\delta S_A = \delta\langle K_A\rangle$ と組み合わせて、球領域に対する CHM 形式：
$$\frac{\delta \text{Area}(\gamma_A)}{4 G_N} = 2\pi \int_A \frac{R^2 - r^2}{2R}\, \delta\langle T_{00}\rangle\, d^{d-1}x.$$

**FGHMR の結果**：この等式が**全ての球領域 $A$ に対して成立する** $\Leftrightarrow$ バルクで線形化Einstein 方程式
$$\delta G_{\mu\nu}^{(1)} = 8\pi G_N\, \delta T_{\mu\nu}$$
が成立する (AdS 真空の周辺)。

つまり「エンタングルメント第1法則 + RT 公式」 ⇔ 「線形化 Einstein 方程式」。

## 4. Brown–Henneaux 関係 (CFT パラメータ → 重力パラメータ)

1+1D CFT 中心電荷 $c$ と AdS$_3$ 半径 $R_{\text{AdS}}$, Newton 定数 $G_N$ の関係：
$$c = \frac{3 R_{\text{AdS}}}{2 G_N} \quad \Longleftrightarrow \quad \frac{R_{\text{AdS}}}{G_N} = \frac{2c}{3}.$$

Phase 1 で XX 模型は $c \approx 1$ と数値的に確認済み → 創発する AdS$_3$ で $R/G = 2/3$。
これにより、各エンタングルメントエントロピーの値は $1/(4G_N)$ 倍の創発双曲幾何上の測地線長さに等しい。

## 5. 本シミュレーションの戦略

1. 自由フェルミオン基底状態 $\rho^{(0)}$ (XXモデル) を「真空」とする。
2. Peschel から $K_A^{(0)} = \sum M_{ij} c_i^\dagger c_j$ の行列 $M$ を求める。
3. 摂動として温度 $T$ の熱平衡状態 $\rho(T)$ を用いる:
   $C_{ij}(T) = \sum_k U_{ik}\, n_F(\epsilon_k/T)\, U_{jk}^*$.
4. 各 $T$ で：
   - $\delta S_A(T) = S(\rho_A(T)) - S(\rho_A^{(0)})$ を直接計算
   - $\delta\langle K_A\rangle(T) = \mathrm{Tr}_A[M_A \cdot (C_A(T) - C_A^{(0)})]$
5. 両者をプロット、$T \to 0$ で完全一致 (1次)、有限 $T$ では $T^2$ で外れる ($\delta\rho^2$ の高次項) ことを確認。

これは線形化Einstein方程式の**検証**であり、(Phase 1 の RT 関係と組み合わせて) 「重力場の方程式が量子情報法則の帰結である」ことの数値的証拠になる。
