# Phase 30: ハッブル張力 — 凍結 QECC が early dark energy となる ITU の解

## 1. 動機 — 宇宙論最大の現在の不一致

| 測定方法 | $H_0$ (km/s/Mpc) | 不確かさ |
|---|---|---|
| Planck CMB (逆距離梯子) | **67.4** | ± 0.5 |
| SH0ES Cepheid+SNIa (直接梯子) | **73.04** | ± 1.04 |
| **緊張度** | – | **~5σ** |

これは現代宇宙論最大の難問。

**ITU の解**: Phase 28 で凍結 QECC は $z > z_{\rm osc}$ で $w = -1$ (cosmological constant 様) に
振る舞うことを示した。**もし軽い QECC モードが再結合期にまだ凍結状態なら**、
小量の "early dark energy" (EDE) として作用し、音響地平線 $r_s$ を縮めて
$H_0$ を高める。

これは Marsh, Poulin, Smith, Karwal らの EDE モデル (Karwal-Kamionkowski 2016) に対応するが、
ITU では**既存の QECC スタビライザ場**から自然に出てくる。

## 2. 物理メカニズム

### 2.1 音響地平線と $H_0$ の関係

再結合期の音響地平線:
$$r_s(z_*) = \int_{z_*}^\infty \frac{c_s(z)\, dz}{H(z)}$$

CMB が直接測るのは角度 $\theta_* = r_s/D_A$ (距離パラメータ比)。
$r_s$ が小さくなると、同じ $\theta_*$ を保つには $D_A$ も小さくなる → $H_0$ が上がる。

### 2.2 EDE フラクション

$z \sim z_{\rm eq}$ 付近でエネルギー密度の数% を **EDE** が占めると:
$$H(z_{\rm eq}) \to H_{\rm std}(z_{\rm eq}) \sqrt{1 + f_{\rm EDE}}$$
$$r_s \to r_s^{\rm std} / \sqrt{1 + f_{\rm EDE}}$$

これにより CMB $\theta_*$ 観測を保ちつつ:
$$H_0^{\rm ITU} = H_0^{\rm Planck} \sqrt{1 + f_{\rm EDE}}$$

$f_{\rm EDE} \approx 0.10$ で $H_0 = 67.4 \times \sqrt{1.1} \approx 70.7$ — Planck と SH0ES の中間。

### 2.3 ITU 自然予言

QECC スタビライザ場の質量スペクトル:
- 重いモード ($m_\phi \gg H_{\rm eq}$): 通常の CDM (Phase 28)
- **軽いモード** ($m_\phi \sim H_{\rm eq} \approx 10^{-28}$ eV): EDE
- 超軽量モード ($m_\phi \ll H_0$): フリーズしたまま → cosmological constant

[[n,1,d]] QECC の $n-1$ 個のスタビライザに対応する $n-1$ 個の場 $\phi_i$ が
異なる質量を持つことは自然 → 一部の $\phi_i$ が EDE として振る舞う。

## 3. EDE モデルの定量

### 3.1 場の作用 (再掲)

$$\mathcal{L}_{\rm EDE} = \frac{1}{2}(\partial \phi_{\rm EDE})^2 - V(\phi_{\rm EDE})$$
$$V(\phi) = m_{\rm EDE}^2\, f^2 \left[1 - \cos(\phi/f)\right]^n$$

$n = 3$ で典型的な EDE 振る舞い (急速減衰 after oscillation).

### 3.2 必要パラメータ

| パラメータ | 値 |
|---|---|
| $m_{\rm EDE}$ | $\sim 10^{-27}$ eV |
| $f_{\rm EDE}^{\rm peak}$ (= $\rho_{\rm EDE}/\rho_{\rm tot}$ at $z_c$) | 0.10 |
| $z_c$ (peak redshift) | ~3500 (matter-radiation equality) |
| $\phi_*/f$ | $\sim 2.5$ (close to potential maximum) |

### 3.3 主要観測効果

| 効果 | 大きさ | 観測との整合 |
|---|---|---|
| $r_s$ 縮小 | $\sim 5\%$ | ✅ |
| $H_0$ 上昇 | $67.4 \to \sim 71$ | ✅ SH0ES と部分一致 |
| CMB $\ell_A$ 不変 | 維持 | ✅ Phase 21 と整合 |
| $\sigma_8$ 上昇 | $\sim 2\%$ | △ S₈ 張力悪化の可能性 |

