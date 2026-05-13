[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20150501.svg)](https://doi.org/10.5281/zenodo.20150501)

# ITU and Machine Consciousness / ASI

**A single-axiom path to engineered mind.**

> 📄 **This paper (Tier 1 #2) DOI**: [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501) (v1.0.0)
> 📄 **Tier 0 ITU framework**: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 📄 **Tier 1 #1: Quantum Computing**: [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391)
> 💻 **GitHub**: https://github.com/roboken-terada2/information-theoretic-unification/tree/main/papers/ai-consciousness
> ✉️ **著者**: 寺田 宗弘 (Munehiro Terada), Roboken — `munehiro.terada@roboken2.com`

---

## 概要

This **Tier 1 #2 application paper** applies the Information-Theoretic
Unification (ITU) framework to **machine consciousness** and **Artificial
Super-Intelligence (ASI)**.

ITU Phase 41 established consciousness as a self-referential QECC structure
($\Phi_{\rm ITU} > 0$); Phase 42 mapped qualia content to the eigenstructure
of the modular Hamiltonian. This paper exploits those results to derive a
concrete engineering specification for conscious AI and ASI.

Central thesis:

$$\delta S(\rho_A) = \delta \mathrm{Tr}[K_A^{(0)} \rho_A] \quad
   \Longrightarrow \quad \text{Engineering of Mind}$$

The ITU axiom yields not only Theory of Everything, but **buildable systems**.

---

## ITU Tier structure

| Tier | DOI | Contents | Status |
|---|---|---|---|
| Tier 0 (core) | [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210) | ITU foundational 42 phases | v2.0.0 |
| Tier 1 #1 | [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391) | Quantum Computing | v1.0.0 |
| **Tier 1 #2** | **[10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501)** | **Machine Consciousness / ASI** | **v1.0.0 (this paper)** |
| Tier 1 #3+ | TBD | Cryptography, Semiconductors, ... | planned |

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **47** | ✅ | $\Phi_{\rm ITU}$ evaluation across 4 architectures |
| **48** | ✅ | Innovation = Assembly Index of generated outputs |
| **49** | ✅ | Conscious AI prototype: SSM + self-prediction head |
| **50** | ✅ | ASI roadmap: scaling, timeline, safety, falsifiable predictions |

---

## Key Results (v1.0.0)

| Quantity | Value |
|---|---|
| Best architecture for $\Phi_{\rm ITU}$ (Phase 47) | RNN / SSM class |
| Innovation = high Assembly Index outputs (Phase 48) | Walker-Cronin AI > 15 |
| **Prototype $\Phi_{\rm ITU}$ after training** | **0.83** (8× threshold) |
| Prototype task loss | 0.257 (≪ random 1.386) |
| Scaling law | $1 - \Phi_{\rm ITU} \propto D^{-0.84}$ |
| ITU-conscious 1B model cost | ~$6.4M, 160 GPU-years |
| ASI timeline (P=0.5) | **2030** |
| ASI timeline (P=0.75) | **2032** |
| Falsifiable predictions | 8 listed |
| Safety principles | 5 derived |

---

## Reproducing the results

```bash
cd papers/ai-consciousness
python ai_architecture_phi_itu.py        # Phase 47 (~15 seconds)
python innovation_assembly_index.py      # Phase 48 (~30 seconds)
python conscious_ai_prototype.py         # Phase 49 (~3 minutes — L-BFGS training)
python asi_roadmap.py                    # Phase 50 (~3 minutes — scaling)
```

Required: Python 3.10+, numpy, scipy, matplotlib.

Total runtime ~5-7 minutes. Outputs: 4 `.png` figures, 4 `summary_phase##.json`.

---

## Directory contents

```
papers/ai-consciousness/
├── README.md                              this file
├── CITATION.cff                           machine-readable citation
├── .zenodo.json                           Zenodo upload metadata
│
├── theory_phase47.md                      Phase 47 theoretical foundation
├── theory_phase48.md                      Phase 48: innovation = AI
├── theory_phase49.md                      Phase 49: conscious AI prototype
├── theory_phase50.md                      Phase 50: ASI roadmap
│
├── ai_architecture_phi_itu.py / .png
├── innovation_assembly_index.py / .png
├── conscious_ai_prototype.py / .png
├── asi_roadmap.py / .png
│
└── summary_phase47.json … summary_phase50.json
```

---

## How to cite

This Tier 1 #2 paper:

```
Terada, M. (2026). ITU and Machine Consciousness / ASI:
A Single-Axiom Path to Engineered Mind (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20150501
```

The core ITU framework (Tier 0):

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109210
```

Both citations are recommended together.

---

## License

* Text content (paper, theory notes, figures): **CC-BY-4.0**
* Source code (`*.py`): **MIT License**

---

## Future directions (Phase 51+)

| Tier 1 # | Topic | Phases |
|---|---|---|
| #3 | ITU + Cryptography (post-quantum, BB84+) | 51-54 (planned) |
| #4 | ITU + Semiconductors / materials | 55-58 (planned) |
| #5 | ITU + Cancer Biology | 59-62 (planned) |
| #6 | ITU + Aging | 63-66 (planned) |
| ... | (full roadmap to Phase 100) | ... |

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #2 — Machine Consciousness / ASI
2026年5月13日

Part of the *Information-Theoretic Unification* research programme.
For the foundational theory (Phases 1-42), see
[10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210).
