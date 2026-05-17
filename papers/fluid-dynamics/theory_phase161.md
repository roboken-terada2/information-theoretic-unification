# Phase 161: 境界層 + 圧縮性流体 + 衝撃波 — Prandtl + Mach + Rankine-Hugoniot

> **Tier 1 #23 Fluid Dynamics — Phase 3/8 (Block A paper 7/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 161 の目的

Phase 159 で NS, Phase 160 で乱流。Phase 161 では **境界層と圧縮性流体** に進む:

1. **Prandtl 境界層理論 (1904)** — 流体力学の中核ブレークスルー
2. **Blasius 解** (平板境界層)
3. **層流 vs 乱流境界層**
4. **圧縮性流体 + Mach 数**
5. **衝撃波 (Rankine-Hugoniot jump 条件)**
6. **超音速 + 極超音速 流れ**
7. **ITU 視点**: K_boundary = K_flow + 壁面 constraint, K_shock = K_flow discontinuity

中心テーゼ:

> **境界層 = K_flow の壁面で粘性が支配する薄層**。
> 衝撃波 = K_flow の不連続性 (entropy 生成 + Mach 圧縮)。
> Mach 数 = K_flow / K_sound 比 = compressibility 制御パラメータ。

---

## 1. ★ Prandtl 境界層理論 (1904) ★

### 1.1 歴史的背景

19 世紀: D'Alembert paradox (理想流体で抵抗 = 0)。
**Prandtl (1904) 解決**: 物体近傍に **薄い粘性層** (境界層) があり、外側は理想流体。

### 1.2 境界層厚さ δ

平板長さ L, 一様流 U_∞:

```
δ / L ~ 1 / √Re_L   (層流)
Re_L = U_∞ L / ν
```

例: 翼弦 1 m, 空気 30 m/s (Re = 2×10⁶):
```
δ ≈ L / √Re = 1 / 1414 ≈ 0.7 mm
```

### 1.3 ★ Blasius solution (1908) ★

平板層流境界層の自己相似解:

```
η = y √(U_∞ / (ν x))
u / U_∞ = f'(η)
```

f(η) は 3 階 ODE 数値解:
```
f''' + (1/2) f f'' = 0
f(0) = f'(0) = 0, f'(∞) = 1
```

特徴量:
- **f''(0) = 0.332** (壁面 shear rate)
- **δ_99 / x = 5.0 / √Re_x** (99% 速度回復厚)
- C_f = 0.664 / √Re_x (摩擦係数)

### 1.4 ITU 視点

```
Prandtl 境界層 = K_flow 壁面 boundary constraint
Blasius 自己相似解 = K_flow 境界層 universal profile
```

---

## 2. 層流 vs 乱流境界層

### 2.1 遷移 Reynolds

```
Re_x,c ≈ 5×10⁵   (平板)
```

実験条件 (表面粗さ等) で 3×10⁵ - 3×10⁶。

### 2.2 乱流境界層

| 量 | 層流 (Blasius) | 乱流 (1/7 power law) |
|---|---|---|
| δ / x | 5.0 / √Re_x | 0.37 / Re_x^{1/5} |
| C_f | 0.664 / √Re_x | 0.0592 / Re_x^{1/5} |

乱流境界層は δ が **より厚い** + C_f が **より大きい**。

### 2.3 ITU 視点

```
層流 → 乱流境界層 = K_flow boundary transition (Phase 160 接続)
```

---

## 3. 圧縮性流体 (Compressible Flow)

### 3.1 ★ Mach 数 ★

```
Ma = U / c
```

c: 音速 = √(γ p / ρ) = √(γ R T) (ideal gas)

### 3.2 流れの分類

| Ma | 名称 | 例 |
|---|---|---|
| < 0.3 | 非圧縮 | 自動車, 風 |
| 0.3-0.8 | Subsonic | 旅客機 (Boeing 747 Ma=0.85) |
| 0.8-1.2 | Transonic | 音速近傍 (Concorde 加速期) |
| 1.2-5 | Supersonic | Concorde Ma=2, SR-71 Ma=3 |
| 5-10 | Hypersonic | X-43A Ma=9.6 |
| > 10 | High hypersonic | 大気再突入 Ma=20-30 |

### 3.3 数値例 (空気 @ 20°C)

```
c = √(1.4 × 287 × 293) = 343 m/s
Ma = 0.85 → U = 292 m/s ≈ 1051 km/h (旅客機)
Ma = 2 → U = 686 m/s (Concorde)
Ma = 25 → U = 8575 m/s (再突入)
```

### 3.4 ITU 視点

```
Ma = K_flow / K_sound 比
Compressibility = K_density 揺らぎ
```

---

## 4. ★ 衝撃波 (Rankine-Hugoniot 1860s) ★

### 4.1 物理

Supersonic 物体の前面 / 背後で **不連続な圧縮**:
- 圧力 jump
- 密度 jump
- 温度 jump
- entropy 生成 (irreversible)

### 4.2 ★ Rankine-Hugoniot jump 条件 ★

定常 1D normal shock:
- mass: ρ_1 u_1 = ρ_2 u_2
- momentum: p_1 + ρ_1 u_1² = p_2 + ρ_2 u_2²
- energy: h_1 + u_1²/2 = h_2 + u_2²/2

ideal gas (γ = 1.4 for air) で Ma_1 = M:

