# Phase 18: ダークマター — 創発重力による銀河回転曲線の再現

## 1. 動機 — ダークマター問題

観測的事実:
- 銀河の**回転曲線が平坦**: $V(r) \to $ const for large $r$ (Rubin 1970s)
- ニュートン重力なら $V \sim 1/\sqrt{r}$ (太陽系で確認済) で減衰するはず
- 銀河団・宇宙背景輻射からも質量不足 ($\Omega_{\rm m} \approx 0.27$ vs バリオン $\Omega_b \approx 0.05$)

主流解釈: 約 **5 倍の見えない物質 (Cold Dark Matter)** が存在
- 未検出の粒子 (WIMPs, axions 等) を想定
- LHC・XENON・LUX 等で 30 年以上探したが**何も見つからない**

別の可能性: **重力法則そのものの低加速度極限における修正** (MOND, Milgrom 1983)
- $a < a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$ で重力が変化
- 銀河スケールで平坦回転曲線・Tully-Fisher 関係を**自然に**説明
- 粒子不要

## 2. Verlinde 2017 — 創発重力からの MOND

Verlinde の主張: **de Sitter 真空のエンタングルメントエントロピー**がダーク重力を生む。

### 2.1 鍵となる公式

de Sitter cosmological 地平面 (Phase 13) のエントロピー:
$$S_{\rm dS} = \frac{\pi}{G_N H^2}$$

バリオン物質質量 $M_B$ が**この真空エントロピーを変位**:
$$\Delta S \propto M_B \times (\text{cosmological scale})$$

このエントロピー変位が**追加の重力**を生む (Verlinde 2010 の entropic gravity を発展):
$$a_D = \sqrt{\frac{a_B \cdot a_0}{6}}$$
ここで $a_B = G M_B / r^2$ はニュートン的バリオン重力。

### 2.2 加速度スケール $a_0$ の予言

Verlinde の解析から:
$$\boxed{\;\;a_0 = \frac{c H_0}{2\pi} \approx 1.14 \times 10^{-10}\,\mathrm{m/s^2}\;\;}$$

これは **Milgrom が銀河観測から経験的に決めた** $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$ と**観測精度内で一致**!
- $a_0$ は**宇宙論的 Hubble 定数から計算可能**な物理量
- 自由フィッティングパラメータではない
- → 「銀河スケールの謎が宇宙論的スケールに繋がる」深い帰結

## 3. MOND 補間関数

ニュートン加速度 $a_N$ と実加速度 $a$ の関係:
$$\mu(a/a_0) \cdot a = a_N$$

簡単な補間関数 $\mu(x) = x/(1+x)$ では:
$$a = \frac{a_N + \sqrt{a_N^2 + 4 a_0 a_N}}{2}$$

極限:
- $a_N \gg a_0$ (太陽系): $a \to a_N$ — 通常のニュートン重力
- $a_N \ll a_0$ (銀河外縁): $a \to \sqrt{a_N a_0}$ — 深い MOND 領域

回転曲線 $V^2(r) = r \cdot a(r)$:
- 深い MOND 領域で $V^2 = r \sqrt{G M a_0/r^2} = \sqrt{G M a_0}$
- → **$V$ が $r$ に依存しない平坦回転曲線**
- → **Tully-Fisher 関係**: $V_\infty^4 = G M a_0$

## 4. 情報理論的統一理論内の位置づけ

Phase 13 で示した:
- 観測可能宇宙の Hilbert 空間次元 $\dim \mathcal{H} \sim \exp(S_{\rm dS})$
- $\Lambda \sim 1/R^2$ (ホログラフィック束縛)

Verlinde の主張は Phase 13 の自然な延長:
- バリオン物質は **Hilbert 空間の "情報構造を変形"**
- この変形が追加重力 (= ダークマター効果) として現れる
- $a_0 = c H/(2\pi)$ は de Sitter エントロピー密度から決まる

ITU の枠組みでは、ダークマター粒子は**仮想物質ではなく情報変位の効果**。

## 5. 限界

⚠️ MOND/Verlinde が**苦戦する**領域:
- **銀河団** の動力学 (Bullet Cluster 等): 重力レンズと x 線分布のずれは MOND だけでは説明困難
- **CMB 音響ピーク** の精密構造: ΛCDM が remarkable な精度で一致
- **構造形成** の N 体シミュレーション: ダークマター粒子なしで成立するか不明

現代の状況: 「銀河スケールでは MOND/Verlinde が驚くほどよく機能、宇宙論スケールでは CDM 必要」 — 統一理論はまだない。

## 6. シミュレーション計画

### Part A: 加速度スケール $a_0$ の予言
- 観測 Hubble $H_0 = 70$ km/s/Mpc から $a_0^{\rm pred} = c H_0/(2\pi)$ を計算
- MOND 観測値 $1.2 \times 10^{-10}$ m/s² との比較

### Part B: 銀河回転曲線
代表的銀河 (天の川、Andromeda、NGC 3198、矮小銀河) について:
- バリオン質量分布 (指数円盤): $\Sigma(R) = \Sigma_0 \exp(-R/R_d)$
- $V_{\rm Newton}(r)$ (普通の Newton 重力)
- $V_{\rm MOND}(r)$ (補間関数経由)
- 観測値 $V_{\rm obs}$ との比較

### Part C: Tully-Fisher 関係
- 質量 $M = 10^7 - 10^{12} M_\odot$ で多数のサンプル
- $V_\infty(M)$ を計算
- log-log plot で $V_\infty \propto M^{1/4}$ を確認 (Tully-Fisher)

### Part D: 加速度関係 (RAR)
McGaugh et al. 2016 が示した**普遍関係**:
$$g_{\rm obs} = g_{\rm bar} + \sqrt{g_{\rm bar} a_0}$$
(または MOND 補間で表現される単一曲線)
SPARC データベース 170 銀河でこの関係が成立する。
我々の計算もこの関係を再現するはず。

## 7. この Phase が示すこと

✅ 示せる:
- $a_0 \sim cH/(2\pi)$ が観測値と一致 (= 自由パラメータでない)
- 銀河回転曲線が**ダークマター粒子なし**で平坦化
- Tully-Fisher 関係 ($V^4 \propto M$) の再現
- 加速度関係 (RAR) の自然な発生

⚠️ 示せない:
- 銀河団・CMB の精密フィット
- 宇宙論大規模構造の N 体シミュレーション結果
- Verlinde のフルな導出 (de Sitter モジュラーフロー → 重力場方程式)

それでも「**ダークマター粒子なしで銀河回転曲線が平坦化する**」事実が、情報理論的統一理論の枠内で示せる意義は大きい。
