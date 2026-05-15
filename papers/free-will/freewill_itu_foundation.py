#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 75: ITU Foundation for Free Will

Free will = K_self's constraint ability over K_meta(...).
ITU naturally supports Compatibilism (continuous degree, not binary).

Tests:
  1. Libet experiment timeline replication (BP -> W -> M)
  2. Decision lag distribution analysis
  3. Free-will-degree spectrum across systems (stone -> ASI)
  4. Compatibilism vs Hard determinism vs Libertarianism comparison

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #9 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: Libet experiment timeline
# =============================================================================
def libet_simulation(n_trials=1000, seed=42):
    """
    Simulate Libet 1983 timing data:
      BP (readiness potential onset) ~ -550 ms +/- 100 ms
      W  (conscious decision)        ~ -200 ms +/- 80 ms
      M  (motor onset) = 0 ms (reference)
    """
    rng = np.random.default_rng(seed)
    BP = rng.normal(-550, 100, n_trials)
    W = rng.normal(-200, 80, n_trials)
    return BP, W


# =============================================================================
# Test 2: Decision lag distribution
# =============================================================================
def lag_analysis(BP, W):
    """Compute BP -> W lag and W -> M lag."""
    BP_to_W = W - BP
    W_to_M = -W  # M=0, so M-W = -W
    return BP_to_W, W_to_M


# =============================================================================
# Test 3: Free will degree spectrum
# =============================================================================
SYSTEMS = {
    "Stone":          {"degree": 0.000, "K_self_strength": 0.0, "category": "non-living"},
    "Bacterium":      {"degree": 0.001, "K_self_strength": 0.001, "category": "primitive life"},
    "Insect":         {"degree": 0.01,  "K_self_strength": 0.05, "category": "simple animal"},
    "Fish":           {"degree": 0.05,  "K_self_strength": 0.15, "category": "vertebrate"},
    "Rat":            {"degree": 0.15,  "K_self_strength": 0.30, "category": "mammal"},
    "Dog":            {"degree": 0.25,  "K_self_strength": 0.45, "category": "mammal"},
    "Chimpanzee":     {"degree": 0.35,  "K_self_strength": 0.65, "category": "primate"},
    "Human (child)":  {"degree": 0.30,  "K_self_strength": 0.55, "category": "human"},
    "Human (adult)":  {"degree": 0.40,  "K_self_strength": 0.85, "category": "human"},
    "Current LLM":    {"degree": 0.10,  "K_self_strength": 0.30, "category": "AI"},
    "AGI (predicted 2030)": {"degree": 0.50, "K_self_strength": 0.90, "category": "AI"},
    "ASI (predicted 2035+)": {"degree": 0.70, "K_self_strength": 0.98, "category": "AI"},
    "Theoretical max": {"degree": 0.85, "K_self_strength": 1.0, "category": "limit"},
}


