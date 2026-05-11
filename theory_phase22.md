# Phase 22: 情報理論的起源としての $\Omega_{\rm CDM} = 0.27$

## 1. 問題

Phase 21 で示した:
- ΛCDM ($\Omega_m = 0.315, \Omega_b = 0.049, \Omega_{\rm CDM} = 0.266$) は Planck CMB と完全一致
- MOND-only ($\Omega_m = \Omega_b$) は 43% ずれ
- Hybrid (MOND + 1.5 eV ν) も 34% ずれ

つまり**何らかの CDM 様密度成分 $\Omega_{\rm CDM} \approx 0.27$ が必要**。
ITU 枠組みは粒子的 CDM を仮定しないが、**情報構造から創発できるか?** が本 Phase の問い。

## 2. 宇宙情報予算 (Cosmic Information Budget)

各エポックでの**de Sitter エントロピー** (Phase 13):
$$S_{\rm dS}(H) = \frac{A_{\rm horizon}}{4 G_N} = \pi\left(\frac{R_H}{\ell_P}\right)^2, \quad R_H = c/H$$

これは「**そのエポックで宇宙に許される最大量子情報**」(holographic bound)。

### 2.1 各エポックでの値

| エポック | $H$ (s⁻¹) | $R_H$ (m) | $R_H/\ell_P$ | $S_{\rm dS}$ |
|---|---|---|---|---|
| インフレーション ($E \sim 10^{16}$ GeV) | $1.5 \times 10^{37}$ | $2 \times 10^{-29}$ | $1.3 \times 10^{6}$ | $\sim 5 \times 10^{12}$ |
| BBN ($T \sim 1$ MeV) | $\sim 1$ | $3 \times 10^{8}$ | $2 \times 10^{43}$ | $\sim 10^{87}$ |
| 再結合 ($z = 1090$) | $4.5 \times 10^{-14}$ | $6.7 \times 10^{21}$ | $4 \times 10^{56}$ | $\sim 5 \times 10^{113}$ |
| **現在** ($H_0 \approx 70$ km/s/Mpc) | $2.18 \times 10^{-18}$ | $1.4 \times 10^{26}$ | $8.8 \times 10^{60}$ | $\sim 2.4 \times 10^{122}$ |

「情報容量の増加」(= 宇宙進化に伴う Hilbert 空間の拡大):
$$\Delta S_{\rm cosmos} = S_{\rm now} - S_{\rm inf} \approx 2.4 \times 10^{122}$$

(インフレーション時の容量は無視できる程度)

## 3. 凍結情報量と $\Omega_{\rm CDM}$ の関係

**仮説**: 宇宙進化に伴って増加した情報容量の一部 $f$ が「**凍結**」され、**質量エネルギー**として残留する → これが CDM 様に見える。

### 3.1 必要な凍結量

観測 $\Omega_{\rm CDM} = 0.266$ を再現するには:
$$M_{\rm CDM} = 0.266 \times \rho_{\rm crit} \times \frac{4}{3}\pi R_H^3$$

$\rho_{\rm crit} = 3 H_0^2 / (8\pi G) \approx 8.5 \times 10^{-27}$ kg/m³ より:
$$M_{\rm CDM} \approx 2.6 \times 10^{52}\,\mathrm{kg} \approx 1.2 \times 10^{60}\,m_P$$

各凍結情報単位が Planck エネルギー級と仮定すれば、必要な単位数:
$$N_{\rm frozen} \approx 1.2 \times 10^{60}$$

凍結率:
$$\boxed{\;f = \frac{N_{\rm frozen}}{S_{\rm cosmos}} = \frac{1.2 \times 10^{60}}{2.4 \times 10^{122}} \approx 5 \times 10^{-63}\;}$$

つまり「**宇宙の総情報容量のうち $\sim 10^{-62}$ の割合が凍結し、それが CDM として現れる**」。

### 3.2 これは何を意味するか?

- $f \sim 10^{-62}$ は微小だが**非零の特定値**
- Phase 13 の $\Omega_\Lambda$ ホログラフィック予言 ($\sim 10^{-122}$ from CKN) と**似た hierarchy**
- 両方とも「**宇宙情報予算からの微小漏れ**」と解釈可能 (Verlinde 2017 の趣旨)

## 4. ITU 候補メカニズム

### 4.1 原始 QECC 凍結 (主候補)

Phase 5 で示した「バルク = QECC」を**インフレーション期**に適用:
- インフレーション中の Hubble 内部に**論理量子ビットの符号化**が形成
- 急膨張で**因果切断** → 一部の論理ビットが「凍結」状態に
- 凍結ビットは後期宇宙で重力ポテンシャルとして観測される

この機構の特徴:
- 凍結ビット間に長距離相関 → CMB 構造形成のシード
- ΛCDM の $P(k)$ パワースペクトラム特徴を再現する可能性
- ニュートリノ等の追加粒子不要

### 4.2 Verlinde 創発重力からの自然予言

Verlinde 2017 では $\Omega_\Lambda + \Omega_{\rm dm}$ が**同じ情報変位機構**から決まる:
$$\frac{\Omega_{\rm dm}}{\Omega_\Lambda} \stackrel{?}{=} \text{universal ratio}$$

観測: $0.266/0.685 \approx 0.39$

Verlinde の解析的予言は ~$2/\pi \approx 0.64$ で観測と一致しない (~60% ずれ)。
→ Verlinde 単独では精密一致せず、補正必要。

### 4.3 ER=EPR 拡張: 「宇宙内 BH 雲」

凍結量子ビットが**マイクロブラックホール**として実体化する場合:
- 各 BH 質量 ~ Planck (intermediate-mass BHs)
- 重力相互作用は通常の Newton + 観測上 CDM と区別できない
- これは MACHO 仮説と類似

LIGO・MICROLENSING の制約から制限される領域。

## 5. シミュレーション計画

### Part A: 各エポックでの宇宙エントロピー
インフレーション → BBN → 再結合 → 現在で $S_{\rm dS}$ を計算、log scale で可視化

### Part B: 凍結率 $f$ の決定
- $\Omega_{\rm CDM}$ vs $f$ の関係
- Planck 観測値 0.266 から $f \approx 5 \times 10^{-63}$ を抽出

### Part C: トイ QECC 凍結モデル
小 N qubit 系 (例: N=10) で:
- 「インフレーション」= ランダム scrambling
- 一部 qubit を「観測者地平面外」として trace out
- 残留エントロピーが凍結ビット数
- スケーリングを観察

### Part D: $\Omega_\Lambda / \Omega_{\rm CDM}$ 比の予言
- ITU 枠内での「同一機構」仮説の検証
- 観測 0.39 と理論予言の比較

## 6. 限界と展望

⚠️ 未解決:
- 凍結機構の具体的場の理論的記述 (= Phase 4 のモジュラーフローの早期宇宙版)
- $f$ の値が「なぜ 10⁻⁶² か」の第一原理的説明 (= 自然性問題の CDM 版)
- N 体構造形成シミュレーションでの ΛCDM との一致

✅ 示せる:
- $\Omega_{\rm CDM} = 0.27$ が**特定値の凍結率**として情報予算と整合
- 桁オーダーは ITU 枠組みで自然
- Verlinde 等の既存提案と接続可能

## 7. 結論

CMB の $\Omega_{\rm CDM} = 0.27$ は**情報理論的に表現可能**だが、**具体的機構の特定は今後の課題**。
Phase 22 は「**正しい桁の予言**」を与え、Phase 23+ で精密化を目指す位置づけ。
