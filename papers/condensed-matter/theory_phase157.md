# Phase 157: ソフトマター — 液晶 + コロイド + 高分子 + 自己組織化 + K_soft

> **Tier 1 #22 Condensed Matter Physics — Phase 7/8 (Block A paper 6/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 157 の目的

Phase 151-156 で固体物理 (結晶 + 半導体 + 超伝導 + 磁性 + topology + 強相関) を扱った。Phase 157 では **ソフトマター** — 結晶と液体の **中間状態** — へ:

1. **液晶 (liquid crystals)** — Nematic, smectic, cholesteric
2. **コロイド (colloids)** — DLVO, Brownian, glass 転移
3. **高分子 (polymers)** — Flory, scaling, ゴム弾性
4. **自己組織化** — Lipid bilayer, micelle, vesicle, DNA
5. **生体ソフトマター** — 細胞膜, タンパク質 folding
6. **Glass 転移** + 非晶質固体
7. **ITU 視点**: K_soft = K_stat の **partial-order** 中間状態

中心テーゼ:

> **ソフトマター = K_order の partial / orientation-only / topological order**。
> 液晶 = K_orientation のみ (位置は液体的)。
> 高分子 = K_chain の長距離 connectivity。
> 自己組織化 = K_amphiphile の minimum free energy 構造。

---

## 1. ★ 液晶 (Liquid Crystals) ★

### 1.1 主要相

| 相 | 秩序 | 例 |
|---|---|---|
| Isotropic 液体 | 無 | 高温液体 |
| **Nematic** | 配向のみ | 5CB, PAA |
| **Smectic-A** | 配向 + 1D 位置 (層) | 5CB cooled |
| **Smectic-C** | 配向 (傾) + 層 | 強誘電液晶 |
| **Cholesteric** | helical nematic | DNA, コレステロール |
| **Discotic** | 円板分子 | hexa-substituted benzenes |

### 1.2 Nematic order parameter

```
S = ⟨(3 cos²θ - 1)/2⟩

S = 0:   isotropic
S = 1:   完全配向
S ≈ 0.5-0.7: 通常 nematic
```

### 1.3 PAA (p-azoxyanisole) 数値

```
T_NI = 408 K (nematic→isotropic)
S at T = 380 K: ≈ 0.6
```

### 1.4 ★ Maier-Saupe 平均場理論 (1958) ★

```
F(S) = (1/2) U_0 S² × n - k_B T ln Z(S)
```

→ S(T) の自己無撞着解。Curie-Weiss 類似。

### 1.5 液晶ディスプレイ (LCD)

電場で nematic 配向制御 → 偏光 透過率 変化 (Sharp 1972, Schadt-Helfrich TN 1972)。

### 1.6 ITU 視点

```
Liquid crystal = K_orientation only (K_position absent)
Maier-Saupe = K_orientation mean-field
LCD = K_orientation electrical control
```

---

## 2. ★ コロイド (Colloids) ★

### 2.1 定義

```
コロイド粒子: 1 nm - 1 μm
分散媒: 通常 液体
```

例: 牛乳, 血液, ペンキ, 煙。

### 2.2 ★ DLVO 理論 (1940年代) ★

コロイド間相互作用:

```
U_total = U_vdW + U_electric

U_vdW = -A H / (12 π r²)   (Hamaker)
U_electric = κ exp(-r/λ_D)   (screened Coulomb)
λ_D: Debye length
```

### 2.3 Debye length

```
λ_D = √(ε k_B T / (Σ n_i z_i² e²))
```

| 溶液 | λ_D |
|---|---|
| 純水 | ~1 μm |
| 10 mM NaCl | 3 nm |
| 100 mM NaCl | 1 nm |
| 生理食塩水 (150 mM) | 0.8 nm |

### 2.4 Stokes-Einstein

```
D = k_B T / (6 π η R)
```

= Phase 146 Brown 運動の core 公式。

### 2.5 Colloidal glass / gel

高 volume fraction φ:

```
φ_glass ≈ 0.58 (hard sphere)
φ_RCP (random close packing) ≈ 0.64
φ_FCC max ≈ 0.74
```