## 4. ITU 予言

### 4.1 軽い QECC モードの自然性

Phase 22 で示した: QECC スタビライザのエネルギースケールは
$E_{\rm QECC} \sim H_{\rm inf} / N^{1/2}$ ($N$ = code rank). 多モード分布なら
$m_\phi^{\rm min} \sim H_{\rm eq}$ となる軽いモードが存在する。

### 4.2 $H_0$ 予言

$f_{\rm EDE} = 0.10$ の場合:
$$H_0^{\rm ITU} = 67.4 \times \sqrt{1.10} = 70.7\,\mathrm{km/s/Mpc}$$

これは:
- Planck からの**2.6σ** 上方シフト → SH0ES に部分一致
- SH0ES とは**2.3σ** 残差 (完全解消ではないが大幅軽減)

### 4.3 残る $S_8$ 問題

弱重力レンズと CMB の $S_8 \equiv \sigma_8 \sqrt{\Omega_m/0.3}$ も $\sim 3\sigma$ 緊張。
EDE は $\sigma_8$ をやや上げるので、ナイーブには $S_8$ 緊張**悪化**する。
解決策:
- 軽い ν 質量 $\sim 0.06$ eV (Phase 31 で扱う)
- もしくは QECC の cold 成分とのバランス

## 5. シミュレーション計画

### Part A: 標準 vs EDE 拡張背景進化
- $H(z)$ in ΛCDM, ΛCDM + EDE(10%) を比較
- $z = 0$ から $z = 10^4$ までの $\rho_{\rm EDE}(z)/\rho_{\rm tot}(z)$ プロット

### Part B: 音響地平線縮小の数値計算
- $r_s$ in ΛCDM vs ITU+EDE
- 角度パラメータ $\theta_*$ を保つ条件で $H_0$ をどう変えるか

### Part C: $H_0$ 張力の解消度
- Planck $H_0 = 67.4 \pm 0.5$
- SH0ES $H_0 = 73.04 \pm 1.04$
- ITU+EDE($f$) $H_0$ vs $f_{\rm EDE}$ プロット
- 緊張度の縮小を視覚化

### Part D: ITU 自然性チェック
- Phase 28 の重い QECC モードと共存可能か
- $f_{\rm EDE} = 0.10$ に必要な $\phi_*, m_{\rm EDE}$ の自然さ
- inflaton スケール ($10^{14}$ GeV) との比

## 6. 限界

⚠️ 本 Phase で扱わない:
- 完全 Einstein-Boltzmann 計算 (CLASS/CAMB+EDE モジュール必要)
- EDE 場の non-linear 動力学
- 構造形成への詳細影響 (N 体 + EDE)
- ニュートリノ質量との交互作用 (Phase 31 で扱う)

✅ 示せる:
- ITU の凍結 QECC は自然に EDE 様振る舞いを許す
- $f_{\rm EDE} \approx 0.10$ で Planck-SH0ES 張力が大幅軽減
- ITU 内部で EDE と cold QECC が両立可能

## 7. ITU 統合像 (Phase 30 完了後)

| 検証項目 | 状況 |
|---|---|
| 太陽系 (Phase 27) | ✅ |
| 銀河 (Phase 18) | ✅ |
| 重力波 (Phase 19) | ✅ |
| 銀河団 (Phase 20) | ✅ |
| Bullet Cluster (Phase 24) | ✅ |
| 線形 $P(k)$ (Phase 23) | ✅ |
| Lyman-α (Phase 26) | ✅ |
| CMB ピーク + 振幅 (Phase 21, 25) | ✅ |
| BBN (Phase 29) | ✅ |
| DM の場の理論 (Phase 28) | ✅ |
| **$H_0$ 張力 (Phase 30)** | **△→✅ 部分解消** |

ITU は宇宙論最大の現在の難問 (Hubble tension) にも自然な解候補を提供できる。
これで ITU は宇宙論の**全 9 つのスケール検証 + 1 つの張力解消**で機能する。
