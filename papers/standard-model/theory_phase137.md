# Phase 137: Higgs Mechanism + 電弱対称性破れ (EWSB) + 階層問題 + K_Higgs

> **Tier 1 #20 Standard Model — Phase 3/8 (Block A paper 4/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 137 の目的

Phase 135 で SM gauge 群、Phase 136 で 3 世代 fermion + Yukawa を扱った。Phase 137 では **質量の起源** = Higgs Mechanism を扱う。

確立する内容:

1. **Higgs Mechanism (Englert-Brout 1964, Higgs 1964)**: spontaneous gauge symmetry breaking
2. **Mexican hat potential** V(φ) = -μ²|φ|² + λ|φ|⁴
3. **Higgs VEV**: v = 246 GeV
4. **Higgs boson 質量**: m_H = 125 GeV (LHC 2012, Nobel 2013)
5. **W/Z 質量**: M_W, M_Z 生成
6. **階層問題** (Higgs mass の量子補正)
7. **ITU 視点**: K_Higgs = symmetry-breaking K-state

中心テーゼ:

> **Higgs Mechanism = ITU の K_Higgs spontaneous symmetry breaking**。
> v = 246 GeV = 電弱 scale の **K_Higgs VEV**。
> m_H = 125 GeV = K_Higgs の Higgs boson mass scale。
> 階層問題 (m_H² が m_Pl² から ~ 10³⁴ 桁 small) = K_Higgs の **fine-tuning issue** = ITU の最大未解決問題の 1 つ。

---

## 1. Higgs Mechanism: Spontaneous Symmetry Breaking

### 1.1 Higgs Field

```
H = (φ⁺, φ⁰)^T  (SU(2)_L doublet, Y = 1)
```

複素 SU(2) doublet = **4 real degrees of freedom**。

### 1.2 Higgs Potential ("Mexican Hat")

```
V(H) = -μ² |H|² + λ |H|⁴
```

- μ² > 0: 真空が **|H|² = v²/2 ≠ 0** (negative term wins)
- λ > 0: 安定 (positive quartic)

最小値:

```
|H₀|² = v² / 2,  v = √(μ²/λ)
```

### 1.3 VEV

```
⟨0|H|0⟩ = (0, v/√2)^T
v ≈ 246 GeV  (observed)
```

これが **電弱対称性破れ (Electroweak Symmetry Breaking, EWSB)** の起源。

---

## 2. Goldstone Bosons → Gauge Boson Mass

### 2.1 Nambu-Goldstone 定理

continuous symmetry が破れると、**massless Goldstone boson** が出現。

破れた 3 generators (SU(2) × U(1) → U(1)_EM):

```
Broken: T_1, T_2, (T_3 - Y/2)  → 3 Goldstone bosons
Unbroken: T_3 + Y/2 = Q  → 1 massless (photon)
```

### 2.2 Higgs Mechanism (Goldstone → W/Z 質量)

gauge bosons "食べる" Goldstone bosons → **longitudinal polarization**:

```
W^± (transverse + longitudinal): massless → 3 dof × 3 → 9 dof (was)
   becomes massive: 3 dof × 3 = 9 (W: 3 dof × 2 + Z: 3 dof × 1)
```

数 chk:
- Before EWSB: 4 (Higgs doublet) + 4 × 3 (gauge bosons SU(2)+U(1)) = 16 dof
- After EWSB: 1 (Higgs boson) + 3 (W⁺) + 3 (W⁻) + 3 (Z) + 2 (photon) = 12 dof
- 差: 4 dof が **Higgs ↔ Goldstone** 移動 (3 W/Z + 1 H)

### 2.3 W/Z 質量

```
M_W = g v / 2 = 80.379 GeV
M_Z = √(g² + g'²) v / 2 = 91.188 GeV
cos θ_W = M_W / M_Z = 0.881  (Weinberg angle)
```

### 2.4 photon 質量

```
M_γ = 0  (U(1)_EM 残存対称性)
```

---

## 3. Higgs Boson 質量

### 3.1 Higgs Boson 発見 (LHC 2012, Nobel 2013)

- **m_H = 125.25 ± 0.17 GeV** (PDG 2024)
- ATLAS + CMS at LHC (2012-07-04)
- 2013 Nobel: Englert + Higgs (Brout 1928-2011 没後)

### 3.2 Lagrangian 質量項

```
V(H) = -μ² |H|² + λ |H|⁴
  → (around v): (1/2) m_H² h² + ...
  m_H² = 2 λ v² = 2 μ²
  m_H = √(2λ) × v
```

### 3.3 Self-coupling λ

```
λ = m_H² / (2 v²) = (125.25)² / (2 × 246²) ≈ 0.129
```

⇒ **λ ≈ 0.13** ← O(0.1)、O(1) 結合 (Yukawa top と同じくらい)。

---

## 4. 階層問題 (Hierarchy Problem) ★

### 4.1 自然性問題

m_H² の量子補正:

```
m_H² (physical) = m_H² (bare) + δm_H² (loop)
δm_H² ~ Λ²_UV / (16π²)  (quadratically divergent)
```

