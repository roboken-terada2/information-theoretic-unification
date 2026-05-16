# Phase 55: 半導体トランジスタの ITU 基礎 ― Landauer 極限と 60 mV/decade の壁

> **Tier 1 #4 (Semiconductors) — Phase 1/4**
> Tier 0 ITU: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 55 の目的

ITU 公理 $\delta S(\rho_A) = \delta\mathrm{Tr}[K_A^{(0)} \rho_A]$ を **半導体トランジスタ** に適用し、

1. **Landauer 極限** ($k_B T \ln 2$ /bit) が ITU から導けることを示す
2. **Boltzmann 暴政 (60 mV/decade @ 300K)** が ITU 公理の必然帰結であることを示す
3. CMOS / FinFET / GAAFET / TFET / NC-FET / spintronics の **ITU 比較** を行う
4. Phase 56-58 (微細化, 新原理 device, 産業ロードマップ) への基盤を与える

中心テーゼ:

> **トランジスタとは、$k_B T$ ノイズから 1 ビットを保護する最小 QECC である。**

---

## 1. トランジスタを情報理論で見る

### 1.1 何を「保護」 しているか

n-MOSFET の ON / OFF 状態:

| 状態 | チャネル電子密度 | 論理値 |
|---|---|---|
| OFF | $n_0 e^{-q V_{GS}/k_B T}$ | 0 |
| ON | $n_0$ (空乏層消失) | 1 |

⇒ **1 bit の論理状態を、熱励起 $k_B T$ の雑音から守る** デバイス。

### 1.2 ITU 公理の適用

部分系 $A$ = トランジスタ・チャネル、modular Hamiltonian $K_A$ = ゲート電位場。

$$\delta S(\rho_A) = \delta\mathrm{Tr}[K_A \rho_A]$$

電圧 $V_{GS}$ を変化させたときの:
- 左辺 $\delta S$: チャネル状態の不確実性変化
- 右辺 $\delta\langle K\rangle$: ゲートによる仕事

両者が等しい ⇒ **トランジスタは、ゲート電圧の仕事を「論理状態の純度向上」 に変換する装置**。これは QECC が syndrome 測定の仕事を「論理状態の純度回復」 に使うのと**完全に対応**する (Phase 43-46)。

---

## 2. Landauer 極限の ITU 導出

### 2.1 Landauer 1961 (古典)

1 bit 消去 (2 状態 → 1 状態) は最小 $k_B T \ln 2$ の熱発生を伴う。

300K では $\approx 2.87 \times 10^{-21}$ J/bit $\approx 0.018$ eV/bit。

### 2.2 ITU 導出

ITU 公理に $\rho_A = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|$ (両状態の重ね合わせ) を入れ、$\rho_A' = |0\rangle\langle 0|$ (消去後) を入れる:

