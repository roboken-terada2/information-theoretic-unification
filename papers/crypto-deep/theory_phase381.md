# Phase 381: K_crypto = -log ρ_key 厳密定義

K_crypto の operator-algebraic 厳密定義。

## Density operator over key space

```
Cryptographic system S は:
  Keyspace H_K = ℂ^|K|  (key space basis)
  Hilbert space H_S = H_K ⊗ H_other

Pure key state: |k⟩ ∈ H_K
Random key: ρ_key = Σ_k p_k |k⟩⟨k|
  uniform prior: p_k = 1/|K|
  ⇒ ρ_key = I_K / |K|, ⟨K_crypto⟩ = log |K|
```

## Conditional on public information

```
Public information P (ciphertext, public key, ...) で:
  ρ_key|P = ρ_key を P で条件付け
  Bayes update:
    p_k|P ∝ Pr[P | key=k] · p_k

K_crypto|P = -log ρ_key|P
⟨K_crypto|P⟩ = -Σ_k p_k|P log p_k|P
            = H(K | P)  (conditional Shannon entropy)
```

これは **Shannon entropy (1948)** の operator-algebraic 拡張。

## Quantum-classical hybrid

```
古典 cryptography: ρ_key は diagonal (classical mixture)
Quantum-classical hybrid (BB84 等):
  ρ_key は superposition coherent (off-diagonal terms)

ITU view では両者 unified:
  K_crypto = -log ρ_key (どちらでも同じ formula)

但し attacker の measurement strategy で
classical vs quantum で hardness 異なる。


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Crypto #K_crypto #Phase381
