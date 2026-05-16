# Phase 146: 非平衡熱力学 + Onsager 相反定理 + 線形応答 + 揺動散逸定理

> **Tier 1 #21 Statistical Mechanics — Phase 4/8 (Block A paper 5/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 146 の目的

Phase 143-145 で平衡統計 + 相転移 を扱った。Phase 146 では **非平衡** に進む:

1. **Onsager 相反定理 (1931, Nobel 1968)**: L_ij = L_ji
2. **線形応答理論** (Kubo 1957)
3. **揺動散逸定理 (FDT)** (Callen-Welton 1951)
4. **Brown 運動** (Einstein 1905, Langevin 1908)
5. **拡散方程式** (Fick, Fokker-Planck)
6. **ITU 視点**: 非平衡 = K_stat の **off-equilibrium response kernel**

中心テーゼ:

> **線形応答 + FDT = ITU K_stat の二点相関関数の Kubo 公式**。
> Onsager 対称性 = K_stat の時間反転対称性 (microscopic reversibility) の帰結。
> 揺動 (fluctuation) と散逸 (dissipation) は同じ K_stat 二点関数の異なる射影。

---

## 1. 非平衡の基本量

### 1.1 流れと力

```
J_i (flux: heat, particle, charge, ...)
X_j (thermodynamic force: ∇T, ∇μ, E-field, ...)
```

### 1.2 エントロピー生成

```
σ = Σ_i J_i X_i  ≥ 0   (Second law)
```

### 1.3 線形領域

```
J_i = Σ_j L_ij X_j
```

L_ij: kinetic coefficients。

---

## 2. ★ Onsager 相反定理 (1931, Nobel 1968) ★

### 2.1 主張

```
L_ij = L_ji
```

(時間反転 even-even or odd-odd 結合の場合)。

### 2.2 例 1: 熱電効果

- Seebeck: ∇T → 電流
- Peltier: 電流 → 熱流

```
L_Seebeck = L_Peltier  (実験で検証済)
```

### 2.3 例 2: 拡散と熱拡散

- Soret: ∇T → 物質流 (D_T)
- Dufour: ∇μ → 熱流

### 2.4 磁場下の修正

```
L_ij(B) = L_ji(-B)
```

(磁場は時間反転で符号反転)。

### 2.5 ITU 視点

```
Onsager L_ij = ITU K_stat ⟨J_i(t) J_j(0)⟩ 時間反転対称性
```

---

## 3. ★ 線形応答理論 (Kubo 1957) ★

### 3.1 設定

外場 H_ext = -A·F(t) (摂動)。

応答:
```
⟨B(t)⟩ - ⟨B⟩_eq = ∫₀^∞ χ_BA(t-t') F(t') dt'
```

### 3.2 Kubo 公式

```
χ_BA(t) = (i/ℏ) θ(t) ⟨[B(t), A(0)]⟩_eq
```

quantum case。古典極限:

```
χ_BA(t) = -β θ(t) ⟨B(t) Ȧ(0)⟩_eq
```

### 3.3 周波数応答

```
χ_BA(ω) = ∫_{-∞}^∞ χ_BA(t) e^{iωt} dt = χ' + i χ''
```

### 3.4 Kramers-Kronig 関係式

χ(ω) の解析性 (causality) ⇒:

```
χ'(ω) = (1/π) P ∫ χ''(ω')/(ω'-ω) dω'
```

### 3.5 ITU 視点

```
Kubo χ = ITU K_stat 二点関数の Heaviside 投影
```

---

## 4. ★ 揺動散逸定理 (FDT) (Callen-Welton 1951) ★

### 4.1 主張

平衡揺動 ⇔ 散逸:

```
S_AA(ω) = (2ℏ/(1 - e^{-βℏω})) χ''_AA(ω)
```

S_AA: power spectral density of fluctuations。

高温極限:
```
S_AA(ω) = (2 k_B T / ω) χ''_AA(ω)
```

### 4.2 例 1: Johnson-Nyquist noise (1928)

抵抗 R の電圧揺動:

```
⟨V²⟩ = 4 k_B T R Δf
```

### 4.3 例 2: Einstein 関係式 (1905)

Brown 運動拡散係数:

```
D = μ k_B T   (μ: mobility = 1/γ for damping γ)
```

D (fluctuation) と μ (dissipation) を結ぶ。

### 4.4 例 3: Nyquist 雑音 (量子版)

```
⟨V²⟩(ω) = 2 R ℏω coth(βℏω/2)
```

高 T: 4 k_B T R (古典 Nyquist)。
低 T: 2 ℏω R (zero-point 揺動)。

### 4.5 ITU 視点

```
FDT = ITU K_stat 二点関数の 揺動チャンネルと応答チャンネルの双対性
```

---

## 5. ★ Brown 運動 (Einstein 1905, Langevin 1908) ★

### 5.1 Einstein 解析

花粉粒子の位置:

```
⟨x²⟩ = 2 D t   (1D)
⟨r²⟩ = 6 D t   (3D)
```

D を計算 ⇒ 分子の存在を確認 (Perrin 1908, Nobel 1926)。

### 5.2 Langevin 方程式

```
m dv/dt = -γ v + R(t)
⟨R(t)⟩ = 0
⟨R(t) R(t')⟩ = 2 γ k_B T δ(t-t')   (FDT)
```

