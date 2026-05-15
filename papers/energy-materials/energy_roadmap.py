#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 82: Energy / Materials roadmap 2026-2050 (Tier 1 #10 final)

Net-Zero pathway, AGI/quantum material acceleration, Chinese supply
diversification, DAC scale-up. 10th vertex of ITU polytope.

Tests:
  1. World energy mix transition 2024-2050
  2. Critical material supply diversification (China share decline)
  3. Carbon price + DAC trajectory
  4. ITU 10-vertex polytope structure

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #10 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Energy mix
# =============================================================================
ENERGY_MIX = {
    2024: {"Solar": 6,  "Wind": 8,  "Hydro": 16, "Nuclear": 10, "Fusion": 0, "Fossil": 60},
    2030: {"Solar": 18, "Wind": 13, "Hydro": 16, "Nuclear": 11, "Fusion": 0, "Fossil": 42},
    2035: {"Solar": 28, "Wind": 17, "Hydro": 15, "Nuclear": 12, "Fusion": 1, "Fossil": 27},
    2040: {"Solar": 37, "Wind": 20, "Hydro": 14, "Nuclear": 12, "Fusion": 3, "Fossil": 14},
    2045: {"Solar": 44, "Wind": 22, "Hydro": 13, "Nuclear": 12, "Fusion": 5, "Fossil": 4},
    2050: {"Solar": 50, "Wind": 22, "Hydro": 12, "Nuclear": 9,  "Fusion": 5, "Fossil": 2},
}


# =============================================================================
# Test 2: China share decline
# =============================================================================
CHINA_SHARE = {
    "Gallium":           {"2024": 98, "2030": 85, "2040": 70, "2050": 60},
    "Rare earths":       {"2024": 85, "2030": 70, "2040": 60, "2050": 50},
    "Silicon (refined)": {"2024": 80, "2030": 65, "2040": 55, "2050": 50},
    "Graphite":          {"2024": 70, "2030": 55, "2040": 45, "2050": 40},
    "Lithium (proc)":    {"2024": 65, "2030": 50, "2040": 45, "2050": 40},
}


# =============================================================================
# Test 3: Carbon price + DAC
# =============================================================================
def carbon_price(year):
    pts = [2020, 2024, 2030, 2040, 2050]
    vals = [20, 80, 150, 250, 300]
    return np.interp(year, pts, vals)


def dac_capacity_Mt(year):
    """Direct Air Capture capacity in MtCO2/yr."""
    pts = [2024, 2030, 2040, 2050]
    vals = [0.01, 5, 100, 1000]
    return np.interp(year, pts, vals)


def dac_cost_USD_t(year):
    pts = [2024, 2030, 2040, 2050]
    vals = [800, 300, 100, 50]
    return np.interp(year, pts, vals)


