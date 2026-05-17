# ITU Tier 1 #22 — Condensed Matter Physics (Block A paper 6/9)

**Author:** Terada, Munehiro (Roboken)
**Date:** 2026-05-17
**Pass-1 milestone:** 71.8% (Phase 158 of 220)
**Tier 0 ITU concept DOI:** 10.5281/zenodo.20109209
**Tier 0 v3.0 DOI:** 10.5281/zenodo.20200156

This Zenodo upload archives the Tier 1 #22 paper "Condensed Matter Physics in the Information-Theoretic Unification framework" together with eight reproducible Python simulations and their figures and JSON output summaries.

## Contents

| File | Description |
|---|---|
| `paper_tier1_22_condensed_matter.md` | Consolidated paper (Phases 151-158) |
| `theory_phase151.md` | Crystal + Bloch + Phonons + Sommerfeld + K_solid |
| `theory_phase152.md` | Band theory + Drude-Sommerfeld + semiconductor physics |
| `theory_phase153.md` | Superconductivity (BCS + Meissner + Josephson + HTS) |
| `theory_phase154.md` | Magnetism (Heisenberg + Hubbard + Mott + Stoner) |
| `theory_phase155.md` | Topological matter (QHE + FQHE + TI + Weyl) |
| `theory_phase156.md` | Strongly correlated electrons (Kondo + HTS + RVB + magic angle) |
| `theory_phase157.md` | Soft matter (liquid crystals + colloids + polymers + self-assembly) |
| `theory_phase158.md` | Tier 1 #22 integration + 22-vertex polytope + 10 predictions |
| `crystal_bloch_phonon_electron.py` (+ .png + _summary.json) | Phase 151 simulation |
| `band_theory_semiconductor.py` (+ .png + _summary.json) | Phase 152 simulation |
| `bcs_meissner_josephson.py` (+ .png + _summary.json) | Phase 153 simulation |
| `heisenberg_hubbard_stoner.py` (+ .png + _summary.json) | Phase 154 simulation |
| `topological_qhe_ti.py` (+ .png + _summary.json) | Phase 155 simulation |
| `strongly_correlated_electrons.py` (+ .png + _summary.json) | Phase 156 simulation |
| `soft_matter_liquid_crystal.py` (+ .png + _summary.json) | Phase 157 simulation |
| `polytope_22vertex_predictions.py` (+ .png + _summary.json) | Phase 158 integration |

## How to reproduce

```bash
python -X utf8 crystal_bloch_phonon_electron.py
python -X utf8 band_theory_semiconductor.py
python -X utf8 bcs_meissner_josephson.py
python -X utf8 heisenberg_hubbard_stoner.py
python -X utf8 topological_qhe_ti.py
python -X utf8 strongly_correlated_electrons.py
python -X utf8 soft_matter_liquid_crystal.py
python -X utf8 polytope_22vertex_predictions.py
```

All scripts use NumPy + Matplotlib (+ SciPy for one root-finder) only. JSON summaries and PNG figures are regenerated locally.

## Headline results

- Cu Fermi energy ε_F = 7.03 eV, T_F = 8.16×10⁴ K (consistent with Phase 144).
- Wiedemann-Franz Lorenz number L_0 = 2.443×10⁻⁸ W·Ω/K² (universal).
- Si intrinsic carrier density n_i = 8.88×10⁹ /cm³ at 300 K; p-n V_bi = 0.84 V (10¹⁷ doping).
- Shockley diode forward 0.6V → 12 mA; Cu Hall R_H = -7.34×10⁻¹¹ m³/C.
- BCS universal ratio 2Δ(0)/k_BT_c = 3.529 (theory 3.53).
- Flux quantum Φ_0 = h/(2e) = 2.0678×10⁻¹⁵ Wb (CODATA exact).
- AC Josephson K_J = 2e/h = 483,598 GHz/mV (CODATA 483.5979).
- T_c progression: Hg 4.2 K (1911) → YBCO 93 K (1987) > LN₂ → LaH10 250 K (170 GPa).
- 2D AF Ising Néel order across Onsager T_c = 2.269; magnon FM ~ k² (slope 1.995), AF ~ |k| (slope 0.990).
- Stoner criterion: 6/6 metals correctly predicted (Fe/Co/Ni FM; Cu/Pd/Pt PM).
- Bloch T^(3/2) magnetization law: log-log slope = 1.500 (exact).
- von Klitzing R_K = h/e² = 25,812.807 Ω (CODATA exact).
- Chern number C ∈ {-1, 0, +1} for two-band model with transitions at m = ±2, 0.
- Bi₂Se₃ TI surface state: linear Dirac, v_F = 5×10⁵ m/s.
- Laughlin ν=1/3 fractional charge e/3 = 5.34×10⁻²⁰ C.
- Heavy-fermion γ_max/γ_Cu = 2464× (YbRh₂Si₂); d-wave gap nodes along k_x=±k_y.
- Cuprate T_c^max = 95 K at x_opt = 0.16; magic-angle graphene at 1.1° → 12.8 nm moiré.
- Maier-Saupe λ_c = 4.54, S(NI) = 0.430 (theory 4.541, 0.43).
- Flory ν: 2D = 0.668 (exact 0.75), 3D = 0.548 (best 0.588).
- 22-vertex ITU polytope: 173 edges, ⟨k⟩ = 15.73, top hubs #17-#22 all degree 21.
- Block A 6-paper P_avg progression: 0.625 → 0.660 → 0.630 → 0.610 → 0.635 → 0.665.

## COMPLETE PHYSICS BLOCK (Block A 1 + 3 + 4 + 5 + 6)

K_geom (#17) + K_cosmic (#19) + K_field (#20) + K_stat (#21) + K_solid (#22) ⇒ physics expressible in five fundamental K-states.

## 10 falsifiable predictions (2026-2050)

P_avg = 0.665 (highest in Block A), Strong 5 / Medium 5 / Weak 0. See `theory_phase158.md` Section 4 for the full table.

## Citation

```
Terada, M. (2026). Tier 1 #22: Condensed Matter Physics in the Information-Theoretic
Unification framework. Block A paper 6/9; Pass-1 71.8% milestone. Zenodo.
DOI: [10.5281/zenodo.20249191](https://doi.org/10.5281/zenodo.20249191).
```

## Repository

https://github.com/roboken-terada2/information-theoretic-unification