### 5.3 数値例

水中 1 μm 粒子 at 300 K:
```
γ = 6π η R ≈ 6π × 10⁻³ × 0.5e-6 ≈ 9.4e-9 N·s/m
D = k_B T / γ ≈ 4e-13 m²/s
⟨x²⟩^{1/2} in 1 s ≈ √(2Dt) ≈ 0.9 μm  ✓
```

### 5.4 ITU 視点

```
Langevin = K_stat 上の effective stochastic dynamics
R(t) = 揺動チャンネル
γ v = 散逸チャンネル
FDT がこの 2 チャンネルを結合
```

---

## 6. Fokker-Planck 方程式

### 6.1 確率分布の発展

Langevin → 確率密度 P(x,t):

```
∂P/∂t = -∂/∂x (F P) + D ∂²P/∂x²
```

F: drift force。

### 6.2 平衡分布

```
P_eq(x) ∝ exp(-βU(x))
```

(Boltzmann distribution = stationary FP)。

### 6.3 拡散方程式 (F=0)

```
∂P/∂t = D ∂²P/∂x²
```

⇒ Gaussian spreading: ⟨x²⟩ = 2Dt。

### 6.4 ITU 視点

```
Fokker-Planck = K_stat 確率密度の master equation
平衡 = K_stat stationary attractor
```

---

## 7. Non-equilibrium 標準モデル: Boltzmann 輸送方程式

### 7.1 BTE

```
∂f/∂t + v·∇f + F·∇_p f = (∂f/∂t)_coll
```

f(r, p, t): 単一粒子分布関数。

### 7.2 H-定理 (Boltzmann 1872)

```
H[f] = ∫ f log f d³p

dH/dt ≤ 0
```

⇒ 熱平衡 (Maxwell-Boltzmann) は H 最小。

### 7.3 数値例: gas 緩和

```
τ_coll ≈ 1/(n σ v_th)
標準大気: τ ≈ 10⁻¹⁰ s
mean free path l ≈ v_th τ ≈ 6e-8 m
```

### 7.4 ITU 視点

```
BTE = K_stat 単一粒子分布の transport equation
H-theorem = K_stat エントロピー増大の microscopic 証明
```

---

## 8. 数値検証項目

本 phase の simulation で確認:

1. **Brown 運動 ⟨x²⟩ = 2Dt** (Langevin numerical integration)
2. **Einstein 関係式** D = μ k_B T 検証
3. **Onsager L_ij = L_ji** (simple 2 流-2 力モデル)
4. **Johnson-Nyquist** ⟨V²⟩ = 4 k_B T R Δf
5. **Fokker-Planck Gaussian spreading**
6. **H-定理** (Maxwell-Boltzmann が H 最小)

---

## 9. Phase 146 主結論

1. **Onsager 1931 (Nobel 1968)**: L_ij = L_ji
2. **Kubo linear response (1957)**: χ_BA = θ(t) [B(t), A(0)]/iℏ
3. **FDT (Callen-Welton 1951)**: S_AA = (2 k_B T/ω) χ''
4. **Einstein 1905**: ⟨x²⟩ = 2Dt, D = μk_BT
5. **Langevin 1908**: m v̇ = -γv + R(t), ⟨RR'⟩ = 2γk_BT δ
6. **Boltzmann H-theorem (1872)**: dH/dt ≤ 0
7. **ITU**: 非平衡応答 = K_stat 二点関数の dual channel
8. **次の Phase 147** で **揺動定理 (Jarzynski 1997, Crooks 1999)**

---

## 10. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Onsager L_ij | K_stat ⟨J_i J_j⟩ 時間反転対称 |
| Kubo χ | K_stat 二点関数 Heaviside 投影 |
| FDT | K_stat 揺動-散逸双対性 |
| Brown / Langevin | K_stat 上 effective stochastic |
| Fokker-Planck | K_stat 確率密度発展 |
| H-定理 | K_stat エントロピー increasing |

---

## 引用

```
Terada, M. (2026). Phase 146: Non-equilibrium thermodynamics, Onsager reciprocity,
linear response, and FDT in ITU (Tier 1 #21 phase 4/8). Zenodo. DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

主要参考文献:
- Einstein, A. (1905) "Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung..." Ann. Phys. 17, 549
- Langevin, P. (1908) "Sur la théorie du mouvement brownien" C. R. Acad. Sci. 146, 530
- Boltzmann, L. (1872) "Weitere Studien über das Wärmegleichgewicht..." Wien. Ber. 66, 275
- Nyquist, H. (1928) "Thermal agitation of electric charge in conductors" Phys. Rev. 32, 110
- Johnson, J. B. (1928) "Thermal agitation of electricity in conductors" Phys. Rev. 32, 97
- Onsager, L. (1931) "Reciprocal relations in irreversible processes" Phys. Rev. 37, 405 & 38, 2265
- Callen, H. B., Welton, T. A. (1951) "Irreversibility and generalized noise" Phys. Rev. 83, 34
- Kubo, R. (1957) "Statistical-mechanical theory of irreversible processes" J. Phys. Soc. Jpn. 12, 570
- Green, M. S. (1954) "Markoff random processes and the statistical mechanics of time-dependent phenomena" J. Chem. Phys. 22, 398
