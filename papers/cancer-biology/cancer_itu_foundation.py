#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 59: ITU Foundation for Cancer Biology

The ITU axiom dS = d<K> applied to cancer:
  - Healthy cell: balanced
  - Cancer cell: dS >> d<K>  OR  K corrupted by driver mutations

Tests:
  1. Healthy logistic vs cancer exponential growth
  2. Multi-hit Armitage-Doll cancer-incidence age distribution
  3. 10 Hallmarks of Cancer mapped onto 10 K-components (spider chart)
  4. Two-hit hypothesis: BRCA1 1-hit vs 2-hit lifetime risk

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #5 paper (in preparation).
"""

import json
import math
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Healthy logistic vs cancer exponential
# =============================================================================
def healthy_logistic(t, N0=100.0, r=0.5, K=1e6):
    """Logistic growth with carrying capacity K (ITU-balanced)."""
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))


def cancer_exponential(t, N0=100.0, r=0.5):
    """Unbounded exponential — δS >> δ<K>"""
    return N0 * np.exp(r * t)


# =============================================================================
# Test 2: Armitage-Doll multi-hit model
# =============================================================================
def armitage_doll_incidence(age, n_hits=6, alpha=None):
    """
    Cumulative cancer probability by age t (years) for n_hits requirement.
    Phenomenological: P(cancer by t) = 1 - exp(-alpha * t^n_hits)
    alpha is calibrated so that lifetime risk (age 80) ~30% for n_hits=6.
    """
    age = np.asarray(age, dtype=float)
    # Default calibration: 30% cumulative risk at age 80 for given n_hits
    if alpha is None:
        target_age = 80.0
        target_risk = 0.30
        alpha = -np.log(1 - target_risk) / (target_age ** n_hits)
    return 1.0 - np.exp(-alpha * age ** n_hits)


# =============================================================================
# Test 3: 10 Hallmarks ↔ 10 K-components
# =============================================================================
HALLMARKS = [
    "Proliferative signaling",
    "Evade growth suppressors",
    "Resist cell death",
    "Replicative immortality",
    "Induce angiogenesis",
    "Activate invasion",
    "Genome instability",
    "Tumor-promoting inflammation",
    "Deregulated metabolism",
    "Avoid immune destruction",
]

# Normal cell: balanced (1.0 = perfect K control)
NORMAL_K = np.array([1.0] * 10)

# Cancer cell: most K-components compromised (typical aggressive tumor)
CANCER_K = np.array([0.2, 0.3, 0.15, 0.1, 0.4, 0.3, 0.1, 0.5, 0.25, 0.2])


def fitness_balance(K_vector):
    """Mean K control. 1.0 = healthy, 0 = total collapse."""
    return float(np.mean(K_vector))


# =============================================================================
# Test 4: Two-hit BRCA1 lifetime risk
# =============================================================================
def brca1_lifetime_risk(age, hits_required=2):
    """
    BRCA1 mutation carrier (1-hit germline) vs general population (2-hit somatic).
    Calibrated to match epidemiology:
      - Carrier (1-hit): ~65-72% lifetime risk by age 80
      - General (2-hit): ~12% lifetime risk by age 80
    Both follow Armitage-Doll: P(t) = 1 - exp(-alpha * t^n)
    """
    age = np.asarray(age, dtype=float)
    if hits_required == 1:
        # Calibrate to 72% at age 80, t^1 dependence
        alpha = -np.log(1 - 0.72) / 80.0
        return 1 - np.exp(-alpha * age)
    elif hits_required == 2:
        # Calibrate to 12% at age 80, t^2 dependence
        alpha = -np.log(1 - 0.12) / (80.0 ** 2)
        return 1 - np.exp(-alpha * age ** 2)


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig = plt.figure(figsize=(13, 10))
    gs = fig.add_gridspec(2, 2)

    # --- (a) Healthy logistic vs cancer exponential ---
    ax = fig.add_subplot(gs[0, 0])
    t = np.linspace(0, 30, 200)
    healthy = healthy_logistic(t)
    cancer = cancer_exponential(t)
    ax.semilogy(t, healthy, lw=2, color="green",
                label="Healthy (logistic, ITU-balanced)")
    ax.semilogy(t, cancer, lw=2, color="red",
                label="Cancer (exponential, ITU-broken)")
    ax.axhline(1e6, ls="--", color="green", alpha=0.5,
               label="Carrying capacity K")
    ax.set_xlabel("Time (arbitrary units)")
    ax.set_ylabel("Cell count")
    ax.set_title("(a) ITU-balanced vs ITU-broken growth")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="lower right", fontsize=9)
    ax.set_ylim(1, 1e10)

    # --- (b) Armitage-Doll multi-hit incidence ---
    ax = fig.add_subplot(gs[0, 1])
    age = np.linspace(10, 90, 50)
    for n_hits, color in zip([4, 5, 6, 7], ["blue", "green", "orange", "red"]):
        incidence = armitage_doll_incidence(age, n_hits=n_hits)
        ax.plot(age, incidence * 100, lw=2, color=color,
                label=f"n_hits = {n_hits}")
    ax.axhline(30, ls="--", color="black", alpha=0.4,
               label="Calibration: 30% @ age 80")
    ax.set_xlabel("Age [years]")
    ax.set_ylabel("Cumulative cancer probability [%]")
    ax.set_title("(b) Multi-hit Armitage–Doll model")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_ylim(0, 50)

    # --- (c) Spider chart: Normal vs Cancer K-profile ---
    ax = fig.add_subplot(gs[1, 0], projection="polar")
    angles = np.linspace(0, 2 * np.pi, len(HALLMARKS), endpoint=False).tolist()
    angles += angles[:1]
    normal_v = np.concatenate([NORMAL_K, [NORMAL_K[0]]])
    cancer_v = np.concatenate([CANCER_K, [CANCER_K[0]]])
    ax.plot(angles, normal_v, lw=2, color="green", label="Normal cell")
    ax.fill(angles, normal_v, color="green", alpha=0.15)
    ax.plot(angles, cancer_v, lw=2, color="red", label="Cancer cell")
    ax.fill(angles, cancer_v, color="red", alpha=0.3)
    ax.set_xticks(angles[:-1])
    # Wrap hallmark labels
    short_labels = [
        "Prolif.\nsignal",
        "Evade\ngrowth supp.",
        "Resist\ndeath",
        "Replicative\nimmortality",
        "Angio-\ngenesis",
        "Invasion",
        "Genome\ninstability",
        "Inflam-\nmation",
        "Metabolism\nshift",
        "Avoid\nimmune",
    ]
    ax.set_xticklabels(short_labels, fontsize=7)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0.25", "0.50", "0.75", "1.0"], fontsize=7)
    ax.set_title("(c) 10 Hallmarks = 10 K-components", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.0), fontsize=8)

    # --- (d) Two-hit BRCA1 lifetime risk ---
    ax = fig.add_subplot(gs[1, 1])
    age = np.linspace(20, 80, 50)
    risk1 = brca1_lifetime_risk(age, hits_required=1)
    risk2 = brca1_lifetime_risk(age, hits_required=2)
    ax.plot(age, risk1 * 100, lw=2, color="red",
            label="1 hit needed (BRCA1+ carrier)")
    ax.plot(age, risk2 * 100, lw=2, color="blue",
            label="2 hits needed (general population)")
    ax.axhline(72, ls="--", color="red", alpha=0.5,
               label="Carrier @80yr: ~72% (data)")
    ax.axhline(12, ls="--", color="blue", alpha=0.5,
               label="General @80yr: ~12% (data)")
    ax.set_xlabel("Age [years]")
    ax.set_ylabel("Cumulative breast-cancer risk [%]")
    ax.set_title("(d) Two-hit hypothesis: BRCA1 example")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=7)
    ax.set_ylim(0, 100)

    plt.suptitle("Phase 59: ITU foundation for cancer biology — "
                 "cell-level breakdown of δS = δ⟨K⟩",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "cancer_itu_foundation.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 59] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 59: ITU foundation for cancer biology")
    print("=" * 60)

    # [1] Growth comparison
    print("\n[1] ITU-balanced vs ITU-broken growth (t=30):")
    healthy_30 = healthy_logistic(30)
    cancer_30 = cancer_exponential(30)
    print(f"    Healthy (logistic): {healthy_30:.2e} cells (saturated at K)")
    print(f"    Cancer (exp):       {cancer_30:.2e} cells (unbounded)")
    print(f"    Ratio cancer/healthy: {cancer_30/healthy_30:.1f}×")

    # [2] Armitage-Doll
    print("\n[2] Multi-hit cancer onset (mu=1e-7, age 60 vs 80):")
    age_test = np.array([30, 50, 60, 70, 80])
    for n in [5, 6, 7]:
        risks = armitage_doll_incidence(age_test, n_hits=n)
        print(f"    n_hits={n} : age 60={risks[2]*100:5.2f}%, "
              f"age 80={risks[4]*100:5.2f}%")

    # [3] K-component profile
    print("\n[3] K-component balance:")
    print(f"    Normal cell mean K: {fitness_balance(NORMAL_K):.3f}")
    print(f"    Cancer cell mean K: {fitness_balance(CANCER_K):.3f}")
    print(f"    K-control loss: {(1 - fitness_balance(CANCER_K))*100:.1f}%")
    for h, kn, kc in zip(HALLMARKS, NORMAL_K, CANCER_K):
        print(f"      {h:<32s} : {kn:.2f} -> {kc:.2f}")

    # [4] Two-hit
    print("\n[4] BRCA1 lifetime risk:")
    age = np.array([50, 70, 80])
    risk_1hit = brca1_lifetime_risk(age, hits_required=1)
    risk_2hit = brca1_lifetime_risk(age, hits_required=2)
    for a, r1, r2 in zip(age, risk_1hit, risk_2hit):
        print(f"    Age {a}: carrier(1-hit)={r1*100:5.1f}%, "
              f"general(2-hit)={r2*100:5.1f}%")

    # Plot
    plot_path = make_plot()

    # Summary
    summary = {
        "phase": 59,
        "paper": "ITU and Cancer Biology",
        "description": "Foundational reframing of cancer as cellular ITU breakdown",
        "growth_comparison": {
            "healthy_at_t30": float(healthy_logistic(30)),
            "cancer_at_t30": float(cancer_exponential(30)),
            "ratio": float(cancer_exponential(30) / healthy_logistic(30)),
        },
        "armitage_doll": {
            f"n_hits_{n}_at_age_60": float(
                armitage_doll_incidence(np.array([60.0]), n_hits=n)[0]
            )
            for n in [5, 6, 7]
        },
        "k_component_profile": {
            "hallmark_names": HALLMARKS,
            "normal_K": NORMAL_K.tolist(),
            "cancer_K": CANCER_K.tolist(),
            "mean_K_normal": fitness_balance(NORMAL_K),
            "mean_K_cancer": fitness_balance(CANCER_K),
            "K_control_loss_percent": float(
                (1 - fitness_balance(CANCER_K)) * 100
            ),
        },
        "brca1_two_hit": {
            "carrier_age80_percent": float(
                brca1_lifetime_risk(np.array([80.0]), hits_required=1)[0] * 100
            ),
            "general_age80_percent": float(
                brca1_lifetime_risk(np.array([80.0]), hits_required=2)[0] * 100
            ),
            "literature_carrier_pct": 72,
            "literature_general_pct": 12,
        },
        "central_thesis": "Cancer = breakdown of dS = d<K> at cellular level. "
                          "10 Hallmarks correspond to 10 K-component failures. "
                          "Two-hit hypothesis = redundant QECC.",
        "honest_framing": "Pass-1 interpretive paper: reframes Hanahan-Weinberg "
                          "hallmarks, Knudson two-hit, Armitage-Doll multi-hit "
                          "in ITU language. No novel cancer-specific prediction "
                          "validated against experiment.",
        "tier": 1,
        "paper_number": 5,
        "tier_0_concept_doi": "10.5281/zenodo.20109209",
        "tier_1_qc_doi": "10.5281/zenodo.20139391",
        "tier_1_ai_doi": "10.5281/zenodo.20150501",
        "tier_1_crypto_doi": "10.5281/zenodo.20151059",
        "tier_1_semi_doi": "10.5281/zenodo.20174036",
        "next_phases": [
            "Phase 60: Warburg effect and cancer metabolism (ITU)",
            "Phase 61: Cancer immunology and immune evasion",
            "Phase 62: Cancer treatments and ITU-informed therapy roadmap",
        ],
        "caveats": [
            "Logistic and exponential models are toy approximations",
            "Armitage-Doll uses simplified probability for clarity",
            "K-component values for hallmarks are illustrative",
            "Two-hit BRCA1 risk simplification — real values from family studies",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase59.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 59] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 59 complete.")
    print("  - Cancer = δS = δ<K> breakdown at cellular level")
    print("  - 10 Hallmarks mapped to 10 K-components")
    print("  - Two-hit hypothesis = redundant QECC")
    print("  - Multi-hit (5-7) = critical mass of K-failures")
    print("=" * 60)


if __name__ == "__main__":
    main()
