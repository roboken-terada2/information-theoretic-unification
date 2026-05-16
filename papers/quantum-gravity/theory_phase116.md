# Phase 116: String Theory + M Theory + Strominger-Vafa + ITU 統合

> **Tier 1 #17 Quantum Gravity — Phase 6/8 (Block A)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 116 の目的

Phase 115 で LQG (bottom-up 離散量子化) を扱った。Phase 116 では **String Theory + M Theory** (top-down) を ITU 公理で再解釈し、両アプローチの統合視点を確立する。

確立する内容:

1. **5 つの超弦理論**: Type I, IIA, IIB, Heterotic SO(32), Heterotic E8×E8
2. **M-theory (Witten 1995)**: 11 次元で 5 つを統合
3. **D-branes**: open string の端点が乗る (d+1) 次元時空対象
4. **Strominger-Vafa (1996)**: BH エントロピーの microstate counting
5. **Calabi-Yau compactification**: 10 → 4 次元
6. **LQG vs String の統合 ITU 視点**: K_geom の 2 表現

中心テーゼ:

> **弦理論 = ITU の連続 K_geom 実現** / **LQG = ITU の離散 K_geom 実現**。
> 共通の δS = δ⟨K_geom⟩ が両者を縫合する。
> Strominger-Vafa の BH 状態数 = Bekenstein-Hawking エントロピー一致は ITU 公理の **microcanonical 検証**。

---

## 1. 弦理論の基礎

### 1.1 5 つの超弦理論 (10 次元)

| 名前 | 弦タイプ | gauge | discovered |
|---|---|---|---|
| Type I | open + closed | SO(32) | Green-Schwarz 1984 |
| Type IIA | closed (non-chiral) | — | 1980s |
| Type IIB | closed (chiral) | — | 1980s |
| Heterotic SO(32) | closed (heterotic) | SO(32) | Gross-Harvey-Martinec-Rohm 1985 |
| Heterotic E8×E8 | closed (heterotic) | E8 × E8 | 同上 |

全て **10 次元時空**で定義され、超対称性を含む。

### 1.2 弦の張力 (T_s) と長さ (ℓ_s)

```
T_s = 1 / (2π α')         (弦張力)
ℓ_s = √α'                  (弦長)
```

α' は Regge slope パラメータ。実験的に ℓ_s は Planck 長より大きい可能性 (ℓ_s ≳ ℓ_P)。

### 1.3 質量公式

```
M² = (1/α') (N + N̄ - a)
```

N, N̄: 左/右回り励起数; a: 真空エネルギー (10D で a=1)。

---

## 2. M-theory (Witten 1995)

### 2.1 双対性ネットワーク

5 つの 10D 超弦理論は **M 理論 (11 次元)** から派生:

```
       T-duality
IIA <-------> IIB
 |              |
 | S-duality    | S-duality
 |              |
HE  <-------> HO
       T-duality

         |
    strong coupling
         |
        M-theory (11D)
```

### 2.2 11 次元の重要性

- M-theory の low energy 効果理論 = 11D supergravity
- AdS_7 × S^4 解 = M5-brane geometry
- 4 次元 N=8 supergravity の理論

### 2.3 ITU 視点

11D の **超対称コホモロジー** が ITU の K-state を最大限まで対称化した状態。M-theory は **K_geom の対称性最大限実現**。

---

## 3. D-branes と Open Strings

### 3.1 Dp-brane

- 空間 p 次元 + 時間 1 次元 = (p+1)D 時空対象
- open string の端点が乗る
- 質量 ∝ 1/g_s (非摂動的)

### 3.2 D-brane の質量

```
M_Dp = T_Dp × V_p = (1 / ((2π)^p α'^{(p+1)/2} g_s)) × V_p
```

### 3.3 Gauge theory on D-branes

N 枚 Dp-brane が重なると、U(N) Yang-Mills (p+1 D) が生成。これが AdS/CFT の起源 (Maldacena 1997)。

### 3.4 ITU での意義

D-brane = **境界条件 = K-flow の boundary 終端**。
N → ∞ で large-N limit → CFT_d → AdS_{d+1} bulk (ITU 公理の連続実現)。

---

## 4. Strominger-Vafa: BH 状態数 (1996)

### 4.1 主結果

5D extremal BPS BH (Type IIB on T^5) の **microstate counting**:

```
S_micro = 2π √(Q_1 Q_5 N) = A_horizon / (4 G_N)
```

- Q_1, Q_5: D1, D5 charge
- N: KK momentum
- 完全一致 = 史上初の string theory による Bekenstein-Hawking 公式の microscopic 導出

### 4.2 ITU 解釈

```
S_micro = log (# microstates) = ⟨K_geom⟩ / ℏ = A / (4 G_N ℏ)
```

⇒ **Strominger-Vafa = ITU 公理 δS = δ⟨K_geom⟩ の microcanonical 検証**。

### 4.3 一般化

その後、多くの BH solution で同様の matching:
- BMPV BH (5D rotating)
- 4D BPS BH
- non-extremal correction
- Hayward et al. AdS_4 BH