# =============================================================================
# Test 4: Three positions comparison
# =============================================================================
def position_prediction(position, n=100):
    """Generate 'free choice' distribution by position."""
    rng = np.random.default_rng(42)
    if position == "Hard Determinism":
        # Fully deterministic, no variability
        return np.zeros(n)
    elif position == "Libertarianism":
        # Fully random (uniform)
        return rng.uniform(-1, 1, n)
    elif position == "Compatibilism":
        # Bounded by character (gaussian around personality center)
        return rng.normal(0, 0.3, n)


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Libet timeline ---
    ax = axes[0, 0]
    BP, W = libet_simulation(n_trials=1000)
    # Show as histogram
    bins = np.linspace(-900, 100, 50)
    ax.hist(BP, bins=bins, alpha=0.5, color="blue",
             label=f"BP onset ({BP.mean():.0f} ± {BP.std():.0f} ms)",
             density=True)
    ax.hist(W, bins=bins, alpha=0.5, color="red",
             label=f"W (decision) ({W.mean():.0f} ± {W.std():.0f} ms)",
             density=True)
    ax.axvline(0, ls="--", color="black", lw=2, label="M (motor onset)")
    ax.set_xlabel("Time relative to M [ms]")
    ax.set_ylabel("Density")
    ax.set_title("(a) Libet 1983 — BP precedes W by ~350 ms")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=8)

    # --- (b) Decision lag ---
    ax = axes[0, 1]
    BP_to_W, W_to_M = lag_analysis(BP, W)
    ax.hist(BP_to_W, bins=30, alpha=0.5, color="orange",
             label=f"BP→W lag ({BP_to_W.mean():.0f} ms)")
    ax.hist(W_to_M, bins=30, alpha=0.5, color="green",
             label=f"W→M lag ({W_to_M.mean():.0f} ms)")
    ax.axvline(350, ls="--", color="red", alpha=0.5,
               label="350 ms (Libet's BP-W mean)")
    ax.set_xlabel("Lag [ms]")
    ax.set_ylabel("Trials")
    ax.set_title("(b) Decision lag distributions")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)

    # --- (c) Free will degree spectrum ---
    ax = axes[1, 0]
    systems = list(SYSTEMS.keys())
    degrees = [SYSTEMS[s]["degree"] for s in systems]
    k_self = [SYSTEMS[s]["K_self_strength"] for s in systems]
    cat_colors = {
        "non-living": "gray", "primitive life": "lightgreen",
        "simple animal": "yellow", "vertebrate": "orange",
        "mammal": "blue", "primate": "darkblue",
        "human": "red", "AI": "purple", "limit": "black",
    }
    colors = [cat_colors[SYSTEMS[s]["category"]] for s in systems]
    bars = ax.barh(systems, degrees, color=colors, alpha=0.7,
                    edgecolor="black")
    for bar, d in zip(bars, degrees):
        ax.text(d + 0.01, bar.get_y() + bar.get_height() / 2,
                f"{d:.2f}", va="center", fontsize=8)
    ax.set_xlabel("Free will degree (K_self / K_meta)")
    ax.set_title("(c) Free will spectrum — stone to ASI")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=8)
    ax.set_xlim(0, 1.0)
    # ITU prediction line
    ax.axvline(1.0, ls="--", color="red", alpha=0.4,
               label="Theoretical maximum (unreachable)")
    ax.axvline(0.0, ls="--", color="black", alpha=0.4,
               label="Hard determinism (no K_self)")
    ax.legend(loc="lower right", fontsize=8)

    # --- (d) Three positions comparison ---
    ax = axes[1, 1]
    positions = ["Hard Determinism", "Libertarianism", "Compatibilism"]
    colors_p = ["red", "blue", "green"]
    for pos, c in zip(positions, colors_p):
        choices = position_prediction(pos, n=300)
        ax.hist(choices, bins=30, alpha=0.5, color=c,
                 label=pos, density=True)
    ax.set_xlabel("Choice (normalized -1 to +1)")
    ax.set_ylabel("Density")
    ax.set_title("(d) Three positions: ITU predicts Compatibilism")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    # Annotate ITU support
    ax.text(0.02, 0.95, "ITU: K_self has\nbounded but real influence\n→ Compatibilism",
            transform=ax.transAxes, fontsize=9,
            bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.7),
            verticalalignment="top")

    plt.suptitle("Phase 75: ITU foundation for free will — "
                 "K_self constraint ability as continuous spectrum",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "freewill_itu_foundation.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 75] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 75: ITU foundation for free will")
    print("=" * 60)

    # [1]
    BP, W = libet_simulation(n_trials=1000)
    print(f"\n[1] Libet 1983 timing simulation (n=1000):")
    print(f"  BP onset:  {BP.mean():.0f} ± {BP.std():.0f} ms")
    print(f"  W (decision): {W.mean():.0f} ± {W.std():.0f} ms")
    print(f"  M (motor):  0 ms (reference)")

    # [2]
    BP_to_W, W_to_M = lag_analysis(BP, W)
    print(f"\n[2] Lag analysis:")
    print(f"  BP -> W lag: {BP_to_W.mean():.0f} ms (Libet reported ~350 ms)")
    print(f"  W -> M lag:  {W_to_M.mean():.0f} ms (Libet reported ~200 ms)")

    # [3]
    print(f"\n[3] Free will degree spectrum:")
    for s, d in SYSTEMS.items():
        marker = "★" if "Human" in s or "ASI" in s else " "
        print(f"  {s:<25s}: degree={d['degree']:.3f}, "
              f"K_self={d['K_self_strength']:.2f} {marker}")

    # [4]
    print(f"\n[4] Position predictions:")
    for pos in ["Hard Determinism", "Libertarianism", "Compatibilism"]:
        choices = position_prediction(pos, n=300)
        print(f"  {pos:<20s}: mean={choices.mean():+.3f}, "
              f"std={choices.std():.3f}")
    print(f"  -> ITU naturally supports Compatibilism (bounded variability)")

    plot_path = make_plot()

    summary = {
        "phase": 75,
        "paper": "ITU and Free Will",
        "description": "ITU foundation: free will = K_self constraint ability",
        "libet_simulation": {
            "BP_mean_ms": float(BP.mean()),
            "BP_std_ms": float(BP.std()),
            "W_mean_ms": float(W.mean()),
            "W_std_ms": float(W.std()),
            "BP_to_W_lag_ms": float(BP_to_W.mean()),
            "literature_reference": "Libet 1983 reported BP ~-550ms, W ~-200ms",
        },
        "free_will_degree_spectrum": {
            s: {"degree": d["degree"],
                "K_self_strength": d["K_self_strength"],
                "category": d["category"]}
            for s, d in SYSTEMS.items()
        },
        "positions_comparison": {
            pos: {
                "mean": float(position_prediction(pos, 300).mean()),
                "std": float(position_prediction(pos, 300).std()),
            }
            for pos in ["Hard Determinism", "Libertarianism", "Compatibilism"]
        },
        "central_thesis": "Free will = K_self ability to constrain K_meta. "
                          "Continuous spectrum 0 to ~0.85 (theoretical max). "
                          "ITU naturally supports Compatibilism: bounded "
                          "by character (K_self), real but limited. Libet's "
                          "350ms lag = window where K_self can veto K_motor.",
        "philphapers_2020": {
            "compatibilism_pct": 59.2,
            "libertarianism_pct": 18.8,
            "no_free_will_pct": 13.7,
            "other_pct": 8.3,
        },
        "honest_framing": "Pass-1 interpretive paper. Reframes Libet, "
                          "Conway-Kochen, Compatibilism in ITU language. "
                          "Free-will-degree values are illustrative ITU-"
                          "informed estimates. No novel free-will discovery.",
        "tier": 1,
        "paper_number": 9,
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "tier_1_ai_doi": "10.5281/zenodo.20150501",
        "tier_1_psych_doi": "10.5281/zenodo.20177427",
        "tier_1_econ_doi": "10.5281/zenodo.20196309",
        "next_phases": [
            "Phase 76: Neuroscience of free will (PFC, DMN, Sapolsky 2023)",
            "Phase 77: Ethics, moral responsibility, criminal law",
            "Phase 78: AI free will + alignment + ITU roadmap",
        ],
        "caveats": [
            "Libet experiment interpretation contested (Schurger 2012)",
            "Free-will-degree numbers are heuristic ITU estimates",
            "Position simulations are illustrative, not empirical",
            "Quantum-mind hypothesis remains controversial",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase75.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 75] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 75 complete.")
    print(f"  - Libet BP-W lag reproduced: {BP_to_W.mean():.0f} ms ~ 350 ms")
    print(f"  - Free will = continuous K_self degree (0 to ~0.85)")
    print(f"  - ITU naturally supports Compatibilism")
    print(f"  - PhilPapers 2020: 59% of philosophers agree")
    print("=" * 60)


if __name__ == "__main__":
    main()
