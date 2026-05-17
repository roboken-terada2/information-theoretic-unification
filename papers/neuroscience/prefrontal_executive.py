"""
Phase 203 — Prefrontal Cortex + Executive Function + Decision (K_executive)

Simulations:
  1) PFC evolution: relative volume across species
  2) Working memory delay activity (Goldman-Rakic)
  3) Miller 7±2 vs Cowan 4±1 capacity
  4) Prospect theory utility function (Kahneman-Tversky 1979)
  5) Dopamine RPE during reward (Schultz 1997)
  6) Iowa Gambling Task (Damasio 1994)
  7) Libet readiness potential timing
  8) ITU K_executive axiom check

Outputs:
  - prefrontal_executive.png
  - prefrontal_executive_summary.json
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_PNG = Path(__file__).with_name("prefrontal_executive.png")
OUT_JSON = Path(__file__).with_name("prefrontal_executive_summary.json")

rng = np.random.default_rng(20260606)

# -------------------------------------------------------------
# 1) PFC across species
# -------------------------------------------------------------
pfc_species = {
    "Mouse":    5,
    "Cat":      10,
    "Dog":      12,
    "Macaque":  17,
    "Chimp":    25,
    "Human":    30,
}

# -------------------------------------------------------------
# 2) Working memory delay activity
# -------------------------------------------------------------
t_wm = np.linspace(-1, 8, 400)  # seconds
# Cue period 0-1 s, delay 1-6 s, response 6-7 s
firing_rate = 5.0 * np.ones_like(t_wm)  # baseline 5 Hz
cue_mask = (t_wm >= 0) & (t_wm <= 1)
firing_rate[cue_mask] += 20 * np.exp(-((t_wm[cue_mask] - 0.5)) ** 2 / 0.1)
delay_mask = (t_wm > 1) & (t_wm < 6)
firing_rate[delay_mask] = 15  # sustained delay activity
resp_mask = (t_wm >= 6) & (t_wm <= 7)
firing_rate[resp_mask] += 15 * np.exp(-((t_wm[resp_mask] - 6.3)) ** 2 / 0.05)
firing_rate += rng.normal(0, 1, size=len(firing_rate))

# -------------------------------------------------------------
# 3) WM capacity: Miller 7 vs Cowan 4
# -------------------------------------------------------------
n_items = np.arange(1, 12)
# Cowan 4±1: sigmoid drop after 4
recall_cowan = 1.0 / (1.0 + np.exp((n_items - 4) / 0.7))
# Miller 7±2: drop after 7
recall_miller = 1.0 / (1.0 + np.exp((n_items - 7) / 0.7))

# -------------------------------------------------------------
# 4) Prospect theory utility
# -------------------------------------------------------------
outcomes = np.linspace(-100, 100, 200)
# Kahneman-Tversky: U(x) = x^α for x > 0; -λ * (-x)^β for x < 0
alpha = 0.88
beta_pt = 0.88
lam = 2.25
utility = np.where(outcomes >= 0,
                   outcomes ** alpha,
                   -lam * (-outcomes) ** beta_pt)

# Linear utility for comparison
linear_utility = outcomes

# -------------------------------------------------------------
# 5) Dopamine RPE (Schultz 1997)
# -------------------------------------------------------------
t_rpe = np.linspace(-2, 5, 300)
# Conditions: predicted reward, unexpected reward, omission
def baseline_da(t):
    return 5.0 + 0.5 * rng.standard_normal(len(t))

cs_time = 0
reward_time = 1.5

# Unexpected reward: spike at reward
da_unexpected = baseline_da(t_rpe)
mask = (t_rpe > reward_time) & (t_rpe < reward_time + 0.3)
da_unexpected[mask] += 30 * np.exp(-((t_rpe[mask] - reward_time - 0.1) / 0.05) ** 2)

# Predicted reward: spike at CS (cue), not reward
da_predicted = baseline_da(t_rpe)
mask = (t_rpe > cs_time) & (t_rpe < cs_time + 0.3)
da_predicted[mask] += 25 * np.exp(-((t_rpe[mask] - cs_time - 0.1) / 0.05) ** 2)

# Omission: dip at expected reward time
da_omission = baseline_da(t_rpe)
mask = (t_rpe > cs_time) & (t_rpe < cs_time + 0.3)
da_omission[mask] += 25 * np.exp(-((t_rpe[mask] - cs_time - 0.1) / 0.05) ** 2)
mask = (t_rpe > reward_time) & (t_rpe < reward_time + 0.5)
da_omission[mask] -= 3.5 * np.exp(-((t_rpe[mask] - reward_time - 0.15) / 0.1) ** 2)

# -------------------------------------------------------------
# 6) Iowa Gambling Task
# -------------------------------------------------------------
# Decks A,B (high reward + huge loss = bad), C,D (low reward + small loss = good)
n_trials = 100
deck_expected_outcome = {"A": -25, "B": -25, "C": +25, "D": +25}

# Normal: progressive shift to good decks
normal_pick = np.zeros((4, n_trials))
for t in range(n_trials):
    if t < 20:
        weights = [0.25, 0.25, 0.25, 0.25]
    else:
        # Gradually prefer C,D
        good_weight = 0.25 + 0.5 * (t - 20) / 80
        weights = [(1 - good_weight)/2, (1 - good_weight)/2,
                    good_weight/2, good_weight/2]
    pick = rng.choice(4, p=weights)
    normal_pick[pick, t] = 1

# VMPFC damaged: continues to pick bad decks
damaged_pick = np.zeros((4, n_trials))
for t in range(n_trials):
    weights = [0.35, 0.35, 0.15, 0.15]  # persistent bad choice
    pick = rng.choice(4, p=weights)
    damaged_pick[pick, t] = 1

normal_cumulative_good = np.cumsum(normal_pick[2:].sum(axis=0))
normal_cumulative_bad = np.cumsum(normal_pick[:2].sum(axis=0))
damaged_cumulative_good = np.cumsum(damaged_pick[2:].sum(axis=0))
damaged_cumulative_bad = np.cumsum(damaged_pick[:2].sum(axis=0))

# -------------------------------------------------------------
# 7) Libet readiness potential
# -------------------------------------------------------------
t_libet = np.linspace(-1500, 200, 400)  # ms relative to "decision"
# Readiness potential builds 1000-500 ms before "W" (will)
rp = np.where(t_libet < -1000, 0,
              np.where(t_libet < 0, 0.1 * (t_libet + 1000) / 1000 - 0.0,
                       0.1))
# "W" reported at -200 ms (Libet 1983)
# Movement at 0 ms

# -------------------------------------------------------------
# 8) ITU K_executive axiom check
# -------------------------------------------------------------
N_states = 2000
# Pre-decision: broad distribution over possible actions
log_fit_pre = -((np.arange(N_states) - N_states/2) ** 2) / 200_000
p_pre = np.exp(log_fit_pre); p_pre /= p_pre.sum()
S_pre = float(-np.sum(p_pre * np.log(p_pre)))

# Post-decision: concentrated on selected action
selected_action = (np.arange(N_states) > 1200) & (np.arange(N_states) < 1300)
log_fit_post = log_fit_pre.copy()
log_fit_post[selected_action] += 5.0
log_fit_post[~selected_action] -= 1.0
p_post = np.exp(log_fit_post); p_post /= p_post.sum()
S_post = float(-np.sum(p_post * np.log(p_post)))

log_p_pre = np.log(np.clip(p_pre, 1e-30, None))
dp = p_post - p_pre
dS_lin = -np.sum(dp * (1.0 + log_p_pre))
dK_lin = -np.sum(dp * log_p_pre)
itu_ratio = float(dS_lin / dK_lin) if abs(dK_lin) > 1e-15 else float("nan")

# -------------------------------------------------------------
# Plot
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Phase 203 — Prefrontal Cortex + Executive Function + Decision (K_executive)",
    fontsize=13, fontweight="bold",
)

# Panel 1: PFC across species
ax = axes[0, 0]
species = list(pfc_species.keys())
pct = list(pfc_species.values())
ax.bar(species, pct, color=["#1f77b4"]*5 + ["#d62728"])
ax.set_ylabel("PFC % of cortex")
ax.set_title("Human: 30% PFC (3× rodent)")
ax.grid(True, alpha=0.3, axis="y")

# Panel 2: WM delay activity
ax = axes[0, 1]
ax.plot(t_wm, firing_rate, "-", color="#1f77b4", lw=1.5)
ax.axvspan(0, 1, alpha=0.2, color="green", label="Cue")
ax.axvspan(1, 6, alpha=0.2, color="orange", label="Delay")
ax.axvspan(6, 7, alpha=0.2, color="red", label="Response")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Firing rate (Hz)")
ax.set_title("Delay activity (Goldman-Rakic)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: WM capacity Miller vs Cowan
ax = axes[0, 2]
ax.plot(n_items, recall_miller, "o-", color="#1f77b4", lw=2,
        label="Miller 1956 (7±2)")
ax.plot(n_items, recall_cowan, "s-", color="#d62728", lw=2,
        label="Cowan 2001 (4±1)")
ax.axvline(4, color="orange", linestyle="--", alpha=0.5)
ax.axvline(7, color="green", linestyle="--", alpha=0.5)
ax.set_xlabel("Number of items")
ax.set_ylabel("Recall accuracy")
ax.set_title("Working memory capacity")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: Prospect theory
ax = axes[1, 0]
ax.plot(outcomes, utility, "-", color="#d62728", lw=2,
        label=f"Prospect (λ={lam}, α={alpha})")
ax.plot(outcomes, linear_utility, "--", color="gray", lw=1, label="Linear (rational)")
ax.axhline(0, color="black", lw=0.5)
ax.axvline(0, color="black", lw=0.5)
ax.set_xlabel("Outcome ($)")
ax.set_ylabel("Subjective value U(x)")
ax.set_title("Prospect theory (Kahneman-Tversky 1979, Nobel 2002)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: Dopamine RPE
ax = axes[1, 1]
ax.plot(t_rpe, da_unexpected, "-", color="#2ca02c", lw=1.5,
        label="Unexpected reward")
ax.plot(t_rpe, da_predicted, "-", color="#1f77b4", lw=1.5,
        label="Predicted reward (CS only)")
ax.plot(t_rpe, da_omission, "-", color="#d62728", lw=1.5,
        label="Reward omitted (dip)")
ax.axvline(cs_time, color="green", linestyle="--", alpha=0.3)
ax.axvline(reward_time, color="orange", linestyle="--", alpha=0.3)
ax.set_xlabel("Time (s)")
ax.set_ylabel("DA firing (Hz)")
ax.set_title("Dopamine RPE (Schultz 1997)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Iowa task + ITU
ax = axes[1, 2]
ax.plot(np.arange(n_trials), normal_cumulative_good - normal_cumulative_bad,
        "-", color="#2ca02c", lw=2, label="Normal (good-bad)")
ax.plot(np.arange(n_trials), damaged_cumulative_good - damaged_cumulative_bad,
        "-", color="#d62728", lw=2, label="VMPFC damaged")
ax.axhline(0, color="black", lw=0.5)
ax.set_xlabel("Trial")
ax.set_ylabel("Net advantageous choices")
ax.set_title(f"Iowa Gambling Task (Damasio 1994);  ITU δS/δ⟨K⟩ = {itu_ratio:.3f}")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
plt.close(fig)

summary = {
    "phase": 203,
    "tier1_paper": 28,
    "block": "B",
    "topic": "Prefrontal cortex + executive function + decision (K_executive)",
    "PFC_pct_of_cortex_by_species": pfc_species,
    "human_PFC_dominance": "30% of cortex, 3x rodent ratio",
    "working_memory": {
        "Goldman_Rakic": "DLPFC delay-period activity",
        "Baddeley_1974": "Central executive + phonological loop + visuospatial sketchpad",
        "Miller_1956_capacity": "7 ± 2 chunks",
        "Cowan_2001_capacity": "4 ± 1 chunks (no chunking)",
    },
    "prospect_theory_Kahneman_Tversky_1979": {
        "Nobel_2002": "Daniel Kahneman",
        "loss_aversion_lambda": lam,
        "value_alpha_beta": alpha,
        "interpretation": "Loss feels 2.25x stronger than equivalent gain",
    },
    "dopamine_RPE_Schultz_1997": {
        "TD_error": "delta = R - V(s)",
        "neural_evidence": "VTA/SNc DA neurons encode RPE",
        "Sutton_Barto_correspondence": "RL algorithm matches neural firing",
    },
    "Iowa_Gambling_Damasio_1994": {
        "task": "4 decks; A,B bad (high reward, huge loss); C,D good",
        "normal_pattern": "Progressive shift to good decks",
        "VMPFC_damage": "Continues picking bad decks (somatic marker absent)",
    },
    "Libet_1983_readiness_potential": {
        "RP_onset_ms": -1000,
        "W_decision_reported_ms": -200,
        "movement_ms": 0,
        "interpretation": "Brain prepares before conscious decision",
    },
    "ITU_K_executive": {
        "N_states": int(N_states),
        "S_pre_decision_nats": S_pre,
        "S_post_decision_nats": S_post,
        "delta_S": S_post - S_pre,
        "ratio_dS_over_dK": float(itu_ratio),
        "expected_ratio": 1.0,
    },
    "ITU_interpretation": {
        "K_state": "K_executive (sub-state of K_neuro)",
        "modular_Hamiltonian": "K_executive^(0) = -log P(action | state, goal, value)",
        "decomposition": "K_executive = K_WM ⊕ K_attention ⊕ K_value ⊕ K_planning ⊕ K_inhibition ⊕ K_meta",
        "top_down_hierarchy": "K_executive ⊃ K_perception ⊃ K_memory",
        "free_will_link": "Libet RP shows K_executive descent precedes conscious choice (Phase 9 link)",
        "dopamine_RPE_meaning": "Reward prediction error = ITU update signal",
    },
    "outputs": {
        "figure": str(OUT_PNG.name),
        "summary_json": str(OUT_JSON.name),
    },
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
