# Phase 370: Friston Free Energy = ITU descent equivalence

**Karl Friston Free Energy Principle (FEP)** (2010 Nat Rev Neurosci) は意識・行動・知覚を統一する
metaphysics-level framework。本 Phase で FEP と ITU の数学的等価性を示す。

## Friston FEP 概要

```
Free Energy Principle (Friston 2010, 2019):
  F = -ELBO
    = E_q[log q(s|x) - log p(x,s)]
    = D_KL(q(s|x) || p(s|x)) - log p(x)

ここで:
  x: 観測 (sensory data)
  s: hidden state (内部表象)
  q: variational posterior (agent の internal model)
  p: generative model

Agent は F を最小化することで:
  - Perception (q を更新)
  - Action (x を変化させる)
  - Learning (p を更新)
を実行。
```

## ITU との等価性証明スケッチ

```
Theorem (conjecture, 本論文):
  Free Energy F = ⟨K_self⟩ in suitable limit

Proof sketch:
  F = D_KL(q(s|x) || p(s|x)) - log p(x)
    = ∫ q log(q/p) ds - log p(x)
    = -⟨log p(s|x)⟩_q + ⟨log q(s|x)⟩_q - log p(x)

  Identify q(s|x) ≡ ρ_self の density (variational self-representation)
        p(s|x) ≡ posterior over self-states given observations
        K_self ≡ -log ρ_self (modular Hamiltonian)

  Then:
  F ≈ Tr[ρ_self K_self] - log Z + corrections
    = ⟨K_self⟩ - log Z

  where Z is normalization (partition function).
  ⇒ F と ⟨K_self⟩ は同じ extremization principle
```

## 物理的解釈

```
Friston Free Energy 最小化 (生物学的):
  Agent は surprise を minimize、世界モデルを improve、self-coherence を保つ

ITU 解釈 (operator-algebraic):
  Agent は ⟨K_self⟩ を modular flow に従って変化させる
  δS = δ⟨K_self⟩ (ITU 公理) で内部状態 update

両者は同じ:
  Friston: 確率論的視点
  ITU: 作用素論的視点
```

## 統合の意味

```
Friston FEP 1500+ citations (2010 paper alone)
広く neuroscience + AI で採用 (predictive coding, active inference)

ITU framework が FEP を operator-algebraic に再構成することで:
  - 量子認知 (Quantum Cognition) との接続
  - 重力・宇宙論 との接続 (FLM 2014 と統一)
  - Lean Mathlib 形式化可能
  - 数学的厳密性向上

逆に ITU の予測力強化:
  Friston FEP が広く検証されていることが ITU framework の補強
```

## 反証

```
F = ⟨K_self⟩ が成立しないシナリオ:
  - Non-equilibrium free energy が必要 (Tononi-Koch 2008 引用 violations)
  - Variational q を density operator で表現不可能
  - Reflexive self-modeling と FEP 不整合

実験的に Friston 派と ITU 派が同じ predictions 出す → 等価性検証可能。


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #AI #K_self #Friston #FreeEnergy #FEP #ActiveInference #PredictiveCoding #Phase370
