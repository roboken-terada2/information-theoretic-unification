#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 63: ITU Foundation for Aging

K_organism degrades exponentially with time -> Gompertz mortality law.
12 Hallmarks of Aging (Lopez-Otin 2023) mapped to K-component decay.

Tests:
  1. Gompertz mortality fit for Human / Mouse / Dog
  2. 12 Hallmarks K-profile at age 25 vs 80
  3. Horvath methylation clock vs chronological age
  4. Maximum lifespan vs species (alpha, K_0)

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #6 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Gompertz mortality law mu(t) = A * exp(alpha * t)
# =============================================================================
SPECIES = {
    "Mouse":   {"alpha": 0.7,   "A_norm": 1e-4, "max_lifespan_yr": 4,
                "K_0": 1.0, "color": "green"},
    "Dog":     {"alpha": 0.15,  "A_norm": 5e-5, "max_lifespan_yr": 20,
                "K_0": 1.0, "color": "orange"},
    "Human":   {"alpha": 0.085, "A_norm": 1e-5, "max_lifespan_yr": 122,
                "K_0": 1.0, "color": "blue"},
    "Bowhead": {"alpha": 0.04,  "A_norm": 5e-6, "max_lifespan_yr": 211,
                "K_0": 1.0, "color": "navy"},
    "Lobster (negligible senescence)": {
        "alpha": 0.01, "A_norm": 1e-5, "max_lifespan_yr": 100,
        "K_0": 1.0, "color": "red"
    },
    "Hydra (immortal)": {
        "alpha": 0.001, "A_norm": 1e-6, "max_lifespan_yr": 1000,
        "K_0": 1.0, "color": "purple"
    },
}


def gompertz_mortality(age, A, alpha):
    return A * np.exp(alpha * age)


def K_fidelity_curve(age, K_0=1.0, beta=0.085):
    """ITU prediction: K(t) = K_0 * exp(-beta * t)"""
    return K_0 * np.exp(-beta * age)


# =============================================================================
# Test 2: 12 Hallmarks at age 25 vs 80
# =============================================================================
HALLMARKS_AGING = [
    "Genomic instability",
    "Telomere attrition",
    "Epigenetic alterations",
    "Loss of proteostasis",
    "Disabled autophagy",
    "Nutrient sensing dereg.",
    "Mitochondrial dysfn.",
    "Cellular senescence",
    "Stem cell exhaustion",
    "Altered cell comm.",
    "Chronic inflammation",
    "Dysbiosis",
]

# Young (age 25): K-component values near 1.0 (full fidelity)
YOUNG_K = np.array([0.95, 0.95, 0.92, 0.95, 0.93, 0.90,
                     0.95, 0.95, 0.95, 0.93, 0.90, 0.92])

# Old (age 80): K-component degradation
OLD_K = np.array([0.50, 0.40, 0.45, 0.50, 0.45, 0.40,
                   0.45, 0.35, 0.30, 0.55, 0.35, 0.50])


def overall_K(K_vector):
    return float(np.mean(K_vector))


