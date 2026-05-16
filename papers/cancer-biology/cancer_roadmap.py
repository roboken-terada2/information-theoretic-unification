#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 62: ITU-informed cancer treatment roadmap 2026-2040 (Tier 1 #5 final)

ITU prediction: multi-K simultaneous restoration (cellular K + metabolic K
+ immune K) is the necessary therapeutic strategy. Single-axis monotherapy
fails because of K-redundancy and compensation.

Tests:
  1. Multi-axis combination response: 1, 2, 3, 4 axes
  2. 5-year survival projection 2024 -> 2040 for 9 cancer types
  3. Drug market growth + per-patient cost trajectory
  4. ITU vs status-quo therapeutic landscape

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #5 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Multi-axis combo response
# =============================================================================
def multi_axis_response(n_axes):
    """
    Approximate response rate as a function of n_axes simultaneously targeted.
    Single axis: 25%. Each additional axis adds diminishing returns.
    Saturation around 75-80%.
    """
    base = 0.25
    inc = [0, 0.20, 0.20, 0.10, 0.05]  # per-axis increment
    total = base
    for i in range(1, n_axes):
        if i < len(inc):
            total += inc[i]
    return min(total, 0.85)


# =============================================================================
# Test 2: 5-year survival projection
# =============================================================================
CANCER_PROJECTIONS = {
    "Melanoma (advanced)": {"2024": 50, "2030": 65, "2040": 80},
    "NSCLC":                {"2024": 25, "2030": 40, "2040": 60},
    "Breast":               {"2024": 90, "2030": 92, "2040": 95},
    "Colorectal":           {"2024": 65, "2030": 73, "2040": 85},
    "Pancreatic":           {"2024": 10, "2030": 25, "2040": 50},
    "Glioblastoma":         {"2024":  5, "2030": 10, "2040": 30},
    "Liver":                {"2024": 20, "2030": 35, "2040": 55},
    "Multiple myeloma":     {"2024": 60, "2030": 75, "2040": 90},
    "Hematologic overall":  {"2024": 70, "2030": 85, "2040": 95},
}


# =============================================================================
# Test 3: Market + cost trajectory
# =============================================================================
def market_USD_B(year):
    pts_y = np.array([2024, 2027, 2030, 2035, 2040])
    pts_v = np.array([240,  290,  350,  430,  500])
    return np.interp(year, pts_y, pts_v)


def cost_per_patient_USD_K(year):
    pts_y = np.array([2024, 2027, 2030, 2035, 2040])
    pts_v = np.array([50,    60,   80,  115,   150])
    return np.interp(year, pts_y, pts_v)


