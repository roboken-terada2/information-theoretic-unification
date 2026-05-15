#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 81: New materials revolution under ITU

Perovskites (solar, qubits), MOFs (CO2 capture), quantum materials
(superconductivity), AI-driven discovery (GNoME, MatterGen).

Tests:
  1. Perovskite solar cell efficiency 2009-2024
  2. Superconductor Tc evolution 1911-2024
  3. MOF surface area records
  4. AI material discovery acceleration

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #10 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Perovskite efficiency
# =============================================================================
PEROVSKITE_HISTORY = {
    2009: 3.8,    # Miyasaka first
    2012: 9.7,    # Park, et al.
    2014: 19.3,
    2016: 22.1,
    2018: 23.7,
    2020: 25.5,
    2022: 25.8,
    2024: 26.7,   # Single junction
    "2024 tandem": 34.6,  # Si+perovskite (Oxford PV)
    "2030 predicted single": 30.0,
    "2030 tandem predicted": 38.0,
}


# =============================================================================
# Test 2: Superconductor Tc
# =============================================================================
SUPERCONDUCTORS = [
    {"year": 1911, "material": "Hg",                  "Tc_K": 4.2,   "type": "elemental"},
    {"year": 1957, "material": "Sn",                  "Tc_K": 7.2,   "type": "BCS"},
    {"year": 1973, "material": "Nb3Ge",               "Tc_K": 23.3,  "type": "alloy"},
    {"year": 1986, "material": "LaBaCuO",             "Tc_K": 35.0,  "type": "cuprate"},
    {"year": 1987, "material": "YBaCuO7",             "Tc_K": 92.0,  "type": "cuprate"},
    {"year": 1993, "material": "HgBaCaCuO",           "Tc_K": 134.0, "type": "cuprate"},
    {"year": 2008, "material": "Fe-based",            "Tc_K": 55.0,  "type": "iron pnictide"},
    {"year": 2015, "material": "H3S @150GPa",         "Tc_K": 203.0, "type": "hydride"},
    {"year": 2019, "material": "LaH10 @170GPa",       "Tc_K": 250.0, "type": "hydride"},
    {"year": 2030, "material": "Room-temp predicted", "Tc_K": 293.0, "type": "predicted"},
]


# =============================================================================
# Test 3: MOF surface area records
# =============================================================================
MOFS = {
    "Activated Carbon (typical)": {"SA_m2_per_g": 1500,  "year": 1900},
    "Zeolite NaY":                 {"SA_m2_per_g": 1000,  "year": 1950},
    "MOF-5":                       {"SA_m2_per_g": 3800,  "year": 1999},
    "MOF-177":                     {"SA_m2_per_g": 4500,  "year": 2004},
    "MIL-101":                     {"SA_m2_per_g": 5900,  "year": 2005},
    "NU-100":                      {"SA_m2_per_g": 6143,  "year": 2010},
    "MOF-210":                     {"SA_m2_per_g": 6240,  "year": 2010},
    "NU-1501":                     {"SA_m2_per_g": 7140,  "year": 2020},
    "Theoretical limit":           {"SA_m2_per_g": 7800,  "year": 2025},
}