### 2.6 ITU 視点

```
Colloid = K_meso particle in K_solvent
DLVO = K_attractive vdW + K_repulsive screened-Coulomb
Glass = K_amorphous frozen K-state
```

---

## 3. ★ 高分子 (Polymers) ★

### 3.1 自由連結鎖 (Freely jointed chain)

N monomers, segment length b:

```
⟨R²⟩ = N b²
R_g (gyration radius) = b √(N/6)
```

### 3.2 ★ Flory 理論 ★

Self-avoiding walk (SAW) in d 次元:

```
⟨R²⟩^(1/2) ∝ N^ν
ν = 3 / (d + 2)   (Flory)
```

| 次元 d | Flory ν | 実際 |
|---|---|---|
| 1 | 1.0 | 1.0 |
| 2 | 0.75 | 0.75 (exact) |
| 3 | 0.60 | **0.588** |
| 4 | 0.5 | 0.5 (upper critical) |

### 3.3 ★ Reptation theory (de Gennes 1971, Nobel 1991) ★

絡まった高分子の拡散:

```
D_chain ∝ N^{-2}   (Doi-Edwards)
τ_rep ∝ N^3        (relaxation time)
```

### 3.4 ゴム弾性 (Gaussian network)

```
F = (1/2) ν k_B T (λ² + 1/λ² + ...)
```

ν: cross-link density。室温で操作可能 (T-依存 stress!)。

### 3.5 ITU 視点

```
Polymer chain = K_chain の長距離 connectivity
Flory ν = K_chain の self-avoiding scaling
Reptation = K_chain の topological constraint dynamics
Rubber elasticity = K_chain entropic spring
```

---

## 4. ★ 自己組織化 ★

### 4.1 両親媒性分子

```
Hydrophilic head (親水) + hydrophobic tail (疎水)
```

水中で **CMC (critical micelle concentration)** 以上で micelle 形成。

### 4.2 主要 morphology

| 構造 | 例 |
|---|---|
| Micelle | SDS in water |
| Reverse micelle | Lecithin in oil |
| Bilayer | Lipid (細胞膜) |
| Vesicle (liposome) | Phospholipid in water |
| Hexagonal phase | Lyotropic liquid crystal |
| Cubic phase | High-symmetry |

### 4.3 細胞膜 (lipid bilayer)

```
厚さ: ~4 nm
組成: phospholipid + cholesterol + 蛋白質
弾性: bending κ ~ 10-50 k_B T, surface tension σ ~ 0
```

### 4.4 DNA double helix

```
直径: 2 nm
ピッチ: 3.4 nm (B-form)
persistence length: 50 nm (in saline)
```

### 4.5 蛋白質 folding

```
Native state: ΔG ≈ -10 to -50 k_B T (typical)
folding time: 1 ms - 1 s (typical)
Levinthal paradox: 10^100 conformations → funnel landscape
```

### 4.6 ITU 視点

```
Self-assembly = K_amphiphile minimum free energy
Lipid bilayer = K_membrane の topology + bending elastic
Protein folding = K_polymer の native attractor (Phase 149 K_complex)
```

---

## 5. ★ Glass 転移 ★

### 5.1 概念

液体を **急冷** → 結晶化を避けて非晶質固体に。

```
T_g (glass transition temperature): η ~ 10^13 poise (~10^12 Pa·s)
```

### 5.2 主要 glass

| 物質 | T_g (K) |
|---|---|
| 水 | 136 (vitreous ice) |
| Pyrex | 820 |
| 石英 SiO₂ | 1473 |
| ポリスチレン | 373 |
| メタクリル PMMA | 378 |

### 5.3 Vogel-Fulcher-Tammann

```
η(T) = η_0 exp(B / (T - T_0))
T_0: VFT temperature (理想 glass 温度)
```

### 5.4 Mode Coupling Theory (MCT)

```
α-relaxation time: τ_α ∝ |T - T_c^MCT|^{-γ}
γ ≈ 2.5 (3D hard sphere)
```

