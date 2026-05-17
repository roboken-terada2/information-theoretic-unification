# Phase 159: 流体力学 開幕 — Euler + Navier-Stokes + 粘性 + K_flow 母骨格

> **Tier 1 #23 Fluid Dynamics — Phase 1/8 (Block A paper 7/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Tier 1 #23 開幕

Block A 6/9 (Tier 1 #22 凝縮系) 完成で **COMPLETE PHYSICS BLOCK** (K_geom + K_cosmic + K_field + K_stat + K_solid) が確立。Phase 159 から **Tier 1 #23 Fluid Dynamics** に進む。

### Tier 1 #23 全 8 phase 構成 (予定)

| Phase | テーマ |
|---|---|
| **159 (本)** | **Euler + Navier-Stokes + 粘性 + Reynolds + K_flow 母骨格** |
| 160 | 乱流 + Kolmogorov 1941 + エネルギーカスケード |
| 161 | 境界層 + 圧縮性流体 + 衝撃波 |
| 162 | 渦力学 + Kelvin 循環定理 + 渦糸 |
| 163 | MHD + プラズマ流体 (#2 Plasma 接続) |
| 164 | 天体流体 (降着円盤 + ジェット) |
| 165 | Millennium problem (Navier-Stokes 存在/滑らかさ) |
| 166 | Tier 1 #23 統合 + 23-vertex polytope + 10 predictions |

### Phase 159 の目的

流体力学の **基礎方程式** を ITU 化:

1. **連続の式** (質量保存)
2. **Euler 方程式** (理想流体, 1755)
3. **Navier-Stokes 方程式** (1822-1845, 粘性)
4. **Reynolds 数** (1883) — 層流/乱流境界
5. **無次元化** + 相似則
6. **ITU 視点**: K_flow = K_stat coarse-grained continuum velocity field

---

## 1. ★ 流体の記述 ★

### 1.1 Eulerian vs Lagrangian

**Eulerian**: 空間固定座標で u(r, t)
**Lagrangian**: 流体粒子に追従

材料微分:
```
D/Dt = ∂/∂t + u·∇
```

### 1.2 連続の式 (質量保存)

```
∂ρ/∂t + ∇·(ρ u) = 0
```

非圧縮 (ρ = const):
```
∇·u = 0
```

### 1.3 ITU 視点

```
K_flow = ITU coarse-grained velocity 場
連続の式 = K_density conservation law
```

---

## 2. ★ Euler 方程式 (1755) ★

### 2.1 形式

理想流体 (粘性無視):
```
∂u/∂t + (u·∇) u = -∇p / ρ + g
```

= **Newton 第 2 法則** の流体版。

### 2.2 Bernoulli 方程式 (1738)

定常 + 非粘性 + 非圧縮 streamline 上:
```
p + (1/2) ρ u² + ρ g z = const
```

### 2.3 応用

| 現象 | 公式 |
|---|---|
| 翼の揚力 | Δp = (1/2) ρ (v_upper² - v_lower²) |
| Venturi 効果 | A v = const → 速い流れ ⇒ 低圧 |
| Torricelli 法則 | v = √(2gh) (タンク排水) |

### 2.4 ITU 視点

```
Euler = K_flow inviscid limit
Bernoulli = K_flow energy conservation
```

---

## 3. ★ Navier-Stokes 方程式 (1822-1845) ★

### 3.1 形式

粘性込み (Newton 流体):
```
ρ Du/Dt = -∇p + μ ∇²u + ρ g
```

非圧縮形 (∇·u = 0):
```
∂u/∂t + (u·∇) u = -∇p/ρ + ν ∇²u + g
```

ν = μ/ρ: 動粘度。

### 3.2 物質 ν 値 (m²/s @ 20°C)

| 流体 | ν (m²/s) | コメント |
|---|---|---|
| 空気 | 1.5×10⁻⁵ | 標準大気 |
| 水 | 1.0×10⁻⁶ | |
| エタノール | 1.4×10⁻⁶ | |
| グリセリン | 1.2×10⁻³ | (粘っこい) |
| 水銀 | 1.2×10⁻⁷ | 動粘度低い |

### 3.3 数値: 球の Stokes drag

```
F_drag = 6 π μ R v   (低 Re)
```

例: 0.5 μm 粒子 in 水, v=1 μm/s:
```
F = 6π × 10⁻³ × 0.5e-6 × 1e-6 = 9.4×10⁻¹⁵ N
```

→ Phase 146 Brown 運動 D = k_BT/(6πμR) と一致 (FDT)。

### 3.4 ITU 視点

```
Navier-Stokes = K_flow + K_dissipation (粘性)
ν = K_flow viscous diffusion coefficient
Stokes drag = K_flow に物体を入れた境界応答
```

---

## 4. ★ Reynolds 数 (1883) ★

### 4.1 定義

```
Re = ρ U L / μ = U L / ν
```

U: 代表速度, L: 代表長さ。

### 4.2 ★ 層流 vs 乱流 ★

```
Re < ~2000 :  laminar (層流)
Re ~ 2000-4000 : 遷移
Re > ~4000 :  turbulent (乱流)
```

(管内流の場合, 平板境界層は Re_c ~ 5×10⁵)。

### 4.3 数値例

| 状況 | U | L | Re |
|---|---|---|---|
| 大腸菌泳ぐ | 30 μm/s | 1 μm | **3×10⁻⁵** (粘性支配) |
| 室内空気循環 | 1 m/s | 1 m | 6.7×10⁴ |
| 自動車 100 km/h | 28 m/s | 4 m | 7.5×10⁶ |
| 航空機 (Boeing 747) | 250 m/s | 70 m | 1.2×10⁹ |
| 木星大赤斑 | 100 m/s | 10⁷ m | ~10¹² |

### 4.4 Stokes vs Newton drag

低 Re (Stokes): F ∝ U (linear)
高 Re (Newton): F = (1/2) C_D ρ A U² (quadratic)

転移 Re ~ 1。

### 4.5 ITU 視点

```
Reynolds 数 = K_flow の inertia / viscosity 比
Laminar → turbulent = K_flow の chaos onset (Phase 160 詳述)
```

---

## 5. 無次元化と相似則

### 5.1 主要無次元数

| 無次元数 | 定義 | 物理 |
|---|---|---|
| Re (Reynolds) | UL/ν | inertia / viscosity |
| Ma (Mach) | U/c_s | 速度 / 音速 |
| Fr (Froude) | U/√(gL) | inertia / gravity |
| We (Weber) | ρU²L/σ | inertia / surface tension |
| Pr (Prandtl) | ν/α | momentum / heat diffusion |
| Ra (Rayleigh) | gβΔTL³/(να) | buoyancy / dissipation |

### 5.2 相似則

風洞実験: 縮尺模型 + 同じ Re → 実機 と同じ流れパターン。

### 5.3 ITU 視点

```
無次元化 = K_flow の dimension stripping
相似則 = K_flow の universality (Phase 145 接続)
```

---

## 6. 数値例: Poiseuille 流れ

### 6.1 円管内層流

半径 R の円管, ∂p/∂x = -G:
```
u(r) = (G / 4μ) (R² - r²)
```

= **放物線速度プロファイル**。

### 6.2 流量

```
Q = π R⁴ G / (8 μ)   (Hagen-Poiseuille 1840)
```

### 6.3 数値 (血管)

```
動脈 R=2 mm, μ=3×10⁻³ Pa·s (血液), ΔP/L=10³ Pa/m
Q = π × (2e-3)⁴ × 10³ / (8 × 3e-3) = 2.1×10⁻⁶ m³/s ≈ 2 mL/s
```

### 6.4 ITU 視点

```
Poiseuille = K_flow laminar の解析解
血流 = K_flow 生体応用
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Reynolds 数** 各種流体系で計算
2. **Stokes drag** F = 6πμRv
3. **Hagen-Poiseuille** Q ∝ R⁴
4. **Bernoulli** Pitot 管圧力 → 速度
5. **Boundary layer** Blasius solution (Phase 161 で扱う)
6. **NS 1D Burgers equation** numerical

---

## 8. Phase 159 主結論

1. **連続の式**: ∂ρ/∂t + ∇·(ρu) = 0
2. **Euler (1755)**: 理想流体 inviscid 方程式
3. **Bernoulli (1738)**: streamline 上 p + ρu²/2 + ρgz = const
4. **Navier-Stokes (1822-1845)**: + 粘性 ν∇²u
5. **Reynolds 数 (1883)**: Re = UL/ν, 層流/乱流境界
6. **Stokes drag** F = 6πμRv (低 Re)
7. **Hagen-Poiseuille** Q ∝ R⁴ (管内層流)
8. **ITU**: K_flow = K_stat coarse-grained continuum velocity
9. **次の Phase 160** で **乱流 + Kolmogorov 1941**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| 連続の式 | K_density 保存 |
| Euler 方程式 | K_flow inviscid limit |
| Bernoulli | K_flow energy conservation |
| Navier-Stokes | K_flow + K_dissipation |
| Reynolds 数 | K_flow inertia/viscosity ratio |
| 無次元化 | K_flow dimension stripping |
| 相似則 | K_flow universality |
| Poiseuille | K_flow laminar analytic solution |

---

## 引用

```
Terada, M. (2026). Phase 159: Fluid dynamics foundations — Euler, Navier-Stokes,
viscosity, and Reynolds number in ITU (Tier 1 #23 phase 1/8).
Zenodo. DOI: [10.5281/zenodo.20249794](https://doi.org/10.5281/zenodo.20249794).
```

主要参考文献:
- Euler, L. (1755) "Principes généraux du mouvement des fluides" Mém. Acad. Sci. Berlin
- Bernoulli, D. (1738) Hydrodynamica. Argentorati
- Navier, C. L. M. H. (1822) "Mémoire sur les lois du mouvement des fluides" Mém. Acad. Sci. 6, 389
- Stokes, G. G. (1845) "On the theories of internal friction of fluids in motion" Trans. Camb. Phil. Soc. 8, 287
- Reynolds, O. (1883) "An experimental investigation of the circumstances which determine whether the motion of water shall be direct or sinuous, and of the law of resistance in parallel channels" Phil. Trans. R. Soc. Lond. 174, 935
- Hagen, G. (1839); Poiseuille, J. L. M. (1840) "Recherches expérimentales sur le mouvement des liquides dans les tubes de très-petits diamètres" C. R. Acad. Sci. 11, 961
- Prandtl, L. (1904) "Über Flüssigkeitsbewegung bei sehr kleiner Reibung" Verh. III Int. Math. Kongr. 484
- Landau, L. D., Lifshitz, E. M. (1987) Fluid Mechanics, 2nd ed. Pergamon
- Batchelor, G. K. (1967) An Introduction to Fluid Dynamics. Cambridge UP
- Tritton, D. J. (1988) Physical Fluid Dynamics, 2nd ed. Oxford UP
