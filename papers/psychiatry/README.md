# ITU and Psychiatry

**A single-axiom view of K_brain failures, predictive coding, drug mechanisms, and the 2026-2050 roadmap.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20177427.svg)](https://doi.org/10.5281/zenodo.20177427)

> 📄 **Tier 0 ITU framework**: [10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209)
> 📄 **Tier 1 #1: Quantum Computing**: [10.5281/zenodo.20139391](https://doi.org/10.5281/zenodo.20139391)
> 📄 **Tier 1 #2: Machine Consciousness / ASI**: [10.5281/zenodo.20150501](https://doi.org/10.5281/zenodo.20150501)
> 📄 **Tier 1 #3: Cryptography**: [10.5281/zenodo.20151059](https://doi.org/10.5281/zenodo.20151059)
> 📄 **Tier 1 #4: Semiconductors**: [10.5281/zenodo.20174036](https://doi.org/10.5281/zenodo.20174036)
> 📄 **Tier 1 #5: Cancer Biology**: [10.5281/zenodo.20174318](https://doi.org/10.5281/zenodo.20174318)
> 📄 **Tier 1 #6: Aging**: [10.5281/zenodo.20175663](https://doi.org/10.5281/zenodo.20175663)
> 📄 **Tier 1 #7 (this paper)**: [10.5281/zenodo.20177427](https://doi.org/10.5281/zenodo.20177427)
> 💻 **GitHub**: https://github.com/roboken-terada2/information-theoretic-unification
> ✉️ **著者**: 寺田 宗弘 (Munehiro Terada), Roboken — `munehiro.terada@roboken2.com`

---

## 概要

This **Tier 1 #7 application paper** completes the **ITU Medicine Triangle** by joining Cancer (#5, acute K breakdown) and Aging (#6, chronic K decay) with Psychiatry — the **structural K-circuit failure** of the brain.

Central thesis:

$$\text{Psychiatric disorder} = \text{breakdown of } K_{\rm brain}\text{-component}
   \quad \text{(predictive coding failure)}$$

The ITU axiom yields:
1. **Friston Free Energy Principle (FEP)** as the brain-specific incarnation of ITU dS = d⟨K⟩
2. **8 major psychiatric disorders** as 8 K-component failures
3. **Schizophrenia** as K_precision failure (top-down prior dominates)
4. **Depression** as K_reward collapse (positive prediction errors not registered)
5. **Anxiety/PTSD** as K_threat over-precision (false-positive explosion)
6. **ASD** as K_social rigid over-precision; **ADHD** as K_attention filter failure
7. **Multi-axis treatment** (drugs + therapy + digital + brain stim) as ITU-necessary
8. **2026-2050 roadmap** with psilocybin/MDMA/FUS approvals and DSM-6 K-based diagnosis

This **completes the medicine triangle**: #5 Cancer + #6 Aging + #7 Psychiatry.

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
| Tier 1 #6 | [10.5281/zenodo.20175663](https://doi.org/10.5281/zenodo.20175663) | Aging | v1.0.0 |
| **Tier 1 #7** | **[10.5281/zenodo.20177427](https://doi.org/10.5281/zenodo.20177427)** | **Psychiatry** | **v1.0.0 (this paper)** |
| Tier 1 #8+ | TBD | Economics, Free Will, ... | planned |

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **67** | ✅ | ITU foundation: FEP = brain ITU axiom; 8 disorders × 9 K-components |
| **68** | ✅ | Schizophrenia: K_precision failure, dopamine asymmetry, KarXT |
| **69** | ✅ | Depression + Anxiety: K_reward / K_threat; STAR*D + ketamine/psilocybin |
| **70** | ✅ | ASD/ADHD; 2026-2050 roadmap; 10 predictions; medicine triangle complete |

---

## Key Results (v1.0.0)

| Quantity | Value |
|---|---|
| Global psychiatric DALYs | **136.8M** (~7% all DALYs) |
| Major depression DALYs | **47.5M** (largest single disorder) |
| Schizophrenia precision-ratio (psychotic) | 0.3 (vs healthy 1.0) |
| K_reward (severe depression, after 100 events) | **0.28** (vs healthy 0.49) |
| Anxiety false-positive threat detections | **97/200** (vs healthy 15/200) |
| ASD response amplitude | 0.83 (vs healthy 0.38, sensory hyper) |
| ADHD attention SNR | 1.82 (vs healthy 12.21) |
| ADHD on stimulant SNR | 5.60 (3× improvement) |
| TRS prevalence | ~30% (Clozapine rescues ~55% of TRS) |
| TRD prevalence (STAR*D) | ~30% |
| Ketamine response (TRD, 1 day) | 88% |
| Psilocybin sustained response (TRD) | **70-80%** |
| Falsifiable predictions | **10 listed** |

---

## Reproducing the results

```bash
cd papers/psychiatry
python psychiatry_itu_foundation.py     # Phase 67 (~5 seconds)
python schizophrenia_itu.py             # Phase 68 (~10 seconds)
python depression_anxiety_itu.py        # Phase 69 (~10 seconds)
python psychiatry_roadmap.py            # Phase 70 (~10 seconds)
```

Required: Python 3.10+, numpy, matplotlib.

Total runtime ~35 seconds. Outputs: 4 `.png` figures, 4 `summary_phase##.json`.

---

## Directory contents

```
papers/psychiatry/
├── README.md                              this file
├── CITATION.cff                           machine-readable citation
├── .zenodo.json                           Zenodo upload metadata
│
├── theory_phase67.md                      ITU foundation, FEP, 8 disorders
├── theory_phase68.md                      Schizophrenia (K_precision)
├── theory_phase69.md                      Depression + Anxiety (K_reward, K_threat)
├── theory_phase70.md                      ASD/ADHD + roadmap + 10 predictions
│
├── psychiatry_itu_foundation.py / .png    Phase 67
├── schizophrenia_itu.py / .png            Phase 68
├── depression_anxiety_itu.py / .png       Phase 69
├── psychiatry_roadmap.py / .png           Phase 70
│
└── summary_phase67-70.json
```

---

## How to cite

This Tier 1 #7 paper:

```
Terada, M. (2026). ITU and Psychiatry:
A Single-Axiom View of K_brain Failures, Predictive Coding,
Drug Mechanisms, and the 2026-2050 Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20177427
```

The core ITU framework (Tier 0):

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109209
```

---

## License

* Text content (paper, theory notes, figures): **CC-BY-4.0**
* Source code (`*.py`): **MIT License**

---

## Honest framing (Pass-1 interpretive paper)

This paper is a **Pass-1 interpretive contribution**: it reframes known psychiatric biology
(Friston's Free Energy Principle, Bayesian Brain, dopamine hypothesis, STAR*D, ICI/CAR-T-like
treatment cascades, computational psychiatry) within the ITU axiom $\delta S = \delta\langle K\rangle$.

Numerical results reproduce established clinical data (TRS ~30%, TRD ~30%, ketamine rapid response,
psilocybin durable effect, ADHD stimulant 70% response, anxiety false-positive rates) but do not
constitute novel psychiatry-biology predictions distinguishing ITU from standard computational
psychiatry literature (Friston, Adams, Sterzer, Pellicano).

The **2026-2050 roadmap and 10 falsifiable predictions** in Phase 70 are ITU-informed but
overlap with industry/regulatory consensus (psilocybin Phase III, MDMA re-application, digital
phenotyping FDA pathway, FUS approvals).

**Pass-2 follow-up** would derive an ITU-specific brain-imaging or EEG biomarker validated
against patient outcome data — a topic potentially involving collaboration with computational
psychiatry groups.

---

## ITU Programme: medicine triangle complete

```
                  Cancer (#5) ──── acute K breakdown
                  /        \
                 /          \
              Aging (#6) ──── Psychiatry (#7) ← THIS PAPER
              chronic         brain circuit
              K decay         K failure
```

| # | Domain | Axis |
|---|---|---|
| #1 | QC | engineering (storage) |
| #2 | AI/ASI | engineering (intelligence) |
| #3 | Crypto | engineering (communication) |
| #4 | Semi | engineering (substrate) |
| #5 | Cancer | medicine (acute) |
| #6 | Aging | medicine (chronic) |
| **#7** | **Psychiatry** | **medicine (brain circuit)** ← NEW |

**Engineering rectangle (4 vertices) + Medicine triangle (3 vertices) = ITU's first complete polytope.**

Future Tier 1 #8+ will branch into Economics, Free Will, Semiconductors-extensions, Materials,
Climate, and so on (Phase 71+).

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #7 — Psychiatry
2026年5月14日

Part of the *Information-Theoretic Unification* research programme.
For the foundational theory (Phases 1-42), see
[10.5281/zenodo.20109209](https://doi.org/10.5281/zenodo.20109209).
