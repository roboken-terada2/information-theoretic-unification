# Phase 8: 真の 4 次元化 — AdS₅/CFT₄ 対応

## 1. 動機

Phase 1-6 は 1D 境界 (AdS₃/CFT₂)、Phase 7 は 2D 境界 (AdS₄/CFT₃) で行った。
**我々の宇宙は 3+1 次元**であり、対応する量子重力理論は AdS₅/CFT₄。これは Maldacena 1997 で発見された最も研究された AdS/CFT 対応であり、現実的な量子重力の最有力候補。

本 Phase は 3 次元正方格子の自由フェルミオンを境界 CFT₄ の最小モデルとし、Phase 1-7 の中心命題

$$\delta S(\rho_A) = \delta\,\mathrm{Tr}[K_A^{(0)} \rho_A] \quad \forall A$$

が**真の 4 次元物理**に拡張されることを数値的に示す。

## 2. 3D 立方格子フェルミオン

3 次元立方格子上の最近接ホッピング:
$$H = -\sum_{\langle ij\rangle} (c_i^\dagger c_j + \mathrm{h.c.})$$

PBC でフーリエ変換すると分散 $\epsilon(\vec k) = -2(\cos k_x + \cos k_y + \cos k_z)$。半占有 ($\mu=0$) でフェルミ面は **2 次元曲面** $\cos k_x + \cos k_y + \cos k_z = 0$ となり、$d=3$ の **臨界系**。

## 3. Gioev-Klich 公式の 3 次元版

$d$ 次元自由フェルミオンの基底状態でフェルミ面の余次元 $d_F$ が 1 (= 一般の Fermi 液体) なら：

$$S(A) \sim L^{d-1} \log L$$

3 次元なら $S(L^3) \sim L^2 \log L$。これは「**area law of $L^{d-1}$ + 対数補正 from 1D Fermi 面**」の形。

予言される L²log L 比:
- $S(L=2) / S(L=1) = 4 \log 2 / \log 1 = $ ill-defined (use ratios L>1)
- $S(L=4) / S(L=2) \to 16 \log 4 / 4 \log 2 = 8$
- $S(L=3) / S(L=2) \to 9 \log 3 / 4 \log 2 \approx 3.56$

数値で 4-8 程度の比なら整合。

## 4. AdS₅ の 4D MERA

3 次元境界の binary MERA：
- 層 $k$: $(N/2^k)^3$ サイト
- 同層内: 6 近傍接続 (3D 正方格子)
- 層間: 各上層サイトは下層 $2 \times 2 \times 2 = 8$ ブロックを縮約

$8 \times 8 \times 8 = 512$ サイトに対し 3 層 (512 → 64 → 8 → 1) で計 585 ノード。
これは **4 次元構造** (3 空間 + 1 動径 = energy scale)。

**予言** (Swingle 2012 の 3D 一般化):
- 境界 2 点間のグラフ距離 $\sim 2 \log_2 |\vec r_1 - \vec r_2|$
- これは **AdS₅ 双曲幾何** における境界 2 点の測地線

## 5. Brown-Henneaux 一般化と Newton 定数

AdS$_{d+1}$/CFT$_d$ で Brown-Henneaux 関係は次のように一般化される:

$$\frac{R_{\rm AdS}^{d-1}}{G_N^{(d+1)}} \propto C_T$$

ここで $C_T$ は CFT の応力テンソル 2 点関数係数 (中心電荷の高次元類推)。
4 次元 CFT₄ の場合 $C_T \sim N^2$ (= $\mathcal{N}=4$ Yang-Mills の SU(N) の階数の自由度数)。

## 6. シミュレーション計画

### Part A: 3D フェルミオン基底状態と面積則
- 8×8×8 = 512 サイトの相関行列
- $L \times L \times L$ 立方領域の S(L) を $L = 2, 3, 4$ で計算
- $S(L) = a L^2 \log L + b L^2 + c L + d$ の係数を fit

### Part B: 効率的な MI 計算
- 130816 ペアの 2 サイトエントロピーを **ベクトル化**して計算 (2x2 行列の解析的固有値)
- 距離行列・MDS で情報幾何の次元性を評価

### Part C: 4D MERA グラフ距離
- 3D MERA 構築 (~ 585 ノード)
- BFS で全境界ペア間グラフ距離計算
- $d_{\rm graph} \sim a \log d_{\rm phys}$ の係数を fit
- AdS₅ 予言 $a = 2/\log 2 \approx 2.885$ と比較

### Part D: 哲学的含意
- 数値結果が AdS₅ 予言と整合すれば、Phase 1-6 の枠組みが我々の宇宙の真の 4 次元重力に適用可能

## 7. 期待される一致度

|  | 1D (Phase 3) | 2D (Phase 7) | 3D (Phase 8 期待値) |
|---|---|---|---|
| 境界サイト数 | 64 | 256 | 512 |
| MERA ノード | 127 | 341 | 585 |
| 距離スロープ精度 | 0.4% | 5% | 5-15% |

格子効果がより大きく、近距離有限サイズ補正もきつくなるので、3D では 1D ほどの精度は期待できないが、**スケーリング則の存在**は確認できるはず。
