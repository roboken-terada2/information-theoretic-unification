#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 58: Semiconductor Industry Roadmap 2026-2040

Tier 1 #4 final phase. Synthesises Phase 55-57 into market/policy forecasts.

Tests:
  1. Logistic adoption curves for 7 technologies
  2. Process node progression and gate length floor
  3. Market size (TAM) + capex projection 2024-2040
  4. Geopolitical wafer-capacity share

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #4 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


def logistic(t, t0, k):
    return 1.0 / (1.0 + np.exp(-k * (t - t0)))


# =============================================================================
# Test 1: Technology adoption logistic curves
# =============================================================================
TECHNOLOGIES = {
    "GAAFET (general)":    {"t0": 2027, "k": 0.8, "color": "black"},
    "Photonic interconnect": {"t0": 2029, "k": 0.6, "color": "orange"},
    "Spin MRAM (cache)":   {"t0": 2031, "k": 0.5, "color": "darkgreen"},
    "CFET stacked":        {"t0": 2032, "k": 0.4, "color": "blue"},
    "NC-FET logic":        {"t0": 2034, "k": 0.3, "color": "purple"},
    "2D material FET":     {"t0": 2036, "k": 0.25, "color": "brown"},
    "TFET (production)":   {"t0": 2038, "k": 0.2, "color": "red"},
}


# =============================================================================
# Test 2: Process node floor
# =============================================================================
def process_node_floor(year):
    """Smallest commercial node (nm) by year.
       Saturates around 0.5 nm — fundamental limit."""
    nodes_year = np.array([2014, 2018, 2020, 2022, 2024, 2026, 2028,
                            2030, 2032, 2035, 2038, 2040])
    nodes_nm   = np.array([14,    7,    5,    4,    3,    2,    1.4,
                             1.0,  0.7,  0.5,  0.5,  0.5])
    return np.interp(year, nodes_year, nodes_nm)


# =============================================================================
# Test 3: Market + capex
# =============================================================================
def market_size_USD_B(year):
    """Semiconductor TAM ($B). 2024=600, 2030=1000, 2040=2000."""
    pts_y = np.array([2024, 2027, 2030, 2035, 2040])
    pts_v = np.array([600,   750,  1000, 1500, 2000])
    return np.interp(year, pts_y, pts_v)


def capex_USD_B(year):
    pts_y = np.array([2024, 2027, 2030, 2035, 2040])
    pts_v = np.array([175,   250,  350,  400,  500])
    return np.interp(year, pts_y, pts_v)


