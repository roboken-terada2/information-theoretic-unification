# Phase 384: QKD (BB84, Ekert91) ITU 再解釈

Quantum Key Distribution の ITU framework での再解釈。

## BB84 protocol (Bennett-Brassard 1984)

```
Alice prepares qubit in random basis (Z or X)
  - Z basis: |0⟩ or |1⟩
  - X basis: |+⟩ or |-⟩

Bob measures in random basis
公開: basis choice (not values)
一致するもののみ retain → shared secret key

Security: no-cloning + non-orthogonal states
  Eavesdropper Eve は disturb せずに information 得られない
```

## ITU 解釈

```
Alice's qubit state: ρ_qubit ∈ S(ℂ^2)
After Eve's eavesdrop attempt: ρ_qubit^{Eve} (partially measured)

K_qubit = -log ρ_qubit
  Original qubit: 1 bit entropy (if random)
  After eavesdrop: K_qubit increases (more uncertainty)

Detection: K_qubit(Alice ↔ Bob) ≠ K_qubit(Alice)
         → Eavesdropping detected

ITU view: K_crypto は eavesdropper の K_qubit fluctuation
         で directly measurable
```

## Ekert91 (Ekert 1991)

```
Entanglement-based QKD:
  EPR pair |Φ^+⟩ = (|00⟩ + |11⟩)/√2
  Alice + Bob each get one qubit
  Random basis measurements

Bell inequality violation (CHSH > 2) で
no local hidden variable confirmed → secure
```

## ITU view of Ekert91

```
Entangled state |Φ^+⟩ has ρ_AB = |Φ^+⟩⟨Φ^+|
Reduced ρ_A = I/2, ρ_B = I/2

K_A = log 2 = 1 bit (maximum entropy)
δS(ρ_A) = δ⟨K_A⟩ (ITU 公理)

Eavesdropping perturbs entanglement:
  ρ_AB → ρ_AB^{Eve}
  Bell inequality satisfied → eavesdropping detected
```

## QKD implementations 2024

```
Toshiba twin-field QKD (2024 Nature):
  600 km record over fiber

ID Quantique Cerberis (commercial):
  Real-world deployment

Quantum Internet (Wehner 2018):
  Stage 5 distributed quantum compute by 2045 (Phase 14)
```

## 反証

```
ITU view of QKD 反証:
  K_qubit fluctuation が eavesdropping と無相関 → ITU framework limited
  Real QKD で K_crypto measurement と security に不一致


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Crypto #K_crypto #Phase384
