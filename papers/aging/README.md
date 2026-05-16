# ITU and Aging

**A single-axiom view of K_organism decay, three-pillar mechanisms, interventions, and the 2026-2050 roadmap.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20175663.svg)](https://doi.org/10.5281/zenodo.20175663)

> 📄 **Tier 0 ITU framework**: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> 📄 **Tier 1 #1: Quantum Computing**: [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391)
> 📄 **Tier 1 #2: Machine Consciousness / ASI**: [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501)
> 📄 **Tier 1 #3: Cryptography**: [10.5281/zenodo.20151059](https://doi.org/10.5281/zenodo.20151059)
> 📄 **Tier 1 #4: Semiconductors**: [10.5281/zenodo.20174036](https://doi.org/10.5281/zenodo.20174036)
> 📄 **Tier 1 #5: Cancer Biology**: [10.5281/zenodo.20174318](https://doi.org/10.5281/zenodo.20174318)
> 📄 **Tier 1 #6 (this paper)**: [10.5281/zenodo.20175663](https://doi.org/10.5281/zenodo.20175663)
> 💻 **GitHub**: https://github.com/roboken-terada2/information-theoretic-unification
> ✉️ **著者**: 寺田 宗弘 (Munehiro Terada), Roboken — `munehiro.terada@roboken2.com`

---

## 概要

This **Tier 1 #6 application paper** is the second medicine paper in the ITU programme, complementing **Tier 1 #5 (Cancer)** to form 2/3 of the medicine triangle.

Central thesis:

$$\text{Aging} = \text{slow exponential decay of } K_{\rm organism}(t)
   \quad \Longrightarrow \quad \text{Gompertz mortality law}$$

The ITU axiom yields:
1. **Gompertz mortality** $\mu(t) = A e^{\alpha t}$ as a direct consequence of $K(t) = K_0 e^{-\beta t}$
2. **12 Hallmarks of Aging** as 12 K-component decays
3. **Three pillars** (telomere/mitochondria/proteostasis) as fundamental K-components
4. **Six interventions** (rapamycin, metformin, senolytics, NAD+, CR, OSKM) as K-restoration strategies
5. **Multi-K combination** as the ITU-necessary therapeutic approach
6. **2026-2050 roadmap** with lifespan 82 → 95 yr, healthspan 72 → 92 yr

This completes Tier 1 #6, advancing the **ITU medicine triangle to 2/3**.

---

## ITU Tier structure

| Tier | DOI | Contents | Status |
|---|---|---|---|
| Tier 0 (core) | [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209) | ITU foundational 42 phases | v2.0.0 |
| Tier 1 #1 | [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391) | Quantum Computing | v1.0.0 |
| Tier 1 #2 | [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501) | Machine Consciousness / ASI | v1.0.0 |
| Tier 1 #3 | [10.5281/zenodo.20151059](https://doi.org/10.5281/zenodo.20151059) | Cryptography | v1.0.0 |
| Tier 1 #4 | [10.5281/zenodo.20174036](https://doi.org/10.5281/zenodo.20174036) | Semiconductors | v1.0.0 |
| Tier 1 #5 | [10.5281/zenodo.20174318](https://doi.org/10.5281/zenodo.20174318) | Cancer Biology | v1.0.0 |
| **Tier 1 #6** | **[10.5281/zenodo.20175663](https://doi.org/10.5281/zenodo.20175663)** | **Aging** | **v1.0.0 (this paper)** |
| Tier 1 #7+ | TBD | Psychiatry, Economics, ... | planned |

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **63** | ✅ | ITU foundation: aging = K_organism exponential decay; Gompertz from ITU |
| **64** | ✅ | Three pillars: telomere (Hayflick=53), mtDNA (10.5% above threshold @80), proteostasis (APOE4 onset 84) |
| **65** | ✅ | Six interventions × K-component matrix; combinations diminishing returns |
| **66** | ✅ | 2026-2050 roadmap; lifespan 82 → 95; healthspan 72 → 92; gap 10 → 3 yr |

---

## Key Results (v1.0.0)

| Quantity | Value |
|---|---|
| Hayflick limit (telomere) | **53 divisions** (L0=12kb, 150bp/div) |
| K-control loss in old (age 80) | **53.6%** (mean K 0.93 → 0.43) |
| mtDNA above 60% threshold @age80 | **10.5%** of cells |
| APOE4 carrier disease onset (model) | **age 84** |
| Composite K @age80 | **0.10** (mortality region) |
| CR mouse lifespan extension | +30% |
| 5-drug combination prediction | **+52%** lifespan |
| Lifespan 2024 → 2050 (ITU mid) | **82 → 95 yr** |
| Healthspan 2024 → 2050 | **72 → 92 yr** |
| Lifespan-healthspan gap | **10 → 3 yr** |
| Longevity industry investment 2024 → 2050 | **$5.2B → $120B** |
| Falsifiable predictions | **10 listed** |

---

## Reproducing the results

```bash
cd papers/aging
python aging_itu_foundation.py    # Phase 63 (~5 seconds)
python aging_mechanisms.py        # Phase 64 (~10 seconds, includes random simulation)
python aging_interventions.py     # Phase 65 (~5 seconds)
python aging_roadmap.py           # Phase 66 (~5 seconds)
```

Required: Python 3.10+, numpy, matplotlib.

Total runtime ~25 seconds. Outputs: 4 `.png` figures, 4 `summary_phase##.json`.

---

## Directory contents

```
papers/aging/
├── README.md                         this file
├── CITATION.cff                      machine-readable citation
├── .zenodo.json                      Zenodo upload metadata
│
├── theory_phase63.md                 ITU foundation (Gompertz, Hallmarks, Horvath)
├── theory_phase64.md                 Three pillars (telomere/mito/proteostasis)
├── theory_phase65.md                 Six interventions evaluation
├── theory_phase66.md                 2026-2050 roadmap + 10 predictions
│
├── aging_itu_foundation.py / .png    Phase 63
├── aging_mechanisms.py / .png        Phase 64
├── aging_interventions.py / .png     Phase 65
├── aging_roadmap.py / .png           Phase 66
│
└── summary_phase63-66.json
```

---

## How to cite

This Tier 1 #6 paper:

```
Terada, M. (2026). ITU and Aging:
A Single-Axiom View of K_organism Decay, Three-Pillar Mechanisms,
Interventions, and the 2026-2050 Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20175663
```

The core ITU framework (Tier 0):

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109209
```

Both citations are recommended together.

---

## License

* Text content (paper, theory notes, figures): **CC-BY-4.0**
* Source code (`*.py`): **MIT License**

---

## Honest framing (Pass-1 interpretive paper)

This paper is a **Pass-1 interpretive contribution**: it reframes known aging biology
(Hallmarks of Aging, Gompertz law, Hayflick limit, Horvath clock, Sinclair information theory,
intervention pharmacology) within the ITU axiom $\delta S = \delta\langle K\rangle$.

Numerical results reproduce established clinical/biological data (Hayflick 53 divisions,
APOE4 onset ~84 yr, BRCA1-like multi-hit dynamics, mtDNA heteroplasmy distributions,
intervention lifespan extension percentages) but do not constitute novel aging-biology
predictions distinguishing ITU from standard gerontology.

The **2026-2050 roadmap and 10 falsifiable predictions** in Phase 66 are ITU-informed but
overlap substantially with industry/demographic consensus. **Pass-2 follow-up work** would
derive an ITU-specific longevity biomarker or intervention validated against long-term
patient outcome data.

This honest framing is consistent across all Tier 1 papers (#1-#6).

---

## ITU programme: medicine triangle now 2/3 complete

```
                Cancer (#5)
                /        \
               /          \
            Aging (#6) ────  [Psychiatry (#7), planned]
              ↑
              this paper
```

| # | Domain | Axis |
|---|---|---|
| #1 | QC | engineering (storage) |
| #2 | AI/ASI | engineering (intelligence) |
| #3 | Crypto | engineering (communication) |
| #4 | Semi | engineering (substrate) |
| #5 | Cancer | medicine (acute K breakdown) |
| **#6** | **Aging** | **medicine (chronic K decay)** ← THIS PAPER |

Future Tier 1 #7 (Psychiatry) will close the medicine triangle.

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #6 — Aging
2026年5月14日

Part of the *Information-Theoretic Unification* research programme.
For the foundational theory (Phases 1-42), see
[10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209).
