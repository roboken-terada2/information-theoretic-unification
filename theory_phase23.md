# Phase 23: マターパワースペクトラム $P(k)$ — 大規模構造形成 in ITU

## 1. 動機

Phase 21 で CMB ピークが ITU の弱点と判明。Phase 22 で「凍結 QECC 情報」として
$\Omega_{\rm CDM} = 0.266$ を桁オーダーで再現できる可能性を示した。

しかし**現代宇宙論の最強の検証**は CMB だけでなく、**銀河の分布パターン**
(= 物質のパワースペクトラム $P(k)$):
- SDSS, BOSS, DESI: $10^6$ 個以上の銀河の3次元分布
- 観測される $P(k)$ は $k_{\rm eq} \approx 0.015$ h/Mpc 付近にピーク
- $\sigma_8 = 0.811$ (Planck, BBKS で 8 h⁻¹ Mpc スケールでの揺らぎ振幅)

本 Phase: ITU 枠組みで $P(k)$ を計算し、観測との一致を評価。

## 2. パワースペクトラムの理論

### 2.1 線形 $P(k)$ の標準形

インフレーション直後の**原始ゆらぎ**:
$$P_{\rm prim}(k) = A_s\, k^{n_s}$$
ここで $n_s \approx 0.965$ (Planck), $A_s$ は振幅。

物質密度ゆらぎは**transfer function** $T(k)$ で重みづけ:
$$P(k) = A\, k^{n_s}\, T^2(k)$$

### 2.2 BBKS Transfer function (Bardeen, Bond, Kaiser, Szalay 1986)

ΛCDM の場合:
$$T(q) = \frac{\ln(1 + 2.34 q)}{2.34 q} \left[1 + 3.89 q + (16.1 q)^2 + (5.46 q)^3 + (6.71 q)^4\right]^{-1/4}$$
$q = k / \Gamma$, $\Gamma \approx \Omega_m h$ (shape parameter).

### 2.3 物質ラジエーション等価点 $k_{\rm eq}$

転移波数:
$$k_{\rm eq} \approx 0.0746\, \Omega_m h^2\, \mathrm{Mpc}^{-1}$$

物理的意味:
- $k < k_{\rm eq}$ (大規模): $P(k) \propto k^{n_s}$ ← 物質優勢で成長
- $k > k_{\rm eq}$ (小規模): $P(k) \propto k^{n_s - 4}$ ← 放射優勢で抑制
- ピーク (turnover) が $k_{\rm eq}$ に現れる

### 2.4 $\sigma_8$ 規格化

8 h⁻¹ Mpc スケール内の質量分散:
$$\sigma_8^2 = \int \frac{dk}{2\pi^2} k^2 P(k) W_{8h^{-1}\rm Mpc}^2(k)$$
Planck 2018 観測: $\sigma_8 = 0.811$。

## 3. ITU 枠組みでのモデル比較

| モデル | $\Omega_m^{\rm eff}$ | $k_{\rm eq}$ (h/Mpc) | $\sigma_8$ |
|---|---|---|---|
| ΛCDM (Planck) | 0.315 | 0.0149 | 0.811 |
| MOND-only | 0.049 | 0.0023 | $\sim 0.06$ (小さい) |
| **ITU hybrid (cold)** | $0.066 + $ effective from $f$ | $\sim 0.0149$ | $\sim 0.81$ |
| ITU hybrid (warm, QECC scale) | 0.066 + warm | ~0.0149 + cutoff at small scales | 異なる |

**核心の仮説**: Phase 22 の「凍結 QECC 情報」が完全に冷たい (CDM 様) なら $P(k)$ は ΛCDM と区別不能。
**QECC 特性長**を持つなら小スケールで cutoff が出現 → 観測との対照で検証可能。

## 4. ITU 予言 (主候補)

### 仮説 A: 冷たい凍結 QECC ($\equiv$ 標準 CDM)
- $\Omega_m^{\rm eff} = 0.315$ で **$P(k)$ は ΛCDM と一致**
- 観測との一致 = ITU の整合性
- 「特定値 $\Omega_{\rm CDM} = 0.266$ がなぜか」は依然未説明

### 仮説 B: 暖かい QECC (特性長あり)
- 凍結 QECC ビット同士に**最小スケール** $\lambda_{\rm QECC}$
- $k > 1/\lambda_{\rm QECC}$ で $P(k)$ 抑制
- 観測上、warm DM 制約 ($\lambda \lesssim 100$ kpc) 内ならOK
- 区別する観測: Lyman-α forest, satellite galaxy counts

### 仮説 C: 完全に MOND (修正重力)
- $\Omega_{\rm CDM} = 0$
- $P(k)$ は完全に異なる (turn-over の位置と形が変)
- 観測と矛盾 → **棄却**

## 5. 数値計画

### Part A: ΛCDM $P(k)$ baseline
BBKS で標準計算、観測 SDSS $P(k)$ (Reid et al. 2010 等) と比較。

### Part B: MOND-only $P(k)$
$\Omega_m = 0.049$ で BBKS。当然観測と大きく外れる予想。

### Part C: ITU hybrid (cold QECC) $P(k)$
$\Omega_m^{\rm eff} = 0.315$ (frozen QECC が cold DM 様に振る舞う) で BBKS。
→ ΛCDM と一致する → ITU は LSS 観測と整合 (DM 機構が情報凍結なら)。

### Part D: $\sigma_8$ 規格化
3 モデルでの $\sigma_8$ を計算、観測 0.811 と比較。

### Part E: 周波数解像度
- ΛCDM: 区別不能
- MOND-only: 明確に違う
- ITU hybrid: ΛCDM と一致

これにより「ITU は LSS 観測と整合する DM 機構を持つ」と結論可能。

## 6. 限界

⚠️ 本 Phase で示せない:
- 非線形構造形成 (= N 体シミュレーション)
- BAO peaks の精密位置
- redshift space distortions (RSD)
- weak lensing power spectrum

これらは将来 Phase で必要。

✅ 示せる:
- 線形理論レベルでの $P(k)$ 構造
- ITU hybrid (cold) が ΛCDM と区別不能であること
- MOND-only は明確に観測と矛盾すること
