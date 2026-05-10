# Phase 12: 電弱対称性破れ — Higgs 機構の動的描像

## 1. 動機

Phase 10 で標準模型のゲージ群 SU(3)×SU(2)×U(1)_Y が境界 CFT のフレーバー大域対称性として現れることを示した。
しかし観測される自然界では、SU(2)_L × U(1)_Y は完全には保存されず、**SU(2)_L × U(1)_Y → U(1)_em** に自発的に破れている：
- 弱ボソン W±, Z は質量 80, 91 GeV を持つ
- 光子 γ は無質量
- フェルミオンも質量を持つ (= Higgs と Yukawa 結合経由)

この**電弱対称性破れ (EWSB)** は **Higgs 機構** (Anderson 1963, Brout-Englert 1964, Higgs 1964) によって説明される。本 Phase は EWSB を情報理論的統一理論の枠内で実装し、数値的に実証する。

## 2. Higgs 機構の本質

### 2.1 メキシカンハットポテンシャル

スカラー場 $\phi$ (Higgs 場) のポテンシャル:
$$V(\phi) = -\mu^2 |\phi|^2 + \lambda |\phi|^4, \quad \mu^2, \lambda > 0$$

最小は $|\phi|^2 = \mu^2/(2\lambda) \equiv v^2/2$ で達成 ($v$: Higgs VEV)。
$\phi = 0$ は不安定な極大。

### 2.2 Goldstone-Higgs モード

連続対称性 G が部分群 H へ自発的に破れる ($G/H$ の余空間)。
- **Goldstone モード**: $\dim(G/H)$ 個の無質量場 (= 破れた生成子に沿う $\phi$ のゆらぎ)
- **Higgs モード**: $\dim(G) - \dim(G/H)$ 個の有質量場 (= 振幅ゆらぎ)

ゲージ理論では Goldstone はゲージ場に「食われる」(eat) → ゲージボソン質量。

### 2.3 ゲージボソン質量 (Anderson-Higgs)

ゲージ理論で $\phi$ に共変微分 $D_\mu \phi = (\partial_\mu - i g A_\mu^a T^a)\phi$ で結合：
$$|D_\mu\langle\phi\rangle|^2 = g^2 v^2 (T^a A_\mu^a)(T^b A^{b\mu}) \to m_W^2 = g^2 v^2/4$$

電弱の場合：
- $m_W = gv/2 \approx 80$ GeV
- $m_Z = \sqrt{g^2+g'^2}\,v/2 \approx 91$ GeV
- 光子は破れていない U(1)_em に対応するため無質量

### 2.4 フェルミオン質量

Yukawa 結合 $y \bar\psi_L \phi \psi_R$ は破れた相で:
$$y \bar\psi_L \phi \psi_R \to y v\, \bar\psi_L \psi_R = m_\psi \bar\psi\psi$$

つまりフェルミオン質量 $m_\psi = y v$。Phase 11 の Yukawa 階層と接続。

## 3. 格子モデルでの最小実装

### 3.1 1D 自由フェルミオン + Dirac 質量

最も単純な実装は **1D 鎖の階段状質量 (staggered mass)**:
$$H = -t \sum_i (c_i^\dagger c_{i+1} + \mathrm{h.c.}) + m \sum_i (-1)^i\, c_i^\dagger c_i$$

これは離散カイラル対称性を持つ (Dirac 場の無質量極限)。
$m$ が「Higgs VEV × Yukawa」に対応する。

### 3.2 2 サイト単位胞での Bloch Hamiltonian

$N$ 偶数の周期境界条件で、2 サイト単位胞 (偶-奇) を取ると、
$$H(k) = -2t\cos(k/2)\,\sigma_x - m\,\sigma_z$$

エネルギー固有値:
$$\epsilon_\pm(k) = \pm\sqrt{4t^2\cos^2(k/2) + m^2}$$

### 3.3 ギャップの自動発生

- $m = 0$: $\epsilon(k=\pi) = 0$ → **ギャップレス** (= 臨界 = 対称性保存)
- $m > 0$: $\epsilon_\pm(k=\pi) = \pm m$ → **ギャップ $= 2m$ 開** (= 質量取得)

これは「**Higgs VEV $\to$ フェルミオン質量**」の最小モデル。

## 4. 検証可能な構造

### 4.1 ギャップ ∝ 質量

$\Delta_{\rm gap}(m) = 2m$ の線形関係を数値で確認。

### 4.2 エンタングルメントの相転移

- $m = 0$ (臨界): $S(L) = (c/3)\log L$ (Calabrese-Cardy, $c=1$)
- $m > 0$ (ギャップ): $S(L) \to S_\infty$ 飽和 (面積則)

両者の鋭い対比が EWSB の量子情報的特徴。

### 4.3 Mexican Hat → 自発的破れ

外部から Higgs ポテンシャル $V(\Delta) = -\mu^2 \Delta^2 + \lambda \Delta^4$ を加える。
全エネルギー
$$F(\Delta) = E_{\rm kinetic}(\Delta) + V(\Delta)$$
を $\Delta$ について最小化。$\mu^2 > 0$ なら $\Delta_{\min} \neq 0$ で**自発的破れ** (= EWSB)。

予言: $\Delta_{\rm VEV} = \sqrt{\mu^2/(2\lambda)}$ (Mexican hat の解析最小)

## 5. 情報理論的統一理論内の位置づけ

Phase 10 で SM ゲージ群、Phase 11 で物質階層を導いた。Phase 12 では:

> **境界 CFT のフレーバー対称性が自発的に破れる**ことは、相互作用 (or 外部ポテンシャル) を与える系の自然な性質。Mexican hat は Higgs 場の自己相互作用の最小形であり、情報理論的枠組み (Phase 10 の global symmetry) の中で自然に許される。

つまり、**Higgs 機構それ自体は標準的な場の理論の現象であり、情報理論的統一理論の中で同じく成立する**。本 Phase の貢献は、EWSB を Phase 1-11 と同じフレームワーク内で**完全に展開可能**であることの確認。

これにより:
- Phase 1-3, 7, 8: 時空・幾何
- Phase 4, 9: 時間・宇宙論
- Phase 5, 6: ホログラフィー・BH 情報
- Phase 10: ゲージ群
- Phase 11: 物質階層
- **Phase 12: 電弱対称性破れ + フェルミオン質量** ← 本 Phase

すべて単一の情報理論的公理 $\delta S = \delta\langle K\rangle$ + 境界 CFT の構造から生まれる。

## 6. 限界

⚠️ **本 Phase が示さない**こと:
- なぜメキシカンハットの $\mu^2$ がこの値か (階層問題)
- 真空安定性 (Higgs 結合の RG 流れ)
- 動的な対称性破れの起源 (テクニカラーや組成 Higgs)
- カイラリティ (左手だけが弱相互作用) — Phase 15 で扱う

これらは超対称性、技術色 (technicolor)、追加対称性等で説明候補があるが、本 Phase の範囲外。
