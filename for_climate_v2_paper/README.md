# ITU Tier 1+ #11 Climate — Pass-1.5 Deep Dive

**K_climate = -log ρ_climate** — Operator-algebraic Earth system modular Hamiltonian.

## Contents

- `paper_tier1plus_11_climate.md` — main paper (16 phases)
- `theory_phase507.md` ... `theory_phase522.md` — per-phase notes
- `polytope_45vertex_climate_deep.py` — ITU verifications + Keeling Curve quadratic fit + radiative forcing K_radiation + polytope refresh
- `REFERENCES.md` — short bibliography
- `CITATION.cff` — citation file
- `zenodo_metadata.json` — Zenodo deposit metadata

## Numerical headline

Keeling Curve quadratic fit on Mauna Loa CO₂ 1958-2024:

```
CO2(t) = 314.72 + 0.7683·(t−1958) + 0.01326·(t−1958)²  ppm
RMSE = 0.7 ppm,   R² = 0.99965
Projection 2030: 439 ppm,   2050: 498 ppm  (BAU)
DeltaF(2024 vs 280 ppm) = 2.21 W/m²  =  59% of 2xCO2 doubling
T_eq committed @ lambda=1.2: 1.84 K
ECS implied = 3.09 K   (matches IPCC AR6 best 3.0)
```

## Run

```bash
python -X utf8 polytope_45vertex_climate_deep.py
```

## License

CC-BY-4.0
