# Phase 153: 超伝導 — BCS 理論 + Meissner 効果 + 高温超伝導 + K_SC

> **Tier 1 #22 Condensed Matter Physics — Phase 3/8 (Block A paper 6/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 153 の目的

Phase 152 で band theory + 半導体物理を扱った。Phase 153 では **超伝導 (Superconductivity)** へ:

1. **歴史**: Kamerlingh Onnes (1911) → Meissner (1933) → BCS (1957)
2. **BCS 理論 (Bardeen-Cooper-Schrieffer 1957, Nobel 1972)**: Cooper pair + gap Δ
3. **Meissner 効果**: 完全反磁性, London 方程式
4. **Type I vs Type II**: 臨界磁場, 渦糸
5. **高温超伝導**: cuprates (Bednorz-Müller 1986, Nobel 1987), 鉄系
6. **Josephson effect (1962, Nobel 1973)**: AC + DC
7. **ITU 視点**: K_SC = K_BE 凝縮の Cooper pair 版

中心テーゼ:

> **超伝導 = K_FD electron-phonon 媒介 → Cooper pair → K_BE 凝縮**。
> Meissner = K_SC の **macroscopic 量子コヒーレンス** の磁場排除。
> Type II 渦糸 = K_SC の **位相欠陥**。

---

## 1. 歴史

| 年 | 事象 |
|---|---|
| 1911 | Kamerlingh Onnes: Hg @ 4.2 K で抵抗 = 0 (Nobel 1913) |
| 1933 | Meissner-Ochsenfeld: 完全反磁性 |
| 1935 | London brothers: 唯象方程式 |
| 1950 | Ginzburg-Landau: order parameter ψ (Nobel 2003) |
| **1957** | **BCS**: Cooper pair + microscopic 理論 (Nobel 1972) |
| 1962 | Josephson: tunneling (Nobel 1973) |
| 1986 | Bednorz-Müller: La₂CuO₄ で 30 K (Nobel 1987) |
| 1987 | YBa₂Cu₃O₇ で 93 K (液体窒素超え) |
| 2008 | 鉄系超伝導 (Hosono) |
| 2015 | H₃S @ 200 K, 150 GPa |
| 2019 | LaH₁₀ @ 250 K, 170 GPa |

---

## 2. ★ BCS 理論 (1957) ★

### 2.1 Cooper pair (1956)

Fermi 海上で 2 電子に **弱い引力 (phonon 媒介)** → 束縛状態 (bound):

```
|Cooper⟩ = Σ_k g_k c^†_{k↑} c^†_{-k↓} |FS⟩
```

(opposite k, opposite spin)。

### 2.2 BCS gap 方程式

```
1 = N(0) V ∫_0^{ℏω_D} dε / √(ε² + Δ²)
```

T = 0 解:

```
Δ(0) = 2 ℏω_D exp(-1 / N(0)V)
```

### 2.3 ★ BCS 普遍関係 ★

```
2 Δ(0) / k_B T_c = 3.53   (weak coupling universal)
```

### 2.4 T_c 公式

```
k_B T_c = 1.13 ℏω_D exp(-1 / N(0)V)
```

### 2.5 数値: Pb

```
T_c = 7.20 K
ω_D / k_B = θ_D = 105 K
2Δ(0) = 3.53 × k_B × 7.20 = 2.19 meV ≈ 観測 ✓
```

### 2.6 ITU 視点

```
BCS = K_FD electron + K_phonon 結合 → K_Cooper-pair → K_BE macroscopic 凝縮
ψ(r) = ⟨c c⟩ = K_SC order parameter (Ginzburg-Landau)
```

---

## 3. ★ Meissner 効果 + London 方程式 ★

### 3.1 Meissner-Ochsenfeld (1933)

T < T_c で **磁場が完全に排除** される (完全反磁性 χ = -1)。

### 3.2 London 方程式 (1935)

```
∂j/∂t = (n_s e² / m) E       (1st London)
∇ × j = -(n_s e² / m) B      (2nd London)
```

合わせて:

```
∇² B = B / λ_L²
```

= 磁場が London penetration depth λ_L で指数減衰。

### 3.3 London penetration depth

```
λ_L = √(m / (μ_0 n_s e²))
```

