# Phase 17: 非線形 Einstein 方程式 — エンタングルメント第2法則と量子 Fisher 情報

## 1. 動機

Phase 2 で線形化 Einstein 方程式 $\delta G_{\mu\nu}^{(1)} = 8\pi G_N \delta T_{\mu\nu}$ が**エンタングルメント第1法則** $\delta S = \delta\langle K\rangle$ から導かれることを示した。

しかし観測的に重要な現象 (BH 合体・重力波伝播・宇宙進化等) は**非線形** Einstein 方程式
$$G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$$
が必要。本 Phase ではこれを**エンタングルメント第2法則** (= 相対エントロピーの 2 次展開) から導出する数値的足がかりを与える。

## 2. 第2次までの展開

任意の1パラメータ族 $\rho(\lambda) = \rho^{(0)} + \lambda\,\delta\rho + \tfrac{1}{2}\lambda^2 \delta^2\rho + \cdots$ に対し:

### 2.1 第1法則 (Phase 2 で示済)
$$\delta S = \delta\langle K\rangle \quad (\text{1 次})$$

### 2.2 第2法則 (本 Phase)
相対エントロピーの**Taylor 展開**:
$$S(\rho_\lambda || \rho^{(0)}) = \frac{1}{2}\, g_F^{(0)}\, \lambda^2 + O(\lambda^3)$$

ここで $g_F^{(0)}$ は**量子 Fisher 情報** (Bures metric):
$$g_F^{(0)} = \mathrm{Var}(K^{(0)})_{\rho^{(0)}} = \langle (K^{(0)})^2\rangle - \langle K^{(0)}\rangle^2$$

つまり**モジュラーハミルトニアンの分散**。

### 2.3 Casini 流の書き換え
Phase 2 で $S_{\rm rel} = \delta\langle K\rangle - \delta S$ を確認した。展開すると:
$$S_{\rm rel}(\lambda) = \frac{1}{2}\mathrm{Var}(K) \lambda^2 + \frac{1}{6} S_3 \lambda^3 + \cdots$$
ここで $S_3$ は 3 次累積量。

**核心**: $\lambda^2$ 係数は**ヒルベルト空間のリーマン計量**であり、バルクの非線形重力構造を完全に決定する。

## 3. バルクとの双対 (Faulkner et al. 2017)

ホログラフィックな含意:
- $\mathrm{Var}(K_A) = \langle T_{\mu\nu}(x) T_{\rho\sigma}(y)\rangle$ の積分 (CFT 応力テンソルの 2 点関数)
- これは**バルクの重力子-重力子相互作用**に直接対応 (3 点関数のレベル)
- 全次数を積み上げると**非線形 Einstein 方程式** $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$ 完全形

$$\boxed{\;\;\text{エンタングルメントの全次展開} \;=\; \text{完全 Einstein 方程式}\;\;}$$

## 4. 自由フェルミオン上での計算

Gaussian 状態 $\rho^{(0)}$ で $K = \sum_{ij} M_{ij} c_i^\dagger c_j$ (Peschel)。

**期待値**: $\langle K\rangle = \mathrm{Tr}(MC)$、$C$ は相関行列。

**分散** (Wick の定理から):
$$\mathrm{Var}(K) = \sum_{ijkl} M_{ij} M_{kl} C_{il}(\delta_{jk} - C_{kj}) = \mathrm{Tr}(M^2 C) - \mathrm{Tr}(M C M C^T)$$

これは数値的に計算可能。

## 5. 検証プログラム

1. XX 模型基底状態 $\rho^{(0)}$、区間 $A$
2. $M_A$, $C_A$ から **$\mathrm{Var}(K_A^{\rm vac})$** を解析的に計算
3. 温度 $T$ で摂動 $\rho(T)$ を作り、各 $T$ で $S_{\rm rel}(T)$ を計算
4. $S_{\rm rel}(T)/T^p$ の冪則を抽出 → 主要 $p=2$ 成分の係数が $\frac{1}{2}\mathrm{Var}(K_A)$ に一致することを確認
5. 一致度から「非線形 Einstein 方程式の第 2 次補正項が情報構造から正しく出る」と結論

## 6. Phase 2 との関係

| Phase | 次数 | 関係式 | 物理 |
|---|---|---|---|
| 2 | 1 | $\delta S = \delta\langle K\rangle$ | 線形化 Einstein $\delta G = 8\pi G \delta T$ |
| **17** | **2** | $S_{\rm rel} = \tfrac{1}{2}\mathrm{Var}(K)\lambda^2$ | **非線形 Einstein 2 次補正** |
| 18+ (未) | 3+ | 高次累積量 | 重力子自己相互作用全次 |

## 7. 残された限界

- $n$ 次相対エントロピーの $n\to\infty$ 極限が真の非線形 Einstein 方程式
- 本 Phase は 2 次までを数値検証
- 3 次以上は Faulkner et al. 2017 で部分的にしか示されておらず、完全証明は未解決

それでも「**2 次が成立する**」ことの確認は線形化を超えた最初の有意な進展。