UV cutoff Λ_UV:
- New physics scale: Λ_UV ~ M_Planck ≈ 10¹⁹ GeV
- δm_H² ~ (10¹⁹)² / (16π²) ~ 10³⁵ GeV²

観測値:
- m_H² ~ (125 GeV)² ~ 10⁴ GeV²

⇒ **m_H² (bare) と δm_H² が ~ 10³¹ 桁で cancel** → **超 fine-tuning**!

### 4.2 解決候補

| 候補 | メカニズム |
|---|---|
| **Supersymmetry (SUSY)** | Boson-fermion 対称性で δm_H² が cancel |
| **Composite Higgs** | Higgs が composite (technicolor) |
| **Large Extra Dimensions** | M_Planck^eff が低い |
| **Anthropic** | Multiverse selection |
| **Naturalness 否定** | Hierarchy は深い意味なし |

### 4.3 LHC での SUSY 探索 (2024)

- gluino > 2.3 TeV (no signal)
- stop > 1.2 TeV
- chargino > 1 TeV
- ⇒ **Natural SUSY 排除気味**

### 4.4 ITU 視点

```
δK_Higgs² ~ Λ²_UV / (16π²)
ITU UV cutoff (Phase 114): f_ITU(ω/E_P) で抑制可能?
```

Pass-2 (Phase 224 予定) で ITU UV cutoff による階層問題解像を提案予定。

---

## 5. Higgs Couplings (LHC 観測)

### 5.1 観測モード

- **H → γγ** (LHC 発見モード)
- H → ZZ → 4ℓ
- H → WW → ℓνℓν
- H → bb̄ (Yukawa最大)
- H → ττ

### 5.2 Coupling 強度 (ATLAS+CMS 2022)

| Coupling | SM 予言 | 観測 (μ = obs/SM) |
|---|---|---|
| κ_W (HWW) | 1.0 | 1.05 ± 0.06 |
| κ_Z (HZZ) | 1.0 | 1.04 ± 0.07 |
| κ_t (Htt) | 1.0 | 0.94 ± 0.11 |
| κ_b (Hbb) | 1.0 | 0.91 ± 0.16 |
| κ_τ (Hττ) | 1.0 | 0.95 ± 0.09 |

⇒ **全 coupling が SM 予言 ±10% 内**で一致 = **Standard Higgs 確認**。

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **Mexican hat potential** V(φ) plot
2. **W, Z 質量 formula** verification: g v / 2 = 80.4 GeV
3. **Higgs self-coupling λ ≈ 0.129**
4. **階層問題 数値**: δm_H² / m_H² ~ 10³¹
5. **Higgs coupling κ** vs SM

---

## 7. Phase 137 主結論

1. **Higgs Mechanism (1964)**: spontaneous gauge symmetry breaking
2. **Mexican hat potential**: V = -μ²|H|² + λ|H|⁴
3. **VEV v = 246 GeV** (electroweak scale)
4. **Higgs boson m_H = 125.25 GeV** (LHC 2012, Nobel 2013)
5. **W/Z 質量**: M_W = gv/2, M_Z = √(g²+g'²) v/2
6. **Self-coupling λ ≈ 0.129** (O(0.1))
7. **階層問題**: δm_H² ~ 10³¹ × m_H² → fine-tuning
8. **Higgs coupling**: SM 予言と ±10% 内一致 (ATLAS+CMS 2022)
9. **次の Phase 138** で **QCD + confinement + asymptotic freedom 詳細**

---

## 8. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Higgs field H | K_Higgs scalar K-state |
| Higgs VEV v | K_Higgs spontaneous symmetry breaking |
| Mexican hat | K_Higgs effective potential |
| Higgs boson m_H | K_Higgs excitation mass |
| W/Z 質量 | K_gauge × K_Higgs interaction |
| 階層問題 | K_Higgs fine-tuning issue |
| LHC κ ≈ 1 | K_Higgs SM-like behavior |

---

## 引用

```
Terada, M. (2026). Phase 137: Higgs mechanism, EWSB, hierarchy problem,
and K_Higgs in ITU (Tier 1 #20 phase 3/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Englert, F., Brout, R. (1964) "Broken symmetry and the mass of gauge vector mesons" PRL 13, 321
- Higgs, P. W. (1964) "Broken symmetries and the masses of gauge bosons" PRL 13, 508
- Guralnik, G., Hagen, C., Kibble, T. (1964) "Global conservation laws and massless particles" PRL 13, 585
- Goldstone, J. (1961) "Field theories with superconductor solutions" Nuovo Cim. 19, 154
- ATLAS Collaboration (2012) "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC" PLB 716, 1
- CMS Collaboration (2012) "Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC" PLB 716, 30
- ATLAS+CMS (2022) "Combined measurements of Higgs boson properties" Nature 607, 60
- 't Hooft, G. (1980) "Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking" NATO Sci. Ser. B 59, 135
- Particle Data Group (2024) "Review of Particle Physics" PRD 110, 030001
