# Phase 401: Sub-nm 物理限界 (quantum tunneling, atomic spacing)

Process node sub-nm regime での **physical limits** を ITU で整理。

## Quantum tunneling limit

```
Gate oxide thickness: 0.5-1 nm
Below 0.5 nm: tunneling current exponential increase
  → device fails as digital switch

High-k dielectrics (HfO2): 0.7-1 nm equivalent oxide thickness
  Used in TSMC, Intel, Samsung modern nodes
```

## Atomic spacing

```
Silicon lattice constant: 0.543 nm
Smallest feature: ~ few atoms
Sub-atomic feature: impossible (atom is fundamental)

Effective Modular Limit ≈ 0.3-0.5 nm
```

## Carrier velocity saturation

```
Electron velocity: saturates at ~10^7 cm/s
At sub-nm gate: ballistic transport regime
→ Below ~5 nm gate: device speed limited not by switching but by carrier inertia
```

## ITU framework での説明

```
K_semi_max = limited by quantum mechanics:
  ⟨K_semi⟩ ≤ log(macroscopic_volume / quantum_volume)
  quantum_volume ~ (λ_de_Broglie)³ for electron ~ (1 nm)³

⟨K_semi⟩ ≤ log(1 cm³ / 1 nm³) ≈ 21 nats ≈ 30 bits per volume

Post-CMOS technologies:
  Quantum computing (mKQEC from Tier 1+ #1)
  Photonic computing (Tier 1+ #26)
  Neuromorphic


---

#情報理論的統一理論 #ITU #Pass1.5 #Tier1plus #Semi #K_semi #Phase401