# =============================================================================
# Test 4: Wafer-fab geopolitics
# =============================================================================
def country_share(year):
    """Wafer capacity share by region (sum = 1.0).
    Captures expected geographic diversification."""
    # 2024 baseline: TSMC ~55% of leading-edge, then projected diversification
    years = np.array([2024, 2027, 2030, 2035, 2040])
    Taiwan = np.array([0.55, 0.50, 0.45, 0.40, 0.36])
    Korea  = np.array([0.18, 0.18, 0.18, 0.17, 0.17])
    USA    = np.array([0.10, 0.13, 0.17, 0.20, 0.22])
    China  = np.array([0.07, 0.08, 0.09, 0.10, 0.10])
    Japan  = np.array([0.05, 0.06, 0.07, 0.08, 0.09])
    EU     = np.array([0.05, 0.05, 0.04, 0.05, 0.06])
    return {
        "Taiwan": float(np.interp(year, years, Taiwan)),
        "Korea":  float(np.interp(year, years, Korea)),
        "USA":    float(np.interp(year, years, USA)),
        "China":  float(np.interp(year, years, China)),
        "Japan":  float(np.interp(year, years, Japan)),
        "EU":     float(np.interp(year, years, EU)),
    }


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Tech adoption logistic curves ---
    ax = axes[0, 0]
    years = np.linspace(2024, 2040, 200)
    for name, p in TECHNOLOGIES.items():
        adoption = logistic(years, p["t0"], p["k"])
        ax.plot(years, adoption * 100, lw=2, color=p["color"],
                label=f"{name} (t₀={p['t0']})")
    ax.axhline(50, ls="--", color="gray", alpha=0.5, label="50% adoption")
    ax.set_xlabel("Year")
    ax.set_ylabel("Adoption (%)")
    ax.set_title("(a) Beyond-CMOS adoption — logistic projection 2024–2040")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7, loc="lower right")
    ax.set_ylim(0, 100)

    # --- (b) Process node floor ---
    ax = axes[0, 1]
    years = np.linspace(2014, 2040, 200)
    nodes = np.array([process_node_floor(y) for y in years])
    ax.plot(years, nodes, lw=2, color="navy", marker="o", ms=3)
    ax.axhline(0.5, ls="--", color="red", alpha=0.7,
               label="Quantum floor (~0.5 nm)")
    ax.axhline(1.0, ls=":", color="orange", alpha=0.5,
               label="CFET limit (~1 nm)")
    # annotate phases
    ax.annotate("FinFET era", xy=(2017, 7), fontsize=8, ha="center")
    ax.annotate("GAAFET", xy=(2026, 2), fontsize=8, ha="center")
    ax.annotate("CFET", xy=(2031, 1.0), fontsize=8, ha="center")
    ax.annotate("Post-classical\nMOSFET", xy=(2038, 0.5), fontsize=8,
                ha="center", color="red")
    ax.set_xlabel("Year")
    ax.set_ylabel("Smallest commercial node [nm]")
    ax.set_yscale("log")
    ax.set_title("(b) Process node floor — saturating at 0.5 nm")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper right", fontsize=9)

    # --- (c) Market size + capex ---
    ax = axes[1, 0]
    years = np.linspace(2024, 2040, 200)
    market = np.array([market_size_USD_B(y) for y in years])
    capex = np.array([capex_USD_B(y) for y in years])
    ax.plot(years, market, lw=2.5, color="green", label="Semi TAM ($B)")
    ax.plot(years, capex, lw=2, color="red", linestyle="--",
            label="Capex ($B)")
    ax.axhline(1000, ls=":", color="black", alpha=0.5)
    ax.annotate("$1 trillion @ 2030", xy=(2030, 1000),
                xytext=(2025, 1300), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black"))
    ax.set_xlabel("Year")
    ax.set_ylabel("Industry size ($B)")
    ax.set_title("(c) Semiconductor TAM + capex projection")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")

    # --- (d) Geopolitics: wafer share ---
    ax = axes[1, 1]
    years = np.array([2024, 2027, 2030, 2035, 2040])
    regions = ["Taiwan", "Korea", "USA", "China", "Japan", "EU"]
    colors = ["red", "blue", "gold", "darkred", "white", "orange"]
    edgecolors = ["red", "blue", "gold", "darkred", "black", "orange"]
    shares = {r: [country_share(y)[r] for y in years] for r in regions}
    # Stacked area chart
    bottom = np.zeros_like(years, dtype=float)
    for r, c, e in zip(regions, colors, edgecolors):
        ax.fill_between(years, bottom, bottom + np.array(shares[r]),
                         alpha=0.7, label=r, color=c, edgecolor=e, linewidth=0.5)
        bottom = bottom + np.array(shares[r])
    ax.set_xlabel("Year")
    ax.set_ylabel("Wafer capacity share (leading-edge)")
    ax.set_title("(d) Geopolitical diversification: Taiwan losing dominance")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xlim(2024, 2040)
    ax.set_ylim(0, 1.0)
    ax.grid(True, alpha=0.2)

    plt.suptitle("Phase 58: Semiconductor industry roadmap 2026–2040 — "
                 "completing the ITU engineering rectangle",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), "industry_roadmap.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 58] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 58: Semiconductor industry roadmap 2026-2040")
    print("=" * 60)

    # [1] Logistic curves
    print("\n[1] Technology adoption (logistic, % at year 2030):")
    for name, p in TECHNOLOGIES.items():
        v = logistic(2030, p["t0"], p["k"]) * 100
        print(f"  {name:<25s} : {v:5.1f}%  (50% at year {p['t0']})")

    # [2] Process node floor
    print("\n[2] Process node floor at key years:")
    for y in [2024, 2026, 2028, 2030, 2035, 2040]:
        node = process_node_floor(y)
        print(f"  {y} : {node:.2f} nm")

    # [3] Market
    print("\n[3] Market ($B):")
    for y in [2024, 2027, 2030, 2035, 2040]:
        m = market_size_USD_B(y)
        c = capex_USD_B(y)
        print(f"  {y} : TAM = ${m:5.0f}B   Capex = ${c:4.0f}B")

    # [4] Geopolitics
    print("\n[4] Wafer capacity share by region:")
    for y in [2024, 2030, 2040]:
        shares = country_share(y)
        line = "  " + str(y) + " : "
        line += " ".join(f"{r}={s*100:4.1f}%" for r, s in shares.items())
        print(line)

    plot_path = make_plot()

    # Falsifiable predictions
    predictions = [
        "GAAFET 2nm mass production by 2026 (TSMC or Samsung)",
        "CFET 1.4nm prototype demonstrated by 2028",
        "Photonic AI chip (>$10/unit) commercial by 2027",
        "Embedded MRAM replaces L3 cache by 2029",
        "Si CMOS will not reach below 0.7 nm (end of classical MOSFET)",
        "Semi market reaches $1T by 2030",
        "Taiwan leading-edge share falls below 50% by 2032",
        "NC-FET mass production not before 2035 (reliability issues)",
        "2D material (MoS2) FET demonstrates 1 nm in lab by 2030",
        "Quantum-classical hybrid SoC (CMOS + superconductor) commercial by 2034",
    ]

    summary = {
        "phase": 58,
        "paper": "ITU and Semiconductors",
        "description": "Industry roadmap 2026-2040, geopolitics, ITU forecasts",
        "technology_adoption_50pct_year": {
            name: p["t0"] for name, p in TECHNOLOGIES.items()
        },
        "process_node_by_year": {
            str(y): float(process_node_floor(y))
            for y in [2024, 2026, 2028, 2030, 2032, 2035, 2038, 2040]
        },
        "market_USD_B": {
            str(y): float(market_size_USD_B(y))
            for y in [2024, 2027, 2030, 2035, 2040]
        },
        "capex_USD_B": {
            str(y): float(capex_USD_B(y))
            for y in [2024, 2027, 2030, 2035, 2040]
        },
        "wafer_share_2030": country_share(2030),
        "wafer_share_2040": country_share(2040),
        "engineering_rectangle": {
            "Tier_1_paper_1_QC":      "10.5281/zenodo.20139391",
            "Tier_1_paper_2_AI":      "10.5281/zenodo.20150501",
            "Tier_1_paper_3_Crypto":  "10.5281/zenodo.20151059",
            "Tier_1_paper_4_Semi":    "(this paper, pending)",
        },
        "falsifiable_predictions": predictions,
        "paper_complete": True,
        "central_thesis": "Semiconductor industry trajectory follows ITU "
                          "predictions: classical MOSFET ends ~0.7 nm, "
                          "heterogeneous SoCs dominate 2030s, Taiwan "
                          "concentration diversifies as engineering "
                          "redundancy demands.",
        "tier": 1,
        "paper_number": 4,
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "tier_1_qc_doi": "10.5281/zenodo.20139391",
        "tier_1_ai_doi": "10.5281/zenodo.20150501",
        "tier_1_crypto_doi": "10.5281/zenodo.20151059",
        "next_paper_candidates": [
            "Tier 1 #5: Cancer biology (cell dS abnormality)",
            "Tier 1 #6: Aging (organism <K> degradation)",
            "Tier 1 #7: Psychiatry (FEP failures)",
        ],
        "caveats": [
            "Logistic curves use illustrative parameters",
            "Market/capex projections extrapolate current trends",
            "Geopolitical assumptions can change rapidly",
            "ITU predictions are first-principles; real industry has noise",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase58.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 58] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 58 complete. Tier 1 #4 (Semiconductors) ready for Zenodo.")
    print(f"  - Engineering rectangle (Tier 1 #1-#4) formed")
    print(f"  - 10 falsifiable predictions issued (2026-2040)")
    print(f"  - $1T market projected at 2030")
    print(f"  - Taiwan share drops 55% -> 36% by 2040")
    print("=" * 60)


if __name__ == "__main__":
    main()
