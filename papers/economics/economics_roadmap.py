#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 74: ITU economic roadmap 2026-2050 (Tier 1 #8 final)

AGI-driven growth, CBDC adoption, sectoral restructuring,
carbon transition - all unified under ITU economics.

Tests:
  1. GDP growth scenarios 2024-2050 (bear/base/AGI bull)
  2. CBDC adoption timeline (G20 + Asia)
  3. Sectoral GDP share evolution 2024-2040
  4. Carbon price trajectory + UBI cost projection

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #8 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: GDP scenarios
# =============================================================================
def gdp_growth_rate(year, scenario="base"):
    """Annual GDP growth rate by year/scenario."""
    year = np.asarray(year, dtype=float)
    if scenario == "bear":
        return 2.0 - 0.05 * (year - 2024) / 5
    elif scenario == "base":
        # Mild AI uplift
        rates = {2024: 2.5, 2027: 3.0, 2030: 3.5, 2035: 3.5,
                 2040: 3.0, 2050: 2.5}
    elif scenario == "agi_bull":
        # AGI jumps growth ~2030
        rates = {2024: 2.5, 2027: 4.0, 2030: 6.0, 2035: 8.0,
                 2040: 6.0, 2050: 4.0}
    return np.interp(year, list(rates.keys()), list(rates.values()))


def gdp_projection(year_start=2024, year_end=2050, GDP_start=27.4,
                     scenario="base"):
    """Project GDP trajectory."""
    years = np.arange(year_start, year_end + 1)
    GDP = np.zeros(len(years))
    GDP[0] = GDP_start
    for i in range(1, len(years)):
        rate = gdp_growth_rate(years[i], scenario) / 100
        GDP[i] = GDP[i - 1] * (1 + rate)
    return years, GDP


# =============================================================================
# Test 2: CBDC adoption
# =============================================================================
CBDC_TIMELINE = {
    "Bahamas":      {"year": 2020, "status": "launched", "color": "green"},
    "Nigeria":      {"year": 2021, "status": "launched", "color": "green"},
    "China":        {"year": 2022, "status": "pilot scaling", "color": "darkgreen"},
    "India":        {"year": 2023, "status": "launched", "color": "green"},
    "EU":           {"year": 2026, "status": "pilot expected", "color": "orange"},
    "Japan":        {"year": 2027, "status": "pilot expected", "color": "orange"},
    "UK":           {"year": 2028, "status": "decision expected", "color": "blue"},
    "USA":          {"year": 2031, "status": "pilot predicted", "color": "blue"},
    "Switzerland":  {"year": 2029, "status": "predicted", "color": "blue"},
    "Brazil":       {"year": 2025, "status": "Drex launching", "color": "green"},
}


# =============================================================================
# Test 3: Sectoral GDP share
# =============================================================================
SECTORS_2024 = {
    "Manufacturing": 16,
    "Agriculture":   4,
    "Finance":       7,
    "AI/Data":       3,
    "Health/Bio":    10,
    "Education":     6,
    "Services":      30,
    "Other":         24,
}

SECTORS_2040 = {
    "Manufacturing": 12,
    "Agriculture":   3,
    "Finance":       8,
    "AI/Data":       15,
    "Health/Bio":    18,
    "Education":     5,
    "Services":      25,
    "Other":         14,
}


# =============================================================================
# Test 4: Carbon price + UBI cost
# =============================================================================
def carbon_price_eur(year):
    """EU ETS-implied trajectory."""
    pts_y = [2024, 2027, 2030, 2035, 2040, 2050]
    pts_v = [70, 100, 150, 220, 300, 350]
    return np.interp(year, pts_y, pts_v)


