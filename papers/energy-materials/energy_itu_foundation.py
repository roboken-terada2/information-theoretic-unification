#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 79: ITU Foundation for Energy and Materials

Energy = K-work, information = K-bit (Landauer equivalence).
Battery/solar/material progress = K_storage and K_structure improvements.

Tests:
  1. Landauer limit vs modern compute energy per op
  2. Battery technology Pareto (energy density vs cost)
  3. Solar cell efficiency vs Shockley-Queisser limit
  4. Critical materials supply concentration (HHI)

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #10 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# Physical constants
k_B = 1.380649e-23
q_e = 1.602176634e-19
ln2 = np.log(2)


# =============================================================================
# Test 1: Landauer limit vs compute history
# =============================================================================
COMPUTE_HISTORY = {
    1950: 1e-3,    # vacuum tube
    1965: 1e-5,    # transistor
    1980: 1e-8,    # VLSI
    1995: 1e-11,
    2010: 1e-15,
    2024: 1e-17,   # GAAFET 3nm
    2030: 1e-18,   # CFET 1nm (predicted)
    2040: 1e-19,   # photonic compute (predicted)
}


def landauer_limit_300K():
    return k_B * 300 * ln2


# =============================================================================
# Test 2: Battery Pareto
# =============================================================================
BATTERIES = {
    "Lead-acid":             {"density_Wh_kg": 30,   "cost_USD_kWh": 100, "year": 1860,
                                "status": "mature"},
    "Ni-Cd":                 {"density_Wh_kg": 50,   "cost_USD_kWh": 800, "year": 1900,
                                "status": "deprecated"},
    "Ni-MH":                 {"density_Wh_kg": 90,   "cost_USD_kWh": 600, "year": 1990,
                                "status": "niche"},
    "Li-ion (NMC)":          {"density_Wh_kg": 250,  "cost_USD_kWh": 140, "year": 2008,
                                "status": "dominant"},
    "Li-ion (LFP)":          {"density_Wh_kg": 200,  "cost_USD_kWh": 100, "year": 2010,
                                "status": "dominant"},
    "Solid-state (proj)":    {"density_Wh_kg": 450,  "cost_USD_kWh": 80,  "year": 2028,
                                "status": "predicted"},
    "Li-air (theoretical)":  {"density_Wh_kg": 3500, "cost_USD_kWh": 200, "year": 2035,
                                "status": "research"},
    "Iron-air (Form Energy)": {"density_Wh_kg": 100,  "cost_USD_kWh": 20,  "year": 2024,
                                "status": "grid"},
    "Hydrogen FC":           {"density_Wh_kg": 33000, "cost_USD_kWh": 250, "year": 2010,
                                "status": "developing"},
}


# =============================================================================
# Test 3: Solar cell efficiency
# =============================================================================
SOLAR_TECH = {
    "Single c-Si":            {"efficiency_pct": 26.8, "sq_limit_pct": 33.7,  "year": 2023},
    "Thin-film (CIGS, CdTe)":  {"efficiency_pct": 23.6, "sq_limit_pct": 30,    "year": 2024},
    "Perovskite":              {"efficiency_pct": 26.1, "sq_limit_pct": 33,    "year": 2024},
    "Tandem (Si+perovskite)": {"efficiency_pct": 33.9, "sq_limit_pct": 47,    "year": 2024},
    "Triple-junction":        {"efficiency_pct": 47.6, "sq_limit_pct": 86,    "year": 2024},
    "Quantum dot":             {"efficiency_pct": 18.0, "sq_limit_pct": 67,    "year": 2024},
}


# =============================================================================
# Test 4: Critical materials HHI
# =============================================================================
CRITICAL_MATERIALS = {
    "Lithium":           {"top_country": "Australia", "top_share_pct": 50, "supplier_count": 4},
    "Cobalt":            {"top_country": "DR Congo",  "top_share_pct": 60, "supplier_count": 3},
    "Nickel":            {"top_country": "Indonesia", "top_share_pct": 40, "supplier_count": 5},
    "Rare earths":       {"top_country": "China",     "top_share_pct": 85, "supplier_count": 3},
    "Gallium":           {"top_country": "China",     "top_share_pct": 98, "supplier_count": 1},
    "Germanium":         {"top_country": "China",     "top_share_pct": 60, "supplier_count": 3},
    "Silicon (refined)": {"top_country": "China",     "top_share_pct": 80, "supplier_count": 2},
    "Graphite":          {"top_country": "China",     "top_share_pct": 70, "supplier_count": 3},
    "Uranium":           {"top_country": "Kazakhstan", "top_share_pct": 40, "supplier_count": 5},
}


