# Phase 7: 4次元化 — 2D 境界 CFT と AdS₄ バルク

## 1. 動機

Phase 1-6 は全て 1+1D CFT で行われた (XX 鎖)。これに対応するバルクは 2+1D AdS₃。
我々の現実の宇宙は 3+1D で、対応する量子重力理論は AdS$_5$/CFT$_4$ または AdS$_4$/CFT$_3$。

本 Phase では **2次元境界 CFT** に拡張する。これは AdS$_4$ の境界に対応し、3+1D 重力理論の最小モデルを与える。
1次元の段階で確立した枠組み:

$$\delta S(\rho_A) = \delta\,\mathrm{Tr}[K_A^{(0)}\rho_A] \quad \forall A$$

が高次元でも成立することを示すのが目的。

## 2. 2D 自由フェルミオンの基底状態

2次元正方格子 $N_x \times N_y$ 上の最近接ホッピング模型：
$$H = -t\sum_{\langle i,j\rangle} (c_i^\dagger c_j + \mathrm{h.c.})$$

PBC でフーリエ変換すると分散 $\epsilon(\vec k) = -2t(\cos k_x + \cos k_y)$。半占有 ($\mu=0$) でフェルミ面は $\cos k_x + \cos k_y = 0$ の正方形 $|k_x| + |k_y| = \pi$。

**ギャップレス・臨界系**：1D の場合と同様、フェルミ点の集合がフェルミ面 (1次元曲線) になり、エンタングルメントが対数的に増大。

## 3. Gioev–Klich 公式 (面積則の対数補正)

Gioev-Klich 2006、Wolf 2006 の結果：$d$ 次元自由フェルミオンの基底状態で領域 $A$ ($\partial A$ は $(d-1)$ 次元) のエンタングルメントエントロピーは
$$S(A) \sim \frac{1}{12} \frac{1}{(2\pi)^{d-1}} L^{d-1} \log L \cdot \left(\int_{\partial \Omega_A} d\sigma_x\right)\left(\int_{\partial F} |n_x\cdot n_k|\, d\sigma_k\right)$$

2D 正方格子半占有の場合 ($d=2$, $L\times L$ 領域)：
$$S(L) \approx c_1 L \log L + c_2 L + c_3$$
$c_1$ はフェルミ面の幾何的不変量で決まる。

これは「面積則の log 因子による対数補正」(area law with log violations) と呼ばれ、臨界系の特徴。Phase 1 の 1D CFT で見た $S \sim (c/3) \log L$ の高次元類推。

## 4. 2D MI 行列と幾何の復元 (Phase 1 一般化)

各サイト対 $(i,j)$ について相互情報量 $I(i:j)$ を計算。Phase 1 と同じ Cao-Carroll-Michalakis 流の距離
$$d(i,j) = -\log\!\left(\frac{I(i:j)}{2\min(S_i, S_j)}\right)$$
を構築し、古典的多次元尺度構成 (MDS) で 2 次元埋め込み。

**予言**：上位 2 個の MDS 固有値が支配的 → 元の 2 次元格子幾何が再構成される。

これは「**情報構造から創発する空間が 2D**」ことを示す Phase 1 の高次元拡張。

## 5. 3D MERA と AdS₄ バルク

2D MERA (Vidal 2009)：
- 層 $k$：$(N_x/2^k) \times (N_y/2^k)$ 格子
- 各層内には disentangler (4近傍接続)
- 層間には isometry (各上層サイトが下層 $2\times 2$ ブロックを縮約)

総ノード数 $\sum_{k=0}^{\log_2 N} N^2/4^k \approx (4/3) N^2$。
グラフは **3次元構造**：2 つの空間方向 + 1 つの energy scale 方向 (AdS の動径方向)。

**予言** (Swingle 2012 の 2D 一般化):
- 境界 2 点 $(i, j)$ 間のグラフ距離 $\sim 2 \log_2 |i-j|$
- これは **AdS₄ 双曲幾何**における境界 2 点の測地線長と同じスケーリング

**Brown-Henneaux 一般化** (4D 重力):
$$\frac{R_{\rm AdS}^2}{G_{N,4}} \propto C_T$$
ここで $C_T$ は 2D CFT の応力テンソル 2点関数係数 (中心電荷の高次元類推)。

## 6. Ryu-Takayanagi の 4次元化

2D 境界の領域 $A$ に対し、AdS₄ バルク内の最小 2 次元曲面 (面積 $\mathrm{Area}(\gamma_A)$) を取ると：
$$S_A = \frac{\mathrm{Area}(\gamma_A)}{4 G_{N,4}}$$

3D MERA の最小カット (= $A$ を境界の他から切り離す最小エッジ集合) はこの公式の離散版を実現。

## 7. 本 Phase のシミュレーション計画

### 7.1 Part A: 2D 自由フェルミオン基底状態

- $16\times 16$ 正方格子 PBC、半占有
- ホッピング行列対角化で相関行列 $C$ (256x256) を計算
- 中央 $L\times L$ 領域 ($L=2,...,7$) で $S(L)$ を計算
- フィット $S(L) = a L\log L + b L + c$、係数 $a$ が Gioev-Klich 予言と整合するか確認

### 7.2 Part B: 2D MI 幾何

- 全 256x255/2 = 32640 ペアの MI 計算
- 距離行列 → MDS → 2D 埋め込み
- 元の格子座標 (x, y) と比較 → R^2 値で評価

### 7.3 Part C: 3D MERA と AdS₄

- 16x16 の binary MERA グラフ (5 層、341 ノード)
- BFS で全ペアグラフ距離計算
- 境界 2 点について $d_{\rm graph}$ vs $\log|i-j|$ のスケーリング検証
- 係数を $2/\log 2$ と比較

## 8. 期待される一致度と限界

- 1D で見た 0.4% 精度は 2D では達成困難 (より複雑なフェルミ面、有限格子効果が大きい)
- それでも：(i) 面積則の log 補正が見えれば臨界性確認、(ii) MDS が 2D 復元すれば情報→空間の 2D 版確認、(iii) AdS₄ 距離スケーリングが log → 双曲性確認、と質的成功は期待できる
- Phase 1-6 の枠組みが「次元によらず成立する」ことの数値的証拠
