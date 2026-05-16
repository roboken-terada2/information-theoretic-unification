#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 71: ITU Foundation for Economics

Markets are collective Bayesian inference engines.
Price = <K_market>, volatility = 1/precision.
Information asymmetry, behavioral biases, prediction markets analyzed
in ITU framework.

Tests:
  1. EMH (Gaussian) vs realistic fat-tailed returns
  2. Akerlof lemons-market collapse simulation
  3. Prospect theory vs expected utility (loss aversion)
  4. Prediction-market accuracy vs polls (2024 US election)

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #8 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: EMH vs realistic returns distribution
# =============================================================================
def emh_returns(n=10000, seed=42):
    """Pure Gaussian: EMH prediction."""
    rng = np.random.default_rng(seed)
    return rng.normal(0, 0.01, n)


def realistic_returns(n=10000, seed=42):
    """Fat-tailed returns (Student-t with low df, mimicking real markets)."""
    rng = np.random.default_rng(seed)
    df = 3
    return rng.standard_t(df, n) * 0.006


# =============================================================================
# Test 2: Akerlof lemons market collapse
# =============================================================================
def akerlof_simulation(n_sellers=1000, n_buyers=1000, n_iterations=20,
                        seed=42):
    """
    Sellers have private quality q ~ Uniform(0, 1).
    Buyers pay average expected quality.
    High-quality sellers withdraw if price < their q.
    Repeat -> market unravels.
    """
    rng = np.random.default_rng(seed)
    qualities = rng.uniform(0, 1, n_sellers)
    history = []
    for iteration in range(n_iterations):
        if len(qualities) == 0:
            history.append({
                "iteration": iteration,
                "avg_quality": 0,
                "n_sellers": 0,
                "price": 0,
            })
            continue
        avg_q = float(qualities.mean())
        price = avg_q  # buyer pays expected quality
        history.append({
            "iteration": iteration,
            "avg_quality": avg_q,
            "n_sellers": int(len(qualities)),
            "price": price,
        })
        # Sellers withdraw if their quality > price
        qualities = qualities[qualities <= price]
    return history


# =============================================================================
# Test 3: Prospect theory vs expected utility
# =============================================================================
def expected_utility(x, lam=2.0):
    """Standard risk-averse utility u(x) = sign(x) * sqrt(|x|)."""
    return np.sign(x) * np.sqrt(np.abs(x))


def prospect_value(x, alpha=0.88, lam=2.25):
    """Kahneman-Tversky prospect value function.
    v(x) = x^alpha   if x >= 0
         = -lam * (-x)^alpha   if x < 0  (loss aversion).
    """
    x = np.asarray(x, dtype=float)
    pos_mask = x >= 0
    v = np.zeros_like(x)
    v[pos_mask] = np.abs(x[pos_mask]) ** alpha
    v[~pos_mask] = -lam * np.abs(x[~pos_mask]) ** alpha
    return v


# =============================================================================
# Test 4: Prediction market accuracy
# =============================================================================
PRED_MARKETS_2024 = {
    "Polymarket (Oct 28)":    {"Trump_prob": 0.60, "outcome": "Trump",
                                 "error": 0.40},  # 60% prob => 40% error if right
    "Kalshi":                  {"Trump_prob": 0.55, "outcome": "Trump",
                                 "error": 0.45},
    "Manifold":                {"Trump_prob": 0.56, "outcome": "Trump",
                                 "error": 0.44},
    "538 polls average":       {"Trump_prob": 0.50, "outcome": "Trump",
                                 "error": 0.50},
    "Selzer poll (last)":      {"Trump_prob": 0.40, "outcome": "Trump",
                                 "error": 0.60},  # wrong direction
    "Pundit aggregate":        {"Trump_prob": 0.45, "outcome": "Trump",
                                 "error": 0.55},
}