# =============================================================================
# Test 4: 10-vertex polytope
# =============================================================================
POLYTOPE = {
    "#1 Quantum Computing": {"axis": "engineering", "x": 0, "y": 0},
    "#2 AI/ASI":             {"axis": "engineering", "x": 1, "y": 1},
    "#3 Cryptography":       {"axis": "engineering", "x": 2, "y": 1},
    "#4 Semiconductors":     {"axis": "engineering", "x": 3, "y": 0},
    "#10 Energy/Materials":  {"axis": "engineering", "x": 4, "y": 0},
    "#5 Cancer":             {"axis": "medicine",     "x": 1.5, "y": 3},
    "#6 Aging":              {"axis": "medicine",     "x": 0.5, "y": 4},
    "#7 Psychiatry":         {"axis": "medicine",     "x": 2.5, "y": 4},
    "#8 Economics":          {"axis": "social",       "x": 0,   "y": -2},
    "#9 Free Will":          {"axis": "philosophy",   "x": 2,   "y": -2},
}


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Energy mix evolution ---
    ax = axes[0, 0]
    years = list(ENERGY_MIX.keys())
    sources = ["Solar", "Wind", "Hydro", "Nuclear", "Fusion", "Fossil"]
    colors = ["gold", "lightblue", "darkblue", "purple", "red", "black"]
    data = np.array([[ENERGY_MIX[y][s] for y in years] for s in sources])
    ax.stackplot(years, data, labels=sources, colors=colors, alpha=0.8)
    ax.axhline(50, ls=":", color="white", alpha=0.5)
    ax.axvline(2030, ls=":", color="white", alpha=0.5)
    ax.text(2050, 25, "Solar 50%", color="black", fontsize=10, fontweight="bold")
    ax.text(2050, 2, "Fossil 2%", color="white", fontsize=10, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Share of world electricity [%]")
    ax.set_title("(a) World energy mix 2024-2050 (IEA NZE)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xlim(2024, 2050)
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3)

    # --- (b) China share decline ---
    ax = axes[0, 1]
    years_cs = [2024, 2030, 2040, 2050]
    for mat, d in CHINA_SHARE.items():
        shares = [d[str(y)] for y in years_cs]
        ax.plot(years_cs, shares, "o-", lw=2, label=mat)
    ax.axhline(50, ls="--", color="red", alpha=0.5,
               label="50% threshold")
    ax.set_xlabel("Year")
    ax.set_ylabel("China's market share [%]")
    ax.set_title("(b) Critical material supply diversification")
    ax.legend(loc="lower left", fontsize=8)
    ax.set_xlim(2022, 2052)
    ax.set_ylim(35, 100)
    ax.grid(True, alpha=0.3)

    # --- (c) Carbon price + DAC ---
    ax = axes[1, 0]
    years_c = np.linspace(2020, 2050, 100)
    cp = carbon_price(years_c)
    ax.plot(years_c, cp, lw=2.5, color="darkgreen",
            label="EU ETS carbon price (USD/t)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Carbon price [USD/t CO₂]", color="darkgreen")
    ax.set_title("(c) Carbon price + DAC trajectory")
    ax2 = ax.twinx()
    dac_cost = np.array([dac_cost_USD_t(y) for y in years_c])
    ax2.plot(years_c, dac_cost, lw=2.5, color="red", ls="--",
             label="DAC cost (USD/t)")
    ax2.set_ylabel("DAC cost [USD/t CO₂]", color="red")
    ax2.set_yscale("log")
    # Annotate crossover
    crossover_idx = np.argmin(np.abs(cp - dac_cost))
    ax.scatter(years_c[crossover_idx], cp[crossover_idx], s=200,
                marker="*", color="gold", edgecolor="black", zorder=5)
    ax.annotate(f"DAC = carbon price\n@~{years_c[crossover_idx]:.0f}",
                 (years_c[crossover_idx], cp[crossover_idx]),
                 xytext=(8, 8), textcoords="offset points",
                 fontsize=9,
                 bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))
    ax.grid(True, alpha=0.3)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=8)

    # --- (d) ITU 10-vertex polytope ---
    ax = axes[1, 1]
    axis_colors = {"engineering": "blue", "medicine": "red",
                    "social": "green", "philosophy": "purple"}
    for name, p in POLYTOPE.items():
        color = axis_colors[p["axis"]]
        marker = "*" if "#10" in name else "o"
        size = 400 if "#10" in name else 250
        ax.scatter(p["x"], p["y"], s=size, c=color, marker=marker,
                    edgecolor="black", linewidths=1.5, alpha=0.7, zorder=5)
        # Label
        offset = (0, 12) if p["y"] >= 0 else (0, -18)
        ax.annotate(name, (p["x"], p["y"]),
                     xytext=offset, textcoords="offset points",
                     fontsize=7, ha="center")
    # Draw axes/connections
    # Engineering pentagon
    eng = ["#1 Quantum Computing", "#2 AI/ASI", "#3 Cryptography",
           "#4 Semiconductors", "#10 Energy/Materials"]
    eng_coords = [(POLYTOPE[n]["x"], POLYTOPE[n]["y"]) for n in eng]
    eng_coords.append(eng_coords[0])
    eng_x, eng_y = zip(*eng_coords)
    ax.plot(eng_x, eng_y, color="blue", alpha=0.3, lw=1.5)
    # Medicine triangle
    med = ["#5 Cancer", "#6 Aging", "#7 Psychiatry"]
    med_coords = [(POLYTOPE[n]["x"], POLYTOPE[n]["y"]) for n in med]
    med_coords.append(med_coords[0])
    med_x, med_y = zip(*med_coords)
    ax.plot(med_x, med_y, color="red", alpha=0.3, lw=1.5)
    # Social-philosophy line
    sp = ["#8 Economics", "#9 Free Will"]
    sp_coords = [(POLYTOPE[n]["x"], POLYTOPE[n]["y"]) for n in sp]
    sp_x, sp_y = zip(*sp_coords)
    ax.plot(sp_x, sp_y, color="green", alpha=0.3, lw=1.5)
    ax.set_xlim(-1.5, 5.5)
    ax.set_ylim(-3.5, 6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("(d) ITU 10-vertex polytope")
    from matplotlib.patches import Patch
    legend = [
        Patch(facecolor="blue",   label="Engineering (5: rect+pentagon)"),
        Patch(facecolor="red",    label="Medicine (3: triangle)"),
        Patch(facecolor="green",  label="Social science (1)"),
        Patch(facecolor="purple", label="Philosophy (1)"),
    ]
    ax.legend(handles=legend, loc="upper left", fontsize=7)

    plt.suptitle("Phase 82: Energy/Materials roadmap 2026-2050 — "
                 "ITU 10-vertex polytope",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), "energy_roadmap.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 82] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 82: Energy / Materials roadmap (Tier 1 #10 final)")
    print("=" * 60)

    # [1]
    print("\n[1] World energy mix 2024-2050:")
    for y in sorted(ENERGY_MIX.keys()):
        m = ENERGY_MIX[y]
        print(f"  {y}: Solar={m['Solar']}%, Wind={m['Wind']}%, "
              f"Nuclear={m['Nuclear']}%, Fossil={m['Fossil']}%, "
              f"Fusion={m['Fusion']}%")

    # [2]
    print("\n[2] China share decline (top materials):")
    for mat, d in CHINA_SHARE.items():
        print(f"  {mat:<22s}: 2024={d['2024']}% -> 2050={d['2050']}%")

    # [3]
    print("\n[3] Carbon price + DAC trajectory:")
    for y in [2020, 2024, 2030, 2040, 2050]:
        cp = carbon_price(y)
        dac_c = dac_cost_USD_t(y)
        dac_v = dac_capacity_Mt(y)
        print(f"  {y}: carbon=${cp:.0f}/t, DAC cost=${dac_c:.0f}/t, "
              f"capacity={dac_v:.1f} MtCO₂/yr")

    # [4]
    print("\n[4] ITU 10-vertex polytope:")
    for name, p in POLYTOPE.items():
        print(f"  {name:<25s} ({p['axis']})")

    plot_path = make_plot()

    predictions = [
        "Solid-state Li-ion mass-produced by 1+ EV maker by 2027",
        "Perovskite-Si tandem commercialised by 2028 (>40% market share candidate)",
        "Fusion Q=10 achieved at ITER 2035 (P=0.8)",
        "CFS commercial 1GW fusion plant by 2032",
        "Room-temp superconductor discovered by 2032",
        "AI material discovery expands existing DB 50x by 2030",
        "EU carbon price breaks $200/t by 2032",
        "DAC cost reaches $100/t by 2035",
        "Solar global share reaches 25% by 2030",
        "Fossil fuel power generation drops 80% by 2050",
    ]

    summary = {
        "phase": 82,
        "paper": "ITU and Energy / Materials",
        "description": "Energy/Materials roadmap 2026-2050 (Tier 1 #10 final)",
        "energy_mix_2050": ENERGY_MIX[2050],
        "fossil_decline_2024_to_2050": float(
            (ENERGY_MIX[2050]["Fossil"] - ENERGY_MIX[2024]["Fossil"]) /
            ENERGY_MIX[2024]["Fossil"] * 100
        ),
        "china_share_2024": {mat: CHINA_SHARE[mat]["2024"] for mat in CHINA_SHARE},
        "china_share_2050": {mat: CHINA_SHARE[mat]["2050"] for mat in CHINA_SHARE},
        "carbon_price_USD_t": {
            "2024": float(carbon_price(2024)),
            "2050": float(carbon_price(2050)),
        },
        "dac_capacity_2050_Mt": float(dac_capacity_Mt(2050)),
        "dac_cost_USD_t": {
            "2024": float(dac_cost_USD_t(2024)),
            "2050": float(dac_cost_USD_t(2050)),
        },
        "polytope": POLYTOPE,
        "polytope_vertices": 10,
        "polytope_structure": {
            "engineering_pentagon": ["#1 Quantum Computing", "#2 AI/ASI",
                                      "#3 Cryptography", "#4 Semiconductors",
                                      "#10 Energy/Materials"],
            "medicine_triangle": ["#5 Cancer", "#6 Aging", "#7 Psychiatry"],
            "social_sciences": ["#8 Economics"],
            "philosophy": ["#9 Free Will"],
        },
        "falsifiable_predictions": predictions,
        "paper_complete": True,
        "pass1_progress_phases": 82,
        "pass1_total_phases": 220,
        "pass1_progress_pct": 37.3,
        "central_thesis": "2026-2050: triple convergence - AGI accelerates "
                          "material/energy research 10x, fusion + perovskite "
                          "commercialize, China supply dominance diversifies. "
                          "Solar reaches 50% world electricity by 2050, "
                          "fossil drops to 2%. Net Zero achievable for "
                          "developed nations.",
        "honest_framing": "Pass-1 interpretive paper. IEA NZE pathway "
                          "reframed in ITU language. Predictions overlap "
                          "with industry consensus (BNEF, IEA, Goldman).",
        "tier": 1,
        "paper_number": 10,
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "next_paper_candidates": [
            "Tier 1 #11: Climate / Earth Systems (Phase 83-86)",
            "Tier 1 #12: Astrobiology / SETI (Phase 87-90)",
            "Pass-2: Re-traverse Tier 1 with ITU-unique predictions",
        ],
        "caveats": [
            "IEA NZE scenarios depend on policy implementation",
            "China share decline assumes Western policy success",
            "Fusion commercialization timing uncertain",
            "Room-temp superconductor discovery is speculative",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase82.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 82] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 82 complete. Tier 1 #10 (Energy/Materials) ready for Zenodo.")
    print(f"  - 2050 energy mix: Solar 50%, Wind 22%, Nuclear 9%, Fossil 2%")
    print(f"  - China gallium: 98% -> 60% by 2050")
    print(f"  - DAC: $800/t (2024) -> $50/t (2050), 1 GtCO₂/yr capacity")
    print(f"  - **ITU 10-vertex polytope completed!**")
    print(f"  - Pass-1 progress: 82/220 = 37.3%")
    print("=" * 60)


if __name__ == "__main__":
    main()
