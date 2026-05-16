# Phase 149: 複雑系 + Active Matter + 生命の熱力学 + K_complex

> **Tier 1 #21 Statistical Mechanics — Phase 7/8 (Block A paper 5/9)**
> Tier 0 ITU concept DOI: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> Tier 0 v3.0: [10.5281/zenodo.20200156](https://doi.org/10.5281/zenodo.20200156)
> 著者: 寺田 宗弘 (Roboken)

---

## 0. Phase 149 の目的

Phase 143-148 で平衡 + 非平衡 + 揺動定理 + 情報理論 を扱った。Phase 149 では **複雑系・生命系** に進む:

1. **Active matter** (自走粒子, Vicsek 1995)
2. **生命の熱力学** (Schrödinger 1944, "What is Life?")
3. **散逸構造** (Prigogine 1977 Nobel)
4. **自己組織化臨界性** (SOC, Bak-Tang-Wiesenfeld 1987)
5. **ネットワーク統計** (Watts-Strogatz, Barabási-Albert)
6. **ITU 視点**: 複雑系 = K_stat の **非自明 attractor + dissipative structure**

中心テーゼ:

> **生命 = K_stat の非平衡 dissipative attractor**。
> Active matter = K_stat に energy injection を加えた非平衡 phase。
> SOC = K_stat の scale-free non-equilibrium fixed point。
> ⇒ K_complex を K_stat の non-trivial sub-manifold として定義。

---

## 1. ★ Active Matter ★

### 1.1 定義

各構成要素が **自身でエネルギーを消費して運動** する系:
- 細菌 (E. coli swimming)
- 鳥群 (starling murmuration)
- 細胞内 motor proteins
- 自走 colloid (Janus particles)

### 1.2 ★ Vicsek model (1995) ★

```
v_i(t+1) = v_0 × ê[θ_i(t+1)]
θ_i(t+1) = ⟨θ_j⟩_{j ∈ neighbor of i} + η ξ_i

η: noise, v_0: speed
```

### 1.3 相転移

- **Low η**: 整列 (flocking phase) — long-range order
- **High η**: 無秩序 (disordered phase)
- **臨界 η_c**: 連続相転移

→ 2D で long-range order が可能 (Mermin-Wagner 例外, **自発的対称性破れ** at non-equilibrium)。

### 1.4 ITU 視点

```
Active matter = K_stat + energy injection per particle
非平衡 K-state attractor → flocking macroscopic order
```

---

## 2. 生命の熱力学 (Schrödinger 1944)

### 2.1 ★ "What is Life?" 中心問い ★

> 「生命は無秩序から秩序を作るのではなく、**負のエントロピー** を吸収する」 (Schrödinger 1944)

### 2.2 Open system

```
dS/dt = (dS/dt)_internal + (dS/dt)_exchange
     ≥ 0                ≤ 0 (可)
```

生命体: 環境から負エントロピーを取り込み、内部 entropy 上昇を相殺。

### 2.3 数値例 (人間)

```
代謝率: ~100 W
体温: 310 K
出力 entropy: 100/310 ≈ 0.32 W/K
1 日: 28 kJ/K = 2 × 10⁴ bit/K × ln 2 entropy 出力
```

### 2.4 ATP 燃料

```
ATP → ADP + P: ΔG ≈ -50 kJ/mol ≈ 20 kT (cellular)
人間: 75 kg → 1 日 75 kg ATP turnover
```

### 2.5 ITU 視点

```
生命 = K_stat sustained far-from-equilibrium attractor
ATP cycle = K_metabolic energy input pathway
```

---

## 3. ★ 散逸構造 (Prigogine 1977 Nobel) ★

### 3.1 定義

非平衡条件下で **自発的に秩序構造** が現れる現象。

### 3.2 例 1: Bénard 対流

加熱した液体で正六角形セル構造:
```
Ra = (g α ΔT L³) / (ν κ) > Ra_c ≈ 1707
```

### 3.3 例 2: Belousov-Zhabotinsky 反応

化学振動:
```
[Ce⁴⁺] が時間振動 + 螺旋波形成
```

### 3.4 例 3: Turing パターン (1952)

反応拡散方程式:
```
∂u/∂t = D_u ∇²u + f(u, v)
∂v/∂t = D_v ∇²v + g(u, v)
```

D_u ≠ D_v で **空間パターン** (zebra stripes, leopard spots)。

### 3.5 ITU 視点

```
散逸構造 = K_stat 非平衡 attractor with broken translation symmetry
Turing = K_stat 反応拡散 instability fixed point
```

---

## 4. ★ 自己組織化臨界性 (SOC, Bak-Tang-Wiesenfeld 1987) ★

### 4.1 砂山モデル

砂粒を投下 → 雪崩 (avalanche)。

```
P(size s) ∝ s^{-τ}    (power-law)
τ ≈ 1.0-1.5  (model dependent)
```

### 4.2 特徴

- **自発的** に critical point へ tune
- **スケール不変** avalanche 分布
- **長距離相関**

### 4.3 自然界の例

- 地震 (Gutenberg-Richter 法則)
- 森林火災
- 太陽 flares
- ニューロン avalanches
- 金融市場 crash

### 4.4 数値: 地震 Gutenberg-Richter

```
log N(M) = a - b M
b ≈ 1.0  (universal)
```

### 4.5 ITU 視点

```
SOC = K_stat self-tuned critical attractor
scale-free → K_stat scale-invariant fixed point
```

---

## 5. ★ ネットワーク統計力学 ★

### 5.1 Watts-Strogatz (1998) "Small-world"

```
- 短い path length (~ ln N)
- 高い clustering
- 6 degrees of separation
```

### 5.2 Barabási-Albert (1999) "Scale-free"

```
P(k) ∝ k^{-γ}    γ ≈ 2-3
```

優先的結合 (preferential attachment) → hub 構造。

### 5.3 例

| Network | nodes | ⟨k⟩ | structure |
|---|---|---|---|
| WWW | 10⁹ | 10 | scale-free γ ≈ 2.1 |
| Internet | 10⁶ | 4 | scale-free γ ≈ 2.5 |
| 神経 (C. elegans) | 302 | 14 | small-world |
| Protein interaction | 10⁴ | 10 | scale-free γ ≈ 2.5 |

### 5.4 ITU 視点

```
Network = K_topo + K_dynamics
Scale-free = K_topo preferential attachment fixed point
```

---

## 6. 複雑系の universal 性質

### 6.1 共通特徴

- **emergence**: 部分の和を超える
- **non-linearity**: 出力が線形でない
- **adaptation**: 環境応答
- **hierarchy**: 多階層
- **far-from-equilibrium**: 平衡から遠い

### 6.2 ITU での統一

```
K_complex = K_stat + non-equilibrium + adaptation
```

- 1 階層: 物理 (粒子相互作用)
- 2 階層: 化学 (分子反応)
- 3 階層: 生物 (細胞代謝)
- 4 階層: 認知 (脳ニューロン)
- 5 階層: 社会 (人間ネットワーク)

### 6.3 階層間 emergence

各階層の K-state が下層から **coarse-grained K-state** として現れる:
```
K_chemical = coarse-grain(K_physical)
K_biological = coarse-grain(K_chemical)
...
```

---

## 7. 数値検証項目

本 phase の simulation で確認:

1. **Vicsek active matter**: 整列 vs 無秩序 phase transition
2. **Turing パターン**: 反応拡散 simulation
3. **SOC 砂山**: avalanche size 分布 power-law
4. **Barabási-Albert** scale-free network 生成
5. **生命 entropy 出力** 計算 (人間 100W @ 310K)

---

## 8. Phase 149 主結論

1. **Active matter (Vicsek 1995)**: 自走粒子 + flocking 相転移
2. **生命の熱力学 (Schrödinger 1944)**: 負エントロピー吸収
3. **散逸構造 (Prigogine 1977 Nobel)**: Bénard, BZ, Turing
4. **SOC (Bak-Tang-Wiesenfeld 1987)**: scale-free avalanche
5. **ネットワーク** (WS 1998, BA 1999): small-world / scale-free
6. **K_complex = K_stat の非平衡 attractor**
7. **階層** emergence: 物理→化学→生物→認知→社会
8. **次の Phase 150** で **Tier 1 #21 統合 + 21-vertex polytope + 10 predictions**

---

## 9. ITU 視点まとめ

| 概念 | ITU 役割 |
|---|---|
| Active matter | K_stat + energy injection |
| 生命 | K_stat dissipative attractor |
| 散逸構造 | K_stat broken symmetry far from equilibrium |
| SOC | K_stat self-tuned critical attractor |
| Scale-free network | K_topo preferential-attachment fixed point |
| Hierarchy | K-state coarse-graining tower |

---

## 引用

```
Terada, M. (2026). Phase 149: Complex systems, active matter, and life thermodynamics
in ITU (Tier 1 #21 phase 7/8). Zenodo. DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

主要参考文献:
- Schrödinger, E. (1944) "What is Life?" Cambridge UP
- Prigogine, I. (1977) "Time, structure and fluctuations" Nobel lecture
- Vicsek, T. et al. (1995) "Novel type of phase transition in a system of self-driven particles" PRL 75, 1226
- Bak, P., Tang, C., Wiesenfeld, K. (1987) "Self-organized criticality" PRL 59, 381
- Turing, A. M. (1952) "The chemical basis of morphogenesis" Phil. Trans. R. Soc. B 237, 37
- Watts, D. J., Strogatz, S. H. (1998) "Collective dynamics of 'small-world' networks" Nature 393, 440
- Barabási, A. L., Albert, R. (1999) "Emergence of scaling in random networks" Science 286, 509
- Belousov, B. P. (1959) "A periodic reaction and its mechanism" Sb. Ref. Radiats. Med. 145
- Bénard, H. (1900) "Les tourbillons cellulaires dans une nappe liquide" Rev. Gén. Sci. Pures Appl. 11, 1261
- Gutenberg, B., Richter, C. F. (1944) "Frequency of earthquakes in California" Bull. Seismol. Soc. Am. 34, 185
- England, J. L. (2013) "Statistical physics of self-replication" J. Chem. Phys. 139, 121923