def market_brier_score(prob, outcome_won):
    """Brier score: (prob - outcome)^2. Lower is better."""
    return (prob - (1.0 if outcome_won else 0.0)) ** 2


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) EMH vs fat tails ---
    ax = axes[0, 0]
    emh = emh_returns(n=10000)
    real = realistic_returns(n=10000)
    bins = np.linspace(-0.05, 0.05, 60)
    ax.hist(emh, bins=bins, alpha=0.5, color="blue",
             label="EMH (Gaussian)", density=True)
    ax.hist(real, bins=bins, alpha=0.5, color="red",
             label="Real-world (fat tails)", density=True)
    ax.set_xlabel("Daily return")
    ax.set_ylabel("Density")
    ax.set_title("(a) EMH vs reality — fat tails everywhere")
    ax.set_yscale("log")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(loc="upper right")
    # Extreme event probabilities
    p_emh_extreme = (np.abs(emh) > 0.03).mean()
    p_real_extreme = (np.abs(real) > 0.03).mean()
    ax.text(0.02, 0.95, f"P(|r|>3%)\nEMH: {p_emh_extreme*100:.2f}%\n"
            f"Real: {p_real_extreme*100:.2f}%",
            transform=ax.transAxes, fontsize=9,
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
            verticalalignment="top")

    # --- (b) Akerlof lemons collapse ---
    ax = axes[0, 1]
    history = akerlof_simulation(n_sellers=1000, n_iterations=20, seed=42)
    iters = [h["iteration"] for h in history]
    avg_q = [h["avg_quality"] for h in history]
    n_sell = [h["n_sellers"] for h in history]
    prices = [h["price"] for h in history]
    ax.plot(iters, avg_q, "o-", color="blue", lw=2, label="Avg quality")
    ax.plot(iters, prices, "s-", color="green", lw=2, label="Price")
    ax2 = ax.twinx()
    ax2.plot(iters, n_sell, "^-", color="red", lw=2, label="Sellers remaining")
    ax2.set_ylabel("Number of sellers", color="red")
    ax.set_xlabel("Iteration (trading round)")
    ax.set_ylabel("Quality / price", color="blue")
    ax.set_title("(b) Akerlof lemons — adverse selection collapse")
    ax.grid(True, alpha=0.3)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="center right", fontsize=8)

    # --- (c) Prospect vs expected utility ---
    ax = axes[1, 0]
    x = np.linspace(-2, 2, 200)
    eu = expected_utility(x)
    pt = prospect_value(x)
    ax.plot(x, eu, lw=2, color="blue", label="Expected utility (sqrt)")
    ax.plot(x, pt, lw=2, color="red", label="Prospect theory (KT 1979)")
    ax.axhline(0, ls="-", color="black", alpha=0.5)
    ax.axvline(0, ls="-", color="black", alpha=0.5)
    # Loss aversion arrow
    ax.annotate("Loss aversion\nlam=2.25",
                 xy=(-1, prospect_value(np.array([-1]))[0]),
                 xytext=(-1.8, -2.5),
                 arrowprops=dict(arrowstyle="->", color="red"),
                 fontsize=9, color="red")
    ax.set_xlabel("Outcome (gain/loss)")
    ax.set_ylabel("Subjective value")
    ax.set_title("(c) Prospect theory: K_decision is asymmetric")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")

    # --- (d) Prediction market accuracy ---
    ax = axes[1, 1]
    sources = list(PRED_MARKETS_2024.keys())
    briers = [market_brier_score(d["Trump_prob"], True)
              for d in PRED_MARKETS_2024.values()]
    colors = ["green" if "market" in s.lower() or "Polymarket" in s or
              "Kalshi" in s or "Manifold" in s
              else "red" for s in sources]
    bars = ax.bar(sources, briers, color=colors, alpha=0.7, edgecolor="black")
    for bar, b in zip(bars, briers):
        ax.text(bar.get_x() + bar.get_width() / 2, b + 0.005,
                f"{b:.2f}", ha="center", fontsize=9)
    ax.set_ylabel("Brier score (lower = better)")
    ax.set_title("(d) Prediction markets vs polls — 2024 US election")
    ax.grid(True, alpha=0.3, axis="y")
    ax.tick_params(axis="x", labelsize=7, rotation=20)
    # Custom legend
    from matplotlib.patches import Patch
    legend = [
        Patch(facecolor="green", label="Prediction market"),
        Patch(facecolor="red", label="Poll / pundit"),
    ]
    ax.legend(handles=legend, loc="upper left", fontsize=8)

    plt.suptitle("Phase 71: ITU foundation for economics — markets as "
                 "collective inference engines",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "economics_itu_foundation.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 71] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 71: ITU foundation for economics")
    print("=" * 60)

    # [1]
    print("\n[1] EMH vs realistic returns:")
    emh = emh_returns(10000)
    real = realistic_returns(10000)
    print(f"  EMH P(|r|>3%): {(np.abs(emh) > 0.03).mean()*100:.3f}%")
    print(f"  Real P(|r|>3%): {(np.abs(real) > 0.03).mean()*100:.3f}%")
    print(f"  Real / EMH extreme ratio: "
          f"{(np.abs(real) > 0.03).mean() / max((np.abs(emh) > 0.03).mean(), 1e-6):.0f}×")

    # [2]
    print("\n[2] Akerlof lemons market collapse:")
    hist = akerlof_simulation(n_sellers=1000, n_iterations=20, seed=42)
    for i, h in enumerate(hist):
        if i in [0, 1, 2, 5, 10, 19]:
            print(f"  iter {h['iteration']:2d}: avg_q={h['avg_quality']:.3f}, "
                  f"price={h['price']:.3f}, "
                  f"sellers={h['n_sellers']:4d}")

    # [3]
    print("\n[3] Prospect theory loss aversion:")
    test_outcomes = [-1.0, -0.5, 0.5, 1.0]
    for x in test_outcomes:
        eu = expected_utility(np.array([x]))[0]
        pt = prospect_value(np.array([x]))[0]
        print(f"  Outcome {x:+.1f}: EU={eu:+.2f}, prospect={pt:+.2f}")

    # [4]
    print("\n[4] 2024 US election prediction accuracy (Brier scores):")
    for src, d in PRED_MARKETS_2024.items():
        b = market_brier_score(d["Trump_prob"], True)
        print(f"  {src:<28s}: P(Trump)={d['Trump_prob']:.2f}, "
              f"Brier={b:.3f}")

    plot_path = make_plot()

    summary = {
        "phase": 71,
        "paper": "ITU and Economics",
        "description": "ITU foundation: markets = collective Bayesian inference",
        "EMH_vs_realistic": {
            "EMH_extreme_event_pct": float((np.abs(emh) > 0.03).mean() * 100),
            "realistic_extreme_event_pct": float((np.abs(real) > 0.03).mean() * 100),
            "fat_tail_ratio": float(
                (np.abs(real) > 0.03).mean() /
                max((np.abs(emh) > 0.03).mean(), 1e-6)
            ),
        },
        "akerlof_lemons": {
            "iterations": len(hist),
            "first_iter_avg_quality": hist[0]["avg_quality"],
            "final_iter_avg_quality": hist[-1]["avg_quality"],
            "final_iter_sellers": hist[-1]["n_sellers"],
            "interpretation": "High-quality sellers progressively withdraw -> market unravels",
        },
        "prospect_theory": {
            "loss_aversion_lambda": 2.25,
            "examples": {
                f"x_{x}": {
                    "expected_utility": float(expected_utility(np.array([x]))[0]),
                    "prospect_value": float(prospect_value(np.array([x]))[0]),
                }
                for x in [-1.0, -0.5, 0.5, 1.0]
            },
        },
        "prediction_market_brier": {
            src: {
                "P_Trump": d["Trump_prob"],
                "Brier_score": market_brier_score(d["Trump_prob"], True),
            }
            for src, d in PRED_MARKETS_2024.items()
        },
        "central_thesis": "Markets are collective Bayesian inference engines "
                          "implementing ITU axiom dS = d<K> at the social "
                          "scale. EMH is the idealised case where this holds "
                          "exactly; reality shows fat tails, lemons-style "
                          "collapses, and behavioral biases. Prediction "
                          "markets (Polymarket, Kalshi) realise ITU "
                          "high-resolution collective K.",
        "honest_framing": "Pass-1 interpretive paper. Reframes Akerlof, "
                          "Fama/EMH, Kahneman-Tversky in ITU language. "
                          "Numerical models are illustrative; no novel "
                          "ITU-derived economic prediction.",
        "tier": 1,
        "paper_number": 8,
        "engineering_rectangle_complete": True,
        "medicine_triangle_complete": True,
        "social_sciences_begin": "Tier 1 #8 opens the social-sciences vector",
        "tier_0_concept_doi": "10.5281/zenodo.20109209",
        "next_phases": [
            "Phase 72: Bubbles and financial crises (dot-com, housing, crypto)",
            "Phase 73: Inequality, growth, and AI labor displacement",
            "Phase 74: ITU economic roadmap 2026-2050 and 10 predictions",
        ],
        "caveats": [
            "EMH violations are well-documented; we summarise rather than discover",
            "Akerlof model is simplified single-good setup",
            "Prospect theory parameters from Tversky-Kahneman 1992",
            "2024 election prediction-market accuracy is one example",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase71.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 71] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 71 complete.")
    print(f"  - Markets = collective ITU inference, EMH = idealised case")
    print(f"  - Fat tails reality vs EMH: ~{(np.abs(real)>0.03).mean()/(np.abs(emh)>0.03).mean()+1:.0f}x more extremes")
    print(f"  - Akerlof lemons: market shrinks {hist[0]['n_sellers']} -> {hist[-1]['n_sellers']}")
    print(f"  - Prediction markets beat polls in 2024 US election")
    print("=" * 60)


if __name__ == "__main__":
    main()
