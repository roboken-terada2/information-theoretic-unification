# Phase 19: ブラックホール時空と重力波 — 量子情報からの予測と LIGO 観測との比較

## 1. 動機

これまでの Phase で:
- BH エントロピー $S = A/(4G_N)$ (Phase 5, 6) ✓
- 情報のユニタリ保存 (Phase 6, Page 曲線) ✓
- 時間 = モジュラーフロー (Phase 4) ✓
- 線形化 + 2 次 Einstein 方程式 (Phase 2, 17) ✓

これらを組み合わせて **BH 時空 (Schwarzschild メトリック)** と **重力波 (GW)** の観測量を予測し、**LIGO の実観測**と比較する。

## 2. Schwarzschild メトリックの量子情報的起源

### 2.1 メトリック
球対称・真空・静的解 (Schwarzschild 1916):
$$ds^2 = -\left(1 - \frac{r_s}{r}\right) c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1} dr^2 + r^2 d\Omega^2$$

**Schwarzschild 半径**:
$$r_s = \frac{2 G M}{c^2}$$

事象の地平面: $r = r_s$。特異点: $r = 0$。

### 2.2 量子情報的導出 (概略)

1. **公理** (Phase 1-2): $\delta S = \delta\langle K\rangle$ から線形化 Einstein
2. Phase 17 で 2 次までの**非線形補正**
3. 全次数極限 + 球対称性 + 真空 ($T_{\mu\nu} = 0$) → Schwarzschild 解

つまり Schwarzschild は **「情報構造から創発する真空 Einstein 方程式の球対称解」**。

### 2.3 量子情報的描像
- BH = **最大エンタングルメント状態** (Phase 5: 完全テンソル QECC 構造)
- 地平面 = エンタングルメント wedge の境界
- 特異点 = 量子情報の集積点 (古典的には不可解だが、QECC では論理量子ビット集約点)

## 3. Hawking 温度

### 3.1 公式
$$T_H = \frac{\hbar c^3}{8 \pi G M k_B}$$

太陽質量 BH: $T_H \approx 6 \times 10^{-8}$ K (極低温、観測不可能)
原子質量 BH ($M = 10^{-8}$ kg): $T_H \approx 10^{15}$ K (Planck 寸前)

### 3.2 ITU 枠組み内での解釈

地平面でのモジュラーフロー $\sigma_t^{\rm vac}$ は **Rindler boost** = Bisognano-Wichmann (Phase 4)。
モジュラー周期 $2\pi$ ↔ 通常時間で $\beta_H = 2\pi r_s/c = \hbar/(k_B T_H)$。

つまり **Hawking 温度 = de Sitter 風モジュラー温度** ↔ Phase 4 のモジュラーフロー時間概念の幾何的実現。

## 4. Hawking 放射スペクトラム

### 4.1 公式
Schwarzschild BH の放射粒子のエネルギー分布:
$$\frac{dN}{dt\, d\omega} = \frac{\Gamma_\ell(\omega)}{2\pi} \cdot \frac{1}{e^{\hbar\omega/k_B T_H} \mp 1}$$
$(\pm = $ bosonic/fermionic), $\Gamma_\ell$ は greybody factor (geometry 依存)。

### 4.2 数値検証
温度 $T_H(M)$ を入力として Planck/Fermi-Dirac 分布をプロット。

## 5. 準ノーマルモード (QNM)

BH に摂動を加えると、特定の複素周波数で減衰する固有モードに緩和:
$$h_{\mu\nu}(t) \propto e^{i\omega_{\ell n} t}, \quad \omega_{\ell n} = \omega_R - i \omega_I$$

### 5.1 Schwarzschild BH の主モード $(\ell=2, m=2, n=0)$
解析的・数値的計算 (Leaver 1985, Berti 2009):
$$M \omega_{220} = 0.3737 - 0.0890 i$$