# =============================================================================
# Test 4: AI material discovery
# =============================================================================
AI_DISCOVERY = {
    "Classical (Edisonian, 1960s)": {"design_to_test_months": 24, "candidates_processed": 100,    "year": 1960},
    "Combinatorial (1990s)":         {"design_to_test_months": 12, "candidates_processed": 10000,  "year": 1990},
    "Materials Project (MIT, 2011)":  {"design_to_test_months": 6,  "candidates_processed": 150000, "year": 2011},
    "DFT screening (2015)":          {"design_to_test_months": 3,  "candidates_processed": 500000, "year": 2015},
    "DeepMind GNoME (2023)":         {"design_to_test_months": 1,  "candidates_processed": 2200000, "year": 2023},
    "MatterGen (2024)":              {"design_to_test_months": 0.5, "candidates_processed": 5000000, "year": 2024},
    "Quantum DFT (predicted 2030)":   {"design_to_test_months": 0.25, "candidates_processed": 100000000, "year": 2030},
}


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Perovskite efficiency ---
    ax = axes[0, 0]
    # Single junction history
    years_single = [k for k in PEROVSKITE_HISTORY.keys()
                     if isinstance(k, int)]
    effs_single = [PEROVSKITE_HISTORY[y] for y in years_single]
    ax.plot(years_single, effs_single, "o-", lw=2.5, color="orange",
            label="Single junction")
    # Tandem
    ax.scatter(2024, PEROVSKITE_HISTORY["2024 tandem"], s=200,
                color="red", marker="*", zorder=5,
                label=f"Si+perovskite tandem 2024 ({PEROVSKITE_HISTORY['2024 tandem']}%)")
    ax.scatter(2030, PEROVSKITE_HISTORY["2030 tandem predicted"], s=200,
                color="purple", marker="*", zorder=5,
                label=f"Tandem 2030 predicted ({PEROVSKITE_HISTORY['2030 tandem predicted']}%)")
    # Annotations
    ax.annotate(f"Miyasaka 2009\n{PEROVSKITE_HISTORY[2009]}%",
                 (2009, PEROVSKITE_HISTORY[2009]),
                 xytext=(8, 4), textcoords="offset points", fontsize=8)
    ax.annotate(f"{PEROVSKITE_HISTORY[2024]}%",
                 (2024, PEROVSKITE_HISTORY[2024]),
                 xytext=(8, -4), textcoords="offset points", fontsize=8)
    # Si record for comparison
    ax.axhline(26.8, ls="--", color="gray", alpha=0.5,
               label="c-Si record (26.8%)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Solar cell efficiency [%]")
    ax.set_title("(a) Perovskite efficiency: 7× growth in 15 years")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)
    ax.set_xlim(2008, 2032)
    ax.set_ylim(0, 45)

    # --- (b) Superconductor Tc ---
    ax = axes[0, 1]
    years_sc = [s["year"] for s in SUPERCONDUCTORS]
    Tcs = [s["Tc_K"] for s in SUPERCONDUCTORS]
    type_colors = {"elemental": "gray", "BCS": "blue",
                    "alloy": "orange", "cuprate": "red",
                    "iron pnictide": "green", "hydride": "purple",
                    "predicted": "gold"}
    for s in SUPERCONDUCTORS:
        ax.scatter(s["year"], s["Tc_K"], s=150,
                    c=type_colors[s["type"]], edgecolor="black",
                    zorder=5)
        # Annotate selected
        if s["material"] in ["Hg", "YBaCuO7", "H3S @150GPa",
                              "LaH10 @170GPa", "Room-temp predicted"]:
            ax.annotate(f"{s['material']}\n{s['Tc_K']:.0f}K",
                         (s["year"], s["Tc_K"]),
                         xytext=(8, 4), textcoords="offset points",
                         fontsize=7)
    ax.axhline(77, ls="--", color="blue", alpha=0.5,
               label="LN2 (77 K)")
    ax.axhline(293, ls="--", color="red", alpha=0.7,
               label="Room temp (293 K) — holy grail")
    ax.set_xlabel("Year")
    ax.set_ylabel("Critical temperature Tc [K]")
    ax.set_title("(b) Superconductor Tc: 1911-2030")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(1905, 2035)
    ax.set_ylim(0, 320)

    # --- (c) MOF surface area ---
    ax = axes[1, 0]
    names = list(MOFS.keys())
    SAs = [MOFS[n]["SA_m2_per_g"] for n in names]
    years = [MOFS[n]["year"] for n in names]
    # Sort by year
    idx = np.argsort(years)
    names_s = [names[i] for i in idx]
    SAs_s = [SAs[i] for i in idx]
    years_s = [years[i] for i in idx]
    bars = ax.barh(names_s, SAs_s, color="purple", alpha=0.7,
                    edgecolor="black")
    for bar, sa, yr in zip(bars, SAs_s, years_s):
        ax.text(sa + 50, bar.get_y() + bar.get_height() / 2,
                f"{sa} ({yr})", va="center", fontsize=8)
    ax.set_xlabel("Specific surface area [m²/g]")
    ax.set_title("(c) MOF surface area records — 1.7 soccer fields/g")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=8)
    ax.set_xlim(0, 9000)

    # --- (d) AI discovery acceleration ---
    ax = axes[1, 1]
    methods = list(AI_DISCOVERY.keys())
    months = [AI_DISCOVERY[m]["design_to_test_months"] for m in methods]
    candidates = [AI_DISCOVERY[m]["candidates_processed"] for m in methods]
    years_ai = [AI_DISCOVERY[m]["year"] for m in methods]
    ax.scatter(months, candidates, s=200, c=years_ai, cmap="viridis",
                edgecolor="black")
    for m, mo, c in zip(methods, months, candidates):
        ax.annotate(m, (mo, c), xytext=(8, 4),
                     textcoords="offset points", fontsize=7)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Design → test time [months, log]")
    ax.set_ylabel("Candidates processed [log]")
    ax.set_title("(d) AI material discovery — exponential acceleration")
    ax.grid(True, alpha=0.3, which="both")
    # Invert x to show "faster = better" on right
    ax.invert_xaxis()
    # Color bar
    plt.colorbar(ax.collections[0], ax=ax, label="Year")

    plt.suptitle("Phase 81: Materials revolution — perovskites, MOFs, "
                 "quantum materials, AI",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "materials_revolution.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 81] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 81: New materials revolution under ITU")
    print("=" * 60)

    # [1]
    print("\n[1] Perovskite efficiency timeline:")
    years_single = [k for k in PEROVSKITE_HISTORY.keys()
                     if isinstance(k, int)]
    for y in years_single:
        print(f"  {y}: {PEROVSKITE_HISTORY[y]:.1f}%")
    print(f"  2024 tandem (Si+perovskite): "
          f"{PEROVSKITE_HISTORY['2024 tandem']}%")
    print(f"  Growth 2009→2024 single: "
          f"{PEROVSKITE_HISTORY[2024]/PEROVSKITE_HISTORY[2009]:.1f}x")

    # [2]
    print("\n[2] Superconductor Tc history:")
    for s in SUPERCONDUCTORS:
        marker = "★" if s["Tc_K"] >= 200 else " "
        print(f"  {s['year']} ({s['type']:<14s}): {s['material']:<28s} "
              f"Tc={s['Tc_K']:6.1f} K {marker}")

    # [3]
    print("\n[3] MOF surface area records:")
    for n, d in sorted(MOFS.items(), key=lambda x: x[1]["year"]):
        print(f"  {d['year']}: {n:<28s} {d['SA_m2_per_g']:5d} m²/g")

    # [4]
    print("\n[4] AI material discovery acceleration:")
    for method, d in AI_DISCOVERY.items():
        print(f"  {d['year']} ({method:<32s}): "
              f"design→test {d['design_to_test_months']:>5.2f} months, "
              f"{d['candidates_processed']:>10,d} candidates")

    plot_path = make_plot()

    summary = {
        "phase": 81,
        "paper": "ITU and Energy / Materials",
        "description": "New materials revolution - perovskites, MOFs, quantum, AI",
        "perovskite_efficiency": {
            str(k): v for k, v in PEROVSKITE_HISTORY.items()
        },
        "perovskite_growth_2009_to_2024_single": float(
            PEROVSKITE_HISTORY[2024] / PEROVSKITE_HISTORY[2009]
        ),
        "superconductor_history": SUPERCONDUCTORS,
        "current_record_Tc_K": 250,
        "room_temp_target_K": 293,
        "MOFs": MOFS,
        "MOF_max_SA_m2_per_g": 7140,
        "MOF_max_year": 2020,
        "AI_discovery_acceleration": AI_DISCOVERY,
        "acceleration_1960_to_2024": {
            "time_compression_factor": float(
                AI_DISCOVERY["Classical (Edisonian, 1960s)"]["design_to_test_months"] /
                AI_DISCOVERY["MatterGen (2024)"]["design_to_test_months"]
            ),
            "throughput_increase_factor": float(
                AI_DISCOVERY["MatterGen (2024)"]["candidates_processed"] /
                AI_DISCOVERY["Classical (Edisonian, 1960s)"]["candidates_processed"]
            ),
        },
        "central_thesis": "21st century materials revolution = K_structure "
                          "atomic-precision design. Perovskites: 3.8% (2009) "
                          "to 34.6% tandem (2024). MOFs: 1.7 soccer fields "
                          "per gram of surface. Superconductors: 250K at "
                          "high pressure (2019), room temp by 2030-2040 "
                          "possible. AI: GNoME 2.2M crystals, MatterGen "
                          "inverse design. 10-100x discovery acceleration.",
        "honest_framing": "Pass-1 interpretive paper. Reframes Miyasaka, "
                          "Yaghi, Bednorz-Müller, Eremets, GNoME, MatterGen "
                          "in ITU language. No novel material proposed.",
        "tier": 1,
        "paper_number": 10,
        "next_phase": "Phase 82: Energy/materials roadmap 2026-2050 + 10 predictions",
        "caveats": [
            "Perovskite stability under humidity/heat remains issue",
            "High-pressure superconductors need >100 GPa, not practical",
            "MOF synthesis at scale challenges",
            "AI predictions need experimental validation",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase81.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 81] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 81 complete.")
    print(f"  - Perovskite: 3.8% (2009) → 34.6% tandem (2024) = 9× in 15yr")
    print(f"  - Superconductor: LaH10 250K (2019), room-temp predicted 2030+")
    print(f"  - MOF NU-1501: 7140 m²/g = 1.7 soccer fields per gram")
    print(f"  - AI: 24mo→0.5mo design cycle = 48× acceleration")
    print("=" * 60)


if __name__ == "__main__":
    main()
