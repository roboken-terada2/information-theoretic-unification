# ITU and Economics

**A single-axiom view of markets, bubbles, inequality, AI labor displacement, and the 2026-2050 roadmap.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20196309.svg)](https://doi.org/10.5281/zenodo.20196309)

> 📄 **Tier 0 ITU framework**: [10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210)
> 📄 **Tier 1 #1-#7 (engineering rectangle + medicine triangle)**: completed
> 📄 **Tier 1 #8 (this paper)**: [10.5281/zenodo.20196309](https://doi.org/10.5281/zenodo.20196309)
> 💻 **GitHub**: https://github.com/roboken-terada2/information-theoretic-unification
> ✉️ **著者**: 寺田 宗弘 (Munehiro Terada), Roboken — `munehiro.terada@roboken2.com`

---

## 概要

This **Tier 1 #8 application paper** opens the **social-sciences axis** of the ITU programme, joining the completed engineering rectangle (#1-#4) and medicine triangle (#5-#7).

Central thesis:

$$\text{Markets} = \text{collective ITU inference engines}
   \quad \text{with} \quad \delta S(\rho_{\rm price}) = \delta\langle K_{\rm market}\rangle$$

The ITU axiom yields:
1. **Markets** as collective Bayesian inference; **prediction markets** are highest-resolution K
2. **EMH** as the idealised case; reality shows fat tails and bubbles (K_market disconnects)
3. **Minsky 3-stage instability** (hedge → speculative → Ponzi) = K_market structural degradation
4. **Pareto distribution** as natural steady-state of ITU economic dynamics
5. **Piketty r > g** = K_capital strengthening relative to K_labor
6. **AI labor exposure** inverts traditional risk (high-pay knowledge work most automatable)
7. **UBI** = K_income state-mediated redistribution
8. **2026-2050 roadmap** with AGI-driven GDP 3×, CBDC adoption, carbon pricing trajectories

---

## Tier 1 Tier structure

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
| **Tier 1 #8** | **[10.5281/zenodo.20196309](https://doi.org/10.5281/zenodo.20196309)** | **Economics** | **v1.0.0 (this paper)** |
| Tier 1 #9+ | TBD | Free Will, Energy/Materials, ... | planned |

---

## Phases in this paper

| Phase | Status | Topic |
|---|---|---|
| **71** | ✅ | ITU foundation: markets = collective Bayesian inference, EMH, Akerlof, prospect theory, prediction markets |
| **72** | ✅ | Bubbles + crises: Minsky 3-stage, BHW cascades, 9 historical bubbles, LTCM/Lehman/FTX |
| **73** | ✅ | Inequality + AI: Pareto, Piketty r>g, AI exposure inverse-pay, UBI, Information Feudalism |
| **74** | ✅ | Roadmap 2026-2050: AGI GDP 3×, CBDC G20, sectoral shift, carbon price, 10 predictions |

---

## Key Results (v1.0.0)

| Quantity | Value |
|---|---|
| EMH vs realistic extreme events ratio | **4×** |
| Akerlof lemons: market shrinks | **1000 → 1** seller in 10 iterations |
| Loss aversion λ | **2.25** (Kahneman-Tversky) |
| 2024 election prediction-market Brier | Polymarket **0.160** (best) vs polls 0.25-0.36 |
| Minsky crash trigger | Ponzi share > **40%** |
| Historical bubble drawdowns | **-58% (Housing) to -100% (FTX)** |
| Pareto simulation top 1% share | **19%** (illustrative; real US ~32%) |
| Piketty K/Y modern scenario (300yr unconstrained) | **23,922×** (without redistribution) |
| AI exposure: weighted | **26.2%** of 22.5M jobs |
| Highest exposure: Translator | **76%** |
| Lowest exposure: Plumber | **4%** |
| US UBI ($1000/mo) cost | **11.1%** of GDP (declining to 6% by 2050) |
| GDP 2024→2050 (AGI bull) | **$27T → $113T** (4.1×) |
| Carbon price (EU) trajectory | **€70 → €350/t** (2024 → 2050) |
| Falsifiable predictions | **10 listed** |

---

## Reproducing the results

```bash
cd papers/economics
python economics_itu_foundation.py     # Phase 71 (~5 seconds)
python bubbles_crises_itu.py           # Phase 72 (~10 seconds)
python inequality_ai_itu.py            # Phase 73 (~5 seconds)
python economics_roadmap.py            # Phase 74 (~5 seconds)
```

Required: Python 3.10+, numpy, matplotlib.

Total runtime ~25 seconds. Outputs: 4 `.png` figures, 4 `summary_phase##.json`.

---

## Directory contents

```
papers/economics/
├── README.md                              this file
├── CITATION.cff                           machine-readable citation
├── .zenodo.json                           Zenodo upload metadata
│
├── theory_phase71.md                      ITU foundation, EMH, Akerlof, prediction markets
├── theory_phase72.md                      Bubbles + crises, Minsky, BHW cascades
├── theory_phase73.md                      Inequality, AI labor, UBI, Information Feudalism
├── theory_phase74.md                      2026-2050 roadmap + 10 predictions
│
├── economics_itu_foundation.py / .png     Phase 71
├── bubbles_crises_itu.py / .png           Phase 72
├── inequality_ai_itu.py / .png            Phase 73
├── economics_roadmap.py / .png            Phase 74
│
└── summary_phase71-74.json
```

---

## How to cite

This Tier 1 #8 paper:

```
Terada, M. (2026). ITU and Economics:
A Single-Axiom View of Markets, Bubbles, Inequality, AI Labor Displacement,
and the 2026-2050 Roadmap (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20196309
```

The core ITU framework (Tier 0):

```
Terada, M. (2026). Information-Theoretic Unification of Physics,
Life, and Consciousness: Numerical Demonstration in 42 Phases (v2.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109210
```

---

## License

* Text content (paper, theory notes, figures): **CC-BY-4.0**
* Source code (`*.py`): **MIT License**

---

## Honest framing (Pass-1 interpretive paper)

This paper is a **Pass-1 interpretive contribution**: it reframes classical and contemporary
economics (Akerlof, Fama EMH, Kahneman-Tversky, Pareto, Piketty, Romer, Minsky, BHW 1992)
within the ITU axiom $\delta S = \delta\langle K\rangle$.

Numerical results reproduce established economic patterns (Pareto power law, Minsky cycle
crash, Akerlof market collapse, BHW cascade < independent crowds, prediction-market accuracy
vs polls, AI exposure index, UBI cost calculations) but do not constitute novel
economics-discipline predictions distinguishing ITU from standard economic theory.

The **2026-2050 roadmap and 10 falsifiable predictions** in Phase 74 are ITU-informed but
overlap with industry/regulatory consensus (Goldman Sachs AI GDP+7%, AGI by 2030 from
Tier 1 #2, CBDC trajectories from BIS, carbon pricing from IPCC/EU).

**Pass-2 follow-up** would derive ITU-specific market-microstructure or macroeconomic
predictions validated against high-frequency or panel data.

---

## ITU Programme: social-sciences axis begins

```
                                    Cancer (#5)
                                    /        \
                                   /          \
                                  /            \
                               Aging (#6) ─── Psychiatry (#7)
                                            (medicine triangle)
            
        AI/ASI (#2) ←─── Cryptography (#3)
            ↑                    ↑
            │                    │
       Quantum Computing (#1) ── Semiconductors (#4)
                  (engineering rectangle)
                  
                      Economics (#8) ★ THIS PAPER
                      (social-sciences first vertex)
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
| **#8** | **Economics** | **social science (first vertex)** ← THIS PAPER |

Future Tier 1 #9 (Free Will), #10 (Energy/Materials), and beyond will continue the social-sciences
and applied-engineering branches.

**Pass-1 progress**: 74 of 220 phases complete (33.6%).

---

**寺田 宗弘 (Roboken)**
ITU Tier 1 paper #8 — Economics
2026年5月14日

Part of the *Information-Theoretic Unification* research programme.
For the foundational theory (Phases 1-42), see
[10.5281/zenodo.20109210](https://doi.org/10.5281/zenodo.20109210).
