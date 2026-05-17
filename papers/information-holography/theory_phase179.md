# Phase 179: ER=EPR + Wormholes + 絡み合い構造 + K_wormhole

> **Tier 1 #25 Information Geometry & Holography — Phase 5/8 (Block A paper 9/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 179 の目的

Phase 175-178 で情報幾何 + holography + complexity + tensor networks。Phase 179 では **量子もつれと時空構造の同一視** = ER=EPR:

1. **Einstein-Rosen bridge (1935)** + **EPR paradox (1935)**
2. **★ Maldacena-Susskind ER=EPR (2013) ★**
3. **Thermofield double (TFD)** = 双方の eternal BH 量子状態
4. **Eternal black hole** 量子もつれ表現
5. **Traversable wormholes** (Gao-Jafferis-Wall 2017)
6. **Replica wormholes** (Penington 2020, AEMM 2019)
7. **SYK model** + Maldacena-Stanford 2016
8. **Wormhole 越し量子テレポート**
9. **ITU 視点**: K_wormhole = K_entangle × K_geom 同一視

中心テーゼ:

> **量子もつれ = 微小ワームホール構造** (Maldacena-Susskind 2013)。
> Eternal BH = TFD = boundary 系の最大もつれ状態。
> Traversable wormhole = もつれ + 二重 trace deformation で実現可能 (GJW 2017)。

---

## 1. ★ Einstein-Rosen Bridge (1935) ★

### 1.1 オリジナル

Einstein-Rosen 1935: Schwarzschild 解の最大解析的拡張 → 2 つの asymptotic region をつなぐ "bridge":

```
ds² = -f(r) dt² + f(r)^{-1} dr² + r² dΩ²
f(r) = 1 - 2GM/(rc²)
```

最大解析拡張 (Kruskal 1960) → **2 universe** つなぐ throat。

### 1.2 非伝統的性質

- **traversable でない** (光すら渡れない, classical GR)
- **時間と共に pinch off** する (Wheeler-Misner)
- 当初は数学的な curiosity

### 1.3 ITU 視点

```
ER bridge = K_geom の topological non-trivial structure
```

---

## 2. ★ EPR Paradox (1935) ★

### 2.1 主張

Einstein-Podolsky-Rosen 1935: 2 粒子もつれ状態:
```
|ψ⟩_EPR ∝ |↑↓⟩ - |↓↑⟩  (singlet)
```

= **片方の測定が瞬時に相手を決定** → "spooky action at a distance"。

### 2.2 Bell 1964 + 実験

Bell 不等式違反: Aspect 1982 → 量子非局所性 確立。

### 2.3 ITU 視点

```
EPR = K_quantum の非局所もつれ
Bell 違反 = K_quantum の classical 表現不能性
```

---

## 3. ★★ Maldacena-Susskind ER=EPR (2013) ★★

### 3.1 主張

**量子もつれ ↔ 微小ワームホール**:

```
2 separated quantum systems (EPR pair)
       ↔
geometric ER bridge between them
```

### 3.2 動機

- 2 つの eternal BH の TFD (Maldacena 2003)
- Firewall paradox 解決 (AMPS, Phase 114) の手がかり
- 量子重力 + AdS/CFT を unifying

### 3.3 帰結

```
全ての量子もつれ = 何らかの form of ER bridge
通常もつれ = 細い非走行性 wormhole
強もつれ = 走行可能性 (Phase 179.4)
```

### 3.4 ITU 視点

```
ER=EPR = K_entangle ≡ K_geom topological coupling
ITU: 2 つの異なる K-state が同一物理 ★
```

---

## 4. ★ Thermofield Double (TFD) ★

### 4.1 定義

熱状態を 2 系もつれで表現:
```
|TFD⟩ = (1/√Z) Σ_n e^{-βE_n/2} |n⟩_L ⊗ |n⟩_R
```

- Left/Right 系の最大絡み合い状態
- Tracing out 一方 → 熱状態 ρ = e^{-βH}/Z

### 4.2 Eternal BH との対応

Maldacena 2003: AdS-Schwarzschild eternal BH の boundary 双対状態 = TFD:
```
2 sides of BH (R-Rindler regions) ↔ Left/Right boundary CFT
geometric connection (ER bridge) = TFD entanglement
```

### 4.3 数値例

```
β = 1/T_Hawking
|TFD⟩ entanglement entropy ≈ S_BH (Bekenstein-Hawking, Phase 122)
```

### 4.4 ITU 視点

```
TFD = K_entangle thermal double
Eternal BH = K_horizon + K_entangle 同一視
```

---

## 5. ★ Traversable Wormholes (Gao-Jafferis-Wall 2017) ★

### 5.1 主張

通常 ER bridge は **traversable でない** (null energy condition)。
GJW (2017): **2 boundary 間の double trace deformation** で wormhole が **走行可能** に:

```
δS = g O_L(t) O_R(t)   (deformation)
```

### 5.2 物理

量子もつれを使った "non-local" trick で時空が "thinner" になり光が通る。

### 5.3 量子テレポート

```
2 boundary 系の量子テレポート プロトコル
= 走行可能 wormhole 越しの particle 送信
```

### 5.4 ITU 視点

```
Traversable wormhole = K_geom + K_entangle 強結合
Quantum teleport = K_entangle 媒介 K_geom 走行
```

---

