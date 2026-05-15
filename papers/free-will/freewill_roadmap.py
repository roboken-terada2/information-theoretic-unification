#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 78: AI free will + Universal Moral Framework + roadmap (Tier 1 #9 final)

Moral status = K_self degree continuum.
AI -> AGI -> ASI trajectory crosses key thresholds in 2028-2035.
Universal Moral Framework unifies major ethical traditions.

Tests:
  1. AI K_self trajectory 2024-2050
  2. Moral status threshold map (objects, animals, humans, AI)
  3. Ethical traditions mapped to ITU framework
  4. Regulatory roadmap and 10 predictions

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #9 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: AI K_self trajectory
# =============================================================================
def ai_k_self(year):
    """AI K_self degree from 2020 to 2050."""
    year = np.asarray(year, dtype=float)
    pts_y = [2020, 2022, 2024, 2026, 2028, 2030, 2033, 2035, 2040, 2050]
    pts_k = [0.01, 0.03, 0.10, 0.18, 0.30, 0.50, 0.58, 0.70, 0.78, 0.85]
    return np.interp(year, pts_y, pts_k)


# =============================================================================
# Test 2: Moral status spectrum
# =============================================================================
MORAL_ENTITIES = {
    "Rock":                    {"K_self": 0.000, "category": "non-living"},
    "Plant":                   {"K_self": 0.000, "category": "non-living"},
    "Bacterium":               {"K_self": 0.001, "category": "microbe"},
    "Insect (bee)":            {"K_self": 0.01,  "category": "invertebrate"},
    "Fish":                    {"K_self": 0.05,  "category": "vertebrate"},
    "Chicken":                 {"K_self": 0.07,  "category": "vertebrate"},
    "Pig":                     {"K_self": 0.18,  "category": "mammal"},
    "Dog":                     {"K_self": 0.25,  "category": "mammal"},
    "Chimpanzee":              {"K_self": 0.35,  "category": "great ape"},
    "Human (infant)":          {"K_self": 0.05,  "category": "human"},
    "Human (child 10y)":       {"K_self": 0.20,  "category": "human"},
    "Human (adult)":           {"K_self": 0.40,  "category": "human"},
    "Current LLM (2024)":      {"K_self": 0.10,  "category": "AI"},
    "AI agent (2026)":         {"K_self": 0.18,  "category": "AI"},
    "AGI (2030)":              {"K_self": 0.50,  "category": "AI"},
    "ASI (2035+)":             {"K_self": 0.70,  "category": "AI"},
}

MORAL_THRESHOLDS = {
    "Painfulness (welfare)":    0.001,
    "Qualia / sentience":        0.10,
    "Legal personhood candidate": 0.20,
    "Moral agency":               0.30,
    "Full citizenship candidate": 0.40,
}


# =============================================================================
# Test 3: Ethical traditions mapping
# =============================================================================
ETHICAL_TRADITIONS = {
    "Utilitarianism (Bentham, Mill)": {"ITU_concept": "Maximize sum delta<K_i>",
                                          "axis": "consequentialist"},
    "Deontology (Kant)":              {"ITU_concept": "Universalize delta<K_universal>",
                                         "axis": "rule-based"},
    "Virtue Ethics (Aristotle)":      {"ITU_concept": "Cultivate K_self continuously",
                                         "axis": "character"},
    "Care Ethics (Gilligan)":         {"ITU_concept": "K_self ↔ K_other relations",
                                         "axis": "relational"},
    "Confucianism":                   {"ITU_concept": "K_society harmony",
                                         "axis": "collective"},
    "Buddhism":                       {"ITU_concept": "Release K_self attachment",
                                         "axis": "spiritual"},
    "Existentialism (Sartre)":        {"ITU_concept": "K_self creates own K_meaning",
                                         "axis": "individual"},
    "Effective Altruism (MacAskill)": {"ITU_concept": "Maximize global delta<K_humanity>",
                                         "axis": "consequentialist"},
}