⇒ ITU 公理は **string vacua 全体で成立**。

---

## 5. Calabi-Yau Compactification

### 5.1 構造

10D string → 4D 物理:

```
M_10 = M_4 × CY_6
```

CY_6 = 6 次元 Calabi-Yau manifold (Ricci-flat, complex Kähler)。

### 5.2 4D 効果

- Hodge numbers (h^{1,1}, h^{2,1}) が low-energy 物理を決定
- N=1 supersymmetry が残る
- Fermion 世代数 = |χ| / 2 (オイラー数の半分)

### 5.3 ITU 視点

CY_6 の **計量構造** が K_geom を 4D に compactify した時の K-state spectrum を決定。

### 5.4 String Landscape

CY 数 ~ 10^500 (Bousso-Polchinski 2000) → 各 vacuum が異なる K-state set を持つ。
ITU は **landscape 構造を K-state 多様体として理解**。

---

## 6. LQG vs String — ITU 統合

### 6.1 比較表

| 観点 | LQG | String / M / AdS-CFT |
|---|---|---|
| 出発点 | GR + canonical 量子化 | 1D 弦 + 超対称 |
| 次元 | 4D (時空) | 10/11D (compact 化) |
| 量子化 | non-perturbative discrete | perturbative continuous |
| BH | state counting via spin network | D-brane microstate (Strominger-Vafa) |
| K_geom | discrete eigenvalue (A_min = 5.17 ℓ_P²) | smooth bulk + Ramond-Ramond flux |
| UV | finite (discrete) | UV completed via string size ℓ_s |
| 実験 | LIGO 補正、GW echo | EHT shadow、collider energy |

### 6.2 ITU での統合

ITU 公理は両方を内包:

```
δS = δ⟨K_geom⟩
  ↓
  - LQG: K_geom が discrete スピン演算子で表現
  - String: K_geom が D-brane charge + RR flux で表現
```

両者は **K_geom の異なる量子化スキーム**で、共通の半古典極限を持つ。

### 6.3 例: 同じ BH エントロピー

| Theory | S_BH 公式 |
|---|---|
| 半古典 GR | A / (4 G_N) |
| LQG | 8π γ ℓ_P² Σ √(j(j+1)) / (4 G_N) |
| Strominger-Vafa | 2π √(Q_1 Q_5 N) |
| ITU | δ⟨K_geom⟩ / ℏ |

⇒ **同じ S_BH を 3 つの方法で導出**。

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Strominger-Vafa 公式の数値計算**: S = 2π √(Q_1 Q_5 N) vs A/(4G_N)
2. **5 弦理論の質量スペクトル**: M² = N/α' の比較
3. **M-theory duality web**: T/S-duality 関係
4. **D-brane gauge group生成**: N 枚 → U(N)
5. **ITU 統合表**: LQG / String / 半古典の S_BH 一致

---

## 8. Phase 116 主結論

1. **弦理論 5 種類 (10D)**: Type I, IIA, IIB, HO, HE
2. **M-theory (Witten 1995)**: 11D で統合
3. **D-brane**: open string boundary = ITU K-flow 終端
4. **Strominger-Vafa (1996)**: S_micro = 2π√(Q_1Q_5N) = A/(4G_N)
5. **CY compactification**: K-state spectrum を 4D へ転送
6. **ITU 統合**: LQG + String = K_geom の 2 量子化スキーム
7. **次の Phase 117** で **量子重力の実験的検証**に進む

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| 弦 | K-flow を 1D 線素として展開 |
| M-theory | K_geom 最大対称化 (11D) |
| D-brane | K-flow boundary 終端 |
| Strominger-Vafa | ITU 公理の microcanonical 検証 |
| CY compactification | K-state spectrum の 4D 転送 |
| LQG vs String | K_geom の 2 量子化 |

---

## 引用

```
Terada, M. (2026). Phase 116: String theory, M-theory, Strominger-Vafa,
and LQG–string integration in ITU. Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Polchinski, J. (1998) "String Theory" (Vol I & II), Cambridge University Press
- Becker, K., Becker, M., Schwarz, J. (2007) "String Theory and M-Theory", Cambridge
- Strominger, A., Vafa, C. (1996) "Microscopic origin of the Bekenstein-Hawking entropy" Phys. Lett. B 379, 99 (arXiv:hep-th/9601029)
- Witten, E. (1995) "String theory dynamics in various dimensions" Nucl. Phys. B 443, 85 (arXiv:hep-th/9503124)
- Polchinski, J. (1995) "Dirichlet branes and Ramond-Ramond charges" PRL 75, 4724 (arXiv:hep-th/9510017)
- Candelas, P., Horowitz, G., Strominger, A., Witten, E. (1985) "Vacuum configurations for superstrings" Nucl. Phys. B 258, 46
- Bousso, R., Polchinski, J. (2000) "Quantization of four-form fluxes and dynamical neutralization of the cosmological constant" JHEP 06, 006
