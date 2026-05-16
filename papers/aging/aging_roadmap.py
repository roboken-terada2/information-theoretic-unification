#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 66: Longevity roadmap 2026-2050 (Tier 1 #6 final)

ITU prediction: multi-K interventions reach the market over the next
25 years; average lifespan rises from 82 -> 95 yr, healthspan from
72 -> 92 yr (lifespan-healthspan gap shrinks 10 -> 3 yr).

Tests:
  1. Historical + projected lifespan (3 scenarios)
  2. Healthspan-lifespan gap evolution
  3. Longevity industry investment growth
  4. Regulatory milestones timeline

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #6 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Historical + projected lifespan
# =============================================================================
def lifespan_scenarios(year):
    """Return three scenarios for average lifespan (developed countries)."""
    year = np.asarray(year, dtype=float)
    # Historical anchors (developed-country average) + future status quo
    hist_years = np.array([1800, 1900, 1950, 2000, 2024, 2050])
    hist_vals = np.array([35, 47, 68, 78, 82, 88.5])  # status quo: +2.5/decade
    statusquo = np.interp(year, hist_years, hist_vals)
    # ITU multi-K scenario (mid): +5 yr by 2040, +13 yr by 2050
    itu_mid = np.interp(year, [1800, 2024, 2030, 2040, 2050],
                        [35, 82, 85, 90, 95])
    # OSKM + combo scenario (optimistic)
    itu_opt = np.interp(year, [1800, 2024, 2030, 2040, 2050],
                         [35, 82, 86, 93, 100])
    return statusquo, itu_mid, itu_opt


# =============================================================================
# Test 2: Healthspan vs lifespan
# =============================================================================
def healthspan_lifespan(year):
    """Predicted healthspan and lifespan (ITU mid scenario)."""
    year = np.asarray(year, dtype=float)
    lifespan = np.interp(year, [2024, 2030, 2040, 2050], [82, 85, 90, 95])
    healthspan = np.interp(year, [2024, 2030, 2040, 2050], [72, 78, 85, 92])
    gap = lifespan - healthspan
    return lifespan, healthspan, gap


# =============================================================================
# Test 3: Industry investment
# =============================================================================
def industry_investment_USD_B(year):
    """Total longevity investment by year ($B)."""
    pts_y = np.array([2018, 2020, 2022, 2024, 2030, 2040, 2050])
    pts_v = np.array([0.5,   1.5,  4.0,  5.2,  15,   50,   120])
    return np.interp(year, pts_y, pts_v)


COMPANIES_2024 = {
    "Altos Labs":         {"funding_M_USD": 3000, "year": 2021, "focus": "OSKM"},
    "Calico (Alphabet)":  {"funding_M_USD": 3000, "year": 2013, "focus": "basic"},
    "Retro Biosciences":  {"funding_M_USD": 180,  "year": 2021, "focus": "OSKM"},
    "Unity Biotech":      {"funding_M_USD": 300,  "year": 2011, "focus": "senolytics"},
    "Loyal":              {"funding_M_USD": 75,   "year": 2019, "focus": "dog longevity"},
    "Insilico Medicine":  {"funding_M_USD": 400,  "year": 2014, "focus": "AI drug disc."},
    "Life Biosciences":   {"funding_M_USD": 60,   "year": 2017, "focus": "Sinclair-aligned"},
}


