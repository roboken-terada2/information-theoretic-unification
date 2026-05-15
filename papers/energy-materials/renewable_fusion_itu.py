#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 80: Renewable energy + nuclear fusion under ITU

LCOE revolution (solar/wind cheapest), NIF Q=1.5 (2022), ITER Q=10 (2035).
21st century energy transition reframed as K_energy source restructuring.

Tests:
  1. LCOE timeline 2010-2030 by technology
  2. Capacity factor vs CO2 emissions
  3. Fusion Q-value history (JET, NIF, SPARC, ITER)
  4. Global generation capacity 2010-2050 (IEA NZE)

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #10 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: LCOE timeline
# =============================================================================
def lcoe_history(year, tech="solar"):
    """LCOE in USD/MWh by year for various technologies."""
    year = np.asarray(year, dtype=float)
    if tech == "solar":
        pts_y = [2010, 2015, 2020, 2024, 2030]
        pts_v = [380,   100,   45,   40,   25]
    elif tech == "wind_onshore":
        pts_y = [2010, 2015, 2020, 2024, 2030]
        pts_v = [125,   80,    50,   38,   30]
    elif tech == "wind_offshore":
        pts_y = [2010, 2015, 2020, 2024, 2030]
        pts_v = [200,   180,   120,  100,  70]
    elif tech == "gas_ccgt":
        pts_y = [2010, 2015, 2020, 2024, 2030]
        pts_v = [80,    70,    55,   60,   65]  # rises with carbon pricing
    elif tech == "coal":
        pts_y = [2010, 2015, 2020, 2024, 2030]
        pts_v = [100,   110,   120,  117,  140]  # rises
    elif tech == "nuclear_new":
        pts_y = [2010, 2015, 2020, 2024, 2030]
        pts_v = [120,   140,   170,  182,  200]  # rising costs
    elif tech == "battery_solar":
        pts_y = [2015, 2020, 2024, 2030]
        pts_v = [220,   120,   68,   45]
    return np.interp(year, pts_y, pts_v)


# =============================================================================
# Test 2: Capacity factor x CO2
# =============================================================================
ENERGY_SOURCES = {
    "Coal":              {"capacity_factor": 60, "co2_gCO2_kWh": 820, "color": "black"},
    "Gas (CCGT)":        {"capacity_factor": 70, "co2_gCO2_kWh": 490, "color": "gray"},
    "Solar PV":          {"capacity_factor": 20, "co2_gCO2_kWh": 41,  "color": "gold"},
    "Wind onshore":      {"capacity_factor": 40, "co2_gCO2_kWh": 12,  "color": "lightblue"},
    "Wind offshore":     {"capacity_factor": 50, "co2_gCO2_kWh": 12,  "color": "blue"},
    "Hydro":             {"capacity_factor": 40, "co2_gCO2_kWh": 24,  "color": "darkblue"},
    "Nuclear fission":   {"capacity_factor": 92, "co2_gCO2_kWh": 12,  "color": "purple"},
    "Fusion (predicted)": {"capacity_factor": 90, "co2_gCO2_kWh": 5,   "color": "red"},
}


# =============================================================================
# Test 3: Fusion Q history
# =============================================================================
FUSION_MILESTONES = [
    {"year": 1991, "device": "JET (D-T)",        "Q": 0.16, "tier": "achieved"},
    {"year": 1997, "device": "JET (D-T)",        "Q": 0.67, "tier": "achieved"},
    {"year": 2022, "device": "NIF (laser)",       "Q": 1.5,  "tier": "ignition"},
    {"year": 2023, "device": "NIF (laser, sustained)", "Q": 1.9, "tier": "ignition"},
    {"year": 2025, "device": "SPARC (predicted)", "Q": 2.0,  "tier": "expected"},
    {"year": 2028, "device": "Helion (target)",   "Q": 5.0,  "tier": "predicted"},
    {"year": 2030, "device": "CFS commercial",   "Q": 8.0,  "tier": "predicted"},
    {"year": 2035, "device": "ITER",              "Q": 10.0, "tier": "predicted"},
    {"year": 2050, "device": "Commercial Fusion", "Q": 30.0, "tier": "predicted"},
]


