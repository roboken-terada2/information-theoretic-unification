# Phase 178: Tensor Networks + MPS + MERA + HaPPY 符号 + K_tensor

> **Tier 1 #25 Information Geometry & Holography — Phase 4/8 (Block A paper 9/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 178 の目的

Phase 175-177 で情報幾何 + holography + complexity。Phase 178 では **tensor networks** — 量子状態の幾何学的表現 + holography 接続:

1. **MPS (Matrix Product States)** + DMRG (1992)
2. **PEPS (Projected Entangled Pair States)** — 2D
3. **★ MERA (Vidal 2007) ★** — Multi-scale Entanglement Renormalization
4. **Swingle 2009**: MERA = AdS/CFT 離散版
5. **HaPPY code (2015)**: Pastawski-Yoshida-Harlow-Preskill
6. **Random tensor networks** (Hayden-Penington-Vasudevan 2016)
7. **Bulk reconstruction**
8. **ITU 視点**: K_tensor = K_info の geometric organization

中心テーゼ:

> **MERA tensor network = AdS/CFT bulk の離散実現**。
> Holographic codes (HaPPY) = boundary CFT → bulk quantum error correction code 構造。
> ITU 公理 δS = δ⟨K_geom⟩ が tensor network 上で離散的に成立。

---

## 1. ★ Tensor Networks 基本 ★

### 1.1 動機

N-qubit 状態 |ψ⟩ は dim 2^N の Hilbert 空間 — N=300 で 2^300 ≈ 10^90 (宇宙原子数より多い)。
**圧縮表現** が必要 → tensor networks。

### 1.2 一般形

```
|ψ⟩ = Σ T(s_1, ..., s_N) |s_1, ..., s_N⟩
```

T = network of low-rank tensors with bond dimension χ。

### 1.3 ITU 視点

```
K_tensor = K_info の geometric organization
bond dimension χ = entanglement budget
```

---

## 2. ★ MPS — Matrix Product States ★

### 2.1 形式

1D で:
```
|ψ⟩ = Σ_s Tr[A^{s_1} A^{s_2} ... A^{s_N}] |s_1...s_N⟩
```

A^s: D × D 行列 (bond dim D)。

### 2.2 DMRG (White 1992)

DMRG = MPS variational algorithm:
- 1D ground state を効率的に探す
- gapped Hamiltonian に最適
- TMD, Heisenberg chain で indispensable

### 2.3 Area law

```
S_entanglement of [0, L] ≤ log D × (boundary size)
                       = log D × 2 (in 1D)
                       = const
```

= **gapped 1D ground state は area law を満たす** → MPS で表現可能 (Hastings 2007)。

### 2.4 ITU 視点

```
MPS = K_info の 1D area-law 状態 efficient representation
```

---

## 3. ★ PEPS — 2D Tensor Networks ★

### 3.1 形式

2D 平面格子上の tensor network:
```
|ψ⟩ = network of T tensors with 4 bond legs (square lattice)
```

### 3.2 物理応用

- 2D 量子磁性体 (Phase 154 接続)
- Topological order
- フラストレーション系
- 2D 強相関電子系

### 3.3 ITU 視点

```
PEPS = K_info の 2D area-law geometric representation
```

---

## 4. ★ MERA — Multi-scale ERA (Vidal 2007) ★

### 4.1 形式

**多重スケール** tensor network:
- 各層が renormalization step
- isometry + disentangler tensor types
- **log N 層** for N-site system

### 4.2 性質

- **logarithmic entanglement entropy**: S ∝ log L (critical CFT に対応 ✓)
- Critical point + scale-invariant systems に最適
- 1+1D Ising (Phase 145, 170) で正確

### 4.3 ★ Swingle 2009 — Holographic Interpretation ★

```
MERA causal cone = AdS_3 spacelike geodesic
MERA additional dimension (scale) = AdS bulk dimension
```

⇒ **MERA = AdS/CFT の離散実現** (Swingle 2009, breakthrough)。

### 4.4 ITU 視点

```
MERA = K_info の hierarchical RG structure
Swingle = K_tensor ↔ K_geom AdS bulk
```

---

## 5. ★ HaPPY Code (2015) ★

### 5.1 主張 (Pastawski-Yoshida-Harlow-Preskill)

Hyperbolic tessellation (pentagonal tiling) tensor network:
```
Bulk logical qubits → boundary physical qubits
= 量子誤り訂正 符号 (QECC) embedded in holography
```

### 5.2 性質

- **Holographic principle 具現化**
- RT formula (Phase 176) を tensor network で実証
- Bulk reconstruction = QECC decoding

### 5.3 ITU 視点

```
HaPPY code = K_info + K_holo + QECC unified
Bulk = boundary の quantum error-correcting redundant encoding
```

