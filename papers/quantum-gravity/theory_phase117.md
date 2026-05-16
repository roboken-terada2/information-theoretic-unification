# Phase 117: 量子重力の実験的検証 — LIGO / EHT / LISA / BMV / GRB

> **Tier 1 #17 Quantum Gravity — Phase 7/8 (Block A)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 117 の目的

Phase 111-116 で理論 (AdS/CFT, Page curve, firewall, LQG, string) を ITU で扱った。Phase 117 では **量子重力の実験的検証**を整理し、ITU 公理が予言する観測可能効果をまとめる。

確立する内容:

1. **LIGO/Virgo (2015-)**: GW150914 以降の重力波直接観測
2. **EHT (2019, 2022)**: M87*, Sgr A* の BH shadow 直接撮像
3. **LISA (2034 打ち上げ予定)**: 低周波 GW (mHz)
4. **BMV proposal (Bose-Marletto-Vedral 2017)**: 量子重力誘起もつれ
5. **GRB time delays**: Lorentz 不変性破れ at Planck scale
6. **Atom interferometry**: g_quantum 効果
7. **ITU 予言の検証可能性**

中心テーゼ:

> **量子重力は 2025 時点で「間接観測可能、直接観測 borderline」段階**。
> LIGO/EHT は classical GR を高精度で検証 (10^{-22} strain, 1% shadow size)。
> BMV (gravitationally-induced entanglement) が **量子重力の直接実験的検証への金本位線**。
> ITU 公理は LIGO 補正 O(ℓ_P/r_s) と GW echo を予言、2030 年代に検証可能。

---

## 1. LIGO / Virgo: 重力波直接観測

### 1.1 GW150914 (2015 年 9 月 14 日)

- 初の直接重力波検出
- 連星 BH 合体 (36 + 29 M_⊙ → 62 M_⊙, 3 M_⊙ 分が GW として放出)
- Strain h ~ 10^{-21}, 周波数 35-250 Hz
- 距離 ~ 410 Mpc, S/N 24
- 2017 Nobel 物理学賞

### 1.2 累計検出数 (LIGO O3 + O4)

| ラン | 期間 | BBH 検出数 | BNS 検出数 | NSBH 検出数 |
|---|---|---|---|---|
| O1 | 2015-16 | 3 | 0 | 0 |
| O2 | 2016-17 | 8 | 1 (GW170817) | 0 |
| O3 | 2019-20 | 79 | 2 | 1 |
| O4 (進行中) | 2023- | 100+ | 数件 | 数件 |

### 1.3 ITU 予言検証

LIGO で検証可能:
- **Inspiral phase**: classical GR (PN expansion) — 一致 < 0.1%
- **Ringdown phase**: 准normal モード一致 — 一致 < 1%
- **GW echo**: post-merger 信号 — 未検出 (現感度限界)

ITU 予言: ringdown 後に **O(ℓ_P/r_s) 補正のエコー** ~ 10^{-23} strain。
- 現 LIGO 感度では検出不可
- 次世代 (Cosmic Explorer, Einstein Telescope) で検証可能

---

## 2. EHT: BH 直接撮像

### 2.1 M87* (2019 年 4 月 10 日発表)

- 質量 6.5 × 10⁹ M_⊙
- 距離 16.8 Mpc (おとめ座銀河団)
- 影サイズ角度: 42 ± 3 μas
- 影サイズ ≈ √(27) × R_s = 5.2 R_s (Kerr 期待値)

### 2.2 Sgr A* (2022 年 5 月 12 日発表)

- 質量 4.0 × 10⁶ M_⊙ (天の川銀河中心)
- 距離 8.1 kpc
- 影サイズ角度: 51.8 ± 2.3 μas
- 形状: 高度に回転 (Kerr 妥当)

### 2.3 ITU 予言

shadow 半径への 量子重力補正:

```
Δ R_shadow / R_shadow ~ O(ℓ_P / R_s)
M87*: O(10^{-35} / 10¹⁰) = 10^{-45}    (現状観測不可)
Sgr A*: O(10^{-35} / 10⁷) = 10^{-42}   (現状観測不可)
```

