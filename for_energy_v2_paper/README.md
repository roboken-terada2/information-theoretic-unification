# ITU Tier 1+ #10 Energy & Materials — Pass-1.5 Deep Dive

**K_energy = -log ρ_energy** — Operator-algebraic energy system modular Hamiltonian.

## Contents

- `paper_tier1plus_10_energy.md` — main paper (16 phases)
- `theory_phase491.md` ... `theory_phase506.md` — per-phase notes
- `polytope_45vertex_energy_deep.py` — ITU axiom verifications + Wright's Law numerical fit + polytope refresh
- `REFERENCES.md` — short bibliography
- `CITATION.cff` — citation file
- `zenodo_metadata.json` — Zenodo deposit metadata

## Numerical headline

Wright's Law fit on BNEF battery pack prices 2010-2024 (15 yr, $1,100 → $115/kWh):

```
P = a · Q^b   with  a = 196.7,  b = -0.4199
Learning rate = 25.3% per cumulative-production doubling
R² ≈ 0.954
K_cost reduction per doubling = 0.291 nats
```

## Run

```bash
python -X utf8 polytope_45vertex_energy_deep.py
```

## License

CC-BY-4.0
