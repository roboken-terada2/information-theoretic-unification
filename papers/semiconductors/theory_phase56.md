# Phase 56: 3D スケーリングと量子限界 ― FinFET から CFET、そして 1 nm の壁

> **Tier 1 #4 (Semiconductors) — Phase 2/4**
> Tier 0 ITU: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 56 の目的

Phase 55 で **トランジスタ = 1-bit QECC** を確立しました。Phase 56 では:

1. **FinFET → GAAFET → CFET の進化を ITU で再導出**
2. **Short Channel Effect (SCE), DIBL, V_t roll-off** が ITU 公理にどう現れるか
3. **量子トンネル漏れ電流**が支配する nm 領域の物理を計算
4. **接触抵抗 (Sharvin)** ― スケーリングの物理的下限
5. **1 nm 以下の領域**で何が起こるか予測

中心テーゼ:

> **ゲート幾何の進化 = $K_A$ がチャネルに及ぼす支配面積の最大化**
> 3 次元ラップ構造は ITU 公理の自然な工学的帰結である。

---

## 1. ゲート支配の ITU 解釈

### 1.1 平面 MOSFET の限界

平面 (bulk) MOSFET の場合、ゲートはチャネル**上面のみ**を制御:

$$\delta\langle K_{\rm gate}\rangle = \int_{\text{top surface}} V_{GS} \cdot \rho_A \, dA$$

ゲート長 $L_g$ を縮めると **ソース・ドレインからの電位影響 (Short Channel Effect, SCE)** が無視できなくなり、$K_A$ の支配が崩れる。

### 1.2 3 次元ラップによる解決

| 構造 | ゲート結合面 | 実効 ITU 結合定数 | 限界ノード |
|---|---|---|---|
| Planar | 1 面 | $\eta_1 = 1$ | ~28 nm |
| **FinFET** | **3 面 (top + 2 sides)** | $\eta_3 \approx 2.5$ | **~5 nm** |
| **GAAFET (nanosheet)** | **4 面 (full wrap)** | $\eta_4 \approx 3.8$ | **~2 nm** |
| **CFET (stacked GAA)** | 4 面 × 多層 | $\eta_4 \times N_{\rm tier}$ | ~1 nm (?) |

**ITU 予測**: チャネル体積 $V$ あたりの $K$ 支配面積 $A_{\rm gate}/V$ を最大化することが scaling の本質。
GAAFET ($A/V \approx 4/W$, $W$ = sheet 幅) は FinFET ($A/V \approx 3/W$) より 33% 効率的。

---

## 2. DIBL と V_t roll-off

### 2.1 経験式 (Yan-Ozturk-Pinto)

$$DIBL = \frac{V_{T}^{V_{DS}=0} - V_{T}^{V_{DS}=V_{DD}}}{V_{DS}} \approx \frac{\epsilon_{\rm Si}}{\epsilon_{\rm ox}} \cdot \frac{t_{\rm ox} \cdot t_{\rm Si}}{L_g^2}$$

⇒ $L_g$ を 1/2 にすると DIBL は **4 倍** 悪化。これが平面 CMOS の崩壊点。

### 2.2 ITU 翻訳

ITU 公理: $\delta S = \delta\langle K\rangle$。

DIBL が大きい = ドレイン電位が $K_A$ に侵入 = ゲートの ITU 支配が破綻。

3D ラップは ドレインから見た静電遮蔽距離を $L_g$ から **min(L_g, W_{\rm fin}/2)** に短縮 ⇒ DIBL を構造的に抑制。

### 2.3 数値検証

Planar / FinFET / GAAFET の DIBL を $L_g$ vs ノードでプロット (Phase 56 simulation 結果)。

---

## 3. 量子トンネル漏れ電流

### 3.1 直接トンネル (Wentzel-Kramers-Brillouin)

OFF 状態でも電子はチャネル障壁を **WKB トンネル** で抜ける:

$$I_{\rm leak} \propto \exp\left(-\frac{2 L_g}{\hbar} \sqrt{2 m^* \phi_B}\right)$$

$\phi_B \approx 0.3$ eV, $m^* = 0.2 m_e$:

| $L_g$ | トンネル係数 | 漏れ電流比 |
|---|---|---|
| 10 nm | $e^{-95}$ | 10⁻⁴¹ (無視可) |
| 5 nm | $e^{-47}$ | 10⁻²¹ |
| **3 nm** | $e^{-28}$ | **10⁻¹²** |
| **2 nm** | $e^{-19}$ | **10⁻⁸** |
| **1 nm** | $e^{-9.5}$ | **10⁻⁴ (致命的)** |
| 0.5 nm | $e^{-4.7}$ | 10⁻² |

⇒ **1 nm 以下では OFF 電流 ≈ ON 電流**。トランジスタの「スイッチ」 機能が崩壊。