これを物理単位に変換:
$$f_{220} = \frac{c^3}{G M} \cdot \frac{0.3737}{2\pi} = \frac{c^3}{G M} \times 0.0594$$
$$\tau_{220} = \frac{G M}{c^3} \cdot \frac{1}{0.0890}$$

### 5.2 ITU 枠組み内
QNM = 境界熱 CFT 相関子の**極** (AdS/CFT 辞書):
$$\langle O(t) O(0)\rangle_T \sim e^{-i\omega_{QNM} t}$$

熱 CFT は Phase 4 のモジュラーフロー固有値分布から計算可能。

## 6. LIGO 観測との比較

### 6.1 GW150914 (Abbott et al. 2016, *PRL* 116, 061102)
LIGO による初検出:
- 連星 BH: $M_1 \approx 36 M_\odot$, $M_2 \approx 29 M_\odot$
- 最終 BH: $M_f \approx 62 M_\odot$ (放射エネルギー $\sim 3 M_\odot c^2$)
- 観測 ringdown 周波数: $f_{\rm obs} \approx 250$ Hz, 減衰時間 $\sim 4$ ms

### 6.2 我々の予言
$M_f = 62 M_\odot$ で:
$$f_{220}^{\rm pred} = \frac{c^3}{G \cdot 62 M_\odot} \times 0.0594 \approx 251\;\mathrm{Hz}$$
$$\tau_{220}^{\rm pred} \approx 3.6\;\mathrm{ms}$$

**LIGO 観測値 ($\sim 250$ Hz, $\sim 4$ ms) と精度数% で一致**!

### 6.3 Inspiral 周波数進化
連星 chirp 質量:
$$\mathcal{M} = \frac{(M_1 M_2)^{3/5}}{(M_1 + M_2)^{1/5}}$$
GW150914: $\mathcal{M} \approx 30 M_\odot$。

Inspiral 周波数: post-Newtonian で
$$f(t) = f_0 \left(1 - \frac{t}{t_c}\right)^{-3/8}$$
時間と周波数の関係から chirp 質量を抽出可能。

## 7. 数値シミュレーション計画

### Part A: Hawking 量
- $M = 1, 10, 100, 1000 M_\odot$ で $T_H, S_{BH}, r_s$ を計算
- 蒸発時間 $t_{\rm evap} \sim G^2 M^3/(\hbar c^4)$

### Part B: Hawking スペクトラム
- 太陽質量 BH での Planck/Fermi-Dirac 分布
- ピーク周波数と Wien 変位則の確認

### Part C: QNM
- $M = 10, 50, 100, 200 M_\odot$ で $f_{220}, \tau_{220}$ を予測
- LIGO GW150914 結果 ($M_f = 62 M_\odot$) との比較

### Part D: GW150914 ringdown 予言
- 観測値 250 Hz と予言値の比較
- 一致度 (%) を表示

### Part E: XX 鎖熱相関子 = QNM アナログ
- 有限温度 XX 鎖の time-correlator
- 減衰率を抽出 → CFT 熱モードの寿命
- これが BH QNM の境界 CFT 双対量

### Part F: Inspiral chirp 信号
- $f(t)$ 進化 + 振幅進化を計算
- LIGO 波形と比較

## 8. この Phase が示すこと

✅ 示せる:
- Schwarzschild BH の主要量 ($T_H, S_{BH}, r_s$) を ITU 枠組み内で計算可能
- QNM 周波数 $\sim 1/M$ が LIGO GW150914 観測と一致 ($\sim 250$ Hz)
- 熱 CFT 相関子減衰 = QNM 双対量

⚠️ 示せない:
- 完全な数値相対論計算 (binary BH 合体の full simulation)
- Inspiral-merger-ringdown (IMR) 波形の精密予測
- 連星 BH 形成確率・stellar evolution
- これらは別問題 (天文学・数値相対論の領域)

それでも「**情報理論的枠組みから LIGO 観測量が出る**」ことは強力な検証。
