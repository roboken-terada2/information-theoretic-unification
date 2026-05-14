#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 67: ITU Foundation for Psychiatry

Friston Free Energy Principle (FEP) is the brain-specific incarnation
of the ITU axiom dS = d<K>. Eight major psychiatric disorders are
re-classified as K-component failures of the predictive-brain machinery.

Tests:
  1. 8 disorders mapped to K-component profile (spider chart)
  2. Disease burden (DALYs) for major mental disorders
  3. Treatment response rate vs K-identification difficulty
  4. FEP <-> ITU axiom equivalence (illustrative free-energy curves)

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #7 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Disorder database
# =============================================================================
DISORDERS = {
    "Schizophrenia": {
        "main_K": "K_precision_sensory",
        "DALYs_M": 13.9,
        "prevalence_pct": 0.3,
        "first_line_response": 0.65,
        "K_diff_score": 0.7,
        "K_profile": [0.30, 0.70, 0.85, 0.75, 0.20, 0.80, 0.50, 0.65, 0.80],
        "color": "purple",
    },
    "Major Depression": {
        "main_K": "K_reward",
        "DALYs_M": 47.5,
        "prevalence_pct": 3.8,
        "first_line_response": 0.40,
        "K_diff_score": 0.6,
        "K_profile": [0.80, 0.85, 0.25, 0.80, 0.60, 0.40, 0.55, 0.65, 0.45],
        "color": "blue",
    },
    "Anxiety": {
        "main_K": "K_threat",
        "DALYs_M": 26.4,
        "prevalence_pct": 4.0,
        "first_line_response": 0.50,
        "K_diff_score": 0.5,
        "K_profile": [0.85, 0.85, 0.55, 0.20, 0.70, 0.65, 0.65, 0.60, 0.55],
        "color": "orange",
    },
    "PTSD": {
        "main_K": "K_threat (trauma)",
        "DALYs_M": 8.4,
        "prevalence_pct": 2.6,
        "first_line_response": 0.45,
        "K_diff_score": 0.55,
        "K_profile": [0.80, 0.80, 0.50, 0.10, 0.60, 0.55, 0.45, 0.50, 0.40],
        "color": "darkred",
    },
    "ASD (Autism)": {
        "main_K": "K_social (rigid)",
        "DALYs_M": 11.5,
        "prevalence_pct": 1.0,
        "first_line_response": 0.30,
        "K_diff_score": 0.8,
        "K_profile": [0.85, 0.70, 0.65, 0.65, 0.65, 0.60, 0.20, 0.55, 0.75],
        "color": "green",
    },
    "ADHD": {
        "main_K": "K_attention",
        "DALYs_M": 16.5,
        "prevalence_pct": 5.0,
        "first_line_response": 0.70,
        "K_diff_score": 0.4,
        "K_profile": [0.80, 0.75, 0.60, 0.70, 0.20, 0.55, 0.55, 0.65, 0.70],
        "color": "red",
    },
    "OCD": {
        "main_K": "K_action (precision)",
        "DALYs_M": 5.1,
        "prevalence_pct": 1.2,
        "first_line_response": 0.60,
        "K_diff_score": 0.6,
        "K_profile": [0.80, 0.80, 0.55, 0.50, 0.50, 0.20, 0.60, 0.60, 0.65],
        "color": "brown",
    },
    "Bipolar Disorder": {
        "main_K": "K_mood (oscillatory)",
        "DALYs_M": 7.5,
        "prevalence_pct": 0.6,
        "first_line_response": 0.55,
        "K_diff_score": 0.7,
        "K_profile": [0.80, 0.80, 0.20, 0.55, 0.55, 0.50, 0.60, 0.20, 0.55],
        "color": "navy",
    },
}

# K-component axes
K_AXES = [
    "K_perception",
    "K_precision",
    "K_reward",
    "K_threat",
    "K_attention",
    "K_action",
    "K_social",
    "K_mood",
    "K_self_model",
]


# =============================================================================
# Test 1: K-component spider chart per disorder
# =============================================================================
def get_K_profile(disorder):
    return np.array(DISORDERS[disorder]["K_profile"])


# =============================================================================
# Test 2: DALYs
# =============================================================================
def total_psych_DALYs():
    return sum(d["DALYs_M"] for d in DISORDERS.values())


# =============================================================================
# Test 3: Treatment response vs K-difficulty
# =============================================================================
def make_response_difficulty():
    names, resp, diff = [], [], []
    for n, d in DISORDERS.items():
        names.append(n)
        resp.append(d["first_line_response"])
        diff.append(d["K_diff_score"])
    return names, np.array(resp), np.array(diff)