# =============================================================================
# Test 4: Therapeutic landscape (status-quo vs ITU)
# =============================================================================
THERAPY_LANDSCAPE = {
    "Chemo (single)":        {"axes": 1, "response": 25, "year": "1950s+"},
    "Targeted (single)":     {"axes": 1, "response": 30, "year": "2000s+"},
    "ICI (single)":          {"axes": 1, "response": 25, "year": "2014+"},
    "ICI + chemo":           {"axes": 2, "response": 40, "year": "2018+"},
    "Ipi+Nivo":              {"axes": 2, "response": 50, "year": "2015+"},
    "ICI + targeted + chemo": {"axes": 3, "response": 60, "year": "2024+"},
    "ITU 3-axis (full)":     {"axes": 3, "response": 70, "year": "2028+ (predicted)"},
    "ITU 4-axis (+microbiome)": {"axes": 4, "response": 80, "year": "2032+ (predicted)"},
}


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes_plot = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Multi-axis response ---
    ax = axes_plot[0, 0]
    n_arr = np.arange(1, 6)
    response = np.array([multi_axis_response(n) for n in n_arr]) * 100
    bars = ax.bar(n_arr, response,
                   color=["red", "orange", "green", "blue", "purple"],
                   alpha=0.7)
    for bar, v in zip(bars, response):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 1, f"{v:.0f}%",
                ha="center", fontsize=10)
    ax.axhline(50, ls="--", color="black", alpha=0.4, label="50% threshold")
    ax.set_xlabel("Number of K-axes targeted")
    ax.set_ylabel("Predicted response rate [%]")
    ax.set_title("(a) Multi-K combo: diminishing returns saturate ~80%")
    ax.set_xticks(n_arr)
    ax.set_xticklabels([f"{n}\n({'mono' if n==1 else 'combo'})"
                         for n in n_arr])
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend()
    ax.set_ylim(0, 100)

    # --- (b) 5-year survival projection ---
    ax = axes_plot[0, 1]
    cancers = list(CANCER_PROJECTIONS.keys())
    years = [2024, 2030, 2040]
    x = np.arange(len(cancers))
    width = 0.27
    for i, year in enumerate(years):
        vals = [CANCER_PROJECTIONS[c][str(year)] for c in cancers]
        bars = ax.bar(x + (i - 1) * width, vals, width,
                      label=str(year), alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([c.split(" ")[0][:9] for c in cancers],
                       fontsize=7, rotation=30)
    ax.set_ylabel("5-year survival (%)")
    ax.set_title("(b) ITU prediction: 2024 → 2040 survival")
    ax.legend(loc="upper right", fontsize=9, title="Year")
    ax.grid(True, alpha=0.3, axis="y")
    ax.set_ylim(0, 100)

    # --- (c) Market + per-patient cost ---
    ax = axes_plot[1, 0]
    years_arr = np.linspace(2024, 2040, 200)
    market = np.array([market_USD_B(y) for y in years_arr])
    cost = np.array([cost_per_patient_USD_K(y) for y in years_arr])
    ax.plot(years_arr, market, lw=2.5, color="green",
            label="Oncology market ($B)")
    ax2 = ax.twinx()
    ax2.plot(years_arr, cost, lw=2, color="red", ls="--",
              label="Cost/patient ($K)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Market size ($B)", color="green")
    ax2.set_ylabel("Cost per patient ($K)", color="red")
    ax.set_title("(c) Oncology market and per-patient cost")
    ax.grid(True, alpha=0.3)
    # combined legend
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper left")

    # --- (d) Therapeutic landscape ---
    ax = axes_plot[1, 1]
    names = list(THERAPY_LANDSCAPE.keys())
    n_axes = [THERAPY_LANDSCAPE[n]["axes"] for n in names]
    responses = [THERAPY_LANDSCAPE[n]["response"] for n in names]
    colors = ["gray", "gray", "gray", "blue", "blue", "purple", "darkgreen",
              "darkgreen"]
    sizes = [200] * len(names)
    sc = ax.scatter(n_axes, responses, s=sizes, c=colors, alpha=0.7,
                    edgecolors="black", linewidths=1)
    for n, r, name in zip(n_axes, responses, names):
        ax.annotate(name, (n, r), xytext=(8, 0),
                    textcoords="offset points", fontsize=7)
    ax.set_xlabel("K-axes targeted")
    ax.set_ylabel("Response rate (%)")
    ax.set_title("(d) Therapeutic landscape: status-quo → ITU")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.5, 5)
    ax.set_ylim(0, 100)
    # ITU sweet spot
    ax.axvspan(2.5, 4.5, alpha=0.1, color="green")
    ax.text(3.5, 90, "ITU sweet spot", ha="center",
            color="darkgreen", fontweight="bold", fontsize=9)

    plt.suptitle("Phase 62: ITU-informed cancer treatment roadmap 2026–2040 — "
                 "multi-K simultaneous restoration",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), "cancer_roadmap.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 62] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 62: ITU-informed cancer roadmap 2026-2040")
    print("=" * 60)

    # [1]
    print("\n[1] Multi-axis combo response (predicted):")
    for n in range(1, 6):
        r = multi_axis_response(n) * 100
        print(f"  {n}-axis ({'mono' if n == 1 else 'combo'}): {r:.1f}%")

    # [2]
    print("\n[2] 5-year survival projection (2024 -> 2040):")
    for c, d in CANCER_PROJECTIONS.items():
        delta = d["2040"] - d["2024"]
        print(f"  {c:<22s} : {d['2024']:3d}% -> {d['2040']:3d}% "
              f"(+{delta} pts)")

    # [3]
    print("\n[3] Market + cost trajectory:")
    for y in [2024, 2030, 2035, 2040]:
        m = market_USD_B(y)
        c = cost_per_patient_USD_K(y)
        print(f"  {y}: market=${m:5.0f}B, cost/patient=${c:5.0f}K")

    # [4]
    print("\n[4] Therapeutic landscape:")
    for name, data in THERAPY_LANDSCAPE.items():
        print(f"  {name:<28s} (axes={data['axes']}) : "
              f"{data['response']:3d}%, since {data['year']}")

    plot_path = make_plot()

    predictions = [
        "3-axis combo for MSS colorectal achieves ≥30% response by 2028",
        "mRNA cancer vaccine achieves melanoma 5-yr survival ≥80% by 2030",
        "KRAS G12D inhibitor (post-sotorasib) FDA-approved by 2027",
        "Quantum computing identifies ≥1 new oncology target by 2030",
        "TIL therapy standardised for ≥5 solid-tumor types by 2032",
        "Multi-K liquid biopsy becomes ASCO standard by 2029",
        "Pancreatic 5-yr survival reaches 30% by 2032",
        "Glioblastoma 5-yr survival reaches 20% by 2034",
        "First microbiome-modulating cancer drug FDA-approved by 2030",
        "ITU multi-K therapeutic index added to NCCN guidelines by 2033",
    ]

    summary = {
        "phase": 62,
        "paper": "ITU and Cancer Biology",
        "description": "ITU-informed cancer treatment roadmap (Tier 1 #5 final)",
        "multi_K_response": {
            f"{n}_axes": float(multi_axis_response(n))
            for n in range(1, 6)
        },
        "five_year_survival_projection": CANCER_PROJECTIONS,
        "market_USD_B": {
            str(y): float(market_USD_B(y))
            for y in [2024, 2027, 2030, 2035, 2040]
        },
        "cost_per_patient_USD_K": {
            str(y): float(cost_per_patient_USD_K(y))
            for y in [2024, 2027, 2030, 2035, 2040]
        },
        "therapy_landscape": THERAPY_LANDSCAPE,
        "falsifiable_predictions": predictions,
        "paper_complete": True,
        "central_thesis": "Cancer = multi-K breakdown; multi-K simultaneous "
                          "restoration (cellular + metabolic + immune) is the "
                          "ITU-necessary therapeutic strategy. ITU predicts "
                          "5-year survival 30-50% for currently-untreatable "
                          "pancreatic and glioblastoma by 2040.",
        "honest_framing": "Pass-1 interpretive paper across 4 phases. "
                          "Reframes Hallmarks, Warburg, immune evasion, and "
                          "drug response in ITU language. Predictions are "
                          "consistent with industry consensus rather than "
                          "ITU-unique. Pass-2 work would derive a specific "
                          "ITU figure-of-merit for patient stratification.",
        "tier": 1,
        "paper_number": 5,
        "tier_0_concept_doi": "10.5281/zenodo.20109209",
        "tier_1_qc_doi": "10.5281/zenodo.20139391",
        "tier_1_ai_doi": "10.5281/zenodo.20150501",
        "tier_1_crypto_doi": "10.5281/zenodo.20151059",
        "tier_1_semi_doi": "10.5281/zenodo.20174036",
        "engineering_rectangle_complete": True,
        "medicine_start": "Tier 1 #5 begins medicine vector "
                          "(cancer -> aging #6 -> psychiatry #7)",
        "next_paper_candidates": [
            "Tier 1 #6: Aging (organism K degradation over time)",
            "Tier 1 #7: Psychiatry (FEP failures in brain K)",
            "Tier 1 #8: Economics (information markets)",
        ],
        "caveats": [
            "Multi-axis response uses linear-with-saturation model",
            "Survival projections are ITU-informed but extrapolative",
            "Market/cost trajectory assumes current trend continuation",
            "10 predictions overlap with industry consensus; not all ITU-unique",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase62.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 62] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 62 complete. Tier 1 #5 (Cancer Biology) ready for Zenodo.")
    print("  - Multi-K combo: 1->25%, 2->45%, 3->65%, 4->75%, 5->80%")
    print("  - Pancreatic 5-yr survival: 10% (2024) -> 50% (2040)")
    print("  - GBM 5-yr survival: 5% (2024) -> 30% (2040)")
    print("  - 10 falsifiable predictions issued")
    print("  - Engineering rectangle (#1-#4) -> + medicine (#5) begin")
    print("=" * 60)


if __name__ == "__main__":
    main()