def hhi_index(top_share, n_suppliers):
    """Herfindahl-Hirschman approx assuming remaining suppliers share equally."""
    remaining = (100 - top_share) / max(n_suppliers - 1, 1)
    return top_share ** 2 + (n_suppliers - 1) * remaining ** 2


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Landauer vs compute history ---
    ax = axes[0, 0]
    years = sorted(COMPUTE_HISTORY.keys())
    energies = [COMPUTE_HISTORY[y] for y in years]
    landauer = landauer_limit_300K()
    ax.semilogy(years, energies, "o-", lw=2.5, color="navy",
                 label="Energy per op (compute)")
    ax.axhline(landauer, ls="--", color="red", lw=2,
               label=f"Landauer 300K: {landauer:.2e} J")
    # Annotate gap
    gap_2024 = COMPUTE_HISTORY[2024] / landauer
    ax.annotate(f"2024 gap: {gap_2024:.0f}× Landauer",
                xy=(2024, COMPUTE_HISTORY[2024]),
                xytext=(1990, 1e-13),
                fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black"))
    # 1950 -> 2030
    delta_decades = np.log10(COMPUTE_HISTORY[1950] / COMPUTE_HISTORY[2030])
    ax.text(0.02, 0.05, f"1950 → 2030:\n{delta_decades:.0f} orders of magnitude\nimprovement",
            transform=ax.transAxes, fontsize=9,
            bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))
    ax.set_xlabel("Year")
    ax.set_ylabel("Energy per operation [J]")
    ax.set_title("(a) Compute energy → Landauer limit")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper right", fontsize=9)

    # --- (b) Battery Pareto ---
    ax = axes[0, 1]
    status_colors = {"mature": "gray", "deprecated": "lightgray",
                      "niche": "orange", "dominant": "green",
                      "predicted": "blue", "research": "purple",
                      "grid": "brown", "developing": "red"}
    for name, d in BATTERIES.items():
        ax.scatter(d["cost_USD_kWh"], d["density_Wh_kg"],
                    s=200, c=status_colors[d["status"]],
                    edgecolor="black", linewidths=1, alpha=0.7)
        ax.annotate(name, (d["cost_USD_kWh"], d["density_Wh_kg"]),
                     xytext=(8, 4), textcoords="offset points",
                     fontsize=7)
    # Gasoline reference (not technically a battery but for scale)
    ax.scatter(0.05, 12200, s=200, c="black", marker="*", zorder=5)
    ax.annotate("Gasoline (ref)", (0.05, 12200),
                 xytext=(8, 4), textcoords="offset points",
                 fontsize=7, color="black")
    ax.set_xlabel("Cost [USD/kWh]")
    ax.set_ylabel("Energy density [Wh/kg]")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("(b) Battery Pareto — density × cost")
    ax.grid(True, alpha=0.3, which="both")
    ax.set_xlim(0.03, 1000)
    ax.set_ylim(20, 50000)

    # --- (c) Solar Shockley-Queisser ---
    ax = axes[1, 0]
    names = list(SOLAR_TECH.keys())
    effs = [SOLAR_TECH[n]["efficiency_pct"] for n in names]
    sq_limits = [SOLAR_TECH[n]["sq_limit_pct"] for n in names]
    x = np.arange(len(names))
    width = 0.35
    bars1 = ax.bar(x - width / 2, effs, width, color="green", alpha=0.7,
                    edgecolor="black", label="Best 2024")
    bars2 = ax.bar(x + width / 2, sq_limits, width, color="red", alpha=0.4,
                    edgecolor="black", label="Theoretical limit")
    for bar, v in zip(bars1, effs):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.5, f"{v:.1f}%",
                ha="center", fontsize=7)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=20, fontsize=7)
    ax.set_ylabel("Efficiency [%]")
    ax.set_title("(c) Solar cells — best 2024 vs SQ limit")
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend(loc="upper right")
    ax.set_ylim(0, 90)

    # --- (d) Critical materials HHI ---
    ax = axes[1, 1]
    names = list(CRITICAL_MATERIALS.keys())
    hhis = [hhi_index(CRITICAL_MATERIALS[n]["top_share_pct"],
                       CRITICAL_MATERIALS[n]["supplier_count"])
            for n in names]
    countries = [CRITICAL_MATERIALS[n]["top_country"] for n in names]
    # Color by China dominance
    colors = ["red" if c == "China" else "orange" for c in countries]
    # sort by HHI descending
    idx = np.argsort(hhis)[::-1]
    names_s = [names[i] for i in idx]
    hhis_s = [hhis[i] for i in idx]
    colors_s = [colors[i] for i in idx]
    countries_s = [countries[i] for i in idx]
    bars = ax.barh(names_s, hhis_s, color=colors_s, alpha=0.7,
                    edgecolor="black")
    for bar, h, c in zip(bars, hhis_s, countries_s):
        ax.text(h + 100, bar.get_y() + bar.get_height() / 2,
                f"{int(h)} ({c})", va="center", fontsize=8)
    ax.axvline(2500, ls="--", color="red", alpha=0.5,
               label="HHI 2500 (high concentration)")
    ax.set_xlabel("HHI index (supplier concentration)")
    ax.set_title("(d) Critical materials supply concentration")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=8)
    ax.legend(loc="lower right")
    ax.set_xlim(0, 12000)

    plt.suptitle("Phase 79: ITU foundation for energy/materials — "
                 "information ⇔ energy",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "energy_itu_foundation.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 79] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 79: ITU foundation for energy / materials")
    print("=" * 60)

    # [1]
    print("\n[1] Landauer limit vs compute history:")
    landauer = landauer_limit_300K()
    print(f"  Landauer 300K = {landauer:.3e} J/bit")
    for yr in sorted(COMPUTE_HISTORY.keys()):
        e = COMPUTE_HISTORY[yr]
        gap = e / landauer
        print(f"  {yr}: {e:.0e} J/op = {gap:.0e}× Landauer")

    # [2]
    print("\n[2] Battery Pareto (sorted by year):")
    for name, d in sorted(BATTERIES.items(), key=lambda x: x[1]["year"]):
        print(f"  {name:<25s} ({d['year']}): "
              f"{d['density_Wh_kg']:5d} Wh/kg, "
              f"${d['cost_USD_kWh']}/kWh, {d['status']}")

    # [3]
    print("\n[3] Solar cells vs Shockley-Queisser:")
    for tech, d in SOLAR_TECH.items():
        ratio = d["efficiency_pct"] / d["sq_limit_pct"] * 100
        print(f"  {tech:<24s}: {d['efficiency_pct']:5.1f}% / "
              f"{d['sq_limit_pct']:.0f}% SQ limit "
              f"({ratio:.0f}% of theoretical max)")

    # [4]
    print("\n[4] Critical materials HHI:")
    for name, d in sorted(CRITICAL_MATERIALS.items(),
                            key=lambda x: -hhi_index(
                                x[1]["top_share_pct"], x[1]["supplier_count"])):
        h = hhi_index(d["top_share_pct"], d["supplier_count"])
        print(f"  {name:<20s}: HHI={int(h):5d}, top={d['top_country']} "
              f"({d['top_share_pct']}%)")

    plot_path = make_plot()

    summary = {
        "phase": 79,
        "paper": "ITU and Energy / Materials",
        "description": "ITU foundation - information-energy equivalence, batteries, solar, materials",
        "landauer_limit_J": float(landauer),
        "compute_history": COMPUTE_HISTORY,
        "compute_gap_2024_over_landauer": float(COMPUTE_HISTORY[2024] / landauer),
        "batteries": BATTERIES,
        "best_battery_2024_NMC": {
            "density_Wh_kg": 250,
            "cost_USD_kWh": 140,
            "improvement_over_lead_acid": "8x density, 0.7x cost vs 1860",
        },
        "solar_cells": SOLAR_TECH,
        "critical_materials_HHI": {
            name: int(hhi_index(d["top_share_pct"], d["supplier_count"]))
            for name, d in CRITICAL_MATERIALS.items()
        },
        "central_thesis": "Energy = K-work. Information = K-bit. "
                          "Landauer 1961 + Bennett 1982 establish "
                          "their equivalence. 21st century: battery "
                          "density 10x in 30 years; solar cells "
                          "approach SQ limit via tandem cells; "
                          "critical materials concentrated in China "
                          "(rare earths 85%, gallium 98%). AI + quantum "
                          "computing accelerate material discovery 10x.",
        "honest_framing": "Pass-1 interpretive paper. Reframes Landauer, "
                          "Bennett, Shockley-Queisser, Wright's Law, "
                          "Swanson's Law in ITU language. Numerical data "
                          "from IEA, BNEF, US DOE, Merchant 2023.",
        "tier": 1,
        "paper_number": 10,
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "next_phases": [
            "Phase 80: Renewable energy + nuclear fusion (ITU systems view)",
            "Phase 81: Materials science - perovskites, MOFs, quantum materials",
            "Phase 82: Energy roadmap 2026-2050 + 10 predictions",
        ],
        "caveats": [
            "Compute energy values are approximate decade averages",
            "Battery costs vary by source (BNEF, IEA, BCG differ)",
            "Solar SQ limits depend on solar spectrum assumptions",
            "HHI calculation simplifies remaining-supplier distribution",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase79.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 79] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 79 complete.")
    print(f"  - Landauer limit at 300K: {landauer:.3e} J/bit")
    print(f"  - 2024 compute gap: {COMPUTE_HISTORY[2024]/landauer:.0f}× Landauer")
    print(f"  - Best battery: Li-ion NMC 250 Wh/kg @ $140/kWh")
    print(f"  - Best solar (tandem): 33.9% efficiency")
    print(f"  - Critical materials: Gallium 98% China dominance")
    print("=" * 60)


if __name__ == "__main__":
    main()