# =============================================================================
# Test 4: Global capacity 2010-2050
# =============================================================================
def global_capacity_GW(year, tech="solar"):
    """World installed capacity GW."""
    year = np.asarray(year, dtype=float)
    if tech == "solar":
        pts_y = [2010, 2015, 2020, 2024, 2030, 2040, 2050]
        pts_v = [40,    230,   720,  1800, 5500, 11000, 20000]
    elif tech == "wind":
        pts_y = [2010, 2015, 2020, 2024, 2030, 2040, 2050]
        pts_v = [200,   430,   740,  1200, 2800, 5000, 8000]
    elif tech == "nuclear":
        pts_y = [2010, 2015, 2020, 2024, 2030, 2040, 2050]
        pts_v = [370,   380,   395,  415,  470,  600,  800]
    elif tech == "fossil":
        pts_y = [2010, 2015, 2020, 2024, 2030, 2040, 2050]
        pts_v = [4000,  4400, 4600, 4500, 3800, 2200, 800]
    return np.interp(year, pts_y, pts_v)


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) LCOE timeline ---
    ax = axes[0, 0]
    years = np.linspace(2010, 2030, 100)
    techs = [
        ("solar", "gold", "Solar PV"),
        ("wind_onshore", "lightblue", "Onshore wind"),
        ("wind_offshore", "blue", "Offshore wind"),
        ("gas_ccgt", "gray", "Gas (CCGT)"),
        ("coal", "black", "Coal"),
        ("nuclear_new", "purple", "Nuclear (new)"),
    ]
    for tech, color, label in techs:
        lcoe = lcoe_history(years, tech)
        ax.plot(years, lcoe, lw=2, color=color, label=label)
    # Battery + solar
    yrs_bs = np.linspace(2015, 2030, 100)
    bs = lcoe_history(yrs_bs, "battery_solar")
    ax.plot(yrs_bs, bs, lw=2, color="orange", ls="--",
            label="Battery + solar (firm)")
    # 2024 reference
    ax.axvline(2024, ls=":", color="black", alpha=0.5)
    ax.text(2024.2, 280, "2024:\nsolar+wind\ncheapest",
            fontsize=9, color="darkgreen",
            bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))
    ax.set_xlabel("Year")
    ax.set_ylabel("LCOE [USD/MWh]")
    ax.set_title("(a) LCOE revolution 2010-2030")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=7)
    ax.set_xlim(2010, 2030)
    ax.set_ylim(0, 400)

    # --- (b) Capacity x CO2 ---
    ax = axes[0, 1]
    for name, d in ENERGY_SOURCES.items():
        ax.scatter(d["capacity_factor"], d["co2_gCO2_kWh"],
                    s=250, c=d["color"], edgecolor="black",
                    linewidths=1, alpha=0.8)
        ax.annotate(name, (d["capacity_factor"], d["co2_gCO2_kWh"]),
                     xytext=(8, 4), textcoords="offset points",
                     fontsize=8)
    # Sweet spot annotation
    ax.text(0.95, 0.95, "★ Sweet spot:\nhigh capacity +\nlow CO2",
            transform=ax.transAxes, fontsize=9, ha="right", va="top",
            bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.8))
    ax.set_xlabel("Capacity factor [%]")
    ax.set_ylabel("CO₂ emissions [g/kWh, log]")
    ax.set_yscale("log")
    ax.set_title("(b) Capacity × CO₂ — nuclear+fusion sweet spot")
    ax.grid(True, alpha=0.3, which="both")
    ax.set_xlim(0, 100)
    ax.set_ylim(1, 1500)

    # --- (c) Fusion Q history ---
    ax = axes[1, 0]
    years = [m["year"] for m in FUSION_MILESTONES]
    Qs = [m["Q"] for m in FUSION_MILESTONES]
    tier_colors = {"achieved": "green", "ignition": "red",
                    "expected": "orange", "predicted": "blue"}
    for m in FUSION_MILESTONES:
        ax.scatter(m["year"], m["Q"], s=150,
                    c=tier_colors[m["tier"]], edgecolor="black",
                    zorder=5)
        ax.annotate(m["device"], (m["year"], m["Q"]),
                     xytext=(5, 8), textcoords="offset points",
                     fontsize=7)
    # Line connecting milestones
    ax.plot(years, Qs, lw=1.5, color="gray", ls="--", alpha=0.5)
    ax.axhline(1.0, ls="--", color="red", alpha=0.5, label="Ignition (Q=1)")
    ax.axhline(10.0, ls=":", color="purple", alpha=0.5,
               label="Commercial threshold (Q=10)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Fusion Q-value")
    ax.set_yscale("log")
    ax.set_title("(c) Fusion Q-value milestones — 30 year journey")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(1985, 2055)

    # --- (d) Global capacity ---
    ax = axes[1, 1]
    years = np.linspace(2010, 2050, 200)
    for tech, color, label in [("solar", "gold", "Solar"),
                                  ("wind", "blue", "Wind"),
                                  ("nuclear", "purple", "Nuclear"),
                                  ("fossil", "black", "Fossil")]:
        cap = global_capacity_GW(years, tech)
        ax.plot(years, cap, lw=2.5, color=color, label=label)
    ax.axvline(2024, ls=":", color="black", alpha=0.5)
    ax.text(2024.5, 15000, "2024", fontsize=8)
    ax.set_xlabel("Year")
    ax.set_ylabel("Installed capacity [GW, log]")
    ax.set_yscale("log")
    ax.set_title("(d) Global capacity 2010-2050 (IEA NZE)")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(2010, 2050)
    ax.set_ylim(50, 30000)

    plt.suptitle("Phase 80: Renewable + nuclear + fusion — "
                 "K_energy source restructuring",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "renewable_fusion_itu.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 80] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 80: Renewable + nuclear + fusion under ITU")
    print("=" * 60)

    # [1]
    print("\n[1] LCOE 2010 vs 2024 (USD/MWh):")
    for tech in ["solar", "wind_onshore", "wind_offshore",
                 "gas_ccgt", "coal", "nuclear_new"]:
        v_2010 = lcoe_history(np.array([2010]), tech)[0]
        v_2024 = lcoe_history(np.array([2024]), tech)[0]
        delta = (v_2024 - v_2010) / v_2010 * 100
        print(f"  {tech:<18s}: ${v_2010:.0f}/MWh -> ${v_2024:.0f}/MWh "
              f"({delta:+.0f}%)")

    # [2]
    print("\n[2] Capacity × CO₂:")
    for name, d in ENERGY_SOURCES.items():
        score = d["capacity_factor"] / d["co2_gCO2_kWh"]
        print(f"  {name:<22s}: CF={d['capacity_factor']:2d}%, "
              f"CO2={d['co2_gCO2_kWh']:4d} g/kWh, score={score:.1f}")

    # [3]
    print("\n[3] Fusion Q-value milestones:")
    for m in FUSION_MILESTONES:
        print(f"  {m['year']} ({m['tier']:<10s}): {m['device']:<32s} "
              f"Q={m['Q']:.2f}")

    # [4]
    print("\n[4] Global capacity 2024 vs 2050 (GW):")
    for tech in ["solar", "wind", "nuclear", "fossil"]:
        v_2024 = global_capacity_GW(np.array([2024]), tech)[0]
        v_2050 = global_capacity_GW(np.array([2050]), tech)[0]
        ratio = v_2050 / v_2024
        print(f"  {tech:<10s}: {v_2024:5.0f} GW -> {v_2050:5.0f} GW "
              f"({ratio:.1f}x)")

    plot_path = make_plot()

    summary = {
        "phase": 80,
        "paper": "ITU and Energy / Materials",
        "description": "Renewable + nuclear + fusion ITU analysis",
        "LCOE_2024_USD_MWh": {
            tech: float(lcoe_history(np.array([2024]), tech)[0])
            for tech in ["solar", "wind_onshore", "wind_offshore",
                          "gas_ccgt", "coal", "nuclear_new", "battery_solar"]
        },
        "energy_sources": ENERGY_SOURCES,
        "fusion_milestones": FUSION_MILESTONES,
        "fusion_Q_2022_NIF": 1.5,
        "fusion_Q_target_ITER_2035": 10.0,
        "global_capacity_GW": {
            "2010": {tech: float(global_capacity_GW(np.array([2010]), tech)[0])
                     for tech in ["solar", "wind", "nuclear", "fossil"]},
            "2024": {tech: float(global_capacity_GW(np.array([2024]), tech)[0])
                     for tech in ["solar", "wind", "nuclear", "fossil"]},
            "2050": {tech: float(global_capacity_GW(np.array([2050]), tech)[0])
                     for tech in ["solar", "wind", "nuclear", "fossil"]},
        },
        "solar_growth_2010_to_2024": float(
            global_capacity_GW(np.array([2024]), "solar")[0] /
            global_capacity_GW(np.array([2010]), "solar")[0]
        ),
        "central_thesis": "2024 is a historic turning point: solar+wind "
                          "become cheapest energy globally ($36-50/MWh). "
                          "NIF Ignition (Dec 2022, Q=1.5) opens the fusion "
                          "era. ITER 2035 Q=10 targets commercial fusion "
                          "by 2050. CO2 sweet spot: nuclear (12) and "
                          "fusion (~5 g/kWh) with high capacity factors.",
        "honest_framing": "Pass-1 interpretive paper. Reframes Lazard "
                          "LCOE, IEA NZE, NIF ignition, ITER milestones "
                          "in ITU language. No novel renewable technology.",
        "tier": 1,
        "paper_number": 10,
        "next_phases": [
            "Phase 81: New materials (perovskites, MOFs, quantum materials)",
            "Phase 82: Energy roadmap 2026-2050 + 10 predictions",
        ],
        "caveats": [
            "LCOE values from multiple sources differ (Lazard, BNEF, IEA)",
            "Fusion Q-value definitions vary (input plasma vs wall plug)",
            "Capacity factors vary by region (e.g., Saharan solar 28%)",
            "CO2 lifecycle differs by methodology (cradle-to-grave)",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase80.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 80] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 80 complete.")
    print(f"  - 2024 turning point: solar $40/MWh, wind $38/MWh (cheapest ever)")
    print(f"  - NIF 2022 ignition: Q=1.5 → 1.9 sustained")
    print(f"  - ITER 2035 target: Q=10 (commercial threshold)")
    print(f"  - Solar 2010→2024: 45x capacity growth")
    print("=" * 60)


if __name__ == "__main__":
    main()
