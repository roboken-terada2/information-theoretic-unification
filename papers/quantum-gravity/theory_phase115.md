# Phase 115: Loop Quantum Gravity + Spin Networks + Area Spectrum

> **Tier 1 #17 Quantum Gravity — Phase 5/8 (Block A)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 115 の目的

Phase 111-114 で AdS/CFT (top-down 弦理論的) アプローチを扱った。Phase 115 では、**Loop Quantum Gravity (LQG)** を bottom-up 量子化として扱い、ITU 公理との関係を解析する。

確立する内容:

1. **LQG 基礎**: Ashtekar 変数、SU(2) ホロノミー、フラックス
2. **Spin Network**: グラフ + SU(2) スピン j_i の組
3. **Area operator のスペクトル**: A = 8π γ_Immirzi ℓ_P² Σ √(j_i(j_i+1))
4. **Immirzi parameter γ ≈ 0.2375** (BH エントロピー一致から決定)
5. **LQG vs 弦理論**: ITU 視点での統合
6. **K_geom の離散化**: LQG = ITU 公理の discrete 実現

中心テーゼ:

> **LQG の area spectrum = ITU の K_geom の離散化**。
> A = 8π γ ℓ_P² Σ √(j_i(j_i+1)) は K_geom = 2π × boost generator の **eigenvalue scale**。
> γ_Immirzi は **BH エントロピーから ITU 公理 δS = δ⟨K_geom⟩ で固定**される (γ ≈ 0.2375)。

---

## 1. Loop Quantum Gravity の基礎

### 1.1 Ashtekar 変数 (1986)

ADM 形式の (q_ab, K^ab) の代わりに:

- **densitized triad**: E^a_i = √(det q) e^a_i (i = 1,2,3)
- **Ashtekar connection**: A^i_a = Γ^i_a + γ K^i_a (γ: Immirzi parameter)

ここで Γ^i_a は spin connection、K^i_a は extrinsic curvature。

### 1.2 ホロノミー = Wilson loop

経路 γ に沿った A の path-ordered exponential:

```
h_γ[A] = P exp(∫_γ A^i_a τ_i dx^a)  ∈ SU(2)
```

τ_i = Pauli matrices / (2i)。

### 1.3 フラックス = E の積分

面 S 上の triad の積分:

```
E_S[f] = ∫_S f^i E^a_i ε_{abc} dx^b ∧ dx^c
```

ホロノミーとフラックスが基本的な **smeared variables**。

### 1.4 量子化

ループ表現で:

```
Ψ[A] = ψ(h_{γ_1}[A], h_{γ_2}[A], ...)
```

→ **Spin Network 状態** に展開される。

---

## 2. Spin Network 状態

### 2.1 グラフ構造

- Vertices (頂点): v_1, v_2, ...
- Edges (辺): e_1, e_2, ... (向き付き)
- 各 edge に SU(2) spin j_e ∈ {1/2, 1, 3/2, 2, ...}
- 各 vertex に SU(2) intertwiner ι_v (invariant tensor)

### 2.2 状態の例: 単純なグラフ

3 valent vertex で SU(2) 不変:

```
j_1 + j_2 + j_3 ∈ Z   (triangle inequality)
```

### 2.3 ITU 視点

Spin Network = **K_geom の discrete encoding**:

```
K_geom |Network⟩ = (eigenvalue depending on edges) |Network⟩
```

これが LQG 量子化の主結果。

---

## 3. Area Operator のスペクトル (Rovelli-Smolin 1995)

### 3.1 公式

面 S を貫く edges の集合 {e_i}, spins {j_i} に対し:

```
A(S) |Network⟩ = (8π γ ℓ_P²) Σ_i √(j_i (j_i + 1)) |Network⟩
```

- γ: Immirzi parameter
- ℓ_P² = ℏ G_N / c³ ≈ (1.616 × 10^{-35})² m² ≈ 2.61 × 10^{-70} m²

### 3.2 最小面積量子

j = 1/2 の場合:

```
A_min = 8π γ ℓ_P² × √(1/2 × 3/2) = 8π γ ℓ_P² × √(3)/2 = 4π√3 γ ℓ_P²
```

γ = 0.2375 なら:

```
A_min ≈ 4π × √3 × 0.2375 × ℓ_P² ≈ 5.17 ℓ_P² ≈ 1.35 × 10^{-69} m²
```

### 3.3 ITU 公理での確認

```
δ S = δ A(S) / (4 G_N) = (1 / (4 ℏ)) × 8π γ ℓ_P² × δ(Σ √(j_i(j_i+1)))
                       = δ⟨K_geom⟩
```

