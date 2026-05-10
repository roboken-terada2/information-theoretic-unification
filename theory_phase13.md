# Phase 13: 宇宙論定数 Λ — de Sitter エントロピーからのホログラフィック解決

## 1. 動機と問題

宇宙論定数 Λ は Einstein 方程式に現れる:
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G_N T_{\mu\nu}$$

観測値 (2024):
- $\Lambda_{\rm obs} \approx 1.1 \times 10^{-52}\, \mathrm{m}^{-2}$
- 自然単位 (Planck): $\Lambda_{\rm obs} / M_{\rm Pl}^2 \approx 10^{-122}$
- $\rho_\Lambda \sim M_{\rm Pl}^2 \Lambda \sim 10^{-122} M_{\rm Pl}^4$

QFT の素朴な予言:
- 真空ゆらぎ: $\rho_{\rm naive} \sim \Lambda_{\rm UV}^4 \sim M_{\rm Pl}^4$
- これは観測値より $10^{122}$ 倍大きい — **120 桁の階層問題** (現代物理学最大の謎)

## 2. de Sitter エントロピー (Gibbons-Hawking 1977)

de Sitter 時空 (一様正曲率、$\Lambda > 0$) には宇宙論的地平線があり、その面積で決まるエントロピー:
$$S_{\rm dS} = \frac{A_{\rm horizon}}{4 G_N} = \frac{\pi}{G_N H^2}$$

ここで $H$ は Hubble parameter。$\Lambda = 3 H^2$ より:
$$\boxed{\;\;S_{\rm dS} = \frac{3\pi}{G_N \Lambda}\;\;}$$

これは **Λ ↔ エントロピー** の直接対応。$\Lambda$ が小さければ $S_{\rm dS}$ が大きく、宇宙の量子情報容量が大きい。

de Sitter 温度 (Gibbons-Hawking):
$$T_{\rm dS} = \frac{H}{2\pi} = \sqrt{\frac{\Lambda}{12\pi^2}}$$

## 3. ホログラフィック束縛 (Cohen-Kaplan-Nelson 1999)

CKN の提案：QFT の真空エネルギーは**ブラックホールにならない最大値**で束縛される。
- 体積 $L^3$ 内の UV モードのエネルギーが $\sim L^3 \Lambda_{\rm UV}^4$
- これがブラックホールにならない条件: $\rho L^3 \leq M_{\rm BH} \sim L M_{\rm Pl}^2$
- $\Rightarrow$ $\rho_\Lambda \leq M_{\rm Pl}^2 / L^2 = M_{\rm Pl}^2 H^2$

つまり:
$$\rho_\Lambda^{\rm holo} \sim M_{\rm Pl}^2 H^2$$

これは観測値と **完全一致**:
- 観測 $\rho_\Lambda \sim 10^{-122} M_{\rm Pl}^4$
- ホログラフィック $\rho_\Lambda \sim M_{\rm Pl}^2 \cdot (10^{-60} M_{\rm Pl})^2 = 10^{-120} M_{\rm Pl}^4$ ✓

「**Λ が小さい理由 = 宇宙地平線が大きい (= 量子情報容量が大きい)**」

## 4. Verlinde のエマージェント宇宙論 (2017)

Verlinde は更に進めて、**ダークエネルギー = エントロピー的応答** と提案:
- 通常の物質 (バリオン + ダークマター = 全質量 $M$) はエントロピー減少を起こす
- Casimir 風の真空エンタングルメントエントロピー欠損 $\Delta S \propto M$
- これが MOND-like 加速 $a \propto \sqrt{a_0 g_N}$ を生む可能性

これは Phase 2 (情報幾何 = 重力) の動的延長として位置づけられる。

## 5. 情報理論的統一理論内の位置づけ

Phase 1-8 で時空・幾何が量子情報構造から創発することを示した。
Phase 9 で粒子地平線 $L_H = v_F t$ が現れた。
Phase 13 ではこれらを組み合わせ、**宇宙論定数 Λ がエントロピー / 地平線サイズから決まる**ことを示す。

中心命題:

> **宇宙論定数の値は、量子情報の有限性 (= 観測可能宇宙の有限な Hilbert 空間次元) から決まる**

この見方では:
- $\Lambda \sim M_{\rm Pl}^2 / R^2$ where $R$ は宇宙地平線
- $R$ が大きい (我々の宇宙年齢) → $\Lambda$ が小さい
- 階層問題は「宇宙が古い」ことの帰結

## 6. シミュレーション計画

### Part A: 熱エントロピー = 地平線エントロピー (1D CFT 類推)

XX 鎖を温度 $T$ で熱平衡化:
- 熱エントロピー密度 $s(T) = S/L$ を計算
- CFT 予言 (Cardy 1986): $s(T) = \pi c T / (3 v)$ for c=1, v=2 → $s = \pi T/6$
- これは "$T \leftrightarrow H/(2\pi)$" 経由で de Sitter エントロピー類推

### Part B: Casimir 真空エネルギー = 宇宙論定数

XX 鎖の基底状態エネルギー (Casimir 部分):
$$E_0(L) - E_0(\infty) \cdot L = -\frac{\pi c v_F}{6 L} = -\frac{\pi}{3L}$$

"真空エネルギー密度": $\epsilon_{\rm vac}(L) = -\pi/(3 L^2)$

これは $1/L^2$ スケーリング、4D 宇宙論で $\Lambda \sim H^2 \sim 1/R^2$ の類推。

### Part C: 階層比

- 素朴 UV カットオフ: $\epsilon_{\rm UV} \sim 1$ (格子間隔 = 1)
- ホログラフィック: $\epsilon_{\rm holo}(L) \sim 1/L^2$
- 階層: $\epsilon_{\rm UV} / \epsilon_{\rm holo} \sim L^2$

For $L = 256$: 階層 $\sim 6.5 \times 10^4$ (1D)
For 4D 宇宙 ($R \sim 10^{60} M_{\rm Pl}^{-1}$): 階層 $\sim 10^{120}$ (観測と一致)

### Part D: $\Lambda$-S 関係の数値検証

- $\Lambda(L) \equiv \epsilon_{\rm vac}(L) / (M_{\rm Pl}^2 / 8\pi G_N) \approx \epsilon_{\rm vac}(L)$ (units)
- $S_{\rm horizon}(L) \approx (c/3) \log L$ (1D CFT 類推)
- 関係: $\Lambda \cdot e^{3 S/c}$ は $L$ に依存しない (= holographic invariant)

これを数値で確認。

## 7. この Phase が示すこと

✅ 示せる:
- 1D CFT の熱エントロピーが de Sitter エントロピーと同形 (Cardy → Gibbons-Hawking)
- Casimir 真空エネルギー $\sim 1/L^2$ がホログラフィック束縛と整合
- 「素朴 UV」と「ホログラフィック」の階層が次元的に発生

⚠️ 示せない:
- 観測 $\Lambda$ の**正確な値** (= なぜ宇宙はこの大きさか)
- なぜ我々の宇宙が de Sitter (正の $\Lambda$) であって AdS (負) でないか
- ダークエネルギーの動的進化 (時間依存 $w(t)$)

これらは別の物理 (人類原理、初期条件、インフレーション等) を必要とする。
