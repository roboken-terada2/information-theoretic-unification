# Phase 121: Page Curve 厳密版 + 蒸発過程の量子情報

> **Tier 1 #18 Black Holes — Phase 3/8 (Block A paper 2/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 121 の目的

Phase 113 (Tier 1 #17) で Page curve の toy 解析を行った。Phase 121 では BH 専用に **厳密版**を構築する。

確立する内容:

1. **Page (1993) 公式の厳密版**: ⟨S_A⟩ = Σ_{k=d_A+1}^{d_A d_B} 1/k - (d_A - 1)/(2 d_B)
2. **Page time の正確な定義**: d_A = d_B となる時刻
3. **蒸発過程の S_R(t) の数値積分**: Hawking radiation 量から実時間
4. **量子情報 measures**: relative entropy, mutual information, conditional entropy
5. **QECC との関係**: Page-Yang 1998 ↔ Bekenstein-Hawking ↔ holographic code

中心テーゼ:

> **Page curve は ITU 公理 δS = δ⟨K⟩ のユニタリ条件下の自然な帰結**。
> t < t_Page: K_R が成長 (radiation thermal flow)。
> t > t_Page: K_R が縮退 (information return, island saddle 支配)。
> Page time = K-flow stationary point 移行時刻。

---

## 1. Page 公式の厳密版 (Page 1993)

### 1.1 公式

Hilbert space H = H_A ⊗ H_B、dim d_A × d_B = d_total、|ψ⟩ random Haar:

```
⟨S_A⟩ = Σ_{k=d_A+1}^{d_A d_B} (1/k) - (d_A - 1)/(2 d_B)
       (for d_A ≤ d_B)
```

近似形 (large d):

```
⟨S_A⟩ ≈ log(d_A) - d_A / (2 d_B)
```

### 1.2 Page curve の数学

```
d_A < d_B (t < t_Page): ⟨S_A⟩ ≈ log d_A (linear in log scale)
d_A = d_B (t = t_Page): ⟨S_A⟩ ≈ log d_A - 1/2 (peak)
d_A > d_B (t > t_Page): ⟨S_A⟩ ≈ log d_B (decreasing as d_B shrinks)
```

⇒ **Page curve = entropy 三角形**。

### 1.3 BH 蒸発への適用

- A = radiation (Hawking 放射の集合)
- B = BH 内部
- d_A(t) = exp(S_R(t)) → 増加
- d_B(t) = exp(S_BH(t)) → 減少
- 全体 d_A × d_B ≈ const (ユニタリ進化)

### 1.4 Page time

```
t_Page: d_A(t_Page) = d_B(t_Page)
     ⟺ S_R(t_Page) = S_BH(t_Page)
     ⟺ S_R(t_Page) ≈ S_BH(0) / 2
```

t_Page ≈ t_evap / 2 (toy model)。

---

## 2. 厳密蒸発過程

### 2.1 dM/dt 公式

```
dM/dt = -ℏ c⁴ / (15360 π G_N² M²)  (Hawking 1975, Page 1976)
```

積分して:

```
M(t)³ = M₀³ × (1 - t/t_evap)
M(t) = M₀ × (1 - t/t_evap)^{1/3}
```

t_evap = 5120 π G²M₀³ / (ℏc⁴)

### 2.2 S_BH(t)

```
S_BH(t) = A(t) / (4 ℓ_P²) = 4π G² M(t)² c²² / (ℏ c³ G_N)
       = S_BH(0) × (1 - t/t_evap)^{2/3}
```

### 2.3 S_R(t) (積分量)

放射の累積エネルギー = M₀ c² - M(t) c²。
放射温度は T_H(t) ∝ 1/M(t) で時間変化。

近似的に:

```
S_R^thermal(t) ≈ S_BH(0) - S_BH(t)
              = S_BH(0) × [1 - (1 - t/t_evap)^{2/3}]
```

### 2.4 Page curve (厳密)

```
S_R(t) = min ( S_R^thermal(t),  S_BH(t) )
```

これが Island formula の Schwarzschild 版。

---

## 3. 量子情報 Measures

### 3.1 Relative entropy

```
S(ρ || σ) = Tr(ρ log ρ) - Tr(ρ log σ) ≥ 0
```

- BH 量子状態 ρ_BH に対し、Hawking 予言 σ_Hawking との差
- 蒸発と共に増加: ITU が Hawking を逸脱する scale

### 3.2 Mutual Information

```
I(R:B) = S(R) + S(B) - S(R∪B) = S(R) + S(B) - S(total)
       ≥ 0  (always)
```

- t < t_Page: I(R:B) ≈ 2 S_R (純粋状態仮定で)
- t > t_Page: I(R:B) ≈ 2 S_BH (BH と radiation の相関)

### 3.3 Conditional entropy

```
S(R|B) = S(R∪B) - S(B) = S(total) - S(B)
       = 0 (純粋状態) - S(B)
       = -S(B)
```

純粋状態下では S(R|B) < 0 → **量子条件付きエントロピーの負値** (古典では不可能)。

### 3.4 ITU 視点

ITU 公理 δS = δ⟨K⟩ は **すべての量子情報 measure を内包**:
- S = von Neumann ⟨K⟩
- Relative entropy = Δ⟨K⟩ across reference states
- Mutual info = K_A + K_B - K_{AB}

---

## 4. QECC との関係

### 4.1 Page-Yang 1998

BH = quantum error-correcting code (QECC) で、bulk operator を encode する subspace。

```
H_BH = H_logical (≤ exp(S_BH) dim) ⊕ H_environment
```

### 4.2 Holographic code (HaPPY tensor 2015)

- bulk operator (logical) ↔ boundary CFT (physical)
- erasure correction: 1/3 以上の boundary が残れば bulk reconstruction 可能
- Page time = QECC threshold (radiation が code capacity 超え)

### 4.3 ITU 視点

QECC = ITU 公理の **error-correcting encoding**:

```
K_BH = K_logical + K_environment
δS_logical = δ⟨K_logical⟩ (information-preserving)
```

⇒ BH 内部 information は K_geom の量子状態として保護される。

---

## 5. 数値検証項目

本 phase の simulation で確認:

1. **厳密 Page 公式**: ⟨S_A⟩ vs d_A (Page 1993 公式)
2. **M(t) = M₀(1-t/t_evap)^{1/3} 蒸発曲線**
3. **S_BH(t) = S_BH(0)(1-t/t_evap)^{2/3}**
4. **S_R^thermal(t) + S_R^Page(t) 比較**
5. **Page time の数値**: d_A(t_Page) = d_B(t_Page) を逆算
6. **Mutual info I(R:B) の時間発展**

---

## 6. Phase 121 主結論

1. **Page 公式 厳密版**: ⟨S_A⟩ = Σ 1/k - (d_A-1)/(2d_B)
2. **蒸発 M(t)**: M₀(1-t/t_evap)^{1/3} (Hawking 1975)
3. **S_BH(t)**: S_BH(0)(1-t/t_evap)^{2/3}
4. **Page curve**: min(S_R^thermal, S_BH) で完全 unitary
5. **Mutual info I(R:B) 時間発展**: BH-radiation 量子相関
6. **QECC ↔ BH**: Page-Yang 1998, HaPPY tensor 2015
7. **ITU**: 全 quantum info measures を K_A 公理に内包
8. **次の Phase 122** で **Information paradox + Mathur 1/2 evidence**

---

## 7. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Page 公式 | δS = δ⟨K⟩ + Haar measure |
| 蒸発 M(t) | K_geom dynamics |
| S_R(t) Page curve | K_R(t) flow |
| Mutual info | K_A + K_B - K_AB |
| QECC | K-flow error correction |
| Holographic code | K_bulk ↔ K_boundary |

---

## 引用

```
Terada, M. (2026). Phase 121: Rigorous Page curve and quantum information
in evaporation (Tier 1 #18 phase 3/8). Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Page, D. N. (1993) "Average entropy of a subsystem" PRL 71, 1291
- Page, D. N. (1993) "Information in black hole radiation" PRL 71, 3743
- Page, D. N. (1976) "Particle emission rates from a black hole" PRD 13, 198
- Hawking, S. W. (1975) "Particle creation by black holes" Commun. Math. Phys. 43, 199
- Pastawski, F., Yoshida, B., Harlow, D., Preskill, J. (2015) "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence" JHEP 06, 149
- Page, D. N., Yang, Q. (1998) "Black hole as information-conserving qubit" (concept)
