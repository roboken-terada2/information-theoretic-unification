#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 77: Ethics, criminal law, K_self-based justice system under ITU

Replace binary guilty/innocent with K_self degree continuum.
Treatment-vs-punishment economics, restorative justice, AI liability.

Tests:
  1. Mens rea levels mapped to K_self thresholds
  2. International recidivism vs justice style
  3. Intervention cost-effectiveness Pareto
  4. Death-penalty vs abolition crime rates

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #9 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Mens rea / K_self mapping
# =============================================================================
MENS_REA_LEVELS = {
    "Purposeful (intent)":      {"K_self_min": 0.40, "sentencing_factor": 1.00},
    "Knowing":                   {"K_self_min": 0.30, "sentencing_factor": 0.80},
    "Reckless":                  {"K_self_min": 0.20, "sentencing_factor": 0.50},
    "Negligent":                 {"K_self_min": 0.10, "sentencing_factor": 0.30},
    "Diminished responsibility": {"K_self_min": 0.05, "sentencing_factor": 0.10},
    "Not responsible (insanity)": {"K_self_min": 0.00, "sentencing_factor": 0.00},
}


# =============================================================================
# Test 2: Recidivism by country
# =============================================================================
COUNTRIES_JUSTICE = {
    "Norway":      {"recidivism_5yr_pct": 20, "style": "rehabilitative",
                     "cost_per_year_USD_K": 35, "color": "green"},
    "Netherlands": {"recidivism_5yr_pct": 25, "style": "rehabilitative",
                     "cost_per_year_USD_K": 45, "color": "green"},
    "Sweden":      {"recidivism_5yr_pct": 25, "style": "rehabilitative",
                     "cost_per_year_USD_K": 50, "color": "green"},
    "Germany":     {"recidivism_5yr_pct": 45, "style": "mixed",
                     "cost_per_year_USD_K": 40, "color": "orange"},
    "Japan":       {"recidivism_5yr_pct": 38, "style": "mixed (strict)",
                     "cost_per_year_USD_K": 30, "color": "orange"},
    "UK":          {"recidivism_5yr_pct": 50, "style": "mixed",
                     "cost_per_year_USD_K": 38, "color": "orange"},
    "USA":         {"recidivism_5yr_pct": 76, "style": "punitive",
                     "cost_per_year_USD_K": 50, "color": "red"},
    "Russia":      {"recidivism_5yr_pct": 65, "style": "punitive",
                     "cost_per_year_USD_K": 10, "color": "red"},
}


# =============================================================================
# Test 3: Intervention cost vs effect (Pareto)
# =============================================================================
INTERVENTIONS = {
    "No intervention":                {"cost": 35,   "recid_reduction_pct": 0,   "tier": "baseline"},
    "Cognitive Behavioral Therapy":   {"cost": 8,    "recid_reduction_pct": 25,  "tier": "treatment"},
    "Drug treatment":                 {"cost": 15,   "recid_reduction_pct": 30,  "tier": "treatment"},
    "Vocational training":            {"cost": 5,    "recid_reduction_pct": 20,  "tier": "rehab"},
    "Education (HS+)":                 {"cost": 5,    "recid_reduction_pct": 40,  "tier": "rehab"},
    "Restorative justice":            {"cost": 3,    "recid_reduction_pct": 30,  "tier": "restorative"},
    "Drug court diversion":           {"cost": 10,   "recid_reduction_pct": 35,  "tier": "treatment"},
    "Standard incarceration":         {"cost": 35,   "recid_reduction_pct": 5,   "tier": "punitive"},
    "Max-security incarceration":     {"cost": 60,   "recid_reduction_pct": 5,   "tier": "punitive"},
    "Combination (CBT+edu+drug)":     {"cost": 25,   "recid_reduction_pct": 55,  "tier": "combo"},
}


