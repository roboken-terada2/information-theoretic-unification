# ITU Tier 1 Application Papers

This directory hosts **focused application papers** that build on the
core Information-Theoretic Unification (ITU) framework.

Each Tier 1 paper:
- has its own **Zenodo deposit and DOI**
- has its own **release tag** (e.g. `qc-paper-v1.0.0`)
- links back to the Tier 0 core ITU paper via Zenodo `isSupplementTo` / `isPartOf` relations
- can be cited independently

| Tier 0 (core) | [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210) | Information-Theoretic Unification of Physics, Life, and Consciousness (42 phases) |
|---|---|---|

## Published Tier 1 Papers

| # | Paper | Concept DOI | Phases | Location | Status |
|---|---|---|---|---|---|
| 1 | [ITU and Fault-Tolerant Quantum Computing](quantum-computing/) | [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391) | 43-46 | `quantum-computing/` | ✅ v1.0.0 published |

## Planned Tier 1 Papers

| # | Paper | Phases | Status |
|---|---|---|---|
| 2 | ITU and AI / Machine Consciousness | 47-50 | planned |
| 3 | ITU and Cancer Biology | 51-54 | planned |
| 4 | ITU and Aging | 55-58 | planned |
| 5 | ITU and Psychiatry / FEP failures | 59-62 | planned |
| 6 | ITU and Economics / Information Markets | 63-66 | planned |
| 7 | ITU and Free Will | 67-70 | planned |
| 8 | ITU and Energy / Materials | 71-75 | planned |
| 9 | ITU and Climate / Earth Systems | 76-80 | planned |
| 10 | ITU and Astrobiology / SETI | 81-85 | planned |

## Structure

```
papers/
├── README.md                          this file
├── quantum-computing/                  Tier 1 #1: QC (v1.0.0)
│   ├── README.md
│   ├── CITATION.cff
│   ├── .zenodo.json
│   ├── theory_phase43-46.md
│   ├── *.py, *.png, summary*.json
│   └── ...
├── ai-consciousness/                   (planned)
├── cancer-biology/                     (planned)
└── ...
```

## How to cite a Tier 1 paper

Each Tier 1 paper has its own DOI. Cite it independently for the
focused contribution, AND cite the core ITU framework for the
underlying axiom.

Example for the Quantum Computing paper:

```
Terada, M. (2026). ITU and Fault-Tolerant Quantum Computing:
A Single-Axiom Derivation of Optimal QECC Architectures (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20139391
```

Plus the core ITU citation:

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109210
```

---

**寺田 宗弘 (Roboken)** — Information-Theoretic Unification research programme.