### 3.2 ITU 視点

トンネル漏れ = ITU 公理が「**部分系 A の閉鎖性が破れる**」 ことの表現。

$$\delta S(\rho_A) \neq \delta\langle K_A\rangle \quad \text{(when tunneling dominates)}$$

⇒ 部分系を再定義 (チャネル + tunneling tail) しないと ITU が成立しない。これは実質的に **古典トランジスタ概念の終わり**。

---

## 4. 接触抵抗 (Sharvin) ― もう一つの下限

### 4.1 Landauer-Büttiker 公式

完全弾道 (ballistic) 領域では:

$$G_{\rm Sharvin} = \frac{2 e^2}{h} \cdot N_{\rm modes}$$

ここで $N_{\rm modes} \approx k_F^2 A / 4\pi$ (3D), $A$ = 接触面積。

$R_{\rm contact} = 1/G_{\rm Sharvin}$。Si で $k_F \approx 10^9 \text{ m}^{-1}$、$A = (3 \text{ nm})^2$:

$$R_{\rm Sharvin} \approx 200 \, \Omega \cdot \mu\text{m} \quad \text{(per contact)}$$

⇒ 1 GHz 動作 + 0.7V 電源では **接触抵抗だけで $V_{DD}$ の 20% 以上を消費**。

### 4.2 ITU 含意

接触抵抗の下限は **チャネルの $K_A$ ではなく source/drain の接合構造** に由来。
スケーリングの主要ボトルネックは **3 nm 以下では「ゲート」 より「接触」 が支配**。

---

## 5. 2D 材料トランジスタ

### 5.1 候補材料

| 材料 | 厚さ | E_g (eV) | $\mu$ (cm²/Vs) | スケーリング限界 |
|---|---|---|---|---|
| Graphene | 0.34 nm | 0 (massless) | 200,000 | スイッチ不可 (E_g = 0) |
| **MoS₂** | 0.65 nm | **1.8** | 200-500 | **~1 nm** |
| **WSe₂** | 0.7 nm | 1.6 | 300 | ~1 nm |
| Black phosphorus | 0.55 nm | 0.3-2.0 | 1000+ | 不安定 |

**MoS₂** が現実的本命。**Intel + IMEC** は 2027 年に 2D-FET 試作を発表予定。

### 5.2 ITU 予測

2D 材料 = チャネル厚 = 単原子層 ⇒ チャネル体積最小 ⇒ ゲート支配係数最大化 ⇒ **ITU 観点で最適**。

しかし接触抵抗 (van der Waals 界面) が高い ⇒ 接触工学が次の課題。

---

## 6. Phase 56 数値検証

### 6.1 検証 1: DIBL vs L_g for Planar / FinFET / GAAFET
3 構造の DIBL を 50 nm 〜 1 nm でプロット。

### 6.2 検証 2: トンネル漏れ電流 vs L_g
WKB 公式で OFF 電流を計算、CMOS 1nA/μm spec との比較。

### 6.3 検証 3: 接触抵抗 vs 接触面積
Sharvin 公式で R_contact を見積もり、3nm/2nm/1nm ノードで評価。

### 6.4 検証 4: ITU 結合効率 (η) と node limit
$\eta$ vs ノードのプロットで Planar (28nm)、FinFET (5nm)、GAAFET (2nm)、CFET (1nm) の限界を視覚化。

---

## 7. Phase 56 の結論

1. **3D ラップ構造は ITU 公理の自然な工学帰結** ($K_A$ 支配面積の最大化)
2. **GAAFET は FinFET の 33% 効率向上** ⇒ 2 nm ノードまで延命
3. **1 nm 以下では量子トンネルで「スイッチ」 が崩壊** ⇒ 古典 MOSFET 概念の終焉
4. **接触抵抗が 3 nm 以下で支配的** ⇒ 接触工学が次の研究領域
5. **2D 材料 (MoS₂) は ITU 最適だが接触課題あり** ⇒ 2027-2030 が商用化リトマス試験

Phase 57 では **トンネル限界を超える非古典デバイス** (TFET, NC-FET, spintronics, 光) を詳細解析し、**ITU 観点での最適選択**を提案します。

---

## 引用

```
Terada, M. (2026). ITU and Semiconductors (Phase 55-58).
Tier 1 #4 application paper. In preparation.
```

参考:
- Yan, Ozturk, Pinto (1992) IEEE TED 39, 1704 (DIBL)
- Frank et al. (1992) IEEE EDL 13, 660 (短チャネル)
- Datta (1995) "Electronic Transport in Mesoscopic Systems" (Sharvin)
- Radisavljevic et al. (2011) Nat Nano 6, 147 (MoS₂ FET)
- IRDS 2023 roadmap
