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

| # | Paper | DOI | Phases | Location | Status |
|---|---|---|---|---|---|
| 1 | [ITU and Fault-Tolerant Quantum Computing](quantum-computing/) | [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391) | 43-46 | `quantum-computing/` | ✅ v1.0.0 |
| 2 | [ITU and Machine Consciousness / ASI](ai-consciousness/) | [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501) | 47-50 | `ai-consciousness/` | ✅ v1.0.0 |
| 3 | [ITU and Cryptography](cryptography/) | [10.5281/zenodo.20151059](https://doi.org/10.5281/zenodo.20151059) | 51-54 | `cryptography/` | ✅ v1.0.0 |
| 4 | [ITU and Semiconductors](semiconductors/) | [10.5281/zenodo.20174036](https://doi.org/10.5281/zenodo.20174036) | 55-58 | `semiconductors/` | ✅ v1.0.0 |
| 5 | [ITU and Cancer Biology](cancer-biology/) | [10.5281/zenodo.20174318](https://doi.org/10.5281/zenodo.20174318) | 59-62 | `cancer-biology/` | ✅ v1.0.0 |
| 6 | [ITU and Aging](aging/) | [10.5281/zenodo.20175663](https://doi.org/10.5281/zenodo.20175663) | 63-66 | `aging/` | ✅ v1.0.0 |
| 7 | [ITU and Psychiatry](psychiatry/) | [10.5281/zenodo.20177427](https://doi.org/10.5281/zenodo.20177427) | 67-70 | `psychiatry/` | ✅ v1.0.0 |
| 8 | [ITU and Economics](economics/) | [10.5281/zenodo.20196309](https://doi.org/10.5281/zenodo.20196309) | 71-74 | `economics/` | ✅ v1.0.0 |
| 9 | [ITU and Free Will](free-will/) | [10.5281/zenodo.20197016](https://doi.org/10.5281/zenodo.20197016) | 75-78 | `free-will/` | ✅ v1.0.0 |

> **🎉 ITU polytope expanded — 9 vertices and growing**: Tier 1 #1-#4 form the **engineering rectangle**. Tier 1 #5-#7 form the **medicine triangle**. **Tier 1 #8 (Economics) opens the social-sciences axis** and **Tier 1 #9 (Free Will/Ethics) opens the philosophy axis**. Nine Tier 1 papers, all under the ITU axiom dS = d<K>. Pass-1 progress: 78 of 220 phases (35.5%).

## Planned Tier 1 Papers

| # | Paper | Phases | Status |
|---|---|---|---|
| 9 | ITU and Free Will | 75-78 | planned |
| 10 | ITU and Energy / Materials | 79-82 | planned |
| 11 | ITU and Climate / Earth Systems | 83-86 | planned |
| 12 | ITU and Astrobiology / SETI | 87-90 | planned |

## Structure

```
papers/
├── README.md                          this file
│
├── quantum-computing/                  Tier 1 #1: QC (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase43-46.md
│   └── *.py, *.png, summary*.json
│
├── ai-consciousness/                   Tier 1 #2: AI/ASI (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase47-50.md
│   └── *.py, *.png, summary*.json
│
├── cryptography/                       Tier 1 #3: Cryptography (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase51-54.md
│   └── *.py, *.png, summary*.json
│
├── semiconductors/                     Tier 1 #4: Semiconductors (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase55-58.md
│   └── *.py, *.png, summary*.json
│
├── cancer-biology/                     Tier 1 #5: Cancer Biology (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase59-62.md
│   └── *.py, *.png, summary*.json
│
├── aging/                              Tier 1 #6: Aging (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase63-66.md
│   └── *.py, *.png, summary*.json
│
├── psychiatry/                         Tier 1 #7: Psychiatry (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase67-70.md
│   └── *.py, *.png, summary*.json
│
├── economics/                          Tier 1 #8: Economics (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase71-74.md
│   └── *.py, *.png, summary*.json
│
├── free-will/                          Tier 1 #9: Free Will / Ethics (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase75-78.md
│   └── *.py, *.png, summary*.json
│
└── ...                                 (Tier 1 #10+ planned)
```

## How to cite a Tier 1 paper

Each Tier 1 paper has its own DOI. Cite it independently for the
focused contribution, AND cite the core ITU framework for the
underlying axiom.

Examples:

```
Terada, M. (2026). ITU and Fault-Tolerant Quantum Computing:
A Single-Axiom Derivation of Optimal QECC Architectures (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20139391
```

```
Terada, M. (2026). ITU and Machine Consciousness / ASI:
A Single-Axiom Path to Engineered Mind (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20150501
```

```
Terada, M. (2026). ITU and Cryptography: A Single-Axiom Framework
for Quantum and Post-Quantum Information Protection (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20151059
```

```
Terada, M. (2026). ITU and Semiconductors: A Single-Axiom Foundation
for Devices, Scaling, Beyond-CMOS, and the 2026-2040 Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20174036
```

```
Terada, M. (2026). ITU and Cancer Biology: A Single-Axiom View of
Cellular Breakdown, Metabolism, Immunology, and the 2026-2040
Treatment Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20174318
```

```
Terada, M. (2026). ITU and Aging: A Single-Axiom View of K_organism
Decay, Three-Pillar Mechanisms, Interventions, and the 2026-2050
Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20175663
```

```
Terada, M. (2026). ITU and Psychiatry: A Single-Axiom View of
K_brain Failures, Predictive Coding, Drug Mechanisms, and the
2026-2050 Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20177427
```

```
Terada, M. (2026). ITU and Economics: A Single-Axiom View of
Markets, Bubbles, Inequality, AI Labor Displacement, and the
2026-2050 Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20196309
```

```
Terada, M. (2026). ITU and Free Will: A Single-Axiom View of
K_self Constraint, Neuroscience, Ethics, AI Agency, and Universal
Moral Framework (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20197016
```

Plus the core ITU citation:

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109210
```

---

**寺田 宗弘 (Roboken)** — Information-Theoretic Unification research programme.
