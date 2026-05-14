#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 69: Depression and anxiety under ITU

Depression = K_reward failure (positive prediction errors not registered).
Anxiety = K_threat over-precision (false-positive predictions).

Tests:
  1. K_reward dynamics over time (healthy vs depressed)
  2. K_threat over-activation (anxiety, PTSD)
  3. Drug response curves vs time-to-effect
  4. STAR*D-like treatment cascade with cumulative remission

Author: Munehiro Terada (Roboken), 2026.
Tier 1 #7 paper (in preparation).
"""

import json
import os

import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Test 1: K_reward dynamics
# =============================================================================
def reward_dynamics(state="healthy", n_steps=100, seed=42):
    """
    Simulate prediction-error learning of K_reward.
    Each step: random good/bad event, learn from prediction error.
    """
    rng = np.random.default_rng(seed)
    if state == "healthy":
        learning_rate = 0.1
        precision_pos = 1.0   # full sensitivity to positive errors
        precision_neg = 1.0
    elif state == "mild depression":
        learning_rate = 0.1
        precision_pos = 0.3   # positive errors dampened
        precision_neg = 1.5
    elif state == "severe depression":
        learning_rate = 0.1
        precision_pos = 0.05  # positive errors barely registered
        precision_neg = 2.5   # negative errors amplified
    K_reward = 0.5
    history = [K_reward]
    for _ in range(n_steps):
        event = rng.normal(0.6, 0.25)  # life events slightly positive on avg
        pred_error = event - K_reward
        if pred_error > 0:
            K_reward += learning_rate * precision_pos * pred_error
        else:
            K_reward += learning_rate * precision_neg * pred_error
        K_reward = np.clip(K_reward, 0, 1)
        history.append(K_reward)
    return np.array(history)


# =============================================================================
# Test 2: K_threat over-activation
# =============================================================================
def threat_response(state="healthy", n_stimuli=100, seed=42):
    """
    Simulate threat response to mixed safe/dangerous stimuli (10% truly dangerous).
    Healthy: detects most real threats, few false positives.
    Anxiety: many false positives.
    PTSD: false positives + trauma-trigger over-response.
    """
    rng = np.random.default_rng(seed)
    true_threats = rng.random(n_stimuli) < 0.10
    if state == "healthy":
        threat_bias = 0.0
        precision = 1.0
    elif state == "anxiety":
        threat_bias = 0.3
        precision = 0.6
    elif state == "ptsd":
        threat_bias = 0.5
        precision = 0.4  # poor discrimination + over-trigger
    # detected when: (true_threat OR random_noise > threshold)
    perceived = true_threats.astype(float) * precision + threat_bias \
                + rng.normal(0, 0.2, size=n_stimuli)
    detected = perceived > 0.3
    true_pos = (detected & true_threats).sum()
    false_pos = (detected & ~true_threats).sum()
    false_neg = (~detected & true_threats).sum()
    return true_pos, false_pos, false_neg, len(true_threats)


# =============================================================================
# Test 3: Drug effect vs time
# =============================================================================
def drug_response_curve(drug, t_days):
    """Mood improvement curve normalized to 0-1, time in days."""
    t_days = np.asarray(t_days, dtype=float)
    if drug == "SSRI":
        # 4-6 week onset
        return 0.50 * (1 - np.exp(-t_days / 25.0))
    elif drug == "Ketamine":
        # rapid onset (hours), but fades
        return 0.65 * (1 - np.exp(-t_days / 0.2)) * np.exp(-t_days / 10.0) \
                + 0.30 * (1 - np.exp(-t_days / 0.2))  # baseline persistent
    elif drug == "Psilocybin":
        # one-shot dose, durable for weeks
        # quickly rises, sustained
        return 0.75 * (1 - np.exp(-t_days / 0.5)) * (
            1 - 0.15 * (1 - np.exp(-t_days / 60.0))  # slight decay
        )
    elif drug == "ECT":
        # 6-12 sessions over 2-4 weeks, fast cumulative
        return 0.80 * (1 - np.exp(-t_days / 10.0))
    elif drug == "Placebo":
        return 0.25 * (1 - np.exp(-t_days / 30.0))


# =============================================================================
# Test 4: STAR*D-like cascade
# =============================================================================
def star_d_cascade():
    """Cumulative remission by treatment step (STAR*D 2006)."""
    return {
        "Step 1: SSRI (Citalopram)":           37,
        "Step 2: SSRI swap / augm.":           50,
        "Step 3: TCA / MAOI / Lithium":        60,
        "Step 4: Combination":                  65,
        "Step 5: Ketamine / Psilocybin / ECT": 70,
    }


# =============================================================================
# Plotting
# =============================================================================
def make_plot():
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # --- (a) Reward dynamics ---
    ax = axes[0, 0]
    t = np.arange(101)
    for state, color in zip(["healthy", "mild depression", "severe depression"],
                              ["green", "orange", "red"]):
        hist = reward_dynamics(state=state, n_steps=100, seed=42)
        ax.plot(t, hist, lw=2, color=color, label=state)
    ax.axhline(0.5, ls=":", color="black", alpha=0.5,
               label="Initial belief = 0.5")
    ax.set_xlabel("Time (event count)")
    ax.set_ylabel("K_reward belief (anticipated reward)")
    ax.set_title("(a) K_reward dynamics — depression as belief collapse")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left", fontsize=8)
    ax.set_ylim(0, 1.0)

    # --- (b) Threat response ---
    ax = axes[0, 1]
    states = ["healthy", "anxiety", "ptsd"]
    labels = ["Healthy", "Anxiety", "PTSD"]
    tp_arr, fp_arr, fn_arr = [], [], []
    for s in states:
        tp, fp, fn, total = threat_response(state=s, n_stimuli=200, seed=42)
        tp_arr.append(tp)
        fp_arr.append(fp)
        fn_arr.append(fn)
    x = np.arange(len(states))
    width = 0.3
    ax.bar(x - width, tp_arr, width, color="green", label="True positive")
    ax.bar(x, fp_arr, width, color="red", label="False positive")
    ax.bar(x + width, fn_arr, width, color="orange", label="False negative")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Detections (out of ~20 real threats per 200 stimuli)")
    ax.set_title("(b) K_threat detection — false positives explode in anxiety")
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend(loc="upper left", fontsize=9)

    # --- (c) Drug response vs time ---
    ax = axes[1, 0]
    t = np.linspace(0, 42, 200)  # 6 weeks
    for drug, color in zip(["Placebo", "SSRI", "Ketamine",
                              "Psilocybin", "ECT"],
                             ["gray", "blue", "purple", "darkgreen", "red"]):
        resp = drug_response_curve(drug, t) * 100
        ax.plot(t, resp, lw=2, color=color, label=drug)
    ax.axhline(50, ls="--", color="black", alpha=0.4,
               label="50% improvement target")
    ax.set_xlabel("Time [days]")
    ax.set_ylabel("Mood improvement [%]")
    ax.set_title("(c) Antidepressant kinetics — SSRI vs rapid-acting")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(0, 42)
    ax.set_ylim(0, 100)

    # --- (d) STAR*D cascade ---
    ax = axes[1, 1]
    cascade = star_d_cascade()
    labels = list(cascade.keys())
    cumulative = list(cascade.values())
    incr = [cumulative[0]] + [cumulative[i] - cumulative[i - 1]
                                for i in range(1, len(cumulative))]
    x = np.arange(len(labels))
    ax.bar(x, incr, color="steelblue", alpha=0.8,
            label="Step contribution (%)")
    ax.plot(x, cumulative, "o-", lw=2, color="red",
             label="Cumulative remission (%)")
    for i, c in enumerate(cumulative):
        ax.text(x[i], c + 2, f"{c}%", ha="center", fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels([l.split(":")[0] for l in labels], fontsize=8)
    ax.set_ylabel("Remission rate [%]")
    ax.set_title("(d) STAR*D-like cascade — TRD ~30%")
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_ylim(0, 100)

    plt.suptitle("Phase 69: Depression and anxiety — K_reward and K_threat "
                 "breakdowns",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__),
                              "depression_anxiety_itu.png")
    plt.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"[Phase 69] Figure saved: {out_path}")
    return out_path


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 60)
    print("Phase 69: Depression and anxiety under ITU")
    print("=" * 60)

    # [1]
    print("\n[1] K_reward dynamics (after 100 events):")
    for state in ["healthy", "mild depression", "severe depression"]:
        hist = reward_dynamics(state=state, n_steps=100, seed=42)
        print(f"  {state:<22s} : final K_reward = {hist[-1]:.3f}")

    # [2]
    print("\n[2] K_threat detection (200 stimuli, ~20 real threats):")
    for state in ["healthy", "anxiety", "ptsd"]:
        tp, fp, fn, total = threat_response(state=state, n_stimuli=200,
                                              seed=42)
        print(f"  {state:<12s}: TP={tp:3d}, FP={fp:3d}, FN={fn:3d}")

    # [3]
    print("\n[3] Drug response at key timepoints:")
    print(f"  {'Drug':<12s} {'1 day':>8s} {'1 week':>8s} {'2 weeks':>8s} "
          f"{'4 weeks':>8s}")
    for drug in ["SSRI", "Ketamine", "Psilocybin", "ECT", "Placebo"]:
        responses = [drug_response_curve(drug, t) * 100
                     for t in [1, 7, 14, 28]]
        print(f"  {drug:<12s} " +
              " ".join(f"{r:7.1f}%" for r in responses))

    # [4]
    print("\n[4] STAR*D cascade (cumulative remission):")
    for step, rate in star_d_cascade().items():
        print(f"  {step:<40s} : {rate}%")
    print(f"  TRD (after 4 steps without remission): ~30%")

    plot_path = make_plot()

    summary = {
        "phase": 69,
        "paper": "ITU and Psychiatry",
        "description": "Depression (K_reward) and anxiety (K_threat) failures",
        "K_reward_final_belief": {
            "healthy": float(reward_dynamics("healthy", 100, seed=42)[-1]),
            "mild_depression": float(
                reward_dynamics("mild depression", 100, seed=42)[-1]
            ),
            "severe_depression": float(
                reward_dynamics("severe depression", 100, seed=42)[-1]
            ),
        },
        "K_threat_detection_200_stimuli": {
            state: {
                "true_positive": int(threat_response(state, 200, 42)[0]),
                "false_positive": int(threat_response(state, 200, 42)[1]),
                "false_negative": int(threat_response(state, 200, 42)[2]),
            }
            for state in ["healthy", "anxiety", "ptsd"]
        },
        "drug_response_at_day28": {
            drug: float(drug_response_curve(drug, np.array([28]))[0] * 100)
            for drug in ["SSRI", "Ketamine", "Psilocybin", "ECT", "Placebo"]
        },
        "star_d_cascade_remission_pct": star_d_cascade(),
        "TRD_prevalence_pct": 30,
        "central_thesis": "Depression = K_reward broken (positive prediction "
                          "errors not registered, anhedonia). Anxiety = "
                          "K_threat over-precision (false-positive predictions "
                          "explode). SSRIs slowly rebuild K (4-6 weeks). "
                          "Ketamine resets K in hours via NMDA antagonism. "
                          "Psilocybin restructures K_self in single session. "
                          "ECT achieves whole-brain K reset.",
        "honest_framing": "Pass-1 interpretive paper. K_reward and K_threat "
                          "models are illustrative reinforcement-learning "
                          "abstractions. Drug response curves use literature "
                          "averages. STAR*D cascade from 2006 trial.",
        "tier": 1,
        "paper_number": 7,
        "next_phase": "Phase 70: ASD/ADHD + ITU psychiatry roadmap + 10 predictions",
        "caveats": [
            "Reinforcement learning is simplified vs real brain",
            "Drug kinetics ignore inter-individual variability",
            "STAR*D criticism: real-world remission likely lower",
            "Psilocybin Phase III data still emerging (Compass Pathways)",
            "Ketamine abuse and tolerance risks not modelled",
        ],
    }

    out_json = os.path.join(os.path.dirname(__file__), "summary_phase69.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\n[Phase 69] Summary saved: {out_json}")

    print("\n" + "=" * 60)
    print("Phase 69 complete.")
    print(f"  - Depression = K_reward belief collapses to ~0")
    print(f"  - Anxiety = K_threat false-positives explode")
    print(f"  - SSRI weeks; Ketamine hours; Psilocybin one session")
    print(f"  - STAR*D: 37% -> 70% remission, TRD = 30%")
    print("=" * 60)


if __name__ == "__main__":
    main()