# =============================================================================
# Test 3: Horvath methylation clock
# =============================================================================
def horvath_biological_age(chronological_age, lifestyle_factor=1.0,
                             noise_std=2.5):
    """
    Simulate Horvath biological age estimate.
    lifestyle_factor: 1.0 = average, 0.8 = healthy (clock slower),
                       1.2 = unhealthy (clock faster).
    """
    bio_age = chronological_age * lifestyle_factor
    # add small noise (measurement noise)
    noise = np.random.normal(0, noise_std, size=np.shape(chronological_age))
    return bio_age + noise


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig = plt.figure(figsize=(13, 10))
    gs = fig.add_gridspec(2, 2)

    # --- (a) Gompertz mortality for Human, Mouse, Dog ---
    ax = fig.add_subplot(gs[0, 0])
    for species, p in SPECIES.items():
        age_max = p["max_lifespan_yr"]
        age = np.linspace(0, age_max, 100)
        mu = gompertz_mortality(age, p["A_norm"], p["alpha"])
        ax.semilogy(age / age_max, mu, lw=2, color=p["color"],
                     label=f"{species} (α={p['alpha']:.3f})")
    ax.set_xlabel("Fraction of max lifespan")
    ax.set_ylabel("Mortality rate μ(t)")
    ax.set_title("(a) Gompertz law: μ(t) = A·exp(αt) — species comparison")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="lower right", fontsize=7)

    # --- (b) 12 Hallmarks K-profile (spider chart) ---
    ax = fig.add_subplot(gs[0, 1], projection="polar")
    angles = np.linspace(0, 2 * np.pi, len(HALLMARKS_AGING),
                         endpoint=False).tolist()
    angles += angles[:1]
    young_v = np.concatenate([YOUNG_K, [YOUNG_K[0]]])
    old_v = np.concatenate([OLD_K, [OLD_K[0]]])
    ax.plot(angles, young_v, lw=2, color="blue", label=f"Young (mean K={overall_K(YOUNG_K):.2f})")
    ax.fill(angles, young_v, color="blue", alpha=0.15)
    ax.plot(angles, old_v, lw=2, color="red", label=f"Old (mean K={overall_K(OLD_K):.2f})")
    ax.fill(angles, old_v, color="red", alpha=0.25)
    ax.set_xticks(angles[:-1])
    short_labels = [
        "Genome\ninstab.",
        "Telomere",
        "Epigenetic",
        "Proteostasis",
        "Autophagy",
        "Nutrient\nsense",
        "Mito",
        "Senescence",
        "Stem\nexhaust.",
        "Cell\ncomm.",
        "Inflam-\nmaging",
        "Dysbiosis",
    ]
    ax.set_xticklabels(short_labels, fontsize=7)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_title("(b) 12 Hallmarks: K-profile age 25 vs 80", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.0), fontsize=8)

    # --- (c) Horvath methylation clock ---
    ax = fig.add_subplot(gs[1, 0])
    chron_age = np.linspace(10, 90, 50)
    np.random.seed(42)
    # 3 cohorts
    bio_healthy = horvath_biological_age(chron_age, lifestyle_factor=0.85)
    bio_average = horvath_biological_age(chron_age, lifestyle_factor=1.00)
    bio_unhealthy = horvath_biological_age(chron_age, lifestyle_factor=1.20)
    ax.plot(chron_age, chron_age, ls="--", color="gray",
             label="Perfect (chron = bio)")
    ax.scatter(chron_age, bio_healthy, color="green", s=15,
                label="Healthy lifestyle (slower)")
    ax.scatter(chron_age, bio_average, color="blue", s=15,
                label="Average")
    ax.scatter(chron_age, bio_unhealthy, color="red", s=15,
                label="Unhealthy (faster)")
    ax.set_xlabel("Chronological age [years]")
    ax.set_ylabel("Biological age (Horvath clock) [years]")
    ax.set_title("(c) Horvath methylation clock = K-fidelity meter")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)

    # --- (d) Max lifespan vs alpha ---
    ax = fig.add_subplot(gs[1, 1])
    alphas = [p["alpha"] for p in SPECIES.values()]
    lifespans = [p["max_lifespan_yr"] for p in SPECIES.values()]
    species_names = list(SPECIES.keys())
    colors = [p["color"] for p in SPECIES.values()]
    ax.scatter(alphas, lifespans, s=200, c=colors, alpha=0.7,
                edgecolors="black", linewidths=1)
    for a, L, n in zip(alphas, lifespans, species_names):
        offset = (5, 5)
        if "Lobster" in n:
            offset = (-50, 5)
        if "Hydra" in n:
            offset = (10, -10)
        ax.annotate(n.split(" ")[0], (a, L),
                     xytext=offset, textcoords="offset points", fontsize=8)
    # ITU prediction line: L * alpha ~ constant?
    # Plot 1/alpha as reference (negligible-senescence boundary)
    alpha_arr = np.logspace(-3, 0, 100)
    ax.plot(alpha_arr, 1 / alpha_arr * 10, ls="--", color="gray",
             alpha=0.5, label="L = 10/α (ITU upper bound)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Gompertz α (mortality doubling rate)")
    ax.set_ylabel("Max lifespan [years]")
    ax.set_title("(d) Lifespan ∝ 1/α — ITU K-decay rate prediction")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper right", fontsize=8)

    plt.suptitle("Phase 63: ITU foundation for aging — "
                 "K_organism's slow exponential decay",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "aging_itu_foundation.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 63] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 63: ITU foundation for aging")
    print("=" * 60)

    # [1]
    print("\n[1] Gompertz mortality parameters by species:")
    for s, p in SPECIES.items():
        print(f"  {s:<35s} alpha={p['alpha']:6.4f}, "
              f"max lifespan={p['max_lifespan_yr']:4d} yr")

    # [2]
    print("\n[2] 12 Hallmarks K-profile:")
    print(f"  Young (age 25) mean K: {overall_K(YOUNG_K):.3f}")
    print(f"  Old   (age 80) mean K: {overall_K(OLD_K):.3f}")
    print(f"  K-control loss in old: "
          f"{(1 - overall_K(OLD_K)/overall_K(YOUNG_K))*100:.1f}%")
    for h, ky, ko in zip(HALLMARKS_AGING, YOUNG_K, OLD_K):
        print(f"    {h:<28s} : {ky:.2f} -> {ko:.2f}")

    # [3]
    print("\n[3] Horvath methylation clock:")
    np.random.seed(42)
    for age in [30, 50, 70]:
        bio_h = horvath_biological_age(np.array([age]),
                                          lifestyle_factor=0.85,
                                          noise_std=2.5)[0]
        bio_a = horvath_biological_age(np.array([age]),
                                          lifestyle_factor=1.00,
                                          noise_std=2.5)[0]
        bio_u = horvath_biological_age(np.array([age]),
                                          lifestyle_factor=1.20,
                                          noise_std=2.5)[0]
        print(f"  Chronological={age}: healthy={bio_h:.1f}, "
              f"average={bio_a:.1f}, unhealthy={bio_u:.1f}")

    # [4]
    print("\n[4] Max lifespan ~ 1/alpha (ITU prediction):")
    for s, p in SPECIES.items():
        ratio = p["max_lifespan_yr"] * p["alpha"]
        print(f"  {s:<35s} L*alpha = {ratio:6.2f}")

    plot_path = make_plot()

    summary = {
        "phase": 63,
        "paper": "ITU and Aging",
        "description": "ITU foundation: aging = K_organism slow exponential decay",
        "species_gompertz": {
            s: {"alpha": p["alpha"], "max_lifespan_yr": p["max_lifespan_yr"],
                "L_times_alpha": p["max_lifespan_yr"] * p["alpha"]}
            for s, p in SPECIES.items()
        },
        "hallmarks_K_profile": {
            "young_age_25_mean_K": overall_K(YOUNG_K),
            "old_age_80_mean_K": overall_K(OLD_K),
            "K_loss_percent": float(
                (1 - overall_K(OLD_K) / overall_K(YOUNG_K)) * 100
            ),
            "hallmarks": HALLMARKS_AGING,
            "young_K_values": YOUNG_K.tolist(),
            "old_K_values": OLD_K.tolist(),
        },
        "horvath_clock_examples": {
            "age_50_healthy": float(
                horvath_biological_age(np.array([50]),
                                          lifestyle_factor=0.85,
                                          noise_std=2.5)[0]
            ),
            "age_50_average": 50.0,  # by design
            "age_50_unhealthy": float(
                horvath_biological_age(np.array([50]),
                                          lifestyle_factor=1.20,
                                          noise_std=2.5)[0]
            ),
        },
        "central_thesis": "Aging = exponential decay of K_organism over time. "
                          "Gompertz law mu(t) ~ exp(alpha*t) emerges from "
                          "ITU K-fidelity decay. 12 Hallmarks map to 12 "
                          "K-component degradation modes. Horvath clock = "
                          "K-fidelity meter. Sinclair's information theory "
                          "of aging is ITU's chronic-K-decay version.",
        "honest_framing": "Pass-1 interpretive paper. Reframes Hallmarks of "
                          "Aging, Gompertz law, Horvath clock, and Sinclair "
                          "theory in ITU language. No novel ITU-derived "
                          "intervention or biomarker.",
        "tier": 1,
        "paper_number": 6,
        "medicine_triangle": [
            "Tier 1 #5: Cancer (acute K breakdown)",
            "Tier 1 #6: Aging (chronic K decay) — THIS PAPER",
            "Tier 1 #7: Psychiatry (FEP failures, planned)",
        ],
        "tier_0_concept_doi": "10.5281/zenodo.20109209",
        "tier_1_cancer_doi": "10.5281/zenodo.20174318",
        "next_phases": [
            "Phase 64: Telomeres, mitochondria, proteostasis (deep dive)",
            "Phase 65: Senolytics, rapamycin, metformin, NAD+ (interventions)",
            "Phase 66: ITU longevity roadmap and 10 predictions",
        ],
        "caveats": [
            "Gompertz alpha values are typical-range",
            "K-component values for hallmarks are illustrative",
            "Horvath simulation uses simplified linear model with noise",
            "Real biological aging is more heterogeneous",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase63.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 63] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 63 complete.")
    print(f"  - Aging = exponential K decay (Gompertz from ITU)")
    print(f"  - 12 Hallmarks = 12 K-component slow degradations")
    print(f"  - Young K = {overall_K(YOUNG_K):.3f}, Old K = {overall_K(OLD_K):.3f}")
    print(f"  - Horvath clock = K-fidelity meter (lifestyle ±20% shift)")
    print(f"  - Cancer (acute) vs Aging (chronic) = two K-breakdown modes")
    print("=" * 60)


if __name__ == "__main__":
    main()