| 物質 | λ_L (nm) |
|---|---|
| Al | 16 |
| Pb | 37 |
| Nb | 39 |
| YBCO | 150 |

### 3.4 Coherence length

```
ξ = ℏ v_F / (π Δ)
```

| 物質 | ξ (nm) |
|---|---|
| Al | 1600 |
| Pb | 83 |
| Nb | 38 |
| YBCO | 2 |

### 3.5 ITU 視点

```
Meissner = K_SC の macroscopic phase coherence による磁場排除
λ_L = K_SC の screening 長
ξ = K_SC order parameter の correlation 長
```

---

## 4. ★ Type I vs Type II ★

### 4.1 Ginzburg-Landau 比

```
κ = λ_L / ξ
```

- **κ < 1/√2**: Type I (完全反磁性 → H_c で normal)
- **κ > 1/√2**: Type II (H_c1 で渦糸 → H_c2 で normal)

| 物質 | κ | Type |
|---|---|---|
| Al, Sn, Pb | < 1 | I |
| Nb, NbTi, Nb₃Sn | > 1 | II |
| YBCO | ~100 | extreme II |

### 4.2 Abrikosov 渦糸 (1957, Nobel 2003)

Type II で H_c1 < H < H_c2 で **量子化された磁束** Φ_0 = h/(2e) = 2.07×10⁻¹⁵ Wb の渦糸が三角格子。

### 4.3 数値

```
Φ_0 = h / (2e) = 2.0678 × 10⁻¹⁵ Wb  ★ 普遍定数
```

### 4.4 ITU 視点

```
Type II 渦糸 = K_SC の topological defect (vortex)
Φ_0 = K_SC の幾何学的量子化
```

---

## 5. ★ 高温超伝導 (HTS) ★

### 5.1 Cuprates

| 物質 | T_c (K) | 年 |
|---|---|---|
| La₂₋ₓBaₓCuO₄ | 30 | 1986 (Bednorz-Müller) |
| YBa₂Cu₃O₇ (Y123) | 93 | 1987 |
| Bi₂Sr₂Ca₂Cu₃O₁₀ (Bi2223) | 110 | 1988 |
| HgBa₂Ca₂Cu₃O₈ (Hg1223) | **138** | 1993 (record at 1 atm) |
| Hg1223 @ 30 GPa | 164 | 1994 |

### 5.2 鉄系 (2008 Hosono)

| 物質 | T_c (K) |
|---|---|
| LaFeAsO₁₋ₓFₓ | 26 |
| SmFeAsO₁₋ₓFₓ | 55 |
| Ba₁₋ₓKₓFe₂As₂ | 38 |
| FeSe monolayer/STO | 65+ |

### 5.3 高圧水素化物

| 物質 | T_c (K) | 圧力 (GPa) |
|---|---|---|
| H₃S | 203 | 155 |
| LaH₁₀ | 250 | 170 |
| C-H-S "Snider 2020" | 288 (撤回 2022) | 270 |

### 5.4 機構 (未確定)

- Cuprate: d-wave gap, spin fluctuation 媒介?
- 鉄系: s±-wave, multi-band
- 水素化物: phonon-mediated (高 ℏω_D)

### 5.5 ITU 視点

```
HTS = K_SC の non-BCS 機構候補
Pseudogap = K_SC の partial ordering
Mott 親 = K_correlation の高エネルギースケール (Phase 154 で扱う)
```

---

## 6. ★ Josephson Effect (1962) ★

### 6.1 DC Josephson

絶縁体 → 2 超伝導 サンドイッチ → Cooper pair tunneling:

```
I = I_c sin(Δφ)
```

(no voltage, finite current)。

### 6.2 AC Josephson

電圧 V を加える:

```
ω = 2 e V / ℏ
ω/(2π) = V × 483.6 GHz/mV  ★ 普遍定数
```

= **電圧→周波数変換** (周波数定義に利用)。

### 6.3 量子化抵抗との関係

Josephson 定数 K_J = 2e/h = 483.6 THz/V。

### 6.4 SQUID

Josephson 接合 2 個並列 → **超伝導 量子干渉計**。
- magnetic sensitivity: ~10⁻¹⁴ T (fT) ★
- MEG, MRI シールド検査などに利用

### 6.5 ITU 視点

