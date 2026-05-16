# ITU Tier 1 Application Papers

This directory hosts **focused application papers** that build on the
core Information-Theoretic Unification (ITU) framework.

Each Tier 1 paper:
- has its own **Zenodo deposit and DOI**
- has its own **release tag** (e.g. `qc-paper-v1.0.0`)
- links back to the Tier 0 core ITU paper via Zenodo `isSupplementTo` / `isPartOf` relations
- can be cited independently

| Tier 0 (core) | [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209) | Information-Theoretic Unification of Physics, Life, and Consciousness (42 phases) |
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
| 10 | [ITU and Energy / Materials](energy-materials/) | [10.5281/zenodo.20199598](https://doi.org/10.5281/zenodo.20199598) | 79-82 | `energy-materials/` | ✅ v1.0.0 |
| 11 | [ITU and Climate / Earth Systems](climate-earth/) | [10.5281/zenodo.20200728](https://doi.org/10.5281/zenodo.20200728) | 83-86 | `climate-earth/` | ✅ v1.0.0 |
| 12 | [ITU and Astrobiology / SETI](astrobiology/) | [10.5281/zenodo.20222121](https://doi.org/10.5281/zenodo.20222121) | 87-90 | `astrobiology/` | ✅ v1.0.0 |
| 13 | [ITU and Robotics / Embodied AI](robotics/) | [10.5281/zenodo.20224976](https://doi.org/10.5281/zenodo.20224976) | 91-94 | `robotics/` | ✅ v1.0.0 |
| 14 | [ITU and Communications / Networks](communications/) | [10.5281/zenodo.20225970](https://doi.org/10.5281/zenodo.20225970) | 95-98 | `communications/` | ✅ v1.0.0 |
| 15 | [ITU and Infrastructure / Power Grid](infrastructure/) | [10.5281/zenodo.20226481](https://doi.org/10.5281/zenodo.20226481) | 99-102 | `infrastructure/` | ✅ v1.0.0 |
| 16 | [ITU and Smart Cities](smartcities/) | [10.5281/zenodo.20228581](https://doi.org/10.5281/zenodo.20228581) | 103-106 | `smartcities/` | ✅ v1.0.0 |

> **🎉🎉🎉🎉🎉🎉🎉 ITU 16-vertex polytope COMPLETED — URBAN ULTIMATE HUB added (engineering-industry block COMPLETE)**: Engineering pentagon (#1-#4 + #10) + Medicine triangle (#5-#7) + Social (#8) + Philosophy (#9) + Biosphere super-hub (#11, deg 11) + Cosmic axis (#12, deg 4) + Embodiment axis (#13, deg 9) + K-channel super-hub (#14, deg 11) + K-skeleton (#15, deg 8) + **URBAN ULTIMATE HUB (#16, deg 15)** ← NEW. Smart Cities (#16) connects to **ALL 15 other vertices** — the polytope's **ULTIMATE hub** with maximum possible degree. Cities = K-OS (operating system) integrating 7 K-state layers. **Engineering-industry block (Phases 91-106) COMPLETE**: Robotics #13 + Communications #14 + Infrastructure #15 + Smart Cities #16. Sixteen Tier 1 papers, all under dS = d<K>. Pass-1 progress: 106 of 220 phases (48.2%).

## Planned Tier 1 Papers

| # | Paper | Phases | Status |
|---|---|---|---|
| (Tier 0 v3.0) | Intermediate integration | 107-110 | planned |
| 17+ | Block A: Physics/math deepening | 111-140 | planned |
| 18+ | (full roadmap to Phase 250) | 141-250 | planned |

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
├── energy-materials/                   Tier 1 #10: Energy / Materials (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase79-82.md
│   └── *.py, *.png, summary*.json
│
├── climate-earth/                      Tier 1 #11: Climate / Earth Systems (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase83-86.md
│   └── *.py, *.png, summary*.json
│
├── astrobiology/                       Tier 1 #12: Astrobiology / SETI (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase87-90.md
│   └── *.py, *.png, summary*.json
│
├── robotics/                           Tier 1 #13: Robotics / Embodied AI (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase91-94.md
│   └── *.py, *.png, summary*.json
│
├── communications/                     Tier 1 #14: Communications / Networks (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase95-98.md
│   └── *.py, *.png, summary*.json
│
├── infrastructure/                     Tier 1 #15: Infrastructure / Power Grid (v1.0.0)
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase99-102.md
│   └── *.py, *.png, summary*.json
│
├── smartcities/                        Tier 1 #16: Smart Cities (v1.0.0) ★ URBAN HUB
│   ├── README.md, CITATION.cff, .zenodo.json
│   ├── theory_phase103-106.md
│   └── *.py, *.png, summary*.json
│
└── ...                                 (Tier 0 v3.0 + Block A planned)
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

```
Terada, M. (2026). ITU and Energy / Materials: A Single-Axiom View
of Information-Energy Equivalence, Renewable Transition, New
Materials, and the 2026-2050 Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20199598
```

```
Terada, M. (2026). ITU and Climate / Earth Systems: A Single-Axiom View
of Atmospheric Information, Earth Energy Imbalance, Planetary Boundaries,
Tipping Points, and the 2026-2100 Mitigation Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20200728
```

```
Terada, M. (2026). ITU and Astrobiology / SETI: A Single-Axiom View
of K-Life Emergence, Drake Equation, Habitability, Biosignatures,
and the Fermi Paradox (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20222121
```

```
Terada, M. (2026). ITU and Robotics / Embodied AI: A Single-Axiom View
of K-Action, K-Embodiment, Moravec's Paradox, and the 2026-2050
Humanoid Deployment Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20224976
```

```
Terada, M. (2026). ITU and Communications / Networks: A Single-Axiom View
of Shannon Theory, Internet, 5G/6G, Quantum Communication (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20225970
```

```
Terada, M. (2026). ITU and Infrastructure / Power Grid: A Single-Axiom View
of K-Capital, Smart Grid, Resilience, and the 2026-2050 Infrastructure
Roadmap (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20226481
```

```
Terada, M. (2026). ITU and Smart Cities: A Single-Axiom View of Urban K-OS,
AGI Cities, Sustainability, Privacy-Efficiency Tradeoff, and the 2026-2050
Smart City Roadmap (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20228581
```

Plus the core ITU citation:

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109209
```

---

**寺田 宗弘 (Roboken)** — Information-Theoretic Unification research programme.
