#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 70: ASD/ADHD + ITU psychiatry roadmap 2026-2050 (Tier 1 #7 final)

ASD = K_social over-precision (rigid prediction model)
ADHD = K_attention precision failure (cannot filter signals)

Tests:
  1. ASD precision-weighting rigidity (sensory hypersensitivity)
  2. ADHD attention dynamics (signal vs distractor)
  3. Digital phenotyping correlations (passive data -> K estimates)
  4. 2026-2050 regulatory roadmap

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #7 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: ASD precision rigidity
# =============================================================================
def precision_response(sensory_intensity, state="healthy"):
    """
    Brain response to sensory input. Healthy: graded.
    ASD: hyper-response to low intensity (rigid precision), saturation early.
    """
    if state == "healthy":
        precision = 1.0
        gain = 0.6
    elif state == "ASD":
        precision = 2.5    # too sharp
        gain = 0.9         # over-response
    elif state == "ASD (low-prec hypothesis)":
        precision = 0.6
        gain = 0.8
    return gain * (1 - np.exp(-precision * sensory_intensity))


# =============================================================================
# Test 2: ADHD attention dynamics
# =============================================================================
def attention_dynamics(state="healthy", n_steps=200, seed=42):
    """
    Each step, brain receives signal + distractor. K_attention should
    suppress distractors. ADHD fails this.
    """
    rng = np.random.default_rng(seed)
    signal = np.zeros(n_steps)
    target_periods = (rng.random(n_steps) < 0.3).astype(float)
    distractors = rng.random(n_steps)
    if state == "healthy":
        attention_filter = 0.85
    elif state == "ADHD":
        attention_filter = 0.30
    elif state == "ADHD on stimulant":
        attention_filter = 0.70
    perceived = attention_filter * target_periods + \
                 (1 - attention_filter) * distractors
    return target_periods, perceived


# =============================================================================
# Test 3: Digital phenotyping
# =============================================================================
def digital_phenotype_data(mood_state, n_days=30, seed=42):
    """
    Simulate passive smartphone/wearable data correlating with mood.
    mood_state: "healthy" (mood ~ 0.7), "depression" (0.3), "manic" (0.9).
    """
    rng = np.random.default_rng(seed)
    if mood_state == "healthy":
        true_mood = np.full(n_days, 0.7)
    elif mood_state == "depression":
        true_mood = np.linspace(0.6, 0.2, n_days) + \
                    rng.normal(0, 0.05, n_days)
    elif mood_state == "manic":
        true_mood = np.linspace(0.5, 0.9, n_days) + \
                    rng.normal(0, 0.05, n_days)
    true_mood = np.clip(true_mood, 0, 1)
    # Derived passive signals (correlations)
    sleep_hours = 5 + 4 * true_mood + rng.normal(0, 0.3, n_days)
    sleep_hours = np.clip(sleep_hours, 3, 11)
    steps = 1000 + 7000 * true_mood + rng.normal(0, 800, n_days)
    steps = np.clip(steps, 0, 15000)
    social_msg_count = 5 + 25 * true_mood + rng.normal(0, 4, n_days)
    social_msg_count = np.clip(social_msg_count, 0, None)
    return true_mood, sleep_hours, steps, social_msg_count


