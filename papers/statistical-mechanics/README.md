# ITU Tier 1 #21 — Statistical Mechanics (Block A paper 5/9)

**Author:** Terada, Munehiro (Roboken)
**Date:** 2026-05-16
**Pass-1 milestone:** 68.2% (Phase 143-150 of 220)
**Tier 0 ITU concept DOI:** 10.5281/zenodo.20109209
**Tier 0 v3.0 DOI:** 10.5281/zenodo.20200156

This Zenodo upload archives the Tier 1 #21 paper "Statistical Mechanics in the Information-Theoretic Unification framework" together with eight reproducible Python simulations and their figures and JSON output summaries.

## Contents

| File | Description |
|---|---|
| `paper_tier1_21_stat_mech.md` | Consolidated paper (Phases 143-150) |
| `theory_phase143.md` | Boltzmann + Maxwell-Boltzmann + K_stat foundation |
| `theory_phase144.md` | Fermi-Dirac + Bose-Einstein + BEC + superfluidity |
| `theory_phase145.md` | Phase transitions + critical phenomena + RG |
| `theory_phase146.md` | Non-equilibrium thermodynamics + Onsager + FDT |
| `theory_phase147.md` | Fluctuation theorems (Jarzynski + Crooks) + Landauer |
| `theory_phase148.md` | Information theory (Shannon + Jaynes + von Neumann) |
| `theory_phase149.md` | Complex systems + active matter + life thermodynamics |
| `theory_phase150.md` | Tier 1 #21 integration + 21-vertex polytope + 10 predictions |
| `boltzmann_maxwell_kstat.py` (+ .png + _summary.json) | Phase 143 simulation |
| `quantum_stat_fd_be.py` (+ .png + _summary.json) | Phase 144 simulation |
| `ising_phase_transition.py` (+ .png + _summary.json) | Phase 145 simulation |
| `nonequilibrium_response.py` (+ .png + _summary.json) | Phase 146 simulation |
| `jarzynski_crooks_landauer.py` (+ .png + _summary.json) | Phase 147 simulation |
| `shannon_jaynes_info.py` (+ .png + _summary.json) | Phase 148 simulation |
| `complex_active_soc.py` (+ .png + _summary.json) | Phase 149 simulation |
| `polytope_21vertex_predictions.py` (+ .png + _summary.json) | Phase 150 integration |

## How to reproduce

```bash
python -X utf8 boltzmann_maxwell_kstat.py
python -X utf8 quantum_stat_fd_be.py
python -X utf8 ising_phase_transition.py
python -X utf8 nonequilibrium_response.py
python -X utf8 jarzynski_crooks_landauer.py
python -X utf8 shannon_jaynes_info.py
python -X utf8 complex_active_soc.py
python -X utf8 polytope_21vertex_predictions.py
```

All scripts use NumPy + Matplotlib only. JSON summaries and PNG figures are regenerated locally.

## Headline results

- Maxwell-Boltzmann v_p, v̄, v_rms for N₂ at 300 K: 422 / 476 / 517 m/s.
- Cu electron Fermi energy ε_F = 7.05 eV, T_F = 8.18×10⁴ K (degenerate at room T).
- Rb-87 BEC critical temperature T_BEC = 398 nK (Cornell-Wieman-Ketterle 1995 order of magnitude).
- Chandrasekhar mass M_Ch ≈ 1.46 M_⊙.
- 2D Ising T_c = 2.269 J/k_B (Onsager exact) reproduced via Monte Carlo.
- Einstein diffusion D = 4.40×10⁻¹³ m²/s vs Langevin D_fit = 4.92×10⁻¹³ (ratio 1.12).
- Jarzynski equality: ⟨e^{-βW}⟩ = e^{-βΔF}; ΔF estimated to 0.07 vs truth 0 in harmonic-spring switching.
- Landauer limit at 300 K: k_BT ln 2 = 17.9 meV/bit.
- Bell state |Φ+⟩: S(ρ_AB) = 0, S(ρ_A) = ln 2, quantum mutual information = 2 ln 2.
- BTW sandpile avalanche exponent τ ≈ 1.18; Barabási-Albert γ ≈ 2.73.
- Human metabolic entropy output: 0.32 W/K = 2.9×10²⁷ bit/day.
- 21-vertex ITU polytope: 152 edges, ⟨k⟩ = 14.48, top hub degree 20.
- Block A 5-paper P_avg progression: 0.625 → 0.660 → 0.630 → 0.610 → 0.635.

## UNIVERSAL FOUNDATION (Block A 1 + 3 + 4 + 5)

K_geom (#17) + K_cosmic (#19) + K_field (#20) + K_stat (#21) ⇒ all of physics expressible in four fundamental K-states.

## 10 falsifiable predictions (2026-2050)

P_avg = 0.635, Strong 5 / Medium 4 / Weak 1. See `theory_phase150.md` Section 5 for the full table.

## Citation

```
Terada, M. (2026). Tier 1 #21: Statistical Mechanics in the Information-Theoretic
Unification framework. Block A paper 5/9; Pass-1 68.2% milestone. Zenodo.
DOI: [10.5281/zenodo.20237082](https://doi.org/10.5281/zenodo.20237082).
```

## Repository

https://github.com/roboken-terada2/information-theoretic-unification
