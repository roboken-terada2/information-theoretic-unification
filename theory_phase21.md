# Phase 21: CMB 音響ピークの精密計算 — Phase 20 の最後の弱点を潰す

## 1. 動機

Phase 20 で「ハイブリッド枠組み (MOND + 原始 QECC + ~1.5 eV ν) で銀河団・CMB が解決可能」と提案したが、CMB ピーク位置は**模式図レベル**だった。本 Phase で**解析的に定量計算**し、Planck 2018 観測値との一致度を評価する。

完全 Boltzmann 計算 (CAMB) は重いが、**Hu-Sugiyama 1996** の解析公式で音響ピーク位置はかなり精度よく予言できる。

## 2. 音響ピーク位置の理論

### 2.1 音響ホライゾン (sound horizon at recombination)

$r_s = c \int_0^{t_*} \frac{c_s(t)}{a(t)} dt$ ($c_s$ = 光子-バリオン流体の音速)

Hu-Sugiyama 1996 の解析近似:
$$r_s \approx \frac{44.5\,\mathrm{Mpc} \cdot \ln(9.83/\Omega_m h^2)}{\sqrt{1 + 10(\Omega_b h^2)^{3/4}}}$$

### 2.2 角度直径距離 (last scattering まで)

平坦宇宙では:
$$D_A^{\rm comoving} = \frac{c}{H_0} \int_0^{z_*} \frac{dz}{E(z)}, \quad E(z) = \sqrt{\Omega_m(1+z)^3 + \Omega_\Lambda}$$

### 2.3 音響角度スケールと ピーク位置

$$\theta_A = \frac{r_s}{D_A}, \quad \ell_n \approx (n - \phi_n) \cdot \frac{\pi}{\theta_A}$$

$\phi_n$ は位相シフト (Hu-Sugiyama, 第 1 ピークで $\phi_1 \approx 0.267$)。

## 3. 3 モデルの比較

| パラメータ | ΛCDM (Planck) | MOND-only | Hybrid (+1.5 eV ν) |
|---|---|---|---|
| $\Omega_b$ | 0.049 | 0.049 | 0.049 |
| $\Omega_{\rm CDM}$ | 0.265 | 0 | 0 |
| $\Omega_\nu$ | ~0 | 0 | $\sim 0.017$ |
| $\Omega_m^{\rm total}$ | **0.315** | **0.049** | **0.066** |
| $h$ | 0.674 | 0.674 | 0.674 |

Hybrid の $\Omega_\nu$: ニュートリノ 3 種で $m_\nu = 1.5$ eV →
$\Omega_\nu h^2 \approx m_\nu / (93.14$ eV$) \approx 0.016$ → $\Omega_\nu \approx 0.036$

実際にはニュートリノは relativistic で、密度寄与は CDM より小さい。本計算ではバリオン+ニュートリノを effective Ω_m として扱う近似。

## 4. 予言と検証

| 量 | ΛCDM 予言 | MOND-only 予言 | Hybrid 予言 | Planck 観測 |
|---|---|---|---|---|
| $r_s$ (Mpc) | $\approx 149$ | $\approx 215$ | $\approx 195$ | $\approx 144.4$ |
| $D_A$ (Mpc) | $\approx 13900$ | $\approx 16200$ | $\approx 15800$ | $\approx 13900$ |
| $\theta_A$ | $\approx 0.01072$ | $\approx 0.01327$ | $\approx 0.01234$ | $0.01041$ |
| $\ell_1$ | $\approx 220$ | $\approx 178$ | $\approx 191$ | **220** |
| $\ell_2$ | $\approx 540$ | $\approx 436$ | $\approx 468$ | **537** |
| $\ell_3$ | $\approx 800$ | $\approx 657$ | $\approx 706$ | **810** |

**予想結果**: 
- ΛCDM は Planck と < 5% で一致 (= 標準モデルの強み)
- MOND-only は 1st ピーク位置が ~20% 低い → 明確な不一致
- Hybrid は ~14% 低い → 部分的な改善だが Planck 精度には届かない
- 完全 Boltzmann + 修正重力での再評価が必要

## 5. ITU 枠組み内での解釈

CMB ピーク位置は **early universe** の物理 (音速 + 距離) で決まる。Phase 20 で提案した「**原始 QECC 残留**」が CDM 様の密度寄与を生む場合:

- Hilbert 空間の早期エンタングルメント分布が **density perturbation** に痕跡を残す
- ΛCDM の Ω_CDM = 0.27 を**情報構造的に**説明する経路
- これは将来課題 (Phase 22+) で取り組むべき

## 6. 本 Phase の限界 (率直に)

- 解析公式は ~5% 精度。完全結果は CAMB / CLASS 必要。
- 音響ピークの**振幅** (peak heights) は計算していない。これは重力ポテンシャルの dark matter 駆動を含むため、修正重力 Boltzmann が必要。
- 上記の通り「ΛCDM が圧倒的に強い」事実は変わらない。

つまり: **CMB は依然として ITU の最後の弱点**。Phase 20-21 の段階では「ΛCDM ライバルではない」と認めるのが学術的に誠実。

しかし、これは ITU 枠組みの**否定**ではなく、「**早期宇宙の情報構造を別途特定する必要**」という方向性を示唆。次の研究フロンティア。
