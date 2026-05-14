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

> **Engineering Rectangle complete**: Tier 1 #1 (Quantum Computing, storage) + #2 (Machine Consciousness, self-model) + #3 (Cryptography, communication) + #4 (Semiconductors, substrate) form a closed engineering rectangle under the ITU axiom dS = d<K>.

## Planned Tier 1 Papers
| 5 | ITU and Cancer Biology | 59-62 | planned |
| 6 | ITU and Aging | 63-66 | planned |
| 7 | ITU and Psychiatry / FEP failures | 67-70 | planned |
| 8 | ITU and Economics / Information Markets | 71-74 | planned |
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
└── ...                                 (Tier 1 #5+ planned)
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

Plus the core ITU citation:

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109210
```

---

**寺田 宗弘 (Roboken)** — Information-Theoretic Unification research programme.
