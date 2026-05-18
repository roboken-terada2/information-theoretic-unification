# ITU Tier 1+ #12 Cosmology — Pass-1.5 Deep Dive

**K_cosmo = -log ρ_cosmo** — Operator-algebraic Λ-CDM modular Hamiltonian.

## Contents

- `paper_tier1plus_12_cosmology.md` — main paper (16 phases)
- `theory_phase523.md` ... `theory_phase538.md` — per-phase notes
- `polytope_45vertex_cosmo_deep.py` — ITU verifications + Hubble tension Bayes/KL + polytope refresh
- `REFERENCES.md` — short bibliography
- `CITATION.cff` — citation file
- `zenodo_metadata.json` — Zenodo deposit metadata

## Numerical headline

Hubble tension between Planck CMB (early universe) and SH0ES Cepheid+SNe (late universe):

```
H0_Planck = 67.40 ± 0.50 km/s/Mpc
H0_SH0ES  = 73.04 ± 1.04 km/s/Mpc
Tension   = 4.89 σ
log Bayes factor (inconsistent/consistent) ≈ 10  (strong)

<K_cosmo>_early = 0.726 nats
<K_cosmo>_late  = 1.445 nats
KL(early ‖ late) = 15.05 nats
KL(late  ‖ early) = 56.33 nats
Jeffreys divergence J = 35.69 nats
```

ITU view: Hubble tension is a 35.7-nat irreducible KL gap between K_cosmo posteriors of early- and late-universe sub-states of ρ_cosmo.

## Run

```bash
python -X utf8 polytope_45vertex_cosmo_deep.py
```

## License

CC-BY-4.0