# =============================================================================
# Test 4: Regulatory milestones
# =============================================================================
MILESTONES = [
    {"year": 2024, "event": "Loyal LOY-001: dog longevity RXE", "tier": "achieved"},
    {"year": 2028, "event": "TAME trial primary endpoint",     "tier": "expected"},
    {"year": 2030, "event": "FDA discusses 'biological aging'", "tier": "predicted"},
    {"year": 2032, "event": "Senolytics broad approvals",       "tier": "predicted"},
    {"year": 2035, "event": "First in-human OSKM trial",        "tier": "predicted"},
    {"year": 2038, "event": "Multi-K combo insurance coverage", "tier": "predicted"},
    {"year": 2040, "event": "ICD-12 codes 'biological aging'",  "tier": "predicted"},
    {"year": 2050, "event": "Healthspan-lifespan gap < 3 yr",   "tier": "predicted"},
]


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Lifespan scenarios ---
    ax = axes[0, 0]
    yrs_full = np.linspace(1800, 2050, 200)
    sq, mid, opt = lifespan_scenarios(yrs_full)
    ax.plot(yrs_full, sq, lw=2, color="gray", label="Status quo")
    ax.plot(yrs_full, mid, lw=2, color="blue",
            label="ITU multi-K (mid)")
    ax.plot(yrs_full, opt, lw=2.5, color="red",
            label="ITU + OSKM (optimistic)")
    # Historical anchor points
    hist_x = [1800, 1900, 1950, 2000, 2024]
    hist_y = [35, 47, 68, 78, 82]
    ax.scatter(hist_x, hist_y, s=80, color="black", zorder=5,
                label="Historical")
    ax.axvline(2024, ls=":", color="black", alpha=0.5)
    ax.axhline(100, ls="--", color="red", alpha=0.4, label="Centenarian")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average lifespan (developed countries) [years]")
    ax.set_title("(a) Lifespan history + ITU projection")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)
    ax.set_xlim(1800, 2055)
    ax.set_ylim(30, 105)

    # --- (b) Healthspan vs lifespan ---
    ax = axes[0, 1]
    yrs = np.linspace(2024, 2050, 100)
    lifespan, healthspan, gap = healthspan_lifespan(yrs)
    ax.fill_between(yrs, healthspan, lifespan,
                     color="red", alpha=0.3, label="Unhealthy gap")
    ax.plot(yrs, lifespan, lw=2, color="blue", label="Lifespan")
    ax.plot(yrs, healthspan, lw=2, color="green", label="Healthspan")
    # Annotate gap
    for yr in [2024, 2050]:
        ls, hs, g = healthspan_lifespan(np.array([yr]))
        ax.annotate(f"gap = {g[0]:.0f}y",
                     xy=(yr, (ls[0] + hs[0]) / 2),
                     xytext=(yr - 8 if yr == 2024 else yr - 8,
                              (ls[0] + hs[0]) / 2 + 3),
                     fontsize=9,
                     bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))
    ax.set_xlabel("Year")
    ax.set_ylabel("Years")
    ax.set_title("(b) Healthspan ↔ lifespan: gap closing 10 → 3 yr")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")
    ax.set_ylim(60, 100)

    # --- (c) Industry investment ---
    ax = axes[1, 0]
    yrs = np.linspace(2018, 2050, 100)
    inv = np.array([industry_investment_USD_B(y) for y in yrs])
    ax.semilogy(yrs, inv, lw=2.5, color="darkgreen")
    # Recent data points
    for x, y in [(2018, 0.5), (2020, 1.5), (2022, 4.0), (2024, 5.2)]:
        ax.scatter(x, y, s=80, color="black", zorder=5)
    # Annotate 2030, 2040, 2050 ITU predictions
    for x, label in [(2030, "$15B"), (2040, "$50B"), (2050, "$120B")]:
        y = industry_investment_USD_B(x)
        ax.annotate(label, (x, y), xytext=(x - 3, y * 2),
                     fontsize=9,
                     arrowprops=dict(arrowstyle="->", color="darkgreen"))
    ax.set_xlabel("Year")
    ax.set_ylabel("Longevity industry investment [$B/yr]")
    ax.set_title("(c) Longevity investment: $5B → $120B")
    ax.grid(True, alpha=0.3, which="both")
    ax.set_xlim(2018, 2052)

    # --- (d) Regulatory milestones timeline ---
    ax = axes[1, 1]
    yrs_m = [m["year"] for m in MILESTONES]
    labels_m = [m["event"] for m in MILESTONES]
    colors_m = ["green" if m["tier"] == "achieved" else
                "orange" if m["tier"] == "expected" else "blue"
                for m in MILESTONES]
    for i, (y, label, color) in enumerate(zip(yrs_m, labels_m, colors_m)):
        ax.scatter(y, i, s=200, c=color, edgecolor="black", zorder=5)
        ax.annotate(label, (y, i), xytext=(8, 0),
                     textcoords="offset points", fontsize=7,
                     verticalalignment="center")
    ax.set_yticks([])
    ax.set_xlabel("Year")
    ax.set_xlim(2022, 2055)
    ax.set_ylim(-1, len(MILESTONES))
    ax.set_title("(d) Regulatory milestones — ITU prediction")
    ax.grid(True, alpha=0.3, axis="x")
    # Custom legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="green", label="Achieved"),
        Patch(facecolor="orange", label="Expected (TAME 2028)"),
        Patch(facecolor="blue", label="Predicted (ITU)"),
    ]
    ax.legend(handles=legend_elements, loc="upper right", fontsize=8)

    plt.suptitle("Phase 66: Longevity roadmap 2026-2050 — "
                 "ITU prediction of 100-year healthy society",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), "aging_roadmap.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 66] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 66: ITU longevity roadmap 2026-2050")
    print("=" * 60)

    # [1]
    print("\n[1] Average lifespan scenarios:")
    for y in [2024, 2030, 2040, 2050]:
        sq, mid, opt = lifespan_scenarios(np.array([y]))
        print(f"  {y}: Status quo={sq[0]:.1f}, "
              f"ITU mid={mid[0]:.1f}, "
              f"ITU+OSKM={opt[0]:.1f}")

    # [2]
    print("\n[2] Healthspan-lifespan gap:")
    for y in [2024, 2030, 2040, 2050]:
        ls, hs, g = healthspan_lifespan(np.array([y]))
        print(f"  {y}: lifespan={ls[0]:.1f}, "
              f"healthspan={hs[0]:.1f}, gap={g[0]:.1f} yr")

    # [3]
    print("\n[3] Longevity industry investment:")
    for y in [2018, 2022, 2024, 2030, 2040, 2050]:
        inv = industry_investment_USD_B(y)
        print(f"  {y}: ${inv:6.1f}B")
    print(f"\n  Top funded (2024):")
    for c, d in COMPANIES_2024.items():
        print(f"    {c:<22s} : ${d['funding_M_USD']}M ({d['focus']})")

    # [4]
    print("\n[4] Regulatory milestones (ITU prediction):")
    for m in MILESTONES:
        print(f"  {m['year']} ({m['tier']:<10s}): {m['event']}")

    plot_path = make_plot()

    predictions = [
        "TAME trial achieves primary endpoint by 2028 (multi-morbidity reduction)",
        "FDA approves first 'biological aging' related indication by 2030",
        "US average lifespan recovers to 81 years by 2030 (currently 78)",
        "Japan average lifespan reaches 86 years by 2035",
        "First in-human OSKM partial reprogramming trial begins by 2030",
        "5+ senolytics drugs approved by FDA by 2035",
        "Multi-K combination therapy reimbursed by insurance by 2040",
        "Longevity industry investment reaches $15B/yr by 2030",
        "Healthspan-lifespan gap drops below 5 years by 2050",
        "Centenarian population worldwide reaches 4 million by 2050 (vs 0.6M today)",
    ]

    summary = {
        "phase": 66,
        "paper": "ITU and Aging",
        "description": "Longevity roadmap 2026-2050 (Tier 1 #6 final)",
        "lifespan_scenarios": {
            str(y): {
                "status_quo": float(lifespan_scenarios(np.array([y]))[0][0]),
                "ITU_mid": float(lifespan_scenarios(np.array([y]))[1][0]),
                "ITU_optimistic": float(lifespan_scenarios(np.array([y]))[2][0]),
            }
            for y in [2024, 2030, 2040, 2050]
        },
        "healthspan_lifespan_gap": {
            str(y): {
                "lifespan": float(healthspan_lifespan(np.array([y]))[0][0]),
                "healthspan": float(healthspan_lifespan(np.array([y]))[1][0]),
                "gap": float(healthspan_lifespan(np.array([y]))[2][0]),
            }
            for y in [2024, 2030, 2040, 2050]
        },
        "industry_investment_USD_B": {
            str(y): float(industry_investment_USD_B(y))
            for y in [2018, 2022, 2024, 2030, 2040, 2050]
        },
        "key_companies_2024": COMPANIES_2024,
        "regulatory_milestones": MILESTONES,
        "falsifiable_predictions": predictions,
        "paper_complete": True,
        "central_thesis": "Multi-K interventions reach the market over "
                          "2026-2050; lifespan rises 82 -> 95 yr, "
                          "healthspan 72 -> 92 yr, gap shrinks 10 -> 3 yr. "
                          "Centenarian population multiplies 7x globally.",
        "honest_framing": "Pass-1 interpretive paper across 4 phases. "
                          "Reframes Hallmarks of Aging, Gompertz law, "
                          "intervention biology in ITU language. Predictions "
                          "are ITU-informed but overlap with industry/demographic "
                          "consensus. Pass-2 would derive ITU-unique biomarker "
                          "or intervention validated against long-term data.",
        "tier": 1,
        "paper_number": 6,
        "tier_0_concept_doi": "10.5281/zenodo.20109209",
        "tier_1_qc_doi": "10.5281/zenodo.20139391",
        "tier_1_ai_doi": "10.5281/zenodo.20150501",
        "tier_1_crypto_doi": "10.5281/zenodo.20151059",
        "tier_1_semi_doi": "10.5281/zenodo.20174036",
        "tier_1_cancer_doi": "10.5281/zenodo.20174318",
        "medicine_triangle_status": {
            "Cancer (#5)": "completed",
            "Aging (#6)": "completed (THIS PAPER)",
            "Psychiatry (#7)": "planned (Phase 67-70)",
        },
        "next_paper_candidates": [
            "Tier 1 #7: Psychiatry (FEP failures in brain K)",
            "Tier 1 #8: Economics (information markets)",
            "Tier 1 #9: Free will (revisited)",
        ],
        "caveats": [
            "Lifespan projections assume continued multi-K intervention success",
            "Industry investment forecast extrapolates current trajectory",
            "Regulatory milestones depend on TAME outcome (2028)",
            "OSKM safety in humans is unproven",
            "Demographic projections ignore catastrophic risks (pandemic, war, climate)",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase66.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 66] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 66 complete. Tier 1 #6 (Aging) ready for Zenodo.")
    print(f"  - Lifespan 2024 → 2050: 82 → 95 (ITU mid)")
    print(f"  - Healthspan 2024 → 2050: 72 → 92 (gap closes 10 → 3 yr)")
    print(f"  - Industry investment: $5B (2024) → $120B (2050)")
    print(f"  - 10 falsifiable predictions issued")
    print(f"  - Medicine triangle: 2/3 complete (Cancer + Aging)")
    print("=" * 60)


if __name__ == "__main__":
    main()
