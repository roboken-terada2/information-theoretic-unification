# Phase 160: 乱流 — Kolmogorov 1941 + エネルギーカスケード + Universality

> **Tier 1 #23 Fluid Dynamics — Phase 2/8 (Block A paper 7/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 160 の目的

Phase 159 で Reynolds 数 が Re ≳ 4000 で **乱流** に突入することを見た。Phase 160 では乱流の **普遍構造** に進む:

1. **Kolmogorov 1941 (K41) 理論**: -5/3 法則
2. **エネルギーカスケード** (Richardson 1922)
3. **Kolmogorov microscale** η = (ν³/ε)^(1/4)
4. **2D vs 3D 乱流** (Kraichnan 1967 dual cascade)
5. **Intermittency と anomalous scaling**
6. **ITU 視点**: K_turbulence = K_flow at high Re, universal RG fixed point

中心テーゼ:

> **K41 -5/3 法則 = ITU K_flow の universal RG fixed point**。
> Energy cascade = K_flow の scale-by-scale K-state transfer。
> 慣性領域 = K_flow の scale-invariant attractor (Phase 145, 149 SOC 接続)。

---

## 1. 乱流の歴史

| 年 | 事象 |
|---|---|
| 1883 | Reynolds 実験 (層流→乱流) |
| 1922 | Richardson "Weather Prediction by Numerical Process" (cascade poem) |
| **1941** | **Kolmogorov K41 -5/3 法則** (Nobel Prize 該当作) |
| 1962 | Obukhov-Kolmogorov K62 (intermittency 補正) |
| 1967 | Kraichnan 2D 乱流 dual cascade |
| 1970s | Mandelbrot fractal (intermittency 観測) |
| 1990s | DNS (direct numerical simulation) で K41 検証 |

---

## 2. ★ Richardson Cascade (1922) ★

### 2.1 詩 (Richardson 1922)

```
"Big whirls have little whirls that feed on their velocity,
 and little whirls have lesser whirls and so on to viscosity."
```

= **大渦 → 中渦 → 小渦 → 散逸** のエネルギー流れ。

### 2.2 階層

```
L (大スケール, energy injection): 大渦, U
↓ (慣性領域 inertial range)
↓
η (Kolmogorov scale, viscous dissipation)
```

### 2.3 ITU 視点

```
Richardson cascade = K_flow scale-by-scale K-state transfer
Inertial range = K_flow scale-invariant region
```

---

## 3. ★ Kolmogorov 1941 (K41) ★

### 3.1 仮説

1. **局所等方性**: 小スケールは大スケールの方向性を忘れる
2. **局所相似則**: 慣性領域は ν と無関係 (ε のみで決まる)

### 3.2 ★ -5/3 法則 (Universal) ★

エネルギースペクトル:

```
E(k) = C_K ε^{2/3} k^{-5/3}
```

C_K ≈ 1.5 (Kolmogorov constant)、ε: エネルギー散逸率。

### 3.3 速度差 (構造関数)

```
S_p(r) = ⟨ |u(x+r) - u(x)|^p ⟩

K41: S_p(r) = C_p (ε r)^{p/3}
```

特に p=2: S_2 ∝ r^{2/3} (二次構造関数)。

### 3.4 ★ Kolmogorov microscale ★

```
η = (ν³ / ε)^{1/4}   (length)
τ_η = (ν / ε)^{1/2}  (time)
u_η = (ν ε)^{1/4}    (velocity)
```

ν = 1.5×10⁻⁵ m²/s (空気), ε = 1 W/kg:
```
η ≈ 4×10⁻⁴ m = 0.4 mm
```

### 3.5 Re と η/L

```
η/L ∝ Re^{-3/4}
```

⇒ Re 増大で η と L が分離 (慣性領域が広がる)。

### 3.6 ITU 視点

```
K41 -5/3 = K_flow universal RG fixed point spectrum
ε = K_flow energy dissipation rate (scale-independent in inertial range)
Kolmogorov microscale = K_flow dissipation cutoff
```

---

## 4. 数値検証 (DNS, 実験)

### 4.1 実験

| 実験 | E(k) slope | comment |
|---|---|---|
| 風洞 grid turbulence | -1.66 | K41 一致 |
| Tidal channel | -1.68 | 一致 |
| Atmospheric BL | -1.67 | 一致 |
| Jet flow | -1.65 | 一致 |
| **K41 theory** | **-5/3 = -1.667** | **universal** |

### 4.2 DNS

| Re_λ | E(k) スロープ |
|---|---|
| 50 | -1.5 (短い慣性領域) |
| 200 | -1.6 |
| 1000 | -1.65 |
| 5000 | -1.667 (K41) |

= 高 Re で K41 universality 顕在化。

### 4.3 ITU 視点

```
K41 universality = K_flow RG fixed point
有限 Re 補正 = K_flow finite-size scaling
```

---

## 5. ★ 2D vs 3D 乱流 (Kraichnan 1967) ★