```
p_2 / p_1 = (2γ M² - (γ-1)) / (γ+1)
ρ_2 / ρ_1 = ((γ+1) M²) / ((γ-1) M² + 2)
T_2 / T_1 = [(2γM² - (γ-1)) × ((γ-1)M² + 2)] / [(γ+1)² M²]
Ma_2² = ((γ-1)M² + 2) / (2γM² - (γ-1))
```

### 4.3 数値例 (空気, Ma_1 = 2)

```
p_2/p_1 = 4.5
ρ_2/ρ_1 = 2.67
T_2/T_1 = 1.69
Ma_2 = 0.577 (subsonic 後流)
```

= **衝撃波後で必ず subsonic** (entropy ↑ 第 2 法則)。

### 4.4 ITU 視点

```
Shock = K_flow discontinuity (jump condition)
Entropy 生成 = K_stat irreversibility (Phase 146 接続)
Ma_2 < 1 after shock = K_flow forced regime transition
```

---

## 5. 衝撃波と空力 (Drag rise)

### 5.1 Critical Mach

Subsonic 翼で局所 Ma が 1 に達する自由流 Ma:
```
Ma_crit ≈ 0.72 (NACA 翼)
```

### 5.2 Wave drag

Ma > Ma_crit で衝撃波形成 → wave drag 急増:
```
C_D ~ (Ma - Ma_crit)^n × const
```

### 5.3 Sound barrier breaking

- 1947 Bell X-1 (Yeager): 初の有人超音速
- 1976-2003 Concorde: Ma 2 商用
- 2003- (NASA, Boom): 静音超音速研究中

### 5.4 ITU 視点

```
Ma_crit = K_flow compressibility onset
Wave drag = K_flow → K_shock dissipation
```

---

## 6. 極超音速と再突入

### 6.1 Hypersonic 物理

Ma > 5 で:
- Shock 後温度 数千 K → ガス解離 + 電離
- 表面熱流束 MW/m² 級
- 化学反応 (アブレーション)

### 6.2 Apollo 再突入

```
v_entry = 11 km/s (Ma ≈ 32)
shock T ~ 25,000 K
ablation shield (PICA, AVCOAT)
```

### 6.3 ITU 視点

```
Hypersonic = K_flow + K_chemistry + K_radiation 結合
再突入 = K_flow 強非平衡 (Phase 146 接続)
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Blasius solution** f''(0) = 0.332
2. **境界層厚 δ** = 5/√Re_x
3. **層流 vs 乱流** C_f 比較
4. **Rankine-Hugoniot** Ma_1 = 1.5, 2, 3, 5 で jump
5. **Sound speed** vs T (温度依存)
6. **Hypersonic shock T** for re-entry

---

## 8. Phase 161 主結論

1. **Prandtl 境界層 (1904)**: D'Alembert paradox 解決
2. **Blasius solution (1908)**: f''(0) = 0.332, δ = 5x/√Re
3. **層流→乱流** 遷移 Re_x ~ 5×10⁵
4. **Mach 数** Ma = U/c で 6 段階分類 (subsonic → hypersonic)
5. **Rankine-Hugoniot**: shock 後で Ma_2 < 1 (subsonic), entropy ↑
6. **Ma=2 normal shock**: p×4.5, ρ×2.67, T×1.69
7. **Wave drag** Ma > Ma_crit で発生
8. **Apollo 再突入** Ma=32, T_shock ~ 25,000 K
9. **ITU**: K_boundary = K_flow + 壁制約, K_shock = K_flow discontinuity
10. **次の Phase 162** で **渦力学 + Kelvin 循環定理**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Prandtl 境界層 | K_flow 壁面 constraint |
| Blasius solution | K_flow 境界層 universal profile |
| 乱流境界層 | K_flow boundary transition |
| Mach 数 | K_flow / K_sound 比 |
| Compressibility | K_density 揺らぎ |
| Shock (R-H) | K_flow discontinuity |
| Entropy 生成 | K_stat irreversibility |
| Wave drag | K_flow → K_shock 散逸 |
| Hypersonic | K_flow + K_chemistry + K_radiation |

---

## 引用

```
Terada, M. (2026). Phase 161: Boundary layer + compressible flow + shocks
in ITU (Tier 1 #23 phase 3/8). Zenodo. DOI: [10.5281/zenodo.20249794](https://doi.org/10.5281/zenodo.20249794).
```

主要参考文献:
- Prandtl, L. (1904) "Über Flüssigkeitsbewegung bei sehr kleiner Reibung" Verh. III Int. Math. Kongr. 484
- Blasius, H. (1908) "Grenzschichten in Flüssigkeiten mit kleiner Reibung" Z. Math. Phys. 56, 1
- Rankine, W. J. M. (1870) "On the thermodynamic theory of waves of finite longitudinal disturbance" Phil. Trans. R. Soc. 160, 277
- Hugoniot, P. H. (1887) "Mémoire sur la propagation du mouvement dans les corps" J. Ec. Polytech. 57, 3
- von Kármán, T. (1921) "Über laminare und turbulente Reibung" Z. Angew. Math. Mech. 1, 233
- Schlichting, H., Gersten, K. (2017) Boundary-Layer Theory, 9th ed. Springer
- Anderson, J. D. (2003) Modern Compressible Flow, 3rd ed. McGraw-Hill
- Liepmann, H. W., Roshko, A. (2001) Elements of Gasdynamics. Dover
- Ackeret, J. (1925) "Luftkräfte auf Flügel, die mit größerer als Schallgeschwindigkeit bewegt werden" Z. Flugtech. Motorluft. 16, 72
- Chapman, S., Enskog, D. (1916-1917) Chapman-Enskog expansion (kinetic theory link)
