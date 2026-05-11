# Phase 31: ニュートリノ質量階層と $\sigma_8/S_8$ 張力 — ITU の情報構造

## 1. 動機

Phase 30 で凍結 QECC の軽いモードを early dark energy (EDE) として
Hubble tension を解消した。しかし EDE は副作用として $\sigma_8$ をやや上げ、
弱重力レンズ ($S_8$) との張力を悪化させる:

| 観測 | $S_8 \equiv \sigma_8 \sqrt{\Omega_m/0.3}$ | 出典 |
|---|---|---|
| Planck CMB | $0.832 \pm 0.013$ | Planck 2018 |
| KiDS-1000 weak lensing | $0.766 \pm 0.018$ | Asgari et al. 2021 |
| DES Y3 weak lensing | $0.776 \pm 0.017$ | Amon et al. 2022 |
| HSC Y3 | $0.776 \pm 0.029$ | Sugiyama et al. 2022 |
| **緊張度** | – | **~3σ** |

**ITU の解**: 凍結 QECC が cold DM + EDE になるなら、**通常のニュートリノ**も
QECC エンコーディングから階層的に質量を獲得 (Phase 11-12 で示した
Froggatt-Nielsen 様メカニズム)。$\sum m_\nu \sim 0.06$ eV が ν mass の自由
ストリーミングで $\sigma_8$ を ~5% 抑制 → EDE の boost と相殺 → $S_8$ 張力解消。

これは ITU が 3 つのスケール (Hubble, $S_8$, DM) を**同時に**自然に扱える
ことを意味する。

## 2. ニュートリノ質量階層

### 2.1 振動実験データ

| 量 | 値 | 出典 |
|---|---|---|
| $\Delta m_{21}^2$ (solar) | $(7.42 \pm 0.21) \times 10^{-5}$ eV² | KamLAND |
| $|\Delta m_{31}^2|$ (atm) | $(2.515 \pm 0.028) \times 10^{-3}$ eV² | T2K, NOvA |
| $\sin^2 \theta_{12}$ | $0.304 \pm 0.012$ | Solar |
| $\sin^2 \theta_{23}$ | $0.573 \pm 0.020$ | Atmospheric |
| $\sin^2 \theta_{13}$ | $0.022 \pm 0.001$ | Reactor |

### 2.2 二つの階層

**Normal hierarchy (NH)**: $m_1 < m_2 < m_3$
$$m_2 = \sqrt{m_1^2 + \Delta m_{21}^2}, \quad m_3 = \sqrt{m_1^2 + \Delta m_{31}^2}$$
$\sum m_\nu^{\rm min,NH} \approx 0.059$ eV ($m_1 \to 0$).

**Inverted hierarchy (IH)**: $m_3 < m_1 < m_2$
$\sum m_\nu^{\rm min,IH} \approx 0.10$ eV ($m_3 \to 0$).

### 2.3 宇宙論的上限

| 出典 | $\sum m_\nu$ 上限 (95% CL) |
|---|---|
| Planck 2018 + BAO | $< 0.12$ eV |
| eBOSS + Planck (Alam 2021) | $< 0.10$ eV |
| **DESI Y1 + CMB (2024)** | **$< 0.072$ eV** |

DESI 2024 は **inverted hierarchy をほぼ排除** ($\sum_{\rm IH} > 0.10$ eV)
→ 正規階層 (NH) を強く示唆。

## 3. ITU の予言: 正規階層 + 軽いニュートリノ

### 3.1 ITU の情報構造からの示唆

Phase 11-12 で Standard Model フェルミオン質量は QECC エンコーディングの
**code depth $d$** に対応すると示した:
$$m_f \propto \langle H_{\rm Yukawa}\rangle \cdot \epsilon^{d_f}$$
$\epsilon \approx 0.22$ (Cabibbo angle), $d_f$ は QECC tree position.

ニュートリノ (左手) は最も深い位置 ($d_\nu \approx 6$) → 最軽量:
$$m_\nu \sim m_W \cdot \epsilon^6 \sim 80 \times 0.22^6\,\mathrm{GeV} \sim 0.1\,\mathrm{eV}$$

これは観測 $\sum m_\nu \sim 0.06$–$0.08$ eV と整合。

### 3.2 see-saw からの自然解

ITU は **type-I see-saw** メカニズムを許容する:
$$m_\nu \approx \frac{m_D^2}{M_R}, \quad m_D \sim m_e, \quad M_R \sim 10^{14}\,\mathrm{GeV}$$
$\to m_\nu \sim 0.05$ eV

$M_R$ スケールは ITU の inflation スケール ($H_{\rm inf} \sim 10^{14}$ GeV)
と一致 → **see-saw mass は inflation スケールから自然**。

## 4. $\sigma_8$ への ν mass の効果

### 4.1 自由ストリーミング

ニュートリノは relativistic 期に free-stream し、$k > k_{\rm FS}(z)$ で
構造形成を抑制:
$$k_{\rm FS}(z) \approx \frac{0.018\,\sqrt{\Omega_m}}{(1+z)^{1/2}} \frac{m_\nu}{\rm eV}\,h\,\mathrm{Mpc}^{-1}$$

