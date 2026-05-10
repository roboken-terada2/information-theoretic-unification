# Phase 3: ホログラフィー — MERAテンソルネットワークと創発AdS₃

## 1. 動機と歴史

Phase 1 で 1 次元境界 (S¹) が情報距離から創発した。Phase 2 でその境界 CFT のエンタングルメント変分が線形化Einstein 方程式に化けることが示せた。
ここでは「**バルクの双曲幾何 (AdS₃) も同じく情報構造から出る**」ことを示す。鍵は MERA (Multi-scale Entanglement Renormalization Ansatz, Vidal 2007)。

Swingle 2012 の主張：MERA の幾何的構造は**離散 AdS 空間**そのものである。

## 2. MERA の構成

1次元 $N$ 点の臨界状態を、層数 $\log_2 N$ の階層で粗視化する：
- **層 0**：$N$ サイト = 物理境界
- **層 $k$**：$N/2^k$ サイトに粗視化 (1サイト=旧2サイトのエンタングル粗視像)
- **層 $\log_2 N$**：1サイト = 全系の積分

各層内には**ディスエンタングラー** (隣接サイト間のユニタリ)、層間には **アイソメトリ** (2→1 の縮約) がある。隣接性グラフは円筒面上の二分木である。

## 3. 創発双曲幾何

MERA グラフ上の最短パス長 $d_G(i,j)$ は、境界の2点 $i, j$ に対し：
$$d_G(i, j) \approx 2 \log_2 |i - j| + \text{const}.$$
これは双曲計量
$$ds^2_{\text{AdS}_3} = R^2\!\left(\frac{-dt^2 + dz^2 + dx^2}{z^2}\right)$$
における境界2点間の測地線長 $L = 2R \log\!\left(|x_1 - x_2|/\epsilon\right)$ と**同じスケーリング**。
ここで $z$ は MERA の層番号 = 創発する**動径方向 (energy scale)**。

## 4. Ryu–Takayanagi 公式の MERA 版

境界の長さ $L$ の区間 $A$ を取り、MERA 上で「$A$ に出入りする全ての枝を切る最小カット」の枝数を $|\gamma_A|$ とする：
$$S_A^{\text{RT}} = \frac{|\gamma_A|}{4 G_N}.$$
最小カットは「層 $k = \log_2 L$ まで $A$ の両端から登り、その層で水平に渡る」ので
$$|\gamma_A| \sim 2 \log_2 L.$$

CFT 結果 $S_A = \frac{c}{3} \log L$ と比較し
$$\frac{2}{4 G_N \log 2} = \frac{c}{3} \quad \Rightarrow \quad \frac{1}{G_N} = \frac{2 c \log 2}{3}.$$
これは Brown–Henneaux $c = 3 R_{\text{AdS}}/(2 G_N)$ の格子版 (適切な単位選択で)。

## 5. Poincaré 円板への埋め込み

MERA の各ノード $(k, m)$ を、Poincaré 円板に
$$r_k = \tanh(k \, \Delta\rho/2), \qquad \theta_m = 2\pi (m + 0.5)/(N/2^k)$$
で配置する ($\Delta\rho$ は層あたりの双曲距離)。境界 ($k=0$) は $r=0$ ではなく $r \to 1$ に置く規約 (Lobachevsky 内部時間 = MERA 上方向)。

## 6. 本シミュレーションの計画

### (i) 純グラフ的検証 (情報構造に依らない MERA 幾何)
- 二分木 MERA グラフを構築。
- BFS で全ペア最短距離 $d_G$ を計算。
- 境界2点 $(i, j)$ に対し $d_G(i, j)$ vs $|i - j|$ を log-log プロット。傾き $\approx 2$ (= $2 \log_2 |i-j|$ と整合)。

### (ii) RT 公式の検証
- 境界の各長さ $L$ の区間に対し、MERA 上の最小カット枝数 $|\gamma_A|$ を計算。
- これが $\sim 2 \log_2 L$ になることを示す。
- 同時に XX 模型基底状態の真の $S_A(L)$ を比較し、**形状が一致する**ことを確認 (Brown–Henneaux 関係の数値検証)。

### (iii) Poincaré 円板可視化
- MERA を双曲円板に埋め込み、視覚的に AdS₃ の時空切片であることを示す。
- 1つの境界区間に対する RT 面 (バルク内測地線) を描画。

これにより**境界の 1D 量子情報構造から、バルクの 2D 双曲時空が完全に再構成される**ことを数値的・視覚的に示す。