### 5.1 3D 乱流

```
Energy: large → small (forward cascade)
E(k) ∝ k^{-5/3}
```

### 5.2 2D 乱流 (Kraichnan)

**enstrophy** ω² も保存:

```
Energy: forced scale → LARGE (inverse cascade)  E(k) ∝ k^{-5/3}
Enstrophy: forced scale → small (forward cascade) E(k) ∝ k^{-3}
```

⇒ **dual cascade**。

### 5.3 観測

| 系 | dim | observation |
|---|---|---|
| 大気 mesoscale (~100 km) | quasi-2D | k^{-5/3} (inverse cascade) |
| 衛星画像渦 (Jupiter, Earth) | 2D | k^{-3} (forward enstrophy) |
| 海洋 mesoscale | 2D | inverse cascade |

### 5.4 ITU 視点

```
2D vs 3D = K_flow の dimension-dependent cascade topology
Inverse cascade = K_flow large-scale K-state self-organization
```

---

## 6. Intermittency (1962-現在)

### 6.1 K41 からのずれ

```
S_p(r) ∝ r^{ζ_p}
K41: ζ_p = p/3
実験: ζ_p < p/3 for p > 3  (intermittency)
```

= **小スケール ε の揺らぎ** が大きい (多重 fractal)。

### 6.2 Obukhov-Kolmogorov K62

```
ζ_p = p/3 + μ × log correction
μ ≈ 0.2-0.3 (intermittency parameter)
```

### 6.3 She-Leveque (1994) hierarchy

```
ζ_p = p/9 + 2(1 - (2/3)^{p/3})
```

実験と良く一致。

### 6.4 ITU 視点

```
Intermittency = K_flow の anomalous scaling (RG fixed point は不変だが現象は anomalous)
She-Leveque = K_flow multi-fractal structure
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **K41 -5/3 法則** synthetic spectrum 生成 + 検証
2. **Kolmogorov microscale** η for 空気/水/油
3. **Inertial range width** L/η ∝ Re^{3/4}
4. **2D vs 3D dual cascade** schematic
5. **Intermittency** ζ_p deviation from K41
6. **3D random Fourier modes** with k^{-5/3} synthesis

---

## 8. Phase 160 主結論

1. **Richardson cascade (1922)**: 大渦→小渦→散逸
2. **K41 (1941)**: **E(k) ∝ k^{-5/3}** universal
3. **Kolmogorov microscale**: η = (ν³/ε)^{1/4}, η/L ∝ Re^{-3/4}
4. **2D Kraichnan (1967)**: inverse energy + forward enstrophy dual cascade
5. **Intermittency (K62, She-Leveque 1994)**: ζ_p < p/3 for p>3
6. **DNS が K41 universality 高 Re で検証**
7. **ITU**: K_turbulence = K_flow universal RG fixed point
8. **次の Phase 161** で **境界層 + 圧縮性流体 + 衝撃波**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Richardson cascade | K_flow scale-by-scale transfer |
| K41 -5/3 | K_flow universal RG fixed point |
| Kolmogorov microscale | K_flow viscous cutoff |
| Inertial range | K_flow scale-invariant attractor |
| 2D vs 3D | K_flow dimension topology |
| Intermittency | K_flow multi-fractal anomalous scaling |
| 高 Re universality | K_flow universality class |

---

## 引用

```
Terada, M. (2026). Phase 160: Turbulence — Kolmogorov 1941, energy cascade,
and universality in ITU (Tier 1 #23 phase 2/8). Zenodo. DOI: [10.5281/zenodo.20249794](https://doi.org/10.5281/zenodo.20249794).
```

主要参考文献:
- Richardson, L. F. (1922) Weather Prediction by Numerical Process. Cambridge UP.
- Kolmogorov, A. N. (1941) "The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers" Dokl. Akad. Nauk SSSR 30, 301
- Obukhov, A. M., Kolmogorov, A. N. (1962) "A refinement of previous hypotheses concerning the local structure of turbulence in a viscous incompressible fluid at high Reynolds number" J. Fluid Mech. 13, 82
- Kraichnan, R. H. (1967) "Inertial ranges in two-dimensional turbulence" Phys. Fluids 10, 1417
- Onsager, L. (1949) "Statistical hydrodynamics" Nuovo Cim. Suppl. 6, 279 (2D dual cascade prediction)
- Frisch, U. (1995) Turbulence: The Legacy of A. N. Kolmogorov. Cambridge UP.
- She, Z. S., Leveque, E. (1994) "Universal scaling laws in fully developed turbulence" PRL 72, 336
- Pope, S. B. (2000) Turbulent Flows. Cambridge UP.
- Tennekes, H., Lumley, J. L. (1972) A First Course in Turbulence. MIT Press.
- Argoul, F. et al. (1989) "Wavelet analysis of turbulence reveals the multifractal nature of the Richardson cascade" Nature 338, 51
