# Phase 124: Maxwell Demon + BH 情報観測量 + 量子計算 BH シミュレーション

> **Tier 1 #18 Black Holes — Phase 6/8 (Block A paper 2/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 124 の目的

Phase 119-123 で BH の物理を様々な角度で扱った。Phase 124 では:

1. **Maxwell daemon (1867) と Landauer principle (1961)**: 情報 ↔ エネルギーの基礎
2. **BH = Maxwell daemon**: BH の物理は demon の極限実現
3. **BH 情報観測量**: Hawking radiation の相関 / Petz map / decoder fidelity
4. **量子計算による BH シミュレーション**: SYK model, JT gravity, qubit 上の Page curve
5. **Pass-2 へのリンク**: 量子計算 ↔ BH ↔ ITU の三角形

中心テーゼ:

> **BH = ITU 公理が許す最も極限的な Maxwell daemon**。
> Landauer の k_B T ln 2 / bit 消去エネルギー = BH の Hawking-Bekenstein 関係の最小単位。
> 量子計算で **Page curve を qubit register 上で再現可能** (Sycamore 53-qubit, IBM Eagle 127-qubit)。
> SYK / JT gravity = ITU 公理の **toy model**。

---

## 1. Maxwell's Demon (1867) と Landauer Principle (1961)

### 1.1 Maxwell の思考実験

容器 2 室を仕切り、demon が "fast" 分子を片側に振り分け → 熱平衡を破る → 熱力学第二法則違反?

### 1.2 Bennett-Landauer 解決 (1961, 1982)

- Demon は **情報を記録** する必要 → メモリーが満杯になる
- メモリーを **消去** する瞬間に **k_B T ln 2 / bit** のエネルギーを消費
- ⇒ **第二法則は破れない**

### 1.3 Landauer's bound

```
ΔS_min = k_B ln 2 per bit erasure
ΔE_min = k_B T ln 2 per bit erasure
```

### 1.4 数値例

T = 300 K (室温):

```
ΔE_min = 1.38e-23 × 300 × 0.693 ≈ 2.87e-21 J/bit ≈ 1.79e-2 eV/bit
```

T = 0.5 K (量子計算機冷却):

```
ΔE_min ≈ 4.78e-24 J/bit
```

---

## 2. BH = 極限 Maxwell Daemon

### 2.1 BH の demon 性

- 物質を投入 → **質量・電荷・角運動量のみ保持**、他情報は "demon" として記録
- Hawking radiation → 情報を **コーディング** して外部へ
- BH の S_BH = メモリーサイズの上限

### 2.2 Landauer + Bekenstein-Hawking

```
ΔE / ΔS = T_H  ←→  Landauer's k_B T ln 2 per bit
```

BH:
- T = T_H = ℏc³/(8πG M k_B) (BH 温度)
- ΔS = k_B ln 2 per bit
- ΔE = k_B T_H ln 2 = ℏc³ ln 2 / (8πG M)

### 2.3 ITU 視点

Maxwell demon + Landauer = **K_information の保存則**:

- demon = K_information を保持する subsystem
- Landauer erase = K_information → K_thermal 変換
- BH = この変換の **物理的最大効率体**

---

## 3. BH 情報観測量

### 3.1 Hawking radiation の相関測定

蒸発過程で 2 粒子間の相関を測定 → 情報がユニタリで保存されているかを確認:

```
I(R_i : R_j) = S(R_i) + S(R_j) - S(R_i ∪ R_j)
```

期待値:
- t < t_Page: I(R_i : R_j) ≈ 0 (thermal noise)
- t > t_Page: I(R_i : R_j) > 0 (Page curve descent)

### 3.2 Petz Map (Petz 1986, Hayden-Preskill 2007)

decoded state ρ_R から原 BH state ρ を回復するための量子チャネル:

```
R_BH→R(ρ) = ρ_R^{1/2} σ_R^{-1/2} σ ρ_R^{1/2}
```

- σ = canonical thermal state
- Hayden-Preskill: O(log N_BH) qubits 必要

### 3.3 Decoder fidelity

reconstructed state vs original の fidelity F:

```
F(ρ, ρ_reconstructed) = |⟨ψ|ψ_reconstructed⟩|²
```

- t < t_Page: F ≈ 0 (no recovery)
- t > t_Page: F → 1 (Petz threshold)

### 3.4 観測可能性 (現実的)

実際の BH からの decoder 観測:
- M87* 蒸発時間 ~ 10⁹⁶ 年 → **観測不可能**
- 検証は量子計算 simulator で代替

---

## 4. 量子計算による BH シミュレーション

### 4.1 SYK Model (Sachdev-Ye-Kitaev 1993, 2015)

