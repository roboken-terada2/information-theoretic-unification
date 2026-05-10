# Phase 9: 動的時空 — クエンチ動力学からの宇宙論的進化

## 1. 動機

Phase 1-8 は静的な時空構造の創発を扱った。Phase 4 ではモジュラーフロー $\sigma_t^\omega$ が時間として機能することを示したが、宇宙論的時間 (= 我々の宇宙が経験する膨張する時間) との接続は未完。

本 Phase は **量子クエンチ動力学** を「ビッグバン後の宇宙進化」のミニマル模型として用い、以下を実装する：

- 「ビッグバン」 = 高エネルギー初期状態 (Néel 状態)
- 「宇宙の進化」 = 自由フェルミオン Hamiltonian による Heisenberg 進展
- 「粒子地平線」 = エンタングルメント光円錐 (Lieb-Robinson 速度 $v_F$)
- 「熱平衡化」 = Calabrese-Cardy エントロピー飽和 = 宇宙の熱史

## 2. クエンチ設定

### 2.1 初期状態 (Big Bang)

$$|\psi_0\rangle = c_0^\dagger c_2^\dagger c_4^\dagger \cdots |0\rangle$$

これは Néel (反強磁性) 状態。相関行列は $C_{ij}(0) = \delta_{ij}\,\delta_{i \bmod 2, 0}$。

### 2.2 時間進展

XX Hamiltonian $H = -\sum_i (c_i^\dagger c_{i+1} + \mathrm{h.c.})$ で
$$|\psi(t)\rangle = e^{-iHt}|\psi_0\rangle, \qquad C(t) = e^{iht}C(0)e^{-iht}.$$

ここで $h$ は単粒子ホッピング行列 ($h$ の Heisenberg 進展で C(t) が得られる)。

## 3. 主要予言

### 3.1 Calabrese-Cardy エントロピー成長 (2005)

長さ $L$ の区間 $A$ について、クエンチ後のエンタングルメント成長:
$$S_A(t) \approx \begin{cases} \alpha\, v_F\, t & t < L/(2 v_F) \quad \text{(線形成長期)}\\ \beta\, L & t > L/(2 v_F) \quad \text{(飽和期)} \end{cases}$$

ここで $v_F = 2$ は XX 鎖の Fermi 速度、$\alpha, \beta$ は初期状態の有効温度に依存する定数。
これは Lieb-Robinson 1972 の因果性束縛から導かれる「**情報の弾道的伝播**」の現れ。

### 3.2 光円錐構造

任意の 2 点 $(i,j)$ の相互情報量 $I(i,j;t)$ は:
- $|i-j| > 2 v_F t$：因果的に切断、$I \approx 0$
- $|i-j| \lesssim 2 v_F t$：有限値

**$|i-j|$ vs $t$ 平面で「光円錐」が見える**。これは Phase 1-8 の静的時空に欠けていた**因果構造**の創発。

### 3.3 宇宙論的解釈

クエンチ動力学の物理量と FRW 宇宙論の対応:

| クエンチ | FRW 宇宙論 |
|---|---|
| 時間 $t$ | 宇宙年齢 $t$ |
| 光円錐速度 $v_F$ | 光速 $c$ |
| 粒子地平線 $L_H(t) = v_F t$ | 粒子地平線 $L_H(t) \sim t$ |
| $H_{\rm eff}(t) \equiv \dot L_H/L_H = 1/t$ | Hubble rate $H \sim 1/t$ (放射優勢で) |
| $S_A(t)$ 線形成長 | エントロピー生成 (脱平衡) |
| $S_A$ 飽和 | 熱平衡 |
| Néel 初期 | ビッグバン (低エントロピー) |

これは「**有限系のクエンチ動力学が局所的に FRW 宇宙論をシミュレートする**」という Hayden-Preskill の脈絡で議論される。

### 3.4 モジュラー熱化

Phase 4 の Peschel modular Hamiltonian $M_A(t)$ も時間進展：
- $t = 0$: 初期状態 Néel → $C_A(0)$ は対角 → $M_A(0)$ は単純な対角行列
- $t \to \infty$: 熱化 → $C_A(\infty)$ は熱状態に近い → $M_A(\infty)$ は CHM Killing kernel に収束

これは「**初期状態の特殊性が消え、状態がモジュラー的に熱平衡へ向かう**」過程の数値実証。
熱的時間仮説 (Connes-Rovelli) の動的バージョン。

## 4. シミュレーション計画

### Part A: クエンチ動力学
- $N = 64$, OBC 鎖、Néel 初期状態
- $h$ の固有分解で $C(t) = e^{iht}C(0)e^{-iht}$ を高速計算
- $t \in [0, 30]$ で 80 点

### Part B: Calabrese-Cardy フィット
- 中央区間 $A = [N/4, 3N/4)$ ($|A| = 32$) で $S_A(t)$
- 線形領域 ($t < L/4$) でスロープ計算 → $\alpha v_F$
- 飽和値で平均 → エントロピー密度

### Part C: 光円錐 heatmap
- 中央サイト $i_0 = N/2$ から各他サイト $j$ への $I(i_0, j; t)$
- 距離 $\times$ 時間平面でカラーマップ
- 因果円錐 $|j - i_0| = 2 v_F t$ の存在確認

### Part D: 有効 Hubble パラメータ
- 「光円錐半径」$L_H(t) \equiv$ {$I > $ 閾値} の最大距離
- $H_{\rm eff}(t) = \dot L_H / L_H$
- $L_H(t) \sim t$, $H \sim 1/t$ の確認

### Part E: モジュラー Hamiltonian の熱化
- $M_A(t)$ を $t = 0, t = L/(4 v_F), t = L/(2 v_F)$ で計算
- 対角プロファイル $M_{ii}(t)$ の時間進展
- $t \to \infty$ で CHM kernel $\propto x(L-x)/L$ に収束する様子

## 5. 期待される結果と限界

✅ 期待:
- Calabrese-Cardy 線形 + 飽和の定量確認
- 光円錐の鮮明な可視化 (= 因果構造の創発)
- $L_H \propto t$ の確認 (= 「宇宙膨張」の最小モデル)

⚠️ 限界:
- 真の FRW 宇宙論には**幾何的膨張** ($a(t) \sim t^{2/3}$ など) が必要だが、これは Hamiltonian だけからは出ない (時空計量が時間依存する設定が必要)
- 本 Phase の「膨張」は**情報的膨張** (因果的に接続された領域の成長) であり、**計量的膨張** (空間自体の伸縮) とは異なる
- 真の動的時空は Phase 9+1 で Witten 2022 の type II 代数 + crossed product に取り組む必要

それでも、**情報理論的枠組みでの宇宙論的時間進化**の最小モデルとしてこれは強力な実証となる。