---

## 6. ★ Random Tensor Networks (2016) ★

### 6.1 主張 (Hayden-Penington-Vasudevan)

Random unitary tensors → AdS/CFT 多くの性質を生成:
- RT formula
- Bulk reconstruction
- Page curve

### 6.2 帰結

```
Holography = 何らかの random-like tensor network structure
特定の物理理論 (string, M) でなくとも 一般的に成立
```

### 6.3 ITU 視点

```
Random tensor networks = K_holo の universality
ITU 公理 = どんな K_tensor でも成立 (universal)
```

---

## 7. ★ Bulk Reconstruction ★

### 7.1 主張

Bulk operator O(x_bulk) を boundary operators の和で再構成:
```
O_bulk = Σ_A (operator on A) ψ_A
```

### 7.2 entanglement wedge reconstruction

Quantum error correction 言語:
```
bulk operator code subspace ↔ boundary entanglement wedge
```

→ **AdS/CFT = QECC**。

### 7.3 ITU 視点

```
Bulk reconstruction = K_geom (bulk) ← K_info (boundary) hologram
QECC = K_info redundant encoding
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **MPS Ising ground state** (small N)
2. **MERA log entanglement** S ∝ log L
3. **HaPPY hexagonal tessellation** schematic
4. **Bond dimension scaling** vs entanglement
5. **Random tensor network** RT verification

---

## 9. Phase 178 主結論

1. **Tensor networks**: 量子状態 efficient representation
2. **MPS** (1D, gapped): area-law (Hastings 2007)
3. **DMRG (1992)**: 1D ground state variational
4. **PEPS** (2D): area-law in 2D
5. **MERA (Vidal 2007)**: log-entanglement, critical
6. **Swingle (2009)**: MERA = AdS/CFT 離散
7. **HaPPY (2015)**: hyperbolic QECC, RT 具現化
8. **Random tensor networks (2016)**: holography universal
9. **Bulk reconstruction = QECC decoding**
10. **ITU**: K_tensor = K_info hierarchical organization
11. **次の Phase 179** で **ER=EPR + wormholes**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Tensor networks | K_info geometric structure |
| MPS / DMRG | K_info 1D area-law efficient |
| PEPS | K_info 2D area-law |
| MERA | K_info hierarchical RG |
| Swingle holographic | K_tensor ↔ K_geom AdS |
| HaPPY code | K_info + K_holo + QECC |
| Random tensors | K_holo universality |
| Bulk reconstruction | K_geom ← K_info QECC |

---

## 引用

```
Terada, M. (2026). Phase 178: Tensor networks — MPS, MERA, HaPPY code, and
holographic interpretations in ITU (Tier 1 #25 phase 4/8). Zenodo.
DOI: 10.5281/zenodo.20253960.
```

主要参考文献:
- White, S. R. (1992) "Density matrix formulation for quantum renormalization groups" PRL 69, 2863
- Östlund, S., Rommer, S. (1995) "Thermodynamic limit of density matrix renormalization" PRL 75, 3537
- Verstraete, F., Cirac, J. I. (2004) "Renormalization algorithms for quantum-many body systems in two and higher dimensions" arXiv:cond-mat/0407066
- Vidal, G. (2007) "Entanglement renormalization" PRL 99, 220405
- Vidal, G. (2008) "Class of quantum many-body states that can be efficiently simulated" PRL 101, 110501
- Swingle, B. (2012) "Entanglement renormalization and holography" PRD 86, 065007 (originally 2009)
- Hastings, M. B. (2007) "An area law for one-dimensional quantum systems" J. Stat. Mech. P08024
- Pastawski, F., Yoshida, B., Harlow, D., Preskill, J. (2015) "Holographic quantum error-correcting codes" JHEP 06, 149
- Hayden, P., Nezami, S., Qi, X. L., Thomas, N., Walter, M., Yang, Z. (2016) "Holographic duality from random tensor networks" JHEP 11, 009
- Almheiri, A., Dong, X., Harlow, D. (2015) "Bulk locality and quantum error correction in AdS/CFT" JHEP 04, 163
- Harlow, D. (2017) "The Ryu-Takayanagi formula from quantum error correction" Comm. Math. Phys. 354, 865
- Czech, B., Lamprou, L., McCandlish, S., Sully, J. (2015) "Integral geometry and holography" JHEP 10, 175
- Hauru, M., Delcamp, C., Mizera, S. (2018) "Renormalization of tensor networks using graph-independent local truncations" PRB 97, 045111
- Cirac, J. I., Pérez-García, D., Schuch, N., Verstraete, F. (2021) "Matrix product states and projected entangled pair states: Concepts, symmetries, theorems" Rev. Mod. Phys. 93, 045003