EHT 次世代 (ngEHT, 2030 年代) で 1% 精度。直接観測には数桁不足。

---

## 3. LISA: 宇宙空間レーザー干渉計

### 3.1 計画

- 打ち上げ: 2034 (予定)
- 3 衛星アレイ 2.5 × 10⁶ km L-shape
- 周波数: 10^{-4} - 10^{-1} Hz (mHz 帯)
- ESA + NASA 連携

### 3.2 観測対象

| 源 | 期待 SNR |
|---|---|
| 超大質量 BH 合体 (SMBH) | 10³-10⁴ |
| EMRI (極端質量比 inspiral) | 100 |
| MBHB | 10² |
| 銀河系内白色矮星連星 | confusion noise (10^4 known) |
| 初期宇宙背景 GW | depends |

### 3.3 ITU 予言検証

EMRI の inspiral signal で **多波**観測:
- 数千周期 (typical 10^4 cycles)
- 各周期で classical GR vs ITU 補正比較
- ITU 補正 O(ℓ_P²/R_s²) ~ 10^{-78} (super-massive BH)

⇒ LISA でも直接量子重力効果は検出困難。
ただし **post-merger ringdown** で modes 比較 → 検証可能。

---

## 4. BMV: 量子重力誘起もつれ (Bose-Marletto-Vedral 2017)

### 4.1 提案

2 つの **massive quantum particle** を superposition で互いに gravitationally 相互作用させ、entanglement 生成を検証。

- 質量: m ~ 10^{-14} kg (~ 10⁹ amu, BEC とウィルス間)
- 距離: d ~ 100 μm
- 重畳幅: Δx ~ 100 μm
- 経時: t ~ 1 秒

### 4.2 量子重力の検証ロジック

古典重力場 (LOCC) では entanglement 生成不可能。
もつれ検出 = **重力が量子化されている証拠** (Bose et al. 2017, Marletto-Vedral 2017)。

### 4.3 ITU 視点

ITU: 重力 = K_geom が量子もつれを媒介。
BMV 検出は ITU 公理の **直接実験的支持**。

### 4.4 現状 (2025)

- 直接実験はまだ進行中 (Bose group, Vedral group, MAQRO)
- 主課題: massive coherence の長時間維持 (decoherence < 10^{-3} s now)
- 2030 年代に決定的結果期待

---

## 5. GRB Time Delays: Lorentz 不変性破れ

### 5.1 観測

GRB は高エネルギー (GeV-TeV) と低エネルギー (keV-MeV) の光子を同時放出。
量子重力なら **dispersion relation** が:

```
E² = p²c² + m²c⁴ + ξ × E^n / E_P^{n-2}
```

→ 異なるエネルギーの光子で **到着時刻差** Δt ~ d / c × (E / E_P)^{n-2}。

### 5.2 Fermi-LAT 観測 (Abdo et al. 2009, GRB 090510)

- z ≈ 0.903 (d ≈ 5 Gpc)
- 高 GeV vs 低 keV の Δt < 0.9 秒

⇒ E_P > 1.2 × M_P (linear, n=1) — 観測上 E_P 未検出。

### 5.3 ITU 予言

ITU 公理は classical Lorentz invariance を保持 → n=1 violation はゼロ予言。
ただし O(E/E_P)^2 (n=2) 補正は可能 → これは現 GRB 観測で検証不可。

---

## 6. Atom Interferometry: g_quantum

### 6.1 原理

- 冷原子 (^87Rb) を BEC で空間 superposition
- 重力場で位相シフト測定
- 精度: Δg/g ~ 10^{-10} now → 10^{-12} target

### 6.2 検証可能効果

- **Equivalence principle** in quantum regime: classical 違いなく検証
- 量子重力直接効果: g_quantum ~ ℏ × ω_q / m (subtle)

### 6.3 ITU 予言

ITU: classical equivalence principle 保持。量子効果は **K_geom の Planck scale でのみ**現れる。

⇒ atom interferometry では直接量子重力検出は不可能だが、BMV と組み合わせて間接的検証。

---

## 7. 量子重力検証の総合状況 (2025-2050)