# =============================================================================
# Test 4: Regulatory roadmap milestones
# =============================================================================
MILESTONES = [
    {"year": 2024, "event": "KarXT FDA approved (schizophrenia, non-D2)",  "tier": "achieved"},
    {"year": 2024, "event": "MDMA-AT FDA rejected (PTSD)",                 "tier": "achieved-neg"},
    {"year": 2025, "event": "Psilocybin TRD Phase III readout",            "tier": "expected"},
    {"year": 2026, "event": "MDMA-AT re-application",                      "tier": "expected"},
    {"year": 2027, "event": "Psilocybin FDA approval (TRD)",               "tier": "predicted"},
    {"year": 2028, "event": "Digital phenotyping SaMD approval",           "tier": "predicted"},
    {"year": 2030, "event": "K-monitoring standard in clinical practice",  "tier": "predicted"},
    {"year": 2032, "event": "FUS approved for depression/OCD",             "tier": "predicted"},
    {"year": 2035, "event": "4-axis combo standard for TRD",               "tier": "predicted"},
    {"year": 2040, "event": "DSM-6 with K-component-based diagnosis",       "tier": "predicted"},
]


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) ASD precision response ---
    ax = axes[0, 0]
    intensity = np.linspace(0, 5, 100)
    for state, color in zip(["healthy", "ASD"],
                              ["green", "red"]):
        r = precision_response(intensity, state)
        ax.plot(intensity, r, lw=2, color=color, label=state)
    ax.axhline(0.5, ls=":", color="black", alpha=0.4)
    ax.set_xlabel("Sensory intensity")
    ax.set_ylabel("Brain response (saturating)")
    ax.set_title("(a) ASD = rigid precision → sensory hyperresponse")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower right", fontsize=9)

    # --- (b) ADHD attention ---
    ax = axes[0, 1]
    np.random.seed(0)
    n_steps = 50
    states = ["healthy", "ADHD", "ADHD on stimulant"]
    colors_a = ["green", "red", "blue"]
    for state, color in zip(states, colors_a):
        targets, perceived = attention_dynamics(state, n_steps=n_steps,
                                                  seed=42)
        ax.plot(perceived, lw=1.2, color=color, label=state, alpha=0.85)
    # Show targets
    targets_only = attention_dynamics("healthy", n_steps=n_steps, seed=42)[0]
    ax.fill_between(range(n_steps), 0, targets_only, color="lightgray",
                     alpha=0.5, label="True target signal")
    ax.set_xlabel("Time step")
    ax.set_ylabel("Perceived signal")
    ax.set_title("(b) ADHD = K_attention filter failure")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    ax.set_ylim(0, 1.1)

    # --- (c) Digital phenotyping ---
    ax = axes[1, 0]
    days = np.arange(30)
    for mood_state, color in zip(["healthy", "depression", "manic"],
                                   ["green", "blue", "red"]):
        true_mood, sleep, steps, social = digital_phenotype_data(
            mood_state, n_days=30, seed=42
        )
        # Plot mood + steps normalised
        ax.plot(days, true_mood, lw=2, color=color, label=f"{mood_state} (mood)")
        ax.plot(days, steps / 10000, lw=1, ls=":", color=color, alpha=0.6)
    ax.set_xlabel("Day")
    ax.set_ylabel("Mood (solid) / steps (dotted, ÷10000)")
    ax.set_title("(c) Digital phenotyping — passive data ↔ K_mood")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left", fontsize=8)
    ax.set_ylim(0, 1.1)

    # --- (d) Regulatory roadmap ---
    ax = axes[1, 1]
    yrs = [m["year"] for m in MILESTONES]
    labels = [m["event"] for m in MILESTONES]
    colors = {
        "achieved": "green",
        "achieved-neg": "red",
        "expected": "orange",
        "predicted": "blue",
    }
    for i, m in enumerate(MILESTONES):
        ax.scatter(m["year"], i, s=180,
                    c=colors[m["tier"]], edgecolor="black", zorder=5)
        ax.annotate(m["event"], (m["year"], i),
                     xytext=(8, 0), textcoords="offset points",
                     fontsize=6, verticalalignment="center")
    ax.set_yticks([])
    ax.set_xlabel("Year")
    ax.set_xlim(2022, 2055)
    ax.set_ylim(-1, len(MILESTONES))
    ax.set_title("(d) Psychiatry regulatory roadmap — ITU prediction")
    ax.grid(True, alpha=0.3, axis="x")
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="green", label="Achieved (positive)"),
        Patch(facecolor="red", label="Achieved (rejection)"),
        Patch(facecolor="orange", label="Expected"),
        Patch(facecolor="blue", label="Predicted"),
    ]
    ax.legend(handles=legend_elements, loc="upper right", fontsize=7)

    plt.suptitle("Phase 70: ASD/ADHD + 2026-2050 psychiatry roadmap — "
                 "ITU Medicine Triangle complete",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "psychiatry_roadmap.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 70] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 70: ASD/ADHD + ITU psychiatry roadmap")
    print("=" * 60)

    # [1]
    print("\n[1] ASD precision response (sensory intensity = 1.0):")
    for state in ["healthy", "ASD"]:
        r = precision_response(1.0, state)
        print(f"  {state:<25s}: response = {r:.3f}")

    # [2]
    print("\n[2] ADHD attention filter (mean of 200 steps):")
    for state in ["healthy", "ADHD", "ADHD on stimulant"]:
        targets, perceived = attention_dynamics(state, n_steps=200, seed=42)
        # signal-to-distractor ratio
        signal_when_target = perceived[targets > 0.5].mean()
        signal_when_no = perceived[targets <= 0.5].mean()
        snr = signal_when_target / signal_when_no
        print(f"  {state:<25s}: SNR = {snr:.2f}")

    # [3]
    print("\n[3] Digital phenotyping correlations (30-day average):")
    for mood_state in ["healthy", "depression", "manic"]:
        m, s, st, soc = digital_phenotype_data(mood_state, n_days=30, seed=42)
        print(f"  {mood_state:<12s}: mood={m.mean():.2f}, "
              f"sleep={s.mean():.1f}h, steps={st.mean():.0f}, "
              f"social_msg={soc.mean():.1f}/day")

    # [4]
    print("\n[4] Regulatory milestones:")
    for m in MILESTONES:
        print(f"  {m['year']} ({m['tier']:<14s}): {m['event']}")

    plot_path = make_plot()

    predictions = [
        "Psilocybin approved by FDA for TRD by 2027",
        "MDMA-AT (re-applied) approved by FDA for PTSD by 2026",
        "Focused ultrasound approved for depression/OCD by 2028",
        "KarXT becomes first-line schizophrenia treatment by 2030",
        "Digital phenotyping app receives FDA SaMD by 2028",
        "Apple Watch standard depression-screening by 2030",
        "ASD retinal/MRI biomarker by 2030",
        "TRD remission rate reaches 85% by 2035",
        "ADHD over-diagnosis prompts criteria tightening by 2030",
        "DSM-6 introduces K-component-based diagnosis by 2040",
    ]

    summary = {
        "phase": 70,
        "paper": "ITU and Psychiatry",
        "description": "ASD/ADHD + roadmap 2026-2050 (Tier 1 #7 final)",
        "ASD_K_profile": {
            "K_social_precision": 2.5,
            "K_perception_precision": 2.5,
            "interpretation": "K is rigidly over-precise; cannot integrate context",
        },
        "ADHD_K_profile": {
            "K_attention_filter": 0.30,
            "K_attention_with_stimulant": 0.70,
            "interpretation": "K_attention cannot suppress distractors without stimulant",
        },
        "digital_phenotyping_examples": {
            mood_state: {
                "30day_mood_mean": float(
                    digital_phenotype_data(mood_state, 30, 42)[0].mean()),
                "30day_sleep_mean_hr": float(
                    digital_phenotype_data(mood_state, 30, 42)[1].mean()),
                "30day_steps_mean": float(
                    digital_phenotype_data(mood_state, 30, 42)[2].mean()),
            }
            for mood_state in ["healthy", "depression", "manic"]
        },
        "regulatory_roadmap": MILESTONES,
        "falsifiable_predictions": predictions,
        "paper_complete": True,
        "central_thesis": "ASD = K_social rigid over-precision. "
                          "ADHD = K_attention precision failure (filter "
                          "broken). Digital phenotyping (Apple Watch + AI) "
                          "enables continuous K monitoring. Psychiatry "
                          "moves toward 4-axis combination: drugs + therapy "
                          "+ digital + brain stimulation. By 2040, DSM-6 "
                          "may adopt K-component-based diagnosis.",
        "honest_framing": "Pass-1 interpretive paper across 4 phases. "
                          "Reframes psychotic, mood, anxiety, ASD, and ADHD "
                          "disorders in ITU FEP language. Drug response and "
                          "diagnostic statistics from peer-reviewed sources. "
                          "Predictions overlap with industry consensus.",
        "tier": 1,
        "paper_number": 7,
        "tier_0_concept_doi": "10.5281/zenodo.20109210",
        "tier_1_qc_doi": "10.5281/zenodo.20139391",
        "tier_1_ai_doi": "10.5281/zenodo.20150501",
        "tier_1_crypto_doi": "10.5281/zenodo.20151059",
        "tier_1_semi_doi": "10.5281/zenodo.20174036",
        "tier_1_cancer_doi": "10.5281/zenodo.20174318",
        "tier_1_aging_doi": "10.5281/zenodo.20175663",
        "medicine_triangle_complete": True,
        "engineering_rectangle_complete": True,
        "next_paper_candidates": [
            "Tier 1 #8: Economics / Information Markets",
            "Tier 1 #9: Free Will (revisited)",
            "Pass-2: Re-traverse Tier 1 #1-#7 with ITU-unique predictions",
        ],
        "caveats": [
            "ASD/ADHD K models are illustrative",
            "Digital phenotyping correlations are simulated",
            "Roadmap predictions depend on TAME, KarXT, psilocybin outcomes",
            "Real-world FDA approval timelines uncertain",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase70.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 70] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 70 complete. Tier 1 #7 (Psychiatry) ready for Zenodo.")
    print("  - ASD = K_social rigid over-precision")
    print("  - ADHD = K_attention filter failure")
    print("  - Digital phenotyping = continuous K-monitoring")
    print("  - 10 falsifiable predictions issued")
    print("  - **ITU Medicine Triangle COMPLETE (Cancer + Aging + Psychiatry)**")
    print("=" * 60)


if __name__ == "__main__":
    main()
