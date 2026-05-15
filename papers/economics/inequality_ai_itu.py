#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 73: Inequality, growth, AI labor displacement under ITU

K_capital accumulation > K_labor growth creates Pareto inequality.
AI displaces "middle-class" K_skill, accelerating divergence.

Tests:
  1. Pareto distribution of wealth (top 1% share)
  2. Piketty r>g simulation over generations
  3. AI labor exposure index by occupation (OpenAI/OpenResearch 2023)
  4. UBI cost as % of GDP by country

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #8 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Pareto distribution
# =============================================================================
def simulate_wealth_pareto(n_agents=10000, n_steps=200, r_capital=0.05,
                            wage=1.0, save_rate=0.1,
                            stochastic_returns=True, seed=42):
    """
    Each agent has wealth W. Capital grows at rate r_capital (with noise).
    Wage is added each step, save_rate of wage is added to wealth.
    Higher initial heterogeneity + larger return variance + longer simulation
    produce realistic Pareto top-1% share around 30%.
    """
    rng = np.random.default_rng(seed)
    # Heterogeneous starting wealth (log-normal)
    wealth = np.exp(rng.normal(2.0, 0.4, n_agents))
    # Heterogeneous individual return rates (some people invest better)
    individual_alpha = rng.normal(r_capital, 0.010, n_agents)
    for _ in range(n_steps):
        if stochastic_returns:
            r_actual = rng.normal(individual_alpha, 0.12, n_agents)
        else:
            r_actual = individual_alpha
        wealth = wealth * (1 + r_actual)
        wealth = wealth + wage * save_rate
        wealth = np.maximum(wealth, 0.1)
    return wealth


def top_percent_share(wealth, top_pct=0.01):
    """Share of total wealth held by top X% richest."""
    sorted_w = np.sort(wealth)[::-1]
    cutoff = int(len(wealth) * top_pct)
    return sorted_w[:cutoff].sum() / wealth.sum()


# =============================================================================
# Test 2: Piketty r > g dynamics
# =============================================================================
def piketty_dynamics(n_generations=10, r=0.05, g=0.025, K0=4.0,
                       Y0=1.0, consumption_rate=0.04):
    """
    Realistic Piketty K/Y dynamics with consumption drag.
    K grows at r but consumption_rate is consumed each year.
    Effective growth = (1+r-consumption_rate) per year.
    """
    K = K0 * 1.0
    Y = Y0 * 1.0
    K_over_Y = [K / Y]
    effective_r = r - consumption_rate
    for _ in range(n_generations):
        K = K * (1 + effective_r) ** 30
        Y = Y * (1 + g) ** 30
        K_over_Y.append(K / Y)
    return K_over_Y


# =============================================================================
# Test 3: AI labor exposure (OpenAI/OpenResearch 2023)
# =============================================================================
OCCUPATIONS = {
    "Translator":              {"exposure": 76, "median_pay_K": 53,  "n_jobs_M": 0.07},
    "Web designer":            {"exposure": 67, "median_pay_K": 80,  "n_jobs_M": 0.20},
    "Legal assistant":         {"exposure": 65, "median_pay_K": 60,  "n_jobs_M": 0.34},
    "Mathematician":           {"exposure": 63, "median_pay_K": 110, "n_jobs_M": 0.003},
    "Programmer":              {"exposure": 60, "median_pay_K": 130, "n_jobs_M": 1.40},
    "Writer":                  {"exposure": 55, "median_pay_K": 72,  "n_jobs_M": 0.15},
    "Accountant":              {"exposure": 50, "median_pay_K": 78,  "n_jobs_M": 1.30},
    "Customer service":        {"exposure": 45, "median_pay_K": 39,  "n_jobs_M": 2.90},
    "Financial analyst":       {"exposure": 40, "median_pay_K": 96,  "n_jobs_M": 0.40},
    "Teacher (general)":       {"exposure": 35, "median_pay_K": 65,  "n_jobs_M": 3.60},
    "Doctor":                  {"exposure": 25, "median_pay_K": 230, "n_jobs_M": 1.00},
    "Construction worker":     {"exposure": 10, "median_pay_K": 50,  "n_jobs_M": 7.40},
    "Nurse":                   {"exposure": 5,  "median_pay_K": 78,  "n_jobs_M": 3.20},
    "Plumber":                 {"exposure": 4,  "median_pay_K": 60,  "n_jobs_M": 0.50},
}