## 6. ★ Replica Wormholes (2019-2020) ★

### 6.1 主張

BH 蒸発の Page curve (Phase 113, 124) を **gravitational path integral** で導出:
```
Z_n = sum over geometries
    = connected (replica) + disconnected
```

Replica wormhole が connected geometry を提供 → Page curve unitarity。

### 6.2 重要論文

- AEMM (2019): Almheiri-Engelhardt-Marolf-Maxfield
- Penington (2019/2020): replica wormhole + island
- AEMS (2020): Almheiri-Engelhardt-Marolf-Stanford

### 6.3 数値

```
disconnected: S(t) → S_BH (information loss)
+ connected (wormhole): S(t) → Page curve ✓
```

= **量子重力で unitarity 保存 demonstrate**。

### 6.4 ITU 視点

```
Replica wormholes = K_geom non-perturbative quantum gravity correction
Page curve from replica = K_holo unitarity
```

---

## 7. SYK Model (Sachdev-Ye-Kitaev)

### 7.1 ハミルトニアン

```
H = Σ_{i<j<k<l} J_{ijkl} χ_i χ_j χ_k χ_l
```

N Majorana fermion + 4-body random interaction。

### 7.2 性質

- **Maximally chaotic** (λ_L = 2π/β, Maldacena-Stanford 2016)
- 1D gravity (JT) dual (Kitaev 2015)
- BH 物理 simulate 可能

### 7.3 ITU 視点

```
SYK = K_holo の minimal lattice realisation
JT gravity dual = K_geom dimensionally-reduced
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **TFD state** entanglement entropy = log Z (2-state model)
2. **Page curve** with island + replica wormhole
3. **SYK λ_L** = 2π/β maximally chaotic
4. **GJW wormhole** schematic
5. **EPR singlet** entanglement S = log 2

---

## 9. Phase 179 主結論

1. **ER bridge (1935)** + **EPR (1935)**: 別物 (当初)
2. **★ ER=EPR (Maldacena-Susskind 2013) ★**: 同一物理の 2 視点
3. **TFD = eternal BH dual** (Maldacena 2003)
4. **Traversable wormhole** (GJW 2017): double trace deformation
5. **Replica wormholes (2019-2020)**: Page curve unitarity ✓
6. **SYK + JT gravity**: maximally chaotic 1D
7. **Quantum teleportation via wormhole**
8. **ITU**: K_wormhole = K_entangle × K_geom 同一視
9. **次の Phase 180** で **Wheeler "it from bit" + ITU 公理厳密化**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| ER bridge | K_geom topological non-trivial |
| EPR | K_quantum 非局所もつれ |
| **ER=EPR** | **K_entangle ≡ K_geom (Maldacena-Susskind 2013)** |
| TFD | K_entangle thermal double |
| Eternal BH | K_horizon + K_entangle 同一 |
| Traversable wormhole | K_geom + K_entangle 強結合 |
| Replica wormholes | K_geom non-perturbative |
| Page curve from replica | K_holo unitarity (Phase 113 接続) |
| SYK + JT | K_holo minimal realization |

---

## 引用

```
Terada, M. (2026). Phase 179: ER=EPR — wormholes, thermofield double, traversable
wormholes, replica wormholes in ITU (Tier 1 #25 phase 5/8). Zenodo.
DOI: 10.5281/zenodo.20253960.
```

主要参考文献:
- Einstein, A., Rosen, N. (1935) "The particle problem in the general theory of relativity" Phys. Rev. 48, 73
- Einstein, A., Podolsky, B., Rosen, N. (1935) "Can quantum-mechanical description of physical reality be considered complete?" Phys. Rev. 47, 777
- Bell, J. S. (1964) "On the Einstein-Podolsky-Rosen paradox" Physics 1, 195
- Aspect, A., Grangier, P., Roger, G. (1982) "Experimental realization of Einstein-Podolsky-Rosen-Bohm gedankenexperiment" PRL 49, 91
- Maldacena, J. (2003) "Eternal black holes in anti-de Sitter" JHEP 04, 021
- Maldacena, J., Susskind, L. (2013) "Cool horizons for entangled black holes" Fortsch. Phys. 61, 781
- Gao, P., Jafferis, D. L., Wall, A. C. (2017) "Traversable wormholes via a double trace deformation" JHEP 12, 151
- Penington, G. (2020) "Entanglement wedge reconstruction and the information paradox" JHEP 09, 002
- Almheiri, A., Engelhardt, N., Marolf, D., Maxfield, H. (2019) "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole" JHEP 12, 063
- Almheiri, A., Hartman, T., Maldacena, J., Shaghoulian, E., Tajdini, A. (2020) "Replica wormholes and the entropy of Hawking radiation" JHEP 05, 013
- Penington, G., Shenker, S. H., Stanford, D., Yang, Z. (2022) "Replica wormholes and the black hole interior" JHEP 03, 205
- Sachdev, S., Ye, J. (1993) "Gapless spin-fluid ground state in a random quantum Heisenberg magnet" PRL 70, 3339
- Kitaev, A. (2015) talks at KITP (SYK model)
- Maldacena, J., Stanford, D. (2016) "Remarks on the Sachdev-Ye-Kitaev model" PRD 94, 106002
- Maldacena, J., Qi, X.-L. (2018) "Eternal traversable wormhole" arXiv:1804.00491
