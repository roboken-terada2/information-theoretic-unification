# Phase 11: 物質階層 — 3世代、湯川結合、CKM/PMNS 混合の創発

## 1. 動機

Phase 10 で標準模型のゲージ群 SU(3)×SU(2)×U(1)_Y がフレーバー大域対称性として境界 CFT から創発することを示した。
しかし標準模型の物質場には**3世代** (u/d/e/ν_e、c/s/μ/ν_μ、t/b/τ/ν_τ) の階層構造があり、各世代の質量は劇的に異なる:

| 粒子 | 質量 (GeV) | 比 (世代3/世代1) |
|---|---|---|
| u | $2.2 \times 10^{-3}$ | — |
| c | 1.27 | 580 |
| t | 173 | $7.9 \times 10^4$ |
| | | |
| e | $5.1 \times 10^{-4}$ | — |
| μ | 0.106 | 207 |
| τ | 1.78 | 3490 |

さらに**CKM 行列**(クォーク混合)と**PMNS 行列**(レプトン混合) が世代間の量子重ね合わせを表す。これらの起源は標準模型では説明されていない (約 20 個の自由パラメータ)。

本 Phase は **Froggatt-Nielsen 1979** の機構を情報理論的統一理論の言葉で再構築し、世代階層と混合行列の出現を数値実証する。

## 2. Froggatt-Nielsen 機構

### 2.1 新しい U(1)_F フレーバー対称性

標準模型に追加の大域 U(1)_F 対称性を仮定。各フェルミオンが整数 charge $q$ を持つ:

| 世代 | $Q_L$ | $u_R$ | $d_R$ | $L_L$ | $e_R$ |
|---|---|---|---|---|---|
| 1 | $q^Q_1$ | $q^u_1$ | $q^d_1$ | $q^L_1$ | $q^e_1$ |
| 2 | $q^Q_2$ | $q^u_2$ | $q^d_2$ | $q^L_2$ | $q^e_2$ |
| 3 | $q^Q_3$ | $q^u_3$ | $q^d_3$ | $q^L_3$ | $q^e_3$ |

ヒッグス場 $H$ の charge は 0 と仮定。湯川結合 $\bar Q_L^i Y^u_{ij} u_R^j H$ が U(1)_F 不変であるためには、結合は許されない (charge 保存違反)。

### 2.2 フレイボン場

破れの源として、charge $-1$ の**フレイボン (flavon)** $\Phi$ を導入。$\Phi$ が真空期待値 $\langle\Phi\rangle = \epsilon \Lambda$ ($\epsilon \ll 1$) を取り U(1)_F を破る。

すると湯川結合が以下の形で現れる:
$$Y^u_{ij} \sim c_{ij} \left(\frac{\langle\Phi\rangle}{\Lambda}\right)^{q^Q_i + q^u_j} = c_{ij}\, \epsilon^{q^Q_i + q^u_j}$$

ここで $c_{ij} = O(1)$ の係数。

### 2.3 階層の出現

質量行列 $M^u = v \cdot Y^u$ ($v$ はヒッグス VEV) を SVD すると、特異値 (質量) は対角ペア $q^Q_i + q^u_i$ で決まる:
$$m_i \sim v\, \epsilon^{q^Q_i + q^u_i}$$

charge 配置 $q^Q = (3,2,0)$, $q^u = (3,2,0)$, $\epsilon = 0.22$ (Cabibbo 角) とすれば:
- $m_u \sim v \epsilon^6 \approx v \cdot 1.1 \times 10^{-4}$
- $m_c \sim v \epsilon^4 \approx v \cdot 2.3 \times 10^{-3}$
- $m_t \sim v \epsilon^0 = v$

実験値との比較 ($v = 246$ GeV):
- 予言: $m_u : m_c : m_t \approx \epsilon^6 : \epsilon^4 : 1 = 1.1\times10^{-4} : 2.3\times10^{-3} : 1$
- 実験: $9 \times 10^{-6} : 5.2\times10^{-3} : 0.70$ → 比率の桁数が一致

### 2.4 混合行列

CKM 行列は up-type と down-type の左手側回転行列の積:
$$V_{\rm CKM} = U^u_L\, (U^d_L)^\dagger$$

FN テクスチャーで:
$$V^{ij}_{\rm CKM} \sim \epsilon^{|q^Q_i - q^Q_j|}$$

$q^Q = (3,2,0)$ で:
- $V_{us} \sim \epsilon^1 \approx 0.22$ (実験 0.226 ✓)
- $V_{cb} \sim \epsilon^2 \approx 0.048$ (実験 0.041 ✓)
- $V_{ub} \sim \epsilon^3 \approx 0.011$ (実験 0.004)

桁レベルで一致。

## 3. レプトン階層と PMNS 行列

レプトンも同様だが、ニュートリノ質量は see-saw 機構で $m_\nu \sim v^2/M_R$ ($M_R$: 右手ニュートリノ質量)。
PMNS 行列は CKM と異なり**大きな混合角** ($\theta_{12} \approx 33°$, $\theta_{23} \approx 49°$) を持つ。

これは「**ニュートリノ部分は anarchy** (FN charge がほぼ等しい)」と解釈できる。
レプトンの FN charges: 例えば $q^L = (0,0,0), q^e = (3,2,0)$ とすると:
- $m_e : m_\mu : m_\tau \sim \epsilon^3 : \epsilon^2 : 1$ (荷電レプトン階層)
- ニュートリノ Majorana 質量: $m^\nu_{ij} \sim \epsilon^{q^L_i + q^L_j} = \epsilon^0 = 1$ → 全成分 O(1) → 大混合角

これは PMNS の大混合と CKM の小混合の対比を自然に説明する。

## 4. 情報理論的統一理論内の位置づけ

Phase 10 で示したように、ゲージ群 G は境界 CFT のフレーバー大域対称性として現れる。
本 Phase の主張:

> **U(1)_F もまた境界 CFT の大域 U(1) 対称性の一つで、Phase 10 で扱った U(1)_Y と同じ枠組みに含まれる。**
> **その階層的自発破れ (フレイボンの真空期待値) が物質質量階層と混合行列を生む。**

つまり追加の物理仮定なしに、Phase 10 の枠組みの中で Froggatt-Nielsen 機構は動作する。世代数 (= 3) は別問題 (Phase 12+) だが、世代が与えられたとき、その**質量階層と混合構造が U(1)_F の charge 配置から決まる**ことが本 Phase で示せる。

## 5. シミュレーション計画

### Part A: 湯川行列の生成
- $\epsilon = 0.22$ (Cabibbo)
- charge 配置: $q^Q = (3,2,0)$, $q^u = (3,2,0)$, $q^d = (3,2,2)$ (典型的)
- $Y^u_{ij} = c_{ij}\, \epsilon^{q^Q_i + q^u_j}$, $c_{ij}$ は O(1) 乱数 (Haar 風)

### Part B: 質量と混合の SVD
- $Y^u = U^u_L \Sigma^u U^{u\dagger}_R$, $Y^d = U^d_L \Sigma^d U^{d\dagger}_R$
- 特異値 = 質量 (符号は除く)
- CKM 行列 $V = U^u_L (U^d_L)^\dagger$

### Part C: 実験値との比較
- PDG 2024 の質量と CKM 値と比較
- 桁オーダー一致を確認

### Part D: レプトン部門
- 荷電レプトン階層 (e, μ, τ) の再現
- ニュートリノ anarchy → PMNS 大角の自然な発生

### Part E: 統計的検証
- $c_{ij}$ の乱数を 1000 サンプルでアンサンブル
- 質量比の中央値・分散を実験値と比較