$$\delta S = S(\rho_A) - S(\rho_A') = \ln 2 - 0 = \ln 2$$

$$\delta\langle K\rangle = W_{\rm erase} / k_B T$$

ITU は $\delta S = \delta\langle K\rangle$ を要求 ⇒

$$W_{\rm erase} \geq k_B T \ln 2 \quad ★ \text{Landauer 極限}$$

これが ITU から自動導出される。**Landauer 極限は ITU 公理の最小帰結**。

---

## 3. Boltzmann 暴政: 60 mV/decade

### 3.1 サブスレッショルド傾斜

ドレイン電流 $I_D \propto \exp(qV_{GS}/n k_B T)$ ($n$: ideality factor ≥ 1)。

電流を 10 倍にするのに必要な電圧:

$$SS = \frac{dV_{GS}}{d(\log_{10} I_D)} = n \cdot \frac{k_B T}{q} \ln 10$$

300K, $n=1$:

$$SS_{\min} = \frac{0.02585 \text{ V}}{0.4343} = 59.6 \text{ mV/decade}$$

**これが Boltzmann 暴政**。$V_{DD}$ を 1V から 0.5V に下げると ON/OFF 比が悲惨になる。

### 3.2 ITU 解釈

ITU 公理は **熱平衡で $K_A = H/k_B T$ (modular = 熱) を要求**。したがって $\partial S/\partial V$ は $1/(k_B T)$ で制限される。

⇒ **熱的 $K_A$ を使う限り 60 mV/decade は破れない**。

### 3.3 突破の道

| 機構 | 原理 | ITU 視点 |
|---|---|---|
| **Tunnel FET (TFET)** | バンド間トンネリング | $K_A$ が non-thermal (WKB 由来) ⇒ SS < 60 mV/dec 可 |
| **Negative Capacitance FET** | 強誘電体の負容量 | ゲート電圧増幅 ⇒ 実効 $T_{\rm eff} < T$ |
| **Spintronics (spin FET)** | スピン偏極 | 量子情報を担持 ⇒ $k_B T \ln 2$ より低エネルギー可 |
| **Optical / photonic switch** | 光子 | 室温だが photon mode は $h\nu \gg k_B T$ |

これらは ITU 公理を破るのではなく、**$K_A$ を熱から非熱に置換** することで SS を下げる。Phase 57 で詳細解析。

---

## 4. デバイス世代の比較 (Phase 55 simulation)

| 世代 | 年 | ノード | 構造 | $V_{DD}$ | エネルギー/op |
|---|---|---|---|---|---|
| Planar CMOS | 2000 | 130 nm | Bulk | 1.5 V | $\sim 10^{-15}$ J |
| Planar 32nm | 2010 | 32 nm | Strained Si | 1.0 V | $\sim 10^{-16}$ J |
| **FinFET** | 2014 | 14 nm | 3D fin | 0.8 V | $\sim 5\times 10^{-17}$ J |
| **GAAFET** | 2023 | 3 nm | Nanosheet | 0.7 V | $\sim 2\times 10^{-17}$ J |
| **CFET (proposed)** | 2028 | 1 nm | Stacked | 0.6 V | $\sim 10^{-17}$ J |
| **Landauer limit (300K)** | — | — | — | — | $\mathbf{2.87 \times 10^{-21}}$ J |

⇒ 現代 CMOS は Landauer 極限の **約 $10^4$ 倍** のエネルギーを消費。残された余地が大きい。

---

## 5. Phase 55 数値検証

### 5.1 検証 1: Landauer 極限の確認

$E_{\rm Landauer}(T) = k_B T \ln 2$ を 100K〜500K で計算し、Boltzmann 法則と比較。

### 5.2 検証 2: 60 mV/decade の温度依存性

$SS(T) = (k_B T / q) \ln 10$ を計算し、77K (cryogenic) で 15 mV/dec、300K で 60 mV/dec、500K (高温動作) で 100 mV/dec を確認。

### 5.3 検証 3: デバイス世代の効率トレンド (Moore's law)

エネルギー/op を 1990〜2030 でプロット (logスケール)。傾きから Koomey の法則 (2 年で 1/2) を抽出。

### 5.4 検証 4: TFET / NC-FET の SS シミュレーション

ボルツマン+トンネル合成式で 30 mV/dec の TFET 動作領域を可視化。

---

## 6. Phase 55 の結論

1. **ITU 公理から Landauer 極限と Boltzmann 暴政が自然に導出される**
2. **トランジスタ = 1 bit QECC** の双対性を確立
3. **60 mV/dec の壁を破るには $K_A$ を non-thermal にする必要** ⇒ TFET, NC-FET, spin
4. 現代 CMOS は Landauer 極限の $10^4$ 倍 ⇒ **理論的には 4 桁の効率改善余地**

Phase 56 では微細化スケーリング (FinFET → GAAFET → CFET) を ITU で再導出し、**1 nm 以下で何が起きるか** を予測します。

---

## 引用

```
Terada, M. (2026). ITU and Semiconductors (Phase 55-58).
Tier 1 #4 application paper. In preparation.
```

参考:
- Landauer (1961) IBM J Res Dev 5, 183
- Theis & Solomon (2010) Science 327, 1600 (TFET)
- Salahuddin & Datta (2008) Nano Lett 8, 405 (Negative Capacitance)
- Moore (1965), Koomey (2011)