### 5.5 ITU 視点

```
Glass transition = K_stat の dynamical arrest
非晶質固体 = K_disordered solid frozen K-state
```

---

## 6. アクティブソフトマター (Phase 149 接続)

### 6.1 Active gels

細胞 cytoskeleton (actin + myosin): ATP 駆動 contractile gel。

### 6.2 細菌コロニー

E. coli swimming: Phase 149 Vicsek model の生物版。

### 6.3 ITU 視点

```
Active soft matter = K_soft + K_active (energy injection)
細胞 = K_amphiphile bilayer + K_polymer cytoskeleton + K_active motor
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Nematic order parameter S(T)** Maier-Saupe 計算
2. **DLVO potential** for charged colloids
3. **Debye length** vs salt concentration
4. **Flory ν** 1D/2D/3D 比較
5. **Self-avoiding walk** numerical (2D/3D)
6. **Stokes-Einstein** D = k_B T / (6πηR)
7. **Glass T_g** for various materials

---

## 8. Phase 157 主結論

1. **液晶**: Nematic / Smectic / Cholesteric / Discotic, S(T) Maier-Saupe
2. **コロイド**: DLVO (vdW + screened Coulomb), λ_D
3. **高分子**: Flory ν = 3/(d+2), 3D = 0.588
4. **Reptation (de Gennes Nobel 1991)**: D ∝ N⁻², τ ∝ N³
5. **自己組織化**: bilayer, vesicle, lipid 細胞膜 4 nm
6. **DNA**: 直径 2 nm, persistence 50 nm
7. **Glass**: T_g, VFT η ∝ exp(B/(T-T_0))
8. **ITU**: K_soft = partial-order K_stat
9. **次の Phase 158** で **Tier 1 #22 統合 + 22-vertex polytope**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Nematic order | K_orientation only |
| DLVO | K_attractive + K_repulsive |
| Flory polymer | K_chain self-avoiding |
| Reptation | K_chain topological constraint |
| Self-assembly | K_amphiphile free energy minimum |
| Lipid bilayer | K_membrane 2D fluid + bending |
| DNA | K_polymer with helical K_orientation |
| Protein folding | K_polymer native attractor |
| Glass transition | K_stat dynamical arrest |
| Active soft matter | K_soft + K_active |

---

## 引用

```
Terada, M. (2026). Phase 157: Soft matter — liquid crystals, colloids, polymers,
and self-assembly in ITU (Tier 1 #22 phase 7/8). Zenodo. DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

主要参考文献:
- de Gennes, P. G. (1974) The Physics of Liquid Crystals. Oxford UP.
- de Gennes, P. G. (1979) Scaling Concepts in Polymer Physics. Cornell UP.
- Maier, W., Saupe, A. (1958) "Eine einfache molekular-statistische Theorie..." Z. Naturforsch. 13a, 564
- Doi, M., Edwards, S. F. (1986) The Theory of Polymer Dynamics. Oxford UP.
- Flory, P. J. (1953) Principles of Polymer Chemistry. Cornell UP.
- Derjaguin, B. V., Landau, L. D. (1941); Verwey, E. J. W., Overbeek, J. Th. G. (1948) DLVO theory
- Israelachvili, J. (2011) Intermolecular and Surface Forces, 3rd ed. Academic Press.
- Singer, S. J., Nicolson, G. L. (1972) "The fluid mosaic model of the structure of cell membranes" Science 175, 720
- Watson, J. D., Crick, F. H. C. (1953) "Molecular structure of nucleic acids" Nature 171, 737
- Anfinsen, C. B. (1973) "Principles that govern the folding of protein chains" Science 181, 223 (Nobel 1972)
- Vogel, H. (1921); Fulcher, G. S. (1925); Tammann, G., Hesse, W. (1926) VFT equation
- Götze, W. (2009) Complex Dynamics of Glass-Forming Liquids: A Mode-Coupling Theory. Oxford UP.
- de Gennes, P. G. (1971) "Reptation of a polymer chain in the presence of fixed obstacles" J. Chem. Phys. 55, 572