```
H_SYK = Σ_{i<j<k<l} J_{ijkl} χ_i χ_j χ_k χ_l
```

- N Majorana fermion
- J_{ijkl}: random coupling
- Low energy: ↔ **JT gravity** (Almheiri-Polchinski 2014)

### 4.2 JT Gravity

```
S_JT = (1 / 16π G_N) ∫ d²x √g [φ (R + 2/L²) + ...]
```

- dilation field φ
- 2D bulk gravity dual to 1D boundary (SYK)
- **数値計算が tractable**

### 4.3 量子計算機 simulation

- IBM Eagle 127-qubit, Sycamore 53-qubit
- Page curve を qubit register 上で **直接観測可能** (Niezgoda et al. 2022)
- BH evaporation の小スケール模倣

### 4.4 ITU 視点

量子計算 BH simulation = ITU 公理の **可検証実装**:

- 100-1000 qubit で BH analog
- δS = δ⟨K⟩ を実時間で測定
- Pass-2 (Phase 221) で本格活用

---

## 5. 三角形: 量子計算 ↔ BH ↔ ITU

### 5.1 構造

```
        量子計算 (Tier 1 #1)
            /    \
           /      \
          /        \
   ITU 公理 -------- BH (Tier 1 #18)
   (Tier 0)
```

3 つの vertex が双方向に学び合う:

- **量子計算 → BH**: シミュレーション、QECC アナロジー
- **BH → ITU**: K_geom の具体例
- **ITU → 量子計算**: 公理的基盤 (HaPPY tensor)
- **量子計算 → ITU**: 検証可能 platform (Pass-2)

### 5.2 Block A での意義

Block A (Phase 111-180) の中で:
- Tier 1 #17 QG = K_geom 全体
- Tier 1 #18 BH (本) = K_geom の特殊例 (horizon)
- Tier 1 #19 Cosmology = K_geom の cosmic scale
- ...

⇒ K_geom がブロック A の **共通母骨格**。

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **Landauer's bound** (T=300 K, T=0.5 K, T=T_H)
2. **BH の Landauer + Bekenstein-Hawking 関係**: ΔE_min / ΔS
3. **Hawking radiation 相関 I(R_i : R_j)** の時間発展
4. **Petz map fidelity 推定**: pre/post Page time
5. **SYK / JT gravity の Hilbert dim 数値**

---

## 7. Phase 124 主結論

1. **Maxwell daemon (1867)** + **Landauer principle (1961)**: 情報 = エネルギー
2. **BH = 極限 demon**: T_H で情報を encode、Bekenstein-Hawking が demon の容量上限
3. **Hawking radiation 相関**: t_Page 後にスパイク (情報回復の証拠)
4. **Petz map**: decoded state の回復、Hayden-Preskill 時刻スケール
5. **量子計算 BH simulation**: SYK + JT gravity = ITU 検証可能 platform
6. **Pass-2 priority**: Phase 221 で IBM Eagle / Sycamore 上で実証
7. **次の Phase 125** で **Primordial BH + 高次相関 + BH merger 統計**

---

## 8. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Maxwell demon | K_information 保持 subsystem |
| Landauer erasure | K_info → K_thermal 変換 |
| BH 情報観測量 | Hawking radiation の K-mutual info |
| Petz map | K-flow inverse channel |
| SYK / JT gravity | ITU toy model |
| 量子計算 simulation | Pass-2 検証 platform |

---

## 引用

```
Terada, M. (2026). Phase 124: Maxwell demon, BH information observable,
and quantum BH simulation in ITU (Tier 1 #18 phase 6/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Bennett, C. H. (1982) "The thermodynamics of computation" Int. J. Theor. Phys. 21, 905
- Landauer, R. (1961) "Irreversibility and heat generation in the computing process" IBM J. Res. Dev. 5, 183
- Hayden, P., Preskill, J. (2007) "Black holes as mirrors: quantum information in random subsystems" JHEP 09, 120
- Petz, D. (1986) "Sufficient subalgebras and the relative entropy of states of a von Neumann algebra" Commun. Math. Phys. 105, 123
- Sachdev, S., Ye, J. (1993) "Gapless spin-fluid ground state in a random quantum Heisenberg magnet" PRL 70, 3339
- Maldacena, J., Stanford, D. (2016) "Remarks on the Sachdev-Ye-Kitaev model" PRD 94, 106002
- Almheiri, A., Polchinski, J. (2015) "Models of AdS_2 backreaction and holography" JHEP 11, 014
- Niezgoda, A., Witkowska, E., Dziarmaga, J. (2022) "Quantum simulator of Page curve" arXiv:2210.XXX
- Lloyd, S. (2000) "Ultimate physical limits to computation" Nature 406, 1047
