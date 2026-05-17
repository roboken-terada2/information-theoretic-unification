# Phase 162: 渦力学 — Helmholtz + Kelvin 循環定理 + Kármán 渦列 + 量子渦

> **Tier 1 #23 Fluid Dynamics — Phase 4/8 (Block A paper 7/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 162 の目的

Phase 159-161 で NS + 乱流 + 境界層を扱った。Phase 162 では **渦** に進む — Phase 161 の不連続性とは対照的な、**連続だが topological** な構造:

1. **Vorticity 場 ω = ∇×u**
2. **Helmholtz 渦定理 (1858)**
3. **Kelvin 循環定理 (1869)** — Γ = ∮ u·dℓ 保存
4. **Kármán 渦列 (1911)** — 円柱後流
5. **Kelvin-Helmholtz instability** — 剪断流
6. **Bénard 対流セル** (Phase 149 接続)
7. **★ 量子渦 ★** in 超流動 / BEC (Phase 144, 153 接続)
8. **ITU 視点**: K_vortex = K_flow with non-zero curl ω

中心テーゼ:

> **Vorticity = K_flow の topological structure**。
> Kelvin 循環定理 = 理想流体での K_vortex 保存則。
> Kármán 渦列 = K_vortex の structured shedding。
> 量子渦 = K_BE の topological defect (Φ_0 = h/m 量子化)。

---

## 1. ★ Vorticity 場 ★

### 1.1 定義

```
ω(r, t) = ∇ × u(r, t)
```

= 流体の **局所回転** の角速度 × 2。

### 1.2 例

- **剛体回転**: u = Ω × r → ω = 2Ω (一様)
- **層流剪断** u_x = γy: ω_z = -γ
- **点渦**: ω は δ-function

### 1.3 ω の保存 (Vorticity 方程式)

非圧縮 NS から:
```
Dω/Dt = (ω·∇) u + ν ∇²ω + (∇×F) / ρ
```

**Vortex stretching** (ω·∇)u が 3D の本質的非線形性。

### 1.4 2D 特殊性

2D で u_z = 0 ⇒ ω は **z 成分のみ** + (ω·∇)u = 0:
```
Dω/Dt = ν ∇²ω  (2D)
```

⇒ inviscid 2D で ω は **物質保存** (Phase 160 Kraichnan 接続)。

### 1.5 ITU 視点

```
ω = K_flow の curl 投影 (topological)
Vortex stretching = K_flow 3D の本質的非線形性
2D inviscid ω 保存 = K_vortex topological conservation
```

---

## 2. ★ Helmholtz 渦定理 (1858) ★

### 2.1 三定理

理想流体 (inviscid, barotropic) で:

1. **第 1**: 流体粒子は渦線 (vortex line) 上に留まる
2. **第 2**: 渦管 (vortex tube) の強さ (Γ) は時間/長さ不変
3. **第 3**: 渦線は閉じるか、無限遠 or 境界まで延びる

### 2.2 帰結

```
渦は消滅も生成もしない (理想流体)
```

(粘性で例外。viscosity が渦を作る/壊す)。

### 2.3 ITU 視点

```
Helmholtz = K_vortex topological invariant
渦の不死性 = K_flow inviscid limit conservation
```

---

## 3. ★ Kelvin 循環定理 (1869) ★

### 3.1 主張

理想流体 (inviscid + barotropic) で、閉曲線 C(t) が流体粒子と共に動くなら:

```
Γ = ∮_C u · dℓ = const   (DΓ/Dt = 0)
```

### 3.2 Stokes 定理との関係

```
Γ = ∮_C u · dℓ = ∫∫_S (∇×u) · dA = ∫∫_S ω · dA
```

= 渦束 ω·A の保存。

### 3.3 ★ 量子化 ★

量子流体 (超流動, BEC) では追加条件:

```
Γ = ∮ u · dℓ = n × (h / m)   (n ∈ ℤ)
```

= **循環は量子化** (Onsager 1949, Feynman 1955)。

### 3.4 ITU 視点

```
Kelvin 循環 = K_vortex の Stokes 双対 invariant
量子循環 Γ = nh/m = K_BE topological quantum number
```

---

## 4. ★ Kármán 渦列 (1911) ★

### 4.1 観測

円柱後方の乱流ウェーク (Re ~ 100 - 10⁵):

```
左右交互に放出される vortex pair
Strouhal 数 St = f L / U
```

### 4.2 数値: 円柱

```
St ≈ 0.21 (Re 200 - 200,000 で ほぼ一定)

例: 円柱直径 1 cm, 流速 1 m/s (Re = 10⁴):
   shedding 周波数 f = 0.21 × 1 / 0.01 = 21 Hz
```

### 4.3 工学応用

- **電線の "唸り"** (aeolian tone)
- **橋の共振** (Tacoma Narrows 1940 崩壊事件)
- **流量計** (vortex flow meter)

### 4.4 ITU 視点

```
Kármán 渦列 = K_vortex の structured shedding
St 普遍 = K_vortex universal frequency ratio
```

---

## 5. ★ Kelvin-Helmholtz Instability ★

### 5.1 物理

平行な異速度 2 流体の境界が不安定:

```
γ_KH ~ k Δu  (growth rate)
λ_critical = 2π (Δu)² / g (重力で安定化)
```

### 5.2 観測例

- 空 cloud (atmospheric KH waves)
- 海洋境界
- Jupiter 帯状流境界
- Sun corona 観測

### 5.3 ITU 視点

```
KH instability = K_flow shear interface の不安定
渦巻雲 = K_vortex の macroscopic 表現
```

---

