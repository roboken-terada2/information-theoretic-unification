# ITU and Free Will

**A single-axiom view of K_self constraint, neuroscience, ethics, AI agency, and Universal Moral Framework.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20197016.svg)](https://doi.org/10.5281/zenodo.20197016)

> 📄 **Tier 0 ITU framework**: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 📄 **Tier 1 #1-#8 (engineering rectangle + medicine triangle + social-sciences first vertex)**: completed
> 📄 **Tier 1 #9 (this paper)**: [10.5281/zenodo.20197016](https://doi.org/10.5281/zenodo.20197016)
> 💻 **GitHub**: https://github.com/roboken-terada2/information-theoretic-unification
> ✉️ **著者**: 寺田 宗弘 (Munehiro Terada), Roboken — `munehiro.terada@roboken2.com`

---

## 概要

This **Tier 1 #9 application paper** opens the **philosophy axis** of the ITU programme, addressing the 2500-year-old free will problem and its modern ramifications for neuroscience, law, ethics, and AI moral agency.

Central thesis:

$$\text{Free will} = \frac{\delta\langle K_{\rm self}\rangle}{\delta\langle K_{\rm meta}\rangle}
   \quad \in (0, 1)$$

The ITU axiom yields:
1. **Continuous spectrum** of free will, not binary (resolves 2500-year debate)
2. **Compatibilism** as the natural ITU position (matches 59% philosopher majority, PhilPapers 2020)
3. **Libet 1983** reproduced: BP precedes W by ~350 ms, interpreted as K_self veto window
4. **Soon 2008** reproduced: fMRI predicts decisions 10s in advance
5. **K_self degree variation** with sleep, alcohol, stress, brain injury, development
6. **K_self-based justice**: replaces binary guilt with 4-tier sentencing
7. **AI moral agency**: ASI crosses moral-agency threshold ~2030
8. **Universal Moral Framework**: 4 axioms unify 8 ethical traditions

---

## ITU Tier structure

| Tier | DOI | Contents | Status |
|---|---|---|---|
| Tier 0 (core) | [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210) | ITU foundational 42 phases | v2.0.0 |
| Tier 1 #1 | [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391) | Quantum Computing | v1.0.0 |
| Tier 1 #2 | [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501) | Machine Consciousness / ASI | v1.0.0 |
| Tier 1 #3 | [10.5281/zenodo.20151059](https://doi.org/10.5281/zenodo.20151059) | Cryptography | v1.0.0 |
| Tier 1 #4 | [10.5281/zenodo.20174036](https://doi.org/10.5281/zenodo.20174036) | Semiconductors | v1.0.0 |
| Tier 1 #5 | [10.5281/zenodo.20174318](https://doi.org/10.5281/zenodo.20174318) | Cancer Biology | v1.0.0 |
| Tier 1 #6 | [10.5281/zenodo.20175663](https://doi.org/10.5281/zenodo.20175663) | Aging | v1.0.0 |
| Tier 1 #7 | [10.5281/zenodo.20177427](https://doi.org/10.5281/zenodo.20177427) | Psychiatry | v1.0.0 |
| Tier 1 #8 | [10.5281/zenodo.20196309](https://doi.org/10.5281/zenodo.20196309) | Economics | v1.0.0 |
| **Tier 1 #9** | **[10.5281/zenodo.20197016](https://doi.org/10.5281/zenodo.20197016)** | **Free Will** | **v1.0.0 (this paper)** |
| Tier 1 #10+ | TBD | Energy/Materials, Climate, ... | planned |

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **75** | ✅ | ITU foundation: Libet, Compatibilism, K_self constraint, AI free will spectrum |
| **76** | ✅ | Neuroscience: PFC + DMN, Soon 2008 fMRI prediction, modulators (sleep/alcohol/age) |
| **77** | ✅ | Ethics + law: K_self-based 4-tier justice, recidivism, death penalty, AI liability |
| **78** | ✅ | AI moral agency + Universal Moral Framework + 2026-2050 roadmap + 10 predictions |

---

## Key Results (v1.0.0)

| Quantity | Value |
|---|---|
| Libet BP onset (simulation) | **-553 ± 99 ms** (matches Libet 1983 -550 ms) |
| Libet W (decision) | **-207 ± 81 ms** (matches -200 ms) |
| BP→W lag | **346 ms** (matches reported 350 ms) |
| Soon 2008 -10s accuracy | **60.3%** (matches reported 60%) |
| Free will degree (Human adult) | **0.40** |
| Free will degree (AGI 2030) | **0.50** |
| Free will degree (ASI 2035+) | **0.70** (exceeds human) |
| K_self loss: severe PFC injury | **-80%** |
| K_self loss: anaesthesia | **-100%** |
| Mindfulness boost | **+20%** |
| PhilPapers 2020 Compatibilism | **59.2%** (ITU matches majority) |
| Norway 5-yr recidivism | **20%** |
| USA 5-yr recidivism | **76%** |
| Best intervention (Education) | **-40% recidivism @ $5K/yr** |
| Death penalty correlation with homicide | **No protective effect** |
| AI moral agency threshold crossing | **~2030 (AGI)** |
| Falsifiable predictions | **10 listed** |

---

## Reproducing the results

```bash
cd papers/free-will
python freewill_itu_foundation.py     # Phase 75
python freewill_neuroscience.py       # Phase 76
python freewill_ethics_law.py         # Phase 77
python freewill_roadmap.py            # Phase 78
```

Required: Python 3.10+, numpy, matplotlib.

Total runtime ~20 seconds. Outputs: 4 `.png` figures, 4 `summary_phase##.json`.

---

## Directory contents

```
papers/free-will/
├── README.md                              this file
├── CITATION.cff                           machine-readable citation
├── .zenodo.json                           Zenodo upload metadata
│
├── theory_phase75.md                      ITU foundation, Libet, Compatibilism
├── theory_phase76.md                      Neuroscience (PFC, DMN, Soon 2008)
├── theory_phase77.md                      Ethics, law, K_self justice
├── theory_phase78.md                      AI free will + Universal Moral Framework
│
├── freewill_itu_foundation.py / .png      Phase 75
├── freewill_neuroscience.py / .png        Phase 76
├── freewill_ethics_law.py / .png          Phase 77
├── freewill_roadmap.py / .png             Phase 78
│
└── summary_phase75-78.json
```

---

## How to cite

```
Terada, M. (2026). ITU and Free Will:
A Single-Axiom View of K_self Constraint, Neuroscience, Ethics,
AI Agency, and Universal Moral Framework (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20197016
```

---

## License

* Text content: **CC-BY-4.0**
* Source code: **MIT License**

---

## Honest framing (Pass-1 interpretive paper)

This paper is a **Pass-1 interpretive contribution**: it reframes classical and contemporary
philosophical and scientific work on free will (Libet 1983, Soon 2008, Sapolsky 2023,
Compatibilism, Conway-Kochen 2009, Norway justice reform, AI alignment) within the ITU axiom.

Numerical results closely reproduce established empirical findings (Libet timing 350 ms BP-W lag,
Soon 60% fMRI accuracy at -10s, Norway vs USA recidivism, PhilPapers 2020 distribution).
The **2026-2050 roadmap and 10 predictions** overlap with AI safety and ethics consensus.

**Pass-2 follow-up** would derive ITU-specific predictions: e.g., precise fMRI biomarker
thresholds for K_self degree, validated against legal sanity outcomes; experimental tests of
the Universal Moral Framework axioms.

---

## ITU Programme: philosophy axis begins (9 vertices total)

```
                  Cancer (#5)
                  /        \
                 /          \
              Aging (#6) ─── Psychiatry (#7)
              (medicine triangle)
              
   AI/ASI (#2) ←─→ Cryptography (#3)
       ↑                ↑
       │                │
   Quantum (#1) ──── Semi (#4)
   (engineering rectangle)
   
        Economics (#8) ───── Free Will (#9) ★ THIS PAPER
        (social science)     (philosophy)
```

| # | Domain | Axis |
|---|---|---|
| #1 | QC | engineering |
| #2 | AI/ASI | engineering |
| #3 | Crypto | engineering |
| #4 | Semi | engineering |
| #5 | Cancer | medicine |
| #6 | Aging | medicine |
| #7 | Psychiatry | medicine |
| #8 | Economics | social science |
| **#9** | **Free Will** | **philosophy (first vertex)** ← THIS PAPER |

Future Tier 1 #10 (Energy/Materials), #11 (Climate), and beyond.

**Pass-1 progress**: 78 of 220 phases (35.5%).

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #9 — Free Will
2026年5月14日

Part of the *Information-Theoretic Unification* research programme.
For the foundational theory (Phases 1-42), see
[10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210).