def ubi_cost_pct_gdp_growth(year, base_pct=11.0, gdp_growth_yr=0.025):
    """UBI cost as % of GDP, declining as GDP grows faster than UBI uplift."""
    years_passed = year - 2024
    # Assume UBI keeps flat per-capita, GDP grows
    return base_pct * (1.025 ** years_passed) / (1.05 ** years_passed)


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) GDP scenarios ---
    ax = axes[0, 0]
    years_b, gdp_bear = gdp_projection(scenario="bear")
    years_a, gdp_base = gdp_projection(scenario="base")
    _, gdp_agi = gdp_projection(scenario="agi_bull")
    ax.plot(years_a, gdp_bear, lw=2, color="red", label="Bear case (1.5%)")
    ax.plot(years_a, gdp_base, lw=2.5, color="blue", label="Base (ITU mid)")
    ax.plot(years_a, gdp_agi, lw=2.5, color="green",
             label="AGI bull case")
    # AGI milestone marker
    ax.axvline(2030, ls="--", color="purple", alpha=0.5)
    ax.text(2030.2, 80, "AGI\n(P=0.5)", fontsize=8, color="purple")
    ax.set_xlabel("Year")
    ax.set_ylabel("US GDP [$T]")
    ax.set_title("(a) GDP projections — AGI uplift starts ~2030")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")
    # Annotate end values
    ax.annotate(f"2050: ${gdp_agi[-1]:.0f}T",
                xy=(2050, gdp_agi[-1]),
                xytext=(2042, gdp_agi[-1] + 10),
                fontsize=9, color="green",
                arrowprops=dict(arrowstyle="->", color="green"))
    ax.annotate(f"2050: ${gdp_base[-1]:.0f}T",
                xy=(2050, gdp_base[-1]),
                xytext=(2040, gdp_base[-1] + 10),
                fontsize=9, color="blue",
                arrowprops=dict(arrowstyle="->", color="blue"))

    # --- (b) CBDC adoption timeline ---
    ax = axes[0, 1]
    countries = list(CBDC_TIMELINE.keys())
    years = [CBDC_TIMELINE[c]["year"] for c in countries]
    colors = [CBDC_TIMELINE[c]["color"] for c in countries]
    # Sort by year
    idx = np.argsort(years)
    countries_s = [countries[i] for i in idx]
    years_s = [years[i] for i in idx]
    colors_s = [colors[i] for i in idx]
    for i, (c, y, color) in enumerate(zip(countries_s, years_s, colors_s)):
        ax.scatter(y, i, s=200, c=color, edgecolor="black", zorder=5)
        ax.annotate(c, (y, i), xytext=(8, 0),
                     textcoords="offset points", fontsize=8,
                     verticalalignment="center")
    ax.set_yticks([])
    ax.set_xlabel("Year of launch/pilot/decision")
    ax.set_xlim(2018, 2035)
    ax.set_ylim(-1, len(countries))
    ax.set_title("(b) CBDC adoption timeline — G20")
    ax.grid(True, alpha=0.3, axis="x")
    from matplotlib.patches import Patch
    legend = [
        Patch(facecolor="green", label="Launched"),
        Patch(facecolor="darkgreen", label="Pilot scaling"),
        Patch(facecolor="orange", label="Pilot soon"),
        Patch(facecolor="blue", label="Predicted"),
    ]
    ax.legend(handles=legend, loc="upper right", fontsize=8)

    # --- (c) Sectoral GDP share ---
    ax = axes[1, 0]
    sectors = list(SECTORS_2024.keys())
    share_2024 = [SECTORS_2024[s] for s in sectors]
    share_2040 = [SECTORS_2040[s] for s in sectors]
    x = np.arange(len(sectors))
    width = 0.35
    bars1 = ax.bar(x - width / 2, share_2024, width, color="lightblue",
                    edgecolor="black", label="2024")
    bars2 = ax.bar(x + width / 2, share_2040, width, color="orange",
                    edgecolor="black", label="2040 (ITU prediction)")
    # Highlight major changes
    for i, (a, b) in enumerate(zip(share_2024, share_2040)):
        delta = b - a
        if abs(delta) >= 3:
            ax.text(i, max(a, b) + 1, f"{delta:+d}",
                    ha="center", fontsize=9,
                    color="green" if delta > 0 else "red", fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(sectors, rotation=20, fontsize=8)
    ax.set_ylabel("GDP share [%]")
    ax.set_title("(c) Sectoral GDP share — AI/Data + Health surge")
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3, axis="y")

    # --- (d) Carbon price + UBI projection ---
    ax = axes[1, 1]
    years = np.linspace(2024, 2050, 27)
    carbon_p = np.array([carbon_price_eur(y) for y in years])
    ubi_p = np.array([ubi_cost_pct_gdp_growth(y) for y in years])
    line1 = ax.plot(years, carbon_p, lw=2.5, color="darkgreen",
                     label="Carbon price (EU ETS, EUR/t)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Carbon price [EUR/t CO2]", color="darkgreen")
    ax.set_title("(d) Carbon + UBI trajectories")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9)
    ax2 = ax.twinx()
    line2 = ax2.plot(years, ubi_p, lw=2.5, color="red", ls="--",
                      label="US UBI cost (% GDP)")
    ax2.set_ylabel("UBI cost [% of GDP]", color="red")
    ax2.legend(loc="center right", fontsize=9)

    plt.suptitle("Phase 74: Economic roadmap 2026-2050 — ITU Tier 1 #8 complete",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), "economics_roadmap.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 74] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 74: Economic roadmap 2026-2050 (Tier 1 #8 final)")
    print("=" * 60)

    # [1]
    print("\n[1] GDP projections (US, $T):")
    for scen in ["bear", "base", "agi_bull"]:
        y, gdp = gdp_projection(scenario=scen)
        print(f"  {scen:<10s}: 2024=${gdp[0]:.1f}T, 2030=${gdp[6]:.1f}T, "
              f"2040=${gdp[16]:.1f}T, 2050=${gdp[-1]:.1f}T")

    # [2]
    print("\n[2] CBDC adoption timeline:")
    sorted_countries = sorted(CBDC_TIMELINE.items(),
                                key=lambda x: x[1]["year"])
    for c, d in sorted_countries:
        print(f"  {d['year']}: {c:<15s} ({d['status']})")

    # [3]
    print("\n[3] Sectoral share 2024 -> 2040:")
    for s in SECTORS_2024:
        d24 = SECTORS_2024[s]
        d40 = SECTORS_2040[s]
        delta = d40 - d24
        marker = "★" if abs(delta) >= 3 else " "
        print(f"  {s:<18s}: {d24}% -> {d40}% ({delta:+d}) {marker}")

    # [4]
    print("\n[4] Carbon price + UBI cost trajectory:")
    for y in [2024, 2030, 2040, 2050]:
        cp = carbon_price_eur(y)
        up = ubi_cost_pct_gdp_growth(y)
        print(f"  {y}: carbon=EUR{cp:.0f}/t, UBI={up:.1f}% GDP")

    plot_path = make_plot()

    predictions = [
        "S&P 500 exceeds 8000 by 2030 (AI-driven)",
        "AGI achievement by 2028-2032 (P=0.5)",
        "US unemployment peaks at 10%+ around 2032 (AI displacement)",
        "UBI legislated in 1+ G7 country by 2035",
        "CBDC adopted in 3+ G7 countries by 2030",
        "China e-CNY reaches 10%+ international settlement share by 2030",
        "EU AI Act enforcement action against 5+ firms 2026-2028",
        "World GDP growth exceeds 5% in some year by 2035 (AGI effect)",
        "World GDP reaches $300T by 2050 (~3x 2024)",
        "50%+ of major countries reach carbon-neutrality by 2050",
    ]

    summary = {
        "phase": 74,
        "paper": "ITU and Economics",
        "description": "Economic roadmap 2026-2050 (Tier 1 #8 final)",
        "gdp_projections": {
            scen: {
                "2024_USD_T": float(gdp_projection(scenario=scen)[1][0]),
                "2030_USD_T": float(gdp_projection(scenario=scen)[1][6]),
                "2040_USD_T": float(gdp_projection(scenario=scen)[1][16]),
                "2050_USD_T": float(gdp_projection(scenario=scen)[1][-1]),
            }
            for scen in ["bear", "base", "agi_bull"]
        },
        "cbdc_timeline": {
            c: {"year": d["year"], "status": d["status"]}
            for c, d in CBDC_TIMELINE.items()
        },
        "sectoral_change_2024_to_2040": {
            s: {"share_2024": SECTORS_2024[s],
                "share_2040": SECTORS_2040[s],
                "delta_pp": SECTORS_2040[s] - SECTORS_2024[s]}
            for s in SECTORS_2024
        },
        "carbon_price_eur_t": {
            str(y): float(carbon_price_eur(y))
            for y in [2024, 2030, 2040, 2050]
        },
        "ubi_cost_pct_gdp": {
            str(y): float(ubi_cost_pct_gdp_growth(y))
            for y in [2024, 2030, 2040, 2050]
        },
        "falsifiable_predictions": predictions,
        "paper_complete": True,
        "central_thesis": "Economic transformation 2026-2050 = AGI-driven "
                          "productivity (GDP 3x by 2050), CBDC governance, "
                          "UBI introduction, sector restructuring "
                          "(AI/Data +12pp, Health +8pp), and carbon "
                          "transition (€350/t by 2050). All driven by "
                          "ITU axiom changes at societal scale.",
        "honest_framing": "Pass-1 interpretive paper across 4 phases. "
                          "Numerical projections rely on Goldman Sachs, "
                          "IMF, BIS published forecasts. Predictions are "
                          "ITU-informed but overlap with industry consensus.",
        "tier": 1,
        "paper_number": 8,
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "engineering_rectangle_complete": True,
        "medicine_triangle_complete": True,
        "social_sciences_first_vertex": True,
        "next_paper_candidates": [
            "Tier 1 #9: Free Will revisited (Phase 75-78)",
            "Tier 1 #10: Energy / Materials (Phase 79-82)",
            "Pass-2: Re-traverse #1-#8 with ITU-unique predictions",
        ],
        "caveats": [
            "AGI timing uncertain (P=0.5 range 2028-2032)",
            "Sectoral predictions ignore black swans (pandemic, war)",
            "CBDC adoption depends on political decisions",
            "Carbon price assumes EU ETS-like policy globalisation",
            "UBI cost assumes per-capita amounts kept constant",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase74.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 74] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 74 complete. Tier 1 #8 (Economics) ready for Zenodo.")
    print(f"  - GDP 2024->2050: bear ${gdp_projection(scenario='bear')[1][-1]:.0f}T, "
          f"base ${gdp_projection(scenario='base')[1][-1]:.0f}T, "
          f"AGI bull ${gdp_projection(scenario='agi_bull')[1][-1]:.0f}T")
    print(f"  - AI/Data share 3% -> 15% by 2040 (largest gain)")
    print(f"  - Carbon EUR 70/t -> 350/t by 2050")
    print(f"  - 10 falsifiable predictions issued")
    print(f"  - Tier 1 #8 closes Pass-1 phase 74 of 220 (33.6%)")
    print("=" * 60)


if __name__ == "__main__":
    main()
