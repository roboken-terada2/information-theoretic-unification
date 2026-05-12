[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20139391.svg)](https://doi.org/10.5281/zenodo.20139391)

# ITU and Fault-Tolerant Quantum Computing

**A single-axiom derivation of optimal QECC architectures.**

> 📄 **Tier 1 paper DOI (concept)**: [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391)
> 📄 **Tier 0 ITU framework**: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 💻 **GitHub**: https://github.com/roboken-terada2/information-theoretic-unification
> ✉️ **著者**: 寺田 宗弘 (Munehiro Terada), Roboken — `munehiro.terada@roboken2.com`

---

## 概要

This **Tier 1 application paper** applies the Information-Theoretic
Unification (ITU) framework — established in 42 phases of numerical
verification (Terada 2026, DOI [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210))
— to fault-tolerant quantum computing.

ITU Phase 5 (Almheiri-Dong-Harlow 2015) established that bulk locality
in AdS/CFT is mathematically equivalent to a quantum error correction
code (QECC). This paper exploits the **reverse direction**: from the
single ITU axiom

$$\delta S(\rho_A) = \delta \mathrm{Tr}[K_A^{(0)} \rho_A]$$

derive optimal QECC architectures for practical quantum computing.

---

## Tier 0 vs Tier 1 (本研究の位置づけ)

| Tier | DOI (concept) | This version | Contents |
|---|---|---|---|
| Tier 0 (core) | [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210) | v2.0.0 | ITU foundational theory (42 phases) |
| **Tier 1 (this paper)** | **[10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391)** | **[10.5281/zenodo.20139392](https://doi.org/10.5281/zenodo.20139392)** (v1.0.0) | **ITU + QC** |
| Tier 1 (future) | TBD | TBD | ITU + AI / Cancer / Economics / ... |

Each Tier 1 paper is an **independent Zenodo deposit** linked to Tier 0 via
`isSupplementTo` and `isPartOf` relations.

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **43** | **✅ included** | [[5,1,3]] perfect code: ITU's discrete bulk-locality is fault-tolerant |
| **44** | **✅ included** | Surface (toric) code threshold under bit-flip noise |
| **45** | **✅ included** | Magic state distillation via [[5,1,3]] (universal QC) |
| **46** | **✅ included** | NISQ-era resource estimates for IBM, Google, IonQ, ... |

---

## Key Results (v1.0.0)

| Quantity | Result |
|---|---|
| [[5,1,3]] code distance | $d = 3$, 15/15 single-qubit errors detected |
| Surface code empirical threshold | $p_c \approx 0.045$ (greedy decoder; theoretical ~0.103) |
| Magic distillation suppression | fit slope 1.98 (theoretical 2.0); $\epsilon_{\rm th} \approx 0.13$ |
| Iterated distillation | machine precision in 4-6 rounds |
| NISQ resource savings (ITU-optimised) | 40-60% qubit overhead reduction |

---

## Reproducing the results

```bash
cd papers/quantum-computing
python qecc_513_fault_tolerance.py     # Phase 43 (~10 seconds)
python surface_code_threshold.py       # Phase 44 (~30 seconds)
python magic_state_distillation.py     # Phase 45 (~10 seconds)
python nisq_resource_estimates.py      # Phase 46 (~5 seconds)
```

Required: Python 3.10+, numpy, scipy, matplotlib.

Total runtime ~1 minute on a modern laptop. Each script generates a `.png`
figure and a `summary_phase##.json` numerical result.

---

## Directory contents

```
papers/quantum-computing/
├── README.md                          this file
├── CITATION.cff                       machine-readable citation
├── .zenodo.json                       metadata used at upload
│
├── theory_phase43.md                  Phase 43 theoretical foundation
├── theory_phase44.md                  Phase 44: surface code
├── theory_phase45.md                  Phase 45: magic state distillation
├── theory_phase46.md                  Phase 46: NISQ resource estimates
│
├── qecc_513_fault_tolerance.py
├── qecc_513_fault_tolerance.png
├── surface_code_threshold.py
├── surface_code_threshold.png
├── magic_state_distillation.py
├── magic_state_distillation.png
├── nisq_resource_estimates.py
├── nisq_resource_estimates.png
│
└── summary_phase43.json … summary_phase46.json
```

---

## How to cite

If you cite this Tier 1 paper (recommended for QC-specific applications):

```
Terada, M. (2026). ITU and Fault-Tolerant Quantum Computing:
A Single-Axiom Derivation of Optimal QECC Architectures (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20139391
```

If you cite the underlying core ITU framework (Tier 0):

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109210
```

**Both citations are recommended** when using this work to indicate both
the focused application (Tier 1) and the underlying framework (Tier 0).

A machine-readable `CITATION.cff` is included with both DOIs encoded.

---

## License

* Text content (paper, theory notes, figures): **CC-BY-4.0**
* Source code (`*.py`): **MIT License**

See `LICENSE` in the repository root for full text.

---

## Future Phases (planned for v1.1.0+)

| Phase | Topic | Status |
|---|---|---|
| 47 | Decoder optimisation via ITU modular flow | planned |
| 48 | Concatenated [[5,1,3]] codes | planned |
| 49 | Hardware co-design with IBM/Google/IonQ | proposal |

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #1 — Quantum Computing
2026年5月12日

Part of the *Information-Theoretic Unification* research programme.
For the foundational theory (Phases 1-42), see
[10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210).
