[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20151059.svg)](https://doi.org/10.5281/zenodo.20151059)

# ITU and Cryptography

**A single-axiom framework for quantum and post-quantum information protection.**

> 📄 **This paper (Tier 1 #3) DOI**: [10.5281/zenodo.20151059](https://doi.org/10.5281/zenodo.20151059) (v1.0.0)
> 📄 **Tier 0 ITU framework**: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 📄 **Tier 1 #1: Quantum Computing**: [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391)
> 📄 **Tier 1 #2: Machine Consciousness / ASI**: [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501)
> 💻 **GitHub**: https://github.com/roboken-terada2/information-theoretic-unification/tree/main/papers/cryptography
> ✉️ **著者**: 寺田 宗弘 (Munehiro Terada), Roboken — `munehiro.terada@roboken2.com`

---

## 概要

This **Tier 1 application paper #3** applies the Information-Theoretic
Unification (ITU) framework to **cryptography**. The ITU axiom

$$\delta S(\rho_A) = \delta \mathrm{Tr}[K_A^{(0)} \rho_A]$$

simultaneously governs:
- **QECC**: protect information from noise (Phase 5, Tier 1 #1)
- **Cryptography**: protect information from adversaries (this paper)

These are **dual applications** of the same axiom.

---

## ITU Tier 1 Engineering Triangle

| Tier 1 # | Paper | DOI | Phases |
|---|---|---|---|
| #1 | [Quantum Computing](../quantum-computing/) | [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391) | 43-46 |
| #2 | [Machine Consciousness / ASI](../ai-consciousness/) | [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501) | 47-50 |
| **#3** | **Cryptography (this paper)** | **[10.5281/zenodo.20151059](https://doi.org/10.5281/zenodo.20151059)** | **51-54** |

These three papers form the ITU engineering triangle, all derived from the
same axiom $\delta S = \delta\langle K\rangle$ applied to different
information-protection challenges.

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **51** | ✅ | ITU information-theoretic security foundation |
| **52** | ✅ | BB84 + QKD detailed analysis (with HONEST NEGATIVE FINDING on naive ITU enhancement) |
| **53** | ✅ | Lattice-based PQC (Kyber, Dilithium) + ITU 3-tier framework |
| **54** | ✅ | ASI-era cryptography roadmap, 10 falsifiable predictions, policy |

---

## Key Results (v1.0.0)

| Quantity | Value |
|---|---|
| Shannon perfect-secrecy threshold | $H(K) \geq H(M)$ → $I(M;C) \approx 0$ |
| BB84 security threshold | 11% QBER (Phase 51 reproduced) |
| BB84 practical distance | ~200 km fibre (Phase 52) |
| Naive [[5,1,3]] QKD enhancement | **WORSE than BB84** (honest negative finding) |
| Kyber-1024 security | 256/240 bits (classical/quantum) |
| LWE classical attack scaling | $2^{0.292 n}$ |
| LWE quantum attack scaling | $2^{0.265 n}$ |
| ITU 3-tier combined security | 584-768 bits (vs ASI) |
| ASI cryptography arrival | ITU predicts 2030 ± 3 years |
| Falsifiable predictions | 10 |

---

## Reproducing the results

```bash
cd papers/cryptography
python itu_information_security.py     # Phase 51 (~10 seconds)
python qkd_analysis.py                 # Phase 52 (~10 seconds)
python lattice_pqc.py                  # Phase 53 (~30 seconds)
python asi_crypto_roadmap.py           # Phase 54 (~10 seconds)
```

Required: Python 3.10+, numpy, matplotlib.

Total runtime ~1-2 minutes. Outputs: 4 `.png` figures, 4 `summary_phase##.json`.

---

## Directory contents

```
papers/cryptography/
├── README.md                          this file
├── CITATION.cff                       machine-readable citation
├── .zenodo.json                       Zenodo upload metadata
│
├── theory_phase51.md                  ITU foundation for security
├── theory_phase52.md                  BB84 + QKD with ITU
├── theory_phase53.md                  Lattice PQC + 3-tier
├── theory_phase54.md                  ASI-era roadmap
│
├── itu_information_security.py / .png
├── qkd_analysis.py / .png
├── lattice_pqc.py / .png
├── asi_crypto_roadmap.py / .png
│
└── summary_phase51.json … summary_phase54.json
```

---

## How to cite

This Tier 1 #3 paper:

```
Terada, M. (2026). ITU and Cryptography: A Single-Axiom Framework
for Quantum and Post-Quantum Information Protection (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20151059
```

The core ITU framework (Tier 0):

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109210
```

---

## License

* Text content: **CC-BY-4.0**
* Source code: **MIT License**

---

## Future directions (Phase 55+)

| Tier 1 # | Topic | Phases |
|---|---|---|
| #4 | ITU + Semiconductors / Materials | 55-58 (planned) |
| #5 | ITU + Cancer Biology | 59-62 (planned) |
| #6 | ITU + Aging | 63-66 (planned) |
| ... | (full roadmap to Phase 100) | ... |

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #3 — Cryptography
2026年5月13日

Part of the *Information-Theoretic Unification* research programme.