def total_exposed_jobs():
    return sum(d["n_jobs_M"] * d["exposure"] / 100
               for d in OCCUPATIONS.values())


# =============================================================================
# Test 4: UBI cost
# =============================================================================
COUNTRIES_UBI = {
    "USA":     {"adults_M": 254, "GDP_T": 27.4, "monthly_UBI_USD": 1000},
    "Japan":   {"adults_M": 100, "GDP_T": 4.2,  "monthly_UBI_USD": 700},
    "Germany": {"adults_M": 70,  "GDP_T": 4.5,  "monthly_UBI_USD": 1000},
    "UK":      {"adults_M": 55,  "GDP_T": 3.3,  "monthly_UBI_USD": 900},
    "India":   {"adults_M": 1050, "GDP_T": 3.7, "monthly_UBI_USD": 50},
}


def ubi_cost_pct_gdp(country):
    d = COUNTRIES_UBI[country]
    annual_cost = d["adults_M"] * 1e6 * d["monthly_UBI_USD"] * 12
    annual_gdp = d["GDP_T"] * 1e12
    return annual_cost / annual_gdp * 100


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Pareto distribution ---
    ax = axes[0, 0]
    wealth = simulate_wealth_pareto(n_agents=10000, n_steps=100, seed=42)
    sorted_w = np.sort(wealth)[::-1]
    rank = np.arange(1, len(wealth) + 1)
    ax.loglog(rank / len(wealth), sorted_w, lw=2, color="darkred",
               label="Simulated wealth")
    # Power-law fit
    log_r = np.log(rank[10:1000])
    log_w = np.log(sorted_w[10:1000])
    slope, intercept = np.polyfit(log_r, log_w, 1)
    fit_w = np.exp(intercept) * (rank[5:1000] ** slope)
    ax.loglog(rank[5:1000] / len(wealth), fit_w, "--", color="black",
               label=f"Power law slope={slope:.2f}")
    ax.set_xlabel("Cumulative population (fraction)")
    ax.set_ylabel("Wealth (sorted descending)")
    ax.set_title("(a) Wealth distribution → Pareto power law")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper right")
    # Top 1%, 10% annotations
    top1 = top_percent_share(wealth, 0.01) * 100
    top10 = top_percent_share(wealth, 0.10) * 100
    ax.text(0.02, 0.05, f"Top 1% holds {top1:.1f}%\nTop 10% holds {top10:.1f}%",
            transform=ax.transAxes, fontsize=10,
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))

    # --- (b) Piketty r > g ---
    ax = axes[0, 1]
    generations = list(range(11))
    # Use net-of-consumption rates (already accounts for ~1% drag)
    K_over_Y_normal = piketty_dynamics(n_generations=10, r=0.039, g=0.025,
                                          consumption_rate=0.0)
    K_over_Y_postwar = piketty_dynamics(n_generations=10, r=0.020, g=0.040,
                                          consumption_rate=0.0)
    K_over_Y_modern = piketty_dynamics(n_generations=10, r=0.050, g=0.020,
                                         consumption_rate=0.0)
    ax.plot(generations, K_over_Y_normal, "o-", lw=2,
             color="orange", label="Normal (net r=3.9%, g=2.5%)")
    ax.plot(generations, K_over_Y_postwar, "s-", lw=2,
             color="green",
             label="Postwar (r=2%, g=4%) — levelling")
    ax.plot(generations, K_over_Y_modern, "^-", lw=2,
             color="red",
             label="Modern (r=5%, g=2%) — divergent")
    ax.set_xlabel("Generation (30 yr)")
    ax.set_ylabel("Capital/Income ratio K/Y")
    ax.set_title("(b) Piketty r > g — wealth-income divergence")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)
    ax.set_yscale("log")

    # --- (c) AI exposure by occupation ---
    ax = axes[1, 0]
    names = list(OCCUPATIONS.keys())
    exposures = [OCCUPATIONS[n]["exposure"] for n in names]
    pays = [OCCUPATIONS[n]["median_pay_K"] for n in names]
    # sort by exposure descending
    idx = np.argsort(exposures)[::-1]
    names_s = [names[i] for i in idx]
    exp_s = [exposures[i] for i in idx]
    pays_s = [pays[i] for i in idx]
    colors_e = ["darkred" if e > 50 else "orange" if e > 25 else "green"
                for e in exp_s]
    bars = ax.barh(names_s, exp_s, color=colors_e, alpha=0.7,
                    edgecolor="black")
    for bar, e, p in zip(bars, exp_s, pays_s):
        ax.text(e + 1, bar.get_y() + bar.get_height() / 2,
                f"{e}% (${p}K)",
                va="center", fontsize=7)
    ax.set_xlabel("AI exposure [%]")
    ax.set_title("(c) AI labor exposure — high-pay jobs at higher risk")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=8)

    # --- (d) UBI cost ---
    ax = axes[1, 1]
    countries = list(COUNTRIES_UBI.keys())
    costs = [ubi_cost_pct_gdp(c) for c in countries]
    monthly = [COUNTRIES_UBI[c]["monthly_UBI_USD"] for c in countries]
    colors_u = ["darkred" if cost > 15 else "orange" if cost > 10 else "green"
                for cost in costs]
    bars = ax.bar(countries, costs, color=colors_u, alpha=0.7,
                   edgecolor="black")
    for bar, c, m in zip(bars, costs, monthly):
        ax.text(bar.get_x() + bar.get_width() / 2, c + 0.5,
                f"{c:.1f}%\n(${m}/mo)", ha="center", fontsize=8)
    ax.set_ylabel("UBI annual cost [% of GDP]")
    ax.set_title("(d) UBI cost feasibility — % of GDP needed")
    ax.grid(True, alpha=0.3, axis="y")
    ax.set_ylim(0, max(costs) * 1.3)

    plt.suptitle("Phase 73: Inequality, AI labor, UBI — K-restructuring",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "inequality_ai_itu.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 73] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 73: Inequality, growth, AI labor displacement")
    print("=" * 60)

    # [1]
    wealth = simulate_wealth_pareto(n_agents=10000, n_steps=100, seed=42)
    top1 = top_percent_share(wealth, 0.01) * 100
    top10 = top_percent_share(wealth, 0.10) * 100
    print(f"\n[1] Pareto distribution after 100 steps:")
    print(f"  Top 1%  holds: {top1:.1f}% of wealth")
    print(f"  Top 10% holds: {top10:.1f}% of wealth")
    print(f"  Median wealth: {np.median(wealth):.1f}")
    print(f"  Max wealth: {wealth.max():.1f}")

    # [2]
    print("\n[2] Piketty r > g over 10 generations (300 years):")
    K_normal = piketty_dynamics(n_generations=10, r=0.039, g=0.025,
                                   consumption_rate=0.0)
    K_modern = piketty_dynamics(n_generations=10, r=0.050, g=0.020,
                                  consumption_rate=0.0)
    print(f"  Normal (net r=3.9%, g=2.5%): K/Y {K_normal[0]:.1f} -> {K_normal[-1]:.1f}")
    print(f"  Modern (net r=5.0%, g=2.0%): K/Y {K_modern[0]:.1f} -> {K_modern[-1]:.1f}")
    print(f"  Note: real-world breaks (war/tax/redistribution) cap K/Y at ~6")

    # [3]
    print("\n[3] AI labor exposure (OpenAI/OpenResearch 2023):")
    total_exposed = total_exposed_jobs()
    total_jobs = sum(d["n_jobs_M"] for d in OCCUPATIONS.values())
    print(f"  Total jobs in dataset: {total_jobs:.1f}M")
    print(f"  Weighted exposure: {total_exposed:.1f}M exposed jobs "
          f"({total_exposed/total_jobs*100:.1f}%)")
    print(f"  By occupation (top 5):")
    sorted_occ = sorted(OCCUPATIONS.items(),
                          key=lambda x: -x[1]["exposure"])[:5]
    for n, d in sorted_occ:
        print(f"    {n:<22s}: {d['exposure']}% (${d['median_pay_K']}K median pay)")

    # [4]
    print("\n[4] UBI cost as % of GDP:")
    for country in COUNTRIES_UBI:
        cost = ubi_cost_pct_gdp(country)
        d = COUNTRIES_UBI[country]
        print(f"  {country:<10s}: ${d['monthly_UBI_USD']}/mo × "
              f"{d['adults_M']}M adults = {cost:.1f}% of GDP")

    plot_path = make_plot()

    summary = {
        "phase": 73,
        "paper": "ITU and Economics",
        "description": "Inequality, growth, AI labor under ITU",
        "pareto_simulation": {
            "n_agents": 10000,
            "top_1_pct_wealth": float(top1),
            "top_10_pct_wealth": float(top10),
            "median_wealth": float(np.median(wealth)),
            "max_wealth": float(wealth.max()),
        },
        "piketty_r_vs_g": {
            "normal_K_Y_after_300yr": float(K_normal[-1]),
            "modern_K_Y_after_300yr": float(K_modern[-1]),
            "interpretation": "K accumulates faster than Y produces -> inequality",
        },
        "AI_labor_exposure": {
            "total_jobs_M": float(total_jobs),
            "weighted_exposed_jobs_M": float(total_exposed),
            "weighted_exposure_pct": float(total_exposed / total_jobs * 100),
            "occupations": {
                n: d["exposure"]
                for n, d in OCCUPATIONS.items()
            },
        },
        "UBI_cost_pct_GDP": {
            country: ubi_cost_pct_gdp(country)
            for country in COUNTRIES_UBI
        },
        "central_thesis": "Pareto distribution emerges naturally from ITU "
                          "steady state. Piketty r > g accelerates K_capital "
                          "accumulation over K_labor. AI exposure inverts "
                          "traditional risk: white-collar work now most "
                          "automatable. UBI = K_income human redistribution.",
        "honest_framing": "Pass-1 interpretive paper. Reframes Piketty, "
                          "Pareto, Romer in ITU. AI exposure data from "
                          "Eloundou 2023 (OpenAI). UBI cost calculations "
                          "are straightforward arithmetic.",
        "tier": 1,
        "paper_number": 8,
        "next_phase": "Phase 74: Economic roadmap 2026-2050 + 10 predictions",
        "caveats": [
            "Pareto simulation uses simplified savings model",
            "Piketty r and g are stylised; real values fluctuate",
            "AI exposure index is OpenAI's preliminary methodology",
            "UBI net cost depends on offsetting tax/welfare changes",
            "Country GDP figures are 2024 approximate",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase73.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 73] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 73 complete.")
    print(f"  - Top 1% wealth share (simulated): {top1:.1f}%")
    print(f"  - Piketty K/Y after 300yr (modern): {K_modern[-1]:.0f}×")
    print(f"  - AI weighted exposure: {total_exposed:.1f}M jobs / {total_jobs:.1f}M")
    print(f"  - US UBI ($1000/mo) = {ubi_cost_pct_gdp('USA'):.1f}% of GDP")
    print("=" * 60)


if __name__ == "__main__":
    main()