## 6. Rayleigh-Bénard 対流 (Phase 149 接続)

### 6.1 設定

上下 ΔT で加熱された薄い流体層:

```
Ra = (g α ΔT L³) / (ν κ)
```

### 6.2 ★ Rayleigh 臨界数 ★

```
Ra_c ≈ 1707.76   (両壁 rigid)
Ra_c ≈ 657.5     (両壁 free)
```

Ra > Ra_c で対流セル発生 → Phase 149 散逸構造の典型例。

### 6.3 ITU 視点

```
Bénard = K_flow buoyancy-driven dissipative structure (Phase 149 Prigogine)
```

---

## 7. ★ 量子渦 (Onsager-Feynman 1949-1955) ★

### 7.1 He-4 超流動の渦

```
Γ = h / m_He4 = 9.97 × 10⁻⁸ m²/s
```

= **量子化された** 循環の基本単位。

### 7.2 渦芯サイズ

```
ξ_coh = ℏ / √(2 m E_gap)
He-4: ξ ≈ 0.1 nm (Phase 144 接続)
```

### 7.3 BEC 渦 (Cornell-Wieman 2000s)

Rb-87 BEC を回転 → 三角格子 渦糸 (Abrikosov 同類, Phase 153 接続)。

### 7.4 ★ 重力との analogy ★

Φ_0^SC = h/(2e) (Phase 153 BCS)
Γ_quantum = h/m  (He-4 超流動)
Q (BH) = (charge, mass, ang. mom.)

⇒ 全て **topological quantum 数**。

### 7.5 ITU 視点

```
量子渦 = K_BE の topological defect
Γ = h/m = K_quantum geometric quantization (Phase 153 Φ_0 と類似)
BEC 渦糸 = K_quantum coherence の lattice (Abrikosov 系)
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Point vortex dynamics** (N-body 2D, energy/momentum 保存)
2. **Strouhal 数 0.21** (円柱 vortex shedding)
3. **Rayleigh-Bénard Ra_c ≈ 1708**
4. **Vorticity stretching** simple shear
5. **量子渦 Γ = h/m** for He-4
6. **Tacoma Narrows resonance** estimate

---

## 9. Phase 162 主結論

1. **Vorticity ω = ∇×u** = 流体回転場
2. **Helmholtz 渦定理 (1858)**: 渦は理想流体で不滅
3. **Kelvin 循環定理 (1869)**: DΓ/Dt = 0 (理想 + barotropic)
4. **Strouhal 0.21** (円柱 Kármán shedding, universal)
5. **Tacoma Narrows 1940** = KH/Kármán 共振崩壊事件
6. **Rayleigh-Bénard Ra_c ≈ 1708**
7. **量子渦 Γ = h/m** (Onsager-Feynman, Phase 144 接続)
8. **BEC 渦糸 lattice** (Cornell-Wieman, Abrikosov 同類)
9. **ITU**: K_vortex = K_flow curl, 量子化 = K_BE topological
10. **次の Phase 163** で **MHD + プラズマ流体**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Vorticity ω = ∇×u | K_flow curl topological |
| Vortex stretching | K_flow 3D non-linearity |
| 2D ω 保存 | K_vortex topological conservation |
| Helmholtz 定理 | K_vortex invariance |
| Kelvin 循環 Γ | K_vortex Stokes 双対 invariant |
| Kármán 渦列 | K_vortex structured shedding |
| Strouhal 0.21 | K_vortex universal frequency |
| KH instability | K_flow shear interface 不安定 |
| Bénard Ra_c | K_flow buoyancy 散逸構造 |
| 量子渦 Γ = h/m | K_BE topological defect (geometric quantization) |

---

## 引用

```
Terada, M. (2026). Phase 162: Vortex dynamics — Helmholtz, Kelvin circulation,
Kármán, and quantum vortices in ITU (Tier 1 #23 phase 4/8).
Zenodo. DOI: [10.5281/zenodo.20249794](https://doi.org/10.5281/zenodo.20249794).
```

主要参考文献:
- Helmholtz, H. (1858) "Über Integrale der hydrodynamischen Gleichungen, welche den Wirbelbewegungen entsprechen" J. reine angew. Math. 55, 25
- Kelvin (W. Thomson) (1869) "On vortex motion" Trans. Roy. Soc. Edinburgh 25, 217
- von Kármán, T. (1911) "Über den Mechanismus des Widerstandes, den ein bewegter Körper in einer Flüssigkeit erfährt" Nach. Gesell. Wiss. Göttingen 547
- Strouhal, V. (1878) "Über eine besondere Art der Tonerregung" Ann. Phys. 5, 216
- Rayleigh, Lord (1916) "On convection currents in a horizontal layer of fluid" Phil. Mag. 32, 529
- Bénard, H. (1900) "Les tourbillons cellulaires dans une nappe liquide" Rev. Gén. Sci. Pures Appl. 11, 1261
- Onsager, L. (1949) "Statistical hydrodynamics" Nuovo Cim. Suppl. 6, 279 (quantum circulation prediction)
- Feynman, R. P. (1955) "Application of quantum mechanics to liquid helium" Progress in Low Temperature Physics 1, 17
- Saffman, P. G. (1992) Vortex Dynamics. Cambridge UP
- Madison, K. W., Chevy, F., Wohlleben, W., Dalibard, J. (2000) "Vortex formation in a stirred Bose-Einstein condensate" PRL 84, 806
- Abo-Shaeer, J. R., Raman, C., Vogels, J. M., Ketterle, W. (2001) "Observation of vortex lattices in Bose-Einstein condensates" Science 292, 476