⇒ **discrete K_geom の eigenvalue ladder** が LQG 予言。

---

## 4. Immirzi Parameter γ の決定

### 4.1 BH エントロピーとの一致

Schwarzschild BH の地平線を spin network の punctures で覆う:

```
S_BH = A / (4 ℏ G_N) = (1 / (4 ℏ G_N)) × 8π γ ℓ_P² × Σ √(j_i(j_i+1))
```

エントロピーを状態数 log から計算 (Ashtekar-Baez-Corichi-Krasnov 1998):

```
S_BH = (γ_0 / γ) × A / (4 ℓ_P²)
```

ここで γ_0 = log 3 / (π √2) ≈ 0.247 (or alternative ≈ 0.2375 depending on regularization)。

### 4.2 ITU 公理の役割

ITU 公理 δS = δ⟨K_geom⟩ が:

- 半古典 BH 熱力学 (S = A/4) と
- LQG state counting (S = (γ_0/γ) A / (4 ℓ_P²))

の両者を結びつけ、**γ を一意に決定**:

```
γ_Immirzi ≈ 0.2375 (or log 3 / (π√2) ≈ 0.2474)
```

文献によって若干の差があるが、いずれも **O(0.1)**。

---

## 5. LQG vs 弦理論 (AdS/CFT)

### 5.1 比較

| 観点 | LQG | 弦理論 (AdS/CFT) |
|---|---|---|
| 出発点 | GR + canonical 量子化 | string + bulk 重力 |
| 空間 | non-perturbative, discrete | perturbative, continuous bulk |
| 公理 | ホロノミー-フラックス代数 | conformal boundary CFT |
| BH entropy | state counting | RT + Cardy |
| 連続性 | discrete area spectrum | smooth bulk |
| 実験 | LIGO 補正、原子干渉計 | EHT shadow, BH thermo |

### 5.2 ITU 統合視点

両者は **K_geom の異なる側面**を捉えている:
- LQG: K_geom の **離散スペクトル** (UV 側)
- AdS/CFT: K_geom の **連続幾何** (IR 側)
- 中間スケール: **renormalization group flow** で繋がる

ITU は両者の **共通母理論**として機能 (Phase 116 で詳細)。

---

## 6. 数値検証項目

本 phase の simulation で確認:

1. **Area spectrum の数値計算**: 多様な j 組み合わせでの A 固有値
2. **Immirzi parameter による area 単位**: γ = 0.2375 vs alternative 値
3. **BH 大規模スピン極限**: A ≈ 8π γ ℓ_P² N⟨√(j(j+1))⟩ ~ 線形
4. **半古典極限**: many-puncture 平均で連続 area に収束
5. **ITU first law 確認**: discrete dS = discrete dA / (4 G_N)

---

## 7. Phase 115 主結論

1. **LQG (Rovelli-Smolin 1995)**: Ashtekar 変数 + spin network
2. **Area spectrum**: A = 8π γ ℓ_P² Σ √(j_i(j_i+1)) (discrete)
3. **Immirzi parameter**: γ ≈ 0.2375 (BH エントロピー一致から)
4. **ITU 解釈**: LQG = ITU の K_geom discrete 実現
5. **LQG vs AdS/CFT**: 同じ K_geom の異なる射影
6. **次の Phase 116** で **弦理論 + M 理論 + AdS/CFT との関係**

---

## 8. ITU 視点まとめ

| LQG 概念 | ITU 役割 |
|---|---|
| Ashtekar 変数 | K_geom の canonical pair |
| Spin Network | K_geom の discrete encoding |
| Area spectrum | K_geom eigenvalue ladder |
| Immirzi γ | δS = δ⟨K⟩ 整合性で固定 |
| BH state counting | ITU 公理の microcanonical 実装 |

---

## 引用

```
Terada, M. (2026). Phase 115: Loop quantum gravity, spin networks, area
spectrum, and the Immirzi parameter in ITU. Zenodo. DOI: [to be assigned].
```

主要参考文献:
- Rovelli, C., Smolin, L. (1995) "Discreteness of area and volume in quantum gravity" Nucl. Phys. B 442, 593
- Ashtekar, A. (1986) "New variables for classical and quantum gravity" PRL 57, 2244
- Ashtekar, A., Baez, J., Corichi, A., Krasnov, K. (1998) "Quantum geometry and black hole entropy" PRL 80, 904
- Rovelli, C. (2004) "Quantum Gravity" Cambridge University Press
- Thiemann, T. (2007) "Modern Canonical Quantum General Relativity" Cambridge University Press
- Immirzi, G. (1997) "Real and complex connections for canonical gravity" Class. Quant. Grav. 14, L177