# =============================================================================
# Test 4: FEP <-> ITU illustrative
# =============================================================================
def free_energy_vs_belief(error_arr, precision=1.0):
    """F = 0.5 * precision * error^2 (linear-Gaussian, illustrative)."""
    return 0.5 * precision * error_arr ** 2


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig = plt.figure(figsize=(13, 10))
    gs = fig.add_gridspec(2, 2)

    # --- (a) K-component spider chart (4 selected disorders) ---
    ax = fig.add_subplot(gs[0, 0], projection="polar")
    angles = np.linspace(0, 2 * np.pi, len(K_AXES), endpoint=False).tolist()
    angles += angles[:1]
    selected = ["Major Depression", "Schizophrenia", "ASD (Autism)", "ADHD"]
    for d in selected:
        prof = get_K_profile(d)
        v = np.concatenate([prof, [prof[0]]])
        ax.plot(angles, v, lw=2, color=DISORDERS[d]["color"], label=d)
        ax.fill(angles, v, color=DISORDERS[d]["color"], alpha=0.1)
    ax.set_xticks(angles[:-1])
    short_K = ["Perc.", "Prec.", "Reward", "Threat",
               "Atten.", "Action", "Social", "Mood", "Self"]
    ax.set_xticklabels(short_K, fontsize=8)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_title("(a) K-component profiles — selected disorders", pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.0), fontsize=8)

    # --- (b) DALYs by disorder ---
    ax = fig.add_subplot(gs[0, 1])
    names = list(DISORDERS.keys())
    dalys = [DISORDERS[n]["DALYs_M"] for n in names]
    colors = [DISORDERS[n]["color"] for n in names]
    # sort by DALYs descending
    idx = np.argsort(dalys)[::-1]
    names_sorted = [names[i] for i in idx]
    dalys_sorted = [dalys[i] for i in idx]
    colors_sorted = [colors[i] for i in idx]
    bars = ax.barh(names_sorted, dalys_sorted, color=colors_sorted,
                    alpha=0.7, edgecolor="black")
    for bar, v in zip(bars, dalys_sorted):
        ax.text(v + 0.5, bar.get_y() + bar.get_height() / 2, f"{v:.1f}M",
                va="center", fontsize=8)
    ax.set_xlabel("Global DALYs (millions)")
    ax.set_title("(b) Global disease burden — psychiatric disorders (2021)")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=8)

    # --- (c) Treatment response vs K-identification difficulty ---
    ax = fig.add_subplot(gs[1, 0])
    names_r, resp, diff = make_response_difficulty()
    for n, r, d in zip(names_r, resp, diff):
        ax.scatter(d, r * 100, s=200, c=DISORDERS[n]["color"], alpha=0.7,
                    edgecolors="black")
        ax.annotate(n, (d, r * 100), xytext=(8, -5),
                     textcoords="offset points", fontsize=8)
    # Trend line (rough negative correlation)
    z = np.polyfit(diff, resp * 100, 1)
    x_fit = np.linspace(0.3, 0.9, 50)
    y_fit = np.polyval(z, x_fit)
    ax.plot(x_fit, y_fit, ls="--", color="gray", alpha=0.5,
             label=f"Trend: slope = {z[0]:.0f}")
    ax.set_xlabel("K-component identification difficulty")
    ax.set_ylabel("First-line treatment response rate [%]")
    ax.set_title("(c) Treatment success ↔ K-identification ease")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")
    ax.set_xlim(0.3, 0.9)
    ax.set_ylim(20, 80)

    # --- (d) FEP <-> ITU equivalence ---
    ax = fig.add_subplot(gs[1, 1])
    error_arr = np.linspace(-3, 3, 100)
    F_low_prec = free_energy_vs_belief(error_arr, precision=0.5)
    F_normal = free_energy_vs_belief(error_arr, precision=1.0)
    F_high_prec = free_energy_vs_belief(error_arr, precision=2.0)
    ax.plot(error_arr, F_low_prec, lw=2, color="green",
             label="Low precision (broad K)")
    ax.plot(error_arr, F_normal, lw=2, color="blue",
             label="Normal precision")
    ax.plot(error_arr, F_high_prec, lw=2, color="red",
             label="High precision (sharp K) — psychosis?")
    ax.axhline(0, ls="-", color="black", alpha=0.5)
    ax.axvline(0, ls=":", color="gray", alpha=0.5,
               label="Zero prediction error")
    ax.set_xlabel("Prediction error")
    ax.set_ylabel("Free energy F (∝ δS = δ⟨K⟩)")
    ax.set_title("(d) FEP curves ⇔ ITU dS = d⟨K⟩")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper center", fontsize=8)

    plt.suptitle("Phase 67: ITU foundation for psychiatry — "
                 "FEP as the brain-specific axiom",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "psychiatry_itu_foundation.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 67] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 67: ITU foundation for psychiatry")
    print("=" * 60)

    # [1]
    print("\n[1] K-component profiles (8 disorders):")
    print(f"  {'Disorder':<22s} main K-failure        prev%")
    for n, d in DISORDERS.items():
        print(f"  {n:<22s} {d['main_K']:<22s} {d['prevalence_pct']}%")

    # [2]
    print("\n[2] Global DALYs (millions, 2021):")
    total = total_psych_DALYs()
    for n, d in sorted(DISORDERS.items(), key=lambda x: -x[1]["DALYs_M"]):
        pct = d["DALYs_M"] / total * 100
        print(f"  {n:<22s} : {d['DALYs_M']:5.1f}M ({pct:5.1f}%)")
    print(f"  {'TOTAL psychiatric':<22s} : {total:5.1f}M (~7% of all DALYs)")

    # [3]
    print("\n[3] Treatment response vs K-difficulty:")
    names_r, resp, diff = make_response_difficulty()
    for n, r, d in zip(names_r, resp, diff):
        print(f"  {n:<22s} : response {r*100:5.1f}%, "
              f"K-difficulty {d:.2f}")

    # [4]
    print("\n[4] FEP <-> ITU axiom equivalence (illustrative):")
    print(f"  F = 0.5 * precision * (prediction_error)^2")
    print(f"  Low precision: K is broad, errors tolerated -> healthy")
    print(f"  High precision: K is sharp, small errors cost much -> psychosis-prone")

    plot_path = make_plot()

    summary = {
        "phase": 67,
        "paper": "ITU and Psychiatry",
        "description": "ITU foundation: FEP = brain-specific ITU axiom",
        "disorders": {
            n: {
                "main_K_failure": d["main_K"],
                "DALYs_M": d["DALYs_M"],
                "prevalence_pct": d["prevalence_pct"],
                "first_line_response": d["first_line_response"],
                "K_diff_score": d["K_diff_score"],
                "K_profile": d["K_profile"],
            }
            for n, d in DISORDERS.items()
        },
        "K_axes": K_AXES,
        "total_psych_DALYs_M": float(total),
        "global_economic_burden_USD_T": 5.0,
        "us_annual_cost_USD_B": 430,
        "central_thesis": "Psychiatric disorders = K-component failures of "
                          "predictive brain machinery. Friston FEP is the "
                          "brain-specific incarnation of ITU dS = d<K>. "
                          "Each disorder maps to a specific K-component "
                          "(precision, reward, threat, attention, etc.).",
        "honest_framing": "Pass-1 interpretive paper. K-profile values are "
                          "illustrative assignments based on computational "
                          "psychiatry literature (Friston, Adams, Sterzer). "
                          "Disease burden and prevalence from WHO/IHME GBD 2021. "
                          "No ITU-unique predictions yet.",
        "tier": 1,
        "paper_number": 7,
        "medicine_triangle_progress": "Cancer (#5) + Aging (#6) + Psychiatry (#7) "
                                       "= medicine triangle complete after Tier 1 #7",
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "tier_1_cancer_doi": "10.5281/zenodo.20174318",
        "tier_1_aging_doi": "10.5281/zenodo.20175663",
        "next_phases": [
            "Phase 68: Schizophrenia (precision-weighting, dopamine, antipsychotics)",
            "Phase 69: Depression + anxiety (mood K, SSRI, ketamine, psilocybin)",
            "Phase 70: ASD/ADHD + treatment roadmap",
        ],
        "caveats": [
            "K-profile values are illustrative, not measured",
            "DALYs from GBD 2021 (WHO/IHME)",
            "Treatment response rates from STAR*D, CATIE, IPAT etc.",
            "K-identification difficulty is heuristic ranking",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase67.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 67] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 67 complete.")
    print(f"  - Total psychiatric DALYs: {total:.1f}M (~7% global)")
    print(f"  - FEP = brain-specific ITU axiom")
    print(f"  - 8 disorders mapped to 9 K-component axes")
    print("=" * 60)


if __name__ == "__main__":
    main()
