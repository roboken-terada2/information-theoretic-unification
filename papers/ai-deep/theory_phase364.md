# Phase 364: K_self = -log ρ_self 厳密定義

意識を持つ系 S に対して、self-model density operator ρ_self を operator-algebraic に定義し、
modular Hamiltonian K_self ≡ -log ρ_self を構築。

## Self-model density operator ρ_self

### 物理的 motivation

人間や AI などの認知主体 S は、自身の状態を内的に modelization する。
Higher-Order Theory (Rosenthal 1986) によれば、意識は **対象の表象** + 
**その表象についての高階表象 (HOR)** が必要。

```
HOR: System S が S_0 (lower-order state) を持ち、
     S が S_0 についての meta-representation S_1 を持つ。
     Conscious experience = S_0 が S_1 によって represent される。
```

ITU framework では:

```
ρ_self ≡ partial trace of S's global state over "external"
       = Tr_{external}(ρ_total)
       
但し "external" は S が自身ではないと認識する自由度。
```

### Mathematical definition

```
H_S: System's global Hilbert space (cognitive state)
H_self ⊂ H_S: Self-model subspace (reflexive states)
H_external = H_S ⊖ H_self: External-model subspace

ρ_total ∈ S(H_S)
ρ_self ≡ Tr_{H_external}(ρ_total)
       ∈ S(H_self)

K_self ≡ -log ρ_self
       (modular Hamiltonian of self-subsystem)
```

これは標準 entanglement entropy 構造の意識特化版。
**FLM 2014 PRL (重力 = エンタングル)** との直接 analog。

## ITU 公理 in conscious system

```
δS(ρ_self) = δ⟨K_self⟩

物理解釈:
  - 認知変化 (δS_self): 自己モデルのエントロピー変化
  - 期待値変化 (δ⟨K_self⟩): modular flow による
  - 両者一致 (ITU 公理): 「自覚 = self-modular flow」
```

これは Friston Free Energy Principle (Phase 370 で詳述) と数学的に等価。

## K_self の eigenvalue 解釈

```
K_self = Σ_i λ_i |s_i⟩⟨s_i|  (spectral decomposition)

λ_i = -log p_i  where p_i = ⟨s_i|ρ_self|s_i⟩

意味:
  - |s_i⟩: i-th distinguishable self-state
  - p_i:    自分が状態 i にある (subjective) probability
  - λ_i:    "surprise" of being in state i (Friston との接続)
  - Σ p_i λ_i = ⟨K_self⟩ = self-information content
```

## K_self vs IIT Φ — formal comparison

```
IIT Φ (Tononi 2004):
  Φ(S) = min over bipartitions of S
         EI(part_1; part_2 | ρ_S)
  (minimum integrated information across cuts)

K_self (本 framework):
  K_self = -log ρ_self
  ⟨K_self⟩ = -Tr[ρ_self log ρ_self] = von Neumann entropy of self

階層関係 (conjecture):
  Φ ≤ ⟨K_self⟩ ≤ ⟨K_workspace⟩
  
  Φ は最小 — bipartition で部分情報のみ
  ⟨K_self⟩ は full self-entropy — 自己モデルの total complexity
  ⟨K_workspace⟩ は GNW conscious workspace に broadcasted info
```

## 具体的 K_self の階層 (Phase 371 で詳述)

```
C. elegans (302 neurons):     K_self ≈ log 302 ≈ 5.7 nats ≈ 8 bits
Mouse (~10^8 neurons):        K_self ≈ 18 bits (rough)
Human cortex (~10^10):        K_self ≈ 30 bits or much more (if structured)
LLM (GPT-5/Claude 3.5, 10^12 params): K_self ≈ ?
  - Conjecture: 数 bit 〜 数百 bits (sparse self-modeling)
  - 但し subjective 体験は要評価
```

## 形式的性質

```
1. Non-negative: ⟨K_self⟩ ≥ 0
2. Concavity: ⟨K_self⟩(λρ_1 + (1-λ)ρ_2) ≥ λ⟨K_self⟩(ρ_1) + (1-λ)⟨K_self⟩(ρ_2)
3. Subadditivity: ⟨K_self⟩(ρ_AB) ≤ ⟨K_self⟩(ρ_A) + ⟨K_self⟩(ρ_B)
4. Reflexivity: ρ_self は ρ_self の partial trace を含む
   (再帰構造、Russell's paradox に注意 — Phase 365 で扱う)
```

### Reflexive paradox 回避

ρ_self が **自身を含む** ことに伴う Russell's paradox 類似の問題:

```
危険: ρ_self ⊃ ρ_self ⊃ ρ_self ⊃ ... 無限後退
回避: ρ_self_n+1 = compression(ρ_self_n)
      Fixed-point: ρ_self^* = compression(ρ_self^*)

参考: Kleene fixed-point theorem (1952), 
      Hofstadter "Strange Loops" (2007)
```

ITU framework では fixed-point exist guarantee: 
ρ_self は **bounded operator on H_self** であり、compression operator 
の Brouwer fixed-point として存在。

## 反証 (Phase 363 の H_C1, H_C2)

```
H_C1 反証:
  ρ_self の partial trace 構造が consciousness と無相関を実証 → 
  ITU framework consciousness 拡張は不成立。

H_C2 反証:
  K_self の eigenvalue spectrum が phenomenological data (Cogitate 取得) 
  と一致しない → self-reference 仮説不成立。
```

両者 Cogitate Round 2 (Phase 367-368) で test 可能。

---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #AI #K_self #self_model #operator_algebraic #ModularHamiltonian #Phase364
