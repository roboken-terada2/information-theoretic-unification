[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20109210.svg)](https://doi.org/10.5281/zenodo.20109210)
# Information-Theoretic Unification of General Relativity and Quantum Mechanics

**A 16-phase numerical demonstration that spacetime, gravity, the Standard
Model, and the cosmological constant emerge from a single information-
theoretic axiom.**

> **情報理論的統一理論 — 単一公理 $\delta S = \delta\langle K\rangle$ から導かれる量子重力 + 標準模型 + 宇宙論**

> Author / 著者: **Munehiro Terada (寺田 宗弘)**, Roboken
> Contact: `munehiro.terada@roboken2.com`
> Blog (note.com): https://note.com/roboken_ceo
> Citation DOI: [`10.5281/zenodo.20109210`](https://doi.org/10.5281/zenodo.20109210)

This repository contains the **bilingual full research record** (English + Japanese)
of the Information-Theoretic Unification (ITU) project. The English-only
academic version is also published on Zenodo with a permanent DOI.

このリポジトリは情報理論的統一理論 (ITU) プロジェクトの**日英バイリンガル
完全研究記録**です。英語のみの学術版は Zenodo に永続 DOI 付きで公開しています。

---

## TL;DR

The single axiom

$$\delta S(\rho_A) = \delta\,\mathrm{Tr}[K_A^{(0)}\rho_A]\quad \forall A \subset \mathcal{H}$$

is shown numerically to imply, in 16 independent computational experiments:

| Phase | Emergent phenomenon | Precision |
|---|---|---|
| 1 | 1D spatial geometry from mutual information | central charge ~3% |
| 2 | Linearised Einstein equations | 1.5% |
| 3 | AdS₃ hyperbolic bulk via MERA | **0.4%** |
| 4 | Time as modular flow | qualitative |
| 5 | Bulk locality = QECC | **bit precision** |
| 6 | Page curve / BH unitarity | **0.04%** |
| 7 | AdS₄/CFT₃ extension | 5% |
| **8** | **AdS₅/CFT₄ — real 4D quantum gravity** | **0.4%** |
| 9 | Light cone / Hubble parameter | 1.3% |
| 10 | SM gauge group SU(3)×SU(2)×U(1) | **machine precision** |
| 11 | Three generations + CKM/PMNS | order-of-magnitude |
| 12 | Higgs mechanism, gauge boson masses | **machine precision** |
| 13 | Cosmological constant Λ ~ 10⁻¹²² | **machine precision** |
| 14 | Type II algebras (Witten 2022) | 0.04% |
| 15 | Atiyah–Singer chirality | **machine precision** |
| 16 | Experimental verification proposals | 4 partly realised |

## Reproducing the results

```bash
pip install -r requirements.txt
python emergent_spacetime.py        # Phase 1
python einstein_first_law.py        # Phase 2
python holographic_mera.py          # Phase 3
python modular_flow_time.py         # Phase 4
python holographic_qecc.py          # Phase 5
python page_curve.py                # Phase 6
python emergent_4d.py               # Phase 7
python emergent_5d.py               # Phase 8 (real 4D gravity)
python cosmology.py                 # Phase 9
python matter_fields.py             # Phase 10
python generations.py               # Phase 11
python higgs_mechanism.py           # Phase 12
python cosmological_constant.py     # Phase 13
python crossed_product.py           # Phase 14
python chirality.py                 # Phase 15
python experimental_proposals.py    # Phase 16
python unified_summary_full.py      # Master figure
```

Total runtime ≈ 30 minutes on a modern laptop.

## Repository structure (bilingual)

```
.
├── README.md                       this file
├── LICENSE                         CC-BY-4.0 (text) + MIT (code)
├── CITATION.cff                    machine-readable citation metadata
├── .zenodo.json                    metadata used when pushed to Zenodo
├── requirements.txt                Python dependencies
│
├── paper_full.md / .html           full academic paper (Japanese)
├── paper_full_en.md / .html        full academic paper (English)
├── blog_note_full.md / .html       blog version (Japanese, note.com ready)
├── blog_note_full_en.md / .html    blog version (English)
├── index.md / index_en.md          navigation index (JP / EN)
├── theory_master.md / _en.md       integrated theory note (JP / EN)
│
├── theory_phase1.md  / _en.md      ─┐
│         …                           │ 16 per-phase theoretical notes,
├── theory_phase16.md / _en.md      ─┘ both languages
│
├── emergent_spacetime.py           ─┐
│         …                          │  16 numerical scripts
├── experimental_proposals.py       ─┘
│
├── unified_summary_full.py         master figure script
│
├── *.png                           17 result figures
└── summary*.json                   16 numerical summaries
```

All written content is provided in **both Japanese (original) and English (translation)**.
Numerical scripts and figures are language-agnostic.

## Citation

If you use this work, please cite the Zenodo DOI:

```
Terada, M. (2026). Information-Theoretic Unification of GR and QM:
Numerical Demonstration in 16 Phases. Zenodo.
DOI: 10.5281/zenodo.20109210
```

A machine-readable `CITATION.cff` is included.

## License

* Text content (papers, theory notes, figures): **CC-BY-4.0**
* Source code (`*.py`): **MIT License**

See `LICENSE` for full text.