# =============================================================================
# Test 4: Death penalty vs abolition (per 100k)
# =============================================================================
DEATH_PENALTY_DATA = {
    # Pairs of comparable states/regions
    "USA (death penalty states)":    {"homicide_per_100k": 6.2, "death_penalty": True},
    "USA (abolition states)":         {"homicide_per_100k": 5.4, "death_penalty": False},
    "Texas":                          {"homicide_per_100k": 7.6, "death_penalty": True},
    "Michigan":                       {"homicide_per_100k": 6.0, "death_penalty": False},
    "Japan":                          {"homicide_per_100k": 0.3, "death_penalty": True},
    "South Korea (de facto abolition)": {"homicide_per_100k": 0.6, "death_penalty": False},
    "Canada (abolished 1976)":        {"homicide_per_100k": 1.9, "death_penalty": False},
    "EU 27 (all abolished)":          {"homicide_per_100k": 1.1, "death_penalty": False},
}


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Mens rea levels ---
    ax = axes[0, 0]
    levels = list(MENS_REA_LEVELS.keys())
    k_min = [MENS_REA_LEVELS[l]["K_self_min"] for l in levels]
    sent_f = [MENS_REA_LEVELS[l]["sentencing_factor"] for l in levels]
    x = np.arange(len(levels))
    width = 0.35
    bars1 = ax.bar(x - width / 2, k_min, width, color="navy", alpha=0.7,
                    label="K_self threshold")
    bars2 = ax.bar(x + width / 2, sent_f, width, color="darkred", alpha=0.7,
                    label="Sentencing factor")
    for bar, v in zip(bars1, k_min):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.01,
                f"{v:.2f}", ha="center", fontsize=8)
    for bar, v in zip(bars2, sent_f):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.01,
                f"{v:.2f}", ha="center", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels([l.split(" ")[0] for l in levels], fontsize=7,
                       rotation=30)
    ax.set_ylabel("Value")
    ax.set_title("(a) Mens rea ↔ K_self degree mapping")
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend(loc="upper right", fontsize=9)
    ax.set_ylim(0, 1.1)

    # --- (b) Recidivism by country ---
    ax = axes[0, 1]
    countries = list(COUNTRIES_JUSTICE.keys())
    recids = [COUNTRIES_JUSTICE[c]["recidivism_5yr_pct"] for c in countries]
    colors = [COUNTRIES_JUSTICE[c]["color"] for c in countries]
    styles = [COUNTRIES_JUSTICE[c]["style"] for c in countries]
    # sort
    idx = np.argsort(recids)
    countries_s = [countries[i] for i in idx]
    recids_s = [recids[i] for i in idx]
    colors_s = [colors[i] for i in idx]
    bars = ax.barh(countries_s, recids_s, color=colors_s, alpha=0.7,
                    edgecolor="black")
    for bar, r in zip(bars, recids_s):
        ax.text(r + 1, bar.get_y() + bar.get_height() / 2, f"{r}%",
                va="center", fontsize=8)
    ax.set_xlabel("5-year recidivism rate [%]")
    ax.set_title("(b) Recidivism by country — style matters")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=8)
    from matplotlib.patches import Patch
    legend = [
        Patch(facecolor="green", label="Rehabilitative"),
        Patch(facecolor="orange", label="Mixed"),
        Patch(facecolor="red", label="Punitive"),
    ]
    ax.legend(handles=legend, loc="lower right", fontsize=8)

    # --- (c) Intervention Pareto ---
    ax = axes[1, 0]
    tier_colors = {"baseline": "gray", "treatment": "blue",
                    "rehab": "green", "restorative": "purple",
                    "punitive": "red", "combo": "darkgreen"}
    for name, d in INTERVENTIONS.items():
        ax.scatter(d["cost"], d["recid_reduction_pct"],
                    s=200, c=tier_colors[d["tier"]], alpha=0.7,
                    edgecolor="black")
        ax.annotate(name, (d["cost"], d["recid_reduction_pct"]),
                     xytext=(8, 0), textcoords="offset points",
                     fontsize=7)
    ax.set_xlabel("Cost per offender per year [$K]")
    ax.set_ylabel("Recidivism reduction [%]")
    ax.set_title("(c) Intervention cost vs effect — Pareto")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 65)
    ax.set_ylim(-5, 65)
    # Annotate sweet spot
    ax.text(0.95, 0.05, "★ Sweet spot:\nlow cost +\nhigh reduction",
            transform=ax.transAxes, fontsize=9,
            bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8),
            ha="right", verticalalignment="bottom")

    # --- (d) Death penalty vs abolition ---
    ax = axes[1, 1]
    regions = list(DEATH_PENALTY_DATA.keys())
    homicide = [DEATH_PENALTY_DATA[r]["homicide_per_100k"] for r in regions]
    death = [DEATH_PENALTY_DATA[r]["death_penalty"] for r in regions]
    colors_d = ["red" if d else "green" for d in death]
    bars = ax.barh(regions, homicide, color=colors_d, alpha=0.7,
                    edgecolor="black")
    for bar, h in zip(bars, homicide):
        ax.text(h + 0.1, bar.get_y() + bar.get_height() / 2,
                f"{h:.1f}", va="center", fontsize=8)
    ax.set_xlabel("Homicide rate per 100,000 (2020-2023 avg)")
    ax.set_title("(d) Death penalty does NOT lower homicide")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=7)
    legend_dp = [
        Patch(facecolor="red", label="Death penalty active"),
        Patch(facecolor="green", label="Abolished / de facto"),
    ]
    ax.legend(handles=legend_dp, loc="lower right", fontsize=8)

    plt.suptitle("Phase 77: Ethics + criminal law — ITU K_self-based justice",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "freewill_ethics_law.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 77] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 77: Ethics, criminal law, K_self-based justice")
    print("=" * 60)

    # [1]
    print("\n[1] Mens rea → K_self mapping:")
    for level, d in MENS_REA_LEVELS.items():
        print(f"  {level:<32s}: K_self >= {d['K_self_min']:.2f}, "
              f"sentence factor {d['sentencing_factor']:.2f}")

    # [2]
    print("\n[2] International recidivism (5-year):")
    sorted_c = sorted(COUNTRIES_JUSTICE.items(),
                       key=lambda x: x[1]["recidivism_5yr_pct"])
    for c, d in sorted_c:
        print(f"  {c:<15s}: {d['recidivism_5yr_pct']:3d}% "
              f"({d['style']:<18s}, ${d['cost_per_year_USD_K']}K/yr)")

    # [3]
    print("\n[3] Intervention Pareto (best cost-effectiveness):")
    # sort by cost-effectiveness (reduction per $K)
    eff = [(name, d["recid_reduction_pct"] / max(d["cost"], 1))
           for name, d in INTERVENTIONS.items()]
    eff.sort(key=lambda x: -x[1])
    for name, e in eff[:5]:
        d = INTERVENTIONS[name]
        print(f"  {name:<32s}: -{d['recid_reduction_pct']}% recid, "
              f"${d['cost']}K → eff={e:.2f}")

    # [4]
    print("\n[4] Death penalty vs homicide rate:")
    dp_yes = [d["homicide_per_100k"] for d in DEATH_PENALTY_DATA.values()
              if d["death_penalty"]]
    dp_no = [d["homicide_per_100k"] for d in DEATH_PENALTY_DATA.values()
             if not d["death_penalty"]]
    print(f"  Death-penalty average homicide: {np.mean(dp_yes):.2f}/100K")
    print(f"  Abolition average homicide:    {np.mean(dp_no):.2f}/100K")
    print(f"  -> Death penalty does NOT correlate with lower homicide")

    plot_path = make_plot()

    summary = {
        "phase": 77,
        "paper": "ITU and Free Will",
        "description": "Ethics, criminal law, ITU K_self-based justice",
        "mens_rea_K_mapping": {
            level: {"K_self_min": d["K_self_min"],
                    "sentencing_factor": d["sentencing_factor"]}
            for level, d in MENS_REA_LEVELS.items()
        },
        "international_recidivism": COUNTRIES_JUSTICE,
        "intervention_pareto": {
            name: {"cost_USD_K": d["cost"],
                    "recidivism_reduction_pct": d["recid_reduction_pct"],
                    "tier": d["tier"]}
            for name, d in INTERVENTIONS.items()
        },
        "death_penalty_homicide": {
            "death_penalty_avg_homicide": float(np.mean(dp_yes)),
            "abolition_avg_homicide": float(np.mean(dp_no)),
            "deterrence_evidence": "No correlation observed",
        },
        "ITU_proposal": "K_self degree-based justice system: "
                         "<0.10 -> treatment, 0.10-0.40 -> reduced + treatment, "
                         ">0.40 -> standard punishment with rehabilitation.",
        "central_thesis": "Classical criminal law assumes binary guilt under "
                          "full free will. ITU replaces with continuous "
                          "K_self degree, requiring multi-axis (treatment + "
                          "rehabilitation + restoration) intervention. "
                          "Rehabilitative justice (Norway 20% recid) "
                          "outperforms punitive (USA 76%) by 4x.",
        "honest_framing": "Pass-1 interpretive paper. Reframes M'Naghten, "
                          "Model Penal Code, Sapolsky 2023, restorative "
                          "justice in ITU. Numerical data from BJS, "
                          "Eurostat, country reports.",
        "tier": 1,
        "paper_number": 9,
        "next_phase": "Phase 78: AI free will + ITU roadmap + 10 predictions",
        "caveats": [
            "Mens rea K-self thresholds are illustrative ITU proposals",
            "Recidivism rates differ by definition between countries",
            "Death-penalty / homicide correlation is sociologically complex",
            "Norway success may not transfer to all cultural contexts",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase77.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 77] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 77 complete.")
    print(f"  - K_self degree-based 4-tier justice proposed")
    print(f"  - Norway 20% vs USA 76% recidivism (4× gap)")
    print(f"  - Best intervention: Education (5K → -40%)")
    print(f"  - Death penalty does NOT lower homicide")
    print("=" * 60)


if __name__ == "__main__":
    main()
