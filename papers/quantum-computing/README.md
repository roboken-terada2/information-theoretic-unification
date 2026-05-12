# ITU and Fault-Tolerant Quantum Computing

**A single-axiom derivation of optimal QECC architectures.**

> 📄 **Core ITU framework (Tier 0)**: https://doi.org/10.5281/zenodo.20109210
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

| Tier | DOI | Contents | Status |
|---|---|---|---|
| Tier 0 (core) | [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210) | ITU foundational theory (42 phases) | v2.0 published |
| **Tier 1 (this paper)** | (new DOI on publication) | **ITU + QC** | **v1.0 (this release)** |
| Tier 1 (future) | TBD | ITU + AI / Cancer / Economics / ... | planned |

Each Tier 1 paper is **independent Zenodo deposit** linked to Tier 0 via
`isSupplementTo` relations.

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **43** | **✅ this release** | [[5,1,3]] code: ITU's discrete bulk-locality realization is a fault-tolerant QECC |
| 44 | planned | ITU-motivated surface code variants |
| 45 | planned | Magic-state distillation in the ITU framework |
| 46 | planned | NISQ-era hardware applications |

When phases 44-46 are completed, this paper will be re-uploaded as
v2.0 (or similar) to the same Zenodo deposit.

---

## Phase 43 Results (this release)

- **[[5,1,3]] perfect code** constructed from first principles
- **4 stabilizers** S₁ = XZZXI, S₂ = IXZZX, S₃ = XIXZZ, S₄ = ZXIXZ
- **Code distance d = 3** verified: all 15 single-qubit Pauli errors give
  distinct syndromes
- **16 decoder entries** (= 2⁴), each mapping correctly
- Numerical fault-tolerance:
  - At physical error rate $p_{\rm phys}$ up to 25%, encoded logical error
    rate remains **below the bare-qubit rate**
  - Code is **protective across the entire tested range**

---

## Reproducing the results

```bash
cd for_qc_paper
python qecc_513_fault_tolerance.py    # Phase 43 (~10 seconds)
```

Required: Python 3.10+, numpy, matplotlib.

Output: `qecc_513_fault_tolerance.png`, `summary_phase43.json`.

---

## Repository contents

```
for_qc_paper/
├── README.md                          this file
├── CITATION.cff                       machine-readable citation
├── .zenodo.json                       metadata for Zenodo upload
├── theory_phase43.md                  theoretical foundation (Phase 43)
├── theory_phase43_en.md               English version (TBA)
├── qecc_513_fault_tolerance.py        numerical experiment
├── qecc_513_fault_tolerance.png       result figure
└── summary_phase43.json               JSON results
```

After phases 44-46:
```
+ theory_phase44.md, qecc_surface_code.py, ...
+ theory_phase45.md, magic_state_distillation.py, ...
+ theory_phase46.md, nisq_applications.py, ...
```

---

## How to cite

If you cite Phase 43 specifically:

```
Terada, M. (2026). ITU and Fault-Tolerant Quantum Computing:
A Single-Axiom Derivation of Optimal QECC Architectures (v1.0.0).
Zenodo. DOI: (assigned on Zenodo upload)
```

If you cite the underlying ITU framework:

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. DOI: 10.5281/zenodo.20109210
```

Both citations recommended when using this work.

---

## License

* Text content (paper, theory note, figure): **CC-BY-4.0**
* Source code (`*.py`): **MIT License**

See `LICENSE` in the parent repository for full text.

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #1 — Quantum Computing
2026年5月12日