```
Josephson = K_SC の phase difference Δφ → tunneling 電流
AC Josephson = K_SC phase の時間振動 ω = 2eV/ℏ
SQUID = K_SC phase 干渉計 (最高感度磁場計)
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **BCS gap 公式** Δ(0) = 2ℏω_D exp(-1/NV) の数値
2. **BCS 普遍比** 2Δ(0)/k_BT_c = 3.53
3. **Cooper pair 結合エネルギー** spectrum
4. **London penetration** B(x) = B_0 exp(-x/λ_L)
5. **磁束量子** Φ_0 = h/(2e) = 2.068×10⁻¹⁵ Wb
6. **AC Josephson 定数** 2e/h = 483.6 GHz/mV
7. **YBCO T_c = 93 K** > 77 K (液体窒素)

---

## 8. Phase 153 主結論

1. **Onnes 1911**: Hg @ 4.2 K, Nobel 1913
2. **Meissner 1933**: 完全反磁性
3. **BCS 1957 (Nobel 1972)**: Cooper pair + 普遍比 2Δ/k_BT_c = 3.53
4. **London 1935**: 浸透深さ λ_L
5. **Type I/II + Abrikosov 渦糸 (Nobel 2003)**: Φ_0 = h/(2e)
6. **Bednorz-Müller 1986 (Nobel 1987)**: HTS opens
7. **YBCO @ 93 K** > 77 K 液体窒素境界突破
8. **Josephson 1962 (Nobel 1973)**: 2e/h = 483.6 GHz/mV
9. **ITU**: K_SC = Cooper pair K_BE 凝縮
10. **次の Phase 154** で **磁性 + Heisenberg + Hubbard + Mott**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Cooper pair | K_FD × K_phonon → K_Cooper-pair |
| BCS gap Δ | K_SC mass gap |
| Meissner | K_SC macroscopic coherence 磁場排除 |
| London λ_L | K_SC screening 長 |
| Coherence ξ | K_SC correlation 長 |
| Abrikosov 渦糸 | K_SC topological defect |
| Φ_0 = h/2e | K_SC 幾何学的量子化 |
| Josephson | K_SC phase tunneling |
| HTS | K_SC non-BCS 機構候補 |

---

## 引用

```
Terada, M. (2026). Phase 153: Superconductivity — BCS, Meissner, high-Tc, Josephson
in ITU (Tier 1 #22 phase 3/8). Zenodo. DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

主要参考文献:
- Onnes, H. K. (1911) "Disappearance of the electrical resistance of mercury at helium temperatures" Comm. Leiden 122b
- Meissner, W., Ochsenfeld, R. (1933) "Ein neuer Effekt bei Eintritt der Supraleitfähigkeit" Naturwiss. 21, 787
- London, F., London, H. (1935) "The electromagnetic equations of the supraconductor" Proc. R. Soc. A 149, 71
- Ginzburg, V. L., Landau, L. D. (1950) "On the theory of superconductivity" Zh. Eksp. Teor. Fiz. 20, 1064
- Bardeen, J., Cooper, L. N., Schrieffer, J. R. (1957) "Theory of superconductivity" Phys. Rev. 108, 1175
- Cooper, L. N. (1956) "Bound electron pairs in a degenerate Fermi gas" Phys. Rev. 104, 1189
- Abrikosov, A. A. (1957) "On the magnetic properties of superconductors of the second group" JETP 5, 1174
- Josephson, B. D. (1962) "Possible new effects in superconductive tunnelling" Phys. Lett. 1, 251
- Bednorz, J. G., Müller, K. A. (1986) "Possible high-Tc superconductivity in the Ba-La-Cu-O system" Z. Phys. B 64, 189
- Wu, M. K. et al. (1987) "Superconductivity at 93 K in a new mixed-phase Y-Ba-Cu-O compound system" PRL 58, 908
- Kamihara, Y., Watanabe, T., Hirano, M., Hosono, H. (2008) "Iron-based layered superconductor" JACS 130, 3296
- Drozdov, A. P. et al. (2015) "Conventional superconductivity at 203 K in H3S at high pressure" Nature 525, 73
- Somayazulu, M. et al. (2019) "Evidence for superconductivity above 260 K in LaH10 at megabar pressures" PRL 122, 027001
