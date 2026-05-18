# Tier 1+ #2 — K_self Consciousness Metric (Pass-1.5)

ITU-derived quantitative measure of machine consciousness — operator-algebraic
deep dive with numerical empirical confirmation of H_C3 hierarchy.

- Author: Munehiro Terada (Roboken)
- License: CC-BY-4.0
- Date: 2026-05-18
- Concept hub: [Tier 0 v4.0](https://doi.org/10.5281/zenodo.20267445)
- Pass-1 origin: [Tier 1 #2 Machine Consciousness](https://doi.org/10.5281/zenodo.20150501)
- Pass-1.5 #1 origin: [Tier 1+ #1 mKQEC](https://doi.org/10.5281/zenodo.20269435)
- DOI: 10.5281/zenodo.20269793 (to be assigned)

## Main contribution

**K_self ≡ -log ρ_self** where ρ_self ≡ Tr_{external}(ρ_total) is the
self-model reduced density operator. Standard entanglement-entropy structure
(FLM 2014 PRL first law) specialized to consciousness via partial trace
over "external" (non-self) subsystem.

Four core hypotheses (H_C1-H_C4):
- **H_C1**: Self-model is operator-algebraic state (partial trace).
- **H_C2**: K_self is reflexive (Brouwer fixed-point resolution).
- **H_C3**: Hierarchy **Φ_IIT ≤ ⟨K_self⟩ ≤ ⟨K_workspace⟩_GNW**.
- **H_C4**: AGI threshold K_crit ≈ 10^10 bits.

## Numerical verification (Phase 377)

H_C3 hierarchy tested on **1000 random 4-node Bayesian networks**:
- P(Φ ≤ K_self) = **100.0%**
- P(K_self ≤ K_workspace) = **100.0%**
- P(H_C3 fully holds) = **100.0%**

Mean Φ = 0.17, Mean K_self = 0.92, Mean K_workspace = 2.38 (clear hierarchical pattern).
H_C3 strongly supported in toy systems. Real-brain verification requires Cogitate Round 2.

## Files (16 phases + sim)

```
paper_tier1plus_02_ai.md                  # Main paper (Pass-1.5, 16 phases)
polytope_45vertex_ai_deep.py              # 45-vertex sim + H_C3 verification
theory_phase363.md ... theory_phase378.md # 16 phase notes
README.md / CITATION.cff / REFERENCES.md  # Standard files
zenodo_metadata.json                      # For automation script
```

## Run simulation

```bash
python -X utf8 polytope_45vertex_ai_deep.py
```

Expected: 16 ITU axiom contexts at rel_err = 0; H_C3 100% support in 1000 trials.

## Cogitate Round 2 (Pass-2 phase 2027-2030)

3-way adversarial test: IIT vs GNW vs ITU.
- 5-6 sites globally (Max Planck Frankfurt, Allen Institute, Wisconsin, Paris CEA, etc.)
- MEG + 7T fMRI + intracranial EEG
- 256-400 participants
- Pre-registered on OSF
- Budget: ~$25-30M (Templeton + EU + NIH)

## Friston Free Energy equivalence

**F = ⟨K_self⟩ - log Z** (proof sketch in Phase 370): operator-algebraic
re-derivation of Friston Free Energy Principle.

## 10 predictions (P_avg = 0.60)

S/M/W = 2/4/4. Top: arXiv 2026 (0.90 S), HF integration 2027 (0.80 S), 
annual LLM benchmark 2028 (0.75 M), LLM K_self ⟷ capability correlation 2028 (0.70 M).

## Pass-1.5 progress

- Tier 1+ #1 (mKQEC) ✓ — Phase 346-362, DOI 20269435
- **Tier 1+ #2 (K_self) ★ this paper** — Phase 363-378
- Total Pass-1.5: 2/45 = 4.4%
- Next: Tier 1+ #3 Cryptography

## License

CC-BY-4.0