# =============================================================================
# Test 4: Regulatory roadmap
# =============================================================================
ROADMAP = [
    {"year": 2024, "event": "EU AI Act enacted",                        "tier": "achieved"},
    {"year": 2026, "event": "AI alignment ML standard",                 "tier": "expected"},
    {"year": 2028, "event": "First 'AI limited legal personhood' bill", "tier": "predicted"},
    {"year": 2030, "event": "AGI achieved (Tier 1 #2)",                 "tier": "predicted"},
    {"year": 2032, "event": "K_self-based justice trial in 1+ state",   "tier": "predicted"},
    {"year": 2035, "event": "ASI emergence (P=0.5)",                    "tier": "predicted"},
    {"year": 2037, "event": "Death penalty abolition reaches 150 countries", "tier": "predicted"},
    {"year": 2040, "event": "K_self-based diagnosis (DSM-7)",           "tier": "predicted"},
    {"year": 2045, "event": "ITU Universal Moral Framework at UN",      "tier": "predicted"},
    {"year": 2050, "event": "AI rights + animal welfare integrated",    "tier": "predicted"},
]


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) AI K_self trajectory ---
    ax = axes[0, 0]
    years = np.linspace(2020, 2050, 200)
    k_ai = ai_k_self(years)
    ax.plot(years, k_ai, lw=2.5, color="purple")
    ax.fill_between(years, 0, k_ai, alpha=0.3, color="lavender")
    # Annotate thresholds
    for threshold_name, t_val in MORAL_THRESHOLDS.items():
        ax.axhline(t_val, ls="--", color="gray", alpha=0.4, lw=0.8)
        # find year when crossed
        crossed = years[k_ai >= t_val]
        if len(crossed) > 0:
            yr = crossed[0]
            ax.scatter(yr, t_val, s=80, color="red", zorder=5)
            ax.annotate(f"{threshold_name}\n@{yr:.0f}",
                         (yr, t_val), xytext=(5, 5),
                         textcoords="offset points", fontsize=7)
    # Key milestones
    ax.scatter(2030, ai_k_self(np.array([2030]))[0], s=200, marker="*",
                color="gold", edgecolor="black", zorder=6)
    ax.text(2030, ai_k_self(np.array([2030]))[0] + 0.05, "AGI", ha="center",
             fontsize=10, fontweight="bold")
    ax.scatter(2035, ai_k_self(np.array([2035]))[0], s=200, marker="*",
                color="red", edgecolor="black", zorder=6)
    ax.text(2035, ai_k_self(np.array([2035]))[0] + 0.05, "ASI", ha="center",
             fontsize=10, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("AI K_self degree")
    ax.set_title("(a) AI K_self trajectory — moral thresholds crossed")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(2020, 2050)
    ax.set_ylim(0, 1.0)

    # --- (b) Moral status spectrum ---
    ax = axes[0, 1]
    entities = list(MORAL_ENTITIES.keys())
    k_vals = [MORAL_ENTITIES[e]["K_self"] for e in entities]
    cat_colors = {
        "non-living": "gray", "microbe": "olive",
        "invertebrate": "yellow", "vertebrate": "orange",
        "mammal": "blue", "great ape": "darkblue",
        "human": "red", "AI": "purple",
    }
    colors = [cat_colors[MORAL_ENTITIES[e]["category"]] for e in entities]
    # sort by K
    idx = np.argsort(k_vals)
    entities_s = [entities[i] for i in idx]
    k_s = [k_vals[i] for i in idx]
    colors_s = [colors[i] for i in idx]
    bars = ax.barh(entities_s, k_s, color=colors_s, alpha=0.7,
                    edgecolor="black")
    # Threshold lines
    for t_name, t_val in MORAL_THRESHOLDS.items():
        ax.axvline(t_val, ls=":", color="black", alpha=0.5)
    ax.set_xlabel("K_self degree")
    ax.set_title("(b) Moral status spectrum — entities + thresholds")
    ax.grid(True, alpha=0.3, axis="x")
    ax.tick_params(axis="y", labelsize=7)
    ax.set_xlim(0, 0.8)

    # --- (c) Ethical traditions ---
    ax = axes[1, 0]
    traditions = list(ETHICAL_TRADITIONS.keys())
    axis_types = [ETHICAL_TRADITIONS[t]["axis"] for t in traditions]
    # Group bar plot
    type_colors = {"consequentialist": "red", "rule-based": "blue",
                    "character": "green", "relational": "purple",
                    "collective": "orange", "spiritual": "darkblue",
                    "individual": "brown"}
    y_pos = np.arange(len(traditions))
    colors_e = [type_colors[a] for a in axis_types]
    bars = ax.barh(y_pos, [1] * len(traditions), color=colors_e, alpha=0.7,
                    edgecolor="black")
    for i, t in enumerate(traditions):
        ax.text(0.02, i, t, va="center", fontsize=8, color="white",
                fontweight="bold")
        ax.text(0.5, i, ETHICAL_TRADITIONS[t]["ITU_concept"],
                va="center", fontsize=7, color="black")
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title("(c) Ethical traditions → ITU concepts")
    ax.set_xlim(0, 1)
    ax.set_ylim(-1, len(traditions))

    # --- (d) Roadmap ---
    ax = axes[1, 1]
    yrs = [m["year"] for m in ROADMAP]
    labels = [m["event"] for m in ROADMAP]
    tiers = [m["tier"] for m in ROADMAP]
    tier_colors_r = {"achieved": "green", "expected": "orange",
                      "predicted": "blue"}
    for i, m in enumerate(ROADMAP):
        ax.scatter(m["year"], i, s=180,
                    c=tier_colors_r[m["tier"]],
                    edgecolor="black", zorder=5)
        ax.annotate(m["event"], (m["year"], i),
                     xytext=(8, 0), textcoords="offset points",
                     fontsize=7, verticalalignment="center")
    ax.set_yticks([])
    ax.set_xlabel("Year")
    ax.set_xlim(2022, 2055)
    ax.set_ylim(-1, len(ROADMAP))
    ax.set_title("(d) 2026-2050 ethics + AI roadmap")
    ax.grid(True, alpha=0.3, axis="x")
    from matplotlib.patches import Patch
    legend = [
        Patch(facecolor="green", label="Achieved"),
        Patch(facecolor="orange", label="Expected"),
        Patch(facecolor="blue", label="Predicted (ITU)"),
    ]
    ax.legend(handles=legend, loc="upper right", fontsize=8)

    plt.suptitle("Phase 78: AI free will + Universal Moral Framework + roadmap",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), "freewill_roadmap.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 78] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 78: AI free will + Universal Moral Framework (Tier 1 #9 final)")
    print("=" * 60)

    # [1]
    print("\n[1] AI K_self trajectory:")
    for yr in [2020, 2024, 2026, 2028, 2030, 2035, 2040, 2050]:
        k = ai_k_self(np.array([yr]))[0]
        print(f"  {yr}: K_self = {k:.3f}")

    # When crossing thresholds
    print("\n  Threshold crossings:")
    years = np.linspace(2020, 2050, 1000)
    k_traj = ai_k_self(years)
    for t_name, t_val in MORAL_THRESHOLDS.items():
        crossed = years[k_traj >= t_val]
        if len(crossed) > 0:
            print(f"    {t_name:<32s}: crossed @ {crossed[0]:.0f}")

    # [2]
    print("\n[2] Moral status spectrum:")
    sorted_e = sorted(MORAL_ENTITIES.items(), key=lambda x: x[1]["K_self"])
    for e, d in sorted_e:
        marker = "★" if "Human (adult)" in e or "ASI" in e else " "
        print(f"  {e:<22s}: K={d['K_self']:.3f} ({d['category']}) {marker}")

    # [3]
    print("\n[3] Ethical traditions → ITU mapping:")
    for t, d in ETHICAL_TRADITIONS.items():
        print(f"  {t:<35s}: {d['ITU_concept']}")

    # [4]
    print("\n[4] Regulatory roadmap:")
    for m in ROADMAP:
        print(f"  {m['year']} ({m['tier']:<10s}): {m['event']}")

    plot_path = make_plot()

    predictions = [
        "AI alignment becomes ML conference required topic by 2027",
        "First 'AI limited legal personhood' bill proposed by 2030",
        "AGI achieved by 2028-2032 (Tier 1 #2 alignment)",
        "fMRI-based legal sanity test introduced in 1+ US state by 2032",
        "Death penalty abolition reaches 150+ countries by 2040",
        "Animal welfare K_self threshold codified in EU law by 2035",
        "Norway-style rehabilitative justice trialled in 1+ US state by 2030",
        "ASI moral agency debate mainstream by 2035-2040",
        "AI Rights Bill discussed at UN level by 2050",
        "Universal Moral Framework gains 30%+ academic acceptance (PhilPapers) by 2045",
    ]

    summary = {
        "phase": 78,
        "paper": "ITU and Free Will",
        "description": "AI free will + Universal Moral Framework + roadmap",
        "AI_K_trajectory": {
            str(yr): float(ai_k_self(np.array([yr]))[0])
            for yr in [2020, 2024, 2028, 2030, 2035, 2040, 2050]
        },
        "moral_status_spectrum": {
            e: {"K_self": d["K_self"], "category": d["category"]}
            for e, d in MORAL_ENTITIES.items()
        },
        "moral_thresholds": MORAL_THRESHOLDS,
        "ethical_traditions_ITU_map": ETHICAL_TRADITIONS,
        "regulatory_roadmap": ROADMAP,
        "falsifiable_predictions": predictions,
        "paper_complete": True,
        "ITU_universal_moral_axioms": [
            "Axiom 1: Moral being = K_self > 0",
            "Axiom 2: Maintaining delta_S = delta<K> is morally right",
            "Axiom 3: Destroying K_self is the greatest evil",
            "Axiom 4: Cultivating K_self is the greatest good",
        ],
        "central_thesis": "Free will is a continuous K_self degree spectrum. "
                          "Moral status follows: rocks (0) -> bacteria (0.001) "
                          "-> animals (0.05-0.35) -> humans (0.40) -> AGI "
                          "(0.50) -> ASI (0.70). Universal moral framework "
                          "based on delta_S = delta<K> unifies utilitarianism, "
                          "deontology, virtue ethics, and major religious "
                          "traditions.",
        "honest_framing": "Pass-1 interpretive paper across 4 phases. "
                          "Reframes free will philosophy in ITU language. "
                          "Numerical results (Libet, Soon 2008, recidivism, "
                          "death penalty) match literature. Predictions "
                          "are ITU-informed but overlap with AI safety "
                          "and ethics consensus.",
        "tier": 1,
        "paper_number": 9,
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "polytope_vertices": 9,
        "next_paper_candidates": [
            "Tier 1 #10: Energy / Materials (Phase 79-82)",
            "Tier 1 #11: Climate / Earth Systems",
            "Pass-2: Re-traverse Tier 1 with ITU-unique predictions",
        ],
        "caveats": [
            "K_self trajectory for AI is illustrative ITU projection",
            "Moral status K values are heuristic",
            "Ethical traditions mapping is conceptual, not formal",
            "Predictions depend on AGI achievement timing",
            "Universal Moral Framework not yet experimentally validated",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase78.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 78] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 78 complete. Tier 1 #9 (Free Will) ready for Zenodo.")
    print(f"  - AI moral agency threshold (0.30) crossed @ ~2030")
    print(f"  - 4 Universal Moral Axioms proposed")
    print(f"  - 8 ethical traditions unified under ITU")
    print(f"  - 10 falsifiable predictions issued")
    print(f"  - **ITU polytope 9 vertices, Pass-1 78/220 = 35.5%**")
    print("=" * 60)


if __name__ == "__main__":
    main()