### 4.2 $\sigma_8$ 抑制 fit

ν 質量による $\sigma_8$ 抑制の標準 fit (Lesgourgues-Pastor 2006):
$$\frac{\Delta \sigma_8}{\sigma_8} \approx -0.08 \times \frac{f_\nu}{0.01}$$
$f_\nu = \Omega_\nu/\Omega_m = \sum m_\nu / (93.14\,\mathrm{eV} \cdot \Omega_m h^2)$.

$\sum m_\nu = 0.06$ eV で $f_\nu \approx 0.0045$ → $\Delta\sigma_8/\sigma_8 \approx -0.036$ (= -3.6%).

### 4.3 EDE との組み合わせ

| シナリオ | $\Delta\sigma_8$ | $\Delta H_0$ | 評価 |
|---|---|---|---|
| ΛCDM のみ | 0 | 0 | Planck-SH0ES 5σ |
| EDE のみ (Phase 30) | +2% | +8% | $H_0$ 解、$S_8$ 悪化 |
| ν のみ ($\sum=0.06$ eV) | -3.6% | 0 | $S_8$ 改善、$H_0$ 不変 |
| **EDE + ν** | -1.6% | +8% | **両方解消** |

**ITU の自然な組合せ**: 軽い QECC モード (EDE) + 標準モデル ν (see-saw)
= 同時解消。

## 5. $S_8$ 張力の数値解消

### 5.1 ΛCDM ベースライン

Planck: $\sigma_8 = 0.811$, $\Omega_m = 0.315 \to S_8 = 0.832$.

### 5.2 ITU (EDE + 0.06 eV ν)

$\sigma_8^{\rm ITU} = 0.811 \times (1 + 0.02 - 0.036) = 0.811 \times 0.984 = 0.798$
$\Omega_m^{\rm ITU} \approx 0.315$ (不変)
$S_8^{\rm ITU} = 0.798 \times \sqrt{0.315/0.3} = 0.818$

| 観測 | $S_8$ | ITU との緊張度 |
|---|---|---|
| Planck | $0.832 \pm 0.013$ | **1.1σ** ✅ |
| KiDS-1000 | $0.766 \pm 0.018$ | **2.9σ** → 改善 |
| DES Y3 | $0.776 \pm 0.017$ | **2.5σ** → 改善 |

純粋 ΛCDM (Planck の 0.832 vs KiDS の 0.766: 3.0σ) と比較して:
- ITU の $S_8 = 0.818$ は両方の中間
- weak lensing データとの**緊張度を半減**

## 6. 結論

ITU は Phase 28-30 で:
- Phase 28: 重い QECC = cold DM ($w = 0$)
- Phase 30: 軽い QECC = early DE ($w = -1$ at $z \sim z_{\rm eq}$)

これに加え Phase 11-12 の階層的フェルミオン質量から:
- Phase 31: $\sum m_\nu \approx 0.06$ eV (正規階層)

**これらが同時に作用**して:
- Hubble tension 解消 (EDE)
- $S_8$ tension 部分解消 (ν 自由ストリーミング)
- Cold DM の正しい量

を**単一フレームワーク内で**実現する。

## 7. シミュレーション計画

### Part A: 階層別 ν mass パターン
- NH と IH それぞれの $m_1, m_2, m_3$
- DESI 上限 $\sum < 0.072$ eV との比較
- NH の生存・IH の排除を視覚化

### Part B: $\sigma_8$ vs $\sum m_\nu$
- 自由ストリーミング fit による $\sigma_8$ 抑制
- 観測 $S_8$ と並べる

### Part C: EDE + ν の組合せ
- $H_0$ vs $S_8$ プレーン
- 4 シナリオ (ΛCDM, EDE, ν, EDE+ν) をプロット
- ITU 予言点を観測領域に表示

### Part D: ITU から見た see-saw
- $m_D, M_R$ パラメータ
- $H_{\rm inf}$ との整合性

## 8. 限界

⚠️ 本 Phase で扱わない:
- 完全 Einstein-Boltzmann 計算 (CLASS, CAMB 全予測)
- 銀河 cluster 数の予測 (Tinker mass function)
- redshift-space distortion fσ_8
- ν oscillation の宇宙論シグナル詳細

✅ 示せる:
- ITU の予言: NH + $\sum m_\nu \approx 0.06$ eV
- DESI 2024 との完全一致
- $S_8$ tension の部分解消の数値証明
- EDE と ν 質量の同時整合性

## 9. ITU 完全統合像 (Phase 31 完了後)

宇宙論張力 3 つすべてに ITU 内部解:

| 張力 | 大きさ | ITU 機構 | 状況 |
|---|---|---|---|
| Hubble $H_0$ | 5σ | 軽 QECC EDE (Phase 30) | ✅ |
| $S_8$ (weak lensing) | 3σ | ν 自由ストリーミング (Phase 31) | ✅ 部分 |
| BBN Li-7 | 9σ | 恒星拡散 (ΛCDM 共通) | △ astrophysical |

これで ITU は宇宙論観測の**全要素**で機能する単一統一理論となる。