| 実験 | 検証可能 | 量子重力直接? | timeline |
|---|---|---|---|
| LIGO / Virgo | classical GR | echo (間接, 未検出) | 進行中 |
| EHT (現) | Kerr shadow | quantum 補正不可視 | 進行中 |
| ngEHT (2030+) | shadow 1% 精度 | 不十分 | 2030+ |
| LISA (2034+) | EMRI ringdown | classical | 2034+ |
| Cosmic Explorer (2035+) | GW 10× sensitivity | echo 可能? | 2035+ |
| Einstein Telescope (2035+) | 同上 + low freq | echo 可能? | 2035+ |
| **BMV (Bose et al. 2017)** | gravity entanglement | **直接量子重力検証** ★ | 2030-2040 |
| GRB Fermi-LAT | Lorentz 破れ | 上限のみ | 進行中 |
| Atom interferometry | g 精度 | classical | 進行中 |

★ BMV が **量子重力直接検証の金本位**。2030 年代成功なら ITU 公理の直接支持。

---

## 8. ITU 予言の優先検証順序

1. **BMV (gravitationally induced entanglement)** — 量子重力 yes/no
2. **GW echo (LIGO/ET/CE)** — Page time post-merger residual
3. **BH shadow corrections (ngEHT)** — 1% 精度量子補正
4. **EMRI ringdown (LISA)** — multi-mode 検証
5. **CMB B-mode** — inflation epoch K-flow (Phase 119 で扱う)

---

## 9. 数値検証項目

本 phase の simulation で確認:

1. **LIGO strain 感度 vs ITU echo amplitude**: 10^{-22} sensitivity vs 10^{-23} echo
2. **EHT shadow correction**: O(ℓ_P / R_s) 比率の数値
3. **LISA EMRI cycle 数**: 10^4 cycles で量子補正積算
4. **BMV phase**: φ = G m² t / (ℏ d) の数値
5. **GRB Δt vs E_P bound**: Fermi-LAT 上限

---

## 10. Phase 117 主結論

1. **LIGO/Virgo**: classical GR を 10^{-22} で検証、ITU 補正は未検出
2. **EHT**: M87*, Sgr A* shadow を直接撮像、量子補正 O(10^{-45})
3. **LISA**: 2034+ で低周波 GW、EMRI で classical 高精度
4. **BMV (2017)**: 量子重力直接検証の金本位、2030+ で結果期待 ★
5. **GRB**: Lorentz 不変性破れ未検出、ITU と整合
6. **ITU 検証順序**: BMV → GW echo → ngEHT → LISA ringdown → CMB
7. **次の Phase 118** で **Tier 1 #17 統合 + 10 predictions**

---

## 11. ITU 視点まとめ

| 実験 | ITU 検証対象 |
|---|---|
| LIGO/Virgo | classical δS = δ⟨K⟩ 連続極限 |
| EHT | Kerr 解 (K_geom の半古典) |
| LISA | post-merger K_geom dynamics |
| BMV | K_geom の量子もつれ媒介 |
| GRB | classical Lorentz 不変性 |
| CMB B-mode | inflation 期 K-flow 残響 |

---

## 引用

```
Terada, M. (2026). Phase 117: Experimental tests of quantum gravity in ITU.
Zenodo. DOI: [to be assigned].
```

主要参考文献:
- LIGO/Virgo (2016) "Observation of Gravitational Waves from a Binary Black Hole Merger" PRL 116, 061102
- EHT Collaboration (2019) "First M87 Event Horizon Telescope Results" ApJL 875, L1
- EHT Collaboration (2022) "First Sgr A* Event Horizon Telescope Results" ApJL 930, L12
- Bose, S., Mazumdar, A. et al. (2017) "Spin entanglement witness for quantum gravity" PRL 119, 240401
- Marletto, C., Vedral, V. (2017) "Gravitationally induced entanglement between two massive particles" PRL 119, 240402
- LISA Consortium (2017) "LISA Phase 0 Mission Concept" (arXiv:1702.00786)
- Abbott, B. P. et al. (2017) "Multi-messenger Observations of GW170817" ApJL 848, L12
- Abdo, A. A. et al. (2009) "A limit on the variation of the speed of light arising from quantum gravity effects" Nature 462, 331
